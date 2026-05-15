# Leerpad-propose-run leerpad-run-20260515T185754Z — Instructies voor Opus

**Programmaonderdeel**: 1.4
**Run-id**: leerpad-run-20260515T185754Z
**Gegenereerd op**: 2026-05-15T18:57:54+00:00
**Model**: claude-opus-4-7

## Jouw taak

Stel een leerpad voor programmaonderdeel 1.4 voor
conform `prompts/leerpad-propose-v1.md`.

## Ordening-principe (didactische opbouw)

oriëntatie → conceptuele basis (begrippen/regels) → wie (actoren) →
hoe (procedures/methoden via competenties) → bijzonderheden (uitzonderingen) →
context (IFRS, Europese richtlijn, etc.)

## Anti-fabricatie

- Oriëntatie-blokken MOETEN rationale_hint geven die verwijst naar bestaande
  concept-records (id's hieronder).
- Thematische clusters MOGEN ALLEEN bestaande record-id's bevatten.
- Geen nieuwe competentie-id's bedenken — gebruik alleen id's hieronder.

## Competenties beschikbaar (9 stuks)

```json
[
  {
    "id": "afbakenen-consolidatiekring",
    "titel": "Afbakenen van de consolidatiekring en beoordelen van uitsluitings- of weglatingsgronden",
    "status": "voorgesteld",
    "gebaseerd_op_concepten": [
      "consolidatiekring",
      "dochteronderneming",
      "moedervennootschap",
      "controle",
      "geassocieerde-onderneming",
      "gemeenschappelijke-dochteronderneming"
    ],
    "voortkomend_uit": {
      "taken": [
        "1.4.taak.1"
      ],
      "kenniselementen": [
        "1.4.I.C",
        "1.4.I.B",
        "1.4.I.G",
        "1.4.II.D"
      ]
    },
    "stap_titels": [
      "Identificeren van de consoliderende vennootschap",
      "Inventariseren van alle dochterondernemingen",
      "Beoordelen of een dochter buiten de consolidatiekring mag worden gelaten",
      "Verwerken van weggelaten dochters via vermogensmutatie",
      "Identificeren van geassocieerde ondernemingen en gemeenschappelijke dochterondernemingen"
    ]
  },
  {
    "id": "bepalen-consolidatieverplichting",
    "titel": "Bepalen of een vennootschap een geconsolideerde jaarrekening moet opstellen",
    "status": "voorgesteld",
    "gebaseerd_op_concepten": [
      "consolidatieverplichting",
      "moedervennootschap",
      "controle",
      "consortium",
      "vrijstelling-subconsolidatie",
      "groottecriteria-consolidatie",
      "groep-van-beperkte-omvang"
    ],
    "voortkomend_uit": {
      "taken": [
        "1.4.taak.1"
      ],
      "kenniselementen": [
        "1.4.I.C",
        "1.4.I.B",
        "1.4.II.B"
      ]
    },
    "stap_titels": [
      "Vaststellen of de entiteit rechtspersoonlijkheid heeft en als vennootschap kwalificeert",
      "Vaststellen of er controle bestaat over één of meer dochterondernemingen",
      "Onderzoeken of er sprake is van een consortium (horizontale groep)",
      "Toetsen of de vrijstelling 'groep van beperkte omvang' van toepassing is",
      "Toetsen of de vrijstelling van subconsolidatie van toepassing is",
      "Formuleren van de eindconclusie"
    ]
  },
  {
    "id": "berekenen-controle-en-belangenpercentage",
    "titel": "Berekenen van controle- en belangenpercentage in een ketenstructuur",
    "status": "voorgesteld",
    "gebaseerd_op_concepten": [
      "controlepercentage",
      "belangenpercentage",
      "exclusieve-controle",
      "controle"
    ],
    "voortkomend_uit": {
      "taken": [
        "1.4.taak.1"
      ],
      "kenniselementen": [
        "1.4.I.C",
        "1.4.I.D",
        "1.4.I.E"
      ]
    },
    "stap_titels": [
      "Tekenen van de aandeelhoudersketen",
      "Berekenen van het controlepercentage in elke schakel",
      "Berekenen van het belangenpercentage in elke schakel",
      "Toetsen of er in elke schakel exclusieve controle bestaat",
      "Toepassen van het belangenpercentage in de consolidatieverwerking"
    ]
  },
  {
    "id": "kiezen-consolidatiemethode",
    "titel": "Kiezen van de toe te passen consolidatietechniek per entiteit",
    "status": "voorgesteld",
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
    "voortkomend_uit": {
      "taken": [
        "1.4.taak.1"
      ],
      "kenniselementen": [
        "1.4.I.D",
        "1.4.I.E",
        "1.4.I.B",
        "1.4.II.C"
      ]
    },
    "stap_titels": [
      "Vaststellen van de kwalificatie van de entiteit",
      "Toepassen integrale consolidatie op exclusief gecontroleerde dochters",
      "Toepassen evenredige consolidatie op gemeenschappelijke dochterondernemingen",
      "Toepassen vermogensmutatiemethode op geassocieerde ondernemingen en bepaalde dochters",
      "Toepassen horizontale consolidatie bij een consortium"
    ]
  },
  {
    "id": "kwalificeren-relatie-deelneming",
    "titel": "Kwalificeren van de relatie met een deelneming (controle, gezamenlijke controle of invloed van betekenis)",
    "status": "voorgesteld",
    "gebaseerd_op_concepten": [
      "controle",
      "exclusieve-controle",
      "gezamenlijke-controle",
      "invloed-van-betekenis",
      "dochteronderneming",
      "geassocieerde-onderneming",
      "gemeenschappelijke-dochteronderneming"
    ],
    "voortkomend_uit": {
      "taken": [
        "1.4.taak.1"
      ],
      "kenniselementen": [
        "1.4.I.C",
        "1.4.I.B",
        "1.4.I.D",
        "1.4.I.E",
        "1.4.II.B"
      ]
    },
    "stap_titels": [
      "Vaststellen van het stemrechtpercentage",
      "Toetsen of er exclusieve controle bestaat",
      "Toetsen of er gezamenlijke controle bestaat",
      "Toetsen of er invloed van betekenis bestaat (geen controle)",
      "Formuleren van de kwalificatie"
    ]
  },
  {
    "id": "toepassen-uniforme-waarderingsregels",
    "titel": "Toepassen van uniforme waarderingsregels en hercorrigeren van enkelvoudige cijfers",
    "status": "voorgesteld",
    "gebaseerd_op_concepten": [
      "uniforme-waarderingsregels-consolidatie",
      "geconsolideerde-jaarrekening",
      "integrale-consolidatie"
    ],
    "voortkomend_uit": {
      "taken": [
        "1.4.taak.1"
      ],
      "kenniselementen": [
        "1.4.I.D",
        "1.4.I.B",
        "1.4.I.G"
      ]
    },
    "stap_titels": [
      "Inventariseren van de waarderingsregels van consoliderende vennootschap en dochters",
      "Toetsen aan de waarderingsregels van de consoliderende vennootschap",
      "Doorvoeren van aanpassingsboekingen voor afwijkende dochters",
      "Beoordelen van afwijkingen in uitzonderingsgevallen",
      "Hercorrigeren van fiscale distorsies",
      "Waarborgen van stelselmatigheid in de tijd"
    ]
  },
  {
    "id": "uitvoeren-eerste-consolidatie",
    "titel": "Uitvoeren van de eerste consolidatie van een nieuw verworven dochter of geassocieerde onderneming",
    "status": "voorgesteld",
    "gebaseerd_op_concepten": [
      "eerste-consolidatie",
      "consolidatieverschil",
      "integrale-consolidatie",
      "vermogensmutatiemethode",
      "belangenpercentage"
    ],
    "voortkomend_uit": {
      "taken": [
        "1.4.taak.1"
      ],
      "kenniselementen": [
        "1.4.I.D",
        "1.4.I.E",
        "1.4.I.G",
        "1.4.II.D"
      ]
    },
    "stap_titels": [
      "Vaststellen van de aanschaffingswaarde van de deelneming",
      "Bepalen van het eigen vermogen van de dochter op verwervingsdatum",
      "Toerekenen van het verschil aan onder-/overgewaardeerde activa en passiva",
      "Berekenen en boeken van het residuele consolidatieverschil",
      "Vastleggen van het afschrijvingsplan voor positief consolidatieverschil",
      "Integreren van de cijfers van de dochter in de geconsolideerde jaarrekening"
    ]
  },
  {
    "id": "uitvoeren-intragroep-eliminaties",
    "titel": "Uitvoeren van intragroep-eliminaties en berekenen van het aandeel van derden",
    "status": "voorgesteld",
    "gebaseerd_op_concepten": [
      "intragroep-eliminaties",
      "minderheidsbelangen",
      "integrale-consolidatie",
      "evenredige-consolidatie",
      "belangenpercentage"
    ],
    "voortkomend_uit": {
      "taken": [
        "1.4.taak.1"
      ],
      "kenniselementen": [
        "1.4.I.D",
        "1.4.I.B",
        "1.4.I.F"
      ]
    },
    "stap_titels": [
      "Identificeren van onderlinge vorderingen en schulden",
      "Elimineren van onderlinge vorderingen en schulden",
      "Elimineren van in activa begrepen onderlinge winsten of verliezen",
      "Elimineren van onderlinge opbrengsten en kosten",
      "Aanpassen van de eliminaties voor evenredig geconsolideerde gemeenschappelijke dochters",
      "Beoordelen van materialiteit",
      "Berekenen van het aandeel van derden (belangen van derden)",
      "Aanpassen van de toelichtingsinformatie"
    ]
  },
  {
    "id": "verwerken-wijziging-consolidatiekring",
    "titel": "Verwerken van een wijziging in de consolidatiekring (inclusief step acquisition)",
    "status": "voorgesteld",
    "gebaseerd_op_concepten": [
      "wijziging-consolidatiekring",
      "eerste-consolidatie",
      "step-acquisition",
      "consolidatieverschil",
      "vermogensmutatiemethode",
      "integrale-consolidatie"
    ],
    "voortkomend_uit": {
      "taken": [
        "1.4.taak.1"
      ],
      "kenniselementen": [
        "1.4.I.G",
        "1.4.II.D"
      ]
    },
    "stap_titels": [
      "Identificeren van de aard van de wijziging",
      "Toetsen van kwalificatiewijziging bij belangsverhoging",
      "Verwerken van een eerste consolidatie bij opname van een nieuwe dochter of geassocieerde",
      "Verwerken van een kantelpunt vermogensmutatie → integrale/evenredige consolidatie",
      "Verwerken van een gehele of gedeeltelijke realisatie van aandelen",
      "Verwerken van transacties onder gemeenschappelijke leiding"
    ]
  }
]
```

## Concept-records beschikbaar (30 stuks)

```json
[
  {
    "id": "belangenpercentage",
    "naam": "Belangenpercentage",
    "node_type": "begrip",
    "definitie_snippet": "Het economische eigendomsaandeel dat een moedervennootschap (direct en indirect, naar rato vermenigvuldigd langs elke ketenschakel) in een dochter- of geassocieerde onderneming aanhoudt. Het belangenpercentage bepaalt het deel van het eigen vermogen en het resultaat van die andere onderneming dat aa",
    "linked_anchors": [
      "1.4.I.C",
      "1.4.I.D",
      "1.4.I.E",
      "1.4.taak.1"
    ]
  },
  {
    "id": "consolidatiekring",
    "naam": "Consolidatiekring",
    "node_type": "begrip",
    "definitie_snippet": "De verzameling entiteiten die in de geconsolideerde jaarrekening worden opgenomen: de consoliderende vennootschap en al haar dochterondernemingen, in voorkomend geval uitgebreid met dochters in ruime zin (WVV art. 3:22). Natuurlijke personen behoren niet tot de consolidatiekring; dat volgt enerzijds",
    "linked_anchors": [
      "1.4.I.C",
      "1.4.I.B",
      "1.4.I.G",
      "1.4.II.D",
      "1.4.taak.1"
    ]
  },
  {
    "id": "consolidatieverplichting",
    "naam": "Consolidatieverplichting",
    "node_type": "regel",
    "definitie_snippet": "Elke moedervennootschap die, alleen of gezamenlijk, één of meer dochterondernemingen controleert, is in beginsel verplicht een geconsolideerde jaarrekening en een jaarverslag over de geconsolideerde jaarrekening op te stellen, te laten controleren en bekend te maken. Bij een consortium (horizontale ",
    "linked_anchors": [
      "1.4.I.C",
      "1.4.I.B",
      "1.4.I.F",
      "1.4.II.B",
      "1.4.taak.1"
    ]
  },
  {
    "id": "consolidatieverschil",
    "naam": "Consolidatieverschil",
    "node_type": "fenomeen",
    "definitie_snippet": "Het verschil dat ontstaat bij de eerste consolidatie tussen (a) de aanschaffingswaarde van een deelneming in een dochter- of geassocieerde onderneming en (b) het overeenkomstige deel van het eigen vermogen van die onderneming op verwervingsdatum, na toerekening van het verschil aan onder-/overgewaar",
    "linked_anchors": [
      "1.4.I.D",
      "1.4.I.G",
      "1.4.I.B",
      "1.4.I.E",
      "1.4.taak.1"
    ]
  },
  {
    "id": "consortium",
    "naam": "Consortium (horizontale groep)",
    "node_type": "actor",
    "definitie_snippet": "Een horizontale groep van vennootschappen die niet door een onderlinge moeder-dochter-relatie verbonden zijn, maar die onder een gemeenschappelijke (centrale) leiding staan. In een verticale concernstructuur rust de consolidatieplicht bij de moedervennootschap. In een consortium ontbreekt zo'n moede",
    "linked_anchors": [
      "1.4.I.C",
      "1.4.I.B",
      "1.4.II.B",
      "1.4.taak.1"
    ]
  },
  {
    "id": "controle",
    "naam": "Controle",
    "node_type": "begrip",
    "definitie_snippet": "De bevoegdheid in rechte of in feite om een beslissende invloed uit te oefenen op de aanstelling van de meerderheid van de bestuurders of zaakvoerders van een vennootschap of op de oriëntatie van het beleid ervan. Controle is het sleutelcriterium dat bepaalt of een vennootschap als moedervennootscha",
    "linked_anchors": [
      "1.4.I.C",
      "1.4.I.B",
      "1.4.I.D",
      "1.4.I.E",
      "1.4.I.G",
      "1.4.II.B",
      "1.4.taak.1"
    ]
  },
  {
    "id": "controlepercentage",
    "naam": "Controlepercentage",
    "node_type": "begrip",
    "definitie_snippet": "Het percentage van de stemrechten dat een vennootschap (direct of indirect via dochterondernemingen) in een andere vennootschap aanhoudt. Het controlepercentage dient om te beoordelen of er sprake is van controle in rechte. In een ketenstructuur (M → A → B) wordt het controlepercentage doorgaans nie",
    "linked_anchors": [
      "1.4.I.C",
      "1.4.I.B",
      "1.4.I.D",
      "1.4.taak.1"
    ]
  },
  {
    "id": "dochteronderneming",
    "naam": "Dochteronderneming",
    "node_type": "actor",
    "definitie_snippet": "De vennootschap (dochtervennootschap) of het organisme (in ruime zin volgens WVV art. 3:22) ten opzichte waarvan een controlebevoegdheid door een andere vennootschap (de moedervennootschap) bestaat. De WVV-definitie van 'dochteronderneming' is ruimer dan die van 'dochtervennootschap' en omvat evenee",
    "linked_anchors": [
      "1.4.I.C",
      "1.4.I.B",
      "1.4.I.D",
      "1.4.I.G",
      "1.4.II.B",
      "1.4.taak.1"
    ]
  },
  {
    "id": "eerste-consolidatie",
    "naam": "Eerste consolidatie",
    "node_type": "fenomeen",
    "definitie_snippet": "De boekjaar-overschrijdende boekhoudkundige verwerking waarbij een nieuw verworven (of voor het eerst geconsolideerde) dochteronderneming of geassocieerde onderneming voor de eerste maal in de geconsolideerde jaarrekening wordt opgenomen. Bij eerste consolidatie wordt de aanschaffingswaarde van de d",
    "linked_anchors": [
      "1.4.I.G",
      "1.4.I.D",
      "1.4.I.E",
      "1.4.II.D",
      "1.4.taak.1"
    ]
  },
  {
    "id": "evenredige-consolidatie",
    "naam": "Evenredige consolidatie (proportionele consolidatie)",
    "node_type": "methode",
    "definitie_snippet": "Een gemeenschappelijke dochteronderneming (een vennootschap waarover een beperkt aantal vennoten gezamenlijke controle uitoefenen via overeenkomst) wordt in de geconsolideerde jaarrekening van elke gezamenlijk controlerende vennoot opgenomen naar rato van haar rechten in het kapitaal (of in de inbre",
    "linked_anchors": [
      "1.4.I.D",
      "1.4.I.B",
      "1.4.II.C",
      "1.4.taak.1"
    ]
  },
  {
    "id": "exclusieve-controle",
    "naam": "Exclusieve controle",
    "node_type": "begrip",
    "definitie_snippet": "De controle die één vennootschap alleen uitoefent over een andere vennootschap, in tegenstelling tot gezamenlijke controle waarbij meerdere vennoten samen beslissen. Exclusieve controle wordt onweerlegbaar vermoed wanneer een vennootschap rechtstreeks of via dochterondernemingen meer dan de helft va",
    "linked_anchors": [
      "1.4.I.C",
      "1.4.I.B",
      "1.4.I.D",
      "1.4.taak.1"
    ]
  },
  {
    "id": "geassocieerde-onderneming",
    "naam": "Geassocieerde onderneming",
    "node_type": "actor",
    "definitie_snippet": "Een onderneming, andere dan een dochteronderneming of een gemeenschappelijke dochteronderneming, waarin een andere onderneming een deelneming en een invloed van betekenis op de oriëntatie van het beleid bezit. Een invloed van betekenis wordt weerlegbaar vermoed wanneer de stemrechten verbonden aan d",
    "linked_anchors": [
      "1.4.I.E",
      "1.4.I.G",
      "1.4.I.C",
      "1.4.taak.1"
    ]
  },
  {
    "id": "geconsolideerd-jaarverslag",
    "naam": "Geconsolideerd jaarverslag",
    "node_type": "begrip",
    "definitie_snippet": "Het door het bestuursorgaan opgestelde toelichtende verslag dat samen met de geconsolideerde jaarrekening wordt opgemaakt, gecontroleerd en bekendgemaakt door elke consolidatieplichtige moedervennootschap (of, voor een consortium, gezamenlijk door de leden). Beschrijft de evolutie van de zaken, het ",
    "linked_anchors": [
      "1.4.I.F",
      "1.4.I.C",
      "1.4.II.C",
      "1.4.taak.1"
    ]
  },
  {
    "id": "geconsolideerde-jaarrekening",
    "naam": "Geconsolideerde jaarrekening",
    "node_type": "begrip",
    "definitie_snippet": "De jaarrekening die het vermogen, de financiële positie en het resultaat van het geconsolideerde geheel (consoliderende vennootschap + dochterondernemingen in de consolidatiekring) opneemt alsof het om één enkele vennootschap ging. Bestaat uit balans, resultatenrekening en toelichting; deze stukken ",
    "linked_anchors": [
      "1.4.I.F",
      "1.4.I.C",
      "1.4.II",
      "1.4.II.A",
      "1.4.II.C",
      "1.4.taak.1"
    ]
  },
  {
    "id": "gemeenschappelijke-dochteronderneming",
    "naam": "Gemeenschappelijke dochteronderneming",
    "node_type": "actor",
    "definitie_snippet": "De vennootschap of onderneming ten opzichte waarvan een gezamenlijke controle bestaat: een beperkt aantal vennoten oefenen samen controle uit op grond van een overeenkomst dat beslissingen omtrent de oriëntatie van het beleid alleen met hun gemeenschappelijke instemming kunnen worden genomen. In de ",
    "linked_anchors": [
      "1.4.I.C",
      "1.4.I.D",
      "1.4.taak.1"
    ]
  },
  {
    "id": "gezamenlijke-controle",
    "naam": "Gezamenlijke controle",
    "node_type": "begrip",
    "definitie_snippet": "De controle die een beperkt aantal vennoten samen uitoefenen, wanneer zij zijn overeengekomen dat beslissingen omtrent de oriëntatie van het beleid niet zonder hun gemeenschappelijke instemming kunnen worden genomen. Een gemeenschappelijke dochtervennootschap is de vennootschap ten opzichte waarvan ",
    "linked_anchors": [
      "1.4.I.C",
      "1.4.I.B",
      "1.4.I.D",
      "1.4.taak.1"
    ]
  },
  {
    "id": "groep-van-beperkte-omvang",
    "naam": "Groep van beperkte omvang",
    "node_type": "begrip",
    "definitie_snippet": "Een groep die op geconsolideerde of geaggregeerde basis niet meer dan één van de criteria van WVV art. 1:26, § 1 overschrijdt (jaaromzet, balanstotaal, jaargemiddelde aantal werknemers). Een vennootschap die deel uitmaakt van een groep van beperkte omvang is in beginsel vrijgesteld van de verplichti",
    "linked_anchors": [
      "1.4.I.C",
      "1.4.I.B",
      "1.4.II.B"
    ]
  },
  {
    "id": "groottecriteria-consolidatie",
    "naam": "Groottecriteria voor de consolidatievrijstelling",
    "node_type": "drempel",
    "definitie_snippet": "Een moedervennootschap is vrijgesteld van de verplichting om een geconsolideerde jaarrekening en jaarverslag op te stellen wanneer haar groep niet meer dan één van de groottecriteria van WVV art. 1:26, § 1 overschrijdt op geconsolideerde of (via vereenvoudigde methode) op geaggregeerde basis (drempe",
    "linked_anchors": [
      "1.4.I.C",
      "1.4.I.B",
      "1.4.taak.1"
    ]
  },
  {
    "id": "horizontale-consolidatie",
    "naam": "Horizontale consolidatie",
    "node_type": "procedure",
    "definitie_snippet": "De consolidatietechniek die wordt toegepast wanneer vennootschappen onder centrale leiding staan zonder dat één rechtspersoon de andere controleert (een consortium / horizontale groep). De vennootschappen die het consortium vormen worden, samen met hun eigen dochters, opgenomen via integrale consoli",
    "linked_anchors": [
      "1.4.I.C",
      "1.4.I.B",
      "1.4.I.D",
      "1.4.II.B",
      "1.4.taak.1"
    ]
  },
  {
    "id": "ifrs-consolidatieraamwerk",
    "naam": "IFRS-consolidatieraamwerk (IFRS 3 / IFRS 10 / IFRS 11 / IFRS 12)",
    "node_type": "begrip",
    "definitie_snippet": "Het geheel van IAS/IFRS-standaarden die het wettelijk kader voor geconsolideerde jaarrekeningen onder IFRS vormen, in het bijzonder IFRS 3 (bedrijfscombinaties), IFRS 10 (geconsolideerde jaarrekeningen / definitie controle), IFRS 11 (gezamenlijke regelingen) en IFRS 12 (informatieverschaffing over b",
    "linked_anchors": [
      "1.4.II",
      "1.4.II.A",
      "1.4.II.B",
      "1.4.II.C",
      "1.4.II.D"
    ]
  },
  {
    "id": "integrale-consolidatie",
    "naam": "Integrale consolidatie",
    "node_type": "methode",
    "definitie_snippet": "De geconsolideerde jaarrekening voorstellen alsof het geheel van de consoliderende vennootschap en haar exclusief gecontroleerde dochterondernemingen één enkele economische entiteit vormt. De activa, passiva, rechten, verplichtingen, opbrengsten en kosten van de moeder en van haar exclusief gecontro",
    "linked_anchors": [
      "1.4.I.D",
      "1.4.I.B",
      "1.4.II.C",
      "1.4.taak.1"
    ]
  },
  {
    "id": "intragroep-eliminaties",
    "naam": "Intragroep-eliminaties",
    "node_type": "procedure",
    "definitie_snippet": "Bij de opstelling van de geconsolideerde jaarrekening moeten alle wederzijdse opbrengsten, kosten, vorderingen, schulden en in activa begrepen onderlinge winsten of verliezen tussen de in de consolidatie opgenomen vennootschappen worden geëlimineerd, om te vermijden dat dezelfde transacties dubbel v",
    "linked_anchors": [
      "1.4.I.D",
      "1.4.I.G",
      "1.4.I.B",
      "1.4.taak.1"
    ]
  },
  {
    "id": "invloed-van-betekenis",
    "naam": "Invloed van betekenis",
    "node_type": "begrip",
    "definitie_snippet": "De macht om deel te nemen aan de financiële en operationele beleidsbeslissingen van een andere onderneming, zonder die beleidsbeslissingen alleen of samen met andere vennoten te kunnen sturen. Invloed van betekenis is het kwalificerend criterium voor een 'geassocieerde onderneming' (WVV art. 1:22): ",
    "linked_anchors": [
      "1.4.I.C",
      "1.4.I.E",
      "1.4.I.G",
      "1.4.taak.1"
    ]
  },
  {
    "id": "minderheidsbelangen",
    "naam": "Belangen van derden / Aandeel van derden in het resultaat (minderheidsbelangen)",
    "node_type": "fenomeen",
    "definitie_snippet": "Het deel van het eigen vermogen en van het resultaat van integraal geconsolideerde dochters dat kan worden toegerekend aan aandelen die worden gehouden door andere personen dan de consoliderende vennootschap of de in de consolidatie opgenomen dochters. Op de geconsolideerde balans verschijnen die al",
    "linked_anchors": [
      "1.4.I.D",
      "1.4.I.B",
      "1.4.I.F",
      "1.4.taak.1"
    ]
  },
  {
    "id": "moedervennootschap",
    "naam": "Moedervennootschap",
    "node_type": "actor",
    "definitie_snippet": "De vennootschap die een controlebevoegdheid uitoefent over een andere vennootschap (de dochtervennootschap). De moedervennootschap is in beginsel verplicht om een geconsolideerde jaarrekening en een jaarverslag over de geconsolideerde jaarrekening op te stellen, te laten controleren en bekend te mak",
    "linked_anchors": [
      "1.4.I.C",
      "1.4.I.B",
      "1.4.I.D",
      "1.4.I.F",
      "1.4.II.B",
      "1.4.taak.1"
    ]
  },
  {
    "id": "step-acquisition",
    "naam": "Step acquisition (trapsgewijze verwerving)",
    "node_type": "fenomeen",
    "definitie_snippet": "Het fenomeen waarbij een onderneming haar belang in een andere onderneming in twee of meer fasen verhoogt, met als gevolg dat (a) een participatie van invloed van betekenis wordt verworven of (b) een bestaande geassocieerde onderneming wordt opgeschaald — al dan niet naar een dochteronderneming. Bij",
    "linked_anchors": [
      "1.4.I.G",
      "1.4.II.D",
      "1.4.taak.1"
    ]
  },
  {
    "id": "uniforme-waarderingsregels-consolidatie",
    "naam": "Uniforme waarderingsregels in de consolidatie",
    "node_type": "regel",
    "definitie_snippet": "De consoliderende vennootschap moet, onverminderd KB WVV art. 3:118, voor haar geconsolideerde jaarrekening dezelfde waarderingsregels toepassen als voor haar enkelvoudige jaarrekening. In uitzonderingsgevallen mag van dit beginsel worden afgeweken op voorwaarde dat de gehanteerde regels stroken met",
    "linked_anchors": [
      "1.4.I.D",
      "1.4.I.B",
      "1.4.I.G",
      "1.4.taak.1"
    ]
  },
  {
    "id": "vermogensmutatiemethode",
    "naam": "Vermogensmutatiemethode (equity method)",
    "node_type": "methode",
    "definitie_snippet": "Een deelneming wordt in de geconsolideerde jaarrekening niet activum-per-activum opgenomen, maar als één gesynthetiseerde balanspost — initieel gewaardeerd aan het pro-rata aandeel in het eigen vermogen van de betrokken onderneming op verwervingsdatum, en vervolgens jaarlijks aangepast voor het pro-",
    "linked_anchors": [
      "1.4.I.E",
      "1.4.I.D",
      "1.4.I.G",
      "1.4.II.C",
      "1.4.taak.1"
    ]
  },
  {
    "id": "vrijstelling-subconsolidatie",
    "naam": "Vrijstelling van subconsolidatie",
    "node_type": "regel",
    "definitie_snippet": "Een tussenliggende (sub)moedervennootschap wordt vrijgesteld van de verplichting om een geconsolideerde jaarrekening en jaarverslag op te stellen, indien zij zelf de dochtervennootschap is van een moedervennootschap die hogerop een geconsolideerde jaarrekening en jaarverslag opstelt, laat controlere",
    "linked_anchors": [
      "1.4.I.C",
      "1.4.I.B",
      "1.4.II.B",
      "1.4.taak.1"
    ]
  },
  {
    "id": "wijziging-consolidatiekring",
    "naam": "Wijziging van de consolidatiekring",
    "node_type": "fenomeen",
    "definitie_snippet": "Elke aanpassing aan de samenstelling van de consolidatiekring tussen twee opeenvolgende boekjaren: opname van een nieuw verworven dochter (eerste consolidatie), wegname van een vervreemde of geliquideerde dochter (de- of buitenkringstelling), verschuiving van kwalificatie (van geassocieerde naar doc",
    "linked_anchors": [
      "1.4.I.G",
      "1.4.II.D",
      "1.4.taak.1"
    ]
  }
]
```

## Programmaonderdeel-context

Titel: Geconsolideerde jaarrekening en wetgeving betreffende de geconsolideerde jaarrekening
Intro: None

## Output-locatie

Schrijf het leerpad als YAML naar:
`data/concepten/leerpaden/1.4.yaml`

Schema: zie `prompts/leerpad-propose-v1.md` §Leerpad-schema

---

## Prompt-referentie (leerpad-propose-v1.md)

# Prompt: Leerpad-opstelling — Fase E (v1)

**Doel**: Stel een didactisch leerpad op voor een programmaonderdeel op basis van beschikbare competenties + concept-records.

**Model**: claude-opus-4-7 (Opus-subagent — ADR-008 §15)

---

## Jouw rol

Je bent een didactisch ontwerper. Je ordent de beschikbare competenties en concept-clusters in een pedagogisch verantwoorde leesvolgorde voor stagiairs GA/GBA met boekhoudkundige basiskennis.

---

## Anti-fabricatie-regels (hard)

1. **Oriëntatie-blokken MOETEN een `rationale_hint` geven die verwijst naar begrippen of thema's die beschreven zijn in de meegeleverde concept-records.** Geen vrije uitvinding.

2. **Thematische clusters mogen ALLEEN bestaande record-id's bevatten.** Geen id's verzinnen.

3. **Competentie-hoofdstukken verwijzen naar BESTAANDE competentie-id's.** Geen nieuwe competenties bedenken.

4. **Maximaal 2 oriëntatie-blokken per leerpad** — één aan het begin, eventueel één aan het eind (IFRS-context, juridische omkadering, etc.).

---

## Ordening-principe (didactische opbouw)

Gebruik onderstaande volgorde als leidraad (niet rigide):

1. **Oriëntatie** — Wat is X? Waarom? Welk beginsel zit erachter?
2. **Conceptuele basis** — Begrippen en regels die de rest funderen (thematisch cluster)
3. **Wie** — Actoren, verplichtingen, criteria (thematisch of competentie)
4. **Hoe** — Procedures en methoden (competenties, meerdere stappen)
5. **Bijzonderheden** — Uitzonderingen, vrijstellingen, speciale gevallen (thematisch of competentie)
6. **Context** — IFRS, Europese richtlijn, rechtsvergelijking (oriëntatie of thematisch)

---

## Drie hoofdstuk-types

```yaml
# Type 1: oriëntatie — LLM-glue, geen records-binding
- type: oriëntatie
  titel: "Wat is consolideren? Waarom?"
  rationale_hint: "<begrippen uit records, bv. 'groep-fictie + economische realiteit + bescherming derden'>"

# Type 2: competentie — references één competentie-yaml
- type: competentie
  competentie_id: <bestaande-competentie-id>

# Type 3: thematisch — concept-cluster zonder pedagogische omhulling
- type: thematisch
  titel: "<Beschrijvende titel van het cluster>"
  concepten:
    - <bestaande-record-id-1>
    - <bestaande-record-id-2>
```

---

## Output-schema (YAML)

```yaml
programmaonderdeel: "<X.Y>"
titel: "<Volledige naam van het programmaonderdeel>"
status: voorgesteld
schema_version: "1.0"
hoofdstukken:
  - type: oriëntatie
    titel: "<Titel>"
    rationale_hint: "<Hint voor Opus-glue — begrippen/thema's uit records>"

  - type: competentie
    competentie_id: <id>

  - type: thematisch
    titel: "<Titel>"
    concepten:
      - <record-id>

_provenance:
  voorgesteld_door: "leerpad-propose-v1-<run-id>"
  voorgesteld_op: "<ISO-8601-UTC>"
  gecureerd_door: null
  gecureerd_op: null
```

---

## Werkwijze

1. Lees de competentie-summaries: wat zijn de kernvaardigheden?
2. Lees de record-summaries: welke clusters zijn er (begrippen, regels, procedures)?
3. Zoek records die NIET via een competentie gedekt worden maar toch centraal zijn → thematisch cluster
4. Bouw de volgorde op van oriëntatie naar specialisatie
5. Schrijf het leerpad naar `data/concepten/leerpaden/<X.Y>.yaml`

---

## Afsluitend rapport

```
Leerpad-run <id> — samenvatting
=================================
Programmaonderdeel : <X.Y>
Hoofdstukken       : <n> totaal
  Oriëntatie       : <n>
  Competentie      : <n>
  Thematisch       : <n>
Niet gedekte records (geen competentie, geen thematisch cluster): <lijst van id's>
Bestand geschreven : data/concepten/leerpaden/<X.Y>.yaml
```

