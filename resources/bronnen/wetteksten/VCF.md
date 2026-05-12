---
tags: ["IV.A", "2.5", "2.6"]
itaa-lex-sectie: "IV.A"
wet: "Decreet 13 december 2013 houdende de Vlaamse Codex Fiscaliteit (VCF)"
bron_rol: "itaa_lex"
status: "beschikbaar"
bijgewerkt: "03.04.2026"
bron: "onbekend"
chunk:
  level: 6
  type: "Art."
  sub_strategy:
provenance:
  inputs:
    - id: resources/raw/wetteksten/VCF-2026.pdf
      sha256: e48d80794da796d8b9822a99acf06ce70e7302f277f0973bd7e942acd3a59aa0
      version: 03.04.2026
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: 6655d4b
    model:
    prompt_version:
  generated_at: '2026-05-12T19:52:34Z'
  stale: false
  stale_reason:
  trust:
    status: needs-rework
    confirmed_at: '2026-05-12T20:58:28Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "Kolom-bleed ETL-fix #3 slechts gedeeltelijk effectief: NL+FR text nog op dezelfde regels door heel document. Headings bevatten FR-tekst: '## TITEL 1 - Inleidende bepalingen  TITRE 1 er - Dispositions introductives'. Article headings: '###### Art. 1.1.0.0.1.  Art. 1.1.0.0.1.' (dubbel). Body-paragrafen: 'In deze codex wordt verstaan onder :  Dans le présent code, il y a lieu d'entendre par :'. OCR-artifact: 'Succes|Upsierechten' (regel ~124). 1225 regels met dubbele content."
    layer1:
      status: warn
      run_id: 20260512-210639
      run_at: '2026-05-12T21:06:42Z'
      heading_count: 836
      max_section_chars: 36043
      file_size_chars: 943675
      flags:
        - name: max_section_size
          status: warn
          detail: 'langste sectie op ######-niveau: 36043 chars (>24000); chunker splitst auto op alinea-grenzen via split_long_chunk'
          samples: []
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-12T20:58:28Z'
      rationale: "Kolom-bleed ETL-fix #3 slechts gedeeltelijk effectief: NL+FR text nog op dezelfde regels door heel document. Headings bevatten FR-tekst: '## TITEL 1 - Inleidende bepalingen  TITRE 1 er - Dispositions introductives'. Article headings: '###### Art. 1.1.0.0.1.  Art. 1.1.0.0.1.' (dubbel). Body-paragrafen: 'In deze codex wordt verstaan onder :  Dans le présent code, il y a lieu d'entendre par :'. OCR-artifact: 'Succes|Upsierechten' (regel ~124). 1225 regels met dubbele content."
      concrete_problemen:
        - regel: 50
          categorie: A8
          type: column-bleed
          voorbeeld: '## TITEL 1 - Inleidende bepalingen  TITRE 1 er - Dispositions introductives'
        - regel: 54
          categorie: A8
          type: column-bleed
          voorbeeld: '###### Art. 1.1.0.0.1.  Art. 1.1.0.0.1.'
        - regel: 60
          categorie: A8
          type: column-bleed
          voorbeeld: "In deze codex wordt verstaan onder :  Dans le présent code, il y a lieu d'entendre par :"
        - regel: 124
          categorie: A9
          type: ocr-confusion
          voorbeeld: "Wetboek van Successierechten : ... 'Succes|Upsierechten'"
---

# Vlaamse Codex Fiscaliteit (VCF)

*Bijgewerkt tot en met 03.04.2026 — gecoördineerde versie.*

## TITEL 1 - Inleidende bepalingen  TITRE 1 er - Dispositions introductives

### Hoofdstuk 1 - Algemene bepalingen en definities  Chapitre 1er - Dispositions générales et définitions

###### Art. 1.1.0.0.1.  Art. 1.1.0.0.1.

Deze codex regelt een gewestaangelegenheid.  Le présent Code règle une matière régionale.

###### Art. 1.1.0.0.2.  Art. 1.1.0.0.2.

In deze codex wordt verstaan onder :  Dans le présent code, il y a lieu d'entendre par :

1° belastingen en toebehoren : de belastingen in  hoofdsom waarop deze codex van toepassing is, in  voorkomend geval met inbegrip van de opcentiemen of  de opdeciem, nalatigheidsinteresten, administratieve  geldboetes,  belastingverhogingen  en  kosten  van  vervolging  of  tenuitvoerlegging,  rechtsplegingsvergoedingen,  gerechtskosten  en  betekeningskosten;

1°/1  belasting  op  de  automatische  ontspanningstoestellen: de belasting die geheven wordt  overeenkomstig de bijzondere wet van 16 januari 1989  betreffende de financiering van de gemeenschappen en  de gewesten en conform de bepalingen van titel 2,  hoofdstuk 13, van deze codex;

1°/2 belasting op de spelen en weddenschappen: de  belasting die geheven wordt overeenkomstig de  bijzondere wet van 16 januari 1989 betreffende de  financiering van de gemeenschappen en de gewesten en  conform de bepalingen van titel 2, hoofdstuk 12, van  deze codex;

2° belasting op de inverkeerstelling : de belasting die  geheven wordt overeenkomstig de bijzondere wet van  16 januari 1989 betreffende de financiering van de  gemeenschappen en de gewesten en conform de  bepalingen van titel 2, hoofdstuk 3, van deze codex;

3° belastingplichtige : iedere natuurlijke persoon of  rechtspersoon in wiens hoofde een belasting wordt  geheven;

4° belastingschuldige : iedere natuurlijke persoon of  rechtspersoon die met toepassing van deze codex of het  gemeen recht gehouden is tot de betaling van een  belasting;

5° bevoegd personeelslid : het personeelslid van de  Vlaamse administratie dat wordt aangewezen conform  de besluiten van de Vlaamse Regering, en dat belast is  met de uitvoering van de bepalingen van deze codex;

6° decreet van 19 april 1995 : het decreet van 19 april  1995  houdende  maatregelen  ter  bestrijding  en  voorkoming van leegstand en verwaarlozing van  bedrijfsruimten;

7° (…)  7° (…) ;

7° /1 dienstaanbieder: elke juridische entiteit die door de  tolheffer, vermeld in artikel 4, tweede lid, 2°, van het  decreet Kilometerheffing geaccrediteerd is om in haar  tolgebied, vermeld in artikel 4, § 2, derde lid, 1°, van het  decreet Kilometerheffing, een dienst aan te bieden van  inning van de kilometerheffing bij de gebruikers, en van  afdracht aan de tolheffer, op basis van door  boordapparatuur geregistreerde of verkregen gegevens;

7° /2 dienstverleningsovereenkomst : de overeenkomst  tussen  de  houder  van  een  voertuig  en  een  dienstaanbieder  naar  zijn  keuze  of  de  hoofddienstaanbieder, die voorafgaand aan het gebruik  van enige weg voor dat voertuig moet worden gesloten;

7°/3  boordapparatuur:  alle  hardware-  of  softwarecomponenten die aan boord van een voertuig  zijn geïnstalleerd of worden meegenomen, en die  worden gebruikt als onderdeel van de toldienst, om  gegevens te verzamelen, op te slaan, te verwerken en  vanop afstand te ontvangen of te verzenden;

8° entiteit van de Vlaamse administratie : een intern of  extern verzelfstandigd agentschap of een departement;

9° erfbelasting : verzamelterm voor het successierecht  en het recht van overgang;

10° eurovignet : de belasting die tot en met de  inwerkingtreding van het decreet van 3 juli 2015 tot  invoering van de kilometerheffing en de stopzetting van  de heffing van het eurovignet en tot wijziging van de  Vlaamse Codex Fiscaliteit van 13 december 2013 in dat  verband geheven werd overeenkomstig de bijzondere  wet van 16 januari 1989 betreffende de financiering van  de gemeenschappen en de gewesten en conform de  toenmalige bepalingen van titel 2, hoofdstuk 4, van deze  codex;

10°/1 heffing ongeschikte en onbewoonbare woningen:  de belasting die geheven wordt conform de bepalingen  van titel 2, hoofdstuk 5, van deze codex;

11° /1 kilometerheffing : de belasting die geheven wordt  conform de bepalingen van titel 2, hoofdstuk 4, van deze  codex;

12°  kinderen  :  de  afstammelingen  van  de  belastingplichtige en die van zijn echtgenoot of van de  wettelijk samenwonende, alsook de kinderen die hij  volledig of hoofdzakelijk ten laste heeft;

13° leegstandsheffing bedrijfsruimten : de belasting die  geheven wordt conform de bepalingen van titel 2,  hoofdstuk 6, van deze codex;

14° onroerende voorheffing : de belasting die geheven  wordt overeenkomstig de bijzondere wet van 16 januari  1989  betreffende  de  financiering  van  de  gemeenschappen en de gewesten en conform de  bepalingen van titel 2, hoofdstuk 1, van deze codex;

15° recht op hypotheekvestiging : de belasting die onder  de benaming "registratierecht op de vestiging van een  hypotheek op een in België gelegen onroerend goed"  geheven wordt overeenkomstig de bijzondere wet van  16 januari 1989 betreffende de financiering van de  gemeenschappen en de gewesten en conform de  bepalingen van titel 2, hoofdstuk 11, van deze codex;

16° recht van overgang : de belasting die onder de  benaming `het recht van overgang bij overlijden van  niet-rijksinwoners' wordt geheven overeenkomstig de  bijzondere wet van 16 januari 1989 betreffende de  financiering van de gemeenschappen en de gewesten en  conform de bepalingen van titel 2, hoofdstuk 7, van deze  codex;

17° registratiebelasting : verzamelterm voor de  schenkbelasting, het verkooprecht, het verdeelrecht en  het recht op hypotheekvestiging;

18° rijksinwoner : de natuurlijke persoon die naargelang  het geval op het ogenblik van zijn overlijden of op het  ogenblik van de schenking binnen het Rijk zijn domicilie  of de zetel van zijn vermogen heeft gevestigd of de  rechtspersoon die op het ogenblik van de schenking  binnen het Rijk zijn zetel van werkelijke leiding heeft  gevestigd;

18°/1  schatter-expert:  natuurlijk  persoon  die  beroepsmatig  schattingen  en  waarderingen  van  onroerende goederen uitvoert en daarvoor beschikt over  de beroepskwalificatie, vermeld in artikel 3.3.1.0.9/1, §  2, 2°;

20° successierecht : de belasting die onder de benaming  `het successierecht van rijksinwoners' wordt geheven  overeenkomstig de bijzondere wet van 16 januari 1989  betreffende de financiering van de gemeenschappen en  de gewesten en conform de bepalingen van titel 2,  hoofdstuk 7, van deze codex;

21° vennootschappen : een vennootschap, vereniging,  inrichting of instelling die regelmatig is opgericht,  rechtspersoonlijkheid  bezit  en  een  onderneming  exploiteert of zich bezighoudt met verrichtingen van  winstgevende aard. Lichamen met rechtspersoonlijkheid  die naar Belgisch recht zijn opgericht en die voor de  toepassing van de inkomstenbelastingen worden geacht  geen rechtspersoonlijkheid te bezitten, worden niet als  vennootschappen aangemerkt;

22° verdeelrecht : de belasting die onder de benaming  `registratierecht  op  de  gedeeltelijke  of  gehele  verdelingen van in België gelegen onroerende goederen,  de afstanden onder bezwarende titel, onder mede-  eigenaars, van onverdeelde delen in soortgelijke  goederen, en de omzettingen overeenkomstig artikel  4.61 en 4.62 van het Burgerlijk Wetboek, zelfs indien er  geen onverdeeldheid is' geheven wordt overeenkomstig  de bijzondere wet van 16 januari 1989 betreffende de  financiering van de gemeenschappen en de gewesten en  conform de bepalingen van titel 2, hoofdstuk 10, van  deze codex;

23° verkeersbelasting : de belastingen die geheven  worden overeenkomstig de bijzondere wet van 16  januari 1989 betreffende de financiering van de  gemeenschappen en de gewesten en conform de  bepalingen van titel 2, hoofdstuk 2, van deze codex;

24° verkooprecht : de belasting die onder de benaming  `registratierecht op de overdrachten onder bezwarende  titel van in België gelegen onroerende goederen met  uitsluiting van de overdrachten die het gevolg zijn van  een inbreng in een vennootschap behalve voor zover het  een inbreng betreft door een natuurlijke persoon van een  woning in een Belgische vennootschap' geheven wordt  overeenkomstig de bijzondere wet van 16 januari 1989  betreffende de financiering van de gemeenschappen en  de gewesten en conform de bepalingen van titel 2,  hoofdstuk 9, van deze codex;

25° (…);  25° (…)

27°  Wetboek  van  Registratie-,  Hypotheek-  en  Griffierechten : het wetboek van 30 november 1939 der  registratie-, hypotheek- en griffierechten;

28° Wetboek van Successierechten : het wetboek van 31  maart 1936 der Succes|Upsierechten.

In titel 2, hoofdstuk 1, wordt verstaan onder :  Dans le titre 2, chapitre 1 er , on entend par :

1° persoon met een handicap : de als gehandicapt  aangemerkte personen, vermeld in artikel 135, eerste lid, 1°,  van het federale WIB 92;

2° gehandicapt kind : een kind met een specifieke  ondersteuningsbehoefte als vermeld in artikel 3, § 1, 39°,  van het decreet van 27 april 2018 tot regeling van de  toelagen in het kader van het gezinsbeleid of een kind dat  door de gezinsbijslagregelgeving van andere gefedereerde  deelentiteiten beschouwd wordt als een kind met een  handicap, een kind met een beperking of een kind dat op  basis van de zelfredzaamheidsgraad of de ernst van de  gevolgen van de aandoening recht heeft op een toeslag van  de basiskinderbijslag of een kind dat voldoet aan de  voorwaarden, vermeld in artikel 47, artikel 56septies of  artikel 63 van de Algemene Kinderbijslagwet, en de  koninklijke besluiten, genomen ter uitvoering van die  bepalingen;

3° grensarbeider : de persoon die in de grensstreek van een  buurland werkt en die volgens het bevolkingsregister op 1  januari van het aanslagjaar zijn woonplaats heeft in de  grensstreek van België, waarnaar hij gewoonlijk dagelijks  of ten minste eenmaal per week terugkeert.

In titel 2, hoofdstuk 2, wordt verstaan onder :  Dans le titre 2, chapitre 2, on entend par :

1° stoom- of motorvoertuigen : de motorvoertuigen,  omschreven in de reglementering voor de inschrijving van  motorvoertuigen en de aanhangwagens, de stoom- of  motorvaartuigen en -boten en, in het algemeen, alle stoom-  of motorvervoermiddelen tot voortbeweging, alsook de  aanhangwagens en opleggers ervan;

2° lichte vrachtauto : in afwijking van punt 1°, elke auto,  opgevat en gebouwd voor het vervoer van zaken waarvan  het maximaal toegestane totaalgewicht niet meer bedraagt  dan 3500 kg en die :

a) bestaat uit een volledig van de laadruimte afgesloten  enkele cabine die ten hoogste twee plaatsen bevat, die van  de bestuurder niet inbegrepen, en een open laadbak. Als de  auto is ingeschreven in het repertorium van het Directoraat- generaal Mobiliteit en Verkeersveiligheid na 31 december  2022, is de auto ingeschreven ofwel op naam van een

b) bestaat uit een volledig van de laadruimte afgesloten  dubbele cabine die ten hoogste zes plaatsen bevat, die van  de bestuurder niet inbegrepen, en een open laadbak. Als de  auto is ingeschreven in het repertorium van het Directoraat- generaal Mobiliteit en Verkeersveiligheid na 31 december  2022, is de auto ingeschreven ofwel op naam van een  rechtspersoon ofwel op naam van een natuurlijke persoon  als vermeld in artikel I.1, eerste lid, 1°, (a), van het Wet-  boek van economisch recht en ingeschreven in de  Kruispuntbank van Ondernemingen conform artikel III.17  van het voormelde wetboek. De voormelde voorwaarde dat  het voertuig moet ingeschreven zijn ofwel op naam van een  rechtspersoon ofwel op naam van een natuurlijke persoon  met een ondernemingsnummer, is alleen van toepassing op  auto's van natuurlijke personen en andere rechtspersonen  dan vennootschappen, autonome overheidsbedrijven en  verenigingen  zonder  winstgevend  doel,  met  leasingactiviteiten;

b) comprend une cabine double comportant six places  au maximum, celle du conducteur non comprise,  complètement séparée de l'espace de chargement, et un  plateau de chargement ouvert. Si le véhicule est inscrit  au répertoire de la Direction générale Mobilité et  Sécurité routière après le 31 décembre 2022, le véhicule  est immatriculé soit au nom d'une personne morale, soit  au nom d'une personne physique telle que visée à  l'article I.1, alinéa 1er, 1°, (a), du Code de droit  économique et inscrit à la Banque-Carrefour des  Entreprises conformément à l'article III.17 du Code  précité. La condition précitée selon laquelle le véhicule  doit être immatriculé soit au nom d'une personne  morale, soit au nom d'une personne physique avec un  numéro d'entreprise, ne s'applique qu'aux véhicules de  personnes physiques et de personnes morales autres que  les sociétés, les entreprises publiques autonomes et les  associations sans but lucratif, exerçant des activités de  leasing ;

c) gelijktijdig bestaat uit een passagiersruimte die ten  hoogste twee plaatsen bevat, die van de bestuurder niet  inbegrepen, en een daarvan afgesloten laadruimte waarvan  de afstand tussen elk punt van de  scheidingswand achter de zitplaatsen en de binnenkant

c) comprend simultanément un espace réservé aux  passagers comportant deux places au maximum, celle  du conducteur non comprise, et un espace de  chargement séparé dont la distance entre chaque point  de la cloison de séparation derrière la rangée de sièges  van de achterzijde van de laadruimte, gemeten in de  langsrichting van het voertuig, op een hoogte van 20 cm  boven de vloer, altijd minstens 50 % bedraagt van de lengte  van de wielbasis. De laadruimte moet bovendien over haar  hele oppervlakte bestaan uit een vaste of duurzaam  bevestigde,  horizontale  laadvloer  zonder  verankeringsplaatsen voor extra banken, zetels of  veiligheidsgordels, die deel uitmaakt van het koetswerk;

et le bord arrière intérieur de l'espace de chargement,  mesurée dans l'axe longitudinal du véhicule, à une  hauteur de 20 cm au-dessus du plancher, atteint toujours  au moins 50 % de la longueur de l'empattement. En  outre, l'espace de chargement doit être pourvu sur toute  sa surface d'un plancher horizontal fixe ou y fixé de  manière durable, sans points d'attache pour des  banquettes, des sièges ou des ceintures de sécurité  complémentaires, faisant partie intégrante de la  carrosserie ;

Als het voertuig, aangewezen als lichte vrachtauto in de  reglementering, vermeld in punt 1°, niet beantwoordt aan  een van de voertuigtypes, vermeld in punt a) tot en met d),  wordt het, afhankelijk van zijn constructie, beschouwd als  een personenauto, een auto voor dubbel gebruik of een  minibus;

3° beroepsmatig gebruik : het gebruik van een voertuig  voor de rechtstreekse uitoefening van werkzaamheden  tegen betaling of met winstoogmerk;

4° persoonlijk gebruik : elk ander gebruik dan beroepsmatig  gebruik;

5° gewone verblijfplaats : de plaats waar iemand  gewoonlijk verblijft, dat wil zeggen gedurende ten minste  185 dagen per kalenderjaar wegens persoonlijke en  beroepsmatige bindingen of, voor personen zonder  beroepsmatige bindingen, wegens persoonlijke bindingen  waaruit nauwe banden blijken tussen hemzelf en de plaats  waar hij woont.

De  gewone  verblijfplaats  van  iemand  die  zijn  beroepsmatige bindingen op een andere plaats heeft dan  zijn persoonlijke bindingen en daardoor afwisselend  verblijft op verschillende plaatsen in twee of meer staten,  wordt evenwel geacht zich op dezelfde plaats te bevinden  als zijn persoonlijke bindingen, op voorwaarde dat hij op  geregelde tijden terugkeert naar die plaats. Die laatste  voorwaarde vervalt als de betrokkene in een staat  verblijft voor een opdracht van een bepaalde duur. Het

La résidence habituelle d'une personne dont les attaches  professionnelles sont situées dans un lieu différent de  celui de ses attaches personnelles et qui, de ce fait, est  amenée à résider alternativement dans des lieux  différents situés dans deux Etats ou plus, est cependant  censée se situer au lieu de ses attaches personnelles, à  condition qu'elle y retourne régulièrement. Cette  dernière condition échoit lorsque la personne réside  dans un Etat pour une mission d'une durée déterminée.  feit dat college wordt gelopen of een school wordt bezocht,  houdt niet in dat de gewone verblijfplaats wordt verplaatst;

6° euronorm: de maximumdrempel voor de concentratie  van bepaalde vervuilende stoffen in de uitlaatgassen van  motorvoertuigen, bepaald in opeenvolgende Europese  richtlijnen en verordeningen;

8° vennootschap: in afwijking van het eerste lid, 21°, een  vennootschap  als  vermeld  in  het  Wetboek  van  vennootschappen en verenigingen.

In titel 2, hoofdstuk 3, wordt verstaan onder :  Dans le titre 2, chapitre 3, on entend par :

1° wegvoertuigen : de personenauto's, auto's voor dubbel  gebruik, minibussen en motorfietsen, zoals die voertuigen  zijn omschreven in de reglementering van de inschrijving  van de motorvoertuigen en de aanhangwagens en zoals ze  worden verstaan in de zin van de laatste zin van punt 2° van  het vorige lid, voor zover die voertuigen voorzien zijn van  of voorzien moeten zijn van een andere nummerplaat dan  een in het kader van de bedoelde regeling uitgereikte  proefrittenplaat, handelaarsplaat of tijdelijke plaat die geen  internationale kentekenplaat is;

2° luchtvaartuigen : de vliegtuigen, watervliegtuigen,  helikopters, zweefvliegtuigen, luchtballons of bestuurbare  luchtschepen en andere luchtvaartuigen, zwaarder of lichter  dan lucht, met of zonder motor, als ze ingeschreven zijn of  moeten zijn;

3° boten : de jachten en pleziervaartuigen die langer zijn dan  7,5 meter, als daarvoor een registratiebrief afgeleverd is of  afgeleverd moet zijn;

4° euronorm: de maximumdrempel voor de concentratie  van bepaalde vervuilende stoffen in de uitlaatgassen van  motorvoertuigen, bepaald in opeenvolgende Europese  richtlijnen en verordeningen.

5° vennootschap: in afwijking van het eerste lid, 21°, een  vennootschap als vermeld in het Wetboek van  vennootschappen en verenigingen.

In titel 2, hoofdstuk 4, wordt verstaan onder :  Au titre 2, chapitre 4, on entend par :

1° Euro-emissieklasse: de klasse gedefinieerd op basis van  emissiegrenswaarden, zoals omschreven in bijlage 0 van  richtlijn 1999/62/EG van het Europees Parlement en de  Raad van 17 juni 1999 betreffende het in rekening brengen  van het gebruik van wegeninfrastructuur aan voertuigen,  met toevoeging van de klasse "minder vervuilend dan Euro  VI, met inbegrip van emissievrije voertuigen";

1° /1 gebruiker: de houder van het voertuig die een  dienstverleningsovereenkomst  heeft  met  een  dienstaanbieder of de hoofddienstaanbieder;

2° gegarandeerde betaalmiddel : het betaalmiddel waarmee  de dienstaanbieder, vermeld in artikel 1.1.0.0.2, eerste lid,  7° /1, of de hoofddienstaanbieder, vermeld in artikel 5,  tweede lid, van het decreet Kilometerheffing de  kilometerheffing en, in voorkomend geval, de aan de  gebruiker gefactureerde inningskosten op het eerste  verzoek kunnen innen, zonder verdere toelating van de  gebruiker en zonder dat die de betaling die met het  betaalmiddel is verricht, kunnen annuleren;

3° kilometer : elke kilometer, afgerond op het hogere of  lagere  duizendste,  naargelang  het  cijfer  van  de  tienduizendsten al of niet vijf bereikt;

4° niet-geconcedeerde weg : de weg of het gedeelte van de  weg waarvan het beheer niet in concessie is gegeven;

4° /1° vervoer over de weg van goederen: het vervoer van  elk goed dat op een voertuig kan worden geladen of  afgeladen, met inbegrip van het vervoer van werktuigen en  gereedschapsmachines en van werktuigvoertuigen, alsook  het vervoer van elk goed door die werktuigen,  gereedschapsmachines en werktuigvoertuigen, als ze  worden gebruikt op een niet-geconcedeerde weg;

5°  Viapass  :  het  publiekrechtelijk  vormgegeven  interregionaal samenwerkingsverband in de vorm van een  gemeenschappelijke instelling als vermeld in artikel 92bis,  § 1, van de bijzondere wet van 8 augustus 1980 tot  hervorming der instellingen, vermeld in artikel 18 van het  samenwerkingsakkoord van 31 januari 2014 tussen het  Vlaamse Gewest, het Waalse Gewest en het Brussels  Hoofdstedelijk Gewest betreffende de invoering van de  kilometerheffing op het grondgebied van de drie gewesten  en tot oprichting van een publiekrechtelijk vormgegeven  Interregionaal Samenwerkingsverband Viapass onder de  vorm van een gemeenschappelijke instelling zoals bedoeld  in artikel 92bis, § 1, van de bijzondere wet van 8 augustus  1980 tot hervorming der instellingen;

7° weg : de landwegen en de aanhorigheden ervan.  7° route : les routes et leurs dépendances.

In titel 2, hoofdstuk 7 en hoofdstuk 8, wordt verstaan onder  :

1° beurswaarde : de slotkoers van een financieel instrument,  zoals die als koersinformatie beschikbaar is  in de gespecialiseerde pers of in gespecialiseerde  elektronisch raadpleegbare bronnen;

1° valeur boursière : le cours de clôture d'un instrument  financier, suivant les informations des cours disponibles  dans la presse écrite spécialisée ou les sources  numériques consultables spécialisées ;  1°/1 bouwgrond: een perceel grond dat stedenbouwkundig  bestemd is tot woningbouw of een onroerend goed dat  ermee wordt gelijkgesteld. Het geheel of het gedeelte van  een gebouw dat, pas na de uitvoering van andere werken  dan normale herstellings- of onderhoudswerken, kan  dienen tot huisvesting van een gezin of een persoon, met in  voorkomend geval de aanhorigheden die tegelijk met het  gebouw worden verkregen, wordt met een bouwgrond  gelijkgesteld;

2° gehandicapt kind : een kind met een specifieke  ondersteuningsbehoefte als vermeld in artikel 3, § 1, 39°,  van het decreet van 27 april 2018 tot regeling van de  toelagen in het kader van het gezinsbeleid of een kind dat  door de gezinsbijslagregelgeving van andere gefedereerde  deelentiteiten beschouwd wordt als een kind met een  handicap, een kind met een beperking of een kind dat op  basis van de zelfredzaamheidsgraad of de ernst van de  gevolgen van de aandoening recht heeft op een toeslag van  de basiskinderbijslag of een kind dat voldoet aan de  voorwaarden, vermeld in artikel 47, artikel 56septies of  artikel 63 van de Algemene Kinderbijslagwet, en de  koninklijke besluiten, genomen ter uitvoering van die  bepalingen;

3° persoon met een handicap : de als gehandicapt  aangemerkte personen, vermeld in artikel 135, eerste lid,  1°, van het federale WIB 92;

4° partner :  4° partenaire :

a) de persoon die op dag van het openvallen van de  nalatenschap met de erflater of op de dag van de schenking  met de schenker gehuwd is;

b) de persoon die op de dag van het openvallen van de  nalatenschap met de erflater of op de dag van de schenking  met de schenker wettelijk samenwoont, overeenkomstig de  bepalingen van boek III, titel Vbis, van het Burgerlijk  Wetboek;

5° verkrijging in rechte lijn :  5° acquisition en ligne directe :

a) een verkrijging tussen personen die de ene van de  andere afstammen, overeenkomstig artikel 4.11, § 1, van  het Burgerlijk Wetboek, of tussen personen die  ingevolge volle adoptie overeenkomstig artikel 356-1 van  het Burgerlijk Wetboek een statuut met dezelfde rechten  en verplichtingen hebben;

b) een verkrijging tussen een persoon en het kind van zijn  partner, ongeacht of de verkrijging plaatsvindt voor of na  het overlijden van de partner. Als de verkrijging plaatsvindt  na het overlijden van de partner, moet die laatste zijn  hoedanigheid van partner ten aanzien van de eerst vermelde  persoon nog hebben op de datum van zijn overlijden;

c) een verkrijging tussen personen tussen wie een relatie  van zorgouder en zorgkind bestaat of heeft bestaan. Er is  sprake van een zorgrelatie als iemand vóór de leeftijd van  eenentwintig jaar gedurende drie achtereenvolgende jaren  bij een andere persoon heeft ingewoond en gedurende die  tijd hoofdzakelijk van die andere persoon, of van de andere  persoon en zijn partner samen, de hulp en verzorging heeft  gekregen die kinderen normaal van hun ouders krijgen. De  inschrijving van het zorgkind in het bevolkings- of het  vreemdelingenregister op het adres van de zorgouder geldt  als weerlegbaar vermoeden van inwoning bij de zorgouder;

d) een verkrijging door een persoon die met de overledene  of de schenker een verwantschapsband had of heeft die  voortkomt uit gewone adoptie, maar uitsluitend als  daarvoor de nodige bewijsstukken worden aangebracht en  als :

2) het adoptiekind op het ogenblik van de adoptie onder de  voogdij was van de openbare onderstand of van een  Openbaar Centrum voor Maatschappelijk Welzijn of van  een  vergelijkbare  instelling  binnen  de  Europese  Economische Ruimte, of wees was van een voor het  vaderland gestorven vader of moeder;

3) het adoptiekind, vóór de leeftijd van eenentwintig jaar,  gedurende drie achtereenvolgende jaren hoofdzakelijk van  de adoptant, of van de adoptant en zijn partner samen, de  hulp en verzorging heeft gekregen die kinderen normaal  van hun ouders krijgen;

4) het kind geadopteerd is door een persoon van wie al de  afstammelingen voor het vaderland gestorven zijn;

e)  een  verkrijging  tussen  ex-partners  als  er  gemeenschappelijke afstammelingen zijn.

De definitie van kinderen, vermeld in het eerste lid, 12°, en  de definitie van vennootschappen, vermeld in het eerste lid,  21°, gelden niet voor de toepassing van  hoofdstuk 7 en hoofdstuk 8 van titel 2.

La définition d'enfants figurant au premier alinéa, 12°,  et la définition de sociétés, figurant au premier alinéa,  21°, ne sont pas valables pour l'application du chapitre  7 et du chapitre 8 du titre 2.  In titel 2, hoofdstuk 7,wordt verstaan onder :  Dans le titre 2, chapitre 7, on entend par :

1° aanvullende rechten : de erfbelasting, geheven omdat de  voorwaarden voor een verlaagd tarief, een vermindering of  een vrijstelling niet vervuld zijn, of wegens de toepassing  van artikel 3.3.1.0.6, artikel 3.17.0.0.2, of van artikel  2.7.7.0.1 in geval van een onjuiste of onvolledige aangifte  of een aangifte die niet binnen de termijn is ingediend;

2° gezinswoning : de gezamenlijke hoofdverblijfplaats van  de erflater en zijn langst|Uplevende partner. Een uittreksel  uit  het  bevolkingsregister  houdt  een  weerlegbaar  vermoeden in van de samenwoning. Als aan de  samenwoning een einde is gekomen door een feitelijke  scheiding van de partners, door een geval van overmacht  dat tot op het ogenblik van het overlijden heeft  voortgeduurd,  of  door  de  verplaatsing  van  de  hoofdverblijfplaats van een van de partners of van beide  partners naar een rust- en verzorgingsinstelling of een  assistentiewoning,  wordt  de  laatste  gezamenlijke  hoofdverblijfplaats van de erflater en zijn langstlevende  partner als gezinswoning aangemerkt. De aanhorigheden,  vermeld in het twaalfde lid, 2°, worden in voorkomend  geval geacht deel uit te maken van de gezinswoning.

In titel 2, hoofdstuk 8 tot en met 11, wordt verstaan onder  :

2° aanvullende rechten : de registratiebelasting, berekend  en geheven ter aanvulling van de registratiebelasting die is  berekend en geheven op zicht van de ter registratie  aangeboden akte of het ter registratie aangeboden geschrift  of wegens de toepassing van artikel 3.17.0.0.2.

In titel 2, hoofdstuk 8 tot en met 11, worden lichamelijke  roerende voorwerpen, aangewend tot de dienst en de  exploitatie van onroerende goederen, niet beschouwd als  onroerende goederen.

In titel 2, hoofdstuk 8, wordt de schenkbelasting, vermeld  in het eerste lid, 19°, ook voor de volgende schenkingen  geacht gelokaliseerd te zijn in het Vlaamse Gewest :

1° de schenking van roerende of onroerende goederen  gedaan door een rijks|Upinwoner-rechtspersoon als de  schenker-rijksinwoner op het ogenblik van de schenking  zijn zetel van werkelijke leiding in het Vlaamse Gewest had  gevestigd of, als de zetel van werkelijke leiding van de  schenker-rijksinwoner in de periode van vijf jaar voor  de schenking in meer dan één gewest gevestigd was, als de schenker-rijksinwoner in de periode van vijf jaar voor de  schenking zijn zetel van werkelijke leiding het langst in het  Vlaamse Gewest had gevestigd;

2° de schenking door een niet-rijksinwoner- rechtspersoon  van een in het in het Vlaamse Gewest gelegen onroerend  goed;

3° de schenking van roerende goederen door een niet-  rijksinwoner natuurlijke persoon of een rechtspersoon aan  een rijksinwoner als de begiftigde-rijksinwoner op het  ogenblik van de schenking zijn fiscale woonplaats of zetel  van werkelijke leiding in het Vlaamse Gewest had  gevestigd of, als de fiscale woonplaats of zetel van  werkelijke leiding van de begiftigde-rijksinwoner in de  periode van vijf jaar voor de schenking in meer dan één  gewest gevestigd was, als de begiftigde-rijksinwoner in de  periode van vijf jaar voor de schenking zijn fiscale  woonplaats of zetel van werkelijke leiding het langst in het  Vlaamse Gewest had gevestigd;

4° de schenking van roerende goederen door een niet-  rijksinwoner natuurlijke persoon of een rechtspersoon aan  een  niet-rijksinwoner  natuurlijke  persoon  of  een  rechtspersoon als de schenking ter registratie wordt  aangeboden in het Vlaamse Gewest.

In titel 2, hoofdstuk 9, wordt in afwijking van het eerste  lid verstaan onder :

° aanhorigheid : elk gebouwd of ongebouwd onroerend  goed dat volgens de aard, de ligging, de oppervlakte en de  waarde ervan een normale bijhorigheid vormt, al  naargelang het geval, hetzij van het huis of de verdieping of  het gedeelte van verdieping, hetzij van een op te richten  woning;

3° (…);  3° (…) ;

4° (…);  4° (…) ;

5° onbebouwd landgoed: het onroerend goed dat bestaat uit  een of meer gronden die voor het landbouwbedrijf gebruikt  worden of bestemd zijn, met uitsluiting van gebouwen en  de grond waarop deze gebouwen zich bevinden;

5° immeuble rural non bâti : le bien immobilier qui se  compose d'un ou de plusieurs terrains qui sont utilisés  pour ou destinés à l'exploitation agricole, à l'exclusion  des bâtiments et du terrain sur lequel ces bâtiments se  trouvent ;  6° woning : het huis of het geheel of het gedeelte van een  verdieping van een gebouw dat hetzij dadelijk, hetzij na  normale herstellings- of onderhoudswerken hoofdzakelijk  dient of zal dienen tot huisvesting van één gezin of een  persoon, met in voorkomend geval de aanhorigheden die  tegelijk met het huis, het geheel of het gedeelte van een  verdieping worden verkregen;

7° bouwgrond : een perceel grond dat stedenbouwkundig  bestemd is tot woningbouw of een onroerend goed dat  ermee wordt gelijkgesteld. Het geheel of het gedeelte van  een gebouw dat, pas na de uitvoering van andere werken  dan normale herstellings- of onderhoudswerken, kan  dienen tot huisvesting van een gezin of een persoon, met in  voorkomend geval de aanhorigheden die tegelijk met het  gebouw worden verkregen, wordt met een bouwgrond  gelijkgesteld.

8° kernsteden: de gemeenten Aalst, Antwerpen, Boom,  Brugge, Dendermonde, Genk, Gent, Hasselt, Kortrijk,  Leuven, Mechelen, Oostende, Roeselare, Sint-Niklaas,  Turnhout en Vilvoorde;

9° gemeenten van de Vlaamse Rand rond Brussel: de  gemeenten Affligem, Asse, Beersel, Bertem, Bever,  Dilbeek, Drogenbos, Galmaarden, Gooik, Grimbergen,  Halle, Herne, Hoeilaart, Huldenberg, Kampenhout,  Kapelle-op-den-Bos, Kortenberg, Kraainem, Lennik,  Liedekerke, Linkebeek, Londerzeel, Machelen, Meise,  Merchtem, Opwijk, Overijse, Pepingen, Roosdaal, Sint-  Genesius-Rode,  Sint-Pieters-Leeuw,  Steenokkerzeel,  Ternat, Tervuren Vilvoorde, Wemmel, Wezembeek-  Oppem, Zaventem en Zemst.

In titel 2, hoofdstuk 12, wordt verstaan onder mediaspelen:  spelen en weddenschappen die worden geëxploiteerd via  elke radio- of televisiezender, en elk dagblad of tijdschrift  waarvan de zetel van activiteit van de exploitant of uitgever  gevestigd is in het Vlaamse Gewest.

In titel 2, hoofdstuk 13, en in titel 3, wordt, overeenkomstig  artikel 76 van het federale Wetboek van 23 november 1965  van  de  met  Inkomstenbelastingen  Gelijkgestelde  Belastingen,  verstaan  onder  automatisch  ontspanningstoestel: een toestel dat dient tot ontspanning  en een mechanisch, elektrisch of elektronisch onderdeel  bevat om het op gang te brengen, te laten werken of te  bedienen, en dat gestart wordt door de inbreng van een  geldstuk, van een penning of van een ander middel dat  daarvoor in de plaats komt

---- historiek ----  ---- historique ----

- gewijzigd door art. 3 van het decreet van 03.04.2026  (M.B. 23.04.2026). Inwerkingtreding: 03.05.2026

- eerste lid 7°/1 vervangen, 7°/2 gewijzigd, 7°/3 vervangen,  vijfde lid 1° vervangen, 1°/1 toegevoegd, 2° gewijzigd, 4°/1  ingevoegd door art. 11 van het decreet van 03.05.2024  (B.S., 22.05.2024). Inwerkingtreding: 01.07.2025

- gewijzigd door art. 2 van het decreet van 15.03.2024 (B.S.  20.03.2024). Inwerkingtreding: 30.03.2024

- gewijzigd door art. 19 van het decreet van 22.12.2023  (B.S. 29.12.2023). Inwerkingtreding: 01.01.2024

- gewijzigd door art. 13 van het decreet van  16.12.2022 (B.S. 29.12.2022). Inwerkingtreding:  01.01.2023

- gewijzigd door art. 2 van het decreet van 09.12.2022 (B.S.  20.12.2022). Inwerkingtreding: 30.12.2022

- gewijzigd door art. 3 van het decreet van 02.04.2021 (B.S.  15.04.2021). Inwerkingtreding: 25.04.2021, artikel 3, 1°  heeft uitwerking met ingang van 01.01.2019

- gewijzigd door art. 58 van het decreet van 26.06.2020  (B.S. 17.07.2020). Tekst treedt in werking op 01.10.2020

- gewijzigd door art. 25 van het decreet van 29.03.2019  (B.S. 29.04.2019). Tekst treedt in werking op 01.01.2021

- gewijzigd door art. 2 van het decreet van 07.12.2018 (B.S.  20.12.2018). Tekst treedt in werking op 01.01.2019

- 8° vervangen door art. IV.240 van het decreet van  07.12.2018 (B.S. 19.12.2018). Tekst treedt in werking op  01.01.2019

- gewijzigd door art. 2 van het decreet van 18.05.2018  (B.S.: 28.05.2018). Tekst is van toepassing op  verkoopovereenkomsten afgesloten vanaf 1 juni 2018

- eerste lid, 18/1° toegevoegd door art. 8, 1° van het decreet  van 08.12.2017 (B.S., 14.12.2017). De tekst is in werking  getreden op 24.12.2017 en treed buiten werking op een door  de Vlaamse Regering vast te stellen datum

- derde lid, 2° gewijzigd en zesde lid, 1°/1 toegevoegd door  art. 8, 2° en 3° van het decreet van 08.12.2017 (B.S.,  14.12.2017). De tekst is in werking getreden op 24.12.2017

- gewijzigd door art. 2 van het decreet van 16 juni 2017  (B.S. : 04.07.2017). Tekst in werking getreden op de  belastbare tijdperken die starten vanaf 1 juli 2017

- gewijzigd door art. 19 van het decreet van 23 december  2016 (B.S. : 29.12.2016 Ed. 2). Tekst in werking getreden  vanaf aanslagjaar 2017

- eerste lid, punt 5° toegevoegd door art. 11 van het decreet  van 3 juli 2015 (B.S., 10.08.2015). De tekst treedt in  werking op 1 april 2016 (besluit van de Vlaamse Regering  van 17 juli 2015 - B.S., 10.08.2015 - art. 4)

- derde lid, punt 6° en punt 7° werd toegevoegd door art.  105 van het decreet van 18 dec. 2015 (B.S., 29.12.2015). De  tekst treedt in werking vanaf 1 januari 2016 (art. 135)

- vierde lid, punt 4° werd toegevoegd door art. 116 van het  decreet van 18 dec. 2015 (B.S., 29.12.2015). De tekst treedt  in werking vanaf 1 januari 2016 (art. 135)

- gewijzigd door art. 2 van het decreet van 17.07.2015 (B.S.  14.08.2015 erratum B.S. 12.09.2017).

Inwerkingtreding op 14.08.2015 (art. 41)

- vervangen door art. 2 van het decreet van 19.12.2014  (B.S. 29.01.2015 Ed.2 erratum B.S. 12.09.2017).  Inwerkingtreding op 01.01.2015 (art. 325)

De begrippen, gehanteerd in titel 2, hoofdstuk 5, van deze  codex, worden geïnterpreteerd in overeenstemming met de  bepalingen van artikel 1.3 en boek 3, deel 5, titel 2, van de  Vlaamse Codex Wonen van 2021.

De begrippen, gehanteerd in titel 2, hoofdstuk 6, van deze  codex, worden geïnterpreteerd in overeenstemming met de  bepalingen van het decreet van 19 april 1995.

---- historiek ----  ---- historique ----

- gewijzigd door art. 33 van het besluit van 17.07.2020 (B.S.  17.11.2020). Tekst treedt in werking op 01.01.2021.  Bekrachtigd door art. 224, 2° van het decreet van  09.07.2021 (B.S., 10.09.2021). Inwerkingtreding:  20.09.2021.

- gewijzigd door art. 26 van het decreet van 29.03.2019  (B.S. 29.04.2019). Tekst treedt in werking op 01.01.2021

###### Art. 1.1.0.0.4.  Art. 1.1.0.0.4.

De Vlaamse Regering kan eenieder die onderhevig is aan  de bepalingen van deze codex de verplichting opleggen om  documenten en formulieren te gebruiken waarvan ze de  inhoud en het gebruik bepaalt.

## TITEL 2 - Belastingheffing  TITRE 2 - Perception des impôts

### Hoofdstuk 1 - Onroerende voorheffing  Chapitre 1 er - Précompte immobilier

#### Afdeling 1 - Belastbaar voorwerp  Section 1 re - Objet imposable

###### Art. 2.1.1.0.1.  Art. 2.1.1.0.1.

Overeenkomstig artikel 249 van het federale WIB 92 wordt  de belasting geheven op inkomsten uit onroerende  goederen, gelegen in het Vlaamse Gewest.

#### Afdeling 2 - Belastingplichtigen  Section 2 - Contribuables

###### Art. 2.1.2.0.1.  Art. 2.1.2.0.1.

De belastingplichtige is degene die op 1 januari van het  aanslagjaar de eigenaar, bezitter, erfpachter, opstalhouder  of vruchtgebruiker is van de belastbare goederen.

#### Afdeling 3. - Belastbare grondslag  Section 3 - Base imposable

###### Art. 2.1.3.0.1.  Art. 2.1.3.0.1.  De onroerende voorheffing wordt vastgesteld op basis van  het kadastraal inkomen van de belastbare goederen dat op  1 januari van het aanslagjaar bekend is.

Voor de vaststelling van de belastbare grondslag wordt  geen  rekening  gehouden  met  de  vermindering  overeenkomstig artikel 15 van het federale WIB 92.

#### Afdeling 4 - Tarieven  Section 4 - Tarifs

###### Art. 2.1.4.0.1.  Art. 2.1.4.0.1.

§ 1. Het tarief van de onroerende voorheffing bedraagt 3,97  %.

§ 2. In afwijking van paragraaf 1 bedraagt het tarief 2,54  %voor :

1° de eigendommen die als sociale woningen worden  verhuurd en toebehoren aan Openbare Centra voor  Maatschappelijk Welzijn of aan door haar opgerichte  verenigingen waarvan slechts één of meer Openbare Centra  voor Maatschappelijk Welzijn deel uitmaken;

2° de eigendommen die als sociale woningen worden  verhuurd en toebehoren aan gemeenten;

3° de eigendommen die als sociale woningen worden  verhuurd en toebehoren aan de Vlaamse Maatschappij voor  Sociaal Wonen of aan de erkende woonmaatschappijen,  vermeld in artikel 4.36 van de Vlaamse Codex Wonen van  2021;

4° de eigendommen die als sociale woningen worden  verhuurd en toebehoren aan het Vlaams Woningfonds;

5° (…)  5° (…)

6° (...);  6° (...) ;

7° de eigendommen die toebehoren aan rechtspersonen,  erkend overeenkomstig artikel 7, tweede lid, van het  decreet van 7 mei 2004 tot oprichting van het intern  verzelfstandigd agentschap met rechtspersoonlijkheid  Vlaams Agentschap voor Personen met een Handicap en die  gebruikt worden voor wooninfrastructuur voor personen  met een handicap, vermeld in artikel 2, 2°, van hetzelfde  decreet, die een duidelijk vastgestelde behoefte aan zorg en  ondersteuning hebben. De Vlaamse  Regering bepaalt de wijze waarop de behoefte aan zorg en  ondersteuning wordt vastgesteld.

Het verlaagde tarief, vermeld in het eerste lid, 7°, wordt  toegekend vanaf het aanslagjaar waarin uiterlijk op 31  maart aan de bevoegde entiteit van de Vlaamse  administratie gemeld wordt dat een rechtspersoon erkend is  overeenkomstig artikel 7, tweede lid, van het decreet van 7  mei 2004 tot oprichting van het intern verzelfstandigd  agentschap met rechtspersoonlijkheid Vlaams Agentschap  voor Personen met een Handicap. De toekenning geldt tot  het einde van de erkenning. Elke beëindiging van een  erkenning moet uiterlijk op 31 maart van het jaar dat volgt  op de beëindiging aan de bevoegde entiteit van de Vlaamse  administratie gemeld worden.

§ 2/1. In afwijking van paragraaf 1 bedraagt het tarief 2,4  % voor de eigendommen die door een erkende  woonmaatschappij  worden  gehuurd  conform  de  voorwaarden ter uitvoering van artikel 4.147 van het  Besluit Vlaamse Codex Wonen van 2021 en waarvan de  oorspronkelijke  hoofd-huurovereenkomst  met  de  woonmaatschappij een aanvangsdatum heeft vóór 1 januari  2026

Het verlaagde tarief, vermeld in het eerste lid, wordt  toegekend vanaf het aanslagjaar waarin uiterlijk op 31  maart aan de bevoegde entiteit van de Vlaamse  administratie gemeld wordt dat de eigendom op 1 januari  van het aanslagjaar gehuurd wordt door een erkende  woonmaatschappij. De toekenning geldt tot het einde van  de huurovereenkomst. Elke vroegtijdige beëindiging van  de huurovereenkomst wordt uiterlijk op 31 maart van het  jaar dat volgt op de beëindiging aan de bevoegde entiteit  van de Vlaamse administratie gemeld.

§ 3. In afwijking van paragraaf 1 bedraagt het tarief voor  materieel en outillage als vermeld in artikel 471, § 3, van het  federale WIB 92, 3,97% vermenigvuldigd met de  coëfficiënt, vermeld in het tweede lid. De toepassing van de  coëfficiënt mag geen aanleiding geven tot een hoger tarief  dan het tarief dat van toepassing is in het vorige  aanslagjaar, met uitzondering van het aanslagjaar waarin dit  decreet in werking treedt waarbij de toepassing van de  coëfficiënt geen aanleiding mag geven tot een hoger tarief  dan 3,97%.

De coëfficiënt wordt verkregen door het gemiddelde van de  maandelijkse indexcijfers van het jaar 1996 te delen door  het gemiddelde van de maandelijkse indexcijfers van het  jaar dat voorafgaat aan het jaar van de  inkomsten.

1° het gemiddelde van de maandelijkse indexcijfers wordt  afgerond op het hogere of lagere honderdste naargelang het  cijfer van de duizendsten al of niet vijf bereikt;

2° de coëfficiënt wordt afgerond op het hogere of lagere  tienduizendste  naargelang  het  cijfer  van  de  honderdduizendsten al of niet vijf bereikt;

3° na de toepassing van de coëfficiënt wordt het verkregen  tariefbedrag afgerond op het hogere of lagere honderdste  naargelang het cijfer van de duizendsten al of niet vijf  bereikt.

---- historiek ----  ---- historique ----

- gewijzigd door art. 85 van het decreet van 19.12.2025  (B.S., 30.12.2025). Inwerkingtreding: 01.01.2026

- gewijzigd door art. 11 van het decreet van 09.07.2021  (B.S., 10.09.2021). Inwerkingtreding: vanaf het aanslagjaar  na publicatie van dit decreet in het Belgisch Staatsblad en  ten vroegste vanaf aanslagjaar 2023.

- gewijzigd door art. 4 van het decreet van 02.04.2021 (B.S.,  15.04.2021). Inwerkingtreding: 25.04.2021

- gewijzigd door art. 34 van het besluit van 17.07.2020 (B.S.  17.11.2020). Tekst treedt in werking op 01.01.2021.  Bekrachtigd door art. 224, 2° van het decreet van  09.07.2021 (B.S., 10.09.2021). Inwerkingtreding:  20.09.2021.

- gewijzigd door art. 19 van het decreet van 06.07.2018  (B.S. 30.08.2018). Tekst in werking getreden vanaf  aanslagjaar 2018

- gewijzigd door art. 5 van het decreet van 22.06.2018.  Tekst in werking getreden vanaf aanslagjaar 2019

- gewijzigd door art. 30 van het decreet van 18 november  2016. Tekst in werking getreden vanaf aanslagjaar 2018

- § 2 vervangen door art. 3 van het decreet van 20 dec. 2013  (B.S., 31.12.2013). De tekst is in werking getreden met  ingang van aanslagjaar 2014 (art. 61).

§ 1. Overeenkomstig artikel 464/1, 1°, van het Wetboek  van de Inkomstenbelastingen 1992, zijn de provincies,  gemeenten  en  de  agglomeraties  gemachtigd  om  opcentiemen op de onroerende voorheffing te heffen.

§ 2. Voor iedere gemeente van het Vlaamse Gewest mag het  tarief, vermeld in artikel 2.1.4.0.1, op zichzelf de opbrengst  van de gemeentelijke opcentiemen van het aanslagjaar  waarin dit artikel in werking treedt niet verhogen ten  opzichte van het vorige aanslagjaar.

Als een gemeente de opbrengst van haar deel in die  onroerende voorheffing evenwel wil wijzigen, geeft ze dat  expliciet aan in haar beslissing en vermeldt ze  afzonderlijk :

Lorsqu’une commune souhaite toutefois modifier le  produit de sa part dans ce précompte immobilier, elle  l’indique explicitement dans sa décision, et elle  mentionné séparément :  1° het aantal opcentiemen dat nodig is om, op haar niveau,  dezelfde opbrengst te verkrijgen als in het aanslagjaar  voorafgaand aan het aanslagjaar waarin dit artikel in  werking treedt;

2° het aantal opcentiemen dat voor het aanslagjaar waarin  dit artikel in werking treedt daadwerkelijk wordt geheven.

§ 3. Voor iedere provincie van het Vlaamse Gewest mogen  de provinciale opcentiemen niet meer bedragen dan :

1° voor de provincie Antwerpen : 145,33 opcentiemen;  1° pour la province d’Anvers : 145,33 centimes  additionnels ;

2° voor de provincie Limburg : 214,52 opcentiemen;  2° pour la province du Limbourg : 214,52 centimes  additionnels ;

3° voor de provincie Oost-Vlaanderen : 148,47  opcentiemen;

4° voor de provincie Vlaams-Brabant : 171,75  opcentiemen;

5° voor de provincie West-Vlaanderen : 186,22  opcentiemen.

---- historiek ----  ---- historique ----

- vervangen door art. 31 van het decreet van 18 november  2016. Tekst in werking getreden vanaf aanslagjaar 2018

- gewijzigd door art. 7 van het decreet van 19.12.2014 (B.S.,  13.01.2015). De tekst is in werking getreden vanaf het  aanslagjaar 2015. (art. 24)

###### Art. 2.1.5.0.1.  Art. 2.1.5.0.1.

§ 1. Er wordt een vermindering verleend van :  § 1er. Il est accordé une réduction :

1° 25 % van de onroerende voorheffing voor de woning  waar de belastingplichtige volgens het bevolkingsregister  op 1 januari van het aanslagjaar zijn hoofdverblijfplaats  heeft, als het kadastraal inkomen van zijn gezamenlijke, in  het Vlaamse Gewest gelegen, onroerende goederen niet  meer bedraagt dan 745 euro;

2° de onroerende voorheffing voor de kinderen die in  aanmerking komen voor de gezinsbijslagen, vermeld in  artikel 5, § 1, IV, van de bijzondere wet van 8 augustus 1980  tot hervorming der instellingen, voor de woning die op 1  januari van het aanslagjaar wordt betrokken door een gezin  met ten minste twee kinderen die daar volgens het  bevolkingsregister hun woonplaats hebben en die in  aanmerking komen voor gezinsbijslag. De vermindering  bedraagt per kind 8 euro. Daarbij wordt een gehandicapt kind  voor twee gerekend.

2° le précompte immobilier pour les enfants qui entrent en  ligne de compte pour les allocations familiales, visées à  l'article 5, § 1er, IV, de la loi spéciale du 8 août 1980 de  réformes institutionnelles, pour l'habitation qui est  occupée, le 1er janvier de l'année d'imposition, par une famille ayant au moins deux enfants, qui y ont leur  domicile selon le registre de la population et qui entrent en  ligne de compte pour l'allocation familiale. La diminution  s'élève à 8 euros par enfant. Dans ce contexte, un enfant handicapé compte pour deux.  Het voormelde bedrag van 8 euro is gekoppeld aan de  schommelingen van het algemene indexcijfer van de  consumptieprijzen van het Rijk en wordt jaarlijks aangepast  op basis van een coëfficiënt die verkregen wordt door het  gemiddelde van de maandelijkse indexcijfers van het jaar  dat voorafgaat aan het jaar van de inkomsten, te delen door  het gemiddelde van de indexcijfers van het jaar 2022. Het  gemiddelde van de maandelijkse indexcijfers wordt  afgerond op het hogere of lagere honderdste naargelang het  cijfer van de duizendsten al of niet vijf bereikt, en de  coëfficiënt wordt afgerond op het hogere of lagere  tienduizendste

naargelang het cijfer van de honderdduizendsten al of niet  vijf bereikt. Na de toepassing van de coëfficiënt wordt het  bedrag afgerond op het hogere of lagere honderdste  naargelang het cijfer van de duizendste al of niet vijf  bereikt;

3° de onroerende voorheffing per persoon met een  handicap, met uitsluiting van de gehandicapte kinderen,  vermeld in punt 2°, voor de woning waar de persoon met  een handicap volgens het bevolkingsregister op 1 januari  van het aanslagjaar zijn woonplaats heeft. Deze  vermindering wordt berekend alsof het een gehandicapt  kind betreft.

§ 1/1. De vermindering, vermeld in paragraaf 1, 2°, wordt  in geval van ouders die niet samenleven proportioneel  toegekend, afhankelijk van de periode waarin die ouder het  kind of de kinderen huisvest, als de volgende voorwaarden  cumulatief zijn vervuld:

2° de ouder waarbij het kind of de kinderen volgens het  bevolkingsregister niet zijn of hun woonplaats hebben,  zorgt voor de huisvesting in een woning die in het Vlaamse  Gewest ligt waarin die ouder op 1 januari van het  aanslagjaar volgens het bevolkingsregister zijn woonplaats  heeft;

3° de gedeeltelijke huisvesting wordt op een van de  volgende wijzen aangetoond:

a) op grond van een overeenkomst die uiterlijk op 1 januari  van het aanslagjaar geregistreerd of door een rechter  gehomologeerd is;

b) op grond van een rechterlijke beslissing die uiterlijk op 1  januari van het aanslagjaar is uitgesproken;

c) op grond van een overeenkomst die uiterlijk op 1 januari  van het aanslagjaar tot stand is gekomen ten gevolge van  een vrijwillige gezinsbemiddeling door een bemiddelaar die  erkend is door de commissie, vermeld in artikel 1727 van  het Gerechtelijk Wetboek;

d) op grond van een overeenkomst die de beide ouders  uiterlijk op 1 januari van het aanslagjaar hebben  ondertekend.

De vermindering, vermeld in paragraaf 1, 2°, wordt  proportioneel verdeeld tussen de woning, vermeld in  paragraaf 1, 2°, en de woning, vermeld in het eerste lid, 2°.

Als de bevoegde entiteit van de Vlaamse Administratie  geen andersluidende kennisgeving ontvangt en de  voorwaarden, vermeld in paragraaf 1, 2°, en paragraaf 1/1,  zijn vervuld, is de aanvraag die ingediend is voor een  aanslagjaar, geldig voor de volgende aanslagjaren.

Als het bedrag, vermeld in paragraaf 1, 2°, overeenkomstig  het eerste lid proportioneel wordt toegekend, worden de  proportioneel verdeelde bedragen afgerond op het hogere of  lagere honderdste naargelang het cijfer van de duizendsten  al of niet vijf bereikt.

§ 2. Er wordt een vermindering verleend van :  § 2. Il est accordé une réduction :

1° 20 % van de onroerende voorheffing gedurende tien jaar  voor  woningen  waarvoor  de  aanvraag  van  een  stedenbouwkundige vergunning is ingediend vóór 1 januari  2013 en die op 1 januari van het aanslagjaar een E-peil  hebben van ten hoogste E60;

2° 20 % van de onroerende voorheffing gedurende tien jaar  voor andere gebouwde onroerende goederen dan woningen  waarvoor de aanvraag van een stedenbouwkundige  vergunning is ingediend vóór 1  januari 2013 en die op 1 januari van het aanslagjaar een E- peil hebben van ten hoogste E70;

4° de 50 % du précompte immobilier pendant cinq ans  pour des biens immeubles bâtis pour lesquels la  demande d'autorisation urbanistique ou de permis  d'environnement pour actes urbanistiques a été  introduite après le 31 décembre 2012 et qui, au 1 janvier  de l'année d'imposition, ont un niveau E maximal tel  qu'indiqué au tableau suivant :

4° 50% van de onroerende voorheffing gedurende vijf jaar  voor gebouwde onroerende goederen waarvoor de  aanvraag van een stedenbouwkundige vergunning of  omgevingsvergunning  voor  stedenbouwkundige  handelingen na 31 december 2012 is ingediend en die op 1  januari van het aanslagjaar ten hoogste een E-peil hebben  als vermeld in de volgende tabel:

datum aanvraag stedenbouwkundige vergunning of

E-peil nieuwbouw

E-peil ingrijpende  energetische renovatie

omgevingsvergunning voor stedenbouwkundige

/  Niveau E constructions

handelingen

/  Niveau E rénovation  énergétique substantielle

/  date de la demande d’autorisation urbanistique ou  de permis d'environnement pour actes urbanistiques

nouvelles

vanaf 1 januari 2013 tot en met 31 december 2013

E50  /

/  du 1 janvier 2013 au 31 décembre 2013

vanaf 1 januari 2014 tot en met 31 december 2015

E40  /

/  du 1 janvier 2014 au 31 décembre 2015

vanaf 1 januari 2016 tot en met 30 september 2016

E30  /

/  du 1 janvier 2016 au 30 septembre 2016

vanaf 1 oktober 2016 tot en met 31 december 2019

E30  E90

/  du 1 octobre 2016 au 31 décembre 2019

vanaf 1 januari 2020 tot en met 31 december 2021

E30  /

/  du 1 janvier 2020 au 31 décembre 2021

vanaf 1 januari 2022 tot en met 31 december 2022 /

E20  /

du 1 janvier 2022 au 31 décembre 2022

5° 100% van de onroerende voorheffing gedurende vijf  jaar voor gebouwde onroerende goederen waarvoor de  aanvraag van een stedenbouwkundige vergunning of  omgevingsvergunning voor stedenbouwkundige  handelingen is ingediend na 31 december 2012 en die op  1 januari van het aanslagjaar een E-peil hebben als  vermeld in de volgende tabel:

5° de 100 % du précompte immobilier pendant cinq ans  pour des biens immeubles bâtis pour lesquels la demande  d'autorisation urbanistique ou de permis d'environnement  pour actes urbanistiques a été introduite après le 31  décembre 2012 et qui, au 1 janvier de l'année d'imposition,  ont un niveau E tel qu'indiqué au tableau suivant :

datum aanvraag stedenbouwkundige vergunning of

E-peil nieuwbouw

E-peil ingrijpende  energetische renovatie

omgevingsvergunning voor stedenbouwkundige

/  Niveau E constructions

handelingen

/  Niveau E rénovation  énergétique substantielle

/  date de la demande d’autorisation urbanistique ou  de permis d'environnement pour actes urbanistiques

nouvelles

/  du 1 janvier 2013 au 31 décembre 2014

vanaf 1 januari 2015 tot en met 31 december 2015

E30  /

/  du 1 janvier 2015 au 31 décembre 2015

vanaf 1 januari 2016 tot en met 30 september 2016  E20  /  /  du 1 janvier 2016 au 30 septembre 2016  vanaf 1 oktober 2016 tot en met 31 december 2021

E20  E60

/  du 1 octobre 2016 au 31 décembre 2021

vanaf 1 januari 2022 tot en met 31 december 2022 /

E10  E60

du 1 janvier 2022 au 31 décembre 2022

vanaf 1 januari 2023 tot en met 30 september 2025  / à partir du 1er janvier 2023 jusqu'au 30 septembre

/  E60

6° 50% van de onroerende voorheffing gedurende vijf  jaar voor gebouwde onroerende goederen waarvoor de  aanvraag  van  een  omgevingsvergunning  voor  stedenbouwkundige handelingen vanaf 1 januari 2023  tot en met 30 september 2025 is ingediend en die na  herbouw of gedeeltelijke herbouw op 1 januari van het  aanslagjaar een E-peil hebben van ten hoogste E20;

6° de 50 % du précompte immobilier pendant cinq ans  pour les biens immeubles bâtis pour lesquels une  demande de permis d'environnement pour actes  urbanistiques est introduite à partir du 1er janvier 2023  jusqu'au 30 septembre 2025 et qui, après reconstruction  ou reconstruction partielle, ont un niveau E maximum  de E20 au 1 janvier de l'année d'imposition ;

7° 100% van de onroerende voorheffing gedurende vijf  jaar voor gebouwde onroerende goederen waarvoor de  aanvraag  van  een  omgevingsvergunning  voor  stedenbouwkundige handelingen vanaf 1 januari 2023  tot en met 30 september 2025 en die na herbouw of  gedeeltelijke herbouw op 1 januari van het aanslagjaar  een E-peil hebben van ten hoogste E10.

7° de 100 % du précompte immobilier pendant cinq ans  pour les biens immeubles bâtis pour lesquels une  demande de permis d'environnement pour actes  urbanistiques est introduite à partir du 1er janvier 2023  jusqu'au 30 septembre 2025 et qui, après reconstruction  ou reconstruction partielle, ont un niveau E maximum  de E10 au 1 janvier de l'année d'imposition.

Het E-peil, vermeld in het eerste lid, is het peil van  primair energieverbruik, zoals berekend ter uitvoering  van titel XI van het Energiedecreet van 8 mei 2009.

Le niveau E, visé à l'alinéa premier, est le niveau de  consommation d'énergie primaire, tel que calculé en  exécution du titre XI du décret relatif à l'énergie du 8  mai 2009.

De grens van het E-peil waaraan het gebouwde  onroerend goed moet voldoen voor de vermindering,  wordt vastgesteld rekening houdend met het ogenblik  waarop  de  volledige  aanvraag  van  een  stedenbouwkundige vergunning is ingediend.

La limite du niveau E à laquelle doit répondre le bien  immobilier bâti pour la réduction est déterminée en  tenant compte du moment auquel la demande complète  d'une autorisation urbanistique est introduite.

De termijn van tien jaar, vermeld in het eerste lid, 1° tot  en met 3°, neemt een aanvang in het jaar dat volgt op het  jaar waarin het E-peil dat recht geeft op een  vermindering, voor de eerste keer is bepaald voor het  gebouwde onroerend goed in kwestie. Die termijn kan  op zijn vroegst een aanvang nemen vanaf het aanslagjaar  2009.

Le délai de dix ans, visé à l'alinéa premier, 1°, à 3°  inclus, prend cours l'année suivant l'année dans laquelle  le niveau E donnant droit à une réduction est déterminé  pour la première fois pour le bien immobilier bâti en  question. Ce délai peut prendre cours au plus tôt à partir  de l'année d'imposition 2009.

Alleen de gebouwde onroerende goederen waarvoor het  vereiste E-peil voor het gebouw als geheel is bepaald,  komen in aanmerking voor de verminderingen, vermeld in  het eerste lid. De verminderingen worden alleen  toegekend als het gaat om gedeeltelijke herbouw,  herbouw, renovatie of nieuwbouw als vermeld in artikel  1.1.1, § 2, 46/2°, 47/2°, 50° en 110°, van het  Energiebesluit van 19 november 2010 en als is voldaan  aan alle EPB-eisen, vermeld in titel IX, hoofdstuk I, van  het Energiebesluit van 19 november 2010, die op de  omgevingsvergunning(en)  voor  stedenbouwkundige  handelingen van het specifieke bouwproject van  toepassing zijn.

Bij de overdracht van een onroerend goed waarvoor een  vermindering als vermeld in het eerste lid, is verleend,  wordt de vermindering vanaf het aanslagjaar dat volgt  op het jaar van de overdracht, verder toegekend aan de  verkrijger van het goed, voor de nog resterende  aanslagjaren in de periode van tien jaar of vijf jaar.

---- historiek ----  ---- historique ----

- gewijzigd door art. 30 van het decreet van 20.12.2024  (B.S. 30.12.2024). Inwerkingtreding op 01.01.2025

- gewijzigd door art. 9 van het decreet van  16.12.2022 (B.S. 29.12.2022). Inwerkingtreding vanaf  aanslagjaar 2023

- gewijzigd door art. 3 van het decreet  van 09.12.2022 (B.S. 20.12.2022). Inwerkingtreding:  30.12.2022

- gewijzigd door art. 2 van het decreet van 19.11.2021  (B.S., 16.12.2021). Inwerkingtreding: 01.01.2022

- gewijzigd door art. 5 van het decreet van 02.04.2021  (B.S. 15.04.2021). Tekst heeft uitwerking met ingang van  01.01.2019

- gewijzigd door art. 2 van het decreet van 05.04.2019  (B.S. 24.04.2019). Tekst in werking getreden op  04.05.2019

- gewijzigd door art. 3 van het decreet van 21.12.2018  (B.S. 28.12.2018). Tekst in werking getreden op

01.01.2019

- gewijzigd door art. 41 van het decreet van 23 december  2016. Tekst in werking getreden vanaf aanslagjaar 2017

- gewijzigd door art. 98 van het decreet van 18 dec. 2015  (B.S., 29.12.2015). De tekst is in werking getreden vanaf  aanslagjaar 2016 (art. 135)

###### Art. 2.1.5.0.2.  Art. 2.1.5.0.2.

§ 1. Op aanvraag van de belastingschuldige wordt :  § 1er. Sur la demande du redevable :

1° de vermindering van de onroerende voorheffing,  vermeld in artikel 2.1.5.0.1, § 1, 1°, op 50 % gebracht  voor een tijdperk van vijf jaar dat aanvangt met het  eerste jaar waarvoor de onroerende voorheffing is  verschuldigd, als het een woning betreft die de  belastingplichtige heeft laten bouwen of nieuw gebouwd  heeft aangekocht;

2° een vermindering van 20 % van de onroerende  voorheffing verleend voor de woning die wordt  betrokken door een oorlogsverminkte die het voordeel  geniet van artikel 13 van de samengeordende wetten op  de vergoedingspensioenen, gecoördineerd op 5 oktober  1948;

3° een kwijtschelding of proportionele vermindering van  de onroerende voorheffing verleend als het belastbaar  inkomen overeenkomstig artikel 15 van het federale  WIB 92 kan worden verminderd;

4° de vermindering van de onroerende voorheffing,  vermeld in artikel 2.1.5.0.1, § 1, 2°, verleend voor de  kinderen  van  grensarbeiders  die  ingevolge  de  regelgeving in het land waar de grensarbeiders zijn  tewerkgesteld, van ieder stelsel van gezinsbijslag zijn  uitgesloten, als ze volgens de Belgische regelgeving  inzake gezinsbijslag in aanmerking zouden komen voor  gezinsbijslag.

§ 2. Voor onroerende goederen die langer dan twaalf  maanden niet in gebruik zijn genomen, rekening  houdend  met  het  vorige  aanslagjaar,  kan  de  kwijtschelding of proportionele vermindering van de  onroerende voorheffing, vermeld in paragraaf 1, eerste  lid, 3°, alleen worden verleend voor:

1° een niet-gemeubileerd gebouwd onroerend goed,  opgenomen in een onteigeningsplan;

2° een niet-gemeubileerd gebouwd onroerend goed in  renovatie of verbouwing met sociaal of cultureel doel,

3° een onroerend goed waarvan door toedoen van een  ramp, overmacht, een lopende gerechtelijke of  administratieve procedure of onderzoek of een niet-  afgehandelde  procedure  van  erfenis  de  belastingplichtige zijn zakelijke rechten niet kan  uitoefenen.

De kwijtschelding of proportionele vermindering voor  het geval, vermeld in het eerste lid, 2°, kan worden  verleend voor een periode van maximaal vijf jaar.

---- historiek ----  ---- historique ----

- gewijzigd door art. 4 van het decreet van 21.12.2018  (B.S. 28.12.2018). Tekst in werking getreden op  01.01.2019

- gewijzigd door art. 20 van het decreet van 23.12.2016  (B.S.: 30.12.2016). Tekst in werking getreden op  08.01.2017

###### Art. 2.1.5.0.3.  Art. 2.1.5.0.3.

De verminderingen, vermeld in artikel 2.1.5.0.1, § 1, 1°  tot en met 3°, artikel 2.1.5.0.1, § 1/1, artikel 2.1.5.0.1, §  2, eerste lid, 1° tot en met 7°, en artikel 2.1.5.0.2, § 1, 1°  en 2°, worden beoordeeld naar de toestand op 1 januari  van het jaar waarnaar het aanslagjaar van de onroerende  voorheffing wordt genoemd. Die verminderingen  kunnen worden samengevoegd, met uitzondering van de  vermindering, vermeld in artikel 2.1.5.0.1, § 2, eerste lid,  3°, die niet samengevoegd kan worden met de  verminderingen, vermeld in artikel 2.1.5.0.1, § 2, eerste  lid, 1° en 2°.

---- historiek ----  ---- historique ----

- gewijzigd door art. 10 van het decreet van 16.12.2022  (B.S., 29.12.2022). Inwerkingtreding vanaf aanslagjaar  2023

- gewijzigd door art. 3 van het decreet van 19.11.2021  (B.S., 16.12.2021). Inwerkingtreding: 01.01.2022

###### Art. 2.1.5.0.4.  Art. 2.1.5.0.4.

De verminderingen, vermeld in artikel 2.1.5.0.1, § 1, 2°  en 3°, artikel 2.1.5.0.1, § 1/1 en artikel 2.1.5.0.2, § 1, 2°,  zijn van de huur aftrekbaar, niettegenstaande elk beding  dat strijdig is daarmee. De verminderingen zijn niet van  toepassing op het gedeelte van de woning of van het  onroerend goed dat wordt bewoond door personen die  geen deel uitmaken van hetzelfde gezin of die niet tot het  gezin van de betrokken oorlogsverminkte of van het  gehandicapt kind of de persoon met een handicap  behoren.

---- historiek ----  ---- historique ----

- gewijzigd door art. 4 van het decreet van 09.12.2022  (B.S. 20.12.2022). Inwerkingtreding: 30.12.2022

###### Art. 2.1.5.0.5.  Art. 2.1.5.0.5.

Als de grens van 745 euro, vermeld in artikel 2.1.5.0.1,  § 1, 1°, wordt overschreden, blijft de vermindering van  25 % ingevolge die bepaling niettemin behouden voor  de belastingplichtige die ze genoten heeft voor het  aanslagjaar 1979, zolang:

Lorsque la limite de 745 euros, visée à l'article 2.1.5.0.1,  § 1er, 1°, est dépassée, la réduction de 25 % prévue par  cette disposition est néanmoins maintenue au profit du  contribuable  qui en a bénéficié pour l'année  d'imposition 1979, aussi longtemps que :  1° de belastingplichtige zijn woning volledig blijft  betrekken;

2° het overschrijden van de grens van 745 euro  uitsluitend het gevolg is van de algemene perequatie van  de kadastrale inkomens die van toepassing is met ingang  van het aanslagjaar 1980;

3° het kadastraal inkomen van zijn gezamenlijke, in het  Vlaamse Gewest gelegen, onroerende goederen niet  meer bedraagt dan 992 euro.

###### Art. 2.1.5.0.6.  Art. 2.1.5.0.6.

(…)  (…)

---- historiek ----  ---- historique ----

- opgeheven door art. 8 van het decreet van 22.12.2017.  Tekst treedt in werking op 09.06.2020 (art. 1 besluit  04.05.2018 B.S. 30.05.2018)

- gewijzigd door art. 5 van het decreet van 21.12.2018  (B.S. 28.12.2018). Tekst treedt in werking op 07.01.2019

- vervangen door art. 33 van het decreet van 18.11.2016.  Tekst in werking getreden vanaf aanslagjaar 2018

- vervangen door art. 52 van het decreet van 01 juli 2016  (B.S., 19.08.2016). Tekst treedt in werking op een door de  Vlaamse Regering vast te stellen datum (art.

66)

###### Art. 2.1.5.0.7.  Art. 2.1.5.0.7.

Aan de belastingplichtige rechtspersoon wordt een  belastingkrediet toegekend dat gelijk is aan :

1° (…);  1° (…) ;

2° (…);  2° (…);

Het belastingkrediet, vermeld in het eerste lid, kan nooit  meer bedragen dan de onroerende voorheffing, na  toepassing van vrijstellingen en verminderingen.

Het belastingkrediet, vermeld in het eerste lid, komt  volledig ten laste van het Vlaamse Gewest.

---- historiek ----  ---- historique ----

- gewijzigd door art. 30 van het programmadecreet van  20 december 2019 (B.S., 30.12.2019). Tekst treedt in  werking vanaf aanslagjaar 2020

- gewijzigd door art 6 van het decreet van 22 juni 2018.  Tekst treden inwerking vanaf aanslagjaar 2019 zien art  21, eerste lid.

- vervangen door art. 34 van het decreet van 18  november 2016. Tekst van toepassing vanaf aanslagjaar  2018

#### Afdeling 6 - Vrijstellingen  Section 6 – Exonérations

###### Art. 2.1.6.0.1.  Art. 2.1.6.0.1.

Op aanvraag van de belastingschuldige wordt een  vrijstelling van de onroerende voorheffing verleend voor  het kadastraal inkomen van :

1° de onroerende goederen of delen ervan, gelegen in het  Vlaamse Gewest die een belastingplichtige of een  bewoner zonder winstoogmerk heeft bestemd voor het  openbaar uitoefenen van een eredienst of van de  vrijzinnige morele dienstverlening, voor onderwijs, voor  het vestigen van hospitalen, klinieken, dispensaria,  rusthuizen, vakantiehuizen voor gepensioneerden, of  van andere soortgelijke weldadigheidsinstellingen;

2° de onroerende goederen die een vreemde staat heeft  bestemd voor de huisvesting van zijn diplomatieke of  consulaire zendingen of van culturele instellingen die  zich niet met verrichtingen van winstgevende aard  bezighouden, op voorwaarde van wederkerigheid;

3° de onroerende goederen die de aard van nationale  domeingoederen hebben, op zichzelf niets opbrengen en  voor een openbare dienst of voor een dienst van  algemeen nut worden gebruikt

5° de nieuwe onroerende goederen, vermeld in artikel  471, § 3, van het federale WIB 92, die overeenkomstig  artikel 472, § 2, van het federale WIB 92 na 1 januari  1998 en voor 1 januari 2008 aanleiding hebben gegeven  tot een verhoogd kadastraal inkomen in vergelijking met  het kadastraal inkomen per 1 januari 1998;

6° des biens immobiliers nouveaux, visés à l'article 471,  § 3, du CIR 92 fédéral, pour lesquels, conformément à  l'article 472, § 2, du CIR 92 fédéral, un revenu cadastral  federale WIB 92, een kadastraal inkomen is vastgesteld  na 1 januari 1998 en voor 1 januari 2008;

6° de nieuwe onroerende goederen, vermeld in artikel  471, § 3, van het federale WIB 92, waarvoor voor de  eerste keer, overeenkomstig artikel 472, § 2, van het

7° de onroerende goederen die onder de toepassing van  het Bosdecreet van 13 juni 1990 vallen en die erkend zijn  voor de productie van bosbouwkundig teeltmateriaal als  vermeld in artikel 42 van het voormelde decreet;

8° de als monument beschermde onroerende goederen of  delen ervan die de Vlaamse Regering in erfpacht heeft  gegeven of in volle eigendom heeft afgestaan aan een  vereniging of stichting die is opgericht overeenkomstig  het Wetboek van vennootschappen en verenigingen, en  waarvan de hoofddoelstelling erin bestaat een of meer  beschermde onroerende goederen waarvan ze eigenaar  of erfpachter is, in stand te houden, te beheren en te  ontsluiten;

9° de onroerende goederen, vermeld in artikel 471, § 3,  van het federale WIB 92 voor het gedeelte dat  overeenstemt met het kadastraal inkomen van de nieuwe  onroerende goederen waarvoor overeenkomstig artikel  472, § 2, van het federale WIB 92 een kadastraal  inkomen wordt vastgesteld vanaf 1 januari 2014 en voor  1 januari 2020. Die vrijstelling kan cumulatief worden  genoten met de vrijstellingen, vermeld in punt 4° tot en  met punt 6°.

10° de onbebouwde onroerende goederen waarvoor een  natuurbeheerplan als vermeld in artikel 16ter, § 1, 4°,  van het decreet van 21 oktober 1997 betreffende het  natuurbehoud en het natuurlijk milieu, is goedgekeurd  conform de bepalingen en uitvoeringsbepalingen van het  voormelde decreet.

De vrijstelling, vermeld in het eerste lid, 5°, wordt  verleend voor het gedeelte dat het kadastraal inkomen,  vastgesteld op 1 januari 1998, overschrijdt.

De vrijstellingen, vermeld in het eerste lid, 1° tot en met  3°, worden ook verleend als het onroerend goed in  kwestie het voorwerp uitmaakt van een financiering  door middel van financiële leasing of huurkoop met  uitgestelde eigendomsoverdracht voor de duur van de  overeenkomst. Onder die overeenkomsten worden  zowel de leasingovereenkomsten, vermeld in artikel 44,

Les exonérations, visées à l'alinéa premier, 1° à 3°  inclus, sont également accordées lorsque le bien  immobilier en question fait l'objet d'un financement par  voie de crédit-bail ou de location-achat avec transfert de  propriété remise pour la durée de la convention. Par ces  conventions, on entend tant les conventions de leasing,  visées à l'article 44, § 3, 2°, b), du Code de la TVA, que  § 3, 2°, b), van het Wetboek van de belasting over de  toegevoegde waarde, als de leasingovereenkomsten of  vergelijkbare  overeenkomsten,  vermeld  in  het  koninklijk besluit van 29 april 2019 tot uitvoering van  het Wetboek van vennootschappen en verenigingen.

In afwijking van het eerste lid, 4° en 9°, wordt de  vrijstelling verleend, hetzij voor nieuwe onroerende  goederen waarvoor voor de eerste keer een kadastraal  inkomen is vastgesteld, hetzij voor het gedeelte dat het  kadastraal inkomen, vastgesteld op 1 januari 1998,  overschrijdt voor nieuwe onroerende goederen die na 1  januari 1998 aanleiding hebben gegeven tot een  verhoogd kadastraal inkomen in vergelijking met het  kadastraal inkomen per 1 januari 1998, voor de  belastingplichtige die behoort tot een doelgroep  waarvoor de Vlaamse Regering, met toepassing van  artikel 7.7.1, § 2, van het Energiedecreet van 8 mei 2009,  een ontwerp van energiebeleidsovereenkomst heeft  voorgelegd aan het Vlaams Parlement, en de  belastingplichtige  die  overeenkomst  niet  heeft  ondertekend of niet naleeft.

De nieuwe onroerende goederen die geplaatst worden in  industriële, nijverheids- of handelsgebouwen die met  toepassing van de Vlaamse Codex Ruimtelijke Ordening  van 15 mei 2009 in overtreding zijn inzake de  bouwvergunning, komen niet in aanmerking voor de  toepassing van het eerste lid, 4°, 5° en 9°.

---- historiek ----  ---- historique ----

- gewijzigd door art. 6 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- gewijzigd door art. 9, 1° van het decreet van 22.12.2017  (B.S., 21.02.2018). Tekst treedt in werking op 09.06.2020  (art. 1 besluit 04.05.2018 B.S.

30.05.2018)

- gewijzigd door art. 9, 2° van het decreet van 22.12.2017  (B.S., 21.02.2018). Tekst treedt in werking op 09.06.2018  (art. 1 besluit 04.05.2018 B.S.

30.05.2018)

- gewijzigd door art. 42 van het decreet van 23 december  2016 (B.S., 29.12.2016). Eerst lid, 9° treedt in werking op  1 januari 2017. Tweede lid treedt in werking vanaf  aanslagjaar 2017.

- eerste lid, 1°, werd vervangen door art. 2 van het  decreet van 15 juli 2016 (B.S., 18.08.2016). Tekst is van  toepassing vanaf aanslagjaar 2016 (art. 4)

- 9°, aangevuld door art. 2 van het decreet van 20 dec.

2013 (B.S., 17.01.2014 – ed. 2). Tekst is in werking  getreden vanaf aanslagjaar 2015 (art. 4).

- lid 5, vervangen door art. 2 van het decreet van 20 dec.  2013 (B.S., 17.01.2014 – ed. 2). Tekst treedt in werking  vanaf aanslagjaar 2015 (art. 4).

- lid 6, vervangen door art. 2 van het decreet van 20 dec.  2013 (B.S., 17.01.2014 – ed. 2). Tekst treedt in werking  vanaf aanslagjaar 2015 (art. 4).

###### Art. 2.1.6.0.2.  Art. 2.1.6.0.2.

Op aanvraag van de belastingschuldige wordt ook een  vrijstelling van de onroerende voorheffing verleend voor  het kadastraal inkomen van:

1° de onroerende goederen die zijn gebruikt om een  kleinhandelsactiviteit uit te oefenen, die in een  winkelarm gebied liggen en die op grond van een  geldige omgevingsvergunning verbouwd worden tot een  of meerdere woningen;

2° de onroerende goederen waarvan minstens de  benedenverdieping  wordt  gebruikt  om  een  kleinhandelsactiviteit uit te oefenen, die in een  kernwinkelgebied liggen en waarvan een of meer  verdiepingen boven de kleinhandelsactiviteit op grond  van een geldige omgevingsvergunning verbouwd  worden tot een of meer woningen;

a) de inventaris van ongeschikte of onbewoonbare  woningen, vermeld in artikel 3.19, § 1, van de Vlaamse  Codex Wonen van 2021;

b) de inventaris van leegstaande of verwaarloosde  bedrijfsruimten, vermeld in artikel 3, § 1, van het decreet  van 19 april 1995.

In het eerste lid wordt verstaan onder:  Dans l’alinéa 1er, on entend par :

1° kernwinkelgebied: een kernwinkelgebied als vermeld  in artikel 2, 3°, van het decreet van 15 juli 2016  betreffende het integraal handelsvestigingsbeleid;

2°  kleinhandelsactiviteit:  de  categorieën  van  kleinhandelsactiviteit, vermeld in artikel 3 van het  voormelde decreet;

3° winkelarm gebied: een winkelarm gebied als vermeld  in artikel 2, 8°, van het voormelde decreet.

3° zone pauvre en commerces : une zone pauvre en  commerces, telles que visée à l’article 2, 8°, du décret  précité.  De vrijstellingen, vermeld in het eerste lid, worden  verleend voor een periode van vijf jaar.

De vrijstellingen, vermeld in het eerste lid, 1° en 2°,  worden verleend vanaf het aanslagjaar dat volgt op het  jaar van de effectieve bewoning die blijkt uit de  inschrijving in het bevolkings- of vreemdelingenregister  binnen vijf jaar na de voorlopige oplevering van de  ombouwwerken.

De vrijstelling, vermeld in het eerste lid, 2°, wordt  verleend voor het gedeelte dat is bestemd voor  huisvesting.

De vrijstelling, vermeld in het eerste lid, 3°, wordt  verleend vanaf het aanslagjaar dat volgt op het jaar dat  het onroerend goed niet meer voorkomt in de inventaris  en wordt in voorkomend geval beperkt tot het gedeelte  van het bedrag van de belasting dat, inclusief de  provinciale en gemeentelijke opcentiemen, per woning  niet hoger is dan 1000 euro of per bedrijfsruimte niet  hoger is dan 4000 euro.

De vrijstellingen, vermeld in het eerste lid, zijn  overdraagbaar op de rechtsopvolger.

De Vlaamse Regering kan de nadere regels voor de  aanvraag van de vrijstellingen bepalen.

---- historiek ----  ---- historique ----

- gewijzigd door art. 27 van het decreet van 29.03.2019  (B.S. 29.04.2019). Tekst treedt in werking op 01.01.2021

- vervangen door art 7 van het decreet van 22 juni 2018  (MB 24.07.218). Tekst in werking getreden vanaf  aanslagjaar 2019, zien art 21, eerste lid.

- gewijzigd door art. 21 van het decreet van 23 december  2016 (B.S.: 30.12.2016). Tekst in werking getreden vanaf  aanslagjaar 2017

###### Art. 2.1.6.0.3.  Art. 2.1.6.0.3.

Aan de belastingschuldige wordt een automatische  vrijstelling van onroerende voorheffing verleend voor  het kadastraal inkomen van :

1° de onroerende goederen of delen ervan, gelegen in het  Vlaamse  Gewest,  die  gebruikt  worden  door  jeugdverenigingen die erkend worden overeenkomstig  het jeugddecreet van 23 november 2023 en hun lokale  afdelingen of door lokale jeugdwerkinitiatieven waarvan  het gemeentebestuur bevestigt dat ze beantwoorden aan  de definitie zoals bepaald in artikel 31, § 3, eerste lid,  van het voormelde decreet;

2° de onroerende goederen of delen ervan die aan al de  volgende voorwaarden voldoen:

a) ze liggen in het Vlaamse Gewest;  a) ils sont situés en Région flamande ;

b) ze worden gebruikt als toeristisch verblijf;  b) ils sont utilisés comme des résidences touristiques ;

c) ze zijn aangemeld als jeugdverblijf of als hostel  conform het decreet van 5 februari 2016 houdende het  toeristische logies;

d) ze hebben het label `Toerisme voor Allen' ontvangen  conform het decreet van 5 februari 2016 houdende het  toeristische logies.

---- historiek ----  ---- historique ----

- gewijzigd door art. 4 van het decreet van 03.04.2026  (M.B. 23.04.2026). Inwerkingtreding: 03.05.2026

- gewijzigd door art. 15 van het decreet van 11.02.2022  (B.S., 11.03.2022). Inwerkingtreding: nog te bepalen  door de Vlaamse Regering

###### Art. 2.1.7.0.1.  Art. 2.1.7.0.1.

De belasting wordt geheven in overeenstemming met de  bepalingen van artikel 3.3.2.0.1, eerste lid, 1°, en tweede  lid, 1°.

### Hoofdstuk 2 - Verkeersbelasting  Chapitre 2 - Taxe de circulation

#### Afdeling 1 - Belastbaar voorwerp  Section 1 re - Objet imposable

###### Art. 2.2.1.0.1.  Art. 2.2.1.0.1.

Overeenkomstig artikel 3 van het federale Wetboek van  23 november 1965 van de met inkomstenbelastingen  gelijkgestelde belastingen, wordt er een belasting  geheven op de stoom- of motorvoertuigen dienende  hetzij tot het vervoer van personen, hetzij tot het vervoer  van goederen of van om het even welke voorwerpen  over de wegen.

#### Afdeling 2 - Belastingplichtigen  Section 2 – Contribuables

###### Art. 2.2.2.0.1.  Art. 2.2.2.0.1.

§ 1. De belastingplichtige is degene die een of meer van  de voertuigen, vermeld in artikel 2.2.1.0.1, aanwendt  voor eigen gebruik of ze exploiteert, hetzij als ze zijn  eigendom of persoonlijk bezit zijn, hetzij als hij er  bestendig of gewoonlijk over beschikt door huur of  andere overeenkomst.

§ 2. De belasting ontstaat ten aanzien van de natuurlijke  persoon of rechtspersoon die vermeld is of vermeld moet  zijn op het inschrijvingsbewijs zolang een voertuig op  naam van die persoon is ingeschreven of ingeschreven  moet zijn in het repertorium van het Directoraat-  generaal Mobiliteit en Verkeersveiligheid. De bedoelde  voertuigen zijn de personenauto's, de auto's voor dubbel  gebruik, de trage auto's voor dubbel gebruik, de  minibussen, de ziekenauto's, de motorfietsen, de  motorfietsen-driewielers, de motorfietsen-vierwielers,

Deze paragraaf is niet van toepassing op :  Le présent paragraphe ne s'applique pas :

1° de voertuigen van alle aard die niet worden bedoeld  in het eerste lid;

2° de voertuigen van alle aard die niet onderworpen zijn  aan de reglementering voor de inschrijving van de  motorvoertuigen en de aanhangwagens.

---- historiek ----  ---- historique ----

- §2, eerste lid, werd gewijzigd door art. 9 van het  decreet van 08.12.2017 (B.S., 14.12.2017).De tekst is in  werking getreden vanaf 24.12.2017

- §2, eerste lid gewijzigd door art. 9 van het decreet van  19.12.2014 (B.S., 13.01.2015).De tekst is in werking  getreden vanaf het aanslagjaar 2015. (art. 24)

#### Afdeling 3 - Belastbare grondslag  Section 3 - Base imposable

###### Art. 2.2.3.0.1.  Art. 2.2.3.0.1.

De belasting wordt, naargelang van het geval,  vastgesteld op basis van het vermogen van de motor, van  zijn cilinderinhoud of van het maximaal toegestane  totaalgewicht van het voertuig, vastgesteld door de  bevoegde overheid, tenzij anders is bepaald in deze  codex.

---- historiek ----  ---- historique ----

- gewijzigd door art. 10 van het decreet van 08.12.2017  (B.S., 14.12.2017).De tekst is in werking getreden vanaf  24.12.2017

###### Art. 2.2.3.0.2.  Art. 2.2.3.0.2.

§ 1. Het belastbaar vermogen van de motor van de  voertuigen (pk) wordt berekend volgens de volgende  formule: pk = k * d2 * c * n.

§ 2. De parameters, vermeld in paragraaf 1, worden  gedefinieerd als volgt:

1° d = de cilinderboring, in meter;  1° d = l'alésage des cylindres, en mètre ;

2° c = de zuigerslag, in meter;  2° c = la course des pistons, en mètre ;

3° n = het aantal cilinders;  3° n = le nombre de cylindres ;

cilinderboring in millimeter tot en met

/  alésage des cylindres en millimètres jusqu'à

/  coefficient  69  6000  70  5887  71  5777  72  5672  73  5570  74  5471  75  5376  76  5284  77  5194  78  5108  79  5024  80  4943  81  4864  82  4788  83  4714  84  4642  85  4572  86  4504  87  4438  88  4373  89  4310  90 en meer

/  90 et plus

Voor de voertuigen waarvan de motor met zware olie  wordt aangedreven en die uitsluitend worden gebruikt  voor het bezoldigd vervoer van personen krachtens een  machtiging  uitgereikt  voor  de  exploitatie  van  autocardiensten, ter uitvoering van de besluitwet van 30  december 1946 betreffende het bezoldigd vervoer van  personen over de weg met autobussen en met autocars,  wordt de coëfficiënt k vastgesteld als volgt:

1° cilinderboring tot en met 89: 3400;  1° alésage des cylindres jusqu'à 89 inclus : 3.400 ;

2° cilinderboring 90 en meer: 3500.  2° alésage des cylindres de 90 et plus : 3500.

Cilinderboring en zuigerslag worden uitgedrukt in  millimeter. Gedeelten van een millimeter worden voor  een millimeter aangerekend of weggelaten, naargelang  ze al dan niet de halve millimeter overschrijden.

§ 3. Het belastbaar vermogen van de motor van de  voertuigen (pk) mag echter niet hoger zijn dan het  belastbaar vermogen dat wordt berekend volgens de  volgende formule: pk = 4 * Cy + Gew / 4.

1° Cy = de cilinderinhoud van de motor, in liter;  1° Cy = la cylindrée du moteur, en litres ;

2° Gew = het gewicht van het rijklare voertuig, in  honderden kilogram.

Gedeelten van een deciliter worden voor een deciliter  aangerekend of weggelaten, naargelang ze al dan niet de  halve deciliter overschrijden.

Gedeelten van honderd kilogram worden voor honderd  kilogram aangerekend of weggelaten, naargelang ze al  dan niet de vijftig kilogram overschrijden.

###### Art. 2.2.3.0.3.  Art. 2.2.3.0.3.

§ 1. In afwijking van de bepalingen van artikel 2.2.3.0.2  wordt het belastbaar vermogen van de motor van de  voertuigen (pk) die uitgerust zijn met motoren met  draaiende zuigers, berekend volgens de volgende  formule: pk = 4 * V + Gew / 4.

§ 2. De parameters, vermeld in paragraaf 1, worden  gedefinieerd als volgt:

1° V = het nuttige volume van de verbrandingskamers,  in liter;

2° Gew = het gewicht van het rijklare voertuig, in  honderden kilogram.

Het nuttige volume van de verbrandingskamers is gelijk  aan de gemiddelde cilinderinhoud van motoren met  heen- en weergaande zuigers, waarvan de werkelijke  motorkracht volgens de normen die aangenomen zijn  door de automobielconstructeurs, overeenstemt met die  van motoren met draaiende zuigers.

Gedeelten van honderd kilogram worden voor honderd  kilogram aangerekend of weggelaten, naargelang ze al  dan niet de vijftig kilogram overschrijden.

###### Art. 2.2.3.0.4.  Art. 2.2.3.0.4.

In afwijking van de bepalingen van artikel 2.2.3.0.2  wordt het belastbaar vermogen van de motor van de  voertuigen (pk) die uitgerust zijn met elektromotoren,  berekend volgens de volgende formule: pk = 0,0012 * n  * e * i.

De parameters, vermeld in het eerste lid, worden  gedefinieerd als volgt:

1° n = het aantal elementen;  1° n = le nombre d'éléments ;

3° i = de gemiddelde sterkte van de stroom bij dezelfde  regeling, in ampère.

###### Art. 2.2.3.0.5.  Art. 2.2.3.0.5.

Het  belastbaar  vermogen  van  de  motor  van  personenauto's,  auto's  voor  dubbel  gebruik  en  minibussen die niet zijn uitgerust met elektromotoren en  die vanaf 1 januari 1972 in de belasting moeten worden  aangegeven, wordt uitsluitend berekend volgens de  formules, vermeld in artikel 2.2.3.0.2, § 3, en artikel  2.2.3.0.3, § 1, waarin de parameter Gew / 4 wordt  vervangen door een coëfficiënt in functie van de  cilinderinhoud van de motor of van het nuttige volume  van de verbrandingskamers, vermeld in de volgende  tabel:

cilinderinhoud of nuttig volume van de

verbrandingskamers, in liter

/  cylindrée ou volume utile des chambres de combustion,

en litres

tot en met 0,9  jusqu'à 0,9 inclusivement  1,50  1 tot met 1,2  1 à 1,2 inclusivement  1,75  1,3 tot en met 1,5  1,3 à 1,5 inclusivement  2,00  1,6 en 1,7  1,6 et 1,7  2,25  1,8 en 1,9  1,8 et 1,9  2,50  2 en 2,1  2 et 2,1  2,75  2,2 en 2,3  2,2 et 2,3  3,00  2,4 tot en met 2,6  2,4 à 2,6 inclusivement  3,25  2,7 tot en met 3,3  2,7 à 3,3 inclusivement  3,50  3,4 tot en met 3,9  3,4 à 3,9 inclusivement  3,75  4 tot en met 4,9  4 à 4,9 inclusivement  4,00  5 tot met 5,9  5 à 5,9 inclusivement  4,50  6 en meer  6 et plus  5,00

###### Art. 2.2.3.0.6.  Art. 2.2.3.0.6.

De opname en de controle van de elementen die nodig  zijn voor de vaststelling van het belastbaar vermogen en  het belastbaar gewicht, gebeuren door middel van  aanduidingen  op  facturen,  in  catalogussen,  beschrijvende handleidingen, weegbons of in andere  bewijskrachtige documenten.

Zo nodig gaat de bevoegde entiteit van de Vlaamse  administratie over tot het wegen van het voertuig of tot  een grondig onderzoek ervan.

###### Art. 2.2.3.0.7.  Art. 2.2.3.0.7.

###### Art. 2.2.3.0.8.  Art. 2.2.3.0.8.

Breuken van fiscale paardenkracht worden naar boven  of naar beneden afgerond, naargelang ze al dan niet de  helft overschrijden.

Les fractions de chevaux fiscaux sont arrondies à l'unité  supérieure ou inférieure, selon qu'elles dépassent la  moitié ou non.

Breuken van deciliter van de cilinderinhoud worden  naar boven of naar beneden afgerond, naargelang ze al  dan niet de halve deciliter overschrijden.

Les fractions de décilitres de la cylindrée sont arrondies  à l'unité supérieure ou inférieure, selon qu'elles  dépassent le demi-décilitre ou non.

#### Afdeling 4 - Tarieven  Section 4 – Tarifs

###### Art. 2.2.4.0.1.  Art. 2.2.4.0.1.

§ 1. De belasting wordt, ofwel per periode van twaalf  opeenvolgende maanden, ofwel per kalenderjaar,  berekend op de wijze die in de hierna volgende  paragrafen wordt vermeld.

§ 1er. La taxe est calculée, soit par période de douze  mois consécutifs, soit par année calendaire, de la  manière visée aux paragraphes suivants.

§ 2. Voor de personenauto's, de auto's voor dubbel  gebruik en de minibussen wordt de belasting berekend,  op basis van fiscale paardenkracht (pk), volgens de  volgende tabel :

§ 2. Pour les voitures particulières, les voitures mixtes et  les minibus, la taxe est calculée, sur la base des chevaux  fiscaux (ch), selon le tableau suivant :

aantal pk

totaalbedrag van de belasting in euro

/  montant total de la taxe en euros  4 en minder / 4 et moins  69,72  5  87,24  6  126,12  7  164,76  8  203,76  9  242,64  10  281,16  11  364,92  12  448,56  13  532,08  14  615,84  15  699,48  16  916,20  17  1133,16  18  1350,00  19  1566,36  20  1783,20  meer dan 20

/  nombre de ch

1783,20 verhoogd met 97,20 per pk boven 20

/  1783,20 majoré de 97,20 par ch supérieur à 20

/  plus de 20

1° in functie van de CO2-uitstoot van het voertuig,  gemeten tijdens de homologatie ervan volgens de op het  moment van de eerste inschrijving geldende Europese  regelgeving, wordt het tarief

a) vermeerderd met 0,30% voor iedere gram CO2-  uitstoot per kilometer boven 122 gram en niet hoger dan  500 gram;

b) verminderd met 0,30% voor iedere gram CO2-  uitstoot per kilometer onder 122 gram, maar hoger dan  24 gram;

2° in functie van de euronorm en de brandstofsoort van  het voertuig en desgevallend de aanwezigheid van een  roetfilter wordt het tarief met een percentage  vermeerderd  of  verminderd  overeenkomstig  de  volgende tabel:

Euronorm

/  Euronorme

euro 0  30 %  50 %  euro 1  10 %  40 %  euro 2  5 %  35 %  euro 3  0 %  30 %  euro 3 + roetfilter

/  euro 3 + filtre à particules

euro 4  - 12,5 %  25 %  euro 4 + roetfilter

/  euro 4 + filtre à particules

euro 5 of EEV

/  euro 5 ou EEV

euro 6  - 15 %  15 %

In afwijking van artikel 2.2.4.0.2, § 2, bedraagt de  belasting, berekend overeenkomstig het eerste lid,  minimum 40 euro.

Deze  paragraaf  is  alleen  van  toepassing  op  wegvoertuigen van natuurlijke personen en andere  rechtspersonen  dan  vennootschappen,  autonome  overheidsbedrijven en verenigingen zonder  winstgevend doel, met leasingactiviteiten.

a) vermeerderd met 0,30% voor iedere gram CO 2 - uitstoot per kilometer boven 149 gram en niet hoger dan  50 gram;

b) verminderd met 0,30% voor iedere gram CO 2 -uitstoot  per kilometer onder 149 gram, maar hoger dan 24 gram.

b) réduit de 0,30% par gramme d'émission de CO 2 par  kilomètre en-dessous de 149 grammes et au-dessus de  24 grammes.    Deze paragraaf is alleen van toepassing op voertuigen  van natuurlijke personen en van andere rechtspersonen  dan vennootschappen, autonome overheidsbedrijven en  verenigingen  zonder  winstgevend  doel,  met  leasingactiviteiten.

Deze paragraaf is ook van toepassing op de  personenauto's, de auto's voor dubbel gebruik en de  minibussen die voor de eerste keer na 31 december 2020  worden ingeschreven bij een vergelijkbare instelling  binnen de Europese Economische Ruimte of een andere  staat, wanneer zij nadien worden ingeschreven in het  repertorium van het Directoraat-generaal Mobiliteit en  Verkeersveiligheid.

§ 3. Voor de motorvoertuigen, bestemd voor het vervoer  van goederen waarvan het maximaal toegestane  totaalgewicht 3 500 kilogram niet overschrijdt, de  lijkwagens, de alleenrijdende landbouwtractoren en de  alleenrijdende trekkers, andere dan die, vermeld in  paragraaf 6, bedraagt de belasting 19,32 euro per 500 kg  maximaal toegestane totaalgewicht.

§ 3/1. Voor de motorvoertuigen, bestemd voor het  vervoer van goederen, de lijkwagens, de alleenrijdende  landbouwtractoren en de alleenrijdende trekkers, als het  andere voertuigen zijn dan de voertuigen, vermeld in  paragraaf 6, die na 30 juni 2017 worden ingeschreven in  het repertorium van het Directoraat-generaal Mobiliteit  en Verkeersveiligheid en waarvan de maximaal  toegelaten massa maximum 2500 kilogram bedraagt,  bedraagt de belasting 19,32 euro per 500 kg maximaal  toegelaten massa, met inachtneming van volgende  elementen:

1° in functie van de CO2-uitstoot van het voertuig,  gemeten tijdens de homologatie ervan volgens de op het  moment van de eerste inschrijving geldende Europese  regelgeving, wordt het tarief

b) verminderd met 0,30% voor iedere gram CO2-  uitstoot per kilometer onder 122 gram, maar hoger dan  24 gram;

b) réduit de 0,30% par gramme d’émission de CO2 par  kilomètre en-dessous de 122 grammes et au-dessus de  24 grammes ;

2° en fonction de l’euronorme et du type de carburant  du véhicule et, le cas échéant, de la présence d’un filtre  à particules, le tarif est majoré ou réduit d’un  pourcentage, conformément au tableau suivant :

2° in functie van de euronorm en de brandstofsoort van  het voertuig en, in voorkomend geval, de aanwezigheid  van een roetfilter wordt het tarief met een percentage  vermeerderd of verminderd conform de volgende tabel:

Euronorm

Benzine en andere brandstoffen

/  Essence et autres carburants

/  Euronorme

Diesel

euro 0  30 %  50 %  euro 1  10 %  40 %  euro 2  5 %  35 %  euro 3  0 %  30 %  euro 3 + roetfilter

/  euro 3 + filtre à particules

/  25 %

euro 4  - 12,5 %  25 %  euro 4 + roetfilter

/  euro 4 + filtre à particules

/  17,5 %

euro 5 of EEV

/  euro 5 ou EEV

- 15 %  17,5 %

euro 6  - 15 %  15 %  In afwerking van artikel 2.2.4.0.2. , § 2, bedraagt de  belasting, berekend overeenkomstig het eerste lid,  minimum 40 euro.

Par dérogation à l’article 2.2.4.0.2, § 2, la taxe, calculée  conformément à l’alinéa 1er, s’élève à 40 euros au  minimum.

Deze paragraaf is alleen van toepassing op voertuigen  van natuurlijke personen en van andere rechtspersonen  dan vennootschappen, autonome overheidsbedrijven en  verenigingen  zonder  winstgevend  doel,  met  leasingactiviteiten.

Le présent paragraphe s’applique uniquement aux  véhicules de personnes physiques et d’autres personnes  morales que les sociétés, les entreprises publiques  autonomes et les associations sans but lucratif, qui  exercent des activités de leasing.

§ 3/2. Voor de motorvoertuigen, bestemd voor het  vervoer van goederen, de lijkwagens, de alleenrijdende  landbouwtractoren en de alleenrijdende trekkers, als het  andere voertuigen zijn dan de voertuigen, vermeld in  paragraaf 6, die na 30 juni 2017 worden ingeschreven in  het repertorium van het Directoraat-generaal Mobiliteit  en Verkeersveiligheid en waarvan de maximaal  toegelaten massa hoger is dan 2500 kilogram en 3500  kilogram niet overschrijdt, bedraagt de belasting 19,32  euro per 500 kg maximaal toegelaten massa.

§ 3/2. Pour les camionnettes, destinées au transport de  marchandises, les corbillards, les tracteurs agricoles à  moteur solos et les tracteurs à moteur solos, autres que  ceux, visés au paragraphe 6, qui sont inscrits au  répertoire de la Direction générale Mobilité et Sécurité  routière après le 30 juin 2017 et dont la masse maximale  autorisée est supérieure à 2500 kg sans dépasser 3500  kg, la taxe s’élève à 19,32 euros par 500 kg de la masse  maximale autorisée.

Euronorm

Percentage

/  Pourcentage  euro 0  35 %  euro 1  25 %  euro 2  20 %  euro 3  15 %  euro 3 + roetfilter

/  Euronorme

/  euro 3 + filtre à particules

10 %

euro 4  10 %  euro 3 + roetfilter

/  euro 4 + filtre à particules

2,5 %

euro 5 of EEV

/  euro 5 ou EEV

2,5 %

euro 6  0 %

In afwijking van artikel 2.2.4.0.2, § 2, bedraagt de  belasting, berekend overeenkomstig het eerste lid,  minimum 40 euro.

Par dérogation à l’article 2.2.4.0.2, § 2, la taxe, calculée  conformément à l’alinéa 1er, s’élève à 40 euros au  minimum.

Deze paragraaf is alleen van toepassing op voertuigen  van natuurlijke personen en van andere rechtspersonen  dan vennootschappen, autonome overheidsbedrijven en

Le présent paragraphe s’applique uniquement aux  véhicules de personnes physiques et d’autres personnes  morales que les sociétés, les entreprises publiques  verenigingen  zonder  winstgevend  doel,  met  leasingactiviteiten.

autonomes et les associations sans but lucratif, qui  exercent des activités de leasing.

§ 3/3. Voor de motorvoertuigen, bestemd voor het  vervoer van goederen, de lijkwagens, de alleenrijdende  landbouwtractoren en de alleenrijdende trekkers, als het  andere voertuigen zijn dan de voertuigen, vermeld in  paragraaf 6, die voor de eerste keer na 31 december 2020  worden ingeschreven in het repertorium van het  Directoraat-generaal Mobiliteit en Verkeersveiligheid en  waarvan de maximaal toegelaten massa maximum 2500  kilogram bedraagt, wordt de belasting berekend als  vermeld in paragraaf 3/1, met dien verstande dat het  element, vermeld onder paragraaf 3/1, 1°, als volgt wordt  toegepast: in functie van de CO 2 -uitstoot van het  voertuig, gemeten tijdens de homologatie ervan volgens  de geldende Europese regelgeving, wordt het tarief:

§ 3/3. Pour les véhicules à moteur, destinés au transport  de marchandises, les corbillards, les tracteurs agricoles à  moteur solos et les tracteurs à moteur solos, autres que  ceux, visés au paragraphe 6, qui sont inscrits pour la  première fois après le 31 décembre 2020 au répertoire de  la Direction générale Mobilité et Sécurité routière, et  dont la masse maximale autorisée s'élève à 2500 kg au  maximum, la taxe est calculée telle que visée au  paragraphe 3/1, étant entendu que l'élément visé au  paragraphe 3/1, 1°, est appliqué comme suit : en fonction  de l'émission de CO 2 du véhicule, mesuré lors de son  homologation selon la réglementation européenne en  vigueur, le tarif est :

a) vermeerderd met 0,30% voor iedere gram CO 2 - uitstoot per kilometer boven 149 gram en niet hoger dan  500 gram;

a) majoré de 0,30% par gramme d'émission de CO 2 par  kilomètre au-dessus de 149 grammes et en-dessous de  500 grammes ;

Deze paragraaf is alleen van toepassing op voertuigen  van natuurlijke personen en van andere rechtspersonen  dan vennootschappen, autonome overheidsbedrijven en  verenigingen zonder winstgevend doel, met  leasingactiviteiten.

Deze paragraaf is ook van toepassing op de  motorvoertuigen, vermeld in het eerste lid, die voor de  eerste keer na 31 december 2020 worden in- geschreven  bij een vergelijkbare instelling binnen de Europese  Economische Ruimte of een andere staat, wanneer zij  nadien worden ingeschreven in het repertorium van het  Directoraat-generaal Mobiliteit en Verkeersveiligheid.

§ 4. Voor de motorfietsen bedraagt de belasting 49,44  euro.

§ 5 Voor de autobussen en de autocars bedraagt de  belasting 4,44 euro per fiscale paardenkracht als het  belastbaar vermogen 10 fiscale paardenkracht niet te  boven gaat, met een minimum van 69,94 euro.

Lorsque la puissance imposable est supérieure à 10  chevaux fiscaux, la taxe pour les autobus et les autocars  est calculée, sur la base des chevaux fiscaux (ch), selon  le tableau suivant :

Als het belastbaar vermogen 10 fiscale paardenkracht te  boven gaat, wordt de belasting voor de autobussen en de  autocars berekend, op basis van fiscale paardenkracht  (pk), volgens de volgende tabel :

aantal pk

/  montant total de la taxe en euros  11  51,48  12  59,04  13  67,08  14  75,60  15  84,60  16  94,08  17  104,04  18  114,48  19  125,40  20  136,80  21  148,68  22  161,04  23  173,88  24  187,20  25  201,00  26  215,28  27  230,04  28  245,28  29  261,00  30  277,20  31  293,88  32  311,04  33  328,68

/  nombre de ch

/  plus de 44  549,12 majoré de 12,48 par ch supérieur à 44

§ 6. Voor de motorvoertuigen of de samengestelde  voertuigen, bestemd voor het vervoer van goederen,  waarvan het maximaal toegestane totaalgewicht 3,5 ton  overschrijdt, maar minder bedraagt dan 12 ton, bedraagt  de belasting 0 euro.

Voor de motorvoertuigen of de samengestelde  voertuigen, bestemd voor het vervoer van goederen,  waarvan het maximaal toegestane totaalgewicht 12 ton  of meer bedraagt, wordt de belasting, afhankelijk van het  aantal assen van het voertuig en de aard van de  ophanging, berekend volgens de volgende bepalingen en  tabellen :

1° voor de alleenrijdende motorvoertuigen is het in  aanmerking  te  nemen  maximaal  toegestane  totaalgewicht  (MTT)  voor  de  toepassing  van  onderstaande tabel het eigen maximaal toegestane  totaalgewicht van het motorvoertuig;

MOTORVOERTUIGEN  VEHICULES A MOTEUR

aantal assen en MTT (in ton)

/  nombre d'essieux et MMA (en tonnes)

gelijk aan of meer dan

/  égale à ou supérieur à

2 assen / 2 essieux  12  13  0  31  13  14  31  86  14  15  86  121  15  121  274  3 assen / 3 essieux

(*) Als gelijkwaardig erkende vering volgens de definitie in bijlage II bij richtlijn 96/53/EG van de Raad van 25 juli

1996 houdende vaststelling, voor bepaalde aan het verkeer binnen de Gemeenschap deelnemende wegvoertuigen,

van de in het nationale en internationale verkeer maximaal toegestane afmetingen, en van de in het internationale

verkeer toegestane gewichten (PB L 235 van 17.9.1996, blz. 59).

/  (*) Suspension reconnue équivalente selon la définition dans l'annexe II à la directive 96/53/CE du Conseil du 25

juillet 1996 fixant, pour certains véhicules routiers circulant dans la Communauté les dimensions maximales  autorisées en trafic national et international et les poids maximaux autorisés en trafic international (JO L 235 du

2° voor de samengestelde voertuigen is het in  aanmerking  te  nemen  maximaal  toegestane  totaalgewicht  (MTT)  voor  de  toepassing  van  onderstaande tabel de som van het eigen maximaal  toegestane totaalgewicht van de voertuigen die deel  uitmaken van het samenstel.

COMBINATIES (GELEDE VOERTUIGEN EN

ENSEMBLES)

SAMENSTELLEN)

aantal assen en MTT (in ton)

/  nombre d'essieux et MMA (en tonnes)

Gelijk aan of meer dan

/  égal ou supérieur à

2 + 1 assen / 2 + 1 essieux  12  14  0  0  14  16  0  0  16  18  0  14  18  20  14  32  20  22  32  75  22  23  75  97  23  25  97  175  25  175  307  2 + 2 assen / 2 + 2 essieux  23  25  30  70

d'essieux et de la MMA que les combinaisons précitées  0  16  0  0  16  18  0  14  18  20  14  32  20  22  32  75  22  23  75  97  23  25  97  175  25  29  175  307  29  31  204  335  31  33  335  465  33    465  706  (*) Als gelijkwaardig erkende vering volgens de definitie in bijlage II bij richtlijn 96/53/EG van de Raad van 25 juli  1996 houdende vaststelling, voor bepaalde aan het verkeer binnen de Gemeenschap deelnemende wegvoertuigen, van

de in het nationale en internationale verkeer maximaal toegestane afmetingen, en van de in het internationale verkeer

toegestane gewichten (PB L 235 van 17.9.1996, blz. 59).

/  (*) Suspension reconnue équivalente selon la définition de l'annexe II à la directive 96/53/CE du Conseil du 25

juillet 1996 fixant, pour certains véhicules routiers circulant dans la Communauté les dimensions maximales  autorisées en trafic national et international et les poids maximaux autorisés en trafic international (JO L 235 du

17.9.1996, p. 59).

De bedragen, vermeld in de tabellen in het tweede lid,  omvatten reeds de opdeciem, vermeld in artikel  2.2.4.0.5, § 2, eerste lid.

Dans les montants visés aux tableaux dans l'alinéa deux,  sont déjà inclus le décime additionnel, visé à l'article  2.2.4.0.5, § 2, alinéa premier

§ 7. De aanhangwagens en de opleggers zijn  onderworpen aan een belasting van respectievelijk 32,64  euro of 67,80 euro, naargelang het maximaal toegestane  totaalgewicht niet hoger is dan 500 kg, of 501 kg bereikt  zonder 3500 kg te overschrijden.

§ 7. Les remorques et semi-remorques sont soumises à  une taxe s'élevant respectivement à 32,64 euros ou 67,80  euros, selon que le poids total autorisé en charge n'est  pas supérieure à 500 kg ou atteint 501 kg sans dépasser  3500 kilogrammes.

§ 8. Pour les camping-cars, la taxe est calculée selon le  tableau suivant :

§ 8. Voor de kampeerwagens wordt de belasting  berekend volgens de volgende tabel :

MTT in kg / PTAC en kg  totaalbedrag van de belasting in euro

/  montant total de la taxe en euros  van / de  tot en met / à

0  1500  84  1501  3500  120  3501  7999  132  8000  10.999  168  11.000  > 11.000  264

Deze bepaling is alleen van toepassing op natuurlijke  personen  en  andere  rechtspersonen  dan  vennootschappen, autonome overheidsbedrijven en

Cette disposition s'applique uniquement à des personnes  physiques et des personnes morales autres que des  sociétés, des entreprises publiques autonomes et des  verenigingen  zonder  winstgevend  doel,  met  leasingactiviteiten.

De kampeerwagens vallen buiten de toepassing van  artikel 2.2.6.0.1, § 1, eerste lid, 13°, en artikel 2.2.6.0.1,  § 2, 2°.

§ 9. Voor alle voertuigen als vermeld in dit artikel, met  uitzondering van deze, vermeld in paragraaf 4 en  paragraaf 6, die uitsluitend aangedreven worden door  een elektrische motor of door waterstof en die na 31  december 2025 worden ingeschreven in het repertorium  van het Directoraat-generaal Mobiliteit en  Verkeersveiligheid, bedraagt de belasting 93,60 euro.

Deze bepaling geldt voor voertuigen van:  Cette disposition s'applique aux véhicules :

1° vennootschappen, autonome overheidsbedrijven en  verenigingen zonder winstgevend doel, met  leasingactiviteiten;

2° natuurlijke personen en rechtspersonen, andere dan  deze, vermeld in punt 1°.

---- historiek ----  ---- historique ----

- gewijzigd door art. 5 van het decreet van 09.12.2022  (B.S., 20.12.2022). Inwerkingtreding vanaf aanslagjaar  2023

- gewijzigd door art. 54 van het decreet van 18.12.2020  (B.S., 30.12.2020). Inwerkingtreding: 01.01.2021

- gewijzigd door art. 11 van het decreet van 08.12.2017  (B.S. : 14.12.2017). Tekst in werking getreden op  24.12.2017

- gewijzigd door art. 3 van het decreet van 16 juni 2017  (B.S. : 04.07.2017). Tekst in werking getreden op de  belastbare tijdperken die starten vanaf 1 juli 2017

- paragraaf 6 vervangen door art. 12 van het decreet van  3 juli 2015 (B.S., 10.08.2015). De tekst treedt in werking  op 1 april 2016 (besluit van de Vlaamse Regering van 17  juli 2015 - B.S., 10.08.2015 - art. 4)

- paragraaf 2/1 werd toegevoegd door art. 106 van het  decreet van 18 dec. 2015 (B.S., 29.12.2015). De tekst

treedt in werking vanaf 1 januari 2016 (art. 135)

###### Art. 2.2.4.0.2.  Art. 2.2.4.0.2.

§ 1. In afwijking van artikel 2.2.4.0.1, § 1, § 2, § 2/1, §  2/2, § 3, § 3/1, § 3/2, § 3/3, § 5, § 6, § 7 en § 8,  bedraagt de belasting:

1° 90,90 euro voor de voertuigen die bij het ontstaan van  de belastingplicht sinds meer dan dertig jaar in het  verkeer zijn gebracht;

1/1° (...)  1/1° (...)

2° 31,61 euro voor de kampeeraanhangwagens en de  aanhangwagens die speciaal zijn ontworpen voor het  vervoer van één boot

2° 31,61 euros pour les remorques de camping et les  remorques spécialement conçues pour le transport d'un  seul bateau  ;  3° (…).  3° (…)

###### Art. 2.2.6.0. 3, eerste lid, artikel 2.2.6.0.4, artikel

3.3.2.0.1 en artikel 3.4.7.0.3 zijn niet van toepassing op  de belasting, vermeld in het eerste lid.

§ 2. Als de belastingplichtige belasting voor een voertuig  is verschuldigd, mag de belasting voor dat voertuig niet  minder dan 31,61 euro bedragen.

Deze paragraaf is niet van toepassing op de voertuigen,  vermeld in artikel 2.2.4.0.1, § 6.

- gewijzigd door art. 5 van het decreet van 03.04.2026  (M.B. 23.04.2026). Inwerkingtreding: 03.05.2026

- gewijzigd door art. 6 van het decreet van  09.12.2022 (B.S., 20.12.2022). Inwerkingtreding vanaf  aanslagjaar 2023

- gewijzigd door art. 7 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- gewijzigd door art. 4 van het decreet van 16 juni 2017  (B.S. : 04.07.2017). Tekst in werking getreden op de  belastbare tijdperken die starten vanaf 1 juli 2017

- §2, tweede lid werd toegevoegd door art. 127 van het  decreet van 18 dec. 2015 (B.S., 29.12.2015). De tekst

treedt in werking op 1 april 2016 (art. 135)

Art 2.2.4.0.3.  Art 2.2.4.0.3.

De belasting, vastgesteld volgens artikel 2.2.4.0.1, § 2 ,  § 3 voor zover het voertuigen betreft van natuurlijke  personen  en  van  andere  rechtspersonen  dan  vennootschappen, autonome overheidsbedrijven en  verenigingen  zonder  winstgevend  doel,  met  leasingactiviteiten, § 3/1, eerste lid, § 3/2, eerste lid, en  § 4, de minimumbelastingen, vermeld in artikel  2.2.4.0.1, § 2/1, tweede lid, artikel 2.2.4.0.1, § 3/1,  tweede lid, artikel 2.2.4.0.1, § 3/2, derde lid, en artikel  2.2.4.0.1, § 5, de belastingen, vermeld in artikel  2.2.4.0.1, § 7 en artikel 2.2.4.0.1, § 9, alsook de  belasting, vermeld in artikel 2.2.4.0.2, § 1, en de  minimumbelasting, vermeld in artikel 2.2.4.0.2, § 2,  alsook het bedrag, vermeld in artikel 2.2.5.0.4, zijn  gekoppeld aan de schommelingen van het algemeen  indexcijfer van de consumptieprijzen van het Rijk. De  belastingbedragen worden aangepast op 1 juli van elk  jaar op grond van de schommelingen van het algemeen  indexcijfer van de consumptieprijzen van het Rijk,  vastgesteld tussen de maand mei van het vorige jaar en  de  maand  mei  van  het  lopende  jaar.  De  belastingbedragen, vermeld in artikel 2.2.4.0.1, met  uitzondering van paragraaf 2/1, § 3 voor zover het  voertuigen betreft van natuurlijke personen en van  andere rechtspersonen dan vennootschappen, autonome  overheidsbedrijven en verenigingen zonder winstgevend  doel, met leasingactiviteiten, § 3/1 en § 3/2, en artikel  2.2.4.0.2, § 1, eerste lid, 2°, en § 2, zijn de bedragen die  van toepassing waren op 1 juli 2013. Voor de toepassing  van de indexatie zijn de bedragen, vermeld in artikel  2.2.4.0.1, § 2/1, tweede lid, en artikel 2.2.5.0.4, de  bedragen die gelden alsof ze van toepassing waren op  1 juli 2015. Voor de toepassing van de indexatie zijn  de bedragen, vermeld in artikel 2.2.4.0.2, § 1, eerste lid,

De aangepaste belastingbedragen, vermeld in het eerste  lid, kunnen met maximaal 0,11 euro worden verlaagd  om een veelvoud van twaalf te vormen.

---- historiek ----  ---- historique ----

- gewijzigd door art. 6 van het decreet van 03.04.2026  (M.B. 23.04.2026). Inwerkingtreding: 03.05.2026

- gewijzigd door art. 36 van het decreet van 19.12.2025  (B.S. 30.12.2025). Inwerkingtreding: 01.01.2026

- gewijzigd door art. 7 van het decreet van 09.12.2022  (B.S. 20.12.2022). Inwerkingtreding: 30.12.2022

- gewijzigd door art. 5 van het decreet van 16 juni 2017  (B.S. : 04.07.2017). Tekst in werking getreden op de  belastbare tijdperken die starten vanaf 1 juli 2017

- eerste lid werd vervangen door art. 107 van het decreet  van 18 dec. 2015 (B.S., 29.12.2015). De tekst

treedt in werking vanaf 1 januari 2016 (art. 135)

###### Art. 2.2.4.0.4.  Art. 2.2.4.0.4.

De personenauto's, de auto's voor dubbel gebruik en de  minibussen, met inbegrip van de lichte vrachtauto's,  vermeld in artikel 1.1.0.0.2, derde lid, 2°, laatste zin,  waarvan de motor, zelfs gedeeltelijk of tijdelijk,  gedreven wordt met vloeibaar petroleumgas of andere  vloeibare koolwaterstofgassen, zijn onderworpen aan  een aanvullende verkeersbelasting van 89,16 euro,  148,68 euro of 208,20 euro, naargelang het belastbaar  vermogen niet hoger is dan 7 pk, 8 pk bereikt zonder 13  pk te overschrijden of meer bedraagt dan 13 pk.

De aanvullende verkeersbelasting, vermeld in het eerste  lid, wordt geregeld volgens de bepalingen die van  toepassing  zijn  op  de  verkeersbelasting,  met  uitzondering van de bepalingen van artikel 2.2.4.0.2, §  2, artikel 2.2.4.0.3, artikel 2.2.4.0.5, § 2, artikel 2.2.5.0.2  en artikel 2.2.6.0.1, § 1, eerste lid, 3°, 4°, 5°, 7°, 8°, 9°,  11° en 15°.

---- historiek ----  ---- historique ----

- gewijzigd door art. 59 van het decreet van 26.06.2020  (B.S. 17.07.2020). Tekst treedt in werking op 01.10.2020

###### Art. 2.2.4.0.5.  Art. 2.2.4.0.5.  § 1. Overeenkomstig artikel 42 van het federale  Wetboek van 23 november 1965 van de met  inkomstenbelastingen gelijkgestelde belastingen, zijn de  provincies, de agglomeraties en de gemeenten niet  gemachtigd tot het heffen van opcentiemen op de  verkeersbelasting  of  enigerlei  belasting  op  de  voertuigen, vermeld in artikel 2.2.1.0.1, behoudens wat  betreft de vaartuigen, de bootjes, de bromfietsen en de  motorfietsen respectievelijk bedoeld in artikel 2.2.6.0.1,  § 1, eerste lid, 6° en 10°.

§ 2. In afwijking van paragraaf 1 wordt voor de  gemeenten  een  opdeciem  geheven  op  de  verkeersbelasting  die  het  Vlaamse  Gewest  op  autovoertuigen heft.

Als de gemeente deel uitmaakt van een agglomeratie van  gemeenten, wordt 20 % van de opbrengst van die  opdeciem  toegekend  aan  de  agglomeratie  van  gemeenten.

§ 3. In afwijking van paragraaf 2 wordt de opdeciem niet  toegepast op de belasting op:

1° voertuigen die uitsluitend gebruikt worden voor  bezoldigd vervoer van personen krachtens een  machtiging  uitgereikt  voor  de  exploitatie  van  autocardiensten, ter uitvoering van de besluitwet van 30  december 1946 betreffende het bezoldigd vervoer van  personen over de weg met autobussen en met autocars;

2° (…)  2° (…)

---- historiek ----  ---- historique ----

- gewijzigd door art. 8 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

Als de euronorm van het voertuig niet bekend is, wordt  die parameter voor de toepassing van artikel 2.2.4.0.1, §  2/1, eerste lid, 2°, artikel 2.2.4.0.1, § 3/1 en § 3/2,  bepaald aan de hand van de datum van de eerste  inschrijving van het voertuig, vermeld in de volgende  tabel:

Datum van de eerste inschrijving van het voertuig in het

binnenland of in het buitenland

/  Date de première inscription du véhicule en Belgique ou

à l'étranger

tot en met 31 december 1993

/  jusqu'au 31 décembre 1993 inclus

vanaf 1 januari 1994 tot en met 31 december 1996

/  du 1er janvier 1994 au 31 décembre 1996 inclus

vanaf 1 januari 1997 tot en met 31 december 2000

/  du 1er janvier 1997 au 31 décembre 2000 inclus

vanaf 1 januari 2001 tot en met 31 december 2005

/  du 1 janvier 2001 au 31 décembre 2005 inclus

vanaf 1 januari 2006 tot en met 31 december 2010

/  du 1er janvier 2006 au 31 décembre 2010 inclus

vanaf 1 januari 2011 tot en met 31 augustus 2015

/  du 1er janvier 2011 au 31 août 2015 inclus

vanaf 1 september 2015

/  à partir du 1er septembre 2015

---- historiek ----  ---- historique ----

- gewijzigd door art. 6 van het decreet van 16 juni 2017  (B.S. : 04.07.2017). Tekst in werking getreden op de  belastbare tijdperken die starten vanaf 1 juli 2017

- toegevoegd door art. 108 van het decreet van 18 dec.  2015 (B.S., 29.12.2015). De tekst is in werking getreden  op 1 januari 2016 (art. 135)

###### Art. 2.2.4.0.7.  Art. 2.2.4.0.7.

§ 1. Als de CO2-uitstoot van het voertuig niet bekend is,  wordt die parameter voor de toepassing van artikel  2.2.4.0.1, § 2/1, eerste lid, 1°, artikel 2.2.4.0.1, § 3/1,  bepaald aan de hand van de brandstofsoort, de  cilinderinhoud en de euronorm, vermeld in de volgende  tabel:

Brandstofsoort

Cilinderinhoud in cc

Euronorm

/  Type de carburant

/  Cylindrée en cc

/  Euronorme  6  5  4  3  2  1  0  Emissions de CO2 en g/km

minder dan 1 400

Benzine en andere

/  moins de 1 400

117  125  140  150  164  173  175

branstoffen, met  uitzondering van aardgas

1 400 tot en met 2 000

en diesel

/  1 400 jusqu'à 2 000

150  159  172  185  200  211  213

/  Essence et autres  carburants, à l'exception  de gaz naturel et du diesel

meer dan 2 000

/  plus de 2 000

228  238  247  259  279  295  297

minder dan 1 400

/  moins de 1 400

98  103  120  116  125  132  133

1 400 tot en met 2 000

/  1 400 jusqu'à 2 000

Diesel

117  125  144  151  163  173  174

meer dan 2 000

/  plus de 2 000

159  169  201  199  214  226  228

minder dan 1 400

/  moins de 1 400

94  100  112  120  131  139  140

Aardgas

1 400 tot en met 2 000

/  Gaz naturel

/  1 400 jusqu'à 2 000

120  127  138  148  160  169  171

meer dan 2 000

/  plus de 2 000

182  190  198  207  223  236  238

§ 2. Als de CO2-uitstoot van het voertuig niet bekend is,  wordt die parameter voor de toepassing van artikel  2.2.4.0.1, § 2/2 en artikel 2.2.4.0.1, § 3/3, bepaald  volgens volgende formule:

§ 2. Si les émissions de CO2 du véhicule ne sont pas  connues, ce paramètre est déterminé selon la formule  suivante aux fins de l'article 2.2.4.0.1, § 2/2 et de l'article  2.2.4.0.1, § 3/3 :

CO2-uitstoot = Constante + (Parameter_CC x CC) +  (Parameter_KW x KW) + (Parameter_FPK x FPK) +  (Parameter_ZP x ZP) + (Parameter_CC_KW x CC x  KW) + (Parameter_CC_FPK x CC x FPK) +  (Parameter_KW_FPK  x  KW  x  FPK)  +  (Parameter_CC_KW_FPK x CC x KW x FPK).

émission CO2 = Constante + (Paramètre_CC x CC) +  (Paramètre_KW x KW) + (Paramètre_FPK x FPK) +  (Paramètre_ZP x ZP) + (Paramètre_CC_KW x CC x  KW) + (Paramètre_CC_FPK x CC x FPK) +  (Paramètre_KW_FPK  x  KW  x  FPK)  +  (Paramètre_CC_KW_FPK x CC x KW x FPK).

De parameters, vermeld in het eerste lid, worden  gedefinieerd als volgt:

Les paramètres figurant à l'alinéa 1er sont définis  comme suit :

1° CC = de cilinderinhoud in cc gedeeld door 1000;  1° CC = cylindrée en cc divisée par 1 000 ;

2° KW = het vermogen van de motor uitgedrukt in  kilowatt gedeeld door 100;

2° KW = puissance du moteur exprimée en kilowatts  divisée par 100 ;

4° ZP = het aantal zitplaatsen.  4° ZP = nombre de sièges.

De overige parameters, vermeld in het eerste lid, worden  voor de toepassing van deze formule, bepaald aan de  hand van de brandstofsoort, vermeld in de volgende  tabel:

Aux fins de la formule précitée, les autres paramètres  figurant à l'alinéa 1er sont déterminés en fonction du  type de carburant, selon le tableau suivant :

Benzine en

andere  brandstoffen,

met  uitzondering  van aardgas,

diesel en

Benzine plug-

Diesel plug-

plug- inhybride /

inhybride /

inhybride /

Aardgas /  Gaz naturel

Diesel

Hybride  rechargeable

Hybride  rechargeable

Essence et

autres  carburants, à  l'exception du

essence

diesel

gaz naturel,

du diesel et  de l'hybride  rechargeable

Parameter  constante /

58.3304  1017.5710  75.3124  1716.4604  7627.0345

Paramètre

constante

Parameter_CC

/  Paramètre_CC

2.9316  -403.6269  -126.9417  -102.5352  -8617.6901

Parameter_KW

/  Paramètre_KW

53.6921  -817.4980  56.3978  -1333.5261  -8710.9573

Parameter_FPK

/  Paramètre_FPK

5.0617  -96.0669  27.1787  -229.5888  -606.3489

Parameter_ZP /

Paramètre_ZP  1.9861  1.9861  1.9861  1.9861  1.9861

Parameter_CC_

KW /  Paramètre_CC_

17.2267  399.2770  -51.8607  -344.2686  8134.2581

KW

Parameter_CC_

FPK /  Paramètre_CC_

-0.2578  41.8433  -1.0233  51.2497  817.4474

FPK

Parameter_  KW_FPK /  -5.4089  76.3656  -2.7148  245.7955  905.1812

KW_FPK

Parameter_CC_

KW_FPK /  Paramètre_CC_

0.1784  -34.3605  3.1869  -30.2220  -854.6351

KW_FPK

De CO2-uitstoot, zoals berekend in het eerste lid, is  minstens gelijk aan nul.

Een plug-inhybride voertuig is een voertuig dat  aangedreven wordt door een elektrische motor en een  verbrandingsmotor waarvoor de energie geleverd wordt  aan de elektrische motor door batterijen die volledig  opgeladen kunnen worden via een aansluiting aan een  externe energiebron buiten het voertuig.

Een voertuig op aardgas is een voertuig waarvan de  motor, ook al is het maar gedeeltelijk of tijdelijk,  aangedreven wordt met aardgas.

---- historiek ----  ---- historique ----

- gewijzigd door art. 7 van het decreet van 03.04.2026  (M.B. 23.04.2026). Inwerkingtreding: 03.05.2026

- gewijzigd door art. 38 van het decreet van 30.06.2023  (B.S., 29.08.2023). Tekst in werking getreden vanaf  01.01.2021

- gewijzigd door art. 7 van het decreet van 16 juni 2017  (B.S. : 04.07.2017). Tekst in werking getreden op de  belastbare tijdperken die starten vanaf 1 juli 2017

- toegevoegd door art. 109 van het decreet van 18 dec.  2015 (B.S., 29.12.2015). De tekst is in werking getreden  op 1 januari 2016 (art. 135

###### Art. 2.2.4.0.8.  Art. 2.2.4.0.8.

De aanwezigheid van een roetfilter als vermeld in artikel  2.2.4.0.1, § 2/1, eerste lid, 2°, artikel 2.2.4.0.1, § 3/1 en  § 3/2, wordt vastgesteld op basis van de PM-gegevens  of op basis van de gegevens over de premie voor de  aankoop en installatie van emissieverminderende  voorzieningen in voertuigen met een dieselmotor. Onder  PM wordt verstaan: de uitstoot van deeltjes, gemeten  tijdens de homologatie van het voertuig volgens de  geldende Europese regelgeving.

Een roetfilter als vermeld in artikel 2.2.4.0.1, § 2/1,  eerste lid, 2°, artikel 2.2.4.0.1, § 3/1 en § 3/2, is een  halfopen of een gesloten roetfilter.

Een halfopen roetfilter wordt geacht aanwezig te zijn bij  voertuigen als de premie-aanvraag voor de aankoop en  installatie van de roetfilter door de Vlaamse overheid is  goedgekeurd.

---- historiek ----  ---- historique ----

-gewijzigd door art. 8 van het decreet van 16 juni 2017  (B.S. : 04.07.2017). Tekst in werking getreden op de  belastbare tijdperken die starten vanaf 1 juli 2017

- toegevoegd door art. 110 van het decreet van 18 dec.

2015 (B.S., 29.12.2015). De tekst is in werking getreden  op 1 januari 2016 (art. 135))

###### Art. 2.2.4.0.9.  Art. 2.2.4.0.9.

De belasting voor de personenauto's, de auto's voor  dubbel gebruik en de minibussen, vermeld in artikel  2.2.4.0.1, § 2/1, wordt berekend op basis van de  bepalingen van dit hoofdstuk zoals deze van toepassing  waren vóór 1 januari 2016, meer bepaald wat betreft de  tarieven, vermeld in deze afdeling, de verminderingen,  vermeld in afdeling 5, en de vrijstellingen, vermeld in  afdeling 6.

Op straffe van verval wordt aan de volgende  voorwaarden voldaan:

1° het wegvoertuig werd vóór 31 oktober 2015 besteld;  1° le véhicule routier a été commandé avant le 31  octobre 2015 ;

2° het wegvoertuig wordt na 31 december 2015 voor de  eerste keer ingeschreven in het repertorium van het  Directoraat-generaal Mobiliteit en Verkeersveiligheid;

3° een kopie van de bestelbon wordt aan de bevoegde  entiteit van de Vlaamse administratie bezorgd vóór 15  januari 2016, samen met een formulier, afgeleverd door  deze entiteit, dat wordt ondertekend door de betrokken  belastingplichtige, en dat minstens de volgende  gegevens bevat:

b) de voornamen, de achternaam en het domicilieadres  van de natuurlijke persoon of de naam, de rechtsvorm en  het adres van de zetel van de rechtspersoon op wiens  naam  het  voertuig ingeschreven  werd  of  zal  ingeschreven worden in het repertorium van het   Directoraat-generaal  Mobiliteit  en  Verkeersveiligheid.

---- historiek ----  ---- historique ----

- gewijzigd door art. 9 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- toegevoegd door art. 111 van het decreet van 18 dec.  2015 (B.S., 29.12.2015). De tekst is in werking getreden  op 1 januari 2016 (art. 135)

#### Afdeling 5 - Verminderingen  Section 5 – Réductions

###### Art. 2.2.5.0.1.  Art. 2.2.5.0.1.  De belasting wordt verminderd met 25 % voor elk  voertuig dat uitsluitend wordt gebruikt voor het  bezoldigd vervoer van personen krachtens een  machtiging  uitgereikt  voor  de  exploitatie  van  autocardiensten, ter uitvoering van de besluitwet van 30  december 1946 betreffende het bezoldigd vervoer van  personen over de weg met autobussen en met autocars,  dat bij het ontstaan van de belastingplicht sedert ten  minste vijf jaar in het verkeer is gebracht. De datum  waarop het voertuig voor het eerst in het verkeer is  gebracht, is die welke op het inschrijvingsbewijs van het  voertuig is vermeld.

De vermindering, vermeld in het eerste lid, wordt ook  verleend voor aanhangwagens die uitsluitend worden  getrokken door voertuigen als vermeld in het eerste lid.

###### Art. 2.2.5.0.2.  Art. 2.2.5.0.2.

(…)  (…)

---- historiek ----  ---- historique ----

###### Art. 2.2.5.0.3.  Art. 2.2.5.0.3.

De belasting wordt met 10 % verminderd als ze is  verschuldigd krachtens een regelmatige aangifte,  ingediend door een belastingplichtige die op 1 januari  van het aanslagjaar, en dit tot minstens 30 juni drie of  meer motorvoertuigen aangeeft die zijn geïnvesteerd in  een handels- of nijverheidsbedrijf en die uitsluitend  worden gebruikt voor het bezoldigd vervoer van  personen krachtens een machtiging uitgereikt voor de  exploitatie van autocardiensten, ter uitvoering van de  besluitwet van 30 december 1946 betreffende het  bezoldigd vervoer van personen over de weg met  autobussen en met autocars.

(…)  (…)

---- historiek ----  ---- historique ----

- gewijzigd door art. 10 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

###### Art. 2.2.5.0.4.  Art. 2.2.5.0.4.

Voor de voertuigen waarvan de motor, ook al is het maar  gedeeltelijk of tijdelijk, aangedreven wordt met  vloeibaar  petroleumgas  of  andere  vloeibare  koolwaterstofgassen, wordt de belasting verminderd  met 100 euro, in voorkomend geval beperkt tot het  bedrag van de belasting als berekend overeenkomstig  artikel 2.2.4.0.1 tot en met 2.2.4.0.3, maar zonder  toepassing van de minimumbelastingen, vermeld in  artikel 2.2.4.0.1, § 2/1, tweede lid, en § 5, en in artikel  2.2.4.0.2, § 2.

Dit artikel is alleen van toepassing op wegvoertuigen, de  lichte vrachtauto’s, vermeld in artikel 1.1.0.0.2, derde  lid, 2°, laatste zin, lijkwagens, en alleenrijdende  trekkers, als het andere voertuigen zijn dan de  voertuigen, vermeld in artikel 2.2.4.0.1, § 6, van  natuurlijke personen en andere rechtspersonen dan  vennootschappen, autonome overheidsbedrijven en  verenigingen  zonder  winstgevend  doel,  met  leasingactiviteiten.

---- historiek ----  ---- historique ----

- gewijzigd door art. 9 van het decreet van 16 juni 2017  (B.S. : 04.07.2017). Tekst in werking getreden op de  belastbare tijdperken die starten vanaf 1 juli 2017

#### Afdeling 6 - Vrijstellingen  Section 6 – Exonérations

###### Art. 2.2.6.0.1.  Art. 2.2.6.0.1.

§ 1. Met uitzondering van de motorvoertuigen en van de  samengestelde voertuigen gebruikt voor het vervoer van  goederen over de weg met het maximaal toegestane  totaalgewicht van minstens twaalf ton, wordt er een  vrijstelling van de belasting verleend voor :

1° de voertuigen die uitsluitend gebruikt worden voor  een openbare dienst van de staat, de gemeenschappen,  de gewesten, de provincies, de agglomeraties, de  federaties van gemeenten of de gemeenten;

2° de voertuigen die uitsluitend gebruikt worden voor  gemeenschappelijk vervoer van personen krachtens

a) een machtiging uitgereikt voor de exploitatie van  openbare  autobusdiensten  of  van  bijzondere  autobusdiensten, ter uitvoering van de besluitwet van 30  december 1946 betreffende het bezoldigd vervoer van  personen over de weg met autobussen en met autocars

b) een machtiging afgeleverd ter uitvoering van het  decreet van 20 april 2001 betreffende de organisatie van  het personenvervoer over de weg of een vergunning  afgeleverd ter uitvoering van het decreet van 29 maart  2019  betreffende  het  individuele  bezoldigd  personenvervoer;

c) een concessie van de openbare machten;  c) d'une concession des pouvoirs publics ;

3° de ziekenauto's die uitsluitend worden gebruikt voor  het vervoer van gewonden en zieken;

4° de personenauto's die als persoonlijk vervoermiddel  worden gebruikt door grootoorlogsinvaliden of door  personen met een handicap;

4° aux voitures particulières employées comme moyen  de transport personnel par des grands invalides de guerre  ou par des personnes handicapées ;  5° de voertuigen die uitsluitend op proef worden  gebruikt door de fabrikanten of handelaars of door hun  bedienden;

6° de vaartuigen en bootjes;  6° aux bateaux et embarcations ;

8° (…);  8° (…) ;

9° (…);  9° (…) ;

10° de bromfietsen en de motorfietsen voorzien van een  motor met een cilinderinhoud van maximaal 250  kubieke centimeter;

11° de autovoertuigen die uitsluitend aangewend  worden voor een taxidienst of voor verhuring met  bestuurder;

12° de autovoertuigen die gebruikt worden door een  Belgische verblijfhouder en ter beschikking zijn gesteld  van hem door zijn werkgever die in het buitenland  gevestigd is, en die in het buitenland zijn ingeschreven;

13° de motorvoertuigen en de samengestelde voertuigen  die uitsluitend bestemd zijn voor het goederenvervoer  over de weg, die slechts af en toe op de openbare weg in  België rijden en die worden gebruikt door natuurlijke  personen of rechtspersonen die het goederenvervoer niet  als hoofdactiviteit hebben, als het vervoer met die  voertuigen niet leidt tot concurrentievervalsing;

14° de voertuigen die ingezet worden door vervoerders  die gesubsidieerd zijn door de Vlaamse Regering en die  uitsluitend gebruikt worden voor het vervoer van

15° de voertuigen voorzien van een nationale plaat.  15° aux véhicules munis d'une plaque nationale.

De vrijstelling, vermeld in het eerste lid, 4°, is beperkt  tot één personenauto per begunstigde en is afhankelijk  van de voorlegging aan het bevoegde personeelslid van  :

1° een getuigschrift, uitgereikt door de overheid die het  invaliditeitspensioen  heeft  toegekend,  met  de  vermelding dat de betrokkene de hoedanigheid van  grootoorlogsinvalide heeft en een invaliditeitspensioen  van ten minste 60 % geniet;

2° een invaliditeitsattest, uitgereikt door de FOD Sociale  Zekerheid, met de vermelding dat de betrokkene recht  heeft op vrijstelling van de verkeersbelasting, of dat hij  is getroffen door volledige blindheid of volledige  verlamming van de bovenste ledematen, of dat die  ledematen geamputeerd zijn, of dat hij is aangetast door  een blijvende invaliditeit die rechtstreeks toe te  schrijven is aan de onderste ledematen en ten minste 50  % bedraagt.

De volgende voertuigen komen in aanmerking voor de  toepassing van de vrijstelling, vermeld in het eerste lid,  11° :

1° de autovoertuigen die uitsluitend worden gebruikt  voor taxidiensten onder de voorwaarden, vermeld in het  decreet van 20 april 2001 betreffende de organisatie van  het personenvervoer over de weg of in het decreet van  29 maart 2019 betreffende het individuele bezoldigd  personenvervoer, en die ingericht zijn krachtens een  vergunning die regelmatig afgeleverd is ter uitvoering  van de voormelde decreten;

2° de autovoertuigen die, naar constructie en uitrusting,  geschikt zijn voor het vervoer van ten hoogste negen  personen, de bestuurder inbegrepen, en die, met  uitsluiting van elk ander gebruik, met bestuurder worden  verhuurd om personen te vervoeren, op voorwaarde dat  de duur van elke verhuring niet meer dan één dag  bedraagt en dat de verhuring op het voertuig en niet op  elk van de plaatsen slaat;

3° de autovoertuigen die tegelijk worden gebruikt voor  taxidiensten als vermeld in 1°, en voor verhuring met  bestuurder als vermeld in 2°.

§ 2. Wat betreft de motorvoertuigen en de  samengestelde voertuigen gebruikt voor het vervoer van  goederen over de weg met het maximaal toegestane  totaalgewicht van minstens twaalf ton, wordt er een  vrijstelling van de belasting verleend voor :

2° de motorvoertuigen en de samengestelde voertuigen  die slechts af en toe op de openbare weg in België rijden  en die worden gebruikt door natuurlijke personen of  rechtspersonen die het goederenvervoer niet als  hoofdactiviteit hebben, als het vervoer met die  voertuigen niet leidt tot concurrentievervalsing.

§ 3. De vrijstellingen, vermeld in paragraaf 1, eerste lid,  13°, en paragraaf 2, 2°, kunnen alleen worden verleend  als ze worden aangevraagd voor het begin van het  belastbare tijdperk.

Aan het begrip ‘af en toe’, vermeld in paragraaf 1, eerste  lid, 13°, en paragraaf 2, 2°, is voldaan in al de volgende  gevallen:

1° als het voertuig in kwestie door de aard ervan maar af  en toe gebruikmaakt van de openbare weg. De Vlaamse  Regering bepaalt welke voertuigen hieronder vallen;

2° als het voertuig in kwestie maximaal vijfhonderd  kilometer per kalenderjaar aflegt op de wegen of de  wegsegmenten, vermeld in bijlage 2, die bij dit decreet  is gevoegd, zoals geregistreerd door de elektronische  registratievoorziening, vermeld in artikel 3.3.1.0.13;

3° als het voertuig in kwestie dat niet beschikt over een  elektronische registratievoorziening als vermeld in  artikel 3.3.1.0.13 maximaal dertig dagen op de openbare  weg wordt gebruikt.

De vrijstelling, vermeld in het tweede lid, 3°, kan  worden bewezen door een rittenblad bij te houden dat  moet worden aangevraagd bij de bevoegde entiteit van  de Vlaamse administratie. Het rittenblad moet zich op  elk moment aan boord van het voertuig bevinden.

De geldigheidsduur van een rittenblad is maximaal  twaalf  opeenvolgende  maanden  vanaf  de  aanvangsdatum van het rittenblad. Als het belastbare  tijdperk minder dan twaalf maanden bedraagt, wordt de  geldigheidsduur van het rittenblad overeenkomstig  ingekort.

---- historiek ----  ---- historique ----

- gewijzigd door art. 11 van het decreet van 02.04.2021  (B.S., 15.04.2021). Tekst heeft uitwerking met ingang van  01.01.2020

- gewijzigd door art. 60 van het decreet van 26.06.2020  (B.S. 17.07.2020). Tekst treedt in werking op 01.10.2020

- gewijzigd door art. 9 van het decreet van 22.06.2018.  Tekst in werking getreden vanaf aanslagjaar 2019

- § 1, eerste lid, en § 2, eerste lid gewijzigd door art. 12  van het decreet van 08.12.2017 (B.S. : 14.12.2017). Tekst  in werking getreden op 24.12.2017

###### Art. 2.2.6.0.2.  Art. 2.2.6.0.2.

Er wordt een gehele of gedeeltelijke vrijstelling van de  aanvullende verkeersbelasting verleend aan:

1° de niet-verblijfhouders als, in de staat waar ze verblijf  houden, geen soortgelijke belasting bestaat of als de  Belgische verblijfhouders daarvan vrijgesteld zijn, en  naargelang van die vrijstelling;

2°  de  internationale  organisaties,  hun  vertegenwoordigers, ambtenaren en leden, voor zover ze  vrijgesteld zijn van de verkeersbelasting op de  autovoertuigen,  ingevolge  de  voorrechten  en  immuniteiten  die  aan  hen  toegestaan  zijn  overeenkomstig het internationale recht.

###### Art. 2.2.6.0.3.  Art. 2.2.6.0.3.

Als de voorwaarden tot vrijstelling in de loop van een  aanslagjaar niet meer vervuld zijn, is de belasting  verschuldigd in verhouding tot de niet-verstreken  maanden.

Dit artikel is niet van toepassing op de voertuigen,  vermeld in artikel 2.2.2.0.1, § 2, tweede lid.

De belasting, betaald voor vrachtauto's, tractors,  aanhangwagens en opleggers, wordt terugbetaald als die  voertuigen afstanden afleggen in het kader van  gecombineerd vervoer als vermeld in artikel 1 van  Richtlijn nr. 92/106/EEG van de Raad van 7 december  1992 houdende vaststelling van gemeenschappelijke  voorschriften voor bepaalde vormen van gecombineerd  vervoer van goederen tussen Lid-Staten.

La taxe, payée pour des camions, des tracteurs, des  remorques et des semi-remorques, est remboursée  lorsque ces véhicules effectuent des parcours dans le  cadre d'un transport combiné, tel que visé à l'article 1er  de la Directive n° 92/106/CEE du Conseil du 7  décembre 1992 relative à l'établissement de règles  communes pour certains transports combinés de  marchandises entre Etats membres.  De terugbetaling (T), vermeld in het eerste lid, wordt op  forfaitaire wijze berekend volgens de volgende formule:  T=t*n/100, waarbij:

1° t = het bedrag van de verschuldigde verkeersbelasting  voor het voertuig;

2° n = het antaal overslagverrichtingen tijdens de  belastbare periode waarbij de vrachtwagen, de  aanhandwagen, de oplegger met of zonder trekker, de  wissellaadbak of de container van 20 voet en meer  overschakelt van vervoer per spoor, via zeetraject of via  de binnenwateren naar vervoer over de weg of  omgekeerd. De parameter n mag niet meer dan 100  bedragen.

In het tweede lid wordt verstaan onder:  Dans l'alinéa 2, il faut entendre par :

1° overslagverrichting: het verplaatsen van intermodale  transporteenheden van de ene vervoermodus, namelijk  per spoor, via zeetraject of via de binnenwateren, naar  de andere vervoermodus, namelijk vervoer over de weg,  of omgekeerd, waarbij de verplaatsing plaatsvindt  tussen minstens twee staten van de Europese  Economische Ruimte;

2° wissellaadbak: een vrachtvervoereenheid die aan de  afmetingen van wegvoertuigen is aangepast en die  voorzien is van inrichtingen voor goederenoverslag  tussen verschillende vervoerswijzen, zoals van weg naar  spoor.

De minimumbelasting, vermeld in artikel 2.2.4.0.2, § 2,  is niet van toepassing.

De Vlaamse Regering bepaalt de wijze van de aanvrag  van de terugbetaling, vermeld in het eerste lid.

---- historiek ----  ---- historique ----

- gewijzigd door art. 96 van het decreet van 22.12.2017  (B.S.: 29.12.2017). De tekst is van toepassing vanaf  aanslagjaar 2017

- gewijzigd door art. 2 van het decreet van 23.12.2016  (B.S.: 13.01.2017). De tekst is van toepassing vanaf  aanslagjaar 2016

§ 1. Er wordt een vrijstelling van de belasting verleend  voor de personenauto's, de auto's voor dubbel gebruik,  de minibussen, met inbegrip van de aanhangwagens van  die voertuigen, en de motorfietsen die tijdelijk in België  worden ingevoerd door een natuurlijke persoon die zijn  gewone verblijfplaats in een andere staat van de  Europese Economische Ruimte heeft, en die op het  Belgische grondgebied voor persoonlijk of voor

beroepsmatig gebruik van de invoerder worden  aangewend.

De vrijstelling, vermeld in het eerste lid, wordt ook  verleend aan de natuurlijke personen met gewone  verblijfplaats in een land dat geen deel uitmaakt van de  Europese Economische Ruimte, als in dat land dezelfde  vrijstelling  wordt  toegekend  aan  de  Belgische  verblijfhouders.

§ 2. De vrijstelling, vermeld in paragraaf 1, wordt  verleend voor een al dan niet ononderbroken duur van  niet meer dan zes maanden per tijdvak van twaalf  maanden.

In afwijking van het eerste lid wordt:  Par dérogation à l'alinéa premier :

1° de duur van de vrijstelling op zeven maanden  vastgesteld per tijdvak van twaalf maanden bij  beroepsmatig gebruik van het voertuig door een  tussenpersoon in handel, industrie of ambacht;

2° de duur van de vrijstelling niet in de tijd beperkt als  het voertuig door de invoerder wordt gebruikt voor de  weg die hij in België regelmatig aflegt om zich  uitsluitend van zijn verblijfplaats naar de arbeidsplaats  van de onderneming in België en terug te begeven;

3° de vrijstelling verleend voor de werkelijke duur van  de studies als het voertuig wordt gebruikt door een  student die in België verblijft, met als enig doel er te  studeren.

§ 3. De tijdelijk ingevoerde voertuigen moeten zijn  verkregen of moeten zijn ingevoerd met toepassing van  de algemene belastingregeling voor de binnenlandse  markt van een andere staat en mogen niet wegens de  uitvoer in aanmerking komen voor ontheffing of  teruggave van omzetbelastingen, accijnzen of andere  verbruiksbelastingen.

§ 4. De tijdelijk ingevoerde voertuigen mogen in België  niet worden overgedragen, noch verhuurd, noch  uitgeleend. Bij tijdelijke invoer voor persoonlijk  gebruik, met uitsluiting van het gebruik, vermeld in  paragraaf 2, tweede lid, 2° en 3°, en als ze toebehoren  aan een verhuuronderneming met

§ 4. Les véhicules importés temporairement ne peuvent  être ni cédés, ni loués, ni prêtés en Belgique. En cas  d'importation  temporaire  à  usage  personnel,  à  l'exclusion de l'usage, visé au paragraphe 2, alinéa deux,  2° et 3°, et lorsqu'ils appartiennent à une entreprise de  location ayant son siège à l'étranger, ils peuvent  zetel in het buitenland, kunnen ze aan een niet-  verblijfhouder worden wederverhuurd met het oog op de  wederuitvoer, als ze zich in België bevinden ingevolge  de uitvoering van een huurovereenkomst die hier te  lande is verstreken. De voertuigen mogen ook naar de  staat van de plaats van oorspronkelijke huur worden  teruggebracht  door  een  personeelslid  van  de  verhuuronderneming, zelfs als dat personeelslid zijn  gewone verblijfplaats in België heeft.

§ 5. Als de tijdelijke invoer plaatsvindt voor  beroepsmatig gebruik en voor het gebruik, vermeld in  paragraaf 2, tweede lid, 2° en 3°, moet de voorwaarde,  vermeld in paragraaf 3, vervuld zijn in de staat waarin  de gebruiker zijn gewone verblijfplaats heeft. Die  voorwaarde wordt geacht te zijn vervuld als de  voertuigen voorzien zijn van een gewone nummerplaat  van die staat, met uitzondering van alle tijdelijke  nummerplaten.

Voor voertuigen die ingeschreven zijn in een staat waar  de afgifte van nummerplaten niet verbonden is aan de  inachtneming van de algemene belastingregeling voor  de buitenlandse markt, moeten de gebruikers, met alle  door het gemeen recht toegelaten bewijsmiddelen, met  uitzondering van de eed, bewijzen dat ze de  verbruiksbelastingen hebben betaald.

De voertuigen die voor dezelfde doeleinden worden  ingevoerd, mogen bovendien niet worden gebruikt voor  vervoer van personen tegen betaling of ander materieel  voordeel, of voor om het even welk vervoer van  goederen, al dan niet tegen betaling.

---- historiek ----  ---- historique ----

###### Art. 2.2.6.0.6.  Art. 2.2.6.0.6.

Op voertuigen die uitsluitend aangedreven worden door  een elektrische motor of waterstof en die uiterlijk op 31  december 2025 worden ingeschreven in het repertorium  van  het  Directoraat-generaal  Mobiliteit  en  Verkeersveiligheid wordt geen belasting geheven.

Dit artikel is niet van toepassing op de voertuigen,  vermeld in artikel 2.2.4.0.1, § 6.

De vrijstelling, vermeld in het eerste lid, wordt ook  toegekend voor voertuigen, die na 31 december 2025  ingeschreven worden in het repertorium van het  Directoraat-generaal Mobiliteit en Verkeersveiligheid of  bij een vergelijkbare instelling binnen de Europese  Economische Ruimte of een andere staat en nadien in  het repertorium van het Directoraat-generaal Mobiliteit  en Verkeersveiligheid, en die voldoen aan de volgende  voorwaarden:

1° het voertuig werd vóór 6 oktober 2025 besteld;  1° le véhicule a été commandé avant le 6 octobre 2025 ;

2° een kopie van de bestelbon wordt aan de bevoegde  entiteit van de Vlaamse administratie bezorgd voor 15  januari 2026, samen met een formulier, afgeleverd door  deze entiteit, dat wordt ondertekend door de betrokken  belastingplichtige, en dat minstens de volgende  gegevens bevat:

a) hetzij het identificatienummer uit het Rijksregister  van de natuurlijke personen, hetzij het  ondernemingsnummer dat bekend is bij de  Kruispuntbank van Ondernemingen, hetzij het  identificatienummer, vermeld in artikel 8 van de wet van  15 januari 1990 houdende oprichting en organisatie van  een Kruispuntbank van de sociale zekerheid, van de  persoon op wiens naam het voertuig ingeschreven werd  of zal worden ingeschreven in het repertorium van het  Directoraat-generaal Mobiliteit en Verkeersveiligheid;

b) de voornamen, de achternaam en het domicilieadres  van de natuurlijke persoon of de naam, de rechtsvorm en  het adres van de maatschappelijke zetel van de  rechtspersoon op wiens naam het voertuig ingeschreven  werd of zal ingeschreven worden in het repertorium van  het Directoraat-generaal Mobiliteit en  Verkeersveiligheid.

- gewijzigd door art. 37 van het decreet van 19.12.2025  (B.S. 30.12.2025). Inwerkingtreding: 01.01.2026

- gewijzigd door art. 61 van het decreet van 26.06.2020  (B.S. 17.07.2020). Tekst is van toepassing op de  belastbare tijdperken die starten vanaf 1 juli 2020

- gewijzigd door art. 10 van het decreet van 16 juni

2017 (B.S. : 04.07.2017). Tekst in werking getreden op  de belastbare tijdperken die starten vanaf 1 juli 2017

imposables qui commencent à partir du 1er juillet 2017

- toegevoegd door art. 113 van het decreet van 18 dec.  2015 (B.S., 29.12.2015). De tekst treedt in werking vanaf  aanslagjaar 2016 (art. 135)

###### Art. 2.2.6.0.7.  Art. 2.2.6.0.7.

Er wordt op volgende voertuigen die uiterlijk op 31  december 2020 worden ingeschreven in het repertorium  van het Directoraat-generaal Mobiliteit en  Verkeersveiligheid geen belasting geheven op:

1° voertuigen waarvan de motor, ook al is het maar  gedeeltelijk of tijdelijk, aangedreven wordt met aardgas;

2° plug-in hybride voertuigen met een maximale CO2-  uitstoot van 50 gram per kilometer.

De vrijstelling, vermeld in het eerste lid, wordt ook  toegekend voor voertuigen, die na 31 december 2020  ingeschreven worden in het repertorium van het  Directoraat-generaal Mobiliteit en Verkeersveiligheid of  bij een vergelijkbare instelling binnen de Europese  Economische Ruimte of een andere staat en nadien in  het repertorium van het Directoraat-generaal Mobiliteit  en Verkeersveiligheid, en die voldoen aan de volgende  voorwaarden:

1° het wegvoertuig werd voor 12 oktober 2020 besteld;  1° le véhicule routier a été commandé avant le 12  octobre 2020 ;

2° een kopie van de bestelbon wordt aan de bevoegde  entiteit van de Vlaamse administratie bezorgd voor 15  januari 2021, samen met een formulier, afgeleverd door  deze entiteit, dat wordt ondertekend door de betrokken  belastingplichtige, en dat minstens de volgende  gegevens bevat:

a) hetzij het identificatienummer uit het Rijksregister  van  de  natuurlijke  personen,  hetzij  het  ondernemingsnummer  dat  bekend  is  bij  de  Kruispuntbank  van  Ondernemingen,  hetzij  het  identificatienummer, vermeld in artikel 8 van de wet van  15 januari 1990 houdende oprichting en organisatie van  een Kruispuntbank van de sociale zekerheid, van de

b) de voornamen, de achternaam en het domicilieadres  van de natuurlijke persoon of de naam, de rechtsvorm en  het adres van de maat- schappelijke zetel van de  rechtspersoon op wiens naam het voertuig ingeschreven  werd of zal ingeschreven worden in het repertorium van  het  Directoraat-generaal  Mobiliteit  en  Verkeersveiligheid.

Een plug-in hybride voertuig is een voertuig dat  aangedreven wordt door een elektrische motor en een  verbrandingsmotor waarvoor de energie geleverd wordt  aan de elektrische motor door batterijen die volledig  opgeladen kunnen worden via een aansluiting aan een  externe energiebron buiten het voertuig.

Het eerste lid, 1°, is alleen van toepassing op de  volgende voertuigen van natuurlijke personen en andere  rechtspersonen  dan  vennootschappen,  autonome  overheidsbedrijven  en  verenigingen  zonder  winstgevend doel, met leasingactiviteiten:

1° de wegvoertuigen die vóór 1 juli 2017 worden  ingeschreven in het repertorium van het Directoraat-  generaal Mobiliteit en Verkeersveiligheid;

2° de wegvoertuigen die na 30 juni 2017 worden  ingeschreven in het repertorium van het Directoraat-  generaal Mobiliteit en Verkeersveiligheid en waarvan  het belastbaar vermogen 11 fiscale paardenkracht niet te  boven gaat;

3° de lichte vrachtauto’s, de lijkwagens, en de  alleenrijdende trekkers, als het andere voertuigen zijn  dan de voertuigen, vermeld in artikel 2.2.4.0.1, § 6.

Het eerste lid, 2°, is alleen van toepassing op de  wegvoertuigen, de lichte vrachtauto’s, de lijkwagens, en  de alleenrijdende trekkers als het andere voertuigen zijn  dan de voertuigen vermeld in artikel 2.2.4.0.1, § 6, van  natuurlijke personen en andere rechtspersonen dan  vennootschappen, autonome overheidsbedrijven en  verenigingen  zonder  winstgevend  doel,  met  leasingactiviteiten.

---- historiek ----  ---- historique ----

- gewijzigd door art. 55 van het decreet van 18.12.2020  (B.S., 30.12.2020). Inwerkingtreding: 01.01.2021

- gewijzigd door art. 11 van het decreet van 16 juni 2017  (B.S. : 04.07.2017). Tekst in werking getreden op

de belastbare tijdperken die starten vanaf 1 juli 2017. De  tekst houdt op uitwerking te hebben vanaf 1 januari 2021  (art.135 van het decreet van 18 december 2015)

#### Afdeling 7 - Wijze van heffing  Section 7- Modalités de perception

###### Art. 2.2.7.0.1.  Art. 2.2.7.0.1.

De belasting wordt geheven in overeenstemming met de  bepalingen van artikel 3.3.2.0.1, eerste lid, 2° en 3°, en  tweede lid, 2° en 3°.

###### Art. 2.2.7.0.2.  Art. 2.2.7.0.2.

§ 1. Met toepassing van artikel 2.2.7.0.1 is de belasting  verschuldigd voor het aantal maanden dat begrepen is  tussen de eerste dag van de maand waarin het voertuig  in de loop van een kalenderjaar in gebruik is genomen  op de openbare weg en 31 december van hetzelfde jaar,  voor de voertuigen, vermeld in artikel 2.2.2.0.1, § 2,  tweede lid.

Het verschuldigde bedrag is gelijk aan een twaalfde van  de jaarlijkse belasting, vermenigvuldigd met het aantal  maanden, vermeld in het eerste lid.

§ 2. In afwijking van paragraaf 1 en artikel 3.3.1.0.1,  eerste lid, is geen enkele belasting verschuldigd voor de  maand december als het gebruik na 15 december begint.

§ 3. Als het gebruik in de loop van het aanslagjaar  ophoudt, is de belasting die betaald moet worden, het  bedrag dat verschuldigd is voor de verstreken maanden.

Dat bedrag mag niet lager zijn dan het minimum,  vermeld in artikel 2.2.4.0.2, § 2.

§ 4. Als het voertuig wordt gewijzigd, is de belasting die  betaald moet worden, het bedrag dat verschuldigd is  voor de verstreken maanden.

### Hoofdstuk 3 - Belasting op de inverkeerstelling  Chapitre 3 - Taxe sur la mise en circulation

#### Afdeling 1 - Belastbaar voorwerp  Section 1re - Objet imposable

###### Art. 2.3.1.0.1.  Art. 2.3.1.0.1.

Overeenkomstig artikel 94 van het federale Wetboek  van  23  november  1965  van  de  met

Conformément à l'article 94 du Code fédéral du 23  novembre 1965 des taxes assimilées aux impôts sur les  inkomstenbelastingen gelijkgestelde belastingen, wordt  er een belasting geheven op de wegvoertuigen, de  luchtvaartuigen en de boten, als ze op de openbare weg  in het verkeer worden gesteld of worden gebruikt in  België.

###### Art. 2.3.2.0.1.  Art. 2.3.2.0.1.

§ 1. De belastingplichtige is degene die vermeld is,  naargelang het geval, op het inschrijvingsbewijs of op  de registratiebrief op het ogenblik van de eerste  inverkeerstelling op de openbare weg van het  wegvoertuig of op het ogenblik van een eerste gebruik  van een luchtvaartuig of van een boot door de vermelde  natuurlijke persoon of rechtspersoon.

De wegvoertuigen worden geacht in het verkeer te zijn  gesteld als ze ingeschreven zijn of moeten zijn in het  repertorium van het Directoraat-generaal Mobiliteit en  Verkeersveiligheid.

De luchtvaartuigen worden geacht in België te zijn  gebruikt als ze ingeschreven zijn of moeten zijn door het  Directoraat-generaal Luchtvaart.

De boten worden geacht in België te zijn gebruikt als  daarvoor een registratiebrief is uitgereikt of moet zijn  uitgereikt door de Federale Overheidsdienst Mobiliteit.

§ 2. In afwijking van paragraaf 1 is de belasting niet  verschuldigd voor een wegvoertuig of een luchtvaartuig  dat wordt ingeschreven, of voor een boot waarvoor een  registratiebrief wordt uitgereikt naar aanleiding van een  overdracht  tussen  echtgenoten  of  wettelijke  samenwonenden of een overdracht tussen uit de echt  gescheiden personen ingevolge de echtscheiding of ex-  wettelijk samenwonenden door de beëindiging van de  wettelijke samenwoning, op voorwaarde dat de  overdrager voor hetzelfde wegvoertuig, hetzelfde  luchtvaartuig of dezelfde boot de belasting al heeft  betaald.

---- historiek ----  ---- historique ----

- gewijzigd door art. 8 van het decreet van 03.04.2026  (M.B. 23.04.2026). Inwerkingtreding: 03.05.2026

- gewijzigd door art. 6 van het decreet van 21.12.2018  (B.S. 28.12.2018). Tekst treedt in werking op 07.01.2019

#### Afdeling 3 - Belastbare grondslag  Section 3 - Base imposable

###### Art. 2.3.3.0.1.  Art. 2.3.3.0.1.  § 1. Voor de wegvoertuigen wordt de belasting  vastgesteld op basis van het vermogen van de motor,  uitgedrukt in fiscale paardenkracht of in kilowatt.

De milieukenmerken van het wegvoertuig worden  uitgedrukt in functie van de CO2-uitstoot en de  milieuklasse euronorm 0, 1, 2, 3, 4, 5 of 6. De  aanwezigheid van een roetfilter wordt ook in rekening  gebracht.

Euronormen zijn de maximumdrempels voor de  concentratie van bepaalde vervuilende stoffen in de  uitlaatgassen  van  autovoertuigen,  bepaald  in  opeenvolgende Europese richtlijnen en verordeningen.

#### Afdeling 4 - Tarieven  Section 4 – Tarifs

##### Onderafdeling 1 - Bedrag van de belasting voor  personenauto's, auto's voor dubbel gebruik en minibussen

als vermeld in artikel 1.1.0.0.2, vierde lid, 1°, die worden  geacht in het verkeer te zijn gesteld in het Vlaamse Gewest

###### Art. 2.3.4.1.1.  Art. 2.3.4.1.1.

De belasting op de personenauto's, auto's voor dubbel  gebruik en de minibussen, vermeld in artikel 1.1.0.0.2,  vierde lid, 1°, die worden geacht in het verkeer te zijn  gesteld in het Vlaamse Gewest, met uitzondering van de  voertuigen die worden geacht in het verkeer te zijn  gesteld  door  vennootschappen,  autonome  overheidsbedrijven  en  verenigingen  zonder  winstgevend doel, met leasingactiviteiten, wordt  berekend op de wijze, vermeld in artikel 2.3.4.1.2 tot en  met 2.3.4.1.7 en artikel 2.3.6.0.3.

In afwijking van het eerste lid bedraagt de belasting voor  de voertuigen, die uitsluitend aangedreven worden door  een elektrische motor of door waterstof en die na 31  december 2025 worden ingeschreven in het repertorium  van  het  Directoraat-generaal  Mobiliteit  en  Verkeersveiligheid, 61,50 euro.

---- historiek ----  ---- historique ----

- gewijzigd door art. 38 van het decreet van 19.12.2025  (B.S. 30.12.2025). Inwerkingtreding: 01.01.2026

- gewijzigd door art. 62 van het decreet van 26.06.2020  (B.S. 17.07.2020). Tekst is van toepassing op de  voertuigen die geacht worden in het verkeer te zijn  gesteld in het Vlaamse Gewest vanaf 1 juli 2020

###### Art. 2.3.4.1.2.  Art. 2.3.4.1.2.

De belasting wordt berekend volgens de volgende  formule:

BIV= ((CO2 * f + x) /246)6 * 4500 + c) * LC  BIV= ((CO2 * f + x) /246)6 * 4500 + c) * LC

De parameters, vermeld in het eerste lid, worden  gedefinieerd als volgt :

1° CO2 = de CO2-uitstoot van het wegvoertuig,  gemeten tijdens de homologatie ervan volgens de op het  moment van de eerste inschrijving geldende Europese  regel- geving;

2° f = 0,88 voor wegvoertuigen die aangedreven worden  door lpg;

f = 0,93 voor wegvoertuigen die aangedreven worden  door aardgas;

f = 0,744 voor wegvoertuigen die aangedreven worden  door zowel aardgas als benzine, als ze als benzinewagen  gehomologeerd zijn;

f = 1 voor andere wegvoertuigen;  f = 1 pour les autres voitures routiers ;

3° x = CO2-correctie in functie van de technologische  evolutie; x is gelijk aan 0 g CO2/km en wordt jaarlijks  verhoogd met 4,5 g CO2/km vanaf het jaar 2013;

4° c = constante (composante air) en fonction de  l'Euronorme et du type de carburant du véhicule routier,  visé au tableau suivant :

4° c = constante (luchtcomponent) in functie van de  euronorm en de brandstofsoort van het wegvoertuig,  vermeld in de volgende tabel :

Brandstofsoort

/  Type de carburant

Diesel

Benzine, en andere brandstoffen

/  Essence, et autres carburants

euro 6  20,61

5° CA = correction d'âge en fonction de l'ancienneté du  véhicule routier, visée au tableau suivant :

5° LC = leeftijdscorrectie in functie van de ouderdom  van het wegvoertuig, vermeld in de volgende tabel :

ouderdom van het wegvoertuig op basis van de datum van de eerste inschrijving ervan, in het

binnenland of in het buitenland, vermeld op het inschrijvingsbewijs

/  ancienneté du véhicule sur la base de la date de sa première immatriculation, en Belgique ou à

l'étranger, mentionnée sur le certificat d'immatriculation

minder dan 12 volle maanden  moins de 12 mois entiers  100  van 12 volle maanden tot en met 23 volle maanden  de 12 à 23 mois entiers  90  van 24 volle maanden tot en met 35 volle maanden  de 24 à 35 mois entiers  80  van 36 volle maanden tot en met 47 volle maanden  de 36 à 47 mois entiers  70  van 48 volle maanden tot en met 59 volle maanden  de 48 à 59 mois entiers  60  van 60 volle maanden tot en met 71 volle maanden  de 60 à 71 mois entiers  50  van 72 volle maanden tot en met 83 volle maanden  de 72 à 83 mois entiers  40  van 84 volle maanden tot en met 95 volle maanden  de 84 à 95 mois entiers  30  van 96 volle maanden tot en met 107 volle

maanden

meer dan 107 volle maanden  plus de 107 mois entiers  10

---- historiek ----  ---- historique ----

- gewijzigd door art. 56 van het decreet van 18.12.2020  (B.S., 30.12.2020). Inwerkingtreding: 01.01.2021

- eerste lid werd gewijzigd door art. 117 van het decreet  van 18 dec. 2015 (B.S., 29.12.2015). De tekst

treedt in werking vanaf 1 januari 2016 (art. 135)

- tweede lid, 4° werd gewijzigd door art. 117 van het  decreet van 18 dec. 2015 (B.S., 29.12.2015). De tekst

treedt in werking vanaf 1 januari 2016 (art. 135))

###### Art. 2.3.4.1.2/1  Art. 2.3.4.1.2/1

De belasting wordt voor de voertuigen, vermeld in  artikel 2.3.4.1.1, die voor de eerste keer worden  ingeschreven in het repertorium van het Directoraat- generaal Mobiliteit en Verkeersveiligheid na 31  december 2020, berekend volgens de volgende  formule:

De parameters, vermeld in het eerste lid, worden  gedefinieerd als volgt:

1° CO 2 = de CO 2 -uitstoot van het wegvoertuig,  gemeten tijdens de homologatie ervan volgens de  geldende Europese regelgeving;

2° f = 0,88 voor wegvoertuigen die aangedreven  worden door lpg;

f = 0,93 voor wegvoertuigen die aangedreven  worden door aardgas;

f = 0,744 voor wegvoertuigen die aangedreven  worden door zowel aardgas als benzine, als ze als  benzinewagen gehomologeerd zijn;

f = 1 voor andere wegvoertuigen;

3° q = een factor in functie van de Europese  emissienormen voor 2025 en 2030; q is gelijk aan  1,07 in 2021 en wordt jaarlijks verhoogd met 0,035  vanaf het jaar 2022;

4° c = constante (composante air) en fonction de  l'Euronorme et du type de carburant du véhicule routier,  visé au tableau suivant :

4° c = constante (luchtcomponent) in functie van de  euronorm en de brand- stofsoort van het  wegvoertuig, vermeld in de volgende tabel:

Brandstofsoort / Type de  carburant

Diesel  euro 0  2.863,15

euro 1  840,00

euro 2  622,57

euro 3  493,36

euro 3 + roetfilter /  filtre à particules  467,06

euro 4  467,06

euro 4 + roetfilter /  filtre à particules  459,35

euro 5 of EEV / ou  EEV  459,35

euro 6  454,07

Benzine, en andere  brandstoffen / Essence et  autres carburants

euro 1  509,28

euro 2  152,29

euro 3  95,53

euro 4  22,93

euro 5 of EEV / ou  EEV  20,61

euro 6  20,61

ouderdom van het wegvoertuig op basis van de datum van de eerste inschrijving ervan, in het binnenland  of in het buitenland, vermeld op het inschrijvingsbewijs / ancienneté du véhicule sur la base de la date de  sa première immatriculation, en Belgique ou à l'étranger, mentionnée sur le certificat d'immatriculation

minder dan 12 volle maanden / Moins de 12 mois entiers  100

van 12 volle maanden tot en met 23 volle maanden / de 12 à 23 mois entiers  90

van 24 volle maanden tot en met 35 volle maanden / de 24 à 35 mois entiers  80

van 36 volle maanden tot en met 47 volle maanden / de 36 à 47 mois entiers  70

van 48 volle maanden tot en met 59 volle maanden / de 48 à 59 mois entiers  60

van 60 volle maanden tot en met 71 volle maanden / de 60 à 71 mois entiers  50

van 72 volle maanden tot en met 83 volle maanden / de 72 à 83 mois entiers  40

van 84 volle maanden tot en met 95 volle maanden / de 84 à 95 mois entiers  30

van 96 volle maanden tot en met 107 volle maanden / de 96 à 107 mois entiers  20

meer dan 107 volle maanden / plus de 107 mois entiers  10

---- historiek ----  ---- historique ----

- ingevoegd door art. 57 van het decreet van 18.12.2020  (B.S., 30.12.2020). Inwerkingtreding: 01.01.2021

###### Art. 2.3.4.1.3.  Art. 2.3.4.1.3.

De belasting bedraagt nooit minder dan 41,99 euro en  nooit meer dan 10.497,70 euro. In afwijking van artikel  2.3.4.1.2 en artikel 2.3.4.1.2/1 bedraagt de belasting  41,99 euro voor de wegvoertuigen die een eerste keer in  het verkeer zijn gesteld 30 jaar geleden of eerder.

---- historiek ----  ---- historique ----

- gewijzigd door art. 9 van het decreet van 03.04.2026  (M.B. 23.04.2026). Inwerkingtreding: 03.05.2026

- gewijzigd door art. 13 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- gewijzigd door art. 58 van het decreet van 18.12.2020  (B.S., 30.12.2020). Inwerkingtreding: 01.01.2021

- gewijzigd door art. 12 van het decreet van 16 juni 2017  (B.S. : 04.07.2017). Tekst in werking getreden op 1 juli  2017

###### Art. 2.3.4.1.4.  Art. 2.3.4.1.4.

De bedragen, vermeld in artikel 2.3.4.1.2, tweede lid, 4°,  en artikel 2.3.4.1.2/1, tweede lid, 4°, en de bedragen,  vermeld in artikel 2.3.4.1.3, zijn gekoppeld aan de  schommelingen van het algemeen indexcijfer van de  consumptieprijzen van het Rijk. De bedragen worden  aangepast op 1 juli van elk jaar op grond van de  schommelingen van het algemeen indexcijfer van de  consumptieprijzen van het Rijk, vastgesteld tussen de  maand mei van het vorige jaar en de maand mei van het  lopende jaar. De bedragen, vermeld in artikel 2.3.4.1.2,  2.3.4.1.2/1 en artikel 2.3.4.1.3, zijn de bedragen die van  toepassing waren op 1 juli 2015.

Les montants, visés à l'article 2.3.4.1.2, alinéa 2, 4°, et à  l'article 2.3.4.1.2/1, alinéa 2, 4°, et les montants, visés à  l'article 2.3.4.1.3, sont liés aux fluctuations de l'indice  général des prix à la consommation du Royaume. Les  montants sont adaptés le 1er juillet de chaque année sur  la base des fluctuations de l'indice général des prix à la  consommation du Royaume, fixé entre le mois de mai  de l'année précédente et le mois de mai de l'année en  cours. Les montants, visés à l'article 2.3.4.1.2, à l'article  2.3.4.1.2/1 et à l'article 2.3.4.1.3, sont les montants qui  s'appliquaient le 1er juillet 2015.

---- historiek ----  ---- historique ----

- gewijzigd door art. 59 van het decreet van 18.12.2020  (B.S., 30.12.2020). Inwerkingtreding: 01.01.2021

- modifié par l’art. 59 du décret du 18.12.2020 (M.B.,  30.12.2020). En vigueur le 01.01.2021

- gewijzigd door art. 119 van het decreet van 18 dec.  2015 (B.S., 29.12.2015). De tekst is in werking getreden  op 1 januari 2016 (art. 135)

- remplacé par art. 119 du décret du 18 déc. 2015 (M.B.,  29.12.2015). Texte est entré en vigueur le 1er janvier  2016 (art. 135)

###### Art. 2.3.4.1.5.  Art. 2.3.4.1.5.

Lorsque l'Euronorme du véhicule routier n'est pas  connue, ce paramètre est déterminé au moyen de la date  de la première immatriculation du véhicule routier,  visée au tableau suivant :

Als de euronorm van het wegvoertuig niet bekend is,  wordt die parameter bepaald aan de hand van de datum  van de eerste inschrijving van het wegvoertuig, vermeld  in de volgende tabel:

datum van de eerste inschrijving van het wegvoertuig in het binnenland of in het buitenland

Euronorm

/  date de la première immatriculation du véhicule routier en Belgique ou à l'étranger

/  Euronorme  tot en met 31 december 1993  jusqu'au 31 décembre 1993 inclus  euro 0  vanaf 1 januari 1994 tot en met 31 december

du 1er janvier 1994 au 31 décembre 1996

inclus  euro 1

vanaf 1 januari 1997 tot en met 31 december

du 1er janvier 1997 au 31 décembre 2000

inclus  euro 2

vanaf 1 januari 2001 tot en met 31 december

du 1er janvier 2001 au 31 décembre 2005

inclus  euro 3

vanaf 1 januari 2006 tot en met 31 december

du 1er janvier 2006 au 31 décembre 2010

inclus  euro 4

vanaf 1 januari 2011 tot en met 31 augustus

du 1er janvier 2011 au 31 août 2015 inclus  euro 5

vanaf 1 september 2015  à partir du 1er septembre 2015  euro 6

###### Art. 2.3.4.1.6.  Art. 2.3.4.1.6.  § 1. Als de CO2-uitstoot van het wegvoertuig niet bekend  is, wordt die parameter voor de toepassing van artikel  2.3.4.2.1, bepaald aan de hand van de brandstofsoort, de  cilinderinhoud en de euronorm, vermeld in de volgende  tabel :

§ 1 er . Lorsque les émissions de CO2 du véhicule routier  ne sont pas connues, ce paramètre est déterminé, aux fins  de l'article 2.3.4.2.1, au moyen du type de carburant, de la  cylindrée et de l'Euronorme, visés au tableau suivant :

brandstofsoort

cilinderinhoud in cc

Euronorm

/  type de carburant

/  cylindrée en cc

/  Euronorme  6  5  4  3  2  1  0  CO2-emissies in g/km

minder dan 1400

/  moins de 1400

117  125  140  150  164  173  175

benzine en andere  brandstoffen, met uitzondering

1400 tot en met 2000

van diesel en aardgas

/  1400 à 2000 inclusivement

/  essence et autres carburants, à  l'exception du diesel et du gaz

150  159  172  185  200  211  213

meer dan 2000

naturel

/  plus de 2000

228  238  247  259  279  295  297

minder dan 1400

/  moins de 1400

98  103  120  116  125  132  133

1400 tot en met 2000

diesel

/  1400 à 2000 inclusivement

117  125  144  151  163  173  174

meer dan 2000

/  plus de 2000

159  169  201  199  214  226  228

minder dan 1400

/  moins de 1400

94  100  112  120  131  139  140

1400 tot en met 2000

aardgas

/  gaz naturel

/  1400 à 2000 inclusivement

120  127  138  148  160  169  171

meer dan 2000

/  plus de 2000

182  190  198  207  223  236  238

§ 2. Als de CO2-uitstoot van het voertuig niet bekend is,  wordt die parameter voor de toepassing van artikel  2.3.4.1.2/1, bepaald volgens volgende formule: CO2- uitstoot = Constante + (Parameter_CC x CC) +  (Parameter_KW x KW) + (Parameter_FPK x FPK) +  (Parameter_ZP x ZP) + (Parameter_CC_KW x CC x KW)  +  (Parameter_CC_FPK  x  CC  x  FPK)  +  (Parameter_KW_FPK  x  KW  x  FPK)  +  (Parameter_CC_KW_FPK x CC x KW x FPK).

§ 2. Si les émissions de CO2 du véhicule ne sont pas  connues, ce paramètre est déterminé selon la formule  suivante aux fins de l'article 2.3.4.1.2/1 : émission CO2 =  Constante + (Paramètre_CC x CC) + (Paramètre_KW x  KW) + (Paramètre_FPK x FPK) + (Paramètre_ZP x ZP)  +  (Paramètre_CC_KW  x  CC  x  KW)  +  (Paramètre_CC_FPK  x  CC  x  FPK)  +  (Paramètre_KW_FPK  x  KW  x  FPK)  +  (Paramètre_CC_KW_FPK x CC x KW x FPK).

De parameters, vermeld in het eerste lid, worden  gedefinieerd als volgt:

Les paramètres figurant à l'alinéa 1er sont définis comme  suit :

2° KW = het vermogen van de motor uitgedrukt in  kilowatt gedeeld door 100;

2° KW = puissance du moteur exprimée en kilowatts  divisée par 100 ;

3° FPK = het vermogen van de motor uitgedrukt in fiscale  pk;

3° FPK = puissance du moteur exprimée en chevaux  fiscaux ;

4° ZP = het aantal zitplaatsen.  4° ZP = nombre de sièges.

De overige parameters, vermeld in het eerste lid, worden  voor de toepassing van deze formule, bepaald aan de hand  van de brandstofsoort, vermeld in de volgende tabel:

Aux fins de la formule précitée, les autres paramètres  figurant à l'alinéa 1er sont déterminés en fonction du type  de carburant, selon le tableau suivant :

Benzine en andere  brand- stoffen, met

uitzondering van  aardgas, diesel en plug-

Diesel plug-

Benzine plug-

inhybride /

Aardgas /

inhybride /

inhybride / Essence et

Diesel

Hybride  rechargeable

Gaz  naturel

Hybride  rechargeable

autres carburants, à

l'exception du gaz  naturel, du diesel et de

diesel

essence

l'hybride rechargeable

Parameter  constante /

58.3304  1017.5710  75.3124  1716.4604  7627.0345

Paramètre

constante

Parameter_

CC /  Paramètre_

2.9316  -403.6269  -126.9417  -102.5352  - 8617.6901

CC

Parameter_

KW /  Paramètre_

53.6921  -817.4980  56.3978  -1333.5261  - 8710.9573

KW

Parameter_

FPK /  Paramètre_

5.0617  -96.0669  27.1787  -229.5888  -606.3489

FPK

Parameter_

ZP /  Paramètre_

1.9861  1.9861  1.9861  1.9861  1.9861

ZP

Parameter_

CC_KW /  Paramètre_

17.2267  399.2770  -51.8607  -344.2686  8134.2581

Parameter_

CC_FPK /  Paramètre_

CC_FPK

Parameter_  KW_FPK /  Paramètre_

KW_FPK

Parameter_

CC_KW_

FPK /  Paramètre_

CC_KW_

FPK

De CO2-uitstoot, zoals berekend in het eerste lid, is  minstens gelijk aan nul.

Een plug-inhybride voertuig is een voertuig dat  aangedreven wordt door een elektrische motor en een  verbrandingsmotor waarvoor de energie geleverd wordt  aan de elektrische motor door batterijen die volledig  opgeladen kunnen worden via een aansluiting aan een  externe energiebron buiten het voertuig.

Een voertuig op aardgas is een voertuig waarvan de  motor, ook al is het maar gedeeltelijk of tijdelijk,  aangedreven wordt met aardgas.

---- historiek ----  ---- historique ----

- gewijzigd door art. 39 van het decreet van 30.06.2023  (B.S., 29.08.2023). Tekst in werking getreden vanaf  01.01.2021

- gewijzigd door art. 120 van het decreet van 18 dec.  2015 (B.S., 29.12.2015). De tekst is in werking getreden  op 1 januari 2016 (art. 135)

###### Art. 2.3.4.1.7.  Art. 2.3.4.1.7.

De aanwezigheid van een roetfilter als vermeld in artikel  2.3.4.1.2, tweede lid, wordt vastgesteld op basis van de  PM-gegevens of op basis van de gegevens over de  premie  voor  de  aankoop  en  installatie  van  emissieverminderende voorzieningen in wegvoertuigen  met een dieselmotor. Onder PM wordt verstaan: de

Een roetfilter als vermeld in artikel 2.3.4.1.2, tweede lid,  is een halfopen of een gesloten roetfilter.

Een gesloten roetfilter wordt geacht aanwezig te zijn bij  wegvoertuigen van euronorm 3 en 4 met een uitstoot  kleiner dan of gelijk aan 10 mg/km PM. Als in de  waarden de combinatie van 0 mg/km PM en 0 g/km CO2  voorkomt, wordt er geacht geen gesloten roetfilter  aanwezig te zijn.

Een halfopen roetfilter wordt geacht aanwezig te zijn bij  wegvoertuigen als de premieaanvraag voor de aankoop  en installatie van de roetfilter door de Vlaamse overheid  is goedgekeurd.

###### Art. 2.3.4.1.8.  Art. 2.3.4.1.8.

(…)  (…)

---- historiek ----  ---- historique ----

- opgeheven door art. 10 van het decreet van 22.06.2018.  Tekst in werking getreden vanaf 03.08.2018

###### Art. 2.3.4.1.9.  Art. 2.3.4.1.9.

(…)  (…)

---- historiek ----  ---- historique ----

- opgeheven door art. 10 van het decreet van 22.06.2018.  Tekst in werking getreden vanaf 03.08.2018

###### Art. 2.3.4.1.10.  Art. 2.3.4.1.10.

(…)  (…)

---- historiek ----  ---- historique ----

- opgeheven door art. 10 van het decreet van 22.06.2018.  Tekst in werking getreden vanaf 03.08.2018

- toegevoegd door art. 121 van het decreet van 18 dec.

2015 (B.S., 29.12.2015). De tekst is in werking getreden  op 1 januari 2016 (art. 135)

##### Onderafdeling 2 - Bedrag van de belasting voor  motorfietsen, luchtvoertuigen,boten en andere voertuigen

dan de wegvoertuigen, vermeld in artikel 2.3.4.1.1

###### Art. 2.3.4.2.1.  Art. 2.3.4.2.1.

§ 1. De belasting op andere voertuigen dan de  voertuigen, vermeld in artikel 2.3.4.1.1, wordt berekend  op de wijze die hierna wordt vermeld:

1° pour les voitures particulières, les voitures mixtes, les  minibus et les motocyclettes, la taxe est calculée sur la  base du tableau suivant :

1° voor de personenauto's, auto's voor dubbel gebruik,  minibussen en motorfietsen wordt de belasting berekend  op basis van de volgende tabel:

aantal pk

/  montant total de la taxe en euros  8 en minder

/  nombre de ch

/  8 et moins

9 tot en met 10

/  de 9 à 10

12 tot en met 14

/  de 12 à 14

16 tot en met 17

/  de 16 à 17

meer dan 17

/  plus de 17

Als het vermogen van eenzelfde motor, uitgedrukt in  fiscale paardenkracht (pk) en in kilowatt (kW),  aanleiding geeft tot de heffing van een verschillend  belastingbedrag, is de belasting voor het hoogste bedrag  verschuldigd;

2° de belasting bedraagt 619 euro voor ultralichte  motorluchtvaartuigen en 2478 euro voor alle andere  luchtvaartuigen;

3° de belasting bedraagt 2478 euro voor boten.  3° la taxe s'élève à 2.478 euros pour des bateaux.

§ 2. (...)  § 2. (...)

Als de verbrandingsmotor van een wegvoertuig wordt  aangedreven door verschillende brandstofsoorten en het  voertuig daardoor in aanmerking komt voor een  combinatie van de vermindering voor benzine en lpg,  wordt de toe te kennen vermindering beperkt tot het  hoogste bedrag dat voor dat aanslagjaar voor een  bepaalde soort van brandstof van toepassing is.

(…)  (…)

§ 3. La taxe, calculée conformément au paragraphe 1er,  1°, et au paragraphe 2, est réduite au pourcentage de la  taxe pour les véhicules routiers, visé au tableau suivant,  selon que les véhicules ont déjà été immatriculés en  Belgique ou à l'étranger avant leur importation  définitive :

§ 3. De belasting, berekend conform paragraaf 1, 1°, en  paragraaf 2, wordt verminderd tot het percentage van de  belasting voor de wegvoertuigen, vermeld in de  volgende  tabel,  naargelang  de  voertuigen  al  ingeschreven zijn geweest in het binnenland of in het  buitenland voor ze definitief ingevoerd werden:

Termijn / Délai  Percentage / Pourcentage  van 1 jaar tot 2 jaar  de 1 an à 2 ans  90  van 2 jaar tot 3 jaar  de 2 ans à 3 ans  80  van 3 jaar tot 4 jaar  de 3 ans à 4 ans  70  van 4 jaar tot 5 jaar  de 4 ans à 5 ans  60  van 5 jaar tot 6 jaar  de 5 ans à 6 ans  55  van 6 jaar tot 7 jaar  de 6 ans à 7 ans  50  van 7 jaar tot 8 jaar  de 7 ans à 8 ans  45  van 8 jaar tot 9 jaar  de 8 ans à 9 ans  40  van 9 jaar tot 10 jaar  de 9 ans à 10 ans  35  van 10 jaar tot 11 jaar  de 10 ans à 11 ans  30  van 11 jaar tot 12 jaar  de 11 ans à 12 ans  25  van 12 jaar tot 13 jaar  de 12 ans à 13 ans  20  van 13 jaar tot 14 jaar  de 13 ans à 14 ans  15  van 14 jaar tot 15 jaar  de 14 ans à 15 ans  10

In afwijking van het eerste lid bedraagt de belasting voor  de voertuigen die vijftien jaar en meer ingeschreven  geweest zijn 61,50 euro.

Na toepassing van het eerste lid mag de belasting voor  een voertuig niet minder dan 61,50 euro bedragen.

De belasting, berekend conform paragraaf 1, 2° en 3°,  wordt verminderd tot het percentage van de belasting  voor de luchtvaartuigen en boten, vermeld in de

Termijn / Délai  Percentage / Pourcentage  van 1 jaar tot 2 jaar  de 1 an à 2 ans  90  van 2 jaar tot 3 jaar  de 2 ans à 3 ans  80  van 3 jaar tot 4 jaar  de 3 ans à 4 ans  70  van 4 jaar tot 5 jaar  de 4 ans à 5 ans  60  van 5 jaar tot 6 jaar  de 5 ans à 6 ans  50  van 6 jaar tot 7 jaar  de 6 ans à 7 ans  40  van 7 jaar tot 8 jaar  de 7 ans à 8 ans  30  van 8 jaar tot 9 jaar  de 8 ans à 9 ans  20  van 9 jaar tot 10 jaar  de 9 ans à 10 ans  10

In afwijking van het vierde lid bedraagt de belasting  61,50 euro voor :

1° de luchtvaartuigen en boten die tien jaar of ouder zijn; 1° les aéronefs et bateaux de dix ans ou plus ;

2° de zelfbouwvliegtuigen, met uitzondering van de  zelfbouwvliegtuigen die worden geacht in het verkeer te  zijn  gesteld  door  vennootschappen,  autonome  overheidsbedrijven en verenigingen zonder winstgevend  doel, met leasingactiviteiten;

3° de paramotoren, met uitzondering van de  paramotoren die worden geacht in het verkeer te zijn  gesteld  door  vennootschappen,  autonome  overheidsbedrijven  en  verenigingen  zonder  winstgevend doel, met leasingactiviteiten.

§ 4. In afwijking van paragraaf 1, 2 en 3, bedraagt de  belasting  voor  de  voertuigen,  die  uitsluitend  aangedreven worden door een elektrische motor of door  waterstof en die na 31 december 2025 worden  ingeschreven in het repertorium van het Directoraat- generaal Mobiliteit en Verkeersveiligheid, 61,50 euro.

---- historiek ----  ---- historique ----

- gewijzigd door art. 10 van het decreet van 03.04.2026  (M.B. 23.04.2026). Inwerkingtreding: 03.05.2026

- gewijzigd door art. 39 van het decreet van 19.12.2025  (B.S., 30.12.2025). Inwerkingtreding: 01.01.2026

- gewijzigd door art. 14 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- gewijzigd door art. 11 van het decreet van 22.06.2018.  Tekst in werking getreden vanaf aanslagjaar 2019

- §3, vijfde lid vervangen door art. 4 van het decreet van  17 juli 2015 (B.S., 14.08.2015 ). De tekst is in werking  getreden vanaf aanslagjaar 2015 (art. 41)

###### Art. 2.3.4.2.2.  Art. 2.3.4.2.2.

Overeenkomstig artikel 107 van het federale Wetboek  van 23 november 1965 van de met inkomstenbelastingen  gelijkgestelde belastingen, zijn de gemeenschappen, de  gewesten, de provincies, de agglomeraties en de  gemeenten niet gemachtigd om opcentiemen te heffen  op de belasting op de  inverkeerstelling.

#### Afdeling 5 - Verminderingen  Section 5 – Réductions

###### Art. 2.3.5.0.1.  Art. 2.3.5.0.1.

Voor voertuigen waarvan het belastbaar vermogen 11  fiscale paardenkracht te boven gaat en waarvan de  motor, ook al is het maar gedeeltelijk of tijdelijk,  aangedreven wordt met aardgas, wordt de belasting  verminderd met vierduizend euro, in voorkomend geval  beperkt tot het bedrag van de belasting als berekend  overeenkomstig artikel 2.3.4.1.2 tot en met 2.3.4.1.4,  maar zonder toepassing van de minimumbelasting,  vermeld in artikel 2.3.4.1.3.

Dit artikel is alleen van toepassing op de wegvoertuigen,  vermeld in artikel 2.3.4.1.1.

De vermindering, vermeld in het eerste lid, wordt  toegekend voor voertuigen die uiterlijk op 31 december  2020 worden ingeschreven in het repertorium van het  Directoraat-generaal Mobiliteit en Verkeersveiligheid.

De vermindering, vermeld in het eerste lid, wordt ook  toegekend voor voer- tuigen die na 31 december 2020  ingeschreven worden in het repertorium van het  Directoraat-generaal Mobiliteit en Verkeersveiligheid of  bij een vergelijk- bare instelling binnen de Europese  Economische Ruimte of een andere staat en nadien in het  repertorium van het Directoraat-generaal Mobiliteit en  Verkeersveiligheid, en die voldoen aan de volgende  voorwaarden:

1° het wegvoertuig werd voor 12 oktober 2020 besteld;  1° le véhicule routier a été commandé avant le 12  octobre 2020 ;

2° een kopie van de bestelbon wordt aan de bevoegde  entiteit van de Vlaamse administratie bezorgd voor 15  januari 2021, samen met een formulier, afgeleverd door  deze entiteit, dat wordt ondertekend door de betrokken  belastingplichtige, en dat minstens de volgende gegevens  bevat:

a) hetzij het identificatienummer uit het Rijksregister van  de natuurlijke personen, hetzij het ondernemingsnummer  dat bekend is bij de Kruispuntbank van Ondernemingen,  hetzij het identificatienummer, vermeld in artikel 8 van  de wet van 15 januari 1990 houdende oprichting en  organisatie van een Kruispuntbank van de sociale  zekerheid, van de persoon op wiens naam het voertuig  ingeschreven werd of zal ingeschreven worden in het  repertorium van het Directoraat-generaal Mobiliteit en  Verkeersveiligheid;

b) de voornamen, de achternaam en het domicilieadres  van de natuur- lijke persoon of de naam, de rechtsvorm  en het adres van de maat- schappelijke zetel van de  rechtspersoon op wiens naam het voertuig ingeschreven  werd of zal ingeschreven worden in het repertorium van  het Directoraat-generaal Mobiliteit en  Verkeersveiligheid.

---- historiek ----  ---- historique ----

- gewijzigd door art. 60 van het decreet van 18.12.2020  (B.S., 30.12.2020). Inwerkingtreding: 01.01.2021

- ingevoegd door art. 13 van het decreet van 16 juni 2017  (B.S. : 04.07.2017). Tekst in werking getreden op de  belastbare tijdperken die starten vanaf 1 juli 2017

#### Afdeling 6 - Vrijstellingen  Section 6 – Exonérations

###### Art. 2.3.6.0.1.  Art. 2.3.6.0.1.

§ 1. Er wordt een vrijstelling van de belasting verleend  voor :

1° de luchtvaartuigen en de boten die uitsluitend  gebruikt worden voor een openbare dienst van de staat,  de gemeenschappen, de gewesten, de provincies, de  agglomeraties, de federaties van gemeenten of de  gemeenten;

2° de voertuigen die uitsluitend gebruikt worden voor  het vervoer van zieke of gewonde personen en, als het  wegvoertuigen betreft, die ingeschreven zijn als  ziekenauto's;

3° de voertuigen die als persoonlijk vervoermiddel  gebruikt worden door :

a) de militaire of burgerlijke grootoorlogsinvaliden die  een invaliditeitspensioen van ten minste 60 % genieten;

b) de personen die volledig blind zijn, volledig verlamd

zijn aan de bovenste ledematen of van wie de bovenste  ledematen geamputeerd zijn, en de personen die  aangetast zijn door een blijvende invaliditeit die  rechtstreeks toe te schrijven is aan de onderste ledematen

4° de voertuigen voorzien van een beroepsplaat;  4° les véhicules munis d'une plaque professionnelle ;

5° de voertuigen voorzien van een nationale plaat.  5° les véhicules munis d'une plaque nationale.

6° de voertuigen die specifiek worden omgebouwd voor  het gemeenschappelijk vervoer van rolstoelgebruikers.

6° les véhicules spécifiquement transformés pour le  transport en commun d'utilisateurs de fauteuils roulants.

1° een getuigschrift, uitgereikt door de overheid die het  invaliditeitspensioen  heeft  toegekend,  met  de  vermelding dat de betrokkene de hoedanigheid van  grootoorlogsinvalide heeft en een invaliditeitspensioen  van ten minste 60 % geniet;

2° een invaliditeitsattest, uitgereikt door de FOD Sociale  Zekerheid, met de vermelding dat de betrokkene recht  heeft op vrijstelling van de verkeersbelasting, of dat hij  is getroffen door volledige blindheid of volledige  verlamming van de bovenste ledematen, of dat die  ledematen geamputeerd zijn, of dat hij is aangetast door  een blijvende invaliditeit die rechtstreeks toe te  schrijven is aan de onderste ledematen en ten minste 50  % bedraagt.

De vrijstelling, vermeld in het eerste lid, 6°, wordt  verleend op voorwaarde dat de volgende documenten  worden voorgelegd aan het bevoegde personeelslid:

1° een geldig certificaat van individuele nationale  goedkeuring van een voertuig dat is afgeleverd door de  bevoegde entiteit van de Vlaamse administratie of een  gelijkwaardig certificaat dat is afgeleverd door de  bevoegde entiteit van een staat binnen de Europese  Economische Ruimte. Uit dat certificaat blijkt dat het  voertuig twee of meer voor rolstoelgebruikers  toegankelijke plaatsen heeft en omgebouwd is met een  bodemverlaging of rolstoelplateaulift;

2° een schriftelijke verklaring waarin de houder van het  voertuig bevestigt dat de verbouwing specifiek heeft  plaatsgevonden om rolstoelgebruikers te vervoeren.

§ 2. Er wordt ook een vrijstelling van de belasting  verleend voor de wegvoertuigen, luchtvaartuigen en  boten die binnen zes maanden na de inschrijving  conform artikel 2.3.2.0.1, § 1, tweede en derde lid, of na  de uitreiking van een registratiebrief conform artikel  2.3.2.0.1, § 1, vierde lid, worden overgebracht naar een  andere staat van de Europese Economische Ruimte en  daar  onder  een  definitieve  regeling  worden  ingeschreven of van een registratiebrief worden  voorzien.

De vrijstelling, vermeld in het eerste lid, is afhankelijk  van de voorlegging van de volgende documenten :

2° het bewijs van de inschrijving van het wegvoertuig of  het luchtvaartuig, of van de aflevering van een  registratiebrief of een gelijkwaardig document, volgens  een definitieve regeling, in de betrokken staat van de  Europese Economische Ruimte.

Als een wegvoertuig in een andere staat van de Europese  Economische Ruimte door een beroepshandelaar uit de  automobielsector geleverd wordt, kan het document,  vermeld in het tweede lid, 2°, geldig worden vervangen  door een afschrift van de factuur die de overdracht  bekrachtigt, en het bewijs van betaling van die factuur.

Lorsqu'un véhicule routier est livré dans un autre état de  l'Espace économique européen par un commerçant  professionnel du secteur de l'automobile, le document,  visé à l'alinéa deux, 2°, peut être valablement remplacé  par une copie de la facture attestant la transaction, et la  preuve de paiement de cette facture.  § 3. Er wordt een vrijstelling van de belasting verleend  voor de op afstand bestuurde luchtvaartuigsystemen.

In het eerste lid wordt verstaan onder op afstand  bestuurde luchtvaartuigsystemen, afgekort als "RPAS":  luchtvaartuigsystemen als vermeld in artikel 1, eerste  lid, 5°, van het koninklijk besluit van 10 april 2016 met  betrekking tot het gebruik van op afstand bestuurde  luchtvaartuigen in het Belgisch luchtruim.

---- historiek ----  ---- historique ----

- gewijzigd door art. 11 van het decreet van 03.04.2026  (M.B. 23.04.2026). Inwerkingtreding: 03.05.2026

- gewijzigd door art. 8 van het decreet van 09.12.2022  (B.S. 20.12.2022). Inwerkingtreding vanaf aanslagjaar  2023

- gewijzigd door art. 63 van het decreet van 26.06.2020  (B.S. 17.07.2020). Tekst treedt in werking op 01.10.2020

- gewijzigd door art. 22 van het decreet van 23.12.2016  (B.S.: 30.12.2016). Tekst in werking getreden vanaf  aanslagjaar 2016

###### Art. 2.3.6.0.2.  Art. 2.3.6.0.2.

Op voertuigen die uitsluitend aangedreven worden door  een elektrische motor of waterstof en die uiterlijk op 31  december 2025 worden ingeschreven in het repertorium  van  het  Directoraat-generaal  Mobiliteit  en  Verkeersveiligheid wordt geen belasting geheven.

De vrijstelling, vermeld in het eerste lid, wordt ook  toegekend voor voertuigen, die na 31 december 2025  ingeschreven worden in het repertorium van het

1° het voertuig werd vóór 6 oktober 2025 besteld;  1° le véhicule a été commandé avant le 6 octobre 2025 ;

2° een kopie van de bestelbon wordt aan de bevoegde  entiteit van de Vlaamse administratie bezorgd voor 15  januari 2026, samen met een formulier, afgeleverd door  deze entiteit, dat wordt ondertekend door de betrokken  belastingplichtige, en dat minstens de volgende gegevens  bevat:

a) hetzij het identificatienummer uit het Rijksregister van  de natuurlijke personen, hetzij het ondernemingsnummer  dat bekend is bij de Kruispuntbank van Ondernemingen,  hetzij het identificatienummer, vermeld in artikel 8 van  de wet van 15 januari 1990 houdende oprichting en  organisatie van een Kruispuntbank van de sociale  zekerheid, van de persoon op wiens naam het voertuig  ingeschreven werd of zal ingeschreven worden in het  repertorium van het Directoraat-generaal Mobiliteit en  Verkeersveiligheid;

b) de voornamen, de achternaam en het domicilieadres  van de natuurlijke persoon of de naam, de rechtsvorm en  het adres van de maatschappelijke zetel van de  rechtspersoon op wiens naam het voertuig ingeschreven  werd of zal worden ingeschreven in het repertorium van  het Directoraat-generaal Mobiliteit en  Verkeersveiligheid.

---- historiek ----  ---- historique ----

- gewijzigd door art. 40 van het decreet van 19.12.2025  (B.S. 30.12.2025). Inwerkingtreding: 01.01.2026

- gewijzigd door art. 64 van het decreet van 26.06.2020  (B.S. 17.07.2020). Tekst is van toepassing op de  voertuigen die geacht worden in het verkeer te zijn  gesteld in het Vlaamse Gewest vanaf 1 juli 2020

- gewijzigd door art. 6 van het decreet van 21.12.2018  (M.B. 28.12.2018). Texte entre en vigueur le 01.01.2019

- vervangen door art. 122 van het decreet van 18 dec.  2015 (B.S., 29.12.2015). De tekst is in werking getreden  op 1 januari 2016 (art. 135))

###### Art. 2.3.6.0.3.  Art. 2.3.6.0.3.

Er wordt voor volgende voertuigen die uiterlijk op 31  december 2020 worden ingeschreven in het repertorium  van het Directoraat-generaal Mobiliteit en  Verkeersveiligheid geen belasting geheven op:

2° plug-in hybride voertuigen met een maximale CO2-  uitstoot van 50 gram per kilometer.

Een plug-in hybride voertuig is een voertuig dat  aangedreven wordt door een elektrische motor en een  verbrandingsmotor waarvoor de energie geleverd wordt  aan de elektrische motor door batterijen die volledig  opgeladen kunnen worden via een aansluiting aan een  externe energiebron buiten het voertuig.

Dit artikel is alleen van toepassing op de wegvoertuigen,  vermeld in artikel 2.3.4.1.1.

De vrijstelling, vermeld in het eerste lid, wordt ook  toegekend voor voertuigen, die na 31 december 2020  ingeschreven worden in het repertorium van het  Directoraat-generaal Mobiliteit en Verkeersveiligheid of  bij een vergelijk- bare instelling binnen de Europese  Economische Ruimte of een andere staat en nadien in  het repertorium van het Directoraat-generaal Mobiliteit  en Verkeersveiligheid, en die voldoen aan de volgende  voorwaarden:

1° het wegvoertuig werd voor 12 oktober 2020 besteld;  1° le véhicule routier a été commandé avant le 12 octobre  2020 ;

2° een kopie van de bestelbon wordt aan de bevoegde  entiteit van de Vlaamse administratie bezorgd voor 15  januari 2021, samen met een formulier, afgeleverd door  deze entiteit, dat wordt ondertekend door de betrokken  belastingplichtige, en dat minstens de volgende  gegevens bevat:

a) hetzij het identificatienummer uit het Rijksregister  van de natuur- lijke personen, hetzij het  ondernemingsnummer dat bekend is bij de  Kruispuntbank van Ondernemingen, hetzij het  identificatienummer, vermeld in artikel 8 van de wet van  15 januari 1990 houdende oprich- ting en organisatie  van een Kruispuntbank van de sociale zekerheid, van de  persoon op wiens naam het voertuig ingeschreven werd  of zal ingeschreven worden in het repertorium van het  Directoraat-gene- raal Mobiliteit en Verkeersveiligheid;

b) de voornamen, de achternaam en het domicilieadres  van de natuur- lijke persoon of de naam, de rechtsvorm  en het adres van de maat- schappelijke zetel van de  rechtspersoon op wiens naam het voertuig ingeschreven  werd of zal ingeschreven worden in het repertorium van  het Directoraat-generaal Mobiliteit en  Verkeersveiligheid.

---- historiek ----  ---- historique ----

- gewijzigd door art. 14 van het decreet van 16 juni 2017  (B.S. : 04.07.2017). Tekst in werking getreden op de  belastbare tijdperken die starten vanaf 1 juli 2017. De  tekst houdt op uitwerking te hebben vanaf 1 januari 2021  (art. 135 van het decreet van 18 december 2015).

- toegevoegd door art. 123 van het decreet van 18 dec.  2015 (B.S., 29.12.2015). De tekst treedt in werking op 1  januari 2016 (art. 135). De tekst houdt op uitwerking te  hebben vanaf 1 januari 2021 (art. 135)

#### Afdeling 7 - Wijze van heffing  Section 7 - Modalités de perception

###### Art. 2.3.7.0.1.  Art. 2.3.7.0.1.

De belasting wordt geheven in overeenstemming met de  bepalingen van artikel 3.3.2.0.1, eerste lid, 4°.

### Hoofdstuk 4 - Kilometerheffing  Chapitre 4 - Prélèvement kilométrique

- gewijzigd door art. 13 van het decreet van 3 juli 2015  (B.S., 10.08.2015). De tekst treedt in werking op een door  de Vlaamse Regering vast te stellen datum en ten  vroegste op 1 april 2016 (art. 44))

#### Afdeling 1 - Belastbaar voorwerp  Section 1re - Objet imposable

###### Art. 2.4.1.0.1.  Art. 2.4.1.0.1.

Er wordt een kilometerheffing geheven op het gebruik  dat een voertuig maakt van een niet-geconcedeerde weg.

---- historiek ----  ---- historique ----

- vervangen door art. 14 van het decreet van 3 juli 2015  (B.S., 10.08.2015). De tekst treedt in werking op 1 april  2016 (art. 44)

###### Art. 2.4.1.0.2.  Art. 2.4.1.0.2.

(…)  (…)

---- historiek ----  ---- historique ----

- opgeheven door art. 15 van het decreet van 3 juli 2015  (B.S., 10.08.2015). De tekst treedt in werking op 1 april  2016 (art. 44)

###### Art. 2.4.2.0.1.  Art. 2.4.2.0.1.

§ 1. De belastingplichtige is degene die houder is van het  voertuig. De houder van het voertuig is degene, hetzij :

1° op naam van wie het kenteken van het voertuig is  ingeschreven bij de overheid die belast is met de  inschrijving van de voertuigen;

2° op naam van wie het kenteken van het voertuig is  ingeschreven bij het buitenlands geldende equivalent  van de overheid die belast is met de inschrijving van de  voertuigen;

3° die het voertuig, waarvoor geen kenteken is  ingeschreven bij de overheid die belast is met de  inschrijving van de voertuigen of zijn equivalent in het  buitenland, feitelijk ter beschikking heeft.

Voor de toepassing van het eerste lid wordt, in geval van  een samenstel van voertuigen, het kenteken van het  trekkend voertuig bedoeld.

§ 2. In afwijking van paragraaf 1, eerste lid, kan de  houder van het voertuig, als het voertuig door de houder  ervan bestendig of gewoonlijk ter beschikking is gesteld  van een derde door verhuur, leasing of een andere  overeenkomst, die derde na hun gezamenlijk akkoord,  aanwijzen als de houder van het voertuig. De initiële  houder van het voertuig blijft solidair aansprakelijk voor  de goede uitvoering van de verplichtingen van de  vermelde derde.

De Vlaamse Regering kan de voorwaarden, beperkingen  en nadere regels van deze mogelijkheid bepalen.

---- historiek ----  ---- historique ----

- §1, tweede lid, gewijzigd door art. 12 van het decreet  van 03.05.2024 (B.S., 22.05.2024). Inwerkingtreding:  01.07.2025

- vervangen door art. 16 van het decreet van 3 juli 2015  (B.S., 10.08.2015). De tekst treedt in werking op 1 april  2016 (art. 44)

#### Afdeling 3 - Belastbare grondslag  Section 3 - Base imposable

###### Art. 2.4.3.0.1.  Art. 2.4.3.0.1.  De heffing wordt vastgesteld op basis van het aantal  kilometers die door een voertuig worden afgelegd en die  geregistreerd worden conform artikel 3.3.1.0.13.

- vervangen door art. 17 van het decreet van 3 juli 2015  (B.S., 10.08.2015). De tekst treedt in werking op 1 april  2016 (art. 44)

#### Afdeling 4 - Tarieven  Section 4 – Tarifs

###### Art. 2.4.4.0.1.  Art. 2.4.4.0.1.

De heffing wordt vastgesteld met behulp van de  volgende berekeningsformule :

Σ Tz x Kz,  z

waarbij :  où :

1° Tz = het tarief, vermeld in artikel 2.4.4.0.2, dat van  toepassing is in een bepaalde tariefzone voor kilometers  afgelegd in een welbepaalde rijrichting, op een  welbepaald moment, uitgedrukt in eurocent/kilometer  en dat rekening houdt met de kost van onderhoud van de  infrastructuur en met de externe kosten;

2° Kz = het aantal aan te rekenen kilometers, vermeld in  artikel 2.4.4.0.3, dat afgelegd wordt in elk van de  tariefzones;

3° z = de onderscheiden tariefzones, vermeld in artikel  1.1.0.0.2, vijfde lid, 5°.

Gezien het tarief Tz kan variëren in de tijd en naargelang  de rijrichting, zal Kz afzonderlijk worden berekend voor  elke waarde van Tz die tijdens het gebruik van het  betreffende wegsegment voorkomt.

Voor de toepassing van deze afdeling wordt verstaan  onder tariefzone : een begrensd wegsegment met een  vast begin- en eindpunt waarop bij gebruik in een  welbepaalde rijrichting op elk moment een eenduidig  bepaald en afstandsgerelateerd tarief Tz van toepassing  is.

---- historiek ----  ---- historique ----

- vervangen door art. 18 van het decreet van 3 juli 2015  (B.S., 10.08.2015). De tekst treedt in werking op 1 april  2016 (art. 44)

###### Art. 2.4.4.0.2.  Art. 2.4.4.0.2.  De hoogte van het tarief Tz, vermeld in artikel 2.4.4.0.1,  1°, uitgedrukt in eurocent wordt als volgt bepaald :

waarbij :  où :

1° F = factor, die 1 is voor de wegen of wegsegmenten,  vermeld in punt 3°, die limitatief opgesomd zijn in  bijlage 2, en 0 voor alle andere wegen of wegsegmenten;

2° Bt = basistarief van de heffing, met waarde 13,5  eurocent;

3° A = variation en fonction du type de route W à taux  d'imposition supérieur à zéro centime, ventilé selon le  tableau suivant :

3° A = variatie in functie van wegtype W met een tarief  dat hoger is dan nul eurocent, gedifferentieerd volgens  de volgende tabel :

wegtype (W) / type de route (W)  A  autosnelwegen en autosnelwegenringen  autoroutes et rings autoroutiers  0  overige gewestwegen met een tarief hoger dan

nul eurocent

gemeentewegen met een tarief hoger dan nul

eurocent

De wegen of wegsegmenten die onder een van de  wegtypes, vermeld in de bovenstaande tabel, vallen,  worden limitatief opgesomd in bijlage 2;

4° G = variation en fonction de la catégorie de poids du  véhicule, différenciée selon les catégories suivantes :

4° G = variatie in functie van gewichtsklasse van het  voertuig, gedifferentieerd volgens de volgende tabel :

maximaal toegestane totaalgewicht / masse maximale autorisée  G  maximaal toegestane totaalgewicht hoger dan

3,5 ton en lager dan 12 ton

maximaal toegestane totaalgewicht hoger dan  of gelijk aan 12 ton en niet hoger dan of gelijk

aan 32 ton

maximaal toegestane totaalgewicht hoger dan

32 ton

5° En = variatie in functie van de hoogte van de EURO-  emissieklasse, vermeld in artikel 1.1.0.0.2, vijfde lid, 1;

6° Et = variatie in functie van de tijd;  6° Et = variation en fonction du moment ;

7° Ep = variatie in functie van de plaats;  7° Ep = variation en fonction du lieu ;  8° Ex = toeslag in functie van de door het voertuig  veroorzaakte externe kosten, in functie van de hoogte  van de EURO-emissieklasse, gedifferentieerd volgens  de volgende tabel :

8° Ex = supplément dû en fonction des coûts externes,  engendrés par le véhicule, en fonction de la hauteur de  la classe d'émission EURO, différenciée selon le tableau  suivant :

EURO-emissieklasse / Classe d'émission EURO  Ex  EURO 6 of hoger / EURO 6 ou supérieure  1,2  EURO 5 of EEV / EURO 5 ou EEV  2,2  EURO 4  3.4  EURO 3  6,6  overige EURO-emissieklassen / autres classes d'émission EURO  8,6

9° a, b, c, d, e, en f = factoren die een invloed uitoefenen  op het gewicht van respectievelijk A, G, En, Et, Ep en  Ex, waarbij a = 1, b = 1, c = 0, d = 0, e = 0, en f = 1.

De Vlaamse Regering wordt ertoe gemachtigd om de  wegenlijst in bijlage 2, vermeld in het eerste lid, 1°, aan  te passen aan :

1° naamswijzigingen van de erin opgenomen wegen;  1° aux changements de nom des routes y reprises ;

2° wijzigingen van de categorisering van de erin  opgenomen wegen.

Het tarief Tz, vermeld in het eerste lid, wordt met ingang  van 1 juli 2017 op 1 juli van elk jaar geïndexeerd met  behulp van de coëfficiënt die wordt verkregen door het  algemene indexcijfer van de consumptieprijzen van het  Rijk, voor de maand maart van het lopende jaar te delen  door het algemene indexcijfer van de consumptieprijzen  van het Rijk voor de maand mei van het jaar 2016.

Daarbij worden de volgende afrondingen toegepast :  Dans ce contexte, les arrondissements suivants sont  appliqués :

1° de coëfficiënt wordt afgerond op het hogere of lagere  tienduizendste  naargelang  het  cijfer  van  de  honderdduizendsten al of niet vijf bereikt;

2° na de toepassing van de coëfficiënt wordt het  verkregen bedrag afgerond op het hogere of lagere

Als de factor F, vermeld in het eerste lid, 1°, gelijk is aan  1, mag het tarief nooit lager zijn dan nul eurocent.

Emissievrije voertuigen met een maximaal toegestane  totaalgewicht (MTT) lager dan of gelijk aan 4,25 ton zijn  vanaf 1 januari 2024 tot en met 31 december 2029  vrijgesteld van de verplichting om de kilometerheffing  te betalen.

Voor de overige emissievrije voertuigen, andere dan  deze vermeld in het vijfde lid, is de toeslag Ex tot en met  31 december 2029 gelijk aan nul. Het overige gedeelte  van de kilometerheffing wordt voor deze voertuigen  verminderd met:

- 100% vanaf 1 januari 2024 tot en met 31 december  2025;

- 80% vanaf 1 januari 2026 tot en met 31 december  2026;

- 60% vanaf 1 januari 2027 tot en met 31 december  2027;

- 40% vanaf 1 januari 2028 tot en met 31 december  2028;

- 20% vanaf 1 januari 2029 tot en met 31 december  2029.

---- historiek ----  ---- historique ----

- gewijzigd door art. 54 van het decreet van 20.12.2024  (B.S., 30.12.2024). Tekst treedt in werking op 01.07.2025

- gewijzigd door art. 20 van het decreet van 22.12.2023  (B.S., 29.12.2023). Tekst treedt in werking op 01.01.2024

- gewijzigd door art. 15 van het decreet van 02.04.2021  (B.S., 15.04.2021). Tekst treedt in werking op 01.01.2023

- gewijzigd door art. 31 van het programmadecreet van  20 december 2019 (B.S., 30.12.2019). Tekst treedt in

werking vanaf 1 juli 2020

- gewijzigd door art. 3 van het decreet van 30 juni 2017  (B.S.: 03.07.2017). Tekst in werking getreden op  01.07.2017

- gewijzigd door art. 23 van het decreet van 23 december  2016 (B.S.: 30.12.2016). Tekst in werking getreden op  01.04.2016

- vervangen door art. 19 van het decreet van 3 juli 2015  (B.S., 10.08.2015). De tekst treedt in werking op 1 april  2016 (art. 44)

Het aantal aan te rekenen kilometers Kz, vermeld in  artikel 2.4.4.0.1, eerste lid, 2°, wordt bepaald volgens de  volgende formule :

Kz = KM x (100% - C)  Kz = KM x (100 % - C)

waarbij :  où :

1° KM = het aantal geregistreerde kilometers in de  betreffende tariefzone waar op dat ogenblik een tarief Tz  van toepassing is, gedurende een bepaalde kalenderdag;

2° C = een correctiefactor ter compensatie van eventueel  onnauwkeurige registratie, met waarde 1%.

---- historiek ----  ---- historique ----

- gewijzigd door art. 13 van het decreet van 03.05.2024  (B.S., 22.05.2024). Inwerkingtreding: 01.07.2024

- gewijzigd door art. 20 van het decreet van 3 juli 2015  (B.S., 10.08.2015). De tekst treedt in werking op 1 april  2016 (art. 44)

###### Art. 2.4.4.0.4.  Art. 2.4.4.0.4.  Op de kilometerheffing mogen geen opcentiemen  worden geheven.

---- historiek ----  ---- historique ----

- gewijzigd door art. 21 van het decreet van 3 juli 2015  (B.S., 10.08.2015). De tekst treedt in werking op een door  de Vlaamse Regering vast te stellen datum en ten  vroegste op 1 april 2016 (art. 44)

###### Art. 2.4.4.0.5.  Art. 2.4.4.0.5.

In dit artikel wordt verstaan onder de niet voor de weg  bestemde mobiele machines: de voertuigen, vermeld in  artikel 1, 1°, van het koninklijk besluit van 5 december  2004 houdende vaststelling van productnormen voor  inwendige verbrandingsmotoren in niet voor de weg  bestemde mobiele machines.

Als de EURO-emissieklasse van het voertuig niet  bekend is, wordt die parameter voor de toepassing van  artikel 2.4.4.0.2, eerste lid, 8°, bepaald overeenkomstig  de volgende bepalingen:

1° voor de niet voor de weg bestemde mobiele  machines:

emissienorm op boorddocumenten

/  norme d’émission dans documents

de bord

prélèvement kilométrique  Fase I / Stage I  Euro I  Fase II / Stage II  Euro II  Fase IIIa / Stage IIIa  Tier 3  Euro III  Fase IIIb / Stage IIIb  Tier 4i  Euro V  Fase IV / Stage IV  Tier 4  Euro VI

b) lorsqu’aucune norme d’émission, exprimée en «  Stage » ou en « Tier », n’est mentionnée dans les  documents de bord du véhicule, conformément au  tableau suivant :

b) als er geen emissienorm, uitgedrukt in "Fase" of in  "Tier", is vermeld op de boorddocumenten van het  voertuig, conform de volgende tabel:

datum van eerste inschrijving van het voertuig in het binnen- of

/  date de première immatriculation du véhicule dans le pays ou à l’étranger

prélèvement kilométrique  vanaf 1 januari 1999 tot en met 31

december 2001

vanaf 1 januari 2002 tot en met 31

december 2005

vanaf 1 januari 2006 tot en met 31

december 2010

vanaf 1 januari 2011 tot en met 31

december 2013

vanaf 1 januari 2014  à partir du 1er janvier 2014  Euro VI

2° pour les camions et les véhicules autres que les  véhicules visés au 1°, lorsqu’aucune norme d’émission  n’est mentionnée dans les documents de bord du  véhicule :

2° voor vrachtwagens en andere voertuigen dan de  voertuigen, vermeld in punt 1°, als er geen emissienorm  is vermeld op de boorddocumenten van het voertuig:

datum van eerste inschrijving van het voertuig in het binnen- of

/  date de première immatriculation du véhicule dans le pays ou à

prélèvement kilométrique  vanaf 1 oktober 1993 tot en met 30

september 1996

vanaf 1 oktober 1996 tot en met 30

september 2001

september 2006

vanaf 1 oktober 2006 tot en met 30

september 2009

vanaf 1 oktober 2009 tot en met 31

december 2013

vanaf 1 januari 2014  à partir du 1er janvier 2014  Euro VI

---- historiek ----  ---- historique ----

- ingevoegd door art. 24 van het decreet van 23  december 2016 (B.S.: 30.12.2016) Tekst in werking  getreden op 01.04.2016

#### Afdeling 5 - Verminderingen  Section 5 – Réductions

###### Art. 2.4.5.0.1.  Art. 2.4.5.0.1.

Voorbehouden voor toekomstig gebruik.  Réservé pour un usage futur.

---- historiek ----  ---- historique ----

- gewijzigd door art. 22 van het decreet van 3 juli 2015  (B.S., 10.08.2015). De tekst treedt in werking op 1 april  2016 (art. 44)

#### Afdeling 6 - Vrijstellingen  Section 6 – Exonérations

###### Art. 2.4.6.0.1.  Art. 2.4.6.0.1.  § 1. Er wordt in een vrijstelling van de heffing voorzien  voor de voertuigen die :

1°  in  het  Waalse  Gewest  of  het  Brusselse  Hoofdstedelijke Gewest overeenkomstig de aldaar  geldende bepalingen zijn vrijgesteld van de heffing;

2° uitsluitend gebruikt worden voor en door defensie,  bescherming burgerbevolking, brandweer en politie en  als zodanig uiterlijk herkenbaar zijn;

3° speciaal en uitsluitend voor medische doeleinden zijn  uitgerust en als zodanig uiterlijk herkenbaar zijn;

4° de aard hebben van een landbouw-, tuinbouw- of  bosbouwvoertuig, die slechts in beperkte mate worden  gebruikt op de openbare weg in België en die uitsluitend  worden gebruikt voor landbouw, tuinbouw, visteelt en  bosbouwwerkzaamheden.

§ 2. De vrijstellingen, vermeld in paragraaf 1, 2° tot en  met 4°, kunnen alleen worden toegekend als ze worden  aangevraagd voor het begin van het belastbare tijdperk  en zullen pas uitwerking hebben vanaf het belastbare  tijdperk dat volgt op de toekenning van de vrijstelling.

(…)  (…)

De houder van een voertuig als vermeld in paragraaf 1,  2° tot en met 4°, dat niet in België moet zijn  ingeschreven, dient de betreffende vrijstelling aan te  vragen bij Viapass.

§ 4. De vrijstellingen vermeld in paragraaf 1 blijven  gelden tot niet langer aan de voorwaarden van dit artikel  is voldaan.

§ 5. De bevoegde entiteit van de Vlaamse administratie  maakt onmiddellijk aan Viapass de voertuigen kenbaar  die van een vrijstelling genieten ingevolge dit artikel.

§ 6. Het vrijgestelde voertuig wordt opgenomen in een  lijst met vrijgestelde voertuigen door de Vlaamse  administratie. Die lijst wordt bijgehouden en bijgewerkt  in overeenstemming met de geldende regels ter  bescherming van de persoonsgegevens.

---- historiek ----  ---- historique ----

- §6 ingevoegd door art. 14 van het decreet van  03.05.2024 (B.S., 22.05.2024). Inwerkingtreding:  01.07.2025

- gewijzigd door art. 16 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- gewijzigd door art. 23 van het decreet van 3 juli 2015  (B.S., 10.08.2015). De tekst treedt in werking op 1 april  2016 (besluit van de Vlaamse Regering van 17 juli 2015 -  B.S., 10.08.2015 - art. 4))

---- info ----  ---- info ----

###### Art. 101. van het decreet van 18 dec. 2015 (B.S.,

29.12.2015). De tekst is in werking getreden vanaf 1  januari 2016 (art. 135)

#### Afdeling 7 - Wijze van heffing  Section 7 - Modalités de perception

###### Art. 2.4.7.0.1.  Art. 2.4.7.0.1.

De heffing wordt geheven in overeenstemming met  artikel 3.3.2.0.1, eerste lid, 10°, en tweede lid, 6°.

---- historiek ----  ---- historique ----

- gewijzigd door art. 24 van het decreet van 3 juli 2015  (B.S., 10.08.2015). De tekst treedt in werking op een door  de Vlaamse Regering vast te stellen datum en ten  vroegste op 1 april 2016 (art. 44)

###### Art. 2.4.7.0.2.  Art. 2.4.7.0.2.

(…)  (…)

---- historiek ----  ---- historique ----

- gewijzigd door art. 25 van het decreet van 3 juli 2015  (B.S., 10.08.2015). De tekst treedt in werking op een door  de Vlaamse Regering vast te stellen datum en ten  vroegste op 1 april 2016 (art. 44)

### Hoofdstuk 5 - Heffing ongeschikte en onbewoonbare

woningen

#### Afdeling 1 - Belastbaar voorwerp  Section 1re - Objet imposable

###### Art. 2.5.1.0.1.  Art. 2.5.1.0.1.

§ 1. De gemeenten zijn gemachtigd tot het heffen van  een gemeentelijke heffing op ongeschikte en/of  onbewoonbare woningen die opgenomen zijn in de  inventaris, rekening houdend met het minimale  voorschrift dat de minimumaanslag bedraagt:

a) 500 euro voor een kamer als vermeld in artikel 3.19,  § 1, van de Vlaamse Codex Wonen van 2021;

b) 990 euro voor elke andere woning dan deze, vermeld  in a).

§ 2. De gemeente geeft vóór 31 maart van het  aanslagjaar aan de bevoegde entiteit van de Vlaamse  administratie kennis over de heffing, vermeld in  paragraaf 1, aan de hand van een voor eensluidend  verklaard afschrift van het gemeenteraadsbesluit.

Voorde toepassing van het eerste lid geldt, behalve in  geval van sloop, het vermoeden dat de woning die is  opgenomen in de inventaris, vermeld in artikel 3.19, § 1,  van  de  Vlaamse  Codex  Wonen  van  2021,  ononderbroken is blijven voortbestaan vanaf datum van  de opname in de inventaris tot op de datum van de  schrapping uit deze inventaris met toepassing van artikel  3.23. Dit vermoeden kan slechts worden weerlegd  wanneer de woning ophield voort te bestaan na het  uitvoeren  van  handelingen  waarvoor  een  omgevingsvergunning werd afgeleverd.

---- historiek ----  ---- historique ----

- gewijzigd door art. 36 en 37 van het besluit van  17.07.2020 (B.S. 17.11.2020). Tekst treedt in werking op  01.01.2021. Bekrachtigd door art. 224, 2° van het  decreet van 09.07.2021 (B.S., 10.09.2021).  Inwerkingtreding: 20.09.2021.

- gewijzigd door art. 28 van het decreet van 29.03.2019  (B.S. 29.04.2019). Inwerkingtreding op 01.01.2021

- vervangen door art. 26 van het decreet van 23  december 2016 (B.S.: 30.12.2016). Tekst in werking  getreden vanaf aanslagjaar 2017

#### Afdeling 2 - Belastingplichtigen  Section 2 – Contribuables

###### Art. 2.5.2.0.1.  Art. 2.5.2.0.1.

De belastingplichtige van de heffing is degene die de  houder is van een van de volgende zakelijke rechten met  betrekking tot een woning op het ogenblik dat elke  opeenvolgende periode van twaalf maanden na de  opname in de inventaris verstreken is :

1° de volle eigendom;  1° la pleine propriété ;

2° het recht van opstal of van erfpacht;  2° le droit de superficie ou d'emphytéose ;

3° het vruchtgebruik.  3° l'usufruit ;

Als een van de zakelijke rechten, vermeld in het eerste  lid, in onverdeeldheid toebehoort aan meer dan één  persoon, geldt de onverdeeldheid als belastingplichtige.

---- historiek ----  ---- historique ----

- gewijzigd door art. 38 van het besluit van 17.07.2020  (B.S. 17.11.2020). Tekst treedt in werking op 01.01.2021.  Bekrachtigd door art. 224, 2° van het decreet van  09.07.2021 (B.S., 10.09.2021). Inwerkingtreding:  20.09.2021.

- gewijzigd door art. 29 van het decreet van 29.03.2019  (B.S. 29.04.2019). Inwerkingtreding op 01.01.2021

- gewijzigd door art. 27 van het decreet van 23.12.2016  (B.S.: 30.12.2016). Tekst in werking getreden vanaf  aanslagjaar 2017

#### Afdeling 3 - Belastbare grondslag  Section 3 - Base imposable

###### Art. 2.5.3.0.1.  Art. 2.5.3.0.1.

De heffing wordt vastgesteld op een basisbedrag van  1100 euro.

Het basisbedrag, vermeld in het eerste lid, wordt met  ingang van 1 januari 2022 jaarlijks geïndexeerd op 1  januari met behulp van de coëfficiënt die wordt  verkregen door het algemene indexcijfer van de  consumptieprijzen van het Rijk voor de maand  november van het vorige jaar te delen door het algemene  indexcijfer van de consumptieprijzen van het Rijk voor  de maand november van het jaar 2020.

Het aangepast basisbedrag, vermeld in het tweede lid,  wordt afgerond op de lagere vijftig euro.

---- historiek ----  ---- historique ----

- gewijzigd door art. 9 van het decreet van 09.12.2022  (B.S. 20.12.2022). Inwerkingtreding vanaf aanslagjaar  2023

- gewijzigd door art. 17 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- vervangen door art. 30 van het decreet van 29.03.2019  (B.S. 29.04.2019). Inwerkingtreding op

01.01.2021

- gewijzigd door art. 28 van het decreet van 23.12.2016  (B.S.: 30.12.2016) Tekst in werking getreden vanaf  aanslagjaar 2017

###### Art. 2.5.4.0.1.  Art. 2.5.4.0.1.

De heffing wordt berekend volgens de volgende  formule: B * (P + 1), waarbij:

- B gelijk is aan het geïndexeerd basisbedrag, vermeld in  artikel 2.5.3.0.1, afgerond naar het eerstvolgende  natuurlijk getal;

- P gelijk is aan het aantal periodes van twaalf maanden  dat de woning zonder onderbreking is opgenomen op de  desbetreffende lijst in de inventaris, vermeld in artikel  3.19, § 1, van de Vlaamse Codex Wonen van 2021, en  waarbij P niet meer bedraagt dan vier.

---- historiek ----  ---- historique ----

- gewijzigd door art. 39 van het besluit van 17.07.2020  (B.S. 17.11.2020). Tekst treedt in werking op 01.01.2021.  Bekrachtigd door art. 224, 2° van het decreet van  09.07.2021 (B.S., 10.09.2021). Inwerkingtreding:  20.09.2021.

- vervangen door art. 31 van het decreet van 29.03.2019  (B.S. 29.04.2019). Inwerkingtreding op

01.01.2021

- gewijzigd door art. 29 van het decreet van 23.12.2016  (B.S.: 30.12.2016). Tekst in werking getreden vanaf  aanslagjaar 2017

###### Art. 2.5.4.0.2.  Art. 2.5.4.0.2.

Met toepassing van artikel 464/1, 2°, van het federale  WIB 92 mogen de provincies, de agglomeraties en de  gemeenten  opcentiemen  heffen  op  de  heffing  ongeschikte en onbewoonbare woningen.

---- historiek ----  ---- historique ----

- gewijzigd door art. 30 van het decreet van 23.12.2016  (B.S.: 30.12.2016). Tekst in werking getreden vanaf  aanslagjaar 2017

- toegevoegd door art. 11 van het decreet van 19.12.2014  (B.S., 13.01.2015). De tekst is in werking getreden vanaf  het aanslagjaar 2015. (art. 24)

#### Afdeling 5 - Verminderingen  Section 5 – Réductions

###### Art. 2.5.5.0.1.  Art. 2.5.5.0.1.

Voorbehouden voor toekomstig gebruik.  Réservé pour un usage futur

###### Art. 2.5.6.0.1.  Art. 2.5.6.0.1.

De houder van een zakelijk recht wordt vrijgesteld van  de heffing als hij de woning volledig en uitsluitend  gebruikt als zijn hoofdverblijfplaats en als hij niet over  een andere woning beschikt.

---- historiek ----  ---- historique ----

- gewijzigd door art. 28 van het decreet van 23.12.2016  (B.S.: 30.12.2016). Tekst in werking getreden vanaf  aanslagjaar 2017

###### Art. 2.5.6.0.2.  Art. 2.5.6.0.2.

§ 1. De houder van een zakelijk recht wordt vrijgesteld  van de heffing op :

1° de woningen die binnen de grenzen liggen van een  door  de  bevoegde  overheid  goedgekeurd  onteigeningsplan of waarvoor geen stedenbouwkundige  vergunning  meer  wordt  afgeleverd  omdat  een  onteigeningsplan wordt voorbereid;

2° (…)  2° (…);

3° de woningen die getroffen zijn door een ramp die zich  heeft voorgedaan onafhankelijk van de wil van de  belastingplichtige, gedurende een periode van twee jaar  die volgt op de datum van de ramp;

4° de woningen waarvoor het sociaal beheersrecht  conform artikel 5.82 tot 5.85 van de Vlaamse Codex  Wonen van 2021, ingesteld is;

5° de woningen waarvoor een renovatiecontract als  vermeld in artikel 3.30, § 2, van de Vlaamse Codex  Wonen van 2021, gesloten is.

Onder een ramp als vermeld in het eerste lid, 3°, wordt  verstaan elke gebeurtenis die uiterlijk waarneembare  schade veroorzaakt aan de woning, waardoor het  gebruik of de bewoning van de woning geheel of ten dele  onmogelijk wordt.

6° de woningen geheel of gedeeltelijk verkregen bij  erfopvolging of testament, gedurende een periode van  twee jaar die volgt op de datum van de verkrijging.

§ 2. Er wordt een vrijstelling van de heffing wegens  overmacht verleend aan de houder van het zakelijk recht  die aantoont dat de woning opgenomen blijft in de  inventaris om redenen die onafhankelijk zijn van zijn  wil. Die vrijstelling wordt verleend voor een termijn van  één jaar, maar wordt jaarlijks verlengd als de overmacht  aanhoudt.

---- historiek ----  ---- historique ----

- gewijzigd door art. 2 van het decreet van 21.04.2023  (B.S. 30.05.2023). Inwerkingtreding: 09.06.2023.  Bekrachtigd door art. 224, 2° van het decreet van  09.07.2021 (B.S., 10.09.2021). Inwerkingtreding:  20.09.2021.

- gewijzigd door art. 40 van het besluit van 17.07.2020  (B.S. 17.11.2020). Tekst treedt in werking op 01.01.2021.  Bekrachtigd door art. 224, 2° van het decreet van  09.07.2021 (B.S., 10.09.2021). Inwerkingtreding:  20.09.2021.

- gewijzigd door art. 31 en 32 van het decreet van  23.12.2016 (B.S.: 30.12.2016). Tekst in werking getreden  vanaf aanslagjaar 2017

- §1, punt 2 opgeheven door art. 5 van het decreet van 17  juli 2015 (B.S., 14.08.2015 ). De tekst treedt in werking  op 1 januari 2016 (art. 41)

###### Art. 2.5.6.0.3.  Art. 2.5.6.0.3.

De Vlaamse Regering kan nadere procedurele regels  vaststellen voor de aanvraag en de toekenning van  vrijstellingen als vermeld in artikel 2.5.6.0.1 en  2.5.6.0.2.

---- historiek ----  ---- historique ----

- ingevoegd door art. 32 van het decreet van 29.03.2019  (B.S. 29.04.2019). Inwerkingtreding op

01.01.2021

#### Afdeling 7 - Wijze van heffing  Section 7 - Modalités de perception

###### Art. 2.5.7.0.1.  Art. 2.5.7.0.1.

De heffing is verschuldigd als de woning gedurende  twaalf opeenvolgende maanden is opgenomen in de  inventaris.

Zolang de woning niet is geschrapt uit de inventaris,  blijft de heffing verschuldigd bij het verstrijken van elke  opeenvolgende periode van twaalf maanden, conform  artikel 2.5.4.0.1 en artikel 3.3.2.0.1, eerste lid, 6°, en  tweede lid, 5°.

---- historiek ----  ---- historique ----

- gewijzigd door art. 28 van het decreet van 23.12.2016  (B.S.: 30.12.2016). Tekst in werking getreden vanaf  aanslagjaar 2017

Aan de verkrijger van een zakelijk recht als vermeld in  artikel 2.5.2.0.1, wordt een opschorting van de heffing  verleend gedurende een periode van twee jaar die volgt  op de volledige overdracht van het gebouw of de

Il est accordé à l'acquéreur d'un droit réel, tel que visé à  l'article 2.5.2.0.1, une suspension de la taxe pendant une  période de deux ans suivant le transfert total du bâtiment  ou de l'habitation, à condition qu'au cours de la période  woning, op voorwaarde dat in de loop van de voormelde  periode geen nieuwe overdracht plaatsvindt, en zich een  van de twee volgende gevallen voordoet :

1° de woning wordt in de loop van de voormelde periode  geschrapt uit de inventaris;

2° bij het verstrijken van de voormelde periode loopt een  periode van vrijstelling op grond van artikel 2.5.6.0.1 of  2.5.6.0.2, of loopt een periode van opschorting op grond  van artikel 2.5.7.0.3, en die opschorting wordt achteraf  niet ongedaan gemaakt.

De opschorting, vermeld in het eerste lid, geldt niet voor  de volgende overdrachten :

1° de overdracht aan vennootschappen die door de  overdrager rechtstreeks of onrechtstreeks in rechten of  in feiten gecontroleerd worden;

2° de overdracht die het gevolg is van een fusie, splitsing  of een andere overgang onder algemene titel;

3° de overdracht aan bloed- en aanverwanten tot en met  de derde graad […].

---- historiek ----  ---- historique ----

- gewijzigd door art. 3 van het decreet van 21.04.2023  (B.S. 30.05.2023). Inwerkingtreding: 09.06.2023

- gewijzigd door art. 28 van het decreet van 23.12.2016  (B.S.: 30.12.2016). Tekst in werking getreden vanaf  aanslagjaar 2017

###### Art. 2.5.7.0.3.  Art. 2.5.7.0.3.

Er wordt een opschorting van de heffing verleend zodra  de belastingplichtige:

- een omgevingsvergunning tot sloop of een schriftelijke  bevestiging van de volledig bevonden aanvraag voor een  omgevingsvergunning tot sloop, opgemaakt door de  gemeentelijke stedenbouwkundige ambtenaar, voorlegt;

- een gedetailleerd renovatieschema voorlegt waaruit  blijkt dat hij de nodige renovatiewerken zal uitvoeren  met het oog op het herstel van de conformiteit, vermeld  in artikel 1.3, § 1, eerste lid, 8°, van de Vlaamse Codex  Wonen van 2021.

1 ° een tekening of schets van de woning met aanduiding  van de geplande werken;

2° een volledige opsomming en korte beschrijving van  alle geplande werken;

2° une énumération complète et une description brève  de tous les travaux envisagés ;  3° een raming van de kosten van de geplande werken via  een van de volgende stukken:

a) een offerte voor de levering en plaatsing van  materialen door een aannemer;

b) een offerte voor de levering van materialen als de  werken in eigen beheer worden uitgevoerd;

c) een combinatie van beide offertes;  c) une combinaison des deux offres ;

4 ° een fotoreportage van de delen van de woning die  gerenoveerd worden.

De opschorting geldt voor de heffingen die verschuldigd  zijn op de inventarisatiedata die in de periode van  opschorting vallen.

De periode van opschorting eindigt op het moment dat  de renovatiewerkzaamheden beëindigd zijn of de sloop  voltooid is. Ze kan niet langer duren dan twee jaar, tenzij  de belastingplichtige aantoont dat voor het herstel van  de conformiteit, vermeld in het eerste lid, een  omgevingsvergunning noodzakelijk is of tenzij de  werken betrekking hebben op drie of meer gebouwen of  woningen, of zo omvangrijk zijn dat ze niet kunnen  worden voltooid in twee jaar. In die gevallen bedraagt  de maximale periode vier jaar.

De opschorting wordt ongedaan gemaakt als de  ongeschikte en/ of onbewoonbare woning op het einde  van de periode van opschorting of op het ogenblik van  de overdracht van een zakelijk recht als vermeld in  artikel 2.5.2.0.1, niet uit de inventaris geschrapt is, tenzij  op dat ogenblik een periode van vrijstelling loopt met  toepassing van artikel 2.5.6.0.1 of 2.5.6.0.2. De  opschorting wordt ook ongedaan gemaakt als de  aanvraag van een omgevingsvergunning tot sloop  geweigerd wordt. De opgeschorte heffingen zijn in die  gevallen alsnog verschuldigd.

Als de renovatiewerkzaamheden of de sloop worden  uitgevoerd door een sociale woonorganisatie, de  gemeente  of  het  Openbaar  Centrum  voor  Maatschappelijk Welzijn, dan kan de termijn, vermeld  in het vierde lid, door de Vlaamse Regering worden  verlengd op grond van een verslag over de  voorbereiding of de vordering van de werkzaamheden.

---- historiek ----  ---- historique ----

- vervangen door art. 33 van het decreet van 29.03.2019  (B.S. 29.04.2019). Inwerkingtreding op

01.01.2021

- gewijzigd door art. 33 van het decreet van 23.12.2016  (B.S.: 30.12.2016). Tekst in werking getreden vanaf  aanslagjaar 2017

###### Art. 2.5.7.0.4.  Art. 2.5.7.0.4.

De Vlaamse Regering kan nadere procedurele regels  vaststellen voor de aanvraag en de toekenning van  opschortingen als vermeld in artikel 2.5.7.0.2 en  2.5.7.0.3.

---- historiek ----  ---- historique ----

- ingevoegd door art. 34 van het decreet van 29.03.2019  (B.S. 29.04.2019). Inwerkingtreding op

01.01.2021

### Hoofdstuk 6 - Leegstandsheffing bedrijfsruimten  Chapitre 6 - Taxe sur les sites d'activité économique

#### Afdeling 1 - Belastbaar voorwerp  Section 1re - Objet imposable

###### Art. 2.6.1.0.1.  Art. 2.6.1.0.1.

Er wordt een leegstandsheffing geheven op de  bedrijfsruimten die opgenomen zijn in de inventaris.

#### Afdeling 2 - Belastingplichtigen  Section 2- Contribuables

###### Art. 2.6.2.0.1.  Art. 2.6.2.0.1.

De belastingplichtige is degene die op 1 januari van het  aanslagjaar eigenaar is van de bedrijfsgebouwen die  onderworpen zijn aan de heffing.

#### Afdeling 3 - Belastbare grondslag  Section 3 - Base imposable

###### Art. 2.6.3.0.1.  Art. 2.6.3.0.1.

De heffing wordt vastgesteld op basis van het kadastraal  inkomen van de gronden dat op 1 januari van het  aanslagjaar bekend is, inclusief opstanden, van het  perceel dat de leegstaande en/of verwaarloosde  bedrijfsruimte  uitmaakt,  alsook  voor  de  niet-  landbouwbedrijven op basis van het kadastraal inkomen  van alle aangrenzende percelen die één geheel ermee  vormen en die behoren tot dezelfde eigenaar.

###### Art. 2.6.4.0.1.  Art. 2.6.4.0.1.

De heffing wordt berekend volgens de volgende tabel,  waarbij het kadastraal inkomen wordt verdeeld in de  volgende schijven, die elk worden onderworpen aan de  volgende een heffingspercentages:

La taxe est calculée selon le tableau suivant, dans lequel  le revenu cadastral est réparti dans les tranches  suivantes, chacune étant soumise aux taux de taxation  suivants :

percentage van toepassing op het

totaalbedrag van de heffing op het

schijf van het kadastraal inkomen in

overeenstemmende gedeelte

voorgaande gedeelte in euro

euro

/  pourcentage qui s'applique à la

/  montant total de la taxe sur la partie

/  tranche du revenu cadastral en euros

précédente en euros  tot en met 12.350

## partie correspondante

/  jusqu'à 12.350 inclus

168  /

van 12.351 tot en met 37.150

/  de 12.351 à 37.150

140  20.748

van 37.151 tot en met 74.350

/  de 37.151 à 74.350

112  55.468

vanaf 74.351

/  à partir de 74.351

84  97.132

De heffing bedraagt nooit minder dan 3.700 euro.  La taxe n'est jamais inférieure à 3.700 euros.

Voor de niet-landbouwbedrijven komt het bedrag van de  heffing minstens overeen met een tarief van 2,47  euro/m2 oppervlakte van het grondvlak van het terrein,  vastgelegd door de diensten van het de Algemene  Administratie van de Patrimoniumdocumentatie. Zo niet  geldt de laatste heffing als minimumtarief.

Pour les entreprises non agricoles, le montant de la taxe  correspond au moins à un tarif de 2,47 euros/m2 de  superficie pour la superficie de base du terrain, telle que  fixée par les services de l'Administration générale de la  Documentation patrimoniale. Sinon, la dernière taxe  vaut comme tarif minimum.

---- historiek ----  ---- historique ----

- gewijzigd door art. 88 van het decreet van 19.12.2025  (B.S., 30.12.2025). Inwerkingtreding: 01.01.2026

- modifié par l'art. 88 du décret du 19.12.2025 (M.B.,  30.12.2025). Entrée en vigueur le 01.01.2026

- gewijzigd door art. 12 van het decreet van 19.12.2014  (B.S., 13.01.2015).De tekst is in werking getreden op  01.01.2015. (art. 24)

- modifié par art. 12 du décret du 19.12.2014 (M.B.,  13.01.2015). Texte applicable à partir du 01.01.2015

###### Art. 2.6.4.0.2.  Art. 2.6.4.0.2.

Met toepassing van artikel 464/1, 2°, van het federale  WIB 92 mogen de provincies, de agglomeraties en de  gemeenten opcentiemen heffen op de leegstandsheffing  bedrijfsruimten.

En application de l'article 464/1er, 2°, du CIR fédéral  92, les provinces, les agglomérations et les communes  peuvent percevoir des centimes additionnels sur la  redevance visant à lutter contre le délabrement  d'habitations et de bâtiments.

---- historiek ----  ---- historique ----

#### Afdeling 5 - Verminderingen  Section 5 – Réductions

###### Art. 2.6.5.0.1.  Art. 2.6.5.0.1.

Voorbehouden voor toekomstig gebruik.  Réservé pour un usage futur

#### Afdeling 6 - Vrijstellingen  Section 6 – Exonérations

###### Art. 2.6.6.0.1.  Art. 2.6.6.0.1.  Voorbehouden voor toekomstig gebruik.  Réservé pour un usage futur

#### Afdeling 7 - Wijze van heffing  Section 7 - Modalités de perception

###### Art. 2.6.7.0.1.  Art. 2.6.7.0.1.

De heffing is verschuldigd vanaf het kalenderjaar dat  volgt op de derde opeenvolgende registratie in de  inventaris voor geheel of gedeeltelijk leegstaande en/of  verwaarloosde bedrijfsruimten.

##### Onderafdeling 1 - Opschorting door een vernieuwing, al of

niet gekoppeld aan de beëindiging van de leegstand

###### Art. 2.6.7.1.1.  Art. 2.6.7.1.1.

Er wordt een opschorting van de heffing verleend voor  de bedrijfsruimten waarvoor uiterlijk op 31 december  van het kalenderjaar dat voorafgaat aan het aanslagjaar,  een vernieuwingsvoorstel wordt ingediend, voor zover  wordt voldaan aan de voorwaarden voor indiening en  aanvaarding van dat voorstel, bepaald met toepassing  van het vierde lid.

De opschorting blijft beperkt tot een termijn van twee  jaar vanaf de betekening van het vernieuwingsvoorstel  aan het departement. Tijdens die periode moet ook de  eventuele leegstand zijn beëindigd.

Het departement kan eenmalig een verlenging van de  opschortingstermijn toestaan met hoogstens twee jaar  als:

1° (…)  1° (…)

2° de aanvaarde vernieuwing dermate buitengewone  werkzaamheden omvat dat ze niet kan worden voltooid  binnen de opschortingstermijn, vermeld in het tweede  lid;

De Vlaamse Regering bepaalt de regels voor de  indiening en aanvaarding van het vernieuwingsvoorstel.

---- historiek ----  ---- historique ----

- gewijzigd door art. 8 van het decreet van 12.12.2025  (B.S., 23.12.2025). Inwerkingtreding: 01.01.2025

###### Art. 2.6.7.1.2.  Art. 2.6.7.1.2.  In de inventaris worden de datum van de indiening van  het  aanvaarde  vernieuwingsvoorstel  en  de  opschortingstermijn vermeld.

##### Onderafdeling 2 - Opschorting ingevolge een definitief

gesloten brownfieldconvenant

###### Art. 2.6.7.2.1.  Art. 2.6.7.2.1.

Er kan een opschorting van de heffing worden verleend  op verzoek van de eigenaar of eigenaars voor de  bedrijfsruimten die gevat zijn in een brownfieldproject  waarvoor het ontwerp van brownfieldconvenant is  goedgekeurd door de Vlaamse Regering, conform  hoofdstuk III van het decreet van 30 maart 2007  betreffende de Brownfieldconvenanten, voor zover de  eigenaar actor is bij het brownfieldconvenant.

De opschorting wordt ongedaan gemaakt als de Vlaamse  Regering  beslist  tot  stopzetting  van  de  onderhandelingen, vermeld in artikel 8, § 3, eerste lid,  van het decreet van 30 maart 2007 betreffende de  Brownfieldconvenanten, of als het brownfieldproject  niet tijdig wordt gestart of gerealiseerd conform de  voorwaarden, vermeld in het brownfieldconvenant. De  opgeschorte heffingen zijn in die gevallen alsnog  verschuldigd.

De opschorting kan worden toegekend voor een termijn  die loopt vanaf de datum van de aanvraag van de  opschorting  tot  aan  de  beëindiging  van  het  brownfieldconvenant, met toepassing van artikel 10, § 3,  van het decreet van 30 maart 2007 betreffende de  Brownfieldconvenanten. Op het einde van die periode  moet de verwaarlozing en/of de leegstand zijn  beëindigd.

De Vlaamse Regering bepaalt de regels voor de  indiening en aanvaarding van het verzoek tot  opschorting.

---- historiek ----  ---- historique ----

- gewijzigd door art. 10 van het decreet van 09.12.2022  (B.S. 20.12.2022). Inwerkingtreding: 30.12.2022

##### Onderafdeling 3 - Opschorting ingevolge een conform

verklaard bodemsaneringsproject

###### Art. 2.6.7.3.1.  Art. 2.6.7.3.1.

Er kan een opschorting van de heffing worden verleend  op verzoek van de eigenaar(s) voor de bedrijfsruimten  die het voorwerp uitmaken van een door de OVAM  conform  verklaard  bodemsaneringsproject,  met  toepassing van titel III, hoofdstuk V, van het decreet van  27 oktober 2006 betreffende de bodemsanering en de  bodembescherming.

De opschorting kan worden toegekend voor een termijn  die loopt vanaf de datum van de aanvraag van de  opschorting tot aan de datum van de eindverklaring van  de OVAM, vermeld in artikel 68 van het decreet van 27  oktober 2006 betreffende de bodemsanering en de  bodembescherming, met een maximumtermijn van vijf  jaar vanaf de conformverklaring van het

La suspension peut être accordée pour un délai qui court  de la date de la demande de la suspension jusqu'à la date  de la déclaration finale par l'OVAM, visée à l'article 68  du décret du 27 octobre 2006 relatif à l'assainissement  du sol et à la protection du sol, pour un délai maximum  de cinq ans à partir de la déclaration de conformité du  projet d'assainissement du sol. A la fin de cette période,  bodemsaneringsproject. Op het einde van die periode  moet de verwaarlozing en/of de leegstand zijn  beëindigd.

De opschorting wordt verleend voor de bedrijfsruimten  waarvoor uiterlijk op 31 december van het kalenderjaar  dat voorafgaat aan het aanslagjaar, een aanvraag tot  opschorting met toepassing van het eerste en het tweede  lid wordt ingediend die leidt tot een aanvaarding van het  verzoek tot opschorting.

De Vlaamse Regering bepaalt de regels voor de  indiening en aanvaarding van het verzoek tot  opschorting.

###### Art. 2.6.7.4.1.  Art. 2.6.7.4.1.

Nieuwe eigenaars van een geregistreerde bedrijfsruimte  krijgen een opschorting van de heffing gedurende twee  jaar vanaf de datum van het verlijden van de authentieke  akte van overdracht. Als er verschillende eigenaars voor  dezelfde bedrijfsruimte zijn, en minstens één ervan een  nieuwe eigenaar is, gelet op de overdracht aan hem door  erfopvolging of testament, krijgen ze een opschorting  van de heffing gedurende twee jaar vanaf de datum van  eigendomsoverdracht door erfopvolging of testament.

De volgende rechtspersonen of natuurlijke personen  worden niet beschouwd als nieuwe eigenaar:

1° de vennootschappen waarin de vroegere eigenaars  van de bedrijfsruimte rechtstreeks of onrechtstreeks  participeren […];

2° bloed- en aanverwanten tot en met de derde graad,  tenzij in geval van overdracht door erfopvolging of  testament.

---- historiek ----  ---- historique ----

- Gewijzigd door art. 10 van het decreet van 18.06.2021  (B.S., 15.07.2021). Inwerkingtreding door de Vlaamse  Regering vast te stellen en uiterlijk op 01.10.2021

###### Art. 2.6.7.4.2.  Art. 2.6.7.4.2.

In de inventaris worden de datum van het verlijden van  de authentieke akte en de opschortingstermijn vermeld.

##### Onderafdeling 5 - Opschorting voor leegstaande maar

niet-verwaarloosde bedrijfsruimten

###### Art. 2.6.7.5.1.  Art. 2.6.7.5.1.

Er kan een opschorting van de heffing worden verleend  op verzoek van de eigenaars voor de bedrijfsruimten die  ten gevolge van bedrijfseconomische omstandigheden  geheel of gedeeltelijk leegstaan, maar die in een goede

De opschorting blijft beperkt tot een termijn van een  jaar. Tijdens die periode moet de leegstand zijn  beëindigd.

De opschorting wordt verleend voor de bedrijfsruimten  waarvoor uiterlijk op 31 december van het kalenderjaar  dat voorafgaat aan het aanslagjaar, een aanvraag tot  opschorting met toepassing van het eerste en het tweede  lid wordt ingediend die leidt tot een aanvaarding van het  verzoek tot opschorting.

De Vlaamse Regering bepaalt de regels voor de  indiening en aanvaarding van het verzoek tot  opschorting.

###### Art. 2.6.7.5.2.  Art. 2.6.7.5.2.

In de inventaris worden de datum van de indiening van  de  aanvaarde  opschortingsaanvraag  en  de  opschortingstermijn vermeld.

##### Onderafdeling 6 - Opschorting ingevolge staving van de

beëindiging van de vernieuwing en/of de leegstand

###### Art. 2.6.7.6.1.  Art. 2.6.7.6.1.

Als  de  eigenaar  tijdens  de  toegestane  opschortingstermijn een aanvraag tot schrapping uit de  inventaris heeft ingediend conform artikel 12 van het  decreet van 19 april 1995, krijgt hij een opschorting van  de heffing gedurende de termijn dat zijn aanvraag,  conform artikel 13 van het decreet van 19 april 1995,  onderzocht wordt. Als de aanvraag tot schrapping  geweigerd wordt, heeft die beslissing rechtsgevolgen  vanaf de datum van de kennisgeving, vermeld in artikel  12 van het voormelde decreet.

##### Onderafdeling 7 - Sancties  Sous-section 7 – Sanctions

###### Art. 2.6.7.7.1.  Art. 2.6.7.7.1.

Als de opschortingen, verleend met toepassing van  artikel 2.6.7.1.1, 2.6.7.2.1, 2.6.7.3.1, 2.6.7.4.1 en  2.6.7.5.1, bij het verstrijken van de toegestane  opschortingstermijnen niet resulteren in een beëindiging  van de verwaarlozing en/of de leegstand, is de  opgeschorte heffing alsnog verschuldigd voor die  termijnen, vermeerderd met de interesten.

Als de eigenaar, aan wie een opschorting is verleend met  toepassing van artikel 2.6.7.1.1, 2.6.7.2.1, 2.6.7.3.1,  2.6.7.4.1 of 2.6.7.5.1, overgaat tot overdracht van de aan  de  heffing  onderworpen  bedrijfsruimte,  is  de  opgeschorte heffing, vermeerderd met de interesten,

In afwijking van het tweede lid, blijft de opschorting van  de heffing behouden als de eigenaar, aan wie een  opschorting is verleend met toepassing van artikel  2.6.7.2.1, overgaat tot overdracht van de aan de heffing  onderworpen bedrijfsruimte aan een actor bij het  brownfieldconvenant.

Als de eigenaar, aan wie een opschorting is verleend met  toepassing van artikel 2.6.7.6.1, overgaat tot overdracht  van de aan de heffing onderworpen bedrijfsruimte, is de  opgeschorte heffing, vermeerderd met de interesten,  alsnog  verschuldigd  vanaf  de  datum  van  de  kennisgeving, vermeld in artikel 12 van het decreet van  19 april 1995.

---- historiek ----  ---- historique ----

- gewijzigd door art. 20 van het decreet van 06.07.2018  (B.S. 30.08.2018). Tekst treedt in werking op 21.07.2012

### Hoofdstuk 7 – Erfbelasting  Chapitre 7 - Impôt de succession

---- historiek ----  ---- historique ----

- hoofdstuk 7 is toegevoegd door art. 3 van het decreet  van 19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

#### Afdeling 1 – Belastbaar voorwerp  Section 1re - Objet imposable

---- historiek ----  ---- historique ----

- afdeling 1 is toegevoegd door art. 4 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.1.0.1.  Art. 2.7.1.0.1.

Overeenkomstig artikel 3, 4°, van de bijzondere wet van  16 januari 1989 betreffende de financiering van de  gemeenschappen  en  de  gewesten  wordt  het  successierecht en het recht van overgang gevestigd op  de goederen die overgaan ingevolge het overlijden

---- historiek ----  ---- historique ----

- toegevoegd door art. 5 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.1.0.2.  Art. 2.7.1.0.2.

Naast het geval, vermeld in het eerste lid, is de  erfbelasting ook verschuldigd op een verkrijging van  vruchtgebruik met toepassing van artikel 4.18 of artikel  4.23, § 2, van het Burgerlijk Wetboek, tenzij de  langstlevende echtgenoot of wettelijk samenwonende  voor het overlijden van de schenker aan het  vruchtgebruik heeft verzaakt conform artikel 4.18, derde  lid, of artikel 4.23, § 2, tweede lid, van het Burgerlijk  Wetboek.

---- historiek ----  ---- historique ----

- gewijzigd door art. 12 van het decreet van 03.04.2026  (M.B. 23.04.2026). Inwerkingtreding: 03.05.2026

- gewijzigd door art. 3 van het decreet van 15.03.2024  (B.S. 20.03.2024). Inwerkingtreding: 30.03.2024

- gewijzigd door art. 18 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- gewijzigd door art. 7 van het decreet van 21.12.2018  (B.S. 28.12.2018). Tekst treedt in werking op 07.01.2019

- gewijzigd door art. 2 van het decreet van 06.07.2018  (B.S. 20.07.2018 Ed.2). Tekst treedt in werking op  01.09.2018

- toegevoegd door art. 6 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.1.0.3.  Art. 2.7.1.0.3.

Worden met het oog op de heffing van het successierecht  als legaten beschouwd :

1° alle schulden die uitsluitend bij uiterste wil erkend  zijn;

2° alle schuldbekentenissen van sommen die voorkomen  als een contract onder bezwarende titel, maar die een  bevoordeling  inhouden  en  die  niet  aan  de  schenkbelasting  of  het  registratierecht  op  de  schenkingen zijn onderworpen;

3° alle schenkingen van roerende goederen die de  erflater heeft gedaan onder de opschortende voorwaarde  of termijn die vervuld wordt ingevolge het overlijden  van de schenker.

Het eerste lid, 3°, is niet van toepassing bij de realisatie  van een beding van terugval die de erflater heeft  bedongen in het voordeel van een derde voor een  vruchtgebruik dat de erflater zich heeft voorbehouden.

---- historiek ----  ---- historique ----

- gewijzigd door art. 3 van het decreet van 06.07.2018  (B.S. 20.07.2018 Ed.2). Tekst treedt in werking op  01.09.2018

- toegevoegd door art. 7 van het decreet van 19.12.2014  (B.S., 29.01.2015, Ed. 2 – Err. B.S., 09.07.2024). De tekst  is in

werking getreden op 01.012015 (art. 325)

###### Art. 2.7.1.0.4.  Art. 2.7.1.0.4.

De langstlevende echtgenoot die ingevolge een  huwelijksovereenkomst die niet aan de regels voor de  schenkingen is onderworpen, meer dan de helft van de  gemeenschap toegekend krijgt, wordt voor de heffing  van de erfbelasting gelijkgesteld met de langstlevende  echtgenoot die, als niet wordt afgeweken van de gelijke  verdeling van de gemeenschap, het deel van de andere  echtgenoot krachtens een schenking onder de levenden  of een uiterste wilsbeschikking geheel of gedeeltelijk  verkrijgt.

---- historiek ----  ---- historique ----

- gewijzigd door art. 24 van het decreet van 3 juli 2015  (B.S., 15.07.2015). De tekst is in werking getreden op  01.07.2015 (art. 61)

- toegevoegd door art. 8 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 01.01.2015 (art. 325)

###### Art. 2.7.1.0.5.  Art. 2.7.1.0.5.

§ 1. De goederen waarvan de bevoegde entiteit van de  Vlaamse administratie het bewijs levert dat de erflater er  kosteloos over beschikte gedurende de vijf jaar vóór zijn  overlijden, worden geacht deel uit te maken van zijn  nalatenschap, tenzij de bevoordeling onderworpen is aan  de schenkbelasting of het registratierecht op de  schenkingen onder de levenden. De erfgenamen of  legatarissen hebben een verhaalsrecht ten aanzien van de  begiftigde voor de successierechten die op die goederen  voldaan zijn.

Als door de bevoegde entiteit van de Vlaamse  administratie of door de erfgenamen en legatarissen  bewezen wordt dat de bevoordeling toekwam aan een  bepaalde persoon, wordt die als legataris van de  geschonken zaak beschouwd.

Voor de toepassing van deze paragraaf wordt een  bevoordeling waarvoor een vrijstelling van de  schenkbelasting is toegepast, gelijkgesteld met een  bevoordeling die aan de schenkbelasting of aan het  registratierecht op de schenkingen onder de levenden is  onderworpen.

§ 2. De termijn van drie jaar, vermeld in paragraaf 1,  wordt evenwel op zeven jaar gebracht als het gaat om  aandelen en activa als vermeld in artikel 2.8.6.0.3.

De termijn van zeven jaar, vermeld in het eerste lid,  wordt teruggebracht tot drie jaar als de kosteloze  beschikking dagtekent van voor 1 januari 2012.

---- historiek ----  ---- historique ----

- gewijzigd door art. 31 van het decreet van 20.12.2024  (B.S., 30.12.2024). Inwerkingtreding op 01.01.2025 en  van toepassing zijn op de kosteloze beschikkingen die  dagtekenen vanaf 1 januari 2025

- toegevoegd door art. 9 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.1.0.6.  Art. 2.7.1.0.6.

§ 1. De sommen, renten of waarden die kosteloos aan  een persoon kunnen toekomen bij het overlijden van de  erflater, ingevolge een contract dat een door de erflater  of door een derde in het voordeel van die persoon  gemaakt beding bevat, worden geacht als legaat te zijn  verkregen door die persoon.

Ook de sommen, renten of waarden die kosteloos aan  een persoon zijn toegekomen, binnen vijf jaar vóór het  overlijden van de erflater, ingevolge een contract dat een  door de erflater in het voordeel van die persoon gemaakt  beding bevat, worden geacht als legaat te zijn verkregen  door die persoon.

Als de erflater een contract had afgesloten op grond  waarvan er pas een uitkering kan gebeuren na het  overlijden van de erflater, worden de sommen, renten of  waarden geacht kosteloos te worden verkregen, en  geacht als legaat te zijn verkregen, naar gelang van het  geval:

1° door de persoon die het levensverzekeringscontract  afkoopt na het overlijden van de erflater, op het tijdstip  van de afkoop;

2° door de persoon die de sommen, renten of waarden  effectief verkrijgt na het overlijden van de erflater, op  het tijdstip dat er een uitkering gebeurt.

Wanneer een overledene gehuwd was onder een stelsel  van gemeenschap, gelden de bepalingen van het eerste,  het tweede en het derde lid ook voor de sommen, renten  of waarden die kosteloos aan de langstlevende  echtgenoot  toekomen  ingevolge  een  levensverzekeringscontract  of  een  contract  met  vestiging van rente dat door die langstlevende  echtgenoot is gesloten.

§ 2. Dit artikel is van toepassing op de sommen of  waarden die kosteloos aan een persoon kunnen  toekomen bij het overlijden van degene die een  levensverzekering aan order of aan toonder is  aangegaan.

De persoon, vermeld in dit artikel, wordt vermoed  kosteloos te ontvangen, behoudens tegenbewijs. Dit  tegenbewijs kan niet worden geleverd door aan te tonen  dat het contract werd geschonken aan deze persoon.

Dit artikel is niet van toepassing op :  Le présent article n'est pas applicable :  1° de sommen, renten of waarden die verkregen zijn  ingevolge een beding dat aan de schenkbelasting of het  registratierecht op de schenkingen onder de levenden is  onderworpen;

2° de renten en kapitalen die gevestigd zijn ter uitvoering  van een wettelijke verplichting;

3° de renten en kapitalen die door tussenkomst van de  werkgever van de erflater, of door tussenkomst van de  werkgever van de langstlevende echtgenoot van de  erflater die met de erflater gehuwd was onder een stelsel  van gemeenschap, gevestigd zijn in het voordeel van de  langstlevende echtgenoot van de erflater of zijn kinderen  die de leeftijd van eenentwintig jaar niet hebben bereikt,  tot  uitvoering  van  hetzij  een  groepsverzekeringscontract, onderschreven ingevolge  een bindend reglement van de onderneming dat  beantwoordt aan de voorwaarden, gesteld door de  reglementering betreffende de controle van dergelijke  contracten, hetzij het bindend reglement van een  voorzorgsfonds, opgericht in het voordeel van het  personeel van de onderneming;

4° de sommen, renten of waarden die bij het overlijden  van de erflater worden verkregen ingevolge een contract  dat een door een derde in het voordeel van de verkrijger  gemaakt beding bevat, als er bewezen wordt dat die  derde kosteloos in het voordeel van de verkrijger heeft  bedongen.

---- historiek ----  ---- historique ----

- gewijzigd door art. 32 van het decreet van 20.12.2024  (B.S. 30.12.2024). Inwerkingtreding op 01.01.2025 en

- gewijzigd door art. 11 van het decreet van 09.12.2022  (B.S. 20.12.2022). Inwerkingtreding: 30.12.2022

- gewijzigd door art. 34 van het decreet van 23.12.2016  (B.S.: 30.12.2016). Tekst in werking getreden voor  overlijdens vanaf 1 januari 2017

- toegevoegd door art. 10 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.1.0.7  Art. 2.7.1.0.7

De roerende en onroerende goederen die wat betreft het  vruchtgebruik door de erflater en wat betreft de blote  eigendom door een derde onder bezwarende titel zijn  verkregen, worden, voor de heffing van de erfbelasting,  geacht in volle eigendom in zijn nalatenschap aanwezig  te zijn en als legaat door die derde te zijn verkregen.  Hetzelfde geldt voor effecten aan toonder of op naam en  voor geldbeleggingen die voor het vruchtgebruik  ingeschreven zijn op naam van de erflater en voor de  blote eigendom op naam van een derde.

Het eerste lid is niet van toepassing :  L'alinéa premier ne s'applique pas

1° als wordt bewezen dat de verkrijging geen bedekte  bevoordeling van de derde is;

1° s'il est établi que l'acquisition ne déguisait pas une  libéralité au profit du tiers ;  2° als de erflater langer heeft geleefd dan de derde of als  de derde niet behoort tot de personen, vermeld in artikel  2.7.3.4.4, eerste, tweede en derde lid.

---- historiek ----  ---- historique ----

- toegevoegd door art. 11 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.1.0.8.  Art. 2.7.1.0.8.

Als aan de erflater bij een verdeling of bij een met  verdeling gelijkgestelde akte een vruchtgebruik, een  rente of elk ander recht toebedeeld is dat vervalt  ingevolge zijn overlijden, wordt de verrichting voor de  heffing van de erfbelasting gelijkgesteld met een legaat  in het voordeel van de deelgenoten van de erflater, de  verkrijgers van de blote eigendom of de personen die  belast zijn met het levenslange recht, in de mate waarin  die deelgenoten, verkrijgers of personen boven hun deel  in de onverdeeldheid goederen in eigendom hebben  verkregen.

Het eerste lid is niet van toepassing als :  L'alinéa premier n'est pas applicable si :

1° wordt bewezen dat de verrichting geen bedekte  bevoordeling is van de verscheidene deelgenoten in de  onverdeeldheid;

2° de erflater langer heeft geleefd dan de deelgenoot in  de onverdeeldheid, de verkrijger van de blote eigendom  of de persoon die belast is met het levenslange recht, of  als de voormelde personen niet behoren tot de personen,  vermeld in artikel 2.7.3.4.4, eerste, tweede en derde lid.

---- historiek ----  ---- historique ----

- toegevoegd door art. 12 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.1.0.9.  Art. 2.7.1.0.9.

Als de roerende of onroerende goederen door de erflater  onder bezwarende titel zijn verkocht of afgestaan,  worden ze voor de heffing van de erfbelasting geacht  deel uit te maken van zijn nalatenschap en als legaat te  zijn verkregen door de verkrijger of door de overnemer  als de erflater zich volgens de overeenkomst ofwel een  vruchtgebruik heeft voorbehouden op de afgestane  goederen of op andere goederen, ofwel de afstand van  om het even welk ander levenslange recht in zijn  voordeel heeft bedongen.

Het eerste lid is niet van toepassing als :  L'alinéa premier n'est pas applicable si :  1° wordt bewezen dat de verkoop of de afstand geen  bedekte bevoordeling is van de verkrijger of van de  overnemer;

2° de erflater langer heeft geleefd dan de verkrijger of de  overnemer, of als de verkrijger of de overnemer niet  behoort tot de personen, vermeld in artikel 2.7.3.4.4,  eerste, tweede en derde lid.

---- historiek ----  ---- historique ----

- toegevoegd door art. 13 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.1.0.10.  Art. 2.7.1.0.10.

De in een testament of andere beschikking die  uitwerking heeft bij het overlijden van de beschikker,  door de erflater aan zijn erfgenaam, legataris of  begiftigde opgelegde verbintenis om aan een met naam  aangeduide derde een kapitaal of een rente te geven die  in natura in de nalatenschap niet bestaat en in geld of in  vervangbare zaken betaalbaar is, wordt voor de heffing  van het successierecht als legaat beschouwd.

De aan een erfgenaam, legataris of begiftigde opgelegde  verbintenis om ten bate van een ander iets te doen en in  het bijzonder de last, opgelegd aan de erfgenamen,  legatarissen of begiftigden, om de rechten en kosten die  verbonden zijn aan een aan een andere persoon gedaan  legaat, te dragen, worden niet beschouwd als legaat.

---- historiek ----  ---- historique ----

- toegevoegd door art. 14 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

#### Afdeling 2 – Belastingplichtigen  Section 2 – Contribuables

---- historiek ----  ---- historique ----

- afdeling 2 toegevoegd door art. 15 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.2.0.1.  Art. 2.7.2.0.1.

De belastingplichtige is degene die erfgenaam, legataris  of begiftigde is of, in voorkomend geval, de onbeheerde  nalatenschap.

---- historiek ----  ---- historique ----

- toegevoegd door art. 13 van het decreet van 08.12.2017  (B.S., 14.12.2017). De tekst is in werking getreden op  24.12.2017

- toegevoegd door art. 16 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

#### Afdeling 3 – Belastbare grondslag  Section 3 - Base imposable

---- historiek ----  ---- historique ----

- afdeling 3 toegevoegd door art. 17 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

##### Onderafdeling 1 – Algemeen  Sous-section 1re. – Généralités

---- historiek ----  ---- historique ----

- onderafdeling 1 toegevoegd door art. 18 van het decreet  van 19.12.2014 (B.S., 29.01.2015 - Ed. 2). De

tekst is in werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.3.1.1.  Art. 2.7.3.1.1.

Het successierecht wordt gevestigd op de waarde van  alles wat uit de nalatenschap van een rijksinwoner wordt  verkregen overeenkomstig afdeling 1 van dit hoofdstuk.

Het recht van overgang wordt gevestigd op de waarde  van de onroerende goederen die in België liggen en  verkregen werden overeenkomstig afdeling 1 van dit  hoofdstuk uit de nalatenschap van iemand die geen  rijksinwoner is.

---- historiek ----  ---- historique ----

- vervangen door art. 4 van het decreet van 06.07.2018  (B.S. 20.07.2018 Ed.2). Tekst treedt in werking op  01.09.2018

- toegevoegd door art. 19 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

##### Onderafdeling 2 – Actief van de nalatenschap  Sous-section 2. - Actif de la succession

---- historiek ----  ---- historique ----

- onderafdeling 2 toegevoegd door art. 20 van het decreet  van 19.12.2014 (B.S., 29.01.2015 - Ed. 2). De

tekst is in werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.3.2.1.  Art. 2.7.3.2.1.

Het successierecht wordt vastgesteld op basis van de  belastbare waarde van alle goederen die toebehoren aan  de erflater, waar ze zich ook bevinden, na aftrek van de  schulden, vermeld in onderafdeling 4, en met behoud  van de toepassing van artikel 2.7.3.2.7 en artikel  2.7.5.0.4.

---- historiek ----  ---- historique ----

- toegevoegd door art. 21 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.3.2.2.  Art. 2.7.3.2.2.

Het recht van overgang wordt vastgesteld op basis van  de belastbare waarde van alle onroerende goederen die  overeenkomstig artikel 5, § 2, 4°, tweede streepje, van  de bijzondere wet van 16 januari 1989 betreffende de  financiering van de Gemeenschappen en de Gewesten in  het Vlaamse Gewest te lokaliseren zijn, en die aan de  erflater toebehoren, na aftrek van de schulden, vermeld  in artikel 2.7.3.4.1, tweede lid.

---- historiek ----  ---- historique ----

- vervangen door art. 6 van het decreet van 17 juli 2015  (B.S., 14.08.2015 ). De tekst is in werking getreden op 14  augustus 2015 (art. 41)

###### Art. 2.7.3.2.3.  Art. 2.7.3.2.3.

Als een erfgenaam, legataris of begiftigde het  vruchtgebruik of de blote eigendom verkrijgt van een  goed waarvan de volle eigendom van de nalatenschap  afhangt, of als hij een door de erflater gevestigde  periodieke rente of pensioen ontvangt, wordt de  belastbare grondslag bepaald overeenkomstig de regels,  vermeld in artikel 2.7.3.3.2 en artikel 2.7.3.3.3.

Als de erflater de rente of prestatie voor een onbepaalde  tijd ten voordele van een rechtspersoon vestigt, bedraagt  de belastbare grondslag twintig keer het jaarlijkse  bedrag.

Als die rente of prestatie voor een bepaalde tijd is  gevestigd, is de belastbare grondslag gelijk aan de  gekapitaliseerde waarde op de dag van het overlijden  van de jaarlijkse rente of prestatie tegen een rentevoet  van 4%, waarbij die waarde niet meer mag bedragen dan  twintig keer het jaarlijkse bedrag van de rente of  prestatie.

Dezelfde regels zijn van toepassing als het gaat om een  vruchtgebruik, gevestigd ten voordele van een  rechtspersoon, met dien verstande dat voor de grondslag

Les mêmes règles sont applicables s'il s'agit d'un  usufruit constitué sur la tête d'une personne morale, sauf  à prendre pour base d'évaluation le revenu annuel des  van de raming de jaarlijkse opbrengst van de goederen  bepaald wordt overeenkomstig artikel 2.7.3.3.2, eerste  lid, 6°.

Als de lijfrente, de levenslange prestatie of het  vruchtgebruik gezamenlijk of achtereenvolgens ten  voordele van twee of meer natuurlijke personen wordt  gevestigd met een beding van aanwas, wordt de  belastbare  grondslag  voor  de  heffing  van  de  opvorderbare belasting op het ogenblik van de aanwas  bepaald volgens de leeftijd die de genieter op dat  ogenblik heeft.

---- historiek ----  ---- historique ----

- toegevoegd door art. 23 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.3.2.4.  Art. 2.7.3.2.4.

Met behoud van de toepassing van artikel 2.7.3.2.1  bestaat er voor de heffing van de erfbelasting, alsook van  de belastingverhogingen, tot bewijs van het tegendeel,  een wettelijk vermoeden van eigendom in de volgende  gevallen :

1° voor onroerende goederen : als ze voor de onroerende  voorheffing zijn ingekohierd op naam van de erflater en  die daarvoor een betaling heeft gedaan;

2° voor hypothecaire renten en schuldvorderingen : als  ze op naam van de erflater in de registers van de  hypothecaire openbaarmaking of in de registers van het  Belgisch Scheepsregister zijn ingeschreven;

3° voor de schuldvorderingen op de Belgische Staat : als  ze op naam van de erflater in het Grootboek van de  Staatsschuld zijn opgenomen;

4°  voor  obligaties,  aandelen  of  andere  schuldvorderingen op provincies, gemeenten, openbare  instellingen en stichtingen van openbaar nut van het Rijk  : als ze op naam van de erflater in hun registers en  rekeningen ingeschreven zijn.

---- historiek ----  ---- historique ----

- gewijzigd door art. 8 van het decreet van 21.12.2018  (B.S. 28.12.2018). Tekst treedt in werking op 07.01.2019

- toegevoegd door art. 24 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.3.2.5.  Art. 2.7.3.2.5.  Voor de heffing van de erfbelasting, alsook van de  belastingverhoging wegens het gebrek aan aangifte of  het verzuim bepaalde goederen aan te geven, is het  bestaan van een roerend of onroerend goed, tot bewijs  van het tegendeel, voldoende vastgesteld bij de akten  van eigendom die ten bate van de erflater of op zijn  verzoek zijn verleden.

Voor lichamelijke roerende goederen, contant geld en  effecten aan toonder bestaat het wettelijk vermoeden,  vermeld in het eerste lid, alleen op voorwaarde dat de  akten niet sinds meer dan vijf jaar vóór het overlijden  bestaan. Als dat wel het geval is, kan het bestaan van die  akten door de bevoegde entiteit van de Vlaamse  administratie alleen ingeroepen worden als een element  van vermoeden als vermeld in artikel 3.17.0.0.1.

---- historiek ----  ---- historique ----

- gewijzigd door art. 33 van het decreet van 20.12.2024  (B.S. 30.12.2024). Inwerkingtreding op 01.01.2025 en  van toepassing is op de akten van eigendom die ten bate  van de erflater of op zijn verzoek zijn verleden vanaf 1  januari 2025

- gewijzigd door art. 4 van het decreet van 15.03.2024  (B.S. 20.03.2024). Inwerkingtreding: 30.03.2024

- toegevoegd door art. 25 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.3.2.6.  Art. 2.7.3.2.6.

Voor de heffing van het successierecht wordt het  volgende, behoudens tegenbewijs, geacht aan de erflater  voor een gelijk deel per hoofd toe te behoren :

1° de effecten, sommen, waarden of om het even welke  voorwerpen die gedeponeerd zijn in een brandkast die  door de erflater en door een of meer andere personen  samen of solidair wordt gehuurd of als gehuurd wordt  beschouwd met toepassing van artikel 3.13.1.3.7;

2° de gehouden zaken en de verschuldigde sommen,  vermeld in artikel 99 van het federale Wetboek van  Successierechten.

Het volgende wordt, behoudens tegenbewijs, geacht in  het geheel toe te behoren aan de erflater :

1° de effecten, sommen, waarden of om het even welke  voorwerpen die zich bevinden in een brandkast die door  de erflater alleen wordt gehuurd of als gehuurd wordt  beschouwd met toepassing van artikel 3.13.1.3.7;

2° de effecten, sommen, waarden of om het even welke  voorwerpen die in een gesloten koffer, omslag of colli  op naam van de erflater alleen gedeponeerd zijn bij de  natuurlijke personen of rechtspersonen.

---- historiek ----  ---- historique ----

- toegevoegd door art. 26 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.3.2.7.  Art. 2.7.3.2.7.

Voor de inning van het successierecht in rechte  nederdalende  lijn  of  tussen  echtgenoten  met  gemeenschappelijke  kinderen  of  afstammelingen  worden de terugnemingen en vergoedingen die  verbonden zijn hetzij aan de gemeenschap die heeft  bestaan tussen de erflater en een echtgenoot, met wie de  erflater bij het overlijden levende kinderen of  afstammelingen heeft, hetzij aan de gemeenschap die  tussen de verwanten in de opgaande lijn van de erflater  heeft bestaan, niet in aanmerking genomen.

---- historiek ----  ---- historique ----

- tweede lid opgeheven door art.5 van het decreet van  06.07.2018 (B.S. 20.07.2018 Ed.2). Tekst treedt in

werking op 01.09.2018

- toegevoegd door art. 27 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.3.2.8.  Art. 2.7.3.2.8.

§ 1. Als de erflater gehuwd was onder een stelsel van  gemeenschap van goederen, worden de sommen, renten  of waarden, vermeld in artikel 2.7.1.0.6, die aan de  echtgenoot als legaat toevallen voor het volledige bedrag  ervan, als legaat belast als ze zijn verkregen als  tegenwaarde voor de eigen goederen van de erflater. Ze  worden slechts voor de helft belast in alle andere  gevallen. Het recht is niet verschuldigd als er bewezen  wordt dat de sommen, renten of waarden verkregen zijn  als tegenwaarde voor eigen goederen van de echtgenoot.  De omstandigheid dat het beding wederkerig is,  ontneemt de aard van bevoordeling niet daaraan.

De verkrijging wordt vermoed kosteloos te zijn  ontvangen, behoudens tegenbewijs.

§ 2. In het geval van een levensverzekeringscontract  wordt de belastbare grondslag van de sommen, renten of  waarden, die aan de persoon, vermeld in artikel  2.7.1.0.6, kunnen toekomen, verminderd met het bedrag  dat als belastbare grondslag heeft gediend voor de  heffing van de schenkbelasting indien het contract door  de erflater aan die persoon werd geschonken.

---- historiek ----  ---- historique ----

- gewijzigd door art. 35 van het decreet van 23.12.2016  (B.S.: 30.12.2016). Tekst in werking getreden op  08.01.2017

- toegevoegd door art. 28 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.3.2.9.  Art. 2.7.3.2.9.

Als er schenkingen onder de levenden als vermeld in  artikel 3.3.1.0.8, § 1, eerste lid, 12°, bestaan, wordt de  basis waarop de schenkbelasting is geheven of zou  moeten worden geheven, gevoegd bij de erfgoederen  van  de  belanghebbenden  om  de  progressieve  erfbelasting die op die erfgoederen van toepassing is, te  bepalen.

Het eerste lid is niet van toepassing op :  L'alinéa premier ne s'applique pas aux :

1° schenkingen onder de levenden van percelen grond  die volgens de stedenbouwkundige voorschriften  bestemd zijn voor woningbouw en waarop de  schenkbelasting, vermeld in artikel 2.8.4.2.1, tabel I, is  geheven;

2° schenkingen onder de levenden van roerende  goederen waarop de schenkbelasting, vermeld in artikel  2.8.4.1.1, § 2, is geheven;

3° schenkingen onder de levenden van ondernemingen  waarop voor 1 januari 2012 het recht, vermeld in artikel  140bis van het Wetboek van Registratie-, Hypotheek-,  en Griffierechten, is geheven of waarvoor vanaf 1  januari 2012 de vrijstelling, vermeld in artikel 2.8.6.0.3,  is toegepast.

4° schenkingen onder de levenden van onbebouwde  onroerende goederen voor het gedeelte waarop de  vrijstelling, vermeld in artikel 2.8.6.0.8, is toegepast.

---- historiek ----  ---- historique ----

- gewijzigd door art. 13 van het decreet van 03.04.2026  (B.S., 23.04.2026). Inwerkingtreding: 03.05.2026

- punt 4° toegevoegd door art. 10 van het decreet van  22.12.2017. Tekst treedt in werking op 09.06.2018 (art. 1  besluit 04.05.2018 B.S. 30.05.2018)

- toegevoegd door art. 29 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.3.2.10.  Art. 2.7.3.2.10.

Als de verkrijger binnen zes maanden na het overlijden  van de erflater sterft, wordt voor de berekening van de  erfbelasting op de nalatenschap van die laatste geen  rekening gehouden met hetgeen de verkrijger in  vruchtgebruik of als levenslange of periodieke rente of  als pensioen heeft verkregen.

---- historiek ----  ---- historique ----

- gewijzigd door art. 5 van het decreet van 15.03.2024  (B.S. 20.03.2024). Inwerkingtreding: 30.03.2024

- toegevoegd door art. 30 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.3.2.11.  Art. 2.7.3.2.11.

Als in de gevallen, vermeld in artikel 2.7.1.0.7, 2.7.1.0.8  en 2.7.1.0.9, niet bewezen wordt dat de verrichting geen  bedekte bevoordeling is, maar kan worden bewezen dat  de erflater werkelijk het levenslange recht genoten heeft,  wordt op de belastbare grondslag op de dag van het  openvallen van de nalatenschap een evenredige  vermindering toegepast, conform artikel 2.7.3.3.4 en  artikel 2.7.3.3.5. Daarbij wordt rekening gehouden met  de waarde van het bedoelde levenslange recht dat wordt  gekapitaliseerd tegen 4%, volgens het werkelijke aantal  volle jaren dat de erflater het recht genoten heeft. Als het  gaat om een vruchtgebruik of een ander zakelijk  levenslang recht, wordt de waarde van het in aanmerking  te nemen jaarlijkse inkomen forfaitair vastgesteld op 4%  van de waarde van de volle eigendom van het goed op  de dag van het contract.

---- historiek ----  ---- historique ----

- toegevoegd door art. 31 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.3.2.12.  Art. 2.7.3.2.12.

§ 1. Op hetgeen een persoon met een handicap of een  gehandicapt kind verkrijgt, wordt een abattement  toegepast voor de som die verkregen is door toepassing  van de volgende formule :

1° (3000 euro) x (cijfer, aangeduid in artikel 2.7.3.3.2,  eerste lid, 5°, volgens de leeftijd van de verkrijger) als  de verkrijging onderworpen is aan het tarief, vermeld in  tabel I van artikel 2.7.4.1.1;

2° (1000 euro) x (cijfer, aangeduid in artikel 2.7.3.3.2,  eerste lid, 5°, volgens de leeftijd van de verkrijger) als  de verkrijging onderworpen is aan het tarief, vermeld in  tabel II van artikel 2.7.4.1.1.

§ 2. Als een persoon met een handicap of een  gehandicapt kind als vermeld in paragraaf 1,  onderworpen is aan het tarief, vermeld in tabel I van  artikel 2.7.4.1.1, wordt het bedrag van het abattement  eerst toegerekend op zijn overeenkomstig artikel  2.7.4.1.1, § 2, derde lid, of artikel  2.7.6.0.6 niet vrijgestelde gedeelte van het netto  onroerend aandeel, vervolgens op zijn overeenkomstig  artikel 2.7.6.0.6 niet vrijgestelde gedeelte van het netto  roerend aandeel en bij uitputting van dat aandeel tot slot  op de belastbare grondslag waarop het verlaagde tarief  voor familiale ondernemingen en vennootschappen, met  toepassing van artikel 2.7.4.2.2, wordt berekend.

Als een persoon met een handicap of een gehandicapt  kind als vermeld in paragraaf 1, samen met personen op  wie

het tarief `tussen anderen' van toepassing is,  onderworpen is aan het tarief, vermeld in tabel II van  artikel 2.7.4.1.1, wordt, in afwijking van artikel  2.7.4.1.1, de belasting voor de persoon met een handicap  of het gehandicapte kind berekend alsof hij als enige  voor de nettoverkrijging van de nalatenschap in  aanmerking komt. Voor de andere verkrijgers wordt  conform artikel 2.7.4.1.1 de belasting berekend alsof de  persoon met een handicap of het gehandicapte kind die  hoedanigheid niet heeft.

§ 3. Als een persoon met een handicap als vermeld in  paragraaf 1, volledig of gedeeltelijk onderworpen is aan  het tarief, vermeld in tabel II van artikel 2.7.4.1.1, § 1,  wordt het bedrag van het abattement eerst toegerekend  op het gedeelte van de verkrijging dat onderworpen is  aan het tarief, vermeld in tabel II van artikel 2.7.4.1.1, §  1, en bij uitputting van dat aandeel op de belastbare  grondslag waarop het verlaagde tarief wordt berekend,  met toepassing van artikel 2.7.4.2.5.

---- historiek ----  ---- historique ----

- gewijzigd door art. 16 van het decreet van 19.12.2025  (B.S. 30.12.2025). Inwerkingtreding: van toepassing op  alle nalatenschappen die openvallen vanaf 1 januari  2026.

- gewijzigd door art. 12 van het decreet van 09.12.2022  (B.S. 20.12.2022). Inwerkingtreding: 30.12.2022

- gewijzigd door art.6 van het decreet van 06.07.2018  (B.S. 20.07.2018 Ed.2). Tekst treedt in werking op  01.09.2018

- toegevoegd door art. 32 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.3.2.13.  Art. 2.7.3.2.13.

In geval van legaat van een geldsom of van legaat van  een periodieke rente of pensioen wordt het bedrag van  de gelegateerde geldsom of het kapitaal waarop het  successierecht naar rato van de bedoelde rente of het  pensioen wordt geheven, voor de berekening van de  rechten afgetrokken van de nettoverkrijging van de  erfgenaam, legataris of begiftigde die het legaat van de  geldsom, de rente of het pensioen moet uitbetalen.

---- historiek ----  ---- historique ----

- toegevoegd door art. 33 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.3.2.14.  Art. 2.7.3.2.14.

Voor de inning van het successierecht worden andere  schuldvorderingen dan de schuldvorderingen, vermeld  in artikel 2.7.3.2.7, die voortkomen uit de toepassing van  een beding in een huwelijksovereenkomst dat door de  erflater en zijn partner is overeengekomen en dat  betrekking  heeft  op  de  vereffening  van  hun  huwelijksvermogensstelsel,  niet  in  aanmerking  genomen.

---- historiek ----  ---- historique ----

- ingevoegd door art. 14 van het decreet van

08.12.2017 (B.S., 14.12.2017). De tekst is in werking  getreden op 24.12.2017

###### Art. 2.7.3.2.1

5 . Art. 2.7.3.2.15.

Als er zich onder de erfgenamen, legatarissen of  begiftigden een of meer legatarissen bevinden van wie  het legaat onder de toepassing van artikel 2.7.4.2.1 valt,  wordt om de rechten te berekenen:

1° voor de legatarissen, vermeld in artikel 2.7.4.2.1, het  eventuele bedrag om de erfbelasting van andere  erfgenamen, legatarissen of begiftigden te voldoen,  gedeeld door (1 - het marginale tarief dat is toegepast om  dat bedrag te berekenen) en begrensd tot het legaat zelf,  niet in aanmerking genomen voor de belastbare  grondslag;

2° voor de andere erfgenamen, legatarissen of  begiftigden, vermeld in punt 1°, het eventuele bedrag,  vermeld in punt 1°, in aanmerking genomen voor de  belastbare grondslag.

---- historiek ----  ---- historique ----

- Ingevoegd door art. 2 van het decreet van 19.03.2021  (B.S., 07.04.2021). Inwerkingtreding: 01.07.2021. Van  toepassing op nalatenschappen die opengevallen zijn  vanaf 1 juli 2021

##### Onderafdeling 3 – Waardering van het actief  Sous-section 3 - Valorisation de l'actif

---- historiek ----  ---- historique ----

- onderafdeling 3 toegevoegd door art. 34 van het decreet  van 19.12.2014 (B.S., 29.01.2015 - Ed. 2). De

tekst is in werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.3.3.1.  Art. 2.7.3.3.1.

De belastbare waarde van de goederen die het actief van  de nalatenschap van een rijksinwoner uitmaken en van  de onroerende goederen die onderworpen zijn aan het  recht van overgang, is de door de aangevers te schatten  verkoopwaarde op de dag van het overlijden.

In afwijking van het eerste lid wordt voor de waardering  van de goederen waarvan de erflater schijnbaar eigenaar  was,  geen  rekening  gehouden  met  de  waardevermindering die zou kunnen voortspruiten uit de  wederroepelijkheid van de titel van verkrijging van de  erflater.

---- historiek ----  ---- historique ----

- toegevoegd door art. 35 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.3.3.2.  Art. 2.7.3.3.2.

In afwijking van artikel 2.7.3.3.1 wordt de belastbare  waarde van de goederen die tot de nalatenschap behoren,  als volgt vastgesteld :

1° voor de onroerende goederen die in het buitenland  liggen, waarvan de verkoopwaarde niet blijkt uit akten  en bescheiden : twintig of dertig keer de jaarlijkse  opbrengst van de goederen of de prijs van de lopende  huurcelen, zonder aftrek van de aan de huurder of aan de  pachter opgelegde lasten, naargelang het gaat om  bebouwde eigendommen of onbebouwde eigendommen.  De belastbare waarde mag in geen geval lager zijn dan  de waarde die tot grondslag gediend heeft voor de  heffing van de belasting in het buitenland;

2° voor het kapitaal en de interesten die vervallen zijn of  die verkregen zijn van de schuldvorderingen : het  nominale bedrag van dat kapitaal en van die interesten.  In geval van onvermogen van de schuldenaar of van het  bestaan  van  elke  andere  oorzaak  van  waardevermindering  mogen  de  aangevers  de  schuldvordering op haar verkoopwaarde schatten;

3° voor financiële instrumenten die toegelaten zijn tot  verhandeling  op  Belgische  of  buitenlandse

4° voor de altijddurende of voor een onbepaalde tijd  gevestigde erfpachten, grondrenten en andere prestaties,  alsook  voor  de  al  dan  niet  gehypothekeerde  altijddurende renten : twintig keer de rente of de  jaarlijkse prestatie. In geval van onvermogen van de  schuldenaar  of  bij  een  andere  oorzaak  van  waardevermindering mogen de aangevers de rente of  prestatie op haar verkoopwaarde schatten;

5° voor de op het hoofd van een derde gevestigde  lijfrenten en andere levenslange uitkeringen : door de  vermenigvuldiging van het jaarlijkse bedrag van de  uitkering met de leeftijdscoëfficiënt uit de onderstaande  tabel :

Leeftijdscoëfficiënt

/  Coefficient d'âge

/  âge de celui sur la tête de qui la rente est créée  18  ≤ 20  17  > 20-30  16  > 30-40  14  > 40-50  13  > 50-55  11  > 55-60  9,5  > 60-65  8  > 65-70  6  > 70-75  4  > 75-80  2  > 80

6° voor het op het hoofd van een derde gevestigde  vruchtgebruik : de jaarlijkse opbrengst van de goederen,  berekend tegen 4% van de waarde van de volle  eigendom, te vermenigvuldigen met het cijfer, vermeld  in punt 5° ;

7° voor de voor een beperkte tijd gevestigde renten of  prestaties : de som die door de kapitalisatie van de renten  of prestaties tegen 4% op de datum van het overlijden  wordt vertegenwoordigd, onder voorbehoud dat het  bedrag van de kapitalisatie, al naargelang het geval, de  belastbare waarde, zoals die in punt 4° en punt 5° wordt  bepaald, niet te boven gaat. Dezelfde regel is van  toepassing als het gaat over een voor een beperkte tijd  gevestigd vruchtgebruik, waarbij de opbrengst van de

8° voor de blote eigendom : de waarde van de volle  eigendom, onder aftrek van de waarde van het  vruchtgebruik, berekend conform dit artikel en artikel  2.7.3.3.3. Er vindt geen aftrek plaats als het  vruchtgebruik met toepassing van artikel 2.7.3.2.10 vrij  is van erfbelasting.

Voor de toepassing van het eerste lid, 3°, kunnen de  aangevers kiezen uit de beurswaarde op de datum van  het overlijden, de beurswaarde op de datum van één  maand na het overlijden of de beurswaarde op de datum  van twee maanden na het overlijden. Als er op een van  die data geen notering is, geldt de beurswaarde op de  eerstvolgende dag waarop er opnieuw een notering  wordt vastgesteld. Als er op de gekozen datum voor  bepaalde van de aan te geven waarden wel en voor  andere geen notering is, moeten laatstbedoelde waarden  worden aangegeven volgens de beurswaarden op de  eerstvolgende dag waarop er wel een notering is. De  aangevers mogen slechts een van de voormelde data  kiezen, die zal gelden voor al de nagelaten waarden. De  aangevers geven hun keuze aan in de aangifte, waarin ze  ook de door hen geraadpleegde bron voor de opgegeven  beurswaarden vermelden.

---- historiek ----  ---- historique ----

- toegevoegd door art. 36 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.3.3.3.  Art. 2.7.3.3.3.

Het recht van gebruik en het recht van bewoning, alsook  het recht op vruchten, inkomsten of opbrengsten worden  voor de toepassing van artikel 2.7.3.3.2 en van artikel  2.7.3.2.3 met vruchtgebruik gelijkgesteld.

Als de lijfrente, de levenslange prestatie of het  vruchtgebruik op het hoofd van twee of meer personen  is gevestigd, is de in aanmerking te nemen leeftijd die  van de jongste persoon.

---- historiek ----  ---- historique ----

- toegevoegd door art. 37 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.3.3.4.  Art. 2.7.3.3.4.

De belastbare waarde (X) van de goederen die het  voorwerp uitmaken van de verrichting, vermeld in  artikel 2.7.1.0.8, wordt als volgt bepaald :

De parameters, vermeld in het eerste lid, worden als  volgt gedefinieerd :

1° a = het bedrag van de bedekte bevoordeling op de dag  van de verrichting;

2° b = de waarde van de goederen die op de dag van het  overlijden in eigendom toebedeeld zijn aan de  deelgenoten;

3° c = de waarde van de goederen die op de dag van de  verrichting in eigendom toebedeeld zijn.

---- historiek ----  ---- historique ----

- toegevoegd door art. 38 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.3.3.5.  Art. 2.7.3.3.5.

De belastbare waarde (X) van de goederen die het  voorwerp uitmaken van een verkoop of afstand als  vermeld in artikel 2.7.1.0.9, wordt, als de erflater  daarenboven de overlating van een goed in eigendom in  zijn voordeel heeft bedongen, als volgt bepaald :

a x b  𝑥 =

De parameters, vermeld in het eerste lid, worden als  volgt gedefinieerd :

1° a = het bedrag van de bedekte bevoordeling op de dag  van de verkoop of de afstand;

2° b = de waarde van de door de erflater verkochte of  afgestane goederen op de dag van het overlijden;

3° c = de waarde van de door de erflater verkochte of  afgestane goederen op de dag van de verkoop of de  afstand.

---- historiek ----  ---- historique ----

- toegevoegd door art. 39 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.3.3.6.  Art. 2.7.3.3.6.

De zekere schuldvorderingen waarvan het bedrag op het  ogenblik van het overlijden onbepaald is, worden in de  aangifte voor de waarde ervan opgenomen, behoudens

---- historiek ----  ---- historique ----

- toegevoegd door art. 40 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.3.3.7.  Art. 2.7.3.3.7.

In de gevallen, vermeld in artikel 3.3.1.0.6, eerste lid,  moet de waarde van de goederen op de dag van het  vonnis, van de dading of van de gebeurtenis die het  uitgangspunt vormt van de termijn voor de indiening van  de aangifte, vermeld in artikel 3.3.1.0.6, vierde lid, als  belastbare waarde worden aangegeven.

---- historiek ----  ---- historique ----

- toegevoegd door art. 41 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

##### Onderafdeling 4 – Passief van de nalatenschap  Sous-section 4 - Passif de la succession

---- historiek ----  ---- historique ----

- onderafdeling 4 toegevoegd door art. 42 van het decreet  van 19.12.2014 (B.S., 29.01.2015 - Ed. 2). De

tekst is in werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.3.4.1.  Art. 2.7.3.4.1.

Als passief van de nalatenschap van een rijksinwoner  wordt alleen het volgende aanvaard :

1° de schulden van de erflater die op de dag van zijn  overlijden bestaan. Andere schulden dan de schulden,  vermeld in artikel 2.7.3.2.7, die voortkomen uit de  toepassing  van  een  beding  in  een  huwelijksovereenkomst dat door de erflater en zijn  partner is overeengekomen en dat betrekking heeft op de  vereffening van hun huwelijksvermogensstelsel worden  niet beschouwd als schulden van de erflater die op de  dag van zijn overlijden bestaan;

2° de begrafeniskosten.  2° aux frais funéraires.

Als passief van de nalatenschap van een erflater die geen  rijksinwoner is, maar die zijn domicilie of de zetel van  zijn vermogen binnen de Europees Economische Ruimte  had, worden alleen de schulden aanvaard waarvan de  aangevers het bewijs leveren dat ze specifiek zijn  aangegaan om de onroerende goederen te verwerven of  te behouden.

Het bedrag van de regularisatieheffing die is geheven en  betaald in uitvoering van een federale wet die een  systeem van fiscale regularisatie voorziet, wordt  gelijkgesteld met een schuld van de erflater als vermeld  in het eerste lid, 1°. Die schuld wordt alleen als passief  van de nalatenschap aanvaard als al de volgende  voorwaarden zijn vervuld:

1° de geregulariseerde inkomsten of kapitalen en de  activa in kwestie die die inkomsten hebben gegenereerd,  zijn aangegeven in een aangifte van nalatenschap;

2° de inkomsten en bedragen die zijn aangegeven in de  regularisatieaangifte  en  waarvoor  de  regularisatieheffing is betaald, zijn door de erflater  behaald of verkregen.

---- historiek ----  ---- historique ----

- gewijzigd door art. 31 van het decreet van 19.12.2025  (B.S., 30.12.2025). Inwerkingtreding: 01.01.2026

- 1° vervangen door art. 15 van het decreet van  08.12.2017 (B.S., 14.12.2017). De tekst is in werking  getreden op 24.12.2017

- toegevoegd door art. 43 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.3.4.2.  Art. 2.7.3.4.2.

De schulden van de erflater die op de dag van het  overlijden bestaan, worden forfaitair bepaald op 1500  euro.

In afwijking van het eerste lid wordt het forfait voor de  schulden van de gemeenschap bepaald op 3000 euro als  de erflater gehuwd was onder een stelsel van  gemeenschap. Hiervan kan de helft in het passief van de  nalatenschap worden opgenomen.

Het forfait, vermeld in het eerste lid, en het forfait,  vermeld in het tweede lid, kunnen niet gecombineerd,  noch gecumuleerd worden.

De schulden die specifiek zijn aangegaan om onroerende  goederen te verwerven of te behouden, zijn uitgesloten  uit het forfaitaire bedrag, vermeld in het eerste en tweede  lid.

De bedragen, vermeld in het eerste, tweede en vijfde lid,  zijn gekoppeld aan de schommelingen van het algemene  indexcijfer van de consumptieprijzen van het Rijk. De  bedragen worden jaarlijks op 1 januari aangepast op  basis van een coëfficiënt die verkregen wordt door het  gemiddelde van de maandelijkse indexcijfers van het  jaar dat voorafgaat aan het jaar, te delen door het  gemiddelde van de indexcijfers van het jaar 2014. Het  gemiddelde van de maandelijkse indexcijfers wordt  afgerond op het hogere of lagere honderdste naargelang  het cijfer van de duizendsten al of niet vijf bereikt, en de  coëfficiënt wordt afgerond op het hogere of lagere  tienduizendste  naargelang  het  cijfer  van  de  honderdduizendsten al of niet vijf bereikt. Na de  toepassing van die coëfficiënt worden de bedragen  afgerond op de cent.

Les montants visés aux premier, deuxième et cinquième  alinéas sont liés aux fluctuations de l'indice général des  prix à la consommation du Royaume. Les montants sont  adaptés chaque année au 1er janvier sur la base d'un  coefficient obtenu en divisant la moyenne des indices  mensuels de l'année qui précède l'année par la moyenne  des indices mensuels de l'année 2014. La moyenne des  indices mensuels est arrondie au centième supérieur ou  inférieur selon que le chiffre des millièmes s’élève à  cinq ou non, et le coefficient est arrondi au dix millième  supérieur ou inférieur selon que le chiffre des cent  millièmes s’élève à cinq ou non. Après application de ce  coefficient, les montants sont arrondis au centime.

---- historiek ----  ---- historique ----

- gewijzigd door art. 36 van het decreet van 23.12.2016  (B.S.: 30.12.2016). Tekst in werking getreden op  08.01.2017

- vervangen door art. 7 van het decreet van 17 juli 2015  (B.S., 14.08.2015 ). De tekst is in werking getreden op 14  augustus 2015 (art. 41)

---- info ----  ---- info ----

Bericht in verband met de automatische indexering  inzake erfbelasting - Aanslagjaar 2016

###### Art. 2.7.3.4.3.  Art. 2.7.3.4.3.

De schulden en schuldbekentenissen, vermeld in artikel  2.7.1.0.3, worden niet aanvaard als passief van de  nalatenschap.

---- historiek ----  ---- historique ----

- toegevoegd door art. 45 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.3.4.4.  Art. 2.7.3.4.4.

De schulden die aangegaan zijn door de erflater in het  voordeel van een van zijn erfgenamen, legatarissen of  begiftigden of van tussenpersonen, worden niet  aanvaard als passief van de nalatenschap.

Het eerste lid is van toepassing op de schulden die door  de erflater aangegaan zijn :

1° in het voordeel van erfgenamen die hij bij uiterste  wilsbeschikking of bij contractuele beschikking uit zijn  nalatenschap heeft gesloten;

2° in het voordeel van erfgenamen, legatarissen of  begiftigden die de nalatenschap ofwel de uiterste  wilsbeschikking of de contractuele beschikking die in  hun voordeel was gemaakt, hebben verworpen.

De personen, vermeld in artikel 4.144, tweede lid, van  het Burgerlijk Wetboek, worden als  tussenpersonen beschouwd.

1° als het bewijs van de echtheid ervan door de  aangevers wordt aangevoerd;

2° als ze de verkrijging, de verbetering, het behoud of  het opnieuw verkrijgen van een goed dat op de dag van  het overlijden van de erflater tot zijn boedel behoorde,  tot onmiddellijke en rechtstreekse oorzaak hebben.

---- historiek ----  ---- historique ----

- gewijzigd door art. 6 van het decreet van 15.03.2024  (B.S. 20.03.2024). Inwerkingtreding: 30.03.2024

- toegevoegd door art. 46 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

##### Onderafdeling 5 – Aanrekening van het passief op het

actief

---- historiek ----  ---- historique ----

- onderafdeling 5 toegevoegd door art. 47 van het decreet  van 19.12.2014 (B.S., 29.01.2015 - Ed. 2). De

tekst is in werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.3.5.1.  Art. 2.7.3.5.1.

De nettoverkrijging wordt bepaald door het aandeel dat  de erfgenaam, legataris of begiftigde in de belastbare  waarde van de goederen verkrijgt, te verminderen met  het passief dat op die goederen moet worden  aangerekend, volgens de regels, vermeld in artikel  2.7.3.5.2.

---- historiek ----  ---- historique ----

- toegevoegd door art. 48 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.3.5.2.  Art. 2.7.3.5.2.

Voor de toepassing van artikel 2.7.4.1.1 worden niet-  specifieke  schulden  en  begrafeniskosten  eerst  aangerekend op de goederen, vermeld in artikel  2.7.4.2.2, vervolgens op de roerende goederen en ten  slotte op de onroerende goederen.

Als de langstlevende partner een deel verkrijgt in de  gezinswoning, wordt zijn aandeel in de schulden van de  nalatenschap, die specifiek zijn aangegaan om de  gezinswoning te verwerven of te behouden, eerst  aangerekend op de waarde van zijn deel in de  gezinswoning. Wanneer zijn deel in de gezinswoning  ontoereikend is voor de aanrekening van de volledige  schuld, wordt het overblijvende gedeelte aangerekend  zoals een specifiek onroerende schuld. Alle andere  schulden van de langstlevende partner volgen,  naargelang het geval, de toerekening voorzien in het  eerste lid of het tweede lid, en worden pas in laatste  instantie aangerekend op de waarde van zijn deel in de  gezinswoning.

---- historiek ----  ---- historique ----

- gewijzigd door art. 11 van het decreet van 22.12.2017  (B.S., 21.02.2018). Tekst treedt in werking op 09.06.2018  (art. 1 besluit 04.05.2018 B.S. 30.05.2018)

- vervangen door art. 8 van het decreet van 17 juli 2015  (B.S., 14.08.2015 ). De tekst is in werking getreden op 14  augustus 2015 (art. 41)

#### Afdeling 4 – Tarieven  Section 4 – Tarifs

---- historiek ----  ---- historique ----

- afdeling 4 toegevoegd door art. 50 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

##### Onderafdeling 1 - Algemene bepalingen  Sous-section 1re - Dispositions générales

---- historiek ----  ---- historique ----

- onderafdeling 1 toegevoegd door art. 51 van het decreet  van 19.12.2014 (B.S., 29.01.2015 - Ed. 2). De

tekst is in werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.4.1.1.  Art. 2.7.4.1.1.

§ 1er. L'impôt de succession est calculé selon le tarif  mentionné dans les tableaux ci-dessous :

§ 1. De erfbelasting wordt berekend volgens het tarief,  vermeld in de onderstaande tabellen :

TABEL I : tarief voor een verkrijging in rechte lijn en tussen partners

/  TABLEAU I : tarif pour une acquisition en ligne directe et entre partenaires  A Schijf in euro

/  A tranche en euros

Vanaf

tot en met

/  A partir de

sur les tranches  précédentes en euro  0,01  50.000  3  50.000,01  250.000  9  1.500  250.000,01  27  19.500  0,01  50.000  3

TABEL II : tarief voor een andere verkrijging dan de verkrijgingen, vermeld in tabel I

/  TABLEAU II : tarif pour une autre acquisition que les acquisitions mentionnées au tableau I

A Schijf in euro

/  A Tranche en euros

Vanaf

tot en met

/  A partir de

/  jusqu'à

0,01  35.000  25  25  35.000,01  75.000  30  45  8.750  8.750  75.000,01  55  55  20.750  26.750

§ 2. Tabel I, vermeld in paragraaf 1, bevat het tarief voor  een verkrijging in rechte lijn en tussen partners.

Dit tarief wordt per rechtverkrijgende toegepast op de  nettoverkrijging in de onroerende goederen enerzijds en  op de nettoverkrijging in de roerende goederen  anderzijds, volgens de overeenstemmende gedeelten in  kolom A.

In afwijking van het tweede lid wordt het tarief van de  erfbelasting voor de onroerende goederen tussen  partners alleen toegepast op de nettoverkrijging van de  rechtverkrijgende partner in de andere goederen dan de  woning die de gezinswoning was van de erflater en zijn  partner op het ogenblik van het overlijden. Die afwijking  geldt evenwel niet als de partner die een deel verkrijgt in  die gezinswoning, een bloedverwant in de rechte lijn van  de erflater is of een rechtverkrijgende is die voor de  toepassing van het tarief met een rechtverkrijgende in de  rechte lijn wordt gelijkgesteld.

§ 3. Tabel II, vermeld in paragraaf 1, bevat het tarief  voor een verkrijging tussen andere personen dan  personen in rechte lijn en tussen partners. Dit tarief  wordt voor broers en zussen toegepast op het

---- historiek ----  ---- historique ----

- gewijzigd door art.7 van het decreet van 06.07.2018  (B.S. 20.07.2018 Ed.2). Tekst treedt in werking op  01.09.2018

- toegevoegd door art. 52 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.4.1.2.  Art. 2.7.4.1.2.

Als er onzekerheid bestaat over de devolutie van de  nalatenschap of de graad van bloedverwantschap van  een erfgenaam, legataris of begiftigde, wordt de hoogste  erfbelasting geheven.

---- historiek ----  ---- historique ----

- toegevoegd door art. 53 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.4.1.3.  Art. 2.7.4.1.3.

Als een persoon in verschillende hoedanigheden tot de  nalatenschap van de erflater komt, wordt de erfbelasting  op alles wat hij verkrijgt, berekend volgens het voor die  persoon voordeligste tarief, vermeld in artikel 2.7.4.1.1.

---- historiek ----  ---- historique ----

- toegevoegd door art. 54 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.4.1.4.  Art. 2.7.4.1.4.

Als een met fideï-commis bezwaard goed op de  verwachter overgaat, alsook in geval van aanwas of  terugval van eigendom, vruchtgebruik of van elk  tijdelijk of levenslang recht, is de erfbelasting bij  overlijden  verschuldigd  volgens  de  graad  van  verwantschap tussen de erflater en de verwachter of  andere verkrijger.

In de gevallen, vermeld in het eerste lid, blijven de  rechten die geheven zijn ten laste van de bezwaarde of  van de ingestelde in eerste rang, verworven voor de  overheid in het voordeel waarvan ze geïnd zijn, tenzij de

---- historiek ----  ---- historique ----

- toegevoegd door art. 55 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.4.1.5.  Art. 2.7.4.1.5.

Het toe te passen tarief is het tarief dat van kracht is op  de dag van het overlijden.

---- historiek ----  ---- historique ----

- toegevoegd door art. 56 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

##### Onderafdeling 2 - Verlaagde tarieven  Sous-section 2 - Tarifs réduits

---- historiek ----  ---- historique ----

- onderafdeling 2 toegevoegd door art. 57 van het decreet  van 19.12.2014 (B.S., 29.01.2015 - Ed. 2). De

tekst is in werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.4.2.1.  Art. 2.7.4.2.1.

In afwijking van artikel 2.7.4.1.1 bedraagt het tarief van  de erfbelasting 0 % voor de legaten aan :

1° het Vlaamse Gewest en de Vlaamse Gemeenschap;  1° à la Région flamande et à la Communauté flamande  ;

2° de Vlaamse, de Franse en de Gemeenschappelijke  Gemeenschapscommissie;

3° de Franse en de Duitstalige Gemeenschap en aan het  Waalse en het Brusselse Hoofdstedelijke Gewest;

4° een staat in de Europese Economische Ruimte;  4° à un Etat de l'Espace économique européen ;

5° de provincies en gemeenten in het Vlaamse Gewest;  5° aux provinces et aux communes en Région flamande  ;

6° de openbare instellingen van de publiekrechtelijke  rechtspersonen, vermeld in punt 1° tot en met 5° ;

8° het Vlaams Woningfonds;  8° au Fonds flamand du Logement ;

9° dienstverlenende en opdrachthoudende verenigingen  als vermeld in artikel 12, § 2, 2° en 3°,  van het decreet van 6 juli 2001 houdende de  intergemeentelijke samenwerking;

10° verenigingen zonder winstoogmerk, ziekenfondsen  en  landsbonden  van  ziekenfondsen,  internationale verenigingen zonder winstoogmerk en  stichtingen van openbaar nut;

11° openbare centra voor maatschappelijk welzijn.  11° aux centres publics d'action sociale.

In afwijking van artikel 2.7.4.1.1 bedraagt het tarief van  de  erfbelasting  8,5%  voor  de  legaten  aan  beroepsverenigingen en private stichtingen.

Het verlaagde tarief, vermeld in het eerste en het tweede  lid,  is  ook  van  toepassing  op  gelijksoortige  rechtspersonen  die  opgericht  zijn  volgens  en  onderworpen zijn aan de wetgeving van een andere staat  van de Europese Economische Ruimte, en die bovendien  hun zetel, hun hoofdbestuur of hun hoofdvestiging  binnen de Europese Economische Ruimte hebben.

---- historiek ----  ---- historique ----

- gewijzigd door art. 12 van het decreet van 09.07.2021  (B.S., 10.09.2021). Inwerkingtreding: 20.09.2021

- gewijzigd door art. 19 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- gewijzigd door art. 3 van het decreet van 19.03.2021  (B.S., 07.04.2021). Inwerkingtreding: 01.07.2021. Van  toepassing op nalatenschappen die opengevallen zijn  vanaf 1 juli 2021.

- gewijzigd door art. 42 van het besluit van 17.07.2020  (B.S. 17.11.2020). Tekst treedt in werking op 01.01.2021.  Bekrachtigd door art. 224, 2° van het decreet van  09.07.2021 (B.S., 10.09.2021). Inwerkingtreding:  20.09.2021.

- toegevoegd door art. 58 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

§ 1. In afwijking van artikel 2.7.4.1.1 wordt het tarief  van de erfbelasting verlaagd tot 3% voor een verkrijging  in rechte lijn en tussen partners en tot 7% voor een  verkrijging tussen andere personen voor :

1° de nettoverkrijging van de volle eigendom, de blote  eigendom of het vruchtgebruik van de activa die door de  erflater of zijn partner beroepsmatig zijn geïnvesteerd in  een familiale onderneming. Het verlaagde tarief is niet  van toepassing op de verkrijging van onroerende  goederen die hoofdzakelijk tot bewoning worden  aangewend of zijn bestemd, met inbegrip van  bouwgronden als vermeld in artikel 1.1.0.0.2, zesde lid,  1° /1;

2° de nettoverkrijging van de volle eigendom, het  vruchtgebruik of de blote eigendom van aandelen van  een familiale vennootschap met zetel van werkelijke  leiding in een van de staten van de Europese

2° l'acquisition nette de la pleine propriété, de l'usufruit  ou l'usufruit des actions d'une entreprise familiale dont  le siège de direction effective est situé dans l'un des  Etats membres de l'Espace économique européen, à  Economische Ruimte, op voorwaarde dat de aandelen  van de vennootschap die op het ogenblik van het  overlijden in volle eigendom toebehoren aan de erflater  en zijn familie ten minste 50% van de stemrechten in die  vennootschap vertegenwoordigen. Het verlaagde tarief  is niet van toepassing op het gedeelte van de waarde van  de aandelen dat de onroerende goederen, vermeld in  punt 1°, in de familiale vennootschap, of in participaties  van minstens 10% van de familiale vennootschap in haar  dochtervennootschappen,  vertegenwoordigt.  Deze  beperking is niet van toepassing voor familiale  vennootschappen waarvan de omzet voor minstens 75%  wordt gegenereerd door de uitoefening van een activiteit  die betrekking heeft op onroerende goederen, vermeld in  punt 1°

In afwijking van het eerste lid vertegenwoordigen de  aandelen van de vennootschap die op het ogenblik van  het overlijden in volle eigendom toebehoren aan de  erflater en zijn familie minstens 30% van de stemrechten  in die vennootschap, als hij en zijn familie aan een van  de volgende voorwaarden voldoen:

1° samen met één andere aandeelhouder en zijn familie  volle eigenaar zijn van de aandelen van de vennootschap  die minstens 70% van de stemrechten in die  vennootschap vertegenwoordigen;

2° samen met twee andere aandeelhouders en hun  familie volle eigenaar zijn van de aandelen van de  vennootschap die minstens 90% van de stemrechten in  die vennootschap vertegenwoordigen.

Voor de toepassing van het tweede lid komen de  aandelen die toebehoren aan rechtspersonen, niet in  aanmerking om te worden samengeteld met de aandelen  die toebehoren aan de erflater.

1° familiale onderneming : een nijverheids-, handels-,  ambachts- of landbouwbedrijf of een vrij beroep dat  door de erflater of zijn partner, al dan niet samen met  anderen,  persoonlijk  wordt  geëxploiteerd  en  uitgeoefend;

2° familiale vennootschap : een vennootschap die de  uitoefening van een nijverheids-, handels-, ambachts- of  landbouwactiviteit, of van een vrij beroep tot voorwerp  heeft en uitoefent.

Als de vennootschap aan het voorgaande niet  beantwoordt, maar aandelen houdt die minstens 30% van  de stemrechten van één directe dochtervennootschap  vertegenwoordigen die aan die voorwaarde beantwoordt  en die haar zetel van werkelijke leiding heeft in een van  de staten van de Europese Economische Ruimte, wordt  ze ook beschouwd als een familiale vennootschap.

Vennootschappen die geen reële economische activiteit  hebben, worden uitgesloten van het verlaagde tarief,  vermeld in paragraaf 1. Voor een vennootschap waarvan  de omzet voor minstens 75% wordt gegenereerd door de  uitoefening van een activiteit die betrekking heeft op  onroerende goederen, vermeld in paragraaf 1, eerste lid,  1°, kan het uitsluiten van de beperking vermeld in artikel  2.7.4.2.2, § 1, eerste lid, 2°, slechts gelden op  voorwaarde dat de vennootschap in de drie jaar  voorafgaand  aan  het  overlijden  minstens  één  tewerkgestelde werknemer telt, uitgedrukt in voltijdse  eenheden.

3° aandelen :  3° actions :

a) naargelang het geval:

1) als de familiale vennootschap een naamloze  vennootschap, een Europese vennootschap of een  Europese coöperatieve vennootschap is, dan wel een  vennootschap met een andere rechtsvorm waarvoor het  Belgische of buitenlandse recht dat haar beheerst,  voorziet in een vergelijkbaar begrip: elk deelbewijs met  stemrecht dat een deel van het kapitaal  vertegenwoordigt;

2) als de familiale vennootschap een vennootschapsvorm  heeft waarvoor het Belgische of buitenlandse recht dat de  vennootschap beheerst, niet voorziet in het begrip  kapitaal of een vergelijkbaar begrip: elk deelbe- wijs met  stemrecht dat is uitgereikt als tegenprestatie voor een  inbreng of naar aanleiding van de incorporatie van  onbeschikbare reserves;

4° familie van de erflater of de aandeelhouder als  vermeld in paragraaf 1, eerste lid, 2° :

4° famille du testateur ou de l'actionnaire, dont il est  question au paragraphe 1er, premier alinéa, 2° :  a) de partner van de erflater of aandeelhouder, waarbij  het begrip partner voor de aandeelhouder op een  gelijkaardige wijze moet worden geïnterpreteerd als dat  het geval is voor de erflater;

b) de verwanten in rechte lijn van de erflater of  aandeelhouder, alsook hun partners, waarbij het begrip  partner op een gelijkaardige wijze moet worden  geïnterpreteerd als dat het geval is voor de erflater;

c) de zijverwanten van de erflater of aandeelhouder tot  en met de tweede graad en hun partners, waarbij het  begrip partner op een gelijkaardige wijze moet worden  geïnterpreteerd als dat het geval is voor de erflater;

d) de kinderen van broers en zussen van de erflater of  aandeelhouder.

§ 3. Als een vennootschap met toepassing van paragraaf  2, 2°, tweede lid, als een familiale vennootschap wordt  beschouwd, wordt de toepassing van het verlaagde tarief  beperkt tot de waarden van de aandelen van de  vennootschap in de dochtervennootschappen die de  uitoefening van een nijverheids-, handels-, ambachts- of  landbouwactiviteit, of van een vrij beroep tot voorwerp  hebben en die hun zetel van werkelijke leiding in een van  de staten van de Europese Economische Ruimte hebben.

---- historiek ----  ---- historique ----

- gewijzigd door art. 4 van het decreet van 19.12.2025  (B.S. 30.12.2025). Inwerkingtreding: 01.01.2026

- gewijzigd door art. 20 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- gewijzigd door art. 9 van het decreet van 21.12.2018  (B.S. 28.12.2018). Inwerkingtreding op 01.05.2019 (art.  3 van het besluit van 05.04.2019 - B.S.

07.05.2019)

###### Art. 2.7.4.2.3.  Art. 2.7.4.2.3.

§ 1. Het verlaagde tarief, vermeld in artikel 2.7.4.2.2, §  1, eerste lid, 1°, wordt alleen behouden als de volgende  voorwaarden cumulatief zijn vervuld :

1° als een activiteit van de familiale onderneming zonder  onderbreking wordt voortgezet gedurende drie jaar  vanaf de datum van het overlijden van de erflater;

2° als de onroerende goederen die met toepassing van  het  verlaagde  tarief  zijn  overgedragen,  niet  hoofdzakelijk tot bewoning aangewend of bestemd  worden gedurende een periode van drie jaar vanaf de  datum van het overlijden van de erflater.

§ 2. Het verlaagde tarief, vermeld in artikel 2.7.4.2.2, §  1, eerste lid, 2°, wordt alleen behouden als al de  volgende voorwaarden zijn vervuld:

1° de familiale vennootschap blijft gedurende drie jaar  vanaf de datum van het overlijden van de erflater  voldoen aan de voorwaarden, vermeld in artikel  2.7.4.2.2, § 2, 2° ;

2° een activiteit van de familiale vennootschap wordt  zonder onderbreking voortgezet gedurende drie jaar  vanaf de datum van het overlijden van de erflater;

3° voor elk van de drie jaar vanaf het overlijden van de  erflater wordt een jaarrekening of geconsolideerde  jaarrekening opgemaakt en in voorkomend geval  gepubliceerd conform de geldende boekhoudwetgeving  van de lidstaat waar de zetel gevestigd is op het ogenblik  van het overlijden, die ook aangewend is ter  verantwoording van de aangifte in de  inkomstenbelasting.

Ondernemingen of vennootschappen waarvan de zetel  buiten het Vlaamse Gewest, maar binnen België ligt,  maken een jaarrekening of geconsolideerde jaarrekening  op en in voorkomend geval publiceren ze die conform  de geldende boekhoudwetgeving in België op het  ogenblik van het overlijden;

a) als de familiale vennootschap een naamloze  vennootschap, een Europese vennootschap of een  Europese coöperatieve vennootschap is, of een  vennootschap met een andere rechtsvorm waarvoor het  Belgische of buitenlandse recht dat haar beheerst,  voorziet in een vergelijkbaar begrip: het kapitaal daalt  op  geen  enkel  moment  door  uitkeringen  of  terugbetalingen gedurende drie jaar vanaf de datum van  het overlijden van de erflater;

b)  als  de  familiale  vennootschap  een  vennootschapsvorm heeft waarvoor het Belgische of  buitenlandse recht dat de vennootschap beheerst, niet  voorziet in het begrip kapitaal of een vergelijkbaar  begrip: de verrichte inbrengen dalen op geen enkel  moment gedurende drie jaar vanaf de datum van het  overlijden van de erflater door uitkeringen of  terugbetalingen tot onder het bedrag van de tot op de  datum van het overlijden verrichte inbrengen, zoals dat  blijkt uit de jaarrekening;

5° de zetel van de werkelijke leiding van de  vennootschap wordt niet overgebracht naar een staat die  geen deel uitmaakt van de Europese Economische  Ruimte gedurende drie jaar vanaf de datum van het  overlijden van de erflater.

---- historiek ----  ---- historique ----

- gewijzigd door art. 5 van het decreet van 19.12.2025  (B.S. 30.12.2025). Inwerkingtreding: 01.01.2026

- gewijzigd door art. 21 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- gewijzigd door art. 10 van het decreet van 21.12.2018  (B.S. 28.12.2018). Inwerkingtreding op 01.05.2019 (art.  3 van het besluit van 05.04.2019 - B.S.

07.05.2019)

- toegevoegd door art. 60 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.4.2.4.  Art. 2.7.4.2.4.

§ 1. Na verloop van een termijn van drie jaar vanaf de  datum van het overlijden van de erflater controleren de  bevoegde personeelsleden of de voorwaarden, gesteld  voor het behoud van het verlaagde tarief, vervuld zijn.

Bij niet-vervulling van de voorwaarde, vermeld in  artikel 2.7.4.2.3, § 2, 4°, is de erfbelasting verschuldigd  tegen het tarief, vermeld in artikel 2.7.4.1.1, zonder  toepassing van het verlaagde tarief, op het bedrag  waarmee het kapitaal of de verrichte inbrengen is  verminderd, vermenigvuldigd met de grondslag waarop  het verlaagde tarief is toegepast, en gedeeld door de  waarde van alle aandelen van de familiale vennootschap  op de datum van het overlijden van de erflater.

§ 2. Als aanvullende rechten verschuldigd zijn doordat  de voorwaarden, gesteld tot behoud van het verlaagde  tarief, niet langer vervuld zijn, kunnen de verkrijgers dat  melden bij de bevoegde entiteit van de Vlaamse  administratie.

Bij niet-vervulling van de voorwaarden, vermeld in het  eerste lid, wordt de erfbelasting geacht verschuldigd te  zijn, berekend tegen het tarief, vermeld in artikel  2.7.4.1.1, zonder toepassing van het verlaagde tarief.

Bij niet-vervulling van de voorwaarde, vermeld in  artikel 2.7.4.2.3, § 2, 4°, is de erfbelasting verschuldigd  tegen het tarief, vermeld in artikel 2.7.4.1.1, zonder  toepassing van het verlaagde tarief, op het bedrag  waarmee het kapitaal of de verrichte inbrengen is  verminderd, vermenigvuldigd met de grondslag waarop  het verlaagde tarief is toegepast, en gedeeld door de  waarde van alle aandelen van de familiale vennootschap  op de datum van het overlijden van de erflater.

---- historiek ----  ---- historique ----

- gewijzigd door art. 6 van het decreet van 19.12.2025  (B.S. 30.12.2025). Inwerkingtreding: 01.01.2026

- toegevoegd door art. 61 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.4.2.5.  Art. 2.7.4.2.5.

§ 1. In afwijking van artikel 2.7.4.1.1, § 1, wordt voor de  verkrijgingen, vermeld in tabel II van artikel 2.7.4.1.1, §  1, het tarief van de erfbelasting verlaagd:

1° tot 3% voor het gedeelte van de nettoverkrijging dat  kleiner is dan of gelijk is aan 50.000 euro;

2° tot 9% voor het gedeelte van de nettoverkrijging dat  groter is dan 50.000 euro en niet meer bedraagt dan  100.000 euro.

Het  verlaagde  tarief  wordt  toegepast  op  een  Le taux réduit s'applique à une acquisition nette jusqu'à

Het gedeelte van de nettoverkrijging dat het maximum,  vermeld in het tweede lid, te boven gaat, wordt  onderworpen aan het tarief voor verkrijgingen, vermeld  in tabel II van artikel 2.7.4.1.1, § 1.

Het verlaagde tarief, vermeld in het eerste lid, wordt  alleen toegepast als al de volgende voorwaarden zijn  vervuld:

1° op de datum van het openvallen van de nalatenschap  heeft de erflater geen partner als vermeld in artikel  1.1.0.0.2, zesde lid, 4°, en geen bloedverwanten in de  rechte nederdalende lijn of daarmee gelijkgestelde  personen als vermeld in artikel 1.1.0.0.2, zesde lid, 5° ;

2° de erflater heeft in een niet-herroepen testament op  ondubbelzinnige wijze een of meer natuurlijke personen  aangewezen die de toepassing van het verlaagde tarief  kunnen vragen.

Als maar één natuurlijke persoon door de erflater is  aangewezen conform het vierde lid, 2°, wordt het  verlaagde tarief, vermeld in het eerste lid, exclusief  toegepast  op  de  volledige  of  gedeeltelijke  nettoverkrijging van die persoon.

Als meer dan één natuurlijke persoon door de erflater is  aangewezen conform het vierde lid, 2°, wordt het  verlaagde tarief, vermeld in het eerste lid, toegepast op  de nettoverkrijgingen van die personen.

Als het totaal van de nettoverkrijgingen, vermeld in het  zesde lid, het maximumbedrag van 100.000 euro te  boven gaat, wordt het verlaagde tarief toegepast op dat  maximumbedrag. Het maximum wordt verdeeld naar  verhouding van de persoonlijke nettoverkrijgingen ten  opzichte van de samengenomen nettoverkrijgingen,  tenzij de erflater een andere verdeling heeft bepaald.

§ 2. Als de nettoverkrijging, vermeld in paragraaf 1,  goederen omvat die vrijgesteld zijn conform artikel  2.7.6.0.5, wordt het vrijgestelde gedeelte proportioneel  verdeeld tussen het gedeelte van de nettoverkrijging dat  is onderworpen aan het tarief, vermeld in paragraaf 1, en  het gedeelte van de nettoverkrijging dat is onderworpen  aan het tarief, vermeld in tabel II van artikel 2.7.4.1.1, §  1.

§ 3. Het gedeelte van de nettoverkrijging waarop het  verlaagde tarief, vermeld in paragraaf 1, eerste lid, wordt  toegepast, wordt bij voorrang toegerekend op het  gedeelte van de verkrijging waarop het tarief, vermeld in  tabel II van artikel 2.7.4.1.1, § 1, wordt toegepast, en  vervolgens op het gedeelte van de verkrijging waarop  het tarief, vermeld in artikel 2.7.4.2.2, wordt toegepast.

---- historiek ----  ---- historique ----

- Ingevoegd door art. 17 van het decreet van 19.12.2025  (B.S., 30.12.2025). Inwerkingtreding: van toepassing op

###### Art. 2.7.4.2.6.  Art. 2.7.4.2.6.

Voor de toepassing van artikel 2.7.4.2.2 en van artikel  2.7.4.2.3, § 1, 2°, moet de aanwending of de bestemming  van een onroerend goed worden nagegaan per kadastraal  perceel of per gedeelte van een kadastraal perceel als dat  gedeelte ofwel een afzonderlijke huisvesting is, ofwel  een afdeling van de productie of van de werkzaamheden  is die, of een onderdeel daarvan dat, afzonderlijk kan  werken, ofwel een eenheid is die van de andere goederen  of delen die het perceel vormen, kan worden  afgezonderd.

---- historiek ----  ---- historique ----

- ingevoegd door art. 7 van het decreet van 19.12.2025  (B.S. 30.12.2025). Inwerkingtreding: 01.01.2026

#### Afdeling 5 – Verminderingen  Section 5 – Réductions

---- historiek ----  ---- historique ----

- afdeling 5 toegevoegd door art. 62 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.5.0.1.  Art. 2.7.5.0.1.

Voor de bepaling van de nettoverkrijging, vermeld in het  eerste lid, wordt geen rekening gehouden met het  aandeel dat de partner verkrijgt in de gezinswoning dat  ingevolge de toepassing van artikel 2.7.4.1.1, § 2, derde  lid, niet onderworpen is aan erfbelasting.

De erfbelasting, verschuldigd uit hoofde van een  verkrijging door een broer of zus, wordt verminderd met  een bedrag gelijk aan hetzij:

1°  2.000  euro,  vermenigvuldigd  met  (nettoverkrijging/20.000  euro),  wanneer  de  nettoverkrijging kleiner is dan of gelijk is aan 18.750  euro;

2°  2.500  euro,  vermenigvuldigd  met  [1-  (nettoverkrijging/75.000  euro)],  wanneer  de  nettoverkrijging groter is dan 18.750 euro en niet meer  bedraagt dan 75.000 euro.

Voor de erfbelasting verschuldigd door andere personen  dan erfgenamen in de rechte lijn, de partners of broers  en zussen, wordt eenzelfde vermindering toegepast als  berekend overeenkomstig het derde lid waarbij onder de  nettoverkrijging moet begrepen worden: de som van de  nettoverkrijgingen.

Voor de bepaling van de nettoverkrijging, vermeld in het  eerste tot en met het vierde lid, wordt geen rekening  gehouden met het abattement, vermeld in artikel  2.7.3.2.12. Het bedrag van de vermindering kan in  voorkomend geval niet meer bedragen dan de  erfbelasting, verschuldigd na de toekenning van het  abattement, vermeld in artikel 2.7.3.2.12.

§ 2. Als voor dezelfde nalatenschap zowel de  vermindering, vermeld in paragraaf 1, als de  vermindering, vermeld in artikel 2.7.5.0.3, genoten kan  worden, wordt de vermindering, vermeld in paragraaf 1,  eerst toegepast.

---- historiek ----  ---- historique ----

- gewijzigd door art.8 van het decreet van 06.07.2018  (B.S. 20.07.2018 Ed.2). Tekst treedt in werking op  01.09.2018

- toegevoegd door art. 63 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

§ 1. De door een kind van de erflater verschuldigde  erfbelasting wordt verminderd met 75 euro voor elk vol  jaar dat nog moet verlopen tot het kind de leeftijd van  eenentwintig jaar bereikt.

De door de langstlevende partner verschuldigde  erfbelasting wordt verminderd met de helft van de  verminderingen die de gemeenschappelijke kinderen  overeenkomstig het eerste lid genieten.

De gemeenschappelijke kinderen, vermeld in het tweede  lid, zijn de kinderen die deel uitmaken van de rechte lijn,  vermeld in artikel 1.1.0.0.2, zesde lid, 5°, a) en b).

§ 2. Als voor dezelfde nalatenschap zowel de  vermindering, vermeld in paragraaf 1, als de  vermindering, vermeld in artikel 2.7.5.0.3, genoten kan  worden, wordt de vermindering, vermeld in paragraaf 1,  eerst toegepast.

---- historiek ----  ---- historique ----

- toegevoegd door art. 64 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.5.0.3.  Art. 2.7.5.0.3.

Als de goederen die belast zijn met de erfbelasting,  binnen een jaar na het overlijden van de erflater het  voorwerp  uitmaken  van  een  of  meer  andere  overdrachten bij overlijden, wordt de wegens die  overdrachten verschuldigde erfbelasting met de helft  verminderd. De vermindering mag voor elk van die  overdrachten nooit hoger zijn dan de erfbelasting,  geheven op de overdracht die er onmiddellijk aan  voorafgaat.

Als voor dezelfde nalatenschap zowel de vermindering,  vermeld in het eerste lid, als de vermindering, vermeld  in artikel 2.7.5.0.4, genoten kan worden, wordt de  vermindering, vermeld in het eerste lid, eerst toegepast.

---- historiek ----  ---- historique ----

- toegevoegd door art. 65 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.5.0.4.  Art. 2.7.5.0.4.

Als het actief van de nalatenschap van een rijksinwoner  buitenlandse goederen bevat die in het buitenland  aanleiding geven tot het heffen van een erfbelasting,  wordt het verschuldigde successierecht, in

De vermindering, vermeld in het eerste lid, wordt alleen  toegekend als aan het bevoegde personeelslid een  behoorlijk gedateerd betalingsbewijs van een in het  buitenland betaalde erfbelasting wordt voorgelegd,  samen met een door de bevoegde overheden eensluidend  verklaard afschrift van de aangifte die ze hebben  ontvangen en de berekening van de belasting die ze  hebben vastgesteld.

Als voor dezelfde nalatenschap zowel de vermindering,  vermeld in het eerste lid, als het abattement, vermeld in  artikel 2.7.3.2.12, genoten kan worden, wordt de  vermindering, vermeld in het eerste lid, eerst toegepast.

---- historiek ----  ---- historique ----

- gewijzigd door art. 13 van het decreet van 09.12.2022  (B.S. 20.12.2022). Inwerkingtreding: 30.12.2022

- toegevoegd door art. 66 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.5.0.5.  Art. 2.7.5.0.5.

Het verkooprecht en het verdeelrecht dat geheven wordt  bij de registratie van de akte van verkoop of van afstand,  en, in voorkomend geval, het overschrijvingsrecht, of  een soortgelijke belasting die geheven wordt in een staat  van de Europese Economische Ruimte, worden  afgetrokken van de erfbelasting als de voormelde  belastingen opeisbaar zijn krachtens artikel 2.7.1.0.9 en  artikel 2.7.3.3.5, eventueel gecombineerd met artikel  2.7.3.2.11.

---- historiek ----  ---- historique ----

- toegevoegd door art. 67 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.5.0.6.  Art. 2.7.5.0.6.

De erfbelasting, verschuldigd door natuurlijke personen  van wie de verkrijging onderworpen is aan het tarief,  vermeld in tabel II van artikel 2.7.4.1.1, en die voldoen  aan de hierna gestelde voorwaarden, wordt verminderd  met een bedrag dat verkregen wordt door toepassing van  de volgende formule: X = a x (b - c).

De parameters, vermeld in het eerste lid, worden  gedefinieerd als volgt:

2° b = het laagste tarief, vermeld in tabel II van het  voormelde artikel;

3° c = het laagste tarief, vermeld in tabel I van het  voormelde artikel.

De vermindering, vermeld in het eerste lid, wordt alleen  toegekend aan de natuurlijke personen die de erflater in  een niet-herroepen testament op ondubbelzinnige wijze  heeft aangewezen als diegenen die de toepassing van de  vermindering, vermeld in het eerste lid, mogen vragen.  Het testament is vóór 1 januari 2026 gedagtekend.

De vermindering, vermeld in het eerste lid, wordt  toegepast op de erfbelasting, verschuldigd door de  verkrijgers die zijn aangewezen overeenkomstig het  derde lid, na de toepassing van alle andere vrijstellingen  en verminderingen waarop de voormelde verkrijgers  aanspraak kunnen maken.

Als er slechts één natuurlijke persoon is aangewezen  overeenkomstig het derde lid, wordt de vermindering,  vermeld in het eerste lid, exclusief toegekend aan deze  persoon.

Als er meer dan één natuurlijke persoon is aangewezen  overeenkomstig het derde lid, wordt de vermindering,  vermeld in het eerste lid, onder deze personen verdeeld  naar verhouding van hun persoonlijke nettoverkrijging  ten opzichte van de samengenomen nettoverkrijgingen  van al deze personen, tenzij de erflater een andere  verdeling heeft bepaald.

De vermindering die conform dit artikel wordt  toegepast, levert in geen geval grond voor een teruggave  op.

De vermindering, vermeld in het eerste lid, wordt niet  toegepast als voor dezelfde nalatenschap toepassing  wordt gemaakt van het verlaagde tarief, vermeld in  artikel 2.7.4.2.5, § 1, eerste lid.

---- historiek ----  ---- historique ----

- gewijzigd door art. 18, 2° van het decreet van  19.12.2025 (B.S. 30.12.2025). Inwerkingtreding: van  toepassing op alle nalatenschappen die openvallen vanaf  1 januari 2026.

- gewijzigd door art. 18, 1° van het decreet van  19.12.2025 (B.S. 30.12.2025). Inwerkingtreding:  31.12.2025

- gewijzigd door art. 14 van het decreet van 09.12.2022  (B.S. 20.12.2022). Inwerkingtreding met ingang van

- Ingevoegd door art. 4 van het decreet van 19.03.2021  (B.S., 07.04.2021). Inwerkingtreding: 01.07.2021. Van  toepassing op nalatenschappen die opengevallen zijn  vanaf 1 juli 2021

#### Afdeling 6 – Vrijstelling  Section 6 – Exonération

---- historiek ----  ---- historique ----

- afdeling 6 toegevoegd door art. 68 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.6.0.1.  Art. 2.7.6.0.1.

§ 1. De waarde van de maatschappelijke rechten,  vermeld in paragraaf 2, die door de erflater of door zijn  echtgenoot ten minste vijf jaar vóór het openvallen van

§ 1er. Sont exemptes du droit de succession, les parts  sociales visées au § 2 du présent article qui sont acquises  par le défunt ou son conjoint au moins cinq ans avant  de nalatenschap en uiterlijk in het jaar 2005 zijn  verworven en die gedurende de vermelde termijn  ingeschreven waren op naam van de erflater of van zijn  echtgenoot, of de waarde van hetgeen verkregen wordt  als terugbetaling van diezelfde maatschappelijke  rechten, wordt vrijgesteld van het successierecht. Als de  erflater op het moment van de inschrijving niet heeft  geopteerd voor de kapitalisatie van het inkomen dat  periodiek toegekend is aan het maatschappelijk recht,  wordt het bedrag dat voor de vrijstelling in aanmerking  komt, toch berekend alsof voor kapitalisatie gekozen is.

De vrijstelling, vermeld in het eerste lid, heeft alleen  betrekking op de waarde van de maatschappelijke  rechten die op datum van de terugbetaling ervan  minstens drie jaar volgestort zijn. De mogelijkheid tot  vrijstelling vervalt in geval van terugbetaling aan, of  vervreemding door de inschrijver van de vermelde  maatschappelijke rechten.

De vrijstelling, vermeld in het eerste lid, is gelijk aan het  kleinste van de volgende bedragen :

1° de beurswaarde van de maatschappelijke rechten  waarvoor een attest als vermeld in paragraaf 4 gevraagd  wordt, verhoogd met het gekapitaliseerde bedrag van de  periodieke netto inkomsten (na belasting) toegewezen  aan de rechten die voor de vrijstelling in aanmerking  komen met betrekking tot de periode waarvoor de  Vlaamse  Regering  de  emitterende  beleggingsvennootschap met vast kapitaal erkende;

Het gekapitaliseerd bedrag, vermeld in het eerste lid,  bevat  enkel  de  inkomsten  toegekend  aan  de  maatschappelijke rechten waarvoor, gelet op artikel 7 en  8 van het besluit van de Vlaamse Regering van 3 mei  1995  tot  regeling  van  de  vrijstelling  inzake  successierechten verbonden aan de maatschappelijke  rechten in vennootschappen opgericht in het kader van  de  realisatie  en/of  financiering  van  investeringsprogramma's van serviceflats, aangetoond is  dat de overledene of zijn echtgenoot er houder van was.

Als slechts een gedeelte van de beurswaarde of van het  bedrag van de volstorting van de maatschappelijke  rechten voor effectieve vrijstelling in aanmerking komt,  zal bovendien het gekapitaliseerd bedrag van de

Si seulement une partie de la valeur en bourse ou du  montant libéré des parts est admissible à l'exonération  effective, le montant capitalisé des revenus nets  périodiques ne sera ajouté que dans la même proportion.  periodieke netto inkomsten slechts in dezelfde  verhouding worden bijgeteld.

Het gekapitaliseerd bedrag is gelijk aan de effectief  uitgekeerde dividenden tijdens de periode, vermeld in  het eerste lid.

§ 2. Onder maatschappelijke rechten wordt verstaan de  maatschappelijke rechten in een vennootschap die door  de Vlaamse Regering is erkend in het kader van de  financiering en de realisatie van serviceflatgebouwen als  vermeld in artikel 88, § 5, van het Woonzorgdecreet van  13  maart  2009,  of  woningcomplexen  met  dienstverlening als vermeld in artikel 88, § 1 en § 2, van  het Woonzorgdecreet van 13 maart 2009.

§ 3. Om erkend te worden door de Vlaamse Regering  moet de vennootschap, vermeld in paragraaf 2, minstens  voldoen aan de volgende voorwaarden :

1° haar zetel gevestigd hebben in de Europese  Economische Ruimte;

2° opgericht zijn na 1 januari 1995;  2° avoir été constituée après le 1er janvier 1995 ;

3° vanaf het ogenblik van de uitgifte van de  maatschappelijke rechten, vermeld in paragraaf 2, en  minstens tot 27 november 2012, uitsluitend de  financiering en realisatie van projecten voor de  oprichting van serviceflatgebouwen als voorwerp  hebben gehad;

4° vanaf 27 november 2012 :  4° à partir du 27 novembre 2012 :

b) voor de Europese Economische Ruimte, uitgezonderd  het Vlaamse Gewest, uitsluitend de financiering en  realisatie van soortgelijke projecten inzake onroerende  goederen als voorwerp hebben;

5° de gelden, die zijn ingezameld ingevolge de uitgifte  van de maatschappelijke rechten, vermeld in paragraaf  2, integraal besteden of besteed hebben aan projecten  binnen de Europese Economische Ruimte.

§ 4. Op verzoek van de houder van maatschappelijke  rechten of van zijn rechtverkrijgenden, wordt een attest  uitgereikt voor het verkrijgen van de vrijstelling van het

§ 4. A la demande du porteur ou de ses ayants droit, une  attestation sera délivrée, pouvant donner droit à  l'exonération des droits de succession. Cette attestation,  successierecht. Dit attest wordt, in de vorm vastgesteld  door de Vlaamse Regering, door de betrokken financiële  instelling slechts uitgereikt voor maatschappelijke  rechten waarop, op de datum van het openvallen van de  nalatenschap wegens het overlijden van de houder van  de rechten of zijn echtgenoot, minstens vijf jaar vóór het  overlijden van de houder ingeschreven werd en die reeds  drie jaar volgestort werden.

Met inschrijving wordt gelijkgesteld de verwerving op  een andere wijze uiterlijk in het jaar 2005, van  maatschappelijke rechten in een door de Vlaamse  Regering erkende beleggingsvennootschap met vast  kapitaal of een gereglementeerde vastgoedvennootschap  als vermeld in artikel 2, 1°, van de wet van 12 mei 2014  betreffende  de  gereglementeerde  vastgoedvennootschappen. Dit houdt tevens in dat een  verwerving na het jaar 2005, met uitzondering van  verkrijging onder echtgenoten en erfgenamen in de  eerste graad waarbij geen vrijstelling van de erfbelasting  verworven werd, nooit aanleiding kan geven tot  vrijstelling van de erfbelasting.

Het attest vermeldt de bedragen, vermeld in paragraaf 1,  derde lid, met betrekking tot het geheel van de  maatschappelijke rechten die voor een hele of  gedeeltelijke vrijstelling in aanmerking komen.

Bij uitreiking van een tweede attest wordt bovendien  melding gemaakt van het vorige attest en van de datum  waarop het werd afgegeven.

---- historiek ----  ---- historique ----

- gewijzigd door art. 22 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- toegevoegd door art. 69 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.6.0.2.  Art. 2.7.6.0.2.

(…)  (…)

---- historiek ----  ---- historique ----

- opgeheven door art. 12 van het decreet van 22.12.2017  (B.S. 21.02.2018). Tekst treedt in werking op 09.06.2020  (art. 1 besluit 04.05.2018 B.S.

30.05.2018)

- toegevoegd door art. 70 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

- vervangen door art. 53 van het decreet van 01 juli 2016  (B.S., 19.08.2016). Tekst treedt in werking op een door de  Vlaamse Regering vast te stellen datum (art.

66)

###### Art. 2.7.6.0.3.  Art. 2.7.6.0.3.

(…)  (…)

---- historiek ----  ---- historique ----

- opgeheven door art. 13 van het decreet van 22.12.2017  (B.S. 21.02.2018). Tekst treedt in werking op 09.06.2020  (art. 1 besluit 04.05.2018 B.S.

30.05.2018)

- toegevoegd door art. 71 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

De waarde van de zaken die ascendenten verkrijgen uit  de nalatenschap van de erflater, wordt vrijgesteld van de  erfbelasting als de volgende voorwaarden cumulatief  zijn vervuld :

1° de zaken zijn door die ascendenten onder de levenden  aan de erflater geschonken voor zijn overlijden;

2° de zaken bevinden zich nog in natura in de  nalatenschap of er is, als ze zijn vervreemd, nog een  schuldvordering in de nalatenschap aanwezig;

3° de erflater is zonder nakomelingen gestorven.  3° le testateur est mort sans descendants.

---- historiek ----  ---- historique ----

- toegevoegd door art. 72 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.6.0.5.  Art. 2.7.6.0.5.

§ 1. De waarde van de nettoverkrijging in de  onbebouwde onroerende goederen waarvoor een  natuurbeheerplan type twee, drie of vier als vermeld in  artikel 16ter, § 1, 2°, 3° en 4°, van het decreet van 21  oktober 1997 betreffende het natuurbehoud en het  natuurlijk milieu, is goedgekeurd conform artikel  16octies van het voormelde decreet, wordt op de datum  van het openvallen van de nalatenschap, zowel voor de  grond- als voor de opstandswaarde, als volgt van de  erfbelasting vrijgesteld:

§ 1er. La valeur de l’acquisition nette dans les biens  immobiliers non bâtis pour lesquels un plan de gestion  de la nature type deux, trois ou quatre tel que visé à  l’article 16ter, § 1er, 2°, 3° et 4°, du décret du 21 octobre  1997 concernant la conservation de la nature et le milieu  naturel, a été approuvée conformément à l’article  16octies du décret précité, est exemptée de l’impôt de  succession à la date de l’ouverture de la succession, tant  pour la valeur du terrain que pour celle des peuplements  ;  1°  ten  belope  van  50%  in  geval  van  een  natuurbeheerplan type twee;

2°  ten  belope  van  75%  in  geval  van  een  natuurbeheerplan type drie;

3° ten belope van 100% in geval van een  natuurbeheerplan type vier.

§ 2. De vrijstelling, vermeld in paragraaf 1, is ook van  toepassing als er nog geen natuurbeheerplan is  afgesloten, en als de erflater een intentieovereenkomst  met het Agentschap voor Natuur en Bos heeft afgesloten  of als de erfgenaam, legataris of begiftigde de intentie  heeft om op het onroerend goed een natuurbeheerplan  type twee, drie of vier als vermeld in artikel 16ter, § 1,  2°, 3° en 4°, van het decreet van 21 oktober 1997  betreffende het natuurbehoud en het natuurlijk milieu,  tot stand te brengen.

In voorkomend geval dient deze overeenkomst  gezamenlijk te zijn afgesloten met alle andere houders  van zakelijke rechten op het desbetreffende goed.

---- historiek ----  ---- historique ----

- ingevoegd door art. 14 van het decreet van 22.12.2017  (B.S. 21.02.2018). Tekst treedt in werking op 09.06.2018  (art. 1 besluit 04.05.2018 B.S.

30.05.2018)

###### Art. 2.7.6.0.6.  Art. 2.7.6.0.6.

§ 1. Voor de toepassing van het tarief, vermeld in artikel  2.7.4.1.1, § 1, in rechte nederdalende lijn, en voor zover  de andere ouder van het betrokken kind reeds  vooroverleden is, wordt de eerste schijf van 75.000 euro  in de nettoverkrijging van het rechtverkrijgende kind  onder de 21 jaar van de roerende goederen vrijgesteld  van het successierecht.

In afwijking van artikel 2.7.4.1.1, § 2, tweede lid, en  voor zover de andere ouder van het betrokken kind reeds  vooroverleden is, wordt het tarief van de erfbelasting  voor de onroerende goederen in rechte lijn niet toegepast  op de nettoverkrijging van het rechtverkrijgende kind  onder de 21 jaar in de woning die op het ogenblik van  het overlijden van de langstlevende ouder de woning

was waar de erflater gedomicilieerd was op het moment  van overlijden.

§ 2. Voor de toepassing van het tarief, vermeld in artikel  2.7.4.1.1, § 1, tussen partners wordt de eerste schijf van  75.000  euro  in  de  nettoverkrijging  van  de  rechtverkrijgende partner van de roerende goederen  vrijgesteld van het successierecht. Die vrijstelling geldt  niet als de rechtverkrijgende partner een bloedverwant  in de rechte lijn van de erflater is of een  rechtverkrijgende is die voor de toepassing van het tarief  met een rechtverkrijgende in de rechte lijn wordt  gelijkgesteld.

---- historiek ----  ---- historique ----

- gewijzigd door art. 19 van het decreet van 19.12.2025  (B.S. 30.12.2025). Inwerkingtreding: Van toepassing op  alle nalatenschappen die openvallen vanaf 1 januari  2026.

vanaf 01.09.2018

- ingevoegd door art. 9 van het decreet van 06.07.2018  (B.S. 20.07.2018 Ed.2). Tekst treedt in werking op  01.09.2018

#### Afdeling 7 - Wijze van heffing  Section 7 - Modalités de perception

---- historiek ----  ---- historique ----

- afdeling 7 toegevoegd door art. 73 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.7.0.1.  Art. 2.7.7.0.1.

De erfbelasting wordt gevestigd op zicht van de aangifte,  vermeld in artikel 3.3.1.0.5 en 3.3.1.0.6, of ambtshalve  als de aangifte niet is ingediend binnen de termijn,  vermeld in artikel 3.3.1.0.5 en artikel 3.3.1.0.6, of bij  onjuistheid of onvolledigheid van de aangifte.

---- historiek ----  ---- historique ----

- toegevoegd door art. 74 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.7.0.2.  Art. 2.7.7.0.2.

In geval van achtereenvolgende overgangen door  overlijden van een goed dat onder opschortende  voorwaarde is verkregen, of van een goed dat in bezit is  van een derde, maar door de nalatenschap is teruggeëist,  is de erfbelasting verschuldigd overeenkomstig de  voorwaarden, vermeld in artikel 2.7.3.3.7, artikel  3.3.1.0.5, § 2, en artikel 3.3.1.0.6, alleen wegens de  laatste overgang.

Als de achtereenvolgende overgangen een goed tot  voorwerp hebben dat betwist in het bezit van de erflater  is of dat aan hem toebehoort onder ontbindende  voorwaarde, is de belasting onmiddellijk opvorderbaar  bij elk overlijden.

---- historiek ----  ---- historique ----

- toegevoegd door art. 75 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.7.7.0.3.  Art. 2.7.7.0.3.

(…)  (…)

- opgeheven door art. 16 van het decreet van 08.12.2017  (B.S., 14.12.2017). De tekst is in werking getreden op  24.12.2017

- toegevoegd door art. 76 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

### Hoofdstuk 8 – Schenkbelasting  Chapitre 8 - Impôt de donation

---- historiek ----  ---- historique ----

- hoofdstuk 8 toegevoegd door art. 77 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

#### Afdeling 1 - Belastbaar voorwerp  Section 1re - Objet imposable

---- historiek ----  ---- historique ----

- afdeling 1 toegevoegd door art. 78 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.8.1.0.1.  Art. 2.8.1.0.1.

Overeenkomstig artikel 1, artikel 19 en artikel 31 van het  federale Wetboek van Registratie-, Hypotheek- en  Griffierechten wordt de schenkbelasting gevestigd naar  aanleiding van de registratie of de verplichting tot  registratie van akten of geschriften die tot bewijs  strekken van een schenking onder de levenden

---- historiek ----  ---- historique ----

- toegevoegd door art. 79 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.8.1.0.2.  Art. 2.8.1.0.2.

§ 1. Vonnissen en arresten die tot bewijs strekken van  een schenking onder de levenden van eigendom of  vruchtgebruik van onroerende goederen in België die  nog niet aan de schenkbelasting onderworpen zijn,  geven aanleiding tot de heffing van de schenkbelasting  waaraan de schenking onderworpen zou zijn als ze in  een schenkingsakte zou zijn vastgesteld.

Dat geldt ook als de rechterlijke beslissing die tot bewijs  van de overeenkomst strekt, de ontbinding of herroeping  ervan uitspreekt of vaststelt voor om het even welke  reden, tenzij uit de beslissing blijkt dat ten hoogste één  jaar na de overeenkomst een eis tot ontbinding of  herroeping, zelfs bij een onbevoegde rechter, is  ingesteld.

Dat geldt ook als de scheidsrechterlijke uitspraak of in  het buitenland gewezen rechterlijke beslissing die tot  bewijs van de overeenkomst strekt, de ontbinding of  herroeping ervan uitspreekt of vaststelt voor om het even  welke reden, tenzij uit de beslissing blijkt dat ten hoogste  één jaar na de overeenkomst een eis tot ontbinding of  herroeping, zelfs bij een onbevoegde rechter, is  ingesteld.

De schenkbelasting is ook van toepassing in geval van  aanbieding ter registratie van een in het buitenland  gewezen rechterlijke beslissing die van rechtswege in  België uitvoerbaar is.

---- historiek ----  ---- historique ----

- toegevoegd door art. 80 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

#### Afdeling 2 – Belastingplichtigen  Section 2 – Contribuables

---- historiek ----  ---- historique ----

- afdeling 2.toegevoegd door art. 81 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.8.2.0.1.  Art. 2.8.2.0.1.

De belastingplichtige is de begiftigde.  Le contribuable est le donataire.

Bij een inbreng om niet is de belastingplichtige de  begunstigde rechtspersoon.

---- historiek ----  ---- historique ----

- toegevoegd door art. 82 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

#### Afdeling 3 - Belastbare grondslag  Section 3 - Base imposable

---- historiek ----  ---- historique ----

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.8.3.0.1.  Art. 2.8.3.0.1.

§ 1. Voor de schenkingen onder de levenden van  roerende  en  onroerende  goederen  wordt  een  schenkbelasting geheven op het aandeel van elke  begiftigde, op basis van de verkoopwaarde van de  geschonken goederen, zonder aftrek van lasten.

§ 2. In afwijking van paragraaf 1 wordt de belastbare  grondslag als volgt vastgesteld :

1° voor de schenking van financiële instrumenten die  toegelaten zijn tot verhandeling op Belgische of  buitenlandse gereglementeerde markten als vermeld in  artikel 2, eerste lid, 5° en 6°, van de wet van 2 augustus  2002 betreffende het toezicht op de financiële sector en  de financiële diensten en voor Belgische of buitenlandse  multilaterale handelsfaciliteiten als vermeld in artikel 2,  eerste lid, 4°, van de voormelde wet, volgens de  beurswaarden ervan op datum van de eerste dag van de  maand waarin de schenking plaatsvindt. Als er op die  datum geen notering is, geldt de beurswaarde op de  eerstvolgende dag waarop er opnieuw een notering  wordt vastgesteld. Als er op de datum van de eerste dag  van de maand waarin de schenking plaatsvindt voor  bepaalde van de geschonken waarden wel en voor  andere geen notering is, wordt de belastbare grondslag  van die laatste waarden vastgesteld volgens de  beurswaarden op de eerstvolgende dag waarop er wel  een notering is;

2° voor de schenking van het vruchtgebruik of de blote  eigendom van een onroerend goed, zoals in artikel  2.9.3.0.4 tot en met artikel 2.9.3.0.7 is bepaald;

2° si la donation a pour objet l'usufruit ou la nue-  propriété d'un immeuble, suivant ce qui est déterminé  aux articles 2.9.3.0.4 à 2.9.3.0.7 inclus ;  3° voor de schenking van het op het leven van de  begiftigde of een derde geves|Uptigde vruchtgebruik van  roerende goederen, volgens de volgende formule :

belastbare grondslag = a x b, waarbij :  base imposable = a x b, où :

a) a = de jaarlijkse opbrengst van de goederen, forfaitair  vastgesteld op 4% van de waarde van de volle eigendom  van de goederen;

b) b = de leeftijdscoëfficiënt, vermeld in de tabel van  artikel 2.9.3.0.4, § 1, naargelang de leeftijd van de  persoon op het hoofd van wie het vruchtgebruik is  gevestigd op de datum van de schenking;

5° voor de schenking van de blote eigendom van  roerende goederen waarvan het vruchtgebruik door de  schenker  is  voorbehouden,  op  basis  van  de  verkoopwaarde van de volle eigendom van de goederen;

6° voor de schenking van de blote eigendom van  roerende goederen waarvan het vruchtgebruik door de  schenker niet is voorbehouden, op basis van de  verkoop|Upwaarde van de volle eigendom van de  goederen, verminderd met de waarde van het  vruchtgebruik, berekend volgens punt 3° of punt 4° ;

7° voor schenkingen van een lijfrente of een levenslang  pensioen, op basis van het jaarlijkse bedrag van de  uitkering, vermenigvuldigd met de leeftijdscoëfficiënt,  vermeld in de tabel van artikel 2.9.3.0.4, § 1, die op de  begiftigde moet worden toegepast;

8° voor schenkingen van een altijddurende rente, op  basis van het jaarlijkse bedrag van de rente,  vermenigvuldigd met twintig.

§ 3. Voor de toepassing van paragraaf 1 wordt de last die  bestaat uit een som, een rente of een pensioen, onder  kosteloze titel bedongen ten voordele van een derde die  aanvaardt, in hoofde van die derde als schenking belast  en wordt de last van het aandeel van de hoofdbegiftigde  afgetrokken. In de mate dat de schenking betrekking  heeft op onroerende goederen, wordt de last in hoofde

§ 3. Pour l'application du paragraphe 1er., la charge  consistant en une somme ou une rente ou pension  stipulée à titre gratuit au profit d'un tiers acceptant, est  imposée à titre de donation dans le chef dudit tiers et  déduite de l'émolument du donataire principal. Dans la  mesure où la donation concerne des biens immobiliers,  la charge est imposée dans le chef du tiers comme une  van de derde als schenking belast volgens de tarieven,  vermeld in artikel 2.8.4.1.1, § 1.

---- historiek ----  ---- historique ----

- gewijzigd door art. 37 van het decreet van 23.12.2016  (B.S.: 30.12.2016). Tekst in werking getreden op  08.01.2017

- toegevoegd door art. 84 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

De schenkbelasting, verschuldigd op akten waarbij  eigendom of vruchtgebruik van een handelszaak  overgedragen wordt, wordt geheven op basis van de  belastbare grondslagen, vermeld in deze afdeling.

De schulden die al dan niet met de handelszaak in  verband staan en die door de nieuwe eigenaar of  vruchtgebruiker ten laste genomen worden, worden als  lasten van de overeenkomst beschouwd.

---- historiek ----  ---- historique ----

- toegevoegd door art. 85 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.8.3.0.3.  Art. 2.8.3.0.3.

§ 1. Als er eerdere schenkingen van onroerende  goederen  bestaan  tussen  dezelfde  partijen,  die  vastgesteld zijn door akten die dateren van minder dan  drie jaar vóór de datum van de nieuwe schenking van  onroerende goederen, wordt de belastbare grondslag van  die eerdere schenkingen gevoegd bij de belastbare  grondslag van de nieuwe schenking om de toepasselijke  schenkbelasting op de nieuwe schenking te bepalen.

Het eerste lid is niet van toepassing op:  L’alinéa premier ne s’applique pas :

1° de onroerende goederen die deel uitmaken van een  vrijgestelde schenking van activa als vermeld in artikel  2.8.6.0.3, § 1, 1°;

2° het gedeelte van de onbebouwde onroerende goederen  waarop de vrijstelling, vermeld in artikel 2.8.6.0.8, is  toegepast.

3° de onroerende goederen waarop de vrijstelling,  vermeld in artikel 2.8.6.0.1, is toegepast.

§ 2. Als in dezelfde akte of in een andere akte van  dezelfde datum naast de grond die volgens de  stedenbouwkundige voorschriften bestemd is voor  woningbouw, nog andere onroerende goederen worden  geschonken, wordt voor de toepassing van paragraaf 1  de schenking van de bouwgrond geacht vóór de

§ 2. Si, dans le même acte ou dans un autre acte de la  même date, il y a donation de biens autres que la parcelle  de terrain destinée à la construction d'habitations selon  les prescriptions d'urbanisme, la donation du terrain à  bâtir est censée, pour l'application du paragraphe 1er,  avoir été enregistrée ou être obligatoirement  enregistrable avant la donation des autres biens.  schenking van de andere goederen geregistreerd te zijn  of verplicht registreerbaar te zijn geworden.

§ 3. In geval van een aan een opschortende voorwaarde  onderworpen schenking wordt voor de toepassing van  paragraaf 1 en paragraaf 2 de datum van de vervulling  van de voorwaarde in de plaats gesteld van de datum van  de akte.

- gewijzigd door art. 14 van het decreet van 03.04.2026  (B.S. 23.04.2026). Inwerkingtreding op 03.05.2026

- gewijzigd door art. 15 van het decreet van 09.12.2022  (B.S. 20.12.2022). Inwerkingtreding: 30.12.2022

- gewijzigd door art. 15 van het decreet van 22.12.2017  (B.S.: 21.02.2018). Tekst treedt in werking op 09.06.2018  (art. 1 besluit 04.05.2018 B.S. 30.05.2018)

- § 1, eerste lid gewijzigd door art. 17 van het decreet  van 08.12.2017 (B.S.: 14.12.2017). Tekst in werking  getreden op 24.12.2017

- gewijzigd door art. 38 van het decreet van 23.12.2016  (B.S.: 30.12.2016). Tekst in werking getreden op  08.01.2017

- toegevoegd door art. 86 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 01.01.2015 (art. 325)

###### Art. 2.8.3.0.4.  Art. 2.8.3.0.4.

Op hetgeen aan een persoon met een handicap of een  gehandicapt kind geschonken wordt, wordt een  abattement toegepast aan de voet van de belastbare  grondslag, voor de som die verkregen is door toepassing  van de volgende formule :

1° (3000 euro) x (cijfer, aangeduid in artikel 2.7.3.3.2,  eerste lid, 5°, volgens de leeftijd van de verkrijger) als  de schenking onderworpen is aan het tarief voor  verkrijgingen in de rechte lijn en tussen partners,  vermeld in artikel 2.8.4.1.1, § 1, of artikel 2.8.4.2.1;

2° (1000 euro) x (cijfer, aangeduid in artikel 2.7.3.3.2,  eerste lid, 5°, volgens de leeftijd van de verkrijger) als  de schenking onderworpen is aan het tarief voor  verkrijgingen tussen alle andere personen, vermeld in  artikel 2.8.4.1.1, § 1, of artikel 2.8.4.2.1.

Het abattement, vermeld in het eerste lid, wordt slechts  toegepast als tussen de schenker en de begiftigde nog  geen schenkingen zijn voorgekomen waarbij van deze  vermindering van belastbare grondslag werd genoten.

---- historiek ----  ---- historique ----

- gewijzigd door art. 16 van het decreet van 09.12.2022  (B.S. 20.12.2022). Inwerkingtreding: 30.12.2022

2015 (B.S., 15.07.2015). De tekst is in werking getreden  op 01.07.2015 (art. 61))

###### Art. 2.8.3.0.5.  Art. 2.8.3.0.5.

Een  akte  die  een  door  de  wet  toegelaten  erfovereenkomst vaststelt, strekt voor de toepassing van  de schenkbelasting niet tot bewijs van een schenking die  in die overeenkomst wordt vermeld en die niet aan de  formaliteit van de registratie is onderworpen, en  waarvan de partijen in of onderaan de akte bevestigen  dat die heeft plaatsgevonden vóór de datum waarop die  overeenkomst gesloten werd.

In afwijking van het eerste lid kunnen de partijen of een  van hen in een uitdrukkelijke fiscale verklaring in of  onderaan de akte te kennen geven dat de vermelding van  een dergelijke schenking wel tot bewijs strekt voor de  toepassing van de schenkbelasting.

---- historiek ----  ---- historique ----

- ingevoegd door art. 10 van het decreet van 06.07.2018  (B.S. 20.07.2018 Ed. 2). Tekst treedt in

werking op 01.09.2018

#### Afdeling 4 - Tarieven  Section 4 - Tarifs.

---- historiek ----  ---- historique ----

- afdeling 4 toegevoegd door art. 87 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

##### Onderafdeling 1 – Algemeen  Sous-section 1re – Généralités

---- historiek ----  ---- historique ----

- onderafdeling 1 toegevoegd door art. 88 van het decreet  van 19.12.2014 (B.S., 29.01.2015 - Ed. 2). De

tekst is in werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.8.4.1.1.  Art. 2.8.4.1.1.

§ 1. De schenkbelasting voor de schenkingen van  onroerende goederen wordt berekend volgens het tarief,  vermeld in de onderstaande tabellen :

TABEL I  TABLEAU I

/  tranche de la donation

tarief, toepasselijk op het  overeenstemmende gedeelte in

totaalbedrag van de belasting over  de voorgaan- de gedeelten, in euro

A schijf in euro

kolom A, in %

/  A tranche en euros

/  tarif applicable à la tranche  correspondante figurant dans la

/  montant total de la taxe sur les  tranches précédentes, en euros

colonne A, en %

Vanaf

tot en met

/  A partir de

/  à  0,01  150.000  3  -  150.000,01  250.000  9  4500  250.000,01  450.000  18  13.500  450.000,01  27  49.500

TABEL II  TABLEAU II

tarief tussen alle andere personen

/  tarif entre toutes les autres personnes  gedeelte van de schenking

/  tranche de la donation

tarief, toepasselijk op het  overeenstemmende gedeelte in

totaalbedrag van de belasting over  de voorgaan- de gedeelten, in euro

A schijf in euro

kolom A, in %

/  A tranche en euros

/  tarif applicable à la tranche  correspondante figurant dans la

/  montant total de la taxe sur les  tranches précédentes, en euros

colonne A, en %

Vanaf

tot en met

/  A partir de

/  à  0,01  150.000  10  -  150.000,01  250.000  20  15.000  250.000,01  450.000  30  35.000  450.000,01  40  95.000

§ 2. Het tarief van de schenkbelasting voor de  schenkingen van roerende goederen bedraagt :

§ 2. Le tarif de l’impôt de donation pour les donations  de biens mobiliers se monte à :

1° 3% voor een verkrijging in de rechte lijn en tussen  partners;

1° 3 % pour une acquisition en ligne directe et entre  partenaires ;

2° 7% voor een verkrijging door alle andere personen.  2° 7 % pour une acquisition par toutes autres personnes.

Dat tarief is niet van toepassing op de schenkingen onder  de levenden van roerende goederen die met legaten  worden gelijkgesteld met toepassing van artikel  2.7.1.0.3, 3°.

Ce tarif n'est pas d'application sur les donations entre  vifs de biens mobiliers qui sont assimilés à des legs en  application de l'article 2.7.1.0.3, 3°.

1° het Vlaamse Gewest en de Vlaamse Gemeenschap;  1° à la Région flamande et à la Communauté flamande  ;

2° de Vlaamse, de Franse en de Gemeenschappelijke  Gemeenschapscommissie;

3° de Franse en de Duitstalige Gemeenschap en aan het  Waalse en het Brusselse Hoofdstedelijke Gewest;

4° een staat van de Europese Economische Ruimte;  4° à un Etat de l'Espace économique européen ;

5° provincies en gemeenten in het Vlaamse Gewest;  5° aux provinces et communes en Région flamande ;

6° de openbare instellingen van de publiekrechtelijke  rechtspersonen, vermeld in de punt 1° tot en met 5° ;

7° erkende woonmaatschappijen als vermeld in artikel  4.36 van de Vlaamse Codex Wonen van 2021;

8° het Vlaams Woningfonds;  8° au Fonds flamand du Logement ;

9° dienstverlenende en opdrachthoudende verenigingen  als vermeld in artikel 12, § 2, 2° en 3°, van het decreet  van 6 juli 2001 houdende de intergemeentelijke  samenwerking;

10° verenigingen zonder winstoogmerk, ziekenfondsen  en landsbonden van ziekenfondsen, internationale  verenigingen zonder winstoogmerk en stichtingen van  openbaar nut;

11° openbare centra voor maatschappelijk welzijn.  11° aux centres publics d'action sociale.

In afwijking van paragraaf 1 en 2 bedraagt het tarief van  de schenkbelasting 5,5% voor schenkingen, inclusief  inbrengen om niet, aan beroepsverenigingen en private  stichtingen.

In afwijking van het tweede lid wordt de  schenkbelasting, vermeld in paragraaf 1 en 2, gebracht  op 100 euro voor de schenkingen, inclusief inbrengen  om niet, gedaan aan rechtspersonen als vermeld in het  tweede lid, als de schenker zelf een rechtspersoon als  vermeld in het eerste lid, 10°, of het tweede lid, is.

---- historiek ----  ---- historique ----

- gewijzigd door art. 17 van het decreet van 09.12.2022  (B.S. 20.12.2022). Inwerkingtreding: 30.12.2022

- gewijzigd door art. 13 van het decreet van 09.07.2021  (B.S., 10.09.2021). Inwerkingtreding: 20.09.2021

- gewijzigd door art. 23 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- gewijzigd door art. 5 van het decreet van 19.03.2021  (B.S., 07.04.2021 – err. B.S., 09.07.2024).  Inwerkingtreding op 01.07.2021. Van toepassing op  schenkingen, inclusief inbrengen om niet, vanaf 1 juli  2021.

- gewijzigd door art. 43 van het besluit van 17.07.2020  (B.S. 17.11.2020). Tekst treedt in werking op 01.01.2021.  Bekrachtigd door art. 224, 2° van het decreet van  09.07.2021 (B.S., 10.09.2021). Inwerkingtreding:  20.09.2021.

- gewijzigd door art. 11 van het decreet van 21.12.2018  (B.S. 28.12.2018). Inwerkingtreding op 01.05.2019 (art.  3 van het besluit van 05.04.2019 - B.S.

07.05.2019)

- §2, 1°, 2° gewijzigd door art. 10 van het decreet van 17  juli 2015 (B.S., 14.08.2015 ). De tekst is in werking  getreden op 14 augustus 2015 (art. 41)

###### Art. 2.8.4.1.2.  Art. 2.8.4.1.2.

Als een akte of geschrift, overeengekomen tussen  dezelfde partijen, verschillende van elkaar afhankelijke  of noodzakelijk uit elkaar voortvloeiende regelingen  bevat waaronder een schenking die onderworpen is aan  de schenkbelasting, wordt de belasting geheven die van  toepassing is op de regeling die aanleiding geeft tot de  heffing van de hoogste belasting, vastgesteld met  toepassing van hoofdstuk 8 tot en met hoofdstuk 11.

---- historiek ----  ---- historique ----

- toegevoegd door art. 90 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

##### Onderafdeling 2. - Tijdelijke bepalingen voor schenkingen

van percelen grond die volgens de stedenbouwkundige

voorschriften bestemd zijn voor woningbouw

---- historiek ----  ---- historique ----

- onderafdeling 2 toegevoegd door art. 91 van het decreet  van 19.12.2014 (B.S., 29.01.2015 - Ed. 2). De

tekst is in werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.8.4.2.1.  Art. 2.8.4.2.1.

In afwijking van artikel 2.8.4.1.1, § 1, wordt de  schenkbelasting voor schenkingen van een perceel

TABEL I / TABLEAU I  verkrijging in rechte lijn en tussen partners / acquisition en ligne directe et entre partenaires

gedeelte van de schenking / tranche de la donation  A Schijf in euro

/  A tranche en euros

Vanaf

tot en met

/  A partir de

/  jusqu'à

0,01  12.500  1  -  12.500,01  25.000  2  125  25.000,01  50.000  3  375  50.000,01  100.000  5  1.125  100.000,01  150.000  8  3.625  150.000,01  200.000  14  7.625  200.000,01  250.000  18  14.625  250.000,01  500.000  24  23.625  500.000,01  30  83.625

TABEL II / TABLEAU II  tarief tussen broers en zussen / tarif entre frères et soeurs

gedeelte van de schenking / tranche de la donation  A Schijf in euro

/  A tranche en euros

Vanaf

/  A partir de

0,01  150.000  10  -  150.000,01  175.000  50  15.000  175.000,01  65  27.500

TABEL III / TABLEAU III  tarief tussen ooms, tantes, neven en nichten / tarif entre oncles et tantes et neveux et nièces

gedeelte van de schenking / tranche de la donation  A Schijf in euro

/  A tranche en euros

Vanaf

/  A partir de

0,01  150.000  10  -

TABEL IV / TABLEAU IV  tarief tussen alle andere personen / tarif entre toutes autres personnes

gedeelte van de schenking / tranche de la donation  A Schijf in euro

/  A tranche en euros

Vanaf

/  A partir de

0,01  150.000  10  -  150.000,01  175.000  65  15.000  175.000,01  80  31.250

---- historiek ----  ---- historique ----

- tabel I gewijzigd door art. 11 van het decreet van 17 juli  2015 (B.S., 14.08.2015 ). De tekst is in werking getreden  op 14 augustus 2015 (art. 41)

- toegevoegd door art. 92 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.8.4.2.2.  Art. 2.8.4.2.2.

De schenkbelasting, vermeld in artikel 2.8.4.2.1, is niet  van toepassing op schenkingen die zijn gedaan onder  een opschortende voorwaarde die vervuld wordt na het  verstrijken van de periode, bepaald in hetzelfde artikel,  of die zijn gedaan onder een tijdsbepaling die verder  reikt dan de periode, bepaald in het voormelde artikel.

---- historiek ----  ---- historique ----

- toegevoegd door art. 93 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.8.4.2.3.  Art. 2.8.4.2.3.

De schenkbelasting, vermeld in artikel 2.8.4.2.1, wordt  alleen toegepast als in de akte van schenking  uitdrukkelijk wordt verklaard dat :

1° het perceel grond volgens de stedenbouwkundige  voorschriften bestemd is voor woningbouw;

2° de begiftigden, of een van hen, zich ertoe verbinden  om binnen vijf jaar vanaf de datum van de akte hun  hoofdverblijfplaats te vestigen op het adres van het  verkregen goed.

Bij niet-nakoming van de aangegane verbintenis,  vermeld in het eerste lid, 2°, zijn de begiftigden die de  verbintenis zijn aangegaan en niet zijn nagekomen, elk  gehouden tot betaling van de aanvullende rechten over  hun eigen aandeel in de schenking. De aanvullende  rechten zijn niet verschuldigd als de niet-nakoming van  de aangegane verbintenis het gevolg is van overmacht.

---- historiek ----  ---- historique ----

- toegevoegd door art. 94 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

##### Onderafdeling 3 - Tarieven voor schenkingen van  gebouwen onderworpen aan een energetische renovatie of  van gebouwen met conformiteitsattest die verhuurd worden

---- historiek ----  ---- historique ----

- onderafdeling 3 toegevoegd door art. 27 van het decreet  van 3 juli 2015 (B.S., 15.07.2015). De tekst is in werking  getreden op 01.07.2015 (art. 61)

###### Art. 2.8.4.3.1.  Art. 2.8.4.3.1.

§ 1. In afwijking van artikel 2.8.4.1.1, § 1, wordt de  schenkbelasting voor schenkingen van onroerende  goederen gelegen in het Vlaamse Gewest en gedaan met  ingang van 1 juli 2015 en voor 1 januari 2025, berekend  volgens het tarief, vermeld in de onderstaande tabellen,  op voorwaarde dat  :

1° de begiftigden, een van hen of de schenker die zich  het vruchtgebruik heeft voorbehouden, binnen vijf jaar  vanaf de datum van de akte van schenking  renovatiewerken laten uitvoeren aan het geschonken  onroerend goed voor een totaalbedrag van minstens  10.000 euro, exclusief de belasting over de toegevoegde  waarde, zoals blijkt uit facturen die uitgereikt zijn door  aannemers van werken;

2° l'entrepreneur de travaux, visé au point 1°, atteste que  les factures pour les travaux de rénovation, visées au  point 1°, concernent des travaux visés aux articles  6.4.1/1, 6.4.1/1/1, 6.4.1/1/2 ou 6.4.1/5, § 1er, de l'Arrêté  relatif à l'Energie du 19 novembre 2010.

2° de aannemer, vermeld in punt 1°, attesteert dat de  facturen voor de renovatiewerken, vermeld in punt 1°,  betrekking hebben op werken vermeld in de artikelen  6.4.1/1, 6.4.1/1/1, 6.4.1/1/2 of 6.4.1/5, § 1, van het  Energiebesluit van 19 november 2010.

TABEL I / TABLEAU I  verkrijging in rechte lijn en tussen partners / tarif en ligne directe et entre partenaires

overeenstemmende  gedeelte in kolom A, in %

euro

/  tarif applicable à la tranche

/  montant total de la taxe sur

Vanaf

tot en met

/  A partir de

/  à

correspondante figurant  dans la colonne A, en %

les tranches précédentes,

en euros

0,01  150.000  3  -  150.000,01  250.000  6  4500  250.000,01  450.000  12  10.500  450.000,01  18  34.500

TABEL II / TABLEAU II  verkrijging tussen alle andere personen / acquisition entre toutes les autres personnes

gedeelte van de schenking / tranche de la donation  A schijf in euro

totaalbedrag van de

tarief, toepasselijk op het

/  A tranche en euros

belasting over de  voorgaan- de gedeelten, in

overeenstemmende  gedeelte in kolom A, in %

euro

/  tarif applicable à la tranche

/  montant total de la taxe sur

Vanaf

tot en met

/  A partir de

/  à

correspondante figurant  dans la colonne A, en %

les tranches précédentes,

en euros

0,01  150 000  9  -  150 000,01  250 000  17  13 500  250 000,01  450 000  24  30 500  450 000,01  31  78 500

Het verschil tussen de schenkbelasting, berekend  overeenkomstig de tabellen van artikel 2.8.4.1.1, § 1, en  de schenkbelasting, berekend overeenkomstig de  tabellen van het eerste lid, wordt teruggegeven  overeenkomstig de bepalingen van artikel 3.6.0.0.6, §  1/1. Het abattement toegepast overeenkomstig artikel  2.8.3.0.4 en de vermindering verleend overeenkomstig  artikel 2.8.5.0.1 blijft in dat geval behouden.

La différence entre l'impôt de donation, calculé  conformément aux tableaux de l'article 2.8.4.1.1, § 1er,  et l'impôt de donation, calculé conformément aux  tableaux de l'alinéa premier, est restituée conformément  aux  dispositions de l'article 3.6.0.0.6,  §  1/1.  L'abattement appliqué conformément à l'article  2.8.3.0.4 et la réduction octroyée conformément à  l'article 2.8.5.0.1 resteront maintenus dans ce cas.

§ 2. In afwijking van artikel 2.8.4.1.1, § 1, wordt de  schenkbelasting voor schenkingen van onroerende  goederen gelegen in het Vlaamse Gewest en gedaan met  ingang van 1 juli 2015, berekend volgens het tarief,  vermeld in paragraaf 1, op voorwaarde dat de  begiftigden of een van hen, binnen een termijn van drie  jaar vanaf de datum van de akte van schenking het  conformiteitsattest, vermeld in boek 3, deel 3, van de  Vlaamse Codex Wonen van 2021, en een geregistreerde  huurovereenkomst voor het geschonken goed met een  minimumduur van negen jaar, beiden daterend van na de  datum van de akte van schenking, voorlegt. Noch de  schenker, noch de begiftigden of een van hen mogen in  de geregistreerde huurovereenkomst als huurder  optreden.

§ 2. Par dérogation à l'article 2.8.4.1.1, § 1er, l'impôt de  donation pour les donations de biens immeubles situés  en Région flamande, faites à partir du 1er juillet 2015,  est calculé selon le tarif, visé au paragraphe 1er, à  condition que les bénéficiaires ou l'un d'entre eux, dans  un délai de trois ans à partir de la date de l'acte de  donation, présente l'attestation de conformité, visée au  livre 3, partie 3, du Code flamand du Logement de 2021,  ainsi qu'un contrat de location enregistré pour le bien  donné d'une durée minimale de neuf années, les deux  datant d'après la date de l'acte de donation. Ni le  donateur ni les bénéficiaires ni un de ceux-ci ne peuvent  agir en tant que locataires dans le contrat de location  enregistré.

Het verschil tussen de schenkbelasting, berekend  overeenkomstig de tabellen van artikel 2.8.4.1.1, § 1, en

La différence entre l'impôt de donation, calculé  conformément aux tableaux de l'article 2.8.4.1.1, § 1er,

Het teruggegeven bedrag, vermeld in het tweede lid,  wordt teruggevorderd als de begiftigden geen effectieve  verhuring van negen jaar kunnen aantonen. De  begiftigden moeten de voortijdige beëindiging van de  geregistreerde  huurovereenkomst  melden  bij  de  bevoegde entiteit van de Vlaamse administratie binnen  een termijn van vier maanden vanaf de beëindiging. Om  de terugvordering te vermijden, moeten de begiftigden  bovendien binnen een termijn van zes maanden na deze  beëindiging  een  nieuwe  geregistreerde  huurovereenkomst, alsmede een conformiteitsattest,  voor het geschonken goed voorleggen.

Bij niet-nakoming van de verbintenissen, vermeld in het  derde lid, zijn de begiftigden elk gehouden tot betaling  van de teruggegeven schenkbelasting over hun eigen  aandeel  in  de  schenking.  De  teruggegeven  schenkbelasting is niet verschuldigd als de niet-  nakoming van de aangegane verbintenis het gevolg is  van overmacht.

§ 3. In afwijking van artikel 2.8.4.1.1, § 3, tweede lid,  bedraagt het tarief van de schenkbelasting 3% voor een  schenking van een onroerend goed gelegen in het  Vlaamse Gewest als de begiftigde voldoet aan de  voorwaarden, vermeld in het eerste lid van hetzij  paragraaf 1, hetzij paragraaf 2.

Het verschil tussen de schenkbelasting, berekend  overeenkomstig het artikel 2.8.4.1.1, § 3, tweede lid, en  de schenkbelasting, berekend overeenkomstig het eerste  lid, wordt teruggegeven overeenkomstig de bepalingen  van artikel 3.6.0.0.6, § 1/1, of § 1/2.

§ 4. Als in dezelfde akte of in een andere akte van  dezelfde datum naast het goed waarvoor de teruggave  overeenkomstig paragraaf 1 of paragraaf 2 wordt  gevraagd, nog andere onroerende goederen werden  geschonken, wordt de schenking van het goed waarop de  teruggave betrekking heeft, geacht vóór de schenking  van de andere goederen geregistreerd te zijn of verplicht  registreerbaar te zijn geworden.

§ 5. In geval van een aan een opschortende voorwaarde  onderworpen schenking wordt voor de toepassing van  dit artikel de datum van de vervulling van de voorwaarde  in de plaats gesteld van de datum van de akte.

---- historiek ----  ---- historique ----

- gewijzigd door art. 18 van het decreet van 09.12.2022  (B.S. 20.12.2022). Inwerkingtreding: 01.07.2021 en van  toepassing op schenkingen, inclusief inbrengen om niet,  vanaf 01.07.2021

- gewijzigd door art. 44 van het besluit van 17.07.2020  (B.S. 17.11.2020). Tekst treedt in werking op 01.01.2021.  Bekrachtigd door art. 224, 2° van het decreet van  09.07.2021 (B.S., 10.09.2021). Inwerkingtreding:  20.09.2021.

- gewijzigd door art. 18 van het decreet van 08.12.2017  (B.S.: 14.12.2017). Tekst in werking getreden op  24.12.2017

- vervangen door art. 96 van het decreet van 18 dec.  2015 (B.S., 29.12.2015). De tekst is in werking getreden  op 1 juli 2015 (art. 135)

##### Onderafdeling 4 — Tarieven voor schenkingen van een

beschermd monument waarvoor een

investeringsverplichting geldt

---- historiek ----  ---- historique ----

- ingevoegd door art. 5 van het decreet van 21.04.2017.  Tekst in werking getreden op 14.05.2017

###### Art. 2.8.4.4.1.  Art. 2.8.4.4.1.

§ 1. In afwijking van artikel 2.8.4.1.1, § 1, wordt de  schenkbelasting voor schenkingen van de geheelheid  eigendom van onroerende goederen in het Vlaamse  Gewest, gedaan voor 1 januari 2025, berekend volgens  het tarief, vermeld in de tabellen, vermeld in artikel  2.8.4.3.1, § 1, eerste lid, op voorwaarde dat:

1° binnen vijf jaar vanaf de datum van de schenkingsakte  het bedrag dat overeenstemt met het verschil tussen de  schenkbelasting, geheven conform artikel 2.8.4.1.1, § 1,  en de schenkbelasting, verschuldigd bij gebrek aan  toepassing van hetzelfde artikel, geïnvesteerd wordt in  beheersmaatregelen, werkzaamheden of diensten die  noodzakelijk zijn voor het behoud of de herwaardering  van de erfgoedkenmerken en -elementen van het  beschermde monument, vermeld in artikel 2.1, 16°, van  het Onroerenderfgoeddecreet van 12 juli 2013. De  voormelde beheersmaatregelen, werkzaamheden of  diensten dienen opgenomen te zijn in een goedgekeurd  beheersplan als vermeld in punt 2°, dat geldig is bij de  aanvang van de voormelde beheersmaatregelen,  werkzaamheden of diensten;

§ 2. Het bedrag, vermeld in paragraaf 1, eerste lid, 1°, is  exclusief btw.

§ 3. In afwijking van artikel 2.8.4.1.1, § 3, tweede lid,  bedraagt het tarief van de schenkbelasting 3% voor een  schenking van een onroerend goed in het Vlaamse  Gewest als de begiftigde voldoet aan de voorwaarden,  vermeld in paragraaf 1, eerste lid.

Het verschil tussen de schenkbelasting, berekend  conform artikel 2.8.4.1.1, § 3, tweede lid, en de  schenkbelasting, berekend conform het eerste lid, wordt  teruggegeven conform de bepalingen van artikel  3.6.0.0.6, § 1/3.

§ 4. Als in dezelfde akte of in een andere akte van  dezelfde datum naast het goed waarvoor de teruggave,  vermeld in paragraaf 1, wordt gevraagd, nog andere  onroerende goederen zijn geschonken, wordt de  schenking van het goed waarop de teruggave betrekking  heeft, geacht vóór de schenking van de andere goederen  geregistreerd te zijn of verplicht registreerbaar te zijn  geworden.

§ 5. Bij een schenking die onderworpen is aan een  opschortende voorwaarde, wordt voor de toepassing van  dit artikel de datum van de vervulling van de voorwaarde  in de plaats gesteld van de datum van de akte.

§ 6. Het voordeel van de toepassing van paragraaf 1 of 3  kan niet gecombineerd worden met de premies, vermeld  in artikel 10.2.1 van het Onroerenderfgoeddecreet van  12 juli 2013, noch met de  belastingvermindering  van  de  personenbelasting,  vermeld in artikel 145/36 van het Wetboek van de  Inkomstenbelastingen 1992, als de voormelde premies  of de belastingvermindering betrekking hebben op  dezelfde  beheersmaatregelen,  werkzaamheden  of  diensten als de beheersmaatregelen, de werkzaamheden  of de diensten, vermeld in paragraaf 1, eerste lid, 1°.

---- historiek ----  ---- historique ----

- gewijzigd door art. 41 van het decreet van 20.12.2024  (B.S., 30.12.2024). Inwerkingtreding: 01.01.2025 en van  toepassing op schenkingen, inclusief inbrengen om niet,  vanaf 01.07.2021

- gewijzigd door art. 19 van het decreet van 09.12.2022  (B.S. 20.12.2022). Inwerkingtreding: 01.07.2021 en van  toepassing op schenkingen, inclusief inbrengen om niet,  vanaf 01.07.2021

- gewijzigd door art. 24 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- gewijzigd door art. 11 van het decreet van 06.07.2018  (B.S. 30.08.2018). Tekst in werking getreden op  31.08.2018

- aangevuld door art. 19 van het decreet van 08.12.2017  (B.S.: 14.12.2017). Tekst in werking

getreden op 24.12.2017

- ingevoegd door art. 6 van het decreet van 21.04.2017.  Tekst in werking getreden op 14.05.2017

#### Afdeling 5 – Verminderingen  Section 5 – Réductions

---- historiek ----  ---- historique ----

- afdeling 5 toegevoegd door art. 95 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.8.5.0.1.  Art. 2.8.5.0.1.

§ 1. Als de belastingplichtige op het tijdstip waarop de  schenkbelasting opvorderbaar is, minstens drie kinderen  in leven heeft die de leeftijd van eenentwintig jaar niet  hebben bereikt, wordt de met toepassing van artikel  2.8.4.1.1, § 1, vastgestelde schenkbelasting verminderd  met 2% voor elk van die kinderen van de begiftigde,  zonder dat de vermindering meer dan 62 euro per kind  mag bedragen.

Die vermindering wordt ten gunste van de begiftigde  partner gebracht op 4% per kind dat de leeftijd van  eenentwintig jaar niet heeft bereikt, zonder dat de  vermindering meer dan 124 euro per kind mag bedragen.

Voor de toepassing van deze paragraaf wordt een kind  dat verwekt is op het ogenblik van de schenking, als het  levensvatbaar geboren wordt, gelijkgesteld met een  geboren kind.

De belastingplichtige die over het aantal kinderen een  onjuiste verklaring heeft afgelegd, is aanvullende  rechten verschuldigd.

---- historiek ----

- tweede lid opgeheven door art. 12 van het decreet

van 17 juli 2015 (B.S., 14.08.2015 ). De tekst is in  werking getreden op 14 augustus 2015 (art. 41)

#### Afdeling 6 – Vrijstellingen  Section 6 – Exonérations

---- historiek ----  ---- historique ----

- toegevoegd door art. 97 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.8.6.0.1.  Art. 2.8.6.0.1.

Er wordt een vrijstelling van de schenkbelasting  verleend voor :

1° de overeenkomsten houdende schenking van  vruchtgebruik  aan  de  blote  eigenaar,  als  de  schenkbelasting of de erfbelasting of een soortgelijk  recht door de blote eigenaar of door een vorige blote  eigenaar, zijn rechtsvoorganger, op de waarde van de  volle eigendom is voldaan;

2° de overeenkomsten houdende schenking van  onroerende goederen die in het buitenland liggen;

3° op voorwaarde van wederkerigheid, de akten  houdende schenking aan vreemde staten van onroerende  goederen die bestemd zijn tot vestiging van hun  diplomatieke of consulaire vertegenwoordiging in  België, of voor de woning van het hoofd van de  standplaats;

4° de akten houdende schenking van onroerende  goederen als vermeld in artikel 2.8.4.1.1, § 1, voor zover  die schenking plaatsvindt met het oog op de realisatie  van een brownfieldproject dat het voorwerp uitmaakt of  zal uitmaken van een bownfieldconvenant als vermeld  in het decreet van 30 maart 2007 betreffende de  Brownfieldconvenanten.

De vrijstelling, vermeld in het eerste lid, 4°, wordt alleen  verleend als bij de aan de formaliteit van de registratie  onderworpen akte of verklaring over de overeenkomst  een attest is gevoegd waarin wordt bevestigd dat de  schenking plaatsvindt met het oog op de realisatie van  een brownfieldproject dat het voorwerp uitmaakt of zal  uitmaken van een brownfieldconvenant, en dat de  onroerende goederen waarvoor de vrijstelling wordt  gevraagd, deel uitmaken van dat brownfieldproject. De  Vlaamse Regering bepaalt de nadere regels voor de  vormgeving van dat attest.

Als de overeenkomst, vermeld in het eerste lid, 4°, ook  andere onroerende goederen omvat dan de onroerende  goederen, vermeld in het tweede lid, moet de  verkoopwaarde  van  elk  van  de  onderscheiden  categorieën van onroerende goederen worden  opgegeven in een aanvullende verklaring als vermeld in  artikel 3.13.1.2.1, eerste lid.

De schenkbelasting is alsnog verschuldigd door de  verkrijger van de onroerende goederen, vermeld in het  eerste lid, 4°, als de Vlaamse Regering beslist tot  stopzetting van de onderhandelingen als vermeld in  artikel 8, § 3, vierde lid, van het decreet van 30 maart  2007 betreffende de Brownfieldconvenanten, of als het  brownfieldproject  niet  tijdig  wordt  gestart  of  gerealiseerd conform de voorwaarden, vermeld in het  brownfieldconvenant.  De  schenkbelasting  wordt  opeisbaar vanaf de kennisgeving aan het bevoegde  personeelslid van het niet langer vervuld zijn van de  voorwaarden voor het behoud van de vrijstelling. De  Vlaamse Regering bepaalt de nadere regels voor die  kennisgeving.

---- historiek ----  ---- historique ----

- gewijzigd door art. 25 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- gewijzigd door art. 39 van het decreet van 23.12.2016  (B.S.: 30.12.2016). Tekst in werking getreden op  08.01.2017

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.8.6.0.2.  Art. 2.8.6.0.2.

Er wordt een vrijstelling van de schenkbelasting  verleend voor vonnissen en arresten houdende  vernietiging, ontbinding of herroeping van een  schenking van onroerende goederen die in België liggen.

Als de vernietiging, ontbinding of herroeping, vermeld  in het eerste lid, uitgesproken is ten voordele van een  andere persoon dan een van de partijen bij de  overeenkomst, haar erfgenamen of legatarissen, wordt al  naargelang het geval de belasting, vermeld in hoofdstuk  8 tot en met hoofdstuk 11, geheven die verschuldigd  geweest zou zijn als de vernietiging, de ontbinding of de  herroeping het voorwerp van een minnelijke akte had  uitgemaakt.

---- historiek ----  ---- historique ----

- toegevoegd door art. 99 van het decreet van 19.12.2014  (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.8.6.0.3.  Art. 2.8.6.0.3.

§ 1. In afwijking van artikel 2.8.4.1.1 wordt van de  schenkbelasting vrijgesteld :

1° de schenking van de volle eigendom, de blote  eigendom of het vruchtgebruik van de activa die door de  schenker of zijn partner beroepsmatig zijn geïnvesteerd  in een familiale onderneming. Die vrijstelling is niet van  toepassing op de overdrachten van onroerende goederen die hoofdzakelijk tot bewoning worden  aangewend  of  zijn  bestemd  met  inbegrip  van  bouwgronden als vermeld in artikel 1.1.0.0.2, zesde lid, 1°  /1;

2° de schenking van de volle eigendom, de blote  eigendom of het vruchtgebruik van aandelen van een  familiale vennootschap met zetel van werkelijke leiding  in een van de staten van de Europese Economische  Ruimte, op voorwaarde dat de aandelen van de  vennootschap die op het ogenblik van de schenking  onder de levenden in volle eigendom toebehoren aan de  schenker en zijn familie, ten minste 50% van de  stemrechten in die vennootschap vertegenwoordigen.  De vrijstelling is niet van toepassing op het gedeelte van  de waarde van de aandelen dat de onroerende goederen,  vermeld in punt 1°, in de familiale vennootschap, of in  participaties van minstens 10% van de familiale  vennootschap  in  haar  dochtervennootschappen,  vertegenwoordigt. Deze beperking is niet van toepassing  voor familiale vennootschappen waarvan de omzet voor  minstens 75% wordt gegenereerd door de uitoefening

In afwijking van het eerste lid vertegenwoordigen de  aandelen van de vennootschap die op het ogenblik van  de schenking in volle eigendom toebehoren aan de  schenker en zijn familie, minstens 30% van de  stemrechten in die vennootschap, als hij en zijn familie  aan een van de volgende voorwaarden voldoen:

1° samen met één andere aandeelhouder en zijn familie  volle eigenaar zijn van de aandelen van de vennootschap  die minstens 70% van de stemrechten in die  vennootschap vertegenwoordigen;

2° samen met twee andere aandeelhouders en hun  familie volle eigenaar zijn van de aandelen van de  vennootschap die minstens 90% van de stemrechten in  die vennootschap vertegenwoordigen.

Voor de toepassing van het tweede lid komen de  aandelen die toebehoren aan rechtspersonen, niet in  aanmerking om te worden samengeteld met de aandelen  die toebehoren aan de schenker.

§ 2. Voor de toepassing van dit artikel en artikel  2.8.6.0.4 tot en met artikel 2.8.6.0.7 wordt verstaan  onder :

1° familiale onderneming : een nijverheids-, handels-,  ambachts- of landbouwbedrijf of een vrij beroep dat  door de schenker of zijn partner, al dan niet samen met  anderen,  persoonlijk  wordt  geëxploiteerd  en  uitgeoefend;

2° familiale vennootschap : een vennootschap die de  uitoefening van een nijverheids-, handels-, ambachts- of  landbouwactiviteit, of van een vrij beroep tot voorwerp  heeft en uitoefent.

Als de vennootschap aan het voorgaande niet  beantwoordt, maar aandelen houdt die minstens 30 %  van  de  stemrechten  van  één  directe  dochtervennootschap vertegenwoordigen die aan die  voorwaarde beantwoordt en die haar zetel van  werkelijke leiding heeft in een van de staten van de  Europese  Economische  Ruimte,  wordt  ze  ook  beschouwd als een familiale vennootschap.

3° aandelen :  3° actions :

a) naargelang het geval:  a) selon le cas :

1) als de familiale vennootschap een naamloze  vennootschap, een Europese vennootschap of een  Europese coöperatieve vennootschap is, dan wel een  vennootschap met een andere rechtsvorm waarvoor het  Belgische of buitenlandse recht dat haar beheerst,  voorziet in een vergelijkbaar begrip: elk deelbewijs met  stemrecht dat een deel van het kapitaal  vertegenwoordigt;

2) als de familiale vennootschap een vennootschapsvorm  heeft waarvoor het Belgische of buitenlandse recht dat de  vennootschap beheerst, niet voorziet in het begrip  kapitaal of een vergelijkbaar begrip: elk deelbewijs met  stemrecht dat is uitgereikt als tegenprestatie voor een  inbreng of naar aanleiding van de incorporatie van  onbeschikbare reserves;

b) de certificaten van aandelen, uitgereikt door  rechtspersonen met een zetel in een van de staten van de  Europese  Economische  Ruimte,  ter

b) les certificats d'actions délivrés par des personnes  morales ayant leur siège dans l'un des Etats membres de  l'Espace économique européen, à titre de représentation  vertegen|Upwoordiging van aandelen van familiale  vennootschappen die aan de gestelde voorwaarden  voldoen en waarvan de rechtspersoon de verplichting  heeft om de dividenden en andere vermogensvoordelen  onmiddellijk en uiterlijk binnen een maand door te  storten aan de certificaathouder;

4° familie van de schenker of de aandeelhouder als  vermeld in paragraaf 1, eerste lid, 2° :

a) de partner van de schenker of aandeelhouder, waarbij  het begrip partner voor de aandeelhouder op een  gelijkaardige wijze moet worden geïnterpreteerd als dat  het geval is voor de schenker;

b) de verwanten in rechte lijn van de schenker of  aandeelhouder, alsook hun partners, waarbij het begrip  partner op een gelijkaardige wijze moet worden  geïnterpreteerd als dat het geval is voor de schenker;

d) de kinderen van broers en zussen van de schenker of  aandeelhouder.

§ 3. Als een vennootschap met toepassing van paragraaf  2, 2°, tweede lid, als een familiale vennootschap wordt  beschouwd, wordt de vrijstelling beperkt tot de waarden  van de aandelen van de vennootschap in de  dochtervennootschappen die de uitoefening van een  nijverheids-, handels-, ambachts- of landbouwactiviteit,  of van een vrij beroep tot voorwerp hebben en die hun  zetel van werkelijke leiding in een van de staten van de  Europese Economische Ruimte hebben.

---- historiek ----  ---- historique ----

- gewijzigd door art. 8 van het decreet van 19.12.2025  (B.S. 30.12.2025). Inwerkingtreding: Van toepassing op  alle authentieke schenkingsakten die worden verleend  vanaf 1 januari 2026.

- gewijzigd door art. 26 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- gewijzigd door art. 12 van het decreet van 21.12.2018  (B.S. 28.12.2018). Inwerkingtreding op 01.05.2019 (art.  3 van het besluit van 05.04.2019 - B.S.

07.05.2019)

- gewijzigd door art. 13 van het decreet van 17 juli 2015  (B.S., 14.08.2015 ). De tekst is in werking getreden op 14  augustus 2015 (art. 41)

###### Art. 2.8.6.0.4.  Art. 2.8.6.0.4.

De vrijstelling, vermeld in artikel 2.8.6.0.3, is alleen  toepasselijk als de volgende voorwaarden cumulatief  zijn vervuld :

1° de schenking van de activa of aandelen van de  familiale  onderneming  of  vennootschap  wordt  vastgesteld bij authentieke akte;

---- historiek ----  ---- historique ----

- gewijzigd door art. 27 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- 2° vervangen door art. 14 van het decreet van 17 juli  2015 (B.S., 14.08.2015 ). De tekst is in werking getreden  op 14 augustus 2015 (art. 41)

###### Art. 2.8.6.0.5.  Art. 2.8.6.0.5.

Voor de toepassing van artikel 2.8.6.0.3 en artikel  2.8.6.0.6. , § 1, 2°, moet de aanwending of de  bestemming van een onroerend goed worden nagegaan  per kadastraal perceel of per gedeelte van een kadastraal  perceel als dat gedeelte ofwel een afzonderlijke  huisvesting is, ofwel een afdeling van de productie of  van de werkzaamheden is die, of een onderdeel daarvan  dat, afzonderlijk kan werken, ofwel een eenheid is die  van de andere goederen of delen die het perceel vormen,  kan worden afgezonderd.

---- historiek ----  ---- historique ----

- toegevoegd door art. 102 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.8.6.0.6.  Art. 2.8.6.0.6.

§ 1. De vrijstelling, vermeld in artikel 2.8.6.0.3, § 1,  eerste lid, 1°, wordt behouden als de volgende  voorwaarden cumulatief zijn vervuld;

1° als een activiteit van de familiale onderneming zonder  onderbreking wordt voortgezet gedurende drie jaar  vanaf de datum van de authentieke akte van schenking ;

2° als de onroerende goederen die met toepassing van de  vrijstelling zijn overge|Updragen, niet hoofdzakelijk tot  bewoning aangewend of bestemd worden gedurende een  periode van drie jaar vanaf de datum van de authentieke  akte van schenking.

§ 2. De vrijstelling, vermeld in artikel 2.8.6.0.3, § 1,  eerste lid, 2°, wordt alleen behouden als al de volgende  voorwaarden zijn vervuld:

1° de familiale vennootschap blijft gedurende drie jaar  vanaf de datum van de authentieke akte van schenking  voldoen aan de voorwaarden, vermeld in artikel  2.8.6.0.3, § 2, 2° ;

3° voor elk van de drie jaar vanaf de datum van de  authentieke akte van schenking wordt een jaarrekening  of geconsolideerde jaarrekening opgemaakt die in  voorkomend geval wordt gepubliceerd conform de  geldende boekhoudwetgeving van de lidstaat waar de  zetel gevestigd is op het ogenblik van de datum van de  authentieke akte van schenking, die ook aangewend is ter  verantwoording van de aangifte in de  inkomstenbelasting.

Ondernemingen of vennootschappen waarvan de zetel  buiten het Vlaamse Gewest, maar binnen België ligt,  maken een jaarrekening of geconsolideerde jaarrekening  op en in voorkomend geval publiceren ze die conform  de geldende boekhoudwetgeving in België op de datum  van de authentieke akte van schenking;

4° naargelang het geval:  4° selon le cas :

a) als de familiale vennootschap een naamloze  vennootschap, een Europese vennootschap of een  Europese coöperatieve vennootschap is, of een  vennootschap met een andere rechtsvorm waarvoor het  Belgische of buitenlandse recht dat haar beheerst,  voorziet in een vergelijkbaar begrip: het kapitaal daalt  op  geen  enkel  moment  door  uitkeringen  of  terugbetalingen gedurende drie jaar vanaf de datum van  de authentieke akte van schenking;

b)  als  de  familiale  vennootschap  een  vennootschapsvorm heeft waarvoor het Belgische of  buitenlandse recht dat de vennootschap beheerst, niet  voorziet in het begrip kapitaal of een vergelijkbaar  begrip: de verrichte inbrengen dalen op geen enkel  moment gedurende drie jaar vanaf de datum van de  authentieke akte van schenking door uitkeringen of  terugbetalingen tot onder het bedrag van de tot op de  datum van de authentieke akte van schenking verrichte  inbrengen, zoals dat blijkt uit de jaarrekening;

5° de zetel van de werkelijke leiding van de  vennootschap wordt niet overgebracht naar een staat die  geen lid is van de Europese Economische Ruimte  gedurende drie jaar vanaf de datum van de authentieke  akte van schenking.

---- historiek ----  ---- historique ----

- gewijzigd door art. 28 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- gewijzigd door art. 13 van het decreet van 21.12.2018  (B.S. 28.12.2018). Inwerkingtreding op 01.05.2019 (art.  3 van het besluit van 05.04.2019 - B.S.

07.05.2019)

- toegevoegd door art. 103 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.8.6.0.7.  Art. 2.8.6.0.7.  § 1. Na verloop van een termijn van drie jaar na de datum  van de authentieke akte van schenking controleert het  bevoegde personeelslid of de voorwaarden, gesteld voor  het behoud van de vrijstelling, vervuld zijn.

Bij niet-vervulling van de voorwaarden, vermeld in het  eerste lid, wordt de schenkbelasting geacht verschuldigd  te zijn, berekend tegen het tarief, vermeld in artikel  2.8.4.1.1, zonder toepassing van de vrijstelling.

Bij niet-vervulling van de voorwaarde, vermeld in  artikel 2.8.6.0.6, § 2, 4°, is de schenkbelasting  verschuldigd tegen het tarief, vermeld in artikel  2.8.4.1.1, zonder toepassing van de vrijstelling op het  bedrag waarmee het kapitaal is verminderd of waarmee  de  verrichte  inbrengen  zijn  verminderd,  vermenigvuldigd met  de  grondslag  waarop  de  vrijstelling is toegepast, en gedeeld door de waarde van  alle aandelen van de familiale vennootschap op de  datum van de authentieke schenkingsakte.

§ 2. Als de schenkbelasting verschuldigd is doordat de  voorwaarden, gesteld tot behoud van de vrijstelling, niet  langer vervuld zijn, kunnen de begiftigden dat melden  bij de bevoegde entiteit van de Vlaamse administratie.

Bij niet-vervulling van de voorwaarden, vermeld in het  eerste lid, wordt de schenkbelasting geacht verschuldigd  te zijn, berekend tegen het tarief, vermeld in artikel  2.8.4.1.1, zonder toepassing van de vrijstelling.

Bij niet-vervulling van de voorwaarde, vermeld in  artikel 2.8.6.0.6, § 2, 4°, is de schenkbelasting  verschuldigd tegen het tarief, vermeld in artikel  2.8.4.1.1, zonder toepassing van de vrijstelling op het  bedrag waarmee het kapitaal is verminderd of waarmee  de  verrichte  inbrengen  zijn  verminderd,  vermenigvuldigd met  de  grondslag  waarop  de  vrijstelling is toegepast, en gedeeld door de waarde van  alle aandelen van de familiale vennootschap op de  datum van de authentieke schenkingsakte.

- gewijzigd door art. 10 van het decreet van 19.12.2025  (B.S. 30.12.2025). Inwerkingtreding: Van toepassing op  alle authentieke schenkingsakten die worden verleend  vanaf 1 januari 2026.

- toegevoegd door art. 104 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.8.6.0.8.  Art. 2.8.6.0.8.

§ 1. De waarde van de onbebouwde onroerende  goederen waarvoor een natuurbeheerplan type twee, drie  of vier als vermeld in artikel 16ter, § 1, 2°, 3° en 4°, van  het decreet van 21 oktober 1997 betreffende het  natuurbehoud en het natuurlijk milieu, is goedgekeurd  conform artikel 16octies van het voormelde decreet,  wordt,  zowel  voor  de  grond-  als  voor  de  opstandswaarde, als volgt van de schenkbelasting  vrijgesteld:

1° ten belope van 75% voor een natuurbeheerplan type  twee;

2° ten belope van 100% voor een natuurbeheerplan type  drie en vier.

§ 2. De vrijstelling, vermeld in paragraaf 1, is ook van  toepassing als er nog geen natuurbeheerplan is  afgesloten, als het onroerend goed wordt geschonken

§ 2. L’exemption visée au paragraphe 1er, s’applique  également lorsqu’aucun plan de gestion de la nature n’a  été conclu, lorsque le bien immobilier fait l’objet d’une  met het oog op het tot stand brengen van een  natuurbeheerplan type twee, drie of vier als vermeld in  artikel 16ter, § 1, 2°, 3° en 4°, van het decreet van 21  oktober 1997 betreffende het natuurbehoud en het  natuurlijk milieu.

De vrijstelling, vermeld in het eerste lid, wordt verleend  op voorwaarde dat uiterlijk bij de aanbieding ter  registratie van de authentieke schenkingsakte een  overeenkomst is gesloten met het Agentschap voor  Natuur en Bos waaruit de intentie blijkt om een  natuurbeheerplan voor het onroerend goed te laten  goedkeuren.

§ 3. Voor de toepassing van dit artikel moet voldaan zijn  aan de verplichtingen van artikel 3.12.3.0.1, § 1, 4°, en  § 5, vierde en vijfde lid.

---- historiek ----  ---- historique ----

- gewijzigd door art. 14 van het decreet van 21.12.2018  (B.S. 28.12.2018). Tekst treedt in werking op 09.06.2018

30.05.2018)

###### Art. 2.8.6.0.9.  Art. 2.8.6.0.9.

Als de waarde van de goederen die belast is met de  erfbelasting, of een deel van deze goederen, binnen het  jaar na het overlijden van de erflater, door een verkrijger  van wie de verkrijging belast werd aan het tarief voor  een verkrijging in de rechte lijn en tussen partners, bij  notariële akte wordt geschonken aan een of meer van  zijn afstammelingen of aan een of meer personen die  voor de toepassing van de schenkbelasting met  afstammelingen  worden  gelijkgesteld,  wordt  de  schenking vrijgesteld van de schenkbelasting in de mate  dat de waarde van de geschonken goederen de  brutowaarde van de met erfbelasting belaste goederen  niet te boven gaat.

In voorkomend geval wordt het bedrag van de  vrijstelling, vermeld in het eerste lid, beperkt met  toepassing van de volgende formule:

X = a x b/c, waarbij de parameters als volgt worden  gedefinieerd:

1° a = het bedrag van de schenkbelasting zonder de  toepassing van de vrijstelling;

2° b = het gedeelte van de schenking dat overeenstemt  met de met erfbelasting belaste brutowaarde;

2° b = la partie de la donation qui correspond à la valeur  brute soumise à l’impôt de succession ;  3° c = de totale belastbare grondslag van de schenking.  3° c = la base imposable totale de la donation.

Het bedrag van de vrijstelling, vermeld in het eerste lid,  kan nooit hoger zijn dan het bedrag van de erfbelasting  dat geheven werd op de overdracht aan de schenker. Als  de schenker meer dan één schenking doet zoals vermeld  in het eerste lid, wordt het maximumbedrag van de  vrijstelling beoordeeld voor alle schenkingen samen.

In voorkomend geval wordt het bedrag van de  erfbelasting, vermeld in het derde lid, beperkt met  toepassing van de volgende formule: X = a x b/c, waarbij  de parameters als volgt worden gedefinieerd:

1° a = het bedrag van de erfbelasting berekend in hoofde  van de schenker ;

2° b = het gedeelte van de schenking dat overeenstemt  met de met erfbelasting belaste brutowaarde;

3° c = de brutowaarde van de met erfbelasting belaste  goederen.

Voor schenkingen onderworpen aan het tarief, vermeld  in artikel 2.8.4.1.1, § 1, of artikel 2.8.4.2.1, kan de  vrijstelling niet verleend worden in de mate deze  schenking een onroerend goed tot voorwerp heeft dat  geen deel uitmaakte van de verkrijging bij het  overlijden, vermeld in het eerste lid.

Voor de toepassing van de vrijstelling, vermeld in het  eerste lid, is vereist dat:

1° de nalatenschap van de erflater waaruit de waarde van  de geschonken goederen werd verkregen fiscaal  gelokaliseerd is in het Vlaamse Gewest;

2° het overlijden heeft plaatsgevonden na 31 augustus  2018;

3° de erfbelasting die werd geheven op de overdracht, is  betaald;

4° de schenking noch aan een opschortende voorwaarde,  noch aan een opschortende termijn is onderworpen;

5° de vrijstelling wordt gevraagd overeenkomstig artikel  3.12.3.0.1, § 1, 3° en 4°.

Voor de toepassing van dit artikel moet onder  brutowaarde worden begrepen: de belastbare waarde

Pour l’application du présent article, on entend par  valeur brute : la valeur imposable des biens concernés  van de betrokken goederen voor de heffing van de  erfbelasting, vóór enige aftrek van passief.

---- historiek ----  ---- historique ----

- gewijzigd door art. 15 van het decreet van 21.12.2018  (B.S. 28.12.2018). Tekst treedt in werking op 07.01.2019

- ingevoegd door art. 11 van het decreet van 06.07.2018  (B.S. 20.07.2018 Ed. 2). Tekst treedt in

werking op 01.09.2018

###### Art. 2.8.6.0.10.  Art. 2.8.6.0.10.

Er wordt een vrijstelling van de schenkbelasting  verleend voor de akten in der minne die betrekking  hebben op onroerende goederen die uitsluitend bestemd  zijn voor onderwijs, en die verleden zijn op naam van of  ten voordele van de inrichtende machten van het  gemeenschapsonderwijs of het gesubsidieerd onderwijs,  of op naam van of ten voordele van verenigingen zonder  winstoogmerk voor patrimoniaal beheer die uitsluitend  tot doel hebben onroerende goederen ter beschikking te

---- historiek ----  ---- historique ----

- ingevoegd door art. 29 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

#### Afdeling 7 - Wijze van heffing  Section 7 - Modalités de perception

---- historiek ----  ---- historique ----

- afdeling 7 toegevoegd door art. 105 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.8.7.0.1.  Art. 2.8.7.0.1.

De schenkbelasting wordt geheven in overeenstemming  met de bepalingen van artikel 3.3.2.0.1, 9°, en artikel  3.3.3.0.1, § 4/2.

---- historiek ----  ---- historique ----

- toegevoegd door art. 106 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.8.7.0.2.  Art. 2.8.7.0.2.

§ 1. De belastingplicht, de belastbare grondslag, het  tarief, de vrijstellingen en de verminderingen worden  bepaald door het ogenblik waarop de rechtshandeling is  gesteld.

In afwijking van het eerste lid worden, als er geen  verplichting tot registratie geldt, de belastingplicht, de  belastbare grondslag en het tarief bepaald door het  ogenblik waarop de akte of het geschrift ter registratie  wordt aangeboden.

§ 2. Op een rechtshandeling die onderworpen is aan een  opschortende voorwaarde, wordt de schenkbelasting  alleen geheven als de voorwaarde vervuld is. In  voorkomend geval wordt gehandeld als volgt :

1° het toepasbare tarief waarmee voor de heffing  rekening moet worden gehouden, is het tarief dat van  kracht is op de datum waarop de schenkbelasting  opvorderbaar geweest zou zijn als de handeling  onvoorwaardelijk was;

2° de belastbare grondslag waarmee voor de heffing  rekening moet worden gehouden, is de belastbare  grondslag op de datum van de vervulling van de  voorwaarde.

---- historiek ----  ---- historique ----

- toegevoegd door art. 107 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.8.7.0.3.  Art. 2.8.7.0.3.

In geval van een handelszaak wordt de schenkbelasting  vastgesteld volgens de aard van elk goed dat er deel van  uitmaakt.

---- historiek ----  ---- historique ----

- toegevoegd door art. 108 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

### Hoofdstuk 9 - Verkooprecht  Chapitre 9 - Droit de vente

---- historiek ----  ---- historique ----

- hoofdstuk 9 toegevoegd door art. 109 van het decreet  van 19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

#### Afdeling 1 - Belastbaar voorwerp  Section 1re - Objet imposable

---- historiek ----  ---- historique ----

- afdeling 1 toegevoegd door art. 110 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.9.1.0.1.  Art. 2.9.1.0.1.

Conformément à l'article 1er, à l'article 19 et à l'article  31 du Code fédéral des droits d'enregistrement,  d'hypothèque et de greffe, le droit de vente est établi à  l'occasion de l'enregistrement ou de l'obligation  d'enregistrement d'actes ou d'écrits tendant à prouver  une convention translative à titre onéreux de propriété  ou d'usufruit de biens immeubles, à l'exception des  apports visés à l'article 115bis du Code fédéral des droits  d'enregistrement, d'hypothèque et de greffe.  vermeld in artikel 115bis van het federale Wetboek van  Registratie-, Hypotheek- en Griffierechten.

Overeenkomstig artikel 1, artikel 19 en artikel 31 van het  federale Wetboek van Registratie-, Hypotheek- en  Griffierechten wordt het verkooprecht gevestigd naar  aanleiding van de registratie of de verplichting tot  registratie van akten of geschriften die als titel gelden  van een overeenkomst houdende overdracht onder  bezwarende titel van eigendom of vruchtgebruik van  onroerende goederen, met uitsluiting van de inbrengen,

---- historiek ----  ---- historique ----

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.9.1.0.2.  Art. 2.9.1.0.2.

Voor de toepassing van dit hoofdstuk worden de  volgende overeenkomsten gelijkgesteld met een  overeenkomst houdende overdracht onder bezwarende  titel van eigendom van onroerende goederen :

1° een overdragende overeenkomst onder bezwarende  titel, waarbij de eigendom wordt verkregen van, hetzij  hout op stam onder beding van het te vellen, hetzij  gebouwen onder beding van ze te slopen, als de  eigendom van de grond nadien wordt verkregen voor het  hout helemaal geveld is of de gebouwen helemaal  gesloopt zijn;

2° een overeenkomst onder de levenden onder  bezwarende titel, waarbij de eigendom wordt verkregen  van hetzij hout op stam, hetzij gebouwen, als die  bewuste overdracht ten voordele van de eigenaar van de  grond wordt toegestaan.

Het eerste lid is niet van toepassing als bewezen wordt  dat de belasting over de toegevoegde waarde is voldaan  voor de levering van de goederen die in de overeenkomst  begrepen zijn.

---- historiek ----  ---- historique ----

- toegevoegd door art. 112 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.9.1.0.3.  Art. 2.9.1.0.3.

Met behoud van de toepassing van artikel 2.9.1.0.1,  wordt, behoudens vestiging van de belasting, vermeld in  hoofdstuk 10 en 11, het verkooprecht gevestigd op een  inbreng van onroerende goederen als vermeld in artikel  115bis van het federale Wetboek van Registratie-,  Hypotheek- en Griffierechten in een Belgische  vennootschap naarmate die inbreng anders vergoed  wordt dan bij toekenning van maatschappelijke rechten.

Als een inbreng als vermeld in het eerste lid meteen  onroerende goederen als vermeld in artikel 115bis van  het federale Wetboek van Registratie-, Hypotheek- en  Griffierechten en goederen van een andere aard omvat,  worden, niettegenstaande elk strijdig beding, de  maatschappelijke rechten en de andere lasten die de

Het eerste en het tweede lid zijn niet van toepassing op  de inbreng van de universaliteit van de goederen of van  een bedrijfstak, vermeld in artikel 117, § 1 en § 2, van  het federale Wetboek van Registratie-, Hypotheek- en  Griffierechten.

Dit artikel is ook van toepassing op de oprichting van  nieuwe vennootschappen, als vermeld in artikel 118 van  het federale Wetboek van Registratie-, Hypotheek- en  Griffierechten.

---- historiek ----  ---- historique ----

- toegevoegd door art. 113 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.9.1.0.4.  Art. 2.9.1.0.4.

Het verkooprecht wordt ook gevestigd op de verkrijging,  op welke wijze ook, anders dan bij inbreng in een  vennootschap, door een of meer vennoten van  onroerende goederen die in België liggen en die  voortkomen van een vennootschap onder firma, van een  commanditaire  vennootschap,  van  een  besloten  vennootschap of van een coöperatieve vennootschap.

De verkrijging zal evenwel belast worden volgens haar  gemeenrechtelijke aard als het gaat om :

1° onroerende goederen die in de vennootschap zijn  ingebracht, als ze verkregen zijn door de persoon die de  inbreng gedaan heeft;

2° onroerende goederen die door de vennootschap met  betaling van het verkooprecht verkregen zijn, als het  vaststaat dat de vennoot die eigenaar van die onroerende  goederen wordt, deel uitmaakte van de vennootschap  toen laatstgenoemde de goederen verkreeg.

In geval van verkrijging van maatschappelijke  onroerende goederen door al de vennoten door een (…)  vereffening conform boek 2, titel 8, hoofdstuk 1,  afdeling 2, van het Wetboek van Vennootschappen en  Verenigingen, is, naargelang van het geval, de  registratiebelasting die met toepassing van het eerste of  het tweede lid is gevestigd, van toepassing  op de latere toebedeling van de goederen aan een of meer  vennoten.

---- historiek ----  ---- historique ----

- gewijzigd door art. 15 van het decreet van 03.04.2026  (B.S. 23.04.2026). Inwerkingtreding op 03.05.2026

- gewijzigd door art. 20 van het decreet van 09.12.2022  (B.S. 20.12.2022). Inwerkingtreding: 30.12.2022

- gewijzigd door art. 16 van het decreet van 21.12.2018  (B.S. 28.12.2018). Inwerkingtreding op 01.05.2019 (art.  3 van het besluit van 05.04.2019 - B.S. 07.05.2019)

- tweede lid, 2° gewijzigd door art. 15 van het decreet  van 17 juli 2015 (B.S., 14.08.2015 ). De tekst is in  werking getreden op 14 augustus 2015 (art. 41)

###### Art. 2.9.1.0.5.  Art. 2.9.1.0.5.

Het verkooprecht wordt ook gevestigd op de verkrijging,  op welke wijze ook, door een of meer vennoten van  onroerende goederen die in België liggen en die  voortkomen van een naamloze vennootschap, van een  Europese  vennootschap  of  van  een  Europese  coöperatieve vennootschap.

Het eerste lid is niet van toepassing bij een verkrijging  bij wijze van inbreng in een vennootschap.

---- historiek ----  ---- historique ----

- gewijzigd door art. 17 van het decreet van 21.12.2018  (B.S. 28.12.2018). Inwerkingtreding op 01.05.2019 (art.  3 van het besluit van 05.04.2019 - B.S.

07.05.2019)

- toegevoegd door art. 115 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.9.1.0.6.  Art. 2.9.1.0.6.

§ 1. Vonnissen en arresten die tot bewijs strekken van  een overeenkomst waarop de bepalingen van deze  afdeling van toepassing zijn, maar die nog niet aan het  verkooprecht onderworpen is, geven aanleiding tot de  heffing van het verkooprecht.

§ 2. Exequaturs van scheidsrechterlijke uitspraken en in  het buitenland gewezen rechterlijke beslissingen  worden, voor de toepassing van dit hoofdstuk, als een  geheel met de desbetreffende akte beschouwd. Als de  desbetreffende akte tot bewijs strekt van een  overeenkomst houdende overdracht onder bezwarende  titel van eigendom of vruchtgebruik van in het Vlaamse

§ 2. Les exequaturs de sentences arbitrales et de  décisions  judiciaires  rendues  à  l'étranger  sont  considérés, pour l'application du présent chapitre,  comme formant un tout avec l'acte concerné. Si l'acte  concerné tend à prouver une convention translative à  titre onéreux de propriété ou d'usufruit de biens  immeubles qui doivent être localisés dans la Région

Dat geldt ook als de scheidsrechterlijke uitspraak of in  het buitenland gewezen rechterlijke beslissing die tot  bewijs van de overeenkomst strekt, de ontbinding of  herroeping ervan uitspreekt of vaststelt voor om het even  welke reden, tenzij uit de beslissing blijkt dat ten hoogste  één jaar na de overeenkomst een eis tot ontbinding of  herroeping, zelfs bij een onbevoegde rechter, is  ingesteld.

Het verkooprecht is ook van toepassing in geval van  aanbieding ter registratie van een in het buitenland  gewezen rechterlijke beslissing die van rechtswege in  België uitvoerbaar is.

---- historiek ----  ---- historique ----

- toegevoegd door art. 116 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.9.1.0.7.  Art. 2.9.1.0.7.

In afwijking van artikel 2.10.1.0.1 wordt in geval van  toebedeling bij verdeling of van afstand van onverdeelde  delen aan een derde die bij overeenkomst een onverdeeld  deel heeft verkregen van goederen die toebehoren aan  een of meer personen, het verkooprecht geheven op de  delen waarvan de derde ten gevolge van de  overeenkomst eigenaar wordt, met toepassing van  artikel 2.9.3.0.1 en artikel 2.9.3.0.4 tot en met artikel  2.9.3.0.7.

Het eerste lid is van toepassing als de toebedeling van  goederen of de afstand van onverdeelde delen gedaan  wordt aan de erfgenamen of legatarissen van de  overleden derde verkrijger.

Het eerste lid is niet van toepassing als de derde, aan wie  de toebedeling of de afstand gedaan wordt, met anderen  het geheel van een of meer goederen heeft verkregen.

---- historiek ----  ---- historique ----

- toegevoegd door art. 117 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

#### Afdeling 2 – Belastingplichtigen  Section 2 - Contribuables

---- historiek ----  ---- historique ----

- afdeling 2 toegevoegd door art. 118 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

De belastingplichtige is de verkrijger van het zakelijk  recht.

Bij een ruilovereenkomst is de belastingplichtige de  verkrijger van het onroerend goed waarvan de  overeengekomen waarde als heffingsgrondslag heeft  gediend overeenkomstig artikel 2.9.7.0.2.

Voor de belasting, vermeld in artikel 2.9.4.2.9, is de  belastingplichtige de persoon die als eerste met naam  wordt vermeld in de akte die of het geschrift dat ter  registratie wordt aangeboden.

---- historiek ----  ---- historique ----

- toegevoegd door art. 119 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

#### Afdeling 3 - Belastbare grondslag  Section 3 - Base imposable

---- historiek ----  ---- historique ----

- afdeling 3 toegevoegd door art. 120 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.9.3.0.1.  Art. 2.9.3.0.1.

§ 1. Het verkooprecht wordt vastgesteld op basis van het  bedrag van de overeengekomen prijs en lasten of het  bedrag van de overeengekomen tegenprestatie ten laste  van de verkrijger.

In afwijking van het eerste lid wordt het verkooprecht  voor overeenkomsten tot inbreng van onroerende  goederen in vennootschappen vastgesteld op basis van  het bedrag van de waarde van de als vergoeding voor de  inbreng toegekende maatschappelijke rechten, verhoogd  met de lasten die door de vennootschap gedragen  worden.

§ 2. De belastbare grondslag mag in geen geval lager zijn  dan de verkoopwaarde van de overgedragen onroerende  goederen.

---- historiek ----  ---- historique ----

- toegevoegd door art. 121 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.9.3.0.2.  Art. 2.9.3.0.2.

(…)  (…)

- opgeheven door art. 3 van het decreet van 18.05.2018  (B.S.: 28.05.2018). Tekst is van toepassing op  verkoopovereenkomsten afgesloten vanaf 1 juni 2018

- § 1, derde lid vervangen door art. 16 van het decreet  van 17 juli 2015 (B.S., 14.08.2015 ). De tekst is in  werking getreden op 14 augustus 2015 (art. 41)

- toegevoegd door art. 122 van het decreet van  19.12.2014 (B.S. 29.01.2015 Ed.2). Inwerkingtreding

op 01.01.2015 (art. 325)

###### Art. 2.9.3.0.3.  Art. 2.9.3.0.3.

(…)  (…)

---- historiek ----  ---- historique ----

- opgeheven door art. 3 van het decreet van 18.05.2018  (B.S.: 28.05.2018). Tekst is van toepassing op  verkoopovereenkomsten afgesloten vanaf 1 juni 2018

- gewijzigd door art. 40 van het decreet van 23.12.2016  (B.S.: 30.12.2016). Tekst in werking getreden op 8  januari 2017

- toegevoegd door art. 123 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.9.3.0.4.  Art. 2.9.3.0.4.

§ 1. Als bij een overeenkomst als vermeld in artikel  2.9.3.0.1, een levenslang vruchtgebruik op een  onroerend  goed  wordt  gevestigd,  wordt  de  verkoopwaarde (vkw), vermeld in artikel 2.9.3.0.1, § 2,  berekend volgens de volgende formule : vkw = a x b.

De parameters, vermeld in het eerste lid, worden als  volgt gedefinieerd :

1° a = de jaarlijkse bruto-opbrengst of, bij gebrek  daaraan, de brutohuurwaarde van het goed;

2° b = de leeftijdscoëfficiënt, vermeld in de  onderstaande tabel, naargelang de leeftijd van de  persoon op het hoofd van wie het vruchtgebruik is  gevestigd op de dag van de akte :

Leeftijdscoëfficiënt

établie, en années  18  ≤ 20  17  > 20-30  16  > 30-40  14  > 40-50  13  > 50-55  11  > 55-60  9,5  > 60-65  8  > 65-70  6  > 70-75  4  > 75-80  2  > 80

§ 2. Als bij een overeenkomst als vermeld in artikel  2.9.3.0.1, een vruchtgebruik voor beperkte tijd op een  onroerend  goed  wordt  gevestigd,  wordt  de  verkoopwaarde, vermeld in artikel 2.9.3.0.1, § 2,  berekend door de jaarlijkse opbrengst tegen 4% te  kapitaliseren, rekening houdend met de bij de  overeenkomst gestelde duur van het vruchtgebruik.

De verkoopwaarde, verkregen in het eerste lid, mag niet  hoger zijn dan een van de volgende bedragen :

1° de waarde, vermeld in paragraaf 1, als het gaat om een  ten voordele van een natuurlijke persoon gevestigd  vruchtgebruik;

2° het bedrag van twintig keer de opbrengst van het  onroerend goed, als het gaat om een ten voordele van een  rechtspersoon gevestigd vruchtgebruik.

§ 3. In geen geval mag de verkoopwaarde van het  vruchtgebruik meer bedragen dan vier vijfde van de  verkoopwaarde van de volle eigendom van het onroerend  goed.

---- historiek ----  ---- historique ----

- toegevoegd door art. 124 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.9.3.0.5.  Art. 2.9.3.0.5.

Als bij een overeenkomst als vermeld in artikel 2.9.3.0.1,  de blote eigendom wordt overgedragen met voorbehoud  van het vruchtgebruik, mag de verkoopwaarde, vermeld  in artikel 2.9.3.0.1, § 2, niet lager zijn dan de  verkoopwaarde van de volle eigendom.

---- historiek ----  ---- historique ----

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.9.3.0.6.  Art. 2.9.3.0.6.

Als bij een overeenkomst als vermeld in artikel 2.9.3.0.1,  de blote eigendom wordt overgedragen zonder dat het  vruchtgebruik door de vervreemder is voorbehouden,  mag de verkoopwaarde, vermeld in artikel 2.9.3.0.1, § 2,  niet lager zijn dan de verkoopwaarde van de volle  eigendom, na aftrek van de waarde van het  vruchtgebruik, berekend volgens artikel 2.9.3.0.4.

---- historiek ----  ---- historique ----

- toegevoegd door art. 126 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.9.3.0.7.  Art. 2.9.3.0.7.

Als bij een overeenkomst als vermeld in artikel 2.9.3.0.1,  een vruchtgebruik op een onroerend goed op het hoofd  van twee of meer personen wordt gevestigd, met recht  van aanwas of van terugvalling, wordt voor de toepassing  van artikel 2.9.3.0.4 en artikel 2.9.3.0.6 rekening  gehouden met de leeftijd van de jongste persoon.

---- historiek ----  ---- historique ----

- toegevoegd door art. 127 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.9.3.0.8.  Art. 2.9.3.0.8.

Het verkooprecht, verschuldigd op akten waarbij  eigendom of vruchtgebruik van een handelszaak  overgedragen wordt, wordt vastgesteld op basis van de in  deze afdeling vastgestelde grondslagen.

De schulden die al dan niet met de handelszaak in  verband staan en die door de nieuwe eigenaar of  vruchtgebruiker ten laste genomen worden, worden als  lasten van de overeenkomst beschouwd.

---- historiek ----  ---- historique ----

- toegevoegd door art. 128 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.9.3.0.9.  Art. 2.9.3.0.9.

In geval van een openbare verkoop van onroerende  goederen, in verschillende loten, wordt het verkooprecht

---- historiek ----  ---- historique ----

- toegevoegd door art. 129 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

#### Afdeling 4 – Tarieven  Section 4 – Tarifs

---- historiek ----  ---- historique ----

- afdeling 4 toegevoegd door art. 130 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

##### Onderafdeling 1 – Algemeen  Sous-section 1re - Généralités

---- historiek ----  ---- historique ----

- onderafdeling 1 toegevoegd door art. 131 van het  decreet van 19.12.2014 (B.S., 29.01.2015 - Ed. 2). De

tekst is in werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.9.4.1.1.  Art. 2.9.4.1.1.

Het verkooprecht bedraagt 12 %.  Le droit de vente se monte à 12 %.

---- historiek ----  ---- historique ----

- gewijzigd door art. 73 van het decreet van 23.12.2022  (B.S., 29.12.2021). Inwerkingtreding: 01.01.2022

- toegevoegd door art. 132 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.9.4.1.2.  Art. 2.9.4.1.2.

Als een akte of geschrift, overeengekomen tussen  dezelfde partijen, verschillende van elkaar afhankelijke  of noodzakelijk uit elkaar voortvloeiende regelingen  bevat  waaronder  een  verkoopovereenkomst  die  onderworpen is aan het verkooprecht, wordt de belasting  geheven die van toepassing is op de regeling die  aanleiding geeft tot de heffing van de hoogste belasting,  vastgesteld met toepassing van hoofdstuk 8 tot en met  hoofdstuk 11.

Als een akte of geschrift, overeengekomen tussen  dezelfde  partijen,  verschillende  van  elkaar  onafhankelijke  of  niet  noodzakelijk  uit  elkaar  voortvloeiende  regelingen  bevat  waaronder  een  verkoopovereenkomst die onderworpen is aan het  verkooprecht, wordt op elke regeling al naargelang het  geval de belasting, vermeld in hoofdstuk 8 tot en met  hoofdstuk 11, geheven.

- toegevoegd door art. 133 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

##### Onderafdeling 2 - Verlaagde tarieven  Sous-section 2 - Tarifs réduits

---- historiek ----  ---- historique ----

- onderafdeling 2 toegevoegd door art. 134 van het  decreet van 19.12.2014 (B.S., 29.01.2015 - Ed. 2). De

tekst is in werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.9.4.2.1.  Art. 2.9.4.2.1.

(…)  (…)

---- historiek ----  ---- historique ----

- opgeheven door art. 3 van het decreet van 18.05.2018  (B.S.: 28.05.2018). Tekst is van toepassing op  verkoopovereenkomsten afgesloten vanaf 1 juni 2018

- gewijzigd door art. 17 van het decreet van 17 juli 2015  (B.S., 14.08.2015 ). De tekst is in werking getreden op 14  augustus 2015 (art. 41)

###### Art. 2.9.4.2.2.  Art. 2.9.4.2.2.

(…)  (…)

---- historiek ----  ---- historique ----

- opgeheven door art. 3 van het decreet van 18.05.2018  (B.S.: 28.05.2018). Tekst is van toepassing op  verkoopovereenkomsten afgesloten vanaf 1 juni 2018

- toegevoegd door art. 136 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.9.4.2.3.  Art. 2.9.4.2.3.

In afwijking van artikel 2.9.4.1.1 bedraagt het  verkooprecht 1,50 % voor verkoopovereenkomsten van  woningen  die  gesloten  zijn  door  de  Vlaamse  Maatschappij voor Sociaal Wonen of door de erkende  woonmaatschappijen, vermeld in artikel 4.36 van de  Vlaamse Codex Wonen van 2021, en voor kopers die  voldoen aan de voorwaarden, opgelegd ter uitvoering van  artikel 4.27, 4.45 en 5.91 van de Vlaamse Codex Wonen  van 2021.

Het verlaagde tarief, vermeld in het eerste lid, is ook van  toepassing op gelijksoortige rechtspersonen die opgericht  zijn volgens en onderworpen zijn aan de wetgeving van  een staat van de Europese Economische Ruimte, en die  bovendien hun zetel, hun hoofdbestuur of hun  hoofdvestiging binnen de Europese Economische Ruimte  hebben.

---- historiek ----  ---- historique ----

- gewijzigd door art. 14 van het decreet van 09.07.2021  (B.S., 10.09.2021). Inwerkingtreding: 20.09.2021

- gewijzigd door art. 30 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- gewijzigd door art. 45 van het besluit van 17.07.2020  (B.S. 17.11.2020). Tekst treedt in werking op 01.01.2021.  Bekrachtigd door art. 224, 2° van het decreet van  09.07.2021 (B.S., 10.09.2021). Inwerkingtreding:  20.09.2021.

- toegevoegd door art. 137 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.9.4.2.4.  Art. 2.9.4.2.4.

§ 1. In afwijking van artikel 2.9.4.1.1 wordt het tarief van  het verkooprecht verlaagd tot 6% voor overeenkomsten  houdende overdrachten ten bezwarende titel, uit de hand  en bij authentieke akte, met uitsluiting van de inbrengen,  vermeld in artikel 115bis van het federale Wetboek van  Registratie-, Hypotheek- en Griffierechten, waarbij de  verkrijger een persoon is die zijn beroep maakt van het  kopen en verkopen van onroerende goederen.

§ 2. Voor de toepassing van het verlaagde tarief, vermeld  in paragraaf 1, moeten de volgende voorwaarden vervuld  zijn :

2° (…)  2° (…)

3° de verkrijger heeft de erkenning verkregen van een in  België gevestigde vertegenwoordiger die met toepassing  van artikel 3.10.4.4.5 met hem instaat voor de nakoming  van zijn fiscale verplichtingen als hij :

3° l'acquéreur a fait agréer un représentant établi en  Belgique, qui assume avec lui, en application de l'article  3.10.4.4.5, l'exécution de ses obligations fiscales s'il est  :  a) een natuurlijke persoon is en zijn wettelijke  verblijfplaats buiten de Europese Economische Ruimte  heeft;

b) een rechtspersoon is zonder vestiging in België  waarvan de zetel gevestigd is buiten de Europese  Economische Ruimte.

§ 3. De akte die de verklaring, vermeld in artikel  3.12.3.0.1, § 1, niet bevat of waarbij de verklaring,  vermeld in artikel 3.12.3.0.1, § 3, tweede lid, niet  gevoegd is, wordt tegen het tarief, vermeld in artikel  2.9.4.1.1, geregistreerd zonder enige mogelijkheid tot  teruggave.

Een andere beroepspersoon dan de persoon, vermeld in  paragraaf 2, 3°, kan de erkenning verkrijgen van een in  België  gevestigde  vertegenwoordiger  die  medeaansprakelijk is en hoofdelijk met hem instaat voor  de nakoming van zijn fiscale verplichtingen.

§ 4. Als de persoon die een beroepsverklaring heeft  ondertekend, bij het verstrijken van een termijn van vijf  jaar na die verklaring, geen drie wederverkopen kan  aantonen waardoor blijkt dat hij het aangegeven beroep  werkelijk uitoefent, is hij op al zijn aankopen het  verkooprecht, vermeld in artikel 2.9.4.1.1, verschuldigd  na aftrek van de reeds geheven belasting.

---- historiek ----  ---- historique ----

- gewijzigd door art. 38 van het decreet van 20.12.2024  (B.S., 30.12.2024). Inwerkingtreding: 01.01.2025

- gewijzigd door art. 31 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- §1 vervangen door art. 18 van het decreet van 17 juli  2015 (B.S., 14.08.2015 ). De tekst is in werking getreden  op 14 augustus 2015 (art. 41)

§ 1. Als de verkrijger, vermeld in artikel 2.9.4.2.4, § 1, of  zijn rechthebbenden het verkregen onroerend goed niet  vervreemd hebben door een wederverkoop of elke andere  overdracht onder bezwarende titel, vastgesteld bij een  authentieke akte die uiterlijk verleden is op 31 december  van het achtste jaar na de datum van de koopakte, is het  tarief, vermeld in artikel 2.9.4.1.1, dat van kracht is op  het ogenblik van de aankoop, verschuldigd na aftrek van  de reeds geheven belasting.

Het verkooprecht wordt geheven op de belastbare  grondslag, vermeld in artikel 2.9.3.0.1, op het moment  van de aankoop.

Als slechts een deel van tegen een enige prijs  aangekochte onroerende goederen wordt vervreemd,  wordt de belastbare waarde van het niet-vervreemde  gedeelte bepaald naar verhouding van de omvang.

Une revente à un professionnel en application de l'article  2.9.4.2.4 et un apport dans une société ne sont pas  considérés comme une revente telle que visée au premier  wederverkoop als vermeld in het eerste lid. Een  overdracht onder bezwarende titel die aan het  verdeelrecht is onderworpen, wordt niet beschouwd als  een overdracht onder bezwarende titel als vermeld in het  eerste lid.

Een wederverkoop aan een beroepspersoon met  toepassing van artikel 2.9.4.2.4 en een inbreng in een  vennootschap  worden  niet  beschouwd  als  een

§ 2. De verkrijger mag de betaling aanbieden van de  belasting, vermeld in paragraaf 1, eerste lid, vóór het  verstrijken van de termijn, vermeld in paragraaf 1, eerste  lid. Hij moet daarvoor een verklaring indienen bij de  bevoegde entiteit van de Vlaamse administratie. Die  verklaring vermeldt de samenstelling en de waarde van  de goederen waarvoor hij de belasting wil betalen.

---- historiek ----  ---- historique ----

- gewijzigd door art. 19 van het decreet van 17 juli 2015  (B.S., 14.08.2015 ). De tekst is in werking getreden op 14  augustus 2015 (art. 41)

###### Art. 2.9.4.2.6.  Art. 2.9.4.2.6.

Bij overlijden van de vertegenwoordiger van een  beroepspersoon als vermeld in artikel 2.9.4.2.4, § 2, 3°,  bij de intrekking van zijn erkenning of als hij onbekwaam  wordt verklaard om als vertegenwoordiger op te treden,  moet binnen een termijn van zes maanden in zijn  vervanging voorzien worden.

Als de voorschriften, vermeld in het eerste lid, niet  voldaan zijn, is de belasting, vermeld in artikel 2.9.4.2.5,  verschuldigd voor de niet-wederverkochte goederen.

- gewijzigd door art. 32 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- toegevoegd door art. 140 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.9.4.2.7.  Art. 2.9.4.2.7.

In afwijking van artikel 2.9.4.1.1 bedraagt het  verkooprecht 6% voor een koopovereenkomst ter  verwezenlijking van haar voorwerp :

1° door een maatschappij die erkend is door de Vlaamse  Maatschappij voor Sociaal Wonen, op voorwaarde van  bewijs van haar erkenning;

2° door het Vlaams Woningfonds.  2° le Fonds flamand du logement ;

Het verlaagde tarief, vermeld in het eerste lid, is ook van  toepassing op gelijksoortige rechtspersonen die opgericht  zijn volgens en onderworpen zijn aan de wetgeving van  een staat van de Europese Economische Ruimte, en die  bovendien hun zetel, hun hoofdbestuur of hun

Le tarif réduit mentionné au premier alinéa s'applique  également aux personnes morales analogues créées  conformément et assujetties à la législation d'un Etat  membre de l'Espace économique européen et ayant en  outre leur siège, leur direction générale ou leur  hoofdvestiging binnen de Europese Economische  Ruimte hebben.

---- historiek ----  ---- historique ----

- gewijzigd door art. 33 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- toegevoegd door art. 141 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.9.4.2.8.  Art. 2.9.4.2.8.

§ 1. In afwijking van artikel 2.9.4.1.1 wordt het tarief van  het  verkooprecht  verlaagd  tot  6%  voor  de  ruilovereenkomsten van ongebouwde landgoederen  waarvan de oppervlakte van elk van de kavels niet meer  bedraagt dan vijf hectare, op voorwaarde dat het  waardeverschil tussen elk van de kavels of de opleg een  vierde van de verkoopwaarde van de minste kavel niet te  boven gaat.

Voor de toepassing van het tarief, vermeld in het eerste  lid, moet voldaan zijn aan de verplichtingen van artikel  3.12.3.0.1, § 1 en § 3, derde lid.

§ 2. Voor elke te laag bevonden opleg of elk te laag  bevonden waardeverschil, zijn aanvullende rechten  verschuldigd.

---- historiek ----  ---- historique ----

- gewijzigd door art. 34 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- gewijzigd door art. 12 van het decreet van 22.06.2018.  Tekst in werking getreden vanaf aanslagjaar 2019

- toegevoegd door art. 142 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.9.4.2.9.  Art. 2.9.4.2.9.

§ 1. Een overeenkomst als vermeld in artikel 2.9.1.0.1,  wordt onderworpen aan een tarief van 10 euro als ze niet  bij authentieke akte is vastgesteld, en als binnen de  termijnen, overeenkomstig artikel 32 of artikel 33 van het  federale Wetboek van Registratie-, Hypotheek- en  Griffierechten, samen met de ter registratie aangeboden  akte of het ter registratie aangeboden geschrift een  schriftelijk vastgestelde overeenkomst ter registratie  wordt aangeboden waarin alle partijen verklaren de  eerste overeenkomst in der minne te hebben ontbonden  of vernietigd of waarin ze verklaren dat een in de eerste  overeenkomst uitdrukkelijk bedongen ontbindende  voorwaarde al is vervuld.

Het tarief, vermeld in het eerste lid, geldt niet voor de  inbrengen door een natuurlijke persoon van een woning

Ce tarif ne vaut pas pour les apports par une personne  physique d'une habitation dans une société belge par une  in een Belgische vennootschap.  personne physique.

§ 2. De schriftelijk vastgestelde overeenkomst waarin  alle partijen verklaren een overeenkomst, zoals  omschreven in artikel 2.9.1.0.1, te hebben ontbonden of  vernietigd of waarin ze verklaren dat een in die  overeenkomst uitdrukkelijk bedongen ontbindende  voorwaarde is vervuld, wordt geregistreerd tegen het  tarief van 10 euro op voorwaarde dat die ontbonden of  vernietigde overeenkomst :

1° niet bij authentieke akte is vastgesteld;  1° n'ait pas été constatée par acte authentique ;

2° dateert van minder dan één jaar vóór de dagtekening  van de ter registratie aangeboden overeenkomst.

---- historiek ----  ---- historique ----

- gewijzigd door art. 35 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.9.4.2.10.  Art. 2.9.4.2.10.

§ 1. Het tarief, vermeld in artikel 2.9.4.1.1, wordt voor  overeenkomsten gesloten voor 1 januari 2025 gehalveerd  voor verkrijgingen onder bezwarende titel bij authentieke  akte van de geheelheid eigendom van een beschermd  monument als vermeld in artikel 2.1, 16°, van het  Onroerenderfgoeddecreet van 12 juli 2013, met  uitzondering van ruilovereenkomsten die onder de  toepassing vallen van artikel 2.9.7.0.2.

§ 2. Voor de toepassing van het verlaagde tarief, vermeld  in paragraaf 1, moeten de volgende voorwaarden vervuld  zijn:

1° de verkrijgers verbinden zich ertoe dat minstens het  bedrag dat overeenkomt met het verschil tussen het  verkooprecht, geheven met toepassing van paragraaf 1,  en het verkooprecht, verschuldigd bij gebrek aan  toepassing van hetzelfde artikel, binnen vijf jaar vanaf de  datum van de authentieke akte van verkrijging  geïnvesteerd  wordt  in  beheersmaatregelen,  werkzaamheden of diensten die noodzakelijk zijn voor  het behoud of de herwaardering van erfgoedkenmerken  en -elementen van het beschermde monument, vermeld  in artikel 2.1, 16°, van het Onroerenderfgoeddecreet van  12 juli 2013. De voormelde beheersmaatregelen,  werkzaamheden of diensten dienen opgenomen te zijn in  een goedgekeurd beheersplan als vermeld in punt 2°, dat  geldig  is  bij  de  aanvang  van  de  voormelde  beheersmaatregelen, werkzaamheden of diensten;

2° voor het beschermde monument, vermeld in artikel  2.1, 16°, van het Onroerenderfgoeddecreet van 12 juli  2013, is er een goedgekeurd beheersplan of zal een

2° pour le monument protégé, visé à l’article 2.1, 16°, du  Décret relatif au patrimoine immobilier du 12 juillet  2013, il y a un plan de gestion approuvé ou un plan de  beheersplan opgemaakt worden conform hoofdstuk 8 van  het Onroerenderfgoeddecreet van 12 juli 2013 en  hoofdstuk 8 van het Onroerenderfgoedbesluit van 16 mei  2014. Het beheersplan is goedgekeurd of zal worden  goedgekeurd door het agentschap, vermeld in artikel 2.1,  2°, van het Onroerenderfgoeddecreet van 12 juli 2013;

3° de verkrijgers voldoen aan de verplichting, vermeld in  artikel 3.12.3.0.1, § 1 en § 3, vierde lid.

§ 3. Het bedrag, vermeld in paragraaf 2, 1°, is exclusief  btw.

§ 4. Het voordeel van de toepassing van de  tariefvermindering uit dit artikel kan niet gecombineerd  worden met de toepassing van de vermindering, vermeld  in artikel 2.9.5.0.1, noch met de ontheffing, vermeld in  artikel 3.6.0.0.6, § 3.

§ 5. Bij een rechtshandeling als vermeld in paragraaf 1  die onderworpen is aan een opschortende voorwaarde,  wordt voor de toepassing van dit artikel de datum van de  vervulling van de voorwaarde in de plaats gesteld van de  datum van de akte.

---- historiek ----  ---- historique ----

- gewijzigd door art. 42 van het decreet van 20.12.2024  (B.S., 30.12.2024). Inwerkingtreding: 01.01.2025

- gewijzigd door art. 36 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- gewijzigd door art. 12 van het decreet van 06.07.2018  (B.S. 30.08.2018). Tekst in werking getreden op  31.08.2018

- gewijzigd door art. 4 van het decreet van 18.05.2018  (B.S.: 28.05.2018). Tekst is van toepassing op  verkoopovereenkomsten afgesloten vanaf 1 juni 2018

- ingevoegd door art. 7 van het decreet van 21.04.2017.  Tekst in werking getreden op 14.05.2017

###### Art. 2.9.4.2.11.  Art. 2.9.4.2.11.

§ 1. In afwijking van artikel 2.9.4.1.1 bedraagt het  verkooprecht 2 % voor overeenkomsten houdende  zuivere aankoop van volle eigendom, waarbij uitsluitend  door een of meer natuurlijke personen samen en  gelijktijdig de geheelheid volle eigendom van een  woning wordt verkregen om er hun  hoofdverblijfplaats te vestigen.

In afwijking van het eerste lid bedraagt het tarief 6% voor  overeenkomsten houdende zuivere aankoop waarvan de  authentieke akte uiterlijk op 31 december 2023 is  verleden, als de verkrijger opteert voor de vermindering,  vermeld in artikel 2.9.5.0.1, of de ontheffing, vermeld in  artikel 3.6.0.0.6, § 3.

§ 2. Om het verlaagde tarief, vermeld in paragraaf 1, te  kunnen toepassen, moeten alle volgende voorwaarden  vervuld zijn:

2° de verkrijger verbindt zich ertoe zijn inschrijving in  het bevolkingsregister of het vreemdelingenregister te  nemen op het adres van de aangekochte woning binnen  drie jaar na de datum van de authentieke aankoopakte, en  die inschrijving gedurende een ononderbroken periode  van minstens een jaar te behouden;

3° de verplichting, vermeld in artikel 3.12.3.0.1, § 1, is  nageleefd.

De koper die de voorwaarde, vermeld in het eerste lid, 2°,  niet is nagekomen, is aanvullende rechten verschuldigd.

§ 3. In afwijking van paragraaf 2, 1°, wordt geen rekening  gehouden met de woning of de bouwgrond als:

1° de verkrijger zich ertoe verbindt om dit onroerend  goed uiterlijk twee jaar na de datum van de authentieke  akte volledig en ten bezwarende titel te vervreemden en  aantoont dat er een causaal verband bestaat tussen die  vervreemding en de verkrijging tegen het verlaagd tarief,  vermeld in paragraaf 1, en als de verkrijger voldoet aan  de verplichting, vermeld in artikel 3.12.3.0.1, § 3, vijfde  lid;

2° het onroerend goed uiterlijk een jaar na de datum van  de authentieke akte van verkrijging, al dan niet  gedwongen, wordt onteigend en als de verkrijger voldoet  aan de verplichting, vermeld in artikel 3.12.3.0.1, § 3,  zesde lid.

De koper die de voorwaarden, vermeld in het eerste lid,  1° of 2°, niet is nagekomen, is aanvullende rechten  verschuldigd.

§ 4. In geval van een overdracht, die aan een  opschortende voorwaarde is onderworpen die nog niet is  vervuld op datum van de authentieke akte, wordt voor de  toepassing van dit artikel de datum van vervulling van de  voorwaarde in de plaats gesteld van de datum van de  authentieke akte.

§ 5. Het tarief, vermeld in paragraaf 1, kan niet voor het  bijbehorende terrein worden toegepast als voor de  overdracht van het gebouw of gedeelten van het gebouw  de vrijstelling, vermeld in  artikel 2.9.6.0.1, eerste lid, 4°, is genoten.

---- historiek ----  ---- historique ----

- gewijzigd door art. 34 van het decreet van 19.12.2025  (B.S. 30.12.2025). Inwerkingtreding: Van toepassing op  verkoopovereenkomsten afgesloten vanaf 1 januari 2026

- gewijzigd door art. 35 van het decreet van 20.12.2024  (B.S. 30.12.2024). Inwerkingtreding: 01.01.2025

- gewijzigd door art. 21 van het decreet van 09.12.2022  (B.S. 20.12.2022). Inwerkingtreding: 30.12.2022

- gewijzigd door art. 74 van het decreet van 23.12.2021  (B.S., 29.12.2021). Van toepassing op overeenkomsten  houdende zuivere aankoop gesloten vanaf 1 januari 2022,  of, in afwijking daarvan, op authentieke akten verleden  vanaf 1 januari 2022, wanneer de overeenkomsten  houdende zuivere aankoop waarop de akten betrekking  hebben, gesloten zijn voor 1 januari 2022

- gewijzigd door art. 37 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- gewijzigd door art. 2 van het decreet van 26 juni 2020  (B.S., 29.06.2020). Tekst treedt in werking op 01.06.2020

- gewijzigd door art. 32 van het programmadecreet van  20 december 2019 (B.S. 30.12.2019). Tekst is van  toepassing op overeenkomsten houdende zuivere aankoop  gesloten vanaf 1 januari 2020, of, in afwijking daarvan,  op authentieke akten verleden vanaf 1 januari 2020,  wanneer de overeen- komsten houdende zuivere aankoop  waarop deze akten betrekking hebben, gesloten zijn voor 1  januari 2020

- gewijzigd door art. 18 van het decreet van 21.12.2018  (B.S. 28.12.2018). Tekst is van toepassing op  verkoopovereenkomsten afgesloten vanaf 1 juni 2018

- ingevoegd door art. 5 van het decreet van 18.05.2018  (B.S.: 28.05.2018). Tekst is van toepassing op  verkoopovereenkomsten afgesloten vanaf 1 juni 2018

###### Art. 2.9.4.2.12.  Art. 2.9.4.2.12.

§ 1. Het verlaagde tarief, vermeld in artikel 2.9.4.2.11, §  1, eerste lid, wordt verminderd tot 1% voor  verkoopovereenkomsten gesloten voor 1 januari 2025,  als aan al de volgende voorwaarden is voldaan:

2° de verkrijger heeft binnen een termijn van zes jaar  vanaf de datum van de authentieke aankoopakte een  EPB-aangifte als vermeld in artikel 1.1.3, 47°, van het  Energiedecreet van 8 mei 2009, laten indienen waaruit  blijkt dat de werken die aan de aangekochte woning  uitgevoerd zijn, betrekking hebben op werken als  vermeld in punt 1° en dat is voldaan aan alle EPB-eisen,  vermeld in titel IX, hoofdstuk I, van het Energiebesluit  van  19  november  2010,  die  op  de  omgevingsvergunning(en)  voor  stedenbouwkundige  handelingen van het specifieke bouwproject van  toepassing zijn;

3° de verkrijger is op de datum van de authentieke  aankoopakte niet voor de geheelheid volle eigenaar van  een andere woning of bouwgrond. Als er verschillende  verkrijgers zijn, zijn ze op de vermelde datum niet samen  voor de geheelheid volle eigenaar van een andere woning  of bouwgrond;

4° de verkrijger verbindt zich ertoe zijn inschrijving in  het bevolkingsregister of het vreemdelingenregister te  nemen op het adres van de aangekochte woning binnen  zes jaar na de datum van de authentieke aankoopakte;

5° de verplichting, vermeld in artikel 3.12.3.0.1, § 1, is  nageleefd.

De koper die de voorwaarden, vermeld in het eerste lid,  1°, 2° en 4°, niet is nagekomen, is aanvullende rechten  verschuldigd.

Als de verkrijger zich ertoe verbindt een gedeeltelijke  herbouw of een herbouw uit te voeren als vermeld in het  eerste lid, 1°, wordt voor de toepassing van het verlaagd  tarief met een woning gelijkgesteld een huis of het geheel  of gedeelte van een verdieping van een gebouw dat op  een bepaald moment in de periode van vijf jaar  voorafgaand aan de datum van de authentieke  aankoopakte hoofdzakelijk tot huisvesting heeft gediend  van één gezin of een persoon, als de verklaring, vermeld  in artikel 3.12.3.0.1, § 3, zevende lid, is gedaan.

De koper die de voorwaarde, vermeld in het derde lid,  niet is nagekomen, is aanvullende rechten verschuldigd.

In afwijking van het eerste lid bedraagt het tarief 5% voor  overeenkomsten houdende zuivere aankoop waarvan de  authentieke akte uiterlijk op 31 december 2023 is  verleden, als de verkrijger opteert voor de vermindering,  vermeld in artikel 2.9.5.0.1, of de ontheffing, vermeld in

§ 2. In afwijking van paragraaf 1, 3°, wordt geen rekening  gehouden met de woning of de bouwgrond als:

1° de verkrijger zich ertoe verbindt om dit onroerend  goed uiterlijk drie jaar na de datum van de authentieke  akte volledig en ten bezwarende titel te vervreemden en  aantoont dat er een causaal verband bestaat tussen die  vervreemding en de verkrijging tegen het verlaagd tarief,  vermeld in paragraaf 1, en als de verkrijger voldoet aan  de verplichting, vermeld in artikel 3.12.3.0.1, § 3, achtste  lid;

2° het onroerend goed uiterlijk een jaar na de datum van  de authentieke akte van verkrijging, al dan niet  gedwongen, wordt onteigend en als de verkrijger voldoet  aan de verplichting, vermeld in artikel 3.12.3.0.1, § 3,  negende lid.

De koper die de voorwaarden, vermeld in het eerste lid,  1° of 2°, niet is nagekomen, is aanvullende rechten  verschuldigd.

§ 3. In geval van een overdracht, die aan een  opschortende voorwaarde is onderworpen die nog niet is  vervuld op datum van de authentieke akte, wordt voor de  toepassing van dit artikel de datum van vervulling van de  voorwaarde in de plaats gesteld van de datum van de akte.

§ 4. Het tarief, vermeld in paragraaf 1, eerste lid, kan niet  gecombineerd worden met de vermindering, vermeld in  artikel 2.9.5.0.1, of de ontheffing, vermeld in artikel  3.6.0.0.6, § 3.

---- historiek ----  ---- historique ----

- gewijzigd door art. 40 van het decreet van 20.12.2024  (B.S., 30.12.2024). Inwerkingtreding: 01.01.2025

- gewijzigd door art. 22 van het decreet van 09.12.2022  (B.S. 20.12.2022). Inwerkingtreding: 30.12.2022

- gewijzigd door art. 75 van het decreet van 23.12.2021  (B.S., 29.12.2021). Van toepassing op overeenkomsten  houdende zuivere aankoop gesloten vanaf 1 januari 2022,  of, in afwijking daarvan, op authentieke akten verleden  vanaf 1 januari 2022, wanneer de overeenkomsten  houdende zuivere aankoop waarop de akten betrekking  hebben, gesloten zijn voor 1 januari 2022

- gewijzigd door art. 38 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- gewijzigd door art. 3 van het decreet van 26 juni 2020  (B.S., 29.06.2020). Tekst treedt in werking op 01.01.2021

- gewijzigd door art. 33 van het programmadecreet van  20 december 2019 (B.S., 30.12.2019). Tekst is van  toepassing op overeenkomsten houdende zuivere aankoop  gesloten vanaf 1 januari 2020, of, in afwijking daarvan,  op authentieke akten verleden vanaf 1 januari 2020,  wanneer de overeen- komsten houdende zuivere aankoop  waarop deze akten betrekking hebben, gesloten zijn voor 1  januari 2020

- gewijzigd door art. 19 van het decreet van 21.12.2018  (B.S. 28.12.2018). Tekst is van toepassing op  verkoopovereenkomsten afgesloten vanaf 1 juni 2018

- ingevoegd door art. 6 van het decreet van 18.05.2018  (B.S.: 28.05.2018). Tekst is van toepassing op

verkoopovereenkomsten afgesloten vanaf 1 juni 2018

###### Art. 2.9.4.2.13.  Art. 2.9.4.2.13.

§ 1. In afwijking van artikel 2.9.4.1.1 bedraagt het  verkooprecht 7 % voor overeenkomsten houdende  zuivere aankoop, waarbij door een of meer natuurlijke  personen samen en gelijktijdig de geheelheid volle  eigendom van een woning wordt verkregen als aan de  volgende voorwaarden is voldaan:

1° de verkrijger verbindt zich ertoe om binnen een  termijn van drie jaar vanaf de datum van de authentieke  akte een huurovereenkomst met een minimumduur van 9  jaar voor het aangekochte goed af te sluiten met een  erkende woonmaatschappij met toepassing van en  conform de voorwaarden opgelegd ter uitvoering van  artikel 4.40, 4°, van de Vlaamse Codex Wonen van 2021 ;

2° de verkrijger verbindt zich ertoe om binnen een  termijn van drie jaar en zes maanden een kopie van de  geregistreerde huurovereenkomst, vermeld in punt 1°, in  te dienen bij de bevoegde entiteit van de Vlaamse  administratie;

3° de verplichting, vermeld in artikel 3.12.3.0.1, § 1, is  nageleefd.

§ 2. In geval van een overdracht, die aan een  opschortende voorwaarde is onderworpen die nog niet is  vervuld op datum van de authentieke akte, wordt voor de  toepassing van dit artikel de datum van vervulling van de  voorwaarde in de plaats gesteld van de datum van de  authentieke akte.

§ 3. Het tarief, vermeld in paragraaf 1, kan niet worden  toegepast als voor de overdracht van het gebouw, of  gedeelten van het gebouw de vrijstelling, vermeld in  artikel 2.9.6.0.1, eerste lid, 4°, is genoten.

§ 4. De verkrijgers melden de voortijdige beëindiging  van de geregistreerde huurovereenkomst bij de bevoegde  entiteit van de Vlaamse administratie binnen vier  maanden vanaf de beëindiging. Bij een beëindiging hetzij  in  onderling  overleg  tussen  de  erkende  woonmaatschappij en de verkrijgers, hetzij door toedoen  van de verkrijgers, zijn er aanvullende rechten  verschuldigd.

---- historiek ----  ---- historique ----

- gewijzigd door art. 15 van het decreet van 09.07.2021  (B.S., 10.09.2021). Inwerkingtreding: 20.09.2021

- gewijzigd door art. 39 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- gewijzigd door art. 20 van het decreet van 21.12.2018

(B.S. 28.12.2018). Tekst is van toepassing op  verkoopovereenkomsten afgesloten vanaf 1 juni 2018

- ingevoegd door art. 7 van het decreet van 18.05.2018  (B.S.: 28.05.2018). Tekst is van toepassing op  verkoopovereenkomsten afgesloten vanaf 1 juni 2018

###### Art. 2.9.4.2.14.  Art. 2.9.4.2.14.

§ 1. Het verlaagde tarief, vermeld in artikel 2.9.4.2.11,  wordt verminderd tot 1 % wanneer deze verkrijging naast  de voorwaarde, vermeld in artikel 2.9.4.2.11, § 2, eerste  lid, 1°, ook voldoet aan de voorwaarden, vermeld in  artikel 2.9.4.2.10.

§ 2. Voor de toepassing van het verlaagde tarief, vermeld  in paragraaf 1, is het bedrag, vermeld in artikel  2.9.4.2.10, § 2, 1°, minstens het bedrag dat overeenkomt  met het verschil tussen het verkooprecht, geheven met  toepassing van artikel 2.9.4.2.14, § 1, en het  verkooprecht, verschuldigd bij toepassing van artikel  2.9.4.2.11, § 1, en dit ongeacht de eventuele toepassing  van paragraaf 7.

§ 3. Het bedrag, vermeld in paragraaf 2, eerste lid, is  exclusief btw.

§ 4. Het verbod, vermeld in artikel 2.9.4.2.10, § 4, eerste  lid, geldt niet voor de verkrijgingen, vermeld in paragraaf  1.

Het  voordeel  van  de  toepassing  van  de  tariefvermindering, vermeld in paragraaf 1, kan niet  gecombineerd worden met de premies, vermeld in artikel  10.2.1 van het Onroerenderfgoeddecreet van 12 juli  2013,  noch  met  de  vermindering  van  de  personenbelasting, vermeld in artikel 145/36 van het  Wetboek van de Inkomstenbelastingen 1992, als de  voormelde  premies  of  de  belastingvermindering  betrekking hebben op dezelfde beheersmaatregelen,  werkzaamheden of diensten als de beheersmaatregelen,  de werkzaamheden of de diensten, vermeld in artikel  2.9.4.2.10, § 2, 1°.

§ 5. In afwijking van de voorwaarde, vermeld in artikel  2.9.4.2.11, § 2, eerste lid, 1°, wordt er geen rekening  gehouden met de woning of de bouwgrond als:

1° de verkrijger zich ertoe verbindt om dit onroerend  goed uiterlijk drie jaar na de datum van de authentieke  akte volledig en ten bezwarende titel te vervreemden en  aantoont dat er een causaal verband bestaat tussen die  vervreemding en de verkrijging tegen het verlaagd tarief,  vermeld in paragraaf 1, en als de verkrijger voldoet aan  de verplichting, vermeld in artikel 3.12.3.0.1, § 3, tiende  lid;

2° het onroerend goed uiterlijk een jaar na de datum van  de authentieke akte van verkrijging, al dan niet  gedwongen, wordt onteigend en als de verkrijger voldoet  aan de verplichting, vermeld in artikel 3.12.3.0.1, § 3,  elfde lid.

De koper die de voorwaarden, vermeld in het eerste lid,  1° of 2°, niet is nagekomen, is aanvullende rechten  verschuldigd.

§ 6. In geval van een overdracht, die aan een  opschortende voorwaarde is onderworpen die nog niet is  vervuld op datum van de authentieke akte, wordt voor de  toepassing van dit artikel de datum van de vervulling van  de voorwaarde in de plaats gesteld van de datum van de  authentieke akte.

---- historiek ----  ---- historique ----

- gewijzigd door art. 23 van het decreet van 09.12.2022  (B.S. 20.12.2022). Inwerkingtreding: 30.12.2022

- gewijzigd door art. 76 van het decreet van 23.12.2021  (B.S., 29.12.2021). Van toepassing op overeenkomsten  houdende zuivere aankoop gesloten vanaf 1 januari 2022,  of, in afwijking daarvan, op authentieke akten verleden  vanaf 1 januari 2022, wanneer de overeenkomsten  houdende zuivere aankoop waarop de akten betrekking  hebben, gesloten zijn voor 1 januari 2022

- gewijzigd door art. 5 van het decreet van 19.11.2021  (B.S., 16.12.2021). Inwerkingtreding: 01.01.2022

- gewijzigd door art. 40 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- gewijzigd door art. 4 van het decreet van 26 juni 2020  (B.S., 29.06.2020). Tekst treedt in werking op 01.06.2020

- gewijzigd door art. 34 van het programmadecreet van  20.12.2019 (B.S., 30.12.2019). Tekst is van toepassing op  overeenkomsten houdende zuivere aankoop gesloten vanaf  1 januari 2020, of, in afwijking daarvan, op authentieke  akten verleden vanaf 1 januari 2020, wanneer de overeen-  komsten houdende zuivere aankoop waarop deze akten  betrekking hebben, gesloten zijn voor 1 januari 2020

- gewijzigd door art. 21 van het decreet van 21.12.2018  (B.S. 28.12.2018). Tekst is van toepassing op  verkoopovereenkomsten afgesloten vanaf 1 juni 2018

- gewijzigd door art. 13 van het decreet van 06.07.2018  (B.S. 30.08.2018). Tekst van toepassing is op  verkoopovereenkomsten afgesloten vanaf 1 juni 2018

- ingevoegd door art. 8 van het decreet van 18.05.2018  (B.S.: 28.05.2018). Tekst is van toepassing op  verkoopovereenkomsten afgesloten vanaf 1 juni 2018

###### Art. 2.9.4.2.15  Art. 2.9.4.2.15.

§ 1. In afwijking van artikel 2.9.4.1.1 bedraagt het  verkooprecht 10% voor verkoopovereenkomsten van  onbebouwde  onroerende  goederen  die  stedenbouwkundig uitsluitend en volledig zijn bestemd  voor landbouw of die uitsluitend en volledig liggen in de

§ 2. Voor de toepassing van het verlaagd tarief, vermeld  in paragraaf 1, moeten naargelang het geval de volgende  voorwaarden vervuld zijn:

1° de verkrijgers van het onbebouwde onroerend goed dat  stedenbouwkundig uitsluitend en volledig is bestemd  voor landbouw of dat uitsluitend en volledig ligt in de  categorie  gebiedsaanduiding  landbouw  of  een  subcategorie van de gebiedsaanduiding landbouw  voldoen aan de verplichting, vermeld in artikel  3.12.3.0.1, § 1;

2° de verkrijgers van het onbebouwde onroerend goed  waarvoor een natuurbeheerplan type twee of drie als  vermeld in artikel 16ter, § 1, 2° en 3°, van het decreet van  21 oktober 1997 betreffende het natuurbehoud en het  natuurlijk milieu, is goedgekeurd conform artikel  16octies van het voormelde decreet, van toepassing is,  voldoen aan de verplichting, vermeld in artikel  3.12.3.0.1, § 1 en § 3.

---- historiek ----  ---- historique ----

- gewijzigd door art. 15 van het decreet van 16.12.2022  (B.S., 29.12.2022). Inwerkingtreding: 01.01.2023

- Ingevoegd door art. 77 van het decreet van 23.12.2021  (B.S., 29.12.2021). Inwerkingtreding: 01.01.2022

#### Afdeling 5 – Verminderingen  Section 5 – Réductions

---- historiek ----  ---- historique ----

- afdeling 5 toegevoegd door art. 144 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

In geval van zuivere aankoop van een tot bewoning  aangewend of bestemd onroerend goed waarvan de  authentieke akte uiterlijk op 31 december 2023 wordt  verleden door een natuurlijke persoon om er zijn  hoofdverblijfplaats te vestigen, wordt zijn wettelijk  aandeel in de belastingen die met toepassing van artikel  2.9.4.1.1, artikel 2.9.4.2.11, artikel 2.9.4.2.12, artikel  2.9.4.2.13 of artikel 2.9.4.2.14, verschuldigd waren op de  aankoop van de woning waarvan de authentieke akte  voor 1 januari 2022 werd verleden en die hem voorheen  tot hoofdverblijfplaats heeft gediend of van de  bouwgrond waarop die woning is opgericht, in mindering  gebracht van zijn wettelijk aandeel in de belastingen,  verschuldigd op de nieuwe aankoop, op voorwaarde dat  de authentieke akte van de nieuwe aankoop is verleden  binnen twee jaar na de datum van het verlijden van de  authentieke akte die aanleiding heeft gegeven of geeft tot  een van de volgende handelingen :

1° de heffing van het verkooprecht op de zuivere  wederverkoop van de woning die hem voorheen tot  hoofdverblijfplaats heeft gediend, of de heffing van het  verdeelrecht op de verdeling van die woning waarbij de  natuurlijke persoon al zijn rechten erin heeft afgestaan;

2° de vrijstelling van het verkooprecht met toepassing  van artikel 2.9.6.0.1, eerste lid, 4°, voor de zuivere  wederverkoop van de woning die hem voorheen tot  hoofdverblijfplaats heeft gediend, of de vrijstelling van  het verdeelrecht met toepassing van artikel 2.10.6.0.1,  eerste lid, 1°, voor de verdeling van die woning, waarbij  de natuurlijke persoon al zijn rechten erin heeft  afgestaan.  Als de authentieke akte van vervreemding geen  aanleiding geeft tot een van de voormelde handelingen  omdat de vervreemding onderworpen is aan een niet-  vervulde opschortende voorwaarde, wordt de termijn van  twee jaar gerekend vanaf de datum van de registratie van  de authentieke akte of het geschrift dat aanleiding heeft  gegeven of geeft tot een van de handelingen, vermeld in  1° of 2°.

De registratiebelasting, betaald voor de verkrijging van  een onroerend goed dat niet in het Vlaamse Gewest ligt,  alsook de aanvullende rechten die om om het even welke  reden op een aankoop zijn geheven, zijn van de  vermindering, overeenkomstig de bepalingen van dit  artikel, uitgesloten.

De vermindering overeenkomstig de bepalingen van dit  artikel levert in geen geval grond voor een teruggave op.

Het in mindering te brengen bedrag, verkregen met  toepassing van het eerste of het vierde lid, kan nooit meer  bedragen dan 12.500 euro. Dit bedrag is gekoppeld aan  de schommelingen van het algemene indexcijfer van de  consumptieprijzen van het Rijk. De bedragen worden  jaarlijks op 1 januari aangepast op basis van een  coëfficiënt die verkregen wordt door het gemiddelde van  de maandelijkse indexcijfers van het jaar dat voorafgaat  aan het jaar, te delen door het gemiddelde van de  indexcijfers van het jaar 2017. Het gemiddelde van de  maandelijkse indexcijfers wordt afgerond op het hogere  of lagere honderdste naargelang het cijfer van de  duizendsten al of niet vijf bereikt, en de coëfficiënt wordt  afgerond op het hogere of lagere tienduizendste  naargelang het cijfer van de honderdduizendsten al of  niet vijf bereikt. Na de toepassing van die coëfficiënt  worden de bedragen afgerond op de lagere vijfhonderd  euro. Het toepasbare geïndexeerde maximumbedrag is  het bedrag voor het jaar waarin de authentieke akte van  de nieuwe aankoop wordt verleden. Het maximale in  mindering te brengen bedrag wordt bepaald in  verhouding tot de fractie die de natuurlijke persoon  verkrijgt in het nieuw aangekochte onroerend goed.

---- historiek ----  ---- historique ----

- gewijzigd door art. 78 van het decreet van 23.12.2021  (B.S., 29.12.2021). Van toepassing op overeenkomsten  houdende zuivere aankoop gesloten vanaf 1 januari 2022,  of, in afwijking daarvan, op authentieke akten verleden  vanaf 1 januari 2022, wanneer de overeenkomsten  houdende zuivere aankoop waarop de akten betrekking  hebben, gesloten zijn voor 1 januari 2022

- gewijzigd door art. 22 van het decreet van 21.12.2018  (B.S. 28.12.2018). Tekst is van toepassing op  verkoopovereenkomsten afgesloten vanaf 1 juni 2018

- gewijzigd door art. 9 van het decreet van 18.05.2018  (B.S.: 28.05.2018). Tekst is van toepassing op  verkoopovereenkomsten afgesloten vanaf 1 juni 2018

###### Art. 2.9.5.0.2.  Art. 2.9.5.0.2.

Aan de vermindering, vermeld in artikel 2.9.5.0.1, zijn de  volgende voorwaarden verbonden :

A la réduction mentionnée à l'article 2.9.5.0.1, sont liées  les conditions suivantes :  1° aan de verplichting, vermeld in artikel 3.12.3.0.1, § 1,  is voldaan en de verklaringen, vermeld in artikel  3.12.3.0.1, § 4, tweede of vierde lid, zijn gedaan;

2° de natuurlijke persoon heeft op een ogenblik in de  periode van achttien maanden die voorafgaan aan de  verkoop of verdeling, zijn hoofdverblijfplaats gehad in de  verkochte of verdeelde woning;

3° de natuurlijke persoon verbindt zich ertoe om zijn  hoofdverblijfplaats te vestigen op de plaats van het nieuw  aangekochte goed :

a) als het een woning betreft, binnen twee jaar na een van  de volgende data :

1) de datum van de registratie van de akte of het geschrift  dat tot de heffing van het verkooprecht op de aankoop  aanleiding geeft, als die akte of dat geschrift binnen de  termijn die daarvoor bepaald is, ter registratie wordt  aangeboden;

2) de uiterste datum voor tijdige aanbieding ter  registratie, als de akte die of het geschrift dat tot de  heffing van het verkooprecht op de aankoop aanleiding  geeft, wordt aangeboden na het verstrijken van de termijn  die daarvoor bepaald is;

b) als het een bouwgrond betreft, binnen vijf jaar na  dezelfde datum.

Als een van de voorwaarden, vermeld in het eerste lid,  niet is vervuld, wordt de akte over de nieuwe aankoop die  of het geschrift over de nieuwe aankoop dat aanleiding  geeft tot de heffing van het verkooprecht, geregistreerd  zonder de toepassing van artikel 2.9.5.0.1.

---- historiek ----  ---- historique ----

- toegevoegd door art. 146 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.9.5.0.3.  Art. 2.9.5.0.3.

In geval van onjuistheid van de vermeldingen,  voorgeschreven bij artikel 2.9.5.0.2, eerste lid, 2°, is de  natuurlijke persoon gehouden tot betaling van de  aanvullende rechten.

---- historiek ----  ---- historique ----

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.9.5.0.4.  Art. 2.9.5.0.4.

Voor de toepassing van artikel 2.9.5.0.1 tot en met artikel  2.9.5.0.3 en voor de toepassing van artikel 3.6.0.0.6, § 3,  wordt met een verrichting als vermeld in artikel 2.9.5.0.1,  eerste lid, of in artikel 3.6.0.0.6, § 3, eerste lid,  gelijkgesteld een combinatie van twee van dergelijke  verrichtingen waarbij de voorlaatste aankoop van de  heffing van het verkooprecht is vrijgesteld met  toepassing van artikel 2.9.6.0.1, eerste lid, 4°.

Bij de vermindering of de teruggave wordt, al naargelang  het geval, rekening gehouden met het wettelijk aandeel  van de natuurlijke persoon in de registratiebelasting,  verschuldigd op de aankoop die voorafgaat aan die welke  is gedaan met toepassing van de vrijstelling, vermeld in  artikel 2.9.6.0.1, eerste lid, 4°, en artikel 2.10.6.0.1,  eerste lid, 1°.

Naast de voorwaarden, vermeld in artikel 2.9.5.0.2,  eerste lid, 2° en 3°, of vermeld in artikel 3.6.0.0.6, § 3,  zesde lid, 3°, die in het kader van een gelijkgestelde  verrichting als vermeld in het eerste lid, de tweede  verrichting in de combinatie betreffen, moet de  natuurlijke persoon bovendien voor de eerste verrichting  in de combinatie vermelden :

1° als de eerste verrichting in de combinatie een  verrichting is als vermeld in artikel 2.9.5.0.1, eerste lid :

a) dat hij op een ogenblik in de periode van achttien  maanden voorafgaand aan de verkoop of verdeling ervan  zijn hoofdverblijfplaats heeft gehad in de eerste woning  in de gelijkgestelde verrichting;

b) dat hij zijn hoofdverblijfplaats had gevestigd op de  plaats van de woning, aangekocht met toepassing van de  vrijstelling van het verkooprecht binnen twee jaar na een  van de volgende data:

1) de datum van de registratie van de akte die of het  geschrift dat tot de toepassing van de vrijstelling van de  heffing van het verkooprecht op de aankoop van die  woning aanleiding heeft gegeven, als die akte of dat  geschrift binnen de termijn die daarvoor bepaald is, ter  registratie wordt aangeboden;

2) de uiterste datum voor tijdige aanbieding ter  registratie, als de akte die of het geschrift dat tot de  toepassing van de vrijstelling van de heffing van het  verkooprecht op de aankoop aanleiding heeft gegeven, is  aangeboden na het verstrijken van de termijn die  daarvoor bepaald is;

a) dat hij op een ogenblik in de periode van achttien  maanden voorafgaand aan de aankoop van de woning  met toepassing van de vrijstelling van het verkooprecht  zijn hoofdverblijfplaats heeft gehad in de eerste woning  in de gelijkgestelde verrichting;

b) dat hij zijn hoofdverblijfplaats had gevestigd op de  plaats van de woning, aangekocht met toepassing van de  vrijstelling van het verkooprecht binnen twee jaar na een  van de volgende data:

1) de datum van de registratie van de akte die of het  geschrift dat tot de vrijstelling van de heffing van het  verkooprecht op de aankoop ervan aanleiding heeft  gegeven, als die akte of dat geschrift binnen de termijn  die daarvoor is bepaald, ter registratie is aangeboden;

2) de uiterste datum voor tijdige aanbieding ter  registratie, als de akte die of het geschrift dat tot de  vrijstelling van de heffing van het verkooprecht op de  aankoop ervan aanleiding heeft gegeven, is aangeboden  na het verstrijken van de termijn die daarvoor bepaald is.

---- historiek ----  ---- historique ----

- toegevoegd door art. 148 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.9.5.0.5.  Art. 2.9.5.0.5.

§ 1. Als er voor alle verkrijgers toepassing wordt gemaakt  van het verlaagde tarief, vermeld in artikel 2.9.4.2.11, §  1, eerste lid, of artikel 2.9.4.2.12, § 1, eerste lid, en als de  totale belastbare grondslag van het onroerend goed niet  hoger  is  dan  220.000  euro,  wordt  er  een  rechtenvermindering toegestaan van respectievelijk 2800  euro of 960 euro op het totaal van de op de aankoop  berekende rechten. Als het verschuldigde verkooprecht  lager is dan, naargelang het geval, hetzij 2800 euro, hetzij  960 euro, dan wordt de rechtenvermindering verlaagd tot  het bedrag van dit verkooprecht.

Als er slechts voor sommige verkrijgers toepassing wordt  gemaakt van het verlaagde tarief, vermeld in artikel  2.9.4.2.11, § 1, eerste lid, of artikel 2.9.4.2.12, § 1, eerste  lid, en als de totale belastbare grondslag van het  onroerend goed niet hoger is dan 220.000 euro, wordt de  rechtenvermindering van 2800 euro of 960 euro herleid  tot het breukdeel van deze bedragen dat overeenstemt  met het aandeel van de betrokken verkrijgers in de totale  aankoop. Als het door deze verkrijgers verschuldigde  verkooprecht lager is dan het overeenkomstige breukdeel  van, naargelang het geval, hetzij 2800 euro, hetzij 960  euro, dan wordt de rechtenvermindering verlaagd tot het  bedrag van het wettelijk aandeel van deze verkrijgers in

Als er slechts voor een deel van de verkrijging toepassing  wordt gemaakt van het verlaagd tarief, vermeld in artikel  2.9.4.2.11, § 1, eerste lid, of artikel 2.9.4.2.12, § 1, eerste  lid, en als de totale belastbare grondslag van het  onroerend goed niet hoger is dan 220.000 euro, wordt de  rechtenvermindering van 2800 euro of 960 euro herleid  tot het breukdeel van deze bedragen dat overeenstemt  met het aandeel van de verkrijging waarvoor het  verlaagde tarief, vermeld in artikel 2.9.4.2.11, § 1, eerste  lid, of artikel 2.9.4.2.12, § 1, eerste lid, wordt toegepast.

Voor de onroerende goederen gelegen op het  grondgebied van de kernsteden en de gemeenten van de  Vlaamse Rand rond Brussel zoals bepaald in artikel  1.1.0.0.2,  twaalfde  lid,  8°  en  9°,  wordt  de  rechtenvermindering, vermeld in het eerste lid,  toegestaan als de totale belastbare grondslag van het  onroerend goed niet hoger is dan 240.000 euro.

§ 2. Als er voor alle verkrijgers toepassing wordt gemaakt  van het verlaagde tarief, vermeld in artikel 2.9.4.2.11, §  1, tweede lid, of artikel 2.9.4.2.12, § 1, vijfde lid, en als  de totale belastbare grondslag van het onroerend goed  niet hoger is dan 220.000 euro, wordt er een  rechtenvermindering toegestaan van respectievelijk 5600  euro of 4800 euro op het totaal van de op de aankoop  berekende rechten. Als het verschuldigde verkooprecht  lager is dan, naargelang het geval, hetzij 5600 euro, hetzij  4800 euro, dan wordt de rechtenvermindering verlaagd  tot het bedrag van dit verkooprecht.

Als er slechts voor sommige verkrijgers toepassing wordt  gemaakt van het verlaagde tarief, vermeld in artikel  2.9.4.2.11, § 1, tweede lid, of artikel 2.9.4.2.12, § 1,  vijfde lid, en als de totale belastbare grondslag van het  onroerend goed niet hoger is dan 220.000 euro, wordt de  rechtenvermindering van 5600 euro of 4800 euro herleid  tot het breukdeel van deze bedragen dat overeenstemt  met het aan- deel van de betrokken verkrijgers in de totale  aankoop. Als het door deze verkrijgers verschuldigde  verkooprecht lager is dan het overeenkomstig breukdeel  van, naargelang het geval, hetzij 5600 euro, hetzij 4800  euro, dan wordt de rechtenvermindering verlaagd tot het  bedrag van het wettelijk aandeel van deze verkrijgers in  het totale verschuldigde verkooprecht.

Voor de onroerende goederen gelegen op het  grondgebied van de kernsteden en de gemeenten van de  Vlaamse Rand rond Brussel zoals bepaald in artikel  1.1.0.0.2,  twaalfde  lid,  8°  en  9°,  wordt  de  rechtenvermindering, vermeld in het eerste lid,  toegestaan als de totale belastbare grondslag van het  onroerend goed niet hoger is dan 240.000 euro.

---- historiek ----  ---- historique ----

- vervangen door art. 79 van het decreet van 23.12.2021  (B.S., 29.12.2021). Van toepassing op overeenkomsten  houdende zuivere aankoop gesloten vanaf 1 januari 2022,  of, in afwijking daarvan, op authentieke akten verleden  vanaf 1 januari 2022, wanneer de overeenkomsten  houdende zuivere aankoop waarop de akten betrekking  hebben, gesloten zijn voor 1 januari 2022

- gewijzigd door art. 23 van het decreet van 21.12.2018  (B.S. 28.12.2018). Tekst is van toepassing op  verkoopovereenkomsten afgesloten vanaf 1 juni 2018

- ingevoegd door art. 10 van het decreet van 18.05.2018  (B.S.: 28.05.2018). Tekst is van toepassing op  verkoopovereenkomsten afgesloten vanaf 1 juni 2018

#### Afdeling 6 - Vrijstellingen  Section 6 – Exonérations

---- historiek ----  ---- historique ----

- Afdeling 6 toegevoegd door art. 149 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.9.6.0.1.  Art. 2.9.6.0.1.

Er wordt een vrijstelling van het verkooprecht verleend  voor :

1° de aanwijzing van lastgever, op voorwaarde dat :  1° la déclaration de command, à condition :

a) de mogelijkheid om een lastgever aan te wijzen in de  akte van toewijzing of koop voorbehouden is;

2° de toewijzingen naar aanleiding van rouwkoop van  onroerende goederen, op voorwaarde dat ze geen  aanleiding geven tot de heffing van een hogere  registratiebelasting dan de registratiebelasting die  geheven is op de vorige toewijzing;

3° de overeenkomsten tot overdracht van het  vruchtgebruik op de blote eigenaar, als de evenredige  registratiebelasting, de erfbelasting of een soortgelijk  recht door de blote eigenaar of door een vorige blote  eigenaar, zijn rechtsvoorganger, op de waarde van de  volle eigendom is voldaan;

3° les conventions ayant pour objet la transmission de  l'usufruit au nu-propriétaire, lorsque le l’impôt  d’enregistrement proportionnel ou l'impôt de succession  a été payé par le nu-propriétaire, ou par un précédent nu-  propriétaire dont il tient ses droits, sur la valeur de la  pleine propriété ;  4° andere overdrachten onder bezwarende titel dan die  welke aan de belasting, overeenkomstig artikel 115bis  het federale Wetboek van Registratie-, Hypotheek- en  Griffierechten onderworpen zijn, van gebouwen,  gedeelten van gebouwen en het bijbehorende terrein,  overeenkomstig artikel 1, § 9, van het Wetboek van de  Belasting over de Toegevoegde Waarde, alsook de  vestigingen, overdrachten of wederoverdrachten van de  zakelijke rechten, overeenkomstig artikel 9, tweede lid,  2°, van het Wetboek van de Belasting over de  Toegevoegde Waarde met betrekking tot gebouwen,  gedeelten van gebouwen en het bijhorende terrein,  overeenkomstig artikel 1, § 9, van het Wetboek van de  Belasting over de Toegevoegde Waarde, op voorwaarde  dat de belasting over de toegevoegde waarde opeisbaar is  op de levering van die goederen of de vestiging, de  overdracht of wederoverdracht van die rechten;

5° de contracten van onroerende financieringshuur,  overeenkomstig artikel 44, § 3, 2°, b, van het Wetboek  van de Belasting over de Toegevoegde Waarde;

6° (…);  6° (…) ;

7° (…).  7° (…).

Als aan de voorwaarden, vermeld in het eerste lid, 1°, niet  is voldaan, wordt de aanwijzing van lastgever voor de  toepassing van dit hoofdstuk als een wederverkoop  beschouwd.

In afwijking van hetgeen vermeld is in het eerste lid, 1°,  a) en b), moet om de vrijstelling van het verkooprecht te  genieten :

1° (…)  1° (…)

In de gevallen, vermeld in het derde lid, wordt de  aanwijzing ingeschreven of vermeld onderaan op het  proces-verbaal van toewijzing zonder dat ze aan het  bevoegde personeelslid betekend moet worden.

Als de toewijzingen, vermeld in het eerste lid, 2°, wel  aanleiding geven tot de heffing van een hoger  verkooprecht dan het verkooprecht dat geheven is op de

Si les adjudications mentionnées au premier alinéa, 2°,  donnent bien lieu à un droit de vente supérieur à celui qui  a été perçu sur la précédente adjudication, l'exonération  vorige toewijzing, wordt de vrijstelling beperkt tot het  verkooprecht dat geheven is op de vorige toewijzing.

Het eerste lid, 2°, is ook van toepassing op de  toewijzingen naar aanleiding van prijsverhoging in de  gevallen waarin het voorbehoud van prijsverhoging geen  opschortende voorwaarde uitmaakt.

Om de vrijstelling, vermeld in het eerste lid, 4°, te  verkrijgen, moet voldaan zijn aan de verplichtingen,  vermeld in artikel 3.12.3.0.1, § 1 en § 5, zesde lid.

Als onroerende goederen verkregen worden in andere  omstandigheden dan de omstandigheden, vermeld in het  eerste lid, 7°, is voor de verkrijging, vermeld in het eerste  lid, 7°, hoe ze ook gebeurt, het verkooprecht  verschuldigd.

---- historiek ----  ---- historique ----

- gewijzigd door art. 41 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- gewijzigd door art. 13 van het decreet van 22.06.2018.  Tekst in werking getreden vanaf aanslagjaar 2021

- gewijzigd door art. 24 van het decreet van 21.12.2018  (B.S. 28.12.2018). Inwerkingtreding op 01.05.2019 (art.

3 van het besluit van 05.04.2019 - B.S. 07.05.2019)

- gewijzigd door art. 41 van het decreet van 23.12.2016  (M.B.: 30.12.2016). Tekst in werking getreden op  08.01.2017

- zevende lid vervangen door art. 21 van het decreet van  17 juli 2015 (B.S., 14.08.2015 ). De tekst is in werking  getreden op 14 augustus 2015 (art. 41)

###### Art. 2.9.6.0.2.  Art. 2.9.6.0.2.

Er wordt een vrijstelling van het verkooprecht verleend  voor :

2° de akten in der minne die betrekking hebben op  onroerende goederen die uitsluitend bestemd zijn voor  onderwijs, verleden op naam van of ten voordele van de  inrichtende machten van het gemeenschapsonderwijs of  het gesubsidieerd onderwijs, alsook op naam van of ten  voordele van verenigingen zonder winstoogmerk voor  patrimoniaal beheer die tot uitsluitend doel hebben  onroerende goederen ter beschikking te stellen voor  onderwijs dat door de voormelde inrichtende machten  wordt verstrekt;

3° (...);  3° (…);  4° de akten die in der minne verleden zijn in naam van of  ten  voordele  van  de  naamloze  vennootschap  A.S.T.R.I.D.;

5° (...);  5° (…) ;

6° de akten die verleden zijn in naam van of ten voordele  van de Vlaamse Maatschappij voor Sociaal Wonen;

7° de akten die verleden zijn in naam van of ten voordele  van  de  Nationale  Maatschappij  der  Belgische  Spoorwegen;

8° de akten houdende oprichting, wijziging, verlenging  of ontbinding van:

a) de Vlaamse Maatschappij voor Watervoorziening;  a) la « Vlaamse Maatschappij voor Watervoorziening »  (Société flamande de Distribution d’Eau) ;

b) de verenigingen of intercommunales, vermeld in de  wet  van  22  december  1986  betreffende  de  intercommunales en het decreet van 6 juli 2001 houdende  de intergemeentelijke samenwerking;

c) de Vlaamse Vervoermaatschappij – De Lijn;  c) la « Vlaamse Vervoermaatschappij - De Lijn »  (Société flamande des Transports - De Lijn) ;

d) de Federale Participatie- en Investeringsmaatschappij  en de gewestelijke investeringsmaatschappijen;

9° de akten die, bij toepassing van de organieke wet van  8 juli 1976 betreffende de openbare centra voor  maatschappelijk welzijn , het decreet van 19 december  2008 betreffende de organisatie van de openbare centra  voor maatschappelijk welzijn of deel 3, titel 4, van het  decreet van 22 december 2017 over het lokaal bestuur, de  overgave vaststellen van goederen aan openbare centra  voor maatschappelijk welzijn ofwel de overgave van  goederen aan verenigingen die op grond van de

Het eerste lid, 1° tot en met 7°, is alleen van toepassing  op de akten waarvan de kosten wettelijk ten laste van  vermelde entiteiten vallen.

Om de vrijstelling, vermeld in het eerste lid, te  verkrijgen, moet voldaan zijn aan de verplichtingen,  vermeld in artikel 3.12.3.0.1, § 1, 4°.

---- historiek ----  ---- historique ----

- gewijzigd door art. 42 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- gewijzigd door art. 14 van het decreet van 22.06.2018.  Tekst in werking getreden vanaf aanslagjaar 2019

- gewijzigd door art. 20 van het decreet van 08.12.2017  (B.S.: 14.12.2017). Tekst in werking getreden op  24.12.2017

- gewijzigd door art. 42 van het decreet van 23.12.2016  (B.S.: 30.12.2016). Tekst in werking getreden op 8 januari  2017

- toegevoegd door art. 151 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.9.6.0.3.  Art. 2.9.6.0.3.

Er wordt een vrijstelling van het verkooprecht verleend  voor:

1° de overdrachten in der minne van onroerende  goederen ten algemenen nutte, aan de federale staat, de  gemeenschappen,  de  gewesten,  de  gemeenschapscommissies, de provincies, de gemeenten,  de openbare instellingen en aan alle andere tot  onteigening gerechtigde organen of personen;

2° de akten voor de wederafstand na onteigening ten  algemenen nutte in de gevallen waarin die bij de wet of  het decreet toegelaten is;

3° de akten houdende verkrijging door vreemde staten  van onroerende goederen die bestemd zijn tot vestiging  van hun diplomatieke of consulaire vertegenwoordiging  in België, of voor de woning van het hoofd van de  standplaats;

5° de akten, vonnissen en arresten voor de ruil, de  ruilverkaveling of de herverkaveling, of voor het vestigen  van een erfdienstbaarheid, ter uitvoering van een wet of  een decreet.

De vrijstelling, vermeld in het eerste lid, 3°, is  ondergeschikt aan de voorwaarde dat wederkerigheid aan  de Belgische Staat toegekend wordt.

De vrijstelling, vermeld in het eerste lid, 4°, wordt alleen  verleend als bij de aan de formaliteit van de registratie  onderworpen akte of verklaring over de overeenkomst  een attest is gevoegd waarin wordt bevestigd dat de  overdracht plaatsvindt met het oog op de realisatie van  een brownfieldproject dat het voorwerp uitmaakt of zal  uitmaken van een brownfieldconvenant, en dat de  onroerende goederen waarvoor de vrijstelling wordt  gevraagd, deel uitmaken van dat brownfieldproject. De

L’exonération visée à l’alinéa 1er, 4°, ne sera accordée  qu’à condition de joindre à l’acte ou à la déclaration  concernant la convention, soumis à la formalité  d’enregistrement, une attestation confirmant que la  cession a lieu en vue de la réalisation d’un projet  Brownfield qui fait ou qui fera l’objet d’une convention  Brownfield et que les biens immeubles pour lesquels  l’exonération est demandée font partie de ce projet  Brownfield. Le Gouvernement flamand arrête les  modalités relatives à la forme de cette attestation.  Vlaamse Regering bepaalt de nadere regels voor de  vormgeving van dat attest.

Als de overeenkomst, vermeld in het eerste lid, 4°, ook  andere onroerende goederen omvat dan de onroerende  goederen, vermeld in het eerste lid, en als de overdracht  gedaan wordt voor een gezamenlijke prijs, wordt de  verkoopwaarde  van  elk  van  de  onderscheiden  categorieën van onroerende goederen opgegeven in een  aanvullende verklaring als vermeld in artikel 3.13.1.2.1.

Het verkooprecht is alsnog verschuldigd door de  verkrijger van de onroerende goederen, vermeld in het  eerste lid, 4°, als de Vlaamse Regering beslist tot  stopzetting van de onderhandelingen als vermeld in  artikel 8, § 3, eerste lid, van het decreet van 30 maart  2007 betreffende de Brownfieldconvenanten, of als het  brownfieldproject niet tijdig wordt gestart of gerealiseerd  conform  de  voorwaarden,  vermeld  in  het  brownfieldconvenant. Het verkooprecht wordt opeisbaar  vanaf de kennisgeving aan het bevoegde personeelslid  dat de voorwaarden voor het behoud van de vrijstelling  niet langer vervuld zijn. De Vlaamse Regering bepaalt de  nadere regels voor die kennisgeving.

---- historiek ----  ---- historique ----

- vervangen door art. 15 van het decreet van 22.06.2018.  Tekst in werking getreden vanaf aanslagjaar 2019

- toegevoegd door art. 152 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.9.6.0.4.  Art. 2.9.6.0.4.

Er wordt een vrijstelling van het verkooprecht verleend  voor  de  ruilovereenkomsten  van  onbebouwde  landeigendommen waarvan de oppervlakte van elk van  de kavels niet meer bedraagt dan vijf hectare, op  voorwaarde dat er tussen elk van de kavels geen  waardeverschil of opleg is.

---- historiek ----  ---- historique ----

- gewijzigd door art. 16 van het decreet van 22.06.2018.  Tekst in werking getreden vanaf aanslagjaar 2019

- toegevoegd door art. 153 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.9.6.0.5.  Art. 2.9.6.0.5.  In afwijking van artikel 2.9.1.0.3 wordt een vrijstelling  van het verkooprecht verleend voor :

1°  de  omvorming van  een  vennootschap met  rechtspersoonlijkheid in een vennootschap van een  verschillende soort en de omzetting van een vereniging  zonder winstoogmerk in een coöperatieve vennootschap  erkend als sociale onderneming. Dit punt is ook van  toepassing als de omvorming plaatsvindt via een  vereffening, gevolgd door de oprichting van een nieuwe  vennootschap, als in die oprichting voorzien wordt in de  akte van invereffeningstelling en als ze binnen vijftien  dagen na de akte plaatsvindt;

2° de overbrenging van de zetel van de werkelijke leiding  of van de zetel van een vennootschap, als die  overbrenging gebeurt uit het grondgebied van een staat  van de Europese Economische Ruimte of als het een  overbrenging naar België betreft van de zetel van de  werkelijke leiding van een vennootschap waarvan de  zetel zich al op het grondgebied van de vermelde  gemeenschap bevindt. Dit punt is alleen van toepassing  als het vaststaat dat de vennootschap behoort tot de soort  van vennootschappen die onderworpen zijn aan een  belasting op het bijeenbrengen van kapitaal in het land dat  in aanmerking komt voor het voordeel van de vrijstelling.

3°  de  omvorming  van  een  vennootschap met  rechtspersoonlijkheid  in  een  vereniging  met  rechtspersoonlijkheid. Die afwijking is ook van  toepassing als de omvorming plaatsvindt via een  vereffening, gevolgd door oprichting van een vereniging  met rechtspersoonlijkheid, als in die oprichting voorzien  wordt in de akte van invereffeningstelling en als ze  binnen vijftien dagen na de akte plaatsvindt.

---- historiek ----  ---- historique ----

- gewijzigd door art. 16 van het decreet van 03.04.2026  (B.S. 23.04.2026). Inwerkingtreding op 03.05.2026

- gewijzigd door art. 43 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- gewijzigd door art. 25 van het decreet van 21.12.2018  (B.S. 28.12.2018). Inwerkingtreding op 01.05.2019 (art.

3 van het besluit van 05.04.2019 - B.S. 07.05.2019)

- toegevoegd door art. 154 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.9.6.0.6.  Art. 2.9.6.0.6.

Er wordt een vrijstelling van het verkooprecht verleend  voor vonnissen en arresten houdende vernietiging,  ontbinding of herroeping van een overeenkomst als  vermeld in artikel 2.9.1.0.1, waarbij eigendom of  vruchtgebruik wordt overgedragen van onroerende  goederen die in België liggen.

Als de vernietiging, ontbinding of herroeping, vermeld in  het eerste lid, uitgesproken is ten voordele van een andere  persoon dan een van de partijen bij de overeenkomst,

Si l'annulation, la résolution ou la révocation, visée à  l'alinéa premier, est prononcée en faveur d'une personne  autre qu'une des parties au contrat, ses héritiers ou  haar erfgenamen of legatarissen worden, al naargelang  het geval, de rechten, vermeld in hoofdstuk 8 tot en met  11, geheven die verschuldigd geweest zouden zijn als de  vernietiging, de ontbinding of de herroeping het  voorwerp van een minnelijke akte had uitgemaakt.

---- historiek ----  ---- historique ----

- toegevoegd door art. 155 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

§ 1. De waarde van de onbebouwde onroerende goederen  waarvoor een natuurbeheerplan type vier als vermeld in  artikel 16ter, § 1, 4°, van het decreet van 21 oktober 1997  betreffende het natuurbehoud en het natuurlijk milieu, is  goedgekeurd conform artikel 16octies van het voormelde  decreet, wordt volledig van het verkooprecht vrijgesteld.  De vrijstelling geldt zowel voor de grond- als voor de  opstandswaarde.

§ 2. De vrijstelling, vermeld in paragraaf 1, is ook van  toepassing als nog geen natuurbeheerplan is gesloten, als  het onroerend goed wordt gekocht met het oog op het tot  stand brengen van een natuurbeheerplan type vier als  vermeld in artikel 16ter, § 1, 4°, van het decreet van 21  oktober 1997 betreffende het natuurbehoud en het  natuurlijk milieu.

De vrijstelling, vermeld in het eerste lid, wordt verleend  op voorwaarde dat uiterlijk bij de aanbieding ter  registratie  van  de  authentieke  koopakte  een  overeenkomst is gesloten met het Agentschap voor  Natuur en Bos waaruit de intentie blijkt om een  natuurbeheerplan voor het onroerend goed te laten  goedkeuren.

§ 3. Voor de toepassing van dit artikel moet voldaan zijn  aan de verplichtingen, vermeld in artikel 3.12.3.0.1, § 1  en § 5, negende en tiende lid.

---- historiek ----  ---- historique ----

- gewijzigd door art. 44 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- ingevoegd door art. 17 van het decreet van 22.12.2017  (B.S. 21.02.2018). Tekst treedt in werking op 09.06.2018  (art. 1 besluit 04.05.2018 B.S. 30.05.2018)

#### Afdeling 7 - Wijze van heffing  Section 7 - Mode de perception

---- historiek ----  ---- historique ----

- afdeling 7 toegevoegd door art. 156 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.9.7.0.1.  Art. 2.9.7.0.1.

Het verkooprecht wordt geheven in overeenstemming  met de bepalingen van artikel 3.3.2.0.1, 9°, en artikel  3.3.3.0.1, § 4/2.

---- historiek ----  ---- historique ----

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.9.7.0.2.  Art. 2.9.7.0.2.

Voor ruilovereenkomsten wordt het verkooprecht  gevestigd  op  basis  van  het  bedrag  van  de  overeengekomen waarde van het onroerend goed waarop  de ruilovereenkomst betrekking heeft, dat aanleiding  geeft tot heffing van het hoogste recht.

Bij  ruilovereenkomsten  van  onbebouwde  landeigendommen, waarbij er ongelijkheid van kavels is  en waarbij de oppervlakte van elk van de kavels niet meer  bedraagt dan vijf hectare, wordt in afwijking van het  eerste  lid  het  verkooprecht  geheven  op  het  waardeverschil of de opleg als die opleg groter is dan dat  verschil.

---- historiek ----  ---- historique ----

- gewijzigd door art. 17 van het decreet van 22.06.2018.  Tekst in werking getreden vanaf aanslagjaar 2019

- toegevoegd door art. 158 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.9.7.0.3.  Art. 2.9.7.0.3.

§ 1. De belastingplicht, de belastbare grondslag, het  tarief, de vrijstellingen en de verminderingen worden  bepaald door het ogenblik waarop de rechtshandeling is  gesteld.

In afwijking van het eerste lid worden, als er geen  verplichting tot registratie geldt, de belastingplicht, de  belastbare grondslag en het tarief bepaald door het  ogenblik waarop de akte of het geschrift ter registratie  wordt aangeboden.

§ 2. Op een rechtshandeling die onderworpen is aan een  opschortende voorwaarde, wordt het verkooprecht alleen  geheven als de voorwaarde is vervuld. In voorkomend  geval wordt gehandeld als volgt :

1° het toepasbare tarief waarmee voor de heffing  rekening moet worden gehouden, is het tarief dat van  kracht is op de datum waarop het verkooprecht

verworven geweest zou zijn als de handeling  onvoorwaardelijk was geweest;

2° de belastbare grondslag waarmee voor de heffing  rekening moet worden gehouden, is de belastbare  grondslag op de datum van de vervulling van de  voorwaarde.

---- historiek ----  ---- historique ----

- toegevoegd door art. 159 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.9.7.0.4.  Art. 2.9.7.0.4.

In geval van een handelszaak wordt het verkooprecht  vastgesteld volgens de aard van elk goed dat er deel van  uitmaakt.

---- historiek ----  ---- historique ----

- toegevoegd door art. 160 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.9.7.0.5.  Art. 2.9.7.0.5.

Voor de toepassing van artikel 115bis van het federale  Wetboek van Registratie-, Hypotheek- en Griffierechten  , en titel 2, hoofdstuk 9 van deze Codex moet de  aanwending of de bestemming van een onroerend goed  worden nagegaan per kadastraal perceel of per gedeelte  van kadastraal perceel als dat gedeelte ofwel een  afzonderlijke huisvesting is, ofwel een afdeling van de  productie of van de werkzaamheden die, of een onderdeel  daarvan dat, afzonderlijk kan werken, ofwel een eenheid  die van de andere goederen of delen die het perceel  vormen, kan worden afgezonderd.

---- historiek ----  ---- historique ----

- gewijzigd door art. 11 van het decreet van 18.05.2018  (B.S.: 28.05.2018). Tekst is van toepassing op  verkoopovereenkomsten afgesloten vanaf 1 juni 2018

- toegevoegd door art. 161 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

### Hoofdstuk 10 – Verdeelrecht  Chapitre 10 - Droit de partage.

---- historiek ----  ---- historique ----

- hoofdstuk 10 toegevoegd door art. 162 van het decreet  van 19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

---- historiek ----  ---- historique ----

- afdeling 1 toegevoegd door art. 163 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.10.1.0.1.  Art. 2.10.1.0.1.

Overeenkomstig artikel 1, artikel 19 en artikel 31 van het  federale Wetboek van Registratie-, Hypotheek- en  Griffierechten wordt het verdeelrecht gevestigd naar  aanleiding van de registratie of de verplichting tot  registratie van akten of geschriften die als titel gelden van  een overeenkomst houdende :

1° gedeeltelijke of gehele verdelingen van onroerende  goederen;

2° afstanden onder bezwarende titel, onder mede-  eigenaars, van onverdeelde delen in onroerende  goederen;

3° omzetting als vermeld in artikel 4.61 en 4.62 van het  Burgerlijk Wetboek, zelfs als er geen onverdeeldheid is.

---- historiek ----  ---- historique ----

- gewijzigd door art. 7 van het decreet van 15.03.2024  (B.S. 20.03.2024). Inwerkingtreding: 30.03.2024

- toegevoegd door art. 164 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.10.1.0.2.  Art. 2.10.1.0.2.

§ 1. Vonnissen en arresten die tot bewijs strekken van een  overeenkomst waarop de bepalingen van deze afdeling  van toepassing zijn, maar die nog niet aan het  verdeelrecht onderworpen is, geven aanleiding tot de  heffing van het verdeelrecht.

Dat geldt ook als de rechterlijke beslissing die tot bewijs  van de overeenkomst strekt, de ontbinding of herroeping  ervan uitspreekt of vaststelt voor om het even welke  reden, tenzij uit de beslissing blijkt dat ten hoogste één  jaar na de overeenkomst een eis tot ontbinding of  herroeping, zelfs bij een onbevoegde rechter, is ingesteld.

Dat geldt ook als de scheidsrechterlijke uitspraak of in  het buitenland gewezen rechterlijke beslissing die tot  bewijs van de overeenkomst strekt, de ontbinding of  herroeping ervan uitspreekt of vaststelt voor om het even  welke reden, tenzij uit de beslissing blijkt dat ten hoogste  één jaar na de overeenkomst een eis tot ontbinding of  herroeping, zelfs bij een onbevoegde rechter, is ingesteld.

Het verdeelrecht is ook van toepassing in geval van  aanbieding ter registratie van een in het buitenland  gewezen rechterlijke beslissing die van rechtswege in  België uitvoerbaar is.

---- historiek ----  ---- historique ----

- toegevoegd door art. 165 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.10.1.0.3.  Art. 2.10.1.0.3.

Met behoud van de toepassing van artikel 2.10.1.0.1  wordt, behoudens vestiging van de belasting, vermeld in  hoofdstukken 9 en 11, het verdeelrecht gevestigd op een  inbreng van onroerende goederen als vermeld in artikel  115bis van het federale Wetboek van Registratie-,  Hypotheek- en Griffierechten in een Belgische  vennootschap naarmate die inbreng anders vergoed  wordt dan bij de toekenning van maatschappelijke  rechten.

Als een inbreng als vermeld in het eerste lid meteen  onroerende goederen als vermeld in artikel 115bis van  het federale Wetboek van Registratie-, Hypotheek- en  Griffierechten, en goederen van een andere aard omvat,  worden, niettegenstaande elk strijdig beding, de  maatschappelijke rechten en de andere lasten, die de  vergoeding van de bedoelde inbreng uitmaken, geacht  evenredig verdeeld te zijn tussen de waarde die aan de  onroerende goederen is toegekend en die welke aan de  andere goederen is toegekend, bij de overeenkomst. De  te vervallen huurprijzen van de huurcontracten waarvan

Het eerste en het tweede lid zijn niet van toepassing op  de inbreng van de universaliteit van de goederen of van  een bedrijfstak overeenkomstig artikel 117, § 1 en § 2,  van het federale Wetboek van Registratie-, Hypotheek-  en Griffierechten.

Dit artikel is ook van toepassing op de oprichting van  nieuwe vennootschappen, als vermeld in artikel 118 van  het federale Wetboek van Registratie-, Hypotheek- en  Griffierechten.

---- historiek ----  ---- historique ----

- toegevoegd door art. 166 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.10.1.0.4.  Art. 2.10.1.0.4.

De bepalingen van dit hoofdstuk zijn niet van toepassing  op de uitvoering van een beding van terugval of van  aanwas.

---- historiek ----  ---- historique ----

- toegevoegd door art. 167 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

#### Afdeling 2 – Belastingplichtigen  Section 2 – Contribuables

---- historiek ----  ---- historique ----

- afdeling 2 toegevoegd door art. 168 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.10.2.0.1.  Art. 2.10.2.0.1.

De belastingplichtige is de verkrijger van het zakelijk  recht.

---- historiek ----  ---- historique ----

- toegevoegd door art. 169 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

#### Afdeling 3 - Belastbare grondslag  Section 3 - Base imposable

---- historiek ----  ---- historique ----

- afdeling 3 toegevoegd door art. 170 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

§ 1. Het verdeelrecht wordt vastgesteld op basis van de  overeengekomen waarde van de goederen, zoals ze blijkt  uit de bepalingen van de akte, zonder dat de belastbare  grondslag lager dan de verkoopwaarde mag zijn.

In voorkomend geval wordt de verkoopwaarde van het  vruchtgebruik of van de blote eigendom overeenkomstig  artikel 2.9.3.0.1 tot en met artikel 2.9.3.0.7 vastgesteld.

§ 2. Voor de goederen waarvan de akte de  onverdeeldheid doet ophouden onder al de mede-  eigenaars, wordt de belasting geheven op de waarde van  die goederen.

Voor de goederen waarvan de akte de onverdeeldheid  niet doet ophouden onder al de mede-eigenaars, wordt de  belasting geheven op de waarde van de afgestane delen.

---- historiek ----  ---- historique ----

- toegevoegd door art. 171 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.10.3.0.2.  Art. 2.10.3.0.2.

(…)  (…)

---- historiek ----  ---- historique ----

- opgeheven door art. 21 van het decreet van 08.12.2017  (B.S.: 14.12.2017). Tekst in werking

getreden op 24.12.2017

- zevende lid toegevoegd door art. 22 van het decreet van  17 juli 2015 (B.S., 14.08.2015 ). De tekst is in werking  getreden op 14 augustus 2015 (art. 41)

###### Art. 2.10.3.0.3.  Art. 2.10.3.0.3.

De rechten die verschuldigd zijn op akten waarbij  eigendom of vruchtgebruik van een handelszaak  aangewezen wordt, worden geheven op de bij dit  hoofdstuk vastgestelde belastbare grondslagen.

De schulden die al dan niet met de handelszaak in  verband staan en die door de nieuwe eigenaar of  vruchtgebruiker ten laste genomen worden, worden als  lasten van de overeenkomst beschouwd.

---- historiek ----  ---- historique ----

- toegevoegd door art. 173 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

---- historiek ----  ---- historique ----

- afdeling 4 toegevoegd door art. 174 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.10.4.0.1.  Art. 2.10.4.0.1.

Het verdeelrecht bedraagt 2,5 %.  Le droit de partage s'élève à 2,5 %.

Het recht wordt op 1% gebracht als de verdeling of de  afstand, vermeld in artikel 2.10.1.0.1, 1° of 2° :

1° tussen ex-echtgenoten plaatsvindt na of uitwerking  heeft door de echtscheiding;

2° tussen ex-wettelijke samenwonenden plaatsvindt  binnen een termijn van drie jaar die volgt op de  beëindiging van de wettelijke samenwoning conform  artikel 1476, § 2, van het Burgerlijk Wetboek en op  voorwaarde dat de personen op de dag van deze  beëindiging ten minste een jaar ononderbroken met  elkaar wettelijk samenwoonden.

Het verlaagde tarief, vermeld in het tweede lid, is ook van  toepassing als de verdeling of de afstand wordt gedaan  volgens de wetgeving van een andere lidstaat van de  Europese Economische Ruimte als de verdeling of de  afstand  plaatsvindt  onder  omstandigheden  en  voorwaarden  die  vergelijkbaar  zijn  met  de  omstandigheden en voorwaarden, vermeld in het tweede  lid.

---- historiek ----  ---- historique ----

- tweede lid werd vervangen door art. 95 van het decreet  van 18 dec. 2015 (B.S., 29.12.2015). De tekst is in  werking getreden op 1 januari 2016 (art. 135)

###### Art. 2.10.4.0.2.  Art. 2.10.4.0.2.

Als een akte of geschrift, overeengekomen tussen  dezelfde partijen, verschillende van elkaar afhankelijke  of noodzakelijk uit elkaar voortvloeiende regelingen  bevat waaronder een rechtshandeling als vermeld in  artikel 2.10.1.0.1, die onderworpen is aan het  verdeelrecht, wordt de belasting geheven die van  toepassing is op de regeling die aanleiding geeft tot de  heffing van de hoogste belasting, vastgesteld met  toepassing van hoofdstuk 8 tot en met hoofdstuk 11.

---- historiek ----  ---- historique ----

- toegevoegd door art. 176 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

#### Afdeling 5 – Verminderingen  Section 5 – Réductions

---- historiek ----  ---- historique ----

- afdeling 5 toegevoegd door art. 177 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.10.5.0.1.  Art. 2.10.5.0.1.

Voorbehouden voor toekomstig gebruik  Réservé pour utilisation future.

---- historiek ----  ---- historique ----

- toegevoegd door art. 178 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

#### Afdeling 6 - Vrijstellingen  Section 6 – Exonérations

---- historiek ----  ---- historique ----

- afdeling 6 toegevoegd door art. 179 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.10.6.0.1.  Art. 2.10.6.0.1.

Er wordt een vrijstelling van het verdeelrecht verleend  voor :

1° de overeenkomsten tot overdracht van het  vruchtgebruik op de blote eigenaar, als de evenredige  registratiebelasting, de erfbelasting of een soortgelijk  recht door de blote eigenaar of door een vorige blote  eigenaar, zijn rechtsvoorganger, op de waarde van de  volle eigendom is voldaan;

2° de overeenkomsten, vermeld in artikel 2.10.1.0.1,  andere dan die welke aan de belasting, overeenkomstig  artikel 115bis van het federale Wetboek van Registratie-  , Hypotheek- en Griffierechten onderworpen zijn, van

3° de akten die met toepassing van de organieke wet van  8 juli 1976 betreffende de openbare centra voor  maatschappelijk welzijn , het decreet van 19 december  2008 betreffende de organisatie van de openbare centra  voor maatschappelijk welzijn of deel 3, titel 4, van het  decreet van 22 december 2017 over het lokaal bestuur,  verrichtingen vaststellen als vermeld in artikel 2.10.1.0.1,  hetzij ten bate van openbare centra voor maatschappelijk  welzijn hetzij ten bate van verenigingen die op grond van  de voormelde wet of de voormelde decreten zijn  opgericht, alsook akten houdende verrichtingen als  vermeld in artikel 2.10.1.0.1, na ontbinding of splitsing  van een voormelde vereniging.

Om de vrijstelling, vermeld in het eerste lid, 2°, te  verkrijgen, moet voldaan zijn aan de verplichtingen,  vermeld in artikel 3.12.3.0.1, § 1 en § 5, zesde lid.

---- historiek ----  ---- historique ----

- gewijzigd door art. 45 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- gewijzigd door art. 44 van het decreet van 23.12.2016  (B.S.: 30.12.2016). Tekst in werking getreden op 8 januari  2017

- toegevoegd door art. 180 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.10.6.0.2.  Art. 2.10.6.0.2.

(…)  (…)

---- historiek ----  ---- historique ----

- opgeheven door art. 18 van het decreet van 22.06.2018.  Tekst in werking getreden vanaf aanslagjaar 2019

- toegevoegd door art. 181 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

Er wordt een vrijstelling van het verdeelrecht verleend  voor de overeenkomsten tot overdracht van onroerende

Une exemption du droit de partage est accordée pour les  conventions de cession de biens immeubles, telles que

De vrijstelling, vermeld in het eerste lid, wordt alleen  verleend als bij de aan de formaliteit van de registratie  onderworpen akte  of verklaring betreffende de  overeenkomst een attest is gevoegd waarin wordt  bevestigd dat de overdracht plaatsvindt met het oog op de  realisatie van een brownfieldproject dat het voorwerp  uitmaakt of zal uitmaken van een brownfieldconvenant,  en dat de onroerende goederen waarvoor de vrijstelling  wordt  gevraagd,  deel  uitmaken  van  dat  brownfieldproject. De Vlaamse Regering bepaalt de  nadere regels voor de vormgeving van dat attest.

Als de overeenkomst, vermeld in het eerste lid, ook  andere onroerende goederen omvat dan de onroerende  goederen, vermeld in het eerste lid, en de overdracht  gebeurt voor een gezamenlijke prijs, moet de  verkoopwaarde  van  elk  van  de  onderscheiden  categorieën van onroerende goederen worden opgegeven  in een aanvullende verklaring als vermeld in artikel  3.13.1.2.1.

Het verdeelrecht is alsnog verschuldigd door de  verkrijger van de onroerende goederen, vermeld in het  eerste lid, als de Vlaamse Regering beslist tot stopzetting  van de onderhandelingen als vermeld in artikel 8, § 3,  vierde lid, van het decreet van 30 maart 2007 betreffende  de Brownfieldconvenanten, of als het brownfieldproject  niet tijdig wordt gestart of gerealiseerd conform de  voorwaarden, vermeld in het brownfieldconvenant. Het  verdeelrecht wordt opeisbaar vanaf de kennisgeving aan  het bevoegde personeelslid van het niet langer vervuld  zijn van de voorwaarden voor het behoud van de  vrijstelling. De Vlaamse Regering bepaalt de nadere  regels voor die kennisgeving.

---- historiek ----  ---- historique ----

- gewijzigd door art. 45 van het decreet van 23.12.2016  (B.S.: 30.12.2016). Tekst in werking getreden op 8 januari  2017

- toegevoegd door art. 182 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.10.6.0.4.  Art. 2.10.6.0.4.

Er wordt een vrijstelling van het verdeelrecht verleend  voor vonnissen en arresten houdende vernietiging,  ontbinding of herroeping van een overeenkomst als  vermeld in artikel 2.10.1.0.1, waarbij eigendom of

Als de vernietiging, ontbinding of herroeping, vermeld in  het eerste lid, uitgesproken is ten voordele van een andere  persoon dan een van de partijen bij de overeenkomst,  haar erfgenamen of legatarissen, worden al naargelang  het geval de belastingen, vermeld in hoofdstukken 8 tot  en met 11, geheven die verschuldigd geweest zouden zijn  als de vernietiging, de ontbinding of de herroeping het  voorwerp van een minnelijke akte had uitgemaakt.

---- historiek ----  ---- historique ----

- toegevoegd door art. 183 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

#### Afdeling 7 - Wijze van heffing  Section 7 - Modalité de perception

---- historiek ----  ---- historique ----

- afdeling 7 toegevoegd door art. 184 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.10.7.0.1.  Art. 2.10.7.0.1.

Het verdeelrecht wordt geheven in overeenstemming met  de bepalingen van artikel 3.3.2.0.1, 9°, en artikel  3.3.3.0.1, § 4/2.

---- historiek ----  ---- historique ----

- toegevoegd door art. 185 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.10.7.0.2.  Art. 2.10.7.0.2.

§ 1. De belastingplicht, de belastbare grondslag, het  tarief, de vrijstellingen en de verminderingen worden  bepaald door het ogenblik waarop de rechtshandeling is  gesteld.

In afwijking van het eerste lid worden, als er geen  verplichting tot registratie geldt, de belastingplicht, de  belastbare grondslag en het tarief bepaald door het  ogenblik waarop de akte of het geschrift ter registratie  wordt aangeboden.

§ 2. Op een rechtshandeling die onderworpen is aan een  opschortende voorwaarde, wordt het verdeelrecht alleen  geheven als de voorwaarde is vervuld. In voorkomend  geval wordt gehandeld als volgt :

2° de belastbare grondslag waarmee voor de heffing  rekening moet worden gehouden, is de belastbare  grondslag op de datum van de vervulling van de  voorwaarde.

De rechtshandeling die door een rechtspersoon verricht  wordt en die aan machtiging, goedkeuring of  bekrachtiging van een overheid onderworpen is, wordt  voor de toepassing van het eerste lid gelijkgesteld met  een aan een opschortende voorwaarde onderworpen  rechtshandeling.

---- historiek ----  ---- historique ----

- toegevoegd door art. 186 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.10.7.0.3.  Art. 2.10.7.0.3.

In geval van een handelszaak wordt het verdeelrecht  vastgesteld volgens de aard van elk goed dat er deel van  uitmaakt.

---- historiek ----  ---- historique ----

- toegevoegd door art. 187 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

### Hoofdstuk 11 - Recht op hypotheekvestiging  Chapitre 11 - droit sur la constitution d'hypothèque

---- historiek ----  ---- historique ----

- hoofdstuk 11 toegevoegd door art. 188 van het decreet  van 19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

#### Afdeling 1 - Belastbaar voorwerp  Section 1re - Objet imposable

---- historiek ----  ---- historique ----

- afdeling 1 toegevoegd door art. 189 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.11.1.0.1.  Art. 2.11.1.0.1.

Overeenkomstig artikel 1, artikel 19 en artikel 31 van het  federale Wetboek van Registratie-, Hypotheek- en  Griffierechten wordt het recht op hypotheekvestiging

---- historiek ----  ---- historique ----

- toegevoegd door art. 190 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.11.1.0.2.  Art. 2.11.1.0.2.

Met behoud van de toepassing van artikel 2.11.1.0.1  wordt, behoudens vestiging van de belasting, vermeld in  hoofdstukken 9 en 10, het recht op hypotheekvestiging  gevestigd op een inbreng van onroerende goederen als  vermeld in artikel 115bis van het federale Wetboek van  Registratie-, Hypotheek- en Griffierechten in een  Belgische vennootschap als die inbreng anders vergoed  wordt dan bij de toekenning van maatschappelijke  rechten en als die inbreng aanleiding geeft tot de nieuwe  inschrijving.

Als een inbreng als vermeld in het eerste lid meteen  onroerende goederen als vermeld in artikel 115bis van  het federale Wetboek van Registratie-, Hypotheek- en  Griffierechten, en goederen van een andere aard omvat,  worden, niettegenstaande elk strijdig beding, de  maatschappelijke rechten en de andere lasten die de  vergoeding van de vermelde inbreng uitmaken, geacht  evenredig verdeeld te zijn tussen de waarde die aan de  onroerende goederen is toegekend, en die welke aan de  andere goederen is toegekend, bij de overeenkomst. De  te vervallen huurprijzen van de huurcontracten waarvan  de rechten worden ingebracht, worden evenwel geacht  alleen op de laatstvermelde rechten betrekking te hebben.

Het eerste en het tweede lid zijn niet van toepassing op  de inbreng van de universaliteit van de goederen of van  een bedrijfstak overeenkomstig artikel 117, § 1 en § 2,  van het federale Wetboek van Registratie-, Hypotheek-  en Griffierechten.

Dit artikel is ook van toepassing op de oprichting van  nieuwe vennootschappen, als vermeld in artikel 118 van  het federale Wetboek van Registratie-, Hypotheek- en  Griffierechten.

---- historiek ----  ---- historique ----

- toegevoegd door art. 191 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

#### Afdeling 2 – Belastingplichtigen  Section 2 – Redevables

- afdeling 2 toegevoegd door art. 192 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.11.2.0.1.  Art. 2.11.2.0.1.

De belastingplichtige is de hypotheeksteller.  Le redevable est l'affectant hypothécaire.

---- historiek ----  ---- historique ----

- toegevoegd door art. 193 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

#### Afdeling 3 - Belastbare grondslag  Section 3 - Base imposable

---- historiek ----  ---- historique ----

- afdeling 3 toegevoegd door art. 194 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.11.3.0.1.  Art. 2.11.3.0.1.

Het recht op hypotheekvestiging wordt vastgesteld op  basis van het bedrag van de sommen die door de  hypotheek gewaarborgd zijn, met uitsluiting van de  interesten of rentetermijnen van drie jaar, die  gewaarborgd zijn door artikel 87 van de Hypotheekwet  van 16 december 1851.

---- historiek ----  ---- historique ----

- toegevoegd door art. 195 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

#### Afdeling 4 - Tarieven  Section 4 – Tarifs

---- historiek ----  ---- historique ----

- afdeling 4 toegevoegd door art. 196 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.11.4.0.1.  Art. 2.11.4.0.1.

Het recht op hypotheekvestiging bedraagt 1 %.  Le droit sur la constitution d'hypothèque s'élève à 1 %.

---- historiek ----  ---- historique ----

- toegevoegd door art. 197 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

De belasting, vermeld in artikel 2.11.4.0.1, is van  toepassing, zelfs als de hypotheek gevestigd is tot  zekerheid van een toekomstige schuld, van een  voorwaardelijke of eventuele schuld of van een  verbintenis om iets te doen.

---- historiek ----  ---- historique ----

- toegevoegd door art. 198 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.11.4.0.3.  Art. 2.11.4.0.3.

De vestiging van een hypotheek op een onroerend goed  tot zekerheid van een schuld die gewaarborgd is door een  hypotheek op een schip dat niet naar zijn aard voor het  zeevervoer bestemd is, door de verpanding van een  handelszaak of door een landbouwvoorrecht, die aan het  recht, vermeld in artikel 88 van het federale Wetboek van  Registratie-,  Hypotheek-  en  Griffierechten,  zijn  onderworpen, wordt onderworpen aan een verlaagd tarief  van 0,50 %.

---- historiek ----  ---- historique ----

- gewijzigd door art. 26 van het decreet van 21.12.2018  (B.S. 28.12.2018). Tekst treedt in werking op 07.01.2019

- toegevoegd door art. 199 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.11.4.0.4.  Art. 2.11.4.0.4.

Als een akte, overeengekomen tussen dezelfde partijen,  verschillende van elkaar afhankelijke of noodzakelijk uit  elkaar voortvloeiende regelingen bevat waaronder een  vestiging van een hypotheek op een onroerend goed dat  onderworpen is aan het recht op hypotheekvestiging,  wordt de belasting geheven die van toepassing is op de  regeling die aanleiding geeft tot de heffing van de  hoogste belasting, vastgesteld met toepassing van  hoofdstuk 8 tot en met hoofdstuk 11.

Als een akte, overeengekomen tussen dezelfde partijen,  verschillende van elkaar onafhankelijke of niet  noodzakelijk uit elkaar voortvloeiende regelingen bevat  waaronder een vestiging van een hypotheek op een  onroerend goed dat onderworpen is aan het recht op  hypotheekvestiging, wordt op elke regeling al naargelang  het geval de belasting, vermeld in hoofdstuk 8 tot en met  11, geheven.

---- historiek ----  ---- historique ----

werking getreden op 1 januari 2015 (art. 325)

#### Afdeling 5 - Verminderingen  Section 5 – Réductions

---- historiek ----  ---- historique ----

- afdeling 5 toegevoegd door art. 201 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.11.5.0.1.  Art. 2.11.5.0.1.

Voorbehouden voor toekomstig gebruik.  Réservé pour une utilisation ultérieure.

---- historiek ----  ---- historique ----

- toegevoegd door art. 202 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

#### Afdeling 6 - Vrijstellingen  Section 6 - Exemptions

---- historiek ----  ---- historique ----

- afdeling 6 toegevoegd door art. 203 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.11.6.0.1.  Art. 2.11.6.0.1.

Er  wordt  een  vrijstelling  van  het  recht  op  hypotheekvestiging verleend voor elke vestiging van een  hypotheek die na de heffing van de belasting, vermeld in  artikel 2.11.3.0.1 of in artikel 87 van het federale  Wetboek van Registratie-, Hypotheek- en Griffierechten,  wordt  toegestaan  tot  zekerheid  van  dezelfde  schuldvordering voor hetzelfde gewaarborgde bedrag.

---- historiek ----  ---- historique ----

- gewijzigd door art. 27 van het decreet van 21.12.2018  (B.S. 28.12.2018). Tekst treedt in werking op 07.01.2019

- toegevoegd door art. 204 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.11.6.0.2.  Art. 2.11.6.0.2.

Er  wordt  een  vrijstelling  van  het  recht  op  hypotheekvestiging verleend voor de gewaarborgde  verbintenis die voortvloeit uit een overeenkomst waarop  een registratiebelasting van minstens 1% is geheven.

- toegevoegd door art. 205 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.11.6.0.3.  Art. 2.11.6.0.3.

Er wordt een vrijstelling van het recht op  hypotheekvestiging verleend voor de akten in der minne  die betrekking hebben op onroerende goederen die  uitsluitend bestemd zijn voor onderwijs, en die verleden  zijn op naam van of ten voordele van de inrichtende  machten van het gemeenschapsonderwijs of het  gesubsidieerd onderwijs, of op naam van of ten  voordele van verenigingen zonder winstoogmerk voor  patrimoniaal beheer die uitsluitend tot doel hebben  onroerende goederen ter beschikking te stellen voor  onderwijs dat door de voormelde inrichtende machten  wordt verstrekt.

---- historiek ----  ---- historique ----

- ingevoegd door art. 46 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

#### Afdeling 7 - Wijze van heffing  Section 7 - Modalité de perception

---- historiek ----  ---- historique ----

- afdeling 7 toegevoegd door art. 206 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.11.7.0.1.  Art. 2.11.7.0.1.

Het recht op hypotheekvestiging wordt geheven in  overeenstemming met de bepalingen van artikel  3.3.2.0.1, 9°, en artikel 3.3.3.0.1, § 4/2.

---- historiek ----  ---- historique ----

- toegevoegd door art. 207 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.11.7.0.2.  Art. 2.11.7.0.2.

§ 1. De belastingplicht, de belastbare grondslag, het  tarief, de vrijstellingen en de verminderingen worden  bepaald door het ogenblik waarop de rechtshandeling is  gesteld.

In afwijking van het eerste lid worden, als er geen  verplichting tot registratie geldt, de belastingplicht, de  belastbare grondslag en het tarief bepaald door het  ogenblik waarop de akte of het geschrift ter registratie  wordt aangeboden.

1° het toepasbare tarief waarmee voor de heffing  rekening moet worden gehouden, is het tarief dat van  kracht is op de datum waarop het recht op  hypotheekvestiging verworven geweest zou zijn als de  handeling onvoorwaardelijk was geweest;

2° de belastbare grondslag waarmee voor de heffing  rekening moet worden gehouden, is de belastbare  grondslag op de datum van de vervulling van de  voorwaarde.

De rechtshandeling die door een rechtspersoon verricht  is en die aan machtiging, goedkeuring of bekrachtiging  van een overheid onderworpen is, wordt voor de  toepassing van het eerste lid gelijkgesteld met een aan  een  opschortende  voorwaarde  onderworpen  rechtshandeling.

---- historiek ----  ---- historique ----

- toegevoegd door art. 208 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 2.11.7.0.3.  Art. 2.11.7.0.3.

In geval van een handelszaak wordt het recht van  hypotheekvestiging vastgesteld volgens de aard van elk  goed dat er deel van uitmaakt.

---- historiek ----  ---- historique ----

- toegevoegd door art. 209 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

### Hoofdstuk 12 - Belasting op de spelen en

weddenschappen

#### Afdeling 1 - Belastbaar voorwerp  Section 1re - Objet imposable

###### Art. 2.12.1.0.1.  Art. 2.12.1.0.1.

Overeenkomstig artikel 3, eerste lid, 1°, van de  bijzondere wet van 16 januari 1989 betreffende de  financiering van de gemeenschappen en de gewesten  wordt er een belasting geheven op de spelen en  weddenschappen.

---- historiek ----  ---- historique ----

#### Afdeling 2 - Belastingplichtigen  Section 2 – Contribuables

###### Art. 2.12.2.0.1.  Art. 2.12.2.0.1.

De belastingplichtige is degene die, zelfs toevallig, enige  inzet of enig inleggeld aanneemt in het kader van spelen  en weddenschappen, hetzij voor eigen rekening, hetzij als  tussenpersoon.

In afwijking van het eerste lid zijn de belastingplichtigen  diegenen die het lokaal of het materieel ter beschikking  stellen van personen die aan spelen of weddenschappen  doen als er, in private kringen of in andere lokalen of via

Par dérogation à l’alinéa premier, les contribuables sont  ceux qui mettent la salle ou le matériel à la disposition  de personnes engagées dans des jeux ou des paris  lorsque, dans des cercles privés ou dans d’autres salles  informatiemaatschappij-instrumenten als vermeld in  artikel 2, 10°, van de Kansspelwet van 7 mei 1999, aan  spelen of aan weddenschappen wordt gedaan op een  wijze dat niemand in het bijzonder belast is om inzetten  of inleggelden aan te nemen, hetzij voor eigen rekening,  hetzij als tussenpersoon.

---- historiek ----  ---- historique ----

- ingevoegd door art. 7 van het decreet van 07.12.2018  (B.S. 20.12.2018). Tekst in werking getreden op  01.01.2019

#### Afdeling 3 - Belastbare grondslag  Section 3 - Base imposable

###### Art. 2.12.3.0.1.  Art. 2.12.3.0.1.

§ 1. De belasting op de spelen en weddenschappen wordt  geheven op de opbrengst van de spelen en de  weddenschappen, met inbegrip van deze die ingezet  worden via informatiemaatschappij-instrumenten als  vermeld in artikel 2, 10°, van de Kansspelwet van 7 mei  1999.

In het eerste lid wordt verstaan onder opbrengst: het  bedrag van de sommen of inleggelden die worden ingezet  bij de spelen en weddenschappen in kwestie, verminderd  met de winsten die voor die spelen en weddenschappen  werkelijk verdeeld zijn. Dat geldt ook voor sommen of  inleggelden die worden ingezet in private kringen.

De opbrengst, vermeld in het derde lid, wordt dagelijks  vastgesteld. Het eventuele verlies dat voor een dag wordt  vastgesteld, wordt in mindering gebracht van de  opbrengst van de volgende dagen.

Voor de toepassing van het eerste lid worden de sommen  of inleggelden geacht ingezet te zijn in het Vlaamse  Gewest als de spelen of weddenschappen worden  ontvangen via een server die in het Vlaamse Gewest  gevestigd is of uitgebaat wordt.

§ 2. In afwijking van paragraaf 1, eerste lid, wordt de  belasting geheven op:

§ 2. Par dérogation au paragraphe 1er, alinéa premier, la  taxe est levée sur :  1° het bedrag van de sommen of inleggelden die ingezet  worden bij spelen of weddenschappen in geval van  mediaspelen als vermeld in artikel 1.1.0.0.2, veertiende  lid, van deze codex, met uitzondering van mediaspelen  via informatiemaatschappij-instrumenten als vermeld in  artikel 2, eerste lid, 10°, van de Kansspelwet van 7 mei  1999.;

2° het vermoedelijke bedrag van de sommen of  inleggelden  die  ingezet  worden  bij  spelen  of  weddenschappen in het geval van een ambtshalve  aanslag als vermeld in artikel 2.12.7.0.1.

---- historiek ----  ---- historique ----

- gewijzigd door art. 17 van het decreet van 03.04.2026  (B.S. 23.04.2026). Inwerkingtreding op 03.05.2026

- ingevoegd door art. 9 van het decreet van 07.12.2018  (B.S. 20.12.2018). Tekst in werking getreden op  01.01.2019

#### Afdeling 4 - Tarieven  Section 4 – Tarifs

###### Art. 2.12.4.0.1.  Art. 2.12.4.0.1.

§ 1. Het tarief van de belasting bedraagt 15%.  § 1er. Le taux la taxe est de 15%.

§ 2. In afwijking van paragraaf 1 bedraagt het tarief:  § 2. Par dérogation au paragraphe 1er, le tarif :

2° est égal au pourcentage dans le tableau suivant, qui  correspond à la tranche du gain dans le cas de jeux de  casino :

2° het percentage in de volgende tabel dat overeenstemt  met de schijf van de opbrengst als het gaat om  casinospelen:

A. schijf in euro

/  A. tranche en euros

Vanaf

/  à partir de

0,01  865.000  33  865.000,01  44  285.450

3° est égal au pourcentage dans le tableau suivant qui  correspond à la tranche du gain pour les appareils  automatiques de divertissement assimilés aux jeux de  casino, visés à l’article 2.13.6.0.1, 2° :

3° het percentage in de volgende tabel dat overeenstemt  met de schijf van de opbrengst voor de met casinospelen  gelijkgestelde automatische ontspanningstoestellen,  vermeld in artikel 2.13.6.0.1, 2°:

A. schijf in euro  tarief toepasselijk op het

/  A. tranche en euros

vanaf  tot en met

0,01  1.200.000  20  1.200.000,01  2.450.000  25  240.000  2.450.000,01  3.700.000  30  552.500  3.700.000,01  6.150.000  35  927.500  6.150.000,01  8.650.000  40  1.785.000  8.650.000,01  12.350.000  45  2.785.000  12.350.001,01  50  4.450.000

De schijven, vermeld in het eerste lid, 2° en 3°, worden  toegepast op de opbrengst voor het kalenderjaar.

---- historiek ----  ---- historique ----

getreden op 01.01.2019

###### Art. 2.12.4.0.2.  Art. 2.12.4.0.2.

De provincies en de gemeenten zijn niet gemachtigd tot  het heffen van opcentiemen op de belasting op de spelen  en de weddenschappen, vermeld in artikel 2.12.1.0.1, of  van welke belasting dan ook op de spelen en  weddenschappen die onderhevig zijn aan de belasting,  vermeld in dit hoofdstuk.

In afwijking van het eerste lid kunnen de provincies en  de gemeenten een belasting heffen op de agentschappen  voor weddenschappen op paardenwedrennen. De  provinciale en gemeentelijke belasting mag per  agentschap niet hoger zijn dan respectievelijk 37,5 en 62  euro per maand bedrijvigheid of per gedeelte daarvan.

---- historiek ----  ---- historique ----

- ingevoegd door art. 12 van het decreet van 07.12.2018  (B.S. 20.12.2018). Tekst in werking

getreden op 01.01.2019

#### Afdeling 5 - Verminderingen  Section 5 – Réductions

###### Art. 2.12.5.0.1.  Art. 2.12.5.0.1.

Voorbehouden voor toekomstig gebruik  Réservées à un usage futur.

---- historiek ----  ---- historique ----

- ingevoegd door art. 14 van het decreet van 07.12.2018  (B.S. 20.12.2018). Tekst in werking

getreden op 01.01.2019

#### Afdeling 6 - Vrijstellingen  Section 6 – Exonérations

###### Art. 2.12.6.0.1.  Art. 2.12.6.0.1.

Er wordt een vrijstelling van de belasting verleend voor:  Une exonération de la taxe est accordée pour :

1° de toegelaten loterijen;  1° les loteries autorisées ;

2°  de  volksvermakelijkheden,  waarbij  alleen  inschrijvings- of deelnemingsrechten worden geheven,  die verdeeld worden in de vorm van prijzen waarvan de  waarde niet meer bedraagt dan het tienvoudige van de  inzet per deelnemer of die besteed worden aan de  normale organisatiekosten, als het totale bedrag van die  rechten per dag en per persoon niet meer bedraagt dan  50 euro;

3° de duivenprijskampen waarbij uitsluitend ingezet  wordt door de eigenaars van de ingeschreven duiven;

5° de wedstrijden die uitsluitend worden georganiseerd  voor musea of voor de instellingen, vermeld in artikel  14533, § 1, 1° en 2°, van het Wetboek van de  Inkomstenbelastingen 1992;

6° de sportbeoefening.  6° la pratique des sports.

De vrijstellingen, vermeld in het eerste lid, 2° tot en met  6°, zijn niet van toepassing op sommen of inleggelden  ingezet voor de betrokken spelen of weddenschappen  via informatiemaatschappij-instrumenten als vermeld in  artikel 2, 10°, van de Kansspelwet van 7 mei 1999.

---- historiek ----  ---- historique ----

- ingevoegd door art. 16 van het decreet van 07.12.2018  (B.S. 20.12.2018). Tekst in werking

getreden op 01.01.2019

#### Afdeling 7 - Wijze van heffing  Section 7 - Modalités de perception

###### Art. 2.12.7.0.1.  Art. 2.12.7.0.1.

De belasting op de spelen en weddenschappen wordt  gevestigd op zicht van de aangifte, vermeld in artikel  3.3.1.0.15, of ambtshalve als de aangifte niet is  ingediend binnen de termijn, vermeld in artikel  3.3.1.0.15, of bij onjuistheid of onvolledigheid van de

La taxe sur les jeux et paris est établie sur la vue de la  déclaration visée à l’article 3.3.1.0.15 ou d’office si la  déclaration n’a pas été introduite endéans le délai visé à  l’article 3.3.1.0.15, ou en cas d’inexactitude ou de  incomplétude de la déclaration et conformément à  aangifte, en conform artikel 3.3.2.0.1, eerste lid, 11°, en  tweede lid, 7°, en artikel 3.3.3.0.1, § 2.

---- historiek ----  ---- historique ----

- ingevoegd door art. 18 van het decreet van 07.12.2018  (B.S. 20.12.2018). Tekst in werking

getreden op 01.01.2019

ontspanningstoestellen

#### Afdeling 1 - Belastbaar voorwerp  Section 1ère - Objet imposable

###### Art. 2.13.1.0.1.  Art. 2.13.1.0.1.

Overeenkomstig artikel 3, eerste lid, 2°, van de  bijzondere wet van 16 januari 1989 betreffende de  financiering van de gemeenschappen en de gewesten en  artikel 76 van het federaleWetboek van 23 november  1965 van de met Inkomstenbelastingen Gelijkgestelde  Belastingen wordt een belasting geheven op de  automatische ontspanningstoestellen, die opgesteld  worden op de openbare weg, in de voor het publiek  toegankelijke plaatsen of in private kringen, ongeacht of  de toegang tot die kringen al dan niet onderworpen is aan  bepaalde formaliteiten.

---- historiek ----  ---- historique ----

- ingevoegd door art. 21 van het decreet van 07.12.2018  (B.S. 20.12.2018). Tekst in werking

getreden op 01.01.2019

#### Afdeling 2 - Belastingplichtigen  Section 2 - Contribuables

###### Art. 2.13.2.0.1.  Art. 2.13.2.0.1.

De  belastingplichtige  is  de  eigenaar  van  het  automatische ontspanningstoestel.

---- historiek ----  ---- historique ----

- ingevoegd door art. 23 van het decreet van 07.12.2018  (B.S. 20.12.2018). Tekst in werking

getreden op 01.01.2019

#### Afdeling 3 - Belastbare grondslag  Section 3 - Base imposable

###### Art. 2.13.3.0.1.  Art. 2.13.3.0.1.

§ 1. De automatische ontspanningstoestellen zijn  volgens hun type ingedeeld in vier categorieën,  respectievelijk aangeduid door de cijfers 1, 2, 3 en 4.

§ 2. De volgende automatische ontspanningstoestellen  behoren respectievelijk tot de volgende categorieën:

1° categorie 1: de automatische ontspanningstoestellen  die kansspelen zijn als vermeld in artikel 2, eerste lid, 1°,  van de Kansspelwet van 7 mei 1999, met uitzondering  van de toestellen die behoren tot de categorie 2, vermeld  in punt 2° ;

3° categorie 3: de automatische ontspanningstoestellen,  met uitzondering van de toestellen die behoren tot de  categorie 1 of 2, vermeld in punt 1° en 2°, die het  toelaten, zelfs toevallig of bijkomstig, een prijs te  winnen in geld, in natura, in de vorm van penningen of  premiebons;

4° categorie 4: de automatische ontspanningstoestellen  die niet behoren tot de categorieën 1 tot en met 3,  vermeld in punt 1° tot en met 3°.

Wanneer  technische,  economische  of  sociale  omstandigheden het vereisen, kan de categorie waarin  een type toestel moet worden gerangschikt, vastgesteld  of gewijzigd worden door de Vlaamse Regering, na  raadpleging van de betrokken beroepsverenigingen.  Voor de rangschikking van een toestel wordt rekening  gehouden met zijn rendabiliteit, de aard van het  aangeboden spel en de menigvuldigheid van de inzet.

---- historiek ----  ---- historique ----

- gewijzigd door art. 2 van het decreet van 25.11.2022  (B.S., 01.12.2022). Inwerkingtreding: 01.01.2023

- ingevoegd door art. 25 van het decreet van 07.12.2018  (B.S. 20.12.2018). Tekst in werking

getreden op 01.01.2019

###### Art. 2.13.3.0.2.  Art. 2.13.3.0.2.

Elke combinatie van toestellen waarop gelijktijdig  verschillende inzetten kunnen worden gedaan, die ieder  recht geven op een afzonderlijk spel, bevat zoveel

Toute combinaison d’appareils sur lesquels plusieurs  mises peuvent simultanément être engagées, chaque  mise donnant droit à un jeu distinct, comprend autant  belastbare toestellen als er afzonderlijke spelen mogelijk  zijn die gelijktijdig kunnen plaatsvinden.

Als de combinatie, vermeld in het eerste lid, de aard  vertoont van een competitiespel, wordt het aantal  belastbare toestellen evenwel beperkt tot het aantal  tekens, nummers, figuren of andere voorwerpen die in  het spel kunnen worden betrokken.

- ingevoegd door art. 26 van het decreet van 07.12.2018  (B.S. 20.12.2018). Tekst in werking

getreden op 01.01.2019

#### Afdeling 4 - Tarieven  Section 4 – Tarifs

###### Art. 2.13.4.0.1.  Art. 2.13.4.0.1.

La taxe est calculée sur la base du tarif par année  calendaire, visé dans le tableau suivant :

De belasting wordt berekend volgens het tarief per  kalenderjaar, vermeld in de volgende tabel:

categorie van het toestel

/  tarif en euro  1  4.600  2  500  3  55  4  0

/  catégorie de l’appareil

Een vierde van de belasting, vermeld in het eerste lid, is  verschuldigd voor elk kwartaal waarin een automatisch  ontspanningstoestel is opgesteld.

De tarieven, vermeld in het eerste lid, worden met  ingang van 1 januari 2020 jaarlijks geïndexeerd met  behulp van de coëfficiënt die wordt verkregen door het  algemene indexcijfer van de consumptieprijzen van het  Rijk, voor de maand oktober van het vorige jaar te delen  door het algemene indexcijfer van de consumptieprijzen  van het Rijk voor de maand oktober van het jaar 2018.

Daarbij worden de volgende afrondingen toegepast:  Dans ce contexte, les arrondissements suivants sont  appliqués :

1° de coëfficiënt wordt afgerond op het hogere of lagere  tienduizendste  naargelang  het  cijfer  van  de  honderdduizendsten al of niet vijf bereikt;

2° na de toepassing van de coëfficiënt wordt het  verkregen bedrag afgerond op het dichtstbijzijnde  veelvoud van 40 cent.

---- historiek ----  ---- historique ----

- gewijzigd door art. 49 van het decreet van 20.12.2024  (B.S., 30.12.2024). Inwerkingtreding: 01.01.2025

- gewijzigd door art. 3 van het decreet van 25.11.2022  (B.S., 01.12.2022). Inwerkingtreding: 01.01.2023

- ingevoegd door art. 28 van het decreet van 07.12.2018  (B.S. 20.12.2018). Tekst in werking

getreden op 01.01.2019

###### Art. 2.13.4.0.2.  Art. 2.13.4.0.2.

De provincies en de gemeenten zijn niet gemachtigd tot  het heffen van opcentiemen op belasting op de  automatische ontspanningstoestellen of van welke  belasting  dan  ook  op  de  automatische  ontspanningstoestellen die onderhevig zijn aan de  belasting, vermeld in dit hoofdstuk.

---- historiek ----  ---- historique ----

- ingevoegd door art. 29 van het decreet van 07.12.2018  (B.S. 20.12.2018). Tekst in werking

getreden op 01.01.2019

#### Afdeling 5 - Verminderingen  Section 5 - Réductions

###### Art. 2.13.5.0.1.  Art. 2.13.5.0.1.

(…)  (…)

---- historiek ----  ---- historique ----

- opgeheven door art. 3 van het decreet van 20.11.2020  (B.S., 03.12.2020). Inwerkingtreding vanaf aanslagjaar  2021

- ingevoegd door art. 31 van het decreet van 07.12.2018  (B.S. 20.12.2018). Tekst in werking

getreden op 01.01.2019

###### Art. 2.13.5.0.2.  Art. 2.13.5.0.2.

[…]  […]

---- historiek ----  ---- historique ----

- Opgeheven door art. 4 van het decreet van 25.11.2022  (B.S., 01.12.2022). Inwerkingtreding: 01.01.2023

getreden op 01.01.2019

#### Afdeling 6 - Vrijstellingen  Section 6 - Exonérations

###### Art. 2.13.6.0.1.  Art. 2.13.6.0.1.

Er wordt een vrijstelling van de belasting verleend voor  de automatische ontspanningstoestellen:

1° die in de lokalen die daarvoor bestemd zijn,  uitsluitend  ter  beschikking  staan  van  de  jeugdbewegingen,  van  bewoners  van  rust-  en  verzorgingsinstellingen  of  van  in  ziekenhuizen  opgenomen personen;

2° die zich bevinden in een kansspelinrichting van klasse  I als vermeld in artikel 6 van de Kansspelwet van 7 mei  1999, en onderworpen worden aan de belasting, vermeld  in artikel 2.12.4.0.1, § 2, 3°.

---- historiek ----  ---- historique ----

- ingevoegd door art. 34 van het decreet van 07.12.2018  (B.S. 20.12.2018). Tekst in werking

getreden op 01.01.2019

#### Afdeling 7 - Wijze van heffing  Section 7 - Modalités de perception

###### Art. 2.13.7.0.1.  Art. 2.13.7.0.1.

De belasting wordt gevestigd op zicht van de aangifte,  vermeld in artikel 3.3.1.0.16, of ambtshalve als de  aangifte niet is ingediend binnen de termijn, vermeld in  artikel 3.3.1.0.16, of bij onjuistheid of onvolledigheid  van de aangifte, en conform de bepalingen van artikel  3.3.2.0.1, eerste lid, 12°, en tweede lid, 8°, en artikel  3.3.3.0.1, § 2.

---- historiek ----  ---- historique ----

- ingevoegd door art. 36 van het decreet van 07.12.2018  (B.S. 20.12.2018). Tekst in werking

getreden op 01.01.2019

###### Art. 2.13.7.0.2.  Art. 2.13.7.0.2.

##### Afdeling 5 en 6 van dit hoofdstuk zijn niet van  toepassing op de automatische ontspanningstoestellen  waarvan de exploitatie is verboden krachtens artikel 4, 7  en 8 van de Kansspelwet van 7 mei 1999.

---- historiek ----  ---- historique ----

- ingevoegd door art. 37 van het decreet van 07.12.2018  (B.S. 20.12.2018). Tekst in werking

getreden op 01.01.2019

## TITEL 3 - Inning en invordering  TITRE 3 - Perception et recouvrement

### Hoofdstuk 1 - Inleidende bepalingen, opcentiemen,  opdeciem en administratieve onkostenvergoedingen

###### Art. 3.1.0.0.1.  Art. 3.1.0.0.1.

De bepalingen van titel 3 zijn, behalve bij afwijkende  bijzondere  bepalingen,  van  toepassing  op  alle  belastingen, vermeld in titel 2, alsook op het eurovignet.

In afwijking van het eerste lid, zijn de volgende  bepalingen van deze titel niet van toepassing op de  kilometerheffing:

- hoofdstuk 2;  - le chapitre 2 ;

- hoofdstuk 3, met uitzondering van artikel 3.3.1.0.11,  3.3.1.0.13, 3.3.2.0.1, eerste lid, 10°, en tweede lid, 6°, en  3.3.3.0.1, § 2, tweede lid;

- hoofdstuk 4;  - le chapitre 4 ;

- hoofdstuk 5 met uitzondering van artikel 3.5.3.0.2;  - le chapitre 5, à l'exception de l'article 3.5.3.0.2 ;

- hoofdstuk 6;  - le chapitre 6 ;

- hoofdstuk 7;  - le chapitre 7 ;

- hoofdstuk 10, met uitzondering van artikel 3.10.3.1.1,  § 2, tweede lid, en artikel 3.10.4.5.1, tweede en derde  lid;

- hoofdstuk 12.  - le chapitre 12.

De Vlaamse Regering kan :  Le Gouvernement flamand peut :

1° de wijze regelen waarop men moet handelen voor de  aangiften, de opmaak en de kennisgeving van de  kohieren, de betalingen, de bewijzen van betaling en de  inning en invordering van de verschuldigde bedragen;

2° het tarief van de vervolgingskosten regelen.  2° fixer le tarif des frais de poursuite ;

Als een vordering voor het gerecht, zelfs gedeeltelijk,  maatregelen tot voorwerp heeft die ertoe strekken de  invordering te verwezenlijken of te waarborgen van de  belastingen en toebehoren, hebben de cassatietermijn  alsook de voorziening in cassatie schorsende kracht.

- gewijzigd door art. 28 van het decreet van 21.12.2018  (B.S. 28.12.2018). Tekst treedt in werking op 07.01.2019

- tussen het eerste en het tweede lid is een lid ingevoegd  door art. 2 van het decreet van 25 maart

2016 (B.S., 01.04.2016). De tekst treedt in werking op 1  april 2016 (art. 4))

###### Art. 3.1.0.0.2.  Art. 3.1.0.0.2.

§ 1. Aan de belastingschuldigen wordt door de bevoegde  entiteit van de Vlaamse administratie een fiscaal  identificatienummer toegekend, namelijk een van de  volgende nummers:

1° het identificatienummer uit het Rijksregister van de  natuurlijke personen;

2° het ondernemingsnummer dat bekend is bij de  Kruispuntbank van Ondernemingen;

3° een automatisch gegenereerd nummer voor alle  overige belastingschuldigen voor wie geen bekend  nummer als vermeld in 1° of 2°, bestaat.

§ 2. Het fiscale identificatienummer mag worden  gebruikt in de bestanden en repertoria van de bevoegde  entiteit van de Vlaamse administratie. Het gebruik ervan  is alleen geoorloofd met het doel om te identificeren.

§ 3. Naast de toepassing, vermeld in paragraaf 2, mag  het fiscale identificatienummer van de natuurlijke  personen alleen gebruikt worden als identificatiemiddel  in de volgende externe betrekkingen die nodig zijn voor  de uitvoering van deze codex en van andere regelgeving  ter uitvoering ervan waarmee de bevoegde entiteit van  de Vlaamse administratie is belast:

1° betrekkingen met de houder van het nummer of met  zijn wettelijke vertegenwoordigers;

2° betrekkingen met de erfgenamen, algemene  legatarissen of begiftigden als de houder van het  nummer overleden is;

3° betrekkingen met de lasthebbers aan wie de houder  van het nummer een algemene lastgeving inzake  belastingen heeft verleend, op voorwaarde dat de houder  van het nummer zijn schriftelijke toestemming geeft aan  de lasthebber;

5° betrekkingen met de natuurlijke personen of  rechtspersonen en de feitelijke verenigingen die ertoe  gehouden zijn informatie te verstrekken over de houder  van het identificatienummer, in het kader van de  verplichtingen die hun zijn opgelegd door deze codex of  ingevolge de uitvoering ervan;

6° betrekkingen met de bestuursdiensten van de staat, de  besturen van de gemeenschappen, de gewesten, de  provincies, de agglomeraties, de federaties van  gemeenten  en  de  gemeenten,  alsook  met  de  vennootschappen,  verenigingen,  instellingen  of  inrichtingen naar publiek recht die met het oog op het  verstrekken  van  bepaalde  voordelen  inkomstengetuigschriften aanvragen over de fiscale  toestand van de houder van het nummer.

De personen, instellingen en verenigingen, vermeld in  het eerste lid, mogen alleen over het nummer beschikken  voor de uitvoering van de vermelde verplichtingen.

De schriftelijke toestemming, vermeld in het eerste lid,  3°, kan op ieder ogenblik worden ingetrokken. De  intrekking ervan heeft alleen uitwerking voor de  toekomst.

§ 4. Als de bevoegde entiteit van de Vlaamse  administratie aan een derde de uitvoering toevertrouwt  van werken die nodig zijn om taken te vervullen  waarmee ze is belast, is die entiteit gemachtigd,  uitsluitend voor de uitvoering van die werken:

1° aan die derde de informatiegegevens, vermeld in  artikel 3, eerste en tweede lid, van de wet van 8 augustus  1983 tot regeling van een Rijksregister van de  natuurlijke personen, mee te delen die noodzakelijk zijn  voor de uitvoering van die werken;

2°  het  fiscale  identificatienummer  alleen  als  identificatiemiddel te gebruiken.

De derden, vermeld in het eerste lid, mogen alleen over  de beoogde informatiegegevens en over het fiscale  identificatienummer beschikken gedurende de tijd die  nodig is voor de uitvoering van die werken, en ze mogen  het fiscale identificatienummer uitsluitend voor dat doel  gebruiken.

§ 5. De volgende personen, instanties en verenigingen  onderworpen aan de verplichting om het fiscale  identificatienummer van de natuurlijke personen te  vermelden:

2° de natuurlijke personen of rechtspersonen en de  feitelijke verenigingen die zich bevinden in de toestand,  vermeld in paragraaf 3, eerste lid, 5°, en die verplicht  zijn gebruik te maken van het identificatienummer van  de natuurlijke personen met toepassing van de  koninklijke besluiten van 5 december 1986 tot regeling

2° les personnes physiques ou personnes morales et les  associations de fait qui se trouvent dans la situation,  citée dans le paragraphe 3, alinéa premier, 5°, et qui sont  obligées d'utiliser le numéro d'identification des  personnes physiques en application des arrêtés royaux  du 5 décembre 1986 réglant l'utilisation dans le secteur  in de sociale sector van het gebruik van het  identificatienummer van het Rijksregister van de  natuurlijke personen.

###### Art. 3.1.0.0.3.  Art. 3.1.0.0.3.

§ 1. De gegevens en de documenten die de bevoegde  entiteit van de Vlaamse administratie heeft ontvangen,  opgesteld of verzonden in het kader van de toepassing  van de bepalingen van deze codex, met inbegrip van de  door de belastingplichtigen ingediende aangiften, alsook  de daarbij gevoegde documenten en bewijsstukken, en  die fotografisch, optisch, elektronisch of volgens elke  andere informatica- of telegeleidingstechniek worden  geregistreerd, bewaard of weergegeven, alsook de  weergave ervan op een leesbare drager, hebben  bewijskracht voor de toepassing van de bepalingen van  deze codex.

---- historiek ----  ---- historique ----

- § 2 opgeheven door art. 2 van het decreet van  19.04.2024 (B.S., 03.06.2024). Inwerkingtreding:  13.06.2024

- gewijzigd door art. 55 van het decreet van 08.06.2018  (B.S. 26.06.2018). Tekst in werking getreden op  25.05.2018

###### Art. 3.1.0.0.4.  Art. 3.1.0.0.4.

§ 1. Als er met toepassing van de bepalingen van deze  codex opcentiemen of een opdeciem worden geheven,  worden die, samen met de belasting zelf, geïnd door de  bevoegde entiteit van de Vlaamse administratie.

In het eerste lid wordt verstaan onder elektronische  zending: een beveiligde zending via het digitale loket,  vermeld in artikel 1, 2°, a), van het besluit van de  Vlaamse Regering van 20 april 2018 tot vaststelling van  de wijze van communicatie tussen het lokaal bestuur, de  indiener van de klacht en de toezichthoudende overheid  in het kader van het bestuurlijk toezicht op het lokaal  bestuur en artikel 1, 2°, a), van het besluit van de  Vlaamse Regering van 7 september 2018 tot vaststelling  van  de  wijze  van  communicatie  tussen  de  provincieoverheid, de indiener van de klacht en de  toezichthoudende overheid in het kader van het  bestuurlijk toezicht op de provincieoverheid.

Als de provincie-, agglomeratie- of gemeenteraad de  opcentiemen op de onroerende voorheffing niet heeft  vastgesteld of als een van de data of beide data, vermeld  in het eerste lid, werden overschreden, zal de onroerende  voorheffing worden gevestigd met toepassing van de  opcentiemen die voor de provincie, gemeente of  agglomeratie in kwestie van toepassing waren voor het  voorafgaande aanslagjaar.

Voor de toepassing van het derde lid wordt uitgegaan  van de naleving van de verplichtingen, vermeld in artikel  2.1.4.0.2, § 2 en § 3.

§ 3. De bevoegde entiteit van de Vlaamse administratie  stort aan de provincies, de agglomeraties en de  gemeenten de ontvangsten die ze voor hun rekening  verwezenlijkt hebben, door in de maand die volgt op de  maand van de ontvangsten, verminderd met de  ontheffingen van betaalde vorderingen die doorgevoerd  zijn tijdens de maand van de inning van die ontvangsten.

De schuldvordering, vermeld in het tweede lid, wordt  ingevorderd door ambtshalve inhouding op de  toekenning van de ontvangsten van de maand die volgt  op die van de verrekening van de ontheffingen. Als het  bedrag van de ontvangsten dat toegekend wordt  gedurende de maand die volgt op die van de verrekening  van de ontheffing ontoereikend is om het bedrag van de  schuldvordering dat overblijft te vrijwaren, wordt dat  saldo van de schuldvordering ingevorderd door  ambtshalve inhouding op de toekenning van de  ontvangsten van de daaropvolgende maand. Die  verrekening wordt herhaald tot de schuldvordering is  aangezuiverd.

§ 4. De ontvangsten, vermeld in paragraaf 3, kunnen  naast de opcentiemen en de opdeciem ook de bedragen,  vermeld in artikel 3.1.0.0.5, bevatten. Ontvangsten die  voortkomen  uit  interesten,  boetes  of  bij  de  belastingschuldige gerecupereerde invorderingskosten,  worden evenwel nooit doorgestort en komen het  Vlaamse Gewest toe.

§ 5. In afwijking van paragraaf 3 geldt voor de  onroerende voorheffing de volgende regeling:

1° de Vlaamse Regering wordt ertoe gemachtigd  voorschotten toe te staan aan de gemeenten, de  agglomeraties en de provincies in het kader van de  inning van de opcentiemen op de onroerende  voorheffing;

2° de voorschotten, vermeld in punt 1°, worden  berekend op 95 % van het bedrag van de jaarontvangsten  inzake opcentiemen op de onroerende voorheffing die  geraamd zijn in hun respectieve goedgekeurde  begrotingen, dat de gemeente respectievelijk de  agglomeratie of de provincie uiterlijk op 15 mei van het  aanslagjaar in kwestie aan de bevoegde entiteit van de  Vlaamse administratie heeft opgegeven. Bij ontstentenis  van een mededeling op de vervaldag wordt de  berekening van de voorschotten gebaseerd op de  jaarontvangsten inzake opcentiemen op de onroerende  voorheffing die de bevoegde entiteit van de Vlaamse  administratie per gemeente, agglomeratie en provincie  voor het aanslagjaar in kwestie geraamd heeft;

4° de voorschotten, vermeld in punt 1°, worden vanaf  het tweede semester van het begrotingsjaar in zes  maandelijkse gelijke schijven uitbetaald met valuta op  de vijfde bankwerkdag van iedere maand;

5° het saldo van alle verworven opcentiemen op de  laatste dag van de maand mei van het jaar dat volgt op  het aanslagjaar in kwestie, verminderd met de  voorschotten die al uitbetaald zijn voor het aanslagjaar  in kwestie en verminderd met de bedragen van betaalde  vorderingen die voor het aanslagjaar in kwestie en  eventueel voor voorgaande aanslagjaren in ontheffing  gezet zijn, wordt uiterlijk gestort op de laatste  bankwerkdag van de maand juli van het jaar dat volgt op  het aanslagjaar in kwestie;

6° opcentiemen die worden verworven na de laatste dag  van de maand mei van het jaar dat volgt op het  aanslagjaar in kwestie, worden na vermindering met de  nog niet verrekende bedragen van betaalde vorderingen  die in ontheffing gezet zijn, doorgestort uiterlijk op de  laatste bankwerkdag van de maand die volgt op de  maand van de verwerving;

7° als wordt vastgesteld dat het saldo, vermeld in 5°  negatief is, wordt het voorschot van het eerstvolgende  aanslagjaar, vermeld in 2° en 4°, verminderd met dat  negatieve saldo. In voorkomend geval worden de  verworven  opcentiemen  van  het  eerstvolgende  aanslagjaar ook verminderd met hetzelfde negatieve  saldo;

8° zowel de orderekeningen als de financiële rekening  waarop de opcentiemen op de onroerende voorheffing

8° tant les comptes d'ordre que le compte financier sur  lequel les centimes additionnels sur le précompte  voor rekening van de gemeenten, de agglomeraties en de  provincies vooraf worden betaald, mogen een negatief  saldo vertonen voor het bedrag van de gecumuleerde  voorschotten.

§ 6. Na afloop van elk kalenderjaar stuurt de bevoegde  entiteit van de Vlaamse administratie naar elke  provincie, agglomeratie en gemeente die opcentiemen  heft, een lijst met vermelding van de totale opbrengst  van de opcentiemen die, op basis van de inningen, aan  respectievelijk de provincie, de agglomeratie of de  gemeente toekomen.

---- historiek ----  ---- historique ----

- gewijzigd door art. 3 van het decreet van 30.06.2017  (B.S. 12.07.2017). Tekst in werking getreden vanaf  aanslagjaar 2018

- gewijzigd door art. 2 van het decreet van 30.06.2017  (B.S. 12.07.2017). Tekst in werking getreden vanaf  aanslagjaar 2017

###### Art. 3.1.0.0.5.  Art. 3.1.0.0.5.

De Vlaamse Regering bepaalt welk percentage van de  leegstandsheffing bedrijfsruimten die elk jaar geïnd  wordt, en van de heffing ongeschikte en onbewoonbare  woningen die elk jaar geïnd wordt, met uitzondering van  de gemeentelijke opcentiemen, de interesten en de  administratieve geldboetes, aan de gemeenten wordt  doorgestort als vergoeding voor de administratiekosten  die ze in het kader van die belastingen moeten maken.

---- historiek ----  ---- historique ----

- gewijzigd door art. 46 van het decreet van 23.12.2016  (B.S.: 30.12.2016). Tekst in werking getreden vanaf  aanslagjaar 2017

###### Art. 3.1.0.0.6.  Art. 3.1.0.0.6.

De provincies en de gemeenten die met toepassing van  artikel 2.1.4.0.2 opcentiemen op de onroerende  voorheffing heffen, en die met toepassing van artikel  2.1.4.0.1, 2, eerste lid, 3°, voor zover het eigendommen  betreft die verhuurd worden conform de voorwaarden ter  uitvoering van artikel 4.40, 4°, van de Vlaamse Codex  Wonen van 2021, en 7, en § 2/1, artikel 2.1.5.0.1, § 2,  artikel 2.1.6.0.2 en artikel 2.2.6.0.1, § 2, 2, die  opbrengsten derven, worden daarvoor volledig vergoed  door het Vlaamse Gewest. De compensatie voor artikel  2.2.6.0.1, § 2, 2, geldt enkel voor voertuigen die voor het  eerst worden vrijgesteld vanaf aanslagjaar 2019.

---- historiek ----  ---- historique ----

- gewijzigd door art. 16 van het decreet van 09.07.2021  (B.S., 10.09.2021). Inwerkingtreding: vanaf het  aanslagjaar na publicatie van dit decreet in het Belgisch  Staatsblad en ten vroegste vanaf aanslagjaar 2023.

- vervangen door art. 19 van het decreet van

22.06.2018. Tekst in werking getreden vanaf aanslagjaar  2019

- gewijzigd door art. 3 van het decreet van 20.12.2013  (B.S. 17.01.2014 Ed.2). Inwerkingtreding vanaf  aanslagjaar 2015 (art. 4)

- vervangen door art. 4 van het decreet van 20.12.2013  (B.S. 31.12.2013). Inwerkingtreding op 01.01.2014  (art.61)

---- info ----  ---- info ----

###### Art. 100. van het decreet van 18 dec. 2015 (B.S.,

29.12.2015). De tekst is in werking getreden op 1 januari  2016 (art. 135)

Als een gemeente met toepassing van artikel 3.1.0.0.6  van de Vlaamse Codex Fiscaliteit van 13 december 2013  recht had op een compensatie voor de opbrengsten, die  zij derfde voor het aanslagjaar 2014 met toepassing van  artikel 2.1.6.0.1, eerste lid, 4°, van deze codex en het  bedrag van deze compensatie is groter dan het verschil  tussen wat de gemeente met toepassing van de artikelen 6  tot en met 11 van het decreet van 5 juli 2002 tot  vaststelling van de regels inzake de dotatie en de  verdeling van het Vlaams Gemeentefonds uit de  hoofddotatie van het Gemeentefonds ontving in 2013 en  wat de gemeente met toepassing van die zelfde  bepalingen uit de hoofddotatie van het Gemeentefonds  ontving in 2014, wordt in 2016, 2017, 2018 en 2019 een  bedrag x betaald aan de gemeente volgens volgende  formule:

x = a-b,  x = a-b,

waarbij:  où :

1° a = het in 2015 uitbetaalde bedrag van de  compensatie voor gederfde opbrengsten voor het  aanslagjaar 2014 met toepassing van de artikelen  2.1.6.0.1, eerste lid, 4°, en 3.1.0.0.6 van de Vlaamse

Codex Fiscaliteit van 13 december 2013;

2° b = het verschil tussen het bedrag dat de gemeente uit  de hoofddotatie van het Gemeentefonds ontving in 2013  en het bedrag dat de gemeente uit de hoofddotatie van  het Gemeentefonds ontving in 2014, telkens met  toepassing van de artikelen 6 tot en met 11 van het  decreet van 5 juli 2002 tot vaststelling van de regels  inzake de dotatie en de verdeling van het Vlaams  Gemeentefonds.

Het bedrag x, vermeld in het eerste lid, wordt aan de  gemeente betaald uiterlijk op 15 oktober van elk jaar.

De beheerder die voor de vereffening van de  nalatenschap aangesteld is overeenkomstig artikel 4.54,  § 1 en § 2, en artikel 4.57 van het Burgerlijk Wetboek,  is ook tot die verplichtingen gehouden.

---- historiek ----  ---- historique ----

- gewijzigd door art. 8 van het decreet van 15.03.2024  (B.S. 20.03.2024). Inwerkingtreding: 30.03.2024

- toegevoegd door art. 210 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 3.1.0.0.8.  Art. 3.1.0.0.8.

Wat de invordering en de vervolging inzake de  erfbelasting betreft, kunnen elke kennisgeving en  betekening aan het adres van de woonplaats, vermeld in  artikel 3.3.1.0.8, § 1, eerste lid, 7°, gedaan worden.

---- historiek ----  ---- historique ----

- toegevoegd door art. 211 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

### Hoofdstuk 2 - Inkohiering  Chapitre 2 – Enrôlement

#### Afdeling 1 - Algemeen  Section 1re – Généralités

###### Art. 3.2.1.0.1.  Art. 3.2.1.0.1.

§ 1. De belastingen worden opgenomen in kohieren.  § 1er. Les impôts sont enrôlés.

De kohieren bevatten ten minste de volgende elementen: Les rôles contiennent au moins les éléments suivants :

1° de identiteit van de belastingplichtige;  1° l'identité du contribuable ;

2° de aanduiding van de belasting;  2° la désignation de l'impôt ;

3° het bedrag van de belasting, alsook het aanslagjaar  waarop de belasting betrekking heeft;

4° het nummer van het kohierartikel;  4° le numéro du rôle ;

5° de datum van uitvoerbaarverklaring.  5° la date de l'exequatur.

§ 2. De opschorting van de belasting belet de inkohiering  van de belasting niet.

###### Art. 3.2.1.0.2.  Art. 3.2.1.0.2.

Aanslagen inzake de onroerende voorheffing die  betrekking hebben op onroerende goederen die samen  een kadastraal inkomen hebben van minder dan 15 euro,  worden niet in een kohier opgenomen.

Een aanslag heeft betrekking op de onroerende goederen  die gelegen zijn in eenzelfde gemeente en waarvan de  zakelijke rechten van een belastingplichtige of groep van  belastingplichtigen voor elk van die onroerende  goederen identiek zijn.

---- historiek ----  ---- historique ----

- toegevoegd door art. 28 van het decreet van 08 juli  2016 (B.S., 22.08.2016). De tekst is in werking getreden  vanaf aanslagjaar 2016 (art. 38)

#### Afdeling 2 - Uitvoerbaarverklaring  Section 2 – Exequatur

###### Art. 3.2.2.0.1.  Art. 3.2.2.0.1.

Van de belastingschuldigen mag alleen een som worden  gevorderd krachtens een uitvoerbaar verklaard kohier  dat de inningstitel vormt. Dat geldt zowel voor de  belastingen zelf, als voor de eventuele administratieve  geldboeten en belastingverhogingen, als voor de  eventuele opcentiemen of de opdeciem voor de  provincies, de agglomeraties en de gemeenten.

De kohieren worden opgemaakt en uitvoerbaar  verklaard door het bevoegde personeelslid.

De boetes die worden opgelegd ingevolge overtredingen  van de regelgeving inzake de kilometerheffing kunnen  door de bevoegde entiteit van de Vlaamse administratie  worden geïnd zonder toepassing van het eerste lid.

---- historiek ----  ---- historique ----

- gewijzigd door art. 29 van het decreet van 21.12.2018  (B.S. 28.12.2018). Tekst treedt in werking op 07.01.2019

- vierde lid werd toegevoegd door art. 26 van het decreet  van 3 juli 2015 (B.S., 10.08.2015). De tekst treedt in  werking op 1 april 2016 (art. 4 van het besluit van  17.07.2015 – B.S. 10.08.2015)

###### Art. 3.2.3.0.1.  Art. 3.2.3.0.1.  De Vlaamse Regering kan de regels bepalen voor de  inkohiering  ten  laste  van  overledenen  en  onverdeeldheden.

#### Afdeling 4 - Aanslag voor overnemende of verkrijgende

vennootschap

###### Art. 3.2.4.0.1.  Art. 3.2.4.0.1.

Als een vennootschap wordt overgenomen of gesplitst in  het kader van een fusie, een aan een fusie gelijkgestelde  verrichting of een splitsing als vermeld in artikel 12:2 tot  en met 12:8 van het Wetboek van vennootschappen en  verenigingen,  of  een  soortgelijke  vennootschapsrechtelijke verrichting onder buitenlands  recht, kan de aanslag die betrekking heeft op belastbare  feiten die dateren van vóór de vermelde verrichting,  binnen de termijnen, bepaald in dit hoofdstuk, gevestigd  worden op naam van de overnemende vennootschap of  de verkrijgende vennootschappen, zelfs op een tijdstip  waarop de overgenomen of gesplitste vennootschap als  rechtspersoon niet langer bestaat.

---- historiek ----  ---- historique ----

- gewijzigd door art. 48 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

#### Afdeling 5 - Berekening en afrondingswijze  Section 5 - Calcul et mode d'arrondissement

###### Art. 3.2.5.0.1.  Art. 3.2.5.0.1.

De Vlaamse Regering bepaalt de regels voor de  berekening van de belastingen en de wijze waarop ze  afgerond worden.

### Hoofdstuk 3 - Aanslagprocedure  Chapitre 3 - Procédure d'imposition

#### Afdeling 1 – Aangifte  Section 1re – Déclaration

---- historiek ----  ---- historique ----

- afdeling 1 gewijzigd door art. 212 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 3.3.1.0.1.  Art. 3.3.1.0.1.

De belastingplichtige moet vóór de ingebruikname van  het voertuig, vermeld in artikel 2.2.2.0.1, § 2, tweede lid,  een aangifte onderschrijven die alle gegevens bevat die  nodig zijn om de belasting te berekenen en voor het  toezicht erop.

Zolang er geen aangifte is gedaan van de verandering  betreffende het houden van het voertuig, is de vroegere  houder aansprakelijk voor de belasting, behalve in geval  van verhaal op de verkrijger.

Tant qu'aucune déclaration n'a été faite concernant le  maintien du véhicule, le détenteur antécédent est  responsable de la taxe, sauf en cas de recours vis-à-vis  de l'attributaire.

---- historiek ----  ---- historique ----

- vierde lid werd toegevoegd door art. 126 van het  decreet van 18 dec. 2015 (B.S., 29.12.2015). De tekst

treedt in werking op 1 april 2016 (art. 135)

---- info ----  ---- info ----

- Art. 23 van het decreet van 19.12.2014 (B.S.  13.01.2015). Inwerkingtreding op 01.01.2015

De aangifte, vermeld in artikel 3.3.1.0.1 van de Vlaamse  Codex Fiscaliteit van 13 december 2013, die op 1 januari  2015 nog loopt, zal voor de lijkwagens automatisch  worden stopgezet op het einde van de maand die  voorafgaat aan de maand die overeenstemt met de maand  waarin de inschrijving in het repertorium van het  Directoraat-generaal Mobiliteit en Verkeersveiligheid is  uitgevoerd. Bij het begin van de daaropvolgende maand  zal de aanslag worden gevestigd voor het belastbaar  tijdperk, vermeld in artikel 3.3.2.0.1, tweede lid, 2°, van  de voormelde codex.

###### Art. 3.3.1.0.2.  Art. 3.3.1.0.2.

Voor de toepassing van titel 2, hoofdstuk 2 en 3, kan  behalve  in  geval  van  wettige  redenen  de  belastingplichtige die zijn voertuig niet inschrijft bij het  Directoraat-generaal Mobiliteit en Verkeersveiligheid,  die niet tijdig inlichtingen verstrekt conform artikel  3.13.1.2.3, die geen aangifte doet of die op de aangifte  onjuiste gegevens over het voertuig vermeldt, door het  bevoegde personeelslid van ambtswege aangeslagen  worden, behoudens zijn recht om bezwaar in te dienen.

Als de belastingplichtige de gevraagde belastbare  elementen niet verstrekt, wordt de ambtshalve aanslag  forfaitair vastgesteld op 1.250 euro per aanslagjaar.

In afwijking van artikel 2.2.2.0.1, § 2, eerste lid, artikel  2.2.7.0.2, § 3 en § 4, en artikel 3.4.7.0.3 kan bij een  ambtshalve gevestigde aanslag voor het desbetreffende  aanslagjaar geen terugbetaling meer gedaan worden op  basis van een afwijkende aangifte, een inschrijving bij  het  Directoraat-generaal  Mobiliteit  en  Verkeersveiligheid of een kennisgeving van belastbare  elementen door de belastingplichtige met betrekking tot  hetzelfde voertuig. De afwijkende aangifte, de  inschrijving bij het Directoraat-generaal Mobiliteit en  Verkeersveiligheid of de kennisgeving van belastbare  elementen door de belastingplichtige heeft pas  uitwerking vanaf het volgende aanslagjaar.

###### Art. 3.3.1.0.3.  Art. 3.3.1.0.3.

(…)  (…)

---- historiek ----  ---- historique ----

- opgeheven door art. 30 van het decreet van 21.12.2018  (B.S. 28.12.2018). Tekst treedt in werking op 07.01.2019

###### Art. 3.3.1.0.4.  Art. 3.3.1.0.4.

Met toepassing van titel 2, hoofdstuk 2 en 4, wordt bij  schrapping of wissing uit het repertorium van het  Directoraat-generaal Mobiliteit en Verkeersveiligheid  van een trekkend voertuig of van een alleen rijdend  voertuig als vermeld in artikel 2.2.2.0.1, § 2, tweede lid,  1°, en artikel 2.4.1.0.1, door het bevoegde personeelslid  ambtshalve overgegaan tot de stopzetting van de  aangifte, vermeld in artikel 3.3.1.0.2 en 3.3.1.0.3.

###### Art. 3.3.1.0.5.  Art. 3.3.1.0.5.

§ 1. De aangifte van nalatenschap moet bij elke  verkrijging overeenkomstig titel 2, hoofdstuk 7, door de  volgende personen ingediend worden bij de bevoegde  entiteit van de Vlaamse administratie :

1° bij overlijden of bij afwezigheid van een rijksinwoner  : door de erfgenamen, de algemene legatarissen en  begiftigden;

2° in geval van overlijden of bij afwezigheid van een  persoon die geen rijksinwoner is : door de erfgenamen,  legatarissen of begiftigden van onroerende goederen die  overeenkomstig artikel 5, § 2, 4°, tweede streepje, van  de bijzondere wet van 16 januari 1989 betreffende de  financiering van de Gemeenschappen en de Gewesten in  het Vlaamse Gewest te lokaliseren zijn.

In afwijking van het eerste lid, 1°, zijn, in geval van  stilzitten van de erfgenamen, algemene legatarissen en  begiftigden, de legatarissen en begiftigden onder  algemene titel of de bijzondere legatarissen en  begiftigden ertoe gehouden, op verzoek van het  bevoegde personeelslid, de aangifte in te dienen voor  datgene wat hen betreft, binnen een termijn van een  maand vanaf de derde werkdag die volgt op de  verzendingsdatum van het verzoek.

§ 2. De termijn voor de indiening van de aangifte,  vermeld in paragraaf 1, eerste (…), is vier maanden  vanaf de datum van het overlijden, als zich dat  in het rijk heeft voorgedaan. De termijn bedraagt vijf

In geval van gerechtelijke verklaring van overlijden  beginnen de termijnen, vermeld in het eerste lid, pas te  lopen zodra het vonnis in kracht van gewijsde is gegaan.

In afwijking van het eerste lid is de termijn voor de  indiening van de aangifte, vermeld in paragraaf 1, eerste  lid, ingeval van verval van de nalatenschap aan de Staat  overeenkomstig artikel 4.32 van het Burgerlijk Wetboek,  vier maanden vanaf de inbezitstelling, vermeld in artikel  4.33, tweede lid, van hetzelfde wetboek.

In afwijking van het eerste lid is de termijn voor de  indiening van de aangifte, vermeld in paragraaf 1, eerste  lid, in geval van een onbeheerde nalatenschap als  vermeld in artikel 4.58, § 1, van het Burgerlijk Wetboek,  vier maanden vanaf de aanstelling van de curator,  vermeld in artikel 4.58, § 2, van het Burgerlijk Wetboek.

---- historiek ----  ---- historique ----

- gewijzigd door art. 9 van het decreet van 15.03.2024  (B.S. 20.03.2024). Inwerkingtreding: 30.03.2024

- gewijzigd door art. 47 van het decreet van 23.12.2016  (B.S.: 30.12.2016). Tekst in werking getreden op 8  januari 2017

- gewijzigd door art. 24 van het decreet van 17 juli 2015  (B.S., 14.08.2015 ). De tekst is in werking getreden op 14  augustus 2015 (art. 41)

###### Art. 3.3.1.0.6.  Art. 3.3.1.0.6.

In de volgende gevallen moet binnen dezelfde termijnen  als vermeld in artikel 3.3.1.0.5, § 2, een nieuwe aangifte  ingediend worden bij de bevoegde entiteit van de  Vlaamse administratie :

1° in geval van een legaat, gemaakt aan een  rechtspersoon, dat aan een machtiging of goedkeuring  onderworpen is, op het moment dat die machtiging of  goedkeuring voorkomt, als op dat moment de belasting  nog niet betaald is;

2° als, na het openvallen van de nalatenschap, de actieve  samenstelling ervan vermeerderd wordt op een van de  volgende wijzen;

a) door het intreden van een voorwaarde of van elk ander  voorval;

3° als er een verandering in de devolutie van de  nalatenschap ontstaat;

4° in geval van aanwas of van terugval van eigendom,  vruchtgebruik of van ieder ander tijdelijk of levenslang  recht dat voortkomt van een beschikking, genomen door  de overledene met betrekking tot zijn overlijden;

5° in geval van fideï-commis, als de met de last van  teruggave bezwaarde goederen naar de verwachter  overgaan.

6° in het geval van artikel 2.7.1.0.6, § 1, derde lid, als,  naar  gelang  van  het  geval,  het  levensverzekeringscontract wordt afgekocht of er op  grond van het contract een uitkering gebeurt.

In de gevallen, vermeld in het eerste lid, 1° tot en met  4°, moet de aangifte ingediend worden door de  personen, vermeld in artikel 3.3.1.0.5, tenzij slechts  bepaalde erfgenamen, legatarissen of begiftigden uit de  gebeurtenis voordeel trekken, in welk geval alleen die  tot aangifte zijn verplicht.

In het geval, vermeld in het eerste lid, 1°, begint de  aangiftetermijn vanaf de datum van de machtiging of de  goedkeuring.

In de gevallen, vermeld in het eerste lid, 2° tot en met  4°, begint de aangiftetermijn op een van de volgende  data :

1° vanaf de datum van het vonnis, niettegenstaande  verzet of beroep, of van de dading als het gaat om een  betwist recht;

2° vanaf de gebeurtenis in alle andere gevallen.  2° à compter de l'événement dans tous les autres cas.

In het geval, vermeld in het eerste lid, 5°, moet de  aangifte ingediend worden door :

1° de verwachter alleen als de overdracht plaatsvindt ten  gevolge van het overlijden van de bezwaarde erfgenaam;

2° door de verwachter en de bezwaarde als de goederen  op de verwachter overgaan tijdens het leven van de  bezwaarde.

In het geval, vermeld in het eerste lid, 5°, begint de  aangiftetermijn vanaf de datum van de devolutie,  teweeggebracht door het overlijden van de bezwaarde of  op een andere wijze. Als de devolutie krachtens een

In het geval vermeld in het eerste lid, 6°, moet de  aangifte worden ingediend, naar gelang van het geval,  door de persoon die het levensverzekeringscontract  afkoopt of door de persoon die de uitkering op grond van  het contract verkrijgt.

---- historiek ----  ---- historique ----

- gewijzigd door art. 48 van het decreet van 23.12.2016  (B.S.: 30.12.2016). Tekst in werking getreden voor  overlijdens vanaf 1 januari 2017

- gewijzigd door art. 25 van het decreet van 17 juli. 2015  (B.S., 14.08.2015). De tekst is in werking getreden op 14  augustus 2015 (art. 41)

###### Art. 3.3.1.0.7.  Art. 3.3.1.0.7.

Met behoud van de toepassing van artikel 3.18.0.0.6, §  2, kan de aangiftetermijn, vermeld in artikel 3.3.1.0.5, §  2, en 3.3.1.0.6, door het bevoegde personeelslid worden  verlengd.

De aangifte, ingediend binnen de termijn, vermeld in  artikel 3.3.1.0.5, § 2, en 3.3.1.0.6, of binnen de met  toepassing van het eerste lid verlengde termijn, kan  worden gewijzigd zolang die termijn niet verstreken is,  tenzij de belanghebbenden in de aangifte uitdrukkelijk  afstand hebben gedaan van dat recht.

---- historiek ----  ---- historique ----

- toegevoegd door art. 215 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 3.3.1.0.8.  Art. 3.3.1.0.8.

§ 1. De aangifte van nalatenschap vermeldt :  La déclaration de succession mentionne :

1° de identificatie van de erflater : de voornamen, de  achternaam,  het  rijksregisternummer  of  het  identificatienummer, vermeld in artikel 8 van de wet van  15 januari 1990 houdende oprichting en organisatie van  een Kruispuntbank van de sociale zekerheid, het beroep,  het domicilie, de plaats en de datum van geboorte van de  erflater en, in voorkomend geval, van de echtgenoot of  de wettelijk samenwonende; de plaats en de datum van  het overlijden van de erflater;

2° de identificatie van de aangevers : de voornamen, de  achternaam,  het  rijksregisternummer  of  het  identificatienummer, vermeld in artikel 8 van de wet van  15 januari 1990 houdende oprichting en organisatie van

3°  de  voornamen,  de  achternaam,  het  rijksregisternummer  of  het  identificatienummer,  vermeld in artikel 8 van de wet van 15 januari 1990  houdende  oprichting  en  organisatie  van  een  Kruispuntbank van de sociale zekerheid, het domicilie,  de plaats en de datum van geboorte van de personen die  de hoedanigheid hebben van erfgenamen, legatarissen  en begiftigden;

4° de graad van verwantschap tussen de erflater en zijn  erfgenamen, legatarissen en begiftigden, wat door ieder  van hen wordt verkregen, en de titel op basis waarvan ze  tot de nalatenschap komen;

5° de voornamen, de achternaam, het domicilie, de  geboorteplaats en -datum van de kinderen, beoogd in  artikel 2.7.5.0.2, § 1;

6° in voorkomend geval, de aanduiding van de  erfgenamen die uitgesloten zijn krachtens uiterste  wilsbeschikkingen of contractuele beschikkingen;

7° de keuze van een woonplaats in België;  7° le choix d'un domicile en Belgique ;

8° de nauwkeurige aanduiding en raming van elk goed  afzonderlijk dat deel uitmaakt van het belastbare actief,  alsook de vermelding van de kadastrale afdeling, het  kadastraal perceel en de ligging als het een onroerend  goed betreft. Als de erfgenamen, algemene legatarissen  en begiftigden en iedereen die ertoe gehouden is een  aangifte van nalatenschap in te dienen met toepassing  van artikel 3.3.1.0.9/1, een schatter-expert aanstellen om  een schatting te maken van het geheel of een deel van de  onroerende goederen die zich in België bevinden en die  voor hun verkoopwaarde moeten of kunnen worden  aangegeven, wordt het deskundige schattingsverslag bij  de aangifte van nalatenschap gevoegd. Als de  erfgenamen, algemene legatarissen en begiftigden en  iedereen die ertoe gehouden is een aangifte van  nalatenschap in te dienen met toepassing van artikel  3.4.3.0.2  van  deze  codex,  een  verzoek  tot  inbetalinggeving indienen, wordt de raming vervangen  door een verwijzing naar artikel 3.4.3.0.2 van deze  codex als het cultuurgoed in zijn geheel deel uitmaakt  van de nalatenschap of op de dag van het overlijden in  zijn geheel toebehoort aan de overledene en zijn  overlevende echtgenoot of zijn wettelijk samenwonende  partner of op de dag van het overlijden in zijn geheel  toebehoort aan de overledene en een van zijn  erfgenamen, legatarissen en begiftigden;

10° behoudens als toepassing wordt gemaakt van artikel  2.7.3.4.2, eerste lid, de aanduiding van iedere schuld die

10° sauf application de l'article 2.7.3.4.2, premier  alinéa, l'indication de toute dette qui peut être admise en

11° (…)  11° (…)

12° de begunstigde persoon, alsook de datum van de  akten of aangiften, en de grondslag waarop het  registratierecht is of moet worden geheven als de erflater  ten bate van zijn erfgenamen, legatarissen of begiftigden  schenkingen heeft gedaan die vastgesteld zijn door  akten, die dagtekenen van minder dan drie jaar vóór de  datum van het overlijden en die vóór dezelfde datum tot  de formaliteit van de registratie aangeboden zijn of  verplicht registreerbaar geworden zijn. Ongeacht de  datum van de akte geldt deze regel ook als de schenking  gedaan is onder een opschortende voorwaarde die  vervuld is ingevolge het overlijden van de schenker of  minder dan drie jaar vóór dat overlijden;

13° als de erflater het vruchtgebruik van goederen gehad  heeft of met fideï-commis bezwaarde goederen  verkregen heeft : welke die goederen zijn, met  aanduiding van de personen die tot het genot van de  volle eigendom zijn gekomen of voordeel getrokken  hebben uit het fideï-commis ten gevolge van het  overlijden van de erflater;

14° met aanduiding van de betrokken persoon of de  betrokken goederen, de vraag tot toepassing van :

a) het abattement, vermeld in artikel 2.7.3.2.12;  a) de l'abattement, visé à l'article 2.7.3.2.12 ;

b) het verlaagde tarief, vermeld in artikel 2.7.4.2.2. In  voorkomend geval moet bij de aangifte de volgende  informatie gevoegd worden :

1) de naam en het ondernemingsnummer van de  familiale onderneming of familiale vennootschap  waarvoor het voordeel gevraagd wordt;

2)  de  voornaam  en  de  achternaam  van  de  medeaandeelhouders van de erflater en hun graad van  verwantschap met de erflater;

3) hetzij de activa van de familiale onderneming met een  duidelijke omschrijving en verwijzing naar de  boekhouding en, als het onroerende goederen betreft, de  vermelding of ze al dan niet hoofdzakelijk voor  bewoning worden aangewend of zijn bestemd, hetzij het  aantal aandelen en de precieze aard van alle aandelen

4) kopieën van de goedgekeurde jaarrekeningen van de  drie boekjaren die voorafgaan aan het overlijden van de  erflater, opgemaakt overeenkomstig de vigerende  boekhoudwetgeving van de plaats waar de zetel  gevestigd is als de zetel van de onderneming of  vennootschap niet in België ligt;

5) kopieën van het rechtsgeldige aandelenregister of, bij  gebrek  daaraan,  de  door  alle  aandeelhouders  ondertekende notulen van de laatste algemene  vergadering die voorafgaat aan het overlijden van de  erflater,  waaruit  op  ondubbelzinnige  wijze  de  participaties blijken, vermeld in artikel 2.7.4.2.2, § 1,  eerste lid, 2°, of tweede lid;

6) een kopie van de laatste voor het overlijden door de  erflater  ingediende  fiscale  aangifte  voor  de  personenbelasting wat familiale ondernemingen betreft;

7) een kopie van de gecoördineerde statuten, zoals van  toepassing op de dag van het overlijden;

8) een verslag dat een bedrijfsrevisor, die niet de  commissaris is, of een gecertificeerd accountant heeft  uitgereikt. Het verslag is gedateerd en ondertekend  voorafgaand aan de datum van de indiening van de  aangifte van nalatenschap voor elke familiale  vennootschap. Het verslag bevat al de volgende  elementen:

i) de voor- en achternaam van de bedrijfsrevisor of de  accountant, het registratienummer in het openbaar  register, vermeld in artikel 10, § 1, van de wet van 7  december 2016 tot organisatie van het beroep van en het  publiek toezicht op de bedrijfsrevisoren, of het  inschrijvingsnummer in het openbaar register, vermeld in  artikel 29 van de wet van 17 maart 2019 betreffende de  beroepen van accountant en belastingadviseur;

ii) de voor- en achternaam, het rijksregisternummer en  het adres van de aanvrager of, als er verschillende zijn,  de aanvragers;

iii) de naam en het ondernemingsnummer van de  familiale vennootschap waarvoor het verlaagde tarief  wordt gevraagd;

iv) de verkoopwaarde van de volle eigendom van de  vererfde aandelen van de familiale vennootschap, zoals  die is geraamd door de bedrijfsrevisor of de accountant;

vi) het gedeelte van de waarde, zoals die is geraamd door  de bedrijfsrevisor of de accountant, vermeld in punt iv),  dat wordt bepaald door de verkoopwaarde van de  onroerende goederen, vermeld in punt v), in de familiale  vennootschap, of in participaties van minstens 10% van  de familiale vennootschap in haar  dochtervennootschappen;

vii) het verschil tussen de verkoopwaarde, vermeld in  punt iv), en de verkoopwaarde, vermeld in punt vi);

viii) de motivering van de wijze waarop de  bedrijfsrevisor of de accountant de verkoopwaarden,  vermeld in punt iv), vi) en vii), heeft bepaald, met  vermelding van de gebruikte waarderingsmethode;

ix) de referentiedatum voor de waardebepaling, vermeld  in punt iv) en v), namelijk de datum van het overlijden  van de erflater;

c) de vermindering, vermeld in artikel 2.7.5.0.3;  c) de la réduction visée à l'article 2.7.5.0.3 ;

d) de vermindering, vermeld in artikel 2.7.5.0.4;  d) de la réduction visée à l'article 2.7.5.0.4 ;

e) de aftrek, vermeld in artikel 2.7.5.0.5;  e) de la déduction, visée à l'article 2.7.5.0.5 ;

f) de vrijstelling, vermeld in artikel 2.7.6.0.1, waarbij  tevens de maatschappelijke rechten moeten worden  vermeld in de aangifte van de nalatenschap die deel  uitmaken van de nalatenschap van de inschrijver, of  belastbaar zijn overeenkomstig artikel 2.7.1.0.4. In  voorkomend geval moet bij de aangifte ook het attest,  vermeld in artikel 2.7.6.0.1, § 4, worden gevoegd;

g) (...);  g) (...) ;

h) (...);  h) (...) ;

i) de vrijstelling, vermeld in artikel 2.7.6.0.4;  i) de l'exemption, visée à l'article 2.7.6.0.4.

j) de vrijstelling, vermeld in artikel 2.7.4.1.1, § 2, derde  lid.

k) de vrijstelling, vermeld in artikel 2.7.6.0.5. In  voorkomend geval moeten de verzoekers in de aangifte  verklaren dat ze kennis hebben van het bepaalde in

l) de vermindering, vermeld in artikel 2.7.5.0.6 van deze  codex;

m) de vrijstelling, vermeld in artikel 2.7.6.0.6, § 1;  m) l'exonération, visée à l'article 2.7.6.0.6, § 1er ;

n) het verzoek tot inbetalinggeving, vermeld in artikel  3.4.3.0.2 van deze codex, als het cultuurgoed in zijn  geheel deel uitmaakt van de nalatenschap of op de dag  van het overlijden in zijn geheel toebehoort aan de  overledene en zijn overlevende echtgenoot of zijn  wettelijk samenwonende partner of op de dag van het  overlijden in zijn geheel toebehoort aan de overledene  en een van zijn erfgenamen, legatarissen en begiftigden;

o) het verlaagde tarief, vermeld in artikel 2.7.4.2.5, § 1,  eerste lid;

15° in voorkomend geval de erfovereenkomst, die is  opgesteld conform artikel 4.254 tot en met 4.259 van het  Burgerlijk Wetboek. In dat geval wordt een kopie van die  notariële erfovereenkomst bij de aangifte gevoegd;

16° in voorkomend geval de verkrijgingen van  vruchtgebruik met toepassing van artikel 4.18 of artikel  4.23, § 2, van het Burgerlijk Wetboek. In dat geval wordt  een kopie van de akte van schenking bij de aangifte  gevoegd. In geval van verzaking aan het vruchtgebruik  op een ander tijdstip wordt het stuk gevoegd waaruit die  verzaking blijkt;

17°  in  voorkomend  geval  welke  schenkingen,  levensverzekeringen en legaten aan inbreng of inkorting  zijn onderworpen en in bevestigend geval op welke  wijze de inbreng of inkorting gebeurt.

Als het successierecht verschuldigd is, bevat de aangifte  bovendien de uitdrukkelijke vermelding van het adres en  de datum en duur van de vestiging van de verschillende  fiscale woonplaatsen die de erflater of de afwezige  gehad heeft in de periode van vijf jaar voorafgaand aan  zijn overlijden of aan het tijdstip waarop het laatste  bericht van de afwezige werd ontvangen.

§ 2. In afwijking van paragraaf 1, eerste lid, 8°, mogen  elk van volgende groepen van goederen het voorwerp  uitmaken van een globale aangifte en globale raming :

1° andere onroerende goederen dan de onroerende  goederen door bestemming, vermeld in punt 2° tot en  met punt 8° hieronder, die een enig bedrijf of een enkel  domeingeheel uitmaken;

2°  wat  betreft  de  voorwerpen  die  tot  een  landbouwbedrijf dienen :

a) elke soort van dieren;  a) chaque espèce d'animaux ;

b) het landbouwgereedschap;  b) les ustensiles aratoires ;

c) de bezaaiingen en andere vruchten te velde;  c) les emblaves et autres récoltes sur pied ;

d) de zaden, de waren, het stro en de meststoffen;  d) les semences, denrées, pailles et engrais ;  3°  wat  betreft  de  voorwerpen  die  tot  een  nijverheidsbedrijf dienen :

a) de werktuigen;  a) l'outillage ;

b) de vervaardigde of bereide koopwaren en de  grondstoffen;

4° wat betreft de voorwerpen die tot een handelsbedrijf  of ambachtsbedrijf dienen :

a) het materieel en de bedrijfstoestellen;  a) le matériel et les ustensiles d'exploitation ;

b) de koopwaren;  b) les marchandises ;

5° de materiële roerende goederen, dienstig voor of  aangewend in het kader van een vrij beroep;

6° de kledingstukken, de juwelen, de boeken en alle  andere voorwerpen tot persoonlijk gebruik van de  erflater;

7° de stoffering, het vaatwerk, het keukengereedschap  en andere voorwerpen van gelijke aard;

8° de verzamelingen van schilderijen, porselein, wapens  en andere voorwerpen;

9° de wijn en andere waren.  9° les vins et autres denrées.

Het eerste lid geldt niet voor cultuurgoederen die worden  aangeboden om de erfbelasting en toebehoren te betalen  met toepassing van artikel 3.4.3.0.2.

---- historiek ----  ---- historique ----

- gewijzigd door art. 20 van het decreet van 19.12.2025  (B.S. 30.12.2025). Inwerkingtreding: Van toepassing op  alle nalatenschappen die openvallen vanaf 1 januari  2026.

- gewijzigd door art. 11 van het decreet van 19.12.2025  (B.S. 30.12.2025). Inwerkingtreding: 01.01.2026

- gewijzigd door art. 10 van het decreet van 15.03.2024  (B.S. 20.03.2024). Inwerkingtreding: 30.03.2024

- gewijzigd door art. 7 van het decreet van 10.03.2023  (B.S., 23.03.2023). Inwerkingtreding op een datum die de  Vlaamse Regering vaststelt en uiterlijk op 01.07.2023

- gewijzigd door art. 49 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- gewijzigd door art. 6 van het decreet van 19.03.2021  (B.S., 07.04.2021). Inwerkingtreding: 01.07.2021. Van  toepassing op nalatenschappen die opengevallen zijn  vanaf 1 juli 2021

- gewijzigd door art. 18, 1° en 2° van het decreet van  22.12.2017 (B.S. 21.02.2018). Tekst treedt in werking op  09.06.2020 (art. 1 besluit 04.05.2018 B.S.

30.05.2018)

- gewijzigd door art. 31,1° van het decreet van  21.12.2018 (B.S. 28.12.2018). Inwerkingtreding op  01.05.2019 (art. 3 van het besluit van 05.04.2019 - B.S.  07.05.2019)

- gewijzigd door art. 31,2° van het decreet van  21.12.2018 (B.S. 28.12.2018). Tekst treedt in werking op  07.01.2019

- gewijzigd door art.12 van het decreet van 06.07.2018  (B.S. 20.07.2018 Ed.2). Tekst treedt in werking op  01.09.2018

- gewijzigd door art. 18, 3° van het decreet van  22.12.2017 (B.S. 21.02.2018). Tekst treedt in werking

op 09.06.2018 (art. 1 besluit 04.05.2018 B.S.

30.05.2018)

- § 1, 14°, j) toegevoegd door art. 26 van het decreet van  17 juli 2015 (B.S., 14.08.2015). De tekst is in werking  getreden op 14 augustus 2015 (art. 41)

###### Art. 3.3.1.0.9.  Art. 3.3.1.0.9.

De erfgenamen, algemene legatarissen en begiftigden en  al wie gehouden is tot het indienen van een aangifte van  nalatenschap, kunnen vóór de aangifte en uiterlijk vóór  het verstrijken van de aangiftetermijn, vermeld in artikel  3.3.1.0.5, § 2, en 3.3.1.0.6, aan de bevoegde entiteit van  de Vlaamse administratie een schatting vragen van het  geheel of een deel van de onroerende goederen die zich  in België bevinden en die voor hun verkoopwaarde  moeten of kunnen worden aangegeven. De aanvragers  kunnen bij hun aanvraag en bij het eventuele  plaatsbezoek, vermeld in het derde lid, elementen  aandragen die nuttig zijn voor die schatting.

De bevoegde entiteit van de Vlaamse administratie  bevestigt de ontvangst van de aanvraag binnen vijftien  kalenderdagen.

Als de bevoegde entiteit van de Vlaamse administratie  een plaatsbezoek noodzakelijk acht, worden de  aanvragers ingelicht over de datum en het uur waarop  dat plaatsbezoek zal plaatsvinden.

Het gemotiveerde resultaat van de schatting wordt  schriftelijk ter kennis gebracht van de aanvragers. De  schatting is bindend voor de bevoegde entiteit van de  Vlaamse administratie en zal bijgevolg gebruikt worden  voor de berekening van de erfbelasting.

De aanvraag tot schatting, vermeld in dit artikel, heeft  voor de aanvrager tot gevolg dat het bindende karakter  van de schatting, vermeld in artikel 3.3.1.0.9/1, vervalt  voor hetzelfde onroerend goed.

---- historiek ----  ---- historique ----

- gewijzigd door art. 50 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- toegevoegd door art. 217 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst treedt in  werking op een door de Vlaamse Regering te bepalen  datum (art. 325)

§ 1. De erfgenamen, algemene legatarissen en  begiftigden en iedereen die ertoe gehouden is een  aangifte van nalatenschap in te dienen, kunnen een  schatter-expert aanstellen om een schatting te maken van  het geheel of een deel van de onroerende goederen die

§ 1er. Les héritiers, légataires et bénéficiaires généraux  et quiconque est tenu d’introduire une déclaration de  succession peuvent désigner un taxateur-expert pour  faire une estimation de l’ensemble ou d’une partie des  biens immobiliers qui se trouvent en Belgique et qui  zich in België bevinden en die voor hun verkoopwaarde  moeten of kunnen worden aangegeven.

De schatting is alleen bindend voor de bevoegde entiteit  van de Vlaamse administratie als:

1° de schatter-expert op het moment van de schatting is  opgenomen op de lijst van aan te stellen erkende  schatters-experten, vermeld in paragraaf 2, na naleving  van de voorwaarden daarvoor;

2° de schatting deugdelijk wordt gemotiveerd in een  deskundig schattingsverslag dat voldoet aan de  voorwaarden, vermeld in paragraaf 3;

3° het deskundige schattingsverslag wordt gevoegd bij  de aangifte van nalatenschap, vermeld in artikel  3.3.1.0.5, binnen de termijnen, bepaald in dat artikel.

Na de ontvangst van de schriftelijke aanvraag bevestigt  de schatter-expert schriftelijk dat hij de aanvraag heeft  ontvangen en meldt hij of hij de opdracht al dan niet  aanvaardt. Hij werkt zijn opdracht af binnen een termijn  die wordt bepaald in onderling overleg met de  opdrachtgever, zonder dat daaraan rechten ontleend  kunnen  worden  voor  de  verlenging  van  de  aangiftetermijn, vermeld in artikel 3.3.1.0.5.

§ 2. De schatter-expert die opgenomen wil worden op  een lijst van aan te stellen schatters-experten als vermeld  in paragraaf 1, dient daarvoor een aanvraag in door een  modelovereenkomst te ondertekenen die de bevoegde  entiteit van de Vlaamse administratie ter beschikking  stelt, waarbij de nodige bewijsstukken zijn gevoegd die  aantonen dat:

1°  de  aanvrager  beroepsmatig  schattingen  en  waarderingen van onroerende goederen uitvoert;

2° de aanvrager over de beroepskwalificatie daarvoor  beschikt door de opleiding die hij gevolgd heeft, en door  permanente bijscholing.

Om te voldoen aan het eerste lid, 2°, bezorgt hij een  afschrift van relevante diploma’s, getuigschriften of  attesten.

Als aan de voorwaarden, vermeld in het eerste lid, niet  is voldaan, deelt het bevoegde personeelslid de  beslissing van weigering tot opname op de lijst en de  redenen daarvoor mee aan de aanvrager. Tegen die

S’il n’a pas été satisfait aux conditions, visées à l’alinéa  premier, le membre du personnel compétent informe le  demandeur de la décision de refus de son inscription sur  la liste et les raisons de la non-inscription. Le  beslissing kan de aanvrager, op straffe van verval,  binnen een maand na de weigering tot opname een  gemotiveerd schriftelijk beroep instellen bij de  bevoegde entiteit van de Vlaamse administratie. Het  beroep  wordt  onderzocht  door  een  besluitvormingsorgaan dat is samengesteld uit de  bevoegde personeelsleden met minstens de graad van  afdelingshoofd. Ze beslissen over het beroep bij  consensus en brengen de aanvrager schriftelijk op de  hoogte van de gemotiveerde beslissing over het beroep.

Als er geen beslissing wordt genomen over de aanvraag  binnen de dertig werkdagen na de ontvangst van de  aanvraag en de bijbehorende bewijsstukken, vermeld in  het tweede lid, of van het beroep tegen de weigering tot  opname, wordt de aanvrager voor een periode van  maximaal zes maanden opgenomen op de lijst. Als  binnen die periode een beslissing wordt genomen over  de aanvraag, geldt die beslissing vanaf het ogenblik van  de kennisgeving ervan. Als dan nog geen beslissing is  genomen, vervalt de tijdelijke opname en moet een  nieuwe aanvraag worden ingediend.

Personeelsleden van de bevoegde entiteit van de  Vlaamse administratie kunnen niet optreden als schatter-  expert.

De bevoegde entiteit van de Vlaamse administratie  publiceert de lijst, vermeld in het eerste lid, minstens  maandelijks op haar publiek toegankelijke website als er  schatters-experten toegevoegd of geschrapt worden. Op  de lijst worden de voor- en achternaam van de schatter-  expert opgenomen, het KBO-nummer waaronder zijn  beroepsactiviteit is geregistreerd, het adres van de plaats  van vestiging en, in voorkomend geval, de commerciële  benaming waaronder de activiteiten worden uitgevoerd,  de datum van opname op de lijst en de eventuele  periodes van tijdelijke schorsing.

§ 3. Het schattingsverslag wordt opgebouwd als een  uitgebreid deskundig rapport en bestaat uit:

1° een inleidend gedeelte, dat de volgende elementen  omvat:

b) de identificatie van de schatter-expert, namelijk voor-  en achternaam, beroepstitel en het door de bevoegde  entiteit van de Vlaamse administratie toegekende  identificatienummer voor schatters-experten;

b) l’identification du taxateur-expert, à savoir le prénom  et  nom,  le  titre  professionnel  et  le  numéro  d’identification pour taxateur-experts qui lui a été  accordé par l’entité compétente de l’administration  flamande ;  c) de identificatie van de opdrachtgever, namelijk voor-  en  achternaam  of  benaming,  rijksregister-  of  ondernemingsnummer, adres en, in voorkomend geval,  de  wettelijke  vertegenwoordiger  van  de  opdrachtgevende overheidsinstantie;

d) het doel van de schatting, namelijk de volgende  vermelding: “Dit schattingsverslag is opgemaakt met  naleving van het kwaliteitscharter van de Vlaamse  Belastingdienst voor schatters-experten en dient als  waardering bij de aangifte van nalatenschap.”;

e) de referentiedatum van de schatting, namelijk de  datum van overlijden van de erflater;

f) de datum van het plaatsbezoek;  f) la date de la visite sur les lieux ;

g) de identificatie van het te schatten goed, namelijk:  g) l’identification du bien à estimer, à savoir :

1) het postnummer en de gemeente, het dorp of gehucht,  de straat en eventueel het huisnummer, en eventueel de  CRAB-gegevens van het onroerend goed;

2) de kadastrale gegevens, namelijk de kadastrale  afdeling, de sectie, het perceelnummer en het  partitienummer,  de  kadastrale  oppervlakte,  het  kadastraal inkomen en, in voorkomend geval, de  kadastrale  detailidentificatie  van  een  privatieve  eigendom;

3) de eigendomstoestand van het onroerend goed, met  een beschrijving van de rechten van elke houder van een  zakelijk recht, alsook van zijn aandeel in de volledige  eigendomssituatie. Voor onroerende goederen in mede-  eigendom worden de aandelen in het hele onroerend  goed meegedeeld;

2° de beschrijving van het te schatten goed, die de  volgende elementen omvat, in voorkomend geval  toegevoegd als bijlage:

a) een algemene beschrijving, namelijk:  a) une description générale, à savoir :

1) de ligging in de straat en de ruimere omgeving, de  toestand en uitrusting van de straat, de openbare  nutsvoorzieningen;

3) de bereikbaarheid met openbaar of privévervoer;  3) l’accessibilité avec les transports publics ou privés ;

4) zowel voor het terrein als de gebouwen: de  bestemming en de aanwending;

4) tant pour le terrain que pour les bâtiments : la  destination et l’affectation ;  5)  alleen  voor  het  terrein:  de  volledige  grondoppervlakte, de vorm, de breedte aan de straat, de  rooilijnbreedte, de relatieve hoogteligging ten opzichte  van de straat of omgeving, de oriëntatie en de  bodemoccupatie;

6) alleen voor de gebouwen: de bouwwijze, het aantal  verdiepingen en bijgebouwen, de gevelbreedte, de  plaatsing op het terrein, de bebouwde oppervlakte, de  nuttige oppervlakte en de algemene toestand op het vlak  van onderhoud, afwerking en comfort;

b) een bijzondere beschrijving van de gebouwen,  namelijk:

1) het bouwjaar, de constructiewijze, de kwaliteit van de  constructie en de gebruikte materialen voor gevels,  vloeren, muren, plafonds, daken en schrijnwerk, en de  algemene staat van onderhoud;

2) de indeling en, volgens de indeling van de gebouwen,  de afwerking, de uitrusting en voorzieningen op het vlak  van comfort;

c) de stedenbouwkundige ligging en voorschriften, de  toestand op het vlak van onroerend erfgoed, van  voorkooprecht en van de watertoets;

d) de gegevens over de zakelijke rechten en de  overeenkomstige datum en wijze van verwerving. Als  het onroerend goed verhuurd is, wordt het type contract,  de duurtijd ervan en de overeengekomen huurprijs  weergegeven;

e) de liggingsplannen en per verdieping schetsen van de  indeling, waarbij een foto van de voorgevel is gevoegd,  en, in voorkomend geval, bijkomende foto’s als die  noodzakelijk zijn om de waarde van het onroerend goed  te bepalen en om de situatie op de datum van het  plaatsbezoek vast te leggen;

3° de beschrijving van de gebruikte vergelijkingspunten,  vermeld in punt 4°, die telkens de volgende elementen  omvat:

a) algemene gegevens over de ligging en de kadastrale  gegevens van het vergelijkingspunt, namelijk:

1) het postnummer en de gemeente, het dorp of gehucht,  de straat en, in voorkomend geval, het huisnummer;

3) in voorkomend geval het bouwjaar van het  vergelijkingspunt;

b) de gegevens van de overdracht die aan de basis liggen  van de opname als vergelijkingspunt: de aard en datum  van de overdracht, en de belastbare grondslag ervan;

c) bijzondere gegevens over de ligging, bestemming en  eventuele bebouwing;

4° de analyse die leidt tot de geschatte waarde. De  analyse wordt in principe uitgevoerd aan de hand van  een afweging ten opzichte van vergelijkingspunten.  Uitzonderlijk  en  voor  specifieke  eigendommen  waarvoor geen vergelijkingspunten beschikbaar zijn,  geeft de schatter-expert weer hoe de waarde dan wel  wordt bepaald. De schatter-expert motiveert die  afwijking in zijn verslag;

5° het besluit, dat de hoofdkenmerken van de analyse  herneemt, de referentiedatum voor de waardebepaling  en als finale conclusie de geschatte waarde;

6° de eedformule “Ik zweer dat ik mijn opdracht in eer  en geweten getrouw heb vervuld”, de dagtekening en de  ondertekening.

§ 4. De bevoegde entiteit van de Vlaamse administratie  organiseert het toezicht en de controle op de naleving  van de bepalingen, vermeld in paragraaf 1 tot en met 3.  Daarbij kan informatie uitgewisseld worden met  beroepsverenigingen waarbij de schatter-expert is  aangesloten.

Bij  vastgestelde  inbreuken  kan  het  bevoegde  personeelslid beslissen tot schrapping van de schatter-  expert van de lijst van schatters-experten. Die beslissing  tot schrapping en de redenen daarvoor worden aan de  schatter-expert meegedeeld. Tegen die beslissing kan de  aanvrager, op straffe van verval, binnen een maand na  de beslissing gemotiveerd schriftelijk beroep instellen  bij de bevoegde entiteit van de Vlaamse administratie.

Als er geen beslissing wordt genomen over het beroep  binnen de dertig werkdagen na de ontvangst van het  beroep, vermeld in het tweede lid, wordt de aanvrager  voor een periode van maximaal zes maanden terug  opgenomen op de lijst. Als binnen die periode een  beslissing wordt genomen over het beroep, geldt die  beslissing vanaf het ogenblik van de kennisgeving  ervan. Als dan nog geen beslissing is genomen, blijft de  aanvrager opgenomen op de lijst.

---- historiek ----  ---- historique ----

- gewijzigd door art. 3 van het decreet van 10.11.2022  (B.S. 19.01.2023). Inwerkingtreding: 04.03.2023 (art. 7  van het besluit van 20.01.2023 - B.S., 22.02.2023)

- ingevoegd door art. 23 van het decreet van 08.12.2017  (B.S., 14.12.2017). De tekst is in werking getreden op  24.12.2017 en treed buiten werking op een door de  Vlaamse Regering vast te stellen datum

###### Art. 3.3.1.0.10.  Art. 3.3.1.0.10.

Als de laatste dag van een termijn als vermeld in deze  afdeling, op een zaterdag, zondag of op een wettelijke of  decretale feestdag valt, wordt de termijn verlengd tot de  eerstvolgende werkdag die volgt op het verstrijken van  de termijn.

---- historiek ----  ---- historique ----

- toegevoegd door art. 218 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 3.3.1.0.11.  Art. 3.3.1.0.11.

§ 1. Tenzij het voertuig is vrijgesteld van de  kilometerheffing, moet de houder van een voertuig als  vermeld in artikel 1.1.0.0.2, vijfde lid, 6°, voorafgaand  aan het gebruik van elke weg, voor dat voertuig met een  dienstaanbieder of de hoofddienstaanbieder naar keuze  een dienstverleningsovereenkomst sluiten.

Bij gebreke aan afdoend bewijs van het maximaal  toegestane totaalgewicht van het voertuig, wordt het  voertuig geacht een maximaal toegestaan totaalgewicht  van hoger dan 32 ton te hebben.

Bij gebreke aan afdoend bewijs van de EURO-  emissieklasse van het voertuig, wordt het voertuig  geacht te behoren tot de categorie `overige EURO-  emissieklassen', vermeld in de tabellen, opgenomen in  artikel 2.4.4.0.2, eerste lid, 5° en 7°.

De vermoedens, vermeld in het derde en vierde lid,  worden toegepast tot die met afdoend bewijs worden  weerlegd. Dat bewijs heeft evenwel geen invloed op de  heffingen die verschuldigd zijn voor kilometers die zijn  afgelegd vóór de verificatie van de gegevens uit het  voorgelegde bewijsstuk door de dienstaanbieder of de  hoofddienstaanbieder.

De houder van het voertuig heeft het recht heeft om,  voorafgaand aan het gebruik van een weg, de  emissieklasse van het voertuig elektronisch mee te  delen.

§ 1/1. De dienstaanbieder of de hoofddienstaanbieder is  ertoe gehouden om de juistheid van de door de houder  van het voertuig voorgelegde voertuigdocumenten,  alsook de elektronisch meegedeelde emissieklasse,  vermeld in paragraaf 1, tweede lid, te controleren.

§ 2. De dienstaanbieder of de hoofddienstaanbieder kan  de uitvoering van de dienstverleningsovereenkomst  alleen schorsen in die gevallen waarin de gebruiker of,  in voorkomend geval, de bestuurder :

1° niet voldoet aan zijn betalingsverplichtingen jegens  de dienstaanbieder of de hoofddienstaanbieder, zoals die  in de dienstverleningsovereenkomst zijn bepaald;

2° in voorkomend geval, geen of een ontoereikend  gegarandeerd betaalmiddel ter beschikking heeft  gesteld;

3° gebruikmaakt van de boordapparatuur op een wijze  die strijdig is met de gebruiksaanwijzing die door de  dienstaanbieder  of  de  hoofddienstaanbieder  ter  beschikking is gesteld;

5° de instructies van de dienstaanbieder of de  hoofddienstaanbieder niet opvolgt met het oog op de  vervanging  of  de  herstelling  van  de  defecte  boordapparatuur.

De dienstaanbieder of de hoofddienstaanbieder vermeldt  de  schorsing  van  de  uitvoering  van  de  dienstverleningsovereenkomst op de lijst van ongeldig  verklaarde boordapparatuur en brengt de gebruiker en de  Vlaamse administratie onmiddellijk op de hoogte van de  schorsing  van  de  uitvoering  van  de  dienstverleningsovereenkomst.

§ 3. De dienstaanbieder en de hoofddienstaanbieder  stellen  een  lijst  op  van  ongeldig  verklaarde  boordapparatuur  die  verband  houdt  met  hun  dienstverleningsovereenkomsten met de gebruikers,  waaronder minstens de gebeurtenissen, vermeld in  paragraaf 2, 1° tot en met 5°, en de schorsing van de  dienstverleningsovereenkomst.

Ze werken die lijst bij en delen de bijgewerkte lijst  minstens dagelijks mee aan de tolheffer.

De lijst van ongeldig verklaarde boordapparatuur wordt  bijgehouden in overeenstemming met de geldende  regels over de bescherming van persoonsgegevens.

---- historiek ----  ---- historique ----

- §1, tweede lid gewijzigd, zesde lid ingevoegd, §1/1  ingevoegd, §2, eerste lid gewijzigd, tweede lid vervangen,  §3 ingevoegd door art. 15 van het decreet van  03.05.2024 (M.B., 22.05.2024). Inwerkingtreding:  01.07.2025

- toegevoegd door art. 27 van het decreet van 3 juli 2015  (B.S., 10.08.2015). De tekst treedt in werking op 1 april  2016 (art. 44)

###### Art. 3.3.1.0.13.  Art. 3.3.1.0.13.

§ 1. De registratie van afgelegde kilometers, die nodig is  voor de berekening van de kilometerheffing, wordt  gedaan met behulp van een boordapparatuur.

§ 2. Tenzij het voertuig is vrijgesteld van de  kilometerheffing, moet de houder van het voertuig  voorafgaand aan het gebruik van elke weg ervoor zorgen  dat het voertuig is uitgerust met de boordapparatuur die  aan hem ter beschikking gesteld is.

§ 3. De bestuurder ziet er tijdens elk gebruik van een weg  op toe dat enkel één boordapparatuur die geschikt is voor  gebruik in het tolgebied geactiveerd is en volgens de  gegevens die de mens-machine-interface aangeeft, de  afstand die het voertuig aflegt registreert.

In het eerste lid wordt verstaan onder mens-machine- interface : ieder onderdeel van de elektronische  registratievoorziening  waarmee  de  elektronische  registratievoorziening en degene die deze gebruikt met  elkaar communiceren, met inbegrip van, in voorkomend  geval, de toetsen en het beeldscherm.

§ 4. De houder van het voertuig stelt zich onmiddellijk  in  verbinding  met  de  dienstaanbieder  en  de  hoofddienstaanbieder in de volgende gevallen :

1° als de elektronische registratievoorziening signaleert  dat het voertuig niet meer voldoet aan de bij deze codex  of de uitvoeringsbesluiten ervan bepaalde vereisten;

2° als elk signaal door de elektronische  registratievoorziening ontbreekt;

3° als hij het signaal ontvangt dat het ter beschikking  gestelde gegarandeerde betaalmiddel ontoereikend is  geworden.

Als de bestuurder niet de houder van het voertuig is, rust  op hem dezelfde verplichting als vermeld in het eerste  lid.

De dienstaanbieder en de hoofddienstaanbieder geeft,  waar nodig, instructies aan de bestuurder van het  voertuig, waarbij die laatste ertoe gehouden is die  instructies na te leven.

Voor de toepassing van dit artikel wordt verstaan onder  elektronische registratievoorziening : de elektronische  boordapparatuur bestemd voor de plaatsbepaling van het  voertuig waarin de boordapparatuur is geplaatst, die, al  dan niet met behulp van elektronische apparatuur op  afstand, data uitwisselt om te komen tot de registratie  van afgelegde kilometers, alsook tot de berekening van  de kilometerheffing op die geregistreerde afstand.

De Vlaamse Regering bepaalt de instructies, vermeld in  het derde lid.

---- historiek ----  ---- historique ----

- gewijzigd door art. 17 van het decreet van 03.05.2024  (B.S., 22.05.2024). Inwerkingtreding: 01.07.2025.

###### Art. 3.3.1.0.14.  Art. 3.3.1.0.14.

De belastingplichtige dient uiterlijk de voorlaatste  werkdag voor het begin van de verrichtingen voor spelen  en weddenschappen bij de bevoegde entiteit van de  Vlaamse administratie een voorafgaande aangifte in.

Als de spelen of de weddenschappen een voortdurend  karakter hebben, geldt de aangifte tot de intrekking  ervan.

De voorafgaande aangifte, vermeld in het eerste lid,  vermeldt:

1° hetzij het identificatienummer uit het Rijksregister  van  de  natuurlijke  personen,  hetzij  het  ondernemingsnummer  dat  bekend  is  bij  de  Kruispuntbank  van  Ondernemingen,  hetzij  het  identificatienummer, vermeld in artikel 8 van de wet van  15 januari 1990 houdende oprichting en organisatie van  een Kruispuntbank van de sociale zekerheid, van de  belastingplichtige;

2° de klasse van de kansspelinrichting, vermeld in artikel  6 van de Kansspelwet van 7 mei 1999, en het type en het  nummer van de vergunning, toegekend door de  Kansspelcommissie;

3° de naam van de plaats en het adres waar de spelen of  de weddenschappen worden georganiseerd;

4° de aard van de spelen of de weddenschappen;  4° la nature des jeux ou des paris ;

5° de periode waarin de spelen of de weddenschappen  worden georganiseerd.

De aangifteplicht die is bepaald in dit artikel geldt niet  voor  de  van  belasting  vrijgestelde  spelen  en  weddenschappen, vermeld in artikel 2.12.6.0.1.

---- historiek ----  ---- historique ----

- ingevoegd door art. 38 van het decreet van 07.12.2018  (B.S. 20.12.2018). Tekst in werking

getreden op 01.01.2019

###### Art. 3.3.1.0.15.  Art. 3.3.1.0.15.

Voor de toepassing van titel 2, hoofdstuk 12, dient de  belastingplichtige uiterlijk de vijfde werkdag van de  maand bij de bevoegde entiteit van de Vlaamse  administratie een aangifte in voor de verrichtingen die  gerealiseerd zijn in de vorige maand.

1° hetzij het identificatienummer uit het Rijksregister  van  de  natuurlijke  personen,  hetzij  het

1° soit le numéro d’identification du Registre national  des personnes physiques, soit le numéro d’entreprise  ondernemingsnummer  dat  bekend  is  bij  de  Kruispuntbank  van  Ondernemingen,  hetzij  het  identificatienummer, vermeld in artikel 8 van de wet van  15 januari 1990 houdende oprichting en organisatie van  een Kruispuntbank van de sociale zekerheid, van de  belastingplichtige;

2° de klasse van de kansspelinrichting, vermeld in artikel  6 van de Kansspelwet van 7 mei 1999, en het type en het  nummer van de vergunning, toegekend door de  Kansspelcommissie;

3° het belastbare bedrag van de verrichtingen volgens de  aard van de verrichting, vermeld in artikel 2.12.3.0.1;

4° de datum of periode van de verrichtingen;  4° la date ou la période des opérations ;

5° een samenvattende maandelijkse staat van de inzetten  ter verificatie van het belastbare bedrag.

De aangifteplicht die is bepaald in dit artikel geldt niet  voor  de  van  belasting  vrijgestelde  spelen  en  weddenschappen, vermeld in artikel 2.12.6.0.1.

---- historiek ----  ---- historique ----

- gewijzigd door art. 51 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- ingevoegd door art. 39 van het decreet van 07.12.2018  (B.S. 20.12.2018). Tekst in werking

getreden op 01.01.2019

###### Art. 3.3.1.0.16.  Art. 3.3.1.0.16.

De belastingplichtige dient uiterlijk de voorlaatste  werkdag voor de opstelling van het automatische  ontspanningstoestel, vermeld in artikel 2.13.1.0.1, een  aangifte in bij de bevoegde entiteit van de Vlaamse  administratie.

De aangifte, vermeld in het eerste lid, vermeldt:  La déclaration visée dans l’alinéa premier, mentionne :

1° hetzij het identificatienummer uit het Rijksregister  van  de  natuurlijke  personen,  hetzij  het  ondernemingsnummer  dat  bekend  is  bij  de  Kruispuntbank  van  Ondernemingen,  hetzij  het  identificatienummer, vermeld in artikel 8 van de wet van  15 januari 1990 houdende oprichting en organisatie van  een Kruispuntbank van de sociale zekerheid, van de  belastingplichtige;

2° voor elke plaats van opstelling:  2° pour chaque endroit d’installation :

b) de voornamen en de achternaam van de natuurlijke  persoon of de naam van de rechtspersoon van de  uitbater, vermeld in artikel 3.10.4.4.6;

b) les prénoms et le nom de la personne physique ou le  nom de la personne morale de l’exploitant, tel que visé à  l’article 3.10.4.4.6 ;  c) de klasse van de kansspelinrichting, vermeld in artikel  6 van de Kansspelwet van 7 mei 1999, en het type en het  nummer van de vergunning, toegekend door de  Kansspelcommissie;

d) het aantal toestellen per categorie als vermeld in  artikel 2.13.3.0.1, dat wordt opgesteld;

e) de periode van de opstelling per categorie als vermeld  in artikel 2.13.3.0.1.

De belastingplichtige geeft elke wijziging van de  elementen van de aangifte, vermeld in het tweede lid, 2°,  aan uiterlijk de voorlaatste werkdag voor hij de  wijzigingen in de opstelling doorvoert. In afwijking  daarvan wordt een wijziging van punt 2°, d) en e), alleen  doorgegeven als daardoor het bedrag van de belasting,  vermeld in artikel 2.13.4.0.1, eerste en tweede lid,  toeneemt.

Bij gebrek aan andersluidende kennisgeving is de  aangifte die ingediend is voor een kwartaal, geldig voor  de volgende kwartalen.

De aangifteplicht die is bepaald in dit artikel geldt niet  voor  de  opstelling  van  automatische  ontspanningstoestellen, vermeld in artikel 2.13.3.0.1, §  2, eerste lid, 4°.

---- historiek ----  ---- historique ----

- gewijzigd door art. 5 van het decreet van 25.11.2022  (B.S. 01.12.2022). Inwerkingtreding: 01.01.2023

- gewijzigd door art. 4 van het decreet van 20.11.2020  (B.S., 03.12.2020). Inwerkingtreding vanaf aanslagjaar  2021

- ingevoegd door art. 40 van het decreet van 07.12.2018  (B.S. 20.12.2018). Tekst in werking

getreden op 01.01.2019

#### Afdeling 2 - Aanslagjaar en belastbaar tijdperk  Section 2. - Année d'imposition et période imposable

###### Art. 3.3.2.0.1.  Art. 3.3.2.0.1.

Het aanslagjaar is voor :  L'année d'imposition a trait :

1° de onroerende voorheffing het kalenderjaar waarvan  de inkomsten de grondslag voor de belasting vormen;

3° de verkeersbelasting voor de voertuigen, vermeld in  artikel 2.2.2.0.1, § 2, tweede lid, de eerste keer het  tijdperk dat gelijk is aan het aantal maanden dat  begrepen is tussen de eerste dag van de maand waarin

3° à la taxe de circulation pour les véhicules, cités dans  l'article 2.2.2.0.1, § 2, alinéa deux, la première fois  pendant la période qui est égale aux nombre de mois  compris entre le premier jour du moins pendant lequel  het voertuig in de loop van een burgerlijk jaar in gebruik  is genomen op de openbare weg, en 31 december van  hetzelfde jaar. Vervolgens wordt het aanslagjaar  gevormd door een tijdperk van twaalf maanden dat  aanvangt op 1 januari van elk volgend kalenderjaar, en  het is het jaar waarin de voormelde tijdperken een  aanvang nemen;

4° de belasting op de inverkeerstelling het jaar waarin de  belasting verschuldigd is. Het begint op de eerste dag  van de maand waarin de belasting verschuldigd is;

5° (...)  5° (...) ;

6° de heffing ongeschikte en onbewoonbare woningen  het jaar waarin de belasting verschuldigd is met  toepassing van artikel 2.5.7.0.1;

7° de leegstandsheffing bedrijfsruimten het kalenderjaar  dat volgt op elke derde opeenvolgende registratie in de  inventaris, waarin de belasting kan worden ingevoerd;

8° de erfbelasting : het jaar waarin het overlijden  plaatsvindt of, in geval van een gebeurtenis als vermeld  in artikel 3.3.1.0.6, het jaar waarin de nieuwe  aangiftetermijn start;

9° de registratiebelasting :  9° aux impôt d'enregistrement :

a)  als  er  een  registratieverplichting  bestaat  overeenkomstig het federale Wetboek van Registratie-,  Hypotheek- en Griffierechten :

1) het jaar waarin de akte die of het geschrift dat  aanleiding  geeft  tot  de  heffing  van  de  registratiebelasting, binnen de ervoor bepaalde termijn,  overeenkomstig het federale Wetboek van Registratie-,  Hypotheek- en Griffierechten, ter registratie wordt  aangeboden;

2) het jaar waarin de termijn, vermeld in punt 1),  verstrijkt bij gebrek aan aanbieding ter registratie binnen  die termijn;

10° de kilometerheffing het kalenderjaar waarin de  belasting verschuldigd is. Het begint op de kalenderdag  waarop de kilometers worden afgelegd op de niet-  geconcedeerde weg.

10° en ce qui concerne le prélèvement kilométrique, à  l'année calendaire dans laquelle la taxe est due. Elle  débute au jour calendaire auquel les kilomètres sont  parcourus sur la route non concédée.  11° de belasting op de spelen en weddenschappen: het  jaar waarin de spelen en de weddenschappen die  aanleiding geven tot de belasting plaatsvinden;

12°  de  belasting  op  de  automatische  ontspanningstoestellen: het jaar waarin een automatisch  ontspanningstoestel is opgesteld.

Het belastbare tijdperk is voor :  La période imposable est :

1° de toepassing van de onroerende voorheffing gelijk  aan het aanslagjaar;

2° de verkeersbelasting voor de voertuigen, vermeld in  artikel 2.2.2.0.1, § 2, eerste lid, gelijk aan elke periode  van twaalf achtereenvolgende maanden, waarvan de  eerste ingaat de eerste dag van de maand waarin het  voertuig in het repertorium van het Directoraat-generaal  Mobiliteit en Verkeersveiligheid is ingeschreven of  moet worden ingeschreven;

3° de verkeersbelasting voor de voertuigen, vermeld in  artikel 2.2.2.0.1, § 2, tweede lid, voor de eerste keer  gelijk aan het aantal maanden dat begrepen is tussen de  eerste dag van de maand waarin het voertuig in de loop  van een burgerlijk jaar in gebruik is genomen op de  openbare weg, en 31 december van hetzelfde jaar.  Vervolgens is het gelijk aan elke periode van twaalf  maanden die aanvangt op 1 januari van elk volgend  kalenderjaar;

4° (...)  4° (...)

5° de heffing ongeschikte en onbewoonbare woningen  gelijk aan de opeenvolgende periodes van twaalf  maanden die volgen op de datum van de inventarisatie,  vermeld in artikel 3.20 van de Vlaamse Codex Wonen  van 2021;

6° de kilometerheffing gelijk aan de kalenderdag waarop  de  kilometers  worden  afgelegd  op  de  niet-  geconcedeerde weg.

7° de belasting op de spelen en weddenschappen gelijk  aan het aanslagjaar;

---- historiek ----  ---- historique ----

- gewijzigd door art. 5 van het decreet van 20.11.2020

(B.S., 03.12.2020). Inwerkingtreding vanaf aanslagjaar  2021

- gewijzigd door art. 46 van het besluit van 17.07.2020  (B.S. 17.11.2020). Tekst treedt in werking op 01.01.2021.  Bekrachtigd door art. 224, 2° van het decreet van  09.07.2021 (B.S., 10.09.2021). Inwerkingtreding:  20.09.2021.

- gewijzigd door art. 35 van het decreet van 29.03.2019  (B.S. 29.04.2019). Inwerkingtreding op 01.01.2021

- gewijzigd door art. 32 van het decreet van 21.12.2018  (B.S. 28.12.2018). Tekst treedt in werking op 07.01.2019

- gewijzigd door art. 41 van het decreet van 07.12.2018  (B.S.: 20.12.2018). Tekst treedt in werking op 01.01.2019

- gewijzigd door art. 46 en 49 van het decreet van  23.12.2016 (B.S.: 30.12.2016). Tekst in werking getreden  vanaf aanslagjaar 2017

- gewijzigd door art. 29 van het decreet van 3 juli 2015  (B.S., 10.08.2015). De tekst treedt in werking op 1 april  2016 (art. 44)

- eerste lid, 6° toegevoegd door art.14 van het decreet  van 19.12.2014 (B.S., 13.01.2015).De tekst is in werking  getreden op 1 januari 2015. (art. 24)

- eerste lid, 7° gewijzigd door art. 219 van het decreet  van 19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

- eerste lid, 8° en 9° toegevoegd door art. 220 van het  decreet van 19.12.2014 (B.S., 29.01.2015 - Ed. 2). De

tekst is in werking getreden op 1 januari 2015 (art. 325)

###### Art. 3.3.3.0.1.  Art. 3.3.3.0.1.

§ 1. Voor de onroerende voorheffing mag de belasting  of de aanvullende belasting worden geheven gedurende  vijf jaar vanaf 1 januari van het aanslagjaar waarvoor de  belasting is verschuldigd.

Die termijn wordt met vier jaar verlengd in geval van  inbreuk op de bepalingen van deze codex of van ter  uitvoering ervan genomen besluiten, gedaan met  bedrieglijk opzet of met het oogmerk te schaden.

§ 2. Voor de verkeersbelasting, de belasting op de  inverkeerstelling, de belasting op de spelen en  weddenschappen en de belasting op de automatische  ontspanningstoestellen  kan  de  belasting  of  de  aanvullende belasting worden geheven gedurende vijf  jaar vanaf de eerste dag van het aanslagjaar waarvoor ze  verschuldigd is.

Voor de kilometerheffing kan de belasting worden  geheven gedurende vijf jaar vanaf de kalenderdag  waarop de kilometers worden afgelegd op de niet-  geconcedeerde weg.

§ 3. Voor de leegstandsheffing bedrijfsruimten moet de  belasting geheven worden vóór 31 december van het  aanslagjaar.

§ 4. Voor de heffing ongeschikte en onbewoonbare  woningen kan de belasting worden geheven vanaf het  ogenblik waarop de periode van twaalf maanden,  vermeld in artikel 2.5.7.0.1, eerste lid, verstreken is, tot  uiterlijk de laatste dag van het kwartaal dat daarop volgt.

In het geval, vermeld in artikel 2.5.7.0.1, tweede lid, kan  de belasting worden geheven tot uiterlijk de laatste dag  van het kwartaal dat volgt op het verstrijken van de  nieuwe periode van twaalf maanden.

§ 4/1. De erfbelasting mag worden geheven gedurende  vijf jaar vanaf de dag waarop de aangiftetermijn,  vermeld in artikel 3.3.1.0.5, § 2, of artikel 3.3.1.0.6,  start.

In afwijking van het eerste lid kunnen de aanvullende  rechten die verschuldigd zijn wegens het niet-naleven  van  voorwaarden  die  gelden  tot  behoud  van  vrijstellingen of verminderingen van grondslagen of  tarieven, worden geheven gedurende vijf jaar vanaf de  dag waarop de vordering voor het Vlaamse Gewest is  ontstaan.

§ 4/2. De registratiebelasting mag worden geheven  gedurende vijf jaar vanaf de dag van de registratie van  de akte die of het geschrift dat aanleiding geeft tot de  heffing van de registratiebelasting.

Bij gebrek aan registratie mag de registratiebelasting  worden geheven gedurende vijf jaar vanaf de dag  waarop de termijn voor de aanbieding ter registratie,  overeenkomstig het federale Wetboek van Registratie-,  Hypotheek- en Griffierechten, verstrijkt.

In afwijking van het eerste lid kunnen de aanvullende  rechten die verschuldigd zijn wegens het niet-naleven  van  voorwaarden  die  gelden  tot  behoud  van  vrijstellingen of verminderingen van grondslagen of  tarieven, worden geheven gedurende vijf jaar vanaf de

dag waarop de vordering voor het Vlaamse Gewest is  ontstaan.

De termijnen uit het eerste, tweede en derde lid worden  met vier jaar verlengd in geval van inbreuk op de  bepalingen van deze codex of van ter uitvoering ervan  genomen besluiten, gedaan met bedrieglijk opzet of met  het oogmerk om te schaden.

§ 5. Als de belastingschuldige binnen de termijn of  datum, vermeld in paragraaf 1 tot en met 4/2, conform  artikel 3.5.2.0.1, 3.5.2.0.2, 3.5.2.0.4 en 3.5.3.0.1 tot en  met 3.5.3.0.3, een bezwaarschrift heeft ingediend, wordt  die termijn of datum verlengd met een tijdperk dat gelijk  is aan de tijd die is verlopen tussen de datum waarop het  bezwaarschrift is ingediend en de datum van de  beslissing van het bevoegde personeelslid, zonder dat  die verlenging meer dan zes maanden mag bedragen.

§ 6. Met behoud van de toepassing van de bepalingen,  vermeld in artikel 3.18.0.0.3, zijn de aanslagtermijnen,  vermeld in dit artikel, ook van toepassing op de  belastingverhogingen en de administratieve geldboetes.

---- historiek ----  ---- historique ----

- gewijzigd door art. 42 van het decreet van 07.12.2018  (B.S.: 20.12.2018). Tekst treedt in werking op 01.01.2019

- gewijzigd door art. 50 van het decreet van 23.12.2016  (B.S.: 30.12.2016). Tekst in werking getreden vanaf  aanslagjaar 2017

treedt in werking op 1 april 2016 (art. 44)

- § 4/1 en § 4/2 ingevoegd door art. 221 van het decreet  van 19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

- § 5 gewijzigd door art. 222 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 3.3.3.0.2.  Art. 3.3.3.0.2.

De belasting en de opcentiemen mogen worden geheven,  zelfs nadat de termijn, vermeld in artikel 3.3.3.0.1, § 1,  is verstreken, als bewijskrachtige gegevens uitwijzen dat  de belastingplichtige nagelaten heeft aangifte te doen  met toepassing van artikel 473 van het federale WIB 92.

In het geval, vermeld in het eerste lid, moeten de  belasting en de opcentiemen worden geheven binnen

Dans le cas, cité dans l'alinéa premier, la taxe et les  centimes additionnels doivent être levés dans les douze  twaalf maanden vanaf de datum waarop de inbreuk,  vermeld in het eerste lid, is vastgesteld.

###### Art. 3.3.3.0.3.  Art. 3.3.3.0.3.

§ 1. Als wordt vastgesteld dat de aangegeven waarde van  de aangegeven goederen voor de berekening van de  erfbelasting te laag is, wordt de belastingplichtige  schriftelijk in kennis gesteld van de intentie van de  bevoegde entiteit van de Vlaamse administratie om  aanvullende rechten en de belastingverhoging, vermeld  in artikel 3.18.0.0.8, eerste lid, te vestigen. Die  kennisgeving gebeurt binnen de 2 jaar na het indienen  van de aangifte, vermeld in artikel 3.3.1.0.5 en 3.3.1.0.6.

Als het verlaagde tarief, vermeld in artikel 2.7.4.2.2, is  toegepast om de erfbelasting te berekenen, gebeurt de  kennisgeving, vermeld in het eerste lid, binnen twee jaar  nadat de termijn, vermeld in artikel 2.7.4.2.4, § 1, eerste  lid, is verstreken.

Als wordt vastgesteld dat de waarde die aangegeven is  of de prijs die opgegeven is voor de berekening van de  registratiebelasting  te  laag  is,  wordt  de  belastingplichtige schriftelijk in kennis gesteld van de  intentie van de bevoegde entiteit van de Vlaamse  administratie  om  aanvullende  rechten  en  de  belastingverhoging, vermeld in artikel 3.18.0.0.13, te  vestigen. Die kennisgeving gebeurt binnen de 2 jaar  vanaf de dag van de registratie van de akte die of het  geschrift dat aanleiding geeft tot de heffing van de  registratiebelasting.

§ 2. De kennisgevingen, vermeld in paragraaf 1,  vermelden de redenen die de intentie van de bevoegde  entiteit van de Vlaamse administratie rechtvaardigen.

§ 3. De toepassing van paragraaf 1 heeft geen invloed op  de aanslagtermijnen, vermeld in artikel 3.3.3.0.1, § 4/1  en § 4/2.

---- historiek ----  ---- historique ----

- gewijzigd door art. 25 van het decreet van 09.12.2022  (B.S. 20.12.2022). Inwerkingtreding: 30.12.2022

- ingevoegd door art. 33 van het decreet van 21.12.2018  (B.S. 28.12.2018). Tekst treedt in werking op 07.01.2019

#### Afdeling 4 - Aanslagbiljet  Section 4 - Feuille d'imposition

###### Art. 3.3.4.0.1.  Art. 3.3.4.0.1.

Het aanslagbiljet vermeldt:  La feuille d'imposition mentionne :

1° de verzendingsdatum;  1° la date d'envoi ;

2° de datum van uitvoerbaarverklaring van het kohier;  2° la date de l'exequatur du rôle ;

3° het kohierartikel;  3° l'article du rôle ;

4° het aanslagjaar;  4° l'année d'imposition ;

5° de grondslag van de belasting;  5° la base de l'impôt ;  6° het te betalen bedrag;  6° le montant à payer ;

7° de uiterste betaaldatum;  7° la date limite de paiement ;

8° de termijn waarin de belastingschuldige bezwaar kan  indienen, de benaming en het adres van de entiteit van  de Vlaamse administratie die bevoegd is om het bezwaar  te ontvangen, en de formaliteiten die daarbij moeten  worden nageleefd.

#### Afdeling 5 - Verzending  Section 5 – Envoi

###### Art. 3.3.5.0.1.  Art. 3.3.5.0.1.

De aanslagbiljetten worden in gesloten omslag aan de  belastingschuldigen toegezonden.

De  Vlaamse  Regering  bepaalt  de  toepassingsmodaliteiten van de procedure, vermeld in  het tweede lid.

---- historiek ----  ---- historique ----

- gewijzigd door art. 26 van het decreet van 09.12.2022  (B.S., 20.12.2022). Inwerkingtreding: 30.12.2022

- gewijzigd door art. 52 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

###### Art. 3.3.5.0.2.  Art. 3.3.5.0.2.

Als artikel 2.5.7.0.2 of 2.5.7.0.3 van toepassing is, moet  het aanslagbiljet om geldig te zijn, verstuurd worden  tegen het einde van het kwartaal dat volgt op de  einddatum van de periode van opschorting.

Het eerste lid geldt voor de aanslagbiljetten die vanaf 5  augustus 2004 verstuurd worden.

### Hoofdstuk 4 - Betalingen  Chapitre 4 – Paiements

#### Afdeling 1 - Algemeen  Section 1re – Généralités

###### Art. 3.4.1.0.1.  Art. 3.4.1.0.1.

De Vlaamse Regering kan bepalen aan wie de  belastingen betaald moeten worden.

###### Art. 3.4.2.0.1.  Art. 3.4.2.0.1.

De belasting of de administratieve geldboete, vermeld in  artikel 3.18.0.0.1, moet uiterlijk binnen een termijn van  twee maanden vanaf de verzendingsdatum, vermeld op  het aanslagbiljet, betaald worden op de rekening van de  bevoegde entiteit van de Vlaamse administratie.

L'impôt ou l’amende administrative, visée à l’article  3.18.0.0.1, doit être payé au plus tard dans un délai de  deux mois à partir de la date d'envoi, citée sur la feuille  d'imposition adressée, sur le compte de l'entité  compétente de l'administration flamande.  In het geval, vermeld in artikel 3.3.5.0.1, tweede lid,  waarbij het aanslagbiljet door middel van een procedure  waarbij informaticatechnieken worden gebruikt, aan de  belastingschuldige is bezorgd, moet de belasting worden  betaald binnen twee maanden na de verzendingsdatum,  vermeld op het aanslagbiljet.

---- historiek ----  ---- historique ----

- gewijzigd door art. 51 van het decreet van 23.12.2016  (B.S.: 30.12.2016). Tekst in werking getreden op 8  januari 2017

- gewijzigd door art. 15 van het decreet van 19.12.2014  (B.S., 13.01.2015). De tekst is in werking getreden op  01.01.2015. (art. 24)

###### Art. 3.4.2.0.2.  Art. 3.4.2.0.2.

(…)  (…)

---- historiek ----  ---- historique ----

- opgeheven door art. 34 van het decreet van 21.12.2018  (B.S. 28.12.2018). Tekst treedt in werking op 07.01.2019

###### Art. 3.4.2.0.3.  Art. 3.4.2.0.3.

Het indienen van een bezwaar, een aanvraag tot  ambtshalve ontheffing, een vordering in rechte of een  verzoek om spreiding van betaling schort de verplichting  tot betaling van de belastingen en toebehoren niet op.

###### Art. 3.4.2.0.4.  Art. 3.4.2.0.4.

In afwijking van artikel 3.4.2.0.1 moeten alle  belastingen en toebehoren onverwijld worden betaald  als de rechten van het Vlaamse Gewest in het gedrang  komen. Als de belastingschuldige betwist dat de rechten  van het Vlaamse Gewest in gevaar verkeren, wordt er  over de betwisting uitspraak gedaan, zoals in kort  geding, door de beslagrechter van de plaats waar de  bevoegde entiteit van de Vlaamse administratie die de  belasting moet innen, is gevestigd.

In  afwijking  van  artikel  3.4.2.0.1  moet  de  belastingschuldige de registratiebelasting onmiddellijk  na de bezorging van het aanslagbiljet betalen.

Het eerste lid is niet van toepassing op de aanvullende  rechten op het verkooprecht, vermeld in artikel 2.9.4.2.3,  tweede lid, artikel 2.9.4.2.11, § 2, tweede lid, of § 3,  tweede lid, artikel 2.9.4.2.12, § 1, tweede lid, vierde lid,  of § 2, tweede lid, artikel 2.9.4.2.13, § 1, tweede lid,  artikel 2.9.4.2.14, § 5, tweede lid, of § 7, en artikel  2.9.5.0.3, tweede lid, en de daaraan verbonden  belastingverhogingen, vermeld in artikel 3.18.0.0.11 en  artikel 3.18.0.0.12.

---- historiek ----  ---- historique ----

- gewijzigd door art. 6 van het decreet van 19.11.2021  (B.S. 16.12.2021). Inwerkingtreding: 01.01.2022

- gewijzigd door art. 35 van het decreet van 21.12.2018  (B.S. 28.12.2018). De tekst is van toepassing op  verkoopovereenkomsten afgesloten vanaf 1 juni 2018

(art 17).

- gewijzigd door art. 12 van het decreet van 18.05.2018  (B.S.: 28.05.2018). Tekst is van toepassing op  verkoopovereenkomsten afgesloten vanaf 1 juni 2018

- aangevuld door art. 24 van het decreet van 08.12.2017  (B.S., 14.12.2017). De tekst is in werking getreden op  24.12.2017

- toegevoegd door art. 223 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

#### Afdeling 3 - Wijze van betaling  Section 3 - Mode de paiement

###### Art. 3.4.3.0.1.  Art. 3.4.3.0.1.

De Vlaamse Regering kan de regels bepalen voor de  wijze van betaling van de belastingen.

###### Art. 3.4.3.0.2.  Art. 3.4.3.0.2.

§ 1. Iedere erfgenaam, legataris of begiftigde kan  verzoeken  de  erfbelasting  en  toebehoren  die  invorderbaar zijn op grond van een nalatenschap, geheel  of gedeeltelijk te betalen door de afgifte van de  geheelheid  volle  eigendom  van  de  volgende  cultuurgoederen :

2° de cultuurgoederen, vermeld in artikel 2, 9°, van het  decreet van 24 januari 2003 houdende bescherming van  het roerend cultureel erfgoed van uitzonderlijk belang,  die een bijzondere verrijking kunnen betekenen voor de  collectie  van  collectiebeherende  cultureelerfgoedorganisaties die aangewezen zijn als  cultureelerfgoedinstellingen met toepassing van artikel  17 van het Cultureelerfgoeddecreet van 23 december  2021, en die daarom als sleutelwerken voor die  collecties beschouwd moeten worden;

3° de cultuurgoederen, vermeld in artikel 2, 9°, van het  decreet van 24 januari 2003 houdende bescherming van  het roerend cultureel erfgoed van uitzonderlijk belang,  die een bijzondere verrijking kunnen betekenen voor de  collectie  van  collectiebeherende  cultureelerfgoedorganisaties die met een kwaliteitslabel  ingedeeld zijn bij het landelijke niveau met toepassing  van artikel 24 van het Cultureelerfgoeddecreet van 23  december 2021, en die daarom als sleutelwerken voor  die collecties beschouwd moeten worden;

4° de cultuurgoederen, vermeld in artikel 2, 9°, van het  decreet van 24 januari 2003 houdende bescherming van  het roerend cultureel erfgoed van uitzonderlijk belang,  die een bijzondere verrijking kunnen betekenen voor de  collectie  van  universiteitsarchieven  en  universiteitsbibliotheken die een kwaliteitslabel hebben  met  toepassing  van  artikel  7  van  het  Cultureelerfgoeddecreet van 23 december 2021, en die  daarom als sleutelwerken voor die collecties beschouwd  moeten worden.

Alleen de cultuurgoederen, vermeld in het eerste lid, die  op de dag van het overlijden in hun geheel in volle  eigendom toebehoren aan de overledene en/of aan zijn  langstlevende  echtgenoot  of  zijn  wettelijk  samenwonende partner en/of aan zijn erfgenamen,  legatarissen of begiftigden, kunnen als betaling als  vermeld in het eerste lid worden aangeboden. Het bewijs  dat de voormelde voorwaarde is vervuld, kan worden  geleverd door alle bewijsmiddelen, met uitsluiting van  de eed.

§ 2. De bevoegde entiteit van de Vlaamse administratie  onderzoekt de ontvankelijkheid van het verzoek tot  inbetalinggeving en brengt de aanvrager op de hoogte

§ 3. Als het verzoek tot inbetalinggeving, vermeld in  paragraaf 1, ontvankelijk is verklaard, bezorgt de  bevoegde entiteit van de Vlaamse administratie het  verzoek aan de Raad, vermeld in artikel 2, 4°, van het  decreet van 24 januari 2003 houdende bescherming van  het roerend cultureel erfgoed van uitzonderlijk belang,  met het oog op een beslissing van de Vlaamse Regering  conform artikel 18ter van het voormelde decreet.

§ 4. Als de Vlaamse Regering conform artikel 18ter van  het decreet van 24 januari 2003 houdende bescherming  van het roerend cultureel erfgoed van uitzonderlijk  belang beslist dat de cultuurgoederen die het voorwerp  uitmaken van het verzoek, in betaling mogen worden  gegeven, worden de cultuurgoederen geacht voor 120  procent van de waarde die is vastgesteld in de beslissing  van de Vlaamse Regering, in betaling te zijn gegeven om  de verschuldigde erfbelasting en toebehoren te voldoen.

De aanvrager wordt op de hoogte gebracht van de  beslissing van de Vlaamse Regering over het verzoek.

De waarde die conform artikel 18ter, derde of vijfde lid,  van het voormelde decreet is vastgesteld bij een  beslissing van de Vlaamse Regering, neemt de bevoegde  entiteit van de Vlaamse administratie in aanmerking om  de erfbelasting en toebehoren te berekenen als het  cultuurgoed deel uitmaakt van de nalatenschap.

In het geval, vermeld in het derde lid, behoudt de  aanvrager de mogelijkheid om conform artikel 3.5.3.0.1  een bezwaar in te dienen tegen de gevestigde aanslag,  behalve voor de waardering van het cultuurgoed, zoals  die is vastgesteld bij een beslissing van de Vlaamse  Regering.

§ 5. De aanvragers kunnen aan de bevoegde entiteit van  de Vlaamse administratie meedelen dat ze hun verzoek  tot inbetalinggeving volledig of gedeeltelijk intrekken.  Bij intrekking van het verzoek tot inbetalinggeving dient  de erfgenaam, legataris of begiftigde, vermeld in  paragraaf  1,  binnen  twee  maanden  vanaf  de  kennisgeving van de intrekking een aanvullende  aangifte in bij de bevoegde entiteit van de Vlaamse  administratie als het cultuurgoed deel uitmaakt van de  nalatenschap, behalve als de waarde is bepaald bij een  beslissing van de Vlaamse Regering conform artikel  18ter, derde of vijfde lid, van het decreet van 24 januari  2003 houdende bescherming van het roerend cultureel

§ 6. Als de Vlaamse Regering binnen vijf maanden na de  kennisgeving van het verzoek door de bevoegde entiteit  van de Vlaamse administratie aan de Raad geen  beslissing heeft genomen, wordt het verzoek tot  inbetalinggeving geacht te zijn afgewezen. Als het  cultuurgoed deel uitmaakt van de nalatenschap, dient de  erfgenaam, legataris of begiftigde, vermeld in paragraaf  1, binnen twee maanden na de kennisgeving van het  verstrijken van voormelde termijn van vijf maanden, een  aanvullende aangifte in bij de bevoegde entiteit van de  Vlaamse administratie.

§ 6. Si le Gouvernement flamand n'a pas pris de  décision dans un délai de cinq mois à compter de la  notification de la demande par l'entité compétente  de l'administration flamande au Conseil, la demande  de dation en paiement est réputée rejetée. Si le bien  culturel fait partie de la succession, l'héritier, le  légataire ou le donataire visé au paragraphe 1  introduit une déclaration complémentaire à l'entité  compétente de l'administration flamande dans un  délai précité de deux mois à compter de la  notification de l'expiration du délai de cinq mois.  Als de Vlaamse Regering het verzoek tot  inbetalinggeving weigert, wordt de aanvullende aangifte,  vermeld in het eerste lid, ingediend binnen twee  maanden vanaf de kennisgeving van de beslissing van de  Vlaamse Regering.

Si le Gouvernement flamand refuse la demande de dation  en paiement, la déclaration complémentaire visée à  l'alinéa 1er doit être présentée dans un délai de deux mois  à compter de la notification de la décision du  Gouvernement flamand.  § 7. De Vlaamse Regering kan nadere regels vaststellen  over de wijze en het tijdstip waarop het verzoek moet  worden ingediend, en kan bepalen welke gegevens en  documenten de aanvraag moet bevatten. De Vlaamse  Regering kan de procedure voor de afhandeling of  intrekking van het verzoek nader bepalen.

---- historiek ----  ---- historique ----

- vervangen door art. 8 van het decreet van 10.03.2023  (B.S., 23.03.2023). Inwerkingtreding op een datum die de  Vlaamse Regering vaststelt en uiterlijk op 01.07.2023

- toegevoegd door art. 224 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

- modifié par art. 224 du décret du 19.12.2014 (M.B.,  29.01.2015, Ed. 2, erratum M.B., 04.03.2015)

#### Afdeling 4 - Vermeldingen op het betaalformulier  Section 4 - Mentions sur le formulaire de paiement

###### Art. 3.4.4.0.1.  Art. 3.4.4.0.1.

De Vlaamse Regering kan de regels bepalen voor de  vermeldingen op het betaalformulier.

#### Afdeling 5 - Bewijs van betaling  Section 5 - Preuve de paiement

###### Art. 3.4.5.0.1.  Art. 3.4.5.0.1.

De Vlaamse Regering kan de regels bepalen voor het  bewijs van betaling.

###### Art. 3.4.6.0.1.  Art. 3.4.6.0.1.

De Vlaamse Regering kan de regels bepalen voor de  datum waarop de betaling uitwerking heeft.

#### Afdeling 7 - Wijze van aanrekening van betaling,

aanwending en aanzuivering

###### Art. 3.4.7.0.1.  Art. 3.4.7.0.1.

§ 1. De belastingschuldige die een of meer belastingen  en toebehoren te betalen heeft, moet bij elke betaling  vermelden wat hij wil vereffenen.

Als een dergelijke vermelding ontbreekt, worden de  betalingen aangerekend naar keuze van het bevoegde  personeelslid, met behoud van de toepassing van  paragraaf 2. Dat geldt ook als een som wordt aangewend  met toepassing van artikel 3.4.7.0.2.

§ 2. Betalingen, teruggaven en moratoriuminteresten  worden per afzonderlijke aanslag in de volgende  volgorde aangerekend:

1° op de kosten van alle aard, ook als ze op verschillende  aanslagen betrekking hebben;

2° op de nalatigheidsinteresten;  2° aux intérêts de retard ;  3°  op  de  administratieve  geldboetes  en  belastingverhogingen;

4° op de verschuldigde belasting en de opcentiemen of  de opdeciem.

###### Art. 3.4.7.0.2.  Art. 3.4.7.0.2.

§ 1. De bepalingen van artikel 5.182 en boek 5, titel 3,  ondertitel 8, hoofdstuk 4, van het Burgerlijk Wetboek  zijn inzake de belastingen, vermeld in deze codex, niet  van toepassing.

§ 2. Elke som die aan een persoon moet worden  teruggegeven of betaald, hetzij in het kader van de  toepassing van deze codex, hetzij krachtens de  bepalingen van het burgerlijk recht met betrekking tot de  onverschuldigde betaling, kan naar keuze en zonder  formaliteit door het bevoegde personeelslid worden  aangewend ter betaling van de door hem verschuldigde  bedragen bij de toepassing van deze codex of ter  voldoening van de niet-fiscale schuldvorderingen  waarvan de inning en invordering, door of krachtens een  bepaling met kracht van wet door de bevoegde entiteit  van de Vlaamse administratie worden verzekerd.

§ 3. De aanwending met toepassing van paragraaf 2 kan  voor betwiste aanslagen verricht worden als bewarende  maatregel als vermeld in artikel 3.10.4.6.1.

§ 4. Met behoud van de toepassing van paragraaf 2,  eerste lid, kan het bevoegde personeelslid elke som die  aan een persoon moet worden teruggegeven inzake de  erfbelasting, ook zonder formaliteit aanwenden ter  betaling van openstaande bedragen die op grond van een  andere oorzaak verschuldigd zijn met betrekking tot  dezelfde nalatenschap.

---- historiek ----  ---- historique ----

- gewijzigd door art. 11 van het decreet van 15.03.2024  (B.S. 20.03.2024). Inwerkingtreding: 30.03.2024

- § 4 toegevoegd door art. 225 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 3.4.7.0.3.  Art. 3.4.7.0.3.

Als een voertuig in de loop van een aanslagjaar wordt  afgevoerd van het repertorium van het Directoraat-  generaal Mobiliteit en Verkeersveiligheid of een  vrijstelling geniet, wordt de betaalde verkeersbelasting  teruggegeven in verhouding tot de niet-verstreken  maanden of, in dezelfde mate, aangerekend op de  belasting die door de belastingschuldige voor een ander  voertuig is verschuldigd.

###### Art. 3.4.7.0.4.  Art. 3.4.7.0.4.

(…)  (…)

---- historiek ----  ---- historique ----

- opgeheven door art. 36 van het decreet van 21.12.2018  (B.S. 28.12.2018). Tekst treedt in werking op 01.01.2021

###### Art. 3.4.7.0.5.  Art. 3.4.7.0.5.

(…)  (…)

---- historiek ----  ---- historique ----

- opgeheven door art. 37 van het decreet van 21.12.2018  (B.S. 28.12.2018). Tekst treedt in werking op 07.01.2019

Inzake de registratiebelasting worden de aanvullende  rechten die ingevolge een tekortschatting of om een  andere reden betaald zijn, aangerekend op de  aanvullende rechten die ingevolge prijsbewimpeling  verschuldigd zijn.

---- historiek ----  ---- historique ----

- toegevoegd door art. 226 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 3.4.7.0.7.  Art. 3.4.7.0.7.

(…)  (…)

---- historiek ----  ---- historique ----

- opgeheven door art. 6 van het decreet van 20.11.2020  (B.S., 03.12.2020). Inwerkingtreding vanaf aanslagjaar  2021

- ingevoegd door art. 43 van het decreet van 07.12.2018  (B.S. 20.12.2018). Tekst in werking

getreden op 01.01.2019

#### Afdeling 8 - Betalingsfaciliteiten  Section 8 - Facilités de paiement

###### Art. 3.4.8.0.1.  Art. 3.4.8.0.1.

§ 1. De belastingschuldige kan verzoeken om spreiding  van betaling van de belastingen en toebehoren.

Het verzoek tot spreiding van betaling, vermeld in het  eerste lid, moet worden gemotiveerd en moet

La demande d'étalement de paiement, visé à l'alinéa  premier, doit être motivée et doit contenir des éléments  bewijskrachtige elementen bevatten met betrekking tot  de financiële toestand van de verzoeker.

Het bevoegde personeelslid kan het verzoek inwilligen.  Le membre du personnel compétent peut satisfaire à la  demande.

---- historiek ----  ---- historique ----

- §2 opgeheven door art. 38 van het decreet van  21.12.2018 (B.S. 28.12.2018). Tekst treedt in werking op  07.01.2019

#### Afdeling 1 - Ontvangstmelding  Section 1re - Notification de réception

###### Art. 3.5.1.0.1.  Art. 3.5.1.0.1.

Aan de indieners van de bezwaarschriften en de  aanvragen tot ambtshalve ontheffing wordt een  ontvangstmelding bezorgd die de datum van ontvangst  van het administratief beroep vermeldt.

#### Afdeling 2 - Bezwaartermijn  Section 2 - Délai de réclamation

###### Art. 3.5.2.0.1.  Art. 3.5.2.0.1.

De bezwaarschriften moeten worden gemotiveerd en op  straffe van verval worden ingediend binnen een termijn  van drie maanden na de derde werkdag die volgt op de  verzendingsdatum, vermeld op het aanslagbiljet.

(…)  (…)

Als het bezwaarschrift wordt ingediend met een  aangetekende brief, geldt de datum van de poststempel  op het verzendingsbewijs als datum van de indiening.

---- historiek ----  ---- historique ----

- gewijzigd door art. 19 van het decreet van 03.04.2026  (B.S. 23.04.2026). Inwerkingtreding op 03.05.2026

- tweede lid gewijzigd door art. 16 van het decreet van  19.12.2014 (B.S., 13.01.2015). De tekst is in werking  getreden op 01.01.2015. (art. 24)

- derde lid toegevoegd door art. 16 van het decreet van  19.12.2014 (B.S., 13.01.2015). De tekst is in werking  getreden op 01.01.2015. (art. 24)

###### Art. 3.5.2.0.2.  Art. 3.5.2.0.2.

Zolang er geen beslissing is gevallen, mag de  belastingschuldige zijn oorspronkelijke bezwaarschrift  aanvullen met nieuwe, schriftelijk geformuleerde  bezwaren, zelfs als die buiten de termijn, vermeld in  artikel 3.5.2.0.1, worden ingediend.

Als een aanvullende aanslag voor een bepaald  aanslagjaar gevestigd wordt met toepassing van artikel  3.3.3.0.1 en de nieuwe aanslag op naam van dezelfde  belastingplichtige voor een of meer aanslagjaren een  door de aanvullende belasting veroorzaakte overmatige  belasting doet ontstaan, kan de belastingschuldige  binnen een termijn van drie maanden vanaf de derde  werkdag die volgt op de verzendingsdatum, vermeld op  het aanslagbiljet dat de aanvullende aanslag omvat, een  bezwaarschrift indienen tegen de voormelde overmatige  belasting.

In het geval, vermeld in artikel 3.3.5.0.1, tweede lid,  waarbij het aanslagbiljet door middel van een procedure  waarbij informaticatechnieken worden gebruikt, aan de  belastingplichtige is bezorgd, vangt de termijn aan vanaf  de verzendingsdatum, vermeld op het aanslagbiljet dat  de aanvullende aanslag omvat.

###### Art. 3.5.2.0.4.  Art. 3.5.2.0.4.

Vanaf het aanslagjaar 2008 kan de termijn, vermeld in  artikel 3.5.2.0.1, niet verstrijken voor 31 maart van het  jaar dat volgt op het aanslagjaar, als met het  bezwaarschrift de vermindering met toepassing van  artikel 2.1.5.0.2, § 1, 3°, wordt ingeroepen.

###### Art. 3.5.2.0.5.  Art. 3.5.2.0.5.

De termijn, vermeld in artikel 3.5.2.0.1, is voor de  leegstandsheffing bedrijfsruimten ook van toepassing in  geval van opschorting van de belasting als vermeld in  artikel 2.6.7.1.1, 2.6.7.2.1, 2.6.7.3.1, 2.6.7.4.1, 2.6.7.5.1  en 2.6.7.6.1. De persoon op naam van wie de belasting  in het kohier is ingeschreven, kan echter alsnog om  ontheffing verzoeken op basis van middelen die geen  betrekking hebben op de vestiging van de belasting zelf  en op basis van feiten die zich hebben afgespeeld  gedurende de opschorting van de belasting en waarvan  die persoon in het kader van de procedure, vermeld in  artikel 3.5.2.0.1, geen kennis kon hebben.

Het verzoek, vermeld in het eerste lid, moet op straffe  van verval bij het bevoegde personeelslid schriftelijk  ingediend worden binnen een termijn van drie maanden  vanaf de derde werkdag die volgt op de datum waarop  de opschorting vervalt.

kunnen indienen

###### Art. 3.5.3.0.1.  Art. 3.5.3.0.1.

De belastingschuldige kan tegen het bedrag van de  gevestigde aanslag, opcentiemen en de opdeciem,  verhogingen en boeten inbegrepen, schriftelijk bezwaar  indienen bij de bevoegde personeelsleden.

De bezwaarindiener voegt bij het bezwaarschrift de  nodige bewijskrachtige stukken om zijn bezwaar te  staven.

###### Art. 3.5.3.0.2.  Art. 3.5.3.0.2.

De belastingschuldige die om om het even welke  vrijstelling of vermindering verzoekt, kan er alleen het  voordeel van verkrijgen of behouden als hij zijn recht op  die vrijstelling of vermindering bewijst.

De belastingschuldige moet het bevoegde personeelslid  onmiddellijk op de hoogte brengen als niet langer aan de  voorwaarden van de vrijstelling is voldaan.

---- historiek ----  ---- historique ----

- tweede lid toegevoegd door art. 31 van het decreet van  3 juli 2015 (B.S., 10.08.2015). De tekst treedt in werking  op 1 april 2016 (art. 44)

###### Art. 3.5.3.0.3.  Art. 3.5.3.0.3.

De bepalingen van artikel 3.5.2.0.1, 3.5.2.0.2 en  3.5.3.0.1 zijn ook van toepassing op aanvragen tot  kwijtschelding of vermindering van de onroerende  voorheffing in de gevallen, vermeld in artikel 2.1.5.0.1  en 2.1.5.0.2.

###### Art. 3.5.3.0.4.  Art. 3.5.3.0.4.

Als de belastingschuldige beroep kon aantekenen met  toepassing van artikel 3.21 van de Vlaamse Codex  Wonen van 2021, of beroep kon aantekenen met  toepassing van artikel 7 van het decreet van 19 april  1995, kan hij bij zijn bezwaar tegen de belasting de  opname in de inventaris niet meer betwisten.

---- historiek ----  ---- historique ----

- gewijzigd door art. 47 van het besluit van 17.07.2020  (B.S. 17.11.2020). Tekst treedt in werking op 01.01.2021.  Bekrachtigd door art. 224, 2° van het decreet van  09.07.2021 (B.S., 10.09.2021). Inwerkingtreding:  20.09.2021.

- gewijzigd door art. 25 van het decreet van 08.12.2017  (B.S.: 14.12.2017). Tekst van toepassing vanaf  24.12.2017

#### Afdeling 4 - Onderzoeksbevoegdheden  Section 4 - Compétences d'enquête

###### Art. 3.5.4.0.1.  Art. 3.5.4.0.1.

Om de behandeling van het bezwaarschrift te verzekeren  beschikt  elk  bevoegde  personeelslid  over  de  bewijsmiddelen en de bevoegdheden die aan de  administratie verleend zijn met toepassing van artikel  3.13.1.1.1, 3.13.1.1.2, 3.13.1.1.3, 3.13.1.2.1 tot en met  3.13.1.2.5, 3.13.1.3.1 tot en met 3.13.1.3.6, 3.13.1.4.1,  3.13.1.4.2, 3.17.0.0.1 en 3.19.0.0.1.

Bovendien kan hij, in het kader van dat bezwaarschrift,  van de kredietinstellingen die onderworpen zijn aan de  wet van 25 april 2014 op het statuut van en het toezicht  op kredietinstellingen en beursvennootschappen, alle  inlichtingen vorderen waarvan ze kennis hebben en die  nuttig kunnen zijn.

---- historiek ----  ---- historique ----

- gewijzigd door art. 53 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

###### Art. 3.5.4.0.2.  Art. 3.5.4.0.2.

Op verzoek van de bevoegde entiteit van de Vlaamse  administratie zal er een protocol over de advisering bij  de behandeling van ingediende bezwaren worden  gesloten met de andere entiteiten van de Vlaamse  administratie die bevoegd zijn voor een van de gegevens  die noodzakelijk zijn om de belastingen, vermeld in deze  codex, te bepalen.

#### Afdeling 5 - Behandeltijd  Section 5 - Temps imparti au traitement

###### Art. 3.5.5.0.1.  Art. 3.5.5.0.1.

Voorbehouden voor toekomstig gebruik.  Réservé pour un usage futur

###### Art. 3.5.6.0.1.  Art. 3.5.6.0.1.

Het bevoegde personeelslid doet, als administratieve  overheid, uitspraak bij een met redenen omklede  beslissing over de bezwaren die aangevoerd worden  door de belastingschuldige.

Het is het personeelslid, vermeld in het eerste lid, niet  toegelaten bij zijn beslissing een aanvullende aanslag te  vestigen, noch de compensatie te verwezenlijken tussen  een  rechtmatig  bevonden  ontheffing  en  een  ontoereikendheid van aanslag die zou zijn vastgesteld.

#### Afdeling 7 - Collectieve beslissing  Section 7 - Décision collective

###### Art. 3.5.7.0.1.  Art. 3.5.7.0.1.

Voorbehouden voor toekomstig gebruik.  Réservé pour un usage futur

#### Afdeling 8 - Hoorzitting  Section 8 – Audition

###### Art. 3.5.8.0.1.  Art. 3.5.8.0.1.

Als de bezwaarindiener dat in zijn bezwaarschrift heeft  gevraagd, zal hij worden uitgenodigd om gehoord te  worden voor de bezwaarbeslissing wordt genomen.

#### Afdeling 9 - Kennisgeving  Section 9 – Notification

###### Art. 3.5.9.0.1.  Art. 3.5.9.0.1.

De beslissing wordt schriftelijk meegedeeld en ze  vermeldt de wijze waarop ertegen in rechte kan worden  getreden. De beslissing is onherroepelijk als geen  vordering is ingesteld bij de rechtbank van eerste aanleg  binnen de termijn, vermeld in artikel 1385undecies van  het Gerechtelijk Wetboek.

### Hoofdstuk 6 - Ambtshalve ontheffing  Chapitre 6 - Exonération d'office

###### Art. 3.6.0.0.1.  Art. 3.6.0.0.1.

Het bevoegde personeelslid verleent in afwijking van  artikel 3.5.9.0.1 ambtshalve ontheffing van de  overmatige belastingen die voortvloeien uit materiële  vergissingen, uit dubbele belasting, alsook van die welke  blijken uit afdoende bevonden nieuwe bescheiden of  feiten waarvan het laattijdig overleggen of inroepen door  de  belastingschuldige  wordt  verantwoord  door  gewettigde redenen en op voorwaarde dat:

1° die overmatige belastingen door de administratie zijn  vastgesteld of door de belastingschuldige aan de  administratie zijn bekendgemaakt binnen vijf jaar vanaf  1 januari van het jaar waarin de belasting is gevestigd;

Het bevoegde personeelslid verleent ook ambtshalve  ontheffing van de verminderingen en vrijstellingen met  toepassing van artikel 2.1.6.0.2, eerste lid, en artikel  2.1.5.0.1, § 1, § 1/1, en § 2, eerste lid, en artikel  2.1.5.0.2, § 1, 1°, 2° en 4°, en artikel 2.1.6.0.3, als het  feit dat aanleiding geeft tot die verminderingen of  vrijstellingen, door de administratie is vastgesteld of  door de belastingschuldige aan de administratie is  bekendgemaakt binnen vijf jaar vanaf 1 januari van het  aanslagjaar waartoe de belasting behoort waarop die  verminderingen moeten worden verleend.

---- historiek ----  ---- historique ----

- gewijzigd door art. 20 van het decreet van 03.04.2026  (B.S. 23.04.2026). Inwerkingtreding op 03.05.2026

- gewijzigd door art. 27 van het decreet van 09.12.2022  (B.S. 20.12.2022). Inwerkingtreding: 30.12.2022

###### Art. 3.6.0.0.2.  Art. 3.6.0.0.2.

Het bevoegde personeelslid doet bij met redenen  omklede beslissing uitspraak over het verzoek dat  ingediend is door de belastingschuldige.

###### Art. 3.6.0.0.3.  Art. 3.6.0.0.3.

De beslissing wordt schriftelijk meegedeeld en ze  vermeldt de wijze waarop ertegen in rechte kan worden  getreden. De beslissing is onherroepelijk als geen  vordering is ingesteld bij de rechtbank van eerste aanleg  binnen de termijn, vermeld in artikel 1385undecies van  het Gerechtelijk Wetboek.

###### Art. 3.6.0.0.4.  Art. 3.6.0.0.4.

Wat de erfbelasting betreft, verleent het bevoegde  personeelslid ook ontheffing van de erfbelasting in de  volgende gevallen op voorwaarde dat een aangifte is  ingediend binnen een termijn van vijf jaar vanaf 1  januari van het jaar waarin het recht tot teruggave is  ontstaan, die het hierna vermelde feit aanduidt :

1° wanneer, na het openvallen van de nalatenschap, de  actieve samenstelling ervan verminderd wordt, hetzij  door :

a) het intreden van een voorwaarde of van elk ander  voorval;

b) de oplossing van een geschil ingevolge een in kracht  van gewijsde gegaan vonnis of een transactie.

2° wanneer een verandering in de devolutie van de  nalatenschap ontstaat waardoor het aanvankelijk  berekende bedrag kan worden verminderd;

3° wanneer in de gevallen, vermeld in artikel 2.7.4.1.2,  de belanghebbende de werkelijke toestand aantoont,  waardoor het aanvankelijk berekende bedrag kan  worden verminderd.

4° wanneer aan de voorwaarde van artikel 2.7.6.0.5, § 2,  tweede lid, wordt voldaan.

4° lorsque la condition de l’article 2.7.6.0.5, § 2, alinéa  deux, est remplie.  De bepalingen van artikel 3.6.0.0.2 en 3.6.0.0.3 zijn  onverminderd van toepassing op dit artikel.

---- historiek ----  ---- historique ----

- gewijzigd door art. 19 van het decreet van 22.12.2017  (B.S. 21.02.2018) Tekst treedt in werking op 09.06.2018  (art. 1 besluit 04.05.2018 B.S. 30.05.2018)

- toegevoegd door art. 227 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 3.6.0.0.5.  Art. 3.6.0.0.5.

Als de erfbelasting en toebehoren zijn betaald met  cultuurgoederen ingevolge de toepassing van artikel  3.4.3.0.2, kan de terugbetaling die voortvloeit uit de  toepassing van artikel 3.6.0.0.1 of 3.6.0.0.4, alleen in  geld gedaan worden.

---- historiek ----  ---- historique ----

- gewijzigd door art. 9 van het decreet van 10.03.2023  (B.S., 23.03.2023). Inwerkingtreding op een datum die de  Vlaamse Regering vaststelt en uiterlijk op 01.07.2023

- toegevoegd door art. 228 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 3.6.0.0.6.  Art. 3.6.0.0.6.

§ 1. Wat de registratiebelasting betreft, verleent het  bevoegde personeelslid ook ontheffing van de  registratiebelasting in de volgende gevallen op  voorwaarde dat een verzoek is ingediend binnen een  termijn van vijf jaar vanaf 1 januari van het jaar waarin  het recht tot teruggave is ontstaan, dat het hierna  vermelde feit aanduidt :

2° wanneer alle partijen die betrokken zijn bij een  overeenkomst waarop het verkooprecht van toepassing  is, verklaren deze overeenkomst in der minne te hebben  ontbonden of te hebben vernietigd, of verklaren dat een  voorwaarde die uitdrukkelijk bedongen is in de  overeenkomst, al is vervuld. Die verklaring moet blijken  uit een geregistreerde overeenkomst, gedateerd minder  dan een jaar na de dagtekening van de eerste  overeenkomst.

De teruggave is niet mogelijk voor het verkooprecht,  geheven op een overeenkomst die bij authentieke akte is  vastgesteld, noch op een inbreng door een natuurlijke  persoon van een woning in een Belgische vennootschap,  noch op een overeenkomst die onderworpen is aan het  tarief, vermeld in artikel 2.9.4.2.4, § 1;

La restitution n'est pas possible pour le droit de vente  levé sur une convention qui est constatée par acte  authentique, ni sur un apport par une personne physique  d'une habitation dans une société belge, ni sur une  convention soumise au tarif visé à l'article 2.9.4.2.4, §  1er ;  3° wanneer een in kracht van gewijsde gegaan vonnis of  arrest de ontbinding of de herroeping uitspreekt of  vaststelt van een overeenkomst, op voorwaarde dat uit  de beslissing blijkt dat ten hoogste één jaar na de  overeenkomst het geding, zelfs bij een onbevoegde  rechter, is ingeleid;

4° wanneer de belasting over de toegevoegde waarde  opeisbaar wordt overeenkomstig artikel 1, § 10, van het  Wetboek van de Belasting over de Toegevoegde Waarde  op de verrichting van vervreemding onder bezwarende  titel van een onroerend goed of van de vestiging,  overdracht en wederoverdracht van een zakelijk recht op  een onroerend goed;

5° wanneer een vonnis of een arrest geheel of  gedeeltelijk wordt vernietigd door een andere in kracht  van gewijsde gegane rechterlijke beslissing.

De ontheffing, vermeld in het eerste lid, 2°, wordt  toegestaan met voorbehoud van 10 euro op de  ontbonden overeenkomst.

Wat de registratiebelasting betreft, verleent het  bevoegde personeelslid ook ontheffing van het bedrag  aan registratiebelasting dat te veel is geheven  overeenkomstig artikel 2.8.5.0.1, § 1, derde lid, op  voorwaarde dat een verzoek is ingediend binnen een  termijn van vijf jaar vanaf 1 januari van het jaar waarin  het kind geboren is.

§ 1/2. Wat de registratiebelasting betreft, verleent het  bevoegde personeelslid ook ontheffing van het geheven  bedrag dat hoger is dan de schenkbelasting, vermeld in  artikel 2.8.4.3.1, hetzij § 2, hetzij § 3, op voorwaarde dat  de bewijsstukken vermeld in artikel 2.8.4.3.1, § 2,  worden ingediend uiterlijk zes maanden na het  verstrijken van het derde jaar na de datum van de akte  van schenking.

§ 1/3. Wat de registratiebelasting betreft, verleent het  bevoegde personeelslid ook ontheffing van het geheven  bedrag dat hoger is dan de schenkbelasting, vermeld in  artikel 2.8.4.4.1, hetzij § 1, hetzij § 3, op voorwaarde dat  de begiftigden een verzoek tot teruggave indienen  uiterlijk zes maanden na het verstrijken van het vijfde  jaar na de datum van de schenkingsakte en een attest  verkrijgen waaruit blijkt dat aan de voorwaarden,  vermeld in artikel 2.8.4.4.1, hetzij § 1, hetzij § 3, is

§ 1/3. En ce qui concerne l’impôt d’enregistrement, le  membre du personnel compétent accorde également  l’exonération du montant perçu qui est supérieur à  l’impôt de donation, visé à l’article 2.8.4.4.1, soit § 1er,  soit § 3, à condition que les bénéficiaires introduisent  une demande de restitution au plus tard six mois après  l’expiration de la cinquième année après la date de l’acte  de donation et obtiennent une attestation qui démontre  que les conditions, visées à l’article 2.8.4.4.1, soit § 1er,  voldaan. Het voormelde attest wordt door de bevoegde  entiteit van de Vlaamse overheid verkregen van het  agentschap, vermeld in artikel 2.1, 2°, van het  Onroerenderfgoeddecreet van 12 juli 2013.

Het recht op ontheffing vervalt bij elke vervreemding  onder de levenden van het beschermde monument  binnen vijf jaar na de datum van de schenkingsakte en  voordat de beheersmaatregelen, werkzaamheden of  diensten die noodzakelijk zijn voor het behoud of de  herwaardering van erfgoedkenmerken en -elementen  van het beschermde monument, zijn beëindigd.

§ 2. Wat de registratiebelasting betreft, verleent het  bevoegde personeelslid ook ontheffing van de  registratiebelasting op voorwaarde dat een verzoek is  ingediend binnen een termijn van vijf jaar vanaf 1  januari van het jaar waarin het recht tot teruggave is  ontstaan, waarin wordt aangetoond dat een onroerend  goed dat door de verkoper of zijn rechtsvoorgangers is  verkregen bij een akte waarop het verkooprecht met  toepassing van artikel 2.9.4.1.1 is voldaan, wordt  wederverkocht. De ontheffing ten voordele van de  wederverkoper beperkt zich in dat geval tot drie vijfde  van het verkooprecht dat geheven is.

De wederverkoop, vermeld in het eerste lid, moet bij  authentieke akte vastgesteld zijn binnen twee jaar na de  datum van de authentieke akte van verkrijging.

Als de verkrijging of de wederverkoop heeft  plaatsgevonden onder een opschortende voorwaarde,  wordt de termijn van wederverkoop berekend op basis  van de datum waarop die voorwaarde is vervuld.

De registratiebelasting die betrekking heeft op het  gedeelte van de prijs en de lasten van de verkrijging, dat  hoger is dan de conform artikel 2.9.3.0.1 bepaalde  heffingsgrondslag van de akte van wederverkoop, wordt  niet teruggegeven.

In geval van gedeeltelijke wederverkoop wordt in het  verzoek tot teruggave het deel van de aanschaffingsprijs

En cas de revente partielle, la part du prix d'acquisition  qui se rapporte à la partie revendue est spécifiée dans la  dat betrekking heeft op het wederverkochte gedeelte,  nader aangegeven onder controle van de bevoegde  entiteit van de Vlaamse administratie.

§ 2/1. Wat de registratiebelasting betreft, verleent het  bevoegde personeelslid ook ontheffing van het bedrag  aan registratiebelasting dat meer bedraagt dan het  verkooprecht, vermeld in artikel 2.9.4.2.11, § 1, artikel  2.9.4.2.12 en artikel 2.9.4.2.14, op voorwaarde dat een  verzoek is ingediend binnen een termijn van vijf jaar  vanaf 1 januari van het jaar waarin het recht tot  teruggave is ontstaan. In het verzoek tot teruggave moet  worden aangetoond dat de woning of bouwgrond die de  toepassing van het verlaagde tarief van artikel  2.9.4.2.11, § 1, artikel 2.9.4.2.12 en artikel 2.9.4.2.14,  heeft verhinderd, uiterlijk twee jaar of uiterlijk drie jaar,  in geval van toepassing van het verlaagd tarief van  artikel 2.9.4.2.12 en 2.9.4.2.14, na de datum van de  authentieke akte van verkrijging van de andere woning  volledig en ten bezwarende titel is vervreemd, en dat er  een causaal verband bestaat tussen die vervreemding en  de verkrijging. Bovendien moet in het verzoek tot  teruggave worden voldaan aan de verplichting, vermeld  in artikel 3.12.3.0.1, § 1 en § 3.

De registratiebelasting, betaald voor de verkrijging van  een onroerend goed dat niet in het Vlaamse Gewest ligt,  alsook de aanvullende rechten die om om het even welke  reden op een aankoop zijn geheven, zijn uitgesloten van  de teruggave, overeenkomstig de bepalingen van deze  paragraaf.

De teruggave, overeenkomstig de bepalingen van deze  paragraaf, kan in geen geval meer bedragen dan het  bedrag van het wettelijk aandeel van de natuurlijke  persoon in de registratiebelasting die conform artikel

La restitution, conformément aux dispositions du  présent paragraphe, ne peut en aucun cas excéder le  montant de la part légale de la personne physique dans  les impôt d’enregistrement dus, conformément àl’article  2.9.4.1.1, artikel 2.9.4.2.11, artikel 2.9.4.2.12, artikel  2.9.4.2.13 of artikel 2.9.4.2.14 verschuldigd was op de  aankoop van de verkochte of verdeelde woning of van  de bouwgrond waarop die woning is opgericht.

Als een verrichting als vermeld in het eerste lid, is  voorafgegaan door een of meer van zulke verrichtingen  of door een of meer verrichtingen als vermeld in artikel  2.9.5.0.1, eerste lid, wordt, in voorkomend geval, de bij  die voorgaande verrichtingen ingevolge de toepassing  van het derde of het vijfde lid van deze paragraaf nog  niet teruggegeven registratiebelasting of de ingevolge de  toepassing van artikel 2.9.5.0.1, derde of vijfde lid, nog  niet verrekende registratiebelasting, gevoegd bij het  wettelijk aandeel van de natuurlijke persoon in de  conform artikel 2.9.4.1.1, artikel 2.9.4.2.11, artikel  2.9.4.2.12, artikel 2.9.4.2.13 of artikel 2.9.4.2.14  verschuldigde registratiebelasting op de voorlaatste  aankoop, om het teruggeefbare bedrag bij de  wederverkoop ervan te bepalen.

Aan de teruggave zijn de volgende voorwaarden  verbonden :

1° het verzoek tot teruggave, ondertekend door de  natuurlijke persoon, wordt gedaan in of onderaan op de  akte die of het geschrift dat aanleiding geeft tot de  heffing van de registratiebelasting op de verkoop of de  verdeling of in een afzonderlijk verzoek tot teruggave;

2° de akte of het geschrift, vermeld in punt 1°, bevat :  2° l'acte ou l'écrit, visé au point 1°, contient :

a) het bedrag en de datum van betaling van de  registratiebelasting, geheven op de aankoop van de  verkochte of verdeelde woning of van de bouwgrond

a) le montant et la date du paiement des impôt  d’enregistrement, perçus sur l'achat de l'habitation  vendue ou partagée ou du terrain à bâtir sur lequel cette  waarop die woning is opgericht, en vermeldt het  wettelijk aandeel van de natuurlijke persoon in de  registratiebelasting, geheven op die aankoop;

b) het bedrag en de datum van betaling van de  registratiebelasting, geheven op de aankoop van de  nieuwe hoofdverblijfplaats, en vermeldt het wettelijk  aandeel  van  de  natuurlijke  persoon  in  de  registratiebelasting, geheven op die aankoop.

Als de teruggave wordt gevraagd met toepassing van het  vierde lid van deze paragraaf, moet de akte of het  geschrift, vermeld in punt 1°, bovendien het bedrag en  de datum van betaling van de registratiebelasting  vermelden, aangebracht op de akten of geschriften die  betreffende de in aanmerking te nemen voorafgaande  verrichtingen aanleiding hebben gegeven tot het heffen  van de registratiebelasting, en bij iedere vermelding het  wettelijk aandeel van de natuurlijke persoon in de  verrekende  of  teruggegeven  registratiebelasting  vermelden;

a) dat hij op een ogenblik in de periode van achttien  maanden voorafgaand aan de aankoop van de woning  die hij tot zijn nieuwe hoofdverblijfplaats aanwendt of  bestemt, zijn hoofdverblijfplaats heeft gehad in de  wederverkochte of verdeelde woning;

b) dat hij zijn hoofdverblijfplaats op de plaats van het  nieuw aangekochte goed heeft gevestigd of zal vestigen  :

1) als het een woning betreft, binnen twee jaar na, ofwel  de datum van de registratie van de akte die of het  geschrift dat tot de heffing van de registratiebelasting op  de aankoop aanleiding geeft, als die akte of dat geschrift  binnen de ervoor bepaalde termijn ter registratie wordt  aangeboden, ofwel de uiterste datum voor tijdige  aanbieding ter registratie, als de akte die of het geschrift  dat tot de heffing van de registratiebelasting op de  aankoop aanleiding geeft, wordt aangeboden na het  verstrijken van de daarvoor bepaalde termijn;

2) als het een bouwgrond betreft, binnen vijf jaar na  dezelfde datum.

In geval van onjuistheid of niet-nakoming van de  vermeldingen, voorgeschreven bij het zesde lid, is de  natuurlijke persoon gehouden tot betaling van de  onrechtmatig teruggegeven registratiebelasting.

§ 4. Wat betreft de registratiebelasting verleent het  bevoegde  personeelslid ook ontheffing van de  registratiebelasting  van  zes  procent,  geheven  overeenkomstig artikel 2.9.4.2.7, als een aangekocht  goed wordt wederverkocht bij authentieke akte, verleden  binnen tien jaar na de datum van de akte van verkrijging,  op voorwaarde dat een aangifte wordt ingediend binnen  een termijn van vijf jaar vanaf 1 januari van het jaar  waarin het recht tot teruggave is ontstaan, die het  hierboven vermelde feit aanduidt.

De bepalingen van paragraaf 2, derde en vierde lid, zijn  van toepassing op deze paragraaf.

§ 6. (...)  § 6. (...)

§ 7. De bepalingen van artikel 3.6.0.0.2 en 3.6.0.0.3 zijn  onverminderd van toepassing op dit artikel.

---- historiek ----  ---- historique ----

- gewijzigd door art. 28 van het decreet van 09.12.2022  (B.S. 20.12.2022). Inwerkingtreding: 30.12.2022

- gewijzigd door art. 80 van het decreet van 23.12.2021  (B.S., 29.12.2021). Van toepassing op overeenkomsten  houdende zuivere aankoop gesloten vanaf 1 januari  2022, of, in afwijking daarvan, op authentieke akten  verleden vanaf 1 januari 2022, wanneer de  overeenkomsten houdende zuivere aankoop waarop de  akten betrekking hebben, gesloten zijn voor 1 januari  2022

- gewijzigd door art. 39, 1° van het decreet van  21.12.2018 (B.S. 28.12.2018). Tekst treedt in werking op  07.01.2019

- gewijzigd door art. 39, 2° en 3° van het decreet van  21.12.2018 (B.S. 28.12.2018). Tekst is van toepassing op  verkoopovereenkomsten afgesloten vanaf 1 juni 2018

- gewijzigd door art. 13 van het decreet van 18.05.2018  (B.S.: 28.05.2018). Tekst is van toepassing op  verkoopovereenkomsten afgesloten vanaf 1 juni 2018

- gewijzigd door art. 27 van het decreet van 17 juli 2015  (B.S., 14.08.2015 ). De tekst is in werking getreden op 14  augustus 2015 (art. 41)

- gewijzigd door art. 8 van het decreet van 21.04.2017.  De tekst is in werking getreden op 14.05.2017

### Hoofdstuk 7 - Nietigverklaring  Chapitre 7 – Annulation

###### Art. 3.7.0.0.1.  Art. 3.7.0.0.1.

###### Art. 3.7.0.0.2.  Art. 3.7.0.0.2.

§ 1. Als een aanslag nietig verklaard is omdat hij niet is  gevestigd overeenkomstig een wettelijke regel, met  uitzondering van een regel over de verjaring, kan de  bevoegde entiteit van de Vlaamse administratie, zelfs als  de termijn om de aanslag te vestigen al verlopen is, op  naam van dezelfde belastingplichtige, op grond van  dezelfde belastingelementen of op een gedeelte ervan,  een nieuwe aanslag vestigen binnen drie maanden vanaf  de datum waarop de beslissing van het bevoegde  personeelslid niet meer voor de rechter kan worden  gebracht.

§ 2. Als tegen een beslissing van het bevoegde  personeelslid een vordering in rechte is ingesteld en de  rechter de aanslag geheel of ten dele nietig verklaart, om  een andere reden dan verjaring, blijft de zaak gedurende  een termijn van zes maanden vanaf de rechterlijke  beslissing ingeschreven op de rol. Gedurende die termijn  van zes maanden die de termijnen om verzet of hoger  beroep aan te tekenen of om een voorziening in cassatie  in te dienen schorst, kan de bevoegde entiteit van de  Vlaamse administratie een subsidiaire aanslag door  middel van conclusies aan het oordeel van de rechter  onderwerpen op naam van dezelfde belastingschuldige  en op grond van dezelfde belastingelementen als in de  initiële aanslag of op grond van een deel van die  belastingelementen.

Als de bevoegde entiteit van de Vlaamse administratie  binnen de termijn van zes maanden een subsidiaire  aanslag aan de rechter voorlegt, beginnen, in afwijking  van het eerste lid, de termijnen om verzet of hoger  beroep aan te tekenen of om een voorziening in cassatie  in te dienen, te lopen vanaf de betekening van de  rechterlijke beslissing over de subsidiaire aanslag.

De subsidiaire aanslag is alleen invorderbaar of  terugbetaalbaar ter uitvoering van de rechterlijke  beslissing.

Als de subsidiaire aanslag gevestigd wordt voor een met  toepassing  van  paragraaf  3  gelijkgestelde  belastingplichtige, wordt die aanslag aan de rechter  onderworpen  door  een  aan  de  gelijkgestelde  belastingschuldige betekend verzoekschrift met  dagvaarding om te verschijnen.

1° de erfgenamen van de belastingplichtige;  1° les héritiers du contribuable ;

2° zijn echtgenoot of wettelijk samenwonende en de  huwgemeenschap;

3°  de  overnemende  of  de  verkrijgende  vennootschappen, naargelang het geval.

4° de vereffenaar van de rechtspersoon waarvan de  vereffening gesloten is, in die hoedanigheid of, bij  afwezigheid daarvan, de personen die beschouwd  worden als vereffenaar krachtens deel 1, boek 2, titel 8,  van het Wetboek van vennootschappen en  verenigingen, gedurende de periode, vermeld in artikel  2:143 van het voormelde wetboek.

---- historiek ----  ---- historique ----

- gewijzigd door art. 54 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

### Hoofdstuk 8 - Gerechtelijk beroep  Chapitre 8 - Recours judiciaire

###### Art. 3.8.0.0.1.  Art. 3.8.0.0.1.

De termijnen van verzet, hoger beroep en cassatie,  alsook het verzet, het hoger beroep en de voorziening in  cassatie  schorsen  de  tenuitvoerlegging  van  de  gerechtelijke beslissing.

###### Art. 3.8.0.0.2.  Art. 3.8.0.0.2.

Het verzoekschrift houdende voorziening in cassatie en  het antwoord op de voorziening mag door een advocaat  worden ondertekend en neergelegd.

###### Art. 3.8.0.0.3.  Art. 3.8.0.0.3.

Inzake de geschillen over de toepassing van deze codex  kan het bevoegde personeelslid in naam van het  Vlaamse Gewest verschijnen.

###### Art. 3.8.0.0.4.  Art. 3.8.0.0.4.

De openbare of ministeriële ambtenaren en officieren  die, krachtens de bepalingen van deze titel, voor de  partijen de registratiebelasting en, in voorkomend geval,  de administratieve geldboeten voorgeschoten hebben,  kunnen met het oog op de terugbetaling ervan,  uitvoerbaar bevel vragen aan de vrederechter van hun  kanton.

###### Art. 3.8.0.0.1. is toepasselijk op het tegen dit bevel

aangetekend verzet.

---- historiek ----  ---- historique ----

werking getreden op 1 januari 2015 (art. 325)

### Hoofdstuk 9 - Interesten  Chapitre 9 – Intérêts

#### Afdeling 1 - Nalatigheidsinteresten  Section 1re - Intérêts de retard

###### Art. 3.9.1.0.1.  Art. 3.9.1.0.1.  § 1. Bij wanbetaling binnen de termijnen, vermeld in  hoofdstuk 4, afdeling 2, brengen de verschuldigde  sommen ten bate van het Vlaamse Gewest, voor de duur  van het verwijl, een interest van 4 % op jaarbasis op,  berekend per kalendermaand.

Die interest wordt voor elke aanslag per kalendermaand  berekend op de nog verschuldigde som, afgerond op het  lagere veelvoud van tien euro, hetzij vanaf de eerste dag  van de maand die volgt op de vervaldag, hetzij vanaf de  eerste dag van de maand die volgt op de vorige betaling  als een som is aangerekend op de hoofdsom van de  schuld, tot op de laatste dag van de maand waarin de  betaling plaatsvindt.

De nalatigheidsinterest is niet verschuldigd als hij geen  vijf euro per maand bedraagt.

§ 2. Als de kennisgeving van de beslissing, vermeld in  artikel 3.5.6.0.1, eerste lid, niet plaatsvindt binnen zes  maanden na de datum van de ontvangst van het  bezwaarschrift, is de nalatigheidsinterest, vermeld in  paragraaf 1, niet verschuldigd voor het betwiste gedeelte  van de aanslag gedurende het tijdperk dat begint op de  eerste dag van de maand die volgt op de maand waarin  de termijn van zes maanden verstrijkt en dat afloopt op  het einde van de maand waarin een vordering conform  artikel 1385undecies van het Gerechtelijk Wetboek  wordt ingesteld en, bij ontstentenis van een dergelijke  vordering, op het einde van de maand waarin de  voormelde beslissing is meegedeeld.

---- historiek ----  ---- historique ----

- gewijzigd door art. 51 van het decreet van 18.12.2020  (B.S., 30.12.2020). Inwerkingtreding: 01.01.2021

###### Art. 3.9.1.0.2.  Art. 3.9.1.0.2.

In bijzondere gevallen mag het bevoegde personeelslid,  onder door hem bepaalde voorwaarden, vrijstelling  verlenen voor al de nalatigheidsinteresten of voor een  deel ervan.

De rechtspersoon die inzake de erfbelasting de  schorsing, vermeld in artikel 3.10.3.1.3, verkrijgt, moet  nalatigheidsinteresten betalen alsof hij die schorsing niet  verkregen had.

Inzake de erfbelasting, waarvan de invordering is  geschorst met toepassing van artikel 3.10.3.1.4, zijn de  nalatigheidsinteresten alleen verschuldigd als de  erfbelasting niet door de inbetalinggeving wordt  voldaan.

---- historiek ----  ---- historique ----

- toegevoegd door art. 231 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

#### Afdeling 2 - Moratoriuminteresten  Section 2 - Intérêts moratoires

###### Art. 3.9.2.0.1.  Art. 3.9.2.0.1.

Bij  terugbetaling  van  belastingen,  nalatigheidsinteresten,  belastingverhogingen  of  administratieve geldboeten wordt moratoriuminterest  toegekend tegen een rentevoet van 4 % op jaarbasis,  berekend per kalendermaand.

Die interest wordt voor elke aanslag per kalendermaand  berekend op het bedrag van elke betaling, afgerond op  het lagere veelvoud van tien euro. De maand waarin de  betaling is uitgevoerd, wordt niet meegerekend, maar de  maand waarin aan de belastingschuldige het bericht  wordt gestuurd dat de terug te betalen som ter  beschikking is, wordt voor een hele maand geteld.

Er wordt geen moratoriuminterest toegekend :  Aucun intérêt moratoire n'est accordé :

1° als de moratoriuminterest minder dan vijf euro per  maand bedraagt;

2° als de terugbetaling voortvloeit uit de kwijtschelding  of de vermindering van een administratieve geldboete of  een  belastingverhoging  die  toegekend  is  als  genademaatregel;

3° in geval van terugbetaling van erfbelasting, tenzij de  terugbetaling plaatsvindt ingevolge een vergissing  vanwege de bevoegde entiteit van de Vlaamse  administratie;

4° in geval van terugbetaling van registratiebelasting,  tenzij de terugbetaling plaatsvindt ingevolge een  vergissing vanwege de bevoegde entiteit van de  Vlaamse administratie.

- gewijzigd door art. 52 van het decreet van 18.12.2020  (B.S., 30.12.2020). Inwerkingtreding: 01.01.2021

- gewijzigd door art. 26 van het decreet van 08.12.2017  (B.S.: 14.12.2017). Tekst van toepassing vanaf  24.12.2017

- 3° en 4° toegevoegd door art. 232 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

### Hoofdstuk 10 - Invordering  Chapitre 10 – Recouvrement

#### Afdeling 1 - Herinnering  Section 1re – Rappel

###### Art. 3.10.1.0.1.  Art. 3.10.1.0.1.

Voorbehouden voor toekomstig gebruik.  Réservé pour un usage futur

#### Afdeling 2 - Laatste herinnering  Section 2 - Dernier rappel

###### Art. 3.10.2.0.1.  Art. 3.10.2.0.1.

Het bevoegde personeelslid moet een herinneringsbrief  sturen  ten  minste  één  maand  voor  de  gerechtsdeurwaarder een bevel tot betaling opstelt,  behalve als de rechten van het Vlaamse Gewest in  gevaar zijn.

#### Afdeling 3 - Vervolging  Section 3 – Poursuite

##### Onderafdeling 1 - Algemeen  Sous-section 1re – Généralités

###### Art. 3.10.3.1.1.  Art. 3.10.3.1.1.

§ 1. De belasting die wordt ingekohierd op naam van één  natuurlijke persoon of rechtspersoon, kan ten laste van  die persoon worden ingevorderd.

§ 2. De onroerende voorheffing die wordt ingekohierd  op naam van verschillende natuurlijke personen of  rechtspersonen kan, behalve in geval van andersluidende  wetsbepalingen, slechts ten laste van elk van hen worden  ingevorderd voor het gedeelte dat verband houdt met  hun aandeel in het onroerend goed. Het kohier is  uitvoerbaar tegen elk van hen in de mate dat de aanslag  ten laste van die natuurlijke personen of rechtspersonen  kan worden ingevorderd op grond van het gemeen recht  of op grond van de bepalingen van deze codex.

De registratiebelasting, die wordt ingekohierd op naam  van  verschillende  natuurlijke  personen  of  rechtspersonen,  kan,  behalve  in  geval  van  andersluidende wetsbepalingen, alleen ten laste van elk  van hen worden ingevorderd voor het gedeelte dat  verband houdt met hun aandeel in het goed dat het  voorwerp uitmaakt van de overeenkomst. Het kohier is  uitvoerbaar tegen elk van hen in de mate dat de aanslag  ten laste van die natuurlijke of rechtspersonen kan

worden ingevorderd op grond van het gemeen recht of  op grond van de bepalingen van deze codex.

§ 3. Het kohier is uitvoerbaar tegen de personen die er  niet in zijn opgenomen als ze gehouden zijn tot de  betaling van de belastingschuld op grond van het  gemeen recht of op grond van de bepalingen van deze  codex.

---- historiek ----  ---- historique ----

- gewijzigd door art. 40 van het decreet van 21.12.2018  (B.S. 28.12.2018). Tekst treedt in werking op 07.01.2019

- gewijzigd door art. 52 van het decreet van 23.12.2016  (B.S.: 30.12.2016). Tekst in werking getreden vanaf  aanslagjaar 2017

- § 2, tweede lid werd toegevoegd door art. 3 van het  decreet van 25 maart 2016 (B.S., 01.04.2016). De tekst

treedt in werking op 1 april 2016 (art. 4))

- §2, derde lid toegevoegd door art. 233 van het decreet  van 19.12.2014 (B.S., 29.01.2015 - Ed. 2). De

tekst is in werking getreden op 01.01.2015 (art. 325)

De met erfstelling bezwaarde erfgenaam die de aangifte  in het geval, vermeld in artikel 3.3.1.0.6, eerste lid, 5°,  niet indient, is en de personen die zijn veroordeeld als  daders of medeplichtigen van misdrijven als vermeld in  artikel 3.15.3.0.1 en artikel 3.15.3.0.2, zijn inzake de  erfbelasting met de belastingschuldige hoofdelijk  gehouden tot de betaling van de belastingen en  toebehoren, die door de inbreuk ontdoken werden, en, in  voorkomend geval, van de nalatigheidsinteresten en van  de  administratieve  geldboetes  en  de  belastingverhogingen.

---- historiek ----  ---- historique ----

- gewijzigd door art. 41 van het decreet van 21.12.2018  (B.S. 28.12.2018). Tekst treedt in werking op 07.01.2019

- toegevoegd door art. 234 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 3.10.3.1.3.  Art. 3.10.3.1.3.

Als een legaat ten behoeve van een rechtspersoon met  zetel,  hoofdbestuur  of  hoofdvestiging  op  het  grondgebied van een staat van de Europese Economische  Ruimte aan een machtiging of aan een  goedkeuring van de overheid onderworpen is, wordt

Si un legs au profit d'une personne morale dont le siège,  l'administration centrale ou le principal établissement  est situé sur le territoire d'un Etat de l'Espace  économique européen est soumis à une  autorisation ou une approbation de l'autorité, le  inzake de erfbelasting, op schriftelijk verzoek van de  rechtspersoon, de invordering van de belastingen en  toebehoren, verschuldigd door die rechtspersoon,  geschorst gedurende twee maanden.

---- historiek ----  ---- historique ----

- gewijzigd door art. 55 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- toegevoegd door art. 235 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 3.10.3.1.4.  Art. 3.10.3.1.4.

[…]  […]

- opgeheven door art. 10 van het decreet van 10.03.2023  (B.S., 23.03.2023). Inwerkingtreding op een datum die de  Vlaamse Regering vaststelt en uiterlijk op 01.07.2023

- toegevoegd door art. 236 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 3.10.3.1.5.  Art. 3.10.3.1.5.

In geval van toepassing van artikel 2.8.4.2.3, tweede lid,  zijn de schenker en de begiftigden hoofdelijk gehouden  tot de betaling van de aanvullende rechten.

In geval van toepassing van artikel 2.8.4.2.3, derde lid,  zijn de begiftigden die de verbintenis zijn aangegaan en  niet zijn nagekomen, bovendien hoofdelijk gehouden tot  de betaling van alle aanvullende rechten over de  aandelen van hun medebegiftigden die de verbintenissen  niet zijn aangegaan, tenzij er een medebegiftigde rest die  wel de verbintenis die door hem is aangegaan, is  nagekomen.

---- historiek ----  ---- historique ----

- toegevoegd door art. 237 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 3.10.3.1.6.  Art. 3.10.3.1.6.

(…)  (…)

---- historiek ----  ---- historique ----

- opgeheven door art. 27 van het decreet van 08.12.2017

(B.S.: 14.12.2017).  Tekst  van  toepassing   vanaf 24.12.2017

- toegevoegd door art. 238 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 3.10.3.1.7.  Art. 3.10.3.1.7.

(…)  (…)

---- historiek ----  ---- historique ----

- opgeheven door art. 27 van het decreet van 08.12.2017  (B.S.: 14.12.2017). Tekst van toepassing

vanaf 24.12.2017

- toegevoegd door art. 239 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

Als de verklaring over de uitbating van de geruilde  onroerende goederen, vermeld in artikel 3.12.3.0.1, § 3,  derde lid, onjuist wordt bevonden, zijn de partijen  hoofdelijk gehouden tot de betaling van de aanvullende  rechten.

---- historiek ----  ---- historique ----

- gewijzigd door art. 56 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- toegevoegd door art. 240 van het decreet van  19.12.2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

##### Onderafdeling 2 - Rechtstreekse vervolging  Sous-section 2 - Poursuite directe

###### Art. 3.10.3.2.1.  Art. 3.10.3.2.1.

Als de belastingen en toebehoren niet voldaan worden,  kunnen de bevoegde personeelsleden een dwangschrift  uitvaardigen.

Op  basis  van  dat  dwangschrift  kan  via  gerechtsdeurwaardersexploot een dwangbevel betekend  worden tot betaling binnen vierentwintig uur, op straffe  van tenuitvoerlegging door beslag.

In  het  dwangbevel  wordt  verwezen  naar  het  dwangschrift en het kohieruittreksel die samen met het  dwangbevel worden betekend.

Behalve in geval van andersluidende bepalingen zijn op  het dwangbevel de bepalingen van deel V van het  Gerechtelijk Wetboek van toepassing.

Gedeeltelijke betalingen die verricht zijn ingevolge de  betekening van een dwangbevel, verhinderen de  voortzetting van de vervolgingen niet.

Les paiements partiels qui sont effectués suite à la  notification d'une contrainte, n'empêchent pas la  continuation des poursuites.  Binnen een termijn van dertig dagen na de betekening  van het dwangbevel kan de belastingschuldige bij  gerechtsdeurwaardersexploot een met redenen omkleed  verzet aantekenen, houdende dagvaarding van het  Vlaamse Gewest, bij de rechtbank van eerste aanleg van  de plaats waar de bevoegde entiteit van de Vlaamse  administratie die de belasting moet innen, is gevestigd.

Dat verzet schorst de tenuitvoerlegging van het  dwangbevel niet.

De Vlaamse Regering kan de regels bepalen voor de  rechtstreekse vervolging.

###### Art. 3.10.3.3.1.  Art. 3.10.3.3.1.

De Vlaamse Regering kan de regels bepalen voor de  onrechtstreekse vervolging.

##### Onderafdeling 4 - Vervolgingskosten  Sous-section 4 - Frais de poursuite

###### Art. 3.10.3.4.1.  Art. 3.10.3.4.1.

De Vlaamse Regering kan de regels bepalen voor de  vervolgingskosten.

##### Onderafdeling 5 - Met vervolging belaste personen  Sous-section 5 - Personnes chargées de la poursuite

###### Art. 3.10.3.5.1.  Art. 3.10.3.5.1.

De Vlaamse Regering kan bepalen welke personen  belast zijn met vervolging en welke regels ze moeten  naleven.

#### Afdeling 4 - Bijzondere gevallen  Section 4 - Cas particuliers

##### Onderafdeling 1. - Invordering bij echtgenoten of ex-

echtgenoten en bij wettelijk samenwonenden of ex-

wettelijksamenwonenden

###### Art. 3.10.4.1.1.  Art. 3.10.4.1.1.

Met behoud van de toepassing van artikel 3.10.4.1.2,  mag de invordering van een belasting die is ingekohierd  op naam van de ene echtgenoot of wettelijk  samenwonende, worden vervolgd ten laste van de  andere echtgenoot of wettelijk samenwonende op  voorwaarde dat aan de andere echtgenoot of wettelijk  samenwonende een exemplaar van het aanslagbiljet is  toegezonden.

Door de verzending van het aanslagbiljet begint voor de  geadresseerde de termijn voor bezwaar, vermeld in  hoofdstuk 5, afdeling 2, te lopen.

###### Art. 3.10.4.1.2.  Art. 3.10.4.1.2.

§ 1. De belasting mag, ongeacht het aangenomen  huwelijksvermogensstelsel of ongeacht de notariële  overeenkomst waarin de wettelijke samenwoning is  geregeld, op al de eigen en de gemeenschappelijke  goederen van beide echtgenoten of op al de eigen en de  onverdeelde  goederen  van  beide  wettelijk  samenwonenden worden verhaald.

De belasting die verschuldigd is door de ene echtgenoot  of wettelijk samenwonende, mag evenwel niet op de  eigen goederen van de andere echtgenoot of wettelijk  samenwonende worden verhaald als die laatste een van  de volgende feiten aantoont :

2° de goederen komen voort van een erfenis of van een  schenking door een andere persoon dan zijn echtgenoot  of wettelijk samenwonende;

3° hij heeft die goederen verkregen door middel van  fondsen die voortkomen van de realisatie van dergelijke  goederen;

4° het gaat om inkomsten die hem krachtens het  burgerlijk recht eigen zijn of om goederen die hij met die  inkomsten heeft verworven.

§ 2. In afwijking van paragraaf 1 kunnen, in geval van  feitelijke scheiding van de echtgenoten of wettelijk  samenwonenden, de belastingen die ontstaan zijn meer  dan twee jaar na de datum van de feitelijke scheiding,  niet meer worden ingevorderd op het inkomen van de  andere echtgenoot of wettelijk samenwonende of op de  goederen die de andere echtgenoot of wettelijk  samenwonende met dat inkomen heeft verworven.

§ 3. Na de ontbinding van het huwelijk of de beëindiging  van de wettelijke samenwoning, vermeld in artikel 1476  van het Burgerlijk Wetboek, kunnen de belastingen die  ontstaan zijn vóór die ontbinding of beëindiging, worden  ingevorderd op de goederen van de beide echtgenoten of  wettelijk samenwonenden, op de wijze, vermeld in  paragraaf 1 en 2.

§ 4. Paragraaf 1 is niet van toepassing op belastingen die  ontstaan zijn vóór het huwelijk en vóór het afleggen van  de verklaring van wettelijke samenwoning.

§  5.  Voor  de  onroerende  voorheffing,  de  leegstandsheffing  bedrijfsruimten,  de  heffing  ongeschikte en onbewoonbare woningen en de heffing  vermeld in titel II, hoofdstuk VI, afdeling 2, van de  Vlaamse Codex Ruimtelijke Ordening, die betrekking

§ 5. Seul le paragraphe 1er, alinéa premier, s'applique  au précompte immobilier, à la taxe sur les sites d'activité  économique désaffectés et la taxe sur les habitations  inadaptées et insalubres ou la redevance citée dans le  titre II, chapitre VI, section 2, du Code flamand de  hebben op een goed in de gemeenschap, is alleen  paragraaf 1, eerste lid, van toepassing.

§ 6. Gelet op de hoofdelijkheid overeenkomstig artikel  3.10.3.1.1, § 2, tweede lid, is dit artikel niet van  toepassing op de leegstandsheffing bedrijfsruimten, de  heffing ongeschikte en onbewoonbare woningen en de  heffing vermeld in titel II, hoofdstuk VI, afdeling 2, van  de Vlaamse Codex Ruimtelijke Ordening, als die  belasting ingekohierd is op naam van beide echtgenoten  of wettelijk samenwonenden en het belaste goed geen  deel uitmaakt van de gemeenschap.

---- historiek ----  ---- historique ----

##### Onderafdeling 2 - Invordering bij vennootschappen  Sous-section 2 - Recouvrement auprès de sociétés

###### Art. 3.10.4.2.1.  Art. 3.10.4.2.1.

De invordering van de belasting die gevestigd is op  naam van de vennoten van vennootschappen zonder  rechtspersoonlijkheid of van de leden van verenigingen  zonder rechtspersoonlijkheid, kan rechtstreeks ten laste  van de vennootschap of de vereniging worden vervolgd  als die belasting proportioneel overeenstemt met het  aandeel van de vennoten of leden in de niet-uitgekeerde  winst  of  baten  van  die  vennootschappen  of  verenigingen.

---- historiek ----  ---- historique ----

- vervangen door art. 57 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

###### Art. 3.10.4.2.2.  Art. 3.10.4.2.2.

De invordering van de belasting van een met toepassing  van artikel 12:4 tot en met 12:6 van het Wetboek van  vennootschappen  en  verenigingen  of  van  een  gelijkaardige  vennootschapsrechtelijke  verrichting  onder buitenlands recht gesplitste vennootschap die  gevestigd  is  op  naam  van  de  verkrijgende  vennootschappen, kan, behalve in geval van afwijkende  vermeldingen in de akte die de verrichting vaststelt,  worden verricht op naam van iedere verkrijgende  vennootschap. Elke verkrijgende vennootschap is  hoofdelijk gehouden tot betaling van de belasting.

---- historiek ----  ---- historique ----

- gewijzigd door art. 58 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

##### Onderafdeling 3 - Invordering bij erfgenamen  Sous-section 3 - Recouvrement auprès des héritiers

###### Art. 3.10.4.3.1.  Art. 3.10.4.3.1.

De erfgenamen, algemene legatarissen en begiftigden in  de nalatenschap van een rijksinwoner zijn, ieder in  verhouding tot zijn erfdeel, samen gehouden tot de  betaling van het gezamenlijke successierecht, de  nalatigheidsinteresten en de kosten van vervolging en  tenuitvoerlegging, verschuldigd door de legatarissen en

Het eerste lid is niet van toepassing op het  successierecht, de nalatigheidsinteresten en de kosten  van vervolging en tenuitvoerlegging, verschuldigd op de  nieuwe aangiften, vermeld in artikel 3.3.1.0.6, eerste lid,  als ze niet verplicht zijn die aangiften in te dienen.

Het eerste lid is evenmin van toepassing op het  successierecht, de nalatigheidsinteresten en de kosten  van vervolging en tenuitvoerlegging, verschuldigd op  een verkrijging die overeenkomstig de artikelen  2.7.1.0.5, § 1, tweede lid, en 2.7.1.0.6 met een legaat  wordt gelijkgesteld.

---- historiek ----  ---- historique ----

- vervangen door art. 94 van het decreet van 18 dec.  2015 (B.S., 29.12.2015). De tekst is in werking getreden  op 1 januari 2016 (art. 135)

##### Onderafdeling 4 - Invordering bij andere personen die

gehouden zijn tot betaling van de schuld

###### Art. 3.10.4.4.1.  Art. 3.10.4.4.1.

De administratie of de instelling die belast is met het  beheer van een goed van de staat, van een gemeenschap  of van een gewest, is verantwoordelijk voor de betaling  van de belastingen die op dat goed betrekking hebben.

###### Art. 3.10.4.4.2.  Art. 3.10.4.4.2.

Zolang een eigendom niet is overgeschreven in de  stukken van het de Algemene Administratie van de  Patrimoniumdocumentatie, zijn de vroegere eigenaar of  zijn erfgenamen, tenzij ze bewijzen dat de belastbare  goederen op een andere eigenaar zijn overgegaan en dat  ze de identiteit en het volledige adres van de nieuwe  eigenaar laten kennen, aansprakelijk voor de betaling  van de onroerende voorheffing, behoudens hun verhaal  op de nieuwe eigenaar.

In geval van overlegging van het bewijsstuk, vermeld in  het eerste lid, mag de invordering van de onroerende  voorheffing, ingekohierd op naam van de vroegere  eigenaar van een onroerend goed dat van titularis is  veranderd,  krachtens  hetzelfde  kohier  worden  voortgezet ten laste van de werkelijke schuldenaar van  de belasting. De belastingschuldige ontvangt een nieuw  exemplaar van het aanslagbiljet met de vermelding dat  het krachtens deze bepaling is uitgereikt.

---- historiek ----  ---- historique ----

###### Art. 3.10.4.4.3.  Art. 3.10.4.4.3.

De vertegenwoordigers van de erfgenamen, legatarissen  en  begiftigden,  de  curatoren  van  onbeheerde  nalatenschappen,  de  sekwesters,  de  testamentuitvoerders en alle anderen die tot opdracht  hebben of de last op zich genomen hebben de aangifte in  te dienen, zijn tegenover het Vlaamse Gewest gehouden  tot  de  betaling  van de  erfbelasting,  van  de  nalatigheidsinteresten en de kosten van vervolging en  tenuitvoerlegging als ze in gebreke zijn gebleven om aan  de verplichtingen inzake de aangifte van de nalatenschap  te voldoen.

---- historiek ----  ---- historique ----

- toegevoegd door art. 242 van het decreet van 19 dec.  2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in werking  getreden op 1 januari 2015 (art. 325)

###### Art. 3.10.4.4.4.  Art. 3.10.4.4.4.

Voor wat betreft de registratiebelasting kunnen de  belasting en de toebehoren eveneens ingevorderd  worden ten laste van :

1° de personen die verplicht zijn tot aanbieding ter  registratie overeenkomstig artikel 35, eerste lid, 1°, 4° en  5°, van het federale Wetboek van Registratie-,  Hypotheek- en Griffierechten, als de belastbaarheid  blijkt uit de akten of geschriften, die door hen ter  registratie aangeboden zijn;

2° elk van de contracterende partijen in geval van :  2° chacune des parties contractantes en cas :

a) een onderhandse of in het buitenland verleden akte als  vermeld in artikel 19, eerste lid, 2°, van het federale  Wetboek  van  Registratie-,  Hypotheek-  en  Griffierechten;

b) een overeenkomst in geval van toepassing van artikel  31, eerste lid, 1° en 2°, van het federale Wetboek van  Registratie-, Hypotheek- en Griffierechten;

c) een overeenkomst die het voorwerp uitmaakt van een  vonnis of arrest als vermeld in artikel 35, vierde lid, van  het federale Wetboek van Registratie-, Hypotheek- en  Griffierechten.

De aanvullende rechten inzake de registratiebelasting  zijn in de volgende gevallen verschuldigd door elk van  de contracterende partijen die aan de overtreding hebben  deelgenomen:

2° als de overeenkomst, vastgesteld in een akte, niet de  overeenkomst is die door de partijen is gesloten, of als  de akte betreffende een overeenkomst, vermeld in artikel  19, eerste lid, 2° of 5°, van het federale Wetboek van  Registratie-, Hypotheek- en Griffierechten, onvolledig  of onjuist is, met dien verstande dat ze al de  bestanddelen van de overeenkomst niet weergeeft.

In de gevallen, vermeld in het tweede lid, zijn de partijen  die aan de overtreding hebben deelgenomen, hoofdelijk  gehouden tot de betaling van de aanvullende rechten.

---- historiek ----  ---- historique ----

- gewijzigd door art. 28 van het decreet van 08.12.2017  (B.S.: 14.12.2017). Tekst van toepassing vanaf  24.12.2017

- toegevoegd door art. 243 van het decreet van 19 dec.  2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in werking  getreden op 1 januari 2015 (art. 325)

###### Art. 3.10.4.4.5.  Art. 3.10.4.4.5.

De vertegenwoordiger, vermeld in artikel 2.9.4.2.4, § 2,  3°, is hoofdelijk gehouden tot de fiscale verplichtingen  van de verkrijger, vermeld in hetzelfde punt 3°.

---- historiek ----  ---- historique ----

- toegevoegd door art. 244 van het decreet van 19 dec.  2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in werking  getreden op 1 januari 2015 (art. 325)

###### Art. 3.10.4.4.6.  Art. 3.10.4.4.6.

Als  de  belastingplichtige  het  automatische  ontspanningstoestel niet heeft aangegeven, wordt de  persoon die als uitbater van lokalen of andere plaatsen  als vermeld in artikel 2.13.1.0.1, toelaat om in die  lokalen  of  andere  plaatsen  het  automatisch  ontspanningstoestel op te stellen, als belastingschuldige  beschouwd voor de belasting en toebehoren.

---- historiek ----  ---- historique ----

- ingevoegd door art. 45 van het decreet van 07.12.2018  (B.S. 20.12.2018). Tekst in werking

getreden op 01.01.2019

##### Onderafdeling 5 - Invordering van het eurovignet bij

andere belastingschuldigen dan de eigenaar

###### Art. 3.10.4.5.1.  Art. 3.10.4.5.1.

In geval van niet-betaling door de houder van het  voertuig, vermeld in artikel 2.4.2.0.1, § 1, is degene die  het voertuig feitelijk ter beschikking heeft hoofdelijk  gehouden tot betaling van de kilometerheffing, onder  voorbehoud van verhaal tegen de houder van het  voertuig.

Voor de toepassing van het tweede lid wordt de  bestuurder van het voertuig beschouwd als een persoon  die het voertuig ter beschikking heeft.

---- historiek ----  ---- historique ----

- tweede en derde lid werd toegevoegd door art. 33 van  het decreet van 3 juli 2015 (B.S., 10.08.2015). De tekst  treedt in werking op 1 april 2016 (art. 44)

##### Onderafdeling 6 - Invordering van betwiste belastingen  Sous-section 6 - Recouvrement d'impôts contesté

###### Art. 3.10.4.6.1.  Art. 3.10.4.6.1.

In geval van bezwaar, van een aanvraag tot ontheffing  als vermeld in artikel 3.6.0.0.1, artikel 3.6.0.0.4 en  artikel 3.6.0.0.6 of in geval van een vordering in rechte,  kan de gedwongen invordering van de betwiste  belastingen en toebehoren opgeschort worden totdat de  beroepstermijn tegen de administratieve beslissing  verstreken is of de rechterlijke beslissing in kracht van  gewijsde is gegaan.

In geval van bezwaar, van een aanvraag tot ontheffing  als vermeld in artikel 3.6.0.0.1, artikel 3.6.0.0.4 en  artikel 3.6.0.0.6, of in geval van een vordering in rechte  kunnen de betwiste belastingen en toebehoren voor het  geheel het voorwerp zijn van bewarende beslagen of van  alle andere maatregelen die ertoe strekken de  invordering te waarborgen.

---- historiek ----  ---- historique ----

- gewijzigd door art. 245 van het decreet van 19 dec.  2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in werking  getreden op 1 januari 2015 (art. 325)

#### Afdeling 5 - Zekerheden  Section 5 – Sûretés

##### Onderafdeling 1 - Waarborg  Sous-section 1re – Garantie

###### Art. 3.10.5.1.1.  Art. 3.10.5.1.1.

De Vlaamse Regering bepaalt de gegevens die als  grondslag dienen voor de bepaling van de bedragen van  de zakelijke zekerheid en van de verbintenis van de  persoonlijke borg, alsook de voorwaarden en de  procedure van vaststelling.

§ 2. Binnen een maand na de kennisgeving van de  beslissing,  vermeld  in  paragraaf  1,  kan  de  belastingschuldige een verhaal inleiden voor de  beslagrechter van de plaats waar de bevoegde entiteit  van de Vlaamse administratie die de belasting moet  innen, is gevestigd.

De rechtspleging verloopt zoals in kort geding.  La procédure judiciaire se déroule comme une  procédure en référé.

###### Art. 3.10.5.1.2.  Art. 3.10.5.1.2.

Het stellen van een zakelijke zekerheid of van een  persoonlijke borg als vermeld in artikel 3.10.5.1.1, § 1,  moet  gebeuren  binnen  twee  maanden  na  de  kennisgeving van de beslissing van het bevoegde  personeelslid of na de datum waarop de rechterlijke  beslissing in kracht van gewijsde is gegaan.

###### Art. 3.10.5.1.3.  Art. 3.10.5.1.3.

(…)  (…)

---- historiek ----  ---- historique ----

- opgeheven door art. 59 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- eerste lid vervangen door art. 28 van het decreet van 17  juli 2015 (B.S., 14.08.2015 ). De tekst is in werking  getreden op 14 augustus 2015 (art. 41)

###### Art. 3.10.5.2.1.  Art. 3.10.5.2.1.

§1. Voor de invordering van de belastingen en  toebehoren heeft het Vlaamse Gewest een algemeen  voorrecht op de inkomsten en op de roerende goederen  van alle aard van de belastingschuldige, met  uitzondering van schepen en vaartuigen.

Het voorrecht bezwaart ook de inkomsten en de  roerende goederen van de echtgenoot of de wettelijk  samenwonende in de mate dat de invordering van de  aanslagen kan worden vervolgd op de bewuste  inkomsten en goederen.

§ 2. Om de invordering van de belastingen en toebehoren  te waarborgen, wordt inzake het successierecht  bovendien op al de nagelaten roerende goederen een  algemeen voorrecht ten bate van het Vlaamse Gewest  gesteld. Dat voorrecht vervalt na achttien maanden vanaf  de dag van het overlijden als het bevoegde personeelslid  geen gerechtelijke vervolging voor het einde van die  periode aangevangen heeft.

---- historiek ----  ---- historique ----

- §2 toegevoegd door art. 247 van het decreet van 19 dec.  2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in werking  getreden op 1 januari 2015 (art. 325)

###### Art. 3.10.5.2.2.  Art. 3.10.5.2.2.

De voorrechten, vermeld in artikel 3.10.5.2.1, nemen de  rang in onmiddellijk na het voorrecht, vermeld in artikel  19, 5°, van de Hypotheekwet van 16 december 1851.

De aanwending bij voorrang, vermeld in artikel 19 in  fine van de Hypotheekwet van 16 december 1851, is van  toepassing op de belastingen, vermeld in deze codex.

---- historiek ----  ---- historique ----

- eerste lid vervangen door art. 248 van het decreet van  19 dec. 2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

###### Art. 3.10.5.2.3.  Art. 3.10.5.2.3.

(…)  (…)

- opgeheven door art. 60 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- toegevoegd door art. 249 van het decreet van 19 dec.  2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in werking  getreden op 1 januari 2015 (art. 325)

##### Onderafdeling 3 - Wettelijke hypotheek  Sous-section 3 - Hypothèque légale

###### Art. 3.10.5.3.1.  Art. 3.10.5.3.1.

§ 1. De belastingen en toebehoren zijn gewaarborgd  door een wettelijke hypotheek op al de goederen in  België die toebehoren aan de belastingschuldige en die  vatbaar zijn daarvoor.

De hypotheek bezwaart ook de goederen van de  echtgenoot of de wettelijk samenwonende in de mate dat  de invordering van de aanslagen op de vermelde  goederen vervolgd mag worden.

§ 2. Bovendien wordt inzake de erfbelasting de  invordering van de belastingen en toebehoren,  gewaarborgd door een wettelijke hypotheek op al de  goederen die vatbaar zijn voor hypotheek, door de  erflater in België nagelaten.

---- historiek ----  ---- historique ----

- § 2 toegevoegd door art. 250 van het decreet van 19  dec. 2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in  werking getreden op 1 januari 2015 (art. 325)

###### Art. 3.10.5.3.2.  Art. 3.10.5.3.2.

§ 1. De wettelijke hypotheek, vermeld in artikel  3.10.5.3.1, § 1, neemt pas rang in vanaf haar  inschrijving.

§ 2. De wettelijke hypotheek, vermeld in artikel  3.10.5.3.1, § 2, kan zonder inschrijving aan derden  worden tegengeworpen gedurende een termijn van  achttien maanden vanaf de datum van het overlijden.

Ze behoudt haar uitwerking met ingang van dezelfde  datum als de inschrijving vóór het verstrijken van de  voormelde termijn gevorderd wordt. In dat geval wordt  de inschrijving genomen onder de naam van de erflater,

Na het verstrijken van die termijn neemt ze pas rang  vanaf de dag van de inschrijving.

§ 3. De wettelijke hypotheek schaadt geenszins de  vorige voorrechten en hypotheken.

---- historiek ----  ---- historique ----

- vervangen door art. 251 van het decreet van 19 dec.  2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in werking  getreden op 1 januari 2015 (art. 325)

###### Art. 3.10.5.3.3.  Art. 3.10.5.3.3.

De hypotheek wordt ingeschreven op verzoek van het  bevoegde personeelslid.

Behalve als de rechten van het Vlaamse Gewest in  gevaar verkeren en met behoud van de toepassing van  artikel 3.12.1.0.1 tot en met 3.12.1.0.10, mag de  inschrijving van de hypotheek, vermeld in artikel  3.10.5.3.1, § 1, pas gevorderd worden vanaf de  vervaldag van de gewaarborgde belastingen. De  inschrijving van de wettelijke hypotheek, vermeld in  artikel 3.10.5.3.1, § 2, kan gevorderd worden vanaf de  datum van het overlijden.

###### Art. XX.113. van het Wetboek van Economisch Recht

is niet van toepassing op de wettelijke hypotheek voor  de belastingen die opgenomen zijn in kohieren die vóór  het vonnis van faillietverklaring uitvoerbaar zijn  verklaard.

---- historiek ----  ---- historique ----

- gewijzigd door art. 42 van het decreet van 21.12.2018  (B.S. 28.12.2018). Tekst heeft uitwerking op  insolventieprocedures geopend vanaf 01.05.2018

- tweede lid vervangen door art. 252 van het decreet van  19 dec. 2014 (B.S., 29.01.2015 - Ed. 2). De tekst is

in werking getreden op 1 januari 2015 (art. 325)

###### Art. 3.10.5.3.4.  Art. 3.10.5.3.4.

De inschrijving van de hypotheek, vermeld in artikel  3.10.5.3.1, vindt plaats, niettegenstaande verzet,  betwisting of beroep, op voorlegging van een door het  bevoegde personeelslid voor echt verklaard afschrift van  het aanslagbiljet houdende vermelding van de datum van  de uitvoerbaarverklaring van het kohier.

Bij gebrek aan een aanslagbiljet kan de inschrijving van  de hypotheek, vermeld in artikel 3.10.5.3.1, § 2, inzake  de erfbelasting plaatsvinden voor een door het bevoegde

---- historiek ----  ---- historique ----

- vervangen door art. 253 van het decreet van 19 dec.  2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in werking  getreden op 1 januari 2015 (art. 325)

###### Art. 3.10.5.3.5.  Art. 3.10.5.3.5.

Met behoud van de toepassing van artikel 87 van de  Hypotheekwet van 16 december 1851 kan de  inschrijving worden gevorderd voor een door het  bevoegde personeelslid in het borderel te bepalen bedrag  dat  al  de  nalatigheidsinteresten  en  kosten  vertegenwoordigt die voor de vereffening van de  belasting verschuldigd zouden kunnen zijn.

###### Art. 3.10.5.3.6.  Art. 3.10.5.3.6.

Het bevoegde personeelslid verleent handlichting in de  administratieve vorm zonder dat hij ertoe gehouden is  verantwoording van de betaling van de verschuldigde  sommen te verstrekken.

---- historiek ----  ---- historique ----

- gewijzigd door art. 43 van het decreet van 21.12.2018  (B.S. 28.12.2018). Tekst treedt in werking op 07.01.2019

###### Art. 3.10.5.3.7.  Art. 3.10.5.3.7.

Als de betrokkenen, voor ze de bedragen betaald hebben  die door de wettelijke hypotheek gewaarborgd zijn, alle  bezwaarde goederen of een deel ervan willen vrijmaken  van de hypotheek, dienen ze daarvoor een verzoek in bij  het bevoegde personeelslid. Dat verzoek wordt  ingewilligd als het Vlaamse Gewest al voldoende  zekerheid bezit, of als die eraan wordt gegeven, voor het  bedrag dat verschuldigd is aan het Vlaamse Gewest.

###### Art. 3.10.5.3.8.  Art. 3.10.5.3.8.

De kosten van de formaliteiten voor de wettelijke  hypotheek, vermeld in artikel 3.10.5.3.1, § 1, zijn ten  laste van de belastingschuldige.

De kosten van de formaliteiten voor de wettelijke  hypotheek, vermeld in artikel 3.10.5.3.1, § 2, zijn ten  laste van het Vlaamse Gewest, behalve in geval van  uitwinning van de onroerende goederen die bezwaard  zijn met die hypotheek. In dat laatste geval zijn de kosten  ten laste van de belastingschuldige.

---- historiek ----  ---- historique ----

##### Onderafdeling 4 - Rechten van derden te goeder trouw  Sous-section 4 - Droits de tiers de bonne foi

---- historiek ----  ---- historique ----

- onderafdeling 4 toegevoegd door art. 255 van het  decreet van 19 dec. 2014 (B.S., 29.01.2015 - Ed. 2). De  tekst is in werking getreden op 1 januari 2015 (art.

325)

###### Art. 3.10.5.4.1.  Art. 3.10.5.4.1.

Als binnen achttien maanden na het openvallen van de  nalatenschap een derde te goeder trouw een goed van de  nalatenschap, een zakelijk recht, een hypotheek, een  pand of een inpandgeving op een dergelijk goed onder  bezwarende titel verkregen heeft nadat de ingeleverde  aangifte definitief geworden is, hetzij door het  verstrijken van de termijn van inlevering, hetzij  ingevolge het afstand doen van de aangevers van het  recht van verbetering, of nadat de erfbelasting  ambtshalve is gevestigd met toepassing van artikel  2.7.7.0.1, kunnen het voorrecht en de wettelijke  hypotheek, vermeld in artikel 3.10.5.3.1, § 2, niet aan de  derde tegengeworpen worden voor de invordering van  de belastingen en toebehoren die betrekking hebben op  de aanvullende rechten.

Het eerste lid is evenwel niet van toepassing in de  volgende gevallen :

1° als vóór de verkrijging een verbeterende aangifte  ingediend is of een gerechtelijke vervolging door het  bevoegde personeelslid ingespannen is wegens de  invordering van de belastingen en toebehoren die  betrekking hebben op de aanvullende rechten;

2° als daartoe al een inschrijving ten bate van het  Vlaamse Gewest genomen is.

De erfgenamen, legatarissen en begiftigden, en de  openbare of ministeriële ambtenaren en officieren die  ermee belast zijn de goederen van de nalatenschap te  verkopen of te hypothekeren, kunnen aan het bevoegde  personeelslid een attest vragen dat de erfbelasting  vermeldt die verschuldigd is wegens de ingeleverde  aangiften.

Dat attest moet binnen een maand na de aanvraag  worden verstrekt.

---- historiek ----  ---- historique ----

##### Onderafdeling 5 - Buiten de Europese Economische Ruimte

wonende erfgenaam

---- historiek ----  ---- historique ----

- onderafdeling 5 toegevoegd door art. 257 van het  decreet van 19 dec. 2014 (B.S., 29.01.2015 - Ed. 2). De  tekst is in werking getreden op 1 januari 2015 (art.

325)

###### Art. 3.10.5.5.1.  Art. 3.10.5.5.1.

Onverminderd de zekerheden, vermeld in artikel  3.10.5.2.1 en 3.10.5.3.1, is iedere persoon die buiten de  Europese Economische Ruimte woont en die erfgenaam,  legataris of begiftigde is in de nalatenschap van roerende  goederen van een rijksinwoner, ertoe verplicht inzake  het successierecht een borg te stellen voor de betaling  van de belastingen en toebehoren waartoe hij tegenover  het Vlaamse Gewest gehouden is.

Het bedrag van de borgstelling wordt bepaald door het  bevoegde personeelslid. Het bevoegde personeelslid  mag de erfgenaam, legataris of begiftigde die buiten de  Europese Economische Ruimte woont, ervan ontslaan  de borgstelling te verstrekken.

De zegels die overeenkomstig artikel 1148 tot en met  1151 van het Gerechtelijk Wetboek gelegd zijn, mogen  niet gelicht worden en geen openbare of ministeriële  ambtenaar of officier mag de goederen van de  nalatenschap verkopen, noch er de akte van verdeling  van opmaken, vóór de aflevering van een getuigschrift  van het bevoegde personeelslid, waaruit blijkt dat de  erfgenaam die buiten de Europese Economische Ruimte  woont, zich naar de bepalingen van dit artikel gedragen  heeft, op straffe van alle kosten en schadevergoedingen.  Dat getuigschrift wordt gevoegd bij het proces-verbaal  van de verkoop van de goederen van de nalatenschap of  bij de akte van verdeling.

---- historiek ----  ---- historique ----

- toegevoegd door art. 258 van het decreet van 19 dec.  2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in werking  getreden op 1 januari 2015 (art. 325)

###### Art. 3.10.5.5.2.  Art. 3.10.5.5.2.

De inschrijvingen, effecten op naam of aan toonder,  sommen, waarden, gesloten koffers, omslagen en colli's,  vermeld in artikel 96 tot en met 99 van het federale  Wetboek van Successierechten, mogen niet het

Als in de gevallen, vermeld in artikel 101 van het  federale Wetboek van Successierechten, onder de  rechthebbenden een of meer personen zijn die buiten de  Europese Economische Ruimte wonen, mag de  verhuurder van de brandkast of de notaris die de door het  voormelde artikel voorgeschreven lijst of inventaris  heeft  opgemaakt,  de  inbezitneming  door  de  rechthebbenden van de in de kast liggende zaken niet  toestaan voordat de door artikel 3.10.5.5.1 opgelegde  waarborg is gesteld.

In afwijking van het eerste lid en voor de waarborg,  opgelegd door artikel 3.10.5.5.1, is gesteld, mag de  schuldenaar van deposito's op een gemeenschappelijke  of onverdeelde zicht- of spaarrekening waarvan de  erflater of de langstlevende echtgenoot houder of  medehouder is of waarvan de langstlevende wettelijk  samenwonende medehouder is, overeenkomstig de bij  artikel 4.65 van het Burgerlijk Wetboek bepaalde nadere  regels een bedrag ter beschikking stellen dat de helft van  de beschikbare creditsaldi noch 5000 euro overschrijdt.

Het bedrag, vermeld in het derde lid, wordt uitbetaald  onverminderd de betaling van de bevoorrechte kosten,  vermeld in artikel 19 en artikel 20 van de Hypotheekwet  van 16 december 1851.

---- historiek ----  ---- historique ----

- gewijzigd door art. 12 van het decreet van 15.03.2024  (B.S. 20.03.2024). Inwerkingtreding: 30.03.2024

- toegevoegd door art. 259 van het decreet van 19 dec.  2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in werking  getreden op 1 januari 2015 (art. 325)

### Hoofdstuk 11 - Wederzijdse internationale bijstand  Chapitre 11 - Assistance internationale mutuelle

###### Art. 3.11.0.0.1.  Art. 3.11.0.0.1.

Voorbehouden voor toekomstig gebruik.  Réservé pour un usage futur

#### Afdeling 1 - Notificatieverplichtingen van derden  Section 1re - Obligations de notification de tiers

###### Art. 3.12.1.0.1.  Art. 3.12.1.0.1.

De notarissen die een akte moeten opmaken die de  vervreemding of de hypothecaire aanwending van een  onroerend goed, van een schip of een vaartuig tot  voorwerp heeft, zijn persoonlijk aansprakelijk voor de

Les notaires requis de dresser un acte ayant pour objet  l'aliénation ou l'affectation hypothécaire d'un immeuble,  d'un bateau ou d'une embarcation, sont personnellement  responsables du paiement des impôts et accessoires

1° de bevoegde entiteit van de Vlaamse administratie  door  middel  van  een  procedure  waarbij  informaticatechnieken gebruikt worden;

2° het bevoegde personeelslid in het ambtsgebied van  wie de eigenaar of de vruchtgebruiker van het goed zijn  woonplaats  of  zijn  hoofdinrichting  heeft  en  daarenboven, als het om een onroerend goed gaat, het  bevoegde personeelslid in het ambtsgebied van wie dat  goed ligt, als het bericht niet meegedeeld kan worden op  de wijze, vermeld in 1°. In dat geval moet het bericht  met een aangetekende brief met ontvangstmelding  worden verzonden.

Als die akte niet verleden wordt binnen drie maanden na  de verzending van het bericht, wordt ze als niet bestaand  beschouwd. Als het bericht meegedeeld is op de wijze,  vermeld in het eerste lid, 1°, wordt onder de datum van  verzending van het bericht verstaan de datum van  ontvangstmelding, meegedeeld door de bevoegde  entiteit van de Vlaamse administratie.

Als hetzelfde bericht achtereenvolgens wordt verstuurd  op de wijze, vermeld in het eerste lid, 1° en 2°, zal het  bericht, opgesteld conform het eerste lid, 2°, alleen  primeren als de datum van toezending vroeger is dan de  verzendingsdatum van het bericht, opgesteld conform  het eerste lid, 1°.

---- historiek ----  ---- historique ----

- eerste lid, 2° gewijzigd door art. 260 van het decreet  van 19 dec. 2014 (B.S., 29.01.2015 - Ed. 2). De tekst is

in werking getreden op 1 januari 2015 (art. 325)

###### Art. 3.12.1.0.2.  Art. 3.12.1.0.2.

Vóór het verstrijken van de tiende werkdag die volgt op  de verzending van het bericht, vermeld in artikel  3.12.1.0.1, wordt door het bevoegde personeelslid aan  de notaris kennisgegeven van het bedrag van de  belastingen en toebehoren die aanleiding kunnen geven  tot inschrijving van de wettelijke hypotheek van het  Vlaamse Gewest op de goederen die het voorwerp van  de akte zijn, op een van de volgende wijzen :

1° door gebruikmaking van informaticatechnieken;  1° en utilisant des techniques informatiques ;

2° met een aangetekende brief met ontvangstmelding.  2° par lettre recommandée avec accusé de réception.

Als de kennisgeving heeft plaatsgevonden op de wijze,  vermeld in het eerste lid, 1°, wordt onder de datum van  verzending van die kennisgeving verstaan, de datum van

Als dezelfde kennisgeving achtereenvolgens wordt  verstuurd op de wijzen, vermeld in het eerste lid, 1° en  2°, zal de kennisgeving, opgesteld conform het eerste  lid, 2°, alleen primeren als de datum van toezending  vroeger  is  dan  de  verzendingsdatum  van  de  kennisgeving, opgesteld conform het eerste lid, 1°.

---- historiek ----  ---- historique ----

- gewijzigd door art. 13 van het decreet van 15.03.2024  (B.S. 20.03.2024). Inwerkingtreding: 30.03.2024

###### Art. 3.12.1.0. 2, eerste lid van de Vlaamse Codex

Fiscaliteit van 13 december 2013, zoals van kracht vanaf  de inwerkingtreding van het decreet van 15.03.2024, is  van toepassing voor alle situaties waarin de berichten,  vermeld in artikel 3.12.1.0.1 en 3.12.1.0.16 van de  voormelde codex, verzonden worden na 1 april 2024.  (art. 21 van het decreet van 15.03.2024 (B.S.,  20.03.2024))

- tweede lid gewijzigd door art. 17 van het decreet van 19  dec. 2014 (B.S., 13.01.2015). De tekst is in werking  getreden op 01.01.2015. (art. 24)

- eerste lid, 2° gewijzigd door art. 261 van het decreet  van 19 dec. 2014 (B.S., 29.01.2015 - Ed. 2). De tekst is

in werking getreden op 1 januari 2015 (art. 325)

###### Art. 3.12.1.0.3.  Art. 3.12.1.0.3.

§ 1. Als de akte, vermeld in artikel 3.12.1.0.1, verleden  is, geldt de kennisgeving, vermeld in artikel 3.12.1.0.2,  als beslag onder derden in handen van de notaris op de  bedragen en waarden die hij krachtens de akte onder zich  houdt  voor  rekening  of  ten  bate  van  de  belastingschuldige, en als verzet tegen de prijs als  vermeld in artikel 1642 van het Gerechtelijk Wetboek,  in de gevallen waarin de notaris gehouden is de bedragen  en waarden conform artikel 1639 tot en met 1654 van  het Gerechtelijk Wetboek te verdelen.

Met behoud van de rechten van derden is de notaris ertoe  gehouden, als de akte, vermeld in artikel 3.12.1.0.1,  verleden is, behalve in geval van de toepassing van  artikel 1639 tot en met 1654 van het Gerechtelijk  Wetboek, de bedragen en waarden die hij krachtens de  akte onder zich houdt voor rekening of ten bate van de  belastingschuldige, uiterlijk de zevende werkdag die  volgt op het verlijden van de akte, aan de bevoegde  entiteit van de Vlaamse administratie te betalen voor het  bedrag van de belastingen en toebehoren die hem ter  uitvoering van artikel 3.12.1.0.2 ter kennis zijn gebracht  en in zoverre deze belastingen en toebehoren niet betwist  worden.

2° het bevoegde personeelslid met een aangetekende  brief met ontvangstmelding, als de inlichtingen niet  kunnen worden verstrekt op de wijze, vermeld in 1°, of  als de notaris voorafgaandelijk het bericht, vermeld in  artikel 3.12.1.0.1, met een aangetekende brief met  ontvangstmelding heeft verstuurd.

De datum van de inlichting is, naargelang het geval, de  datum van ontvangstmelding, meegedeeld door de  bevoegde entiteit van de Vlaamse administratie, of de  datum van ontvangstmelding van de aangetekende brief.

§ 2. Als dezelfde inlichting achtereenvolgens wordt  verstuurd op de wijzen, vermeld in paragraaf 1, derde  lid, 1° en 2°, zal de inlichting, opgesteld conform  paragraaf 1, derde lid, 2°, alleen primeren als de datum  van toezending vroeger is dan de verzendingsdatum van  de inlichting, opgesteld conform paragraaf 1, derde lid,  1°.

§ 3. Met behoud van de rechten van derden kan de  overschrijving of de inschrijving van de akte niet tegen  het Vlaamse Gewest ingeroepen worden als de  inschrijving van de wettelijke hypotheek plaatsvindt  binnen zeven werkdagen na de datum van de inlichting,  vermeld in paragraaf 1, vierde lid.

Alle niet-ingeschreven schuldvorderingen waarvoor pas  na het verstrijken van de termijn, vermeld in paragraaf  1, derde lid, beslag wordt gelegd of verzet wordt  aangetekend, zijn zonder uitwerking ten opzichte van de  schuldvorderingen inzake belastingen en toebehoren,  die ter uitvoering van artikel 3.12.1.0.2 ter kennis zijn  gegeven.

---- historiek ----  ---- historique ----

- gewijzigd door art. 14 van het decreet van 15.03.2024  (B.S. 20.03.2024). Inwerkingtreding: 30.03.2024

###### Art. 3.12.1.0.3. van de Vlaamse Codex Fiscaliteit van

13 december 2013, zoals van kracht vanaf de  inwerkingtreding van het decreet van 15.03.2024, is van  toepassing voor alle situaties waarin de berichten,  vermeld in artikel 3.12.1.0.1 en 3.12.1.0.16 van de  voormelde codex, verzonden worden na 1 april 2024.  (art. 21 van het decreet van 15.03.2024 (B.S.,  20.03.2024))

- derde lid, 2° en vierde lid gewijzigd door art. 262 van  het decreet van 19 dec. 2014 (B.S., 29.01.2015 - Ed. 2).  De tekst is in werking getreden op 1 januari 2015 (art.  325)

De inschrijvingen, genomen na de termijn, vermeld in  artikel 3.12.1.0.3, § 3, eerste lid, of tot zekerheid van  belastingen die niet overeenkomstig artikel 3.12.1.0.2  ter kennis zijn gegeven, kunnen niet worden ingeroepen  tegen de hypothecaire schuldeisers, noch tegen de  verkrijger die handlichting ervan zal kunnen vorderen.

Les inscriptions, faites après le délai, cité dans l'article  3.12.1.0.3, § 3, alinéa premier, ou prise en sureté des  impôts qui n'ont pas été notifiés conformément à l'article  3.12.1.0.2, ne peuvent pas être invoquées contre les  créanciers hypothécaires, ni contre l'attributaire qui  pourra en demander la mainlevée.

###### Art. 3.12.1.0.5.  Art. 3.12.1.0.5.

###### Art. 3.12.1.0.6.  Art. 3.12.1.0.6.

§ 1. De Vlaamse Regering kan voor de berichten en  inlichtingen, vermeld in artikel 3.12.1.0.1 en 3.12.1.0.3,  de modellen vaststellen.

§ 2. De informatie in de berichten, kennisgevingen en  inlichtingen, vermeld in artikel 3.12.1.0.1 tot en met  3.12.1.0.3, is dezelfde, ongeacht of ze worden  meegedeeld door middel van een procedure waarbij  informaticatechnieken worden gebruikt, of met een  aangetekende brief met ontvangstmelding.

Bij de verzending van de berichten, inlichtingen en  kennisgevingen, vermeld in het eerste lid, gericht tot of  afkomstig van het bevoegde personeelslid of de  bevoegde entiteit van de Vlaamse administratie, worden  de betrokken personen geïdentificeerd aan de hand van  het identificatienummer, vermeld in artikel III.17 van  het Wetboek van Economisch Recht, als het gaat om een  rechtspersoon, en het rijksregisternummer als het gaat  om  een  natuurlijke  persoon  en  van  het  identificatienummer, vermeld in artikel 8 van de wet van  15 januari 1990 houdende oprichting en organisatie van  een Kruispuntbank van de sociale zekerheid.

§ 3. De oorsprong en de integriteit van de inhoud van de  berichten, inlichtingen en kennisgevingen, vermeld in  artikel 3.12.1.0.1 tot en met 3.12.1.0.3, moeten, in geval  van verzending door middel van een procedure waarbij  informaticatechnieken  worden  gebruikt,  worden  verzekerd met aangepaste beveiligingstechnieken.

§ 4. Opdat de kennisgevingen, vermeld in artikel  3.12.1.0.2, op geldige wijze als beslag onder derden  zouden gelden als ze worden verzonden door middel van  een procedure waarbij informaticatechnieken worden  gebruikt, moeten ze een elektronische handtekening  dragen, die met een van de volgende technieken wordt  aangebracht :

1° creatie van een elektronische handtekening met  behulp van een Belgische elektronische identiteitskaart;

2° creatie van een digitale handtekening met behulp van  een private sleutel, toegekend aan een bevoegde  personeelslid, waarbij een certificaat gevoegd is dat  uitgereikt is aan dat personeelslid, waarbij zowel de  private sleutel als het certificaat op een beveiligde wijze  in het geheugen van een computer is opgeslagen;

4° creatie van een geavanceerde elektronische  handtekening als vermeld in artikel 2, 2°, van de wet van  9 juli 2001 houdende vaststelling van bepaalde regels in  verband met het juridisch kader voor elektronische  handtekeningen en certificatiediensten.

Ongeacht de toegepaste techniek wordt er gegarandeerd  dat alleen de gerechtigde personen toegang hebben tot  de middelen waarmee de handtekening wordt gecreëerd.

De gevolgde procedures moeten bovendien toelaten dat  de natuurlijke persoon die verantwoordelijk is voor de  verzending, correct kan worden geïdentificeerd en dat  het tijdstip van de verzending correct kan worden  vastgesteld. Die gegevens moeten gedurende een  periode van tien jaar door de afzender worden bewaard  en in geval van betwisting binnen een redelijke termijn  worden voorgelegd.

---- historiek ----  ---- historique ----

- gewijzigd door art. 29 van het decreet van 08.12.2017  (B.S.: 14.12.2017). Tekst van toepassing vanaf  24.12.2017

- § 2, eerste lid gewijzigd door art. 263 van het decreet  van 19 dec. 2014 (B.S., 29.01.2015 - Ed. 2). De tekst is

in werking getreden op 1 januari 2015 (art. 325)

###### Art. 3.12.1.0.7.  Art. 3.12.1.0.7.

###### Art. 3.12.1.0.1. tot en met 3.12.1.0.6 zijn van

toepassing op elke persoon die bevoegd is om de  authenticiteit te verlenen aan de akten, vermeld in artikel  3.12.1.0.1.

###### Art. 3.12.1.0.8.  Art. 3.12.1.0.8.

Met het akkoord van de belastingschuldige zijn de  banken die onderworpen zijn aan de wet van 25 april  2014 op het statuut van en het toezicht op  kredietinstellingen en beursvennootschappen, en ook de  kredietgevers en bemiddelaars inzake hypothecair  krediet die onderworpen zijn aan boek VII, titel 4,  hoofdstuk 4, van het Wetboek van economisch recht,  gemachtigd het bericht, vermeld in artikel 3.12.1.0.1, toe  te sturen en in staat om de kennisgeving,  vermeld in artikel 3.12.1.0.2, te ontvangen.

---- historiek ----  ---- historique ----

- gewijzigd door art. 61 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

###### Art. 3.12.1.0.9.  Art. 3.12.1.0.9.

Geen akte die in het buitenland verleden is en de  vervreemding of de hypothecaire aanwending van een  onroerend goed, een schip of een vaartuig tot voorwerp  heeft, wordt in België tot overschrijving of inschrijving  in de registers van de hypothecaire openbaarmaking of  in de registers van het Belgisch Scheepsregister  toegelaten, als er niet een attest bij gevoegd is van het  bevoegde personeelslid in het ambtsgebied van wie het  onroerend goed ligt en, in voorkomend geval, van het  bevoegde personeelslid in het ambtsgebied van wie de  betrokkene zijn woonplaats of zijn hoofdinrichting  heeft.

Het attest, vermeld in het eerste lid, geeft er blijk van dat  de eigenaar of de vruchtgebruiker geen belastingen  schuldig is of dat de wettelijke hypotheek die de  verschuldigde belastingen waarborgt, ingeschreven is.

---- historiek ----  ---- historique ----

- gewijzigd door art. 44 van het decreet van 21.12.2018  (B.S. 28.12.2018). Tekst treedt in werking op 07.01.2019

###### Art. 3.12.1.0.10.  Art. 3.12.1.0.10.

Openbare ambtenaren of ministeriële officieren, belast  met de openbare verkoping van roerende goederen  waarvan de waarde ten minste 2500 euro bedraagt, zijn  persoonlijk aansprakelijk voor de betaling van de  belastingen en toebehoren die de eigenaar op het  ogenblik van de verkoping schuldig is, als ze niet ten  minste zeven werkdagen vooraf de volgende instanties  of personen verwittigen op de volgende wijze:

1° de bevoegde entiteit van de Vlaamse administratie  door  middel  van  een  procedure  waarbij  informaticatechnieken gebruikt worden;

2° het bevoegde personeelslid van de woonplaats of van  de  hoofdinrichting  van  de  eigenaar  met  een  aangetekende brief met ontvangstmelding als het bericht  niet meegedeeld kan worden op de wijze, vermeld in 1°.

---- historiek ----  ---- historique ----

- gewijzigd door art. 15 van het decreet van 15.03.2024  (B.S. 20.03.2024). Inwerkingtreding: 30.03.2024

###### Art. 3.12.1.0. 10, eerste lid, van de Vlaamse Codex

Fiscaliteit van 13 december 2013, zoals van kracht vanaf  de inwerkingtreding van het decreet van 15.03.2024, is  van toepassing voor alle situaties waarin het bericht van  de openbare verkoop van roerende goederen, vermeld in  artikel 3.12.1.0.10 van de voormelde codex, verzonden  wordt na 1 april 2024. (art. 21 van het decreet van  15.03.2024 (B.S., 20.03.2024))

- eerste lid, 2° gewijzigd door art. 264 van het decreet  van 19 dec. 2014 (B.S., 29.01.2015 - Ed. 2). De tekst is

in werking getreden op 1 januari 2015 (art. 325)

###### Art. 3.12.1.0.11.  Art. 3.12.1.0.11.

Als de verkoping heeft plaatsgevonden, geldt de  kennisgeving van het bedrag van de verschuldigde  bedragen, die uiterlijk daags vóór de verkoping  uitgevoerd wordt door de entiteit, vermeld in artikel  3.12.1.0.10, eerste lid, 1°, of door het bevoegde  personeelslid, vermeld in artikel 3.12.1.0.10, eerste lid,  2°, als beslag onder derden in handen van de openbare  ambtenaren of ministeriële officieren als vermeld in  artikel 3.12.1.0.10, eerste lid. De kennisgeving gebeurt:

1°  door  middel  van  een  procedure  waarbij  informaticatechnieken worden gebruikt;

2° met een aangetekende brief met ontvangstmelding,  als de kennisgeving niet op de wijze, vermeld in 1°, kan  worden verzonden.

Als de kennisgeving heeft plaatsgevonden conform het  eerste lid, 1°, wordt onder de datum van verzending van  die  kennisgeving  verstaan,  de  datum  van  ontvangstmelding die de Koninklijke Federatie van het  Belgisch Notariaat heeft meegedeeld.

Met behoud van de rechten van derden en behalve in  geval van de toepassing van artikel 1627 tot en met 1638  van het Gerechtelijk Wetboek, zijn de openbare  ambtenaren of ministeriële officieren gehouden de  bedragen en waarden die ze onder zich houden, uiterlijk  de zevende werkdag die volgt op de verkoping, te betalen  aan de bevoegde entiteit van de Vlaamse administratie  ten bedrage van de belastingen en toebehoren die de  openbare ambtenaar of de ministeriële officier ter  uitvoering van het eerste lid ter kennis zijn gebracht en  in zoverre deze belastingen en toebehoren niet betwist  worden.

---- historiek ----  ---- historique ----

- gewijzigd door art. 16 van het decreet van 15.03.2024  (B.S. 20.03.2024). Inwerkingtreding: 30.03.2024

###### Art. 3.12.1.0. 11, vierde lid, van de Vlaamse Codex

Fiscaliteit van 13 december 2013, zoals van kracht vanaf  de inwerkingtreding van het decreet van 15.03.2024, is  van toepassing voor alle situaties waarin het bericht van  de openbare verkoop van roerende goederen, vermeld in  artikel 3.12.1.0.10 van de voormelde codex, verzonden  wordt na 1 april 2024. (art. 21 van het decreet van  15.03.2024 (B.S., 20.03.2024))

- tweede lid gewijzigd door art. 18 van het decreet van 19  dec. 2014 (B.S., 13.01.2015). De tekst is in werking  getreden op 01.01.2015. (art. 24)

- eerste lid, 2° gewijzigd door art. 265 van het decreet  van 19 dec. 2014 (B.S., 29.01.2015 - Ed. 2). De tekst is

in werking getreden op 1 januari 2015 (art. 325)

###### Art. 3.12.1.0.12.  Art. 3.12.1.0.12.

De aansprakelijkheid door de openbare ambtenaren en  ministeriële officieren, opgelopen met toepassing van  artikel 3.12.1.0.10 en 3.12.1.0.11, gaat, naargelang het  geval, de waarde van de verkochte goederen, na aftrek  van de sommen en waarden waarop in hun handen  beslag onder derden werd gelegd, niet te boven.

###### Art. 3.12.1.0.13.  Art. 3.12.1.0.13.

§ 1. De Vlaamse Regering kan voor de berichten en  inlichtingen, vermeld in het artikel 3.12.1.0.10, de  modellen vaststellen.

Bij de verzending van de berichten, inlichtingen en  kennisgevingen, vermeld in het eerste lid, gericht tot of  afkomstig van het bevoegde personeelslid of de  bevoegde entiteit van de Vlaamse administratie, worden  de betrokken personen geïdentificeerd aan de hand van  het identificatienummer, vermeld in artikel III.17 van  het Wetboek van Economisch Recht, als het gaat om een  rechtspersoon,  en  aan  de  hand  van  het  rijksregisternummer als het gaat om een natuurlijke  persoon, en aan de hand van het identificatienummer,  vermeld in artikel 8 van de wet van 15 januari 1990  houdende  oprichting  en  organisatie  van  een  Kruispuntbank van de sociale zekerheid.

§ 3. De oorsprong en de integriteit van de inhoud van de  berichten, inlichtingen en kennisgevingen, vermeld in  artikel 3.12.1.0.10 en 3.12.1.0.11, moeten, in geval van  verzending door middel van een procedure waarbij  informaticatechnieken  worden  gebruikt,  worden  verzekerd met aangepaste beveiligingstechnieken.

§ 4. Opdat de kennisgevingen, vermeld in artikel  3.12.1.0.11, op geldige wijze als beslag onder derden  zouden gelden als ze worden verzonden door middel van  een procedure waarbij informaticatechnieken worden  gebruikt, moeten ze een elektronische handtekening  dragen, die met een van de volgende technieken wordt  aangebracht ;

1° creatie van een elektronische handtekening met  behulp van een Belgische elektronische identiteitskaart;

2° creatie van een digitale handtekening met behulp van  een private sleutel, toegekend aan een bevoegde  personeelslid, waarbij een certificaat is gevoegd dat  uitgereikt is aan dat personeelslid, waarbij zowel de  private sleutel als het certificaat op een beveiligde wijze  in het geheugen van een computer is opgeslagen;

3° creatie van een digitale handtekening met behulp van  een private sleutel, toegekend aan de bevoegde entiteit  van de Vlaamse administratie, vermeld in artikel  3.12.1.0.11, waarbij een certificaat gevoegd is dat  uitgereikt is aan die entiteit, waarbij zowel de private  sleutel als het certificaat op een beveiligde wijze in het  geheugen van een computer is opgeslagen;

Ongeacht de toegepaste techniek wordt er gegarandeerd  dat alleen de gerechtigde personen toegang hebben tot  de middelen waarmee de handtekening wordt gecreëerd.

De gevolgde procedures moeten bovendien toelaten dat  de natuurlijke persoon die verantwoordelijk is voor de  verzending, correct kan worden geïdentificeerd en dat  het tijdstip van de verzending correct kan worden  vastgesteld.

Die gegevens moeten gedurende een periode van tien  jaar door de afzender worden bewaard en in geval van  betwisting binnen een redelijke termijn worden  voorgelegd.

---- historiek ----  ---- historique ----

- gewijzigd door art. 29 van het decreet van 08.12.2017  (B.S.: 14.12.2017). Tekst van toepassing vanaf  24.12.2017

- § 2, eerste lid gewijzigd door art. 266 van het decreet  van 19 dec. 2014 (B.S., 29.01.2015 - Ed. 2). De tekst is

in werking getreden op 1 januari 2015 (art. 325)

###### Art. 3.12.1.0.14.  Art. 3.12.1.0.14.

§ 1. Met behoud van de toepassing van artikel 3.12.1.0.1  tot en met 3.12.1.0.8 is de overdracht in eigendom of in  vruchtgebruik van een geheel van goederen,  samengesteld uit onder meer elementen die het behoud  van de clientèle mogelijk maken, die voor de uitoefening  van een vrij beroep, ambt of post of een industrieel,  handels- of landbouwbedrijf worden aangewend, alsook  de vestiging van een vruchtgebruik op dezelfde  goederen,  pas  tegenstelbaar  aan  de  bevoegde  personeelsleden na verloop van de maand die volgt op  de maand waarin een eensluidend verklaard afschrift van  de akte tot overdracht of vestiging ter kennis is gebracht  van het bevoegde personeelslid van de woonplaats of  van de zetel van de overdrager.

§ 2. De overnemer is hoofdelijk aansprakelijk voor de  betaling van de belastingschulden, verschuldigd door de  overdrager na verloop van de termijn, vermeld in  paragraaf 1, voor het bedrag dat al door hem is betaald  of verstrekt, of voor een bedrag dat overeenstemt met de  nominale waarde van de aandelen die in ruil voor de  overdracht zijn toegekend vóór de afloop van de  voormelde termijn.

De uitreiking van dat certificaat is afhankelijk van een  aanvraag die de overdrager in tweevoud heeft ingediend  bij het bevoegde personeelslid van de belastingen van de  woonplaats of de zetel van de overdrager.

Het certificaat wordt geweigerd door het bevoegde  personeelslid als de overdrager bedragen verschuldigd  blijft als belastingen en toebehoren op de dag van de  aanvraag of als de aanvraag is ingediend na de  aankondiging van of tijdens een belastingonderzoek of  na het verzenden van een verzoek om inlichtingen.

Het certificaat wordt ofwel uitgereikt ofwel geweigerd  binnen een termijn van dertig dagen na de indiening van  de vraag van de overdrager.

§ 4. De overdrachten die worden uitgevoerd door een  curator, een gerechtsmandataris, belast met het  organiseren en realiseren van een overdracht onder  gerechtelijk gezag met toepassing van artikel XX.85 van  het Wetboek van Economisch Recht of in geval van  fusie, splitsing, inbreng van de algemeenheid van  goederen of van een tak van werkzaamheid, verricht  overeenkomstig de bepalingen van het Wetboek van  vennootschappen  en  verenigingen,  zijn  niet  onderworpen aan de bepalingen van dit artikel.

§ 5. De Vlaamse Regering kan modellen vaststellen voor  de aanvraag en het certificaat, vermeld in dit artikel.

---- historiek ----  ---- historique ----

- gewijzigd door art. 62 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- gewijzigd door art. 45 van het decreet van 21.12.2018  (B.S. 28.12.2018). Tekst heeft uitwerking op  insolventieprocedures geopend vanaf 1 mei 2018

Iedere rechtspersoon of natuurlijke persoon die, al dan  niet samen met zijn echtgenoot of zijn wettelijk  samenwonende of zijn descendenten, ascendenten en  zijverwanten tot en met de tweede graad, onrechtstreeks  of onmiddellijk minstens 33 % bezit van de aandelen in  een binnenlandse vennootschap en die aandelen, of een  gedeelte daarvan, voor minstens 75 % overdraagt  uiterlijk in een tijdspanne van één jaar, is van rechtswege  hoofdelijk aansprakelijk voor de betaling van de  belastingschulden en toebehoren als het actief van de  vennootschap uiterlijk op de dag van de betaling van de  prijs van de aandelen voor ten minste 75 % bestaat uit  vorderingen, financiële vaste activa, geldbeleggingen of  liquide middelen.

De hoofdelijke aansprakelijkheid, vermeld in het eerste  lid, geldt alleen voor de belastingschulden en toebehoren  die betrekking hebben op:

1° het aanslagjaar waarin de overdracht van de aandelen  plaatsvindt;

2° de drie aanslagjaren voorafgaand aan de aanslagjaren  waarin de overdracht van de aandelen plaatsvindt.

Het eerste lid is niet van toepassing op de overgedragen  aandelen van een genoteerde vennootschap of van een  onderneming die onder het toezicht staat van de  Autoriteit voor Financiële Diensten en Markten.

###### Art. 3.12.1.0.16.  Art. 3.12.1.0.16.

§ 1. De notarissen die een akte of attest van erfopvolging  moeten opmaken overeenkomstig artikel 4.59 van het  Burgerlijk Wetboek, zijn persoonlijk aansprakelijk voor  de betaling van de schulden van de overledene, zijn  erfgenamen en legatarissen, van wie de identiteit  vermeld is in de akte of het attest, of de begunstigden  van een door hem gemaakte contractuele erfstelling, op  voorwaarde dat die schulden het onderwerp kunnen  uitmaken van een kennisgeving als vermeld in artikel  3.12.1.0.17 als ze daarvan geen bericht geven aan :

1° de bevoegde entiteit van de Vlaamse administratie  door  middel  van  een  procedure  waarbij  informaticatechnieken gebruikt worden;

Als het gaat om schulden ten laste van de overledene, is  de aansprakelijkheid, vermeld in het eerste lid, beperkt  tot de waarde van de nalatenschap. Als het gaat om  schulden ten laste van de rechtverkrijgenden, is de  aansprakelijkheid, vermeld in het eerste lid, beperkt tot  de waarde van de tegoeden die toekomen aan de  rechtverkrijgenden, van wie de identiteit vermeld is in  de akte of het attest, en voor welke bedragen de notaris  aansprakelijk kan worden gesteld.

Als die akte of dat attest niet wordt opgesteld binnen drie  maanden na de verzending van het bericht, wordt ze als  niet bestaand beschouwd.

Als hetzelfde bericht achtereenvolgens gegeven wordt  op de wijze, vermeld in het eerste lid, 1° en 2°, zal het  bericht dat opgesteld is conform het eerste lid, 2°, alleen  primeren als de datum van toezending vroeger is dan de  verzendingsdatum van het bericht dat wordt gegeven  conform het eerste lid, 1°.

Als het bericht gegeven wordt op de wijze, vermeld in  het eerste lid, 1°, wordt onder de datum van verzending  van  het  bericht  verstaan  de  datum  van  de  ontvangstmelding, meegedeeld door de bevoegde  entiteit van de Vlaamse administratie.

§ 2. Het bericht vermeldt de identiteit van de overledene,  van de erfgenamen of legatarissen, alsook de eventuele  begunstigde van een contractuele erfstelling.

Voor de toepassing van het eerste lid omvat de identiteit  :

1° voor natuurlijke personen : de voornaam, de  achternaam  en,  in  voorkomend  geval,  het  rijksregisternummer  of  het  identificatienummer,  vermeld in artikel 8 van de wet van 15 januari 1990  houdende  oprichting  en  organisatie  van  een  Kruispuntbank van de sociale zekerheid of, bij gebrek  aan dat nummer, de geboortedatum;

2° voor een rechtspersoon, een trust, een fiduciaire of  een soortgelijke rechtsvorm : de naam en zetel en, in  voorkomend geval, het ondernemingsnummer.

---- historiek ----  ---- historique ----

- gewijzigd door art. 63 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: nog te bepalen  door de Vlaamse Regering

- toegevoegd door art. 267 van het decreet van 19 dec.  2014 (B.S., 29.01.2015 - Ed. 2). De tekst treedt in  werking op een door de Vlaamse Regering te bepalen  datum (art. 325)

###### Art. 3.12.1.0.17.  Art. 3.12.1.0.17.

§ 1. Vóór het verstrijken van de tiende werkdag die volgt  op de datum van de verzending van het bericht, vermeld  in artikel 3.12.1.0.16, kan door het bevoegde  personeelslid aan de notaris, kennisgegeven worden van  het bestaan ten laste van de overledene of een andere  persoon, vermeld in het bericht, van een fiscale schuld  die onder het toepassingsgebied van deze codex valt en  die bestaat uit belastingen en toebehoren, met opgave  voor elk van de schuldenaars van het bedrag van die  schuld op een van de volgende wijzen :

1° door gebruikmaking van informaticatechnieken;  1° par l'utilisation de techniques informatiques ;

2° met een aangetekende brief met ontvangstmelding.  2° par une lettre recommandée avec accusé de réception.

Als de kennisgeving heeft plaatsgevonden op de wijze,  vermeld in het eerste lid, 1°, wordt onder de datum van  verzending van die kennisgeving verstaan de datum van  de ontvangstmelding, meegedeeld door de Koninklijke  Federatie van het Belgisch Notariaat.

Als dezelfde kennisgeving achtereenvolgens wordt  verstuurd op de wijzen, vermeld in het eerste lid, 1° en  2°, zal de kennisgeving, opgesteld conform het eerste  lid, 2°, alleen primeren als de datum van toezending  vroeger  is  dan  de  verzendingsdatum  van  de  kennisgeving, opgesteld conform het eerste lid, 1°.

§ 2. De kennisgeving vermeldt de identiteit van de  overledene, van de erfgenamen of legatarissen, alsook  van de eventuele begunstigde van een contractuele  erfstelling op de wijze, vermeld in artikel 3.12.1.0.16.

§ 3. Behalve als de rechten van het Vlaamse Gewest in  gevaar verkeren, mogen de schulden, vermeld in  paragraaf 1, pas meegedeeld worden vanaf de vervaldag  ervan.

---- historiek ----  ---- historique ----

- toegevoegd door art. 268 van het decreet van 19 dec.  2014 (B.S., 29.01.2015 - Ed. 2). De tekst treedt in  werking op een door de Vlaamse Regering te bepalen  datum (art. 325)

###### Art. 3.12.1.0.18.  Art. 3.12.1.0.18.

In het attest van erfopvolging of onderaan op de uitgifte  van de akte van erfopvolging wordt vermeld hetzij dat er  geen kennisgeving van schulden met toepassing van  artikel 3.12.1.0.17 is gedaan, zowel wat de overledene  betreft als wat een of meer personen betreft die vermeld  zijn in het bericht en die bestemmeling zijn van het attest  of de uitgifte, hetzij dat de schulden waarvan met  toepassing van artikel 3.12.1.0.17 is kennisgegeven, zijn  betaald of, in voorkomend geval, zullen worden betaald  met de tegoeden, gehouden door de schuldenaar.

De vermelding van de gedane of van de nog te verrichten  betaling wordt door de notaris onderaan op het attest  toegevoegd of vervolledigd.

De notaris die een attest van erfopvolging of een uitgifte  van een akte van erfopvolging aflevert waarin onjuiste  vermeldingen staan over het ontbreken van de  kennisgeving of over de betaling van schulden waarvan  van het bestaan ervan is kennisgegeven overeenkomstig  artikel 3.12.1.0.17, loopt dezelfde aansprakelijkheid op  als de notaris die de verplichting, vermeld in artikel  3.12.1.0.16, § 1, niet naleeft. Die aansprakelijkheid is  evenwel beperkt tot het bedrag dat als gevolg van die  onjuistheden niet kon worden ingevorderd.

---- historiek ----  ---- historique ----

- toegevoegd door art. 269 van het decreet van 19 dec.  2014 (B.S., 29.01.2015 - Ed. 2). De tekst treedt in  werking op een door de Vlaamse Regering te bepalen  datum (art. 325)

###### Art. 3.12.1.0.19.  Art. 3.12.1.0.19.

§ 1. Op straffe van persoonlijk aansprakelijk te zijn voor  de betaling van de belastingen en hun toebehoren,  waarvan is kennisgegeven met toepassing van artikel  3.12.1.0.17, kan iemand die tegoeden van een  overledene vrijgeeft overeenkomstig artikel 4.59 van het  Burgerlijk Wetboek, dat maar op een bevrijdende wijze  doen als duidelijk uit het attest van erfopvolging of uit  de uitgifte van de akte van erfopvolging blijkt dat geen  enkele kennisgeving als vermeld in artikel 3.12.1.0.17,  is gedaan.

1° dat minstens alle op naam van de overledene en alle  op naam van de erfgenaam, de legataris of de  begunstigde van een contractuele erfstelling onbetwiste  bestaande schulden, waarvan met toepassing van artikel  3.12.1.0.17 in voorkomend geval is kennisgegeven, zijn  betaald;

2° dat de tegoeden kunnen worden vrijgegeven aan de  erfgenaam, de legataris of de begunstigde van een  contractuele erfstelling na betaling, door middel van de  door de schuldenaar gehouden fondsen, van zijn  schulden en van zijn deel in de schulden van de  overledene waarvan is kennisgegeven, als die schulden  niet betwist worden.

§ 3. De aansprakelijkheid, vermeld in paragraaf 1, is  beperkt tot de waarde van de tegoeden die zijn  vrijgegeven aan de schuldenaars die zijn vermeld in de  kennisgeving, vermeld in artikel 3.12.1.0.17.

---- historiek ----  ---- historique ----

- gewijzigd door art. 19 van het decreet van 15.03.2024  (B.S. 20.03.2024). Inwerkingtreding: nog te bepalen door  de Vlaamse Regering (zie art. 22, lid 3 van het decreet  van 15.03.2024 (B.S., 20.03.2024))

- toegevoegd door art. 270 van het decreet van 19 dec.  2014 (B.S., 29.01.2015 - Ed. 2). De tekst treedt in  werking op een door de Vlaamse Regering te bepalen  datum (art. 325)

###### Art. 3.12.1.0.20.  Art. 3.12.1.0.20.

§ 1. De Vlaamse Regering kan voor de berichten en  kennisgevingen, vermeld in artikel 3.12.1.0.16 en  3.12.1.0.17, modellen vaststellen.

§2. De informatie in de berichten en kennisgevingen,  vermeld in artikel 3.12.1.0.16 en 3.12.1.0.17, is  dezelfde, ongeacht of ze worden meegedeeld door  middel  van  een  procedure  waarbij  informaticatechnieken worden gebruikt, of met een  aangetekende brief met ontvangstmelding.

§ 4. Opdat de kennisgevingen, vermeld in artikel  3.12.1.0.17, geldig zouden zijn als ze worden verzonden  door  middel  van  een  procedure  waarbij  informaticatechnieken worden gebruikt, moeten ze een  elektronische handtekening dragen, die met een van de  volgende technieken wordt aangebracht :

1° creatie van een elektronische handtekening met  behulp van een Belgische elektronische identiteitskaart;

2° creatie van een digitale handtekening met behulp van  een private sleutel, toegekend aan een bevoegd  personeelslid, waarbij een certificaat gevoegd is dat  uitgereikt is aan dat personeelslid, waarbij zowel de  private sleutel als het certificaat op een beveiligde wijze  in het geheugen van een computer is opgeslagen;

2° création d'une signature digitale à l'aide d'une clé  privée accordée à un membre du personnel compétent et  accompagnée d'un certificat délivré à ce membre du  personnel, où tant la clé privée que le certificat sont  stockés de manière sécurisée dans la mémoire d'un  ordinateur ;  3° creatie van een digitale handtekening met behulp van  een private sleutel, toegekend aan de bevoegde entiteit  van de Vlaamse administratie, waarbij een certificaat  gevoegd is dat uitgereikt is aan die entiteit, waarbij  zowel de private sleutel als het certificaat op een  beveiligde wijze in het geheugen van een computer is  opgeslagen;

4° creatie van een geavanceerde elektronische  handtekening als vermeld in artikel 2, 2°, van de wet van  9 juli 2001 houdende vaststelling van bepaalde regels in  verband met het juridisch kader voor elektronische  handtekeningen en certificatiediensten.

Ongeacht de toegepaste techniek wordt er gegarandeerd  dat alleen de gerechtigde personen toegang hebben tot  de middelen waarmee de handtekening wordt gecreëerd.

De gevolgde procedures moeten bovendien toelaten dat  de natuurlijke persoon die verantwoordelijk is voor de  verzending, correct kan worden geïdentificeerd en dat  het tijdstip van de verzending correct kan worden  vastgesteld.  Die  identificatiegegevens  moeten  gedurende een periode van tien jaar door de afzender  worden bewaard en in geval van betwisting binnen een  redelijke termijn worden voorgelegd.

---- historiek ----  ---- historique ----

- toegevoegd door art. 271 van het decreet van 19 dec.  2014 (B.S., 29.01.2015 - Ed. 2). De tekst treedt in  werking op een door de Vlaamse Regering te bepalen  datum (art. 325)

###### Art. 3.12.1.0.16. tot en met artikel 3.12.1.0.20 zijn van

overeenkomstige toepassing op elke persoon of dienst  die bevoegd is om een attest van erfopvolging op te  maken overeenkomstig artikel 4.59 van het Burgerlijk  Wetboek.

---- historiek ----  ---- historique ----

- gewijzigd door art. 20 van het decreet van 15.03.2024  (B.S. 20.03.2024). Inwerkingtreding: nog te bepalen door  de Vlaamse Regering (zie art. 22, lid 4 van het decreet  van 15.03.2024 (B.S., 20.03.2024))

- toegevoegd door art. 272 van het decreet van 19 dec.  2014 (B.S., 29.01.2015 - Ed. 2). De tekst treedt in  werking op een door de Vlaamse Regering te bepalen  datum (art. 325)

#### Afdeling 2 - Verplichtingen van kredietinstellingen of

-inrichtingen

###### Art. 3.12.2.0.1.  Art. 3.12.2.0.1.

Als openbare of private kredietinstellingen of -  inrichtingen kredieten, leningen of voorschotten  toekennen waarvoor een voordeel is verleend in het  kader van de regelgeving inzake economische expansie  of waarvoor een dergelijk voordeel is aangevraagd aan  de bevoegde overheid, mogen ze de fondsen noch geheel  noch gedeeltelijk vrijgeven, tenzij nadat de genieter of  aanvrager hun een attest heeft overgelegd dat is  uitgereikt door het bevoegde personeelslid en waaruit  een van de volgende feiten blijkt:

1° er zijn geen ingekohierde belastingen of toebehoren  waarvoor de betalingstermijn verstreken is;

2° er is een bepaald bedrag aan ingekohierde belastingen  of  toebehoren  verschuldigd  waarvoor  de  betalingstermijn verstreken is, in welk geval de betaling  van de verschuldigde bedragen, in de vorm en binnen de  termijnen, bepaald in het attest, het voorwerp moet  uitmaken van een bijzonder beding in de beslissing tot  toekenning van het voordeel.

#### Afdeling 3 - Andere verplichtingen in het kader van de

registratiebelasting

---- historiek ----  ---- historique ----

- afdeling 3 toegevoegd door art. 273 van het decreet van  19 dec. 2014 (B.S., 29.01.2015 - Ed. 2). De tekst is

in werking getreden op 1 januari 2015 (art. 325)

§ 1. Al naargelang de situatie verklaren de partijen in de  akte of het geschrift, of in een vermelding onderaan op  de akte of het geschrift, dat :

1°de voorwaarden van het abattement, vermeld in artikel  2.8.3.0.4, vervuld zijn;

2° de voorwaarden van het verlaagde tarief dat ze willen  verkrijgen, vervuld zijn;

3° de voorwaarden van hetzij de vermindering, hetzij de  vrijstelling die ze willen verkrijgen, vervuld zijn of  vervuld zullen worden;

4° ze de toepassing vragen van artikel 2.8.6.0.3, artikel  2.8.6.0.8, artikel 2.8.6.0.9, artikel 2.9.4.2.4, artikel  2.9.4.2.10, artikel 2.9.4.2.11, § 1, eerste lid, artikel  2.9.4.2.11, § 1, tweede lid, artikel 2.9.4.2.12, § 1, eerste  lid, artikel 2.9.4.2.12, § 1, vijfde lid, artikel 2.9.4.2.13,  artikel 2.9.4.2.14, artikel 2.9.4.2.15, artikel 2.9.5.0.1,  artikel 2.9.6.0.1, eerste lid, 4°, artikel 2.9.6.0.2, artikel  2.9.6.0.7, artikel 2.10.4.0.1, tweedelid, artikel  2.10.6.0.1, eerste lid, 2°, of artikel 2.10.6.0.2;

5° het geschonken onroerend goed een beschermd  monument is en dat het voornemen bestaat toepassing te  vragen van artikel 2.8.4.4.1.

5° le bien immobilier donné est un monument protégé  et que l’intention existe de demander application de  l’article 2.8.4.4.1.  § 2. Als partijen de toepassing vragen van het  abattement, vermeld in artikel 2.10.3.0.2, maken ze ook  melding van het aantal kinderen die recht geven op een  verhoging van het bedrag, vermeld in dat artikel, met  vermelding  van  hun  naam,  geboortedatum  en  afstammingsband.

§ 3. Als de partijen de toepassing van het tarief, vermeld  in artikel 2.8.4.4.1, § 1, van deze codex, inroepen, is  vereist dat de volgende elementen in de verklaring,  vermeld in paragraaf 1, worden vermeld:

1° het goedgekeurde beheersplan, vermeld in artikel  2.8.4.4.1, § 1, eerste lid, 2°, van deze codex, met opgave  van de referentie en ook de datum van de goedkeuring  van het beheersplan door het agentschap, vermeld in  artikel 2.1, 2°, van het Onroerenderfgoeddecreet van 12  juli 2013. Als het beheersplan nog niet is opgemaakt en  goedgekeurd op het moment waarop de authentieke akte  van schenking wordt verleden, wordt in de verklaring  vermeld dat er een beheersplan opgemaakt zal worden  als vermeld in artikel 8.1.1 tot en met 8.1.3 van het  Onroerenderfgoeddecreet van 12 juli 2013;

2° het feit dat ze op de hoogte zijn van de bepalingen,  vermeld  in  artikel  10.5.2  van  het  Onroerenderfgoeddecreet van 12 juli 2013.

Als partijen de toepassing vragen van het verlaagde  tarief, vermeld in artikel 2.9.4.2.8, is vereist dat :

1° de verkoopwaarde van elke kavel door de partijen  wordt aangegeven, hetzij in de akte, hetzij onderaan op  de akte, vóór de registratie;

2° de partijen vóór de registratie in een verklaring,  opgenomen in de akte of onderaan op de akte, aanduiden  of de geruilde onroerende goederen door henzelf of door  derden worden geëxploiteerd en dat, in dat laatste geval,  de akte of een document dat erbij gevoegd is vóór de  registratie, de instemming inhoudt van alle exploitanten  van de in de ruiling begrepen goederen.

Als de partijen de toepassing van het verlaagde tarief,  vermeld in artikel 2.9.4.2.10, § 1, van dit decreet,  inroepen, is ook vereist dat in de verklaring, vermeld in  paragraaf 1:

1° melding wordt gemaakt van het goedgekeurde  beheersplan, vermeld in artikel 2.9.4.2.10, § 2, 2°, van  dit decreet, met opgave van de referentie, alsook de  datum van de goedkeuring van het beheersplan door het  agentschap, vermeld in artikel 2.1, 2°, van het  Onroerenderfgoeddecreet van 12 juli 2013. Als het  beheersplan nog niet is opgemaakt en goedgekeurd op  het moment van het verlijden van de authentieke akte  van verkrijging, bestaat de verklaring in de melding dat  er een beheersplan opgemaakt zal worden als vermeld in  artikel  8.1.1  tot  en  met  8.1.3  van  het  Onroerenderfgoeddecreet van 12 juli 2013;

2° de partijen melding maken van hun kennis van artikel  10.5.2 van het Onroerenderfgoeddecreet van 12 juli  2013.

Als partijen voor de toepassing van het verlaagde tarief,  vermeld in artikel 2.9.4.2.11, § 1, eerste lid, of artikel  2.9.4.2.11, § 1, tweede lid, de toepassing van artikel  2.9.4.2.11, § 3, 1°, inroepen, is ook vereist dat in de  verklaring, vermeld in paragraaf 1:

Si, pour l’application du tarif réduit, visé à l'article  2.9.4.2.11, § 1, alinéa premier ou l'article 2.9.4.2.11, §  1, alinéa deux, les parties invoquent l’application de  l’article 2.9.4.2.11, § 3, 1°, la déclaration, visée au  paragraphe 1er doit également :  1° melding wordt gemaakt van de onroerende goederen  die de toepassing van het verlaagde tarief, vermeld in  artikel 2.9.4.2.11, § 1, eerste lid, of artikel 2.9.4.2.11, §  1, tweede lid, verhinderen;

1°  faire mention des biens immobiliers qui  compromettent l’application du tarif réduit, visé à l'article  2.9.4.2.11, § 1, alinéa premier ou l'article 2.9.4.2.11, § 1,  alinéa deux;  2° wordt gesteld dat de verkrijger de onroerende  goederen, vermeld in punt 1°, binnen twee jaar na de  datum van de authentieke akte van verkrijging volledig  en onder bezwarende titel zal vervreemden;

Als partijen voor de toepassing van het verlaagde tarief,  vermeld in artikel 2.9.4.2.11, § 1, eerste lid, of artikel  2.9.4.2.11, § 1, tweede lid, de toepassing van artikel  2.9.4.2.11, § 3, 2°, inroepen, is ook vereist dat in de  verklaring, vermeld in paragraaf 1:

1° melding wordt gemaakt van de onroerende goederen  die de toepassing van het verlaagde tarief, vermeld in  artikel 2.9.4.2.11, § 1, eerste lid, of artikel 2.9.4.2.11, §  1, tweede lid, verhinderen;

2° wordt gesteld dat de onroerende goederen, vermeld in  punt 1°, binnen een jaar na de datum van de akte van  verkrijging, al dan niet gedwongen, worden onteigend.

Als partijen voor de toepassing van het verlaagde tarief,  vermeld in artikel 2.9.4.2.12, § 1, eerste lid, of artikel  2.9.4.2.12, § 1, vijfde lid, de toepassing van artikel  2.9.4.2.12, § 1, derde lid, inroepen, is ook vereist dat in  de verklaring, vermeld in paragraaf 1, wordt gesteld dat  er in een periode van 5 jaar voorafgaand aan de datum  van de authentieke aankoopakte een inschrijving in het  bevolkingsregister of het vreemdelingenregister op het  adres van het aangekochte goed is geweest.

Als partijen voor de toepassing van het verlaagde tarief,  vermeld in artikel 2.9.4.2.12, § 1, eerste lid, of artikel  2.9.4.2.12, § 1, vijfde lid, de toepassing van artikel  2.9.4.2.12, § 2, 1°, inroepen, is ook vereist dat in de  verklaring, vermeld in paragraaf 1:

1° melding wordt gemaakt van de onroerende goederen  die de toepassing van het verlaagde tarief, vermeld in  artikel 2.9.4.2.12, § 1, eerste lid, of artikel 2.9.4.2.12, §  1, vijfde lid, verhinderen;

2° wordt gesteld dat de verkrijger de onroerende  goederen, vermeld in punt 1°, binnen drie jaar na de  datum van de authentieke akte van verkrijging volledig  en onder bezwarende titel zal vervreemden;

3° wordt aangetoond door de verkrijger dat er een  causaal verband bestaat tussen de vervreemding,  vermeld in punt 2°, en de verkrijging tegen het verlaagde  tarief, vermeld in artikel 2.9.4.2.12, § 1, eerste lid, of  artikel 2.9.4.2.12, § 1, vijfde lid.

Als partijen voor de toepassing van het verlaagde tarief,  vermeld in artikel 2.9.4.2.12, § 1, eerste lid, of artikel  2.9.4.2.12, § 1, vijfde lid, de toepassing van artikel  2.9.4.2.12, § 2, 2°, inroepen, is ook vereist dat in de  verklaring, vermeld in paragraaf 1:

1° melding wordt gemaakt van de onroerende goederen  die de toepassing van het verlaagde tarief, vermeld in  artikel 2.9.4.2.12, § 1, eerste lid, of artikel 2.9.4.2.12, §

2° wordt gesteld dat de onroerende goederen, vermeld in  punt 1°, binnen een jaar na de datum van de akte van  verkrijging, al dan niet gedwongen, worden onteigend.

Als partijen voor de toepassing van het verlaagde tarief,  vermeld in artikel 2.9.4.2.14, § 1, de toepassing van  artikel 2.9.4.2.14, § 5, 1°, inroepen, is ook vereist dat in  de verklaring, vermeld in paragraaf 1:

1° melding wordt gemaakt van de onroerende goederen  die de toepassing van het verlaagde tarief, vermeld in  artikel 2.9.4.2.14, § 1, verhinderen;

2° wordt gesteld dat de verkrijger de onroerende  goederen, vermeld in punt 1°, binnen drie jaar na de  datum van de authentieke akte van verkrijging volledig  en onder bezwarende titel zal vervreemden;

3° wordt aangetoond door de verkrijger dat er een  causaal verband bestaat tussen de vervreemding,  vermeld in punt 2°, en de verkrijging tegen het verlaagde  tarief, vermeld in artikel 2.9.4.2.14, § 1.

Als partijen voor de toepassing van het verlaagde tarief,  vermeld in artikel 2.9.4.2.14, § 1, de toepassing van  artikel 2.9.4.2.14, § 5, 2°, inroepen, is ook vereist dat in  de verklaring, vermeld in paragraaf 1:

1° melding wordt gemaakt van de onroerende goederen  die de toepassing van het verlaagde tarief, vermeld in  artikel 2.9.4.2.14, § 1, verhinderen;

2° wordt gesteld dat de onroerende goederen, vermeld in  punt 1°, binnen een jaar na de datum van de akte van  verkrijging, al dan niet gedwongen, worden onteigend.

Als de partijen de toepassing van het verlaagd tarief,  vermeld in artikel 2.9.4.2.15, § 1, van dit decreet,  inroepen voor de aankoop van een onbebouwd  onroerend goed, wordt bij de akte, vermeld in paragraaf  1, een afschrift van de beslissing tot goedkeuring van het  natuurbeheerplan als vermeld in artikel 16octies, § 1,  eerste lid, 5°, van het decreet van 21 oktober 1997  betreffende het natuurbehoud en het natuurlijk milieu  toegevoegd.

§ 4. Voor de toepassing van de vermindering, vermeld  in artikel 2.8.5.0.1, moeten in de akte van schenking de  voornamen, de achternaam, de woonplaats, de  geboorteplaats en de geboortedatum van de kinderen van  de belastingplichtige vermeld worden.

Bij een gelijkgestelde verrichting als vermeld in artikel  2.9.5.0.4, eerste lid, moeten het bedrag en de datum van  betaling van de registratiebelasting en de vermelding  van het wettelijk aandeel van de natuurlijke persoon in  de rechten, vermeld in het vorige lid en in artikel  3.6.0.0.6, § 3, zesde lid, 2°, in de akte die of het geschrift  dat de vraag tot toepassing van artikel 2.9.5.0.1 bevat of  in de akte die of het geschrift dat het verzoek tot  teruggave, vermeld in artikel 3.6.0.0.6, § 3, eerste lid,  bevat, betrekking hebben op de aankoop voorafgaand  aan de aankoop die is gedaan met toepassing van de  vrijstelling, vermeld in artikel 2.9.6.0.1, eerste lid, 4°.

En cas d'opération assimilée telle que visée à l'article  2.9.5.0.4, premier alinéa, le montant et la date du  paiement de l'impôt d'enregistrement et la mention de la  part légale de la personne physique dans les droits, visés  au précédent alinéa et à l'article 3.6.0.0.6, § 3, sixième  alinéa, 2°, doivent, dans l'acte ou l'écrit contenant la  demande d'application de l'article 2.9.5.0.1 ou dans  l'acte ou l'écrit contenant la demande de restitution,  visée à l'article 3.6.0.0.6, § 3, premier alinéa, avoir trait  à l'acquisition préliminaire à l'acquisition qui a été  effectuée en application de l'exonération, visée à l'article  2.9.6.0.1, premier alinéa, 4°.  Als de vermindering wordt gevraagd met toepassing van  artikel 2.9.5.0.1, vierde lid, moet de akte of het geschrift,  vermeld in paragraaf 1, 4°, bovendien het bedrag en de  datum van betaling van de registratiebelasting bevatten  inzake de akten of geschriften die betreffende de in  aanmerking te nemen voorafgaande verrichtingen  aanleiding hebben gegeven tot het heffen van het  verkooprecht, en bij elk bedrag het wettelijk aandeel van  de natuurlijke persoon in de in mindering gebrachte of  teruggegeven belastingen vermelden.

Aan de toepassing van paragraaf 1, 3°, juncto artikel  2.9.5.0.2 kan ook voldaan zijn als het verzoek en de  vermeldingen het voorwerp uitmaken van een verzoek,  ondertekend door de natuurlijke persoon, dat gevoegd is  bij de akte die of het geschrift dat ter registratie  aangeboden is en dat aanleiding geeft tot de heffing van  het verkooprecht.

§ 5. Als partijen de toepassing vragen van de vrijstelling,  vermeld in artikel 2.8.6.0.3, en als de schenking ook  andere goederen omvat dan de goederen, vermeld in  artikel 2.8.6.0.3, § 1, geven ze nauwkeurig aan voor  welke van de geschonken goederen die deel uitmaken  van de familiale onderneming of van het aandelenpakket  van de familiale vennootschap, de toepassing van de  vrijstelling gevraagd wordt, en voor welke van de  geschonken goederen geen toepassing van de vrijstelling  gevraagd wordt. Daarnaast moet melding gemaakt  worden van :

1° de naam en het ondernemingsnummer van de  familiale onderneming of familiale vennootschap  waarvoor de vrijstelling gevraagd wordt;

3° hetzij de activa van de familiale onderneming met een  duidelijke omschrijving en verwijzing naar de  boekhouding en, als het onroerende goederen betreft, de  vermelding of ze al dan niet hoofdzakelijk voor  bewoning worden aangewend of zijn bestemd, hetzij het  aantal aandelen en de precieze aard van alle aandelen  van een familiale vennootschap met enerzijds de  vermelding van het aantal aandelen dat in het bezit was  van de schenker en van andere bij naam te noemen  mede-aandeelhouders, alsook met het percentage van de  stemrechten dat zij vertegenwoordigen, en anderzijds de  aard van het zakelijk recht dat de schenker en andere bij  naam te noemen personen bezitten.

Als toepassing gemaakt wordt van het eerste lid, en om  de vrijstelling, vermeld in artikel 2.8.6.0.3, te kunnen  verkrijgen, moeten de volgende bescheiden binnen  zeven dagen vanaf de werkdag die volgt op de datum  van registratie van de authentieke akte van de schenking  bij de bevoegde entiteit van de Vlaamse administratie  ingediend zijn :

1° kopieën van de goedgekeurde jaarrekeningen van de  drie boekjaren die voorafgaan aan de authentieke akte  van de schenking, opgemaakt overeenkomstig de  vigerende boekhoudwetgeving van de plaats waar de  zetel gevestigd is als de zetel van de onderneming of  vennootschap niet in België ligt;

2° kopieën van het rechtsgeldige aandelenregister of, bij  gebrek  daaraan,  de  door  alle  aandeelhouders  ondertekende notulen van de laatste algemene  vergadering die voorafgaat aan de authentieke akte van  schenking, waaruit op ondubbelzinnige wijze de  participaties blijken, vermeld in artikel 2.8.6.0.3, § 1;

3° een kopie van de laatste door de schenker ingediende  fiscale aangifte voor de personenbelasting wat familiale  ondernemingen betreft;

4° een kopie van de gecoördineerde statuten, zoals die  van toepassing zijn op de datum van de authentieke akte  van de schenking.

5° een verslag dat een bedrijfsrevisor, die niet de  commissaris is, of een gecertificeerd accountant heeft  uitgereikt. Het verslag is ondertekend en gedateerd  voorafgaand aan de datum van de authentieke akte van  de schenking voor elke familiale vennootschap. Het  verslag vermeldt al de volgende gegevens:

b) de voor- en achternaam, het rijksregisternummer en  het adres van de aanvrager of, als er verschillende zijn,  de aanvragers;

c) de naam en het ondernemingsnummer van de  familiale vennootschap waarvoor de vrijstelling wordt  gevraagd;

d) de verkoopwaarde van de volle eigendom van de  geschonken aandelen van de familiale vennootschap,  zoals die is geraamd door de bedrijfsrevisor of de  accountant;

e) de verkoopwaarde en de opsomming van de  onroerende goederen die tot bewoning worden  aangewend of bestemd, met inbegrip van bouwgronden  als vermeld in artikel 1.1.0.0.2, zesde lid, 1° /1, van deze  codex, waarop de familiale vennootschap of haar  dochtervennootschappen zakelijke rechten hebben en de  aard van die zakelijke rechten. De vermelding bevat de  kadastrale gegevens, namelijk de kadastrale afdeling, de  sectie, het perceelnummer en het partitienummer, de  kadastrale oppervlakte, het kadastraal inkomen en, in  voorkomend geval, de kadastrale detailidentificatie van  een privatieve eigendom;

f) het gedeelte van de waarde, zoals die is geraamd door  de bedrijfsrevisor of de accountant, vermeld in punt d),  dat wordt bepaald door de verkoopwaarde van de  onroerende goederen, vermeld in punt e), in de familiale  vennootschap, of in participaties van minstens 10% van  de  familiale  ven-nootschap  in  haar  dochtervennootschappen;

g) het verschil tussen de verkoopwaarde, vermeld in  punt d), en de verkoopwaarde, vermeld in punt f);

h) een motivering van de wijze waarop de  bedrijfsrevisor of de accountant de verkoopwaarden,  vermeld in punt d), f) en g), heeft bepaald, met  vermelding van de gebruikte waarderingsmethode;

i) de referentiedatum voor de waardebepaling, vermeld  in punt d) en f), namelijk de datum waarop de waarde  van de aandelen wordt bepaald.

Als de bescheiden, vermeld in het tweede lid, worden  bezorgd met een aangetekende brief, geldt de datum van  de poststempel op het verzendingsbewijs als datum van  de indiening.

Als partijen de toepassing vragen van de vrijstelling,  vermeld in artikel 2.8.6.0.8, § 2, wordt bij de akte,  vermeld in paragraaf 1, een afschrift van de  overeenkomst, vermeld in artikel 2.8.6.0.8, § 2, tweede  lid, toegevoegd.

De vrijstelling, vermeld in artikel 2.9.6.0.1, eerste lid,  4°, en artikel 2.10.6.0.1, eerste lid, 2°, is alleen van  toepassing als in de akte of in een vóór de registratie bij  de akte te voegen geschrift de volgende gegevens  worden vermeld :

1° de datum van de eerste ingebruikneming of  inbezitneming van het gebouw waarop de overeenkomst  betrekking heeft;

2° in voorkomend geval, een verklaring van de verkopers  dat die hun medecontractanten op de hoogte hebben  gebracht van hun bedoeling om de handeling te  verrichten met toepassing van de belasting over de  toegevoegde waarde overeenkomstig artikel 1 van het  koninklijk besluit nr. 14 van 3 juni 1970 met betrekking  tot de vervreemdingen van gebouwen, gedeelten van  gebouwen en het bijhorende terrein en de vestigingen,  overdrachten en wederoverdrachten van een zakelijk  recht in de zin van artikel 9, tweede lid, 2°, van het  Wetboek van de belasting over de toegevoegde waarde  op zulke goederen;

3° (…)  3° (…)

4° als de vervreemding of de vestiging, overdracht of  wederoverdracht van zakelijke rechten ook goederen  betreft waarop de vrijstelling van het verkooprecht of  verdeelrecht niet van toepassing is, de nauwkeurige  aanduiding van die goederen op basis van hun kadastrale  beschrijving.

Voor de toepassing van de vrijstelling, vermeld in artikel  2.9.6.0.4, is vereist dat :

1° de verkoopwaarde van elke kavel door de partijen  wordt aangegeven, hetzij in de akte, hetzij onderaan op  de akte, vóór de registratie;

Als partijen de toepassing vragen van de vrijstelling,  vermeld in artikel 2.9.6.0.7, § 1, wordt bij de akte,  vermeld in paragraaf 1, een afschrift van de beslissing  tot goedkeuring van het natuurbeheerplan als vermeld in  artikel 16octies, § 1, eerste lid, 5°, van het decreet van  21 oktober 1997 betreffende het natuurbehoud en het  natuurlijk milieu toegevoegd.

Als partijen de toepassing vragen van de vrijstelling,  vermeld in artikel 2.9.6.0.7, § 2, wordt bij de akte,  vermeld in paragraaf 1, een afschrift van de  overeenkomst, vermeld in artikel 2.9.6.0.7, § 2, tweede  lid, toegevoegd.

Als de partijen de toepassing vragen van het verlaagde  tarief, vermeld in artikel 2.9.4.2.14, is ook vereist dat in  de verklaring, vermeld in paragraaf 1:

1° melding wordt gemaakt van het goedgekeurde  beheersplan, vermeld in artikel 2.9.4.2.10, § 2, 2°, met  opgave van de referentie, alsook de datum van de  goedkeuring van het beheersplan door het agentschap,  vermeld  in  artikel  2.1,  2°,  van  het  Onroerenderfgoeddecreet van 12 juli 2013. Als het  beheersplan nog niet is opgemaakt en goedgekeurd op  het moment van het verlijden van de authentieke akte  van verkrijging, bestaat de verklaring in de melding dat  er een beheersplan opgemaakt zal worden als vermeld in  artikel  8.1.1  tot  en  met  8.1.3  van  het  Onroerenderfgoeddecreet van 12 juli 2013;

2° de partijen melding maken van hun kennis van artikel  10.5.2 van het Onroerenderfgoeddecreet van 12 juli  2013.

---- historiek ----  ---- historique ----

- gewijzigd door art. 21 van het decreet van 03.04.2026  (B.S. 23.04.2026). Inwerkingtreding op 03.05.2026

- gewijzigd door art. 12 van het decreet van 19.12.2025  (B.S. 30.12.2025). De tekst is van toepassing op alle  authentieke schenkingsakten die zijn verleden vanaf 1  januari 2026.

Overeenkomstig artikel 15 van het decreet van  19.12.2025: "Als de authentieke akte van schenking  wordt verleden tussen 1 januari 2026 en 31 maart 2026,  wordt de termijn om een verslag als vermeld in artikel

Als het verslag, vermeld in artikel 3.12.3.0.1, § 5, tweede  lid, 5°, na de authentieke akte wordt opgesteld, wordt in  afwijking van artikel 3.12.3.0.1, § 5, tweede lid, 5°, i), de  datum van de authentieke schenkingsakte als  referentiedatum voor de waardebepaling in het verslag  vermeld."

- gewijzigd door art. 29 van het decreet van 09.12.2022  (B.S., 20.12.2022). Inwerkingtreding: 30.12.2022

- gewijzigd door art. 81 van het decreet van 23.12.2021  (B.S., 29.12.2021). Inwerkingtreding: 01.01.2022

- gewijzigd door art. 7 van het decreet van 19.11.2021  (B.S., 16.12.2021). Inwerkingtreding: 01.01.2022

- gewijzigd door art. 64 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- gewijzigd door art. 46 van het decreet van 21.12.2018  (B.S. 28.12.2018). Inwerkingtreding op 01.05.2019 (art.  3 van het besluit van 05.04.2019 - B.S.

07.05.2019)

- gewijzigd door art.13 van het decreet van 06.07.2018  (B.S. 20.07.2018 Ed.2). Tekst treedt in werking op  01.09.2018

- gewijzigd door art. 14 van het decreet van 18.05.2018  (B.S.: 28.05.2018). Tekst is van toepassing op  verkoopovereenkomsten afgesloten vanaf 1 juni 2018

- gewijzigd door art. 20 van het decreet van 22.12.2017  (B.S. 21.02.2018. Tekst treedt in werking op 09.06.2018  (art. 1 besluit 04.05.2018 B.S. 30.05.2018)

- gewijzigd door art. 29 van het decreet van 17 juli 2015  (B.S., 14.08.2015 ). De tekst is in werking getreden op 14  augustus 2015 (art. 41)

- gewijzigd door art. 9 van het decreet van 21.04.2017.  De tekst is in werking getreden op 14.05.2017

Als in een authentieke akte die aan de formaliteit van de  registratie is onderworpen en die geen vonnis of arrest  is, melding wordt gemaakt van een onderhandse akte of  van een in het buitenland verleden akte als vermeld in  artikel 19, eerste lid, 2°, van het federale Wetboek der  Registratie-, Hypotheek- en Griffierechten, moet die  authentieke akte het bedrag en de datum van betaling  van de registratiebelasting, geheven op vermelde akte,  vermelden.

Indien de onderhandse akte of in het buitenland verleden  akte, vermeld in het eerste lid, niet werd geregistreerd,  wordt daarvan in de authentieke akte melding gemaakt.

---- historiek ----  ---- historique ----

- toegevoegd door art. 275 van het decreet van 19 dec.

2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in werking  getreden op 1 januari 2015 (art. 325)

In geval van een schenking moet de notaris in de akte  een verklaring van de schenker opnemen die de  vermelding inhoudt van het adres en de datum en de duur  van de vestiging van de verschillende fiscale  woonplaatsen die de schenker gehad heeft in de periode  van vijf jaar voorafgaand aan de datum van de  schenking.

---- historiek ----  ---- historique ----

- toegevoegd door art. 276 van het decreet van 19 dec.  2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in werking  getreden op 1 januari 2015 (art. 325)

###### Art. 3.12.3.0.4.  Art. 3.12.3.0.4.

§ 1. De akten van schenking van onroerende goederen  moeten vermelden of er tussen dezelfde partijen al een  of meer schenkingen van onroerende goederen zijn  voorgekomen die vastgesteld zijn door akten die dateren  van minder dan drie jaar vóór de datum van de nieuwe  schenking en die vóór dezelfde datum geregistreerd zijn  of verplicht registreerbaar geworden zijn.

In voorkomend geval moeten de akten, vermeld in het  eerste lid, de datum van de akten van de reeds  voorgekomen schenkingen, vermeld in het eerste lid,  vermelden, alsook de belastbare grondslag.

De vastgelegde bepalingen, vermeld in dit artikel,  mogen gedaan worden onderaan op de akte in een  verklaring vóór de registratie, ondertekend en voor echt  bevestigd door de begiftigde, of, in zijn naam, door de  instrumenterende openbare of ministeriële ambtenaar of  officier.

§ 2. In geval van een schenking die onderworpen is aan  een opschortende voorwaarde, wordt voor de toepassing  van dit artikel de datum van de akte vervangen door de  datum van de vervulling van de voorwaarde.

---- historiek ----  ---- historique ----

- toegevoegd door art. 277 van het decreet van 19 dec.  2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in werking  getreden op 1 januari 2015 (art. 325)

###### Art. 3.12.3.0.5.  Art. 3.12.3.0.5.

§ 1. Alle uitgiften, afschriften of uittreksels van een  burgerlijke authentieke akte die aan de registratie  onderworpen is, moeten het bedrag en de datum van  betaling van de registratiebelasting vermelden.

§ 2. De verplichting, vermeld in paragraaf 1, geldt niet  voor :

2° de uitgiften en uittreksels van akten, verleden voor  notarissen, die aanleiding geven tot neerlegging op de  griffie  van  de  Rechtbank  van  Koophandel  overeenkomstig artikel 2:12 van het Wetboek van  vennootschappen en verenigingen;

3° de uitgiften en uittreksels van akten, verleden voor  notarissen, die worden uitgereikt met als enig doel de  inschrijving  van  een  onderneming  bij  een  ondernemingsloket, op voorwaarde dat het uitdrukkelijk  vermeld wordt op de uitgifte of het uittreksel;

4° afschriften die vereist zijn voor de betekening van  exploten en van andere soortgelijke akten;

5°  afschriften  waarvan  de  aflevering  wegens  hoogdringendheid is bevolen door de voorzitter van de  rechtbank van eerste aanleg;

6° de gedematerialiseerde afschriften van notariële akten  die worden neergelegd in de Notariële Aktebank  overeenkomstig artikel 18 van de wet van 25 ventôse  jaar XI op het notarisambt;

7° de uitgiften van akten, gemaakt met het oog op de  aanbieding ervan ter formaliteit van de registratie;

8° de uitgiften van akten, verleden door notarissen,  vermeld in artikel 1394/1 van het Gerechtelijk Wetboek,  die ingevolge artikel 1394/18 van het Gerechtelijk  Wetboek aan het centraal bestand van vonnissen,  arresten en akten houdende toekenning van een  onderhoudsuitkering moeten bezorgd worden.

---- historiek ----  ---- historique ----

- gewijzigd door art. 65 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- toegevoegd door art. 278 van het decreet van 19 dec.  2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in werking  getreden op 1 januari 2015 (art. 325)

###### Art. 3.12.3.0.6.  Art. 3.12.3.0.6.

Geen akte of geschrift mag bij een akte van een notaris  of bij een exploot of proces-verbaal van een  gerechtsdeurwaarder worden gevoegd, of onder de  minuten van een notaris worden neergelegd zonder dat  de registratiebelasting die erop verschuldigd is, betaald  is.

---- historiek ----  ---- historique ----

- gewijzigd door art. 53 van het decreet van 23.12.2016  (B.S.: 30.12.2016). Tekst in werking getreden op 8  januari 2017

- toegevoegd door art. 279 van het decreet van 19 dec.  2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in werking  getreden op 1 januari 2015 (art. 325)

#### Afdeling 4 - Verplichtingen van derden in het kader van

de belasting op de automatische ontspanningstoestellen

###### Art. 3.12.4.0.1.  Art. 3.12.4.0.1.

Een automatisch ontspanningstoestel dat een kansspel is  als vermeld in artikel 2, eerste lid, 1°, van de  Kansspelwet van 7 mei 1999, en niet beschikt over het  goedkeuringsattest, vermeld in artikel 52 van voormelde  wet, wordt ambtshalve beschouwd als een toestel van de  categorie 1, vermeld in artikel 2.13.3.0.1, § 2, eerste lid,  1°.

---- historiek ----  ---- historique ----

- vervangen door art. 6 van het decreet van 25.11.2022  (B.S., 01.12.2022). Inwerkingtreding: 01.01.2023

- vervangen door art. 7 van het decreet van 20.11.2020  (B.S., 03.12.2020). Inwerkingtreding: 01.01.2021

- ingevoegd door art. 47 van het decreet van 07.12.2018  (B.S. 20.12.2018). Tekst in werking

getreden op 01.01.2019

burgerlijke vordering

###### Art. 3.12.5.0.1.  Art. 3.12.5.0.1.

De bepalingen van deze codex doen geen afbreuk aan  het recht van het Vlaamse Gewest om het herstel van de  schade te vorderen die kan bestaan uit de niet-betaling  van  de  belastingen  en  toebehoren,  door  een  burgerlijkepartijstelling  of  door  een  aansprakelijkheidsvordering.

---- historiek ----  ---- historique ----

- vernummerd door art. 9 van het decreet van

20.11.2020 (B.S., 03.12.2020). Inwerkingtreding vanaf

aanslagjaar 2021

- ingevoegd door art. 48 van het decreet van 21.12.2018  (B.S. 28.12.2018). Tekst treedt in werking op 07.01.2019

### Hoofdstuk 13 - Onderzoek en controle  Chapitre 13 - Enquête et contrôle

#### Afdeling 1 - Administratieve controle  Section 1re - Contrôle administratif

##### Onderafdeling 1 - Algemeen  Sous-section 1re – Généralités

###### Art. 3.13.1.1.1.  Art. 3.13.1.1.1.

Elk bevoegde personeelslid, regelmatig belast met een  controle of een onderzoek in verband met de toepassing  van een belasting, vermeld in deze codex, bij een  natuurlijke persoon of een rechtspersoon, is van  rechtswege gemachtigd alle inlichtingen op te zoeken of  in te winnen die de juiste heffing van alle belastingen,  vermeld in deze codex, die door deze persoon  verschuldigd zijn, kunnen verzekeren.

###### Art. 3.13.1.1.2.  Art. 3.13.1.1.2.

Elke inlichting, elk stuk, elk proces-verbaal of elke akte,  door een bevoegde personeelslid ontdekt of verkregen  bij de uitoefening van zijn functie, hetzij rechtstreeks,  hetzij door tussenkomst van een van de diensten,  besturen of inrichtingen, vermeld in artikel 3.13.1.4.1,  kan door het Vlaamse Gewest worden ingeroepen om  elke som op te sporen die met toepassing van de  bepalingen van deze codex verschuldigd is.

###### Art. 3.13.1.1.3.  Art. 3.13.1.1.3.

Met behoud van de toepassing van de bevoegdheden,  vermeld in artikel 3.3.3.0.1, kan de bevoegde entiteit van  de Vlaamse administratie de onderzoekingen, vermeld  in dit hoofdstuk, verrichten, zelfs als de desbetreffende  belastingen al betaald zijn.

De onderzoekingen, vermeld in het eerste lid, mogen  bovendien voor de onroerende voorheffing worden  verricht gedurende de aanvullende termijn van vier jaar,  vermeld in artikel 3.3.3.0.1, § 1, op voorwaarde dat de  bevoegde entiteit van de Vlaamse administratie de  belastingplichtige vooraf schriftelijk en op nauwkeurige  wijze heeft kennisgegeven van de aanwijzingen inzake  belastingontduiking die voor hem bestaan voor het  bedoelde tijdperk.

Die voorafgaande kennisgeving, vermeld in het derde  lid, is voorgeschreven op straffe van nietigheid van de  aanslag.

###### Art. 3.13.1.1.4.  Art. 3.13.1.1.4.

§ 1. In de gevallen, vermeld in artikel 3.13.1.3.1, § 2, en  3.13.1.4.1, § 3, tweede lid, stelt de bevoegde entiteit van  de Vlaamse administratie de belastingschuldige in  kennis van de aanwijzing of de aanwijzingen van  belastingontduiking die een vraag om inlichtingen bij  een  financiële  instelling  rechtvaardigen.  Deze  kennisgeving gebeurt bij aangetekende brief, gelijktijdig  met het verzenden van de voormelde vraag om  inlichtingen.

Het eerste lid is niet van toepassing als de rechten van  het Vlaamse Gewest in gevaar zijn. De kennisgeving  gebeurt desgevallend post factum bij aangetekende  brief, uiterlijk 30 dagen na het verzenden van de in het  eerste lid vermelde vraag om inlichtingen.

§ 2. De bevoegde entiteit van de Vlaamse administratie  bezorgt de Vlaamse minister van Financiën eenmaal per  jaar een verslag dat onder meer volgende informatie  bevat:

1° het aantal keren dat in overeenstemming met artikel  3.13.1.2.5, tweede lid, een onderzoek is gevoerd bij  financiële instellingen en gegevens zijn gebruikt met het  oog op het belasten van hun cliënten;

2° het aantal keren dat in overeenstemming met artikel  3.13.1.3.1, § 2, en 3.13.1.4.1, § 3, tweede lid, een  onderzoek is gevoerd en gegevens zijn opgevraagd bij  financiële instellingen.

Dit verslag wordt openbaar gemaakt door de Vlaamse  minister van Financiën en overgezonden aan het  Vlaamse Parlement.

Met toepassing van artikel 23, lid 1, e) en h), van  verordening (EU) 2016/679 van het Europees Parlement  en de Raad van 27 april 2016 betreffende de  bescherming van natuurlijke personen in verband met de  verwerking van persoonsgegevens en betreffende het  vrije verkeer van die gegevens en tot intrekking van  Richtlijn  95/46/EG  (algemene  verordening  gegevensbescherming) kan de bevoegde entiteit van de  Vlaamse administratie beslissen om de reikwijdte van de  verplichtingen en de rechten, vermeld in artikel 12 tot en  met 22 van de voormelde verordening, te beperken bij  de verwerkingen van persoonsgegevens in het kader van  een onderzoek dat betrekking heeft op een welbepaalde  natuurlijke persoon, als voldaan is aan de voorwaarden,  vermeld in het tweede tot en met het negende lid.

De afwijkingsmogelijkheid, vermeld in het eerste lid,  geldt alleen gedurende de periode waarin de betrokkene  het voorwerp uitmaakt van een controle, een onderzoek  of de voorbereidende werkzaamheden die daarmee  verband houden, in het kader van de decretale en  reglementaire opdrachten van de bevoegde entiteit van  de Vlaamse administratie, op voorwaarde dat het voor  het goede verloop van het onderzoek noodzakelijk is of  kan zijn dat de verplichtingen en de rechten, vermeld in  artikel 12 tot en met 22 van de voormelde verordening,  niet worden toegepast. De duur van de voorbereidende  werkzaamheden mag in voorkomend geval niet meer  bedragen dan een jaar vanaf de ontvangst van een  verzoek tot uitoefening van een van de rechten, vermeld  in artikel 12 tot en met 22 van de voormelde  verordening.

De afwijkingsmogelijkheid, vermeld in het eerste lid,  heeft geen betrekking op de gegevens die losstaan van  het voorwerp van het onderzoek dat of van de controle  die de weigering of beperking van de rechten, vermeld  in het eerste lid, rechtvaardigt.

Als de betrokkene in het geval, vermeld in het eerste lid,  tijdens de periode, vermeld in het tweede lid, een  verzoek indient op basis van artikel 12 tot en met 22 van  de voormelde verordening, bevestigt de bevoegde  functionaris voor gegevensbescherming de ontvangst  daarvan.

De bevoegde functionaris voor gegevensbescherming  informeert de betrokkene ook over de mogelijkheid om  een verzoek in te dienen bij de toezichthoudende  autoriteit, vermeld in artikel 4, 21), van de voormelde  verordening, conform artikel 10/5 van het decreet van 18  juli 2008 betreffende het elektronische bestuurlijke  gegevensverkeer en om een beroep in rechte in te stellen.

De bevoegde functionaris voor gegevensbescherming  noteert de feitelijke of juridische gronden waarop de  beslissing is gebaseerd. Die informatie houdt hij ter  beschikking van de voormelde toezichthoudende  autoriteit, vermeld in artikel 4, 21), van de voormelde  verordening.

Nadat het onderzoek afgesloten is, worden de rechten,  vermeld in artikel 13 tot en met 22 van de voormelde  verordening, in voorkomend geval, conform artikel 12  van de voormelde verordening opnieuw toegepast.

Als een dossier dat persoonsgegevens als vermeld in het  eerste lid, bevat, naar het Openbaar Ministerie is  gestuurd en kan leiden tot activiteiten onder leiding van  het Openbaar Ministerie of een onderzoeksrechter, en er  onduidelijkheid is over het geheim van het onderzoek  onder leiding van het Openbaar Ministerie of een  onderzoeksrechter, mag de bevoegde functionaris voor  gegevensbescherming op verzoek van de betrokkene  overeenkomstig artikel 12 tot en met 22 van de  voormelde verordening pas antwoorden nadat het  Openbaar Ministerie of, in voorkomend geval, de  onderzoeksrechter heeft bevestigd dat een antwoord het  onderzoek niet in het gedrang brengt of kan brengen.

---- historiek ----  ---- historique ----

- gewijzigd door art. 3 van het decreet van 19.04.2024  (B.S., 03.06.2024). Inwerkingtreding: 13.06.2024

- vervangen door art. 30 van het besluit van 19.07.2019  (B.S. 02.09.2019). Inwerkingtreding op 12.09.2019

##### Onderafdeling 2 - Plichten van de belastingplichtige  Sous-section 2 - Obligations du contribuable

###### Art. 3.13.1.2.1.  Art. 3.13.1.2.1.

Eenieder die onderhevig is aan de belastingen, vermeld  in deze codex, is verplicht de bevoegde entiteit van de  Vlaamse administratie, op haar verzoek, en zonder dat  de belastingschuldige zich moet verplaatsen naar de  kantoren van de administratie, met het oog op de  controle ervan, alle documenten en aanvullende  verklaringen voor te leggen die noodzakelijk zijn om het  bedrag van zijn verschuldigde belastingen te bepalen.

Behalve als ze door het gerecht in beslag genomen zijn,  of behalve bij een afwijking, toegestaan door de  bevoegde entiteit van de Vlaamse administratie, moeten  de documenten aan de hand waarvan het bedrag van de  verschuldigde belastingen kan worden vastgesteld,  vermeld in het eerste lid, ter beschikking van de  bevoegde entiteit van de Vlaamse administratie worden  bewaard in het kantoor, agentschap, bijhuis of elk ander  beroeps- of privélokaal van de belastingplichtige waar  die  documenten  zijn  gehouden,  opgesteld  of  toegezonden, tot het verstrijken van de termijn, vermeld  in artikel 3.3.3.0.1.

Als de nalatenschap van een rijksinwoner de gehele of  een deel van de eigendom van een handelszaak bevat,  mag het bevoegde personeelslid het voorleggen van de  handelsboeken, inventarissen en balansen eisen en  daaruit alle nuttige inlichtingen putten.

In geval van een rechtsgeding tussen het Vlaamse  Gewest en de erfgenamen mag de mededeling in rechte  van de stukken, vermeld in het derde lid, niet geweigerd  worden.

---- historiek ----  ---- historique ----

- eerste lid gewijzigd door art. 280 van het decreet van  19 dec. 2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in

werking getreden op 1 januari 2015 (art. 325)

- derde lid en vierde lid toegevoegd door art. 281 van het  decreet van 19 dec. 2014 (B.S., 29.01.2015 - Ed. 2). De  tekst is in werking getreden op 1 januari 2015 (art. 325)

De natuurlijke personen en rechtspersonen die een  beroep doen op een informaticasysteem of elk ander  elektronisch apparaat om de documenten waarvan de  voorlegging is voorgeschreven met toepassing van  artikel 3.13.1.2.1, geheel of ten dele, te houden, op te  stellen, toe te zenden of te bewaren, zijn ook verplicht,  op verzoek van de bevoegde entiteit van de Vlaamse  administratie, ter plaatse, de dossiers over de analyses,  de programma's en het beheer van het gebruikte systeem,  alsook de informatiedragers en alle gegevens die ze  bevatten, ter inzage voor te leggen.

De gegevens die geplaatst zijn op de informatiedragers,  moeten in een leesbare en verstaanbare vorm ter inzage  worden voorgelegd.

Als de bevoegde entiteit van de Vlaamse administratie  hen erom verzoekt, zijn de personen, vermeld in het  eerste lid, verplicht met hun materiaal en in het bijzijn  van de personeelsleden van de bevoegde entiteit van de  Vlaamse administratie kopieën te maken van het geheel  of een deel van de voormelde gegevens in de vorm die  de personeelsleden van de bevoegde entiteit van de  Vlaamse  administratie  vragen,  alsook  om  de  informaticabewerkingen te verrichten die nodig zijn om  het bedrag van de belastingen te bepalen.

Si l'entité compétente de l'administration flamande le  leur demande, les personnes, citées dans l'alinéa  premier, sont obligées de faire des copies, avec leur  matériel et en présence de l'entité compétente de  l'administration flamande, de l'ensemble ou d'une partie  des données précitées dans la forme demandée par les  membres du personnel de l'entité compétente de  l'administration flamande, ainsi que d'exécuter les  opérations informatiques nécessaires à fixer le montant  des impôts.  De bepalingen van artikel 3.13.1.2.1, tweede lid, zijn  van toepassing op de bewaring van de dossiers met  betrekking tot de analyses, de programma's en het beheer  van het gebruikte systeem, alsook van de gegevens die  ze bevatten.

De verplichtingen, vermeld in het eerste en derde lid,  gelden ook als de gegevens waar de bevoegde entiteit  van de administratie om verzoekt, zich digitaal in België  of in het buitenland bevinden.

---- historiek ----  ---- historique ----

- gewijzigd door art. 30 van het decreet van 09.12.2022  (B.S. 20.12.2022). Inwerkingtreding: 30.12.2022

###### Art. 3.13.1.2.2/1.  Art. 3.13.1.2.2/1.

De personeelsleden van de bevoegde entiteit van de  Vlaamse administratie kunnen de documenten die  voorgelegd moeten worden met toepassing van artikel  3.13.1.2.1, voor de duur van het onderzoek behouden  telkens als ze menen dat die documenten nodig zijn om  het bedrag van de belastingen van de belastingplichtige  of van derden te bepalen.

De retentie, vermeld in het eerste lid, maakt het  voorwerp uit van een proces-verbaal van retentie dat

---- historiek ----  ---- historique ----

- Ingevoegd door art. 31 van het decreet van 09.12.2022  (B.S., 20.12.2022). Inwerkingtreding: 30.12.2022

###### Art. 3.13.1.2.3.  Art. 3.13.1.2.3.

Met behoud van het recht van de bevoegde entiteit van  de Vlaamse administratie tot het vragen van mondelinge  inlichtingen is eenieder die onderhevig is aan de  belastingen, vermeld in deze codex, verplicht de  bevoegde entiteit van de Vlaamse administratie, op haar  verzoek, binnen een maand vanaf de derde werkdag die  volgt op de verzending van de aanvraag, schriftelijk alle  inlichtingen te verstrekken die van hem worden  gevorderd met het oog op het onderzoek van zijn fiscale  toestand. De termijn kan om wettige redenen worden  verlengd.

###### Art. 3.13.1.2.4.  Art. 3.13.1.2.4.

De verificaties en vragen om inlichtingen, vermeld in  artikel 3.13.1.2.1, eerste lid, artikel 3.13.1.2.2, eerste tot  en met derde lid, artikel 3.13.1.2.2/1, eerste lid, en  artikel 3.13.1.2.3, mogen slaan op alle verrichtingen  waaraan de belastingplichtige heeft deelgenomen. De  aldus ingewonnen inlichtingen kunnen ook worden  ingeroepen met het oog op het belasten van derden.

---- historiek ----  ---- historique ----

- gewijzigd door art. 32 van het decreet van 09.12.2022  (B.S. 20.12.2022). Inwerkingtreding: 30.12.2022

###### Art. 3.13.1.2.5.  Art. 3.13.1.2.5.

In afwijking van artikel 3.13.1.2.4, en met behoud van  de toepassing van artikel 3.13.1.2.1 tot en met  3.13.1.2.3, is de bevoegde entiteit van de Vlaamse  administratie niet gemachtigd om in de rekeningen,  boeken en documenten van de bank-, wissel-, krediet- en  spaarinstellingen inlichtingen in te zamelen met het oog  op het belasten van hun cliënten.

Dit artikel is niet van toepassing op de erfbelasting en de  registratiebelasting.

---- historiek ----  ---- historique ----

- derde lid toegevoegd door art. 282 van het decreet van  19 dec. 2014 (B.S., 29.01.2015 - Ed. 2). De tekst is

in werking getreden op 1 januari 2015 (art. 325)

###### Art. 3.13.1.2.6.  Art. 3.13.1.2.6.

Natuurlijke personen of rechtspersonen zijn gehouden  aan de bevoegde personeelsleden, voorzien van hun  legitimatiebewijs en belast met het verrichten van een  controle of een onderzoek over de toepassing van de  belastingen, vermeld in deze codex, tijdens de uren dat  er een werkzaamheid wordt uitgeoefend, vrije toegang  te verlenen tot de beroepslokalen of de lokalen waar  rechtspersonen hun werkzaamheden uitoefenen, zoals  kantoren,  fabrieken,  werkplaatsen,  werkhuizen,  magazijnen, bergplaatsen, garages of tot hun terreinen  die als werkplaats, werkhuis of opslagplaats van  voorraden dienst doen, om aan die personeelsleden de  mogelijkheid te verschaffen het bedrag van de  verschuldigde belastingen vast te stellen.

De bevoegde personeelsleden, voorzien van hun  legitimatiebewijs, mogen, als ze met dezelfde taak belast  zijn, vrije toegang eisen tot alle andere lokalen,  gebouwen, werkplaatsen of terreinen die niet bedoeld  zijn in het eerste lid, maar waar werkzaamheden verricht  of vermoedelijk verricht worden. Tot particuliere  woningen of bewoonde lokalen hebben ze evenwel  alleen toegang tussen vijf uur 's morgens en negen uur 's  avonds en met machtiging van de rechter in de  politierechtbank.

###### Art. 3.13.1.2.7.  Art. 3.13.1.2.7.

De personeelsleden die belast zijn met de invordering,  beschikken over alle onderzoeksbevoegdheden, vermeld  in deze codex, om de vermogenssituatie van de  schuldenaar te bepalen met het oog op de invordering  van de belastingen en toebehoren.

De bevoegdheden van de personeelsleden, belast met de  invordering, vermeld in het eerste lid, worden ook  uitgeoefend zonder de beperkingen ten aanzien van de  instellingen, vermeld in artikel 3.13.1.2.5, 3.13.1.3.1, §  2 tot en met § 5, en artikel 3.13.1.4.1.

In afwijking van artikel 3.13.1.3.1, § 6, derde tot en met  zesde lid, van deze codex kunnen de personeelsleden die  belast zijn met de invordering, vermeld in het eerste lid,  om de vermogenssituatie van de schuldenaar te bepalen  met het oog op de invordering van de erfbelasting en de  registratiebelasting en toebehoren ook de volgende  handelingen stellen:

1° inlichtingen opvragen bij een bank-, wissel-, krediet- , en spaarinstelling;

2° de beschikbare gegevens over de belastingschuldige  of de erflater, in geval van erfbelasting, opvragen bij het  centrale aanspreekpunt, vermeld in de wet van 8 juli  2018  houdende  organisatie  van  een  centraal  aanspreekpunt van rekeningen en financiële contracten  en tot uitbreiding van de toegang tot het centraal bestand  van berichten van beslag, delegatie, overdracht,  collectieve schuldenregeling en protest.

---- historiek ----  ---- historique ----

- derde lid ingevoegd door art. 22 van het decreet van  03.04.2026 (B.S. 23.04.2026). Inwerkingtreding op  03.05.2026

De verklaring, vermeld in het eerste lid, mag op straffe  van schadevergoeding door de schuldeiser niet worden  geweigerd als ze wettig wordt aangevraagd.

De verklaring blijft bij de aangifte van nalatenschap  gevoegd.

---- historiek ----  ---- historique ----

- toegevoegd door art. 283 van het decreet van 19 dec.  2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in werking  getreden op 1 januari 2015 (art. 325)

###### Art. 3.13.1.2.9.  Art. 3.13.1.2.9.

De belastingplichtige houdt het bedrag van de inzetten,  de  inleggelden,  de  uitgekeerde  winsten,  de  weddenschappen  en  alle  andere  gegevens  die  noodzakelijk zijn om de belasting op de spelen en  weddenschappen te bepalen, bij op een elektronische  informatiedrager.

---- historiek ----  ---- historique ----

- ingevoegd door art. 48 van het decreet van 07.12.2018  (B.S. 20.12.2018). Tekst in werking

getreden op 01.01.2019

##### Onderafdeling 3 - Plichten van derden  Sous-section 3 - Obligations de tiers

###### Art. 3.13.1.3.1.  Art. 3.13.1.3.1.

§ 1. De bevoegde entiteit van de Vlaamse administratie  mag geschreven attesten inzamelen, derden horen, een  onderzoek instellen, en binnen de door haar bepaalde  termijn, die om wettige redenen kan worden verlengd,  van natuurlijke personen of rechtspersonen, alsook van  verenigingen zonder rechtspersoonlijkheid en openbare  of  ministeriële  ambtenaren  en  officieren  alle  inlichtingen vorderen die ze nodig acht om de juiste  vestiging en inning van de belasting te verzekeren.

In voorkomend geval kan een personeelslid met  minstens de graad van afdelingshoofd, een personeelslid  met minstens de graad van directeur ermee belasten om  bij een bank-, wissel-, krediet- en spaarinstelling elke  inlichting op te vragen die nuttig kan zijn om het bedrag  van de belastbare grondslag van de belastingplichtige te  bepalen.

Het personeelslid met minstens de graad van  afdelingshoofd mag de machtiging pas verlenen :

1° nadat het personeelslid dat het onderzoek voert, de  inlichtingen en gegevens over de rekeningen tijdens het  onderzoek met een verzoek om inlichtingen als vermeld  in artikel 3.13.1.2.3, heeft gevraagd en bij die vraag  duidelijk heeft aangegeven dat hij de toepassing van  paragraaf 2 van dit artikel kan vragen als de  belastingplichtige de gevraagde gegevens verborgen  houdt of weigert te verschaffen. De opdracht, vermeld in  het tweede lid, kan pas aanvangen als de termijn,  vermeld in artikel 3.13.1.2.3, is verlopen;

2° nadat hij heeft vastgesteld dat het gevoerde onderzoek  een of meer aanwijzingen van belastingontduiking heeft  opgeleverd en dat er vermoedens zijn dat de  belastingplichtige gegevens daarover bij een instelling  als vermeld in het tweede lid, verborgen houdt of dat de  belastingplichtige weigert om die gegevens zelf te  verschaffen.

§ 3. Als het personeelslid met minstens de graad van  directeur heeft vastgesteld dat het gevoerde onderzoek,  vermeld in paragraaf 2, een of meer aanwijzingen van  belastingontduiking heeft opgeleverd, kan hij de  beschikbare gegevens over die belastingplichtige  opvragen bij het centrale aanspreekpunt, vermeld in de  wet van 8 juli 2018 houdende organisatie van een  centraal aanspreekpunt van rekeningen en financiële  contracten en tot uitbreiding van de toegang tot het  centraal bestand van berichten van beslag, delegatie,  overdracht, collectieve schuldenregeling en protest.

§ 4. Paragraaf 2 en 3 zijn ook van toepassing als een  inlichting wordt gevraagd door een buitenlandse staat in  een van de volgende gevallen :

1° in het geval, vermeld in artikel 9 van het decreet van  21  juni  2013  betreffende  de  administratieve  samenwerking op het gebied van de belastingen;

De vraag van de buitenlandse staat wordt gelijkgesteld  met een aanwijzing van belastingontduiking als vermeld  in paragraaf 2. In dat geval verleent het personeelslid  met minstens de graad van afdelingshoofd, in afwijking  van paragraaf 2, de machtiging op basis van de vraag,  gesteld door de buitenlandse staat.

§ 5. De inlichtingen waarover de administratie uit  hoofde van dit artikel beschikt, vallen onder de  geheimhoudingsplicht en genieten de bescherming met  betrekking tot soortgelijke inlichtingen, vermeld in  artikel 3.19.0.0.2.

§ 6. De bepalingen van paragraaf 2 en 3 zijn inzake de  registratiebelasting en de erfbelasting niet van  toepassing, behalve wat de toepassing van paragraaf 4  betreft.

Een bank-, wissel-, krediet-, en spaarinstelling wordt  beschouwd als een derde waarop de bepalingen van  paragraaf 1 van toepassing zijn.

Aan de instellingen, vermeld in het tweede lid, kunnen  alleen  inlichtingen  gevraagd  worden  door  een  personeelslid met minstens de graad van directeur, als  die daartoe gemachtigd is door een personeelslid met  minstens de graad van afdelingshoofd.

Met betrekking tot de registratiebelasting moet de  machtiging een nauwkeurige aanduiding bevatten van  het rechtsfeit waarvoor het onderzoek noodzakelijk  wordt geacht.

Met betrekking tot de erfbelasting moet de machtiging  de aanduiding van de overleden persoon bevatten en, als  het onderzoek betrekking heeft op feiten die meer dan  vijf jaar voor het openvallen van de nalatenschap hebben  plaatsgevonden, of op verrichtingen die gedaan zijn door  een andere persoon dan de overledene of zijn echtgenoot  of wettelijk samenwonende, de nauwkeurige aanduiding  van de feiten die het voorwerp van de opzoeking  uitmaken.

§ 7. De inlichtingen, vermeld in dit artikel, moeten  worden verschaft binnen drie maanden na de datum  waarop ze zijn gevraagd. Die termijn kan worden  verlengd door het bevoegde personeelslid met minstens  de graad van afdelingshoofd.

---- historiek ----  ---- historique ----

- § 2, tweede lid gewijzigd door art. 23 van het decreet  van 03.04.2026 (B.S. 23.04.2026). Inwerkingtreding op  03.05.2026

- gewijzigd door art. 34 van het decreet van 20.12.2024  (B.S. 30.12.2024). Inwerkingtreding: 01.01.2025

- gewijzigd door art. 33 van het decreet van 09.12.2022  (B.S. 20.12.2022). Inwerkingtreding: 30.12.2022

- §1 gewijzigd door art. 284 van het decreet van 19 dec.  2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in werking  getreden op 1 januari 2015 (art. 325)

- §6 en §7 toegevoegd door art. 285 van het decreet van  19 dec. 2014 (B.S., 29.01.2015 - Ed. 2). De tekst is

in werking getreden op 1 januari 2015 (art. 325)

De bevoegde entiteit van de Vlaamse administratie mag  van natuurlijke personen of rechtspersonen alsook van  verenigingen zonder rechtspersoonlijkheid en openbare  of ministeriële ambtenaren en officieren, binnen de door  haar bepaalde termijn, voor alle of voor een deel van hun  verrichtingen of activiteiten de overlegging vorderen  van inlichtingen over elke persoon of groep van  personen, zelfs als ze niet met naam zijn aangeduid, met  wie ze rechtstreeks of onrechtstreeks contact hebben  gehad uit hoofde van die verrichtingen of activiteiten.  De termijn kan wegens wettige redenen worden  verlengd.

---- historiek ----  ---- historique ----

- gewijzigd door art. 286 van het decreet van 19 dec.  2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in werking  getreden op 1 januari 2015 (art. 325)

###### Art. 3.13.1.3.3.  Art. 3.13.1.3.3.

De bepalingen van artikel 3.13.1.2.2 zijn van toepassing  op verenigingen zonder rechtspersoonlijkheid alsook op  derden op wie een beroep wordt gedaan om de  documenten, waarvan de voorlegging is voorgeschreven  door artikel 3.13.1.2.1, geheel of gedeeltelijk te houden,  op te stellen, toe te zenden of te bewaren door middel  van computersystemen.

###### Art. 3.13.1.3.4.  Art. 3.13.1.3.4.

De bevoegde entiteit van de Vlaamse administratie mag  de juistheid nagaan van de inlichtingen, vermeld in  artikel 3.13.1.3.1, 3.13.1.3.2 en 3.13.1.3.3.

###### Art. 3.13.1.3.5.  Art. 3.13.1.3.5.

De belastingschuldige wordt met een aangetekende brief  opgeroepen om het getuigenverhoor bij te wonen.

De getuigen zijn verplicht getuigenis af te leggen over  alle daden en feiten waarvan ze kennis hebben en  waarvan de vaststelling nuttig kan zijn voor de  toepassing van de belastingwetten op de feiten waarover  een geschil bestaat.

Voor ze getuigen, leggen ze de eed af, vermeld in artikel  934 van het Gerechtelijk Wetboek.

Het tegenbewijs is rechtens toegelaten.  La preuve du contraire est autorisée de droit.

###### Art. 3.13.1.3.6.  Art. 3.13.1.3.6.

Van de verklaringen van de getuigen en, als de  belastingschuldige dat verlangt, van zijn eigen  verklaringen wordt een proces-verbaal opgemaakt.

Ze laten hun handtekening voorafgaan door de met de  hand geschreven woorden "Gelezen en goedgekeurd".  Als een van de betrokkenen weigert te ondertekenen,  wordt daarvan melding gemaakt in het proces-verbaal,  dat de reden van de weigering nader omschrijft.

Een eensluidend verklaard afschrift van het proces-  verbaal wordt aan de belastingschuldige betekend  binnen acht dagen na zijn dagtekening.

###### Art. 3.13.1.3.7.  Art. 3.13.1.3.7.

###### Art. 96. tot en met artikel 99 en artikel 101 tot en met

artikel  103 2  van  het  federale  Wetboek  van  Successierechten, en de ter uitvoering daarvan genomen  besluiten, blijven onverminderd van toepassing met het  oog op de juiste heffing en de invordering van het  successierecht.  De  erin  vermelde  federale  belastingdiensten en federale belastingambtenaren  behouden de bevoegdheden en taken die uit die  bepalingen voortvloeien.

De bestuursdiensten van de staat bezorgen de aldus  verkregen informatie overeenkomstig artikel 3.13.1.4.2  aan de bevoegde entiteit van de Vlaamse administratie.

De aangewezen ambtenaar van de bestuursdienst van de  staat moet het bevoegde personeelslid op de hoogte  brengen van de opmaak van de lijst of inventaris,  vermeld in artikel 98, laatste lid, en artikel 101, eerste  lid, van het federale Wetboek van Successierechten. Het  bevoegde personeelslid kan in voorkomend geval de  opmaak van de lijst of inventaris, vermeld in deze  artikelen, bijwonen.

---- historiek ----  ---- historique ----

- gewijzigd door art. 66 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- toegevoegd door art. 287 van het decreet van 19 dec.  2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in werking  getreden op 1 januari 2015 (art. 325)

###### Art. 3.13.1.4.1.  Art. 3.13.1.4.1.

§ 1. De bestuursdiensten van de staat, met inbegrip van  de parketten en de griffies van de hoven en van alle  rechtscolleges, de besturen van de gemeenschappen, de  gewesten, de provincies, de agglomeraties, de federaties  van gemeenten en de gemeenten, alsook de openbare  instellingen en inrichtingen, zijn gehouden, als ze  daarvoor worden aangezocht door een personeelslid,  belast met de vestiging of de invordering van de  belastingen, hem alle inlichtingen die ze in hun bezit  hebben, te verstrekken, hem, zonder verplaatsing, in alle  akten, stukken, registers en om het even welke  bescheiden die ze in hun bezit hebben, inzage te  verlenen, en hem alle inlichtingen, afschriften of  uittreksels te laten nemen die het bedoelde personeelslid  nodig acht voor de vestiging of de invordering van de  belastingen, vermeld in deze codex.

In de akten, stukken, registers, bescheiden of  inlichtingen over de rechtspleging mag evenwel geen  inzage worden verleend zonder uitdrukkelijk verlof van  het openbaar ministerie.

De originelen van de ontvangstbewijzen-getuigschriften  voor verstrekte hulp, uitgereikt door de geneesheren, de  tandheelkundigen en de paramedische medewerkers,  mogen echter niet worden meegedeeld zonder dat de  nationale raad van de Orde van Geneesheren of de  provinciale geneeskundige commissies de gelegenheid  hebben gehad zich ervan te vergewissen dat de bevoegde  entiteit van de Vlaamse administratie daardoor geen  inlichtingen krijgt over de identiteit van de zieken en van  de verzekerden.

§ 2. Paragraaf 1 is niet van toepassing op de Algemene  Directie Statistiek en Economische Informatie (ADSEI)  wat de individueel verkregen inlichtingen betreft.

§ 3. Paragraaf 1 is niet van toepassing op de naamloze  vennootschap van publiek recht bpost.

Paragraaf 1 blijft evenwel van toepassing in de gevallen  en onder de voorwaarden, vermeld in artikel 3.13.1.2.5,  tweede lid, en artikel 3.13.1.3.1, § 2 tot en met § 5.

§ 5. Onder openbare instellingen of inrichtingen als  vermeld in paragraaf 1 wordt verstaan: de instellingen,  maatschappijen, verenigingen, inrichtingen en diensten  die de staat, een gemeenschap of een gewest mee  beheert, waaraan de staat, een gemeenschap of een  gewest een waarborg verstrekt, op de werkzaamheden  waarvan de staat, een gemeenschap of een gewest  toezicht uitoefent of waarvan het bestuurspersoneel  wordt aangewezen door de Federale Regering of een  gemeenschaps- of gewestregering, op haar voordracht of  met haar goedkeuring.

---- historiek ----  ---- historique ----

- gewijzigd door art. 34 van het decreet van 09.12.2022  (B.S. 20.12.2022). Inwerkingtreding: 30.12.2022

###### Art. 3.13.1.4.2.  Art. 3.13.1.4.2.

De diensten, besturen, vennootschappen, verenigingen,  instellingen of inrichtingen, vermeld in artikel  3.13.1.4.1, zijn gehouden de gegevens die noodzakelijk  zijn om de belastingen, vermeld in deze codex, te  bepalen, op elektronische wijze ter beschikking te  stellen van de bevoegde entiteit van de Vlaamse  administratie. De leidend ambtenaar van de bevoegde  entiteit van de Vlaamse administratie richt daarvoor een  eenmalig  verzoek  aan  de  diensten,  besturen,  vennootschappen,  verenigingen,  instellingen  of  inrichtingen, vermeld in artikel 3.13.1.4.1, met  vermelding van de frequentie en de wijze waarop de  gegevens ter beschikking gesteld moeten worden.

De  mogelijkheid  om  via  eenvoudig  verzoek  elektronische gegevensuitwisseling tot stand te brengen,  vermeld in het eerste lid, doet geen afbreuk aan de  rechtsgeldigheid van bestaande gegevensuitwisselingen  of gegevensuitwisselingen die tot stand zouden komen  zonder een dergelijk verzoek.

---- historiek ----  ---- historique ----

- tweede lid toegevoegd door art. 19 van het decreet van  19 dec. 2014 (B.S., 13.01.2015). De tekst is in werking  getreden op 01.01.2014. (art. 24)

###### Art. 3.13.2.0.1.  Art. 3.13.2.0.1.

Voor de verkeersbelasting, de belasting op de  inverkeerstelling, het eurovignet en de kilometerheffing  houden de bevoegde personeelsleden toezicht op de  naleving van de bepalingen van deze codex en de  uitvoeringsbesluiten ervan met betrekking tot de  voertuigen die zich op de openbare weg bevinden. Ze  kunnen alle documenten die nuttig zijn voor de  identificatie van het voertuig of vaartuig, van de  bestuurder of houder doen voorleggen, alsook een ander  document dat de betaling van de belasting bewijst. Ze  zijn gemachtigd zonder enige bijstand de garages, de  hangars en de berg- of aanmeerplaatsen te onderzoeken.

Voor de belasting op de spelen en weddenschappen en  de belasting op de automatische ontspanningstoestellen  houden de bevoegde personeelsleden toezicht op de  naleving van de bepalingen van deze codex en de  uitvoeringsbesluiten ervan op de plaatsen waar die  spelen en weddenschappen plaatsvinden of de  automatische ontspanningstoestellen opgesteld zijn.

De bevoegde personeelsleden die toezicht houden op de  naleving van de bepalingen van deze codex en de  uitvoeringsbesluiten ervan kunnen zich bij een controle  ter plaatse alle documenten laten voorleggen die nuttig  zijn voor de identificatie van de personen die aan de  controle onderworpen zijn.

---- historiek ----  ---- historique ----

- gewijzigd door art. 67 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- gewijzigd door art. 49 van het decreet van 07.12.2018  (B.S. 20.12.2018). Tekst treedt in werking op 01.01.2019

- vervangen door art. 34 van het decreet van 3 juli 2015  (B.S., 10.08.2015). De tekst treedt in werking op 1 april  2016 (art. 44)

###### Art. 3.13.2.0.2.  Art. 3.13.2.0.2.

In het kader van de uitoefening van hun opdracht kunnen  de bevoegde personeelsleden:

1° bevelen geven aan bestuurders en het verkeer regelen  als vermeld in artikel 11 van de wet van 16 maart 1968  betreffende de politie over het wegverkeer;

3° de bijstand vorderen van de lokale en federale politie  bij de uitoefening van controles waarbij ze zich tijdens  de uitoefening van hun ambt desgevraagd kenbaar  maken door hun legitimatiebewijs voor te leggen.

4° vaststellingen doen aan de hand van vaste en mobiele  camera's met automatische nummerplaatherkenning.

---- historiek ----  ---- historique ----

- 4° ingevoegd door art. 4 van het decreet van  19.04.2024  (B.S.,  03.06.2024).  Inwerkingtreding:  13.06.2024

###### Art. 3.13.2.0.3.  Art. 3.13.2.0.3.

Met behoud van de bevoegdheden die toevertrouwd  worden aan de andere officieren of agenten van  gerechtelijke politie en aan de leden van het operationele  kader van de lokale en de federale politie, hebben de  bevoegde personeelsleden die toezicht houden op de  uitvoering van de bepalingen van deze codex en de  uitvoeringsbesluiten ervan, de hoedanigheid van agent  of officier van de gerechtelijke politie.

###### Art. 3.13.2.0.4.  Art. 3.13.2.0.4.

§ 1. Als de niet-betaling van de verkeersbelasting, de  belasting op de inverkeerstelling, het eurovignet of de  administratieve geldboetes die worden opgelegd  ingevolge overtredingen van de regelgeving inzake de  kilometerheffing, met inbegrip van de administratieve  geldboetes  inzake  kilometerheffing  die  worden  opgelegd voor overtredingen die eerder zijn begaan,  maar die niet vroeger ter kennis konden worden gebracht  aan de overtreder ingevolge de niet-naleving van zijn  verplichtingen, wordt vastgesteld op de openbare weg,  moet de bestuurder van het voertuig dat aan een van die  belastingen onderhevig is, de niet-betaalde belastingen  en toebehoren die voor het gecontroleerde voertuig  verschuldigd zijn op het ogenblik van de vaststelling van  de overtreding dadelijk betalen aan het bevoegde  personeelslid, vermeld in artikel 3.13.2.0.3.

§ 2. In geval van niet-betaling van de sommen, vermeld  in paragraaf 1, op het ogenblik van de vaststelling van  de overtreding, wordt het voertuig door het bevoegde  personeelslid, vermeld in artikel 3.13.2.0.3, aangehaald  tot de verschuldigde sommen betaald zijn.

Het bevoegde personeelslid, vermeld in artikel  3.13.2.0.3, stelt in het geval, vermeld in het eerste lid,  een verslag van vaststelling van aanhaling op.

De aanhaling, vermeld in het eerste lid, kan onder meer  bestaan uit het inhouden van de boorddocumenten, het  inhouden van de vrachtbrief, het plaatsen van een  wielklem, het wegtakelen van het voertuig, vermeld in  paragraaf 1, naar een stallingplaats en het stallen van het  voertuig.

Het aangehaalde voertuig mag niet worden vervreemd  noch worden verplaatst zonder toestemming van het  bevoegde personeelslid.

§ 3. Als de sommen, vermeld in paragraaf 1, niet betaald  zijn binnen een week na de dag van de vaststelling van  de overtreding, vermeld in paragraaf 1, kan de bevoegde  entiteit van de Vlaamse administratie het aangehaalde  voertuig in beslag nemen en tot de verkoop ervan laten  overgaan, waarbij ze een bericht van inbeslagneming  opstelt. Er verstrijken minstens dertig dagen tussen de  ontvangst van het bericht van inbeslagneming, conform  artikel  3.13.2.0.6,  §  2,  eerste  lid,  door  de  belastingschuldige en de verkoop van het voertuig.

Als  de  belastingschuldige  het  bericht  van  inbeslagneming betwist kan hij binnen een termijn van  dertig dagen na ontvangst van het bericht van  inbeslagneming, vermeld in artikel 3.13.2.0.6, § 2, eerste  lid, verzet aantekenen, houdende dagvaarding van het  Vlaamse Gewest, bij de beslagrechter van de plaats waar  de bevoegde entiteit van de Vlaamse administratie die de  belasting moet innen, is gevestigd. Over deze betwisting  wordt uitspraak gedaan zoals in kortgeding.

In het bericht van inbeslagneming en het dwangbevel  kunnen naast de sommen, vermeld in paragraaf 1, andere  openstaande  schulden  worden  opgenomen  die  betrekking hebben op de belastingen, opcentiemen,  opdeciem, interesten en kosten ten laste van de  belastingschuldige die door de bevoegde entiteit van de  Vlaamse administratie worden geïnd.

Als de belastingschuldige niet de eigenaar is van het  voertuig dat het voorwerp uitmaakt van het […] beslag,  en over de eigendom een geschil ontstaat, kan er over de  betwisting uitspraak gedaan worden, zoals in kortgeding  door de beslagrechter van de plaats waar de bevoegde  entiteit van de Vlaamse administratie die de belasting  moet innen is gevestigd.

§ 4. Het risico en de eventuele kosten die voortvloeien  uit de aanhaling en het beslag, zijn ten laste van de  belastingschuldige.

§ 5. De opbrengst van de verkoop van het voertuig,  vermeld in artikel 1.1.0.0.2, derde lid, 1° en 2°, en artikel  2.2.1.0.1 wordt aangerekend volgens de regels, vermeld  in artikel 3.4.7.0.1. Het eventuele overschot wordt aan  de  belastingschuldige  terugbetaald.  De  belastingschuldige wordt op de hoogte gebracht van de  bestemming van de opbrengst van de verkoop van het  voertuig en in voorkomend geval van het saldo dat hij  nog verschuldigd is.

---- historiek ----  ---- historique ----

- gewijzigd door art. 2 van het decreet van 26.04.2024  (B.S. 24.05.2024). Inwerkingtreding: 01.09..2024

- gewijzigd door art. 35 van het decreet van 09.12.2022  (B.S. 20.12.2022). Inwerkingtreding: 30.12.2022

- gewijzigd door art. 49 van het decreet van 21.12.2018  (B.S. 28.12.2018). Tekst treedt in werking op 07.01.2019

- gewijzigd door art. 50 van het decreet van 07.12.2018  (B.S. 20.12.2018). Tekst treedt in werking op 01.01.2019

- gewijzigd door art. 35 van het decreet van 3 juli 2015  (B.S., 10.08.2015). De tekst treedt in werking op 1 april  2016 (art. 44)

###### Art. 3.13.2.0.5.  Art. 3.13.2.0.5.

Als een overtreding van de bepalingen van deze codex  wordt geconstateerd, zal een verslag van vaststelling  worden opgemaakt door het bevoegde personeelslid,  vermeld in artikel 3.13.2.0.3. Het verslag van  vaststelling vermeldt minstens de overtreding alsook de  elementen die moeten toelaten de overtreder te  identificeren. Het verslag van vaststelling voor een  overtreding van de bepalingen met betrekking tot de  kilometerheffing vermeldt minstens het bedrag van de  administratieve boete, de aard, de datum en het uur van  de gepleegde overtreding, de verwijzing naar de  artikelen die werden miskend, de naam en het adres van  de bevoegde entiteit van de Vlaamse administratie bij  wie informatie over de inbreuk en de boete kan worden  verkregen en het administratief beroep dat kan worden  ingesteld samen met de termijn, alsook de elementen die  moeten toelaten de houder of de bestuurder van het  voertuig te identificeren.

De verslagen van vaststelling, vermeld in het eerste lid,  opgemaakt door het bevoegde personeelslid, vermeld in  artikel 3.13.2.0.3, verdienen het volle geloof in rechten  totdat de valsheid ervan bewezen is.

Als de overtreder niet kan worden geïdentificeerd op de  dag van de vaststelling van de overtreding begint de  termijn van vijftien dagen, vermeld in het tweede lid, te  lopen na de dag waarop het bevoegde personeelslid,  vermeld in artikel 3.13.2.0.3, de overtreder met  zekerheid kon identificeren.

Als in samenhang met de overtredingen, vermeld in het  eerste lid, tegelijkertijd een strafrechtelijk misdrijf wordt  vastgesteld, wordt de vaststelling van dat misdrijf,  opgenomen in een proces-verbaal.

---- historiek ----  ---- historique ----

- eerste en tweede lid aangevuld door art. 17 van het  decreet van 03.05.2024 (B.S. 22.05.2024). Tekst treedt in  werking op 01.07.2025

- gewijzigd door art. 51 van het decreet van 07.12.2018  (B.S. 20.12.2018). Tekst treedt in werking op 01.01.2019

- eerste lid vervangen door art. 36 van het decreet van 3  juli 2015 (B.S., 10.08.2015). De tekst treedt in

werking op 1 april 2016 (art. 44)

- vierde lid toegevoegd door art. 36 van het decreet van 3  juli 2015 (B.S., 10.08.2015). De tekst treedt in

werking op 1 april 2016 (art. 44))

###### Art. 3.13.2.0.6.  Art. 3.13.2.0.6.

§ 1. Het bericht van inbeslagneming, opgemaakt  ingevolge artikel 3.13.2.0.4, § 3, eerste lid, bevat  minstens:

2° de oorzaken van het bericht van inbeslagneming;

3° de elementen die toelaten om het voertuig te  identificeren en de plaats waar het wordt gestald te  lokaliseren.t van inbeslagneming;

§ 2. Het bericht van inbeslagneming wordt verstuurd  naar het adres van de belastingschuldige en wordt geacht  door hem te zijn ontvangen op de derde werkdag na de  verzending ervan.

De belastingschuldige bezorgt het bericht van  inbeslagneming onmiddellijk aan de eigenaar van het  voertuig.

§ 3. Het bericht van inbeslagneming, vermeld in  paragraaf 1, dat is opgemaakt door de bevoegde entiteit  van de Vlaamse administratie, verdient het volle geloof  in rechten tot de valsheid ervan bewezen is.

---- historiek ----  ---- historique ----

- Ingevoegd door art. 3 van het decreet van 26.04.2024  (B.S., 24.05.2024). Inwerkingtreding: 01.09.2024

### Hoofdstuk 14 - Verjaring  Chapitre 14 – Prescription

#### Afdeling 1 - Termijn  Section 1re – Délai

###### Art. 3.14.1.0.1.  Art. 3.14.1.0.1.

De belastingen, vermeld in deze codex, verjaren na  verloop van vijf jaar vanaf de datum waarop ze betaald  moeten zijn.

---- historiek ----  ---- historique ----

- gewijzigd door art. 288 van het decreet van 19 dec.  2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in werking  getreden op 1 januari 2015 (art. 325)

###### Art. 3.14.1.0.2.  Art. 3.14.1.0.2.

[…]  […]

---- historiek ----  ---- historique ----

- toegevoegd door art. 289 van het decreet van 19 dec.  2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in werking  getreden op 1 januari 2015 (art. 325)

#### Afdeling 2 - Stuiting  Section 2 – Interruption

###### Art. 3.14.2.0.1.  Art. 3.14.2.0.1.  De termijn, vermeld in artikel 3.14.1.0.1, kan worden  gestuit op de wijze, vermeld in artikel 2244 tot en met  artikel 2250 van het Burgerlijk Wetboek, door de  verzending met een aangetekende brief van elke  aanmaning tot betaling waarin de gegevens van de  schuldvordering volledig en ondubbelzinnig zijn  opgenomen, of door afstand te doen van de termijn die  verlopen is op de verjaring. In geval van stuiting van de  verjaring treedt een nieuwe verjaring in, die op dezelfde  wijze kan worden gestuit na verloop van vijf jaar na de  laatste akte of handeling waardoor de vorige verjaring is  gestuit, als geen geding voor het gerecht aanhangig is.

Voor een aanmaning tot betaling die met een  aangetekende brief wordt verzonden, geldt de datum van  de  poststempel  op  het  verzendingsbewijs  als  indieningsdatum van die aanmaning. Als de schuldenaar  of de medeschuldenaar geen bekende woonplaats in  België of in het buitenland heeft, wordt de aanmaning  tot betaling met een aangetekende brief aan de procureur  des Konings van Brussel verzonden.

De kosten voor de verzending met een aangetekende  brief van de aanmaning tot betaling, vermeld in het  eerste en tweede lid, zijn ten laste van de  belastingschuldige.

---- historiek ----  ---- historique ----

- derde lid ingevoegd door art. 24 van het decreet van  03.04.2026 (B.S. 23.04.2026). Inwerkingtreding op  03.05.2026

- gewijzigd door art. 4 van het decreet van 26.04.2024  (B.S., 24.05.2024). Inwerkingtreding: 03.06.2024

###### Art. 3.14.3.0.1.  Art. 3.14.3.0.1.

Elk rechtsgeding met betrekking tot de vestiging, de  inning of de invordering van de belastingen, vermeld in  deze codex, dat wordt ingesteld door het Vlaamse  Gewest, door de schuldenaar van de belastingen of door  iedere andere persoon die gehouden is tot de betaling  van de schuld met toepassing van deze codex, van de  besluiten die genomen zijn ter uitvoering ervan, of van  het gemeen recht, schorst de verjaring.

Het bezwaar en de aanvraag tot ontheffing, vermeld in  artikel 3.6.0.0.1, artikel 3.6.0.0.4 en artikel 3.6.0.0.6,  schorsen de verjaring ook.

---- historiek ----  ---- historique ----

- gewijzigd door art. 50 van het decreet van 21.12.2018  (B.S. 28.12.2018). Tekst treedt in werking op 07.01.2019

- gewijzigd door art. 290 van het decreet van 19 dec.  2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in werking  getreden op 1 januari 2015 (art. 325)

###### Art. 3.14.3.0.2.  Art. 3.14.3.0.2.

In het geval, vermeld in artikel 3.14.3.0.1, eerste lid,  vangt de schorsing aan met de inleidende vordering en  eindigt als de rechterlijke beslissing in kracht van  gewijsde is gegaan.

In het geval, vermeld in artikel 3.14.3.0.1, tweede lid,  vangt de schorsing aan met het verzoek waarbij het  administratief beroep wordt ingeleid. Ze eindigt:

1° als de belastingplichtige een rechtsvordering heeft  ingesteld, op de dag dat de rechterlijke beslissing in  kracht van gewijsde is gegaan;

2° in de andere gevallen, na verloop van de termijn die  voor de belastingplichtige openstaat om een beroep in te  stellen tegen de administratieve beslissing.

###### Art. 3.14.3.0.3.  Art. 3.14.3.0.3.  Elke daad van onderzoek of van vervolging als vermeld  in artikel 22 van de Voorafgaande Titel van het Wetboek  van Strafvordering, betreffende de misdrijven, vermeld  in artikel 3.15.3.0.1 tot en met 3.15.3.0.4 van deze  codex, schorst de verjaring van de belastingen die erop  betrekking hebben.

De schorsing begint bij het opstarten van de  strafvordering, en eindigt op een van de volgende  momenten:

2° als de strafvordering vervalt;  2° en cas d’abandon de l’action pénale ;

3° als het vonnis of arrest in kracht van gewijsde is  gegaan voor de misdrijven, vermeld in het eerste lid.

---- historiek ----  ---- historique ----

- ingevoegd door art. 51 van het decreet van 21.12.2018  (B.S. 28.12.2018). Tekst treedt in werking op 07.01.2019

### Hoofdstuk 15 - Strafrechtelijke vervolging  Chapitre 15 - Poursuite pénale

#### Afdeling 1 - Algemene bepalingen  Section 1re - Dispositions générales

###### Art. 3.15.1.0.1.  Art. 3.15.1.0.1.

Overeenkomstig artikel 460 van het federale WIB 92 en  artikel 94, § 1, van het Wetboek van de minnelijke en  gedwongen invordering van fiscale en niet-fiscale  schuldvorderingen wordt de strafvordering uitgeoefend  door het Openbaar Ministerie.

Het Openbaar Ministerie kan echter geen vervolgingen  instellen, indien het kennis heeft gekregen van de feiten  ten gevolge van een klacht of een aangifte van het  bevoegd personeelslid dat niet de machtiging had  waarvan sprake is in artikel 29, § 2, van het Wetboek van  Strafvordering.

Het Openbaar Ministerie kan de strafrechtelijk strafbare  feiten vervolgen waarvan het tijdens het in artikel 29, §  3, van het Wetboek van Strafvordering bedoelde overleg  kennis heeft genomen.

---- historiek ----  ---- historique ----

- gewijzigd door art. 68 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

§ 1. Overeenkomstig artikel 461 van het federale WIB  92 en onverminderd het in artikel 29, § 3, van het  Wetboek van Strafvordering bedoelde overleg kan de  procureur des Konings, indien hij een vervolging instelt  wegens feiten die strafrechtelijk strafbaar zijn ingevolge  de bepalingen van deze codex of van de ter uitvoering  ervan genomen besluiten, het advies vragen van het  bevoegde personeelslid. De procureur des Konings  voegt het feitenmateriaal waarover hij beschikt bij zijn  verzoek om advies. Het bevoegde personeelslid  antwoordt op dit verzoek binnen vier maanden na de  ontvangst ervan.

In geen geval schorst het verzoek om advies de  strafvordering.

§ 2. Overeenkomstig artikel 462 van het federale WIB  92 en in het kader van de kennisgeving en het overleg  bedoeld in artikel 29, § 2 en § 3, van het Wetboek van  Strafvordering, deelt het bevoegde personeelslid, de  gegevens van het fiscaal dossier met betrekking tot de  feiten die strafrechtelijk strafbaar zijn ingevolge de  bepalingen van deze codex of van de ter uitvoering ervan  genomen besluiten mede aan het Openbaar Ministerie.

---- historiek ----  ---- historique ----

- gewijzigd door art. 69 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

#### Afdeling 2 - Opsporing van inbreuken  Section 2 - Détection d'infractions

###### Art. 3.15.2.0.1.  Art. 3.15.2.0.1.

Voorbehouden voor toekomstig gebruik.  Réservé pour un usage futur

#### Afdeling 3 - Strafrechtelijke sancties  Section 3 - Sanctions pénales

###### Art. 3.15.3.0.1.  Art. 3.15.3.0.1.

Een persoon die met bedrieglijk opzet of met het  oogmerk om te schaden de bepalingen van deze codex  of van de besluiten die genomen zijn ter uitvoering  ervan,  overtreedt,  wordt  gestraft  met  een  gevangenisstraf van acht dagen tot twee jaar en met een  geldboete van 250 euro tot 500.000 euro of met een van  die straffen alleen.

---- historiek ----  ---- historique ----

- gewijzigd door art. 70 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

Een persoon wordt gestraft met een gevangenisstraf van  een maand tot vijf jaar en met een geldboete van 250  euro tot 500.000 euro of met een van die straffen alleen  als hij, met het oogmerk om een van de misdrijven,  vermeld in artikel 3.15.3.0.1, te plegen, in openbare  geschriften, in handelsgeschriften of in private  geschriften valsheid pleegt, of als hij gebruikmaakt van  een geschrift dat op die manier vervalst is.

Een persoon die willens en wetens een vals getuigschrift  opstelt dat de belangen van het Vlaamse Gewest kan  schaden of die van een dergelijk getuigschrift  gebruikmaakt, wordt gestraft met een gevangenisstraf  van acht dagen tot twee jaar en met een geldboete van  250 euro tot 500.000 euro of met een van die straffen  alleen.

---- historiek ----  ---- historique ----

- gewijzigd door art. 70 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

###### Art. 3.15.3.0.3.  Art. 3.15.3.0.3.  Een persoon die een valse getuigenis aflegt, die als tolk  of als deskundige een valse verklaring aflegt, of die een  of meer getuigen, deskundigen of tolken in een van de  informatiegevallen die toegelaten zijn met toepassing  van artikel 3.5.4.0.1, 3.5.8.0.1, 3.13.1.3.1 en 3.13.1.3.5,  verleidt, wordt gestraft overeenkomstig de bepalingen  van artikel 220 tot en met 224 van het Strafwetboek.

###### Art. 3.15.3.0.4.  Art. 3.15.3.0.4.

De niet-verschijning of de weigering om te getuigen in  de onderzoeken die toegelaten zijn met toepassing van  artikel 3.5.4.0.1, 3.5.8.0.1, 3.13.1.3.1 en 3.13.1.3.5,  wordt gestraft met een gevangenisstraf van acht dagen  tot zes maanden en met een geldboete van 125 euro tot  500.000 euro of met een van die straffen alleen.

---- historiek ----  ---- historique ----

- gewijzigd door art. 71 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

###### Art. 3.15.3.0.5.  Art. 3.15.3.0.5.

De schending van het beroepsgeheim, vermeld in artikel  3.19.0.0.2, wordt gestraft conform artikel 458 van het  Strafwetboek.

§ 1. Als de beoefenaar van een van de volgende  beroepen of van een ander beroep dat tot doel heeft voor  een of meer belastingplichtigen boek te houden of te  helpen houden, ofwel voor eigen rekening ofwel als  hoofd, lid of bediende van een vennootschap,  vereniging, groepering of onderneming of, meer in het  algemeen, het beroep dat erin bestaat een of meer  belastingplichtigen raad te geven of bij te staan bij het  vervullen van de verplichtingen, opgelegd bij deze  codex of bij de besluiten die vastgesteld zijn ter  uitvoering ervan, wordt veroordeeld wegens een van de  misdrijven, vermeld in artikel 3.15.3.0.1 tot en met  3.15.3.0.5, kan het vonnis hem het verbod opleggen om  gedurende drie maanden tot vijf jaar, rechtstreeks of  onrechtstreeks, dezelfde beroepen op welke wijze ook  uit te oefenen:

1° belastingadviseur;  1° conseiller comptable ;

2° zaakbezorger;  2° représentant ;

3° deskundige in belastingzaken of in boekhouden.  3° expert en affaires comptables ou en comptabilité.

De rechter kan bovendien, als hij zijn beslissing op dat  stuk motiveert, voor een duur van drie maanden tot vijf  jaar de sluiting bevelen van de inrichtingen van de  vennootschap, vereniging, groepering of onderneming  waarvan de veroordeelde hoofd, lid of bediende is.

§ 2. Het verbod en de sluiting, vermeld in paragraaf 1,  treden in werking vanaf de dag waarop de veroordeling  in kracht van gewijsde is gegaan.

###### Art. 3.15.3.0.7.  Art. 3.15.3.0.7.

Een persoon die rechtstreeks of onrechtstreeks het  verbod of de sluiting, uitgesproken met toepassing van  artikel 3.15.3.0.6 of 3.16.0.0.5, overtreedt, wordt  gestraft met een gevangenisstraf van acht dagen tot twee  jaar en met een geldboete van 250 euro tot 500.000 euro  of met een van die straffen alleen.

---- historiek ----  ---- historique ----

- gewijzigd door art. 72 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- gewijzigd door art. 52 van het decreet van 07.12.2018  (B.S. 20.12.2018). Tekst in werking getreden op  01.01.2019

De wet van 5 maart 1952 betreffende de opdecimes op  de strafrechterlijke geldboeten, is van toepassing op de  misdrijven, vermeld in artikel 3.15.3.0.1, 3.15.3.0.2,  3.15.3.0.4 en 3.15.3.0.7.

---- historiek ----  ---- historique ----

- gewijzigd door art. 73 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

###### Art. 3.15.3.0.9.  Art. 3.15.3.0.9.

Personen die als daders of als medeplichtigen van  misdrijven als vermeld in artikel 3.15.3.0.1 tot en met  3.15.3.0.4, zijn veroordeeld, zijn hoofdelijk gehouden  tot betaling van de ontdoken belasting en de  nalatigheidsintresten  verschuldigd  door  de  belastingplichtige.

De personen die beschuldigd zijn als daders of als  medeplichtigen van misdrijven als vermeld in artikel  3.15.3.0.1 tot en met 3.15.3.0.4, zijn ook hoofdelijk  gehouden tot betaling van de ontdoken belasting en de  nalatigheidsinteresten, vermeld in het eerste lid, als de  bestanddelen van de misdrijven bewezen verklaard zijn,  en als ze genieten van:

1° een opschorting van de uitspraak van de veroordeling  of een uitstel van de tenuitvoerlegging van de straffen  als vermeld in hoofdstuk III en hoofdstuk IV van de wet  van 29 juni 1964 betreffende de opschorting, het uitstel  en de probatie;

2° een veroordeling bij eenvoudige schuldigverklaring  als vermeld in artikel 21ter van de Voorafgaande Titel  van het Wetboek van Strafvordering;

3° de procedure van voorafgaande erkenning van schuld,  vermeld in artikel 216 van het Wetboek van  Strafvordering;

4° de verjaring van de strafvordering.  4° la prescription de l’action disciplinaire.

De natuurlijke personen of de rechtspersonen zijn  burgerlijk  en hoofdelijk aansprakelijk  voor de  geldboeten en kosten die het gevolg zijn van de

---- historiek ----  ---- historique ----

- gewijzigd door art. 52 van het decreet van 21.12.2018  (B.S. 28.12.2018). Tekst treedt in werking op 07.01.2019

###### Art. 3.15.3.0.10.  Art. 3.15.3.0.10.

De rechter kan bevelen dat ieder vonnis of arrest  houdende  veroordeling  tot  een  gevangenisstraf,  uitgesproken met toepassing van artikel 3.15.3.0.1 tot en  met 3.15.3.0.4 en artikel 3.15.3.0.7, wordt aangeplakt in  de plaatsen die hij bepaalt en, eventueel bij uittreksel,  wordt bekendgemaakt op de wijze die hij bepaalt, op  kosten van de veroordeelde.

De mogelijkheid, vermeld in het eerste lid, geldt ook  voor iedere met toepassing van artikel 3.15.3.0.6  uitgesproken beslissing tot verbod van het uitoefenen  van een beroepswerkzaamheid in België of tot sluiting  van de in het land geëxploiteerde inrichtingen.

###### Art. 3.15.3.0.11.  Art. 3.15.3.0.11.

Als de verkeersbelasting, de belasting op de  inverkeerstelling of de kilometerheffing niet is betaald,  kan de rechtbank de nummerplaat van het voertuig  verbeurd verklaren en de teruggave ervan bevelen aan  de overheid die belast is met de inschrijving van de  voertuigen.

---- historiek ----  ---- historique ----

- vervangen door art. 37 van het decreet van 3 juli 2015  (B.S., 10.08.2015). De tekst treedt in werking op 1 april  2016 (art. 44))

###### Art. 3.15.3.0.12.  Art. 3.15.3.0.12.

Met behoud van de toepassing van hoofdstuk VII van  boek 1 van het Strafwetboek wordt de persoon die, op  welke plaats en onder welke vorm ook, in het openbaar  of op een andere wijze, spelen of weddenschappen  organiseert of exploiteert, aan die organisatie of aan die  exploitatie deelneemt door spelen of weddenschappen  aan te bieden of door rechtstreeks of met hulp van een  tussenpersoon te spelen of te wedden, of zich aanbiedt  om gelden die bestemd zijn tot de dienst van spelen of  van weddenschappen in ontvangst te nemen, ze inzamelt  of ze stort, beschouwd als dader, mededader of  medeplichtige van de overtredingen van de bepalingen

---- historiek ----  ---- historique ----

- ingevoegd door art. 53 van het decreet van 07.12.2018  (B.S. 20.12.2018). Tekst in werking

getreden op 01.01.2019

###### Art. 3.15.3.0.13.  Art. 3.15.3.0.13.

Met behoud van de toepassing van de andere bepalingen  van dit hoofdstuk, kan een overtreding op de bepalingen  van deze codex over de belasting op de spelen en  weddenschappen, of van de uitvoeringsbesluiten ervan,  aanleiding geven tot de verbeurdverklaring van de  gelden of effecten die bij spelen of weddenschappen zijn  ingezet of die bestemd zijn voor de dienst van de spelen  of de weddenschappen en in het bezit worden gevonden  van de overtreders op het ogenblik dat het misdrijf wordt  vastgesteld.

---- historiek ----  ---- historique ----

- ingevoegd door art. 54 van het decreet van 07.12.2018  (B.S. 20.12.2018). Tekst in werking

getreden op 01.01.2019

### Hoofdstuk 16 - Administratieve sancties  Chapitre 16 - Sanctions administratives

---- historiek ----  ---- historique ----

- hoofdstuk 16 gewijzigd door art. 291 van het decreet  van 19 dec. 2014 (B.S., 29.01.2015 - Ed. 2). De tekst is

in werking getreden op 1 januari 2015 (art. 325)

###### Art. 3.16.0.0.1.  Art. 3.16.0.0.1.

De Vlaamse Regering kan voor een tijdperk dat vijf jaar  niet overtreft, elke persoon het recht ontzeggen  belastingplichtigen  te  vertegenwoordigen  in  de  hoedanigheid van lasthebber, behalve als die persoon  onderworpen  is  aan  een  wettelijk  ingestelde  beroepstucht of zijn last vervult krachtens de wet of een  rechterlijke beslissing.

###### Art. 3.16.0.0.2.  Art. 3.16.0.0.2.

Het besluit, vermeld in artikel 3.16.0.0.1, mag pas  worden uitgevaardigd nadat de betrokken lasthebber is  uitgenodigd om binnen twintig dagen te verschijnen, om  te worden gehoord door het bevoegde personeelslid. De  lasthebber mag zich door een raadsman laten bijstaan.

Er wordt een proces-verbaal opgemaakt van het verhoor,  vermeld in het eerste lid. Na voorlezing wordt het  proces-verbaal door het bevoegde personeelslid en de  betrokken lasthebber ondertekend. Ze laten hun

Een eensluidend verklaard afschrift van het proces-  verbaal wordt binnen acht dagen na zijn dagtekening aan  de lasthebber ter kennis gegeven.

###### Art. 3.16.0.0.3.  Art. 3.16.0.0.3.

Het besluit, vermeld in artikel 3.16.0.0.1, waarvan een  eensluidend verklaard afschrift met een aangetekende  brief naar de betrokken lasthebber wordt gestuurd, wordt  in uittreksel in het Belgisch Staatsblad bekendgemaakt,  tenzij de betrokkene zijn beroep heeft ingesteld bij de  Raad van State. In dat geval zal de bekendmaking in het  Belgisch Staatsblad alleen plaatsvinden als het besluit  niet door de Raad van State verbroken is.

###### Art. 3.16.0.0.4.  Art. 3.16.0.0.4.

Derden die betreffende de erfbelasting administratieve  geldboeten verschuldigd zijn, zijn zelf gehouden tot  betaling van de belastingen en toebehoren die ten  gevolge van de overtreding niet konden worden geïnd.

---- historiek ----  ---- historique ----

- gewijzigd door art. 292 van het decreet van 19 dec.  2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in werking  getreden op 1 januari 2015 (art. 325)

###### Art. 3.16.0.0.5.  Art. 3.16.0.0.5.

Met behoud van de toepassing van hoofdstuk 15, kan een  overtreding op de bepalingen van deze codex over de  belasting op de spelen en weddenschappen, of van de  uitvoeringsbesluiten ervan, aanleiding geven tot de  sluiting van de kansspelinrichting of tot het verbod om  inzetten of weddenschappen aan te nemen voor een duur  van tien dagen tot dertig dagen.

Als het gaat om een weigering om de reglementaire  controlemaatregelen, vermeld in titel 3, hoofdstuk 13, na  te leven of de belasting te betalen, ofwel om een verzet  tegen het optreden van de bevoegde personeelsleden,  wordt de sluiting of het verbod gehandhaafd zolang die  weigering of dat verzet blijft bestaan.

De sluiting van de kansspelinrichting of het verbod om  inzetten of weddenschappen aan te nemen wordt door  het bevoegde personeelslid uitgesproken en wordt  meegedeeld aan de bevoegde procureur des Konings die  voor de uitvoering ervan zorgt.

De voorziening schorst de uitvoering van de beslissing  niet als die laatste genomen is wegens de weigering om  de reglementaire controlemaatregelen, vermeld in titel 3,  hoofdstuk 13, na te leven of de belasting te betalen,  ofwel, wegens het verzet tegen het optreden van de  bevoegde personeelsleden.

---- historiek ----  ---- historique ----

- ingevoegd door art. 55 van het decreet van 07.12.2018  (B.S. 20.12.2018). Tekst in werking

getreden op 01.01.2019

### Hoofdstuk 17 – Bewijsmiddelen  Chapitre 17 - Moyens de preuve

---- historiek ----  ---- historique ----

- hoofdstuk 17 gewijzigd door art. 293 van het decreet  van 19 dec. 2014 (B.S., 29.01.2015 - Ed. 2). De tekst is

in werking getreden op 1 januari 2015 (art. 325)

###### Art. 3.17.0.0.1.  Art. 3.17.0.0.1.

Om het bestaan en het bedrag van de belastingschuld te  bepalen, alsook ter vaststelling van een overtreding van  de bepalingen van deze codex of van de besluiten die  genomen zijn ter uitvoering ervan, kan de bevoegde  entiteit  van  de  Vlaamse  administratie  alle  bewijsmiddelen aanvoeren die door het gemeen recht  toegelaten zijn, met inbegrip van de processen-verbaal,  opgesteld door het bevoegde personeelslid, maar met  uitzondering van de eed.

De processen-verbaal hebben bewijskracht tot bewijs  van het tegendeel.

###### Art. 3.17.0.0.2.  Art. 3.17.0.0.2.

Aan de bevoegde entiteit van de Vlaamse administratie  kan niet worden tegengeworpen, de rechtshandeling  noch het geheel van rechtshandelingen dat een zelfde  verrichting tot stand brengt, wanneer die entiteit door  vermoedens of door andere bewijsmiddelen, vermeld in  artikel 3.17.0.0.1, en aan de hand van objectieve  omstandigheden aantoont dat er sprake is van fiscaal  misbruik.

1° hetzij een verrichting waarbij hij zichzelf in strijd met  de doelstellingen van een bepaling van deze codex of de  ter uitvoering daarvan genomen besluiten buiten het  toepassingsgebied van die bepaling plaatst;

2° hetzij een verrichting waarbij aanspraak wordt  gemaakt op een belastingvoordeel, voorzien door een  bepaling van deze codex of de ter uitvoering daarvan  genomen besluiten, en de toekenning van dit voordeel in  strijd zou zijn met de doelstellingen van die bepaling en  die in wezen het verkrijgen van dit voordeel tot doel  heeft.

Het komt aan de belastingplichtige toe te bewijzen dat  de keuze voor zijn rechtshandeling of het geheel van  rechtshandelingen door andere motieven verantwoord is  dan het ontwijken van de belasting. Als de  belastingplichtige het tegenbewijs niet levert, dan wordt  de verrichting aan een belastingheffing overeenkomstig  het doel van deze codex onderworpen alsof het misbruik  niet heeft plaatsgevonden.

---- historiek ----  ---- historique ----

- vervangen door art. 294 van het decreet van 19 dec.  2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in werking  getreden op 1 januari 2015 (art. 325)

###### Art. 3.17.0.0.3.  Art. 3.17.0.0.3.

Wat de erfbelasting betreft, wordt elke schuld, waarvan  het bestaan bewezen wordt door een stuk voor te leggen  waarop een niet-gedagtekend betalingsbewijs is gesteld,  geacht vóór het overlijden voldaan te zijn, tenzij het  tegendeel bewezen wordt.

---- historiek ----  ---- historique ----

- toegevoegd door art. 295 van het decreet van 19 dec.  2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in werking  getreden op 1 januari 2015 (art. 325)

###### Art. 3.17.0.0.4.  Art. 3.17.0.0.4.

Wat de registratiebelasting betreft, wordt de verandering  in eigen-dom of vruchtgebruik van een onroerend goed  dat in België ligt, ten gevolge van een overdragende of  aanwijzende overeenkomst, voor de invordering van de  belastingen en toebehoren bij de nieuwe eigenaar of  vruchtgebruiker, in voldoende mate bewezen door daden  van beschikking of van bestuur of door andere  handelingen of akten waarbij de eigendom of het

---- historiek ----  ---- historique ----

- toegevoegd door art. 296 van het decreet van 19 dec.  2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in werking  getreden op 1 januari 2015 (art. 325)

###### Art. 3.17.0.0.5.  Art. 3.17.0.0.5.

Wat de registratiebelasting betreft, wordt iedere  tussenpersoon die de verkoop van een onroerend goed  bewerkstelligt, voor de invordering van de belastingen  en toebehoren als koper voor eigen rekening beschouwd.  Hij mag zich op de hoedanigheid van lasthebber of van  commissionair van de verkoper niet beroepen als  vaststaat dat hij al voor de totstandbrenging van de  verkoop aan de verkoper de prijs of elke som die  voortkomt uit de verkoop, betaald heeft of er zich toe  verbonden heeft die prijs of som te betalen.

De tussenpersoon, vermeld in het eerste lid, wordt  geacht het onroerend goed te hebben verkregen op de  dag van de betaling of van de verbintenis tot betaling.

---- historiek ----  ---- historique ----

- toegevoegd door art. 297 van het decreet van 19 dec.  2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in werking  getreden op 1 januari 2015 (art. 325)

###### Art. 3.17.0.0.6.  Art. 3.17.0.0.6.

Als een akte of geschrift waarvan geen minuut bestaat,  inlichtingen bevat die kunnen dienen om verschuldigde  bedragen te ontdekken, heeft het bevoegde personeelslid  het recht er een afschrift van te maken en dat eensluidend  te laten verklaren met het origineel door de  instrumenterende openbare of ministeriële ambtenaar of  officier of, als het gaat om een onderhandse of in het  buitenland verleden akte, door de betrokken persoon die  de registratie heeft gevorderd. Bij weigering waarmerkt  het bevoegde personeelslid zelf de eensluidendheid van  het afschrift, met vermelding van de weigering. Het  afschrift wordt, behoudens bewijs van het tegendeel, als  eensluidend beschouwd

---- historiek ----  ---- historique ----

- toegevoegd door art. 298 van het decreet van 19 dec.  2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in werking  getreden op 1 januari 2015 (art. 325)

###### Art. 3.17.0.0.7.  Art. 3.17.0.0.7.

De datum van de onderhandse akten of van de  overeenkomsten die door het feit alleen van hun bestaan

---- historiek ----  ---- historique ----

- toegevoegd door art. 299 van het decreet van 19 dec.  2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in werking  getreden op 1 januari 2015 (art. 325)

###### Art. 3.17.0.0.8.  Art. 3.17.0.0.8.

Voor het bewijs van het passief van de nalatenschap  betreffende de erfbelasting volstaat het voorleggen van  de rechtstitel niet om het bestaan vast te stellen van :

1° de hypotheekschulden waarvan de inschrijving op de  dag waarop de nalatenschap openviel, doorgehaald was  of sinds één jaar vervallen was;

2° de interesten van de al dan niet hypothecaire  schulden, van de huur- en pachtsommen, boven het  vervallen en het lopende jaar;

3° de sinds meer dan een jaar vóór het overlijden  verschenen termijnen van schuldbekentenissen waarvan  het bedrag bij annuïteiten wordt afgelost.

---- historiek ----  ---- historique ----

- toegevoegd door art. 300 van het decreet van 19 dec.  2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in werking  getreden op 1 januari 2015 (art. 325)

###### Art. 3.17.0.0.9.  Art. 3.17.0.0.9.

Tegenbrieven zijn niet tegenstelbaar aan het Vlaamse  Gewest als ze een vermindering van het actief of een  vermeerdering van het passief van de nalatenschap tot  gevolg hebben.

---- historiek ----  ---- historique ----

- toegevoegd door art. 301 van het decreet van 19 dec.  2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in werking  getreden op 1 januari 2015 (art. 325)

###### Art. 3.17.0.0.10.  Art. 3.17.0.0.10.

Het tegenbewijs van de vermoedens van eigendom,  vermeld in artikel 2.7.3.2.6, kan geleverd worden door  alle rechtsmiddelen, met inbegrip van getuigen en  vermoedens, maar met uitzondering van de eed.

---- historiek ----  ---- historique ----

###### Art. 3.17.0.0.11.  Art. 3.17.0.0.11.

Het bewijs dat te leveren is krachtens artikel 2.7.1.0.6, §  2, tweede lid, artikel 2.7.1.0.7, tweede lid, 1°, artikel  2.7.1.0.8, tweede lid, 1°, artikel 2.7.1.0.9, tweede lid, 1°,  artikel 2.7.3.2.8, tweede lid, en artikel 2.7.3.2.11, kan  door alle gewone rechtsmiddelen, ook door getuigen en  vermoedens, bijgebracht worden.

---- historiek ----  ---- historique ----

- toegevoegd door art. 303 van het decreet van 19 dec.  2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in werking  getreden op 1 januari 2015 (art. 325)

###### Art. 3.17.0.0.12.  Art. 3.17.0.0.12.

In het geval, vermeld in artikel 2.7.3.4.2, zevende lid,  moet het bestaan van de schulden bewezen worden door  de bewijsmiddelen die in rechte toelaatbaar zijn in de  verhouding tussen schuldeiser en schuldenaar.

De schulden met betrekking tot het beroep van de  erflater en de schulden met betrekking tot de  huishoudelijke uitgaven van het verstreken jaar en van  het lopende jaar kunnen door getuigen en vermoedens  worden vastgesteld.

---- historiek ----  ---- historique ----

- gewijzigd door art. 74 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- toegevoegd door art. 304 van het decreet van 19 dec.  2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in werking  getreden op 1 januari 2015 (art. 325)

### Hoofdstuk 18 - Belastingverhogingen en

administratieve geldboetes

###### Art. 3.18.0.0.1.  Art. 3.18.0.0.1.

§ 1. Het bevoegde personeelslid kan een administratieve  geldboete van 50 euro tot 1250 euro opleggen voor  iedere overtreding van de bepalingen van deze codex,  alsook van de besluiten die genomen zijn ter uitvoering  ervan, met uitzondering van overtredingen van artikel  3.1.0.0.2, §§ 2 tot en met 4 en van de bepalingen,  vermeld in hoofdstuk 23.

2° voor iedere overtreding van artikel 3.12.3.0.3 : een  administratieve geldboete van 50 euro ten laste van de  notaris die nagelaten heeft de schenker te vragen de  verklaring te doen;

3° voor iedere overtreding van artikel 3.12.3.0.6 : een  administratieve geldboete van 50 euro ten laste van de  notaris of gerechtsdeurwaarder;

4° voor iedere overtreding van artikel 3.3.1.0.8, § 1, 9° :  een administratieve geldboete van 50 euro tot 250 euro  ten laste van iedere overtreder afzonderlijk;

5° voor iedere overtreding van artikel 3.10.5.5.2 en  artikel 3.13.1.2.8 : een administratieve geldboete van  250 euro tot 500 euro ten laste van iedere overtreder  afzonderlijk;

6° voor iedere overtreding van artikel 3.13.1.3.7, die  volgt uit een overtreding van artikel 96, 97, 99 of 103 1  van het federale Wetboek van Successierechten : een  administratieve geldboete van 250 euro tot 500 euro ten  laste van iedere overtreder afzonderlijk;

7° voor iedere overtreding van artikel 3.13.1.2.1, derde  en vierde lid, en artikel 3.13.1.3.1, § 1 en § 6 : een  administratieve geldboete van 250 euro tot 2500 euro ten  laste van iedere overtreder afzonderlijk;

8° voor iedere overtreding van artikel 3.13.1.3.7, die  volgt uit een overtreding van artikel 98, 101 of 1021 van  het federale Wetboek van Successierechten : een  administratieve geldboete van 250 euro tot 2500 euro ten  laste van iedere overtreder afzonderlijk;

9° voor iedere weigering van inzageverlening, waardoor  inbreuk wordt gepleegd op artikel 3.13.1.1.1, artikel  3.13.1.2.1 of artikel 3.13.1.3.1 : een administratieve  geldboete van 250 euro tot 2500 euro ten laste van de  persoon, vermeld in artikel 2.9.4.2.4, § 1, die de  beroepsverklaring, vermeld in artikel 2.9.4.2.4, § 2, 1°,  heeft ondertekend;

11° voor iedere weigering van inzageverlening,  waardoor inbreuk wordt gepleegd op artikel 3.13.1.1.1,  artikel  3.13.1.2.1  of  artikel  3.13.1.3.1  :  een  administratieve geldboete van 1250 euro voor de  personen die de toepassing vragen van artikel 2.7.4.2.2  of artikel 2.8.6.0.3;

12° voor iedere overtreding van artikel 3.13.1.3.7, die  volgt uit het feit dat de kennisgeving, vermeld in artikel  1023 van het federale Wetboek van Successierechten,  niet verricht werd binnen de aldaar gestelde termijn : een  administratieve geldboete van 500 euro tot 10.000 euro,  waartoe de rechtspersoon en degenen die in zijn naam de  brandkast ter beschikking van de derde hebben gesteld,  hoofdelijk gehouden zijn.

§ 2/1. In afwijking van paragraaf 1, kan het bevoegde  personeelslid een administratieve geldboete van 5.000  euro opleggen voor een overtreding van artikel 2.2.4.0.9  als de overtreding is gepleegd met de bedoeling de  belasting te ontduiken of om dat mogelijk te maken.

§ 2/2. In afwijking van paragraaf 1, kan het bevoegde  personeelslid een administratieve geldboete van 5.000  euro opleggen voor een overtreding van artikel  2.3.4.1.10 als de overtreding is gepleegd met de  bedoeling de belasting te ontduiken of dat mogelijk te  maken.

§ 3. De administratieve geldboete, vermeld in paragraaf  1, kan ook worden opgelegd voor iedere overtreding van  artikel 473, 474 en 475 van het federale WIB 92 die de  vestiging van de belastingen, opgenomen in deze codex,  verhindert.

§ 4. Als de overtredingen, vermeld in paragraaf 1 en  paragraaf 2, blijven bestaan nadat een administratieve  geldboete wordt opgelegd, kan daarvoor een nieuwe  administratieve geldboete worden opgelegd telkens als  de overtreding opnieuw wordt vastgesteld. In dat geval  worden de bedragen, vermeld in paragraaf 1 of paragraaf  2, vermenigvuldigd met een factor die overeenkomt met  het aantal keer dat de overtreding is vastgesteld.  Dezelfde overtreding kan maximaal tien keer per  kalenderjaar worden beboet.

§ 4/1. Paragraaf 4 is niet van toepassing op de  kilometerheffing.

Onverminderd de toepassing van het tweede lid, wordt  er geen administratieve geldboete opgelegd voor iedere  overtreding die werd begaan binnen een ononderbroken  tijdvak van drie uren vanaf de vaststelling van een  eerdere overtreding op de bepalingen van deze codex en  de uitvoeringsbesluiten ervan of van de wetgeving van  het Brusselse Hoofdstedelijke Gewest of het Waalse  Gewest met betrekking tot de kilometerheffing, in  zoverre de betrokken overtredingen werden begaan met  hetzelfde voertuig en in zoverre een administratieve  geldboete werd opgelegd voor de eerst begane  overtreding.

L'amende administrative, visée à l'alinéa 2, est calculée  selon le tableau suivant :

De administratieve geldboete, vermeld in het tweede lid,  wordt berekend volgens de volgende tabel:

Categorie van  de overtreding

/  Catégorie  d'infraction

euros)  A  -manipulatie van de  boordapparatuur;  -vervalsing van de voertuigdocumenten  die nodig zijn om het maximaal  toegestane totaalgewicht en de euro- emissieklasse van het voertuig te  bepalen;

B  -er is geen boordapparatuur voor België  aan boord van het voertuig;  -er is geen  dienstverleningsovereenkomst afgesloten  voor het betrokken voertuig;

-de boordapparatuur aan boord van het  voertuig is diegene van een ander  voertuig; -gebruik van het belastbaar  wegennet terwijl de dienst- verleningsovereenkomst geschorst is;

-gebruik van het belastbaar wegennet  nadat de boordapparatuur het signaal  heeft ontvangen dat het ter beschikking  gestelde gegarandeerde betaalmiddel  ontoereikend is geworden;

- gebruik van het belastbaar wegennet  terwijl de boordapparatuur een  probleem signaleert, of elk signaal door  de boordapparatuur ontbreekt, zonder  dat de houder van het voertuig zich  onmiddellijk in verbinding stelt met de  dienstaanbieder of de  hoofddienstaanbieder;

- gebruik van het belastbaar  wegennet terwijl de  boordapparatuur een probleem  signaleert, of elk signaal door  de boordapparatuur ontbreekt,  nadat de houder van het  voertuig zich onmiddellijk in  verbinding stelt met de  dienstaanbieder of de  hoofddienstaanbieder, maar  zonder dat hij de gegeven  instructies naleeft;

D  elke andere overtreding van de  regelgeving inzake de kilometer- heffing in deze codex en zijn  uitvoeringsbesluiten die hierboven niet  expliciet vermeld is

Het bevoegde personeelslid kan de administratieve  geldboete, vermeld in het vierde lid, categorie C,  verminderen tot 250 euro als de boete betrekking heeft  op de eerste overtreding van categorie C in het  betreffende kalenderjaar.

§ 5. De administratieve geldboeten, vermeld in paragraaf  1 tot en met paragraaf 4 worden ingevorderd volgens de  regels die van toepassing zijn op de overeenstemmende  belasting.

De administratieve geldboeten, vermeld in paragraaf  4/1, worden ingevorderd conform de bepalingen van  titel 3, met uitzondering van artikel 3.1.0.0.1, eerste en  tweede lid, en de bepalingen die louter betrekking  hebben op een andere belasting als vermeld in titel 2 dan  de kilometerheffing.

---- historiek ----  ---- historique ----

- §4/1 gewijzigd door art. 18 van het decreet van  03.05.2024 (B.S., 22.05.2024). Inwerkingtreding:  01.07.2025

- § 1 gewijzigd door art. 5 van het decreet van  19.04.2024 (B.S., 03.06.2024). Inwerkingtreding:  13.06.2024

- gewijzigd door art. 75 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- gewijzigd door art. 53 van het decreet van 21.12.2018  (B.S. 28.12.2018). Tekst treedt in werking op 07.01.2019

- gewijzigd door art. 97 van het decreet van 22.12.2017  (B.S.: 29.12.2017). Tekst in werking getreden op  01.01.2018

- gewijzigd door art. 4 van het decreet van 30.06.2017  (B.S.: 03.07.2017). Tekst in werking getreden op 1 juli  2017

- gewijzigd door art. 54 van het decreet van 23.12.2016

(B.S.: 30.12.2016). Tekst in werking getreden op 1 april  2016

- § 4, tweede, derde, vierde, vijfde lid toegevoegd door  art. 38 van het decreet van 3 juli 2015 (B.S., 10.08.2015).  De tekst treedt in werking op 1 april 2016 (besluit van de  Vlaamse Regering van 17 juli 2015 - B.S., 10.08.2015 -  art. 4)

- paragraaf 2/2 werd toegevoegd door art. 124 van het  decreet van 18 dec. 2015 (B.S., 29.12.2015). De tekst is  in werking getreden vanaf 1 januari 2016 (art. 135)

###### Art. 3.18.0.0.2.  Art. 3.18.0.0.2.

(…)  (…)

---- historiek ----  ---- historique ----

- opgeheven door art. 54 van het decreet van 21.12.2018  (B.S. 28.12.2018). Tekst treedt in werking op 07.01.2019

- gewijzigd door art. 55 van het decreet van 23.12.2016  (B.S.: 30.12.2016). Tekst in werking getreden op 1 april  2016

- tweede lid opgeheven door art. 31 van het decreet van  17 juli 2015 (B.S., 14.08.2015 ). De tekst is in werking  getreden op 14 augustus 2015 (art. 41)

###### Art. 3.18.0.0.3.  Art. 3.18.0.0.3.

In afwijking van artikel 3.2.2.0.1 kunnen de bevoegde  personeelsleden tijdens de uitvoering van het toezicht,  vermeld in artikel 3.13.2.0.1, de administratieve  geldboetes, vermeld in artikel 3.18.0.0.1, of de  belastingverhogingen, vermeld in artikel 3.18.0.0.2,  3.18.0.0.15/1 en 3.18.0.0.15/2, opleggen zonder dat ze  moeten worden ingekohierd. Als daarbij geen contante  betaling  verkregen  kan  worden,  worden  die  administratieve geldboetes of belastingverhogingen op  een later tijdstip alsnog ingekohierd.

---- historiek ----  ---- historique ----

- gewijzigd door art. 56 van het decreet van 07.12.2018  (B.S 20.12.2018). Tekst treedt in werking op 01.01.2019

###### Art. 3.18.0.0.4.  Art. 3.18.0.0.4.  De ontdoken verkeersbelasting wordt op het drievoudige  gebracht als ze een tiende van de oorspronkelijke  belasting overschrijdt.

Iedere persoon die een overtreding van de bepalingen  van deze codex betreffende de erfbelasting, alsook van  de ter uitvoering ervan genomen besluiten, heeft  gepleegd, is gehouden tot de betaling van de wegens  deze overtreding verschuldigde belastingverhoging.

Als verschillende personen een overtreding plegen die  aanleiding geeft tot een belastingverhoging inzake de  erfbelasting,  is  iedere  overtreder  voor  die  belastingverhoging gehouden tot de betaling ervan als  hij tot de betaling van de desbetreffende erfbelasting kan  worden gedwongen.

Als iemand verschillende overtredingen als vermeld in  het eerste lid gepleegd heeft, is hij voor al die  overtredingen een belastingverhoging verschuldigd.

---- historiek ----  ---- historique ----

- toegevoegd door art. 306 van het decreet van 19 dec.  2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in werking  getreden op 1 januari 2015 (art. 325)

###### Art. 3.18.0.0.6.  Art. 3.18.0.0.6.

§ 1er. Si la déclaration n'est pas introduite dans le délai  de déclaration visé à l'article 3.3.1.0.5, § 2 ou 3.3.1.0.6,  toute personne qui est tenue d'introduire une déclaration  est redevable d'une majoration d'impôt, conformément  au tableau suivant :

§ 1. Als de aangifte niet binnen de aangiftetermijn,  vermeld in artikel 3.3.1.0.5, § 2, of 3.3.1.0.6, is  ingediend, is elke persoon die tot de aangifte gehouden  is, een belastingverhoging verschuldigd, conform de  onderstaande tabel :

ogenblik van indiening na het verstrijken van de aangiftetermijn

/  moment de l'introduction après l'échéance du délai de la déclaration

Vanaf

/  jusqu'au dernier jour de  dag 1  maand 5  5  maand 6  maand 11  10  maand 12  maand 17  15  maand 18  20

/  à partir de

§ 2. Als met toepassing van artikel 3.3.1.0.7 de  aangiftetermijn is verlengd, is elke persoon die tot de  aangifte gehouden is, in afwijking van paragraaf 1 een  belastingverhoging verschuldigd, conform de  onderstaande tabel :

§ 2. Si, en application de l'article 3.3.1.0.7, le délai de  déclaration est prolongé, toute personne qui est tenue  d'introduire  une  déclaration, en  dérogation  au  paragraphe 1er, est redevable d'une majoration d'impôt,  conformément au tableau ci-dessous :  ogenblik van indiening na het verstrijken van de aangiftetermijn

/  moment de l'introduction après l'échéance du délai de la déclaration

Vanaf

/  à partir de

Als  met  toepassing  van  artikel  3.3.1.0.7  de  aangiftetermijn is verlengd, en de aangifte niet binnen de  toegestane verlengingstermijn wordt ingediend, wordt  paragraaf 1 opnieuw van toepassing.

---- historiek ----  ---- historique ----

- toegevoegd door art. 307 van het decreet van 19 dec.  2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in werking  getreden op 1 januari 2015 (art. 325)

###### Art. 3.18.0.0.7.  Art. 3.18.0.0.7.

De erfgenaam, legataris of begiftigde die niet alle  goederen  heeft  aangegeven  overeenkomstig  de  bepalingen  van  artikel  3.3.1.0.8,  betaalt  een  belastingverhoging die gelijk is aan 20 % van de  daardoor verschuldigde aanvullende rechten.

De belastingverhoging, vermeld in het eerste lid, wordt  vervangen door een belastingverhoging conform de  onderstaande tabel als een erfgenaam, legataris of  begiftigde uit eigen beweging, een goed dat in afwijking  van artikel 3.3.1.0.8 niet was opgenomen in de aangifte,  alsnog aangeeft:

ogenblik van indiening na het verstrijken van de aangiftetermijn, vermeld in  artikel 3.3.1.0.5, § 2, VCF of artikel 3.3.1.0.6 VCF / moment d'introduction  après l'expiration du délai de déclaration visé à l'article 3.3.1.0.5, § 2, du CFF,  ou à l'article 3.3.1.0.6 du CFF

belastingverhoging in % van de  te betalen erfbelasting /  accroissement d'impôt en % des  droits de succession à payer  vanaf de eerste dag van / à  partir du premier jour du

maand / mois 1  maand / mois 1  1

maand / mois 2  maand / mois 2  2

maand / mois 3  maand / mois 3  3

maand / mois 4  maand / mois 4  4

maand / mois 5  maand / mois 5  5

maand / mois 6  maand / mois 6  6

maand / mois 7  maand / mois 10  10

- gewijzigd door art. 49 van het decreet van 18.12.2020  (B.S., 30.12.2020). Van toepassing op nalatenschappen  opengevallen vanaf 01.01.2021

- tweede lid toegevoegd door art. 32 van het decreet van  17 juli 2015 (B.S., 14.08.2015 ). De tekst is in werking  getreden op 14 augustus 2015 (art. 41)

###### Art. 3.18.0.0.8.  Art. 3.18.0.0.8.

Als wordt vastgesteld dat de aangegeven waarde van de  aangegeven  goederen  te  laag  is,  is  een  belastingverhoging verschuldigd, conform de  onderstaande tabel :

verhouding van het tekort in % ten opzichte van de aangegeven waarde van

aanvullende rechten  /  rapport du manque en % par rapport à la valeur déclarée du bien

/  majoration d'impôt en %  des droits complémentaires  Vanaf / De  Tot / À  10  25  5  25  50  10  50  100  15  100  20

In  afwijking  van  het  eerste  lid,  wordt  de  belastingverhoging verminderd tot de helft van het  percentage van de verschuldigde aanvullende rechten,  vermeld in het eerste lid, als een erfgenaam, legataris of  begiftigde uit eigen beweging, en binnen tien maanden  na hetzij het overlijden, hetzij de start van de  aangiftetermijn zoals berekend overeenkomstig artikel  3.3.1.0.6, derde of vierde lid, voor een goed dat in  afwijking van artikel 3.3.1.0.8 voor een te lage waarde  was opgenomen in de aangifte, alsnog een hogere  waarde aangeeft.

---- historiek ----  ---- historique ----

- gewijzigd door art. 50 van het decreet van 18.12.2020  (B.S., 30.12.2020). Van toepassing op nalatenschappen  opengevallen vanaf 01.01.2021.

- vervangen door art. 33 van het decreet van 17 juli 2015  (B.S., 14.08.2015). De tekst is in werking getreden op 14  augustus 2015 (art. 325)

###### Art. 3.18.0.0.9.  Art. 3.18.0.0.9.

De erfgenaam, legataris of begiftigde die geen aangifte  als vermeld in artikel 3.3.1.0.5 of 3.3.1.0.6 indient,  betaalt een belastingverhoging die gelijk is aan 20 % van  de verschuldigde erfbelasting

- toegevoegd door art. 310 van het decreet van 19 dec.  2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in werking  getreden op 1 januari 2015 (art. 325)

###### Art. 3.18.0.0.10.  Art. 3.18.0.0.10.

Een belastingverhoging van 20 % van de aanvullende  rechten inzake de erfbelasting is verschuldigd door de  erfgenaam, legataris of begiftigde als de verplichte  vermeldingen, vermeld in artikel 3.3.1.0.8, foutief of  onvolledig zijn, tenzij die fout of onvolledigheid al  aanleiding geeft tot een belastingverhoging ingevolge de  toepassing van artikel 3.18.0.0.6, 3.18.0.0.7, 3.18.0.0.8  of 3.18.0.0.9.

---- historiek ----  ---- historique ----

- toegevoegd door art. 311 van het decreet van 19 dec.  2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in werking  getreden op 1 januari 2015 (art. 325)

###### Art. 3.18.0.0.11.  Art. 3.18.0.0.11.  Een  belastingverhoging  van  20  %  van  de  registratiebelasting, respectievelijk van de aanvullende  rechten, is in de volgende gevallen verschuldigd door :

1° de persoon die binnen de voorgeschreven termijnen  de akten of geschriften die aan de registratieformaliteit  zijn onderworpen, niet heeft laten registreren;

2° de schenker en begiftigde bij een onjuiste opgave van  hun  graad  van  verwantschap  of  van  de  samenwoningsrelatie die tussen hen bestaat;

3° elk van de begiftigden die de verbintenis, vermeld in  artikel 2.8.4.2.3, eerste lid, 2°, is aangegaan en niet is  nagekomen;

4° de schenker en de begiftigden in geval van de onjuiste  verklaring, vermeld in artikel 2.8.4.2.3, tweede lid;

4° /1 elk van de begiftigden die de verbintenis, vermeld  in artikel 2.8.4.3.1, § 2, derde lid, niet is nagekomen;

5° de belastingplichtige die voor de toepassing van  artikel 2.8.5.0.1 over het aantal afstammelingen een  onjuiste verklaring heeft afgelegd;

6° de verkrijger in geval van onjuiste vermeldingen van  de voorwaarden, vermeld in artikel 2.9.4.2.11, § 2, eerste  lid, 1°, artikel 2.9.4.2.12, § 1, eerste lid, 1°, 2° en 3°,  artikel 2.9.4.2.12, § 1, derde lid, artikel 2.9.4.2.13, § 1,  eerste lid, 1° en 2°, of artikel 2.9.4.2.14, § 1;

7° /1 de verkrijger, als het verlaagde tarief, vermeld in  artikel 2.9.4.2.11, § 1, vervalt bij gebrek aan  vervreemding van de woning of de bouwgrond en  waarmee voor de toepassing van artikel 2.9.4.2.11, § 2,  eerste lid, 1°, geen rekening is gehouden binnen de  termijn, vermeld in artikel 2.9.4.2.11, § 3, 1°;

7° /2 de verkrijger, als het verlaagde tarief, vermeld in  artikel 2.9.4.2.12, § 1, vervalt bij gebrek aan tijdige  uitvoering van de renovatie, gedeeltelijke herbouw of  herbouw, vermeld in artikel 2.9.4.2.12, § 1, eerste lid,  1°, of bij gebrek aan naleving van de voorwaarde,  vermeld in artikel 2.9.4.2.12, § 1, eerste lid, 2°;

7° /3 de verkrijger, als het verlaagde tarief, vermeld in  artikel 2.9.4.2.12, § 1, vervalt bij gebrek aan  vervreemding van de woning of de bouwgrond en  waarmee voor de toepassing van artikel 2.9.4.2.12, § 2,  1°, geen rekening is gehouden binnen de termijn,  vermeld in artikel 2.9.4.2.12, § 2, 1°;

7° /4 de verkrijger, als het verlaagd tarief, vermeld in  artikel 2.9.4.2.13, § 1, vervalt bij gebrek aan tijdige  verhuring als vermeld in artikel 2.9.4.2.13, § 1, eerste  lid, 1°, of bij gebrek aan tijdige indiening van de  bewijsstukken, vermeld in artikel 2.9.4.2.13, § 1, eerste  lid, 2°, of bij vroegtijdige beëindiging van de  huurovereenkomst  of  bij  gebrek  aan  tijdige  kennisgeving hiervan als vermeld in artikel 2.9.4.2.13, §  4;

7° /5 de verkrijger, als het verlaagd tarief, vermeld in  artikel 2.9.4.2.14, § 1, vervalt bij gebrek aan inschrijving  binnen de termijn, vermeld in artikel 2.9.4.2.14, § 2,  tweede lid, 1°;

7° /6 de verkrijger, als het verlaagde tarief, vermeld in  artikel 2.9.4.2.14, § 1, vervalt bij gebrek aan  vervreemding van de woning of de bouwgrond en  waarmee voor de toepassing van artikel 2.9.4.2.11, § 2,  eerste lid, 1°, geen rekening is gehouden binnen de  termijn, vermeld in artikel 2.9.4.2.14, § 5, 1°;

8° de persoon die een beroepsverklaring heeft  ondertekend, als hij bij het verstrijken van een termijn  van vijf jaar na die verklaring niet bij machte is om door  een reeks wederverkopen te laten blijken dat hij het  aangegeven  beroep  werkelijk  uitoefent,  zoals  voorgeschreven door artikel 2.9.4.2.4, § 4;

10° de partijen bij een ruiling als vermeld in artikel  2.9.4.2.8 voor elke te laag bevonden opleg of elk te laag  bevonden waardeverschil, en voor elke overschatting  van de kavels die een vermindering van de  registratiebelasting tot gevolg heeft;

11° de natuurlijke persoon die het voordeel heeft  genoten van artikel 2.9.5.0.1, in geval van onjuistheid of  niet-nakoming van de vermeldingen, voorgeschreven bij  artikel 2.9.5.0.2;

12° de cedent in geval van onjuiste vermeldingen  omtrent de voorwaarden, vermeld in artikel 2.9.6.0.1,  eerste lid, 4° ;

13° de natuurlijke persoon die een teruggave van de  registratiebelasting heeft ontvangen met toepassing van  artikel 3.6.0.0.6, in geval van onjuistheid of niet-  nakoming van de vermeldingen, voorgeschreven bij  artikel 3.6.0.0.6, § 3, zesde lid;

13° la personne physique qui a reçu un remboursement  de la taxe d'immatriculation en application de l'article  3.6.0.0.6, en cas d'inexactitude ou de non-respect des  mentions visées à l'article 3.6.0.0.6, § 3, sixième alinéa  ;  14° de partijen in geval van onjuistheid van de  verklaring over de uitbating van de geruilde onroerende  goederen, vermeld in artikel 3.12.3.0.1, § 3, derde lid;

15° de partijen, als voor de toepassing van artikel  3.12.3.0.4 bewuste vermeldingen ontbreken of als ze  onjuist of onvolledig zijn;

16° de personen die een verklaring afgelegd hebben over  elke andere onjuistheid, bevonden in de elementen van  een verklaring in of onderaan op de akte, gesteld tot  vereffening van de registratiebelasting, dan de  onjuistheid die beboet wordt met de belastingverhoging,  vermeld in artikel 3.18.0.0.15.

Voor de gevallen, vermeld in het eerste lid, 1°, 2°, 4°,  10°, 14° en 15°, zijn de vermelde personen of partijen  hoofdelijk  gehouden  tot  de  betaling  van  de  belastingverhoging.

In afwijking van het eerste lid, 1°, bedraagt de  belastingverhoging 1% van de registratiebelasting als de  persoon de voorgeschreven termijnen met hoogstens  dertig kalenderdagen heeft overschreden, zonder dat  deze belastingverhoging lager mag zijn dan 100 euro.

---- historiek ----  ---- historique ----

- gewijzigd door art. 36 van het decreet van 09.12.2022  (B.S., 20.12.2022). Inwerkingtreding: 30.12.2022

- gewijzigd door art. 8 van het decreet van 19.11.2021  (B.S., 16.12.2021). Inwerkingtreding: 01.01.2022

- gewijzigd door art. 5 van het decreet van 26 juni 2020  (B.S. 29.06.2020). Tekst treedt in werking op 01.06.2020

- gewijzigd door art. 55 van het decreet van 21.12.2018  (B.S. 28.12.2018). Tekst treedt in werking op 07.01.2019

- gewijzigd door art. 15 van het decreet van 18.05.2018  (B.S.: 28.05.2018). Tekst is van toepassing op  verkoopovereenkomsten afgesloten vanaf 1 juni 2018

- aangevuld door art. 43 van het decreet van 23  december 2016 (B.S., 29.12.2016). De tekst is in werking  getreden op 01 januari 2017

- punt 7° /1 ingevoegd door art. 34 van het decreet van  17 juli 2015 (B.S., 14.08.2015 ). De tekst is in werking  getreden op 14 augustus 2015 (art. 41)

###### Art. 3.18.0.0.12.  Art. 3.18.0.0.12.

Een belastingverhoging van 50 % van de aanvullende  rechten inzake de registratiebelasting is verschuldigd  door de verkrijgers als de verklaring, vermeld in artikel  3.12.3.0.1, § 1, 1°, onjuist wordt bevonden.

Une augmentation de l’impôt de 50 % des droits  complémentaires  en  matière  de  l’impôt  d’enregistrement est payable par les cessionnaires si la  déclaration, visée à l’article 3.12.3.0.1, § 1er, 1°, a été  jugée incorrecte.  Een belastingverhoging van 50 % van de aanvullende  rechten inzake de registratiebelasting is verschuldigd  door de schenker, als hij weigert de verklaring, vermeld  in artikel 3.12.3.0.3, te doen, of als deze verklaring  onjuist of onvolledig is.

---- historiek ----  ---- historique ----

- gewijzigd door art. 16 van het decreet van 18.05.2018  (B.S.: 28.05.2018). Tekst is van toepassing op  verkoopovereenkomsten afgesloten vanaf 1 juni 2018

- toegevoegd door art. 313 van het decreet van 19 dec.  2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in werking  getreden op 1 januari 2015 (art. 325)

###### Art. 3.18.0.0.13.  Art. 3.18.0.0.13.

S'il est constaté que la valeur qui est indiquée ou le prix  qui est indiqué pour le calcul de impôt d’enregistrement  est trop faible, une majoration d'impôt est due  conformément au tableau ci-dessous :

Als wordt vastgesteld dat de waarde die aangegeven is  of de prijs die opgegeven is voor de berekening van de  registratiebelasting, te laag is, is een belastingverhoging  verschuldigd, conform de onderstaande tabel :

/  rapport du manque en % par rapport à la valeur indiquée du bien

complémentaires  Vanaf / De  Tot / À  10  25  5  25  50  10  50  100  15  100  20

---- historiek ----  ---- historique ----

- toegevoegd door art. 314 van het decreet van 19 dec.  2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in werking  getreden op 1 januari 2015 (art. 325)

###### Art. 3.18.0.0.14.  Art. 3.18.0.0.14.

Een belastingverhoging van 100 % van de aanvullende  rechten inzake de registratiebelasting is in de volgende  gevallen verschuldigd door elk van de contracterende  partijen die aan de overtreding hebben deelgenomen:

1° in geval van bewimpeling over de prijs en de lasten  of de overeengekomen waarde;

2° als de overeenkomst, vastgesteld in een akte, niet  diegene is die door de partijen is gesloten, of als de akte  betreffende een overeenkomst, vermeld in artikel 19,  eerste lid, 2° of 5°, van het federale Wetboek van  Registratie-, Hypotheek- en Griffierechten, onvolledig  of onjuist is, met dien verstande dat ze al de  bestanddelen van de overeenkomst niet weergeeft.

In de gevallen, vermeld in het eerste lid, zijn de partijen  die aan de overtreding hebben deelgenomen, hoofdelijk  gehouden tot de betaling van de belastingverhoging.

---- historiek ----  ---- historique ----

- gewijzigd door art. 30 van het decreet van 08.12.2017  (B.S.: 14.12.2017). Tekst van toepassing vanaf  24.12.2017

- toegevoegd door art. 315 van het decreet van 19 dec.  2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in werking  getreden op 1 januari 2015 (art. 325)

###### Art. 3.18.0.0.15.  Art. 3.18.0.0.15.

De belastingverhogingen, vermeld in artikel 3.18.0.0.6  tot en met artikel 3.18.0.0.13, worden verhoogd tot 100  % als de overtredingen zijn gepleegd met de bedoeling  de belasting te ontduiken of dat mogelijk te maken.

- toegevoegd door art. 316 van het decreet van 19 dec.  2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in werking  getreden op 1 januari 2015 (art. 325)

###### Art. 3.18.0.0.15/1  Art. 3.18.0.0.15/1

In geval van een ambtshalve aanslag als vermeld in  artikel 2.12.7.0.1, of in geval van onjuiste gegevens op  de elektronische informatiedrager, vermeld in artikel  3.13.1.2.9, is een belastingverhoging verschuldigd van  20% van de belasting op de spelen en weddenschappen,  vermeld in artikel 2.12.4.0.1.

In afwijking van het eerste lid bedraagt de  belastingverhoging 100% als de overtredingen zijn  gepleegd met de bedoeling de belasting te ontduiken of  de vestiging ervan onmogelijk te maken, of indien het  gaat om een spel of weddenschap dat is verboden  krachtens artikel 4, 7 en 8 van de Kansspelwet van 7 mei  1999.

---- historiek ----  ---- historique ----

- ingevoegd door art. 57 van het decreet van 07.12.2018  (B.S. 20.12.2018). Tekst in werking

getreden op 01.01.2019

###### Art. 3.18.0.0.15/2  Art. 3.18.0.0.15/2

In geval van een ambtshalve aanslag als vermeld in  artikel 2.13.7.0.1, is een belastingverhoging per  automatisch ontspanningstoestel verschuldigd van 20%  van de verschuldigde belasting, met een minimum van  50 euro per aanslag.

In afwijking van het eerste lid bedraagt de  belastingverhoging 100%, met een minimum van 100  euro per aanslag, als de overtredingen zijn gepleegd met  de bedoeling de belasting te ontduiken of de vestiging  ervan onmogelijk te maken, of indien het gaat om een  verboden automatisch ontspanningstoestel als bedoeld  in artikel 2.13.7.0.2.

---- historiek ----  ---- historique ----

- gewijzigd door art. 10 van het decreet van 20.11.2020  (B.S., 03.12.2020). Inwerkingtreding vanaf aanslagjaar  2021

- ingevoegd door art. 58 van het decreet van 07.12.2018  (B.S. 20.12.2018). Tekst in werking

getreden op 01.01.2019

De leidend ambtenaar van de bevoegde entiteit van de  Vlaamse  administratie  kan  kwijtschelding  of  vermindering van de administratieve geldboetes of van  de belastingverhogingen, vermeld in dit hoofdstuk,  verlenen als de betrokken partij bewijst niet in fout te  zijn.

---- historiek ----  ---- historique ----

- toegevoegd door art. 317 van het decreet van 19 dec.  2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in werking  getreden op 1 januari 2015 (art. 325)

###### Art. 3.18.0.0.17.  Art. 3.18.0.0.17.

Zonder afbreuk te doen aan de geldigheid van de  bestuurs- of gerechtelijke handelingen, verricht met het  oog op de vestiging of de invordering van de  belastingschuld, wordt de mogelijkheid om een  administratieve geldboete of een belastingverhoging als  vermeld in dit hoofdstuk, op te leggen of in te vorderen  en het verloop van de verjaring van de vordering tot  voldoening ervan geschorst als het Openbaar Ministerie  de strafvordering overeenkomstig artikel 3.15.1.0.1  uitoefent. De aanhangigmaking bij de correctionele  rechtbank maakt het opleggen van of het invorderen van  een administratieve geldboete of een belastingverhoging  definitief  onmogelijk.  Daarentegen  maakt  de  beschikking van buitenvervolgingstelling een einde aan  de schorsing.

Zodra  een  administratieve  geldboete  of  een  belastingverhoging, opgelegd met toepassing van de  bepalingen van dit hoofdstuk, definitief is geworden,  vervalt de strafvordering.

---- historiek ----  ---- historique ----

- toegevoegd door art. 35 van het decreet van 17 juli  2015 (B.S., 14.08.2015 ). De tekst is in werking getreden  op 14 augustus 2015 (art. 41)

### Hoofdstuk 19 - Beroepsgeheim  Chapitre 19 - Secret professionnel

###### Art. 3.19.0.0.1.  Art. 3.19.0.0.1.

Als een met toepassing van artikel 3.13.1.2.1, eerste lid,  artikel 3.13.1.2.2, eerste tot en met derde lid, artikel  3.13.1.2.3 en artikel 3.13.1.3.1 tot en met 3.13.1.3.4  aangezochte persoon het beroepsgeheim doet gelden,  verzoekt de bevoegde entiteit van de Vlaamse  administratie om tussenkomst van de territoriaal  bevoegde tuchtoverheid om te oordelen of, en eventueel  in welke mate, de vraag om inlichtingen of de  overlegging van documenten verzoenbaar is met het  eerbiedigen van het beroepsgeheim.

Een persoon die, op welke grond ook, optreedt bij de  toepassing van de bepalingen van deze codex of die  toegang heeft tot de ambtsvertrekken van de bevoegde  entiteit van de Vlaamse administratie, is, buiten de  uitoefening van zijn ambt verplicht tot volstrekte  geheimhouding over alle zaken waarvan hij wegens de  uitvoering van zijn opdracht kennis heeft.

De personeelsleden van de bevoegde entiteit van de  Vlaamse administratie oefenen hun ambt uit als ze aan  andere administratieve diensten van de staat, daaronder  begrepen de parketten en de griffies van de hoven en van  alle rechtsmachten, en van de gemeenschappen en de  gewesten en aan de openbare instellingen of  inrichtingen, vermeld in artikel 3.13.1.4.1, inlichtingen  verstrekken die voor die diensten, instellingen of  inrichtingen nodig zijn voor de uitvoering van wettelijke  of reglementaire bepalingen die eraan zijn opgedragen.

De personeelsleden van de bevoegde entiteit van de  Vlaamse administratie oefenen hun ambt uit als ze aan  de administratieve diensten van de gemeenten en  provincies inlichtingen verstrekken met betrekking tot  de fiscale toestand van rechtspersonen die nodig zijn  voor de uitvoering van wettelijke of reglementaire  bepalingen die eraan zijn opgedragen.

De personeelsleden van de bevoegde entiteit van de  Vlaamse administratie oefenen ook hun ambt uit als ze  met betrekking tot de fiscale toestand van een  belastingplichtige een vraag om raadpleging, uitleg of  mededeling inwilligen van de echtgenoot of wettelijk  samenwonende op de goederen van wie de aanslag  wordt ingevorderd.

Les membres du personnel de l'entité compétente de  l'administration flamande exercent également leur  fonction lorsque dans le cadre de la situation fiscale d'un  contribuable ils répondent à une question de  consultation, d'explication ou de communication de  l'époux ou du cohabitant légal sur les biens duquel  l'imposition est recouvrée.  Personen die deel uitmaken van diensten waaraan de  bevoegde entiteit van de Vlaamse administratie  ingevolge het tweede en het derde lid inlichtingen van  fiscale  aard  heeft  verstrekt, zijn  tot  dezelfde  geheimhouding verplicht en mogen de verkregen  inlichtingen niet gebruiken buiten het kader van de  wettelijke bepalingen voor de uitvoering waarvan ze zijn  verstrekt.

De bepalingen van het vijfde lid zijn ook van toepassing  op de personen die behoren tot diensten waaraan  ingevolge een controle als vermeld in titel 3, hoofdstuk  13, inlichtingen van fiscale aard kunnen worden  verstrekt.

---- historiek ----  ---- historique ----

- een lid is ingevoegd tussen lid 2 en 3, door art. 2 van  het decreet van 4 apr. 2014 (B.S., 13.06.2014). Tekst  treedt in werking vanaf 23 juni 2014 (art. -);

### Hoofdstuk 20 - Te verstrekken inlichtingen  Chapitre 20 - Renseignements à fournir

---- historiek ----  ---- historique ----

- hoofdstuk 20 toegevoegd door art. 318 van het decreet  van 19 dec. 2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in  werking getreden op 1 januari 2015 (art.

325)

###### Art. 3.20.0.0.1.  Art. 3.20.0.0.1.

Het bevoegde personeelslid reikt op verzoek van de  betrokkenen in rechtstreekse naam, van hun erfgenamen  of rechthebbenden of op verzoek van derden die  voldoende belang aantonen, een afschrift of een  uittreksel van de successieaangiften uit.

---- historiek ----  ---- historique ----

- toegevoegd door art. 319 van het decreet van 19 dec.  2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in werking  getreden op 1 januari 2015 (art. 325)

### Hoofdstuk 21 - Voorafgaande attesten  Chapitre 21 - Attestations antérieures

---- historiek ----  ---- historique ----

- hoofdstuk 21 toegevoegd door art. 320 van het decreet  van 19 dec. 2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in  werking getreden op 1 januari 2015 (art.

325)

###### Art. 3.21.1.0.0.1.  Art. 3.21.1.0.0.1.

§ 1. Voor de aangifte en uiterlijk voor het verstrijken van  de aangiftetermijn, vermeld in artikel 3.3.1.0.5, § 2, en  artikel 3.3.1.0.6, kunnen de erfgenamen, algemene  legatarissen, begiftigden en al wie gehouden is tot het  indienen van een aangifte van nalatenschap een verzoek  richten tot de bevoegde entiteit van de Vlaamse  administratie tot het bekomen van een attest dat op basis  van de gegevens, aangereikt door de verzoeker, de  waardering, bedoeld in artikel 3.3.1.0.8, § 1, eerste lid,  14°, b), 8), iv), vi) en vii) bevestigt.

Het verzoek bevat de gegevens en de bescheiden,  vermeld in artikel 3.3.1.0.8, § 1, eerste lid, 14°, b).

Een attest over de waardering kan alleen worden  verkregen als het verzoek wordt ingediend binnen dertig  dagen na de datum van het verslag, vermeld in artikel  3.3.1.0.8, § 1, eerste lid, 14°, b), 8).

§ 2. De bevoegde entiteit van de Vlaamse administratie  verleent het attest, vermeld in paragraaf 1, binnen zestig  dagen nadat ze het verzoek, vermeld in paragraaf 1, heeft

Als het verzoek, vermeld in paragraaf 1, niet alle  gegevens of de bescheiden, vermeld in artikel 3.3.1.0.8,  § 1, eerste lid, 14°, b), bevat, meldt de bevoegde entiteit  van de Vlaamse administratie dat vóór de termijn,  vermeld in het eerste lid, is verstreken, met opgave van  de gegevens of de bescheiden die ontbreken. In dat geval  wordt de termijn, vermeld in het eerste lid, geschorst  vanaf de datum van verzending van die melding tot de  datum waarop de bevoegde entiteit van de Vlaamse  administratie de ontbrekende gegevens of bescheiden  heeft ontvangen.

Het attest, vermeld in paragraaf 1, is bindend voor de  bevoegde entiteit van de Vlaamse administratie en wordt  gebruikt om de erfbelasting te berekenen.

---- historiek ----  ---- historique ----

- ingevoegd door art. 13 van het decreet van 19.12.2025  (B.S. 30.12.2025). Inwerkingtreding: 01.01.2026

###### Art. 3.21.0.0.1/1  Art. 3.21.0.0.1/1  § 1. Voorafgaand aan de authentieke akte van schenking  kan de belanghebbende een verzoek richten tot de  bevoegde entiteit van de Vlaamse administratie tot het  bekomen van een attest waaruit blijkt dat op het moment  van het verzoek en op basis van de gegevens, aangereikt  door de verzoeker, al dan niet aan de voorwaarden,  vermeld in artikel 2.8.6.0.3, is voldaan en dat, in  voorkomend geval, de waardering, bedoeld in artikel  3.12.3.0.1, § 5, tweede lid, 5°, d), f) en g), bevestigt op  de referentiedatum, vermeld in artikel 3.12.3.0.1, § 5,  tweede lid, 5°, i), op basis van de gegevens, aangereikt  door de verzoeker.

In het verzoek wordt opgave gedaan van de gegevens,  vermeld in artikel 3.12.3.0.1, § 5, eerste lid, en de  bescheiden, vermeld in artikel 3.12.3.0.1, § 5, tweede  lid, worden toegevoegd.

Een voorafgaand attest over de waardering kan alleen  worden verkregen als het verzoek wordt ingediend  binnen dertig dagen na de referentiedatum, vermeld in  artikel 3.12.3.0.1, § 5, tweede lid, 5°, i).

§ 2. De bevoegde entiteit van de Vlaamse administratie  verleent het attest, vermeld in paragraaf 1, binnen zestig  dagen na de ontvangst van het verzoek.

Het attest, vermeld in paragraaf 1, is zestig dagen vanaf  de datum van de eindbeslissing geldig en bindend voor  de bevoegde autoriteit van de Vlaamse administratie.

---- historiek ----  ---- historique ----

- gewijzigd en vernummerd door art. 14 van het decreet  van 19.12.2025 (B.S. 30.12.2025). Inwerkingtreding: Van  toepassing op alle authentieke schenkingsakten die  worden verleend vanaf 1 januari 2026

- gewijzigd door art. 77 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- toegevoegd door art. 321 van het decreet van 19 dec.  2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in werking  getreden op 1 januari 2015 (art. 325)

### Hoofdstuk 22 - Voorafgaande beslissingen over de

materies en bepalingen vervat in deze codex

---- historiek ----  ---- historique ----

- toegevoegd door art. 36 van het decreet van 17 juli  2015 (B.S., 14.08.2015 ). De tekst is in werking getreden  op 14 augustus 2015 (art. 41)

###### Art. 3.22.0.0.1.  Art. 3.22.0.0.1.

§ 1. De bevoegde entiteit van de Vlaamse administratie  spreekt zich bij voorafgaande beslissing uit over alle  aanvragen die uitsluitend de toepassing van de  bepalingen van deze codex betreffen.

Onder voorafgaande beslissing wordt verstaan de  juridische handeling waarbij de bevoegde entiteit van de  Vlaamse administratie overeenkomstig de bepalingen  die van kracht zijn, vaststelt hoe de bepaling van deze  codex wordt toegepast op een bijzondere situatie of  verrichting, die op fiscaal vlak nog geen uitwerking  heeft gehad.

Une décision anticipée peut être définie comme une  opération juridique par laquelle l'entité compétente de  l'Administration flamande constate conformément aux  dispositions en vigueur comment la disposition de ce  code est appliquée à une situation ou une opération  particulière qui n'a pas encore eu d'effets au niveau  fiscal.  De voorafgaande beslissing mag geen vrijstelling of  vermindering van de belasting tot gevolg hebben.

1° de identiteit van de aanvrager en, in voorkomend  geval, die van de betrokken partijen en derden;

2° de volledige beschrijving van de bijzondere situatie  of verrichting;

3° de verwijzing naar de wettelijke of reglementaire  bepalingen waarop de beslissing moet slaan.

De aanvraag bevat, in voorkomend geval, een volledige  kopie van de aanvragen die voor hetzelfde onderwerp  zijn ingediend bij de fiscale overheden van de lidstaten  van de Europese Unie of van derde staten waarmee  België een overeenkomst tot het vermijden van dubbele  belasting heeft gesloten, en van de beslissingen over die  aanvragen.

Zolang er geen beslissing is genomen, moet de aanvraag  worden aangevuld met elk nieuw element dat betrekking  heeft op de voorgenomen situatie of verrichting.

De  aanvraag  wordt  onderzocht  door  een  besluitvormingsorgaan dat als volgt is samengesteld :

1° de leidend ambtenaar van de bevoegde entiteit van de  Vlaamse administratie, die optreedt als voorzitter;

2° het afdelingshoofd van de afdeling van de bevoegde  entiteit van de Vlaamse administratie, bevoegd voor de  taxatie van de erf- en registratiebelastingen;

3° het afdelingshoofd van de afdeling van de bevoegde  entiteit van de Vlaamse administratie, bevoegd voor de  regelgeving inzake de erf- en registratiebelastingen;

4° maximaal vier personeelsleden van de bevoegde  entiteit van de Vlaamse administratie met minstens de  graad van adviseur of directeur;

5° een personeelslid van de bevoegde entiteit van de  Vlaamse administratie, dat optreedt als secretaris.

De voorafgaande beslissing, vermeld in paragraaf 1,  eerste lid, wordt meegedeeld aan de aanvrager binnen  een termijn van drie maanden vanaf de datum van de  indiening van de aanvraag. De bevoegde entiteit van de  Vlaamse administratie en de aanvrager kunnen in  onderlinge overeenstemming deze termijn wijzigen.

Uiterlijk binnen vijftien werkdagen vanaf het ogenblik  dat de aanvraag, vermeld in paragraaf 1, eerste lid,  volledig is, licht de bevoegde entiteit van de Vlaamse  administratie de aanvrager in over de vastgestelde  antwoordtermijn.

§ 3. Een voorafgaande beslissing kan niet worden  genomen als :

1° de aanvraag betrekking heeft op situaties of  verrichtingen die op fiscaal vlak al het voorwerp  uitmaken van een administratieve bezwaarprocedure of  van een gerechtelijke handeling tussen de bevoegde  entiteit van de Vlaamse administratie en de aanvrager;

2° het nemen van een voorafgaande beslissing niet  aangewezen is of zonder uitwerking is op grond van de  wettelijke of reglementaire bepalingen, die in de  aanvraag aangevoerd zijn;

Meer bepaald kan er geen voorafgaande beslissing  worden genomen over :

a) de belastingtarieven en de berekening van de  belastingen;

b) de bedragen en de percentages;  b) les montants et les pourcentages ;

c) de aangifte, het onderzoek en de controle, het gebruik  van  bewijsmiddelen,  de  aanslagprocedure,  de  rechtsmiddelen, de rechten en voorrechten van de  Vlaamse schatkist, de termijnen, de verjaring, het  beroepsgeheim,  de  inwerkingtreding,  de  aansprakelijkheid en de plichten van sommige openbare  ambtenaren, andere personen of bepaalde instellingen;

d) de bepalingen waarvoor een specifieke procedure  inzake erkenning of beslissing is ingesteld;

g) de forfaitaire grondslagen van aanslag;  g) les bases forfaitaires de taxation ;

3° de aanvraag betrekking heeft op de toepassing van de  codex betreffende invordering en vervolgingen.

§ 4. Behoudens in de gevallen waarin het voorwerp van  de aanvraag dat rechtvaardigt, wordt de beslissing  getroffen voor een termijn die niet langer mag zijn dan  vijf jaar.

De voorafgaande beslissing bindt de bevoegde entiteit  van de Vlaamse administratie voor de toekomst, behalve  :

1° als de voorwaarden waaraan de voorafgaande  beslissing is onderworpen, niet vervuld zijn;

2° als blijkt dat de situatie of de verrichtingen door de  aanvrager onvolledig of onjuist omschreven zijn, of als  essentiële elementen van de verrichtingen niet zijn  verwezenlijkt op de wijze die de aanvrager omschreven  heeft;

3° ingeval van wijziging van bepalingen van de  verdragen, van het unierecht of van het interne recht die  van toepassing zijn op de door de voorafgaande  beslissing beoogde situatie of verrichting;

4° als blijkt dat de voorafgaande beslissing niet in  overeenstemming is met de bepalingen van de  verdragen, van het unierecht of van het interne recht;

5° als de voornaamste gevolgen van de situatie of de  verrichtingen gewijzigd zijn door toedoen van de  aanvrager. In dat geval heeft de intrekking van de  voorafgaande beslissing uitwerking vanaf de dag van de  aan de aanvrager ten laste gelegde feiten.

Elke aanvraag die ingediend is bij de fiscale overheden  van een lidstaat van de Europese Unie of een derde staat  als vermeld in paragraaf 2, tweede lid, tijdens de periode  waarin de voorafgaande beslissing wordt toegepast,  alsook elke beslissing die daarmee verband houdt,  moeten onverwijld worden meegedeeld aan de bevoegde  entiteit van de Vlaamse administratie met het oog op de  toepassing van dit artikel.

§ 5. De voorafgaande beslissingen worden op anonieme  wijze gepubliceerd op de website van de bevoegde  entiteit van de Vlaamse administratie.

- toegevoegd door art. 37 van het decreet van 17 juli  2015 (B.S., 14.08.2015 ). De tekst is in werking getreden  op 14 augustus 2015 (art. 41)

###### Art. 3.22.0.0.2.  Art. 3.22.0.0.2.

§ 1. Met betrekking tot de toepassing van de bepalingen  van deze codex, verstrekt de bevoegde entiteit van de  Vlaamse  administratie  een  bindend  advies  tot  voorafgaande beslissing  als  vermeld in artikel  3.22.0.0.1, § 1, tweede lid, aan de federale Dienst  Voorafgaande Beslissingen in fiscale zaken over alle  aanvragen inzake situaties of verrichtingen, die deels  onder haar bevoegdheid en deels onder de bevoegdheid  van de federale Dienst Voorafgaande Beslissingen in  fiscale zaken vallen.

Het bindend advies tot voorafgaande beslissing,  afgeleverd in toepassing van het eerste lid, heeft ten  aanzien van de aanvrager dezelfde waarde als de  voorafgaande beslissing, vermeld in artikel 3.22.0.0.1, §  1, tweede lid.

Het bindend advies tot voorafgaande beslissing mag  geen vrijstelling of vermindering van de belasting tot  gevolg hebben.

§ 2. De aanvraag van een voorafgaande beslissing als  vermeld in paragraaf 1 moet schriftelijk gericht worden  aan hetzij de bevoegde entiteit van de Vlaamse  administratie, hetzij de Federale Overheidsdienst  Financiën overeenkomstig artikel 21 van de wet van 24  december  2002  tot  wijziging  van  de  vennootschapsregeling inzake inkomstenbelastingen en  tot instelling van een systeem van voorafgaande  beslissingen in fiscale zaken.

Het bindend advies, vermeld in paragraaf 1, eerste lid,  wordt verstrekt door het besluitvormingsorgaan,  vermeld in artikel 3.22.0.0.1, § 2, vierde lid, en op de  wijze vermeld in dat lid.

§ 3. De bepalingen van artikel 3.22.0.0.1, § 3 tot en met  § 5, zijn van overeenkomstige toepassing op dit artikel.

---- historiek ----  ---- historique ----

- toegevoegd door art. 37 van het decreet van 17 juli  2015 (B.S., 14.08.2015 ). De tekst is in werking getreden  op 15 september 2015 ( (besluit van de Vlaamse Regering  van 18 september 2015 - B.S., 12.10.2015 - art. 2))

#### Afdeling 1 - Bepalingen die aan alle  gegevensverwerkingen gemeenschappelijk zijn

###### Art. 3.23.1.0.1.  Art. 3.23.1.0.1.

De bevoegde entiteit van de Vlaamse administratie kan  persoonsgegevens verwerken als dat noodzakelijk is  voor de vervulling van een taak van algemeen belang,  namelijk om de juiste heffing en inning van alle  belastingen, vermeld in deze codex, te kunnen  verzekeren.

De bevoegde entiteit van de Vlaamse administratie is  verwerkingsverantwoordelijke als vermeld in artikel 4,  7), van verordening (EU) 2016/679 van het Europees  Parlement en de Raad van 27 april 2016 betreffende de  bescherming van natuurlijke personen in verband met de  verwerking van persoonsgegevens en betreffende het  vrije verkeer van die gegevens en tot intrekking van  Richtlijn  95/46/EG  (algemene  verordening  gegevensbescherming), voor de verwerking van de  persoonsgegevens, vermeld in het eerste lid.

---- historiek ----  ---- historique ----

- Ingevoegd door art. 8 van het decreet van 19.04.2024  (B.S., 03.06.2024). Inwerkingtreding: 13.06.2024

###### Art. 3.23.1.0.2.  Art. 3.23.1.0.2.

De volgende categorieën van persoonsgegevens worden  in het kader van de toepassing van artikel 3.23.1.0.1,  eerste lid, van deze codex, verwerkt:

1° het rijksregisternummer of het identificatienummer,  vermeld in artikel 8 van de wet van 15 januari 1990  houdende  oprichting  en  organisatie  van  een  Kruispuntbank van de Sociale Zekerheid;

2° het ondernemingsnummer dat bekend is bij de  Kruispuntbank van Ondernemingen;

3° het fiscaal identificatienummer;  3° le numéro d'identification fiscale ;

4° de persoonlijke identificatiegegevens, namelijk de  naam, het adres, het telefoonnummer en het e-mailadres;

5° de persoonlijke kenmerken, namelijk de leeftijd, de  geboortedatum, de geboorteplaats, de burgerlijke staat  en de nationaliteit;

6° de financiële bijzonderheden.  6° les particularités financières.

---- historiek ----  ---- historique ----

- Ingevoegd door art. 9 van het decreet van 19.04.2024  (B.S., 03.06.2024). Inwerkingtreding: 13.06.2024

###### Art. 3.23.1.0.3.  Art. 3.23.1.0.3.

De persoonsgegevens van de volgende categorieën van  betrokkenen kunnen in het kader van de toepassing van

1° de belastingplichtige;  1° le contribuable ;

2° de belastingschuldige;  2° le redevable ;

3° de vertegenwoordigers van de personen, vermeld in  punt 1° en 2° ;

4° de natuurlijke personen, vermeld in artikel 3.13.1.3.1  tot en met 3.13.1.3.6, waartoe de bevoegde entiteit van  de Vlaamse administratie zich kan richten in het kader  van de uitoefening van haar onderzoeksbevoegdheden.

De  persoonsgegevens  van  de  categorieën  van  betrokkenen, vermeld in het eerste lid, worden alleen  verwerkt als dat noodzakelijk is voor het concrete doel  van de gegevensverwerking.

---- historiek ----  ---- historique ----

- Ingevoegd door art. 10 van het decreet van 19.04.2024  (B.S., 03.06.2024). Inwerkingtreding: 13.06.2024

###### Art. 3.23.1.0.4.  Art. 3.23.1.0.4.

§ 1. Met behoud van de toepassing van paragraaf 2  kunnen in het kader van de toepassing van artikel  3.23.1.0.1, eerste lid, de persoonsgegevens, vermeld in  artikel 3.23.1.0.2, uitgewisseld worden met de volgende  categorieën van ontvangers:

1° de advocaten die in opdracht van de bevoegde entiteit  van de Vlaamse administratie het Vlaamse Gewest  vertegenwoordigen in geschillen over de toepassing van  deze codex;

2° de gerechtsdeurwaarders die in opdracht van de  bevoegde entiteit van de Vlaamse administratie de  belastingen, vermeld in deze codex, invorderen;

3° de erkende woonmaatschappijen, vermeld in artikel  4.36 van de Vlaamse Codex Wonen van 2021, die  namens de huurders de vermindering, vermeld in artikel  2.1.5.0.1, § 1, 2° en 3°, § 1/1, en artikel 2.1.5.0.2, § 1,  2°, aanvragen;

4° de derden, vermeld in titel 3, hoofdstuk 12, die  verplicht zijn informatie te verstrekken aan de bevoegde  eniteit van de Vlaamse administratie;

5° de derden, vermeld in artikel 3.13.1.3.1 tot en met  3.13.1.3.7, en de openbare instellingen en inrichtingen,  vermeld in artikel 3.13.1.4.1 en 3.13.1.4.2, tot wie de  bevoegde entiteit van de Vlaamse administratie zich  mag richten in het kader van haar onderzoeks- en  controlebevoegdheden;

6° de administratieve diensten en de openbare  instellingen of inrichtingen, vermeld in 3.19.0.0.2;

7° de derden met een voldoende belang, vermeld in  artikel 3.20.0.0.1, die verzoeken om een afschrift of een  uittreksel van een successieaangifte.

§ 2. Als de bevoegde entiteit van de Vlaamse  § 2. Lorsque l'entité compétente de l'administration

De derden, vermeld in het eerste lid, kunnen alleen over  de beoogde persoonsgegevens beschikken gedurende de  tijd die nodig is voor de uitvoering van de handelingen,  vermeld  in  het  eerste  lid,  en  kunnen  die  persoonsgegevens uitsluitend voor dat doel gebruiken.

---- historiek ----  ---- historique ----

- Ingevoegd door art. 11 van het decreet van 19.04.2024  (B.S., 03.06.2024). Inwerkingtreding: 13.06.2024

#### Afdeling 2 - Gegevensverwerking voor de onroerende

voorheffing, heffing ongeschikte en onbewoonbare

woningen en leegstandsheffing bedrijfsruimten

###### Art. 3.23.2.0.1.  Art. 3.23.2.0.1.

Met behoud van de toepassing van afdeling 1 zijn de  bepalingen van deze afdeling van toepassing op de  gegevensverwerking die noodzakelijk is voor de juiste  heffing en inning van de belastingen, vermeld in titel 2,  hoofdstuk 1, 5 en 6.

---- historiek ----  ---- historique ----

- Ingevoegd door art. 13 van het decreet van 19.04.2024  (B.S., 03.06.2024). Inwerkingtreding: 13.06.2024

###### Art. 3.23.2.0.2.  Art. 3.23.2.0.2.

In het kader van de gegevensverwerking, vermeld in  artikel 3.23.2.0.1, kunnen naast de categorieën van  persoonsgegevens, vermeld in artikel 3.23.1.0.2, de  volgende specifieke categorieën van persoonsgegevens  worden verwerkt:

1° beeldopnamen, namelijk plannen, plattegronden en  foto's van onroerende goederen;

2° de gebouw- of woningkenmerken;  2° les caractéristiques du bâtiment ou du logement ;

3° de gegevens over de samenstelling van het gezin;  3° les données relatives à la composition du ménage ;

4° de gegevens over de gezondheid die noodzakelijk zijn  voor de toekenning van de vermindering, vermeld in  artikel 2.1.5.0.1, § 1, 2° en 3°, en artikel 2.1.5.0.2, § 1,  2°.

---- historiek ----  ---- historique ----

- Ingevoegd door art. 14 van het decreet van 19.04.2024  (B.S., 03.06.2024). Inwerkingtreding: 13.06.2024

###### Art. 3.23.2.0.3.  Art. 3.23.2.0.3.

In het kader van de gegevenswerking, vermeld in artikel  3.23.2.0.1, kunnen naast de persoonsgegevens van de  categorieën van betrokkenen, vermeld in artikel

1° het gehandicapt kind, vermeld in artikel 2.1.5.0.1, §  1, 2° ;

2° de persoon met een handicap, vermeld in artikel  2.1.5.0.1, § 1, 3° ;

3° de oorlogsverminkte, vermeld in artikel 2.1.5.0.2, §  1, 2° ;

4° de huurder die van de verminderingen, vermeld in  artikel 2.1.5.0.4, kan genieten.

De  persoonsgegevens  van  de  categorieën  van  betrokkenen, vermeld in het eerste lid, worden alleen  verwerkt als dat noodzakelijk is voor het concrete doel  van de gegevensverwerking.

---- historiek ----  ---- historique ----

- Ingevoegd door art. 15 van het decreet van 19.04.2024  (B.S., 03.06.2024). Inwerkingtreding: 13.06.2024

###### Art. 3.23.2.0.4.  Art. 3.23.2.0.4.

Met behoud van de toepassing van de noodzakelijke  bewaring ervan voor de latere verwerking met het oog  op archivering in het algemeen belang, wetenschappelijk  of historisch onderzoek of statistische doeleinden,  vermeld in artikel 89 van verordening (EU) 2016/679  van het Europees Parlement en de Raad van 27 april  2016 betreffende de bescherming van natuurlijke  personen  in  verband met  de  verwerking  van  persoonsgegevens en betreffende het vrije verkeer van  die gegevens en tot intrekking van Richtlijn 95/46/EG  (algemene verordening gegevensbescherming), worden  de persoonsgegevens, vermeld in artikel 3.23.2.0.2,  bewaard gedurende tien jaar na de betaling of de  verjaring van de belastingen, vermeld in artikel  3.23.2.0.1, of, in voorkomend geval, tien jaar na de  definitieve  beëindiging  van  de  administratieve  procedure en de integrale betaling van alle bedragen die  daaraan verbonden zijn.

---- historiek ----  ---- historique ----

- Ingevoegd door art. 16 van het decreet van 19.04.2024  (B.S., 03.06.2024). Inwerkingtreding: 13.06.2024

#### Afdeling 3 - Gegevensverwerking voor de  verkeersbelasting, de belasting op inverkeerstelling, de

kilometerheffing en het eurovignet

###### Art. 3.23.3.0.1.  Art. 3.23.3.0.1.

Met behoud van de toepassing van afdeling 1 zijn de  bepalingen van deze afdeling van toepassing op de  gegevensverwerking die noodzakelijk is voor de juiste  inning en heffing van de belastingen, vermeld in titel 2,  hoofdstuk 2, 3 en 4, en het eurovignet.

- Ingevoegd door art. 18 van het decreet van 19.04.2024  (B.S., 03.06.2024). Inwerkingtreding: 13.06.2024

###### Art. 3.23.3.0.2.  Art. 3.23.3.0.2.

In het kader van de gegevensverwerking, vermeld in  artikel 3.23.3.0.1, kunnen naast de categorieën van  persoonsgegevens, vermeld in artikel 3.23.1.0.2, de  volgende specifieke categorieën van persoonsgegevens  worden verwerkt:

1° de voertuig-, boot- of luchtvaartuigkenmerken;  1° les caractéristiques du véhicule, du navire ou de  l'aéronef ;

2° de gegevens over de samenstelling van het gezin;  2° les données relatives à la composition du ménage ;

3° de gegevens over de gezondheid die noodzakelijk zijn  voor de toekenning van de vrijstelling, vermeld in artikel  2.2.6.0.1, § 1, eerste lid, 4°, en artikel 2.3.6.0.1, § 1,  eerste lid, 3°.

Met behoud van de toepassing van het eerste lid worden  met behulp van de camera's, vermeld in artikel  3.13.2.0.2, 4°, voor de belastingen, vermeld in titel 2,  hoofdstuk 2, 3 en 4, de volgende persoonsgegevens  verwerkt:

1° een beeldopname van de nummerplaat aan de  voorkant van het voertuig en, in voorkomend geval, aan  de achterkant van het voertuig;

2° een beeldopname van het voertuig;  2° l'enregistrement visuel du véhicule ;

3° de datum, het tijdstip en de plaats van de  beeldopname;

4° de voertuigkenmerken.  4° les caractéristiques du véhicule.

---- historiek ----  ---- historique ----

- Ingevoegd door art. 19 van het decreet van 19.04.2024  (B.S., 03.06.2024). Inwerkingtreding: 13.06.2024

###### Art. 3.23.3.0.3.  Art. 3.23.3.0.3.

In het kader van de gegevensverwerking, vermeld in  artikel 3.23.3.0.1, kunnen naast de persoonsgegevens  van de categorieën van betrokkenen, vermeld in artikel  3.23.1.0.3, de persoonsgegevens van de persoon met een  handicap en de grootoorlogsinvalide, vermeld in artikel  2.2.6.0.1 en 2.3.6.0.1, worden verwerkt.

De persoonsgegevens van de betrokkenen, vermeld in  het eerste lid, worden alleen verwerkt als dat  noodzakelijk is voor het concrete doel van de  gegevensverwerking.

---- historiek ----  ---- historique ----

- Ingevoegd door art. 20 van het decreet van 19.04.2024  (B.S., 03.06.2024). Inwerkingtreding: 13.06.2024

Met behoud van de toepassing van de noodzakelijke  bewaring ervan voor de latere verwerking met het oog  op archivering in het algemeen belang, wetenschappelijk  of historisch onderzoek of statistische doeleinden,  vermeld in artikel 89 van verordening (EU) 2016/679  van het Europees Parlement en de Raad van 27 april  2016 betreffende de bescherming van natuurlijke  personen  in  verband met  de  verwerking  van  persoonsgegevens en betreffende het vrije verkeer van  die gegevens en tot intrekking van Richtlijn 95/46/EG  (algemene verordening gegevensbescherming), worden  de persoonsgegevens, vermeld in artikel 3.23.3.0.2,  bewaard gedurende tien jaar na de betaling of de  verjaring van de belastingen, vermeld in artikel  3.23.3.0.1, of, in voorkomend geval, tien jaar na de  definitieve  beëindiging  van  de  administratieve  procedure en de integrale betaling van alle bedragen die  daaraan verbonden zijn.

In  afwijking  van  het  eerste  lid  worden  de  persoonsgegevens, vermeld in artikel 3.23.3.0.2, tweede  lid, die aanleiding geven tot een vaststelling op de  openbare weg als vermeld in artikel 3.13.2.0.4, § 1,  negentig dagen na die vaststelling bewaard.

---- historiek ----  ---- historique ----

- Ingevoegd door art. 21 van het decreet van 19.04.2024  (B.S., 03.06.2024). Inwerkingtreding: 13.06.2024

#### Afdeling 4 - Gegevensverwerking voor de erfbelasting  Section 4 - Traitement de données aux fins des droits de

###### Art. 3.23.4.0.1.  Art. 3.23.4.0.1.

Met behoud van de toepassing van afdeling 1 zijn de  bepalingen van deze afdeling van toepassing op de  gegevensverwerking die noodzakelijk is voor de juiste  heffing en inning van de belastingen, vermeld in titel 2,  hoofdstuk 7.

---- historiek ----  ---- historique ----

- Ingevoegd door art. 23 van het decreet van 19.04.2024  (B.S., 03.06.2024). Inwerkingtreding: 13.06.2024

###### Art. 3.23.4.0.2.  Art. 3.23.4.0.2.

In het kader van de gegevensverwerking, vermeld in  artikel 3.23.4.0.1, kunnen naast de categorieën van  persoonsgegevens, vermeld in artikel 3.23.1.0.2, de  volgende specifieke categorieën van persoonsgegevens  worden verwerkt:

1° beeldopnamen, namelijk plannen, plattegronden en  foto's van onroerende goederen;

2° de gebouw- of woningkenmerken;  2° les caractéristiques du bâtiment ou du logement ;

3° de gegevens over de samenstelling van het gezin;  3° les données relatives à la composition du ménage ;

5° gerechtelijke gegevens met betrekking tot de  onwaardigheid om tot een nalatenschap te komen,  vermeld in artikel 4.6 van het Burgerlijk Wetboek.

---- historiek ----  ---- historique ----

- Ingevoegd door art. 24 van het decreet van 19.04.2024  (B.S., 03.06.2024). Inwerkingtreding: 13.06.2024

###### Art. 3.23.4.0.3.  Art. 3.23.4.0.3.

In het kader van de gegevenswerking, vermeld in artikel  3.23.4.0.1, kunnen naast de persoonsgegevens van de  categorieën van betrokkenen, vermeld in artikel  3.23.1.0.3, de persoonsgegevens van de volgende  categorieën van betrokkenen worden verwerkt:

1° de partner van de erflater;  1° le partenaire du testateur ;

2° de persoon die de nalatenschap verwerpt;  2° la personne qui renonce à la succession ;

3° de schuldeiser van de erflater;  3° le créancier du testateur ;

4° de begunstigde van een schenking;  4° le bénéficiaire d'une donation ;

5° de begunstigde van een vruchtgebruik;  5° le bénéficiaire d'un usufruit ;

6° de begunstigde van een fideï-commis de residuo.  6° le bénéficiaire d'un fidéicommis de residuo.

De  persoonsgegevens  van  de  categorieën  van  betrokkenen, vermeld in het eerste lid, worden alleen  verwerkt als dat noodzakelijk is voor het concrete doel  van de gegevensverwerking.

---- historiek ----  ---- historique ----

- Ingevoegd door art. 25 van het decreet van 19.04.2024  (B.S., 03.06.2024). Inwerkingtreding: 13.06.2024

###### Art. 3.23.4.0.4.  Art. 3.23.4.0.4.

Met behoud van de toepassing van de noodzakelijke  bewaring ervan voor de latere verwerking met het oog  op archivering in het algemeen belang, wetenschappelijk  of historisch onderzoek of statistische doeleinden,  vermeld in artikel 89 van verordening (EU) 2016/679  van het Europees Parlement en de Raad van 27 april  2016 betreffende de bescherming van natuurlijke  personen  in  verband met  de  verwerking  van  persoonsgegevens en betreffende het vrije verkeer van  die gegevens en tot intrekking van Richtlijn 95/46/EG  (algemene verordening gegevensbescherming), worden  de persoonsgegevens, vermeld in artikel 3.23.4.0.2,  bewaard gedurende dertig jaar na de betaling of de  verjaring van de belastingen, vermeld in artikel  3.23.4.0.1, of, in voorkomend geval, dertig jaar na de  definitieve  beëindiging  van  de  administratieve  procedure en de integrale betaling van alle bedragen die  daaraan verbonden zijn.

- Ingevoegd door art. 26 van het decreet van 19.04.2024  (B.S., 03.06.2024). Inwerkingtreding: 13.06.2024

#### Afdeling 5 - Gegevensverwerking voor de

registratiebelasting

###### Art. 3.23.5.0.1.  Art. 3.23.5.0.1.

Met behoud van de toepassing van afdeling 1 zijn de  bepalingen van deze afdeling van toepassing op de  gegevensverwerking die noodzakelijk is voor de juiste  heffing en inning van de belastingen, vermeld in titel 2,  hoofdstuk 8, 9, 10 en 11.

---- historiek ----  ---- historique ----

- Ingevoegd door art. 28 van het decreet van 19.04.2024  (B.S., 03.06.2024). Inwerkingtreding: 13.06.2024

###### Art. 3.23.5.0.2.  Art. 3.23.5.0.2.

In het kader van de gegevensverwerking, vermeld in  artikel 3.23.5.0.1, kunnen naast de categorieën van  persoonsgegevens, vermeld in artikel 3.23.1.0.2, de  volgende specifieke categorieën van persoonsgegevens  worden verwerkt:

1° beeldopnamen, namelijk plannen, plattegronden en  foto's van onroerende goederen;

2° de gebouw- en woningkenmerken;  2° les caractéristiques du bâtiment et du logement ;

3° de gegevens over de samenstelling van het gezin;  3° les données relatives à la composition du ménage ;

4° de gegevens over de gezondheid die noodzakelijk zijn  voor de toekenning van het abattement, vermeld in  artikel 2.8.3.0.4.

---- historiek ----  ---- historique ----

- Ingevoegd door art. 29 van het decreet van 19.04.2024  (B.S., 03.06.2024). Inwerkingtreding: 13.06.2024

###### Art. 3.23.5.0.3.  Art. 3.23.5.0.3.

Met behoud van de toepassing van de noodzakelijke  bewaring ervan voor de latere verwerking met het oog  op archivering in het algemeen belang, wetenschappelijk  of historisch onderzoek of statistische doeleinden,  vermeld in artikel 89 van verordening (EU) 2016/679  van het Europees Parlement en de Raad van 27 april  2016 betreffende de bescherming van natuurlijke  personen  in  verband met  de  verwerking  van  persoonsgegevens en betreffende het vrije verkeer van  die gegevens en tot intrekking van Richtlijn 95/46/EG  (algemene verordening gegevensbescherming), worden  de persoonsgegevens, vermeld in artikel 3.23.5.0.2,  bewaard gedurende dertig jaar na de betaling of de  verjaring van de belastingen, vermeld in artikel  3.23.5.0.1, of, in voorkomend geval, dertig jaar na de  definitieve  beëindiging  van  de  administratieve  procedure en de integrale betaling van alle bedragen die  daaraan verbonden zijn.

- Ingevoegd door art. 30 van het decreet van 19.04.2024  (B.S., 03.06.2024). Inwerkingtreding: 13.06.2024

#### Afdeling 6 - Gegevensverwerking voor de belasting op de

spelen en weddenschappen en de belasting op de

automatische ontspanningstoestellen

###### Art. 3.23.6.0.1.  Art. 3.23.6.0.1.

Behoudens de toepassing van afdeling 1 zijn de  bepalingen van deze afdeling van toepassing op de  gegevensverwerking die noodzakelijk is voor de juiste  heffing en inning van de belastingen, vermeld in titel 2,  hoofdstuk 12 en 13.

---- historiek ----  ---- historique ----

- Ingevoegd door art. 32 van het decreet van 19.04.2024  (B.S., 03.06.2024). Inwerkingtreding: 13.06.2024

###### Art. 3.23.6.0.2.  Art. 3.23.6.0.2.

In het kader van de gegevensverwerking, vermeld in  artikel 3.23.6.0.1, kunnen naast de categorieën van  persoonsgegevens, vermeld in artikel 3.23.1.0.2,  beeldopnamen  van  de  automatische  ontspanningstoestellen, de toestellen voor de aanneming  van  weddenschappen,  de  kansspelen  en  de  vergunningen, toegekend door de Kansspelcommissie,  worden verwerkt.

---- historiek ----  ---- historique ----

- Ingevoegd door art. 33 van het decreet van 19.04.2024  (B.S., 03.06.2024). Inwerkingtreding: 13.06.2024

###### Art. 3.23.6.0.3.  Art. 3.23.6.0.3.

Met behoud van de toepassing van de noodzakelijke  bewaring ervan voor de latere verwerking met het oog  op archivering in het algemeen belang, wetenschappelijk  of historisch onderzoek of statistische doeleinden,  vermeld in artikel 89 van verordening (EU) 2016/679  van het Europees Parlement en de Raad van 27 april  2016 betreffende de bescherming van natuurlijke  personen  in  verband met  de  verwerking  van  persoonsgegevens en betreffende het vrije verkeer van  die gegevens en tot intrekking van Richtlijn 95/46/EG  (algemene verordening gegevensbescherming), worden  de persoonsgegevens, vermeld in artikel 3.23.6.0.2,  bewaard gedurende tien jaar na de betaling of de  verjaring van de belastingen, vermeld in artikel  3.23.6.0.1, of, in voorkomend geval, tien jaar na de  definitieve  beëindiging  van  de  administratieve  procedure en de integrale betaling van alle bedragen die  daaraan verbonden zijn.

---- historiek ----  ---- historique ----

- Ingevoegd door art. 34 van het decreet van 19.04.2024  (B.S., 03.06.2024). Inwerkingtreding: 13.06.2024

### Hoofdstuk 1 - Wijzigingen van het wetboek van 23

november 1965 van de met inkomstenbelastingen

gelijkgestelde belastingen

###### Art. 4.1.0.0.1.  Art. 4.1.0.0.1.

###### Art. 95. van het wetboek van 23 november 1965 van

de met inkomstenbelastingen gelijkgestelde belastingen,  ingevoegd bij de wet van 1 juni 1992 en het laatst  gewijzigd bij het decreet van 23 december 2010, wordt  vervangen door wat volgt:

"Art. 95. Artikel 35 is van toepassing op de belasting op  de inverkeerstelling.".

### Hoofdstuk 2 - Wijzigingen van het decreet van 22  december 1995 houdende bepalingen tot begeleiding

van de begroting 1996

###### Art. 4.2.0.0.1.  Art. 4.2.0.0.1.

Aan artikel 24 van het decreet van 22 december 1995  houdende bepalingen tot begeleiding van de begroting  1996, gewijzigd bij de decreten van 8 juli 1997, 7 juli  1998, 24 maart 2006 en 29 april 2011, worden 9° en 10°  toegevoegd, die luiden als volgt:

"9° inventaris: de inventaris, vermeld in artikel 28;  10° houder van een zakelijk recht: de persoon, vermeld  in artikel 2.5.2.0.1 van de Vlaamse Codex Fiscaliteit van  13 december 2013.".

###### Art. 4.2.0.0.2.  Art. 4.2.0.0.2.

In hoofdstuk VIII, afdeling 2, van hetzelfde decreet, het  laatst gewijzigd bij het decreet van 9 november 2012,  wordt onderafdeling 1, die bestaat uit artikel 25 en 26,  opgeheven.

###### Art. 4.2.0.0.3.  Art. 4.2.0.0.3.

In artikel 27 van hetzelfde decreet, gewijzigd bij de  decreten van 7 mei 2004, 24 december 2004, 23  december 2005, 24 maart 2006, 16 juni 2006 en 27 maart  2009, worden de volgende wijzigingen aangebracht:

1° in paragraaf 2 worden de zinnen "Behoort één van die  zakelijke rechten in onverdeeldheid toe aan meer dan  één persoon dan geldt de onverdeeldheid als  belastingplichtige. De leden van de onverdeeldheid zijn  hoofdelijk gehouden tot betaling van de verschuldigde  heffing." opgeheven;

2° paragraaf 3 wordt vervangen door wat volgt:  2° le paragraphe 3 est remplacé par ce qui suit :

###### Art. 4.2.0.0.4.  Art. 4.2.0.0.4.

In artikel 35 van hetzelfde decreet, gewijzigd bij de  decreten van 8 juli 1997, 7 mei 2004, 24 december 2004,  24 maart 2006, 27 maart 2009 en 29 april 2011, wordt  de zinsnede "artikel 39, § 2," telkens vervangen door de  zinsnede "titel 3, hoofdstuk 5, van de Vlaamse Codex  Fiscaliteit van 13 december 2013,".

Dans l'article du même décret, modifié par les décrets  des 8 juillet 1997, 7 mai 2004, 24 décembre 2004, 24  mars 2006, 27 mars 2009 et 29 avril 2011, la partie de  phrase « l'article 39, § 2, » est chaque fois remplacée par  la partie de phrase « titre 3, chapitre 5, du Code flamand  de la Fiscalité du 13 décembre 2013. ».

###### Art. 4.2.0.0.5.  Art. 4.2.0.0.5.

In hoofdstuk VIII, afdeling 2, van hetzelfde decreet, het  laatst gewijzigd bij het decreet van 9 november 2012,  wordt onderafdeling 4, die bestaat uit artikel 36 en 37,  opgeheven.

Dans le chapitre VIII, section 2, du même décret,  modifié en dernier lieu par le décret du 9 novembre  2012, la sous-section 4, comprenant les articles 36 et 37,  est abrogée.

###### Art. 4.2.0.0.6.  Art. 4.2.0.0.6.

###### Art. 38. van hetzelfde decreet, gewijzigd bij de

decreten van 24 december 2004 en 24 maart 2006, wordt  opgeheven.

L'article 38 du même décret, modifié par les décrets des  24 décembre 2004 et 24 mars 2006, est abrogé.

###### Art. 4.2.0.0.7.  Art. 4.2.0.0.7.

###### Art. 39. van hetzelfde decreet, gewijzigd bij de

decreten van 8 juli 1996, 7 juli 1998, 30 juni 2000, 7 mei  2004, 24 december 2004, 24 juni 2005, 21 november  2008, 18 december 2009, 29 april 2011 en 8 juli 2011,  wordt opgeheven.

L'article 39 du même décret, modifié par les décrets des  8 juillet 1996, 7 juillet 1998, 30 juin 2000, 7 mai 2004,  24 décembre 2004, 24 juin 2005, 21 novembre 2008, 18  décembre 2009, 29 avril 2011 et 8 juillet 2011, est  abrogé.

###### Art. 4.2.0.0.8.  Art. 4.2.0.0.8.

In artikel 40 van hetzelfde decreet worden paragraaf 1  tot en met 3 en paragraaf 5 en 6 opgeheven.

A l'article 40 du même décret les paragraphes 1er à 3  inclus et les paragraphes 5 et 6 sont abrogés.

###### Art. 4.2.0.0.10.  Art. 4.2.0.0.10.

In hoofdstuk VIII, afdeling 2, van hetzelfde decreet, het  laatst gewijzigd bij het decreet van 9 november 2012,  worden onderafdeling 6, die bestaat uit artikel 41 tot en  met 42bis, onderafdeling 7, die bestaat uit artikel 43 tot  en met 44, en onderafdeling 8, die bestaat uit artikel 44,  opgeheven.

### Hoofdstuk 3 - Wijzigingen van het decreet van 19 april

1995 houdende maatregelen ter bestrijding en  voorkoming van leegstand en verwaarlozing van

bedrijfsruimten

###### Art. 4.3.0.0.1.  Art. 4.3.0.0.1.

In artikel 2 van het decreet van 19 april 1995 houdende  maatregelen ter bestrijding en voorkoming van  leegstand en verwaarlozing van bedrijfsruimten,  gewijzigd bij de decreten van 19 december 2003, 10  maart 2006, 23 juni 2006 en 11 mei 2012, worden 13°,  14° en 16° opgeheven.

###### Art. 4.3.0.0.2.  Art. 4.3.0.0.2.

###### Art. 15. van hetzelfde decreet, vervangen bij het

decreet van 23 juni 2006, wordt opgeheven.

###### Art. 4.3.0.0.3.  Art. 4.3.0.0.3.

###### Art. 16. van hetzelfde decreet, gewijzigd bij de

decreten van 6 juli 2001 en 23 juni 2006, wordt  opgeheven.

###### Art. 4.3.0.0.4.  Art. 4.3.0.0.4.

In artikel 17 van hetzelfde decreet, gewijzigd bij de  decreten van 20 december 1996, 8 juli 1997, 5 juli 2002,  27 juni 2003, 10 maart 2006, 21 november 2008 en 27  maart  2009,  worden  de  volgende  wijzigingen  aangebracht:

1° in paragraaf 1 wordt de zinsnede "artikel 45 van de  gecoördineerde wetten op de rijkscomptabiliteit"  vervangen door de zinsnede "artikel 12 van het decreet  van 8 juli 2011 houdende regeling van de begroting, de  boekhouding, de toekenning van subsidies en de  controle op de aanwending ervan, en de controle door  het Rekenhof";

3° in paragraaf 3, 2°, wordt de zinsnede "zoals ingevoerd  bij dit decreet" vervangen door de zinsnede "vermeld in  titel 2, hoofdstuk 6, van de Vlaamse Codex Fiscaliteit  van 13 december 2013";

4° in paragraaf 3, 4°, wordt de zinsnede "Hoofdstuk  VIII, Afdeling 2, van het decreet van 22 december 1995  houdende bepalingen tot begeleiding van de begroting  1996, zoals later gewijzigd" vervangen door de zinsnede  "titel 2, hoofdstuk 5, van de Vlaamse Codex Fiscaliteit  van 13 december 2013".

###### Art. 4.3.0.0.5.  Art. 4.3.0.0.5.

###### Art. 19

van hetzelfde decreet wordt opgeheven. L'article 19 du même décret est abrogé.

###### Art. 4.3.0.0.6.  Art. 4.3.0.0.6.

###### Art. 20. tot en met 23 van hetzelfde decreet, gewijzigd

bij het decreet van 10 maart 2006, worden opgeheven.

###### Art. 4.3.0.0.7.  Art. 4.3.0.0.7.

In hoofdstuk III van hetzelfde decreet, het laatst  gewijzigd bij het decreet van 22 juni 2012, worden  afdeling 2, die bestaat uit artikel 24 tot en met 33, en  afdeling 3, die bestaat uit artikel 34 tot en met 41,  opgeheven.

### Hoofdstuk 4 - Wijzigingen van de Vlaamse Codex

Ruimtelijke Ordening van 15 mei 2009

###### Art. 4.4.0.0.1.  Art. 4.4.0.0.1.

In artikel 2.6.17 van de Vlaamse Codex Ruimtelijke  Ordening van 15 mei 2009, wordt in paragraaf 1 de  zinsnede  "artikel  45  van  de  wetten  op  de  rijkscomptabiliteit, gecoördineerd bij het koninklijk  besluit van 17 juli 1991" vervangen door de zinsnede  "artikel 12 van het decreet van 8 juli 2011 houdende  regeling van de begroting, de boekhouding, de  toekenning van subsidies en de controle op de  aanwending ervan, en de controle door het Rekenhof".

###### Art. 4.4.0.0.2.  Art. 4.4.0.0.2.

In titel II, hoofdstuk VI, afdeling 2, onderafdeling 7 van  dezelfde codex wordt sectie 1, dat bestaat uit artikel  2.6.18, vervangen door wat volgt:

###### Art. 2.6.18. Onverminderd de bepalingen van of

krachtens deze afdeling, zijn de bepalingen van titel 3  van de Vlaamse Codex Fiscaliteit van 13 december 2013  van toepassing op de planbatenheffing.".

### Hoofdstuk 5 - Wijzigingen van andere decreten  Chapitre 5 - Modifications d'autres décrets

###### Art. 4.5.0.0.1.  Art. 4.5.0.0.1.

In artikel 31 van het decreet van 5 juli 2013 tot wijziging  van diverse bepalingen van het decreet van 19 april 1995  houdende maatregelen ter bestrijding en voorkoming  van leegstand en verwaarlozing van bedrijfsruimten  wordt de zinsnede "artikel 36, § 1, van het voormelde  decreet" vervangen door de zinsnede "artikel 2.6.7.4.1,  eerste lid, van de Vlaamse Codex Fiscaliteit van 13  december 2013.".

### Hoofdstuk 6 - Kruisverwijzingen  Chapitre 6 - Références mutuelles

###### Art. 4.6.0.0.1.  Art. 4.6.0.0.1.

Kruisverwijzingen naar bepalingen, opgeheven naar  aanleiding van deze codificatie, moeten worden gelezen  overeenkomstig de concordantietabel 1 uit bijlage 1, die  integraal deel uitmaakt van deze codex.

###### Art. 4.6.0.0.2.  Art. 4.6.0.0.2.

De Vlaamse Regering wordt ertoe gemachtigd om  verwijzingen in andere decreten naar bepalingen die in  deze codex zijn onder gebracht waar nodig aan te passen.

## TITEL 5 - Opheffingsbepalingen en

##### overgangsmaatregelen

###### Art. 5.0.0.0.1.  Art. 5.0.0.0.1.

De volgende regelingen worden opgeheven :  Les règlements suivants sont abrogés :

1° het WIB 92, zoals van toepassing op de onroerende  voorheffing wat betreft het Vlaamse Gewest, het laatst  gewijzigd bij het decreet van 21 juni 2013, met  uitzondering van artikel 249, artikel 464/1 en titel IX,  met behoud van de toepassing van artikel 5.0.0.0.6;

2°/1 het wetboek van 23 november 1965 van de met  Inkomstenbelastingen Gelijkgestelde Belastingen, zoals  van toepassing op de belasting op de spelen en

2°/1 le Code du 23 novembre 1965 des taxes assimilées  aux impôts sur les revenus, tel qu’il s’applique sur la  taxe sur les jeux et paris et sur la taxe sur les appareils

3° de wet van 27 december 1994 tot goedkeuring van het  Verdrag inzake de heffing van rechten voor het gebruik  van bepaalde wegen door zware vrachtwagens,  ondertekend in Brussel op 9 februari 1994 door de  Regeringen van het Koninkrijk België, het Koninkrijk  Denemarken,  de  Bondsrepubliek  Duitsland,  het  Groothertogdom Luxemburg en het Koninkrijk der  Nederlanden, en tot invoering van een Eurovignet  overeenkomstig richtlijn 93/89/EEG van de Raad van de  Europese Gemeenschappen van 25 oktober 1993 wat  betreft het Vlaamse Gewest, het laatst gewijzigd bij het  decreet van 9 november 2012, met uitzondering van  artikel 1, 2, eerste lid, 2bis en 3, eerste lid;

4° het Wetboek van Successierechten, zoals van  toepassing voor wat betreft het Vlaamse Gewest, voor  de belastingen, vermeld in artikel 3, 4°, van de  bijzondere wet van 16 januari 1989 betreffende de  financiering van de gemeenschappen en de gewesten,  het laatst gewijzigd bij de wet van 21 december 2013,  met uitzondering van artikel 1, artikel 60bis, § 1 tot en  met § 9, § 10, 1° en 3°, § 11, tweede tot en met vijfde lid  (als het betrekking heeft op overlijdens van voor 1  januari 2012), artikel 76, artikel 96 tot en met 99 van het  federale Wetboek van Successierechten, artikel 101 tot  en met 103 2 van het federale Wetboek van  Successierechten, artikel 144, artikel 145, artikel 163 en  boek II, IIbis en III;

5° het Wetboek der Registratie-, Hypotheek- en  Griffierechten, zoals van toepassing voor wat betreft het  Vlaamse Gewest voor de belastingen, vermeld in artikel  3, 6°, 7° en 8°, van de bijzondere wet van 16 januari  1989  betreffende  de  financiering  van  de  gemeenschappen en de gewesten, het laatst gewijzigd bij  het decreet van 28 maart 2014, met uitzondering van  artikel 1, artikel 2 (met uitzondering van het derde lid,  de woorden "alsook de voorschriften die voor de juiste  heffing van de verschuldigde rechten nodig zijn"),  artikel 2bis tot en met artikel 8bis, artikel 9, eerste en  tweede lid, artikel 10, tweede lid, artikel 11, tweede en  derde lid, artikel 13, artikel 19, artikel 211, artikel 212,  1°, artikel 23 tot en met artikel 34, artikel 35, eerste en  vijfde lid (als die leden geen betrekking hebben op de  registratiebelasting), artikel 35, tweede en derde lid,  artikel 36 tot en met artikel 39, artikel 41, 2° en 3°,  artikel 41bis, artikel 43 (als het geen betrekking heeft op  schenkbelasting, verkooprecht of verdeelrecht), artikel  75, tweede lid, tweede zin, artikel 77 tot en met artikel  84, artikel 88, artikel 921 (als het geen betrekking heeft  op het recht van hypotheekvestiging), artikel 922, artikel  94, artikel 103, artikel 115 tot en met artikel 119, artikel  121 (als het geen betrekking heeft op verkooprecht),

5° /1 artikel 161, 1°, van het Wetboek der Registratie-,  Hypotheek- en Griffierechten, zoals van toepassing voor  het Vlaamse Gewest voor de belastingen, vermeld in  artikel 3, eerste lid, 6°, 7° en 8°, van de bijzondere wet  van 16 januari 1989 betreffende de financiering van de  gemeenschappen en de gewesten, als het betrekking  heeft op schenkbelasting en op het recht op  hypotheekvestiging;

6° artikel 9 van het organiek besluit van 18 maart 1831  van het bestuur van `s lands middelen voor wat betreft  de  administratieve  geldboetes  of  de  belastingverhogingen opgelegd in toepassing van titel 3,  hoofdstuk 18;

7° artikel 4, 5, de bijlage en de tweede bijlage van het  koninklijk besluit van 11 januari 1940 betreffende de  uitvoering  van  het  Wetboek  der  Registratie-,  Hypotheek- en Griffierechten;

8° artikel 3 van het besluit van de Vlaamse Regering van  2 maart 2012 tot uitvoering van de artikelen  140quinquies en 140sexies van het Wetboek der  Registratie-, Hypotheek- en Griffierechten en de  artikelen 60/4 en 60/5 van het Wetboek der  Successierechten;

9° artikel 11, 12, 13 en 14 van het besluit van de Vlaamse  Regering van 3 mei 1995 tot regeling van de vrijstelling  inzake  successierechten  verbonden  aan  de  maatschappelijke rechten in vennootschappen opgericht  in het kader van de realisatie en/of financiering van  investeringsprogramma's van serviceflats.

---- historiek ----  ---- historique ----

- gewijzigd door art. 78 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- gewijzigd door art. 56 van het decreet van 23.12.2016  (B.S.: 30.12.2016). Tekst in werking getreden op  01.01.2017

- punt 5 gewijzigd door art. 38 van het decreet van 17

juli 2015 (B.S., 14.08.2015). De tekst is in werking  getreden op 14 augustus 2015 (art. 41)

###### Art. 5.0.0.0.2.  Art. 5.0.0.0.2.

###### Art. 29. van het decreet van 6 juli 2001 houdende

bepalingen tot begeleiding van de aanpassing van de  begroting 2001, gewijzigd bij het decreet van 9  november 2012, wordt opgeheven.

###### Art. 5.0.0.0.3.  Art. 5.0.0.0.3.

###### Art. 52. van het decreet van 23 december 2010

houdende bepalingen tot begeleiding van de begroting  2011 wordt opgeheven.

###### Art. 5.0.0.0.4.  Art. 5.0.0.0.4.

In artikel 7 van het decreet van 23 mei 2008 houdende  bepalingen tot begeleiding van de aanpassing van de  begroting 2008, gewijzigd bij het decreet van 21  december 2012, wordt paragraaf 1 opgeheven.

###### Art. 5.0.0.0.5.  Art. 5.0.0.0.5.

###### Art. 6. van het decreet van 21 december 2012 tot

wijziging van artikel 257, 258 en 376 van het wetboek  van de inkomstenbelastingen 1992 en artikel 7 van het  decreet van 23 mei 2008 houdende bepalingen tot  begeleiding van de aanpassing van de begroting 2008,  wat de vermindering van de onroerende voorheffing  voor  energiezuinige  gebouwen  betreft,  worden  opgeheven.

###### Art. 5.0.0.0.6.  Art. 5.0.0.0.6.

###### Art. 433. tot en met 440 van het WIB 92, zoals ze van

toepassing waren op de onroerende voorheffing wat  betreft het Vlaamse Gewest, vóór de inwerkingtreding  van deze codex, blijven van toepassing voor berichten  die met toepassing van artikel 433 van het WIB 92, zoals  het van toepassing was op de onroerende voorheffing  wat  betreft  het  Vlaamse  Gewest  vóór  de  inwerkingtreding van deze codex, zijn verzonden vóór  de datum van inwerkingtreding van artikel 3.12.1.0.1 tot  en met 3.12.1.0.8.

###### Art. 3.3.1.0.4. is alleen van toepassing op elke

schrapping of wissing van een voertuig die plaatsvindt  na de inwerkingtreding van deze codex.

###### Art. 5.0.0.0.8.  Art. 5.0.0.0.8.

De bevoegde entiteit van de Vlaamse administratie is  bevoegd om de overeenkomstig de toepassing van  artikel 5, § 3, van de bijzondere wet van 16 januari 1989  betreffende de financiering van de Gemeenschappen en  de Gewesten overgedragen en nog niet afgehandelde  dossiers, ongeacht of daarvoor al een dwangschrift door  de federale ontvanger is uitgevaardigd, te innen en  verder in te vorderen.

---- historiek ----  ---- historique ----

- gewijzigd door art. 60 van het decreet van 07.12.2018  (B.S. 20.12.2018). Tekst treedt in werking op 01.01.2019

###### Art. 5.0.0.0.9.  Art. 5.0.0.0.9.

Voor  de  aanslagen  die  de  rechter  vóór  de  inwerkingtreding van artikel 3.7.0.0.2 geheel of ten dele  nietig heeft verklaard om een andere reden dan  verjaring, worden de subsidiaire aanslagen die  voorgelegd worden na de sluiting van de debatten door  een aan de belastingschuldige betekend verzoekschrift  met toepassing van artikel 356 van het WIB 92, zoals het  van toepassing was op de onroerende voorheffing wat  betreft het Vlaamse Gewest vóór de inwerkingtreding  van artikel 3.7.0.0.2, geldig aan het oordeel van de  rechter onderworpen op voorwaarde dat de procedures  zijn ingeleid binnen zes maanden na de rechterlijke  uitspraak die in kracht van gewijsde is gegaan.

###### Art. 5.0.0.0.10.  Art. 5.0.0.0.10.

De reeds begonnen verjaringen worden geregeld  overeenkomstig titel 3, hoofdstuk 14, van deze codex.

###### Art. 5.0.0.0.11.  Art. 5.0.0.0.11.

De belastingen, vermeld in artikel 3, eerste lid, 4° en 6°  tot en met 8°, van de bijzondere wet van 16 januari 1989  betreffende de financiering van de gemeenschappen en  de gewesten, alsook de nalatigheidsinteresten en de  forfaitaire en proportionele fiscale boeten op die  belastingen, die nog niet zijn voldaan op 31 december  2014, en waarvoor de termijnen voor invordering die op  die datum van toepassing zijn, nog niet verstreken zijn,  kunnen in afwijking van de termijn, vermeld in artikel  3.3.3.0.1, § 4/1 en § 4/2, worden geheven tot en met 31  december 2019.

Voor de belastingen, vermeld in artikel 3, eerste lid, 6°  tot en met 8°, van de bijzondere wet van 16 januari 1989  betreffende de financiering van de gemeenschappen en  de gewesten, alsook de nalatigheidsinteresten en de  forfaitaire en proportionele fiscale boeten op die  belastingen, die op 31 december 2014 vatbaar zijn voor  teruggave en waarvoor volgens de termijn die op dat  ogenblik van toepassing is, de eis tot teruggave nog niet  is verjaard, worden de termijnen van vijf jaar, vermeld  in artikel 3.6.0.0.1 en 3.6.0.0.6, vervangen door een  termijn die eindigt op 31 december 2016.

Voor de belastingen, vermeld in artikel 3, eerste lid, 4°,  van de bijzondere wet van 16 januari 1989 betreffende  de financiering van de gemeenschappen en de gewesten,  alsook de nalatigheidsinteresten en de forfaitaire en  proportionele fiscale boeten op die belastingen, die op  31 december 2014 vatbaar zijn voor teruggave en  waarvoor volgens de termijn die op dat ogenblik van  toepassing is, de eis tot teruggave nog niet is verjaard,  worden de termijnen van vijf jaar, vermeld in artikel  3.6.0.0.1 en 3.6.0.0.4, vervangen door een termijn die  eindigt op 31 december 2019.

In afwijking van artikel 5.0.0.0.1, 4°, worden voor de  belastingen, vermeld in artikel 3, eerste lid, 4°, van de  bijzondere wet van 16 januari 1989 betreffende de  financiering van de gemeenschappen en de gewesten, de  procedures die vóór 1 januari 2015 zijn opgestart in  toepassing van artikel 20 Wb. Succ., afgewerkt volgens  de regels vermeld in dat artikel.

---- historiek ----  ---- historique ----

- toegevoegd door art. 323 van het decreet van 19 dec.  2014 (B.S., 29.01.2015 - Ed. 2). De tekst is in werking  getreden op 1 januari 2015 (art. 325)

###### Art. 5.0.0.0.12.  Art. 5.0.0.0.12.

(…)  (…)

---- historiek ----  ---- historique ----

- toegevoegd door art. 104 van het decreet van 18 dec.  2015 (B.S., 29.12.2015). De tekst is in werking getreden  vanaf 1 januari 2016 (art. 135))

###### Art. 5.0.0.0.13.  Art. 5.0.0.0.13.

(…)  (…)

---- historiek ----  ---- historique ----

- opgeheven door art. 56, 2° van het decreet van  21.12.2018 (B.S. 28.12.2018). Tekst treedt in werking op  07.01.2019

- toegevoegd door art. 2 van het decreet van 16 oktober  2015 (B.S., 23.10.2015 (Ed. 2)). De tekst is in werking  getreden op 1 november 2015 (Art. 3)

###### Art. 5.0.0.0.14.  Art. 5.0.0.0.14.

De termijn van drie jaar, vermeld in artikel 2.9.4.2.11, §  2, eerste lid, 2°, en de termijn van vijf jaar, vermeld in  artikel 2.9.4.2.14, § 2, tweede lid, 1°, geldt van  rechtswege ook voor de verkoopovereenkomsten die  zijn gesloten vanaf 1 juni 2018 en voor 1 juni 2020 met  toepassing van het tarief, vermeld in respectievelijk  artikel 2.9.4.2.11 en 2.9.4.2.14.

---- historiek ----  ---- historique ----

Ingevoegd door art. 6 van het decreet van 26 juni 2020  (B.S., 29.06.2020). Tekst in werking getreden op 1 juni  2020

###### Art. 5.0.0.0.15.  Art. 5.0.0.0.15.

De zekerheden die werden gesteld ter uitvoering van  artikel 3.10.5.1.3, zoals het van toepassing was voor de  opheffing van dat artikel, worden vrijgegeven. Kosten  die aan deze vrijgave zouden verbonden zijn, zijn ten  laste van de borgsteller.

---- historiek ----  ---- historique ----

- ingevoegd door art. 79 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

###### Art. 5.0.0.0.16.  Art. 5.0.0.0.16.

In afwijking van artikel 3.3.1.0.16, eerste lid, kan de  belastingplichtige  voor  een  automatisch  ontspanningstoestel dat in de eerste helft van januari  2023 wordt opgesteld, een aangifte indienen bij de  bevoegde entiteit van de Vlaamse administratie uiterlijk  op 15 januari 2023.

---- historiek ----  ---- historique ----

- Ingevoegd door art. 7 van het decreet van 25.11.2022  (B.S., 01.12.2022). Inwerkingtreding: 01.01.2023

###### Art. 5.0.0.0.17.  Art. 5.0.0.0.17.

###### Art. 3.6.0.0. 1, zoals gewijzigd bij het decreet van 9

december 2022, is van toepassing op de aanslagen,  waarvoor de termijn, vermeld in artikel 3.6.0.0.1, eerste  lid, 1°, nog niet is verstreken.

---- historiek ----  ---- historique ----

- Ingevoegd door art. 37 van het decreet van 09.12.2022  (B.S., 20.12.2022). Inwerkingtreding: 30.12.2022

###### Art. 5.0.0.0.18.  Art. 5.0.0.0.18.

De termijn van drie jaar, vermeld in artikel 2.9.4.2.12, § 2,  eerste lid, 1°, en artikel 2.9.4.2.14, § 5, eerste lid, 1°, geldt  van rechtswege ook voor overeenkomsten houdende  zuivere aankoop die gesloten zijn vanaf 1 januari 2022, of,  in afwijking daarvan, op authentieke akten verleden vanaf 1 januari 2022, wanneer de overeenkomsten houdende  zuivere aankoop waarop de akten betrekking hebben,  gesloten zijn voor 1 januari 2022 en waarvoor het tarief,  vermeld in respectievelijk artikel 2.9.4.2.12 en 2.9.4.2.14,  werd toegepast.

---- historiek ----  ---- historique ----

- Ingevoegd door art. 38 van het decreet van 09.12.2022  (B.S., 20.12.2022). Inwerkingtreding: 30.12.2022

###### Art. 5.0.0.0.19.  Art. 5.0.0.0.19.

De definitie van lichte vrachtauto, vermeld in artikel  1.1.0.0.2, derde lid, 2°, a) en b), wordt op de voertuigen die  na 31 december 2022 voor de eerste keer ingeschreven  worden in het repertorium van het Directoraat-generaal  Mobiliteit en Verkeersveiligheid of bij een vergelijkbare  instelling binnen de Europese Economische Ruimte of een  andere staat en nadien in het repertorium van het  Directoraat-generaal Mobiliteit en Verkeersveiligheid  toegepast zoals de voormelde definitie van toepassing was  vóór 1 januari 2023, als voldaan is aan de volgende  voorwaarden:

1° het voertuig is voor 1 januari 2023 besteld;  1° le véhicule a été commandé avant le 1er janvier 2023 ;

2° een kopie van de bestelbon is aan de bevoegde entiteit  van de Vlaamse administratie bezorgd voor 15 februari  2023, samen met een formulier, dat de voormelde entiteit te  beschikking stelt, dat wordt ondertekend door de betrokken

a) het identificatienummer uit het Rijksregister van de  natuurlijke personen of het identificatienummer, vermeld in  artikel 8 van de wet van 15 januari 1990 houdende  oprichting en organisatie van een Kruispuntbank van de  sociale zekerheid, van de persoon op de naam van wie het  voertuig ingeschreven is of zal worden in het repertorium  van het Directoraat- generaal Mobiliteit en  Verkeersveiligheid;

b) de voornamen, de achternaam en het domicilieadres van  de natuurlijke persoon op de naam van wie het voertuig  ingeschreven is of zal worden in het repertorium van het  Directoraat-generaal Mobiliteit en Verkeersveiligheid.

---- historiek ----  ---- historique ----

- Ingevoegd door art. 14 van het decreet van 16.12.2022  (B.S., 29.12.2022). Inwerkingtreding: 01.01.2023

###### Art. 5.0.0.0.20.  Art. 5.0.0.0.20.

###### Art. 2.9.4.2. 11, § 1, eerste lid, en artikel 2.9.5.0.5, § 1,

zijn van toepassing op overeenkomsten houdende zuivere  aankoop gesloten vanaf 1 januari 2025, of, in afwijking  daarvan, op authentieke akten verleden vanaf 1 januari  2025, wanneer de overeenkomsten houdende zuivere  aankoop waarop de akten betrekking hebben, gesloten zijn  voor 1 januari 2025.

---- historiek ----  ---- historique ----

- Ingevoegd door art. 37 van het decreet van 20.12.2024  (B.S. 30.12.2024). Inwerkingtreding op 01.01.2025

###### Art. 5.1.0.0.14.  Art. 5.1.0.0.14.

(…)  (…)

---- historiek ----  ---- historique ----

- opgeheven door art. 80 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- ingevoegd door art. 61 van het decreet van 07.12.2018  (B.S. 20.12.2018). Tekst in werking

getreden op 01.01.2019

###### Art. 5.1.0.0.15.  Art. 5.1.0.0.15.

(…)  (…)

- opgeheven door art. 80 van het decreet van 02.04.2021  (B.S., 15.04.2021). Inwerkingtreding: 25.04.2021

- abrogé par l'art. 80 du décret du 02.04.2021 (M.B.,  15.04.2021). En vigueur le 25.04.2021

- ingevoegd door art. 62 van het decreet van 07.12.2018  (B.S. 20.12.2018). Tekst in werking

- inséré par l’art. 62 du décret du 07.12.2018 (M.B.  20.12.2018). Texte entre en vigueur le 01.01.2019.

getreden op 01.01.2019

###### Art. 6.0.0.0.1.  Art. 6.0.0.0.1.

Deze codex wordt aangehaald als: Vlaamse Codex  Fiscaliteit van 13 december 2013.

## TITEL 7 - Inwerkingtredingsbepalingen  TITRE 7 - Dispositions d'entrée en vigueur

###### Art. 7.0.0.0.1.  Art. 7.0.0.0.1.

### Titel 1, 3, 4, 5, 6 en 7 van dit decreet treden in werking  op 1 januari 2014, met uitzondering van artikel 5.0.0.0.1,  2° en 3°, dat in werking treedt vanaf aanslagjaar 2014  voor wat betreft de bepalingen van de verkeersbelasting  op  de  autovoertuigen,  de  belasting  op  de  inverkeerstelling en het eurovignet die overeenkomstig  de  concordantietabel  1  uit  bijlage  1  een  corresponderende bepaling hebben in titel 2 van deze  codex.

### Titel 2 treedt in werking vanaf aanslagjaar 2014.  Le Titre 2 entre en vigueur à partir de l'année  d'imposition 2014.

Kondigen dit decreet af, bevelen dat het in het Belgisch

Staatsblad zal worden bekendgemaakt.

Brussel, 13 december 2013.  Bruxelles, le 13 décembre 2013.

De minister-president van de Vlaamse Regering,  Le Ministre-Président du Gouvernement flamand,

K. PEETERS  K. PEETERS

De Vlaamse minister van Financiën, Begroting, Werk,

Ruimtelijke Ordening en Sport,

Ph. MUYTERS  Ph. MUYTERS