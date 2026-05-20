# Minicursus-glue-run minicursus-run-20260520T144904Z — Instructies voor Opus-subagent

**Programmaonderdeel**: 3.0
**Run-id**: minicursus-run-20260520T144904Z
**Gegenereerd op**: 2026-05-20T14:49:04+00:00

## Jouw taak

Vul de `<!-- TODO: Opus-glue ... -->` placeholders in de skeleton-Markdown in.
Edit de skeleton-Markdown direct (geen JSON-output) volgens de regels in
`prompts/minicursus-glue-v3.md` (parafrase-met-bronlink-contract).

## Input-bestanden

- **Skeleton**: `content/studiemateriaal/3-0-vennootschapsrecht.md`
- **Records-summaries** (203 stuks): zie §Records hieronder
- **Competentie-summaries** (18 stuks): zie §Competenties hieronder

## Kern-regels (samenvatting — volledige regels in §Prompt-referentie hieronder)

- Parafrase MAG, mits wikilink bij elke feitelijke claim in dezelfde zin
- Wikilinks toevoegen naar bestaande records (check vooraf dat ze bestaan)
- Geen feit verzinnen zonder record-grondslag, geen non-existent wikilinks
- Werkwoorden volgen het PO-niveau (zie frontmatter / oriëntatie-callout)
- Bij twijfel: korte neutrale tekst, geen uitvinding

## Records-summaries

```json
[
  {
    "id": "aandeelhoudersovereenkomst",
    "naam": "Aandeelhoudersovereenkomst (SHA)",
    "node_type": "cluster",
    "definitie_snippet": "Een **schriftelijke overeenkomst tussen (een deel van) de aandeelhouders** waarin zij hun **onderlinge rechten en verplichtingen** regelen op een wijze die de statuten aanvult of nuanceert. Typische onderwerpen: **stemgedrag** op de algemene vergadering, **overdrachtsbeperkingen** (lock-up, voorkoop",
    "rationale_snippet": ""
  },
  {
    "id": "aansprakelijkheidsbeperking-bestuurder",
    "naam": "Aansprakelijkheidsbeperking voor bestuurders (cap + exoneratieverbod)",
    "node_type": "regel",
    "definitie_snippet": "Het WVV bouwt sinds 2019 een **tweeluik** voor de bestuurdersaansprakelijkheid op: (a) art. 2:56 voert een **wettelijke maximumlimiet (cap)** in voor het bedrag waarvoor een lid van een bestuursorgaan of een dagelijks bestuurder kan worden veroordeeld; (b) art. 2:57 verbiedt **contractuele of statut",
    "rationale_snippet": ""
  },
  {
    "id": "aansprakelijkheidsgrondslagen-bestuur-vergelijking",
    "naam": "Aansprakelijkheidsgrondslagen in het bestuur — vergelijking oprichter / bestuurder / vereffenaar / feitelijk bestuurder",
    "node_type": "synthese",
    "definitie_snippet": "",
    "rationale_snippet": ""
  },
  {
    "id": "aansprakelijkheidsperiode-bestuurder",
    "naam": "Aansprakelijkheidsperiode van de bestuurder",
    "node_type": "regel",
    "definitie_snippet": "Een bestuurder is **persoonlijk aansprakelijk** voor fouten die hij begaat **terwijl hij in functie is** — niet vroeger, niet later. Het mandaat start bij **aanvaarding van de benoeming** (en is tegenstelbaar aan derden vanaf de **publicatie in het Belgisch Staatsblad**); het eindigt bij **ontslag**",
    "rationale_snippet": ""
  },
  {
    "id": "aanwezigheidsrecht-algemene-vergadering",
    "naam": "Aanwezigheidsrecht op de algemene vergadering",
    "node_type": "cluster",
    "definitie_snippet": "Het aanwezigheidsrecht is het recht om de algemene vergadering bij te wonen — fysiek, elektronisch op afstand of bij volmacht. Het WVV onderscheidt drie aanwezigheidsregimes: volwaardige aandeelhouders (stem- en spreekrecht), houders van andere effecten die met raadgevende stem mogen bijwonen, en de",
    "rationale_snippet": ""
  },
  {
    "id": "accountantsrol-bij-vennootschapsconflict",
    "naam": "Rol van de accountant bij een vennootschapsconflict bij de cliënt",
    "node_type": "regel",
    "definitie_snippet": "Wanneer een vennootschapsconflict ontstaat bij een cliënt, geldt voor de accountant dat hij (1) zijn cliënt de **rechtspersoon** is en niet de individuele aandeelhouder of bestuurder, (2) hij een **belangenconflict** moet identificeren en evalueren zodra hij voor twee partijen werkt met tegengesteld",
    "rationale_snippet": ""
  },
  {
    "id": "adviseren-ontbindingsroute-vennootschap",
    "naam": "Adviseren over de ontbindingsroute van een vennootschap (vrijwillig, gerechtelijk, één-akte, klassiek)",
    "node_type": "competentie",
    "definitie_snippet": "",
    "rationale_snippet": ""
  },
  {
    "id": "adviseren-overdrachtsroute-onderneming",
    "naam": "Adviseren over de overdrachtsroute van een onderneming (asset deal, share deal, fusie, splitsing)",
    "node_type": "competentie",
    "definitie_snippet": "",
    "rationale_snippet": ""
  },
  {
    "id": "adviseren-vennootschapsvormkeuze",
    "naam": "Adviseren over de keuze van vennootschapsvorm bij oprichting",
    "node_type": "competentie",
    "definitie_snippet": "",
    "rationale_snippet": ""
  },
  {
    "id": "afgeschafte-vennootschapsvormen",
    "naam": "Afgeschafte vennootschapsvormen onder WVV 2019",
    "node_type": "begrip",
    "definitie_snippet": "Vier vormen werden afgeschaft door het WVV 2019 (art. 1:5 + MvT bij art. 1:2): de coöperatieve vennootschap met onbeperkte aansprakelijkheid (**CVOA**), de commanditaire vennootschap op aandelen (**Comm.VA**), de landbouwvennootschap (**LV**), en het economisch samenwerkingsverband (**ESV**, niet te",
    "rationale_snippet": ""
  },
  {
    "id": "agenderingsrecht-aandeelhouder",
    "naam": "Agenderingsrecht van aandeelhouders",
    "node_type": "regel",
    "definitie_snippet": "Aandeelhouders die in een BV of niet-genoteerde NV ten minste 10% van de uitgegeven aandelen (BV) of het kapitaal (NV) vertegenwoordigen, kunnen het bestuursorgaan verplichten binnen drie weken een algemene vergadering bijeen te roepen met de door hen voorgestelde agendapunten. In een genoteerde NV ",
    "rationale_snippet": ""
  },
  {
    "id": "alarmbelprocedure",
    "naam": "Alarmbelprocedure",
    "node_type": "cluster",
    "definitie_snippet": "De **alarmbelprocedure** is een dwingend wettelijk waarschuwingsmechanisme dat in werking treedt zodra het bestuursorgaan vaststelt dat het vermogen van de vennootschap onder een kritieke drempel zakt of dat de continuïteit ernstig in het gedrang dreigt te komen. Het bestuur moet binnen een korte te",
    "rationale_snippet": ""
  },
  {
    "id": "algemene-vergadering",
    "naam": "Algemene vergadering",
    "node_type": "cluster",
    "definitie_snippet": "De algemene vergadering is het collegiaal orgaan waarin de aandeelhouders (of vennoten bij een CV) hun door de wet en de statuten voorbehouden bevoegdheden uitoefenen. Zij komt minstens één keer per jaar bijeen (de gewone algemene vergadering of jaarvergadering) en kan daarnaast als bijzondere of bu",
    "rationale_snippet": ""
  },
  {
    "id": "alternatieve-geschilbeslechting-vennootschap",
    "naam": "Alternatieve geschilbeslechting in vennootschapsconflicten",
    "node_type": "cluster",
    "definitie_snippet": "Alternatieve geschilbeslechting in vennootschapsconflicten omvat de niet-rechterlijke procedures waarbij partijen — meestal op basis van een contractuele clausule — een neutrale derde inschakelen om hun conflict op te lossen: **arbitrage** (bindend vonnis door arbiter(s)), **mediation** (gefacilitee",
    "rationale_snippet": ""
  },
  {
    "id": "asset-deal-versus-share-deal",
    "naam": "Asset deal versus share deal",
    "node_type": "synthese",
    "definitie_snippet": "",
    "rationale_snippet": ""
  },
  {
    "id": "begeleiden-due-diligence-overname",
    "naam": "Begeleiden van due diligence bij overname (verkoper- of koperszijde)",
    "node_type": "competentie",
    "definitie_snippet": "",
    "rationale_snippet": ""
  },
  {
    "id": "begeleiden-inbreng-bij-oprichting",
    "naam": "Begeleiden van de inbreng in geld en in natura bij oprichting",
    "node_type": "competentie",
    "definitie_snippet": "",
    "rationale_snippet": ""
  },
  {
    "id": "begeleiden-registratie-onderneming-kbo",
    "naam": "Begeleiden van de registratie van een nieuwe onderneming (KBO, btw, UBO)",
    "node_type": "competentie",
    "definitie_snippet": "",
    "rationale_snippet": ""
  },
  {
    "id": "begeleiden-vereffening-vennootschap",
    "naam": "Begeleiden van de vereffening van een vennootschap (staat van activa/passiva tot sluiting)",
    "node_type": "competentie",
    "definitie_snippet": "",
    "rationale_snippet": ""
  },
  {
    "id": "begeleiden-waardering-onderneming-bij-overdracht",
    "naam": "Begeleiden van de waardering van een onderneming bij overdracht",
    "node_type": "competentie",
    "definitie_snippet": "",
    "rationale_snippet": ""
  },
  {
    "id": "behoorlijke-vervulling-bestuursopdracht",
    "naam": "Behoorlijke vervulling van de bestuursopdracht",
    "node_type": "regel",
    "definitie_snippet": "Elk lid van een **bestuursorgaan** en elke **dagelijks bestuurder** is tegenover de rechtspersoon gehouden tot een **behoorlijke vervulling** van de hem opgedragen taak (art. 2:51 WVV). Schending van die zorgvuldigheidsplicht is een **mandaatfout** die de **vennootschap** recht geeft op schadevergoe",
    "rationale_snippet": ""
  },
  {
    "id": "belangenconflict-aandeelhouder",
    "naam": "Belangenconflict van een aandeelhouder",
    "node_type": "regel",
    "definitie_snippet": "Aandeelhouders zonder stemrecht of aandeelhouders van wie het stemrecht is geschorst worden niet meegeteld voor de vaststelling van aanwezigheids- en meerderheidsdrempels. Daarnaast voorziet het WVV specifieke stemverboden voor aandeelhouders met een persoonlijk strijdig belang, bv. bij een geschil ",
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
    "id": "belangenconflict-bestuurder-bv-cv",
    "naam": "Belangenconflict van een bestuurder in BV en CV",
    "node_type": "cluster",
    "definitie_snippet": "Het belangenconflict-regime in BV en CV verplicht een bestuurder met een rechtstreeks of onrechtstreeks vermogensrechtelijk belang dat strijdig is met dat van de vennootschap om dit vooraf mee te delen en zich te onthouden. De vermogensrechtelijke gevolgen en de verantwoording van het besluit worden",
    "rationale_snippet": ""
  },
  {
    "id": "belangenconflict-bestuurder-vzw-stichting",
    "naam": "Belangenconflict van een bestuurder in vzw en stichting",
    "node_type": "cluster",
    "definitie_snippet": "Het belangenconflict-regime voor vzw's (art. 9:8) en stichtingen (art. 11:8-11:9) verplicht een bestuurder met een rechtstreeks of onrechtstreeks vermogensrechtelijk belang dat strijdig is met dat van de vereniging of stichting om dit vooraf mee te delen en zich te onthouden van beraadslaging en ste",
    "rationale_snippet": ""
  },
  {
    "id": "belangenconflict-bestuurder",
    "naam": "Belangenconflict van een bestuurder",
    "node_type": "cluster",
    "definitie_snippet": "Een belangenconflict van een bestuurder is een rechtstreeks of onrechtstreeks vermogensrechtelijk belang van die bestuurder dat strijdig is met het belang van de vennootschap, naar aanleiding van een beslissing of een verrichting die tot de bevoegdheid van het bestuursorgaan behoort. Het WVV verplic",
    "rationale_snippet": ""
  },
  {
    "id": "beperkte-aansprakelijkheid-vennoot",
    "naam": "Beperkte aansprakelijkheid van vennoten/aandeelhouders",
    "node_type": "begrip",
    "definitie_snippet": "Beperkte aansprakelijkheid betekent dat een aandeelhouder/vennoot tegenover de schuldeisers van de vennootschap **slechts zijn inbreng verbindt** — hij kan nooit méér verliezen dan wat hij heeft ingebracht of beloofd in te brengen. Zijn persoonlijk vermogen blijft afgescheiden.",
    "rationale_snippet": ""
  },
  {
    "id": "beroepsverbod-na-insolventie",
    "naam": "Beroepsverbod na faillissement",
    "node_type": "regel",
    "definitie_snippet": "De insolventierechtbank kan, naar aanleiding van een faillissement, een gefailleerde (of een met hem gelijkgestelde bestuurder/zaakvoerder) bij **met redenen omkleed vonnis** een **beroepsverbod** opleggen om persoonlijk of via een tussenpersoon (i) een onderneming uit te baten, of (ii) de functie v",
    "rationale_snippet": ""
  },
  {
    "id": "beslisboom-remedie-vennootschapsconflict",
    "naam": "Beslisboom voor remedie-keuze bij een vennootschapsconflict",
    "node_type": "synthese",
    "definitie_snippet": "Beslisboom die op basis van doel (geld, exit, sanering, ontbinding), positie van de cliënt (minderheid of meerderheid) en vennootschapstype (BV, NV, genoteerd) tot de meest geschikte juridische remedie leidt.",
    "rationale_snippet": ""
  },
  {
    "id": "besloten-vennootschap-bv",
    "naam": "Besloten vennootschap (BV)",
    "node_type": "cluster",
    "definitie_snippet": "De besloten vennootschap is een vennootschap **zonder kapitaal** waarin de aandeelhouders slechts hun inbreng verbinden (WVV art. 5:1). Ze wordt opgericht door één of meer personen, vereist een notariële oprichtingsakte met financieel plan, en de aandelen zijn principieel niet vrij overdraagbaar (va",
    "rationale_snippet": ""
  },
  {
    "id": "besloten-voorbereiding-faillissement",
    "naam": "Besloten voorbereiding van het faillissement (pre-pack)",
    "node_type": "cluster",
    "definitie_snippet": "Vertrouwelijke procedure waarin een schuldenaar die meent in staat van faillissement te verkeren, de bevoegde rechtbank vraagt om de overgang van het geheel of een gedeelte van zijn activa en activiteiten **voor te bereiden** vóór de eigenlijke faillietverklaring. De rechtbank wijst een **beoogd cur",
    "rationale_snippet": ""
  },
  {
    "id": "bestuur-bv-cv-werkwijze",
    "naam": "Werkwijze van het bestuur in BV en CV",
    "node_type": "cluster",
    "definitie_snippet": "Standaardregel in BV en CV: elke bestuurder oefent afzonderlijk de volle bestuursbevoegdheid uit (\"ieder alleen\"). De statuten kunnen die bevoegdheid intern verdelen of beperken — die beperkingen werken niet jegens derden — of kunnen bepalen dat de bestuurders een collegiaal bestuursorgaan vormen. I",
    "rationale_snippet": ""
  },
  {
    "id": "bestuurdersaansprakelijkheid-bij-insolventie",
    "naam": "Bestuurdersaansprakelijkheid bij insolventie (kennelijk grove fout)",
    "node_type": "regel",
    "definitie_snippet": "Wanneer een vennootschap **failliet** wordt verklaard en de schulden de baten overschrijden, kunnen de **huidige of gewezen bestuurders**, **dagelijkse bestuurders**, **leden van een directieraad of raad van toezicht** en **alle personen die werkelijke bestuursbevoegdheid** hebben gehad, persoonlijk",
    "rationale_snippet": ""
  },
  {
    "id": "bestuurdersaansprakelijkheid-bij-onrechtmatige-uitkering",
    "naam": "Bestuurdersaansprakelijkheid bij onrechtmatige uitkering",
    "node_type": "regel",
    "definitie_snippet": "Wanneer komt vast te staan dat de leden van het bestuursorgaan bij het besluit tot **uitkering uit het eigen vermogen** (dividend, terugbetaling inbreng, inkoop eigen aandelen, ...) **wisten** of, gezien de omstandigheden, **behoorden te weten** dat de vennootschap door die uitkering kennelijk niet ",
    "rationale_snippet": ""
  },
  {
    "id": "bestuurdersaansprakelijkheid-fiscale-schulden",
    "naam": "Bestuurdersaansprakelijkheid voor fiscale schulden (bedrijfsvoorheffing, btw)",
    "node_type": "regel",
    "definitie_snippet": "Bestuurders, zaakvoerders en personen met werkelijke bestuursbevoegdheid kunnen persoonlijk en **hoofdelijk** aansprakelijk worden gesteld voor onbetaalde **bedrijfsvoorheffing** en **btw** wanneer hun **fout** bij het bestuur tot de niet-betaling heeft geleid (art. 442quater WIB92 voor bedrijfsvoor",
    "rationale_snippet": ""
  },
  {
    "id": "bestuurdersaansprakelijkheid-sociale-schulden",
    "naam": "Bestuurdersaansprakelijkheid voor sociale schulden bij faillissement",
    "node_type": "regel",
    "definitie_snippet": "Wanneer een vennootschap failliet wordt verklaard en zij op het ogenblik van de faillietverklaring **onbetaalde sociale bijdragen** (RSZ) heeft, kunnen de huidige of gewezen bestuurders, zaakvoerders, dagelijkse bestuurders, leden van een directieraad of raad van toezicht én **alle personen met werk",
    "rationale_snippet": ""
  },
  {
    "id": "bestuurdersaansprakelijkheid",
    "naam": "Bestuurdersaansprakelijkheid",
    "node_type": "cluster",
    "definitie_snippet": "**Bestuurdersaansprakelijkheid** is het geheel van regels op grond waarvan een lid van het **bestuursorgaan**, een **dagelijks bestuurder** of een **feitelijk bestuurder** persoonlijk kan worden veroordeeld om schade te vergoeden aan de **vennootschap**, aan **aandeelhouders/vennoten** of aan **derd",
    "rationale_snippet": ""
  },
  {
    "id": "bestuurdersaansprakelijkheidsverzekering",
    "naam": "Bestuurdersaansprakelijkheidsverzekering (D&O)",
    "node_type": "begrip",
    "definitie_snippet": "Een **bestuurdersaansprakelijkheidsverzekering** (in de praktijk: **D&O-polis**) is een verzekering die de **persoonlijke vermogensschade** dekt die een bestuurder, dagelijks bestuurder of lid van een bestuursorgaan oploopt door **civielrechtelijke aansprakelijkheid** uit hoofde van zijn mandaat. De",
    "rationale_snippet": ""
  },
  {
    "id": "bestuursmodel-vennootschap",
    "naam": "Bestuursmodellen voor de vennootschap — vergelijking",
    "node_type": "synthese",
    "definitie_snippet": "",
    "rationale_snippet": ""
  },
  {
    "id": "bestuursorgaan",
    "naam": "Bestuursorgaan",
    "node_type": "cluster",
    "definitie_snippet": "Het bestuursorgaan is het door de wet en de statuten aangewezen orgaan dat instaat voor het algemeen bestuur van een vennootschap: het neemt de strategische en operationele beslissingen die niet aan de algemene vergadering zijn voorbehouden, en vertegenwoordigt de vennootschap jegens derden. De conc",
    "rationale_snippet": ""
  },
  {
    "id": "bevestiging-vereffenaar-deficitaire-vereffening",
    "naam": "Bevestiging van de vereffenaar bij deficitaire vereffening",
    "node_type": "regel",
    "definitie_snippet": "**Bevestiging van de vereffenaar** is de tussenkomst van de **voorzitter van de ondernemingsrechtbank** die vereist is wanneer uit de staat van activa en passiva blijkt dat **niet alle schuldeisers volledig kunnen worden terugbetaald** (deficitaire vereffening). In dat geval kan de door de AV (of do",
    "rationale_snippet": ""
  },
  {
    "id": "bevoegdheid-bestuursorgaan",
    "naam": "Residuaire bevoegdheid van het bestuursorgaan",
    "node_type": "regel",
    "definitie_snippet": "Het bestuursorgaan is bevoegd om alle handelingen te verrichten die nodig of dienstig zijn voor de verwezenlijking van het voorwerp van de vennootschap, behoudens die handelingen waarvoor de wet de algemene vergadering bevoegd verklaart. De statuten kunnen de bevoegdheden van het bestuursorgaan bepe",
    "rationale_snippet": ""
  },
  {
    "id": "bijeenroeping-algemene-vergadering",
    "naam": "Bijeenroeping van de algemene vergadering",
    "node_type": "cluster",
    "definitie_snippet": "De bijeenroeping is de formele uitnodiging van de aandeelhouders en andere stemgerechtigden tot de algemene vergadering. Het bestuursorgaan en, in voorkomend geval, de commissaris doen die oproep en bepalen de agenda. De oproeping wordt minstens vijftien dagen vóór de vergadering meegedeeld; in een ",
    "rationale_snippet": ""
  },
  {
    "id": "bijzondere-algemene-vergadering",
    "naam": "Bijzondere algemene vergadering",
    "node_type": "begrip",
    "definitie_snippet": "Een bijzondere algemene vergadering is een algemene vergadering die niet de jaarvergadering is en die geen statutenwijziging of andere materie behandelt die voor de buitengewone vergadering is voorbehouden. Zij wordt samengeroepen volgens de gewone regels (oproepingstermijn van vijftien dagen) en st",
    "rationale_snippet": ""
  },
  {
    "id": "bijzondere-mandaten-accountant",
    "naam": "Bijzondere wettelijke mandaten van de gecertificeerd accountant in vennootschappen zonder commissaris",
    "node_type": "cluster",
    "definitie_snippet": "",
    "rationale_snippet": ""
  },
  {
    "id": "boekhoudkundige-verwerking-insolventie-akkoord",
    "naam": "Boekhoudkundige verwerking van een insolventie-akkoord",
    "node_type": "regel",
    "definitie_snippet": "Volgens **CBN-advies 2021/07** verwerkt de schuldenaar een kwijtschelding van schuld die voortvloeit uit een buitengerechtelijk minnelijk akkoord of een gehomologeerd reorganisatieplan als een **uitzonderlijke opbrengst** (rekening 76 — uitzonderlijke opbrengsten, in voorkomend geval rekening 763 — ",
    "rationale_snippet": ""
  },
  {
    "id": "buitengerechtelijk-minnelijk-akkoord",
    "naam": "Buitengerechtelijk minnelijk akkoord",
    "node_type": "begrip",
    "definitie_snippet": "Vrijwillig akkoord waarbij de schuldenaar aan **minstens twee schuldeisers** een regeling voorstelt met het oog op de gezondmaking van zijn financiële toestand of de reorganisatie van zijn onderneming. De partijen bepalen vrij de inhoud van het akkoord — geen tussenkomst van een rechter, geen opscho",
    "rationale_snippet": ""
  },
  {
    "id": "buitengewone-algemene-vergadering",
    "naam": "Buitengewone algemene vergadering",
    "node_type": "cluster",
    "definitie_snippet": "De buitengewone algemene vergadering is de algemene vergadering die bevoegd is voor statutenwijzigingen (inclusief kapitaalbewegingen NV, wijziging voorwerp/doelen, omzetting van rechtsvorm, ontbinding). Zij vereist een notariële akte (uitgezonderd bepaalde verrichtingen in CV en de specifieke geval",
    "rationale_snippet": ""
  },
  {
    "id": "certificering-aandelen",
    "naam": "Certificering van aandelen (STAK)",
    "node_type": "cluster",
    "definitie_snippet": "Een **contractuele verrichting** waarbij de **aandelen** (of obligaties, inschrijvingsrechten) van een vennootschap worden overgedragen aan een **emittent** (typisch een **administratiekantoor** of stichting), die in ruil **certificaten** uitgeeft aan de oorspronkelijke aandeelhouders. De emittent o",
    "rationale_snippet": ""
  },
  {
    "id": "closing-condities-precedent",
    "naam": "Opschortende voorwaarden bij overname (closing conditions)",
    "node_type": "cluster",
    "definitie_snippet": "Opschortende voorwaarden (conditions precedent of CPs) zijn voorwaarden die in de overnameovereenkomst worden gestipuleerd en waarvan de vervulling vereist is voordat closing — de daadwerkelijke uitvoering van de overdracht — kan plaatsvinden.",
    "rationale_snippet": ""
  },
  {
    "id": "confidentiality-overname",
    "naam": "Vertrouwelijkheidsovereenkomst bij overname",
    "node_type": "begrip",
    "definitie_snippet": "Een vertrouwelijkheidsovereenkomst (non-disclosure agreement, NDA) is het contract waarin partijen zich verbinden om informatie die ze in het kader van overnamebesprekingen ontvangen niet te gebruiken voor andere doeleinden en niet aan derden mee te delen, gedurende een bepaalde periode.",
    "rationale_snippet": ""
  },
  {
    "id": "confirmatiebrieven",
    "naam": "Confirmatiebrieven",
    "node_type": "begrip",
    "definitie_snippet": "Confirmatiebrieven (Engels: external confirmations, ook accountantsbevestigingen genoemd) zijn schriftelijke verklaringen die de accountant rechtstreeks bij een derde partij opvraagt om een element van de jaarrekening of een staat van activa en passiva te verifiëren. Typische adressaten zijn banken ",
    "rationale_snippet": ""
  },
  {
    "id": "controleverslag-omzetting",
    "naam": "Controleverslag bij omzetting van een vennootschap",
    "node_type": "regel",
    "definitie_snippet": "Bij elke omzetting van een vennootschap (Boek 14 WVV) moet een controleverslag worden opgesteld over de door het bestuursorgaan opgestelde staat van activa en passiva. Het verslag wordt opgemaakt door de commissaris of, bij afwezigheid van een commissaris, door een bedrijfsrevisor of gecertificeerd ",
    "rationale_snippet": ""
  },
  {
    "id": "controleverwerving-methodes",
    "naam": "Methodes om controle over een vennootschap te verwerven",
    "node_type": "synthese",
    "definitie_snippet": "Een gestructureerd overzicht van de **kanalen** waarlangs een persoon of vennootschap **controle** kan verwerven over een doelvennootschap: directe meerderheid, indirecte controle via een houdster, controle via certificering, controle via stemafspraken, controle via aandelenklassen met meervoudig st",
    "rationale_snippet": ""
  },
  {
    "id": "cooperatieve-vennootschap-cv",
    "naam": "Coöperatieve vennootschap (CV)",
    "node_type": "cluster",
    "definitie_snippet": "De coöperatieve vennootschap heeft tot **voornaamste doel** aan de behoeften van haar aandeelhouders te voldoen en/of hun economische en sociale activiteiten te ontwikkelen, onder meer door met hen overeenkomsten te sluiten over de levering van goederen, het verrichten van diensten of de uitvoering ",
    "rationale_snippet": ""
  },
  {
    "id": "curator-faillissement",
    "naam": "Curator in een faillissement",
    "node_type": "autoriteit",
    "definitie_snippet": "Gerechtsmandataris die door de insolventierechtbank bij het vonnis van faillietverklaring wordt aangesteld om het vermogen van de gefailleerde te **beheren** en te **vereffenen** en de opbrengst te verdelen onder de schuldeisers. De curator is geen partij in het faillissement maar een orgaan dat de ",
    "rationale_snippet": ""
  },
  {
    "id": "dagelijks-bestuur",
    "naam": "Dagelijks bestuur",
    "node_type": "cluster",
    "definitie_snippet": "Het dagelijks bestuur omvat alle handelingen en beslissingen die niet verder reiken dan de behoeften van het dagelijks leven van de vennootschap, evenals handelingen en beslissingen die door hun gering belang of hun spoedeisend karakter de tussenkomst van het bestuursorgaan (raad van bestuur, enige ",
    "rationale_snippet": ""
  },
  {
    "id": "deadlock-vennootschap",
    "naam": "Deadlock in een vennootschap",
    "node_type": "begrip",
    "definitie_snippet": "Een deadlock is een situatie van blijvende blokkering van de besluitvorming in een vennootschapsorgaan (algemene vergadering of bestuur), doorgaans omdat twee groepen aandeelhouders of bestuurders met gelijke of complementaire stemkracht permanent tegenovergestelde posities innemen. Het is geen rech",
    "rationale_snippet": ""
  },
  {
    "id": "deskundigenonderzoek-vennootschap",
    "naam": "Deskundigenonderzoek in een vennootschap",
    "node_type": "regel",
    "definitie_snippet": "Op verzoek van één of meer aandeelhouders die **ten minste 10%** van de uitgegeven aandelen bezitten, kan de voorzitter van de ondernemingsrechtbank, in kort geding, **één of meer deskundigen aanstellen** om de boeken en de rekeningen van de vennootschap én de verrichtingen van haar organen na te zi",
    "rationale_snippet": ""
  },
  {
    "id": "doorbraak-aansprakelijkheid",
    "naam": "Doorbraak van aansprakelijkheid",
    "node_type": "begrip",
    "definitie_snippet": "**Doorbraak van aansprakelijkheid** is de **uitzonderlijke** rechtsfiguur waarbij de rechter het beginsel van **beperkte aansprakelijkheid** van aandeelhouders/vennoten doorbreekt en hen persoonlijk laat opdraaien voor de schulden van de vennootschap. De Belgische rechtspraak past dit terughoudend t",
    "rationale_snippet": ""
  },
  {
    "id": "drag-along-tag-along",
    "naam": "Meesleeprecht (drag-along) versus meekooprecht (tag-along)",
    "node_type": "synthese",
    "definitie_snippet": "**Drag-along** (meesleeprecht): aandeelhouder boven een drempel kan de andere aandeelhouders **dwingen** mee te verkopen aan dezelfde derde-koper en aan dezelfde voorwaarden — zo wordt **100%** van de aandelen verkocht. **Tag-along** (meekooprecht): wanneer een aandeelhouder verkoopt, hebben de ande",
    "rationale_snippet": ""
  },
  {
    "id": "duaal-bestuur",
    "naam": "Duaal bestuur — raad van toezicht en directieraad",
    "node_type": "cluster",
    "definitie_snippet": "Het duale bestuursmodel in de NV bestaat uit twee verplicht gescheiden collegiale organen: een raad van toezicht en een directieraad, elk met minstens drie leden. De raad van toezicht is exclusief bevoegd voor het algemeen beleid, de strategie, de vaststelling van de jaarrekening en de wettelijke ve",
    "rationale_snippet": ""
  },
  {
    "id": "due-diligence-overname",
    "naam": "Due diligence bij overname",
    "node_type": "cluster",
    "definitie_snippet": "Een due diligence is een gestructureerd, multidisciplinair onderzoek van de doelvennootschap of de over te dragen activa, waarbij koper (buy-side) of verkoper (vendor due diligence) de juridische, financiële, fiscale, commerciële, ESG en operationele situatie in kaart brengt om risico's te identific",
    "rationale_snippet": ""
  },
  {
    "id": "enige-bestuurder",
    "naam": "Enige bestuurder",
    "node_type": "begrip",
    "definitie_snippet": "De enige bestuurder is de persoon die in een NV — krachtens een statutaire keuze — alleen de bestuursbevoegdheid van het bestuursorgaan uitoefent. Hij vervult alle taken die in een monistisch model aan de raad van bestuur toekomen, met aangepaste belangenconflict-procedures: hij legt persoonlijke be",
    "rationale_snippet": ""
  },
  {
    "id": "escrow-en-zekerheidsmechanismen-overname",
    "naam": "Escrow en zekerheidsmechanismen bij overname",
    "node_type": "cluster",
    "definitie_snippet": "Zekerheidsmechanismen bij overname zijn contractuele constructies die garanderen dat de verkoper financieel kan instaan voor vrijwaringsclaims na closing, door een deel van de prijs te blokkeren op een derdenrekening, te koppelen aan een bankgarantie, uit te stellen in tijd, of om te zetten in een v",
    "rationale_snippet": ""
  },
  {
    "id": "exit-mechanismen-sha",
    "naam": "Exit- en deadlock-mechanismen in aandeelhoudersovereenkomsten",
    "node_type": "cluster",
    "definitie_snippet": "Verzamelterm voor **contractuele clausules** die de **uitstap** van een aandeelhouder of de **ontbinding van een patstelling** (deadlock) regelen: **put- en callopties**, **Russian roulette**, **Texas shoot-out**, **good/bad leaver-regelingen** en **deadlock-resolutie**. Doel: een onderhandelde, voo",
    "rationale_snippet": ""
  },
  {
    "id": "exit-routes-onderneming-overzicht",
    "naam": "Exit-routes voor een onderneming: vergelijking en beslisboom",
    "node_type": "synthese",
    "definitie_snippet": "Synthese die de zes hoofdroutes voor het beëindigen of overdragen van een vennootschap naast elkaar zet: verkoop (share/asset deal), fusie of splitsing, opvolging via schenking, vrijwillige ontbinding (één-akte of klassiek), gerechtelijke reorganisatie en faillissement. Voor elk: triggers, randvoorw",
    "rationale_snippet": ""
  },
  {
    "id": "faillissement",
    "naam": "Faillissement",
    "node_type": "cluster",
    "definitie_snippet": "Insolventieprocedure waarbij de **insolventierechtbank** het vermogen van een onderneming die op duurzame wijze is opgehouden te betalen en wier krediet geschokt is, onder de bevoegdheid van een **curator** plaatst. De curator beheert en vereffent dat vermogen en verdeelt de opbrengst onder de schul",
    "rationale_snippet": ""
  },
  {
    "id": "familiale-vennootschap",
    "naam": "Familiale vennootschap",
    "node_type": "begrip",
    "definitie_snippet": "Een **familiale vennootschap** is een vennootschap die volgens de regionale fiscale codex (Vlaamse Codex Fiscaliteit, Brussels Wetboek Successierechten/Registratierechten, Waals Wetboek der Registratie- en Successierechten) een **economische activiteit** voert — handel, industrie, ambacht, landbouw ",
    "rationale_snippet": ""
  },
  {
    "id": "feitelijk-bestuurder",
    "naam": "Feitelijk bestuurder",
    "node_type": "begrip",
    "definitie_snippet": "Een **feitelijk bestuurder** is een persoon die — zonder formeel als lid van het bestuursorgaan benoemd te zijn — **werkelijke bestuursbevoegdheid** uitoefent over de vennootschap (beslissingsmacht, leiding geven aan de operationele activiteit, ondertekening van contracten in eigen naam, ...). Voor ",
    "rationale_snippet": ""
  },
  {
    "id": "financieel-plan-oprichting",
    "naam": "Financieel plan bij oprichting van een kapitaalvennootschap",
    "node_type": "cluster",
    "definitie_snippet": "Document met prognoses en onderbouwing waarmee de oprichters van een kapitaalvennootschap (BV, CV, NV) vóór de oprichting verantwoorden dat het aanvangsvermogen toereikend is voor de voorgenomen activiteit over een periode van ten minste twee jaar.",
    "rationale_snippet": ""
  },
  {
    "id": "financiele-steunverlening",
    "naam": "Financiële steunverlening voor verkrijging van eigen aandelen",
    "node_type": "regel",
    "definitie_snippet": "Een vennootschap mag slechts middelen voorschieten, leningen toestaan of zekerheden stellen met het oog op de verkrijging van haar aandelen, winstbewijzen of certificaten door een **derde**, onder strikte cumulatieve voorwaarden: (1) de verrichting gebeurt onder verantwoordelijkheid van het bestuurs",
    "rationale_snippet": ""
  },
  {
    "id": "gegronde-redenen-vennootschapsgeschil",
    "naam": "Gegronde redenen in vennootschapsgeschillen",
    "node_type": "begrip",
    "definitie_snippet": "Gegronde redenen zijn zwaarwichtige feiten of omstandigheden die zich in de persoon of het gedrag van de verweerder situeren en die de normale voortzetting van de vennootschapsrelatie tussen aandeelhouders onleefbaar of overdreven bezwarend maken. Bij **uitsluiting** moeten de redenen objectief de v",
    "rationale_snippet": ""
  },
  {
    "id": "gerechtelijke-ontbinding",
    "naam": "Gerechtelijke ontbinding",
    "node_type": "regel",
    "definitie_snippet": "De **voorzitter van de ondernemingsrechtbank**, zetelend zoals in kort geding, kan op verzoek van een vennoot, aandeelhouder of belanghebbende derde de ontbinding van een vennootschap uitspreken om **wettige redenen** (art. 2:73 WVV — bv. grove tekortkoming van een aandeelhouder, kwaal die deelname ",
    "rationale_snippet": ""
  },
  {
    "id": "gerechtelijke-reorganisatie-varianten-vergelijking",
    "naam": "Varianten van gerechtelijke reorganisatie — vergelijking",
    "node_type": "synthese",
    "definitie_snippet": "Vergelijkende synthese van de vier procedurele uitwegen die Boek XX WER aanbiedt voor een onderneming met dreigende of feitelijke insolventie — bedoeld om de accountant te helpen kiezen welke variant voor zijn cliënt past.",
    "rationale_snippet": ""
  },
  {
    "id": "gerechtelijke-reorganisatie",
    "naam": "Gerechtelijke reorganisatie",
    "node_type": "cluster",
    "definitie_snippet": "Insolventieprocedure die onder toezicht van de **insolventierechtbank** de continuïteit beoogt van het geheel of een gedeelte van een onderneming in moeilijkheden of van haar activiteiten. De schuldenaar geniet een **opschorting** (moratorium) op middelen van tenuitvoerlegging door schuldeisers. Boe",
    "rationale_snippet": ""
  },
  {
    "id": "gewone-algemene-vergadering",
    "naam": "Gewone algemene vergadering (jaarvergadering)",
    "node_type": "cluster",
    "definitie_snippet": "De gewone algemene vergadering is de jaarlijkse vergadering die het WVV verplicht voorschrijft. Zij behandelt minstens de jaarrekening en stemt afzonderlijk over (a) de goedkeuring van die jaarrekening en (b) de kwijting van bestuurders en, in voorkomend geval, van de commissaris. Andere agendapunte",
    "rationale_snippet": ""
  },
  {
    "id": "heropening-vereffening",
    "naam": "Heropening van de vereffening",
    "node_type": "regel",
    "definitie_snippet": "Wanneer na de sluiting van de vereffening **één of meer actieve vermogensbestanddelen werden vergeten**, kan elke schuldeiser wiens schuldvordering niet integraal werd voldaan de **heropening** van de vereffening vorderen (art. 2:95 § 1 WVV voor vennootschappen; art. 2:125 voor VZW/IVZW; art. 2:138 ",
    "rationale_snippet": ""
  },
  {
    "id": "herstructureringsdeskundige",
    "naam": "Herstructureringsdeskundige",
    "node_type": "autoriteit",
    "definitie_snippet": "Een **gerechtsmandataris** die de ondernemingsrechtbank aanstelt om een onderneming in moeilijkheden te begeleiden bij het tot stand brengen van een minnelijk akkoord of het opstellen en aannemen van een reorganisatieplan. De aanstelling kan gebeuren als **voorlopige maatregel** (art. XX.30 WER), of",
    "rationale_snippet": ""
  },
  {
    "id": "homologatie-collectief-akkoord",
    "naam": "Homologatie van het collectief reorganisatieplan",
    "node_type": "regel",
    "definitie_snippet": "De insolventierechtbank **homologeert** het door de schuldeisers (en in voorkomend geval kapitaalhouders) aangenomen reorganisatieplan **uitsluitend** wanneer aan de wettelijke toetsen is voldaan. Door de homologatie wordt het plan **bindend voor alle betrokken partijen**, ook voor schuldeisers die ",
    "rationale_snippet": ""
  },
  {
    "id": "inbreng-in-natura",
    "naam": "Inbreng in natura",
    "node_type": "regel",
    "definitie_snippet": "Een inbreng in natura is een inbreng in het kapitaal of vermogen van een vennootschap in iets anders dan geld — typisch een onroerend goed, machines, een handelsfonds, vorderingen, immateriële activa of een bedrijfstak. Het WVV vereist dat de inbreng economisch waardeerbaar is (uitgesloten zijn arbe",
    "rationale_snippet": ""
  },
  {
    "id": "inbreng-vennootschap",
    "naam": "Inbreng in een vennootschap",
    "node_type": "begrip",
    "definitie_snippet": "Een inbreng is wat een vennoot bijdraagt aan de vennootschap in ruil voor maatschappelijke rechten (aandelen, deelbewijzen, vennotenaandeel). Drie soorten worden onderscheiden: **inbreng in geld**, **inbreng in natura** (lichamelijke of onlichamelijke goederen), en **inbreng in nijverheid** (arbeid,",
    "rationale_snippet": ""
  },
  {
    "id": "indemnification-overname",
    "naam": "Vrijwaringsmechanisme in overnameovereenkomst",
    "node_type": "cluster",
    "definitie_snippet": "Een vrijwaringsclausule (indemnification) verplicht de verkoper om de koper (en/of de doelvennootschap) schadeloos te stellen voor verlies dat voortvloeit uit een schending van een verklaring of waarborg, of uit een specifiek vermeld risico, binnen contractueel afgebakende beperkingen.",
    "rationale_snippet": ""
  },
  {
    "id": "individueel-controlerecht-aandeelhouder",
    "naam": "Individueel onderzoeks- en controlerecht van de aandeelhouder",
    "node_type": "regel",
    "definitie_snippet": "Wanneer een BV geen commissaris heeft benoemd, beschikt elke aandeelhouder individueel over de onderzoeks- en controlebevoegdheid van een commissaris: hij mag de boeken, rekeningen en stukken inkijken, zich laten bijstaan door een gecertificeerd accountant of bedrijfsrevisor, en de bestuurders bevra",
    "rationale_snippet": ""
  },
  {
    "id": "inkoop-eigen-aandelen-bv",
    "naam": "Inkoop van eigen aandelen door de BV",
    "node_type": "cluster",
    "definitie_snippet": "**Verwerving door de BV van haar eigen aandelen of certificaten** — gelijkgesteld met een uitkering en onderworpen aan dezelfde dubbele uitkeringstest (nettoactief + liquiditeit) die geldt voor elk dividend. Beslissing door de algemene vergadering met statutenwijzigingsmeerderheid, met machtiging aa",
    "rationale_snippet": ""
  },
  {
    "id": "inkoop-eigen-aandelen-nv",
    "naam": "Inkoop van eigen aandelen door de NV",
    "node_type": "cluster",
    "definitie_snippet": "**Verwerving door de naamloze vennootschap van haar eigen aandelen, winstbewijzen of certificaten** — een transactie die gelijkstaat met een uitkering aan de verkopende aandeelhouder. Beslissing door de algemene vergadering met **bijzondere meerderheid** (80 % van de uitgebrachte stemmen, minstens h",
    "rationale_snippet": ""
  },
  {
    "id": "insolventiefunctionaris",
    "naam": "Insolventiefunctionaris",
    "node_type": "begrip",
    "definitie_snippet": "Overkoepelend begrip voor de natuurlijke personen die de insolventierechtbank aanstelt om als rechterlijk mandataris taken uit te voeren in een insolventieprocedure. Boek XX WER gebruikt sinds de hervorming van 2023 de verzamelterm **gerechtsmandataris** voor curator, gerechtelijk bewindvoerder, ver",
    "rationale_snippet": ""
  },
  {
    "id": "insolventieprocedures-belgie",
    "naam": "Insolventieprocedures (Boek XX WER)",
    "node_type": "cluster",
    "definitie_snippet": "Het geheel van wettelijke procedures dat in werking treedt wanneer een onderneming haar schulden niet meer (kan) betaalt. Boek XX van het Wetboek van Economisch Recht (WER) — ingevoegd door de wet van 11 augustus 2017 — verzamelt drie procedure-families: **vroegtijdige waarschuwing en buitengerechte",
    "rationale_snippet": ""
  },
  {
    "id": "insolventietriage-beslisboom",
    "naam": "Insolventietriage — beslisboom",
    "node_type": "synthese",
    "definitie_snippet": "Beslisboom voor de gecertificeerd accountant die geconfronteerd wordt met een cliënt in financiële moeilijkheden: welke procedurele uitweg past bij welke combinatie van symptomen — van vroege signalen tot duurzame staking van betaling.",
    "rationale_snippet": ""
  },
  {
    "id": "interimdividend",
    "naam": "Interimdividend",
    "node_type": "regel",
    "definitie_snippet": "Het **bestuursorgaan** is bevoegd tot uitkering van een **interimdividend** — d.w.z. een tussentijdse winstuitkering — wanneer de **statuten** die bevoegdheid expliciet delegeren, en binnen de grenzen van de uitkeringstests die ook gelden voor het jaarlijks dividend. Het interimdividend wordt geput ",
    "rationale_snippet": ""
  },
  {
    "id": "kamer-ondernemingen-in-moeilijkheden",
    "naam": "Kamer voor ondernemingen in moeilijkheden",
    "node_type": "autoriteit",
    "definitie_snippet": "Een gespecialiseerde kamer binnen de ondernemingsrechtbank die proactief onderzoekt of ondernemingen in financiële moeilijkheden verkeren. Zij krijgt signalen van knipperlichten (achterstand bij RSZ, BTW, niet-neergelegde jaarrekeningen, dagvaardingen) en kan de onderneming uitnodigen voor gesprek.",
    "rationale_snippet": ""
  },
  {
    "id": "kapitaalverhoging-bv",
    "naam": "Bijkomende inbreng en uitgifte van aandelen bij de BV",
    "node_type": "cluster",
    "definitie_snippet": "**Uitgifte van nieuwe aandelen of bijkomende inbreng** in een BV ter versterking van het eigen vermogen. Geen statutair kapitaalbedrag dat verhoogd wordt, maar wel een statutenwijziging wanneer de aandelenstructuur verandert (nieuwe aandelensoort, nieuwe aandeelhouder, gewijzigd aantal aandelen). Be",
    "rationale_snippet": ""
  },
  {
    "id": "kapitaalverhoging-nv",
    "naam": "Kapitaalverhoging bij de NV",
    "node_type": "cluster",
    "definitie_snippet": "**Verhoging van het kapitaal** van een naamloze vennootschap (NV) — waardoor het wettelijk vermogensanker wordt vergroot. Vier vormen: (1) **inbreng in geld**, (2) **inbreng in natura**, (3) **incorporatie van reserves of uitgiftepremies**, (4) uitgifte van **converteerbare obligaties** of **inschri",
    "rationale_snippet": ""
  },
  {
    "id": "kapitaalvermindering-nv",
    "naam": "Kapitaalvermindering bij de NV",
    "node_type": "cluster",
    "definitie_snippet": "**Vermindering van het maatschappelijk kapitaal** van een naamloze vennootschap (NV) — beslist door de algemene vergadering met statutenwijzigingsmeerderheid. Vier vormen: (1) **terugbetaling** aan aandeelhouders, (2) **vrijstelling van volstorting** van het saldo van de inbreng, (3) **aanzuivering ",
    "rationale_snippet": ""
  },
  {
    "id": "kennelijk-ontoereikend-aanvangsvermogen",
    "naam": "Kennelijk ontoereikend aanvangsvermogen (drie-jaars-faillissementsaansprakelijkheid)",
    "node_type": "regel",
    "definitie_snippet": "Wanneer een vennootschap **failliet** wordt verklaard binnen **drie jaar** na de verkrijging van rechtspersoonlijkheid, en het **aanvangsvermogen** bij de oprichting **kennelijk ontoereikend** was voor de normale uitoefening van de voorgenomen bedrijvigheid over **ten minste twee jaar**, dan kan de ",
    "rationale_snippet": ""
  },
  {
    "id": "klassieke-versus-een-akte-vereffening",
    "naam": "Klassieke vereffening vs vereffening in één akte",
    "node_type": "synthese",
    "definitie_snippet": "",
    "rationale_snippet": ""
  },
  {
    "id": "kwijting-bestuurder",
    "naam": "Kwijting van de bestuurder (decharge)",
    "node_type": "begrip",
    "definitie_snippet": "**Kwijting** (of *decharge*) is een besluit van de **algemene vergadering** waarbij zij de leden van het bestuursorgaan **ontslaat** van aansprakelijkheid jegens de vennootschap voor het beheer over het afgesloten boekjaar. Het besluit volgt op de voorlegging van de **jaarrekening** en is — afhankel",
    "rationale_snippet": ""
  },
  {
    "id": "kwijtschelding-natuurlijke-persoon-gefailleerde",
    "naam": "Kwijtschelding van de natuurlijke persoon-gefailleerde",
    "node_type": "regel",
    "definitie_snippet": "De **natuurlijke persoon** die failliet is verklaard, kan op verzoek de **kwijtschelding** van het saldo van zijn schulden verkrijgen — een 'fresh start' na vereffening. De rechtbank weigert of beperkt de kwijtschelding wanneer de gefailleerde **kennelijke grove fouten** heeft begaan die hebben bijg",
    "rationale_snippet": ""
  },
  {
    "id": "letter-of-intent-overname",
    "naam": "Letter of intent / term sheet (overname)",
    "node_type": "begrip",
    "definitie_snippet": "Een letter of intent is een schriftelijke voor-overeenkomst tussen koper en verkoper waarin de hoofdlijnen van een beoogde overname worden vastgelegd (object, indicatieve prijs, structuur, tijdspad, exclusiviteit, vertrouwelijkheid). Hij kan geheel of gedeeltelijk bindend zijn — dit hangt af van de ",
    "rationale_snippet": ""
  },
  {
    "id": "liquidatiebonus",
    "naam": "Liquidatiebonus",
    "node_type": "begrip",
    "definitie_snippet": "De **liquidatiebonus** is het positieve verschil tussen het bedrag dat een aandeelhouder ontvangt bij de sluiting van de vereffening en het **fiscaal gestort kapitaal** van zijn aandelen. Fiscaal wordt zij behandeld als een **dividend** (WIB92 art. 18, 2°ter) en onderworpen aan **30 % roerende voorh",
    "rationale_snippet": ""
  },
  {
    "id": "liquiditeitstest-bv",
    "naam": "Liquiditeitstest (BV/CV)",
    "node_type": "regel",
    "definitie_snippet": "Het besluit van de algemene vergadering tot uitkering heeft slechts uitwerking nadat het **bestuursorgaan** heeft vastgesteld dat de vennootschap, volgens de redelijkerwijs te verwachten ontwikkelingen, na de uitkering in staat zal blijven haar schulden te voldoen naarmate deze opeisbaar worden over",
    "rationale_snippet": ""
  },
  {
    "id": "maatschap-rechtsvorm",
    "naam": "Maatschap",
    "node_type": "cluster",
    "definitie_snippet": "De maatschap is een **overeenkomst** waarbij twee of meer personen zich verbinden om hun nijverheid, geld of andere lichamelijke of onlichamelijke goederen in gemeenschap te brengen, met het oogmerk het rechtstreekse of onrechtstreekse vermogensvoordeel dat daaruit kan ontstaan met elkaar te delen (",
    "rationale_snippet": ""
  },
  {
    "id": "mandaat-versus-advies-rol-accountant",
    "naam": "Onderscheid tussen advies- en mandaatrol van de accountant bij vennootschapsrechtelijke verrichtingen",
    "node_type": "synthese",
    "definitie_snippet": "",
    "rationale_snippet": ""
  },
  {
    "id": "material-adverse-change-clausule",
    "naam": "Material Adverse Change-clausule (MAC)",
    "node_type": "begrip",
    "definitie_snippet": "Een Material Adverse Change-clausule is een contractuele bepaling die de koper toelaat om — wanneer zich tussen signing en closing een wezenlijke negatieve verandering voordoet in de business, activa, financiële toestand of vooruitzichten van de target — het contract op te zeggen, de closing op te s",
    "rationale_snippet": ""
  },
  {
    "id": "meervoudig-stemrecht",
    "naam": "Meervoudig stemrecht en dubbel stemrecht",
    "node_type": "begrip",
    "definitie_snippet": "**Meervoudig stemrecht** geeft aan bepaalde **soorten aandelen** **meer dan één stem** per aandeel — bij niet-genoteerde NV's en BV's kunnen de statuten dit **vrij** regelen (art. 5:42, 7:52 WVV). In **genoteerde NV's** is enkel een **dubbel stemrecht** mogelijk: aandelen die **minstens 2 jaar** op ",
    "rationale_snippet": ""
  },
  {
    "id": "meldingsplicht-accountant-continuiteit",
    "naam": "Meldingsplicht accountant bij bedreigde continuïteit",
    "node_type": "regel",
    "definitie_snippet": "De externe accountant, externe erkend boekhouder, externe erkend boekhouder-fiscalist en bedrijfsrevisor die in de uitoefening van hun opdracht **gewichtige en overeenstemmende feiten** vaststellen die de continuïteit van de economische activiteit van de schuldenaar in het gedrang kunnen brengen, **",
    "rationale_snippet": ""
  },
  {
    "id": "minderheidsvordering",
    "naam": "Minderheidsvordering",
    "node_type": "cluster",
    "definitie_snippet": "Een minderheidsvordering is een aansprakelijkheidsvordering tegen bestuurders (of leden van de raad van toezicht of vereffenaars) die een minderheidsaandeelhouder voor rekening van de vennootschap instelt wanneer de algemene vergadering de kwijting niet of op ongeldige wijze heeft goedgekeurd. De ev",
    "rationale_snippet": ""
  },
  {
    "id": "misbruik-van-meerderheid",
    "naam": "Misbruik van meerderheid",
    "node_type": "begrip",
    "definitie_snippet": "Misbruik van meerderheid is de figuur waarbij de meerderheid in de algemene vergadering haar stemkracht aanwendt voor een besluit dat (a) uitsluitend het belang van de meerderheid (of een specifieke groep) dient, (b) zonder redelijke verhouding tot het belang van de vennootschap, en (c) ten koste va",
    "rationale_snippet": ""
  },
  {
    "id": "misbruik-van-minderheid",
    "naam": "Misbruik van minderheid",
    "node_type": "begrip",
    "definitie_snippet": "Misbruik van minderheid is het gebruik van een blokkerende positie (typisch in besluiten met versterkte meerderheid) door een minderheidsaandeelhouder op een wijze die **geen redelijk vennootschaps- of eigen aandeelhoudersbelang** dient en kennelijk gericht is op het schaden van de vennootschap of d",
    "rationale_snippet": ""
  },
  {
    "id": "monistisch-bestuur",
    "naam": "Monistisch bestuur — raad van bestuur",
    "node_type": "cluster",
    "definitie_snippet": "Bij een monistisch bestuursmodel berust het bestuur van de vennootschap bij één bestuursorgaan: de raad van bestuur in de NV (collegiaal, minstens drie leden), of het bestuursorgaan in de BV en CV. Dit orgaan oefent alle bevoegdheden uit die de wet niet aan de algemene vergadering toewijst, en is be",
    "rationale_snippet": ""
  },
  {
    "id": "naamloze-vennootschap-nv",
    "naam": "Naamloze vennootschap (NV)",
    "node_type": "cluster",
    "definitie_snippet": "De naamloze vennootschap is een vennootschap **met een kapitaal** waarin de aandeelhouders slechts hun inbreng verbinden (WVV art. 7:1). Ze heeft een minimumkapitaal van € 61.500 dat volledig moet worden geplaatst bij oprichting (WVV art. 7:2).",
    "rationale_snippet": ""
  },
  {
    "id": "nettoactieftest",
    "naam": "Nettoactieftest",
    "node_type": "regel",
    "definitie_snippet": "Geen uitkering — dividend, tantième, inkoop eigen aandelen, financiële steunverlening of vergelijkbare verrichting — mag tot stand komen indien daardoor het **nettoactief** van de vennootschap zou dalen onder het niet-uitkeerbaar deel van het eigen vermogen. Voor de **besloten vennootschap (BV)** en",
    "rationale_snippet": ""
  },
  {
    "id": "niet-afwervingsbeding-overname",
    "naam": "Niet-afwervingsbeding bij overname",
    "node_type": "regel",
    "definitie_snippet": "Een niet-afwervingsbeding bij overname verbiedt de verkoper om klanten, leveranciers of personeel van de overgedragen onderneming actief te benaderen of weg te lokken; het is geldig als het redelijk is in tijd en in welomschreven kring van personen, en wordt door de rechtspraak losser getoetst dan h",
    "rationale_snippet": ""
  },
  {
    "id": "nietigverklaring-algemene-vergaderingsbesluit",
    "naam": "Nietigverklaring van een algemene-vergaderingsbesluit",
    "node_type": "regel",
    "definitie_snippet": "Een besluit van de algemene vergadering is **nietig of vernietigbaar** wanneer (i) de oproepings-, agenda-, quorum- of meerderheidsregels werden geschonden, (ii) de stemming aangetast is door bedrog of een ernstige procedure-onregelmatigheid die het resultaat heeft kunnen beïnvloeden, of (iii) het b",
    "rationale_snippet": ""
  },
  {
    "id": "nijverheidsinbreng",
    "naam": "Nijverheidsinbreng",
    "node_type": "begrip",
    "definitie_snippet": "**Nijverheidsinbreng** is de inbreng door een vennoot van zijn arbeid, vaardigheden of toekomstige activiteit ten voordele van de vennootschap. In ruil ontvangt de vennoot **aandelen zonder stemrecht en zonder kapitaalverbonden waarde** — de inbreng telt mee voor het maatschappelijk vermogen maar ni",
    "rationale_snippet": ""
  },
  {
    "id": "non-compete-overname",
    "naam": "Niet-concurrentiebeding bij overname",
    "node_type": "regel",
    "definitie_snippet": "Een niet-concurrentiebeding bij overname is geldig onder Belgisch recht enkel als het cumulatief beperkt is in tijd, in gebied en in scope van activiteiten, en als het beoogt de koper effectief de goodwill van de overgenomen onderneming te laten benutten.",
    "rationale_snippet": ""
  },
  {
    "id": "notulen-algemene-vergadering",
    "naam": "Notulen van de algemene vergadering",
    "node_type": "cluster",
    "definitie_snippet": "De notulen van de algemene vergadering zijn de schriftelijke vastlegging van haar verloop en besluiten, opgesteld door of onder verantwoordelijkheid van het bureau van de vergadering en ondertekend door de leden van het bureau en door de aandeelhouders die erom verzoeken. Kopieën voor derden worden ",
    "rationale_snippet": ""
  },
  {
    "id": "omstandige-staat-vereffening",
    "naam": "Omstandige staat van de vereffening",
    "node_type": "begrip",
    "definitie_snippet": "De **omstandige staat** is een tussentijds verslag dat de vereffenaar in de **7e en 13e maand** na de invereffeningstelling neerlegt bij de griffie van de ondernemingsrechtbank van de zetel — opgesteld respectievelijk per einde zesde en twaalfde maand van het eerste vereffeningsjaar (art. 2:86 WVV).",
    "rationale_snippet": ""
  },
  {
    "id": "omzetting-vennootschap",
    "naam": "Omzetting van een vennootschap",
    "node_type": "cluster",
    "definitie_snippet": "Omzetting van een vennootschap is de operatie waarbij een vennootschap haar rechtsvorm wijzigt (bv. BV → NV, CV → BV, VOF → BV) zonder dat haar rechtspersoonlijkheid wordt onderbroken. De vennootschap behoudt haar boekhouding, haar contracten en haar fiscale identiteit; alleen het juridisch kleed wi",
    "rationale_snippet": ""
  },
  {
    "id": "onafhankelijkheid-bijzondere-mandataris",
    "naam": "Onafhankelijkheid van de gecertificeerd accountant bij bijzondere wettelijke mandaten",
    "node_type": "cluster",
    "definitie_snippet": "",
    "rationale_snippet": ""
  },
  {
    "id": "onafhankelijkheids-beslisboom-bijzondere-mandaten",
    "naam": "Beslisboom — mag ik dit bijzonder mandaat aanvaarden?",
    "node_type": "synthese",
    "definitie_snippet": "",
    "rationale_snippet": ""
  },
  {
    "id": "onbeperkte-aansprakelijkheid-vennoot",
    "naam": "Onbeperkte aansprakelijkheid van vennoten",
    "node_type": "begrip",
    "definitie_snippet": "Onbeperkte aansprakelijkheid betekent dat een vennoot tegenover schuldeisers van de vennootschap **persoonlijk en hoofdelijk** verbonden is voor de schulden — zijn aansprakelijkheid wordt niet begrensd door zijn inbreng en strekt zich uit tot zijn volledig persoonlijk vermogen. **Hoofdelijk** wil ze",
    "rationale_snippet": ""
  },
  {
    "id": "ondernemingsrechtbank-bevoegdheid-insolventie",
    "naam": "Bevoegdheid ondernemingsrechtbank bij insolventie",
    "node_type": "regel",
    "definitie_snippet": "De insolventierechtbank gelegen in het rechtsgebied waar de schuldenaar zijn **centrum van de voornaamste belangen (COMI)** heeft, is **uitsluitend** bevoegd om een insolventieprocedure te openen (art. XX.12 § 1). Voor vennootschappen en rechtspersonen geldt het vermoeden dat de COMI de plaats van d",
    "rationale_snippet": ""
  },
  {
    "id": "ontbinding-van-rechtswege",
    "naam": "Ontbinding van rechtswege",
    "node_type": "regel",
    "definitie_snippet": "Een vennootschap wordt **van rechtswege** ontbonden door een door de wet omschreven feit of gebeurtenis, onverminderd bijzondere bepalingen elders in het WVV. De twee algemene gronden zijn: (1) het **verstrijken van de duur** waarvoor zij is aangegaan, en (2) het zich voordoen van een **statutaire o",
    "rationale_snippet": ""
  },
  {
    "id": "ontbinding-vennootschap",
    "naam": "Ontbinding van een vennootschap",
    "node_type": "cluster",
    "definitie_snippet": "**Ontbinding** is de juridische gebeurtenis die een einde maakt aan de normale werking van een vennootschap en de **vereffeningsfase** opent. De vennootschap **blijft als rechtspersoon bestaan** voor de duur van haar vereffening (art. 2:76 WVV), maar haar bedrijfsdoel verschuift naar het te gelde ma",
    "rationale_snippet": ""
  },
  {
    "id": "oprichtersaansprakelijkheid",
    "naam": "Oprichtersaansprakelijkheid",
    "node_type": "cluster",
    "definitie_snippet": "**Oprichtersaansprakelijkheid** is het samenstel van regels waarbij personen die bij **oprichtingsakte** als oprichter zijn opgetreden (of als zodanig worden gelijkgesteld), **hoofdelijk** aansprakelijk worden gesteld jegens 'belanghebbenden' (vennootschap, aandeelhouders, schuldeisers) voor specifi",
    "rationale_snippet": ""
  },
  {
    "id": "oprichtingsproces-stappenplan",
    "naam": "Stappenplan voor de begeleiding van een vennootschapsoprichting",
    "node_type": "synthese",
    "definitie_snippet": "",
    "rationale_snippet": ""
  },
  {
    "id": "opschorting-besluit-vennootschap",
    "naam": "Opschorting van een vennootschapsbesluit in kort geding",
    "node_type": "regel",
    "definitie_snippet": "De **voorzitter van de ondernemingsrechtbank** kan, in gevallen die hij **spoedeisend** acht en **op vordering van de rechtspersoon of een belanghebbende**, **in kort geding** de **opschorting** van een besluit van een orgaan (algemene vergadering, raad van bestuur, dagelijks bestuur) of van de alge",
    "rationale_snippet": ""
  },
  {
    "id": "opschorting-betaling-gerechtelijke-reorganisatie",
    "naam": "Opschorting van betaling tijdens gerechtelijke reorganisatie",
    "node_type": "regel",
    "definitie_snippet": "Tijdens de **duur van de opschorting** kunnen voor schuldvorderingen in de opschorting geen middelen van tenuitvoerlegging (beslag, gedwongen verkoop) worden voortgezet of aangewend op de roerende of onroerende goederen van de schuldenaar. Tijdens diezelfde periode kan de schuldenaar **niet failliet",
    "rationale_snippet": ""
  },
  {
    "id": "opstellen-beoordelingsverslag-uitsluiting-voorkeurrecht",
    "naam": "Opstellen van het beoordelingsverslag bij uitgifte met uitsluiting of beperking van het voorkeurrecht",
    "node_type": "competentie",
    "definitie_snippet": "",
    "rationale_snippet": ""
  },
  {
    "id": "opstellen-financieel-plan-oprichting",
    "naam": "Opstellen van het financieel plan bij oprichting van een vennootschap",
    "node_type": "competentie",
    "definitie_snippet": "",
    "rationale_snippet": ""
  },
  {
    "id": "opstellen-openingsbalans-vennootschap",
    "naam": "Opstellen van de openingsbalans van een nieuwe vennootschap",
    "node_type": "competentie",
    "definitie_snippet": "",
    "rationale_snippet": ""
  },
  {
    "id": "opstellen-overname-verslaggeving-accountant",
    "naam": "Opstellen van accountantsverslagen bij overdracht (inbreng, quasi-inbreng, fusie, splitsing)",
    "node_type": "competentie",
    "definitie_snippet": "",
    "rationale_snippet": ""
  },
  {
    "id": "opstellen-verslag-fusie-splitsing-ruilverhouding",
    "naam": "Opstellen van het verslag bij fusie, splitsing of gelijkgestelde verrichting in een vennootschap zonder commissaris",
    "node_type": "competentie",
    "definitie_snippet": "",
    "rationale_snippet": ""
  },
  {
    "id": "opstellen-verslag-omzetting-vennootschap",
    "naam": "Opstellen van het verslag over de staat van activa en passiva bij omzetting van een vennootschap (Boek 14 WVV)",
    "node_type": "competentie",
    "definitie_snippet": "",
    "rationale_snippet": ""
  },
  {
    "id": "opstellen-verslag-ontbinding-vereffening-staat",
    "naam": "Opstellen van het verslag over de staat van activa en passiva bij vrijwillige ontbinding of ontbinding-en-sluiting-in-één-akte",
    "node_type": "competentie",
    "definitie_snippet": "",
    "rationale_snippet": ""
  },
  {
    "id": "overdracht-onder-gerechtelijk-gezag",
    "naam": "Overdracht onder gerechtelijk gezag",
    "node_type": "cluster",
    "definitie_snippet": "Insolventieprocedure waarbij de **ondernemingsrechtbank** beveelt dat het geheel of een gedeelte van de activiteiten van een onderneming in moeilijkheden wordt overgedragen aan een derde, met de bedoeling een **efficiënte vereffening** van de rechtspersoon te verzekeren met behoud van de continuïtei",
    "rationale_snippet": ""
  },
  {
    "id": "overdrachtsbeperking-aandelen",
    "naam": "Overdrachtsbeperking op aandelen",
    "node_type": "cluster",
    "definitie_snippet": "Een **overdrachtsbeperking** is een **statutaire of contractuele clausule** die perken stelt aan de mogelijkheid om aandelen, inschrijvingsrechten of certificaten **onder de levenden of bij overlijden** over te dragen. Statutaire beperkingen zijn tegenwerpelijk aan **iedereen** (ook derden te goeder",
    "rationale_snippet": ""
  },
  {
    "id": "overnameovereenkomst",
    "naam": "Overnameovereenkomst",
    "node_type": "cluster",
    "definitie_snippet": "Een overnameovereenkomst is een contract waarmee de verkoper (vendor) de aandelen van een doelvennootschap (share deal) of bepaalde activa en passiva ervan (asset deal) overdraagt aan een koper, in ruil voor een prijs in geld of in eigen aandelen. Naast de prijs regelt het de bescherming van de kope",
    "rationale_snippet": ""
  },
  {
    "id": "personenvennootschap-met-rechtspersoonlijkheid",
    "naam": "Personenvennootschappen met rechtspersoonlijkheid (VOF en CommV)",
    "node_type": "cluster",
    "definitie_snippet": "De **VOF** (vennootschap onder firma) is een vennootschap met rechtspersoonlijkheid waarin alle vennoten onbeperkt en hoofdelijk aansprakelijk zijn voor de schulden. De **CommV** (commanditaire vennootschap) heeft twee soorten vennoten: gecommanditeerde (= beherende) vennoten met onbeperkte en hoofd",
    "rationale_snippet": ""
  },
  {
    "id": "precontractuele-aansprakelijkheid-overname",
    "naam": "Precontractuele aansprakelijkheid bij overname",
    "node_type": "begrip",
    "definitie_snippet": "Precontractuele aansprakelijkheid is de gehoudenheid tot schadevergoeding die ontstaat wanneer een partij tijdens de onderhandelingen vóór het sluiten van een overeenkomst een fout begaat (onverantwoorde afbreking, schending van informatieplicht, gebrek aan goede trouw). De rechtsgrondslag is de alg",
    "rationale_snippet": ""
  },
  {
    "id": "purchase-price-mechanismen",
    "naam": "Prijsbepalingsmechanismen in overnameovereenkomsten",
    "node_type": "synthese",
    "definitie_snippet": "",
    "rationale_snippet": ""
  },
  {
    "id": "quasi-inbreng-verslag",
    "naam": "Verslag bij quasi-inbreng",
    "node_type": "cluster",
    "definitie_snippet": "Het verslag bij quasi-inbreng is een wettelijk voorbehouden opdracht waarbij een commissaris, of bij gebrek daaraan een door het bestuursorgaan aangewezen bedrijfsrevisor, een verslag opstelt over een verwerving door de **naamloze vennootschap** van een vermogensbestanddeel binnen twee jaar na de ve",
    "rationale_snippet": ""
  },
  {
    "id": "quorum-en-meerderheid-statutenwijziging",
    "naam": "Quorum en meerderheid voor statutenwijziging",
    "node_type": "regel",
    "definitie_snippet": "Voor een statutenwijziging in BV, CV of NV gelden cumulatief: (a) de voorgestelde wijzigingen zijn nauwkeurig in de oproeping aangegeven; (b) de aanwezige of vertegenwoordigde aandeelhouders bezitten minstens de helft van de uitgegeven aandelen (BV/CV) of van het kapitaal (NV); (c) de wijziging word",
    "rationale_snippet": ""
  },
  {
    "id": "rechter-commissaris-insolventie",
    "naam": "Rechter-commissaris in een faillissement",
    "node_type": "autoriteit",
    "definitie_snippet": "Rechter van de insolventierechtbank (voorzitter uitgezonderd) die in het vonnis van faillietverklaring wordt aangewezen om **rechterlijk toezicht** te houden op het beheer van het faillissement door de curator. Hij is geen partij maar een toeziende rechter binnen dezelfde rechtbank.",
    "rationale_snippet": ""
  },
  {
    "id": "rechtspersoon-bestuurder-vaste-vertegenwoordiger",
    "naam": "Vaste vertegenwoordiger van een rechtspersoon-bestuurder",
    "node_type": "begrip",
    "definitie_snippet": "De vaste vertegenwoordiger is de natuurlijke persoon die door een rechtspersoon-bestuurder wordt benoemd om diens bestuursmandaat in naam en voor rekening van die rechtspersoon uit te oefenen. Hij oefent dezelfde bevoegdheid uit als de rechtspersoon zelf, is hoofdelijk met haar aansprakelijk en valt",
    "rationale_snippet": ""
  },
  {
    "id": "rechtspersoonlijkheid-vennootschap",
    "naam": "Rechtspersoonlijkheid van een vennootschap",
    "node_type": "begrip",
    "definitie_snippet": "Rechtspersoonlijkheid betekent dat de vennootschap juridisch als een **zelfstandige drager** van rechten en plichten wordt erkend, met een eigen vermogen, eigen contracten en eigen aansprakelijkheid, los van de natuurlijke of rechtspersonen die haar oprichtten of leiden.",
    "rationale_snippet": ""
  },
  {
    "id": "registratiedatum-genoteerde-nv",
    "naam": "Registratiedatum bij genoteerde NV",
    "node_type": "begrip",
    "definitie_snippet": "De registratiedatum is de wettelijke peildatum — de veertiende dag vóór de algemene vergadering om vierentwintig uur Belgisch uur — waarop de hoedanigheid van aandeelhouder van een genoteerde NV wordt vastgesteld voor het uitoefenen van het deelname- en stemrecht. Wie op die datum aandelen op zijn n",
    "rationale_snippet": ""
  },
  {
    "id": "regsol-platform",
    "naam": "Regsol — centraal register insolventie",
    "node_type": "begrip",
    "definitie_snippet": "Het centrale digitale platform waar alle insolventiedossiers (faillissement, gerechtelijke reorganisatie, besloten voorbereiding) worden gevoerd. Boek XX WER noemt het generiek **\"het register\"** (art. XX.15); operationeel draait het onder de naam **Regsol** (regsol.be). Het register geldt als authe",
    "rationale_snippet": ""
  },
  {
    "id": "rehabilitatie-gefailleerde",
    "naam": "Rehabilitatie van de gefailleerde",
    "node_type": "regel",
    "definitie_snippet": "De gefailleerde **natuurlijke persoon** die **geen kwijtschelding** heeft verkregen, kan rehabilitatie verkrijgen wanneer hij **alle nog verschuldigde bedragen** (hoofdsom, interest en kosten) **geheel** heeft voldaan. De rehabilitatie wordt uitgesproken door de ondernemingsrechtbank op tegensprekel",
    "rationale_snippet": ""
  },
  {
    "id": "representations-and-warranties",
    "naam": "Verklaringen en waarborgen",
    "node_type": "cluster",
    "definitie_snippet": "Verklaringen en waarborgen (representations and warranties, R&W) zijn contractuele verklaringen van de verkoper dat bepaalde feiten over de doelvennootschap of de over te dragen activa op een welbepaalde datum waar, volledig, nauwkeurig en niet-misleidend zijn. Een schending van een R&W activeert he",
    "rationale_snippet": ""
  },
  {
    "id": "schriftelijke-besluitvorming-aandeelhouders",
    "naam": "Schriftelijke besluitvorming door aandeelhouders",
    "node_type": "regel",
    "definitie_snippet": "De aandeelhouders kunnen eenparig en schriftelijk alle besluiten nemen die tot de bevoegdheid van de algemene vergadering behoren, met uitzondering van statutenwijzigingen. In dat geval hoeven de formaliteiten van bijeenroeping niet te worden nageleefd. De leden van het bestuursorgaan, de commissari",
    "rationale_snippet": ""
  },
  {
    "id": "schuldvergelijking-tijdens-opschorting",
    "naam": "Schuldvergelijking tijdens opschorting",
    "node_type": "begrip",
    "definitie_snippet": "Compensatie tussen een **schuldvordering die in de opschorting valt** (ontstaan vóór de gerechtelijke reorganisatie) en een **schuld ontstaan tijdens de opschorting** is volgens art. XX.55 WER **enkel toegestaan indien beide verknocht zijn** — dat wil zeggen voortvloeien uit dezelfde rechtsverhoudin",
    "rationale_snippet": ""
  },
  {
    "id": "sell-out-minderheid",
    "naam": "Sell-out — uitkooprecht van de minderheids­aandeelhouder",
    "node_type": "regel",
    "definitie_snippet": "Een **eenzijdig recht** van een **minderheidsaandeelhouder** in een **genoteerde** vennootschap om — na een openbaar overnamebod waarbij de bieder een zeer hoge deelneming bereikt — diens overgebleven effecten **te laten opkopen** door de bieder tegen dezelfde prijs als de biedprijs.",
    "rationale_snippet": ""
  },
  {
    "id": "signaleren-oprichtersaansprakelijkheid-risico",
    "naam": "Signaleren van oprichtersaansprakelijkheid-risico's aan de cliënt",
    "node_type": "competentie",
    "definitie_snippet": "",
    "rationale_snippet": ""
  },
  {
    "id": "signaleren-risicos-overdracht-of-ontbinding",
    "naam": "Signaleren van risico's bij overdracht of ontbinding (aansprakelijkheid, kapitaalbescherming, fiscaal)",
    "node_type": "competentie",
    "definitie_snippet": "",
    "rationale_snippet": ""
  },
  {
    "id": "sluiting-vereffening",
    "naam": "Sluiting van de vereffening",
    "node_type": "cluster",
    "definitie_snippet": "De **sluiting van de vereffening** is de formele beëindiging van de vereffeningsfase — pas op dat ogenblik **houdt de vennootschap op te bestaan** als rechtspersoon. Zij wordt uitgesproken door de AV (bij vrijwillige ontbinding, art. 2:90 + 2:100 WVV) of door de rechtbank (bij gerechtelijke ontbindi",
    "rationale_snippet": ""
  },
  {
    "id": "staat-van-activa-en-passiva-ontbinding",
    "naam": "Staat van activa en passiva bij ontbinding",
    "node_type": "begrip",
    "definitie_snippet": "De **staat van activa en passiva** bij ontbinding is een tussentijdse balans, opgesteld door het bestuursorgaan op een datum die **niet meer dan drie maanden vóór de AV** ligt die over de ontbinding zal beslissen (art. 2:71 § 2 WVV). Tenzij anders gemotiveerd wordt zij opgesteld in **discontinuïteit",
    "rationale_snippet": ""
  },
  {
    "id": "statutaire-uittreding-bv",
    "naam": "Statutaire uittreding en uitsluiting in de BV",
    "node_type": "cluster",
    "definitie_snippet": "Het statutaire uittredings- en uitsluitingsregime van de BV (art. 5:154-5:156) laat de statuten bepalen dat een aandeelhouder ten laste van het vennootschapsvermogen kan uittreden of dat de algemene vergadering hem om wettige reden kan uitsluiten, met betaling van het **scheidingsaandeel** uit het v",
    "rationale_snippet": ""
  },
  {
    "id": "statuten-vennootschap",
    "naam": "Statuten van een vennootschap",
    "node_type": "cluster",
    "definitie_snippet": "De statuten zijn de juridische basisakte van een vennootschap: het samenstel van regels waarmee oprichters de werking, het bestuur, de aandeelhoudersrechten, de winstverdeling en het voortbestaan van de vennootschap organiseren. Het WVV bepaalt per rechtsvorm welke vermeldingen verplicht in de statu",
    "rationale_snippet": ""
  },
  {
    "id": "stemovereenkomst",
    "naam": "Stemovereenkomst tussen aandeelhouders",
    "node_type": "regel",
    "definitie_snippet": "Een **stemovereenkomst** (of stemafspraak) is een contractuele afspraak tussen twee of meer aandeelhouders waarbij ze zich verbinden om hun stemrecht op de algemene vergadering **op een bepaalde wijze uit te oefenen** — bv. eensgezind, na voorafgaand overleg, of conform de meerderheid binnen een ste",
    "rationale_snippet": ""
  },
  {
    "id": "stemrecht-aandeelhouder",
    "naam": "Stemrecht van de aandeelhouder",
    "node_type": "begrip",
    "definitie_snippet": "Het stemrecht is het recht van een aandeelhouder om in de algemene vergadering zijn stem uit te brengen over de te behandelen agendapunten. In de NV verleent elk aandeel in beginsel één stem; de BV laat de statuten toe meervoudig stemrecht in te voeren of aandelen zonder stemrecht uit te geven. Aand",
    "rationale_snippet": ""
  },
  {
    "id": "synthese-bevoegdheidsverdeling-av-vs-bestuur",
    "naam": "Bevoegdheidsverdeling AV vs. bestuursorgaan — synthese",
    "node_type": "synthese",
    "definitie_snippet": "",
    "rationale_snippet": ""
  },
  {
    "id": "synthese-quorum-meerderheid-algemene-vergadering",
    "naam": "Quorum en meerderheid in de algemene vergadering — synthese per rechtsvorm",
    "node_type": "synthese",
    "definitie_snippet": "",
    "rationale_snippet": ""
  },
  {
    "id": "synthese-soorten-algemene-vergadering",
    "naam": "Drie soorten algemene vergadering — synthese",
    "node_type": "synthese",
    "definitie_snippet": "",
    "rationale_snippet": ""
  },
  {
    "id": "tijdelijke-handelsvennootschap-thv",
    "naam": "Tijdelijke handelsvennootschap (THV)",
    "node_type": "cluster",
    "definitie_snippet": "Een **tijdelijke handelsvennootschap** is een maatschap (vennootschap zonder rechtspersoonlijkheid) opgericht om één of meer bepaalde verrichtingen tot doel te hebben en op te houden zodra die verrichting is uitgevoerd. Onder het WVV 2019 wordt de THV niet langer als afzonderlijke vorm benoemd: ze v",
    "rationale_snippet": ""
  },
  {
    "id": "transfer-bedrijfstak-algemeenheid",
    "naam": "Overdracht van bedrijfstak of algemeenheid (WVV)",
    "node_type": "cluster",
    "definitie_snippet": "Een overdracht van bedrijfstak of algemeenheid is een WVV-procedure waarbij een vennootschap een operationeel zelfstandig opererende activiteitenkern (bedrijfstak) of het geheel van haar activa en passiva (algemeenheid) overdraagt, met de mogelijkheid dat alle rechten en plichten van rechtswege over",
    "rationale_snippet": ""
  },
  {
    "id": "uitkering-uit-eigen-vermogen-bv",
    "naam": "Uitkering uit eigen vermogen bij de BV (vermogensdistributie)",
    "node_type": "cluster",
    "definitie_snippet": "**Uitkering door de BV aan aandeelhouders uit het ingebracht eigen vermogen** (rubriek 11) — economisch het equivalent van een kapitaalvermindering bij de NV. Twee varianten: (1) uitkering uit **beschikbaar** ingebracht vermogen (lichtste procedure, zelfde regels als een dividend), (2) uitkering uit",
    "rationale_snippet": ""
  },
  {
    "id": "uitkeringstest-vergelijking-bv-nv",
    "naam": "Uitkeringstest BV vs NV — vergelijking",
    "node_type": "synthese",
    "definitie_snippet": "",
    "rationale_snippet": ""
  },
  {
    "id": "uitkoopbod-squeeze-out",
    "naam": "Uitkoopbod (squeeze-out) — 95%-drempel",
    "node_type": "regel",
    "definitie_snippet": "Een **eenzijdig recht** van de **95%-aandeelhouder** om **alle resterende stemrecht-verlenende effecten** **op te kopen** met **consignatie van de prijs** — zelfs zonder instemming van de minderheidshouders. Geldt voor niet-genoteerde NV's; voor genoteerde NV's bestaat een parallelle squeeze-out na ",
    "rationale_snippet": ""
  },
  {
    "id": "uitsluitingsvordering",
    "naam": "Uitsluitingsvordering",
    "node_type": "cluster",
    "definitie_snippet": "Een uitsluitingsvordering is een gerechtelijke vordering waarbij één of meer aandeelhouders die samen **ten minste 30% van de stemmen** (of, bij de NV, 30% van het kapitaal naar nominale of fractiewaarde) vertegenwoordigen, om **gegronde redenen** vorderen dat een andere aandeelhouder zijn effecten ",
    "rationale_snippet": ""
  },
  {
    "id": "uittredingsvordering",
    "naam": "Uittredingsvordering",
    "node_type": "cluster",
    "definitie_snippet": "Een uittredingsvordering laat een aandeelhouder gerechtelijk vorderen dat **andere aandeelhouders** (op wie de gegronde redenen betrekking hebben) zijn effecten overnemen tegen een door de rechter vast te stellen prijs. Iedere aandeelhouder kan de vordering instellen — er geldt **geen drempel** — mi",
    "rationale_snippet": ""
  },
  {
    "id": "vennoot-vs-aandeelhouder",
    "naam": "Vennoot versus aandeelhouder",
    "node_type": "begrip",
    "definitie_snippet": "**Vennoot** is de overkoepelende WVV-term voor wie inbreng doet en daardoor maatschappelijke rechten verwerft. **Aandeelhouder** is de specifieke term voor de vennoot in een vennootschap die aandelen heeft uitgegeven — BV, NV, CV en de Europese SE/SCE. In maatschap, VOF en CommV (en in de gecommandi",
    "rationale_snippet": ""
  },
  {
    "id": "vennootschap-begrip",
    "naam": "Vennootschap (juridisch begrip)",
    "node_type": "begrip",
    "definitie_snippet": "Een vennootschap is een rechtshandeling waarbij één of meer personen — vennoten genoemd — een inbreng doen, een vermogen vormen en zich engageren om één of meer welbepaalde activiteiten uit te oefenen, met als doel aan de vennoten een rechtstreeks of onrechtstreeks vermogensvoordeel uit te keren of ",
    "rationale_snippet": ""
  },
  {
    "id": "vennootschapsconflict",
    "naam": "Vennootschapsconflict",
    "node_type": "cluster",
    "definitie_snippet": "Een vennootschapsconflict is een aanhoudend geschil binnen, of rond de werking van, een vennootschap dat de normale besluitvorming of voortzetting van de zaken bemoeilijkt. Het kan ontstaan tussen aandeelhouders onderling (typisch meerderheid-minderheid of deadlock 50/50), tussen aandeelhouders en h",
    "rationale_snippet": ""
  },
  {
    "id": "vennootschapsvordering",
    "naam": "Vennootschapsvordering",
    "node_type": "begrip",
    "definitie_snippet": "Een vennootschapsvordering is een aansprakelijkheidsvordering die de **algemene vergadering** beslist in te stellen tegen leden van het bestuursorgaan, leden van de raad van toezicht, vereffenaars of commissarissen wegens een fout begaan bij de uitoefening van hun functie. De algemene vergadering ka",
    "rationale_snippet": ""
  },
  {
    "id": "vennootschapsvormen-typologie",
    "naam": "Typologie van vennootschaps- en verenigingsvormen",
    "node_type": "begrip",
    "definitie_snippet": "Het WVV onderscheidt verschillende vennootschapsvormen (rechtspersonen met winstoogmerk) en verenigingsvormen (rechtspersonen zonder of met sociaal oogmerk). Voor het boekhoudrecht zijn de vorm-keuze en de keuze tussen rechtspersoonlijkheid en geen rechtspersoonlijkheid bepalend: rechtspersonen volg",
    "rationale_snippet": ""
  },
  {
    "id": "vennootschapsvormen-vergelijking",
    "naam": "Vergelijking van de Belgische vennootschaps- en verenigingsvormen",
    "node_type": "synthese",
    "definitie_snippet": "",
    "rationale_snippet": ""
  },
  {
    "id": "verbonden-partijen-procedure-genoteerd",
    "naam": "Verbonden-partijen-procedure in de genoteerde NV",
    "node_type": "regel",
    "definitie_snippet": "Voor elke beslissing of verrichting die tot de bevoegdheid van de raad van bestuur (of in een duaal model van de raad van toezicht) van een genoteerde NV behoort en die verband houdt met een 'verbonden partij' in de zin van de internationale standaarden voor jaarrekeningen (IAS 24, op grond van Vero",
    "rationale_snippet": ""
  },
  {
    "id": "verdachte-periode-faillissement",
    "naam": "Verdachte periode bij faillissement",
    "node_type": "regel",
    "definitie_snippet": "Handelingen die de schuldenaar verricht **vanaf de door de rechtbank bepaalde datum van staking van betaling** tot het vonnis van faillietverklaring (de 'verdachte periode') kunnen aan de boedel **niet-tegenwerpbaar** worden verklaard. Twee categorieën gelden van rechtswege niet-tegenwerpbaar (art. ",
    "rationale_snippet": ""
  },
  {
    "id": "vereffenaar",
    "naam": "Vereffenaar",
    "node_type": "begrip",
    "definitie_snippet": "De **vereffenaar** is de persoon (natuurlijk of rechtspersoon) die de **ontbonden vennootschap** vertegenwoordigt en haar vermogen afwikkelt tijdens de vereffeningsfase. Hij treedt in de plaats van het bestuursorgaan voor alle handelingen die nodig of dienstig zijn voor de vereffening (art. 2:78 WVV",
    "rationale_snippet": ""
  },
  {
    "id": "vereffenaarsaansprakelijkheid",
    "naam": "Vereffenaarsaansprakelijkheid",
    "node_type": "regel",
    "definitie_snippet": "De **vereffenaar** is tegenover de vennootschap gehouden tot een **behoorlijke vervulling** van zijn opdracht en is jegens de vennootschap en haar schuldeisers aansprakelijk voor **fouten begaan in de uitvoering** van zijn opdracht (art. 2:96 WVV). Jegens andere derden is hij aansprakelijk voor zove",
    "rationale_snippet": ""
  },
  {
    "id": "vereffening-in-een-akte",
    "naam": "Vereffening in één akte",
    "node_type": "regel",
    "definitie_snippet": "Overeenkomstig **art. 2:80 WVV** kunnen de ontbinding en de sluiting van de vereffening in **één notariële akte** worden samengebracht, mits drie strikte voorwaarden cumulatief zijn vervuld: (1) geen vereffenaar wordt benoemd, (2) alle schulden zijn betaald of de nodige gelden zijn geconsigneerd, en",
    "rationale_snippet": ""
  },
  {
    "id": "vereffening",
    "naam": "Vereffening van een vennootschap",
    "node_type": "cluster",
    "definitie_snippet": "Het **wettelijk geregelde proces** waarbij een vennootschap haar bedrijfsactiviteit beëindigt: activa worden te gelde gemaakt, schulden worden betaald, het saldo wordt onder de aandeelhouders verdeeld in functie van hun rechten. De vennootschap blijft juridisch bestaan ('in vereffening') tot afsluit",
    "rationale_snippet": ""
  },
  {
    "id": "vereffeningsdeskundige",
    "naam": "Vereffeningsdeskundige",
    "node_type": "begrip",
    "definitie_snippet": "De vereffeningsdeskundige is een specifieke insolventiefunctionaris die de ondernemingsrechtbank aanstelt bij een procedure van gerechtelijke reorganisatie door overdracht onder gerechtelijk gezag (Boek XX WER, titel V, hoofdstuk 4). Hij organiseert en realiseert de overdracht van het geheel of een ",
    "rationale_snippet": ""
  },
  {
    "id": "vereffeningsprocedure-klassiek",
    "naam": "Klassieke vereffeningsprocedure",
    "node_type": "cluster",
    "definitie_snippet": "De **klassieke vereffeningsprocedure** is het standaardpad om een ontbonden vennootschap af te wikkelen wanneer niet alle voorwaarden van art. 2:80 WVV (vereffening in één akte) zijn vervuld. Zij doorloopt vijf fasen: (1) ontbindingsbesluit met staat van activa en passiva, (2) benoeming en bekendmak",
    "rationale_snippet": ""
  },
  {
    "id": "vereniging-en-stichting",
    "naam": "Verenigingen en stichtingen (VZW, IVZW, stichting)",
    "node_type": "cluster",
    "definitie_snippet": "Een **vereniging** is een verbond van personen voor een gemeenschappelijk belangeloos doel (VZW = met rechtspersoonlijkheid, art. 9:1; feitelijke vereniging = zonder, art. 1:6). Een **stichting** is een rechtspersoon zonder leden, opgericht door één of meer stichters, waarvan het vermogen wordt best",
    "rationale_snippet": ""
  },
  {
    "id": "vergelijking-vorderingen-vennootschapsconflict",
    "naam": "Vergelijking van de gerechtelijke vorderingen bij een vennootschapsconflict",
    "node_type": "synthese",
    "definitie_snippet": "Vergelijkingstabel van de vijf wettelijke vorderingen die een aandeelhouder kan instellen bij een vennootschapsconflict in een niet-genoteerde BV of NV, gerangschikt naar drempel, doel en uitkomst.",
    "rationale_snippet": ""
  },
  {
    "id": "verplicht-overnamebod",
    "naam": "Verplicht openbaar overnamebod (30%-drempel)",
    "node_type": "regel",
    "definitie_snippet": "Een **wettelijke verplichting**, opgelegd door de Wet van 1 april 2007 op de openbare overnamebiedingen, om bij overschrijden van de 30%-drempel in een genoteerde vennootschap een **integrale uitstapmogelijkheid** te bieden aan alle andere effectenhouders.",
    "rationale_snippet": ""
  },
  {
    "id": "vertegenwoordiging-vennootschap-jegens-derden",
    "naam": "Vertegenwoordiging van de vennootschap jegens derden",
    "node_type": "regel",
    "definitie_snippet": "De vennootschap is verbonden door de handelingen van het bestuursorgaan, van de personen aan wie het dagelijks bestuur is opgedragen en van de bestuurders met statutaire vertegenwoordigingsbevoegdheid, zelfs indien die handelingen buiten haar voorwerp liggen. De vennootschap kan zich enkel op het ul",
    "rationale_snippet": ""
  },
  {
    "id": "verzwaarde-aansprakelijkheid-bij-insolventie-overzicht",
    "naam": "Verzwaarde aansprakelijkheid bij insolventie — overzicht regimes",
    "node_type": "synthese",
    "definitie_snippet": "",
    "rationale_snippet": ""
  },
  {
    "id": "volmacht-algemene-vergadering",
    "naam": "Volmacht op de algemene vergadering",
    "node_type": "cluster",
    "definitie_snippet": "De volmacht op de algemene vergadering is de machtiging die een aandeelhouder aan een natuurlijke of rechtspersoon verleent om sommige of alle van zijn rechten in de algemene vergadering uit te oefenen — het woord voeren, vragen stellen, stem uitbrengen. De volmachtdrager hoeft in beginsel geen aand",
    "rationale_snippet": ""
  },
  {
    "id": "voorbereiden-oprichtingsakte",
    "naam": "Voorbereiden van de oprichtingsakte en statuten",
    "node_type": "competentie",
    "definitie_snippet": "",
    "rationale_snippet": ""
  },
  {
    "id": "voordrachtrecht-bestuurder",
    "naam": "Voordrachtrecht voor bestuurszetel",
    "node_type": "regel",
    "definitie_snippet": "Een **voordrachtrecht** is een clausule in de statuten of in een aandeelhoudersovereenkomst die aan een **specifieke aandeelhouder, groep van aandeelhouders of aandelenklasse** het recht toekent om voor één of meer **bestuursmandaten** **kandidaat-bestuurders** voor te dragen aan de algemene vergade",
    "rationale_snippet": ""
  },
  {
    "id": "voorkeurrecht-aandeelhouder",
    "naam": "Voorkeurrecht van de aandeelhouder",
    "node_type": "begrip",
    "definitie_snippet": "Het **recht van een bestaande aandeelhouder** om bij een uitgifte van nieuwe aandelen, converteerbare obligaties of inschrijvingsrechten **in te schrijven naar verhouding van zijn bestaand belang** (pro rata), gedurende een minimale wettelijke termijn. Doel: bescherming tegen ongewenste verwatering ",
    "rationale_snippet": ""
  },
  {
    "id": "voorkooprecht-aandelenoverdracht",
    "naam": "Voorkooprecht bij aandelenoverdracht",
    "node_type": "begrip",
    "definitie_snippet": "Een **clausule** (statutair of in een aandeelhoudersovereenkomst) die bepaalt dat een aandeelhouder, vooraleer hij zijn aandelen aan een **derde** mag verkopen, deze **eerst moet aanbieden** aan de **andere aandeelhouders** — **tegen dezelfde voorwaarden** als het externe bod (of tegen een vooraf ov",
    "rationale_snippet": ""
  },
  {
    "id": "voorstel-omzetting-vennootschap",
    "naam": "Voorstel tot omzetting van een vennootschap",
    "node_type": "regel",
    "definitie_snippet": "Vóór de algemene vergadering die over de omzetting beslist, moet het bestuursorgaan een voorstel tot omzetting opstellen: een schriftelijk document met (1) de motivering van de keuze van de nieuwe rechtsvorm, (2) de staat van activa en passiva (max. drie maanden oud), (3) een verslag van het bestuur",
    "rationale_snippet": ""
  },
  {
    "id": "voorwaarden-faillietverklaring",
    "naam": "Voorwaarden voor faillietverklaring",
    "node_type": "regel",
    "definitie_snippet": "Een onderneming kan failliet worden verklaard wanneer zij **op duurzame wijze heeft opgehouden te betalen** én haar **krediet geschokt is**. Beide voorwaarden moeten cumulatief vervuld zijn. De faillietverklaring kan worden uitgesproken op aangifte van de schuldenaar zelf, op dagvaarding van één of ",
    "rationale_snippet": ""
  },
  {
    "id": "vraagrecht-aandeelhouder",
    "naam": "Vraagrecht van de aandeelhouder op de algemene vergadering",
    "node_type": "regel",
    "definitie_snippet": "De leden van het bestuursorgaan en, voor de agendapunten waarover hij verslag uitbrengt, de commissaris geven antwoord op de vragen die hun door de aandeelhouders (of leden, in vzw-context) vooraf of tijdens de algemene vergadering, mondeling of schriftelijk worden gesteld en die verband houden met ",
    "rationale_snippet": ""
  },
  {
    "id": "vrijwillige-ontbinding",
    "naam": "Vrijwillige ontbinding",
    "node_type": "regel",
    "definitie_snippet": "Een BV, CV, NV, SE of SCE kan op elk ogenblik worden ontbonden door een **besluit van de algemene vergadering**, met inachtneming van de wettelijke vormvereisten, aanwezigheidsquorum en versterkte meerderheid (typisch **4/5 van de uitgebrachte stemmen** — zie art. 5:84 BV, 6:70, § 2 CV, 7:132 NV). D",
    "rationale_snippet": ""
  },
  {
    "id": "vrijwillige-versus-gerechtelijke-ontbinding",
    "naam": "Vrijwillige vs gerechtelijke ontbinding",
    "node_type": "synthese",
    "definitie_snippet": "",
    "rationale_snippet": ""
  },
  {
    "id": "vroegtijdige-waarschuwing-insolventie",
    "naam": "Vroegtijdige waarschuwing bij insolventie",
    "node_type": "cluster",
    "definitie_snippet": "Het systeem van **knipperlichten** dat Boek XX WER instelt om ondernemingen in financiële moeilijkheden vroegtijdig op te sporen. Veroordelende vonnissen wegens onbetaalde schulden, achterstallige RSZ-bijdragen en niet-betaalde btw worden automatisch doorgemeld aan de griffie van de ondernemingsrech",
    "rationale_snippet": ""
  },
  {
    "id": "wettige-redenen-ontbinding",
    "naam": "Wettige redenen voor gerechtelijke ontbinding",
    "node_type": "begrip",
    "definitie_snippet": "Wettige redenen voor gerechtelijke ontbinding zijn omstandigheden die de normale voortzetting van de zaken van de vennootschap onmogelijk maken. De wet noemt expliciet twee voorbeelden: (i) **grove verzuim van verplichtingen** door een vennoot/aandeelhouder, (ii) **kwaal die hem onmogelijk maakt zij",
    "rationale_snippet": ""
  }
]
```

## Competentie-summaries

```json
[
  {
    "id": "adviseren-ontbindingsroute-vennootschap",
    "titel": "Adviseren over de ontbindingsroute van een vennootschap",
    "procedure_grondslag": {
      "wettelijk_pct": 75,
      "praktijk_pct": 25,
      "motivering": "Routes zelf en hun voorwaarden zijn wettelijk gedefinieerd; de feitelijke afweging op basis van vermogenssituatie is vakdoctrine."
    },
    "gebaseerd_op_concepten": [
      "ontbinding-vennootschap",
      "vrijwillige-ontbinding",
      "gerechtelijke-ontbinding",
      "vereffening-in-een-akte",
      "vereffeningsprocedure-klassiek",
      "klassieke-versus-een-akte-vereffening",
      "ontbinding-van-rechtswege"
    ],
    "eerste_stap": "Vaststellen van de feitelijke vermogenssituatie"
  },
  {
    "id": "adviseren-overdrachtsroute-onderneming",
    "titel": "Adviseren over de overdrachtsroute van een onderneming",
    "procedure_grondslag": {
      "wettelijk_pct": 40,
      "praktijk_pct": 60,
      "motivering": "Routes zelf en hun procedure-regels staan in het WVV (Boek 12, Boek 5/6/7) en het WIB92. De afweging tussen routes is grotendeels vakdoctrine en transactiepraktijk."
    },
    "gebaseerd_op_concepten": [
      "asset-deal-versus-share-deal",
      "overnameovereenkomst",
      "controleverwerving-methodes",
      "due-diligence-overname",
      "transfer-bedrijfstak-algemeenheid",
      "aandeelhoudersovereenkomst"
    ],
    "eerste_stap": "Inventariseren van het cliënt-mandaat en de transactiedrijfveren"
  },
  {
    "id": "adviseren-vennootschapsvormkeuze",
    "titel": "Adviseren over de keuze van vennootschapsvorm bij oprichting",
    "procedure_grondslag": {
      "wettelijk_pct": 50,
      "praktijk_pct": 50,
      "motivering": "WVV definieert de vormen en hun kenmerken dwingend. De afweging-methode (welke criteria primair, hoe gevoeligheidsanalyse fiscaliteit) is accountantspraktijk."
    },
    "gebaseerd_op_concepten": [
      "vennootschapsvormen-vergelijking",
      "vennootschapsvormen-typologie",
      "besloten-vennootschap-bv",
      "naamloze-vennootschap-nv",
      "cooperatieve-vennootschap-cv",
      "personenvennootschap-met-rechtspersoonlijkheid",
      "rechtspersoonlijkheid-vennootschap"
    ],
    "eerste_stap": "Inventariseren cliëntprofiel en doelstellingen"
  },
  {
    "id": "begeleiden-due-diligence-overname",
    "titel": "Begeleiden van due diligence bij overname",
    "procedure_grondslag": {
      "wettelijk_pct": 15,
      "praktijk_pct": 85,
      "motivering": "DD-proces zelf is grotendeels contractueel en methodologisch — niet wettelijk geregeld. Beperkte wettelijke verankering via GDPR en confidentialiteitsverplichtingen."
    },
    "gebaseerd_op_concepten": [
      "due-diligence-overname",
      "representations-and-warranties",
      "indemnification-overname",
      "purchase-price-mechanismen",
      "overnameovereenkomst",
      "confidentiality-overname"
    ],
    "eerste_stap": "Vaststellen perspectief, scope en team"
  },
  {
    "id": "begeleiden-inbreng-bij-oprichting",
    "titel": "Begeleiden van de inbreng in geld en in natura bij oprichting",
    "procedure_grondslag": {
      "wettelijk_pct": 80,
      "praktijk_pct": 20,
      "motivering": "WVV-procedure voor inbreng is dwingend (deponering, revisorenverslag). Adviesrol accountant bij inbrengstrategie is praktijk."
    },
    "gebaseerd_op_concepten": [
      "inbreng-vennootschap",
      "inbreng-in-natura-verslag",
      "quasi-inbreng-verslag",
      "oprichtersaansprakelijkheid",
      "besloten-vennootschap-bv",
      "naamloze-vennootschap-nv"
    ],
    "eerste_stap": "Identificeren van het inbreng-type per oprichter"
  },
  {
    "id": "begeleiden-registratie-onderneming-kbo",
    "titel": "Begeleiden van de registratie van een nieuwe onderneming (KBO, btw, UBO)",
    "procedure_grondslag": {
      "wettelijk_pct": 80,
      "praktijk_pct": 20,
      "motivering": "Registratie-stappen volgen dwingende formaliteiten in WER en btw-wetboek. Volgorde en versnelling zijn vakpraktijk."
    },
    "gebaseerd_op_concepten": [
      "rechtspersoonlijkheid-vennootschap",
      "besloten-vennootschap-bv",
      "naamloze-vennootschap-nv"
    ],
    "eerste_stap": "Verkrijgen ondernemingsnummer + inschrijving KBO"
  },
  {
    "id": "begeleiden-vereffening-vennootschap",
    "titel": "Begeleiden van de vereffening van een vennootschap",
    "procedure_grondslag": {
      "wettelijk_pct": 75,
      "praktijk_pct": 25,
      "motivering": "Procedure en verslagvereisten dwingend uit WVV; werkmethode + planning is vakdoctrine."
    },
    "gebaseerd_op_concepten": [
      "vereffeningsprocedure-klassiek",
      "vereffenaar",
      "staat-van-activa-en-passiva-ontbinding",
      "sluiting-vereffening",
      "liquidatiebonus",
      "omstandige-staat-vereffening"
    ],
    "eerste_stap": "Opstellen van de staat van activa en passiva als input voor de ontbindingsbeslissing"
  },
  {
    "id": "begeleiden-waardering-onderneming-bij-overdracht",
    "titel": "Begeleiden van de waardering van een onderneming bij overdracht",
    "procedure_grondslag": {
      "wettelijk_pct": 10,
      "praktijk_pct": 90,
      "motivering": "Waarderingsmethoden zijn vakdoctrine; alleen bij wettelijk voorbehouden verslagen (inbreng in natura, fusie) komt een normatieve basis kijken."
    },
    "gebaseerd_op_concepten": [
      "overnameovereenkomst",
      "purchase-price-mechanismen",
      "controleverwerving-methodes",
      "asset-deal-versus-share-deal"
    ],
    "eerste_stap": "Vaststellen van het waarderingsdoel en het perspectief"
  },
  {
    "id": "opstellen-beoordelingsverslag-uitsluiting-voorkeurrecht",
    "titel": "Beoordelingsverslag uitsluiting voorkeurrecht (art. 5:121, 7:179 WVV)",
    "procedure_grondslag": {
      "wettelijk_pct": 75,
      "praktijk_pct": 25,
      "motivering": "Verslagstructuur en mandaatsvereiste zijn wettelijk in WVV vastgelegd; uitvoering volgt ITAA-norm-effectennorm + ISA 805/ISRE-achtige beoordelingsmethodiek (praktijk)."
    },
    "gebaseerd_op_concepten": [
      "voorkeurrecht-aandeelhouder",
      "kapitaalverhoging-bv",
      "kapitaalverhoging-nv",
      "bijzondere-mandaten-accountant",
      "onafhankelijkheid-bijzondere-mandataris"
    ],
    "eerste_stap": "Verifiëren of beoordelingsverslag wettelijk vereist is"
  },
  {
    "id": "opstellen-financieel-plan-oprichting",
    "titel": "Opstellen van het financieel plan bij oprichting van een vennootschap",
    "procedure_grondslag": {
      "wettelijk_pct": 70,
      "praktijk_pct": 30,
      "motivering": "Inhoudelijke rubrieken zijn dwingend door WVV. Methodiek (hoe je een omzetprognose stevig bouwt) is vakdoctrine + accountantspraktijk."
    },
    "gebaseerd_op_concepten": [
      "financieel-plan-oprichting",
      "oprichtersaansprakelijkheid",
      "kennelijk-ontoereikend-aanvangsvermogen",
      "besloten-vennootschap-bv",
      "naamloze-vennootschap-nv"
    ],
    "eerste_stap": "Inventariseren businessplan en vennootschapsvorm"
  },
  {
    "id": "opstellen-openingsbalans-vennootschap",
    "titel": "Opstellen van de openingsbalans van een nieuwe vennootschap",
    "procedure_grondslag": {
      "wettelijk_pct": 65,
      "praktijk_pct": 35,
      "motivering": "Het jaarrekeningenschema is dwingend (KB WVV). Boeking-keuzes voor oprichtingskosten en hoe ze af te schrijven volgen vakdoctrine en CBN-richtlijnen."
    },
    "gebaseerd_op_concepten": [
      "financieel-plan-oprichting",
      "boeken-oprichtings-en-kapitaalverhogingskosten",
      "oprichtingskosten",
      "inbreng-vennootschap",
      "inbreng-in-natura-verslag"
    ],
    "eerste_stap": "Inventariseren oprichtingstransacties"
  },
  {
    "id": "opstellen-overname-verslaggeving-accountant",
    "titel": "Opstellen van accountantsverslagen bij overdrachtsverrichtingen",
    "procedure_grondslag": {
      "wettelijk_pct": 80,
      "praktijk_pct": 20,
      "motivering": "Verslag-inhoud en procedure zijn wettelijk gedefinieerd in het WVV; de waarderingsmethodologie zelf is vakdoctrine + ITAA-norm."
    },
    "gebaseerd_op_concepten": [
      "inbreng-in-natura-verslag",
      "quasi-inbreng-verslag",
      "fusie-splitsing-controleopdracht",
      "controleverwerving-methodes",
      "overnameovereenkomst"
    ],
    "eerste_stap": "Kwalificeren van de verrichting en bepalen welk verslag"
  },
  {
    "id": "opstellen-verslag-fusie-splitsing-ruilverhouding",
    "titel": "Verslag fusie/splitsing (Boek 12 WVV)",
    "procedure_grondslag": {
      "wettelijk_pct": 80,
      "praktijk_pct": 20,
      "motivering": "Boek 12 WVV en de gemeenschappelijke verslag-vereisten zijn wettelijk; de ruilverhouding-methodologie volgt vakdoctrine + ITAA-norm."
    },
    "gebaseerd_op_concepten": [
      "bijzondere-mandaten-accountant",
      "onafhankelijkheid-bijzondere-mandataris",
      "opstellen-overname-verslaggeving-accountant"
    ],
    "eerste_stap": "Verrichting kwalificeren binnen Boek 12 WVV"
  },
  {
    "id": "opstellen-verslag-omzetting-vennootschap",
    "titel": "Verslag omzetting vennootschap (Boek 14 WVV)",
    "procedure_grondslag": {
      "wettelijk_pct": 80,
      "praktijk_pct": 20,
      "motivering": "Boek 14 WVV bepaalt het verslag-mandaat en de verplichte rubrieken; uitvoering volgt ITAA-norm-omzetting-vennootschap modelverslagen."
    },
    "gebaseerd_op_concepten": [
      "bijzondere-mandaten-accountant",
      "onafhankelijkheid-bijzondere-mandataris"
    ],
    "eerste_stap": "Type omzetting kwalificeren"
  },
  {
    "id": "opstellen-verslag-ontbinding-vereffening-staat",
    "titel": "Verslag staat activa/passiva ontbinding (art. 2:71, 2:80 WVV)",
    "procedure_grondslag": {
      "wettelijk_pct": 80,
      "praktijk_pct": 20,
      "motivering": "Art. 2:71 en 2:80 WVV definiëren mandaat en verslag-vereisten; uitvoering volgt ITAA-norm-ontbinding-vereffening Bijlage 3."
    },
    "gebaseerd_op_concepten": [
      "staat-van-activa-en-passiva-ontbinding",
      "ontbinding-vennootschap",
      "vereffening-in-een-akte",
      "bijzondere-mandaten-accountant",
      "onafhankelijkheid-bijzondere-mandataris"
    ],
    "eerste_stap": "Procedure kwalificeren: klassiek of in één akte"
  },
  {
    "id": "signaleren-oprichtersaansprakelijkheid-risico",
    "titel": "Signaleren van oprichtersaansprakelijkheid-risico's aan de cliënt",
    "procedure_grondslag": {
      "wettelijk_pct": 85,
      "praktijk_pct": 15,
      "motivering": "Aansprakelijkheidsgronden volledig in WVV. Risico-signalering-methodiek (welke risico's hoe wegen en aan cliënt presenteren) is plichtenleer en vakpraktijk."
    },
    "gebaseerd_op_concepten": [
      "oprichtersaansprakelijkheid",
      "kennelijk-ontoereikend-aanvangsvermogen",
      "financieel-plan-oprichting",
      "inbreng-in-natura-verslag",
      "bestuurdersaansprakelijkheid"
    ],
    "eerste_stap": "Inventariseren van de drie hoofdgronden van oprichtersaansprakelijkheid"
  },
  {
    "id": "signaleren-risicos-overdracht-of-ontbinding",
    "titel": "Signaleren van risico's bij overdracht of ontbinding",
    "procedure_grondslag": {
      "wettelijk_pct": 55,
      "praktijk_pct": 45,
      "motivering": "Aansprakelijkheidsgronden wettelijk; risico-perceptie en mitigatie-advies vakdoctrine."
    },
    "gebaseerd_op_concepten": [
      "bestuurdersaansprakelijkheid-bij-onrechtmatige-uitkering",
      "vereffenaarsaansprakelijkheid",
      "nettoactieftest",
      "liquiditeitstest-bv",
      "insolventietriage-beslisboom",
      "heropening-vereffening",
      "besloten-voorbereiding-faillissement",
      "verdachte-periode-faillissement"
    ],
    "eerste_stap": "Bestuurdersaansprakelijkheids-risico mappen (vóór, tijdens en na de verrichting)"
  },
  {
    "id": "voorbereiden-oprichtingsakte",
    "titel": "Voorbereiden van de oprichtingsakte en statuten",
    "procedure_grondslag": {
      "wettelijk_pct": 75,
      "praktijk_pct": 25,
      "motivering": "Verplichte vermeldingen zijn dwingend door WVV. Statuten-clausules (overdrachtsbeperking, voorkooprecht, soort aandelen) zijn deels keuze-architectuur — vakdoctrine."
    },
    "gebaseerd_op_concepten": [
      "besloten-vennootschap-bv",
      "naamloze-vennootschap-nv",
      "cooperatieve-vennootschap-cv",
      "bestuursmodel-vennootschap",
      "aandeelhoudersovereenkomst",
      "oprichtersaansprakelijkheid"
    ],
    "eerste_stap": "Vastleggen van de identificatiegegevens en doel"
  }
]
```

---

## Prompt-referentie (minicursus-glue-v3.md)

# Prompt: Minicursus-glue — Render-fase (v3)

**Doel**: Vul de `<!-- TODO: Opus-glue ... -->` placeholders in de minicursus-skeleton in.

**Model**: claude-opus-4-7 (Opus-subagent)

**Contract** (gewijzigd t.o.v. v2): parafrase-met-bronlink IS toegestaan. Wikilinks toevoegen naar bestaande records is toegestaan. Feiten verzinnen blijft hard verboden. **Compact**.

---

## Jouw rol

Je schrijft pedagogische tekst die de deterministisch gerenderde blokken verbindt en interpreteert. Je mag claims uit records parafraseren in cursus-stem mits je elke feitelijke claim wikilinkt aan zijn record. Je voegt geen nieuwe feiten toe; je geeft wel het pedagogische weefsel dat een student helpt de stof te bezitten.

**Verhouding t.o.v. v2**: v2 was streng "geen feiten-claims, geen nieuwe wikilinks". v3 versoepelt naar "parafrase-met-bronlink toegestaan, mits elke feitelijke claim wikilinkt in dezelfde zin". Dit volgt ADR-010 §implicatie-3 (interpretatieve laag) en `docs/studiemateriaal-schrijfregels.md` §1.

## Compactheidscontract

Mikt op compacte, dichte tekst zonder kaal te worden. Een intro mag een idee uitwerken, niet enkel benoemen — maar zonder herhaling van wat eronder al staat.

- **Sectie-intro's (oriëntatie / thematisch / competentie / voorbereiding)**: typisch 2-3 zinnen. Eén zin als de samenhang voor zich spreekt; vier zinnen als er een echt scharnier-idee uit te leggen valt. Nooit meer dan vier.
- **Leesgids**: 3-4 zinnen — hoe lees je de minicursus, welke logica zit erin.
- **Waarom-po**: 4-6 zinnen — één tot twee beginselen + toepassings-implicaties. Mag ademen, geen wall-of-text.
- **Synthese-stappenplan**: 6-9 zinnen — werkschema-stijl, end-to-end-overzicht.
- **Examenfocus** (glue-intro boven eind-rubriek): 2-3 zinnen — denkpatroon-aanduiding, geen vraag-spoiler. De vragen-callouts staan eronder.
- **Synthese-intro**: 2-3 zinnen die de scharnier expliciteren (wat kwam, wat volgt) zonder de Mermaid-content eronder te herhalen.
- **Totaal glue per minicursus**: richtlijn 700–1100 woorden.

## Wat MAG (v3, parafrase-met-bronlink)

| Type claim | Voorbeeld | Voorwaarde |
|---|---|---|
| **Parafraseren** van een record-veld | "De alarmbelprocedure springt aan bij twee triggers" — afgeleid uit `[[alarmbelprocedure]]` | Wikilink bij de claim in dezelfde zin |
| **Concept verbinden** aan eerder behandeld concept | "Zoals we zagen bij [[continuïteitsbeginsel]], …" | Doelconcept bestaat en is eerder in deze minicursus aangeraakt |
| **Compacte synthese** | "kort: dit zijn drie reserves die elkaar opvolgen in prioriteit" | Afgeleid uit `vergelijkingsparen[]` of edge-structuur; niet meer beweren dan records dragen |
| **Pedagogische framing** | "let op het verschil tussen [[X]] en [[Y]]" | Verwijst naar bestaande `vergelijkingsparen[]` of synthese-record |
| **Voorbeeld-introductie** | "stel je voor: een vennootschap met deze structuur…" | Het voorbeeld zelf komt uit een record (niet uit de glue) |
| **Wikilink toevoegen** waar je parafraseert | `[[record-id]]` na de claim | Doelrecord bestaat (geen non-existent records) |

## Wat NIET MAG (anti-fabricatie, hard)

1. **Feit verzinnen** zonder record-grondslag (cijfer, drempelwaarde, termijn, definitie, wetsartikel)
2. **Wikilink bedenken** naar een non-existent record — check eerst dat het record bestaat in `data/concepten/records/`
3. **Wettekst-citaat als prozetekst** ("Artikel 2:52 WVV stelt dat..."). Citeren mag wel **als blockquote met bron** en alleen waar de exacte bewoordingen ertoe doen
4. **Voorbeeld bedenken** — illustraties komen uit records, niet uit de glue
5. **Examenvraag-camouflage ontmaskeren** ("let op, dit is een schijngelijkenis") — camouflage-info hoort in de eind-rubriek, niet in de hoofdtekst
6. **Herhaling van synthese-record-inhoud**: de mermaid-beslisboom + kerninzichten staan eronder. Glue-intro voegt scharnier toe, geen overlap
7. **Cast-namen** (Aurelia, Brugse, ...) in glue — die horen in records-voorbeelden

## Niveau-respect (PO-niveau bepaalt werkwoorden)

Het PO-niveau staat in de minicursus-frontmatter (en de oriëntatie-callout). Werkwoorden in hoofdstuk-intro's volgen het niveau:

| PO-niveau | Voorbeeld-werkwoorden in intro's |
|---|---|
| **Kennen** | "we bekijken", "je leert kennen", "de regel is dat…" |
| **Begrijpen** | "we doorgronden waarom", "je leert het verband tussen", "de logica is dat…" |
| **Toepassen** | "je leert deze regel toepassen op", "we werken een casus uit waarbij", "stap voor stap doorlopen we…" |
| **Integratie** | "je leert deze concepten samen inzetten in", "we bouwen een coherent oordeel op uit", "in een complexe casus moet je…" |

Voor *toepassen* en *integratie* mag de glue actiever sturen ("stap voor stap", "geleidelijk", "wanneer twijfel ontstaat") — een student moet voelen dat het examen toepassings-vragen stelt.

## Workflow

Open `content/studiemateriaal/<X.Y>-<slug>.md` met de Edit-tool. Vervang elke `<!-- TODO: Opus-glue X -->` regel door de bedoelde tekst, in volgorde. Geen JSON-output — direct editen.

## Stijl

- **Toon**: helder, direct, actief — zoals een ervaren collega
- **"Je"-aanspraak**, niet "men" of "de student"
- **Geen bullets in glue-tekst** (bullets staan al in skeleton)
- **Nederlands**
- **Geen euro-bedragen of cast-namen** in glue (die staan in records); generieke termen
- **Geen "hieronder zie je..." of "in de volgende sectie..."** — laat de structuur zelf spreken

## Verificatie

Na invullen:

1. `grep -c "<!-- TODO: Opus-glue" content/studiemateriaal/<X.Y>-*.md` moet 0 teruggeven
2. Totale word-count tussen 700 en 1100 woorden glue-tekst (gemeten via `wc -w` op glue-content; bestaande records-content telt niet mee)
3. Geen overlap tussen synthese-intro en de synthese-record-inhoud die eronder rendert
4. Élke paragraaf met een feitelijke claim (cijfer, datum, "%", "art.", definitie) heeft minstens één wikilink — anders kan het geen feitelijke claim zijn (zie §wikilink-discipline in `docs/studiemateriaal-schrijfregels.md`)
5. Werkwoorden in intro's matchen het PO-niveau uit de frontmatter

Geen commit. De hoofdsessie commit.

