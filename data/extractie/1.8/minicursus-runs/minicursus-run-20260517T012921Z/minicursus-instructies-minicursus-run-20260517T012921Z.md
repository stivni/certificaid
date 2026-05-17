# Minicursus-glue-run minicursus-run-20260517T012921Z — Instructies voor Opus-subagent

**Programmaonderdeel**: 1.8
**Run-id**: minicursus-run-20260517T012921Z
**Gegenereerd op**: 2026-05-17T01:29:21+00:00

## Jouw taak

Vul de `<!-- TODO: Opus-glue ... -->` placeholders in de skeleton-Markdown in.
Schrijf de output als één JSON-object naar stdout met de velden beschreven in
`prompts/minicursus-glue-v1.md`.

## Input-bestanden

- **Skeleton**: `content/studiemateriaal/1-8-analytische-boekhouding.md`
- **Records-summaries** (44 stuks): zie §Records hieronder
- **Competentie-summaries** (9 stuks): zie §Competenties hieronder

## Anti-fabricatie-regels (verplicht)

- Geen feiten-claims in glue-tekst — alleen rationale, beginselen, transities
- Geen wikilinks bedenken — die staan al in de skeleton
- Verbind aan beginselen die in de records beschreven zijn
- Bij twijfel: korte neutrale tekst, geen uitvinding

## Records-summaries

```json
[
  {
    "id": "abc-methode",
    "naam": "ABC-methode (Activity Based Costing)",
    "node_type": "methode",
    "definitie_snippet": "Activity Based Costing (ABC) verfijnt de kostentoewijzing door indirecte kosten niet via één algemene sleutel maar via meerdere activiteiten en cost drivers naar producten te verdelen. ABC herkent dat verschillende indirecte kosten verschillende oorzaken hebben (set-up versus productie-uren versus o",
    "rationale_snippet": ""
  },
  {
    "id": "algemene-boekhouding",
    "naam": "Algemene boekhouding",
    "node_type": "begrip",
    "definitie_snippet": "De algemene boekhouding is het wettelijk verplichte registratiesysteem waarin alle financiële transacties van de onderneming chronologisch en systematisch worden vastgelegd volgens het Minimum Algemeen Rekeningstelsel (KB 21.10.2018, Bijlage 1). Output: jaarrekening (balans, resultatenrekening, toel",
    "rationale_snippet": ""
  },
  {
    "id": "analytische-boekhouding",
    "naam": "Analytische boekhouding",
    "node_type": "begrip",
    "definitie_snippet": "De analytische boekhouding (ook: bedrijfseconomische boekhouding of kostprijsboekhouding) is een intern, vrij in te vullen registratiesysteem waarin kosten en opbrengsten worden herverdeeld over kostendragers (producten, opdrachten, klanten) en kostencentra (afdelingen, machines). Doel: beslissingsi",
    "rationale_snippet": ""
  },
  {
    "id": "arbeidskosten",
    "naam": "Arbeidskosten",
    "node_type": "begrip",
    "definitie_snippet": "Arbeidskosten in analytische zin omvatten het brutoloon plus alle bijhorende werkgeverslasten (sociale zekerheid, vakantiegeld, eindejaarspremie, verzekering arbeidsongevallen, bedrijfsvoorheffing als doorstortingsplicht). Het bruto-loon alleen onderschat de werkelijke arbeidskost met typisch 25-40 ",
    "rationale_snippet": ""
  },
  {
    "id": "break-even-analyse",
    "naam": "Break-even-analyse",
    "node_type": "methode",
    "definitie_snippet": "De break-even-analyse (kosten-volume-winst-analyse, CVP) berekent welke omzet of welk volume nodig is om alle vaste kosten te dekken — het punt waarop de onderneming geen verlies en geen winst maakt. Aan dat volume betekent elke extra eenheid winst; eronder wordt verlies geleden.",
    "rationale_snippet": ""
  },
  {
    "id": "budget-cyclus",
    "naam": "Budgetcyclus",
    "node_type": "synthese",
    "definitie_snippet": "",
    "rationale_snippet": ""
  },
  {
    "id": "budgetbeheer",
    "naam": "Budgetbeheer",
    "node_type": "fenomeen",
    "definitie_snippet": "Budgetbeheer is het management-proces waarbij toekomstige kosten, opbrengsten en cashstromen vooraf worden geraamd in een geheel van budgetten, en waarbij realisaties periodiek tegen die ramingen worden afgezet om bij te sturen. Het omvat zowel de budgetprocedure (opstellen) als de budgetcontrole (o",
    "rationale_snippet": ""
  },
  {
    "id": "budgetboekhouding",
    "naam": "Budgetboekhouding",
    "node_type": "begrip",
    "definitie_snippet": "De budgetboekhouding is het deel van de analytische boekhouding waarin de goedgekeurde budgetbedragen worden opgenomen, zodat realisaties rechtstreeks tegen budgetcijfers kunnen worden vergeleken. Typisch ondergebracht in klasse 9 van het MAR (vaak rekeningen 90 'Niet-uitgevoerde verbintenissen' / b",
    "rationale_snippet": ""
  },
  {
    "id": "budgetprocedure",
    "naam": "Budgetprocedure",
    "node_type": "procedure",
    "definitie_snippet": "Een budgetprocedure verloopt typisch in vijf opeenvolgende fasen: richtlijnen opstellen, decentraal ramen, consolidatie en confrontatie, goedkeuring en distributie, periodieke opvolging. Elke fase heeft een eigenaar en een doorlooptijd. Een degelijke procedure waarborgt dat alle afdelingen tijdig hu",
    "rationale_snippet": ""
  },
  {
    "id": "contributiemarge",
    "naam": "Contributiemarge",
    "node_type": "begrip",
    "definitie_snippet": "De contributiemarge is het verschil tussen verkoopprijs en variabele kost per eenheid (eenheidscontributie) of tussen omzet en totale variabele kosten (totale contributiemarge). Dit bedrag draagt eerst bij aan het dekken van de vaste kosten en daarna aan de winst.",
    "rationale_snippet": ""
  },
  {
    "id": "costing-methodes-vergelijking",
    "naam": "Kostencalculatiemethoden vergeleken",
    "node_type": "synthese",
    "definitie_snippet": "",
    "rationale_snippet": ""
  },
  {
    "id": "direct-costing",
    "naam": "Direct costing (gedeeltelijke kostencalculatie)",
    "node_type": "methode",
    "definitie_snippet": "Direct costing (synoniem: variable costing, gedeeltelijke kostencalculatie) berekent een kostprijs die enkel directe en variabele kosten omvat. Vaste indirecte kosten worden niet op de kostendrager toegerekend maar direct als periodekost in de resultatenrekening geboekt. Doel: transparante zicht op ",
    "rationale_snippet": ""
  },
  {
    "id": "directe-kosten",
    "naam": "Directe kosten",
    "node_type": "begrip",
    "definitie_snippet": "Directe kosten zijn kosten die op een ondubbelzinnige en economisch verantwoorde manier rechtstreeks aan één specifieke kostendrager (product, opdracht, dienst) kunnen worden toegewezen, zonder verdeelsleutel. Typische voorbeelden: grondstoffen die in een welomschreven order zijn verwerkt, en arbeid",
    "rationale_snippet": ""
  },
  {
    "id": "doelstellingen-analytische-boekhouding",
    "naam": "Doelstellingen van de analytische boekhouding",
    "node_type": "fenomeen",
    "definitie_snippet": "De analytische boekhouding dient vier samenhangende doelen: (1) de werkelijke kostprijs per product, opdracht of dienst berekenen; (2) de winstgevendheid per kostendrager, klant of markt-segment in kaart brengen; (3) de werking per kostencentrum opvolgen (efficiëntie, productiviteit); (4) input leve",
    "rationale_snippet": ""
  },
  {
    "id": "flexibel-budget",
    "naam": "Flexibel budget",
    "node_type": "begrip",
    "definitie_snippet": "Een flexibel budget herrekent het budget op basis van het werkelijke productie- of verkoopvolume. Variabele kosten worden aangepast aan werkelijke volume; vaste kosten blijven gelijk. Resultaat: een 'gecorrigeerd budget' dat eerlijker vergeleken kan worden met de realisatie.",
    "rationale_snippet": ""
  },
  {
    "id": "gemiddelde-kostprijs",
    "naam": "Gemiddelde kostprijs",
    "node_type": "begrip",
    "definitie_snippet": "De gemiddelde kostprijs is de totale kost (vaste én variabele kosten samen) gedeeld door het aantal geproduceerde eenheden. Geeft een indicatie van de 'kost per stuk' inclusief gedragen overhead — bruikbaar voor lange-termijn prijszetting.",
    "rationale_snippet": ""
  },
  {
    "id": "indirecte-kosten",
    "naam": "Indirecte kosten",
    "node_type": "begrip",
    "definitie_snippet": "Indirecte kosten zijn kosten die meerdere kostendragers of kostencentra gemeenschappelijk ondersteunen en daarom enkel via een verdeelsleutel aan een specifiek product, opdracht of afdeling kunnen worden toegerekend. Typische voorbeelden: huur fabriekspand, energie, salaris afdelingshoofd, afschrijv",
    "rationale_snippet": ""
  },
  {
    "id": "kostenanalyse-make-or-buy",
    "naam": "Make-or-buy-analyse",
    "node_type": "afwegingskader",
    "definitie_snippet": "De make-or-buy-analyse vergelijkt de kost van zelf produceren met de kost van uitbesteden, gericht op de relevante kosten (vermijdbare kosten bij uitbesteden vs. inkoopprijs + transactiekost). Sunk costs en niet-vermijdbare overhead doen niet ter zake.",
    "rationale_snippet": ""
  },
  {
    "id": "kostencentrum",
    "naam": "Kostencentrum",
    "node_type": "begrip",
    "definitie_snippet": "Een kostencentrum is een organisatorische eenheid (afdeling, machine-groep, hulpdienst) waar kosten worden verzameld voordat ze worden doorverdeeld naar kostendragers of naar andere kostencentra. Het centrum heeft een verantwoordelijke en een eigen budget; het is de plek waar je 'wie is verantwoorde",
    "rationale_snippet": ""
  },
  {
    "id": "kostendrager",
    "naam": "Kostendrager",
    "node_type": "begrip",
    "definitie_snippet": "Een kostendrager is het object waarvan je de kostprijs wil weten: een product, productlijn, dienst, opdracht, klant, project of markt-segment. Alle kosten convergeren uiteindelijk naar kostendragers — direct via toewijzing, indirect via verdeling over kostencentra.",
    "rationale_snippet": ""
  },
  {
    "id": "kostensoort",
    "naam": "Kostensoort",
    "node_type": "begrip",
    "definitie_snippet": "Een kostensoort is een categorie van kosten naar economische aard: handelsgoederen, grond- en hulpstoffen, diensten en diverse goederen, bezoldigingen, afschrijvingen, financiële kosten, etc. De algemene boekhouding registreert standaard per kostensoort in klasse 60 t/m 65 van het Minimum Algemeen R",
    "rationale_snippet": ""
  },
  {
    "id": "kostprijs-per-eenheid",
    "naam": "Kostprijs per eenheid",
    "node_type": "begrip",
    "definitie_snippet": "De kostprijs per eenheid is het bedrag aan opgeofferde middelen om één eenheid van een product, dienst of order te realiseren. De kostprijs kan een vervaardigingsprijs zijn (wettelijk, CBN 132/7), een volledige bedrijfskostprijs (interne, inclusief commercieel + administratief) of een variabele kost",
    "rationale_snippet": ""
  },
  {
    "id": "marginale-kostprijs",
    "naam": "Marginale kostprijs",
    "node_type": "begrip",
    "definitie_snippet": "De marginale kostprijs is de kost van één extra geproduceerde of verkochte eenheid. Bij lineair kostengedrag valt dat samen met de variabele kost per eenheid; in werkelijkheid kan ze afwijken door schaalsprong (extra ploeg, overuren, capaciteitsuitbreiding).",
    "rationale_snippet": ""
  },
  {
    "id": "master-budget",
    "naam": "Master-budget (geconsolideerd budget)",
    "node_type": "begrip",
    "definitie_snippet": "Het master-budget is het geconsolideerde geheel van alle deelbudgetten, uitgedrukt in drie geprojecteerde financiële overzichten: pro-forma resultatenrekening, pro-forma balans en pro-forma kasstroomtabel voor het komende boekjaar. Het bestaat uit een operationeel budget (verkopen, productie, kosten",
    "rationale_snippet": ""
  },
  {
    "id": "materiaalkosten",
    "naam": "Materiaalkosten",
    "node_type": "begrip",
    "definitie_snippet": "Materiaalkosten zijn kosten verbonden aan het verwerven, opslaan en verbruiken van grondstoffen, hulpstoffen, halffabrikaten en handelsgoederen. In de analytische boekhouding worden ze opgesplitst in aankoopprijs (vermenigvuldigd met verbruikte hoeveelheid) en bijkomende kosten (transport, douane, o",
    "rationale_snippet": ""
  },
  {
    "id": "opportuniteitskost",
    "naam": "Opportuniteitskost",
    "node_type": "begrip",
    "definitie_snippet": "De opportuniteitskost is de waarde van het opgegeven alternatief — wat je had kunnen verdienen als je hetzelfde middel (tijd, machine, kapitaal) anders had ingezet. Niet boekhoudkundig geregistreerd; wel cruciaal voor beslissingen waar resources schaars zijn.",
    "rationale_snippet": ""
  },
  {
    "id": "overige-kosten",
    "naam": "Overige kosten (diensten, diverse goederen, afschrijvingen)",
    "node_type": "begrip",
    "definitie_snippet": "Overige kosten in een analytische boekhouding zijn alle productie- en exploitatiekosten die geen materiaal of arbeid zijn: diensten en diverse goederen (huur, energie, telecom, externe consultants, onderhoud), afschrijvingen op productie-activa, verzekeringen, en eventueel provisies voor toekomstige",
    "rationale_snippet": ""
  },
  {
    "id": "prijsverschil-arbeid",
    "naam": "Tariefverschil en efficiëntieverschil bij arbeid",
    "node_type": "begrip",
    "definitie_snippet": "Bij arbeidskosten wordt het totaal verschil tussen werkelijke en standaard arbeidskost gesplitst in: tariefverschil = werkelijke uren × (werkelijk uurtarief − standaard uurtarief) en efficiëntieverschil = (werkelijke uren − standaarduren) × standaard uurtarief. Tariefverschil wijst op HR-/loon-oorza",
    "rationale_snippet": ""
  },
  {
    "id": "registratiesysteem-eenvoudige-integratie",
    "naam": "Eenvoudige integratie (registratiesysteem)",
    "node_type": "methode",
    "definitie_snippet": "Bij eenvoudige integratie neemt elke deelnemer of elke onderneming in eigen boekhouding rechtstreeks zijn aandeel in de kosten en opbrengsten op — zonder aparte 'tussen-boekhouding'. In analytische context betekent het: kosten en opbrengsten worden meteen aan de kostendrager toegerekend zonder extra",
    "rationale_snippet": ""
  },
  {
    "id": "registratiesysteem-proportionele-integratie",
    "naam": "Proportionele integratie (registratiesysteem)",
    "node_type": "methode",
    "definitie_snippet": "Bij proportionele integratie worden kosten en opbrengsten 'rubriek per rubriek, proportioneel met het aandeel' opgenomen. CBN 3/3 formuleert dit voor tijdelijke verenigingen; in analytische boekhouding wordt het analoog toegepast wanneer een gemeenschappelijke kost over meerdere centra of dragers pr",
    "rationale_snippet": ""
  },
  {
    "id": "registratiesysteem-waarderingsneutraal",
    "naam": "Waarderingsneutraal registratiesysteem",
    "node_type": "methode",
    "definitie_snippet": "Een waarderingsneutraal registratiesysteem vermijdt waarderingsconflicten door belangrijke beslissingen (afschrijvingen, waardeverminderingen, voorraadwaardering) centraal te coördineren en consistent toe te passen tussen algemene en analytische boekhouding. CBN 3/3 beschrijft hiervoor vijf principe",
    "rationale_snippet": ""
  },
  {
    "id": "rekeningenstelsel-analytisch",
    "naam": "Rekeningenstelsel voor analytische boekhouding (klasse 9)",
    "node_type": "begrip",
    "definitie_snippet": "Klasse 9 van het Minimum Algemeen Rekeningstelsel (KB 21.10.2018 Bijlage 1) is door de wetgever vrij gelaten voor analytische rekeningen, budgetrekeningen, niet-uitgevoerde verbintenissen en interne verrekeningen. Elke onderneming richt klasse 9 in volgens haar eigen analytische behoeften — typisch ",
    "rationale_snippet": ""
  },
  {
    "id": "statisch-budget",
    "naam": "Statisch budget",
    "node_type": "begrip",
    "definitie_snippet": "Een statisch budget is een budget dat opgesteld werd voor één gepland activiteitenniveau en niet wordt aangepast aan latere wijzigingen in productie- of verkoopvolume. Het is de oorspronkelijke 'plan'-versie zoals goedgekeurd in december.",
    "rationale_snippet": ""
  },
  {
    "id": "sunk-cost",
    "naam": "Sunk cost (reeds gemaakte kost)",
    "node_type": "begrip",
    "definitie_snippet": "Een sunk cost is een kost die al gemaakt is en onomkeerbaar — niet meer te beïnvloeden door een toekomstige beslissing. Sunk costs zijn nooit relevant voor beslissingen over de toekomst (extra-order, make-or-buy, stopzetting).",
    "rationale_snippet": ""
  },
  {
    "id": "typologie-van-kosten",
    "naam": "Typologie van kosten",
    "node_type": "synthese",
    "definitie_snippet": "",
    "rationale_snippet": ""
  },
  {
    "id": "variabele-kosten",
    "naam": "Variabele kosten",
    "node_type": "begrip",
    "definitie_snippet": "Variabele kosten zijn kosten die proportioneel mee veranderen met het productie- of verkoopvolume. Hun totaal stijgt bij meer output; per eenheid blijven ze (binnen een relevante range) constant.",
    "rationale_snippet": ""
  },
  {
    "id": "vaste-kosten",
    "naam": "Vaste kosten",
    "node_type": "begrip",
    "definitie_snippet": "Vaste kosten (ook: structuurkosten of periode-kosten) zijn kosten die binnen een relevante volumebandbreedte niet meebewegen met het productie- of verkoopvolume. Ze worden gemaakt om productiecapaciteit beschikbaar te houden — ongeacht of die capaciteit wordt benut.",
    "rationale_snippet": ""
  },
  {
    "id": "verdeelsleutel",
    "naam": "Verdeelsleutel",
    "node_type": "begrip",
    "definitie_snippet": "Een verdeelsleutel is de maatstaf waarmee een indirecte kost over meerdere kostencentra of kostendragers wordt verdeeld. De sleutel moet causaal verantwoord zijn: ze moet weerspiegelen hoeveel elke ontvanger de gemeenschappelijke bron heeft gebruikt.",
    "rationale_snippet": ""
  },
  {
    "id": "verschillenboekhouding",
    "naam": "Verschillenboekhouding",
    "node_type": "methode",
    "definitie_snippet": "Verschillenboekhouding (variance accounting) registreert systematisch het verschil tussen werkelijke kost en budget- of standaardkost, en splitst dat verschil in oorzaakcomponenten (prijsverschil, hoeveelheidverschil, mix-verschil, efficiëntieverschil). Doel: snel lokaliseren waar afwijkingen vandaa",
    "rationale_snippet": ""
  },
  {
    "id": "vervaardigingsprijs",
    "naam": "Vervaardigingsprijs",
    "node_type": "regel",
    "definitie_snippet": "De vervaardigingsprijs van producten omvat (a) de aanschaffingsprijs van de gebruikte grondstoffen, verbruiksgoederen en hulpstoffen, (b) de productiekosten die rechtstreeks aan het individuele product kunnen worden toegerekend (directe productiekosten), en (c) het evenredig deel van de productiekos",
    "rationale_snippet": ""
  },
  {
    "id": "volledige-kostencalculatie",
    "naam": "Volledige kostencalculatie (full costing)",
    "node_type": "methode",
    "definitie_snippet": "De volledige kostencalculatie (synoniem: full costing, absorption costing) berekent een 'volledige kostprijs' per kostendrager door alle directe én alle (productie-)indirecte kosten op te tellen en aan het product toe te wijzen. Dit is de wettelijke aanpak voor de vervaardigingsprijs in de Belgische",
    "rationale_snippet": ""
  },
  {
    "id": "voorbepaalde-kosten",
    "naam": "Voorbepaalde kosten (standaardkostencalculatie)",
    "node_type": "methode",
    "definitie_snippet": "Voorbepaalde kosten (standaardkosten) zijn vooraf vastgelegde normbedragen voor materiaal, arbeid en overhead per eenheid product. Ze worden gebruikt om de werkelijke kosten meteen tegen een norm af te zetten en zo afwijkingen (verschillen) snel te detecteren. Dit ondersteunt budgetbeheer, kostencon",
    "rationale_snippet": ""
  },
  {
    "id": "voorraadwaardering",
    "naam": "Voorraadwaardering (kostprijsmethoden)",
    "node_type": "regel",
    "definitie_snippet": "Voorraden worden gewaardeerd aan aanschaffingswaarde (gekochte goederen) of vervaardigingsprijs (zelf vervaardigde producten), eventueel verminderd tot lagere marktwaarde (laagstewaarderegel). Voor identieke goederen waarvan de prijs schommelt, wordt één van de wettelijk toegestane berekeningsmethod",
    "rationale_snippet": ""
  },
  {
    "id": "werkelijke-kostencalculatie",
    "naam": "Werkelijke kostencalculatie (vastgestelde kosten)",
    "node_type": "methode",
    "definitie_snippet": "Werkelijke kostencalculatie (synoniem: post-calculatie, vastgestelde kostencalculatie) berekent de kostprijs op basis van de werkelijk geboekte kosten, achteraf bekend uit de boekhouding. Tegenpool van voorbepaalde kostencalculatie (standaardkosten). Vereist een afgesloten boekhoudperiode vóór de ko",
    "rationale_snippet": ""
  }
]
```

## Competentie-summaries

```json
[
  {
    "id": "bepalen-vervaardigingsprijs-kb-21-10-2018",
    "titel": "Bepalen van de vervaardigingsprijs volgens KB 21.10.2018 en CBN 132/7",
    "procedure_grondslag": {
      "wettelijk_pct": 75,
      "praktijk_pct": 25,
      "motivering": "KB 21.10.2018 art. 22 + CBN 132/7 §2.1 leggen de samenstelling van de vervaardigingsprijs wettelijk vast (aanschaffingsprijs grondstoffen + direct toerekenbare productiekosten + evenredig deel indirecte productiekosten). Vakdoctrine aspect zit in de invulling (welke verdeelsleutel voor indirect, wat is 'evenredig')."
    },
    "gebaseerd_op_concepten": [
      "vervaardigingsprijs",
      "voorraadwaardering",
      "volledige-kostencalculatie",
      "directe-kosten",
      "indirecte-kosten",
      "materiaalkosten",
      "arbeidskosten",
      "overige-kosten",
      "kostprijs-per-eenheid"
    ],
    "eerste_stap": "Toetsen of het object onder de vervaardigingsprijs-regel valt"
  },
  {
    "id": "berekenen-interpreteren-budgetverschillen",
    "titel": "Berekenen en interpreteren van budgetverschillen (verschillenboekhouding)",
    "procedure_grondslag": {
      "wettelijk_pct": 0,
      "praktijk_pct": 100,
      "motivering": "Verschillenboekhouding (variance analysis) is integraal management-accounting-doctrine zonder Belgische trusted bron. Vereist mens-review wegens praktijk_pct > 70%."
    },
    "gebaseerd_op_concepten": [
      "verschillenboekhouding",
      "prijsverschil-arbeid",
      "voorbepaalde-kosten",
      "werkelijke-kostencalculatie",
      "flexibel-budget",
      "statisch-budget",
      "budgetbeheer",
      "variabele-kosten",
      "vaste-kosten"
    ],
    "eerste_stap": "Voorbereiden van de vergelijkingsbasis"
  },
  {
    "id": "opstellen-master-budget",
    "titel": "Opstellen van een master-budget (operationeel + financieel)",
    "procedure_grondslag": {
      "wettelijk_pct": 5,
      "praktijk_pct": 95,
      "motivering": "Budgetbeheer en master-budget zijn integraal vakdoctrine. Het enige wettelijke raakpunt is dat het bestuursorgaan via WVV-bepalingen (bv. art. 7:228, 5:153) een alarmbelprocedure moet starten wanneer het netto-actief dreigt onder kritieke drempels te dalen — daarbij is een budget vaak praktisch instrument, maar niet wettelijk verplicht. Vereist mens-review wegens praktijk_pct > 70%."
    },
    "gebaseerd_op_concepten": [
      "master-budget",
      "budgetbeheer",
      "budgetprocedure",
      "budget-cyclus",
      "statisch-budget",
      "flexibel-budget",
      "vaste-kosten",
      "variabele-kosten",
      "volledige-kostencalculatie"
    ],
    "eerste_stap": "Plannen van de budgetcyclus en uitgangspunten"
  },
  {
    "id": "opzetten-analytisch-rekeningenstelsel",
    "titel": "Opzetten van een analytisch rekeningenstelsel met kostencentra en kostendragers",
    "procedure_grondslag": {
      "wettelijk_pct": 25,
      "praktijk_pct": 75,
      "motivering": "KB 21.10.2018 (MAR) reserveert klasse 9 vrij voor analytische rekeningen en CBN-advies 3/3 vraagt waarderingsneutraliteit, maar het feitelijke ontwerp (welke kostencentra, welke verdeelsleutels, koppeling met algemene boekhouding) is vakdoctrine en bedrijfsafhankelijk. Vereist mens-review wegens praktijk_pct > 70%."
    },
    "gebaseerd_op_concepten": [
      "analytische-boekhouding",
      "doelstellingen-analytische-boekhouding",
      "rekeningenstelsel-analytisch",
      "kostensoort",
      "kostencentrum",
      "kostendrager",
      "verdeelsleutel",
      "registratiesysteem-waarderingsneutraal",
      "registratiesysteem-eenvoudige-integratie",
      "registratiesysteem-proportionele-integratie"
    ],
    "eerste_stap": "Bepalen van de informatiebehoeften en doelstellingen"
  },
  {
    "id": "toepassen-abc-methode-op-productlijn",
    "titel": "Toepassen van de ABC-methode (Activity Based Costing) op een productlijn",
    "procedure_grondslag": {
      "wettelijk_pct": 5,
      "praktijk_pct": 95,
      "motivering": "ABC-methode is internationale vakdoctrine (Cooper-Kaplan) zonder Belgische trusted wettelijke of CBN-bron. Wettelijk raakvlak is enkel dat een ABC-toerekening kan dienen als 'evenredig deel' indirecte productiekosten conform KB 21.10.2018 art. 22, mits consistent toegepast. Vereist mens-review wegens praktijk_pct > 70%."
    },
    "gebaseerd_op_concepten": [
      "abc-methode",
      "indirecte-kosten",
      "volledige-kostencalculatie",
      "verdeelsleutel",
      "kostprijs-per-eenheid",
      "kostendrager",
      "overige-kosten",
      "costing-methodes-vergelijking"
    ],
    "eerste_stap": "Identificeren van de activiteiten in het productieproces"
  },
  {
    "id": "toepassen-direct-costing-en-contributiemarge",
    "titel": "Toepassen van direct costing en contributiemarge-analyse",
    "procedure_grondslag": {
      "wettelijk_pct": 10,
      "praktijk_pct": 90,
      "motivering": "Direct costing en contributiemarge-analyse zijn management-accounting-doctrine zonder Belgische wettelijke verankering. Wettelijk raakvlak is uitsluitend dat CBN 2012/15 direct costing aanvaardt voor analytische rapportering mits voorraad op de balans aan vervaardigingsprijs gewaardeerd blijft. Vereist mens-review wegens praktijk_pct > 70%."
    },
    "gebaseerd_op_concepten": [
      "direct-costing",
      "contributiemarge",
      "variabele-kosten",
      "vaste-kosten",
      "volledige-kostencalculatie",
      "costing-methodes-vergelijking",
      "marginale-kostprijs",
      "opportuniteitskost",
      "kostprijs-per-eenheid"
    ],
    "eerste_stap": "Identificeren van variabele versus vaste kosten"
  },
  {
    "id": "toepassen-volledige-kostencalculatie",
    "titel": "Toepassen van de volledige kostencalculatie (full costing) op een productie-eenheid",
    "procedure_grondslag": {
      "wettelijk_pct": 35,
      "praktijk_pct": 65,
      "motivering": "De volledige bedrijfskostprijs is vakdoctrine, maar de wettelijke vervaardigingsprijs (KB 21.10.2018 art. 22 + CBN 132/7) gebruikt dezelfde mechanica met expliciete verplichting indirecte productiekosten op te nemen. Voor voorraadwaardering wordt de procedure dus deels wettelijk gestuurd."
    },
    "gebaseerd_op_concepten": [
      "volledige-kostencalculatie",
      "directe-kosten",
      "indirecte-kosten",
      "variabele-kosten",
      "vaste-kosten",
      "kostencentrum",
      "kostendrager",
      "verdeelsleutel",
      "kostprijs-per-eenheid",
      "vervaardigingsprijs"
    ],
    "eerste_stap": "Identificeren van directe versus indirecte kosten"
  },
  {
    "id": "uitvoeren-break-even-analyse",
    "titel": "Uitvoeren van een break-even-analyse en bepalen van de veiligheidsmarge",
    "procedure_grondslag": {
      "wettelijk_pct": 0,
      "praktijk_pct": 100,
      "motivering": "Break-even-analyse is zuivere management-accounting-doctrine zonder Belgische trusted wettelijke of CBN-bron. Geheel gebaseerd op vakdoctrine (CVP-analysis). Vereist mens-review wegens praktijk_pct > 70%."
    },
    "gebaseerd_op_concepten": [
      "break-even-analyse",
      "contributiemarge",
      "vaste-kosten",
      "variabele-kosten",
      "direct-costing"
    ],
    "eerste_stap": "Inventariseren van vaste en variabele kosten + contributiemarge"
  },
  {
    "id": "uitvoeren-make-or-buy-beslissing",
    "titel": "Uitvoeren van een make-or-buy-beslissing op basis van kostenanalyse",
    "procedure_grondslag": {
      "wettelijk_pct": 0,
      "praktijk_pct": 100,
      "motivering": "Make-or-buy-analyse is management-accounting-doctrine zonder Belgische wettelijke grondslag. Vereist mens-review wegens praktijk_pct > 70%."
    },
    "gebaseerd_op_concepten": [
      "kostenanalyse-make-or-buy",
      "marginale-kostprijs",
      "variabele-kosten",
      "vaste-kosten",
      "opportuniteitskost",
      "sunk-cost",
      "contributiemarge",
      "volledige-kostencalculatie"
    ],
    "eerste_stap": "Afbakenen van de beslissingshorizon en scope"
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

