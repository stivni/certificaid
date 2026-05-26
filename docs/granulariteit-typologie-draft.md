# Granulariteit-typologie — draft

**Status**: GECONSOLIDEERD in [ADR-030](adr/ADR-030-granulariteit-typologie.md) (2026-05-23, na iteratie 5; aangevuld iteratie 6 — Regel J geïntegreerde Regeling + Regel I anti-patterns filter-categorie & PO-anchor-cohort). Dit document blijft staan als sparring-historiek + stress-test-bijlage + casussen. Voor de canonieke regels: zie ADR-030.
**Doel**: een principieel criterium voor *"wanneer is iets een eigen concept-record, en wanneer is het een sub-element binnen een ander record?"* — als antwoord op de observatie dat de huidige 396 records inconsistent gegranuleerd zijn (`moeder-dochterrichtlijn` als top-level fiche van 21KB, terwijl `dbi-aftrek` als sub-element verstopt zit binnen `belastbare-grondslag-vennootschapsbelasting`).

**Iteratie 5 — paradigma-shift**: in iteraties 1-4 stonden de 4 super-categorieën (Kader/Entiteit/Gebeurtenis/Regeling) centraal. Gebruikersfeedback iter. 5 kantelt dat:
> "we moeten naar het conceptuele kijken... gewoon meerdere concepten bundelen in één groep omdat het een conceptueel geheel vormt (net zoals een Regeling als DBI-aftrek een conceptueel geheel vormt)... vb. ondernemingsvormen — BV — NV — eenmanszaak... dat mengt natuurlijk wel entiteiten en kaders, die lagen hebben ons geholpen om de rol te bepalen, maar ze hangen allemaal aan elkaar."

Nieuw hoofd-principe (§1.5 hieronder): **1 concept-record = 1 conceptueel coherente eenheid = 1 studiefiche**. De 4 super-categorieën blijven als *oriëntatie* ("welke rol speelt dit primair?") maar zijn geen rigide hokjes meer — één concept mag over categorieën heen reiken zolang het conceptueel een geheel vormt.

**Relatie tot bestaand werk**:
- Schema 2.1 v1.5 heeft `concept_type` met 10 waarden (instrument · verrichting · procedure · balanspost · ratio · regime · methode · kader · principe · actor). Beslissing 2026-05-23: **die 10 worden vervangen door de 4 super-categorieën** uit deze typologie. Migratie-mapping in §5.
- Vereist schema-aanpassing (enum-update op `concept_type`). Beperkte impact — 1 veld, 396 records te hertypen.
- **Geen aparte competenties-laag**. Sinds schema 2.1 v1.5 leven competenties (wat-de-stagiair-moet-DOEN/KUNNEN, inclusief inzicht) in `inhoud.accountant_perspectieven[]` per concept-record: per rol × perspectief staat daar wat de accountant met dat concept moet kunnen. De legacy `data/concepten/competenties/`-map is leeg en niet meer in gebruik. Competenties zijn dus *geïntegreerd* in de 4 super-categorieën, niet apart erbuiten.

---

## 1. De vier super-categorieën

| Categorie | Heuristiek "wanneer is iets dit?" | Voorbeelden |
|---|---|---|
| **Kader** | Een professionele aanpak, discipline of techniek. Tree-structuur (rol → sub-domein → techniek). Bevat *eigen* disciplinaire inhoud (wat is de techniek/discipline, hoe pas je ze toe), maar dupliceert geen inhoud van Regelingen die erin spelen. | boekhouding · fiscaal/vennootschapsbelasting · audit/COSO · advies/ratio-analyse · jaarrekening-opmaak · aangifte-personenbelasting · consolidatie-techniek · getrouw-beeld-principe |
| **Entiteit** | Een ding met identiteit dat in transacties optreedt, *ongeacht of de wetgever het ontwierp*. Default: **lichtgewicht record** (naam + 1-zin definitie + relaties), tenzij expansie vereist door cross-Kader-impact. | vennootschap · BV · aandeel · obligatie · vordering · vruchtgebruik · vast actief · voorraad · klant · consortium |
| **Gebeurtenis** | Een transactie of event tussen Entiteiten — een handeling op een moment, met deelnemers en gevolgen. | dividend-uitkering · kapitaalverhoging · fusie · faillissement · verkoop-met-meerwaarde · aankoop-aandelen |
| **Regeling** | Een wettelijke regel die *gedrag corrigeert, stuurt, voorkomt of stimuleert*. Normatief van karakter — schrijft voor wat moet, mag of verboden is. Werkt in op een Kader, Entiteit of Gebeurtenis. | DBI-aftrek · quasi-inbreng-regeling · anti-misbruik-bepaling · meerwaardevrijstelling-aandelen · alarmbel-procedure · liquidatiereserve · innovatie-aftrek · huwelijksquotiënt |

**Kern-heuristieken per onderscheid**:

| Onderscheid | Heuristiek |
|---|---|
| **Kader vs alle anderen** | Is het een organisatorische koepel/aanpak/discipline? Geen "wat IS het ding", maar "binnen welk perspectief werk je?" |
| **Entiteit vs Gebeurtenis** | Heeft het identiteit en bestaat het in de tijd ("een aandeel bestaat") → Entiteit. Gebeurt het op een moment, met deelnemers en gevolgen ("een dividend wordt uitgekeerd") → Gebeurtenis. |
| **Entiteit vs Regeling** | Is het *een ding* dat in transacties optreedt (zelfs als wettelijk gecreëerd, zoals een BV of vruchtgebruik) → Entiteit. Is het een *normatieve regel* die gedrag voorschrijft/stuurt → Regeling. |
| **Gebeurtenis vs Regeling** | Is het *iets dat gebeurt* (kapitaalverhoging) → Gebeurtenis. Is het een *regel die op zo'n gebeurtenis inwerkt* (quasi-inbreng-regeling) → Regeling. |

**Belangrijke nuance**: het onderscheid Entiteit vs Regeling gaat *niet* over "wel of niet wettelijk gecreëerd". BV, aandeel en vruchtgebruik zijn alle drie wettelijk gecreëerd, maar zijn *dingen* (Entiteiten), geen *regels*. Een Regeling is altijd normatief; een Entiteit altijd descriptief.

**Naam "Entiteit"**: behouden. Vroeger "fenomeen" overwogen maar te abstract. "Concept" zou kunnen als we de overkoepelende term "concept" laten vallen, maar dat is een grotere herziening die hier nog niet aan de orde is.

---

## 1.5. Hoofd-principe — conceptuele coherentie boven categorie-zuiverheid

**Eén concept-record = één conceptueel coherente eenheid = één studiefiche.**

De 4 super-categorieën uit §1 zijn een denkkader om de *rol* van iets te bepalen ("dit gedraagt zich primair als Entiteit, dat als Regeling"). Ze zijn **geen administratieve hokjes** die elk concept tot één categorie reduceren. Een concept-record mag categorieën mengen zolang het didactisch en conceptueel een geheel vormt.

**Toetsvraag bij elk record**: *"Vormt dit één conceptueel geheel zoals een domein-expert (boekhouder, fiscalist, auditor) het zou clusteren — een eenheid die in vakliteratuur, opleiding en praktijk samen wordt behandeld?"* Zo ja → één concept. Zo nee → splitsen.

Stagiair-leesbaarheid is een **gevolg** van conceptuele coherentie, niet de primaire toets. Wat domein-experts als één samenhangend onderwerp zien (bv. "de componenten van het eigen vermogen", "de keuze van ondernemingsvorm"), studeert een stagiair ook als één geheel.

**Implicaties voor de oudere werkingsregels**:

| Oude regel | Wat blijft | Wat verandert in iter. 5 |
|---|---|---|
| **Regel A** (1+1=1) | Combineer E+G+R-clusters tot één concept als ze samen voorkomen. | Geldt nu *generieker*: ook E-clusters (BV+NV+CommV), R-clusters (verwante aftrekken), of E+Kader-mengingen (vennootschapsvormen + vormkeuze) mogen samen wonen in één concept. |
| **Regel D** (aspect-secties per Kader) | Entiteiten en Gebeurtenissen krijgen perspectief-secties per rol. | Geldt nu voor *alle* concept-records ongeacht primaire categorie. |
| **Regel F** (lichte Entiteiten) | Lichte stubs zijn waardevol als referentie. | Lichte Entiteiten worden **geen eigen records meer**, maar **sub-secties met anchor binnen een bundel-concept** (zie casus §6 ondernemingsvormen). |
| **Regel G** (synthese-records) | Integratie hoort niet in nieuwe records. | Synthese-records verdwijnen als sub-soort. Integratie woont altijd binnen een bestaand bundel-concept. |
| **§4 PO-taken → Kader-techniek** | Lesplan-eenheid komt uit PO-taak. | Een PO-taak-Kader-techniek kan tegelijk *het bundel-concept* zijn dat de bijhorende Entiteiten/Regelingen als secties draagt. |

**Cross-record-relaties via anchor-targets**: andere records linken niet alleen naar een record-ID, maar mogen ook naar een **anchor binnen een bundel-concept** linken — bv. `vennootschapsvormen#bv`. Dat lost het "linken-naar-BV"-probleem op zonder een eigen BV-record te vereisen.

Schema-aanpassing: `relaties[].target` mag een anchor-suffix dragen (`{record}#{anchor-id}`). Eén klein veld-toevoeging.

**Embeddings**: voor RAG-doeleinden mag een bundel-concept *intern gesplitst* worden in chunks per sectie (BV-chunk, NV-chunk, CommV-chunk, afweging-chunk), zodat retrieval-precisie behouden blijft. De *record-eenheid* (= fiche) blijft het bundel-concept als geheel.

---

## 2. Werkingsregels

### Regel A — 1+1=1: combineer als 1-op-1 of coherent

**Kerngranulariteit-regel** (vervangt de eerdere "events by default splitsen"). Eén concept-record kan Entiteit + Gebeurtenis + Regeling combineren *zolang ze 1-op-1 of coherent samen optreden*. Splits zodra divergentie:

| Combinatie | Beslissing |
|---|---|
| 1 E + 1 G + 1 R | **1 concept** (samen behandelen) |
| 1 E + n G + 1 R (symmetrie tussen events) | **1 concept** |
| 1 E + 2 G + 2 R | **3 concepten** (1 E + 2 koppels G+R) |
| 1 E + n G + n R (divergent) | **splitsen** |
| 1 G + 1 R | **1 concept** |
| 1 G + n R (verschillende invalshoeken) | **splitsen** per R |
| n G (uit 1 E) + 1 R (coherente set events onder één regel) | **samen** als coherent verhaal |
| n G (uit n E) + 1 R (regel over verschillende dingen) | **apart** record per G of per E |

Voorbeelden:
- **leasing** = 1 E (instrument) + 1 G (leasing-transactie) + meerdere R's (BEGAAP-, IFRS-, fiscale-kwalificatie) → hoofdrecord leasing (E+G+kern-aspecten) + eventueel apart Regeling-record voor BEGAAP/IFRS-kwalificatie.
- **afschrijving** = 1 E (vast actief, lichtgewicht) + 1 G (jaarlijkse boeking) + 1 R (afschrijvingsregels) → 1 concept "afschrijving" (Kader-techniek-record).
- **statutaire uittreding** = 1 G + 1 R → 1 concept.

### Regel B — Regelingen kunnen op alles inwerken

Een Regeling kan inwerken op:
- een **Kader** (consolidatieperimeter-regels werken op de consolidatie-techniek)
- een **Entiteit** (regels rond aandelenoverdracht-formaliteiten)
- een **Gebeurtenis** (DBI op dividend-uitkering)
- meerdere tegelijk

Het Regeling-record beschrijft het werkingsmechanisme van de Regeling zelf, met `relaties[]` naar wat ze beïnvloedt.

### Regel C — Kader-records: eigen inhoud + lichte verwijzingen naar Regelingen

Een Kader-record bevat **eigen disciplinaire inhoud** (wat is de techniek, hoe pas je ze toe, structuur, methodologie). Bv. `jaarrekening-opmaak` legt uit wat een jaarrekening is, hoe ze is opgebouwd, wat de presentatieregels zijn — dat is de "body".

Het Kader-record bevat **geen volledige uitleg** van de Regelingen die binnen het Kader spelen — daar wijst het naar. Bv. `belastbare-grondslag-VenB` verwijst naar DBI-aftrek-record, herhaalt niet de DBI-inhoud.

> "Binnen deze techniek spelen Regelingen R1, R2, R3 in deze volgorde met deze interactie. Voor uitleg per Regeling: zie het Regeling-record."

Vermijdt content-duplicatie. Render-laag kan via transclusion de inhoud van de Regeling op de Kader-pagina tonen als didactisch nuttig — bron blijft één plek.

**Uitzondering — synthese-Kader-techniek-records** (zie Regel G, zeldzaam): in de uitzonderlijke gevallen waar een eigen synthese-record verantwoord is (alle 4 drempels gehaald), mag de body **didactisch samenvattend** zijn — niet de volledige Regeling-inhoud dupliceren, wel zoveel context dat de samenhang zelfstandig leesbaar is.

### Regel D — Entiteiten en Gebeurtenissen hebben aspect-secties per Kader

Een Entiteit-record voor "aandeel" heeft aspect-secties zoals:
- Boekhoudkundige verwerking (presentatie op balans, waardering)
- Fiscale behandeling — personenbelasting (roerend inkomen, RV)
- Fiscale behandeling — vennootschapsbelasting (deelneming, meerwaarden)
- Audit-implicaties (controle eigendom, waardering)
- Advies-context (kapitaalstructuur, dividendpolitiek)

**Schema-locatie**: aspect-secties leven in `inhoud.accountant_perspectieven[]` (schema 2.1 v1.5), **niet** in `inhoud.kern.definitie`. Definitie blijft generiek; perspectieven dragen het rol-specifieke "hoe doe ik hier mee in mijn vak".

### Regel E — Wat NIET een eigen record is

- **Uitzonderingen, drempels, parameters** binnen een Regeling → sub-velden van die Regeling, geen eigen record.
- **Rechtsbasis** (wet, KB, richtlijn) → bron-anchor in `resources/bronnen/`, geen concept-record.
- **Lemma's en begrippen** (EBITDA, ROCE) → gedefinieerd in het Kader-record waar ze leven (ratio-analyse), niet apart.
- **Document-sjablonen** (aangifte VenB als formulier) → sub-structuur binnen het Kader-record dat de techniek beschrijft.
- **Groepsnamen zonder eigen wettelijke inhoud** ("aftrekken-en-verminderingen-PB", "bijzondere-aanslagen-VenB") → géén Kader-record. Werkt als filter/categorie binnen het ouder-Kader; render-laag toont via "alle Regelingen onder PB met type=aftrek".

### Regel F — Lichte Entiteiten = sub-secties met anchor, geen eigen records (iter. 5 herzien)

Een Entiteit die op zichzelf geen volwaardige studiefiche kan dragen (BV, NV, voorraad, klant) wordt **geen eigen concept-record**. In plaats daarvan landt ze als **sub-sectie met anchor** binnen het natuurlijke bundel-concept:

- BV / NV / CommV / eenmanszaak → secties binnen `ondernemingsvormen`
- klant / leverancier / voorraad → secties binnen een Kader-techniek zoals `aankoop-cyclus` of `verkoop-cyclus`, of binnen een bundel-concept `balansposten-werkkapitaal`
- vordering / schuld → secties binnen `balansposten-werkkapitaal` of binnen relevante Kader-techniek-records

**Wanneer wél een eigen Entiteit-record**: enkel als de Entiteit *zelfstandig didactische diepte* draagt (uitwerking in meerdere rollen × perspectieven, eigen mechanismes die de stagiair op zich moet begrijpen). Voorbeeld-kandidaten: `aandeel` (uitgebreide fiscaal/boekhouding/audit/advies-secties), `leasing` (kwalificatie-keuze + aspecten).

**Toetsvraag**: "kan ik over deze Entiteit een zinvolle studiefiche schrijven die op zichzelf staat?" Zo nee → sub-sectie binnen bundel-concept. Zo ja → eigen record.

Dit drukt het concept-aantal substantieel (ten opzichte van iter. 4) en maakt elke fiche didactisch substantieel.

### Regel G — Integratie-leerstof landt ALTIJD in een bestaand bundel-concept (iter. 5 herzien)

De **interessante leerstof voor het examen** zit zelden in een individuele Regeling of Entiteit, maar in de **samenhang ertussen**: "wanneer welke aftrek toepassen", "welke vennootschapsvorm kies je", "welke kwalificatie geldt voor deze leasing". Verleidelijk om voor elk zo'n integratie-narratief een eigen "synthese-record" te maken — dat lijkt netjes, maar leidt tot **concept-inflatie** (richting 1000 records) en verbergt dat schema 2.1 daar al een structurele plek voor heeft.

**Default-route** (toepassen tenzij de uitzonderingsdrempel hieronder gehaald wordt):

Integratie/afweging/keuze-narratieven **landen in een bestaand record**:
- als **`inhoud.accountant_perspectieven[]`-sectie** in het meest geschikte rol-perspectief (typisch `advies` voor afwegingen, `fiscaal` voor aftrek-volgordes, `boekhouding` voor kwalificatie-keuzes)
- of als **`inhoud.kern`-sectie** binnen een Kader-techniek-record dat uit een PO-taak volgt (Regel §4)
- of als **sectie binnen het ouder-Entiteit-/Kader-record** waar het cluster onder hangt

**Concrete herijking van eerder voorgestelde "synthese-records"**:

| Eerder voorgesteld als eigen record | Hoort eigenlijk in |
|---|---|
| afweging-vennootschapsvormen | `accountant_perspectieven[].advies` op één vennootschapsvorm-record (bv. BV als meest representatief), of binnen Kader-techniek `vennootschap-oprichten` (PO-taak) |
| consolidatie-perimeter-bepalen | `inhoud.kern` van Kader-techniek `consolidatie-techniek` |
| aftrekvolgorde-vennootschapsbelasting | `inhoud.kern` of `accountant_perspectieven[].fiscaal` van Kader-techniek `aangifte-vennootschapsbelasting-opmaken` |
| leasing-kwalificatie-kiezen | `accountant_perspectieven[].boekhouding`+`.fiscaal` op Entiteit-record `leasing` |
| dividend-uitkering-fiscaal-behandelen | `accountant_perspectieven[].fiscaal` op Gebeurtenis-record `dividend-uitkering` |

In alle vijf de gevallen bestaat er al een natuurlijk ouder-record (of het zou er als Kader-techniek uit een PO-taak komen) — daar landt het narratief. Geen extra record.

**Iter. 5**: in iter. 4 stond hier een uitzondering "synthese-Kader-techniek-record verantwoord als 4 drempels gehaald". **Die uitzondering vervalt**. Onder het hoofd-principe (§1.5) hoort integratie altijd binnen een bestaand bundel-concept — desnoods door het bundel-concept iets ruimer te snijden zodat de integratie er natuurlijk in past.

Als er écht geen bundel-concept bestaat waarbinnen de integratie kan landen, is dat een signaal dat het bundel-concept zelf nog **niet bestaat** en aangemaakt moet worden — niet als "synthese-record", maar als gewoon bundel-concept dat de cluster + integratie samen draagt. Voorbeeld: `ondernemingsvormen` is op zich een bundel-concept dat én de vormen beschrijft én de afweging draagt.

**Risico-bewaking**: bij elke "ik zou een record voor X-afwegen of X-vergelijken kunnen maken"-impuls: nee. Het hoort in een ruimer bundel-concept dat de afgewogen dingen al bevat.

### Regel H — Diepte-tabel per categorie (schrijfregel)

Schrijf-richtlijn over hoe diep een record bevolkt moet worden. Tegen-gewicht voor de neiging om elk record "compleet" te willen maken.

| Categorie (primaire rol) | Diepte | Voorbeelden |
|---|---|---|
| **Entiteit-bundel** (meerdere verwante Entiteiten + integratie) | Diep — secties per lid (anchors) + perspectief-secties met afweging | `ondernemingsvormen`, `balansposten-werkkapitaal`, `eigen-vermogen-componenten` |
| **Entiteit-solo** (zelfstandige didactische diepte) | Middelmatig-diep — aspect-secties per relevante rol | `aandeel`, `leasing`, `vruchtgebruik-en-blote-eigendom` |
| **Gebeurtenis** | Middelmatig — wat gebeurt, deelnemers, gevolgen, perspectieven | `kapitaalverhoging`, `dividend-uitkering`, `fusie` |
| **Regeling** | Middelmatig-diep — mechanisme, voorwaarden, uitzonderingen, perspectieven | `dbi-aftrek`, `notionele-interestaftrek`, `liquidatiereserve` |
| **Kader-rol / Kader-domein** | Licht — koepel, navigatie | `boekhouding`, `fiscaal`, `audit` |
| **Kader-techniek** (uit PO-taak) | Diep — methodologie + perspectieven + integratie-secties + verwijzingen naar Regelingen | `consolidatie-techniek`, `aangifte-vennootschapsbelasting-opmaken`, `juridische-vormkeuze-adviseren` |

**Vervallen** (iter. 5): aparte rij voor "lichtgewicht Entiteit-stubs" — die bestaan niet meer als records. Aparte rij voor "Kader-techniek-synthese" — die smelt samen met "Kader-techniek".

**Implicatie**: élk record draagt een substantieel verhaal. Geen schamele stubs. Het zwaartepunt zit op Kader-techniek-records (uit PO-taken) en Entiteit-bundels.

### Regel I — Bundel-criterium: wanneer wél en wanneer NIET bundelen (iter. 5 verfijning)

Niet elk cluster van verwante concepten is een bundel-concept. Bundel pas als één van twee patronen geldt — anders blijven het aparte records.

**Patroon 1 — Keuze-bundel**: de leden worden **naast elkaar gelegd om TUSSEN te kiezen**. De afweging is de leerstof.
- `ondernemingsvormen` (kies BV vs NV vs CommV)
- `consolidatie-methoden` (kies integraal vs vermogensmutatie vs proportioneel)
- `afschrijvings-methoden` (lineair vs degressief)
- `waarderingsmethoden-voorraad` (FIFO vs LIFO vs gewogen gemiddelde)

**Patroon 2 — Samenhang-bundel**: de leden zijn **onlosmakelijk verstrengeld** — je begrijpt ze pas als je ze samen ziet, en in toepassing moet je ze allemaal hanteren.
- `eigen-vermogen` (kapitaal · reserves · overgedragen-resultaat · herwaarderingsmw — mutaties lopen tussen componenten, totaal moet kloppen op de balans)
- `werkkapitaal` (klant-vordering · leverancier-schuld · voorraad · liquide-middelen — samen leveren ze de cash-conversion-cycle)

**Patroon NIET-bundelen — losse mechanismes**: de leden hebben elk een **eigen mechanisme dat los te bestuderen is**, en hun interactie (volgorde, samenloop) is een aparte didactische laag die in een Kader-techniek-record landt.
- `dbi-aftrek` · `notionele-interestaftrek` · `innovatie-aftrek` · `investeringsaftrek` · `overgedragen-verliezen` → **elk eigen Regeling-record**. De aftrekvolgorde + korf-systeem + interactie woont in Kader-techniek `aangifte-vennootschapsbelasting-opmaken`.
- `pensioensparen` · `huwelijksquotiënt` · `decumul` (PB-faciliteiten) → elk eigen Regeling.

**Beslis-toets per cluster**:
1. *"Moet de stagiair tussen de leden KIEZEN?"* → ja → keuze-bundel.
2. *"Zijn de leden onlosmakelijk verstrengeld in toepassing (kun je lid X correct hanteren zonder Y te kennen)?"* → ja → samenhang-bundel.
3. *"Zo nee op 1+2"* → losse records + integratie in ouder-Kader-techniek.

**Naamgeving-conventie** (consistentie-eis voor alle bundel-concepten):
- **Voorkeur**: bundel-naam = de naam van het conceptuele geheel zelf, zonder generieke suffix.
  - `eigen-vermogen` ✅ (niet `eigen-vermogen-componenten`)
  - `werkkapitaal` ✅ (niet `balansposten-werkkapitaal`)
  - `ondernemingsvormen` ✅
  - `consolidatie-methoden` ✅ (plural-suffix `-methoden` deel van de natuurlijke naam, geen generieke meta-label)
- **Toegelaten alternatief** (consistent als prefix): `balanspost-eigen-vermogen` · `balanspost-werkkapitaal`, of `aftrek-dbi` · `aftrek-nia` (mits alle leden van dezelfde categorie hetzelfde prefix dragen).
- **NIET**: suffix als categorie-marker (`eigen-vermogen-componenten`, `balansposten-werkkapitaal`) — leest dubbel en herhaalt info die uit de record-typering al volgt.
- Anchors dragen de specifieke naam: `eigen-vermogen#kapitaal`, `werkkapitaal#klant-vordering`, `ondernemingsvormen#bv`.

Reden: bundel-naam = wat een domein-expert intuïtief zegt ("we behandelen het eigen vermogen", "we kijken naar het werkkapitaal"), niet wat het *systeem-type* van het record is.

---

## 3. Bronnen-laag — buiten de typologie

Wetten, KB's, EU-richtlijnen, IBR-normen, COSO-framework als document, IFRS-standaarden als document → **leven in `resources/bronnen/`**, niet als concept-records.

Cross-referencing: een Regeling-record verwijst naar zijn rechtsbasis via `grondslag.bronnen[]` (al ondersteund in schema 2.1 v1.5). De wettekst zelf wordt niet gedupliceerd in het Regeling-record.

**Bestaande bronnen-mappen blijven onaangeraakt**. De typologie raakt enkel records in `data/concepten/records/` die feitelijk bron-inhoud bevatten (zoals `moeder-dochterrichtlijn.json`). De distillatie van zo'n hybride record naar (a) bron-aanvulling in `resources/bronnen/` + (b) Regeling-record-aanvulling gebeurt per geval, niet als bulk-operatie.

---

## 4. Kader-boomstructuur — flexibel diep

Kaders zijn niet plat, maar de diepte is **niet vast**. Sommige Kaders bestaan enkel op niveau 1 (een rol zonder veel sub-structuur). Andere reiken tot niveau 4. Diepte is descriptief, niet voorschrijvend.

```
Niveau 1: Rol (5 stuks — de professionele perspectieven)
  • boekhouding
  • fiscaal
  • audit (externe controle)
  • advies (bedrijfsvoering, strategie, jaarrekening-analyse)
  • begeleiding (oprichting, ontbinding, formaliteiten)

Niveau 2: Sub-domein (binnen een rol)
  • boekhouding → BEGAAP · IFRS · jaarrekening-opmaak · consolidatie
  • fiscaal     → personenbelasting · vennootschapsbelasting · BTW · registratie · successie · douane
  • audit       → COSO · ISA · interne-controle-cycli
  • advies      → ratio-analyse · cashflow-analyse · waarderingstechnieken · successieplanning
  • begeleiding → vennootschapsoprichting · insolventie-procedures · vereffening

Niveau 3 (en dieper): Techniek (concrete aanpak binnen een sub-domein)
  • ratio-analyse → liquiditeit-ratios · solvabiliteit-ratios · rentabiliteit-ratios
  • COSO         → controle-omgeving · risico-inschatting · controle-activiteiten · informatie · monitoring
  • jaarrekening-opmaak → balans-opmaak · resultatenrekening-opmaak · toelichting-opmaak · waarderingsregels
```

Elk niveau kan een eigen Kader-record zijn, met `relaties[]` naar het ouder-Kader (`onderdeel-van`).

**Beslisregel voor niveau-record**: een Kader op niveau N krijgt een eigen record als het minstens 3-4 Regelingen of cross-Kader-aspecten heeft en didactisch een eigen verhaal kan dragen. Anders blijft het sectie binnen het ouder-Kader.

### Programmaonderdeel-taken → Kader-techniek

Observatie: bijna alle **taken** uit de examenprogramma-onderdelen (PO's) zijn van de vorm "kan X doen" — een aangifte opmaken, een audit uitvoeren, een advies geven, een vereffening begeleiden. Die taken vertalen quasi 1-op-1 naar **Kader-techniek-records** binnen de relevante rol. Ook voor de rol "advies" (waarvan we er veel hebben: ratio-analyse, cashflow-prognose, waarderingsoefening, herstructurerings-advies, …).

Implicatie: het aantal Kader-techniek-records is **vermoedelijk groter dan eerder geschat**. De "techniek"-laag van de boom wordt rijk bevolkt door PO-taken, en die records dragen het zwaartepunt van de studeer-stof (samen met Regelingen). Entiteiten en Gebeurtenissen zijn referentie-laag.

Concrete invulling per record: de taak-vereisten uit het PO landen in `inhoud.accountant_perspectieven[]` van het techniek-record — daar staat per rol × perspectief wat de stagiair moet kunnen. De Kader-techniek-record vormt zo de **lesplan-eenheid**.

---

## 5. Migratie van bestaande 10 `concept_type`-waarden

De 10 waarden worden **vervangen** door de 4 super-categorieën. Migratie-mapping:

| Huidig `concept_type` | Wordt | Toelichting |
|---|---|---|
| `kader` | **Kader** | rechtstreeks |
| `principe` | **Kader** | beginselen/principes (getrouw beeld, voorzichtigheid) zijn vormgevend voor de discipline, geen normatieve regels |
| `methode` | **Kader** | techniek-niveau (consolidatiemethoden, kostprijsmethoden) |
| `procedure` | **Kader** of **Gebeurtenis** | als sequentieel proces binnen 1 rol → Kader-sub-techniek. Als event-georiënteerd (faillissement) → Gebeurtenis. |
| `ratio` | **Kader** | sub van ratio-analyse-techniek; individuele ratio-families als sub-record als ze didactisch eigen verhaal dragen |
| `balanspost` | **Entiteit** of **Kader** | echte (vordering, vast actief) → Entiteit (lichtgewicht). Pure boekhoudconstructies (overlopende rek., herwaarderingsmw) → Kader-sub binnen balans-opmaak. |
| `instrument` | **Entiteit** | aandeel, obligatie, lening, leasing |
| `actor` | **Entiteit** | commissaris, FOD Financiën, kamer voor ondernemingen in moeilijkheden |
| `verrichting` | **Gebeurtenis** | rechtstreeks |
| `regime` | **Regeling** | rechtstreeks |

Procedure en balanspost zijn ambigu en vereisen handmatig oordeel per record. Geschatte verdeling na migratie van 396 records: ~80 Kader, ~120 Entiteit (waarvan veel lichtgewicht), ~50 Gebeurtenis, ~70 Regeling — restant van ~70 verschuift door consolidaties (zie §7).

---

## 6. Casus uitgewerkt — het DBI/moeder-dochter-cluster

### Huidige situatie (inconsistent)

```
data/concepten/records/
├── moeder-dochterrichtlijn.json          (21KB, top-level — bevat bron-inhoud)
├── deelneming-financieel-vast-actief.json (top-level)
├── kwalificatie-controle-deelneming.json  (top-level)
├── controle-test-deelneming.json          (top-level)
├── meerwaarde-aandelen-venb.json          (top-level)
└── belastbare-grondslag-vennootschapsbelasting.json
       └── elementen[] bevat id "dbi-aftrek" als SUB-element
```

Datastate-bevestiging: in de candidates-DB staat `dbi-aftrek` als "gerealiseerd op 21 mei", maar het bestaat fysiek als sub-element binnen `belastbare-grondslag-vennootschapsbelasting`. Geen bug — bewuste granulariteit-keuze die we nu heroverwegen.

### Voorgestelde situatie

```
data/concepten/records/
├── dbi-aftrek.json                          ← NIEUW top-level Regeling
│   ├── (inhoud.kern: wat IS DBI, mechanisme, voorwaarden)
│   ├── (inhoud.accountant_perspectieven[]: 
│   │       boekhoudkundige verwerking,
│   │       VenB-aangifte (vak + aftrekvolgorde),
│   │       audit (verificatie bij dochter),
│   │       advies (holdingstructuur))
│   ├── relaties[]:
│   │   ├── werkt-op → Gebeurtenis "dividend-uitkering"
│   │   ├── voorwaarde → Entiteit "deelneming"
│   │   └── rechtsbasis → bron "moeder-dochterrichtlijn-EU" + WIB92 art. 202-205
│
├── dividend-uitkering.json                  ← Gebeurtenis (bestaat al als 'uitkering-aan-aandeelhouders'?)
├── deelneming.json                          ← Entiteit (consolidatie van 3 huidige deelneming-records)
├── meerwaardevrijstelling-aandelen.json     ← Regeling (rename van meerwaarde-aandelen-venb)
└── belastbare-grondslag-vennootschapsbelasting.json   ← Kader-techniek
    ├── (inhoud.kern: wat is "belastbare grondslag VenB", structuur, aftrekvolgorde)
    ├── verwijst naar dbi-aftrek (geen inhoudherhaling)
    └── verwijst naar andere aftrekken in volgorde

resources/bronnen/wetteksten/eu/
└── moeder-dochterrichtlijn.md               ← NIEUW (richtlijn-tekst als bron)
```

**Effect op andere records**: de 3 deelneming-detail-records (FVA, kwalificatie, controle-test) zijn allemaal aspecten van **één concept "deelneming"**. Voorstel: consolideren tot één Entiteit-record met sub-secties per aspect. Reductie: 3 → 1.

### Tweede casus — groep / consortium / consolidatiekring (Regel G default-route)

Drie verwante Entiteiten staan vandaag los: `groep`, `consortium`, `consolidatiekring`. De examen-relevante integratie ("wanneer kies je welke perimeter") moet ergens landen — maar volgens Regel G **niet** als nieuw synthese-record, want er bestaat een natuurlijk ouder-Kader-techniek (`consolidatie-techniek`, uit PO-taak) waar dat in past.

**Test op Regel G (4 drempels)**:
1. Clustergrootte: 3 entiteiten → ✅
2. PO-vereiste: "kan consolidatieperimeter bepalen" → ✅
3. Overstijgende inhoud: beslisboom controle/gemeenschappelijke-leiding/significante-invloed → ✅
4. **Geen natuurlijk ouder-record**: ❌ — er bestaat (of komt er via PO-taak) een Kader-techniek `consolidatie-techniek` waar dit in landt.

**Conclusie**: drempel 4 NIET gehaald → geen apart synthese-record. Default-route geldt.

**Voorgestelde structuur**:

```
data/concepten/records/
├── groep.json                          ← Entiteit (lichtgewicht: WVV-definitie + relaties)
├── consortium.json                     ← Entiteit (lichtgewicht: WVV-definitie + relaties)
├── consolidatiekring.json              ← Entiteit (lichtgewicht: definitie + relaties)
│
└── consolidatie-techniek.json          ← Kader-techniek (uit PO-taak — bestaat of komt er)
    ├── inhoud.kern:
    │   ├── wat is consolidatie + waarom
    │   └── PERIMETER-BEPALING (beslisboom, vergelijkingstabel WVV-criteria,
    │       perimeter-inclusie-logica voor groep/consortium/consolidatiekring)
    ├── inhoud.accountant_perspectieven[]:
    │       boekhouding (consolidatie-plicht),
    │       audit (wie tekent welke jaarrekening),
    │       fiscaal (fiscale eenheid is iets ANDERS),
    │       advies (groepsstructurering)
    └── relaties[]:
        ├── omvat → Entiteit "groep"
        ├── omvat → Entiteit "consortium"
        ├── omvat → Entiteit "consolidatiekring"
        └── grondslag → bron WVV art. 1:14-1:20
```

**Effect**: 3 Entiteiten blijven lichte referentie-records (Regel F), 1 bestaande Kader-techniek krijgt de integratie als kern-sectie. **Geen** nieuw record. Totaal: 3 + 1 (al bestaand) = 4 records voor het hele cluster.

### Derde casus — ondernemingsvormen als bundel-concept (iter. 5 — kantelend voorbeeld)

In iter. 4 stond hier "afweging-vennootschapsvormen landt als perspectief-sectie op `juridische-vormkeuze-adviseren`, met 3 aparte BV/NV/CommV-Entiteit-records". Iter. 5-feedback kantelt dat: **conceptueel horen vennootschapsvormen + afweging bij elkaar**. Voorgesteld bundel-concept:

```
data/concepten/records/
└── ondernemingsvormen.json                  ← ÉÉN bundel-concept (Entiteit-bundel)
    ├── inhoud.kern:
    │   ├── wat is een ondernemingsvorm + waarom kies je een vorm
    │   └── secties met anchors:
    │       ├── #eenmanszaak (definitie, aansprakelijkheid, fiscaal-PB)
    │       ├── #bv (definitie, kapitaal, governance, aansprakelijkheid)
    │       ├── #nv (definitie, kapitaal, aandeelhouders, governance)
    │       ├── #commv (definitie, gecommanditeerden, gewone vennoten)
    │       └── (eventueel #cv, #vof, etc. waar relevant)
    ├── inhoud.accountant_perspectieven[]:
    │       boekhouding (wat verandert per vorm bij verwerking),
    │       fiscaal (PB vs VenB, vormkeuze-impact),
    │       audit (commissaris-plicht per vorm),
    │       advies (AFWEGING: beslismatrix per criterium —
    │                aansprakelijkheid, kapitaal, fiscaal, governance,
    │                opvolging — voor concrete cliënt-situatie),
    │       begeleiding (oprichtings-procedure verschillen)
    └── relaties[]:
        ├── grondslag → bron WVV boek 5-7
        └── (geen aparte BV/NV/CommV-records meer — alles intern)
```

**Effect**: van 3 lichte Entiteit-records + mogelijk 1 Kader-techniek (afweging) → **1 bundel-concept**. Reductie: 4 → 1.

**Andere records linken naar ondernemingsvormen**:
- `kapitaalverhoging` → `relaties[].target = "ondernemingsvormen#bv"` (BV-specifieke kapitaal-regels)
- `alarmbel` → `relaties[].target = "ondernemingsvormen#bv"` en `"...#nv"`
- `statutaire-uittreding` → `relaties[].target = "ondernemingsvormen#bv"`

De `#anchor`-suffix lost de fijnmazige link-behoefte op zonder aparte BV/NV-records te vereisen.

**Generaliseerbaar patroon — bundel-concepten** (na Regel I-filter):

| Bundel-concept | Patroon (I) | Bevat als secties (anchors) | Integratie in perspectief |
|---|---|---|---|
| `ondernemingsvormen` | Keuze | eenmanszaak · BV · NV · CommV (· CV · VOF) | advies: vormkeuze-matrix |
| `consolidatie-methoden` | Keuze | integraal · vermogensmutatie · proportioneel | boekhouding: methode-keuze per deelnemingstype (beslisboom) — verwijst naar Regelingen `groottecriterium`, `controle-test-deelneming` als triggers |
| `afschrijvings-methoden` | Keuze | lineair · degressief · andere | boekhouding/fiscaal: methode-keuze per actief |
| `eigen-vermogen` | Samenhang | maatschappelijk-kapitaal · reserves · overgedragen-resultaat · herwaarderingsmw | boekhouding: mutaties + presentatie |
| `werkkapitaal` | Samenhang | klant-vordering · leverancier-schuld · voorraad · liquide-middelen | boekhouding/advies: cash-conversion-cycle |

**NIET als bundel** (na Regel I-toets):

| Cluster | Waarom niet | Hoe wel? |
|---|---|---|
| Aftrekken VenB (DBI/NIA/innovatie/investering/verliezen) | Patroon "losse mechanismes" — elk eigen Regeling-mechanisme, los bestudeerbaar | Aparte Regeling-records + integratie (volgorde, korf, samenloop) in Kader-techniek `aangifte-vennootschapsbelasting-opmaken` |
| PB-faciliteiten (pensioensparen, huwelijksquotiënt, decumul) | Idem | Aparte Regelingen + integratie in `aangifte-personenbelasting-opmaken` |
| Anti-misbruik-bepalingen | Elk eigen mechanisme + eigen toepassingsgebied | Aparte Regelingen + eventueel `anti-misbruik-perspectief` als Kader-techniek-sectie |

Bundel-concepten zijn de concrete vorm van het hoofd-principe (§1.5): **één conceptueel coherente eenheid = één studiefiche**. Maar niet elk cluster van verwante dingen is een bundel — Regel I onderscheidt.

---

## 7. Reductie-schatting met deze typologie

Toegepast op de eerder geïdentificeerde 15 cluster-kandidaten + de nieuwe principes:

| Type-werking | Geschatte reductie |
|---|---|
| Bronnen-inhoud weghalen uit records (moeder-dochterrichtlijn, andere richtlijnen) | −10 à −15 |
| Detail-records consolideren tot Entiteit met aspecten (deelneming-cluster, ratio-families, COSO-componenten) | −30 à −40 |
| Sub-elementen van Regelingen bevrijden als top-level Regeling | +5 à +10 (toevoeging) |
| Verstopte Kader-records expliciet maken (PB-aangifte-techniek, BTW-aangifte-techniek) | +5 à +10 (toevoeging) |
| Procedures consolideren onder Kaders | −10 à −15 |
| **Nieuw**: 1+1=1 toepassen op E+G+R-clusters (afschrijving, leasing-kern, statutaire-uittreding-stijl) | −20 à −30 |
| **Nieuw**: lichtgewicht Entiteiten (voorraad, klant, leverancier, generieke balansposten) — niet gerekend als reductie, maar als drempelverlaging om er meer te hebben zonder studeerlast | (geen aantal-effect, wel kwaliteit) |
| **Nieuw (Regel G)**: synthese-Kader-techniek-records (alleen waar alle 4 drempels gehaald) | **+0 à +5** (zeldzaam) |
| **Tegenkracht (Regel G default-route)**: integratie-narratieven die anders eigen record waren geworden, landen nu IN een Kader-techniek- of Entiteit-record als perspectief/kern-sectie | (geen aantal-effect, beheerst inflatie) |

**Netto-effect iter. 5**: 396 → **~150-200 records** (reductie 50-60%). Forsere reductie dan iter. 4 (~270) omdat:
- Lichte Entiteiten verdwijnen als eigen records (~80 records gaan op in bundel-concepten of Kader-techniek-secties)
- Synthese-records verdwijnen volledig (~20 worden secties)
- Bundel-concepten zoals `ondernemingsvormen`, `balansposten-werkkapitaal`, `eigen-vermogen-componenten` consolideren elk 3-6 Entiteiten + integratie tot 1 record

**Verdeling per categorie (schatting iter. 5 — indicatief)**:

| Categorie | Aantal | Aandeel studeerlast |
|---|---|---|
| Entiteit-bundel (meerdere leden + integratie) | ~15-20 | hoog |
| Entiteit-solo (zelfstandige diepte) | ~15-20 | middel-hoog |
| Gebeurtenis | ~30 | middel |
| Regeling | ~60-70 | hoog (atomair) |
| Kader-rol + Kader-domein | ~15 | laag (navigatie) |
| Kader-techniek (uit PO-taken, draagt vaak integratie-secties of bundelt Regelingen) | ~30-40 | **zeer hoog** |
| **Totaal** | **~165-195** | |

**Kwalitatief effect**: élke fiche staat op zich. Geen schamele 1-zin-stubs. Een stagiair leest het totale corpus als ~165-195 substantiële fiches, niet als 396 versnipperde records waarvan de helft naar elkaar wijst zonder eigen inhoud.

**Risico-bewaking concept-inflatie**: bij elke "ik zou een record kunnen maken voor X" eerst toetsvraag uit §1.5: *"kan ik over X een zinvolle studiefiche schrijven die op zichzelf staat?"* Zo nee → sub-sectie in bundel-concept. Zo ja → eigen record. Plus: bij twijfel of het bundel-concept al bestaat, eerst de bestaande tree raadplegen (zie §10 nieuwe pilot-aanpak).

---

## 8. Open spanningen (jouw beslissing)

### 8.1 PB en VenB — Kader of Regeling-cluster? → **akkoord: Kader**

PB en VenB zijn Kaders (sub-domein binnen K-fiscaal). Het feit dat ze wettelijk geregeld zijn, maakt ze geen Regeling. Specifieke regels binnen PB/VenB (huwelijksquotiënt, decumul, DBI, NIA) zijn Regelingen.

### 8.2 Deliverables (jaarrekening, aangiftes) → **akkoord: geen apart sub-type, gewoon Kader-techniek**

Render-laag kan deliverables visueel onderscheiden (eigen icoon/pagina). Content-model hoeft het niet apart te kennen.

### 8.3 Groepen-van-Regelingen als sub-Kader of niet? → **akkoord: niet als sub-Kader**

"Aftrekken-en-verminderingen-PB", "Bijzondere-aanslagen-VenB" zijn **geen Kader-records** — het zijn filters/categorieën die op het ouder-Kader-PB (of -VenB) of via een attribuut op Regelingen werken. Render-laag toont ze als gegroepeerde lijsten.

De individuele Regelingen (huwelijksquotiënt, pensioensparen, decumul) zijn elk eigen Regeling-record.

### 8.4 Kader-niveau-3 — wanneer eigen record? → **TBD**

Voorstel blijft: eigen record op niveau 3 als didactisch een eigen "wat-hoort-bij-elkaar-en-hoe-werkt-het"-verhaal te vertellen is. Anders sub-sectie. Jij gemarkeerd als TBD — laten we per geval beslissen tijdens pilot-doorlichting.

### 8.5 Entiteit-naam — **beslist: Entiteit**

Vroeger "fenomeen" overwogen maar te abstract. Behoud "Entiteit" als werknaam. Een eventuele toekomstige herziening waarbij we de overkoepelende term "concept" laten vallen zou "Concept" kunnen vrijspelen als alternatief — maar dat is een aparte beslissing.

---

## 9. Wat dit niet oplost

- **Grenzen blijven grijs in ~10-15% van de gevallen.** Voorbeelden:
  - **Hybride events**: `oprichting-vennootschap` is tegelijk Gebeurtenis (kapitaal → entiteit ontstaat) én onlosmakelijk verbonden met wettelijke procedure. Voorstel: Gebeurtenis met expliciete Regeling-lagen via `relaties[]` of bij 1+1=1 één concept.
  - **Leasing**: hoofdrecord (E+G+kern-R) volstaat voor cohesie, maar 4 kwalificatie-perspectieven (BEGAAP/IFRS/fiscaal/BTW) vragen mogelijk aparte Regeling-records.
- **Sub-element vs eigen-record** blijft schaalkwestie. Criteria (cross-Kader-impact, 1+1=1-matrix, didactische cohesie) verkleinen de grijze zone maar elimineren ze niet.
- **Renaming van bestaande records** is een aparte operatie (disk + RAG + relaties). records-API ondersteunt het atomair, maar in batch over 50+ records vraagt zorgvuldige planning.
- **Reductie ≠ halvering naar 200**. Realistisch eindbereik 280-320. Sterkere reductie zou didactische cohesie aantasten.

---

## 10. Voorgestelde volgende stappen (iter. 5 — top-down tree-afleiding)

Iter. 4 stelde voor: per huidig record classificeren onder 4 categorieën (bottom-up). Gebruikersfeedback iter. 5: *"we moeten dus onze huidige candidates in een (zo klein mogelijke) tree zetten die 'logisch' is, of onze huidige candidates loslaten en een nieuwe set afleiden van wat we nu weten."*

**Voorgestelde aanpak — top-down tree-afleiding, niet bottom-up reclassificatie**:

1. **Jouw reactie op iter. 5**. Akkoord met:
   - hoofd-principe §1.5 (1 concept = 1 conceptueel coherente eenheid = 1 studiefiche)?
   - bundel-concept-aanpak (Regel F+G herzien, ondernemingsvormen-casus)?
   - schema-aanpassing `relaties[].target` met `#anchor`-suffix?
   - top-down tree-afleiding als pilot-aanpak (in plaats van bottom-up reclassificatie)?

2. **ADR-030 schrijven** ("Granulariteit-typologie voor concept-records") — formaliseert:
   - hoofd-principe + 4 super-categorieën als oriëntatie
   - 8 werkingsregels (A-H, met F en G in iter. 5-vorm)
   - bundel-concept-patroon + `#anchor`-relaties

3. **Pilot-tree afleiden voor één domein** (voorstel: K-fiscaal/VenB):
   - Top-down: vanuit PO-taken + ITAA-programma de **logische tree** schetsen (welke bundel-concepten + Kader-technieken + Regelingen).
   - Pas daarna: huidige 396 candidates *afkruisen* tegen de tree — wat blijft als eigen record, wat smelt in een bundel, wat verdwijnt als sub-sectie.
   - Verwacht resultaat voor pilot: van ~80 huidige VenB-gerelateerde records → ~25-35 records.

4. **Validatie per cluster met jou** (tree + mapping → reductie-voorstel).

5. **Implementatie via records-API** (atomair disk + RAG + content). Schema-aanpassing `#anchor`-suffix eerst (kleine PR).

**Niet doen** in deze sparring-ronde: feitelijke records hernoemen, verplaatsen, mergen of schema wijzigen. Eerst pilot-tree afleiden + valideren.

**Alternatief overwogen, afgewezen**: huidige candidates loslaten en volledige tree top-down opnieuw bouwen. Te risicovol voor één keer — pilot per domein laat valideren dat de aanpak werkt voordat we het over alle 11 PO's uitrollen.

---

## Bijlage A — Open vragen en jouw antwoorden

| # | Vraag | Antwoord |
|---|---|---|
| 1 | Verfijnde Entiteit-vs-Regeling heuristiek ("ding-met-identiteit" vs "normatieve regel", ongeacht wettelijke oorsprong) overtuigend? | ✅ akkoord |
| 2 | PB/VenB als Kader (niet Regeling) | ✅ akkoord — specifieke aftrekken/verminderingen wél Regelingen |
| 3 | Geen apart sub-type voor deliverables | ✅ akkoord |
| 4 | Kader-niveau-3 alleen bij didactische cohesie-vraag | ⏳ TBD — per geval beslissen |
| 5 | Reductie-realisme 280-320 ipv 200 | ✅ akkoord met nuance — entiteiten zijn meer informatief dan studeer-stof; gewicht voor de studie ligt bij Kaders + Regelingen, niet bij stub-Entiteiten |
| 6 | Bronnen-migratie uit concept-records | ✅ akkoord — maar bestaande bronnen-mappen niet aanraken, alleen records met misplaatste bron-inhoud verplaatsen/distilleren |
| 7 | Naam "Entiteit" goed of zoeken we alternatief? | ✅ behoud "Entiteit" — "fenomeen" was te abstract |
| 8 (nieuw) | Competenties als aparte laag of geïntegreerd? | ✅ geïntegreerd in `inhoud.accountant_perspectieven[]` sinds schema 2.1 v1.5 — geen aparte laag |
| 9 (nieuw) | PO-taken als basis voor Kader-techniek-records? | ✅ akkoord — taken vertalen quasi 1-op-1 naar Kader-techniek (zie §4) |
| 10 (iter. 3, herzien iter. 4) | Synthese-Kader-techniek-records als aparte sub-soort? | ⚠️ **gekanteld in iter. 4** — geen aparte sub-soort, maar zeldzame uitzondering. Default-route: integratie landt als perspectief/kern-sectie in een bestaand record. Reden: feedback "schrik voor 1000 concepten" + besef dat schema 2.1 `accountant_perspectieven[]` exact die plek levert. |
| 11 (iter. 3) | "Begrijpt samenhang" telt als PO-vereiste (Regel G vw. 2)? | ✅ akkoord — receptief samenhang-begrip kwalificeert; verandert niet aan iter. 4 omdat het in beide routes (sectie of zeldzaam record) de PO-relevantie aantoont. |
| 12 (iter. 3) | Diepte-tabel per categorie als schrijfregel (Regel H)? | ✅ akkoord — beheerst de neiging om elk record "compleet" te willen maken; tabel in iter. 4 aangepast (Kader-techniek draagt nu ook integratie-secties). |
| 13 (iter. 4, herzien iter. 5) | Vierde drempel "geen natuurlijk ouder-record" voor synthese-records? | ⚠️ **vervallen in iter. 5** — synthese-records bestaan niet meer als sub-soort. Integratie woont altijd in een bestaand bundel-concept. |
| 14 (iter. 5, NIEUW) | Hoofd-principe "1 concept = 1 conceptueel coherente eenheid = 1 studiefiche"? | ⏳ jouw bevestiging gevraagd in §10 stap 1 |
| 15 (iter. 5, NIEUW) | Bundel-concept-aanpak (ondernemingsvormen-casus) als generiek patroon? | ⏳ jouw bevestiging gevraagd in §10 stap 1 |
| 16 (iter. 5, NIEUW) | Schema-aanpassing `relaties[].target` met `#anchor`-suffix? | ⏳ kleine PR, te bevestigen in §10 stap 1 |
| 17 (iter. 5, NIEUW) | Top-down tree-afleiding als pilot-aanpak (i.p.v. bottom-up reclassificatie)? | ⏳ pilot-domein voorgesteld: K-fiscaal/VenB |
| 18 (iter. 5, verfijning) | Toetsvraag §1.5 verbreed: niet alleen stagiair-leesbaarheid maar **domein-expert-clustering** als primaire toets? | ✅ verwerkt — stagiair-leesbaarheid is gevolg, niet primair criterium |
| 19 (iter. 5, verfijning) | Regel I — bundel-criterium met drie patronen (Keuze · Samenhang · NIET losse mechanismes)? | ✅ verwerkt — aftrekken VenB verschuiven van bundel naar losse Regelingen + integratie in Kader-techniek |
| 20 (iter. 5, verfijning) | Naamgeving-conventie bundel-concepten: intrinsieke naam zonder generieke suffix? | ✅ akkoord — voorkeur intrinsiek, prefix-stijl (`balanspost-X`, `aftrek-X`) toegelaten als consistent toegepast, suffix-marker NIET |
| 21 (iter. 5, verfijning) | `consolidatie-methoden` als keuze-bundel correct? | ✅ akkoord — je kunt de methoden oplijsten + beslisboom in `advies/boekhouding`-perspectief; trigger-criteria leven in aparte Regelingen (bv. `groottecriterium`, `controle-test-deelneming`) |
| 22 (pilot-input) | Waar leven PO-taken canoniek? | ✅ `data/programma/programma.json` (taken, doelstellingen, kenniselementen) + `data/programma/anchors.json` (uitbreiding). **Let op**: anchors.json bevat `anchors[].vector` — eerst filteren naar werkbare kopie alvorens te lezen. |

---

## Bijlage B — Stress-test op 24 records

Iteratie 1 (15 willekeurige records, automatisch gekozen):

| # | Record | Classificatie | Twijfel |
|---|---|---|---|
| 1 | `aansprakelijkheid-oprichters-bestuurders` | **Regeling** — wettelijk sanctie-mechanisme | scherp |
| 2 | `alarmbel` | **Regeling** — wettelijk dwingmiddel op vennootschap | scherp |
| 3 | `boekhoudbeginselen` | **Kader** — vormgevend voor de discipline (correctie iteratie 1: niet "grijs") | scherp |
| 4 | `cash-conversion-cycle` | **Kader** — techniek binnen financiële analyse | scherp |
| 5 | `dubbele-boekhouding` | **Kader** — fundamentele boekhoudtechniek | scherp |
| 6 | `uitkering-aan-aandeelhouders` | **Gebeurtenis** — transactie entiteit↔entiteit | scherp |
| 7 | `kapitaalverhoging` | **Gebeurtenis** — verrichting aandeelhouder↔vennootschap | scherp |
| 8 | `materialiteit-audit` | **Kader** — audit-discipline-techniek | scherp |
| 9 | `notionele-interestaftrek` | **Regeling** — corrigerend fiscaal instrument | scherp |
| 10 | `oprichting-vennootschap` | **Gebeurtenis** met procedurele Regeling (1+1=1 → 1 concept) | scherp (na regel A) |
| 11 | `quasi-inbreng` | **Regeling** — controle op verkapte inbrengen | scherp |
| 12 | `risicoanalyse-audit` | **Kader** — techniek binnen auditdiscipline | scherp |
| 13 | `verkoopcyclus-ic` | **Kader** — IC/COSO-techniek | scherp |
| 14 | `vruchtgebruik-en-blote-eigendom` | **Entiteit** — juridisch construct met identiteit | scherp (na heuristiek-verfijning) |
| 15 | `bv-rechtsvorm` | **Entiteit** — vennootschapstype | scherp (na heuristiek-verfijning) |

Iteratie 2 (9 cases door gebruiker gekozen):

| # | Concept | Classificatie | Argument |
|---|---|---|---|
| 16 | `getrouw-beeld-principe` | **Kader** (principe binnen boekhouding/audit) | denkwijze die discipline vormt, geen normatieve regel |
| 17 | `consolidatiekring` | **Entiteit** met Regeling-aspect (1+1=1 → 1 concept) | herzien op gebruikersfeedback: een consolidatiekring IS een ding (de set vennootschappen die samen rapporteren, met identiteit per moeder × boekjaar) — vergelijkbaar met "groep" of "consortium". De inclusie/exclusie-criteria zijn een aspect-sectie binnen het Entiteit-record, niet zelf het hoofd-concept |
| 18 | `consortium` | **Entiteit** (met Regeling-aspect, 1+1=1 → 1 concept) | groep onder gemeenschappelijke leiding; WVV-definitie als aspect-sectie |
| 19 | `waarderingsregels` | **Kader** (techniek binnen jaarrekening-opmaak) | discipline van *kiezen hoe je waardeert*; specifieke methodes als Regelingen of sub-secties |
| 20 | `afschrijving` | **Kader-techniek** met E+G+R samen (1+1+1=1) | vast actief (E, lichtgewicht) + jaarlijkse boeking (G) + afschrijvingsregels (R) → 1 concept |
| 21 | `leasing` | **Entiteit** (E+G+kern-R samen) + apart Regeling-record voor BEGAAP/IFRS-kwalificatie | meerdere R's met divergent karakter → splitsen waar zinvol |
| 22 | `vereffening` | **Gebeurtenis** met procedure-R samen (1+1=1) | fiscale R's (liquidatiereserve) blijven aparte records |
| 23 | `statutaire-uittreding` | **1 concept** (G+R, 1+1=1) | BV-specifieke uittreding + WVV-regel zijn coherent samen |
| 24 | `huwelijksquotiënt` | **Regeling** binnen K-fiscaal/PB | wettelijke faciliteit die inkomsten herverdeelt; normatief |

**Totaalbalans**: 22/24 scherp (92%) na heuristiek-verfijning en 1+1=1-regel. 2 cases waar pragmatische keuze gemaakt moet worden (leasing-splitsing, oprichting-vennootschap als 1 of meer concepten).

**Conclusie**: typologie houdt. Hybride cases zijn beheersbaar via Regel A (1+1=1) en relaties[].

---

## Bijlage C — 1+1=1-matrix met voorbeelden uit het bestand

| Patroon | Voorbeeld | Resultaat |
|---|---|---|
| 1 E + 1 G + 1 R | afschrijving (vast actief + boeking + regels) | 1 record |
| 1 E + 1 G + 1 R | statutaire uittreding (BV + uittreding + WVV-regel) | 1 record |
| 1 E + n G + 1 R | (zoek-case) | 1 record als symmetrisch |
| 1 G + 1 R | oprichting-vennootschap (event + procedure-regels) | 1 record |
| 1 G + n R | dividend-uitkering (event + DBI + RV + vermomde-dividenden + liquidatie-reserve) | aparte R-records, G als hub |
| 1 E + n R | aandeel (entiteit + emissie-regels + overdrachts-regels + meerwaarden-regels) | aparte R-records, E als hub |
| n E + 1 R | anti-misbruik-bepaling (werkt op vennootschap+oprichter+transactie) | 1 R-record, aparte E-records |

De **hub-rol** van het ouder-concept (E of G) is cruciaal: het overkoepelende record blijft bestaan en linkt naar de aparte R-records, maar dupliceert hun inhoud niet. Render-laag kan via `relaties[]` een geïntegreerde view tonen.

---

## Iteratie 6 — Geïntegreerde Regeling + anti-patterns (2026-05-23, na pilot-review PO 2.3)

**Aanleiding**: pilot-rapport `granulariteit-pilot-venb-draft.md` (parallelle Opus-sessie) + mijn match-review beide vielen terug op mechanische toepassing van de typologie. Twee fouten kwamen aan het licht:

### Fout 1 — Filter-categorie als bundel behandeld

Pilot-cluster 6: `verworpen-uitgaven` → bundel-concept met `#autokosten` / `#receptie` / `#geschenken` als sub-anchors.

**Gebruikers-correctie**:
> "autokosten zijn inderdaad fiscaal verworpen, maar hebben ook een btw component, boekingsafspraken, ... AL DIE DINGEN SAMEN ZIJN CONCEPTUELE COHESIE, dus dat is wat ik een 'regeling' zou noemen — de 'regeling rond autokosten'. Dan gaan we geen X autokost-regelingen hebben. En we kunnen alle regelingen die 'fiscaal verworpen' zijn verzamelen op een overzicht-Regeling of zelfs gewoon in het fiscaal Kader. Jullie laten zich te veel sturen door de toevallige bewoordingen uit het programmaonderdeel."

**Geleerde les**: een groepsnaam die enkel een fiscaal/boekhoudkundig *kenmerk* uitdrukt ("verworpen uitgaven", "voordelen alle aard", "niet-aftrekbare BTW") is geen bundel-concept. Dat zijn filter-categorieën die als overzichts-sectie in het bovenliggend Kader landen, met links naar de fenomeen-records.

### Fout 2 — PO-anchor-cohort als record-grens

Pilot-cluster 4 + mijn validatie: `kapitaalverhoging` + `kapitaalvermindering` in één PO-anchor 2.3.III.A.iv → behandeld als 1 G + 2 R.

**Gebruikers-correctie**:
> "Kapitaalverhoging en kapitaalvermindering werden in het programma (denk ik toevallig) samengezet omdat het tegenhangers zijn. Daardoor komen ze in hetzelfde anker. Waar we nu 1 G + 2 × R hebben in plaats van 2 × (G + R). Dus het ontploft."

**Geleerde les**: PO-bewoordingen en PO-anchor-cohort zijn organisatorische artefacten (didactische groepering, tegenhangers). Ze mogen geen record-grenzen opleggen. Twee tegenhanger-Gebeurtenissen blijven twee aparte records, elk met eigen Regeling-aspect.

### Fout 3 — Naamgeving `dbi-aftrek` als suffix-stijl gemarkeerd

Mijn match-review markeerde `dbi-aftrek` als compound-naam vs `reorganisatie-vennootschap-fiscaal` als suffix-stijl.

**Gebruikers-correctie**: `dbi-aftrek` is een domein-term — "aftrek" is geen generieke suffix maar deel van de geijkte naam. `reorganisatie-vennootschap-fiscaal` daarentegen heeft een dimensie-suffix (`-fiscaal`), wat Regel J expliciet verbiedt.

### Resulterend in ADR-030

- **Regel J — Geïntegreerde Regeling**: één fenomeen × alle dimensies (fiscaal · BTW · boekhouding · juridisch · loonfiscaliteit) = één record met N `accountant_perspectieven[]`.
- **Regel I uitgebreid** met twee anti-patterns: NIET bundelen als filter-categorie (verworpen-uitgaven); NIET bundelen op basis van PO-anchor-cohort (kapitaalverhoging+vermindering).
- **Naamgeving aangescherpt**: domein-termen waar aftrek/vrijstelling/regeling deel van de geijkte naam zijn blijven intact. Dimensie-suffix (`-fiscaal`, `-btw`) is verboden — dimensies leven binnen het record.

### Implicatie voor pilot PO 2.3

- Cluster 6 (verworpen uitgaven) **herzien**: geen `verworpen-uitgaven`-bundel. `autokosten`, `receptie-kosten`, `restaurantkosten`, `relatiegeschenken` worden eigen Regeling-records elk met fiscaal+BTW+boekhouding+loonfiscaliteit-perspectieven waar relevant. Het fiscaal Kader `vennootschapsbelasting` krijgt een overzichts-sectie "verworpen uitgaven" die naar deze records verwijst.
- Cluster 4 (kapitaalverrichtingen) **herzien**: `kapitaalverhoging` en `kapitaalvermindering` blijven twee aparte records (elk eigen G + R), ongeacht dat PO 2.3.III.A.iv ze samen-noemt.
- Naamgeving: `reorganisatie-vennootschap-fiscaal` herdopen tot `reorganisatie-vennootschap` met fiscaal/juridisch/boekhouding-perspectieven binnen één record.
