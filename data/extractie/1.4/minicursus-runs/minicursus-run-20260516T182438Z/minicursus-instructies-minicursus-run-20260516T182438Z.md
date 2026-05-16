# Minicursus-glue-run minicursus-run-20260516T182438Z — Instructies voor Opus-subagent

**Programmaonderdeel**: 1.4
**Run-id**: minicursus-run-20260516T182438Z
**Gegenereerd op**: 2026-05-16T18:24:38+00:00

## Jouw taak

Vul de `<!-- TODO: Opus-glue ... -->` placeholders in de skeleton-Markdown in.
Schrijf de output als één JSON-object naar stdout met de velden beschreven in
`prompts/minicursus-glue-v1.md`.

## Input-bestanden

- **Skeleton**: `content/studiemateriaal/1-4-geconsolideerde-jaarrekening/minicursus.md`
- **Records-summaries** (32 stuks): zie §Records hieronder
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
    "id": "belangenpercentage",
    "naam": "Belangenpercentage",
    "node_type": "begrip",
    "definitie_snippet": "Het deel van het kapitaal (en dus van het winstrecht) dat een moeder in een dochter of geassocieerde onderneming bezit. Bij een keten van vennootschappen wordt het belangenpercentage van schakel tot schakel vermenigvuldigd. Het belangenpercentage bepaalt welk stuk van het eigen vermogen en het resul",
    "rationale_snippet": ""
  },
  {
    "id": "consolidatiekring",
    "naam": "Consolidatiekring",
    "node_type": "begrip",
    "definitie_snippet": "De lijst van vennootschappen die in de geconsolideerde jaarrekening worden opgenomen: de moeder en al haar dochters. In bepaalde gevallen mag of moet een dochter buiten de lijst worden gehouden; dan wordt zij doorgaans via de vermogensmutatiemethode opgenomen. Natuurlijke personen horen nooit in de ",
    "rationale_snippet": ""
  },
  {
    "id": "consolidatiemethodes-vergelijking",
    "naam": "De vier consolidatiemethodes vergeleken",
    "node_type": "synthese",
    "definitie_snippet": "",
    "rationale_snippet": ""
  },
  {
    "id": "consolidatieplicht-beslisboom",
    "naam": "Moet ik consolideren? — Beslisboom",
    "node_type": "synthese",
    "definitie_snippet": "",
    "rationale_snippet": ""
  },
  {
    "id": "consolidatieverplichting",
    "naam": "Consolidatieverplichting",
    "node_type": "regel",
    "definitie_snippet": "Elke moeder die — alleen of samen met een andere — één of meer dochters controleert, moet een geconsolideerde jaarrekening en een jaarverslag opstellen, laten controleren door een commissaris en publiceren. Bij een consortium (horizontale groep) ligt die plicht gezamenlijk bij de consortium-leden. D",
    "rationale_snippet": ""
  },
  {
    "id": "consolidatieverschil",
    "naam": "Consolidatieverschil",
    "node_type": "fenomeen",
    "definitie_snippet": "Het verschil dat bij de **eerste consolidatie** van een dochter overblijft tussen (a) wat de moeder betaalde voor de aandelen van een dochter of geassocieerde onderneming en (b) haar pro-rata aandeel in het eigen vermogen (EV) van die onderneming op datum van aankoop — nadat je dat verschil zoveel m",
    "rationale_snippet": ""
  },
  {
    "id": "consortium",
    "naam": "Consortium (horizontale groep)",
    "node_type": "actor",
    "definitie_snippet": "Een groep vennootschappen die niet door een moeder-dochter-relatie zijn verbonden, maar wel onder één gemeenschappelijke leiding staan. In een gewone (verticale) groep moet de moeder consolideren. In een consortium is er geen moeder — de consolidatieplicht rust gezamenlijk bij de leden van het conso",
    "rationale_snippet": ""
  },
  {
    "id": "controle",
    "naam": "Controle",
    "node_type": "begrip",
    "definitie_snippet": "De macht — juridisch (in rechte) of feitelijk (in feite) — om beslissende invloed uit te oefenen op een vennootschap: de meerderheid van de bestuurders aanstellen of de hoofdlijn van het beleid bepalen. Controle is het kernbegrip dat bepaalt of een vennootschap als moeder geldt en dus verplicht is o",
    "rationale_snippet": ""
  },
  {
    "id": "controlepercentage",
    "naam": "Controlepercentage",
    "node_type": "begrip",
    "definitie_snippet": "Het percentage van de stemrechten dat een moeder direct of indirect (via dochters) in een andere vennootschap aanhoudt. Het controlepercentage gebruik je om te toetsen of er sprake is van controle in rechte. Belangrijk verschil met belangenpercentage: in een keten (moeder → tussenschakel → onderste ",
    "rationale_snippet": ""
  },
  {
    "id": "dochteronderneming",
    "naam": "Dochteronderneming",
    "node_type": "actor",
    "definitie_snippet": "Een vennootschap waarover een andere vennootschap (de moeder) controle uitoefent. In het WVV is 'dochteronderneming' ruimer dan 'dochtervennootschap': het omvat ook elke instelling naar Belgisch of buitenlands recht — al dan niet openbaar, met of zonder winstoogmerk — zolang ze een commerciële, fina",
    "rationale_snippet": ""
  },
  {
    "id": "eerste-consolidatie",
    "naam": "Eerste consolidatie",
    "node_type": "fenomeen",
    "definitie_snippet": "Het moment waarop een nieuw verworven dochter (of een dochter die je voor het eerst gaat consolideren) voor het eerst in de geconsolideerde jaarrekening wordt opgenomen. Op dat ogenblik vergelijk je wat je voor de aandelen betaalde met jouw pro-rata aandeel in het eigen vermogen van de dochter op de",
    "rationale_snippet": ""
  },
  {
    "id": "evenredige-consolidatie",
    "naam": "Evenredige consolidatie (proportionele consolidatie)",
    "node_type": "methode",
    "definitie_snippet": "Een gemeenschappelijke dochter (een vennootschap die door een beperkt aantal vennoten samen wordt gecontroleerd, op grond van een overeenkomst) neem je in de geconsolideerde jaarrekening van elke gezamenlijk controlerende moeder op naar rato van haar aandeel in het kapitaal (of in de inbreng bij ven",
    "rationale_snippet": ""
  },
  {
    "id": "exclusieve-controle",
    "naam": "Exclusieve controle",
    "node_type": "begrip",
    "definitie_snippet": "De controle die één vennootschap alleen uitoefent over een andere — niet samen met andere vennoten. Exclusieve controle is onweerlegbaar wanneer een vennootschap (rechtstreeks of via dochters) meer dan de helft van de stemrechten in de andere vennootschap bezit, of het recht heeft om de meerderheid ",
    "rationale_snippet": ""
  },
  {
    "id": "geassocieerde-onderneming",
    "naam": "Geassocieerde onderneming",
    "node_type": "actor",
    "definitie_snippet": "Een onderneming waarop een andere onderneming een invloed van betekenis heeft — maar niet voldoende om er controle over uit te oefenen. De geassocieerde is dus geen dochter en geen gemeenschappelijke dochter. Vermoeden: zodra de moeder 20 % of meer van de stemrechten houdt, wordt invloed van beteken",
    "rationale_snippet": ""
  },
  {
    "id": "geconsolideerd-jaarverslag",
    "naam": "Geconsolideerd jaarverslag",
    "node_type": "begrip",
    "definitie_snippet": "Het narratieve (toelichtende) verslag dat het bestuursorgaan samen met de geconsolideerde jaarrekening opmaakt, laat controleren en publiceert. Het beschrijft de evolutie van de zaken, het resultaat en de positie van de groep, gebeurtenissen na balansdatum, de voornaamste risico's, vooruitzichten, e",
    "rationale_snippet": ""
  },
  {
    "id": "geconsolideerde-jaarrekening",
    "naam": "Geconsolideerde jaarrekening",
    "node_type": "begrip",
    "definitie_snippet": "De jaarrekening die het vermogen, de financiële positie en het resultaat van de hele groep (moeder + alle dochters in de consolidatiekring) presenteert alsof het om één bedrijf gaat. Ze bestaat uit balans, resultatenrekening en toelichting — samen één geheel. Ze wordt afgesloten op dezelfde datum al",
    "rationale_snippet": ""
  },
  {
    "id": "gemeenschappelijke-dochteronderneming",
    "naam": "Gemeenschappelijke dochteronderneming",
    "node_type": "actor",
    "definitie_snippet": "Een vennootschap waarover een beperkt aantal vennoten samen controle uitoefenen op basis van een overeenkomst dat beleidsbeslissingen alleen met hun gemeenschappelijke instemming kunnen worden genomen. Standaard wordt een gemeenschappelijke dochter evenredig (pro-rata) geconsolideerd. Is haar bedrij",
    "rationale_snippet": ""
  },
  {
    "id": "gezamenlijke-controle",
    "naam": "Gezamenlijke controle",
    "node_type": "begrip",
    "definitie_snippet": "De controle die een beperkt aantal vennoten samen uitoefenen, op grond van een overeenkomst dat beleidsbeslissingen alleen met hun gemeenschappelijke instemming kunnen worden genomen. De vennootschap die het voorwerp is van die gezamenlijke controle heet een gemeenschappelijke dochter. Onweerlegbaar",
    "rationale_snippet": ""
  },
  {
    "id": "groep-van-beperkte-omvang",
    "naam": "Groep van beperkte omvang",
    "node_type": "begrip",
    "definitie_snippet": "Een groep die op geconsolideerde of geaggregeerde basis hoogstens één van de drie criteria van WVV art. 1:26, § 1 overschrijdt: jaaromzet, balanstotaal en jaargemiddelde personeel. Een vennootschap die deel uitmaakt van een groep van beperkte omvang is in principe vrijgesteld van de plicht om een ge",
    "rationale_snippet": ""
  },
  {
    "id": "groottecriteria-consolidatie",
    "naam": "Groottecriteria voor de consolidatievrijstelling",
    "node_type": "drempel",
    "definitie_snippet": "Een moeder is vrijgesteld van de plicht om een geconsolideerde jaarrekening en jaarverslag op te stellen wanneer haar groep hoogstens één van de groottecriteria van WVV art. 1:26, § 1 overschrijdt. Je toetst op geconsolideerde basis of, via de vereenvoudigde methode, op geaggregeerde basis (dan word",
    "rationale_snippet": ""
  },
  {
    "id": "horizontale-consolidatie",
    "naam": "Horizontale consolidatie",
    "node_type": "procedure",
    "definitie_snippet": "De consolidatietechniek die je toepast wanneer vennootschappen onder gemeenschappelijke leiding staan zonder dat één rechtspersoon de andere controleert — een consortium. De leden van het consortium en hun eigen dochters worden via integrale consolidatie samengevoegd (KB WVV art. 3:124, 1° jo. WVV a",
    "rationale_snippet": ""
  },
  {
    "id": "ifrs-consolidatieraamwerk",
    "naam": "IFRS-consolidatieraamwerk (IFRS 3 / IFRS 10 / IFRS 11 / IFRS 12)",
    "node_type": "begrip",
    "definitie_snippet": "De verzameling IAS/IFRS-standaarden die het wettelijk kader bepalen voor een geconsolideerde jaarrekening onder IFRS. Voor consolidatie zijn vier standaarden centraal: IFRS 3 (bedrijfscombinaties), IFRS 10 (geconsolideerde jaarrekeningen + definitie van controle), IFRS 11 (gezamenlijke regelingen) e",
    "rationale_snippet": ""
  },
  {
    "id": "integrale-consolidatie",
    "naam": "Integrale consolidatie",
    "node_type": "methode",
    "definitie_snippet": "De geconsolideerde jaarrekening voorstellen alsof het geheel van de consoliderende vennootschap en haar exclusief gecontroleerde dochterondernemingen één enkele economische entiteit vormt. De activa, passiva, rechten, verplichtingen, opbrengsten en kosten van de moeder en van haar exclusief gecontro",
    "rationale_snippet": ""
  },
  {
    "id": "intragroep-eliminaties",
    "naam": "Intragroep-eliminaties",
    "node_type": "procedure",
    "definitie_snippet": "Bij het opstellen van de geconsolideerde jaarrekening moet je alle onderlinge opbrengsten en kosten, vorderingen en schulden, en niet-gerealiseerde winsten of verliezen tussen groepsleden schrappen. Anders zou dezelfde transactie dubbel verschijnen, en zou de groep winst boeken op verkopen aan zichz",
    "rationale_snippet": ""
  },
  {
    "id": "invloed-van-betekenis",
    "naam": "Invloed van betekenis",
    "node_type": "begrip",
    "definitie_snippet": "De macht om deel te nemen aan de financiële en operationele beleidsbeslissingen van een andere onderneming, zonder die beslissingen alleen of samen met anderen te kunnen sturen. Invloed van betekenis is het kwalificerende criterium voor een 'geassocieerde onderneming' (WVV art. 1:22): de moeder heef",
    "rationale_snippet": ""
  },
  {
    "id": "minderheidsbelangen",
    "naam": "Belangen van derden (minderheidsbelangen)",
    "node_type": "fenomeen",
    "definitie_snippet": "Het deel van het eigen vermogen en van het resultaat van een integraal geconsolideerde dochter dat toebehoort aan andere aandeelhouders dan de moeder of de andere dochters in de consolidatiekring. Op de geconsolideerde balans verschijnt dat als 'Belangen van derden' aan passiefzijde; in de geconsoli",
    "rationale_snippet": ""
  },
  {
    "id": "moedervennootschap",
    "naam": "Moedervennootschap",
    "node_type": "actor",
    "definitie_snippet": "Een vennootschap die controle uitoefent over een andere vennootschap (de dochter). De moeder is in principe verplicht om een geconsolideerde jaarrekening en een geconsolideerd jaarverslag op te stellen, te laten controleren door de commissaris en te publiceren, zodra ze — alleen of samen met anderen",
    "rationale_snippet": ""
  },
  {
    "id": "step-acquisition",
    "naam": "Step acquisition (trapsgewijze verwerving)",
    "node_type": "fenomeen",
    "definitie_snippet": "Het fenomeen waarbij een onderneming haar belang in een andere onderneming in twee of meer fasen verhoogt — met als gevolg dat (a) een eerste deelneming met invloed van betekenis ontstaat of (b) een bestaande geassocieerde wordt opgeschaald, al dan niet tot dochter. Bij elke trap controleer je of de",
    "rationale_snippet": ""
  },
  {
    "id": "uniforme-waarderingsregels-consolidatie",
    "naam": "Uniforme waarderingsregels in de consolidatie",
    "node_type": "regel",
    "definitie_snippet": "Voor haar geconsolideerde jaarrekening past de moeder dezelfde waarderingsregels toe als voor haar enkelvoudige jaarrekening (onverminderd KB WVV art. 3:118). In uitzonderingsgevallen mag je afwijken, op voorwaarde dat de gehanteerde regels nog steeds met het wettelijk kader stroken; afwijkingen mot",
    "rationale_snippet": ""
  },
  {
    "id": "vermogensmutatiemethode",
    "naam": "Vermogensmutatiemethode (equity method)",
    "node_type": "methode",
    "definitie_snippet": "Een deelneming verschijnt in de geconsolideerde jaarrekening niet activum-per-activum, maar als één samengevatte balanspost. Bij de eerste opname waardeer je die post aan jouw pro-rata aandeel in het eigen vermogen van de andere onderneming op de datum van aankoop. Daarna pas je die boekwaarde elk b",
    "rationale_snippet": ""
  },
  {
    "id": "vrijstelling-subconsolidatie",
    "naam": "Vrijstelling van subconsolidatie",
    "node_type": "regel",
    "definitie_snippet": "Een tussenliggende (sub)moeder is vrijgesteld van de plicht om een geconsolideerde jaarrekening en jaarverslag op te stellen, op voorwaarde dat: (1) ze zelf dochter is van een hogere moeder die hogerop al consolideert; (2) die hogere moeder de geconsolideerde jaarrekening en het jaarverslag opmaakt,",
    "rationale_snippet": ""
  },
  {
    "id": "wijziging-consolidatiekring",
    "naam": "Wijziging van de consolidatiekring",
    "node_type": "fenomeen",
    "definitie_snippet": "Elke verandering in de samenstelling van de consolidatiekring tussen twee opeenvolgende boekjaren. Vijf typische gevallen: (1) opname van een nieuw verworven dochter (eerste consolidatie); (2) wegvallen van een verkochte of geliquideerde dochter; (3) verschuiving van kwalificatie (van geassocieerde ",
    "rationale_snippet": ""
  }
]
```

## Competentie-summaries

```json
[
  {
    "id": "afbakenen-consolidatiekring",
    "titel": "Afbakenen van de consolidatiekring en beoordelen van uitsluitings- of weglatingsgronden",
    "procedure_grondslag": {
      "wettelijk_pct": 80,
      "praktijk_pct": 20,
      "motivering": "De samenstelling van de kring is wettelijk vastgelegd (WVV art. 3:22 en volgende, KB WVV art. 3:97-3:99). Het afwegen van 'te verwaarlozen betekenis' en 'getrouw beeld' vergt feitelijke beoordeling."
    },
    "gebaseerd_op_concepten": [
      "consolidatiekring",
      "dochteronderneming",
      "moedervennootschap",
      "controle",
      "geassocieerde-onderneming",
      "gemeenschappelijke-dochteronderneming"
    ],
    "eerste_stap": "Identificeren van de consoliderende vennootschap"
  },
  {
    "id": "bepalen-consolidatieverplichting",
    "titel": "Bepalen of een vennootschap een geconsolideerde jaarrekening moet opstellen",
    "procedure_grondslag": {
      "wettelijk_pct": 90,
      "praktijk_pct": 10,
      "motivering": "De plicht volgt rechtstreeks uit WVV art. 3:22 en volgende. Vrijstellingen staan in WVV art. 1:26 en KB WVV. Enkel de feitelijke beoordeling van controle-in-feite en de toetsing aan groottecriteria vragen oordeel."
    },
    "gebaseerd_op_concepten": [
      "consolidatieverplichting",
      "moedervennootschap",
      "controle",
      "consortium",
      "vrijstelling-subconsolidatie",
      "groottecriteria-consolidatie",
      "groep-van-beperkte-omvang"
    ],
    "eerste_stap": "Vaststellen of de entiteit als vennootschap kwalificeert"
  },
  {
    "id": "berekenen-controle-en-belangenpercentage",
    "titel": "Berekenen van controle- en belangenpercentage in een ketenstructuur",
    "procedure_grondslag": {
      "wettelijk_pct": 60,
      "praktijk_pct": 40,
      "motivering": "De definities en de drempel (> 50 %) zijn wettelijk. De rekenregels in ketens (controle-% niet vermenigvuldigen, belangen-% wél) zijn praktijkconventies die in de CBN-doctrine en KB WVV-toepassing worden gehanteerd."
    },
    "gebaseerd_op_concepten": [
      "controlepercentage",
      "belangenpercentage",
      "exclusieve-controle",
      "controle"
    ],
    "eerste_stap": "Tekenen van de aandeelhoudersketen"
  },
  {
    "id": "kiezen-consolidatiemethode",
    "titel": "Kiezen van de toe te passen consolidatietechniek per entiteit",
    "procedure_grondslag": {
      "wettelijk_pct": 80,
      "praktijk_pct": 20,
      "motivering": "De koppeling kwalificatie → techniek is wettelijk: KB WVV art. 3:124 en volgende dwingen integrale consolidatie voor dochters, evenredige voor gemeenschappelijke dochters, vermogensmutatie voor geassocieerden. Alleen 'nauwe integratie' van een gemeenschappelijke dochter is een beoordelingselement."
    },
    "gebaseerd_op_concepten": [
      "integrale-consolidatie",
      "evenredige-consolidatie",
      "vermogensmutatiemethode",
      "horizontale-consolidatie",
      "dochteronderneming",
      "gemeenschappelijke-dochteronderneming",
      "geassocieerde-onderneming",
      "consortium"
    ],
    "eerste_stap": "Vaststellen van de kwalificatie per entiteit"
  },
  {
    "id": "kwalificeren-relatie-deelneming",
    "titel": "Kwalificeren van de relatie met een deelneming (controle, gezamenlijke controle of invloed van betekenis)",
    "procedure_grondslag": {
      "wettelijk_pct": 75,
      "praktijk_pct": 25,
      "motivering": "De drempelvermoedens (> 50 %, 50/50 met overeenkomst, ≥ 20 %) zijn wettelijk vastgelegd in WVV art. 1:14-1:22. Controle-in-feite en het weerleggen van het 20 %-vermoeden vergen feitelijke beoordeling."
    },
    "gebaseerd_op_concepten": [
      "controle",
      "exclusieve-controle",
      "gezamenlijke-controle",
      "invloed-van-betekenis",
      "dochteronderneming",
      "geassocieerde-onderneming",
      "gemeenschappelijke-dochteronderneming"
    ],
    "eerste_stap": "Vaststellen van het stemrechtpercentage"
  },
  {
    "id": "toepassen-uniforme-waarderingsregels",
    "titel": "Toepassen van uniforme waarderingsregels en hercorrigeren van enkelvoudige cijfers",
    "procedure_grondslag": {
      "wettelijk_pct": 85,
      "praktijk_pct": 15,
      "motivering": "De plicht en de uitzonderingen volgen rechtstreeks uit KB WVV art. 3:116-3:118. De motivering en de feitelijke aanpassingen vergen een beperkte mate van praktijkoordeel."
    },
    "gebaseerd_op_concepten": [
      "uniforme-waarderingsregels-consolidatie",
      "geconsolideerde-jaarrekening",
      "integrale-consolidatie"
    ],
    "eerste_stap": "Inventariseren van de waarderingsregels"
  },
  {
    "id": "uitvoeren-eerste-consolidatie",
    "titel": "Uitvoeren van de eerste consolidatie van een nieuw verworven dochter of geassocieerde onderneming",
    "procedure_grondslag": {
      "wettelijk_pct": 75,
      "praktijk_pct": 25,
      "motivering": "De stappen volgen KB WVV art. 3:127-3:131 (compensatie, toerekening verschil aan onder- of overgewaardeerde activa, boeking residueel consolidatieverschil, afschrijving). De waardering van stille meer- of minderwaarden en de keuze van de afschrijvingsduur vergen oordeel."
    },
    "gebaseerd_op_concepten": [
      "eerste-consolidatie",
      "consolidatieverschil",
      "integrale-consolidatie",
      "vermogensmutatiemethode",
      "belangenpercentage"
    ],
    "eerste_stap": "Vaststellen van de aanschaffingswaarde van de deelneming"
  },
  {
    "id": "uitvoeren-intragroep-eliminaties",
    "titel": "Uitvoeren van intragroep-eliminaties en berekenen van het aandeel van derden",
    "procedure_grondslag": {
      "wettelijk_pct": 80,
      "praktijk_pct": 20,
      "motivering": "De eliminatieplichten en de berekening van het aandeel van derden zijn wettelijk vastgelegd (KB WVV art. 3:134-3:140). De materialiteitsbeoordeling (verwaarloosbare bedragen, art. 3:139) is een praktijkoordeel."
    },
    "gebaseerd_op_concepten": [
      "intragroep-eliminaties",
      "minderheidsbelangen",
      "integrale-consolidatie",
      "evenredige-consolidatie",
      "belangenpercentage"
    ],
    "eerste_stap": "Identificeren van onderlinge vorderingen en schulden"
  },
  {
    "id": "verwerken-wijziging-consolidatiekring",
    "titel": "Verwerken van een wijziging in de consolidatiekring (inclusief step acquisition)",
    "procedure_grondslag": {
      "wettelijk_pct": 75,
      "praktijk_pct": 25,
      "motivering": "De verwerking is grotendeels wettelijk (KB WVV art. 3:127-3:132 voor eerste consolidatie en realisaties). De behandeling van kantelpunten tussen technieken (vermogensmutatie ↔ integrale of evenredige consolidatie) en transacties onder gemeenschappelijke leiding vergt doctrinair inzicht (CBN-adviezen)."
    },
    "gebaseerd_op_concepten": [
      "wijziging-consolidatiekring",
      "eerste-consolidatie",
      "step-acquisition",
      "consolidatieverschil",
      "vermogensmutatiemethode",
      "integrale-consolidatie"
    ],
    "eerste_stap": "Identificeren van de aard van de wijziging"
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

