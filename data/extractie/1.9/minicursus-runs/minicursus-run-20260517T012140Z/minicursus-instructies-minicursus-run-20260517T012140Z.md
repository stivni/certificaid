# Minicursus-glue-run minicursus-run-20260517T012140Z — Instructies voor Opus-subagent

**Programmaonderdeel**: 1.9
**Run-id**: minicursus-run-20260517T012140Z
**Gegenereerd op**: 2026-05-17T01:21:40+00:00

## Jouw taak

Vul de `<!-- TODO: Opus-glue ... -->` placeholders in de skeleton-Markdown in.
Schrijf de output als één JSON-object naar stdout met de velden beschreven in
`prompts/minicursus-glue-v1.md`.

## Input-bestanden

- **Skeleton**: `content/studiemateriaal/1-9-financiele-analyse-bekwaamheid.md`
- **Records-summaries** (38 stuks): zie §Records hieronder
- **Competentie-summaries** (6 stuks): zie §Competenties hieronder

## Anti-fabricatie-regels (verplicht)

- Geen feiten-claims in glue-tekst — alleen rationale, beginselen, transities
- Geen wikilinks bedenken — die staan al in de skeleton
- Verbind aan beginselen die in de records beschreven zijn
- Bij twijfel: korte neutrale tekst, geen uitvinding

## Records-summaries

```json
[
  {
    "id": "altman-z-score",
    "naam": "Altman Z-score (faillissement-predictiemodel)",
    "node_type": "methode",
    "definitie_snippet": "Het Altman Z-model voorspelt het faillissementsrisico van een onderneming via een gewogen lineaire combinatie van vijf ratio's. Een lage Z-waarde signaleert verhoogd faillissementsrisico binnen 2 jaar; een hoge Z-waarde wijst op financiële gezondheid. Belangrijk: het is een discriminantmodel, geen w",
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
    "id": "behoefte-aan-bedrijfskapitaal",
    "naam": "Behoefte aan bedrijfskapitaal (BBK)",
    "node_type": "begrip",
    "definitie_snippet": "De behoefte aan bedrijfskapitaal (BBK) is het bedrag dat de onderneming permanent moet financieren omdat haar exploitatiecyclus geld vastzet in voorraden en handelsvorderingen voordat zij van haar klanten betaling krijgt — vermindert door wat ze zelf op krediet bij leveranciers koopt.",
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
    "id": "falen-van-de-onderneming",
    "naam": "Falen van de onderneming (financiële diagnose)",
    "node_type": "fenomeen",
    "definitie_snippet": "Falen van de onderneming is de toestand waarin de onderneming niet meer in staat is haar verbintenissen na te komen — vaak voorafgegaan door een geleidelijke verslechtering van rentabiliteit, solvabiliteit en liquiditeit. Het juridische sluitstuk is faillissement of gerechtelijke reorganisatie; de a",
    "rationale_snippet": ""
  },
  {
    "id": "financiele-analyse-software",
    "naam": "Financiële-analyse-software (IT-tools)",
    "node_type": "begrip",
    "definitie_snippet": "Financiële-analyse-software is software die jaarrekening-gegevens importeert (uit NBB-Centrale voor Balansen of XBRL-bestanden), automatisch ratio's berekent, sector-benchmarking levert en visuele rapporten genereert. Voorbeelden in de Belgische markt: NBB-Online (gratis), Belfius Score, Graydon, Ro",
    "rationale_snippet": ""
  },
  {
    "id": "financiering-met-derdenkapitaal",
    "naam": "Financiering met derdenkapitaal (vreemd vermogen)",
    "node_type": "begrip",
    "definitie_snippet": "Financiering met derdenkapitaal omvat alle middelen die de onderneming aantrekt van externe schuldeisers: banken (bankleningen), obligatiehouders (obligatieleningen), leveranciers (handelsschulden), de fiscus (uitgestelde belastingen) en het personeel (sociale schulden). Op de balans: rubrieken 16-1",
    "rationale_snippet": ""
  },
  {
    "id": "financiering-met-eigen-vermogen",
    "naam": "Financiering met eigen vermogen",
    "node_type": "begrip",
    "definitie_snippet": "Financiering met eigen vermogen verzamelt alle middelen die door de aandeelhouders zijn ingebracht of in de onderneming gereserveerd. Op de balans: kapitaal, uitgiftepremies, herwaarderingsmeerwaarden, reserves en het overgedragen resultaat (rubrieken 10/15).",
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
    "id": "herstructurering-resultatenrekening",
    "naam": "Herstructurering van de resultatenrekening",
    "node_type": "methode",
    "definitie_snippet": "De resultatenrekening wordt herwerkt zodat ze leesbaar wordt vanuit economisch perspectief: opbrengsten en kosten worden gegroepeerd in bedrijfs-, financiële, uitzonderlijke en belastingblokken; binnen het bedrijfsblok wordt de toegevoegde waarde geïsoleerd. Voor verkort/microschema's vraagt dat mee",
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
    "id": "interpretatie-financiele-ratios",
    "naam": "Interpretatie en evaluatie van financiële ratio's (bekwaamheid)",
    "node_type": "methode",
    "definitie_snippet": "Een ratio interpreteren betekent: cijfer naast benchmark plaatsen, vergelijken over tijd, vergelijken over sector, en de cijfer-uitkomst vertalen naar een betekenisvolle diagnose voor het bedrijfsmodel. Niet 'is 1,45 goed of slecht?' maar 'wat betekent 1,45 in deze sector, in dit business model, in ",
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
    "id": "kasstroomoverzicht-drie-segmenten",
    "naam": "Kasstroomoverzicht — operationeel, investerings- en financierings-kasstroom",
    "node_type": "synthese",
    "definitie_snippet": "",
    "rationale_snippet": ""
  },
  {
    "id": "kwantitatieve-financiele-diagnose",
    "naam": "Kwantitatieve modellen voor financiële diagnose — overzicht",
    "node_type": "synthese",
    "definitie_snippet": "",
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
    "id": "ohlson-o-score",
    "naam": "Ohlson O-score (faillissement-predictiemodel via logit)",
    "node_type": "methode",
    "definitie_snippet": "Het Ohlson O-model voorspelt de kans op faillissement via logistische regressie op negen variabelen uit de jaarrekening. Anders dan Altman geeft Ohlson een kansprobabiliteit (tussen 0 en 1) — niet een score-zone.",
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
    "id": "tabel-waardemutaties",
    "naam": "Tabel van waardemutaties (mutatietabel vaste activa)",
    "node_type": "methode",
    "definitie_snippet": "De tabel van waardemutaties toont voor elke rubriek vaste activa de bewegingen van het boekjaar: aanschaffingen, desinvesteringen, overdrachten, afschrijvingen, waardeverminderingen en hun terugnemingen. Ze verbindt de openingsbalans met de eindbalans en is bron voor de kasstroomanalyse.",
    "rationale_snippet": ""
  },
  {
    "id": "toegevoegde-waarde-financiele-analyse",
    "naam": "Toegevoegde waarde (economische maatstaf in financiële analyse)",
    "node_type": "methode",
    "definitie_snippet": "Toegevoegde waarde meet de welvaart die de onderneming zelf creëert door productie of dienstverlening, los van de waarde die ze inkoopt bij derden. Het is de economische bovenbouw van de resultatenrekening: hoeveel waarde voegt de onderneming toe aan de aangekochte goederen en diensten?",
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
    "id": "bepalen-behoefte-aan-bedrijfskapitaal",
    "titel": "Bepalen van de behoefte aan bedrijfskapitaal en de nettokas-positie",
    "procedure_grondslag": {
      "wettelijk_pct": 15,
      "praktijk_pct": 85,
      "motivering": "Geen wettelijke definitie van BBK; volledig vakdoctrine (Ooghe-Van Wymeersch, Vereeck). De balansrubrieken die als input dienen (voorraden klasse 3, vorderingen klasse 40, schulden klasse 44) zijn wel KB WVV-verankerd. Vereist mens-review wegens praktijk_pct > 70%."
    },
    "gebaseerd_op_concepten": [
      "behoefte-aan-bedrijfskapitaal",
      "werkkapitaal",
      "analytische-balans",
      "liquiditeitsratio"
    ],
    "eerste_stap": "Identificeren van de exploitatiecyclus-rubrieken"
  },
  {
    "id": "gebruiken-financiele-analyse-software",
    "titel": "Gebruiken van financiële-analyse-software voor ratio-set en sectorvergelijking",
    "procedure_grondslag": {
      "wettelijk_pct": 10,
      "praktijk_pct": 90,
      "motivering": "Commerciële tools (Bel-First, NBB-Online, Graydon, Belfius Score) zijn marktrealiteit zonder normatieve bron. De NBB-Centrale voor Balansen is wel wettelijk verankerd (Boek III WVV) en levert de standaard-data-bron. Vereist mens-review wegens praktijk_pct > 70%."
    },
    "gebaseerd_op_concepten": [
      "financiele-analyse-software",
      "sectorvergelijking-financiele-analyse",
      "ratio-vier-doelen-vergelijking",
      "interpretatie-financiele-ratios"
    ],
    "eerste_stap": "Kiezen van een gepaste tool voor de analyse-vraag"
  },
  {
    "id": "herstructureren-resultatenrekening-en-toegevoegde-waarde",
    "titel": "Herstructureren van de resultatenrekening en isoleren van de toegevoegde waarde",
    "procedure_grondslag": {
      "wettelijk_pct": 40,
      "praktijk_pct": 60,
      "motivering": "De vier-blokken-indeling van de resultatenrekening (bedrijf, financieel, uitzonderlijk, belasting) en de schema's volledig/verkort/micro zijn vastgelegd in KB WVV. De herwerking tot analytisch-functionele groepering met toegevoegde waarde-isolatie is vakdoctrine (NBB-balansanalyse, Ooghe-Van Wymeersch)."
    },
    "gebaseerd_op_concepten": [
      "herstructurering-resultatenrekening",
      "toegevoegde-waarde-financiele-analyse",
      "analytische-balans"
    ],
    "eerste_stap": "Identificeren van het jaarrekeningschema"
  },
  {
    "id": "opstellen-driesegmenten-kasstroomoverzicht",
    "titel": "Opstellen van een drie-segmenten-kasstroomoverzicht (CFO, CFI, CFF)",
    "procedure_grondslag": {
      "wettelijk_pct": 25,
      "praktijk_pct": 75,
      "motivering": "Het kasstroomoverzicht is in het Belgisch volledig schema (KB WVV) niet wettelijk verplicht; IFRS-rapporteerders volgen IAS 7. De drie-segmenten-structuur en indirecte methode zijn vakdoctrine (NBB-balansanalyse). De inputbronnen (jaarrekening-rubrieken, tabel waardemutaties) zijn wel wettelijk vastgelegd in KB WVV. Vereist mens-review wegens praktijk_pct > 70%."
    },
    "gebaseerd_op_concepten": [
      "kasstroomoverzicht-drie-segmenten",
      "cashflow-analyse",
      "behoefte-aan-bedrijfskapitaal",
      "tabel-waardemutaties",
      "financiering-met-eigen-vermogen",
      "financiering-met-derdenkapitaal"
    ],
    "eerste_stap": "Berekenen van de operationele kasstroom (CFO)"
  },
  {
    "id": "stellen-bekwaamheid-financiele-diagnose",
    "titel": "Stellen van een complete bekwaamheid-financiële diagnose met aanbevelingen aan het management",
    "procedure_grondslag": {
      "wettelijk_pct": 30,
      "praktijk_pct": 70,
      "motivering": "De alarmbel-procedure (WVV art. 7:228 en 2:52) en de signaleringsplicht naar Kamer voor Ondernemingen in Moeilijkheden (Boek XX WER) zijn wettelijk verankerd. De bestuursverslag-risicoparagraaf is KB WVV-verplichting. De synthese-methode en interpretatie zijn vakdoctrine. Vereist mens-review (praktijk_pct = 70%, op de grenslijn)."
    },
    "gebaseerd_op_concepten": [
      "interpretatie-financiele-ratios",
      "falen-van-de-onderneming",
      "kwantitatieve-financiele-diagnose",
      "ratio-vier-doelen-vergelijking",
      "sectorvergelijking-financiele-analyse",
      "horizontale-analyse-jaarrekening",
      "risicoparagraaf-bestuursverslag"
    ],
    "eerste_stap": "Plaatsen van elke ratio in zijn doel-categorie"
  },
  {
    "id": "toepassen-faillissement-predictiemodellen",
    "titel": "Toepassen van kwantitatieve faillissement-predictiemodellen (Altman Z en Ohlson O)",
    "procedure_grondslag": {
      "wettelijk_pct": 5,
      "praktijk_pct": 95,
      "motivering": "Faillissement-predictiemodellen zijn internationale vakdoctrine (Altman 1968, Ohlson 1980). Belgisch recht (Boek XX WER, alarmbel-procedure WVV) levert wel het juridische kader voor falen, maar de modellen zelf zijn geen onderdeel van Belgisch wetgevend kader. Vereist mens-review wegens praktijk_pct > 70%."
    },
    "gebaseerd_op_concepten": [
      "altman-z-score",
      "ohlson-o-score",
      "kwantitatieve-financiele-diagnose",
      "falen-van-de-onderneming"
    ],
    "eerste_stap": "Verzamelen van de input-ratio's voor Altman Z"
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

