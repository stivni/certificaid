# Minicursus-glue-run minicursus-run-20260516T125726Z — Instructies voor Opus-subagent

**Programmaonderdeel**: 1.3
**Run-id**: minicursus-run-20260516T125726Z
**Gegenereerd op**: 2026-05-16T12:57:26+00:00

## Jouw taak

Vul de `<!-- TODO: Opus-glue ... -->` placeholders in de skeleton-Markdown in.
Schrijf de output als één JSON-object naar stdout met de velden beschreven in
`prompts/minicursus-glue-v1.md`.

## Input-bestanden

- **Skeleton**: `content/studiemateriaal/1.3-analyse/minicursus.md`
- **Records-summaries** (33 stuks): zie §Records hieronder
- **Competentie-summaries** (11 stuks): zie §Competenties hieronder

## Anti-fabricatie-regels (verplicht)

- Geen feiten-claims in glue-tekst — alleen rationale, beginselen, transities
- Geen wikilinks bedenken — die staan al in de skeleton
- Verbind aan beginselen die in de records beschreven zijn
- Bij twijfel: korte neutrale tekst, geen uitvinding

## Records-summaries

```json
[
  {
    "id": "algemene-vergadering-toezichtsfunctie",
    "naam": "Algemene vergadering — toezichtsfunctie op jaarrekening",
    "node_type": "actor",
    "definitie_snippet": "De algemene vergadering van aandeelhouders (of leden bij een VZW) is het orgaan dat de jaarrekening goedkeurt. Het bestuursorgaan licht aan de algemene vergadering de financiële toestand en de uitvoering van de begroting toe; de AV beslist of ze de cijfers aanvaardt en kwijting geeft aan bestuurders",
    "rationale_snippet": ""
  },
  {
    "id": "analytische-balans",
    "naam": "Analytische balans (herstructureringsschema)",
    "node_type": "methode",
    "definitie_snippet": "De wettelijke balans omvormen tot een herwerkt schema dat de analyse vereenvoudigt: activa gerangschikt naar liquiditeit, passiva naar opeisbaarheid; bepaalde posten geherklasseerd zodat economisch verband en risico zichtbaar worden.",
    "rationale_snippet": ""
  },
  {
    "id": "bestuursverslag",
    "naam": "Bestuursverslag (jaarverslag)",
    "node_type": "procedure",
    "definitie_snippet": "Het bestuursorgaan stelt een bestuursverslag op dat een getrouw overzicht geeft van de ontwikkeling, de resultaten en de positie van de onderneming, alsmede een beschrijving van de voornaamste risico's en onzekerheden. Het overzicht moet evenwichtig en volledig zijn, in verhouding tot omvang en comp",
    "rationale_snippet": ""
  },
  {
    "id": "cashflow-analyse",
    "naam": "Cashflow (bedrijfscashflow)",
    "node_type": "begrip",
    "definitie_snippet": "Cashflow is het nettoresultaat na belastingen, verhoogd met de niet-kaskosten (afschrijvingen, waardeverminderingen, voorzieningen). Het is een benadering van de cash die de onderneming uit haar eigen werking genereert, vóór investeringen of financieringsbeslissingen.",
    "rationale_snippet": ""
  },
  {
    "id": "cijferanalyses-controle-norm",
    "naam": "Cijferanalyses (controlenorm KMO)",
    "node_type": "regel",
    "definitie_snippet": "De beroepsbeoefenaar dient cijferanalyses uit te voeren (i) bij het identificeren en inschatten van de risico's van een afwijking van materieel belang, (ii) kan ze inzetten als gegevensgerichte controleprocedure, en (iii) voert ze uit aan het einde van de controle om een algehele conclusie te trekke",
    "rationale_snippet": ""
  },
  {
    "id": "commissaris-toezicht-jaarrekening",
    "naam": "Commissaris (extern toezicht op jaarrekening)",
    "node_type": "actor",
    "definitie_snippet": "Een commissaris is een bedrijfsrevisor (lid van het IBR) die door de algemene vergadering benoemd wordt om de jaarrekening te controleren bij vennootschappen die de groottecriteria voor verplichte controle overschrijden. Hij geeft een verklaring af over het getrouwe beeld van de jaarrekening.",
    "rationale_snippet": ""
  },
  {
    "id": "corporate-governance-verklaring",
    "naam": "Corporate-governance-verklaring",
    "node_type": "procedure",
    "definitie_snippet": "Vennootschappen als bedoeld in artikel 2, lid 1, punt a) van Richtlijn 2013/34/EU (i.e. genoteerde en bepaalde andere) moeten een verklaring inzake corporate governance in hun bestuursverslag opnemen. Die verklaring vormt een specifiek deel van het bestuursverslag.",
    "rationale_snippet": ""
  },
  {
    "id": "current-ratio",
    "naam": "Current ratio (liquiditeit in ruime zin)",
    "node_type": "methode",
    "definitie_snippet": "Meten of de vennootschap genoeg vlottende activa heeft tegenover haar schulden op ten hoogste een jaar. De current ratio is de breedst gebruikte liquiditeitsratio in ruime zin.",
    "rationale_snippet": ""
  },
  {
    "id": "debt-equity-ratio",
    "naam": "Debt-equity ratio (schuldgraad)",
    "node_type": "methode",
    "definitie_snippet": "Direct meten hoe groot de vreemde-vermogen-financiering is tegenover het eigen vermogen. Toont de hefboom: 1,5 betekent dat er € 1,50 vreemd vermogen tegenover elke € 1 eigen vermogen staat.",
    "rationale_snippet": ""
  },
  {
    "id": "doelstellingen-financiele-analyse",
    "naam": "Doelstellingen van financiële analyse",
    "node_type": "begrip",
    "definitie_snippet": "De doelstellingen van financiële analyse zijn de specifieke vragen die de analyst over de jaarrekening wil beantwoorden: kan de onderneming haar korte schulden betalen (liquiditeit), is de schuldenstructuur houdbaar (solvabiliteit), levert de onderneming voldoende winst op het ingezet kapitaal (rend",
    "rationale_snippet": ""
  },
  {
    "id": "gebruikers-jaarrekening",
    "naam": "Gebruikers van de jaarrekening",
    "node_type": "begrip",
    "definitie_snippet": "De jaarrekening wordt opgesteld voor en gebruikt door verschillende belanghebbenden met uiteenlopende informatiebehoeften. Elke gebruiker leest dezelfde cijfers met een eigen bril, wat bepaalt welke ratio's en kengetallen voor hem relevant zijn.",
    "rationale_snippet": ""
  },
  {
    "id": "getrouw-beeld-jaarrekening",
    "naam": "Getrouw beeld van de jaarrekening",
    "node_type": "beginsel",
    "definitie_snippet": "De jaarrekening moet een getrouw beeld geven van het vermogen, de financiële positie en het resultaat van de vennootschap. Volstaat de toepassing van de regels in titel 2 en 3 van het uitvoeringsbesluit niet om dat beeld te geven, dan moeten in de toelichting bijkomende inlichtingen worden verstrekt",
    "rationale_snippet": ""
  },
  {
    "id": "historische-evolutie-financiele-analyse",
    "naam": "Historische evolutie in financiële analyse",
    "node_type": "methode",
    "definitie_snippet": "Een ratio of kengetal pas interpreteren in het licht van de eigen historiek over meerdere boekjaren (typisch 3 tot 5). Trends zijn vaak informatiever dan momentopnames — een verslechterende solvabiliteit is alarmerender dan een statisch lage solvabiliteit.",
    "rationale_snippet": ""
  },
  {
    "id": "horizontale-analyse-jaarrekening",
    "naam": "Horizontale analyse (evolutie-analyse)",
    "node_type": "methode",
    "definitie_snippet": "De evolutie van balans- en resultatenposten over meerdere boekjaren in kaart brengen. Elke post wordt uitgedrukt als verandering tegenover een basisjaar (in absolute euro's of in procenten), zodat trends zichtbaar worden.",
    "rationale_snippet": ""
  },
  {
    "id": "intake-financiele-analyse",
    "naam": "Intake (scoping) van financiële analyse",
    "node_type": "procedure",
    "definitie_snippet": "Vóór ratio's te berekenen, identificeer de scope: vanuit welke gebruikersperspectief analyseer je, welke onderneming, welke boekjaren, welke specifieke vragen moet de analyse beantwoorden, en welke bijzondere posten (uitzonderlijke voorzieningen, herwaarderingen, geconsolideerde cijfers vs statutair",
    "rationale_snippet": ""
  },
  {
    "id": "jaarrekening-als-studieobject",
    "naam": "Jaarrekening als studieobject van financiële analyse",
    "node_type": "begrip",
    "definitie_snippet": "Voor de financiële analist is de jaarrekening het samenspel van balans, resultatenrekening en toelichting waarop alle structuur-, ratio- en evolutie-analyses worden gevoerd. Het is geen kennisbron op zich maar het te onderzoeken object — vergelijkbaar met een patiëntdossier voor een arts.",
    "rationale_snippet": ""
  },
  {
    "id": "kamer-ondernemingen-in-moeilijkheden",
    "naam": "Kamer voor ondernemingen in moeilijkheden",
    "node_type": "actor",
    "definitie_snippet": "Een gespecialiseerde kamer binnen de ondernemingsrechtbank die proactief onderzoekt of ondernemingen in financiële moeilijkheden verkeren. Zij krijgt signalen van knipperlichten (achterstand bij RSZ, BTW, niet-neergelegde jaarrekeningen, dagvaardingen) en kan de onderneming uitnodigen voor gesprek.",
    "rationale_snippet": ""
  },
  {
    "id": "klasse-0-niet-in-balans",
    "naam": "Klasse 0 — niet in de balans opgenomen rekeningen",
    "node_type": "begrip",
    "definitie_snippet": "Klasse 0 verzamelt de boekhoudrekeningen (rekeningen 00 tot 07) waarop de vennootschap haar niet in de balans opgenomen rechten en verplichtingen registreert. Deze rekeningen werken paarsgewijs (recht/verplichting met tegenrekening), volgens MAR (Minimum Algemeen Rekeningstelsel).",
    "rationale_snippet": ""
  },
  {
    "id": "liquiditeitsratio",
    "naam": "Liquiditeitsratio (begrip)",
    "node_type": "begrip",
    "definitie_snippet": "Een liquiditeitsratio is een verhoudingsgetal dat de capaciteit van de vennootschap meet om haar schulden op korte termijn (≤ 1 jaar) te betalen met haar vlottende activa of een deel ervan. Het is een categorie van ratio's, geen één enkel cijfer.",
    "rationale_snippet": ""
  },
  {
    "id": "liquiditeitstoets-beslisboom",
    "naam": "Welke liquiditeitstoets gebruik ik? — Beslisboom",
    "node_type": "synthese",
    "definitie_snippet": "",
    "rationale_snippet": ""
  },
  {
    "id": "materieel-belang-jaarrekening",
    "naam": "Materieel belang (materiality)",
    "node_type": "beginsel",
    "definitie_snippet": "Een element heeft materieel belang als 'redelijkerwijze kan worden verwacht dat de weglating of onjuiste vermelding ervan de beslissingen die een gebruiker op basis van de financiële overzichten van een onderneming neemt, zou kunnen beïnvloeden'. Het materieel belang van afzonderlijke posten wordt b",
    "rationale_snippet": ""
  },
  {
    "id": "niet-in-balans-opgenomen-rechten-verplichtingen",
    "naam": "Niet in de balans opgenomen rechten en verplichtingen",
    "node_type": "regel",
    "definitie_snippet": "In de toelichting worden per soort de rechten en verplichtingen vermeld die niet in de balans voorkomen en die het vermogen, de financiële positie of het resultaat van de vennootschap aanmerkelijk kunnen beïnvloeden. Belangrijke rechten en verplichtingen die niet kunnen worden becijferd, worden op p",
    "rationale_snippet": ""
  },
  {
    "id": "ondernemingsraad-sociaal-economische-info",
    "naam": "Ondernemingsraad — sociaal-economische informatie",
    "node_type": "actor",
    "definitie_snippet": "De ondernemingsraad is een paritair orgaan (vertegenwoordigers werkgever + werknemers) in vennootschappen met gemiddeld minstens 100 werknemers. Hij krijgt jaarlijks een uitgebreide 'jaarinformatie' (sociaal-economische informatie) met financiële, economische en sociale gegevens van de onderneming.",
    "rationale_snippet": ""
  },
  {
    "id": "quick-ratio",
    "naam": "Quick ratio (liquiditeit in enge zin, zuurtegraad)",
    "node_type": "methode",
    "definitie_snippet": "Strengere liquiditeitstoets: kan de vennootschap haar korte schulden betalen zónder dat ze voorraden moet verkopen? Voorraden zijn vaak niet snel cash te maken, vooral bij specifieke goederen of dalende vraag. Ook bekend als 'acid test' of 'zuurtegraad'.",
    "rationale_snippet": ""
  },
  {
    "id": "ratio-covenants",
    "naam": "Ratiocovenants (financial covenants)",
    "node_type": "begrip",
    "definitie_snippet": "Een ratiocovenant is een contractuele clausule (typisch in een bankkredietovereenkomst of obligatielening) die de kredietnemer verplicht om bepaalde financiële ratio's binnen een afgesproken bandbreedte te houden. Overschrijding triggert een 'event of default' — de bank kan onmiddellijke terugbetali",
    "rationale_snippet": ""
  },
  {
    "id": "ratio-vier-doelen-vergelijking",
    "naam": "De vier analyse-doelen en hun ratio's — overzicht",
    "node_type": "synthese",
    "definitie_snippet": "",
    "rationale_snippet": ""
  },
  {
    "id": "rentabiliteit-eigen-vermogen-roe",
    "naam": "Rentabiliteit van het eigen vermogen (ROE)",
    "node_type": "methode",
    "definitie_snippet": "Meten welk rendement de onderneming behaalt op het eigen vermogen — het kapitaal dat de aandeelhouders hebben ingezet of laten staan. ROE staat voor 'Return On Equity'. Het kerngetal voor aandeelhouders die willen weten of hun ingezet kapitaal voldoende oplevert.",
    "rationale_snippet": ""
  },
  {
    "id": "rentabiliteit-totaal-activa-roa",
    "naam": "Rentabiliteit van het totaal der activa (ROA)",
    "node_type": "methode",
    "definitie_snippet": "Meten welk rendement de onderneming behaalt op het totaal van haar bezittingen — onafhankelijk van hoe ze die bezittingen heeft gefinancierd. ROA staat voor 'Return On Assets' (rentabiliteit totaal der activa). Het toont de economische rentabiliteit zonder vertekening door belasting- of financiering",
    "rationale_snippet": ""
  },
  {
    "id": "risicoparagraaf-bestuursverslag",
    "naam": "Risicoparagraaf in het bestuursverslag",
    "node_type": "regel",
    "definitie_snippet": "Het bestuursverslag bevat een beschrijving van de voornaamste risico's en onzekerheden waarmee de onderneming geconfronteerd wordt, met inbegrip van de doelstellingen en het beleid inzake het beheer van financiële risico's (prijsrisico, kredietrisico, liquiditeitsrisico en kasstroomrisico) en het he",
    "rationale_snippet": ""
  },
  {
    "id": "sectorvergelijking-financiele-analyse",
    "naam": "Sectorvergelijking (benchmarking)",
    "node_type": "methode",
    "definitie_snippet": "De ratio's en kengetallen van een onderneming plaatsen tegenover de mediaan of het gemiddelde van haar sector. Een ratio die in absolute zin lijkt zwak (of sterk), kan in sectorcontext normaal zijn. Sectorvergelijking maakt de analyse interpreteerbaar.",
    "rationale_snippet": ""
  },
  {
    "id": "solvabiliteitsratio",
    "naam": "Solvabiliteitsratio",
    "node_type": "methode",
    "definitie_snippet": "Meten welk aandeel van de balans gefinancierd is met eigen vermogen — een maatstaf voor structurele schokbestendigheid op middellange en lange termijn. Een vennootschap met hoge solvabiliteit kan tegenslag (verliezen, waardeverminderingen) opvangen zonder direct in betalingsproblemen te komen.",
    "rationale_snippet": ""
  },
  {
    "id": "verticale-analyse-jaarrekening",
    "naam": "Verticale analyse (percentageanalyse, common-size)",
    "node_type": "methode",
    "definitie_snippet": "De samenstelling van balans en resultatenrekening uitdrukken in procenten van een gemeenschappelijke noemer (balanstotaal voor de balans, omzet voor de resultatenrekening). Zo wordt vergelijking tussen ondernemingen van verschillende grootte mogelijk.",
    "rationale_snippet": ""
  },
  {
    "id": "werkkapitaal",
    "naam": "Werkkapitaal (working capital)",
    "node_type": "begrip",
    "definitie_snippet": "Werkkapitaal is het verschil tussen vlottende activa en schulden op ten hoogste een jaar. Het toont de absolute buffer waarmee de onderneming haar lopende activiteiten kan financieren zonder beroep te doen op nieuwe schulden.",
    "rationale_snippet": ""
  }
]
```

## Competentie-summaries

```json
[
  {
    "id": "beoordelen-bestuursverslag-en-niet-financiele-info",
    "titel": "Beoordelen van het bestuursverslag en de niet-financiële informatie",
    "procedure_grondslag": {
      "wettelijk_pct": 75,
      "praktijk_pct": 25,
      "motivering": "Inhoud bestuursverslag, risicoparagraaf en corporate-governance-verklaring is wettelijk geregeld (Richtlijn 2013/34/EU art. 19-20 + KB WVV). De kritische lezing-stijl is vakdoctrine."
    },
    "gebaseerd_op_concepten": [
      "bestuursverslag",
      "risicoparagraaf-bestuursverslag",
      "corporate-governance-verklaring",
      "commissaris-toezicht-jaarrekening",
      "getrouw-beeld-jaarrekening"
    ],
    "eerste_stap": "Verzamelen van het bestuursverslag en het commissarisverslag"
  },
  {
    "id": "beoordelen-werkkapitaal-en-kasstroom",
    "titel": "Beoordelen van het werkkapitaal en de kasstroom van een onderneming",
    "procedure_grondslag": {
      "wettelijk_pct": 15,
      "praktijk_pct": 85,
      "motivering": "Werkkapitaal-formule en cashflow-definitie zijn vakdoctrine. CBN-2011/14 levert wel een Belgische grondslag voor de cashflow-definitie (resultaat + niet-kaskosten). Verdere interpretatie en behoeftenwerkkapitaal is praktijk. Vereist mens-review wegens praktijk_pct > 70%."
    },
    "gebaseerd_op_concepten": [
      "werkkapitaal",
      "cashflow-analyse",
      "analytische-balans",
      "historische-evolutie-financiele-analyse",
      "liquiditeitsratio"
    ],
    "eerste_stap": "Berekenen van het werkkapitaal in twee richtingen"
  },
  {
    "id": "berekenen-interpreteren-liquiditeitsratios",
    "titel": "Berekenen en interpreteren van de liquiditeitsratio's",
    "procedure_grondslag": {
      "wettelijk_pct": 5,
      "praktijk_pct": 95,
      "motivering": "Liquiditeitsratio's zijn vakdoctrine — geen Belgische wettekst legt de formules op. Wettelijke link is uitsluitend dat de balansposten zelf uit KB WVV komen. Vereist mens-review wegens praktijk_pct > 70%."
    },
    "gebaseerd_op_concepten": [
      "liquiditeitsratio",
      "current-ratio",
      "quick-ratio",
      "werkkapitaal",
      "analytische-balans",
      "sectorvergelijking-financiele-analyse"
    ],
    "eerste_stap": "Vertrekken vanuit de analytische balans"
  },
  {
    "id": "berekenen-interpreteren-rentabiliteitsratios",
    "titel": "Berekenen en interpreteren van de rentabiliteitsratio's",
    "procedure_grondslag": {
      "wettelijk_pct": 35,
      "praktijk_pct": 65,
      "motivering": "CBN-2011/14 levert expliciete Belgische grondslag voor de netto- en bruto-ROE/ROA-formules (zowel resultaat- als cashflow-variant). De interpretatie tegen sectormediaan en de hefboom-redenering blijven vakdoctrine."
    },
    "gebaseerd_op_concepten": [
      "rentabiliteit-eigen-vermogen-roe",
      "rentabiliteit-totaal-activa-roa",
      "cashflow-analyse",
      "analytische-balans",
      "sectorvergelijking-financiele-analyse",
      "historische-evolutie-financiele-analyse"
    ],
    "eerste_stap": "Klaarzetten van de bouwstenen uit balans en resultatenrekening"
  },
  {
    "id": "berekenen-interpreteren-solvabiliteitsratios",
    "titel": "Berekenen en interpreteren van de solvabiliteitsratio's",
    "procedure_grondslag": {
      "wettelijk_pct": 5,
      "praktijk_pct": 95,
      "motivering": "Klassieke solvabiliteitsformule (EV/balanstotaal) en debt-equity ratio zijn vakdoctrine; ratio-covenants zijn contractueel (bankpraktijk) niet wettelijk. Vereist mens-review wegens praktijk_pct > 70%."
    },
    "gebaseerd_op_concepten": [
      "solvabiliteitsratio",
      "debt-equity-ratio",
      "analytische-balans",
      "ratio-covenants",
      "sectorvergelijking-financiele-analyse"
    ],
    "eerste_stap": "Vertrekken vanuit de analytische balans"
  },
  {
    "id": "confronteren-toelichting-en-off-balance",
    "titel": "Confronteren van de financiële analyse met de toelichting en off-balance posten",
    "procedure_grondslag": {
      "wettelijk_pct": 75,
      "praktijk_pct": 25,
      "motivering": "Off-balance-verplichtingen worden geregeld door KB W.Venn. art. 25 §3, 91, 94, 94/3 en 97, en CBN-2017/07 + Richtlijn 2013/34/EU art. 16. De rapportering en confrontatie-met-cijfers is praktijk."
    },
    "gebaseerd_op_concepten": [
      "niet-in-balans-opgenomen-rechten-verplichtingen",
      "klasse-0-niet-in-balans",
      "getrouw-beeld-jaarrekening",
      "materieel-belang-jaarrekening",
      "analytische-balans"
    ],
    "eerste_stap": "Doorlezen van de volledige toelichting"
  },
  {
    "id": "formuleren-financiele-diagnose-en-adviezen",
    "titel": "Formuleren van een financiële diagnose en concrete verbeteradviezen",
    "procedure_grondslag": {
      "wettelijk_pct": 30,
      "praktijk_pct": 70,
      "motivering": "Going-concern-beoordeling en signaleringsplicht naar Kamer voor Ondernemingen in Moeilijkheden (Boek XX WER) zijn wettelijk verankerd. Ratio-covenants zijn contractueel. De diagnose-synthese en adviesformulering zijn vakdoctrine."
    },
    "gebaseerd_op_concepten": [
      "doelstellingen-financiele-analyse",
      "kamer-ondernemingen-in-moeilijkheden",
      "ratio-covenants",
      "cijferanalyses-controle-norm",
      "cashflow-analyse",
      "historische-evolutie-financiele-analyse"
    ],
    "eerste_stap": "Synthetiseren van de bevindingen uit alle deelanalyses"
  },
  {
    "id": "opstellen-analytische-balans",
    "titel": "Opstellen van een analytische balans voor een vennootschap",
    "procedure_grondslag": {
      "wettelijk_pct": 20,
      "praktijk_pct": 80,
      "motivering": "Het wettelijke balansschema (KB WVV) volgt al een liquiditeits/opeisbaarheidsordening. De herwerking tot analytische balans (herklassificeren, off-balance integreren, normalisatie) is vakdoctrine zonder Belgische bron."
    },
    "gebaseerd_op_concepten": [
      "analytische-balans",
      "jaarrekening-als-studieobject",
      "werkkapitaal",
      "niet-in-balans-opgenomen-rechten-verplichtingen"
    ],
    "eerste_stap": "Sorteren van de activa volgens liquiditeit"
  },
  {
    "id": "positioneren-toezichtsorganen-rond-jaarrekening",
    "titel": "Positioneren van de toezichtsorganen rond de jaarrekening",
    "procedure_grondslag": {
      "wettelijk_pct": 70,
      "praktijk_pct": 30,
      "motivering": "De rol van algemene vergadering (WVV art. 9:19), commissaris (WVV + ITAA-normen), ondernemingsraad (KB 27 november 1973), KOM (Boek XX WER) is wettelijk verankerd. Ratio-covenants zijn contractueel. De synthese-procedure (welk orgaan vraag je wat) is praktijk."
    },
    "gebaseerd_op_concepten": [
      "algemene-vergadering-toezichtsfunctie",
      "commissaris-toezicht-jaarrekening",
      "ondernemingsraad-sociaal-economische-info",
      "kamer-ondernemingen-in-moeilijkheden",
      "ratio-covenants"
    ],
    "eerste_stap": "In kaart brengen van welke organen op de onderneming van toepassing zijn"
  },
  {
    "id": "uitvoeren-horizontale-verticale-analyse",
    "titel": "Uitvoeren van een horizontale en verticale analyse van de jaarrekening",
    "procedure_grondslag": {
      "wettelijk_pct": 25,
      "praktijk_pct": 75,
      "motivering": "KB WVV verplicht vergelijkende cijfers (horizontale basis grounded). De methode-naam \"horizontaal\" en \"verticaal\" en de % omzet/balanstotaal-rekenwijze zijn vakdoctrine."
    },
    "gebaseerd_op_concepten": [
      "horizontale-analyse-jaarrekening",
      "verticale-analyse-jaarrekening",
      "analytische-balans",
      "historische-evolutie-financiele-analyse",
      "materieel-belang-jaarrekening"
    ],
    "eerste_stap": "Voorbereiden van een werkmatrix over meerdere boekjaren"
  },
  {
    "id": "voorbereiden-financiele-analyse",
    "titel": "Voorbereiden van een financiële analyse van de jaarrekening",
    "procedure_grondslag": {
      "wettelijk_pct": 25,
      "praktijk_pct": 75,
      "motivering": "De doelstelling \"getrouw beeld\" is wettelijk verankerd (KB WVV art. 3:1) en de gebruikers-categorieën hebben deels wettelijke basis (bv. WIB92 art. 321/1 voor fiscus). De intake-procedure zelf (doel definiëren, jaarrekeningen 3-5 boekjaren ophalen, bijzondere posten flaggen) is vakdoctrine zonder Belgische bron."
    },
    "gebaseerd_op_concepten": [
      "intake-financiele-analyse",
      "doelstellingen-financiele-analyse",
      "gebruikers-jaarrekening",
      "jaarrekening-als-studieobject",
      "materieel-belang-jaarrekening"
    ],
    "eerste_stap": "Definiëren van het doel en de gebruiker van de analyse"
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

