---
tags: ["2.3", "2.8"]
itaa-lex-sectie: ""
wet: "Circulaire 2020/C/35 betreffende richtlijnen inzake verrekenprijzen voor multinationale ondernemingen en belastingadministraties — FOD Financiën AAFisc Internationale fiscaliteit"
bron_rol: "interpretatief"
status: "beschikbaar"
bijgewerkt: "25.02.2020"
bron: "onbekend"
chunk:
  level: 2
  type: "Art."
  sub_strategy:
provenance:
  inputs:
    - id: resources/raw/handcrafted/Circ-2020-C-35-verrekenprijzen.md
      sha256: cc114988dfc9ca2234e9277f127a8c299aa7aec0708b7fb739c83cd3ce60cb34
      version: 25.02.2020
      pages:
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: 0c77206e-dirty
    model:
    prompt_version:
  generated_at: '2026-05-19T18:46:02Z'
  stale: false
  stale_reason:
  trust:
    status: trusted
    confirmed_at: '2026-05-19T18:51:56Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: 'Grote circulaire (1507 regels, 12 hoofdstukken) met correcte hoofdstuk-headings op ##-niveau en paragrafen genummerd 1-286. Inhoud is volledig en ononderbroken leesbaar tot en met het slotartikel; geen OCR-confusion of scrambled volgorde. De TOC-items vóór Hoofdstuk I zijn weliswaar niet als headings geformatteerd maar als plain-tekst-blokken — dit is een cosmetisch residu, geen functioneel probleem voor de chunker.'
    caveat:
    layer1:
      status: pass
      run_id: 20260519-184604
      run_at: '2026-05-19T18:46:04Z'
      heading_count: 24
      max_section_chars: 22534
      file_size_chars: 136203
      flags: []
    layer2:
      status: trusted
      agent: subagent-sonnet-4-6
      run_at: '2026-05-19T18:51:56Z'
      rationale: 'Grote circulaire (1507 regels, 12 hoofdstukken) met correcte hoofdstuk-headings op ##-niveau en paragrafen genummerd 1-286. Inhoud is volledig en ononderbroken leesbaar tot en met het slotartikel; geen OCR-confusion of scrambled volgorde. De TOC-items vóór Hoofdstuk I zijn weliswaar niet als headings geformatteerd maar als plain-tekst-blokken — dit is een cosmetisch residu, geen functioneel probleem voor de chunker.'
      concrete_problemen:
        - "Regels 48-143 (TOC-blok): De inhoudsopgave is als platte tekst bewaard direct vóór de eigenlijke hoofdstukken. Meerdere TOC-items staan op één regel samengevloeid (bv. lijn 70: 'De methode van de vergelijkbare vrijemarktprijs ... De wederverkoopprijs ... De cost plus-methode' als één regel), wat kolom-bleed uit het originele PDF-layout verraadt. Dit zijn C-categorie-problemen (kolom-bleed in TOC) maar treft alleen de TOC, niet de body-tekst."
        - "Interne sub-sectie-titels (bv. 'HET VASTSTELLEN VAN VERREKENPRIJZEN', 'KEUZE VAN DE METHODE', 'CASH POOL') staan als ALLCAPS plain-tekst vóór de paragrafen in plaats van als ###-headings. Dit is consistent door het gehele document en matcht de bronopmaak, maar mist heading-promotie op sub-hoofdstuk-niveau."
        - "Lijn 1457: '(11 )' met spatie vóór het haakje — source-typo."
        - "Lijn 1507: 'NL' als laatste regel — taalcode-residu uit origineel document, functioneel neutraal."
---

# Circulaire 2020/C/35 betreffende richtlijnen inzake verrekenprijzen voor multinationale ondernemingen en belastingadministraties — FOD Financiën AAFisc Internationale fiscaliteit

*Bijgewerkt tot en met 25.02.2020 — gecoördineerde versie.*

Inhoudstafel

Inleiding

## Hoofdstuk I: Het arm's length principe

Het vaststellen van verrekenprijzen
Diverse topics

Verliezen (TPG 2017, § 1.129 - 1.131)
Overheidspolitiek (TPG 2017, § 1.132 - 1.136)
Ontvangen subsidies
Location savings (TPG 2017, § 1.140 - 1.143)
Groepssynergiën (TPG 2017, § 1.157 - 1.163)

## Hoofdstuk II: De verrekenprijsmethoden

Keuze van de methode
Verrekenprijsmethoden

De traditionele methoden (TPG 2017, § 2.13 - 2.61)

De methode van de vergelijkbare vrijemarktprijs (CUP) (TPG 2017, § 2.14 - 2.26) De wederverkoopprijs (RPM) (TPG 2017, § 2.27 - 2.44) De cost plus-methode (CPM) (TPG 2017, § 2.45 - 2.61)

De transactionele winstmethoden (TPG 2017, § 2.62 - §§ 2.183)

De transactionele nettomargemethode (TNMM) (TPG 2017, § 2.64 - 2.113)
De Profit Split methode (4) (PSM) (TPG 2017, §§ 2.114 - 2.183) (5)

Aandachtspunten voor alle methodes

## Hoofdstuk III: De vergelijkbaarheidsanalyse

Inleiding
Verloop van een vergelijkbaarheidsanalyse

Stap 1. Bepalen van de periode voor het vergelijkbaarheidsonderzoek (TPG 2017, § 3.74 - 3.79) Stap 2. Brede analyse van de omstandigheden waaronder de belastingplichtige zijn activiteiten voert (TPG 2017, § 3.7) Stap 3: Analyse van de gelieerde transactie(s) (TPG 2017, § 3.8 - 3.17) Stap 4: Beoordeling van de bestaande interne vergelijkingspunten (TPG 2017, § 3.27 - 3.28) Stap 5: Externe vergelijkingspunten en hun bronnen (TPG 2017, § 3.29 - 3.39) Stap 6: Selectie van de meest geschikte verrekenprijsmethode (TPG 2017, § 3.20 - 3.23) Stap 7: Selecteren en verwerpen van potentiële vergelijkbare bedrijven (TPG 2017, § 3.40 - 3.46) Stap 8: Aanpassingen om verschillen in vergelijkbaarheid te elimineren (TPG 2017, § 3.47 - 3.54) Stap 9: Het gebruik van een arm's length range (TPG 2017, § 3.55 - 3.66)

## Hoofdstuk IV: Administratieve benaderingen tot het voorkomen en het oplossen van geschillen inzake verrekenprijzen

## Hoofdstuk V: Documentatieverplichtingen

## Hoofdstuk VI: Bijzondere overwegingen inzake immateriële activa

Inleiding
Identificatie van immateriële activa
Eigendom van immateriële activa en DEMPE functies
Bepalen van de verrekenprijs in transacties met immateriële activa
Enkele aandachtspunten bij het gebruik van waarderingstechnieken
De verrekenprijs wanneer de waardering van het immaterieel actief op het tijdstip van de transactie hoogst onzeker is Moeilijk te waarderen immateriële activa

## Hoofdstuk VII: Bijzondere overwegingen inzake intragroepsdiensten

Inleiding
Intragroepsdiensten
Vergoeding volgens het arm's length-beginsel
Intragroepsdiensten met beperkte toegevoegde waarde

## Hoofdstuk VIII: Kostenbijdrageregelingen of Cost Contribution Agreements (CCA)

Inleiding
Arm's length beginsel
Bepalen van de deelnemers
Waardebepaling van de CCA
Verwachte opbrengsten
Bijdragen
Compensatiebetalingen
Nieuwe leden, uittredende leden en stopzetting van de CCA
Documenteren van CCA's

## Hoofdstuk IX: Verrekenprijsaspecten van bedrijfsherstructureringen

Inleiding
Aandachtspunten bij bedrijfsherstructureringen
Arm's Length vergoeding voor de herstructurering zelf

Stap 1: analyse van de transacties die begrepen zijn in de herstructurering door (TPG 2017, § 9.13 - 9.33) Stap 2: erkenning van de herstructurering (TPG 2017, § 9.34 - 9.38) Stap 3: onderzoek van de relatie tussen de herstructurering en de verplaatsing van winstpotentieel (TPG 2017, § 9.39 - 9.47) Stap 4: onderzoek van de verrekenprijsgevolgen van de herstructurering

Verrekenprijzen na de herstructurering

## Hoofdstuk X: Financiële transacties

Inleiding
Rating
Intra-groep leningen
Intra-groep garanties
Cash pool

## Hoofdstuk XI: Vaste inrichtingen en verrekenprijzen

Algemeen
De toepassing van de AOA methode: 2 stappen
Op welke wijze dient 'vrij kapitaal' aan de vaste inrichting toegewezen te worden?

## Hoofdstuk XII: Inwerkingtreding

Inleiding

Deze circulaire heeft als doel een overzicht te geven van de OESO-richtlijnen betreffende verrekenprijzen (1) voor multinationale ondernemingen en belastingadministraties. In het vervolg van deze circulaire zal naar deze richtlijnen als volgt verwezen worden: TPG 2017, § …. Deze richtlijnen werden door het BEPS-actieplan en meer bepaald de actieplannen 8 - 10 ingrijpend gewijzigd.

(1) OECD Transfer Pricing Guidelines for Multinational Enterprises and Tax Administrations, OECD, July 2017

Ter zake kan worden verwezen naar de toepassing van artikel 31 van het Verdrag van Wenen van 23.05.1969 inzake het verdragenrecht.

De circulaire bespreekt de hoofdstukken I, II, III,VI,VII, VIII en IX van de OESO-richtlijnen betreffende verrekenprijzen. Eveneens worden bepaalde financiële transacties overlopen. Ten slotte is een summiere bespreking opgenomen van de OESO-richtlijnen betreffende vaste inrichtingen.

Waar nuttig en aangewezen wordt de voorkeur van de administratie weergegeven.

Een verrekenprijs is een prijs voor een goed of dienst tussen verbonden ondernemingen op basis waarvan Multinationale Ondernemingen (MNO) hun winsten (verliezen) at arm's length verdelen over de leden van de groep.

Alhoewel andere methodes denkbaar zijn om tot een dergelijke verdeling te komen onderschrijft de Belgische belastingadministratie de principes van de TPG 2017 waarbij het arm's length principe centraal staat. Algemeen kan aangenomen worden dat latere wijzigingen aan de TPG 2017 ook door België zullen gevolgd worden.

Het arm's length principe is eveneens een internationaal aanvaarde standaard om winsten (verliezen) van MNO te verdelen over de leden ervan.

Het arm's length principe vindt zijn verantwoording in de 'afzonderlijke entiteiten benadering' (separate entity approach). In zijn meest eenvoudige vorm betekent dit dat de leden van een multinationale groep in hun prijszetting moeten worden beschouwd als niet-verbonden. Deze benadering beschouwt de OESO als de meest optimale voor de toewijzing van een correcte belastbare basis aan de verschillende landen waar leden van de multinationale groep gevestigd zijn en ter vermijding van dubbele belasting.

Een verbonden onderneming is een onderneming die voldoet aan de voorwaarden gesteld in artikel 9, sub paragrafen a) en b) van het OESO Modelverdrag ter vermijding van dubbele belasting (2).

(2) Model Tax Convention on Income and on Capital, OECD, November 2017

Verbonden ondernemingen kunnen transacties tot stand brengen die derde partijen niet aangaan.

Dergelijke transacties zijn niet noodzakelijkerwijs ingegeven door belastingontwijking, maar kunnen hun bestaansreden vinden in de verschillende commerciële omstandigheden tussen leden van een MNO-groep onderling ten overstaan van onafhankelijke ondernemingen. Het loutere feit dat een transactie niet tussen onafhankelijke partijen kan worden teruggevonden, betekent op zich niet dat deze het arm's length principe zou miskennen.

Het is van belang te erkennen dat de manier om prijzen tussen verbonden ondernemingen vast te stellen geen exacte wetenschap is. Zowel de belastingadministratie als de belastingplichtige zullen bijgevolg de nodige flexibiliteit en samenwerking aan de dag moeten leggen om tot een arm's length prijs te komen. Hierbij mag de administratie geen onredelijke eisen stellen qua onderbouw en bewijs van een verrekenprijs. De belastingplichtige daarentegen moet voor de nodige documentatie zorgen ter verantwoording van een toegepaste verrekenprijs. Deze twee uitgangspunten kunnen een spanningsveld creëren. Het is bijgevolg aangewezen dat beide partijen constructief samenwerken bij het bepalen van de gehanteerde verrekenprijzen.

Een rechtzetting van een verrekenprijs, al dan niet met het akkoord van de belastingplichtige, kan leiden tot een dubbele belasting. De belastingplichtige kan ter opheffing hiervan een beroep doen op de procedures voorzien in de dubbelbelastingverdragen, de wet d.d. 02.05.2019 (BS 17.05.2019) tot omzetting van de richtlijn (EU) 2017/1852 van de raad van 10.10.2017 betreffende mechanismen ter beslechting van belastinggeschillen in de Europese Unie of het arbitrageverdrag.

## Hoofdstuk I: Het arm's length principe
HET VASTSTELLEN VAN VERREKENPRIJZEN

1. Voor het bepalen van een prijs geldt het arm's length principe zoals dit bepaald is in het artikel 9 van het OESO Modeldubbelbelastingverdrag. Dit artikel stelt dat verbonden ondernemingen in hun financiële en commerciële transacties moeten handelen alsof ze niet-verbonden zijn. Indien ze voorwaarden overeenkomen die afwijken van de voorwaarden die niet-verbonden ondernemingen zouden overeenkomen kan de (verreken)prijs worden aangepast.

2. Finaal moet een analyse van de verrekenprijzen nagaan of een Belgische onderneming niet teveel betaalde (of zal betalen) of te weinig aanrekende (of zal aanrekenen) voor een goed of een dienst. Centraal hierbij staat de vergelijkbaarheidsanalyse waarbij onderzocht wordt of de voorwaarden overeengekomen tussen verbonden ondernemingen vergelijkbaar zijn met deze overeengekomen tussen niet-verbonden ondernemingen. Hierbij wordt als volgt tewerk gegaan:

Het identificeren en accuraat omschrijven zal gebeuren middels een grondige analyse van de vergelijkbaarheidsfactoren:

- contractuele voorwaarden van de transactie;

- functies, activa en risico's (functionele analyse);

- karakteristieken van verhandelde goederen en diensten;

- economische omstandigheden van de betrokken partijen en de markten waarin ze werkzaam zijn;

- bedrijfsstrategieën.

Het zoeken naar betrouwbare comparables

3. Deze worden ook de 'economisch relevante karakteristieken' genoemd. De vergelijkbaarheidsanalyse en de functionele analyse die het corpus vormt, worden gelijktijdig uitgevoerd. Belangrijk hierbij is dat de prijs het resultaat is van ondermeer de uitgeoefende functies, de ingezette activa en de gedragen risico's (voorwaarden).

Zo zal een wederverkoper van goederen bereid zijn eventueel een hogere prijs te betalen bij de aankoop van de door hem te verkopen goederen indien hij de garantie heeft verkregen dat hij de niet verkochte goederen zal mogen terugsturen aan zijn leverancier.

4. Een analyse van de bestaande contractuele bepalingen afgesloten tussen verbonden ondernemingen betreffende intercompany transacties is het vertrekpunt bij het vaststellen van een verrekenprijs. De contracten zouden moeten verwoorden wat de functionele analyse vaststelt. Indien dit niet het geval is zullen het gedrag van de partijen betrokken bij de transactie en de andere relevante informatie primeren bij het vaststellen van de verrekenprijs.

5. Een analyse van de karakteristieken van de verhandelde goederen en diensten is van groter belang bij het gebruik van de Comparable Uncontrolled Price methode (CUP methode). Bij de andere methodes waarbij de nadruk meer ligt op een analyse van uitgeoefende functies, ingezette activa en gedragen risico's is dit van minder belang.

6. Voor een efficiënte analyse van de risico's wordt best de volgende 6-stappen benadering gebruikt (TPG 2017, § 1.60):

- Stap 1: Identificatie van de specifieke economisch belangrijke risico's;

- Stap 2: Welke verbonden partijen dragen contractueel deze risico's?

- Stap 3: Welke verbonden partijen dragen de risico's in werkelijkheid? Wie de controle over het risico en de financiële capaciteit om een risico te dragen heeft staat centraal bij deze analyse;

- Stap 4: Nagaan of stap 2 en 3 consistent zijn, m.a.w. komt datgene wat gebeurt in de praktijk overeen met hetgeen contractueel is bepaald;

- Stap 5: Indien de gedragingen van de verbonden partijen niet consistent zijn wordt het risico toegewezen aan de partij die het risico controleert en de financiële capaciteit hiervoor heeft;

- Stap 6: Rekening houdende met het voorgaande wordt de prijs bepaald voor de verbonden transactie.

7. Het risico management staat centraal en impliceert de mogelijkheid tot het nemen van beslissingen betreffende het beheer van het risico. Dit houdt het volgende in (TPG 2017, § 1.61):

- Beslissen om al dan niet een risico te nemen.

- Reageren indien een risico zich voordoet.

- Maatregelen nemen om de effecten bij een mogelijke realisatie ervan te verminderen.

8. Financiële capaciteit (TPG 2017, § 1.64) is de mogelijkheid om de materialisering van het risico te dragen rekening houdend met de realistische mogelijkheid om eventueel beroep te doen op bijkomende liquiditeiten. De inschatting moet gebeuren alsof de partij die het risico ondergaat handelt alsof ze een onafhankelijke zou zijn.

9. De controle over het risico (TPG 2017, § 1.65) omvat het nemen van beslissingen over en het reageren op een risico. Bepaalde functies die behoren bij het beheer van het risico kunnen uitbesteed worden. Zo kan het dagelijkse beheer van het risico in bepaalde situaties worden uitbesteed. In een vergelijkbare situatie tussen derden zal de opdrachtgever nauwgezet toezien op de werkzaamheden van de opdrachtnemer en meer bepaald of deze handelt binnen het kader van de opdracht die hem is toegewezen.

Het vergelijken van deze voorwaarden met de voorwaarden van vergelijkbare financiële en commerciële transacties zoals deze tussen derden zijn overeengekomen

10. Na de analyse van de verbonden transacties worden deze vergeleken met vergelijkbare transacties tussen niet verbonden partijen. Voor het bepalen van een prijs kan worden verwezen naar volgende hoofdstukken.

11. In situaties waarbij één van de verbonden vennootschappen zowel de controle over het risico als de financiële capaciteit heeft om het risico te dragen kan de verrekenprijs relatief eenvoudig worden bepaald. Er zijn echter situaties mogelijk waarbij meerdere partijen betrokken zijn bij de controle over de risico's. In een dergelijke situatie bepaalt TPG 2017, § 1.94 dat dient nagegaan te worden wie de financiële capaciteit heeft om de risico's te dragen. De onderneming die zowel controle over de risico's heeft als de financiële mogelijkheid om deze risico's te dragen heeft recht op de winst die overblijft nadat alle bij de transactie(s) betrokken partijen marktconform vergoed werden. TPG 2017, § 105 stelt duidelijk dat partijen die eveneens controle over het risico uitoefenen voor deze functie marktconform dienen vergoed te worden. Als verrekenprijsmethode zou in dergelijk geval een profit split methode kunnen aanbevolen worden.

12. Het kan gebeuren dat bepaalde transacties tussen verbonden ondernemingen zich niet voordoen tussen onafhankelijke ondernemingen. Een voorbeeld hiervan zijn cash-pooling overeenkomsten. Dergelijke transacties moeten niet per definitie worden afgewezen voor verrekenprijsdoeleinden. De vraag die hier centraal staat is of de transactie 'commercieel rationeel is' en niet of de transactie zich voordoet tussen derden. Transacties die zich onmogelijk kunnen voordoen tussen derde partijen kunnen in bepaalde omstandigheden als marktconform worden beschouwd.

13. Al het mogelijke moet gedaan worden om een transactie zo accuraat mogelijk te omschrijven. Indien de transactie niet verloopt conform de geschreven contracten zal het gedrag van de betrokken partijen primeren. Slechts in uitzonderlijke omstandigheden zal een transactie niet erkend worden en zal een herkwalificatie plaatsvinden (TPG 2017, §§ 1.122 - 1.125). Dit zal slechts gebeuren indien de voorwaarden van de transactie, zoals ze door derden zouden zijn overeengekomen, verschillen van de voorwaarden van de verbonden transactie. Centraal hierbij staat de overweging of de verbonden transactie als commercieel rationeel kan beschouwd worden en niet de mogelijkheid of een dergelijke transactie zich voordoet tussen derde partijen.

DIVERSE TOPICS
Verliezen (TPG 2017, § 1.129 - 1.131)

14. Speciale aandacht moet worden besteed aan vennootschappen met verliezen en in het bijzonder indien de groep in zijn geheel winstgevend is. Verliezen kunnen het gevolg zijn van een bepaalde commerciële strategie of de wens van de groep om verlieslatende producten in de markt te houden in het kader van het aanbieden van een totaal productassortiment. In al deze gevallen is het van belang te stellen dat deze verliezen slechts een beperkte tijdsduur kunnen hebben. Een commerciële strategie moet finaal uitmonden in een winstgevendheid zo niet wordt deze stopgezet.

Overheidspolitiek (TPG 2017, § 1.132 - 1.136)

15. In sommige gevallen kunnen de acties van een lokale overheid de prijzen van een goed of dienst beïnvloeden. Voorbeelden hiervan zijn subsidies, bepaalde belastingen of overheidsreglementeringen. Een voorbeeld van een overheidsmaatregel met een verregaand effect op de verrekenprijzen zijn de RIZIV heffingen op de omzet van terugbetaalbare geneesmiddelen, een soort van omzetbelasting op medicijnen met voorschrift. Het is duidelijk dat de effecten van een overheidspolitiek mee moeten verwerkt worden in de bepaling van een verrekenprijs.

16. De administratie is van mening dat voor ondernemingen, met een beperkt functioneel en risicoprofiel, die onderworpen zijn aan de zogenaamde RIZIV heffingen, de operationele winst, bij voorkeur bepaald wordt op basis van een TNMM methode met als PLI Return On Sales (voor een gedetailleerde uitleg betreffende deze begrippen: zie verder in de circulaire). Er werd vastgesteld dat deze heffingen soms worden geboekt in mindering van de omzet. Overeenkomstig het CBN-advies 2018/10 moeten deze heffingen echter als kost worden geboekt en niet in mindering worden gebracht op de omzet.

Ontvangen subsidies

17. Het probleem dat zich hier stelt is of ontvangen overheidssubsidies moeten worden meegerekend bij het bepalen van de verrekenprijs. Afhankelijk van de weerhouden PLI bij de TNMM-methode kan het volgende zich voordoen:

- Subsidies komen in mindering van de kostengrondslag/omzet indien er een rechtstreeks verband is tussen de subsidie en de productie/omzet van het goed of de levering van de dienst. Bijvoorbeeld de vrijstelling bedrijfsvoorheffing kan in aanmerking komen.

- Indien er geen rechtstreeks verband is tussen de subsidie en de productie/omzet van het goed of de levering van de dienst, dan komen de subsidies niet in mindering van de kostengrondslag.

- Fiscale aftrekken komen niet in mindering van de kostengrondslag. Een investeringsaftrek bijvoorbeeld komt niet in mindering van de kostengrondslag.

Location savings (TPG 2017, § 1.140 - 1.143)

18. Location savings kunnen omschreven worden als besparingen die worden gerealiseerd door te opereren in een bepaalde markt.

19. Voor de eventuele verdeling van deze 'location savings' kan nuttig verwezen worden naar TPG 2017, §§ 1.140 – 1.143 en 9.126 – 9.131.

Groepssynergiën (TPG 2017, § 1.157 - 1.163)

20. Groepssynergiën kunnen omschreven worden als voordelen die gerealiseerd worden door interacties tussen verschillende leden van een multinationale groep en die zich per definitie niet voordoen tussen onafhankelijke entiteiten. Groepssynergiën worden dus in eerste instantie niet gevat door een verrekenprijs. Voorbeelden zijn voordelen verkregen bij groepsaankopen (procurement) en het verkrijgen van leningen aan betere voorwaarden. Ook hier stelt zich hier de vraag aan wie deze voordelen moeten toekomen.

21. Bij procurement moeten gerealiseerde voordelen tengevolge van het bundelen van aankopen van de leden volledig ten goede komen aan de leden van de groep. De procurement-werkzaamheden zullen vergoed worden met een winstmarge met de operationele kosten als basis. Indien kan aangetoond worden dat de procurement activiteiten meer omvatten dan enkel het bundelen van de aankopen kan een andere vergoedingswijze overwogen worden. De functionele analyse moet in dergelijk geval het waarde-toevoegend karakter van het procurement center aantonen.

## Hoofdstuk II: De verrekenprijsmethoden
KEUZE VAN DE METHODE

22. De keuze van een verrekenprijsmethode beoogt altijd het bepalen van de meeste geschikte methode voor een welbepaalde transactie. Het selectieproces (TPG 2017, § 2.2) dient rekening te houden met:

- de voor- en nadelen van de door de OESO erkende methoden;

- de samenhang van de methode ten opzichte van de aard van de gecontroleerde transactie die wordt onderzocht;

- de beschikbaarheid van noodzakelijke en betrouwbare informatie;

- de graad van vergelijkbaarheid van de gecontroleerde transacties en de onafhankelijke transacties, met inbegrip van de betrouwbaarheid van de vergelijkbaarheidsaanpassingen die nodig zouden kunnen zijn om de onderlinge verschillen weg te werken.

23. De administratie dient bij het vaststellen van de verrekenprijzen te vertrekken vanuit de methode die de belastingplichtige heeft gekozen om zijn prijzen vast te stellen (TPG 2017, § 4.9). De belastingplichtige is vrij in de keuze van een verrekenprijsmethode, mits de gekozen methode leidt tot een arm's length-uitkomst voor de specifieke transactie. De analyse van de specifieke transactie evenals de analyse van de vergelijkbaarheid laten toe de meest passende methode te bepalen.

Aandachtspunten bij de selectie van de methoden

24. De accurate omschrijving van de transactie levert de meeste informatie op die nodig is om de meest passende methode te kiezen. Wanneer uit de functionele analyse blijkt dat een partij een 'routinematige' inbreng levert terwijl de inbreng van de andere partij veel belangrijker is (bv. de inbreng van unieke immateriële activa omvat of het dragen van significante economische risico's inhoudt), wordt een eenzijdige methode geacht meer aangewezen te zijn en zal het nodig zijn een geteste partij te selecteren (3).

(3) Zie §§ 3.18 - 3.19 van de TPG 2017, die betrekking hebben op de keuze van de geteste partij. Algemeen heeft de toepassing van een eenzijdige methode tot gevolg dat alle overblijvende winsten (of verliezen) van de transactie naar de andere partij gaan; de geteste partij is gewoonlijk die met de minst complexe functies, rekening gehouden met de gebruikte activa en de gelopen risico's.

25. Kiest een belastingplichtige voor een transactie de meest geschikte methode van verrekenprijzen (TPG 2017, § 2.8), dan is hij niet gehouden een analyse te maken met behulp van alle methoden die tot zijn beschikking staan en evenmin om de afwijzing van bepaalde methoden te rechtvaardigen. Het getuigt van een goede praktijk dat de belastingplichtige kan aantonen dat de gebruikte methode, rekening houdend met de feiten en omstandigheden, aanleiding geeft tot een marktconforme prijs.

26. In sommige gevallen kunnen methoden worden gecombineerd. Bijvoorbeeld ter bevestiging van een methode op basis van de bruto marge door een methode die steunt op de netto marge. Een belastingplichtige is echter niet gehouden meerdere methoden te gebruiken om de arm's length-prijs van een transactie te bepalen.

27. Er bestaat niet echt een 'hiërarchie' van de verschillende methoden. Indien meerdere methoden met een identieke betrouwbaarheidsgraad kunnen worden toegepast, is een traditionele methode te verkiezen boven een transactionele winstmethode. Bovendien geniet de CUP-methode de voorkeur indien de CUP-methode en een andere verrekenprijsmethode kunnen toegepast worden met een identieke betrouwbaarheidsgraad (TPG 2017, § 2.3).

28. De transactionele winstmethoden kunnen in sommige gevallen meer aangewezen zijn dan de traditionele methoden (TPG 2017, § 2.4). Het gaat bijvoorbeeld om de toepassing van de Profit Split methode in gevallen waar alle ondernemingen unieke en waardevolle bijdragen leveren of in gevallen waarbij de partijen deelnemen in zeer geïntegreerde transacties.

29. Het staat multinationale groepen vrij om voor de vaststelling van de prijzen methoden toe te passen die niet worden beschreven in TPG 2017, op voorwaarde dat die prijzen in overeenstemming zijn met het arm's length-principe (TPG 2017, § 2.9). Die andere methoden mogen echter niet gebruikt worden ter vervanging van een door de OESO erkende methode indien die laatste passender blijken te zijn gelet op de feiten en omstandigheden van het geval. De keuze van andere methoden moet gestaafd worden door:

- de reden(en) waarom de door de OESO erkende methoden niet kunnen toegepast worden;

- de reden(en) waarom een andere methode een betere oplossing opleverde.

VERREKENPRIJSMETHODEN

30. De traditionele methoden op basis van de transacties (focus op prijs of bruto marge) zijn:

- de methode van de vergelijkbare vrijemarktprijs (Comparable Uncontrolled Price - CUP)

- de methode van de wederverkoopprijs (Resale Price Method - RPM),

- de cost plus methode (Cost Plus Method - CPM).

31. De transactionele winstmethoden (focus op de winst) zijn:

- de transactionele nettomargemethode (Transactional Net Margin Method - TNMM),

- de transactionele profit split methode (Profit Split Method - PSM).

Samenvatting van de methoden en hun kenmerken

Methode

Belangrijk(e)

element(en)

Vergelijkings-punt

Toepassingsvoorbeelden

CUP

Product

Prijs

Alle transacties m.b.t. goederen en diensten evenals financiële transacties

RPM

Functies/product

Brutomarge

Verdeler/wederverkoper die geen substantiële waarde toevoegt aan het product

CPM

Functies

Brutomarge

Onderaannemer/bewerker - Producent onder contract

TNMM

Functies

Ondernemingen die geen substantiële waarde toevoegen aan het product maar waarvan de toegevoegde waarde zich situeert in hun exploitatiekosten

PSM

Functies/Bijdragen

Relevante winst

Sterk geïntegreerde transacties / transacties waarvoor elke partij unieke immateriële activa van grote waarde inbrengt / De partijen dragen de risico's samen

(*) Netto winst = exploitatieresultaat = Ebit

De traditionele methoden (TPG 2017, § 2.13 - 2.61)
DE METHODE VAN DE VERGELIJKBARE VRIJEMARKTPRIJS (CUP) (TPG 2017, § 2.14 - 2.26)

32. Deze methode legt de klemtoon op de kenmerken van een goed of een dienst. Hoe meer soortgelijke kenmerken een product heeft, hoe meer zijn prijs vergelijkbaar is en hoe minder het noodzakelijk is om correcties toe te passen om deze prijs vergelijkbaar te maken.

33. De CUP methode vergelijkt de prijs van een gecontroleerde transactie met de prijs van een transactie, uitgevoerd onder vergelijkbare omstandigheden, tussen een verbonden vennootschap en een onafhankelijke vennootschap ('intern' vergelijkingspunt) of tussen twee onafhankelijke vennootschappen ('extern' vergelijkingspunt).

34. De methode van de vergelijkbare marktprijs wordt voornamelijk in de volgende gevallen toegepast:

- wanneer er een intern vergelijkingspunt bestaat;

- bij basisproducten, in het bijzonder die van actieve en liquide markten, die de neiging vertonen de prijsverschillen te neutraliseren in functie van de omstandigheden. In dergelijke gevallen zijn gegevens betreffende de prijzen van basisproducten soms beschikbaar, ook al kunnen aanpassingen noodzakelijk blijken;

- bij financiële transacties (bv. rentevoeten van leningen, kosten van garantie);

- bij het verlenen van een licentie op bepaalde immateriële activa; meer bepaald indien het niet gaat om een unieke licentie.

35. De toepassing van deze methode veronderstelt dat er geen verschil bestaat tussen de gecontroleerde en de niet-gecontroleerde transacties dat de marktprijs kan beïnvloeden, of dat het mogelijk is dit verschil door middel van aanpassingen te corrigeren om tot een vergelijkbare prijs te komen (TPG 2017, § 2.15).

36. Ter illustratie van de toepassing van de CUP-methode en van aanpassingen die noodzakelijk zouden kunnen blijken, zie TPG 2017, § 2.23 - 2.26.

DE WEDERVERKOOPPRIJS (RPM) (TPG 2017, § 2.27 - 2.44)

37. De resale price-methode bestaat uit de vergelijking van de brutomarge op de wederverkoop aan een derde onderneming met de wederverkoop van een goed of een dienst in een verbonden transactie.

38. Bij het bepalen van de brutomarge wordt inzake verrekenprijzen rekening gehouden met de zogenaamde cost of goods sold (CoGS). Opgemerkt moet worden dat de CoGS niet altijd overeenstemmen met de rekening 60 van het Belgische rekeningstelsel (de CoGS kunnen bijvoorbeeld de directe loonkosten omvatten voor de distributieactiviteit, geregistreerd onder de klasse 62 van het MAR - Minimumindeling van het Algemeen Rekeningenstelsel). Bij de boekhoudkundige controle moet hiermee rekening worden gehouden.

39. De resale price-methode wordt meestal toegepast bij:

- activiteiten van verkoop en distributie die niet gepaard gaan met de tenlasteneming van een specifiek economisch significant risico (bv. routinematige distributeurs die enkel de risico's dragen die eigen zijn aan hun functie). In de praktijk wordt deze methode soms gebruikt wanneer men beschikt over interne vergelijkingspunten;

- activiteiten met een beperkte waardecreatie, indien er externe vergelijkingspunten bestaan in dezelfde activiteitensector en op een geografisch gezien vergelijkbare markt.

40. Voorbeelden van de resale price-methode: TPG 2017, § 2.42 - 2.44).

Aandachtspunten bij de resale price-methode

41. Door het ontbreken van beschikbare betrouwbare openbare gegevens m.b.t. de brutomarge, is het niet gemakkelijk om deze methode te gebruiken.

42. Het gebruik van de RPM kan vergelijkingen moeilijk maken, daar de definitie van de gepubliceerde kosten (kostprijs van de verkochte goederen) die in aanmerking komen bij de berekening van de brutomarge kan verschillen volgens de boekhoudkundige normen van toepassing in de diverse landen.

DE COST PLUS-METHODE (CPM) (TPG 2017, § 2.45 - 2.61)

43. De cost plus methode bestaat erin de brutomarge op de kosten (CoGS) van de fabrikant of dienstverlener in een gecontroleerde transactie te vergelijken met de brutomarge op de kosten van een fabrikant of dienstverlener in een vergelijkbare vrije markt transactie.

44. De cost plus-methode is het meest geschikt voor fabrikanten en leveranciers van diensten die geen specifieke economisch significante risico's op zich nemen of geen waardevolle unieke immateriële activa exploiteren. In de praktijk wordt deze methode vaak gebruikt indien men over interne vergelijkingspunten beschikt. Bv. voor een product dat verschillend is maar betrekking heeft op vergelijkbare functies, activa en risico's.

45. Voorbeelden van de toepassing van de CPM: TPG 2017, § 2.59 – 2.61).

Aandachtspunten voor de cost plus-methode (CPM)

46. Voor de betrouwbaarheid van de toepassing van deze methode gelden dezelfde aandachtspunten als die welke werden geformuleerd bij de RPM.

47. Bij de toepassing van de CPM vereist de passende vaststelling van de kostenbasis meer aandacht dan de vaststelling van de marge, meer bepaald indien de betrokken activiteiten worden geacht een beperkte waarde toe te voegen.

48. Gewoonlijk kan men ervan uitgaan dat de hogere kosten die te wijten zijn aan een gebrek aan efficiëntie worden gedragen door de onderneming die de goederen of de diensten levert, daar het immers deze onderneming is die invloed kan uitoefenen op de omvang van de betrokken kosten. Een onafhankelijke koper aanvaardt in deze situatie geen prijsaanpassing.

De transactionele winstmethoden (TPG 2017, § 2.62 - §§ 2.183)
DE TRANSACTIONELE NETTOMARGEMETHODE (TNMM) (TPG 2017, § 2.64 - 2.113)

49. De TNMM bestaat erin de nettowinst (doorgaans de EBIT) die een belastingplichtige boekt met een gecontroleerde transactie te vergelijken, vertrekkende van de gepaste grondslag (bijvoorbeeld de kosten, de verkopen of de activa), met de nettowinst die, volgens dezelfde basis, wordt gerealiseerd in het kader van vrijemarkttransacties. Deze methode vertoont overeenkomsten met zowel de CPM als de RPM, maar wordt toegepast op basis van de nettomarge in plaats van de brutomarge.

50. Net als de CPM en de RPM is de TNMM een eenzijdige methode die als referentie de resultaten van slechts één partij bij de transactie (i.e. de 'geteste partij') hanteert terwijl de andere partij alle resterende winst (of verliezen) krijgt toegewezen.

De methode is dus gepast wanneer de geteste partij:

- een routinematige activiteit uitoefent,

- slechts een basistechnologie gebruikt,

- geen unieke bijdrage levert,

- slechts beperkte toegevoegde waarde toevoegt en deze toegevoegde waarde zich gewoonlijk situeert op het niveau van de exploitatiekosten.

51. Op te merken valt dat de TNMM kan worden toegepast met verschillende nettowinstindicatoren naargelang de aard van de activiteiten bijvoorbeeld, nl. de nettowinstindicatoren die een afspiegeling zijn van de voornaamste activiteiten die toegevoegde waarde creëren.

52. Gewoonlijk worden de volgende winstindicatoren gebruikt:

- nettowinst/omzet (Return On Sales = ROS) voor de verdelers/wederverkopers;

- nettowinst/operationele activa, i.e. het rendement van het actief (Return on Assets = ROA) voor productieactiviteiten met een hoge intensiteit aan activa of het rendement van de aangewende kapitalen (Return On Capital Employed = ROCE) voor sommige financiële activiteiten. In deze gevallen zijn de ingezette activa of het ingezette kapitaal een doorslaggevende factor voor de winst. Eén van de moeilijkheden bij het gebruik van een ROA is de waarde van activa die dient gebruikt te worden (boekhoudkundige waarde, aanschafwaarde, marktwaarde) en de mogelijkheid dat een onderneming activa huurt;

- nettowinst/totale kosten of het rendement ten opzichte van de operationele kosten (Net Cost Plus = NCP); voor dienstprestaties of productieactiviteiten waarvan de toegevoegde waarde zich eveneens op het niveau van de totale kosten situeert;

- Berry ratio of de brutomarge op de exploitatiekosten: het kan bijvoorbeeld aangewezen zijn om tussenbedrijven te testen in een keten van verbonden verrichtingen met een beperkt risico, zonder immateriële activa. Er dient te worden gewezen op de voorbehouden onder de TPG, § 2.107, inzake het gebruik van deze ratio.

Aandachtspunten voor de transactionele nettomargemethode

De kostenbasis en de voorschotten (TPG 2017, § 2.98 - 2.100)

53. Volgens TPG 2017, § 2.98 is een methode van verrekenprijzen, gebaseerd op de kosten, enkel gepast indien die kosten een relevante factor zijn van de waarde van de uitgevoerde functies, de gebruikte activa en de risico's die de geteste partij op zich neemt. Dit betekent dat de kosten die geen relevante factor voor deze waarde vertegenwoordigen moeten worden uitgesloten van de kostenbasis voor de berekening van de winst.

54. Met 'voorschotkosten' worden de kosten bedoeld van de diensten die derden of verbonden ondernemingen leveren aan de intragroepsdienstverlener, op voorwaarde dat het gaat om diensten die de derden rechtstreeks zouden kunnen factureren aan de vennootschappen van de groep die de begunstigde zijn van de intragroepsdiensten, en die derden of verbonden ondernemingen aan de intragroepsdienstverlener factureren voor een prijs die een arm's length-winstmarge omvat.

55. Een eenvoudige opdeling van kosten in 'interne kosten' en 'externe kosten' volstaat niet om deze 'externe' kosten te elimineren uit de kostenbasis en ze door te factureren zonder marge. Heel wat 'externe' kosten behoren immers tot de activiteit zelf en dragen bij tot de toegevoegde waarde. Een functionele analyse is onmisbaar om aanspraak te maken op de uitsluiting van bepaalde 'externe' kosten uit de kostenbasis (zie ook TPG 2017, § 7.34).

56. Voorbeeld: een logistieke vennootschap kan de niet-herbruikbare verpakkingen die dienen om haar goederen naar de klant te brengen niet uit de kostenbasis sluiten onder het voorwendsel dat de winstmarge op deze verpakkingen al is genomen door de leverancier ervan. Deze verpakkingen maken deel uit van haar functie van logistieke vennootschap en maken dus deel uit van de kostenbasis die haar toegevoegde waarde bepaalt.

57. Indien alle bovenstaande voorwaarden vervuld zijn, dient er geen winstmarge te worden toegepast op de voorschotkosten.

Vaststelling van de kostenbasis

58. In principe dienen de Belgische boekhoudnormen als referentie om te bepalen welke kosten al dan niet deel uitmaken van de kostenbasis.

59. Berekening van de winstindicatoren: impact van de niet-recurrente kosten en opbrengsten in het schema van de jaarrekening:

- Als gevolg van wijzigingen ingevoegd door het koninklijk besluit van 18.12.2015 tot omzetting van de richtlijn 2013/34/EU, werd de voorstelling van de jaarrekening (in casu de resultatenrekening) gewijzigd voor de boekjaren die beginnen na 31.12.2015;

- Het voornaamste verschil betreft de verdwijning van de uitzonderlijke resultaten en de verschijning van de niet-recurrente resultaten, inzonderheid in het nieuwe schema op pagina VOL 4:

code 76A, Toel. 6.12; Niet-recurrente bedrijfsopbrengsten;

code 66A, Toel. 6.12; Niet-recurrente bedrijfskosten;

code 76B, Toel. 6.12; Niet-recurrente financiële opbrengsten;

code 66B, Toel. 6.12; Niet-recurrente financiële kosten;

- Bij de berekening van de nettowinstindicator dient men voortaan rekening te houden met de opname van deze niet-recurrente resultaten in de jaarrekening (en in de databanken die ze verzamelen) en dienen dus aanpassingen doorgevoerd te worden indien dit nodig blijkt bij gebrek aan enig verband met de betreffende activiteit, zowel in de berekening van de marges van de Belgische belastingplichtigen als in de analyse van de vergelijkbare vennootschappen, indien deze informatie beschikbaar is voor deze laatsten.

DE PROFIT SPLIT METHODE (4) (PSM) (TPG 2017, §§ 2.114 - 2.183) (5)

(4) 16 voorbeelden van toepassing van de PSM zijn opgenomen in bijlage II van hoofdstuk II van de TPG 2017.
(5) Dit onderdeel van hoofdstuk II is gebaseerd op de aanpassing van TPG 2017 die door de OESO in juni 2018 werd gepubliceerd (de tekst is via deze link raadpleegbaar: http://www.oecd.org/tax/transfer-pricing/revised-guidance-on-the-application-of-the-transactional-profit-split-method-beps-action-10.htm ). De verwijzingen naar §§ randnummers van de TPG 2017 verwijzen naar de randnummers gebruikt in voormeld document.

60. De transactionele winstverdelingsmethode bestaat erin aan elke verbonden onderneming die deelneemt aan een gecontroleerde transactie het deel van de gemeenschappelijke nettowinst (of van het verlies) van deze transactie toe te kennen die een onafhankelijke onderneming zou mogen verwachten indien ze betrokken was bij een vergelijkbare vrijemarkttransactie (TPG 2017, §§ 2.114). De PSM is een van de methoden die de OESO aanbeveelt en zoals voor elke methode zijn het de afbakening van de transactie, de functionele analyse en de beschikbaarheid van betrouwbare informatie die bepalen welke methode het best geschikt is om de prijs van de transactie vast te stellen. Het gebrek aan betrouwbare informatie is in se onvoldoende om te besluiten dat de PSM de meest geschikte methode is (TPG 2017, §§ 2.128).

61. In tegenstelling met de eenzijdige methoden houdt de PSM rekening met de bijdragen van alle bij de transactie betrokken ondernemingen om tot een passende verdeling van de gecombineerde winst te komen. De gezamenlijke winst (verlies) van de gecontroleerde transactie(s) dienen geïdentificeerd te worden en vervolgens verdeeld te worden volgens de bijdragen van elk van de verbonden ondernemingen op een coherente basis vergelijkbaar met de wijze waarop niet-verbonden ondernemingen de winst (het verlies) zouden verdelen.

62. Het gebruik van de PSM kan het meest gepast zijn indien:

- beide partijen unieke en waardevolle bijdragen leveren (TPG 2017, §§ 2.130 – 2.132);

- de activiteiten van de verbonden ondernemingen sterk geïntegreerd zijn (TPG 2017, §§ 2.133 – 2.138);

- belangrijke economische risico's worden gezamenlijk gedragen door de verbonden ondernemingen of economisch belangrijke risico's worden afzonderlijk gedragen door de verbonden ondernemingen maar de risico's zijn zo nauw verbonden dat de uitwerking van een risico de volledige transactie beïnvloedt (TPG 2017, §§ 2.139 – 2.142).

63. Het voornaamste zwakke punt van deze methode bestaat in haar moeilijke toepassing (TPG 2017, §§ 2.123): toegankelijkheid van de informatie, de opbrengsten en kosten van elke partij vaststellen om tot het nettoresultaat te komen, toewijzing van de indirecte kosten tussen de al dan niet verbonden transacties ….

64. Er bestaan twee soorten PSM:

- De bijdrageanalyse (contribution analysis): de volledige gecombineerde nettowinst van de gecontroleerde transacties wordt verdeeld op een economisch coherente basis, waarbij de relatieve bijdragen van elke verbonden onderneming in aanmerking worden genomen.

- De residuele analyse: er wordt in twee stappen gewerkt :

* aan iedere deelnemer wordt uit de gecombineerde winst eerst een winst toegekend op basis van de uitgeoefende routinefuncties. Hierbij wordt een éénzijdige methode gebruikt;
* nadien wordt het saldo van de gecombineerde winst toegewezen aan de verbonden ondernemingen op basis van een analyse van ieders bijdragen.

65. Het is de reële winst, d.i. de winst die effectief gerealiseerd is, wordt verdeeld indien de verbonden ondernemingen gezamenlijk de economisch belangrijke risico's dragen of de economisch belangrijke risico's worden afzonderlijk gedragen door de verbonden ondernemingen maar de risico's zijn zo nauw verbonden dat de uitwerking van een risico de volledige transactie beïnvloedt. In andere gevallen zou een verdeling van de te verwachte winst passender zijn.

66. Er bestaan voor de winstverdeling geen echte lijsten van criteria die optimale verdeelsleutels definiëren (TPG 2017, §§ 2.166 - 2.168).

67. De verdeelsleutels dienen wel:

- gebaseerd te zijn op objectieve gegevens;

- verifieerbaar te zijn en

- gestaafd door vergelijkbare gegevens, interne gegevens of beide samen.

Aandachtspunten voor alle methodes

68. Gebudgetteerde kosten versus reële kosten

- De prijzen worden in het algemeen voorafgaandelijk bepaald op basis van gebudgetteerde kosten.

- De administratie zal toezien op de impact van het gebruik van de gebudgetteerde kosten op de transactie, op de politiek van afstemming met de werkelijke kosten, alsmede op de blijvende afwijking van deze gebudgetteerde kosten met de werkelijke kosten en de consistentie doorheen de tijd van de keuze van het type kosten (gebudgetteerd of daadwerkelijk). Aanpassingen zijn mogelijk indien de werkelijke kosten in verband met de transacties zonder enige economische reden abnormaal afwijken van de gebudgetteerde kosten of indien het gebruik van de gebudgetteerde kosten niet leidt tot een overeenstemming van de kostenbasis met een marktconforme kostenbasis.

## Hoofdstuk III: De vergelijkbaarheidsanalyse
INLEIDING

69. Het onderzoek naar de vergelijkbaarheid van transacties wordt de vergelijkbaarheidsanalyse genoemd. De vergelijkbaarheidsanalyse is van belang voor alle verrekenprijsmethoden die gebruikt worden om te beoordelen of gelieerde transacties in overeenstemming zijn met het arm's length beginsel en dus markconform zijn. Zij vormt de basis voor iedere onderbouwing van de gehanteerde verrekenprijzen.

70. Vergelijkbaar zijn betekent dat er geen verschillen bestaan die de onderzochte voorwaarde (prijs, winstmarge, …) essentieel kunnen beïnvloeden of dat de invloed van eventuele verschillen kan worden weggewerkt mits voldoende nauwkeurige aanpassingen door te voeren.

VERLOOP VAN EEN VERGELIJKBAARHEIDSANALYSE

71. Na de analyse van de functies, de gedragen risico's en de aangewende activa van de bij de transacties betrokken partijen (cfr. bespreking onder hoofdstuk I van deze circulaire) is de zoektocht naar betrouwbare vergelijkingspunten ('comparables') de volgende stap bij het vinden van de arm's length prijs.

72. De TPG 2017 beschrijven in hoofdstuk III (rubriek A.1) hoe een dergelijk proces kan verlopen aan de hand van 9 stappen. Echter, eender welk ander proces dat kan leiden tot de identificatie van betrouwbare vergelijkingspunten, kan worden aanvaard. De nadruk ligt eerder op de betrouwbaarheid van het resultaat van het vergelijkbaarheidsonderzoek dan op het te volgen proces (TPG 2017, § 3.4).

73. Overzicht van het verloop van een vergelijkbaarheidsanalyse:

Stap 1

Bepalen van de periode van analyse

Stap 2

Algemene analyse van de omstandigheden van de belastingplichtige

Stap 3

Analyse van de gelieerde transactie(s) gebaseerd op de functionele analyse om te beoordelen wie de te testen partij zal zijn, welke verrekenprijsmethode passend is, welke financiële indicator daarbij hoort (in het geval van een transactionele winstmethode) en welke vergelijkbaarheidsfactoren in de analyse betrokken moeten worden

Stap 4

Beoordeling van mogelijk bestaande interne comparables

Stap 5

Bepaling van de aanwezige informatie met betrekking tot externe comparables met beoordeling van hun relatieve betrouwbaarheid

Stap 6

Keuze van de meest passende verrekenprijsmethode en de bepaling van de relevante financiële indicator

Stap 7

Identificatie van de potentiële comparables, rekening houdend met de factoren die reeds in stap 3 zijn bepaald en in overeenstemming met de vergelijkbaarheidsfactoren zoals deze zijn opgenomen in TPG 2017, § 1.38 – 1.63

Stap 8

Bepaling van passende comparability adjustments indien noodzakelijk

Stap 9

Interpretatie en gebruik van de verzamelde gegevens ter bepaling van de passende arm's-lengthvergoeding

74. Het proces van een vergelijkbaarheidsonderzoek wordt hierna beknopt besproken met telkens een verwijzing naar de richtlijnen die de OESO hieromtrent heeft verstrekt.

Stap 1. Bepalen van de periode voor het vergelijkbaarheidsonderzoek (TPG 2017, § 3.74 - 3.79)

75. Bij de analyse van de prijzen dienen alle relevante feiten en omstandigheden, die op het moment van het bepalen van de prijs bekend zijn, te worden meegenomen.

76. Om een beter beeld te krijgen van de omstandigheden waarin een transactie plaatsvond, kan het aangewezen zijn om meerdere jaren in beschouwing te nemen wanneer dit een meerwaarde betekent voor de verrekenprijsanalyse.

77. Het in aanmerking nemen van meerdere jaren kan scheeftrekkingen milderen ingevolge verschillen in economische, markt- of ondernemingsomstandigheden. Zodoende kunnen verschillen inzake markt- en productcycli worden genivelleerd wat leidt tot een betere vergelijkbaarheid. Hoeveel jaren uiteindelijk moeten worden in aanmerking genomen, hangt af van de feiten en omstandigheden eigen aan elk geval. De specifieke kenmerken van de sector waarin de belastingplichtige actief is kan eveneens een invloed hebben op de bepaling van de tijdshorizon die wordt in aanmerking genomen.

78. De administratie verkiest dat minstens 3 jaren worden meegenomen in de analyse van de vergelijkingspunten. Bij de te testen partij daarentegen worden de gegevens beperkt tot die van de transactie die wordt onderzocht voor een welbepaald jaar.

79. Inzake het gebruik van informatie van jaren die vallen na het jaar waarin de transactie heeft plaatsgevonden kan worden verwezen naar TPG 2017, § 3.74. Deze informatie kan bijvoorbeeld relevant zijn voor de analyse van de werkelijke voorwaarden en de afspraken die gelden tussen partijen in het kader van een nauwkeurige afbakening van de transactie die wordt onderzocht.

Stap 2. Brede analyse van de omstandigheden waaronder de belastingplichtige zijn activiteiten voert (TPG 2017, § 3.7)

80. In deze stap worden de industrie, de concurrentie en de wetgevende factoren die de context bepalen waarbinnen de belastingplichtige zijn bedrijvigheid voert, geanalyseerd.

81. De prijzen verschillen van markt tot markt, zelfs voor dezelfde goederen en diensten.

82. Om transacties te vergelijken kan het o.m. noodzakelijk zijn de volgende economische omstandigheden te analyseren:

- geografische ligging;

- omvang van de markt;

- concurrentie, omvang en belang van concurrenten;

- beschikbaarheid van vervangende goederen en diensten;

- niveaus van vraag en aanbod;

- koopkracht van de consument;

- overheidsvoorschriften en

- productiekosten (bv. kosten van lokale arbeidskrachten en grondstoffen).

83. Aanvullend kan worden verwezen naar de bespreking van de vergelijkbaarheidsindicatoren en de behandeling van locatievoordelen ('location savings') in het hoofdstuk I van deze circulaire.

Stap 3: Analyse van de gelieerde transactie(s) (TPG 2017, § 3.8 - 3.17)

84. Het is bij de analyse van belang om de economisch relevante factoren van de commerciële en financiële relaties tussen de verbonden ondernemingen te onderzoeken en de relevante voorwaarden en omstandigheden in kaart te brengen, om op deze wijze de werkelijk aangegane transactie te bepalen die uiteindelijk moet worden vergeleken met de transacties tussen niet-verbonden ondernemingen. Alvorens te vergelijken moet duidelijk worden afgebakend wat de transactie als zodanig precies behelst.

85. Dit proces wordt in OESO-terminologie de 'accurate delineation of the actual transaction' genoemd.

86. De verbonden onderneming met de minst complexe functies in de te onderzoeken transactie zal in het overgrote deel van de gevallen worden weerhouden als de te testen partij (TPG 2017, § 3.18 - 3.19).

Samengestelde of opgesplitste transacties:

87. Bij toepassing van het arm's length principe worden de voorwaarden van een transactie tussen verbonden ondernemingen vergeleken met deze van een gelijkaardige transactie onder vergelijkbare omstandigheden tussen niet verbonden ondernemingen. Echter, derde partijen gegevens zijn vaak beschikbaar op bedrijfsniveau of bedrijfssegment en niet op transactioneel niveau. Afwijkend van het uitgangspunt van een vergelijking op transactieniveau, kan een vergelijking op basis van een combinatie van transacties ook aangewezen zijn, in die gevallen waarbij de strategieën van verbonden ondernemingen afwijken van die van onafhankelijke ondernemingen, mits wordt aangetoond dat het geheel arm's length werd vergoed.

88. Wanneer goederen zeer gelijkaardig of nauw gerelateerd zijn kunnen deze worden beschouwd als één geheel op voorwaarde dat deze verschillende goederen zeer gelijkaardige kenmerken hebben die zich weerspiegelen in productie-, marketing- en verkoopkosten.

89. Gezien samengestelde of opgesplitste transacties een afwijking vormen op het principe van de toepassing van het arm's length principe op transactiebasis, is het aan de belastingplichtige om aan te tonen dat de aangenomen verrekenprijs als arm's length kan worden beschouwd.

Intentionele compensaties:

90. Soms besluiten ondernemingen om niet iedere levering afzonderlijk te vergoeden maar om bijvoorbeeld de waarde van de levering van onderneming A aan verbonden onderneming B te vergelijken met de waarde van de levering van onderneming B aan verbonden onderneming A en slechts het verschil tussen deze respectievelijke waarden te vereffenen. In de TPG 2017 wordt dan gesproken van intentionele compensatieregelingen (TPG 2017, § 3.13 e.v., 'intentional set-offs').

91. Het bestaan van een compensatieregeling neemt niet weg dat elk van de transacties op zich moet gebeuren tegen marktconforme voorwaarden.

Stap 4: Beoordeling van de bestaande interne vergelijkingspunten (TPG 2017, § 3.27 - 3.28)

92. Een goede bron van vergelijkingspunten zal in sommige gevallen binnen de multinationale groep van ondernemingen zelf te vinden zijn. Een grote multinationale groep zal contracten en handelsrelaties hebben met vele klanten, leveranciers, aannemers, enz. De prijzen, voorwaarden en condities van deze transacties met onafhankelijke ondernemingen kunnen worden vergeleken met de prijzen, voorwaarden en condities van gelijkaardige transacties met verbonden ondernemingen.

93. Interne vergelijkingspunten moeten eveneens voldoen aan de 5 vergelijkbaarheidsfactoren zoals besproken in hoofdstuk I van deze circulaire.

Stap 5: Externe vergelijkingspunten en hun bronnen (TPG 2017, § 3.29 - 3.39)

94. Daar waar voor interne vergelijkingspunten de informatie aanwezig is binnen de onderzochte entiteit of binnen de betreffende multinationale groep, dient voor de externe vergelijkingspunten te worden gezocht in voor het publiek toegankelijke gegevens of in commerciële databanken.

95. Bij het gebruik van commerciële databanken dient de kwaliteit van de vergelijkingspunten voorop te staan en niet de kwantiteit. Het is dan ook aangewezen om bij het gebruik ervan de hieruit voorvloeiende informatie vervolgens te verfijnen door deze te testen aan andere publiek beschikbare informatie (zoals bijvoorbeeld informatie opgenomen in de jaarverslagen en op de website van de potentiële vergelijkingspunten).

96. Het identificatieproces van vergelijkbare transacties van derden moet transparant, systematisch en verifieerbaar (6) zijn.

(6) EU Joint Transfer Pricing Forum, Report on the use of comparables in the EU, october 2016 JTPF link

Stap 6: Selectie van de meest geschikte verrekenprijsmethode (TPG 2017, § 3.20 - 3.23)

97. Deze stap omvat het identificeren van de meest betrouwbare verrekenprijsmethode voor het vaststellen of het testen van de arm's length voorwaarden. Hoewel de keuze van de meest geschikte methode, om uitvoerbaar te zijn, in de eerste plaats moet afhangen van de afbakening van de te testen transactie (zoals hierboven besproken onder stap 3), moet ook rekening worden gehouden met de beschikbaarheid van potentiële vergelijkingspunten die nodig zijn om de gekozen methode te kunnen toepassen.

98. Zie voor een uitvoerige bespreking van de verrekenprijsmethoden hoofdstuk II van deze circulaire.

Stap 7: Selecteren en verwerpen van potentiële vergelijkbare bedrijven (TPG 2017, § 3.40 - 3.46)

Algemeen

99. TPG 2017, § 3.40 - 3.42 vermelden 2 benaderingen om potentieel vergelijkbare transacties te identificeren:

- De additieve benadering

100. Onder de additieve methode wordt door de onderneming zelf een lijst opgesteld van mogelijke derde partijen in potentieel vergelijkbare transacties. Vervolgens wordt informatie verzameld over die transacties om te kunnen analyseren of deze transacties vergelijkbaar zijn. Vertrekkend van deze vergelijkingspunten wordt dan een marktconforme vergoeding bepaald.

- De deductieve benadering

101. Hierbij is het vertrekpunt een uitgebreide lijst van potentieel vergelijkbare partijen die bij voorkeur in dezelfde sector actief zijn en een vergelijkbare functie lijken te verrichten door gebruik te maken van een (commerciële) databank.

102. Het kan voorkomen dat op basis van de functionele analyse en op basis van de duidelijke afbakening van de gecontroleerde transactie er geen potentiële interne vergelijkingspunten kunnen worden geïdentificeerd. In dat geval moeten externe vergelijkingspunten in aanmerking worden genomen en geïdentificeerd. Afhankelijk van de feiten en omstandigheden van het geval en van de vergelijkbaarheidsfactoren die van invloed zijn op de potentiële vergelijkingspunten, kunnen externe vergelijkingspunten worden gezocht bij binnenlandse en/of buitenlandse informatiebronnen.

103. Wanneer onvoldoende vergelijkingspunten kunnen worden gevonden in het land van de te testen partij kan een uitbreiding worden gedaan naar de markten die het nauwst aansluiten bij de thuismarkt mits die markten voldoende vergelijkbaar zijn. De administratie aanvaardt binnen dat kader Pan-Europese studies.

104. Er zouden geen verschillen mogen zijn tussen de markt waar de activiteiten plaatsvinden en de markt waar een vergelijkbare onderneming activiteiten ontplooit die van wezenlijke invloed kunnen zijn op de prijs die tussen onafhankelijke ondernemingen zou worden overeengekomen.

105. De keuze van de belastingplichtige voor het in aanmerking nemen van andere dan de hierboven beoogde landen moet worden verantwoord en onderbouwd.

Verlieslatende ondernemingen

106. De administratie aanvaardt in het kader van limited risk ondernemingen onder de vergelijkingspunten in de range geen ondernemingen met 2 of meer verlieslatende jaren.

107. Hoewel normale business activiteiten kunnen leiden tot een occasioneel verlies dient in dergelijke gevallen te worden nagegaan of de volatiliteit van de exploitatieresultaten bij de vergelijkingspunten te maken heeft met de industrie waarin de onderneming actief is of eerder het gevolg is van een herstructurering in de zin van hoofdstuk 9. In dit laatste geval dient de verwijdering van het vergelijkingspunt te worden overwogen.

Startende ondernemingen

108. Tenzij de te testen partij zelf een startende onderneming is, worden startende ondernemingen niet meegenomen in de set van vergelijkingspunten omdat de data kunnen worden vertekend door specifieke omstandigheden die te maken hebben met de opstart van de activiteiten (bv. opstartverliezen, aanwezigheid van marktpenetratiekosten, ...). De administratie is van mening dat ondernemingen die minder dan 4 jaren geleden werden opgericht buiten beschouwing dienen gelaten te worden.

Diagnostische ratio's

109. Om het selectieproces verder te verfijnen kan worden gebruik gemaakt van kwantitatieve criteria onder de vorm van diagnostische ratio's.

110. Er zijn 2 hoofdredenen die pleiten voor het gebruik van diagnostische ratio's:

- om de betrouwbaarheid in termen van vergelijkbaarheid van de weerhouden vergelijkbare ondernemingen/transacties te verbeteren;

- om het aantal weerhouden potentieel vergelijkbare bedrijven te reduceren tot een beheersbare set met minder bedrijven.

111. Diagnostische ratio's zijn ratio's die zijn gebaseerd op items uit de balans- en resultatenrekening, waarbij wordt nagegaan in welke mate deze van de vergelijkingspunten matchen met deze van de te testen partij. Dergelijke ratio's kunnen vele vormen aannemen zoals bijvoorbeeld:

- immateriële activa over totale activa of vaste activa over totale activa;

- omzet per personeelslid of vaste activa per personeelslid;

- operationele uitgaven over verkopen of CoGS over verkopen;

- voorraad over verkopen of voorraad over totale activa;

- gemiddeld uitstaand klantenkrediet of gemiddeld uitstaand leverancierskrediet.

112. Welke diagnostische ratio('s) uiteindelijk word(t)(en) gebruikt hangt af van verschillende factoren, waaronder de aard van de gevoerde business en de 'value drivers' die kunnen worden geïdentificeerd.

113. Gezien de focus van de vergelijkbaarheidsanalyse ligt op de identificatie van vergelijkbare ondernemingen/transacties eerder dan op het vergelijkbaar maken van ondernemingen gaat de voorkeur naar de toepassing van diagnostische ratio's boven het routinematig doorvoeren van vergelijkbaarheidsaanpassingen aan de weerhouden vergelijkingspunten. Het gebruik van diagnostische ratio's vervangt geenszins de kwalitatieve screening van de uiteindelijk weerhouden vergelijkingspunten.

114. Onder de omstandigheden aangehaald in TPG 2017, § 3.57 kunnen statistische tools de betrouwbaarheid van de analyse uiteindelijk nog verhogen (zie verder onder stap 9 voor de bespreking van het gebruik van de interkwartielrange).

Periodiciteit

115. De voorafgaande uitvoering van de vergelijkbaarheidsanalyse sluit best zo goed mogelijk aan bij het tijdstip waarop de te testen transactie plaatsvindt met het oog op het verhogen van de vergelijkbaarheid. Een jaarlijkse actualisatie van de bekomen resultaten van de oorspronkelijke vergelijkbaarheidsanalyse is aangewezen. De documentatie van de vergelijkbaarheidsanalyse zal regelmatig worden bijgewerkt in het licht van eventuele wijzigingen in de functies, de risico's en de economische omgeving van de onderzochte onderneming. (TPG 2017, § 3.67 – 3.69).

116. De administratie meent dat een herwerking van de oorspronkelijke TP-studie bij voorkeur om de drie jaar gebeurt tenzij de feiten en omstandigheden een snellere herwerking noodzakelijk maken.

117. De selectie van potentiële 'comparables' en met name de keuze van de selectiecriteria is van essentieel belang voor de toepassing van de vergelijkbaarheidsanalyse. De keuze van de selectiecriteria beïnvloedt immers rechtstreeks het resultaat van de vergelijkbaarheidsanalyse.

Stap 8: Aanpassingen om verschillen in vergelijkbaarheid te elimineren (TPG 2017, § 3.47 - 3.54)

118. Materiële verschillen tussen de gelieerde en niet-gelieerde transacties beïnvloeden de vergelijkbaarheid. Teneinde deze negatieve impact op de vergelijkbaarheid te elimineren, kunnen zogenoemde vergelijkbaarheidsaanpassingen ('comparability adjustments') worden aangebracht. De OESO benadrukt dat aanpassingen enkel mogen worden uitgevoerd als ze tot een vergelijkbare 'comparable' leiden (TPG 2017, § 3.52). De enige correcties die dus mogen worden toegepast zijn deze die de vergelijkbaarheid verbeteren.

119. Naarmate het aantal correcties toeneemt, kan echter de betrouwbaarheid van de potentiële 'comparables' verminderen en groeit het risico dat totaal ongeschikte 'comparables' kunstmatig geschikt worden gemaakt.

120. Vergelijkbaarheidsaanpassingen dienen in het bijzonder te worden onderbouwd op de volgende punten:

- de belangrijkheid van het verschil waarvoor een correctie wordt overwogen;

- de kwaliteit van de gegevens die het voorwerp zijn van een correctie;

- de omstandigheden die worden geacht een belangrijke invloed te hebben op de prijs (winst);

- het doel van de correctie;

- de betrouwbaarheid van de voor de correctie gebruikte methode.

121. Vergelijkbaarheidsaanpassingen kunnen doorgaans niet worden gebruikt om belangrijke verschillen te corrigeren inzake activa en risico's gezien deze eerder wijzen op inconsistentie van de gebruikte selectiecriteria en op verschillen in het risico- en functieprofiel met de te testen partij.

122. Vergelijkbaarheidsaanpassingen worden doorgaans toegepast om rekening te houden met verschillen inzake werkkapitaal/bedrijfskapitaal tussen de vergelijkingspunten en de te testen partij.

Stap 9: Het gebruik van een arm's length range (TPG 2017, § 3.55 - 3.66)

Bepalen en toepassen van de range

123. De bepaling van een verrekenprijs is geen exacte wetenschap. Meestal zal niet één waarde bekomen worden, maar zal een range aan waarden bekomen worden waarbinnen de te hanteren verrekenprijs zich zal bevinden.

124. In uitzonderlijke omstandigheden en mits de vergelijkingspunten onderling zeer goed vergelijkbaar zijn en van een evenwaardige hoge kwaliteit kan elk punt van de volledige range een referentie zijn voor een marktconforme verrekenprijs.

125. Een vergelijkbaarheidsonderzoek kan maar betrouwbaar worden uitgevoerd als er voldoende informatie beschikbaar is over vergelijkbare transacties met betrekking tot alle vergelijkbaarheidsfactoren. Na de screening van de vergelijkbaarheidspunten op hun betrouwbaarheid en vergelijkbaarheid kunnen mogelijks toch nog vergelijkbaarheidsproblemen blijven bestaan, die moeilijk te identificeren en/of te kwantificeren zijn. Statistische methoden kunnen hierbij soelaas bieden om de betrouwbaarheid van de vergelijkbaarheidsanalyse te verhogen. De administratie geeft daarom de voorkeur aan de interkwartiele range (IQR) -benadering van de weerhouden vergelijkingspunten zonder hierbij andere statistische methoden, die het risico en de foutenmarge m.b.t. onbekende of moeilijk te kwantificeren vergelijkbaarheidsgebreken minimaliseren, uit te sluiten. De nadruk ligt op het vergroten van de betrouwbaarheid van het vergelijkbaarheidsmateriaal. De administratie zal het resultaat van de geteste partij aanvaarden wanneer het resultaat van de geteste transactie in de IQR valt.

126. Indien het resultaat van de geteste transactie buiten de range (hetzij de volledige range in geval van zeer goede vergelijkingspunten, hetzij de interkwartiele range in de andere gevallen) valt en de belastingplichtige deze afwijking niet gemotiveerd kan verklaren, is een aanpassing nodig. Deze aanpassing dient te gebeuren naar een punt in de range (hetzij de volledige range in geval van zeer goede vergelijkingspunten, hetzij de interkwartiele range in de andere gevallen) dat zo goed mogelijk aansluit bij de feiten en omstandigheden van de geteste transactie. Indien een dergelijk specifiek punt binnen de range (hetzij de volledige range in geval van zeer goede vergelijkingspunten, hetzij de interkwartiele range in de andere gevallen) niet kan worden aangewezen, heeft de administratie de voorkeur om aan te passen naar de mediaan.

## Hoofdstuk IV: Administratieve benaderingen tot het voorkomen en het oplossen van geschillen inzake verrekenprijzen

127. Dit hoofdstuk van de TPG 2017 wordt niet besproken in deze circulaire.

Hier kan verwezen worden naar:

- Circulaire 2018/C/27 van 07.03.2018 met betrekking tot de regels voor geschillenbeslechting in verband met de toepassing van internationale belastingverdragen.

Deze circulaire kan u raadplegen via de volgende link:

Circulaire geschillenbeslechting in verband met de toepassing van internationale belastingverdragen

- FAQ

FAQ Onderling overleg - Advance Pricing Arrangement (APA)

## Hoofdstuk V: Documentatieverplichtingen

128. Dit hoofdstuk van de TPG 2017 wordt niet besproken in deze circulaire.

Hier kan verwezen worden naar:

- de artikelen 321/1 tot 321/7 van het Wetboek Inkomstenbelastingen 1992;

- de circulaire nr. 2017/C/56 van 04.09.2017 betreffende de bijkomende aangifteverplichtingen inzake verrekenprijzen en

- de website van de administratie betreffende BEPS 13:
BEPS 13

## Hoofdstuk VI: Bijzondere overwegingen inzake immateriële activa
INLEIDING

129. In het algemeen zijn de principes van de TPG 2017, hoofdstukken I – III mutatis mutandis van toepassing op transacties van immateriële activa. Zo zal de verrekenprijsanalyse van transacties met betrekking tot immateriële activa beginnen met een analyse van de commerciële en financiële relaties van de betrokken ondernemingen, de onderliggende voorwaarden en de relevante economische omstandigheden opdat de transactie duidelijk kan afgelijnd worden. De functionele analyse zal ook hier rekening houden met de uitgeoefende functies, gedragen risico's en gebruikte activa van de betrokken ondernemingen in verband met de onderzochte transactie(s). Vervolgens zal men een vergelijkbaarheidsstudie dienen uit te voeren teneinde de correcte verrekenprijs te kunnen bepalen van de onderliggende transactie(s). Het kan echter in uitzonderlijke omstandigheden voorkomen dat de transactie(s) genegeerd moet(en) worden.

IDENTIFICATIE VAN IMMATERIËLE ACTIVA

130. Elk land heeft zijn eigen wetgeving om te bepalen wat al dan niet een immaterieel actief is voor fiscale doeleinden en hoe men dit actief behandelt. Gelet op het internationaal karakter van de verrekenprijzen dient men echter een algemene internationale definitie te hanteren om overeenstemming te kunnen hebben omtrent wat vergoed dient te worden.

131. De OESO richtlijnen voor verrekenprijzen hanteren de volgende definitie (TPG 2017, § 6.6):

'Een immaterieel actief is iets dat geen materieel of financieel actief is en dat in eigendom kan aangehouden of gecontroleerd worden voor commerciële doeleinden en waarvan het gebruik of de overdracht aanleiding zou geven tot een vergoeding indien deze transactie had plaatsgevonden tussen onafhankelijke partijen in vergelijkbare omstandigheden.'

132. Er werd uitdrukkelijk geopteerd om niet aan te sluiten bij de boekhoudkundige standaarden die gelden voor immateriële activa. Een immaterieel actief moet bijgevolg niet altijd uitgedrukt zijn in de jaarrekening van de entiteit om een vergoeding te kunnen vragen voor het gebruik of de overdracht ervan. Evenmin moet een immaterieel actief wettelijk beschermd zijn om een vergoeding te kunnen vragen voor het gebruik of de overdracht ervan.

133. Specifieke eigenschappen van de markt (bijvoorbeeld gemiddeld inkomen, de grootte van de afzetmarkt, toegang tot hoogopgeleid personeel, klimaat, enz.) kunnen niet in eigendom aangehouden of gecontroleerd worden en kunnen bijgevolg niet aangemerkt worden als immateriële activa.

134. De OESO richtlijnen bevatten een niet-exhaustieve lijst van voorbeelden van mogelijke immateriële activa (TPG 2017, §§ 6.18-6.31)

EIGENDOM VAN IMMATERIËLE ACTIVA EN DEMPE FUNCTIES

135. Bij transacties waar immateriële activa deel uitmaken zal het belangrijk zijn om naast de identificatie van de juridische eigenaar van de immateriële activa na te gaan welke groepsentiteiten functies uitoefenen, risico's dragen en activa gebruiken met betrekking tot de ontwikkeling, verbetering, behoud, bescherming en gebruik van de immateriële activa (deze begrippen zijn in de praktijk beter gekend onder hun Engelse benamingen ('development, enhancement, maintainance, protection, exploitation' – kortweg 'DEMPE'). De ondernemingen die DEMPE functies uitgeoefend hebben dienen een marktconforme vergoeding te ontvangen voor deze uitgeoefende functies, gedragen risico's en gebruikte activa.

136. Om een correcte verrekenprijsanalyse uit te voeren van een transactie die immateriële activa omvat, kan het volgende stappenplan gebruikt worden (TPG 2017, § 6.34):

- identificatie van de immateriële activa die onderdeel uitmaken van de onderzochte transactie(s) alsook van de daarmee verbonden risico's;

- identificatie van de contractuele afspraken en andere schriftelijke documentatie met speciale aandacht voor de identificatie van de juridische eigenaar van het immaterieel actief;

- identificatie van de partijen die DEMPE-functies uitoefenen;

- de consistentie nagaan tussen de contractuele verplichtingen en het werkelijk gedrag van de partijen;

- de eigenlijke transactie(s) afbakenen met betrekking tot de DEMPE functies, gebaseerd op de onderzochte contractuele verplichtingen, de vastgestelde juridische eigendom en het geobserveerde werkelijk gedrag;

- waar mogelijk de arm's length prijs bepalen voor de onderzochte transactie(s) tenzij, in uitzonderlijke gevallen, de transacties dienen te worden genegeerd.

137. Indien er geen schriftelijke bepalingen bestaan die een bepaalde partij als juridische eigenaar van het onderzochte immaterieel actief aanduiden, dan zal voor verrekenprijsdoeleinden als eigenaar van het immaterieel actief de onderneming aangeduid worden die de voornaamste beslissingen neemt met betrekking tot het gebruik van het actief en die andere partijen het gebruik van het actief kan beperken (TPG 2017, § 6.40).

138. Het kan eveneens voorkomen dat er meer dan één juridische eigenaar kan geïdentificeerd worden. In dat geval zullen de verschillende transacties moeten geïdentificeerd worden tussen deze ondernemingen die betrekking hebben op de uitgeoefende functies, gedragen risico's en gebruikte activa met betrekking tot de DEMPE functies.

139. Bij het onderzoeken van de uitgeoefende functies dient men zowel na te gaan welke entiteit die functies daadwerkelijk uitoefent en welke partij een controle daarover uitoefent. Een entiteit kan bijvoorbeeld verder onderzoek en ontwikkeling voeren in verband met het verbeteren van een bepaald immaterieel actief, maar een andere groepsentiteit kan de controle uitoefenen over dit onderzoek (o.a. door belangrijke beslissingen te nemen in verband met dit onderzoek). Het spreekt vanzelf dat beide entiteiten een marktconforme vergoeding dienen te ontvangen voor hun uitgeoefende functies.

140. Inzake gedragen risico's kan verwezen worden naar de principes van hoofdstuk I. Indien een groepsentiteit bepaalde belangrijke risico's op zich neemt in verband met de DEMPE functies, dan zal deze groepsentiteit recht hebben op (een deel van) de actuele inkomsten uit dat immaterieel actief.

141. Om een correcte vergoeding van de bijgedragen activa te bepalen, zal men eveneens naar de achterliggende functies en gedragen risico's dienen te kijken. In het bijzonder dient er aandacht besteed te worden aan het bepalen van een marktconforme vergoeding van het kapitaal. Wanneer een groepsentiteit kapitaal bijdraagt voor de ontwikkeling van een immaterieel actief, dient men o.a. na te gaan of deze groepsentiteit de daarmee verbonden financiële risico's controleert en of deze groepsentiteit eveneens een controle uitoefent over de ontwikkeling van het immaterieel actief. In het eerste geval zal de groepsentiteit slechts een financiële vergoeding ontvangen voor het bijgedragen kapitaal, in het tweede geval dient eveneens de vergoeding voor de uitgeoefende functies bepaald te worden. Indien de groepsentiteit geen enkele controlefunctie over de ontwikkeling van het immaterieel actief of over de financiële risico's uitoefent, dan zal de groepsentiteit slechts recht hebben op ten hoogste een risicovrije premie voor het bijgedragen kapitaal.

142. In het algemeen kan gesteld worden dat indien de juridische eigenaar alle DEMPE functies uitoefent of daarover controle uitoefent, alle risico's verbonden met DEMPE functies draagt of controleert, en alsook de financiële capaciteit heeft deze risico's te dragen, en alle activa bijdraagt aan deze DEMPE functies, deze recht heeft op alle inkomsten die voortvloeien uit het gebruik van die immateriële activa.

BEPALEN VAN DE VERREKENPRIJS IN TRANSACTIES MET IMMATERIËLE ACTIVA

143. Voor het bepalen van een verrekenprijs van een transactie waar een immaterieel actief deel van uitmaakt kan verwezen worden naar de principes van hoofdstukken I – III. Het kan echter moeilijk zijn om deze principes toe te passen omwille van volgende redenen:

- een gebrek aan vergelijkbaarheid tussen de geïdentificeerde transacties en transacties tussen onafhankelijke partijen;

- een gebrek aan vergelijkbaarheid tussen verschillende immateriële activa;

- de juridische eigendom of het gebruik van het immaterieel actief door verschillende entiteiten;

- de uitdagingen om de impact die een immaterieel actief heeft op de gehele transactie te onderzoeken;

- verschillende groepsentiteiten kunnen functies uitoefenen, risico's dragen of activa bijdragen met betrekking tot de DEMPE functies;

- bovenvermelde functies, risico's en activa kunnen bijgedragen zijn op een ander tijdstip dan het moment waarop de onderzochte transactie(s) plaatsvind(t)(en).

144. Wanneer men een vergelijkbaarheidsstudie uitvoert met betrekking tot immateriële activa dient rekening gehouden te worden met de specifieke karakteristieken van de activa. Een aantal zaken waar aandacht dient aan besteed te worden zijn onder andere:

- exclusiviteit;

- omvang en duur van een eventuele juridische bescherming;

- geografisch bereik;

- nuttige levensduur;

- ontwikkelingsfase;

- rechten op verbeteringen, herzieningen en updates;

- verwachte toekomstige opbrengsten.

145. Het algemene principe dat de selectie van de meest geschikte verrekenprijsmethode afhankelijk is van de functionele analyse is ook van toepassing bij transacties met immateriële activa. Desalniettemin zullen, afhankelijk van de feiten en omstandigheden, bepaalde verrekenprijsmethodes meer aangewezen zijn dan andere. Zo zal het in het algemeen niet gepast zijn om de CPM toe te passen aangezien er niet altijd een correlatie bestaat tussen de kosten en de opbrengsten van een immaterieel actief. De CPM kan echter wel aangewezen zijn voor het vergoeden van puur routinematige bijdragen tot het immaterieel actief, bijvoorbeeld, wanneer een boekhoudsoftware ontwikkeld werd voor puur interne doeleinden.

146. De verrekenprijsmethodes die meer aangewezen zijn om een vergoeding van een immaterieel actief te bepalen zijn de CUP of de PSM. Om de marktconforme prijs te bepalen kan eventueel gebruik gemaakt worden van waarderingstechnieken.

ENKELE AANDACHTSPUNTEN BIJ HET GEBRUIK VAN WAARDERINGSTECHNIEKEN

147. Er zijn verschillende waarderingstechnieken beschikbaar, elkeen met hun eigen voor- en nadelen. Hoewel de OESO richtlijnen voornamelijk de discounted cash flow techniek beschrijft, worden andere technieken eveneens aanvaard (bijvoorbeeld de relief from royalty method, residual value method, premium profit method, …). Voor de administratie is het van uitermate belang dat de belastingplichtige in zijn verrekenprijsdocumentatie deze voor- en nadelen aangeeft en de redenen waarom hij juist voor een bepaalde techniek heeft gekozen. Het kan tevens nuttig zijn, maar het is niet vereist, om verschillende technieken te gebruiken teneinde de verrekenprijs te onderbouwen.

148. Bij het gebruik van waarderingstechnieken zijn er in ieder geval een aantal zaken waarmee men zeker rekening dient te houden (afhankelijk van de techniek die gebruikt wordt):

- de accuraatheid van financiële voorspellingen;

- de verwachte groei;

- de discontovoeten;

- nuttige levensduur en terminale waarde;

- royaltypercentages;

- routinematige opbrengsten;

- belastingen.

-

149. Tenslotte is het belangrijk te benadrukken dat waarderingstechnieken dikwijls voor andere redenen worden gehanteerd dan voor verrekenprijsdoeleinden. In dergelijk geval mag een belastingplichtige met de nodige omzichtigheid van deze waardering gebruik maken als basis voor de waardering van het immaterieel actief voor verrekenprijzen (zie o.m. TPG 2017, § 6.155).

DE VERREKENPRIJS WANNEER DE WAARDERING VAN HET IMMATERIEEL ACTIEF OP HET TIJDSTIP VAN DE TRANSACTIE HOOGST ONZEKER IS

150. Wanneer de waarde van het immaterieel actief hoogst onzeker is op het tijdstip van de transactie zullen de betrokken partijen in bepaalde omstandigheden een aantal zekerheden inbouwen om zich te beschermen tegen bepaalde ontwikkelingen die zich op een later tijdstip kunnen voordoen, maar die op het tijdstip van de transactie moeilijk te voorspellen zijn.

151. Voorbeelden van de manier waarop onafhankelijke bedrijven zich proberen in te dekken tegen deze onzekerheden zijn onder andere het voorzien van de mogelijkheid om prijsaanpassingen binnen het contract door te voeren, contracten van kortere duur afsluiten, een andere betalingsstructuur aannemen of heronderhandelingsclausules inbouwen.

152. In het bepalen van een verrekenprijs voor transacties waarvan moeilijk te waarderen immateriële activa deel uitmaken zal men deze onzekere factoren mee in rekening dienen te brengen en afhankelijk van de feiten en de omstandigheden bepaalde clausules dienen in te bouwen.

MOEILIJK TE WAARDEREN IMMATERIËLE ACTIVA

153. Moeilijk te waarderen immateriële activa zijn immateriële activa waarvoor (i) geen betrouwbare vergelijkingspunten bestaan en (ii) de voorspelde financiële kasstromen of de assumpties waarop de waardering van het actief berust hoogst onzeker waren op het moment van de transactie, waardoor het zeer moeilijk is om het uiteindelijke succes van het immaterieel actief in te schatten op het moment van de transactie (TPG 2017, § 6.189). Voorbeelden van dergelijke transacties zijn onder andere (TPG 2017, § 6.190):

- een immaterieel dat slechts gedeeltelijk is ontwikkeld op het moment van transactie;

- er wordt verwacht dat het immaterieel actief slechts meerdere jaren na de transactie commercieel gebruikt zal worden;

- het immaterieel actief draagt bij tot de ontwikkeling van een ander immaterieel actief dat voldoet aan de definitie van moeilijk te waarderen immateriële activa;

- het immaterieel actief zal waarschijnlijk gebruikt worden op een manier die innovatief is ten tijde van de transactie en de afwezigheid van eerdere ervaringen inzake ontwikkeling en gebruik van vergelijkbare immateriële activa maken de voorspellingen hoogst onzeker;

- het moeilijk te waarderen immaterieel actief werd overgebracht voor een éénmalige betaling;

- het immaterieel actief wordt gebruikt in een kostenbijdrageregeling.

154. Bij het vaststellen van een verrekenprijs is er steeds sprake van informatie-asymmetrieën tussen de belastingplichtige en de belastingadministratie. De belastingplichtige beschikt immers over meer informatie omtrent de gecontroleerde transacties dan de belastingadministratie. Dit heeft onder andere tot gevolg dat het vaststellen van een verrekenprijs lang kan duren en zeer informatie vergarend is.

155. Hoewel dit voor iedere vaststelling van een verrekenprijs geldt, kunnen deze informatie-asymmetrieën zeer belangrijke gevolgen hebben voor het bepalen van de verrekenprijs met betrekking tot immateriële activa. Zo is het van uitermate belang voor de belastingplichtige om in te schatten welke latere ontwikkelingen of gebeurtenissen in verband met de immateriële activa relevant zijn voor het bepalen van de verrekenprijs en in welke mate deze ontwikkelingen of gebeurtenissen correct kunnen worden ingeschat of worden voorzien door de belastingplichtige rekening houdende met de relevante feiten en omstandigheden. Deze inschatting zal een zeer specifieke kennis, expertise of inzicht vereisen van de immateriële activa alsook van de omgeving waarbinnen deze zich voortdoen. Dit kan een kennis, expertise of inzicht zijn die op het moment van de transactie niet aanwezig is bij de belastingadministratie.

156. Omwille van deze redenen kan de belastingadministratie de ex post resultaten van het gebruik van een immaterieel actief aanwenden als een bewijs door feitelijke vermoedens om na te gaan of de ex ante prijsafspraken correct werden toegepast door de belastingplichtige ten tijde van de transactie en of de latere ontwikkelingen of gebeurtenissen die hebben geleid tot de afwijkende ex post resultaten voldoende konden worden ingeschat door de belastingplichtige en om de betrouwbaarheid na te gaan van de assumpties die werden aangegaan ten tijde van de transactie om de verrekenprijs van het immaterieel actief te rechtvaardigen.

157. Wanneer de belastingadministratie op basis van dit bewijs door feitelijke vermoedens aantoont dat de bij de overdracht aangenomen assumpties niet betrouwbaar zijn of latere ontwikkelingen of gebeurtenissen die geleid hebben tot afwijkende resultaten door de belastingplichtige konden worden voorzien, maar niet werden ingebouwd in de ex ante prijsafspraken, dan kan de belastingadministratie een prijsaanpassing doorvoeren of een andere betalingsstructuur opleggen rekening houdende met de assumpties die hadden moeten worden aangenomen en/of latere ontwikkelingen of gebeurtenissen die hadden voorzien kunnen worden. Dit zal dan gelden als een weerlegbaar vermoeden. Deze aanpassingen mogen dan weer niet gebeuren enkel en alleen op basis van de ex post resultaten, de ex ante prijsafspraken dienen aangepast te worden door de betrouwbare assumpties of latere voorzienbare ontwikkelingen in rekening te brengen.

158. Een verrekenprijsaanpassing van de overdracht van een immaterieel actief kan bijvoorbeeld worden doorgevoerd wanneer door de belastingplichtige werd aangenomen dat verder onderzoek en ontwikkeling van het immaterieel actief nog 10 jaar zou duren, terwijl in de praktijk dergelijke verdere onderzoeken slechts 3 jaar duren en dit wordt bevestigd in de ex post resultaten. Een andere mogelijkheid zou kunnen zijn dat de prijsafspraken tussen onafhankelijke partijen een tussentijdse betaling voorzien wanneer een bepaalde fase van het onderzoek afgerond werd.

159. Wanneer de belastingadministratie daarentegen vaststelt dat de gemaakte assumpties en de latere ontwikkelingen en gebeurtenissen correct werden ingeschat, dan zal de belastingadministratie geen prijsaanpassingen of wijzigingen aanbrengen aan de betaalstructuur louter en alleen omwille van het feit dat de ex post resultaten verschillen van de ex ante prijsafspraken.

160. De hierboven beschreven benadering zal niet worden toegepast indien één van de volgende situaties kan worden ingeroepen:

a. De belastingplichtige voorziet de belastingadministratie van:

i. details van de op het moment van de transactie gebruikte geschatte voorspellingen om de ex ante prijsafspraken te bepalen, inclusief hoe de verschillende geïdentificeerde risico's werden ingecalculeerd in de verrekenprijs en hoe verschillende voorzienbare gebeurtenissen en andere risico's, samen met de waarschijnlijkheid dat deze zich voortdoen in rekening werden gebracht, en ii. betrouwbaar bewijs dat alle belangrijke afwijkingen tussen deze voorspellingen en ex post resultaten het resultaat zijn van (i) onvoorzienbare ontwikkelingen of gebeurtenissen na de bepaling van de verrekenprijs of (ii) de realisatie van de waarschijnlijkheid van voorzienbare gebeurtenissen en andere risico's zonder dat deze waarschijnlijkheid sterk werd overschat of onderschat.

b. De transactie maakt het voorwerp uit van een in werking zijnde bilaterale of multilaterale ruling tussen de landen van de koper en verkoper.

c. De belangrijke afwijkingen waarvan sprake in a.ii. hebben niet tot effect dat de waarde van het moeilijk te waarderen immaterieel actief meer dan 20 % afwijkt van de waarde die bepaald werd ten tijde van de transactie.

d. Een commercialisatieperiode van 5 jaar is verlopen nadat het moeilijk te waarderen immaterieel actief voor het eerst opbrengsten met onafhankelijke partijen heeft gegenereerd voor de overnemer en gedurende die 5 jaren werd er geen belangrijke afwijking van meer dan 20 % in de ex ante voorspellingen of ex post uitkomsten vastgesteld.

161. De administratie streeft ernaar om dergelijke transacties zo snel mogelijk op te sporen.

162. In voorkomend geval zal de Belgische administratie toegang geven tot de regeling voor onderling overleg zoals bepaald in het overeenkomstig dubbelbelastingverdrag, of , in voorkomend geval, zoals bepaald door het Arbitrageverdrag (Verdrag 90/436/EEG) of de wet van 02.05.2019 tot omzetting van de richtlijn (EU) 2017/1852 van de raad van 10.10.2017 betreffende mechanismen ter beslechting van belastinggeschillen in de Europese Unie.

163. Indien een buitenlandse belastingadministratie een aanpassing doet op basis van deze regeling zal de Belgische belastingadministratie, teneinde dubbele belasting te voorkomen een compenserende aanpassing doorvoeren indien de aanpassing van de buitenlandse belastingadministratie correct en gegrond blijkt.

## Hoofdstuk VII: Bijzondere overwegingen inzake intragroepsdiensten
INLEIDING

164. Bijna alle multinationale groepen van ondernemingen verlenen aan hun leden een brede waaier van diensten, meer bepaald administratieve, technische, financiële of commerciële diensten zoals beheer-, coördinatie- en controlediensten. De uitgaven voor het verstrekken van deze diensten kunnen initieel worden gedragen door de moedermaatschappij of door één of meerdere speciaal aangewezen leden van de groep (een dienstencentrum van de groep) of door andere leden van de groep.

165. De TPG 2017 hebben tot doel te verzekeren dat de diensten naar behoren worden geïdentificeerd en dat de kosten die daarmee gepaard gaan op passende wijze worden toegewezen binnen een multinationale groep van ondernemingen in overeenstemming met het arm's length-beginsel.

166. Twee aandachtspunten zijn van belang bij de analyse van de vaststelling van de verrekenprijzen van intragroepsdiensten:

- is er effectief sprake van intragroepsdiensten en

- is de toegepaste prijs marktconform.

INTRAGROEPSDIENSTEN

167. Voor de omschrijving van een intragroepsdienst wordt verwezen naar TPG 2017, § 7.6 – 7.18. Om te antwoorden op de vraag of er een intragroepsdienst werd geleverd wanneer een activiteit wordt uitgeoefend ten gunste van een of meerdere leden van de groep door een ander lid van de groep, dient men zich af te vragen of de activiteit van economisch of commercieel belang is en of, onder vergelijkbare omstandigheden, een onafhankelijke onderneming bereid zou zijn geweest om een onafhankelijke onderneming te betalen voor de uitvoering van de betrokken activiteit ofwel dat zij de betrokken activiteit intern zou hebben uitgevoerd.

168. Indien de activiteit niet behoort tot de activiteiten waarvoor een onafhankelijke onderneming bereid zou zijn geweest te betalen of die zij zelf zou hebben uitgevoerd, dan moet die activiteit in principe niet worden beschouwd als een intragroepsdienst conform het arm's length-beginsel. Dit geldt meer in het bijzonder voor de activiteiten die worden uitgeoefend in de hoedanigheid van aandeelhouder.

169. Activiteiten die in de hoedanigheid van aandeelhouder worden uitgeoefend (TPG 2017, § 7.9 - 7.10), worden gewoonlijk uitgeoefend ten gevolge van de deelname door de dienstverlener aan het kapitaal van een of meerdere leden van de groep.

170. Indien activiteiten die worden beschouwd als aandeelhoudersactiviteiten door een vennootschap van de groep worden uitgeoefend om andere redenen dan haar deelname aan het kapitaal van een of meerdere leden van de groep, moet de betrokken vennootschap worden geacht een dienst te leveren aan de moedermaatschappij of de holdingvennootschap.

171. De kosten m.b.t. aandeelhoudersactiviteiten moeten worden gedragen op het niveau van de aandeelhouder(s).

172. Het onderzoek van de activiteiten die een lid van een groep uitoefent ten voordele van de andere entiteiten van de groep moet eveneens uitmaken of deze diensten eventueel een dubbel gebruik vertegenwoordigen en, desgevallend, de reden van dit dubbel gebruik vaststellen (TPG 2017, § 7.11).

173. Diensten van dezelfde aard kunnen van bijkomende of aanvullende aard zijn en maken in dergelijk geval geen dubbel gebruik uit.

174. Ten gevolge van een herstructurering van de activiteiten van een groep kunnen bepaalde activiteiten tijdelijk dubbel gebruik uitmaken.

VERGOEDING VOLGENS HET ARM'S LENGTH-BEGINSEL

Al dan niet rechtstreekse doorrekening

175. Bij het vaststellen van de modaliteiten voor doorrekening van de intragroepsdiensten moet men ernaar streven passende tarieven te hanteren die worden gerechtvaardigd door een identificeerbaar en voorzienbaar voordeel.

176 De rechtstreekse doorrekening van een specifieke dienst draagt de voorkeur weg omdat deze het verband aantoont tussen de geleverde dienst en de betaling. Dergelijke doorrekening is met name aangewezen indien de onderneming specifieke diensten levert, niet alleen aan verbonden ondernemingen maar ook aan onafhankelijke ondernemingen (TPG 2017, § 7.21 - 7.22).

177. Aangezien de rechtstreekse doorrekening moeilijk toepasbaar kan zijn binnen multinationale ondernemingen, kan gebruik worden gemaakt van methodes van onrechtstreekse aanrekening op basis van een verdeling van de kosten. Dergelijke onrechtstreekse doorrekening heeft dikwijls tot gevolg dat gebruik moet worden gemaakt van ramingen of benaderingen, inzonderheid wat betreft het aandeel van de waarde van de diensten voor de betrokken ondernemingen (TPG 2017, § 7.23 – 7.26).

178. Bijvoorbeeld bij het verstrekken van diensten inzake bezoldigingen van loontrekkenden kan de doorrekening gebeuren op basis van het aantal loontrekkenden dan wel op basis van omzet, terwijl diensten inzake assistentie voor IT doorgerekend worden o.b.v. het aantal computers.

179. Om de impact van de ramingen te beperken dient men oog te hebben voor de waarde van de aan de begunstigde geleverde diensten en voor de commerciële kenmerken van de transactie; de methode moet gebaseerd zijn op een rationele verdeelsleutel (bv. de omzet of het aantal werknemers) en moet leiden tot een resultaat dat overeenstemt met hetgeen onafhankelijke partijen bereid zouden zijn geweest te aanvaarden.

Methode

180. De methode die moet worden gebruikt om de arm's length prijs te bepalen die toepasselijk is op intragroepsdiensten, moet worden vastgesteld overeenkomstig de TPG 2017, hoofdstukken I - III. In de praktijk leidt de toepassing van deze richtlijnen ertoe dat meestal gebruik wordt gemaakt van een op kosten gebaseerde methode.

181. De administratie is van mening dat bij toepassing van de CPM of de TNMM op basis van de kosten er rekening dient te worden gehouden met de volgende elementen:

- wanneer een onderneming enkel optreedt als agent of tussenpersoon in het kader van een dienstverrichting, dient de marge toegepast te worden op de kosten die inherent zijn aan de uitoefening van de functies van agent en niet op de diensten zelf in de mate waarin de leden van de groep deze uitgaven rechtstreeks zouden hebben gedragen indien ze onafhankelijk waren geweest (TPG 2017, § 7.34);

- de rentabiliteit van een dienstverlener die beperkte risico's op zich neemt zou in principe gewaarborgd moeten zijn en zou bijgevolg niet de negatieve gevolgen mogen ondergaan van financiële of niet-recurrente kosten die niet in overeenstemming zijn met het functioneel profiel van de dienstenverstrekker.

INTRAGROEPSDIENSTEN MET BEPERKTE TOEGEVOEGDE WAARDE

Definitie

182. Voor de toepassing van hieronder uiteengezette vereenvoudigde benadering worden als intragroepsdiensten met beperkte toegevoegde waarde aangemerkt de diensten geleverd door een of meerdere leden van een multinationale groep van ondernemingen leveren ten behoeve van een of meerdere andere leden van de groep en die:

- betrekking hebben op een ondersteunende functie, i.e. geen deel uitmaken van de kernactiviteit van de multinationale groep van ondernemingen;

- geen gebruik vereisen van unieke en waardevolle immateriële activa en geen aanleiding geven tot de creatie van dergelijke activa;

- er niet toe leiden dat de leverancier van diensten wezenlijke of belangrijke risico's op zich dient te nemen en evenmin aanleiding geven tot het ontstaan van een belangrijk risico voor diezelfde dienstverlener.

183. Vormen inzonderheid geen intragroepsdiensten met beperkte toegevoegde waarde voor de toepassing van de vereenvoudigde benadering (TPG 2017, § 7.47):

- diensten die de kernactiviteit van de multinationale groep van ondernemingen vormen;

- onderzoek en ontwikkeling;

- fabricage en productie;

- aankoopactiviteiten met betrekking tot de grondstoffen of andere materialen die worden gebruikt in het fabricage- of productieproces;

- verkoop, marketing en distributie;

- financiële transacties;

- extractie, exploratie of bewerking van natuurlijke bronnen;

- verzekering en herverzekering;

- diensten van algemene leiding van een onderneming.

184. Kunnen diensten met beperkte toegevoegde waarde zijn voor de toepassing van de vereenvoudigde benadering (TPG 2017, § 7.49):

- boekhouding;

- verwerking en beheer van de rekeningen van klanten en leveranciers;

- activiteiten in verband met human resources;

- opvolging en compilatie van de gegevens m.b.t. gezondheid, veiligheid en leefmilieu en andere normen die toepasselijk zijn op de onderneming;

- diensten in het domein van de informatietechnologieën die geen deel uitmaken van de hoofdactiviteit van de multinationale groep van ondernemingen;

- bijstand op het vlak van interne en externe communicatie en van public relations (met uitzondering van specifieke reclame- of commercialiseringsactiviteiten en het uitstippelen van de strategieën in verband daarmee);

- juridische diensten;

- activiteiten in verband met het naleven van de fiscale verplichtingen;

- algemene administratieve diensten of diensten van gewoon beheer.

Vereenvoudigde benadering tot vaststelling van de arm's length-vergoeding voor intragroepsdiensten met beperkte toegevoegde waarde

185. Om de arm's length-vergoeding van intragroepsdiensten met beperkte toegevoegde waarde vast te stellen moet de dienstverlener een winstmarge vaststellen op alle kosten in verband met die diensten, met uitzondering van de voorschotkosten. Dezelfde marge moet worden gebruikt voor alle diensten met beperkte toegevoegde waarde.

186. De winstmarge is gelijk aan 5 % van de betrokken kosten en moet niet worden gerechtvaardigd door een vergelijkende studie.

187. Een multinationale groep van ondernemingen die gekozen heeft voor de toepassing van de vereenvoudigde benadering moet deze benadering toepassen in alle landen waar de vereenvoudigde benadering mag toegepast worden.

188. Opgelet, het feit dat de vereenvoudigde benadering niet toepasselijk is voor een bepaalde activiteit, betekent niet dat deze activiteit noodzakelijkerwijze hogere rendementen oplevert. De activiteit zou nog een beperkte toegevoegde waarde kunnen hebben, maar de arm's length-prijs voor een dergelijke activiteit moet worden vastgesteld op basis van de 'normale' richtlijnen.

Documentatie

189. Een groep van multinationale ondernemingen die ervoor kiest om de vereenvoudigde benadering toe te passen, moet de nodige documentatie samenstellen met onder meer:

- de beschrijving van de geleverde diensten met beperkte waarde, de begunstigden en alle elementen die toelaten te besluiten dat de betrokken diensten moeten worden beschouwd als intragroepsdiensten in de betekenis van het huidige hoofdstuk;

- de contracten of schriftelijke afspraken;

- documenten en berekeningen betreffende de vaststelling van de kostengroepen, in het bijzonder een lijst met een gedetailleerde opgave van de categorieën van diensten en het bedrag van de relevante kosten, met inbegrip van de kosten van de diensten die exclusief aan een lid van de groep worden verstrekt;

- de berekeningen betreffende de toepassing van de gebruikte verdeelsleutels.

## Hoofdstuk VIII: Kostenbijdrageregelingen of Cost Contribution Agreements (CCA) INLEIDING

190. Een kostenbijdrageregeling, beter gekend als een cost contribution arrangement (hierna CCA) is een contractuele overeenkomst waarin partijen afspreken om gezamenlijk immateriële of materiële vaste activa te ontwikkelen, te produceren of te verwerven, of om dienstverlening te ontwikkelen ten voordele van alle deelnemers. De bijdragen en kosten alsook de bijhorende risico's worden gedeeld door de deelnemende partijen. De bijdrage moet in overeenstemming zijn met de relatieve verwachte voordelen. Een CCA is een contract. Het is doorgaans geen aparte juridische entiteit of vaste inrichting.

191. We onderscheiden 2 types CCA's, deze die zijn opgezet voor de gezamenlijke ontwikkeling, productie of het verwerven van immateriële of materiële vaste activa ('ontwikkelings-CCA's' of 'development CCA's') en deze die zijn opgezet om diensten te verlenen ('diensten-CCA's of 'service CCA's').

192. Eén van de grote verschillen tussen deze twee types CCA's is, dat in het geval van ontwikkelings-CCA's de voordelen over het algemeen in de toekomst verwacht worden, terwijl bij diensten-CCA's de voordelen voor de partijen reeds gekend zijn op het moment van de dienstverlening.

193. Bij een ontwikkelings-CCA heeft elke deelnemer rechten op de ontwikkelde immateriële of materiële vaste activa. Bij immateriële vaste activa is het mogelijk dat elke deelnemer bijvoorbeeld de juridische eigendom verwerft, maar het is eveneens mogelijk dat slechts één deelnemer de juridische eigendom verkrijgt en de andere deelnemers bepaalde gebruiks- of exploitatierechten verkrijgen (bv het alleenrecht tot verkoop in de Benelux voor de periode 2018 tot 2023). In dat geval moet er dan geen royalty of andere vergoeding meer betaald worden voor het gebruik van de ontwikkelde activa.

ARM'S LENGTH BEGINSEL

194. Een CCA voldoet aan het arm's length beginsel indien de bijdragen van de deelnemers overeenkomen met datgene wat een onafhankelijke onderneming onder vergelijkbare omstandigheden bereid zou zijn bij te dragen, gegeven de voordelen die zij redelijkerwijs verwacht op grond van de overeenkomst. Om het arm's length principe te kunnen toepassen op een CCA, is het dus fundamenteel dat elke deelnemer redelijkerwijs verwacht een voordeel te behalen. Dit betekent dat de waarde van de bijdrage van elke deelnemer moet bepaald worden om vervolgens te toetsen of dat in overeenstemming is met eenieders relatief aandeel in de totale opbrengsten van de CCA-activiteit.

BEPALEN VAN DE DEELNEMERS

195. Wanneer een partij geen voordeel verwacht te behalen uit de CCA, kan ze niet beschouwd worden als deelnemer van de CCA. Een onderneming die R&D doet voor de CCA, maar zelf geen voordeel verwacht te behalen van de CCA, zal niet beschouwd worden als een deelnemer, maar als een service provider van de CCA.

196. Het is tevens belangrijk en noodzakelijk dat elke deelnemer de risico's draagt die verbonden zijn aan diens inbreng in de CCA, controle heeft over die risico's en eveneens de nodige financiële capaciteit heeft om deze risico's te dragen. Hij moet ook effectief de controle over deze risico's kunnen uitoefenen en zelf de belangrijke beslissingen in dit verband kunnen nemen. Het is niet noodzakelijk dat de activiteiten van de CCA door het eigen personeel van de deelnemers worden uitgevoerd. Bepaalde activiteiten kunnen uitbesteed worden zolang de deelnemers maar de controle uitoefenen over de risico's die zij dragen onder de CCA inzake de uitbestede functies.

WAARDEBEPALING VAN DE CCA

197.Om tot een arm's length vergoeding te komen en om te bepalen waar er waarde tot stand komt, is een duidelijke omschrijving van de eigenlijke transactie noodzakelijk. Zo dient uitgezocht te worden wat partijen echt overeenkomen en daarbij is een juiste risicoanalyse zeer belangrijk. In dit verband verwijzen we naar hoofdstuk I van deze circulaire waar de verschillende stappen worden toegelicht om tot de correcte bepaling te komen van de functionaliteit en de risico's van de partijen.

VERWACHTE OPBRENGSTEN

198. Het relatieve aandeel van iedere deelnemer in de totale verwachte voordelen kan worden geschat op basis van de te verwachten extra inkomsten of de door iedere deelnemer bespaarde kosten ten gevolge van de CCA.

199. In de praktijk worden de relatieve aandelen van de deelnemers in de totale verwachte opbrengsten vaak bepaald d.m.v. een verdeelsleutel. Voorbeelden van verdeelsleutels zijn: omzet, gebruikte, geproduceerde of verkochte eenheden, brutowinst, aantal personeelsleden …. Soms kan het nodig zijn om meer dan één verdeelsleutel te hanteren, bv. indien de CCA meerdere activiteiten omvat. Het kan eveneens gebeuren dat de verdeelsleutels over de jaren heen dienen aangepast te worden.

200. Indien verwacht wordt dat een belangrijk deel van of alle voordelen uit een door een CCA bestreken activiteit zullen worden gerealiseerd in de toekomst en niet op dit moment, dient bij de allocatie van bijdragen rekening te worden gehouden met toekomstverwachtingen ten aanzien van het aandeel van de deelnemers in die voordelen, zeker voor wat betreft de ontwikkelings-CCA's.

201. Bij een ontwikkelings-CCA, en zeker als er immateriële activa zijn betrokken, is het niet steeds eenvoudig de verwachte opbrengst te bepalen. Voor deze gevallen kunnen de waarderingstechnieken (valuation techniques) van de immateriële vaste activa nuttig zijn.

BIJDRAGEN

202. Bij de bijdragen dient er een onderscheid gemaakt te worden tussen de bijdragen d.m.v. bestaande Immateriële Activa (IA) en de bijdragen tijdens de duur van de CCA zelf. Voor de waardering van de eerste zal gebruikt gemaakt worden van de waarderingstechnieken zoals bij de te verwachten opbrengsten. Voor de waardering van de tweede houden we rekening met de waarde van de uitgeoefende functies en niet noodzakelijk met de kosten.

203. In uitzonderlijke gevallen, wanneer het verschil tussen de kosten en de waarde minimaal is, kan louter at cost doorgerekend worden. Dit model wordt vaak gebruikt voor ontwikkelings-CCA's.

COMPENSATIEBETALINGEN

204. Een CCA is arm's length indien het totale aandeel in de bijdragen van een deelnemer (vermeerderd of verminderd met eventuele compensatiebetalingen) in overeenstemming is met zijn totale aandeel in de (verwachte) opbrengsten.

205. Wanneer dit niet overeenstemt, moet er een aanpassing van de bijdrage gebeuren onder de vorm van een (verdere) compensatiebetaling. Vanuit fiscaal standpunt dienen deze compensaties op dezelfde manier behandeld te worden als de bijdragen zelf.

NIEUWE LEDEN, UITTREDENDE LEDEN EN STOPZETTING VAN DE CCA

206. Een toetreding tot, uittreding uit of stopzetting van een CCA kan aanleiding geven tot een vergoeding. Een nieuwe deelnemer die toetreedt tot een reeds bestaande CCA zal een buy-in payment verschuldigd zijn, ter vergoeding van de reeds ontwikkelde IA.

207. Een zelfde situatie kan zich voordoen bij een uittredend lid. Dit lid zal vergoed worden met een buy-out payment als vergoeding voor de achtergebleven activa.

208. Bij de stopzetting van de CCA zal ieder lid recht hebben op het gebruik van de resultaten voortvloeiend uit de CCA indien die er zijn, of zal ze een vergoeding ontvangen indien ze dit recht afstaat aan een van de andere leden.

DOCUMENTEREN VAN CCA'S

209. De opbrengsten en bijdragen voortkomende uit een CCA moeten consistent zijn met het arm's length principe. Bijgevolg is een degelijke documentatie vereist. Hierna volgt een indicatieve lijst van nuttige en relevante documentatie bij de aanvang van de CCA en tijdens de duur van de CCA.

210. Bij de aanvang van de CCA:

- een lijst met deelnemers;

- een lijst van alle andere verbonden ondernemingen die bij de CCA-activiteit betrokken zullen zijn of waarvan wordt verwacht dat ze de resultaten van de betreffende activiteit zullen exploiteren of gebruiken;

- de omvang van de activiteiten en specifieke projecten die door de CCA worden beheerd;

- de duur van de afspraak;

- de manier waarop het relatieve aandeel van de deelnemers in de verwachte voordelen wordt gemeten, en alle toekomstverwachtingen die gebruikt zijn in dit verband;

- de vorm en waarde van de initiële bijdragen van elke deelnemer en een gedetailleerde beschrijving van de wijze waarop de waarde van de oorspronkelijke en verdere bijdragen wordt bepaald;

- de verwachte toewijzing van verantwoordelijkheden en taken, die verband houden met de activa gebruikt in de CCA-activiteit;

- de procedures voor en de gevolgen van het toetreden tot, uittreden uit of beëindiging van de CCA;

- alle bepalingen in verband met compensatiebetalingen en de aanpassing van contractuele voorwaarden om wijzigingen in de economische omstandigheden weer te geven.

211. Tijdens de duur van de CCA:

- elke wijziging aan de overeenkomst (bv. in voorwaarden, deelnemers, activiteit) en de gevolgen hiervan;

- een vergelijking tussen de projecties die werden gebruikt om de verwachte voordelen van de CCA te bepalen en de werkelijke resultaten;

- de jaarlijkse uitgaven voor het uitvoeren van de CCA-activiteit, de vorm en de waarde van de bijdragen van elke deelnemer tijdens de duur van de CCA, en een detail van de manier waarop de waarde van de bijdragen wordt bepaald.

## Hoofdstuk IX: Verrekenprijsaspecten van bedrijfsherstructureringen
INLEIDING

212. Onder een bedrijfsherstructurering wordt verstaan, een grensoverschrijdende reorganisatie van de commerciële of financiële relaties tussen verbonden ondernemingen, met inbegrip van de beëindiging of de substantiële reorganisatie van bestaande afspraken/overeenkomsten. Verhoudingen met derde partijen (bv. leveranciers, onderaannemers, klanten, …) kunnen een aanleiding zijn voor de herstructurering of kunnen er door beïnvloed worden (TPG 2017, § 9.1). Klassieke fusie-, splitsing-, afsplitsingverrichtingen worden hier dus niet bedoeld.

213. Bedrijfsherstructureringen hebben dikwijls te maken met een conversie van 'full-fledged' distributeurs (verkoopondernemingen die alle bij de verkoop behorende activiteiten uitoefenen, alle verkooprisico's dragen en ook eigenaar zijn van alle activa die bij de verkoop nodig zijn) naar 'limited risk' distributeurs, marketeers, verkoop agenten of commissionairs, die hun activiteiten uitoefenen voor een buitenlandse verbonden onderneming die als principaal voor de groep opereert.

214. Een herstructurering kan ook betekenen een conversie van een 'full-fledged producent' (onderneming met een relatief hoger niveau van uitgevoerde functies en gedragen risico's) naar een 'contract manufacturer' (maakloonwerker met eigen voorraad grondstoffen en afgewerkte producten) of naar een 'toll manufacturer' (maakloonwerker die geen eigenaar is van de grondstoffen die hij verwerkt noch van de afgewerkte producten die hij produceert).

215. Andere voorbeelden van bedrijfsherstructurering zijn (i) overdracht van immateriële vaste activa ('intangibles') of rechten in die activa naar een centrale entiteit (zgn. 'IP company') binnen de groep, (ii) concentratie van de functies in een regionale of centrale entiteit, met een afname van die functies in aard of in schaal bij de andere betrokken entiteiten (bv. aankopen ('procurement'), verkoopondersteuning en logistieke bevoorrading) en (iii) toewijzen van 'intangibles' of risico's aan operationele groepsondernemingen.

216. Verscheidene redenen kunnen aan de basis liggen van een bedrijfsherstructurering, waaronder:

- realiseren of maximaliseren van synergiën of schaalvoordelen;

- stroomlijnen van het beheer van de bedrijfslijnen;

- verbeteringen van de bevoorrading ('supply chain');

- ontwikkeling van web-gebaseerde technologieën (invoering ERP/SAP).

217. Tenslotte kunnen bedrijfsherstructureringen noodzakelijk zijn om de rendabiliteit van de ondernemingen van de groep te behouden of verliezen te beperken (bv. bij overcapaciteit of in tijden van recessie).

AANDACHTSPUNTEN BIJ BEDRIJFSHERSTRUCTURERINGEN

218. Verplaatsing van winstpotentieel van één groepsonderneming naar een andere is een belangrijk aandachtspunt. Bij de beoordeling van de verrekenprijsgevolgen dient rekening te worden gehouden met de complexiteit van bedrijfsherstructureringen en dient gepoogd te worden om de situatie realistisch en pragmatisch te overschouwen (TPG 2017, § 9.6).

219. De TPG 2017 en het arm's length beginsel moeten consequent worden toegepast. Zo zullen de TPG 2017 niet op een andere wijze worden toegepast bij herstructureringen en transacties na de herstructurering dan bij transacties die vanaf het begin op dezelfde wijze werden gestructureerd (TPG 2017, § 9.9).

ARM'S LENGTH VERGOEDING VOOR DE HERSTRUCTURERING ZELF

220. Een bedrijfsherstructurering kan een grensoverschrijdende overdracht van 'iets van waarde' tot gevolg hebben maar dit is niet altijd het geval (TPG 2017, § 9.10).

221. Om uit te maken of dit het geval is (m.a.w. om de verrekenprijsgevolgen te kunnen inschatten) dienen een aantal stappen te worden gevolgd, welke hierna worden uiteengezet.

Stap 1: analyse van de transacties die begrepen zijn in de herstructurering door (TPG 2017, § 9.13 - 9.33)

222. Identificatie van de commerciële en financiële relaties die geleid hebben tot de overdracht van iets van waarde, waarbij (de verplaatsing van) risico's zeer belangrijk is, omdat – in een vrije markt – het dragen van risico's een invloed heeft op de wijze waarop winsten of verliezen worden gealloceerd tussen de betrokken partijen;

223. Inzicht omtrent de redenen waarom de herstructurering wordt doorgevoerd en van de verwachte voordelen, met inbegrip van synergiën;

224. Vergelijking met de andere mogelijke realistische opties die voorhanden zijn voor de betrokken partijen;

225. Voorlegging van een passende verrekenprijsdocumentatie m.b.t. de bedrijfsherstructurering.

Stap 2: erkenning van de herstructurering (TPG 2017, § 9.34 - 9.38)

226. Multinationale ondernemingen zijn vrij om hun bedrijfsactiviteiten te organiseren zoals ze dit het best vinden. Bedrijfsherstructureringen leiden dikwijls naar globale bedrijfsmodellen die bijna nooit terug te vinden zijn tussen onafhankelijke partijen.

227. De belastingadministraties mogen deze bedrijfsmodellen niet naast zich neerleggen bij de beoordeling van de verrekenprijzen (behalve in uitzonderlijke situaties als bedoeld in de TPG 2017, § 1.222).

Het volstaat niet om aan te tonen dat de bedrijfsherstructurering commercieel zinvol is op groepsniveau. De gevolgen van de herstructurering dienen voor alle leden van groep afzonderlijk te worden beoordeeld met in acht name van het arm's length principe (TPG 2017, § 9.37).

228. Belastingmotieven kunnen een rol spelen bij de herstructurering, maar zijn op zich geen reden om de aard en de structuur van de transacties niet te erkennen (TPG 2017, § 9.38).

Stap 3: onderzoek van de relatie tussen de herstructurering en de verplaatsing van winstpotentieel (TPG 2017, § 9.39 - 9.47)

229. De vraag dient te worden beantwoord of de overdracht, beëindiging of heronderhandeling tussen onafhankelijke partijen aanleiding zou geven tot een (schade)vergoeding.

230. Met winstpotentieel wordt in de TPG 2017 bedoeld de 'verwachte toekomstige winsten' (in sommige gevallen kan het gaan om 'verwachte verliezen').

231. In deze context worden niet bedoeld de winsten/verliezen die zich zouden voordoen indien geen herstructurering zou plaats vinden.

232. Een interessant voorbeeld is te vinden in de TPG 2017, § 9.46 en 9.47.

Stap 4: onderzoek van de verrekenprijsgevolgen van de herstructurering

233. Dit onderzoek dient uitsluitsel te geven over de vraag of 'iets van waarde' van de geherstructureerde onderneming wordt overgedragen aan een andere groepsonderneming en tegen welke waarde.

234. Waardevolle overdrachten kunnen betrekking hebben op (TPG 2017, § 9.48 e.v.)

- materiële vaste activa (bv. voorraden);

- immateriële vaste activa (bv. patenten, merken, contractuele rechten, enz.);

- een activiteit ('on going concern');

- uitbesteding van activiteiten ('outsourcing').

235. Bij stopzetting of substantiële herziening van bestaande regelingen rijst de vraag of de geherstructureerde entiteit geen recht heeft op een (schade)vergoeding, welke zou moeten worden betaald tussen onafhankelijke partijen. Volgende zaken dienen hiervoor te worden bekeken:

- eventueel wettelijke bepalingen welke hierover terug te vinden zijn in het handelsrecht;

- arm's length karakter van eventuele afspraken tot vergoeding;

- welke partij dient de vergoeding(en) te dragen.

Wanneer bijvoorbeeld een Belgische entiteit die kan gekarakteriseerd worden als een toll manufacturer of een limited risk distributeur die vergoed wordt op basis van een TNMM bij haar herstructurering uitzonderlijke kosten oploopt (zoals bv. ontslagvergoedingen, uitzonderlijke afschrijvingen, …) moeten deze kosten in principe doorgerekend worden aan ofwel de principaal, ofwel aan de entiteit die de beslissing genomen heeft, ofwel aan de entiteit die voordeel haalt uit de verrichting of aan meerdere van deze entiteiten. In voorkomend geval moeten deze herstructureringskosten dus niet ten laste genomen worden door deze Belgische entiteiten en kunnen ze worden doorgerekend zonder mark-up (zie ook TPG 2017, § 9.94 - 9.97).

236. Er mag niet worden uitgegaan van de veronderstelling dat elke stopzetting of substantiële herziening van een bestaande regeling aanleiding geeft tot een recht op vergoeding. Bedoeling blijft, zoals steeds inzake verrekenprijzen, vast te stellen hoe derde partijen zouden omgaan met de herstructurering en welke vergoedingen door hen zouden worden betaald. Het arm's length karakter dient hier te worden bekeken vanuit het perspectief van de betrokken groepsvennootschappen en niet vanuit groepsniveau (TPG 2017, § 9.12).

237. Voor voorbeelden kan worden verwezen naar:

- conversie van full-fledged producent naar contract manufacturer (TPG 2017, § 9.44);

- conversie van full-fledged distributor naar limited risk distributor (TPG 2017, § 9.45);

- voorbeeld inzake centrale inkoop (TPG 2017, § 9.25):

* bedoeling: volume kortingen en besparingen in administratieve kosten;

* voordelen dienen te worden toegewezen aan de verbonden ondernemingen die betrokken zijn bij het realiseren van de synergievoordelen.

VERREKENPRIJZEN NA DE HERSTRUCTURERING

238. Als algemeen principe geldt dat verrekenprijzen niet anders worden bepaald na een herstructurering dan wanneer de activiteiten van in het begin worden gestructureerd (TPG 2017, § 9.98 - 101).

239. Wel kunnen zich een aantal feitelijke verschilpunten voordoen die een impact hebben op de vergelijkbaarheidsanalyse en bijgevolg op de arm's length vergoeding (TPG 2017, § 9.102 e.v.), bijvoorbeeld:

- de voorhanden zijnde andere mogelijke realistische opties van de betrokken partijen;

- de reeds aanwezige marktpenetratie;

- de vóór de herstructurering opgebouwde intangibles;

- de mogelijk nog te dragen risico's van de pre-conversie activiteiten ('cut-off issue').

240. Wat de selectie en toepassing van een verrekenprijsmethode op verbonden transacties na de herstructurering betreft dient men de functies, activa en risico's van beide betrokken partijen te kennen. Aandacht moet hierbij geschonken worden aan de waardevolle (lokaal niet-beschermde) intangibles en aan economische belangrijke risico's die zouden achterblijven bij de geherstructureerde onderneming (TPG 2017, § 9.108).

241. De verrekenprijsmethode moet voortvloeien uit de analyse van de economisch relevante karakteristieken van de verbonden transacties na de herstructurering.

242.In bepaalde omstandigheden kan er een belangrijke relatie bestaan tussen de vergoeding voor de herstructurering en de vergoeding na de herstructurering (TPG 2017, § 9.114).

243. Hierdoor bestaat de mogelijkheid om een compensatie voor herstructurering uit te drukken in een lagere/hogere toekomstige vergoeding tussen de betrokken partijen.

244. Wanneer de herstructurering betrekking heeft op een verplaatsing van bepaalde activiteiten kan dit 'location savings' met zich meebrengen.

## Hoofdstuk X: Financiële transacties

Secties A tot E van het rapport van 11 februari 2020* worden geïntegreerd in de OESO TPG als Hoofdstuk X. Sectie F is toegevoegd aan Sectie D.1.2.1. in hoofdstuk I van de TPG en volgt onmiddellijk op paragraaf 1.106.

*OECD (February 2020), Transfer Pricing Guidance on Financial Transactions: Inclusive Framework on BEPS Actions 4, 8-10, OECD, Paris.

INLEIDING

245. Het is niet de bedoeling om hier omstandig de bepaling van een arm's length rentevoet voor een intra-groepslening, een intra-groep garantiefee of de vergoedingen van de deelnemers in een cash pool te beschrijven maar wel om een aantal zaken aan te geven waarmee de administratie zal rekening houden bij de behandeling van dossiers waarin dergelijke verrichtingen voorkomen.

246. Hierna worden achtereenvolgens de intra-groep leningen, het verstrekken van intra-groep garanties voor leningen en cash pool behandeld. Aangezien het begrip 'rating' in de drie behandelde intra-groep financiële transacties een belangrijke rol speelt wordt hierover vooraf een kleine toelichting gegeven.

RATING

247. Een rating kan, kort, omschreven worden als de uitdrukking van de kredietwaardigheid van een onderneming. Een rating is m.a.w. een uitdrukking van de mate waarin een ontlenende onderneming in staat geacht wordt aan haar financiële verplichtingen (waaronder de terugbetaling van een lening) te kunnen voldoen.

248. Het bepalen van een rating is van bijzonder belang om een overeenkomstige marktconforme rentevoet en garantievergoeding te kunnen bepalen bij een intra-groep verrichting.

249. Sommige multinationale groepen kregen een rating toegekend door één van de internationale rating bureaus terwijl andere multinationale groepen niet over een dergelijke rating beschikken. De individuele leden van een groep beschikken doorgaans niet over een rating toegekend door een onafhankelijk ratingbureau. Om tot een marktconforme vergoeding te kunnen komen dienen de administratie en/of de belastingplichtige dus een individuele rating te bepalen voor de ontlenende onderneming(en).

250. Bij het bepalen van een dergelijke rating voor een lid van de multinationale groep zal de administratie rekening houden met o.m. volgende principes:

- zoals in de TPG 2017 aangegeven (§ 1.158 e.v., § 1.167 en § 7.13) dient een lid van de multinationale groep geen vergoeding te betalen indien het een betere rating heeft, enkel en alleen op basis van het deel uitmaken van de groep. Dit is de zogenaamde 'impliciete steun';

Een voorbeeld ter verduidelijking:

Op een zuivere 'stand alone' basis heeft een groepslid de volgende rating:

BB

Rekening houdend met de 'impliciete' ondersteuning heeft dit groepslid de volgende rating:

A

Voor de stijging van de rating van BB naar A mag het groepslid geen vergoeding betalen.

- Indien een lid van de multinationale groep een strategisch belangrijke functie binnen de groep heeft (op het ogenblik van de bepaling van de rating of rekening houdende met de toekomstige strategie van de groep) dan zal de rating van het groepslid (zeer) nauw aansluiten bij de rating van de groep.

- Indien een onderneming van de groep een garantie verstrekt aan de ontlener dan zal de ontlener in principe dezelfde rating hebben als de garantieverstrekker (hierbij wordt er vanuit gegaan dat de garantieverstrekker een betere rating heeft dan de ontlener).

- Er zijn op de markt commerciële tools beschikbaar om ratings te bepalen. De administratie aanvaardt in principe het gebruik van dergelijke tools.

- De maximale rating van een groepslid kan in principe niet hoger zijn dan de rating van de groep zelf.

INTRA-GROEP LENINGEN

251. Bij het verstrekken van financieringen binnen de groep dienen zich de volgende vragen aan:

- heeft de uitlener andere realistische opties ter beschikking? De uitlener zal zeker een grondige financiële analyse maken van de mogelijke ontlener;

- zou de ontlener ook een financiering (van hetzelfde bedrag, dezelfde looptijd, …) van een derde (bv. bank) kunnen krijgen?

- zou de ontlener, ook al kan hij een financiering van een derde bekomen, hetzelfde bedrag ontlenen gelet op de sector waarin hij actief is?

- zijn de contractuele voorwaarden marktconform?

- wat is een marktconforme rentevoet?

252. Bovendien is het evident dat ook voor financiële transacties tussen verbonden ondernemingen (en waar van toepassing, d.i. waar in het dubbelbelastingverdrag een artikel 7, versie 2010 opgenomen is, tussen hoofdhuis en vaste inrichting – zie hoofdstuk XI Vaste inrichtingen en verrekenprijzen) de verrichting nauwgezet dient geanalyseerd te worden. Het kader uit hoofdstuk I van deze circulaire dient dan ook gevolgd te worden voor deze analyse.

253. Inzake financiële transacties zijn er op de markt heel wat vergelijkingspunten te vinden zodat bij intra-groep leningen de toepassing van de CUP methode zeker in overweging dient genomen te worden. Hierbij dient dan naar vergelijkbare transacties tussen derden gezocht te worden. Vergelijkingselementen zijn o.m. de rating van de ontlenende onderneming, het bedrag van de lening, de looptijd van de lening, de munt van de lening, ….

254. Ook een interne CUP kan uiteraard dienst doen als referentie om een marktconforme rentevoet te bepalen voor een intra-groep lening.

255. Indien de CUP methode niet kan toegepast worden, dan dient de marktconforme rentevoet opgebouwd te worden rekening houdende met volgende elementen:

- bepalen van een basisrente (bv. LIBOR of EURIBOR voor leningen tot maximaal 1 jaar);

- de looptijd van de lening;

- de rating van de ontlenende onderneming;

- het bedrag van de lening;

- de munt van de lening;

- ….

256. Indien het zuivere 'doorgeefleningen' betreft, dit zijn leningen waarbij de onderneming enkel een rol speelt als doorgeefluik, dan heeft de onderneming, aangezien geen enkel risico genomen wordt met betrekking tot de lening, enkel recht op een vergoeding voor haar diensten. Deze vergoeding kan bv. bepaald worden aan de hand van een methode gebaseerd op de kosten voor het verstrekken van de dienst.

INTRA-GROEP GARANTIES

257. Indien een groepslid een garantie verstrekt aan een ander groepslid (de ontlener) en deze garantie de ontlener in staat stelt om aan betere voorwaarden een lening te bekomen, dan is een vergoeding voor de verstrekte garantie verantwoord.

255. De administratie heeft voor het bepalen van de vergoeding voor de garantie een voorkeur voor de zogenaamde 'yield approach'. Hierbij wordt een vergelijking gemaakt tussen de rente die een onderneming zou dienen te betalen met en zonder de garantie. Hierbij dient eveneens rekening gehouden met het feit dat voor de 'impliciete' garantie geen vergoeding dient betaald te worden.

259. Een voorbeeld ter verduidelijking:

Op een zuivere 'stand alone' basis heeft een groepslid de volgende rating:

BB

Rekening houdend met de 'impliciete' ondersteuning heeft dit groepslid de volgende rating:

A

Na de garantie heeft het groepslid de volgende rating:

AAA

Indien nu, zuiver theoretisch, voor een A rating een rente zou dienen betaald te worden van 4 % en voor een AAA rating 1,5 %, dan zal de vergoeding voor de garantie liggen tussen 0 % en 2,5 %. Aangezien beide ondernemingen een zeker 'nut' moeten hebben van de garantie zal de vergoeding voor de garantie geen 0 % zijn (in dit geval heeft de garantieverstrekker geen enkel voordeel uit het verstrekken van de garantie) maar ook geen 2,5 % (op dit ogenblik zou de genieter van de garantie geen enkel voordeel halen uit de garantie).

CASH POOL

260. De voornaamste reden waarom een multinationale groep een cash pool organiseert is om de 'cash' in de groep beter te kunnen beheren. Het voordeel van een dergelijke cash pool is dat negatieve saldi gecompenseerd worden door positieve saldi en de groep uiteindelijk hetzij minder rente dient te betalen op de totale negatieve positie hetzij meer rente ontvangt voor de totale positieve positie. Door alle posities samen te brengen staat de groep ook sterker om de rentevoeten voor de cash pool te onderhandelen met de bank. De administratie is dan ook van mening dat het grootste voordeel van de cash pool een zogenaamd 'synergie' effect is en dat dit synergievoordeel ten goede dient te komen aan de deelnemers in de cash pool.

261. Inzake cash pool kunnen twee soorten onderscheiden worden:

- de fysieke pooling (ook wel zero balancing genoemd). Hierbij worden de saldi van de rekeningen van de deelnemers dagelijks overgemaakt naar een zogenaamde 'head account' en

- de notionele pooling waarbij de saldi niet werkelijk overgemaakt worden maar waarbij op basis van de saldi een 'theoretische' positie opgesteld wordt en op basis daarvan worden de vergoedingen van de deelnemers in de cash pool berekend.

262. In afwijking van het bepalen van een rating per onderneming is de administratie van mening dat inzake cash pool redelijkerwijze kan aangenomen worden dat alle deelnemers aan de cash pool voor elkaar garant staan. Alle deelnemers in de cash pool kunnen dan ook geacht worden dezelfde rating te hebben.

263. Tenzij uit de functieanalyse (beperkt tot de functies uitgeoefend als 'cash pool leader') anders blijkt, is de administratie van mening dat de cash pool 'leader', dit is de onderneming die de cash pool beheert, een dienst verleent in de cash pool en dat hij dus ook een marktconforme vergoeding dient te ontvangen voor deze dienstverlening. Doorgaans zal deze vergoeding kunnen bepaald worden op basis van een kosten gerelateerde methode.

264. Alle deelnemers in de cash pool dienen door hun deelname een voordeel te behalen. Hierboven werd reeds gesproken van het synergievoordeel. Ook indien bovenop het synergievoordeel nog betere voorwaarden bij de bank kunnen bekomen worden dienen de deelnemers hier mee van te genieten.

265. Alhoewel andere methoden die aanleiding geven tot een marktconforme vergoeding niet uitgesloten zijn, is de administratie van mening dat de vergoeding van de cash pool deelnemers best bepaald wordt op een rentevoet die beter is dan de rentevoet die zij op een 'stand-alone' basis zouden kunnen verkrijgen bij een bank.

266. Indien de cash pool leader effectief een dienstverlener is, dient er op gelet te worden dat deze niet meer ontvangt dan een marktconforme vergoeding voor deze dienst. Meestal zal deze dan bepaald worden op basis van een kostenbenadering. Om uit te sluiten dat de cash pool leader teveel winst zou ontvangen bij het toepassen van de 'verbeterde rentevoet' – methode dient de onderneming periodiek te evalueren of de winst uit de cash pool, na de vergoeding voor de cash pool leader in mindering te hebben gebracht, wel degelijk via de verbeterde rentevoeten onder alle deelnemers aan de cash pool verdeeld wordt.

267. Ten slotte dient opgemerkt dat cash pool een korte termijn verrichting betreft (in principe een dagelijkse verrichting). De administratie is van mening dat indien gedurende een periode van 12 maand dezelfde deelnemer in de cash pool een bedrag als deposito aanhoudt of gedurende dezelfde periode een bepaald bedrag in negatief staat (8), niet langer de rentevoet uit de cash pool kan toegepast worden maar dat een rentevoet, gebaseerd op de hierboven vermelde principes van intra-groep leningen, dient toegepast te worden.

(8) Bv. Een bedrag van 2.000.000 euro. Alhoewel de dagelijkse posities wisselen, wordt er steeds een bedrag van minimaal 2.000.000 euro hetzij als deposito hetzij als negatief saldo aangehouden gedurende 12 maand. De administratie zal dan oordelen dat dit bedrag van 2.000.000 euro hetzij een korte termijn lening hetzij een korte termijn ontlening betreft.

## Hoofdstuk XI: Vaste inrichtingen en verrekenprijzen

Doel van dit hoofdstuk is in hoofdlijnen de toepassing van de Authorised OECD Approach (AOA) door de Belgische administratie toe te lichten. Hierbij worden enkel een paar onderdelen van deel I 'Algemene Overwegingen' van de in de tekst vermelde rapporten besproken.

ALGEMEEN

268. Artikel 9 van het OESO modelverdrag bepaalt hoe de winstverdeling tussen verbonden ondernemingen (rechtspersonen) dient te gebeuren. Artikel 7 van het OESO modelverdrag bepaalt dan weer hoe de winsttoewijzing tussen hoofdhuis en vaste inrichting dient te gebeuren. Bij deze toewijzing wordt eveneens gebruik gemaakt van de verrekenprijzen.

269. De OESO ontwikkelde hiervoor een uitgebreide toelichting in 2008 en 2010 (9). Het is niet de bedoeling om beide rapporten hier uitgebreid toe te lichten maar wel om de algemene principes van deel I van deze rapporten in algemene bewoordingen weer te geven en, waar opportuun geacht, een toelichting te geven van de houding die de administratie met betrekking tot bepaalde situaties zal aannemen.

(9) De beide rapporten kunnen teruggevonden worden via deze link http://www.oecd.org/tax/transfer-pricing/attributionofprofitstopermanentestablishments.htm

270. Het is belangrijk om aan te geven dat artikel 7 van het OESO modelverdrag in 2010 grondig gewijzigd werd. België heeft nog maar enkele dubbelbelastingverdragen waarin artikel 7 van het OESO modelverdrag van 2010 is opgenomen. Bij de opmaak van de circulaire zijn Zwitserland (10) (inkomsten vanaf 01.01.2018), Noorwegen (11) (inkomsten vanaf 01.01.2019) en Japan (12) (inkomsten vanaf 01.01.2020) de enige verdragen dat een artikel 7, versie 2010 bevat. Verder werd met de Verenigde Staten (13) overeen gekomen om bij de toepassing van het dubbelbelastingverdrag ook de AOA (Authorised OECD Approach) uit het OESO rapport 2010 toe te passen.

(10) http://www.dekamer.be/FLWB/PDF/54/1574/54K1574001.pdf.
(11 )http://www.dekamer.be/FLWB/PDF/54/1999/54K1999001.pdf.
(12) http://www.dekamer.be/FLWB/PDF/54/2946/54K2946001.pdf.
(13) BS 06.08.2013 Ed. 2 blz. 49.123 C-2013/03264 Numac: 2013003264.

271. De methode die België hanteert om de winstverdeling tussen hoofdhuis en vaste inrichting te regelen is de zogenaamde AOA. Hierbij is het van groot belang om een onderscheid te maken tussen de verdragen die een artikel 7 van het OESO modelverdrag bevatten van vóór 2010 en de verdragen die een artikel 7 bevatten zoals opgenomen in het OESO modelverdrag vanaf 2010.

272. De verschillen tussen beide artikelen kunnen als volgt samengevat worden:

- voor een dubbelbelastingverdrag dat gebaseerd is op het OESO Modelverdrag van vóór 2010 kunnen geen leningen, met uitzondering van banken en verzekeringen, verstrekt worden tussen hoofdhuis en vaste inrichting (of vice versa). Er kunnen, met uitzondering van banken en verzekeringen, dus ook geen intresten betaald worden op basis van dergelijke leningen tussen hoofdhuis en vaste inrichting (of vice versa) en

- voor een dubbelbelastingverdrag dat gebaseerd is op het OESO Modelverdrag van vóór 2010 is geen betaling van royalty's mogelijk tussen vaste inrichting en hoofdhuis (of vice versa).

Met dit onderscheid dient steeds rekening gehouden bij het lezen van het vervolg van dit hoofdstuk en bij de toepassing in de praktijk.

273. Alhoewel in een hoofdhuis - vaste inrichting relatie geen wettelijk onderscheid kan gemaakt worden om uit te maken wie bepaalde activa in bezit heeft, de risico's op zich neemt, het kapitaal bezit, … dient toch gehandeld te worden alsof hoofdhuis en vaste inrichting twee afzonderlijke ondernemingen zijn.

274. Om die reden is onder artikel 7 van het OESO Modelverdrag een mechanisme ontwikkeld om risico's toe te wijzen, de economische eigendom van activa en kapitaal te bepalen, ….

275. Deze toewijzing gebeurt op basis van de zogenaamde Significant People Functions (SPF). Dit wil zeggen dat activa, risico's, kapitaal, … aan hetzij het hoofdhuis hetzij de vaste inrichting zullen toegewezen worden in functie van het belang van de activiteiten die personen (aanwezig in het hoofdhuis of de vaste inrichting) uitoefenen in relatie tot die activa, risico's, ….

276. Ondanks het feit dat er juridisch in principe geen handelingen (verkopen, dienstverlening, …) kunnen plaatsgrijpen tussen hoofdhuis en vaste inrichting wordt er voor de toewijzing van de winst aan de vaste inrichting toch gehandeld alsof hoofdhuis en vaste inrichting afzonderlijke ondernemingen zijn. De OESO spreekt in dit geval van 'dealings' tussen hoofdhuis en vaste inrichting. Deze 'dealings' zijn verrichtingen die tussen verbonden ondernemingen (rechtspersonen) aanleiding geven tot de toepassing van verrekenprijzen.

DE TOEPASSING VAN DE AOA METHODE: 2 STAPPEN

277. In stap 1 dient een grondige functionele en feitenanalyse uitgevoerd te worden (zoals aangegeven in hoofdstuk I van deze circulaire) om uit te maken wie (het hoofdhuis of de vaste inrichting) de economische eigendom heeft van activa, bepaalde risico's op zich neemt, ….

278. Op basis van deze analyse dienen de activa dan verdeeld te worden tussen het hoofdhuis en de vaste inrichting. Tevens zal deze analyse bepalen waar de risico's genomen worden m.b.t. bepaalde verrichtingen.

279. Uiteindelijk zal op basis van de verdeling van de activa en de toewijzing van de risico's ook 'vrij kapitaal' (d.i. financiering van de onderneming die geen aanleiding geeft tot aftrekbare intresten) en schuld verdeeld worden tussen hoofdhuis en vaste inrichting. Merk op dat de schuld die op deze wijze toegewezen wordt aan de vaste inrichting ook aanleiding geeft tot aftrekbare intresten bij de vaste inrichting.

280. In stap 2 van de AOA dienen dan de verrekenprijsregels toegepast te worden om een marktconforme prijs te bepalen voor de 'dealings'.

281. Bij stap 2 mag niet vergeten worden dat ook de functies die niet kunnen beschouwd worden als SPF dienen vergoed te worden op basis van de verrekenprijsregels.

OP WELKE WIJZE DIENT 'VRIJ KAPITAAL' AAN DE VASTE INRICHTING TOEGEWEZEN TE WORDEN?

282. Zowel in het rapport 2008 als in het rapport 2010 worden een aantal methoden opgenomen om 'vrij kapitaal' toe te wijzen aan de vaste inrichting. Het valt buiten het doel van deze circulaire om een omstandige uiteenzetting op te nemen van de diverse methoden.

283. Door de eenvoudige toepassingsmodaliteiten en het feit dat deze methode meer dan waarschijnlijk ook aanleiding geeft tot een correcte verdeling, heeft de administratie een voorkeur voor de toepassing van de 'Capital allocation approach' De toewijzing van 'vrij kapitaal' gebeurt hierbij in verhouding tot de toegewezen activa en risico's. Indien bv. 10 % van de activa en de risico's zijn toegewezen aan de vaste inrichting dan wordt ook 10 % van het 'vrij kapitaal' van het hoofdhuis toegewezen aan de vaste inrichting.

## Hoofdstuk XII: Inwerkingtreding

284. Behoudens de randnrs. 78, 106, 108, 115, 116 en 126, zijn de bepalingen van deze circulaire van toepassing op de transacties tussen verbonden ondernemingen die plaatsvinden vanaf 1 januari 2018. Voor de transacties tussen verbonden ondernemingen die plaatsvinden voor laatstgenoemde datum, zal zowel de belastingplichtige als de administratie zich bijgevolg kunnen baseren op de op dat moment geldende raadgevende instrumenten, met inbegrip van internationale standaarden.

285. De randnrs. 78, 106, 108, 115, 116 en 126 evenals het hoofdstuk X zijn van toepassing op de transacties tussen verbonden ondernemingen die plaatsvinden vanaf 1 januari 2020.

286. Voorafgaande beslissingen welke vóór de publicatie van de circulaire werden verstrekt door de Dienst Voorafgaande Beslissingen blijven onverminderd gelden aangezien deze circulaire geen wijziging vormt zoals bedoeld in artikel 23, tweede lid, 3° W 24/12/2002 tot wijziging van de vennootschapsregeling inzake inkomstenbelastingen en tot instelling van een systeem van voorafgaande beslissingen in fiscale zaken, waardoor de FOD Financiën verbonden blijft voor de resterende duur van de voorafgaande beslissing.

Interne ref.: 723.165

NL
