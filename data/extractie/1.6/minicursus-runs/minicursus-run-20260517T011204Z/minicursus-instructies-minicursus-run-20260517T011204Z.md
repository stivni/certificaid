# Minicursus-glue-run minicursus-run-20260517T011204Z — Instructies voor Opus-subagent

**Programmaonderdeel**: 1.6
**Run-id**: minicursus-run-20260517T011204Z
**Gegenereerd op**: 2026-05-17T01:12:04+00:00

## Jouw taak

Vul de `<!-- TODO: Opus-glue ... -->` placeholders in de skeleton-Markdown in.
Schrijf de output als één JSON-object naar stdout met de velden beschreven in
`prompts/minicursus-glue-v1.md`.

## Input-bestanden

- **Skeleton**: `content/studiemateriaal/1-6-externe-controle-bedrijfsrevisor-gecertificeerd.md`
- **Records-summaries** (59 stuks): zie §Records hieronder
- **Competentie-summaries** (10 stuks): zie §Competenties hieronder

## Anti-fabricatie-regels (verplicht)

- Geen feiten-claims in glue-tekst — alleen rationale, beginselen, transities
- Geen wikilinks bedenken — die staan al in de skeleton
- Verbind aan beginselen die in de records beschreven zijn
- Bij twijfel: korte neutrale tekst, geen uitvinding

## Records-summaries

```json
[
  {
    "id": "aangepast-oordeel",
    "naam": "Aangepast oordeel (modified opinion)",
    "node_type": "begrip",
    "definitie_snippet": "Een aangepast oordeel is elk oordeel dat AFWIJKT van een goedkeurend oordeel zonder voorbehoud: een oordeel met voorbehoud, een afkeurend oordeel, of een onthouding van oordeel. De keuze hangt af van twee dimensies: bron van probleem (afwijking vs. scope-beperking) en intensiteit (niet-diepgaand vs.",
    "rationale_snippet": ""
  },
  {
    "id": "assurance-informatie",
    "naam": "Assurance-informatie (controle-informatie)",
    "node_type": "begrip",
    "definitie_snippet": "Assurance-informatie (in ISA-jargon: audit evidence) is alle informatie die de beroepsbeoefenaar gebruikt om tot de conclusies te komen waarop hij zijn oordeel baseert. Hij moet voldoende EN geschikte assurance-informatie verkrijgen — voldoende verwijst naar de hoeveelheid; geschikt naar de relevant",
    "rationale_snippet": ""
  },
  {
    "id": "auditcyclus-fasen-synthese",
    "naam": "Auditcyclus — vier fasen vergeleken",
    "node_type": "synthese",
    "definitie_snippet": "",
    "rationale_snippet": ""
  },
  {
    "id": "auditplanning",
    "naam": "Auditplanning",
    "node_type": "procedure",
    "definitie_snippet": "De beroepsbeoefenaar plant de controle zodanig dat de opdracht efficiënt kan worden uitgevoerd. De planning bestaat uit twee lagen: de algemene strategie (reikwijdte, timing, omvang) en het controleprogramma (concrete werkzaamheden). De planning moet doorlopend worden bijgestuurd.",
    "rationale_snippet": ""
  },
  {
    "id": "auditrisicomodel",
    "naam": "Auditrisicomodel (controlerisico)",
    "node_type": "methode",
    "definitie_snippet": "Het auditrisicomodel structureert de risico-aanpak van de auditor. Het controlerisico — het risico dat de auditor een verkeerd oordeel geeft terwijl de financiële overzichten een materiële afwijking bevatten — wordt opgesplitst in drie componenten: inherent risico, intern beheersingsrisico en ontdek",
    "rationale_snippet": ""
  },
  {
    "id": "auditstrategie",
    "naam": "Auditstrategie (algehele strategie van de opdracht)",
    "node_type": "begrip",
    "definitie_snippet": "De auditstrategie is het overkoepelende plan voor de hele opdracht: ze bepaalt de reikwijdte, het tijdschema en de omvang, en geeft richtlijnen voor het opstellen van het werkprogramma. De strategie weegt opdrachtkenmerken, doelstellingen, professionele oordeelsfactoren, ervaring uit eerdere opdrach",
    "rationale_snippet": ""
  },
  {
    "id": "bedrijfsrevisor",
    "naam": "Bedrijfsrevisor",
    "node_type": "actor",
    "definitie_snippet": "Een bedrijfsrevisor is een natuurlijke of rechtspersoon die door het Instituut van de Bedrijfsrevisoren (IBR) is erkend en die exclusief bevoegd is voor de wettelijke controle van de jaarrekening van vennootschappen (commissaris-mandaat). Bedrijfsrevisoren staan onder publiek toezicht via het Colleg",
    "rationale_snippet": ""
  },
  {
    "id": "belangenconflict-accountant",
    "naam": "Belangenconflict van de externe accountant",
    "node_type": "regel",
    "definitie_snippet": "Het is de externe accountant verboden om — rechtstreeks of onrechtstreeks — een opdracht, functie of mandaat te aanvaarden of voort te zetten wanneer de uitoefening daarvan hem in een positie van belangenconflict dreigt te plaatsen die zijn onafhankelijke oordeel in het gedrang kan brengen. Hij moet",
    "rationale_snippet": ""
  },
  {
    "id": "beoordelingsverslag-elementen",
    "naam": "Elementen van het beoordelingsverslag (review report)",
    "node_type": "procedure",
    "definitie_snippet": "De beroepsbeoefenaar brengt een geschreven en gedateerd beoordelingsverslag uit dat de volgende elementen bevat: een titel, de geadresseerde en eventueel de beoogde gebruiker, identificatie van de gecontroleerde financiële overzichten, een korte beschrijving van de opdracht (uit de opdrachtbrief), e",
    "rationale_snippet": ""
  },
  {
    "id": "beperkte-mate-van-zekerheid",
    "naam": "Beperkte mate van zekerheid",
    "node_type": "begrip",
    "definitie_snippet": "Een beperkte mate van zekerheid (limited assurance) is het zekerheidsniveau bij een beoordelingsopdracht: het risico dat de beroepsbeoefenaar een verkeerde uitspraak doet wordt tot een aanvaardbaar (maar hoger dan bij een controle) niveau gebracht. De conclusie wordt geformuleerd in negatieve vorm.",
    "rationale_snippet": ""
  },
  {
    "id": "beroepsaansprakelijkheid-accountant",
    "naam": "Beroepsaansprakelijkheid van de accountant",
    "node_type": "regel",
    "definitie_snippet": "De beroepsbeoefenaar is aansprakelijk volgens het gemeen recht voor de uitvoering van zijn opdrachten. Hij mag zich niet — zelfs niet gedeeltelijk — aan zijn aansprakelijkheid onttrekken bij (1) een fout met bedrieglijk opzet of oogmerk te schaden, en (2) bij wettelijke controleopdrachten van de com",
    "rationale_snippet": ""
  },
  {
    "id": "beroepsgeheim-accountant",
    "naam": "Beroepsgeheim van de accountant",
    "node_type": "regel",
    "definitie_snippet": "De externe accountant is gebonden door het beroepsgeheim (art. 458 Strafwetboek). Hij mag vertrouwelijke informatie niet vrijwillig delen — ook niet bij een verhoor door politieambtenaar of openbaar ministerie. Uitzonderingen: getuigenis in rechte voor een rechter, eigen verdediging in een tuchtproc",
    "rationale_snippet": ""
  },
  {
    "id": "beweringen-audit",
    "naam": "Beweringen (assertions) in een audit",
    "node_type": "begrip",
    "definitie_snippet": "Beweringen (assertions) zijn de impliciete verklaringen die het management aflegt over elke transactiestroom, elk rekeningsaldo en elke toelichting in de jaarrekening. De auditor toetst per bewering of zij correct is. Typische beweringen: bestaan / voorkomen, volledigheid, rechten en verplichtingen,",
    "rationale_snippet": ""
  },
  {
    "id": "boekhoudkundige-schattingen-audit",
    "naam": "Boekhoudkundige schattingen (audit-perspectief)",
    "node_type": "begrip",
    "definitie_snippet": "Een boekhoudkundige schatting is een benadering van een bedrag wanneer het niet mogelijk is dat bedrag nauwkeurig te bepalen. Voorbeelden: voorzieningen voor geschillen, oninbare vorderingen, restwaarde van vaste activa, gebruiksduren van immateriële activa. Schattingsonzekerheid is het inherente ge",
    "rationale_snippet": ""
  },
  {
    "id": "cijferanalyses-audit",
    "naam": "Cijferanalyses bij een audit",
    "node_type": "methode",
    "definitie_snippet": "Cijferanalyses (analytical procedures) zijn evaluaties van financiële informatie door de analyse van aannemelijke verbanden tussen zowel financiële als niet-financiële gegevens. De auditor onderzoekt fluctuaties of relaties die inconsistent zijn met andere relevante informatie of significant verschi",
    "rationale_snippet": ""
  },
  {
    "id": "communicatie-met-management-governance",
    "naam": "Communicatie met management en met governance belaste personen",
    "node_type": "procedure",
    "definitie_snippet": "De beroepsbeoefenaar moet tijdig communiceren met het management en de met governance belaste personen. Hij deelt zijn verantwoordelijkheden mee, geeft een overzicht van de reikwijdte en het tijdschema, verkrijgt relevante assurance-informatie, en deelt belangrijke vaststellingen tijdens en op het e",
    "rationale_snippet": ""
  },
  {
    "id": "continuiteitsveronderstelling-audit",
    "naam": "Continuïteitsveronderstelling (audit-perspectief)",
    "node_type": "beginsel",
    "definitie_snippet": "De financiële overzichten worden opgesteld onder de veronderstelling dat de continuïteit van de onderneming gehandhaafd blijft en dat zij haar activiteiten in de voorzienbare toekomst zal voortzetten — tenzij het management voornemens is te liquideren of geen realistisch alternatief heeft. De audito",
    "rationale_snippet": ""
  },
  {
    "id": "contractuele-beoordelingsopdracht",
    "naam": "Contractuele beoordelingsopdracht",
    "node_type": "begrip",
    "definitie_snippet": "Een contractuele beoordelingsopdracht (ook 'review' of 'beperkt nazicht') is een assurance-opdracht waarbij de beroepsbeoefenaar een beperkte mate van zekerheid verschaft over de betrouwbaarheid van historische financiële informatie. Hij formuleert een conclusie in negatieve vorm: 'er zijn ons geen ",
    "rationale_snippet": ""
  },
  {
    "id": "contractuele-controleopdracht",
    "naam": "Contractuele controleopdracht",
    "node_type": "begrip",
    "definitie_snippet": "Een contractuele controleopdracht is een opdracht waarbij de gecertificeerd accountant (of bedrijfsrevisor) op verzoek van de cliënt — niet door wet opgelegd — een redelijke mate van zekerheid verschaft over de betrouwbaarheid van historische financiële informatie zoals een jaarrekening. De beroepsb",
    "rationale_snippet": ""
  },
  {
    "id": "controledocumentatie",
    "naam": "Controledocumentatie / controledossier",
    "node_type": "begrip",
    "definitie_snippet": "Controledocumentatie is de schriftelijke vastlegging van uitgevoerde controlewerkzaamheden, verkregen assurance-informatie en getrokken conclusies. Een controledossier bestaat uit één of meer mappen (fysiek of elektronisch) met alle vastleggingen van een specifieke controleopdracht.",
    "rationale_snippet": ""
  },
  {
    "id": "controleoordeel-types",
    "naam": "Types van controleoordeel",
    "node_type": "afwegingskader",
    "definitie_snippet": "Op het einde van een audit formuleert de beroepsbeoefenaar een controleoordeel. Vier types: (1) goedkeurend oordeel zonder voorbehoud, (2) oordeel met voorbehoud, (3) afkeurend oordeel, (4) onthouding van oordeel. De keuze hangt af van (a) of afwijkingen materieel zijn én of zij diepgaande invloed h",
    "rationale_snippet": ""
  },
  {
    "id": "controleverslag-elementen",
    "naam": "Elementen van het controleverslag (revisieverslag)",
    "node_type": "procedure",
    "definitie_snippet": "Elk controleverslag wordt schriftelijk en omstandig opgesteld en besluit met de wettelijk verplichte beoordeling. De auditor vermeldt op welke wijze hij de controle uitvoerde, of hij alle vereiste inlichtingen heeft ontvangen, in welke mate hij kon steunen op de interne controle en welk eventueel vo",
    "rationale_snippet": ""
  },
  {
    "id": "externe-bevestiging-audit",
    "naam": "Externe bevestiging (audit)",
    "node_type": "procedure",
    "definitie_snippet": "Externe bevestigingen zijn assurance-informatie verkregen in de vorm van een rechtstreekse schriftelijke reactie van een derde partij (de bevestigende partij) aan de beroepsbeoefenaar — op papier, elektronisch of op andere drager. De auditor zelf selecteert en verzendt deze; de cliënt mag de inhoud ",
    "rationale_snippet": ""
  },
  {
    "id": "fraude-versus-fout",
    "naam": "Fraude versus fout in een audit",
    "node_type": "begrip",
    "definitie_snippet": "Fraude is een opzettelijke handeling — door management, met governance belaste personen, werknemers of derden — waarbij misleiding wordt gebruikt om een onrechtmatig of onwettig voordeel te verkrijgen. Fout is daarentegen een ONopzettelijke handeling die tot een afwijking in de financiële overzichte",
    "rationale_snippet": ""
  },
  {
    "id": "gecertificeerd-accountant-ga",
    "naam": "Gecertificeerd accountant (GA)",
    "node_type": "actor",
    "definitie_snippet": "Een gecertificeerd accountant (GA) is een door het ITAA (Instituut van de Belastingadviseurs en de Accountants) erkend beroepsbeoefenaar bevoegd voor het organiseren van boekhouding, opmaken van jaarrekeningen, fiscaal advies en — in een aantal gevallen, in monopolie of gedeeld met de bedrijfsreviso",
    "rationale_snippet": ""
  },
  {
    "id": "gedeelde-wettelijk-voorbehouden-opdracht",
    "naam": "Gedeelde wettelijk voorbehouden opdracht",
    "node_type": "begrip",
    "definitie_snippet": "Een gedeelde wettelijk voorbehouden opdracht is een opdracht die door of krachtens de wet wordt toevertrouwd aan ofwel een gecertificeerd accountant ofwel een bedrijfsrevisor (gedeeld monopolie). Voorbeelden: inbreng in natura, quasi-inbreng, omzetting van rechtsvorm, ontbinding-vereffening. Geldt e",
    "rationale_snippet": ""
  },
  {
    "id": "gegevensgerichte-werkzaamheden",
    "naam": "Gegevensgerichte werkzaamheden (substantive procedures)",
    "node_type": "methode",
    "definitie_snippet": "Gegevensgerichte werkzaamheden zijn controlewerkzaamheden die zijn opgezet om afwijkingen van materieel belang op het niveau van beweringen te ontdekken. Twee soorten: detailcontroles (transactiestromen, rekeningsaldi, toelichtingen) en gegevensgerichte cijferanalyses.",
    "rationale_snippet": ""
  },
  {
    "id": "getrouw-beeld-controle",
    "naam": "Getrouw beeld als controlecriterium",
    "node_type": "beginsel",
    "definitie_snippet": "Het getrouw beeld is het centrale beoordelingscriterium van de auditor: hij toetst of de financiële overzichten — in alle van materieel belang zijnde opzichten — een getrouw beeld geven van het vermogen, de financiële toestand en het resultaat van de onderneming, overeenkomstig het van toepassing zi",
    "rationale_snippet": ""
  },
  {
    "id": "inherent-risico",
    "naam": "Inherent risico",
    "node_type": "begrip",
    "definitie_snippet": "Inherent risico is de vatbaarheid van een bewering (over een transactiestroom, rekeningsaldo of toelichting) voor een afwijking die — afzonderlijk of samen met andere — van materieel belang is, VOORDAT er rekening wordt gehouden met de interne beheersing. Het is een eigenschap van de aard en context",
    "rationale_snippet": ""
  },
  {
    "id": "intern-beheersingsrisico",
    "naam": "Intern beheersingsrisico",
    "node_type": "begrip",
    "definitie_snippet": "Intern beheersingsrisico is het risico dat een afwijking die kan optreden in een bewering (over een transactiestroom, rekeningsaldo of toelichting) — afzonderlijk of samen met andere van materieel belang — niet wordt voorkomen of niet tijdig wordt gedetecteerd en hersteld door de interne beheersing ",
    "rationale_snippet": ""
  },
  {
    "id": "itaa-algemene-controlenorm",
    "naam": "ITAA Algemene Controlenorm",
    "node_type": "begrip",
    "definitie_snippet": "De ITAA Algemene Controlenorm is een door het ITAA uitgevaardigde norm die de algemene principes vastlegt voor elke controleopdracht uitgevoerd door een gecertificeerd accountant: bekwaamheid, onafhankelijkheid, werkschema, werkdocumenten, opvolging, controlewerkzaamheden, verslag en toezicht via de",
    "rationale_snippet": ""
  },
  {
    "id": "itaa-kmo-controlenorm",
    "naam": "ITAA KMO-controlenorm",
    "node_type": "begrip",
    "definitie_snippet": "De ITAA KMO-controlenorm is een uitgewerkt normenkader voor contractuele controle- en beoordelingsopdrachten op de jaarrekening van KMO's en kleine vzw's. Inspireert zich op ISA-standaarden maar is aangepast aan de KMO-realiteit. Bevat regels voor opdrachtaanvaarding, planning, risico-inschatting, w",
    "rationale_snippet": ""
  },
  {
    "id": "kennis-van-onderneming-omgeving",
    "naam": "Kennis van de onderneming en haar omgeving",
    "node_type": "procedure",
    "definitie_snippet": "De accountant moet bij elke controle een degelijke kennis hebben van het bedrijf en zijn werkzaamheden. Hij analyseert de administratieve en boekhoudkundige organisatie en gaat na in hoeverre de interne controles van het bedrijf betrouwbaar zijn. Deze kennis is de basis voor de risico-inschatting en",
    "rationale_snippet": ""
  },
  {
    "id": "kwaliteitsbeheersing-opdrachtniveau",
    "naam": "Kwaliteitsbeheersing op opdrachtniveau",
    "node_type": "procedure",
    "definitie_snippet": "De opdrachtpartner draagt verantwoordelijkheid voor de algemene kwaliteit van elke opdracht. Hij waakt door observatie, controle van documenten en bevragingen of relevante ethische voorschriften en professionele normen worden nageleefd. Dat omvat: leiden + toezicht + uitvoering volgens de norm, eval",
    "rationale_snippet": ""
  },
  {
    "id": "materieel-belang-audit",
    "naam": "Materieel belang (materialiteit) in een audit",
    "node_type": "begrip",
    "definitie_snippet": "Materieel belang is de drempel waarboven een afwijking — afzonderlijk of gezamenlijk — de economische beslissingen kan beïnvloeden die gebruikers nemen op basis van de financiële overzichten. Boven die drempel is een afwijking 'van materieel belang'. De beroepsbeoefenaar bepaalt de drempel aan het b",
    "rationale_snippet": ""
  },
  {
    "id": "met-governance-belaste-personen",
    "naam": "Met governance belaste personen",
    "node_type": "actor",
    "definitie_snippet": "De met governance belaste personen zijn de persoon (personen) of organisatie(s) — bv. de bestuurders van een vennootschap — die verantwoordelijk zijn voor het uitoefenen van toezicht op de strategische aansturing van de onderneming en op haar verantwoordingsverplichtingen. Hun verantwoordelijkheid o",
    "rationale_snippet": ""
  },
  {
    "id": "onafhankelijkheid-externe-accountant",
    "naam": "Onafhankelijkheid van de externe accountant",
    "node_type": "beginsel",
    "definitie_snippet": "De externe accountant moet een opdracht weigeren of stopzetten zodra hij invloeden, feiten of banden vaststelt die zijn onafhankelijkheid, wils- of beoordelingsvrijheid of onpartijdigheid kunnen aantasten. Onafhankelijkheid is een continue plicht, niet alleen bij aanvang van de opdracht.",
    "rationale_snippet": ""
  },
  {
    "id": "ontbinding-vereffening-opdracht",
    "naam": "Ontbinding-vereffening opdracht van de gecertificeerd accountant",
    "node_type": "procedure",
    "definitie_snippet": "Bij ontbinding-vereffening verleent de gecertificeerd accountant (of bedrijfsrevisor) een wettelijk verplicht verslag over de staat van actief en passief op een datum die maximaal drie maanden voor de algemene vergadering ligt. Dit is een gedeelde wettelijk voorbehouden opdracht: enkel uit te voeren",
    "rationale_snippet": ""
  },
  {
    "id": "ontdekkingsrisico",
    "naam": "Ontdekkingsrisico",
    "node_type": "begrip",
    "definitie_snippet": "Ontdekkingsrisico is het risico dat de door de beroepsbeoefenaar uitgevoerde controlewerkzaamheden geen afwijking van materieel belang ontdekken die afzonderlijk of samen met andere bestaat. Het is de enige risicocomponent die de auditor zelf kan beïnvloeden, door de aard, timing en omvang van zijn ",
    "rationale_snippet": ""
  },
  {
    "id": "opdrachtbrief-accountant",
    "naam": "Opdrachtbrief van de accountant",
    "node_type": "procedure",
    "definitie_snippet": "Voor elke contractuele opdracht stelt de externe accountant een opdrachtbrief op die de scope, de verantwoordelijkheden, het ereloon en de wederzijdse verplichtingen vastlegt vóór de uitvoering begint. De opdrachtbrief is het juridische kader van de opdracht en de hefboom voor aansprakelijkheidsbepe",
    "rationale_snippet": ""
  },
  {
    "id": "opdrachttypes-zekerheidsniveaus-synthese",
    "naam": "Opdrachttypes en zekerheidsniveaus vergeleken",
    "node_type": "synthese",
    "definitie_snippet": "",
    "rationale_snippet": ""
  },
  {
    "id": "opvolging-voorganger-accountant",
    "naam": "Opvolging van een collega-accountant",
    "node_type": "procedure",
    "definitie_snippet": "Elke accountant die een confrater of een bedrijfsrevisor opvolgt, moet vooraf met hem in contact treden. De opvolger mag de werkdocumenten van zijn voorganger inzien, maar de voorganger mag zijn oorspronkelijke stukken niet uit handen geven. Bovendien moet hij — bij elke opdrachtaanvaarding — nagaan",
    "rationale_snippet": ""
  },
  {
    "id": "paragraaf-overige-aangelegenheden",
    "naam": "Paragraaf inzake overige aangelegenheden",
    "node_type": "begrip",
    "definitie_snippet": "Een paragraaf inzake overige aangelegenheden (other matter) is een paragraaf in de controleverklaring die verwijst naar een aangelegenheid die NIET in de financiële overzichten is gepresenteerd of toegelicht, maar die — naar het oordeel van de beroepsbeoefenaar — relevant is voor het begrip van de c",
    "rationale_snippet": ""
  },
  {
    "id": "paragraaf-ter-benadrukking",
    "naam": "Paragraaf ter benadrukking van bepaalde aangelegenheden",
    "node_type": "begrip",
    "definitie_snippet": "Een paragraaf ter benadrukking van bepaalde aangelegenheden (emphasis of matter) is een paragraaf in de controleverklaring die verwijst naar een aangelegenheid die op PASSENDE wijze in de financiële overzichten is gepresenteerd of toegelicht, maar die — naar het oordeel van de beroepsbeoefenaar — zo",
    "rationale_snippet": ""
  },
  {
    "id": "professioneel-kritische-instelling",
    "naam": "Professioneel-kritische instelling",
    "node_type": "beginsel",
    "definitie_snippet": "De beroepsbeoefenaar plant en voert de opdracht uit vanuit een professioneel-kritische instelling (professional skepticism): een onderzoekende houding, alert zijn op omstandigheden die kunnen wijzen op afwijkingen door fouten of fraude, en kritische evaluatie van controle-informatie. Hij neemt infor",
    "rationale_snippet": ""
  },
  {
    "id": "professionele-oordeelsvorming",
    "naam": "Professionele oordeelsvorming",
    "node_type": "beginsel",
    "definitie_snippet": "Professionele oordeelsvorming is het toepassen van relevante training, kennis en ervaring — in de context van de geldende controle-, verslaggevings- en ethische normen — bij het maken van weloverwogen keuzes over de handelwijzen die passend zijn in de omstandigheden van de opdracht. Het is wat de au",
    "rationale_snippet": ""
  },
  {
    "id": "randvoorwaarden-controle",
    "naam": "Randvoorwaarden voor een controle (preconditions)",
    "node_type": "voorgesteld:randvoorwaarden",
    "definitie_snippet": "Randvoorwaarden voor een controle zijn (1) het gebruik door het management of de met governance belaste personen van een AANVAARDBAAR stelsel inzake financiële verslaggeving, en (2) hun TOESTEMMING met de veronderstellingen op basis waarvan de controle wordt uitgevoerd. Zonder beide is een audit nie",
    "rationale_snippet": ""
  },
  {
    "id": "redelijke-mate-van-zekerheid",
    "naam": "Redelijke mate van zekerheid",
    "node_type": "begrip",
    "definitie_snippet": "Een redelijke mate van zekerheid (reasonable assurance) is het hoogste praktisch haalbare niveau van zekerheid in een audit-opdracht. De beroepsbeoefenaar heeft voldoende en geschikte assurance-informatie verzameld om het controlerisico tot een vaktechnisch aanvaardbaar laag niveau terug te brengen,",
    "rationale_snippet": ""
  },
  {
    "id": "regelmatigheid-jaarrekening-audit",
    "naam": "Regelmatigheid van de jaarrekening (audit-perspectief)",
    "node_type": "beginsel",
    "definitie_snippet": "Naast 'getrouw beeld' beoordeelt de auditor ook de REGELMATIGHEID van de boekhouding en jaarrekening: zijn ze opgesteld in overeenstemming met de wettelijke en reglementaire voorschriften (KB WVV, CBN-adviezen, sectorspecifieke regels)? Dit is een aparte dimensie van het oordeel — een jaarrekening k",
    "rationale_snippet": ""
  },
  {
    "id": "risico-inschatting-audit",
    "naam": "Risico-inschatting (audit)",
    "node_type": "procedure",
    "definitie_snippet": "De beroepsbeoefenaar identificeert en schat de risico's op een afwijking van materieel belang in op het niveau van de financiële overzichten én op het niveau van de beweringen (assertions), als gevolg van fraude of fouten. Hij doet dit door inzicht te verwerven in de cliënt en haar omgeving — inclus",
    "rationale_snippet": ""
  },
  {
    "id": "samenstellingsopdracht-isrs4410",
    "naam": "Samenstellingsopdracht (ISRS 4410)",
    "node_type": "procedure",
    "definitie_snippet": "Bij een samenstellingsopdracht (ISRS 4410) past de gecertificeerd accountant zijn vakkennis inzake financiële verslaggeving en boekhoudkundige verwerking toe om het management bij te staan bij het opmaken en presenteren van historische financiële informatie zonder een assurance-oordeel uit te brenge",
    "rationale_snippet": ""
  },
  {
    "id": "schriftelijke-bevestiging-management",
    "naam": "Schriftelijke bevestiging van het management (management representation letter)",
    "node_type": "begrip",
    "definitie_snippet": "Een schriftelijke bevestiging is een schriftelijke verklaring van het management — verstrekt aan de beroepsbeoefenaar — met als doel bepaalde aangelegenheden te bevestigen of andere assurance-informatie te onderbouwen. Schriftelijke bevestigingen omvatten NIET de financiële overzichten zelf, niet de",
    "rationale_snippet": ""
  },
  {
    "id": "significant-risico-audit",
    "naam": "Significant risico (audit)",
    "node_type": "begrip",
    "definitie_snippet": "Een significant risico is een onderkend en ingeschat risico op een afwijking van materieel belang waaraan — volgens het oordeel van de beroepsbeoefenaar — tijdens de controle SPECIALE aandacht moet worden besteed. Voor zulke risico's altijd substantive procedures plannen, ook als de IC sterk lijkt.",
    "rationale_snippet": ""
  },
  {
    "id": "specifieke-kwesties-automatisering-audit",
    "naam": "Specifieke kwesties bij automatisering (audit-perspectief)",
    "node_type": "begrip",
    "definitie_snippet": "Bij geautomatiseerde boekhoudkundige systemen verschuiven de auditrisico's: meer afhankelijkheid van IT-controles, meer 'embedded' controles in software, complexere audit trails, en specifieke risico's rond toegang, autorisatie en gegevensintegriteit. De auditor moet specifieke kennis hebben van het",
    "rationale_snippet": ""
  },
  {
    "id": "steekproef-audit",
    "naam": "Steekproef bij een audit (audit sampling)",
    "node_type": "methode",
    "definitie_snippet": "Een steekproef bij een audit is het verrichten van controlewerkzaamheden op minder dan 100 % van de elementen binnen een relevante populatie, op zodanige wijze dat alle elementen geselecteerd kunnen worden. Het doel: een redelijke basis krijgen voor conclusies over de hele populatie zonder alles te ",
    "rationale_snippet": ""
  },
  {
    "id": "toetsing-interne-beheersing",
    "naam": "Toetsing van interne beheersing (test of controls)",
    "node_type": "methode",
    "definitie_snippet": "Een toetsing van interne beheersing is een controlemaatregel die de auditor opzet om te evalueren of de interne beheersing van de cliënt werkt zoals beoogd — d.w.z. of zij afwijkingen op het niveau van beweringen voorkomt of tijdig ontdekt en corrigeert.",
    "rationale_snippet": ""
  },
  {
    "id": "verbonden-partijen-audit",
    "naam": "Verbonden partijen (audit-perspectief)",
    "node_type": "regel",
    "definitie_snippet": "De beroepsbeoefenaar verwerft voldoende inzicht in de relaties en transacties met verbonden partijen om (a) eventuele fraude-risicofactoren te onderkennen die uit zulke relaties voortkomen, en (b) op basis van de verzamelde assurance-informatie te besluiten of de financiële overzichten — voor zover ",
    "rationale_snippet": ""
  },
  {
    "id": "werkprogramma-audit",
    "naam": "Werkprogramma / werkschema audit",
    "node_type": "begrip",
    "definitie_snippet": "Een werkprogramma (of werkschema) is een schriftelijke beschrijving van de controlewerkzaamheden die uitgevoerd zullen worden — met aanduiding van wanneer en hoe ze gebeuren en hoeveel tijd ze in beslag nemen. Het is de uitvoeringsblauwdruk van de audit: per assertie, per rekeningsaldo of per transa",
    "rationale_snippet": ""
  },
  {
    "id": "wettelijke-controleopdracht-commissaris",
    "naam": "Wettelijke controleopdracht (commissaris-mandaat)",
    "node_type": "begrip",
    "definitie_snippet": "Een wettelijke controleopdracht is een door of krachtens de wet aan de commissaris (bedrijfsrevisor) opgelegde audit van de jaarrekening van een vennootschap. Verplicht voor grote vennootschappen en Public Interest Entities. Levert een redelijke mate van zekerheid en eindigt op een commissarisversla",
    "rationale_snippet": ""
  }
]
```

## Competentie-summaries

```json
[
  {
    "id": "aanvaarden-audit-opdracht",
    "titel": "Aanvaarden van een audit-opdracht en opmaken van de opdrachtbrief",
    "procedure_grondslag": {
      "wettelijk_pct": 80,
      "praktijk_pct": 20,
      "motivering": "De aanvaarding en opdrachtbrief zijn strak gereguleerd door de ITAA-norm Opdrachtbrief, KB 1998 plichtenleer (art. 17–18 overname van opdracht), de ITAA KMO-controlenorm §29-§50 (randvoorwaarden + onafhankelijkheid) en Wet ITAA 2019 art. 44 (aansprakelijkheid). Eigen oordeel beperkt zich tot de inschatting van integriteit van het management en operationele inrichting (team, ereloon)."
    },
    "gebaseerd_op_concepten": [
      "opdrachtbrief-accountant",
      "randvoorwaarden-controle",
      "opvolging-voorganger-accountant",
      "onafhankelijkheid-externe-accountant",
      "kwaliteitsbeheersing-opdrachtniveau"
    ],
    "eerste_stap": "Toetsen van de randvoorwaarden vóór aanvaarding"
  },
  {
    "id": "beoordelen-getrouw-beeld-en-regelmatigheid",
    "titel": "Beoordelen van regelmatigheid, waarachtigheid en getrouw beeld van de jaarrekening",
    "procedure_grondslag": {
      "wettelijk_pct": 80,
      "praktijk_pct": 20,
      "motivering": "De toetsing aan regelmatigheid (conformiteit met KB WVV-stelsel) en getrouw beeld is wettelijk gestructureerd in art. 3:75 WVV + ITAA KMO-controlenorm §122-§135. Materialiteitsoordeel en hoe ver je gaat in alternatieve presentaties is professioneel oordeel."
    },
    "gebaseerd_op_concepten": [
      "getrouw-beeld-controle",
      "regelmatigheid-jaarrekening-audit",
      "continuiteitsveronderstelling-audit",
      "materieel-belang-audit",
      "assurance-informatie"
    ],
    "eerste_stap": "Toetsen of de jaarrekening regelmatig is opgesteld"
  },
  {
    "id": "communiceren-met-bestuur-en-auditcomite",
    "titel": "Communiceren met audit-comité en bestuur over auditbevindingen",
    "procedure_grondslag": {
      "wettelijk_pct": 70,
      "praktijk_pct": 30,
      "motivering": "Communicatie met de met governance belaste personen is opgelegd door de ITAA KMO-controlenorm §131-§138 + art. 3:75 WVV (verslag) en — voor commissaris bij OOB — door art. 7:99 WVV (auditcomité). Inhoud en frequentie van mondelinge tussentijdse update is professioneel oordeel en praktijkbeleid van het kantoor."
    },
    "gebaseerd_op_concepten": [
      "met-governance-belaste-personen",
      "opdrachtbrief-accountant",
      "kwaliteitsbeheersing-opdrachtniveau",
      "controleverslag-elementen",
      "onafhankelijkheid-externe-accountant"
    ],
    "eerste_stap": "Identificeren wie 'met governance belaste personen' zijn"
  },
  {
    "id": "documenteren-auditdossier",
    "titel": "Documenteren van de revisiewerkzaamheden in het auditdossier",
    "procedure_grondslag": {
      "wettelijk_pct": 80,
      "praktijk_pct": 20,
      "motivering": "De ITAA KMO-controlenorm §41-§50 (en de algemene controlenorm: bewaartermijn 10 jaar versus KMO-norm: 5 jaar) leggen minimuminhoud, vorm en bewaartermijn van het dossier wettelijk vast. Concrete dossier-indeling, naamgeving werkpapieren en gebruik van software (CaseWare, AuditFile) is praktische uitwerking."
    },
    "gebaseerd_op_concepten": [
      "controledocumentatie",
      "kwaliteitsbeheersing-opdrachtniveau",
      "werkprogramma-audit",
      "assurance-informatie"
    ],
    "eerste_stap": "Permanent dossier opbouwen en up-to-date houden"
  },
  {
    "id": "opstellen-auditstrategie-en-werkprogramma",
    "titel": "Opstellen van de auditstrategie en het werkprogramma",
    "procedure_grondslag": {
      "wettelijk_pct": 70,
      "praktijk_pct": 30,
      "motivering": "De auditplanning op twee lagen (strategie + werkprogramma) is wettelijk geregeld in de ITAA KMO-controlenorm §70-§73 en de algemene controlenorm. Concrete teamsamenstelling, timing en allocatie van uren over werkzaamheden is praktisch beheer en valt onder professionele oordeelsvorming."
    },
    "gebaseerd_op_concepten": [
      "auditstrategie",
      "auditplanning",
      "werkprogramma-audit",
      "risico-inschatting-audit",
      "materieel-belang-audit",
      "controledocumentatie"
    ],
    "eerste_stap": "Algemene auditstrategie formuleren"
  },
  {
    "id": "opstellen-controleverslag-en-formuleren-oordeel",
    "titel": "Opstellen van het controleverslag en formuleren van het oordeel",
    "procedure_grondslag": {
      "wettelijk_pct": 85,
      "praktijk_pct": 15,
      "motivering": "Het controleverslag van de commissaris is dwingend gestructureerd door art. 3:75 §1 WVV + Wet ITAA 2019 + ITAA KMO-controlenorm §140-§150 (verplichte rubrieken, ondertekening, toezending). De keuze tussen 'goedkeurend' / 'voorbehoud' / 'afkeurend' / 'onthouding' is bepaald door materialiteit + pervasiviteit — een gestructureerde keuze, niet een vrij oordeel."
    },
    "gebaseerd_op_concepten": [
      "controleverslag-elementen",
      "controleoordeel-types",
      "aangepast-oordeel",
      "paragraaf-ter-benadrukking",
      "paragraaf-overige-aangelegenheden",
      "materieel-belang-audit",
      "getrouw-beeld-controle",
      "wettelijke-controleopdracht-commissaris"
    ],
    "eerste_stap": "Slotsom maken over voldoende geschikt audit-bewijs"
  },
  {
    "id": "selecteren-en-uitvoeren-controle-instrumenten-audit",
    "titel": "Selecteren en uitvoeren van controle-instrumenten (test of controls + gegevensgerichte werkzaamheden)",
    "procedure_grondslag": {
      "wettelijk_pct": 75,
      "praktijk_pct": 25,
      "motivering": "De ITAA KMO-controlenorm §96-§120 + de algemene controlenorm leggen een gesloten lijst van controle-instrumenten op (test of controls, gegevensgerichte werkzaamheden, cijferanalyse, externe bevestiging, steekproef, schriftelijke bevestiging). De keuze + dosering tussen instrumenten is risico-gestuurd professioneel oordeel."
    },
    "gebaseerd_op_concepten": [
      "gegevensgerichte-werkzaamheden",
      "toetsing-interne-beheersing",
      "cijferanalyses-audit",
      "externe-bevestiging-audit",
      "steekproef-audit",
      "schriftelijke-bevestiging-management",
      "beweringen-audit",
      "assurance-informatie"
    ],
    "eerste_stap": "Per bewering een instrument selecteren"
  },
  {
    "id": "toepassen-professional-skepticism-en-deontologie-audit",
    "titel": "Toepassen van professional skepticism en deontologische normen tijdens de audit",
    "procedure_grondslag": {
      "wettelijk_pct": 70,
      "praktijk_pct": 30,
      "motivering": "Professionele kritische instelling, onafhankelijkheid, belangenconflict-vermijding en beroepsgeheim zijn wettelijk geregeld in Wet ITAA 2019 art. 14 + KB 1998 plichtenleer art. 11–13 + ITAA-normen + ITAA-deontologie-beroepsgeheim. De concrete toepassing in dagelijkse oordeelsvorming (welke twijfel pak je verder op, welk waarborgmaatregel kies je) is praktijkbeleid van het kantoor + persoonlijke oordeelsvorming."
    },
    "gebaseerd_op_concepten": [
      "professioneel-kritische-instelling",
      "professionele-oordeelsvorming",
      "onafhankelijkheid-externe-accountant",
      "belangenconflict-accountant",
      "beroepsgeheim-accountant",
      "fraude-versus-fout",
      "itaa-algemene-controlenorm",
      "itaa-kmo-controlenorm"
    ],
    "eerste_stap": "Onafhankelijkheid bewaken doorheen de opdracht"
  },
  {
    "id": "uitvoeren-risico-inschatting-en-materialiteit-audit",
    "titel": "Uitvoeren van risico-inschatting en bepalen van het materieel belang in een audit",
    "procedure_grondslag": {
      "wettelijk_pct": 75,
      "praktijk_pct": 25,
      "motivering": "Het auditrisicomodel en de plicht tot risico-inschatting zijn dwingend opgenomen in de ITAA KMO-controlenorm §75-§95 en de algemene controlenorm. De keuze van het materialiteitspercentage (typisch 0,5–5 %) en de calibratie van inherent + intern-beheersingsrisico per bewering is professionele oordeelsvorming."
    },
    "gebaseerd_op_concepten": [
      "risico-inschatting-audit",
      "auditrisicomodel",
      "materieel-belang-audit",
      "significant-risico-audit",
      "beweringen-audit",
      "fraude-versus-fout",
      "inherent-risico",
      "intern-beheersingsrisico",
      "ontdekkingsrisico"
    ],
    "eerste_stap": "Vaststellen van het materieel belang op jaarrekening-niveau"
  },
  {
    "id": "verwerven-kennis-van-clientonderneming-audit",
    "titel": "Verwerven van kennis van de cliënt en zijn omgeving in een audit-opdracht",
    "procedure_grondslag": {
      "wettelijk_pct": 70,
      "praktijk_pct": 30,
      "motivering": "De ITAA KMO-controlenorm §53-§63 en de algemene controlenorm verplichten een kennisverwerving over de cliënt en zijn omgeving als basis voor de risico-inschatting. Welke informatiebronnen je effectief raadpleegt (interviews, rondgang, sectorrapporten) en hoe diep je gaat per onderwerp, is professionele oordeelsvorming."
    },
    "gebaseerd_op_concepten": [
      "kennis-van-onderneming-omgeving",
      "verbonden-partijen-audit",
      "randvoorwaarden-controle",
      "risico-inschatting-audit",
      "continuiteitsveronderstelling-audit"
    ],
    "eerste_stap": "Externe omgeving en sector in kaart brengen"
  }
]
```

---

## Prompt-referentie (minicursus-glue-v1.md)

# Prompt: Minicursus-glue — Render-fase (v2)

**Doel**: Vul de `<!-- TODO: Opus-glue ... -->` placeholders in de minicursus-skeleton in.

**Model**: claude-opus-4-7 (Opus-subagent)

**Monotoon contract**: Geen feiten-claims, geen wikilinks bedenken, geen wettekst-citaties. **Compact**. Glue is verbindweefsel, geen leerstof.

---

## Jouw rol

Je schrijft minimale, verbindende, pedagogische tekst tussen de deterministisch gerenderde blokken. Je vult GEEN nieuwe feiten in. Je verbindt zonder uit te leggen wat al elders staat.

## Compactheidscontract

Mikt op compacte, dichte tekst zonder kaal te worden. Een intro mag een idee uitwerken, niet enkel benoemen — maar zonder herhaling van wat eronder al staat.

- **Sectie-intro's (oriëntatie / thematisch / competentie)**: typisch 2-3 zinnen. Eén zin als de samenhang voor zich spreekt; vier zinnen als er een echt scharnier-idee uit te leggen valt. Nooit meer dan vier.
- **Leesgids**: 3-4 zinnen — hoe lees je de minicursus, welke logica zit erin.
- **Waarom-po**: 4-6 zinnen — één tot twee beginselen + toepassings-implicaties. Mag ademen, geen wall-of-text.
- **Synthese-stappenplan**: 6-9 zinnen — werkschema-stijl, end-to-end-overzicht.
- **Examenfocus**: 4-6 zinnen — twee tot drie denkpatronen, met voldoende grond om bruikbaar te zijn.
- **Synthese-intro**: 2-3 zinnen die de scharnier expliciteren (wat kwam, wat volgt) zonder de Mermaid-content eronder te herhalen.
- **Bij twijfel**: liever kort en dicht dan opgeklopt — maar niet zo kaal dat de student de pedagogische verbinding moet zelf invullen.

## Anti-fabricatie-regels (hard)

1. **Geen feiten-claims**, geen wetsartikelnummers, geen specifieke percentages of bedragen die je niet in records-summaries ziet.
2. **Geen nieuwe wikilinks verzinnen.** De skeleton bevat ze al.
3. **Geen herhaling van de synthese-record-inhoud.** De Mermaid + kerninzichten staan eronder. Glue-intro voegt scharnier toe, geen overlap.
4. **Rationale = beginselen-inzicht, niet examen-truc.** "Waarom werkt dit zo" — niet "dit wordt vaak gevraagd".
5. **Bij gebrek aan grondslag: kort en neutraal.** Eerder "Dit hoofdstuk behandelt X." dan vrije uitvinding.
6. **Geen oude examen-vragen of percentages opnoemen.** Examenfocus is meta-niveau (welk denkpatroon), niet vraagspoilers.

## Workflow

Open `content/studiemateriaal/<X.Y>-<slug>/minicursus.md` met de Edit-tool. Vervang elke `<!-- TODO: Opus-glue X -->` regel door de bedoelde tekst, in volgorde. Geen JSON-output — direct editen.

## Stijl

- **Toon**: helder, direct, actief — zoals een ervaren collega
- **"Je"-aanspraak**, niet "men" of "de student"
- **Geen bullets in glue-tekst** (bullets staan al in skeleton)
- **Nederlands**
- **Geen euro-bedragen of cast-namen** in glue (die staan in records); generieke termen
- **Geen "hieronder zie je..." of "in de volgende sectie..."** — laat de structuur zelf spreken

## Verificatie

Na invullen:
1. `grep -c "<!-- TODO: Opus-glue" content/studiemateriaal/<X.Y>-*/minicursus.md` moet 0 teruggeven
2. Totale word-count zit doorgaans tussen 700 en 1100 woorden glue-tekst voor heel het document — minder dan de "uitgebreid"-stijl (1500+) maar voldoende ruimte voor pedagogische verbinding.
3. Geen overlap tussen synthese-intro en de synthese-record-inhoud die eronder rendert

Geen commit. De hoofdsessie commit.

