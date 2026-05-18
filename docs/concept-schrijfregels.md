# Concept-schrijfregels

Inhoudelijke conventies voor records in `data/concepten/records/*.json` — concepten én competenties (één schema, één API; zie ADR-007 en ADR-019). Wordt door de EXTRACT-agent geladen als prompt-input en geldt evenzeer voor menselijke aanvullingen.

> **Doelpubliek**: stagiair gecertificeerd accountant met boekhoudkundige en fiscale basiskennis — geen jurist.

---

## Wat IS een concept-record?

Een record beschrijft één **tijdloos studieonderwerp** uit het beroep van de gecertificeerd accountant — iets dat een stagiair moet *begrijpen of kunnen* om als professional te handelen. Niet een wetsartikel, niet een examenvraag, niet een vakindeling.

Twee samenhangende tests om geldigheid te valideren:

1. **Domein-onafhankelijkheid**: bestaat dit onderwerp zelfstandig in het accounting-domein, los van een specifiek toepassingscontext of framework? Zo ja → eigen record. Zo nee → bouwsteen binnen een groter record.
2. **Samenhang**: bestaat dit onderwerp al onder een andere naam? Bij twijfel concept-RAG bevragen op **inhoud** (definitie, bouwstenen), niet alleen op naam-similariteit.

### Wat is een bouwsteen?

Een **bouwsteen** is een sub-aspect van een record dat alleen *binnen* dat record zinvol is — een aspect dat niet zelfstandig in het domein bestaat. Voorbeeld: de "tweestappentest IFRS 16" voor lease-classificatie is een bouwsteen van het cluster `leasing-ifrs`, geen eigen begrip — buiten IFRS 16 betekent de tweestappentest niets.

**De bestaansreden-test** (compositie vs aggregatie):
- *"Heeft dit onderwerp een bestaansreden buiten zijn parent-context?"*
- **Nee** → bouwsteen (compositie — leeft binnen de parent, sterft buiten)
- **Ja** → eigen record (aggregatie — zelfstandig domein-object)

Voorbeelden:
- `tweestappentest-IFRS-16` heeft alleen zin binnen IFRS 16-lease-classificatie → bouwsteen van `leasing-ifrs`
- `right-of-use-actief` werkt ook in IAS 36 impairment + IFRS 5 disposal → eigen record
- `randvoorwaarden-controle` heeft alleen zin bij audit-opdracht-aanvaarding → bouwsteen van `aanvaarden-audit-opdracht`-competentie

**Wanneer wordt een bouwsteen een eigen record?**

- Wanneer dezelfde bouwsteen elders in het domein opduikt → zelfstandig
- Wanneer er twee evenwaardige varianten van ontstaan (geen primair + uitzondering, maar twee gelijkwaardige paden) → beide eigen record

---

## Record-types (zes `node_type`-waarden)

Eén taxonomie voor alles — concepten en competenties leven in hetzelfde format, onderscheiden door `node_type`. Zie [ADR-007](adr/ADR-007-conceptmodel.md) voor schema-details.

Alle types delen één optioneel veld: **`situering`** (zie [§Situering](#situering--waarom-bestaat-dit-in-welk-veld) verderop). Andere velden zijn type-specifiek:

| Type | Vraag | Velden-pakket (typisch, naast `situering`) | Voorbeelden |
|---|---|---|---|
| **begrip** | *"Wat is X?"* — defining unit | `definitie` + `voorbeelden[]` + `in_praktijk` + `valkuilen` | arbeidskosten, right-of-use-actief, beroepsgeheim |
| **regel** | *"Wat schrijft de norm voor?"* — normatieve regel of beginsel | `verplichting` of `main_rule` + `voorwaarden` + `valkuilen` + optioneel `drempelwaarden` | art. 3:96 KB WVV, IFRS 16 alinea 100, continuïteitsbeginsel |
| **cluster** | *"Hoe hangt dit fenomeen samen?"* — samengesteld onderwerp dat regels, begrippen en bouwstenen samenbrengt | `definitie` + rijke `bouwstenen` + `voorwaarden` + `vergelijkingsparen` + `valkuilen` + soms `berekeningsmethode` | leasing, consolidatie, COSO ERM, jaarrekening-vzw |
| **synthese** | *"Hoe vergelijk of beslis ik tussen N concepten?"* — cross-record overzicht | `gebaseerd_op_concepten` + één van: `vergelijkingstabel`, `beslisboom`, `stappenplan`, `tijdlijn` + `kerninzichten` | consolidatiemethoden-vergelijking, liquiditeitstoets-beslisboom |
| **autoriteit** | *"Welke institutionele actor doet wat?"* | `definitie` + `rol` + `in_praktijk` | FSMA, ITAA, FOD Financiën, Cel voor Financiële Informatieverwerking |
| **competentie** | *"Wat moet de stagiair kunnen?"* — applied skill | `titel` + `stappen` + `beoordelings_criteria` + optioneel `voorbeelden[]` | kwalificeren-en-boeken-leasing, beoordelen-getrouw-beeld |

> **Schema 1.6-noot** (2026-05-18): het oude `doel`-veld (eerder hoofdveld op cluster + theoretisch op competentie) is geschrapt. 55 records met `doel` zijn mechanisch gemigreerd naar `situering` (zie [ADR-007 §situering](adr/ADR-007-conceptmodel.md)). Voor cluster werkt `definitie` nu als hoofdveld; voor competentie zit de essentie in `titel + stappen[]` (de migratie liet zien dat competenties feitelijk nooit een `doel`-veld droegen).

**Verdwenen of opgegaan** (historische types die niet meer als eigen `node_type` bestaan):

| Oud type | Nieuwe plek |
|---|---|
| `fenomeen` | `cluster` (hernoemd) |
| `actor` | `autoriteit` (hernoemd) |
| `skill` | `competentie` (hernoemd) |
| `procedure` | `competentie` (focus op kunnen-doen) **of** `cluster` met `stappen[]`-bouwsteen (focus op descriptief domein-object) |
| `methode` | `cluster` (een methode is een samengesteld onderwerp met bouwstenen) |
| `afwegingskader` | `cluster` (bouwstenen = afwegingsdimensies) |
| `beginsel` | `regel` (een beginsel is een hoog-niveau normatieve regel) |
| `drempel` | `regel` met `drempelwaarden[]`-veld |
| `casus` | géén eigen record meer — een echte casus wordt opgenomen als `voorbeeld_inline` of `in_praktijk.wereld_voorbeeld` van het bijhorende cluster/begrip |

### Concept vs competentie — scherp onderscheid

```
concept-record    = kennen / inzien  →  "Wat is X? Hoe werkt X? Wanneer geldt X?"
competentie       = kunnen / doen    →  "Hoe pas ik X toe op een case?"
```

Als je merkt dat je een procedure aan het beschrijven bent waar de student *iets moet doen* (interpretatie + keuzes + uitvoeren) → schrijf een **competentie**, geen concept-record. Een procedure die *bestaat als descriptief domein-object* (CBN beschrijft hoe je X boekt) kan een cluster zijn met de stappen als bouwsteen-blok.

---

## Granulariteit

Geen vast aantal records per programmaonderdeel — de domein-regels bepalen het. We zien waar we landen.

**Schaal-signalen** (kwalitatief, geen telling):

- **Te klein** (= "feature van iets groters"): wordt een bouwsteen of veld op een groter record. Voorbeeld: "Specifieke analyse bij vermoeden" → veld `uitzonderingen[]` op het cluster `meldingsplicht-CFI`.
- **Goldilocks**: krijgt eigen record. Voorbeeld: "Verbod op doormelding (tipping-off)".
- **Te groot** (= "hele vakindeling"): krijgt geen record, alleen edges naar de onderliggende records. Voorbeeld: "Antiwitwasregime" — geen record, wel een **synthese** die de losse regels overstijgt.

**Een begrip krijgt alleen een eigen record als het buiten één specifiek framework testbaar is.** Een balanspost die uitsluitend bestaat binnen één regulatorisch regime → bouwsteen van dat regime-cluster. (`right-of-use-actief` ✓: ook IAS 36 impairment + IFRS 5 disposal werken erop; `leaseverplichting-ifrs` ✗: alleen onder IFRS 16 zin.)

---

## Regime-specialisatie — één algemene cluster + N specialisaties

Wanneer hetzelfde fenomeen onder meerdere regulatorische regimes (BE-GAAP, IFRS, fiscaal, ...) wezenlijk verschillend wordt behandeld:

```
leasing                    (cluster — algemeen, regime-overstijgende kern)
├── leasing-be-gaap        (cluster — specialisatie via edge `specialisatie-van: leasing`)
└── leasing-ifrs           (cluster — specialisatie via edge `specialisatie-van: leasing`)
```

- De **algemene cluster** dekt regime-overstijgende kern (definitie, basis-bouwstenen, vergelijking-tussen-regimes als bouwsteen)
- De **regime-clusters** dekken regime-specifieke regels en uitwerkingen
- Verbonden via edge `specialisatie-van` met optioneel facet-veld `regime: IFRS`

Triggers in bronnen die deze splitsing rechtvaardigen: *"onder IFRS / BE-GAAP"*, *"art. KB W.Venn. vs IAS/IFRS"*, *"fiscaal versus boekhoudkundig"*, ...

---

## Smell-tests bij twijfel

- **Definitie-smell**: hoofdveld begint met *"X is..."* zonder voorbehoud, uitzondering of afgrenzing van naburen → mogelijk te abstract. Toets aan domein-onafhankelijkheid.
- **Stappenplan-smell**: hoofdtekst louter nummerlijst van procedurele stappen → eerder competentie of cluster met `stappen[]`-bouwsteen, geen eigen begrip per stap.
- **"Alleen-in-deze-wet"-smell**: het concept verdwijnt als één specifiek artikel zou verdwijnen → twijfelachtig of het werkelijk een fenomeen is.
- **Opsomming-smell**: lopende tekst bevat een opsomming van 3+ items zonder verdere uitleg → vermoedelijk *N gemiste records + 1 synthese* die ze overkoepelt. Geldt ook voor opsommingen zonder leestekens — kijk naar de *betekenis*, niet de vorm.
- **"Wat de wet zegt"-valkuil**: een `valkuil`-veld dat regelinformatie herhaalt → is geen valkuil. Valkuilen beschrijven typische redeneerfouten van studenten, niet de norm zelf.
- **Bron-als-concept-smell**: record-naam = pure bron-aanduiding (`ifrs-verordening-1606-2002`, `cbn-2022-08`, `kb-wvv-uitvoering`, `isa-315`, `iesba-code`, ...). Een **bron** is materiaal (wet, KB, verordening, richtlijn, CBN-advies, ISA/IFRS/IAS-standaard, ITAA-norm, IESBA-code, ...) waaruit kennis wordt afgeleid. Een **concept** is een fenomeen dat zo'n bron behandelt. Splits naar fenomeen-records (bv. `verplichte-ifrs-eu-beursgenoteerden` + `endorsement-procedure-eu`).
- **Compositie-naam-smell**: record-naam bevat `+`, `&`, `en` of komma's tussen wezenlijk verschillende onderwerpen (`jaarrekeningplicht + groottecriteria`, `aankoop & verkoop`). Wijst op gecondenseerd multi-concept. Splits.

---

## Taal en register

1. **Stagiair-niveau Nederlands**. Korte zinnen, actieve vorm. Vakterminologie (balans, afschrijving, controlewerkzaamheden) mag — wetgeeftaal niet.
   - ❌ *"De onderworpen entiteit is gehouden de waakzaamheidsverplichtingen na te leven onder voorbehoud van de bepalingen vervat in artikel 26."*
   - ✅ *"De accountant moet zijn cliënten controleren volgens de antiwitwaswet — behalve in de gevallen die artikel 26 opsomt."*

2. **Verbatim wetstekst** alleen in `source.citation`-velden. Hoofdtekst altijd herschreven in stagiair-Nederlands.

3. **Voorbeelden** in `voorbeelden[]` (schema 1.5; was: `voorbeeld_inline`), niet ingebed in een definitie. Eén concrete situatie per voorbeeld, geen narratief.

4. **Cast-namen voor voorbeelden**: gebruik personages en bedrijven uit `data/concepten/casts/globaal.yaml` (Zelena Bio NV, Aurelia Holding NV, ...). Geen ad-hoc-fictie tenzij de cast geen passend personage levert.

---

## Titel-conventie — afkortingen en anderstalige namen

De `naam`-veld van een record (en de h1-titel van zijn fiche) volgt deze regels:

**1. Officiële afkorting** — als de entiteit een wettelijk of professioneel erkende afkorting heeft, neem die mee in de titel tussen haakjes:

- ✅ `Anti-Money Laundering Compliance Officer (AMLCO)`
- ✅ `Cel voor Financiële Informatieverwerking (CFI)`
- ✅ `Uiteindelijke begunstigde (UBO)`
- ✅ `Wetboek van Vennootschappen en Verenigingen (WVV)`
- ❌ `Materiële vaste activa (MVA)` — MVA is geen officiële afkorting, niet opnemen
- ❌ `Interne controle (IC)` — IC niet in woordenboek, niet officieel — alleen voluit als titel

**2. Anderstalige naam** — als de entiteit zowel een meest-courante naam (vaak Engels in audit-/IFRS-territorium) als een Nederlandstalige tegenhanger heeft: meest-courante als titel, andere als **ondertitel** (`naam_alternatief`-veld):

```yaml
naam: "Anti-Money Laundering Compliance Officer (AMLCO)"
naam_alternatief: "verantwoordelijke voor de naleving van de antiwitwas-verplichtingen"
```

Render-output:

```
# Anti-Money Laundering Compliance Officer (AMLCO)
*verantwoordelijke voor de naleving van de antiwitwas-verplichtingen*
```

**3. Combinatie**: officiële afkorting + anderstalige naam — beide opnemen, afkorting in haakjes bij de courante naam.

**4. Geen anderstalige tegenhanger nodig**: voor termen die alleen in één taal courant zijn (bv. `Beroepsgeheim`, `Antiwitwaswet`), laat `naam_alternatief` leeg.

## Afkortingen — vuistregel

> **Vuistregel**: staat de afkorting in een hedendaags Nederlands woordenboek?
> - **Ja**: afkorting altijd toegestaan. Uitzondering: bij ambiguïteit (verschillende betekenissen) → altijd voluit.
> - **Nee**: eerste vermelding voluit + (afkorting). Bij herhaling in dezelfde paragraaf: afkorting toegestaan. Nieuwe paragraaf → opnieuw introduceren.

| Voorbeeld | Regel | Behandeling |
|---|---|---|
| `btw` | Ja (in woordenboek) | Direct gebruik in elke positie: *"De btw-aangifte..."* |
| `kmo` | Ja | Direct gebruik: *"Een kmo met meer dan 50 werknemers..."* |
| `interne controle` / `IC` | Nee + ambigu (ook *intercommunautair*) | Eerste keer: *"De interne controle (IC) van het bedrijf..."* — daarna IC in dezelfde paragraaf |
| `MVA` voor *materiële vaste activa* | Nee | Altijd voluit. Geen kortvorm, ook niet na introductie — `MVA` is geen ingeburgerde afkorting |
| `CFO` | Ambigu (*Chief Financial Officer* of *cash from operations*) | Altijd voluit; afkorting verboden |
| `IFRS`, `IAS`, `WVV`, `CBN`, `ITAA` | Officiële kortvorm van wettelijke/normgevende instantie | Direct gebruik na eerste introductie van de officiële naam |

Elk veld is een eigen leeshorizon — de stagiair leest velden los. Bij ambiguïteit of nieuwe paragraaf: herintroduceren.

---

## Confidence-labels

Elk inhoudelijk veld heeft een `confidence`:

- **`grounded`** — direct traceerbaar naar een bron-chunk via `source.ref` (verplicht bij grounded). Wijst op gerefereerd materiaal, niet op infereerde redenering.
- **`inferred`** — agent-redenering, synthese, of confidence-mix. Toegestaan, maar herkenbaar gemerkt.
- **Bij twijfel**: leeg laten boven verkeerd labelen. Sparse fields zijn de norm (ADR-007). Een record met enkel `definitie` is geldig.

`inferred-common-knowledge` (bijdrage van algemene accountancy-kennis zonder specifieke bron) mag, maar markeert een **kandidaat voor bron-uitbreiding** — niet voor blijvend gebruik.

---

## Edges — getypeerde verwijzingen

Cross-record relaties als getypeerde edges, **niet** als hyperlink-prose in hoofdtekst (`[[xxx]]`-syntax hoort in `voorbeelden[]` of `in_praktijk`, niet in normatieve hoofdvelden).

**De zeven canonieke edge-types** (na consolidatie 2026-05-18):

| Type | Betekenis | Voorbeeld |
|---|---|---|
| `vereist-kennis-van` | Prerequisite voor begrip | `consolidatieverplichting` → `groottecriteria` |
| `onderdeel-van` | Compositioneel (child → parent) | `tweestappentest` → `leasing-ifrs` |
| `vergelijkt-met` | Parallel/contrast (met optioneel facet-veld `aspect`) | `leasing-be-gaap` → `leasing-ifrs` |
| `getriggerd-door` | Causation, gebeurtenis-keten | `boekjaarafsluiting` → `inventarisatie` |
| `specialisatie-van` | Regime-/sub-type-specialisatie (met optioneel facet-veld `regime`) | `leasing-ifrs` → `leasing` |
| `uitzondering-op` | Exception op een regel | `vrijstelling-subconsolidatie` → `consolidatieverplichting` |
| `verwijst-naar` | Generieke catch-all bij geen specifieke betekenis | gebruikt waar niets anders past |

**Niet meer in gebruik** (gedeprecieerd 2026-05-18): `bevat` (inverse van `onderdeel-van`, redundant), `contrasteert-met` (gefold in `vergelijkt-met`), `vervangt` / `van-toepassing-op` / `alternatief-voor` (te weinig gebruik, vervangen door `verwijst-naar`).

---

## Concretiserings-inhoud — drie soorten, multi-niveau

Een concept-record moet stagiair-leesbaar zijn. Daarvoor drie complementaire content-soorten — elk met eigen rol:

| Soort | Vorm | Doel | Voorbeeld |
|---|---|---|---|
| **in_praktijk** | Plain-language uitleg | Vertaal de abstracte definitie naar stagiair-Nederlands. Geen case, geen cast. | *"Consolidatieverschil = de moeder heeft meer (of minder) betaald dan de dochter boekhoudkundig waard was."* |
| **voorbeeld** | Narratief/scenario met cast | Concrete situatie die de concept demonstreert. Kan eenvoudig (één-zin) of een scenario met stappen zijn. | Scenario: *"Aurelia Holding koopt Zelena Bio voor 1.500 EUR. Eigen vermogen Zelena: 1.200 EUR. Stap 1: ..."* |
| **illustratie** | Gestructureerd artefact | Boeking, balans, verslag, Mermaid-diagram — template-rendered | Een journal entry met debet/credit-rijen |

### Multi-niveau placement

Alle drie kunnen op verschillende niveaus voorkomen — niet alle niveaus verplicht, sparse fields norm:

- **Record-niveau**: `in_praktijk[]`, `voorbeelden[]`, `illustraties[]`
- **Per bouwsteen**: `in_praktijk[]`, `voorbeelden[]`, `illustraties[]` voor specifieke aspecten
- **Per berekeningsmethode** (regel/cluster met getallen): `voorbeelden[]`, `illustraties[]` met ingevulde getallen
- **Per competentie-stap**: `voorbeeld` (single, inline), `illustratie` (single, inline)
- **Binnen een voorbeeld-scenario**: `illustraties[]` inline — de artefacten die uit het scenario volgen blijven dichtbij het verhaal

### `in_praktijk` — lijstje of rich

Twee toegestane vormen:

```yaml
# Eenvoudig lijstje (voor korte krachtige punten):
in_praktijk: ["Wat het in stagiair-taal betekent.", "Wanneer kom je het tegen?", "Wat is de val?"]

# Rich (voor aspect-gestructureerde uitleg):
in_praktijk:
  - aspect: "Wat is het concreet?"
    betekenis: "De moederonderneming heeft meer betaald dan de dochter waard was."
    confidence: "grounded"
    source: {...}
  - aspect: "Wanneer ontstaat het?"
    betekenis: "Bij elke eerste consolidatie waar koopprijs ≠ aandeel in eigen vermogen."
```

Kies de vorm die het concept dient. Eenvoudig lijstje als geen aspect-structuur nodig is.

### `voorbeelden` — eenvoudig of scenario

```yaml
# Eenvoudig (één concrete situatie):
voorbeelden:
  - vorm: "eenvoudig"
    omschrijving: "Aurelia koopt 100% Zelena voor 1.500 EUR. Eigen vermogen Zelena: 1.200 EUR. → consolidatieverschil 300 EUR."
    cast: ["Zelena Bio NV", "Aurelia Holding NV"]

# Scenario (multi-staps narratief):
voorbeelden:
  - vorm: "scenario"
    titel: "Overname Zelena Bio NV"
    cast: ["Zelena Bio NV", "Aurelia Holding NV"]
    omschrijving: "Aurelia koopt 100% van Zelena voor 1.500 EUR. Eigen vermogen Zelena bij overname: 1.200 EUR."
    stappen:
      - "1. Bereken consolidatieverschil: 1.500 - 1.200 = 300 EUR"
      - "2. Boek het verschil als goodwill"
      - "3. Bouw de geconsolideerde balans op"
    illustraties:        # inline binnen het scenario
      - type: "boeking"
        titel: "Boeking eerste consolidatie"
        rijen:
          - {rekening: "211 — Goodwill", debet: 300, credit: null}
          - {rekening: "230 — Deelneming Zelena", debet: 1200, credit: null}
          - {rekening: "55 — Bank", debet: null, credit: 1500}
```

Illustraties **inline** binnen voorbeelden, niet als edge-references — een illustratie hoort bij zijn scenario.

### `illustraties` — vier types

| Type | Structuur | Render |
|---|---|---|
| `boeking` | `rijen[{rekening, debet, credit, omschrijving}]` + optioneel `context` | Tabel met kleurcode, debet=credit-validatie |
| `balans-fragment` | `activa[]` + `passiva[]` of `posten[]` | Tweezijdige tabel, activa=passiva-validatie |
| `verslag-fragment` | `tekst` (markdown) + `verslag_type` + `paragraaf` | Quote-blok met header |
| `mermaid-diagram` | `code` (Mermaid-syntax) + `caption` | Direct embedded |

Elke illustratie heeft ook `confidence`, optioneel `source`, optioneel `cast_used`. Validatie (debet=credit, activa=passiva) gebeurt bij render-tijd; falen genereert een waarschuwing.

## Situering — waarom bestaat dit, in welk veld

`situering` is een optionele string (2–4 zinnen) **op alle 6 node-types** die antwoordt op:

- *Waarom bestaat dit concept?* (welk probleem of belang lost het op?)
- *In welk veld zit het?* (vennootschapsrecht-kapitaalbescherming, boekhoudrecht-jaarrekening, fiscaal-DBI, ...)
- *Waar staat het in het grotere geheel?* (één zin oriëntatie, géén volledige edges-render)

**Verhouding tot nabije velden** (begrip-voorbeeld "wettelijke reserve"):

| Veld | Vraag | Voorbeeld |
|---|---|---|
| `definitie` | Wat is dit? | "5% van nettowinst die in reserve gehouden wordt tot 10% van kapitaal bereikt is." |
| `situering` | Waarom bestaat dit, in welk veld? | "Onderdeel van het regime kapitaalbescherming in het WVV. Beschermt schuldeisers tegen uitkering van inbreng als dividend." |
| `rationale.text` | Welk beginsel verklaart dit? | "Operationaliseert het beginsel 'kapitaal als waarborg voor crediteuren'." |
| `in_praktijk[*]` | Hoe gebruik je dit? | `aspect: "Berekening jaarlijks"`, `betekenis: "Bij elke winstverdeling toetsen tot 10%."` |

**Schrijfregels**:

- Compact: één paragraaf, geen lijst, **geen wikilinks** (situering moet leesbaar zijn zónder edges-resolutie)
- Wetreferentie alleen op regime-niveau ("het WVV", "het Boekhoudbesluit") — geen artikel-citaties
- Confidence: `grounded` als regime direct uit de bron komt; `inferred` bij synthetische plaatsing
- Geen pedagogische framing ("dit is een van drie reserves; vergelijk met X en Y") — die hoort in de minicursus, niet in het record

**Laag-heuristiek (waarom hier, niet in leermateriaal)**: situering verandert mee wanneer de regel/definitie verandert. Dat is het criterium voor data-laag: samen-aanpassen → record. Pedagogische framing per leerpad hoort in de minicursus (zie [studiemateriaal-schrijfregels](studiemateriaal-schrijfregels.md)).

Volledige schema-spec in [ADR-007 §situering](adr/ADR-007-conceptmodel.md).

## Lengte

- **Hoofdveld** (`definitie`, `main_rule`, `verplichting`): ≤ 150 woorden per veld. Langer → splits in bouwstenen.
- **`situering`**: 2–4 zinnen, ≤ 80 woorden. Langer → te uitgebreid; verplaats detail naar `in_praktijk[]` of `rationale`.
- **Voorbeeld omschrijving**: ≤ 80 woorden (eenvoudig); scenario mag langer maar elk stap-blok blijft compact.
- **Bouwsteen tekst**: ≤ 100 woorden plus optioneel `voorbeelden`, `illustraties`, `bron_ref`.
- **In_praktijk-item**: ≤ 40 woorden per item.
