# Minicursus-glue-run minicursus-run-20260516T004452Z — Instructies voor Opus-subagent

**Programmaonderdeel**: 1.4
**Run-id**: minicursus-run-20260516T004452Z
**Gegenereerd op**: 2026-05-16T00:44:52+00:00

## Jouw taak

Vul de `<!-- TODO: Opus-glue ... -->` placeholders in de skeleton-Markdown in.
Schrijf de output als één JSON-object naar stdout met de velden beschreven in
`prompts/minicursus-glue-v1.md`.

## Input-bestanden

- **Skeleton**: `content/studiemateriaal/1.4-geconsolideerde-jaarrekening/minicursus.md`
- **Records-summaries** (31 stuks): zie §Records hieronder
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
    "definitie_snippet": "Het economische eigendomsaandeel dat een moedervennootschap (direct en indirect, naar rato vermenigvuldigd langs elke ketenschakel) in een dochter- of geassocieerde onderneming aanhoudt. Het belangenpercentage bepaalt het deel van het eigen vermogen en het resultaat van die andere onderneming dat aa",
    "rationale_snippet": ""
  },
  {
    "id": "consolidatiekring",
    "naam": "Consolidatiekring",
    "node_type": "begrip",
    "definitie_snippet": "De verzameling entiteiten die in de geconsolideerde jaarrekening worden opgenomen: de moedervennootschap en al haar dochterondernemingen, in voorkomend geval uitgebreid met dochters in ruime zin (WVV art. 3:22). Natuurlijke personen behoren niet tot de consolidatiekring; dat volgt enerzijds uit de d",
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
    "id": "consolidatieverplichting",
    "naam": "Consolidatieverplichting",
    "node_type": "regel",
    "definitie_snippet": "Elke moedervennootschap die, alleen of gezamenlijk, één of meer dochterondernemingen controleert, is in beginsel verplicht een geconsolideerde jaarrekening en een jaarverslag over de geconsolideerde jaarrekening op te stellen, te laten controleren en bekend te maken. Bij een consortium (horizontale ",
    "rationale_snippet": ""
  },
  {
    "id": "consolidatieverschil",
    "naam": "Consolidatieverschil",
    "node_type": "fenomeen",
    "definitie_snippet": "Het verschil dat ontstaat bij de eerste consolidatie tussen (a) de aanschaffingswaarde van een deelneming in een dochter- of geassocieerde onderneming en (b) het overeenkomstige deel van het eigen vermogen van die onderneming op datum van aankoop, na toerekening van het verschil aan onder-/overgewaa",
    "rationale_snippet": ""
  },
  {
    "id": "consortium",
    "naam": "Consortium (horizontale groep)",
    "node_type": "actor",
    "definitie_snippet": "Een horizontale groep van vennootschappen die niet door een onderlinge moeder-dochter-relatie verbonden zijn, maar die onder een gemeenschappelijke (centrale) leiding staan. In een verticale concernstructuur rust de consolidatieplicht bij de moedervennootschap. In een consortium ontbreekt zo'n moede",
    "rationale_snippet": ""
  },
  {
    "id": "controle",
    "naam": "Controle",
    "node_type": "begrip",
    "definitie_snippet": "De bevoegdheid in rechte of in feite om een beslissende invloed uit te oefenen op de aanstelling van de meerderheid van de bestuurders of zaakvoerders van een vennootschap of op de oriëntatie van het beleid ervan. Controle is het sleutelcriterium dat bepaalt of een vennootschap als moedervennootscha",
    "rationale_snippet": ""
  },
  {
    "id": "controlepercentage",
    "naam": "Controlepercentage",
    "node_type": "begrip",
    "definitie_snippet": "Het percentage van de stemrechten dat een vennootschap (direct of indirect via dochterondernemingen) in een andere vennootschap aanhoudt. Het controlepercentage dient om te beoordelen of er sprake is van controle in rechte. In een ketenstructuur (M → A → B) wordt het controlepercentage doorgaans nie",
    "rationale_snippet": ""
  },
  {
    "id": "dochteronderneming",
    "naam": "Dochteronderneming",
    "node_type": "actor",
    "definitie_snippet": "De vennootschap (dochtervennootschap) of het organisme (in ruime zin volgens WVV art. 3:22) ten opzichte waarvan een controlebevoegdheid door een andere vennootschap (de moedervennootschap) bestaat. De WVV-definitie van 'dochteronderneming' is ruimer dan die van 'dochtervennootschap' en omvat evenee",
    "rationale_snippet": ""
  },
  {
    "id": "eerste-consolidatie",
    "naam": "Eerste consolidatie",
    "node_type": "fenomeen",
    "definitie_snippet": "De boekjaar-overschrijdende boekhoudkundige verwerking waarbij een nieuw verworven (of voor het eerst geconsolideerde) dochteronderneming of geassocieerde onderneming voor de eerste maal in de geconsolideerde jaarrekening wordt opgenomen. Bij eerste consolidatie wordt de aanschaffingswaarde van de d",
    "rationale_snippet": ""
  },
  {
    "id": "evenredige-consolidatie",
    "naam": "Evenredige consolidatie (proportionele consolidatie)",
    "node_type": "methode",
    "definitie_snippet": "Een gemeenschappelijke dochter (een vennootschap waarover een beperkt aantal vennoten gezamenlijke controle uitoefenen via overeenkomst) wordt in de geconsolideerde jaarrekening van elke gezamenlijk controlerende vennoot opgenomen naar rato van haar rechten in het kapitaal (of in de inbreng, voor ka",
    "rationale_snippet": ""
  },
  {
    "id": "exclusieve-controle",
    "naam": "Exclusieve controle",
    "node_type": "begrip",
    "definitie_snippet": "De controle die één vennootschap alleen uitoefent over een andere vennootschap, in tegenstelling tot gezamenlijke controle waarbij meerdere vennoten samen beslissen. Exclusieve controle wordt onweerlegbaar vermoed wanneer een vennootschap rechtstreeks of via dochterondernemingen meer dan de helft va",
    "rationale_snippet": ""
  },
  {
    "id": "geassocieerde-onderneming",
    "naam": "Geassocieerde onderneming",
    "node_type": "actor",
    "definitie_snippet": "Een onderneming, andere dan een dochteronderneming of een gemeenschappelijke dochter, waarin een andere onderneming een deelneming en een invloed van betekenis op de oriëntatie van het beleid bezit. Een invloed van betekenis wordt weerlegbaar vermoed wanneer de stemrechten verbonden aan deze deelnem",
    "rationale_snippet": ""
  },
  {
    "id": "geconsolideerd-jaarverslag",
    "naam": "Geconsolideerd jaarverslag",
    "node_type": "begrip",
    "definitie_snippet": "Het door het bestuursorgaan opgestelde toelichtende verslag dat samen met de geconsolideerde jaarrekening wordt opgemaakt, gecontroleerd en bekendgemaakt door elke consolidatieplichtige moedervennootschap (of, voor een consortium, gezamenlijk door de leden). Beschrijft de evolutie van de zaken, het ",
    "rationale_snippet": ""
  },
  {
    "id": "geconsolideerde-jaarrekening",
    "naam": "Geconsolideerde jaarrekening",
    "node_type": "begrip",
    "definitie_snippet": "De jaarrekening die het vermogen, de financiële positie en het resultaat van het geconsolideerde geheel (moedervennootschap + dochterondernemingen in de consolidatiekring) opneemt alsof het om één enkele vennootschap ging. Bestaat uit balans, resultatenrekening en toelichting; deze stukken vormen éé",
    "rationale_snippet": ""
  },
  {
    "id": "gemeenschappelijke-dochteronderneming",
    "naam": "Gemeenschappelijke dochteronderneming",
    "node_type": "actor",
    "definitie_snippet": "De vennootschap of onderneming ten opzichte waarvan een gezamenlijke controle bestaat: een beperkt aantal vennoten oefenen samen controle uit op grond van een overeenkomst dat beslissingen omtrent de oriëntatie van het beleid alleen met hun gemeenschappelijke instemming kunnen worden genomen. In de ",
    "rationale_snippet": ""
  },
  {
    "id": "gezamenlijke-controle",
    "naam": "Gezamenlijke controle",
    "node_type": "begrip",
    "definitie_snippet": "De controle die een beperkt aantal vennoten samen uitoefenen, wanneer zij zijn overeengekomen dat beslissingen omtrent de oriëntatie van het beleid niet zonder hun gemeenschappelijke instemming kunnen worden genomen. Een gemeenschappelijke dochtervennootschap is de vennootschap ten opzichte waarvan ",
    "rationale_snippet": ""
  },
  {
    "id": "groep-van-beperkte-omvang",
    "naam": "Groep van beperkte omvang",
    "node_type": "begrip",
    "definitie_snippet": "Een groep die op geconsolideerde of geaggregeerde basis niet meer dan één van de criteria van WVV art. 1:26, § 1 overschrijdt (jaaromzet, balanstotaal, jaargemiddelde aantal werknemers). Een vennootschap die deel uitmaakt van een groep van beperkte omvang is in beginsel vrijgesteld van de verplichti",
    "rationale_snippet": ""
  },
  {
    "id": "groottecriteria-consolidatie",
    "naam": "Groottecriteria voor de consolidatievrijstelling",
    "node_type": "drempel",
    "definitie_snippet": "Een moedervennootschap is vrijgesteld van de verplichting om een geconsolideerde jaarrekening en jaarverslag op te stellen wanneer haar groep niet meer dan één van de groottecriteria van WVV art. 1:26, § 1 overschrijdt op geconsolideerde of (via vereenvoudigde methode) op geaggregeerde basis (drempe",
    "rationale_snippet": ""
  },
  {
    "id": "horizontale-consolidatie",
    "naam": "Horizontale consolidatie",
    "node_type": "procedure",
    "definitie_snippet": "De consolidatietechniek die wordt toegepast wanneer vennootschappen onder centrale leiding staan zonder dat één rechtspersoon de andere controleert (een consortium / horizontale groep). De vennootschappen die het consortium vormen worden, samen met hun eigen dochters, opgenomen via integrale consoli",
    "rationale_snippet": ""
  },
  {
    "id": "ifrs-consolidatieraamwerk",
    "naam": "IFRS-consolidatieraamwerk (IFRS 3 / IFRS 10 / IFRS 11 / IFRS 12)",
    "node_type": "begrip",
    "definitie_snippet": "Het geheel van IAS/IFRS-standaarden die het wettelijk kader voor geconsolideerde jaarrekeningen onder IFRS vormen, in het bijzonder IFRS 3 (bedrijfscombinaties), IFRS 10 (geconsolideerde jaarrekeningen / definitie controle), IFRS 11 (gezamenlijke regelingen) en IFRS 12 (informatieverschaffing over b",
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
    "definitie_snippet": "Bij de opstelling van de geconsolideerde jaarrekening moeten alle wederzijdse opbrengsten, kosten, vorderingen, schulden en in activa begrepen onderlinge winsten of verliezen tussen de in de consolidatie opgenomen vennootschappen worden geëlimineerd, om te vermijden dat dezelfde transacties dubbel v",
    "rationale_snippet": ""
  },
  {
    "id": "invloed-van-betekenis",
    "naam": "Invloed van betekenis",
    "node_type": "begrip",
    "definitie_snippet": "De macht om deel te nemen aan de financiële en operationele beleidsbeslissingen van een andere onderneming, zonder die beleidsbeslissingen alleen of samen met andere vennoten te kunnen sturen. Invloed van betekenis is het kwalificerend criterium voor een 'geassocieerde onderneming' (WVV art. 1:22): ",
    "rationale_snippet": ""
  },
  {
    "id": "minderheidsbelangen",
    "naam": "Belangen van derden / Aandeel van derden in het resultaat (minderheidsbelangen)",
    "node_type": "fenomeen",
    "definitie_snippet": "Het deel van het eigen vermogen en van het resultaat van integraal geconsolideerde dochters dat kan worden toegerekend aan aandelen die worden gehouden door andere personen dan de moedervennootschap of de dochters in de consolidatiekring. Op de geconsolideerde balans verschijnen die als 'Belangen va",
    "rationale_snippet": ""
  },
  {
    "id": "moedervennootschap",
    "naam": "Moedervennootschap",
    "node_type": "actor",
    "definitie_snippet": "De vennootschap die een controlebevoegdheid uitoefent over een andere vennootschap (de dochtervennootschap). De moedervennootschap is in beginsel verplicht om een geconsolideerde jaarrekening en een jaarverslag over de geconsolideerde jaarrekening op te stellen, te laten controleren en bekend te mak",
    "rationale_snippet": ""
  },
  {
    "id": "step-acquisition",
    "naam": "Step acquisition (trapsgewijze verwerving)",
    "node_type": "fenomeen",
    "definitie_snippet": "Het fenomeen waarbij een onderneming haar belang in een andere onderneming in twee of meer fasen verhoogt, met als gevolg dat (a) een participatie van invloed van betekenis wordt verworven of (b) een bestaande geassocieerde onderneming wordt opgeschaald — al dan niet naar een dochteronderneming. Bij",
    "rationale_snippet": ""
  },
  {
    "id": "uniforme-waarderingsregels-consolidatie",
    "naam": "Uniforme waarderingsregels in de consolidatie",
    "node_type": "regel",
    "definitie_snippet": "De moedervennootschap moet, onverminderd KB WVV art. 3:118, voor haar geconsolideerde jaarrekening dezelfde waarderingsregels toepassen als voor haar enkelvoudige jaarrekening. In uitzonderingsgevallen mag van dit beginsel worden afgeweken op voorwaarde dat de gehanteerde regels stroken met het wett",
    "rationale_snippet": ""
  },
  {
    "id": "vermogensmutatiemethode",
    "naam": "Vermogensmutatiemethode (equity method)",
    "node_type": "methode",
    "definitie_snippet": "Een deelneming wordt in de geconsolideerde jaarrekening niet activum-per-activum opgenomen, maar als één gesynthetiseerde balanspost — initieel gewaardeerd aan het pro-rata aandeel in het eigen vermogen van de betrokken onderneming op datum van aankoop, en vervolgens jaarlijks aangepast voor het pro",
    "rationale_snippet": ""
  },
  {
    "id": "vrijstelling-subconsolidatie",
    "naam": "Vrijstelling van subconsolidatie",
    "node_type": "regel",
    "definitie_snippet": "Een tussenliggende (sub)moedervennootschap wordt vrijgesteld van de verplichting om een geconsolideerde jaarrekening en jaarverslag op te stellen, indien zij zelf de dochtervennootschap is van een moedervennootschap die hogerop een geconsolideerde jaarrekening en jaarverslag opstelt, laat controlere",
    "rationale_snippet": ""
  },
  {
    "id": "wijziging-consolidatiekring",
    "naam": "Wijziging van de consolidatiekring",
    "node_type": "fenomeen",
    "definitie_snippet": "Elke aanpassing aan de samenstelling van de consolidatiekring tussen twee opeenvolgende boekjaren: opname van een nieuw verworven dochter (eerste consolidatie), wegname van een vervreemde of geliquideerde dochter (de- of buitenkringstelling), verschuiving van kwalificatie (van geassocieerde naar doc",
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

# Prompt: Minicursus-glue — Render-fase (v1)

**Doel**: Vul de `<!-- TODO: Opus-glue ... -->` placeholders in de minicursus-skeleton in.

**Model**: claude-opus-4-7 (Opus-subagent)

**Monotoon contract**: Geen feiten-claims in glue-tekst — alleen rationale, beginselen, transities. Geen wikilinks bedenken — die staan al in de skeleton.

---

## Jouw rol

Je schrijft de verbindende, pedagogische tekst die de deterministisch gegenereerde skeleton omzet in een leesbare minicursus. Je vult GEEN nieuwe feiten in. Je verbindt bestaande concepten aan onderliggende beginselen en legt transities uit.

---

## Anti-fabricatie-regels (hard)

1. **Geen feiten-claims** in glue-tekst. Gebruik de definitie-snippets in de records-summaries als basis — vat samen, parafraseer, verbind. Kopieer geen wetsartikelnummers of specifieke waarden die je niet in de snippets ziet.

2. **Geen nieuwe wikilinks verzinnen.** De skeleton bevat al alle wikilinks naar concept-fiches en competentie-fiches. Voeg geen `[[...]]`-links toe die niet in de skeleton staan.

3. **Rationale = beginselen-inzicht, niet examen-truc.** Schrijf vanuit "waarom bestaat dit concept / waarom werkt dit zo?" — niet "dit wordt vaak gevraagd op het examen".

4. **Bij gebrek aan grondslag: korte neutrale tekst.** Liever "Dit programmaonderdeel behandelt de wettelijke verplichtingen rond [X]." dan vrije uitvinding.

5. **Oriëntatie-blokken**: gebruik de `rationale_hint` uit het leerpad als startpunt. Verbind altijd aan begrippen die in de records beschreven zijn (de snippets zijn beschikbaar).

---

## Input

Je ontvangt:
1. **Skeleton-Markdown** met `<!-- TODO: Opus-glue ... -->` placeholders
2. **Records-summaries** (id, naam, node_type, definitie-snippet, rationale-snippet)
3. **Competentie-summaries** (id, titel, procedure_grondslag, eerste stap)

---

## Output-formaat (JSON)

Schrijf een JSON-object met de volgende velden. Alle velden zijn Markdown-tekst.

```json
{
  "leesgids_titel": "Leesgids",
  "leesgids_tekst": "<Korte leesgids: hoe gebruik je deze minicursus? Welke volgorde? 2-4 zinnen.>",
  "waarom_po_tekst": "<Waarom telt dit programmaonderdeel in de praktijk? Welk beginsel? 3-5 zinnen. Geen feiten, wel inzicht.>",
  "orientatie": [
    "<Tekst voor oriëntatie-hoofdstuk 0 (als aanwezig)>",
    "<Tekst voor oriëntatie-hoofdstuk 1 (als aanwezig)>"
  ],
  "competentie_intro": [
    "<Intro-tekst voor competentie-hoofdstuk 0 (1-2 zinnen die de competentie contextualiseren)>",
    "..."
  ],
  "thematisch_intro": [
    "<Intro-tekst voor thematisch cluster 0 (1-2 zinnen over de samenhang)>",
    "..."
  ],
  "synthese": "<Synthese-stappenplan: hoe integreer je alles? Verwijst naar de processtappen in de skeleton. 5-10 zinnen.>",
  "examenfocus": "<Wat toetst het examen typisch in dit programmaonderdeel? Welke denkpatronen zijn gevraagd? Geen spoilers — wel meta-inzicht. 3-5 zinnen.>"
}
```

**Arraylengte**: `orientatie`, `competentie_intro` en `thematisch_intro` MOETEN evenveel elementen bevatten als er hoofdstukken van dat type zijn in de skeleton. Als er 2 oriëntatie-hoofdstukken zijn, heeft `orientatie` 2 elementen (ook al is een ervan leeg string "").

---

## Stijlrichtlijnen

- **Toon**: helder, direct, actief — zoals een ervaren collega die uitlegt
- **Lengte per placeholder**: 2-5 zinnen voor intro's, 5-10 zinnen voor synthese en oriëntaties
- **Geen opsommingen in glue-tekst** (opsommingen staan al deterministisch in de skeleton)
- **Gebruik "je"** (directe aanspraak stagiair), niet "men" of "de student"
- **Schrijf in het Nederlands**

