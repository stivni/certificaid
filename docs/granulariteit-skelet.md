# Granulariteit-skelet — concept-tree voor de hele corpus

**Status**: in opbouw (2026-05-23). Sparring-document met user. Wordt bij voltooiing de canonieke skelet-spec waar nieuwe records tegen aangelegd worden.
**Gerelateerd**: [ADR-030](adr/ADR-030-granulariteit-typologie.md) (rationale-meta) · [granulariteit-typologie-draft.md](granulariteit-typologie-draft.md) (sparring-historiek)
**Werkwijze**: top-down, sparring per laag, rationale per knoop. Mapping van bestaande 396 records gebeurt op het einde, niet tijdens opbouw.

---

## Compact top-level skelet (snapshot)

*Eén lijn per concept. Anchors (`▸ X`) en sub-records (`└── X`) staan op de regel ernaast. Tags: `[K]`=Kader · `[E]`=Entiteit · `[G]`=Gebeurtenis · `[R]`=Regeling · `[Σ]`=verzamelconcept (zie sectie hieronder) · combinaties = lijst-categorie. ⏳ = nog te ontwikkelen.*

**Disciplines (Kaders, top-niveau)**

```
boekhouding                              [K]
fiscaliteit                              [K]
├── personenbelasting                    [K]
├── vennootschapsbelasting               [K]
├── btw                                  [K]
├── registratie-en-successierechten      [K]
└── lokale-en-regionale-belastingen      [K]
audit-en-assurance                       [K]
├── controle-opdracht                    [K]
├── beoordelings-opdracht                [K]
├── isae-opdrachten                      [K]
└── overeengekomen-procedures            [K]
vennootschapsrecht                       [K]
beroep-en-deontologie                    [K]
bedrijfseconomie-en-management           [K]
```

**Cross-cutting clusters (per thema)**

```
mobiliteit                               [Σ-cluster, 4 records]
├── autokosten                           [R, Σ]
├── mobiliteitsbudget                    [R]      ▸ pijler-1-milieuvriendelijke-wagen ▸ pijler-2-duurzame-mobiliteit ▸ pijler-3-cash-saldo
├── cash-for-car                         [R, uitdovend]
└── woon-werkverkeer-en-km-vergoeding    [R]

kapitaalstructuur                        [16 records, na triangulatie]
├── oprichting-vennootschap              [G+R]    ▸ oprichtingskosten (boekhouding-aspect)
├── kapitaalverhoging                    [G+R]    └── kapitaalverhoging-in-natura [G+R] ▸ inbreng-onroerend
├── kapitaalvermindering                 [G+R]
├── inbreng-bedrijfstak-of-algemeenheid  [G+R]    (1 record — bevestigd door bestaand record; ook thema: reorganisatie)
├── quasi-inbreng                        [R]
├── inkoop-eigen-aandelen                [G+R]    (bestaand record; PO 3.0.IV.C)
├── voorkeurrecht                        [R]
├── volstortingsplicht                   [R]
├── aandeel                              [E]      ▸ aandeelhouders-rechten-en-plichten
├── algemene-vergadering                 [E-orgaan]  (bestaand record; PO 3.0.III)
├── aandeelhoudersovereenkomsten         [E]      ▸ stand-stillclausule ▸ voorkooprecht ▸ exit-clausule ▸ board-vertegenwoordiging ▸ controle-verwerving  (PO 3.0.VI)
├── eigen-vermogen                       [E-bundel] ▸ kapitaal ▸ uitgiftepremies ▸ herwaarderingsmeerwaarden ▸ reserves ▸ overgedragen-resultaat ▸ kapitaalsubsidies(?)
├── financieel-plan                      [E]
├── kapitaalbescherming                  [K-principe ⏳]  positionering TBD — OP-K.5
└── (meerwaarde-aandelen-venb)           TBD — perspectief van aandeel of eigen record (OP-K.6)

werknemers-vergoedingen                  [R, Σ — cluster-record]
├── bedrijfsleidersbezoldiging           [R, Σ]
├── forfaitaire-onkostenvergoeding       [R]
├── maaltijdcheques                      [R]
├── ecocheques                           [R]
├── sport-cultuur-cheques                [R]
├── geschenken-aan-werknemers            [R]
├── groepsverzekering-ipt                [R]
├── warrants-en-aandelenopties           [R]
├── niet-recurrente-resultaatsgebonden-bonus  [R]   (CAO 90)
├── vaa-woning                           [R]
├── vaa-pc-en-communicatie               [R]
├── vaa-renteloze-lening                 [R]
├── vaa-verwarming-en-elektriciteit      [R]
└── loon-en-payroll                      [K-techniek ⏳]   *berekenings-flow, geen keuze-Σ*
    ├── bruto-loon                       [R ⏳]
    ├── bedrijfsvoorheffing              [R ⏳]
    ├── rsz-werknemer                    [R ⏳]
    ├── rsz-werkgever                    [R ⏳]
    ├── werkbonus                        [R ⏳]
    ├── eindejaarspremie                 [R ⏳]
    ├── enkel-en-dubbel-vakantiegeld     [R ⏳]
    ├── dertiende-maand                  [R ⏳]
    ├── opzegvergoeding                  [R ⏳]
    └── outplacementkost                 [R ⏳]

winstuitkering                           [Σ-cluster ⏳]
├── dividend-uitkering                   ⏳
├── tussentijdse-dividenden              ⏳       (flag uit triangulatie KS — PO 3.0.IV.B)
├── tantième                             [G+R]    (primair hier; ook in werknemers-vergoedingen-lijst)
├── winstbestemming                      ⏳
├── liquidatiereserve                    ⏳
└── vvpr-bis-en-vvpr-uitkering           ⏳

overdracht-onderneming                   [eigen cluster — user-keuze 2026-05-24]
├── overdracht-onderneming               [R, Σ]   share-deal-aandelenovername · asset-deal-handelsfonds-overname; gedeelde aspecten: waardering · due-diligence · garanties
└── overnameovereenkomst-spa             [E]      (bestaand record; PO 3.0.V)

schuldfinanciering                       [eigen cluster — user-keuze 2026-05-24]
├── banklening-investeringskrediet       [E]      (bestaand)
├── achtergestelde-lening                [E+R]    (bestaand)
├── obligatielening                      [E]      (nieuw; PO 1.1.II.V)
├── leasing                              [E+R]    (bestaand — ook in mobiliteit-perspectief)
│   ├── financiele-leasing               [E+R]    (bestaand)
│   └── operationele-leasing             [E+R]    (bestaand)
└── (schuldfinanciering-Σ)               TBD — verzamelconcept "vreemd vermogen kiezen"?

reorganisatie                            [Σ-cluster ⏳]
├── fusie                                ⏳
├── splitsing                            ⏳
├── partiële-splitsing                   ⏳
└── (inbreng-bedrijfstak-of-algemeenheid → kapitaalstructuur)

fiscale-voordelen-vennootschap           [Σ-cluster ⏳]
├── dbi-aftrek                           ⏳
├── innovatie-aftrek                     ⏳
├── investeringsaftrek                   ⏳
├── notionele-interestaftrek             ⏳ (historisch)
└── gespreide-belasting-meerwaarden      ⏳

anti-misbruik                            [⏳]
├── algemene-anti-misbruik-bepaling      ⏳
├── simulatie                            ⏳
├── transfer-pricing-correcties          ⏳
└── thin-cap                             ⏳

insolventie                              [⏳]
├── alarmbel-procedure                   ⏳
├── faillissement                        ⏳
└── gerechtelijke-reorganisatie          ⏳

beroepsbeoefening                        [⏳]
├── witwasplicht-aml                     ⏳
├── opdrachtbrief                        ⏳
├── onafhankelijkheid                    ⏳
└── archiefplicht                        ⏳
```

**Leesregel**: een record hangt op één plek in deze tree (zijn thuis-cluster). Verbindingen naar andere clusters via `relaties[]`. Discipline-binding via `accountant_perspectieven[]`. Thema-tag `thema: []` is orthogonaal (een record kan meerdere thema's dragen, één primair-cluster).

---

## Verzamelconcept-pattern (`[Σ]`)

Sommige records zijn primair een **lijst + keuzekader/vergelijking** voor een familie van alternatieven. Ze dragen overkoepelende stof die nergens anders thuishoort, en linken naar de individuele leden.

| Kenmerk | Wat |
|---|---|
| **Doel** | "Welke modaliteit kies ik?" — beslisboom voor accountant-stagiair |
| **Inhoud verplicht** | (1) lijst leden met één-zin-samenvatting per stuk · (2) keuze-criteria/vergelijkingstabel · (3) overkoepelende regels die ALLE leden raken |
| **Categorie** | meestal `[R]` (advies-Regeling); kan ook `[K]` (sub-discipline-overzicht) zijn |
| **Tag** | `[Σ]` in skelet-tree-snapshot; in schema later via `is_verzamelconcept: true` (formalisatie via ADR-update) |
| **Onderscheid met bundel** | Bundel = Entiteiten met samenhang (Regel F, `#anchor`-sub-records binnen één record). Verzamelconcept = aparte records + één overkoepelend record met `relaties[]` naar elk lid. |
| **Onderscheid met filter-categorie** | Filter-categorie (verworpen-uitgaven) = geen overkoepelende keuze of stof — alleen een fiscaal-administratieve verzameling. Verzamelconcept = WEL keuzekader + overkoepelende stof. |

**Voorbeelden in huidig skelet**:
- `werknemers-vergoedingen` — keuze cash vs cheque vs VAA vs aandelenoptie vs pensioen; afbakening "wanneer is iets loon (BV+RSZ)?"; cluster-niveau-Σ
- `bedrijfsleidersbezoldiging` — lijst van 4 bouwblokken (loon · tantième · VAA · onrechtstreekse vergoeding) + 45.000-EUR-regel + bezoldigingstheorie
- `autokosten` — lijst van modaliteiten (eigen wagen · bedrijfswagen · leasing · km-vergoeding) + gedeelde fiscale spelregels (VU-CO2, BTW 50%, VAA-auto)
- `winstuitkering` (⏳) — lijst uitkeringsvormen (dividend · tantième · liquidatiereserve · pro-rata-kapitaalvermindering) + keuze-criteria (RV-tarief · timing · winstbestemmings-volgorde)

**Onderscheid met Kader-techniek `[K-techniek]`**: een berekenings-/proces-flow zonder echte keuze is geen Σ maar een K-techniek. Verschil:
- **Σ (verzamelconcept)** = "welke kies ik" (advies-georiënteerd, vergelijkingsmatrix kern)
- **K-techniek** = "hoe doe ik dit deterministisch" (procesflow, geen keuze-vraag)

Voorbeeld: `loon-en-payroll` (⏳) = K-techniek (bruto → BV → RSZ → netto is geen keuze, het is een dwingende methodologie). Componenten (`bruto-loon`, `bedrijfsvoorheffing`, ...) blijven aparte Regeling-records; `loon-en-payroll` als K-techniek bundelt het stappenplan.

**Wanneer GEEN verzamelconcept én GEEN K-techniek**: als de "lijst" puur een filter-administratieve verzameling is zonder overkoepelende stof of keuze (verworpen-uitgaven = filter-categorie, geen advies-keuze en geen proces-flow).

---

## Vocabularium — super-categorieën + synoniemen

De 4 super-categorieën van ADR-030 zijn umbrella's. Per categorie meerdere sub-types/synoniemen die we mogen gebruiken in record-namen en schrijfstijl, mits ze consistent zijn.

| Super-categorie | Synoniemen / sub-types | Wanneer welk woord |
|---|---|---|
| **Kader** | discipline · sub-discipline · techniek · principe · denkkader | discipline = top (boekhouding); sub-discipline = vak binnen discipline (vennootschapsbelasting); techniek = methodologie (consolidatie-techniek, aangifte-vennootschapsbelasting-opmaken); principe = denkregel (getrouw-beeld-principe, voorzichtigheidsbeginsel) |
| **Entiteit** | actor · ding · object · construct · instrument | actor = persoon/organisatie die handelt (vennootschap, aandeelhouder, bestuurder, commissaris); construct = juridisch geconstrueerd ding (vruchtgebruik, aandeel, consolidatiekring); instrument = financieel/juridisch werktuig (leasing-contract, obligatie) |
| **Gebeurtenis** | handeling · transactie · verrichting · event · operatie | handeling = bewuste daad (statutaire-uittreding); transactie = uitwisseling tussen partijen (dividend-uitkering); verrichting = formele operatie (kapitaalverhoging); event = passief/extern (faillissement) |
| **Regeling** | regime · faciliteit · stelsel · maatregel · regel | regime = wettelijk afwijkend stelsel (dbi-aftrek, liquidatiereserve, gespreide-belasting-meerwaarden); faciliteit = belastingvoordeel (innovatie-aftrek, notionele-interestaftrek); maatregel = corrigerend (verworpen-uitgaven-overzicht, alarmbel-procedure) |

**Rationale**: sub-types zijn alleen taalkundig (record-namen mogen `-techniek`, `-principe`, `-procedure`, `-aftrek`, `-regime` dragen als die het natuurlijke woord zijn, niet als verplichte categorie-suffix). Zie ook ADR-030 §Naamgeving-conventie.

**Schema-impact (2026-05-23)**: `categorie` is een **lijst** (`categorie: []`), niet één waarde. Een record dat coherent meerdere super-categorieën combineert (Regel A — 1+1=1) draagt ze allemaal in `categorie[]`. Naam = de gangbaarste accountantsterm (niet de "primaire" categorie afdwingen). Voorbeelden:
- `afschrijving` → `categorie: [entiteit, gebeurtenis, regeling]` — vindbaar via `vast-actief`, `aankoop-vast-actief`, `afschrijvingsmethode` als synoniemen
- `kapitaalverhoging` → `categorie: [gebeurtenis, regeling]`
- `dbi-aftrek` → `categorie: [regeling]` (puur Regeling)
- `aandeel` → `categorie: [entiteit]`

---

## Inhoud vs perspectief — scherpe lijn

Twee onderscheidende rubrieken per record:

| Rubriek | Wat | Voorbeelden |
|---|---|---|
| **`inhoud`** | *Wat het IS* — beschrijving, toepassingscontext, voorwaarden, wettelijke verankering, formaliteiten, eigenschappen | Definitie van een aandeel, welk type vennootschap er statuten moet hebben, AV-meerderheid voor kapitaalverhoging, notariële akte vereiste, fiscaal-rechtelijke grondslag, criteria toepasbaarheid Regeling |
| **`accountant_perspectieven[]`** | *Wat de accountant DOET* met dit fenomeen — werk-perspectief | Boekingen maken, aangifte opstellen, btw-aftrek berekenen, controle uitvoeren, advies geven, AML-melding doen |

**NIET als perspectief gebruiken**: `juridisch`, `vennootschapsrecht`, `notarieel`, `civielrechtelijk` — dat zijn *eigenschappen van het object*, niet werk van de accountant. Een vennootschapsrechtelijke vereiste (notariële akte voor BV-oprichting) is inhoud, geen perspectief.

**Wél als perspectief**: `boekhouding` · `fiscaal-PB` / `fiscaal-VenB` / `btw` / `registratie` · `audit` · `advies` · `beroep-en-deontologie` (eigen plichten zoals AML, archief, onafhankelijkheid). De vraag is steeds: zit dit op het bureau van de accountant als concreet werk?

**Gevolg**: records worden slanker. Eigenschappen-van-het-ding zitten in `inhoud`, niet verspreid over vijf pseudo-perspectieven.

---

## Laag 1 — Discipline-stam (Kaders top-niveau)

```
Disciplines (Kaders top)
├── boekhouding
├── fiscaliteit
│   ├── personenbelasting
│   ├── vennootschapsbelasting
│   ├── btw
│   ├── registratie-en-successierechten
│   └── lokale-en-regionale-belastingen
├── audit-en-assurance
│   ├── controle-opdracht
│   ├── beoordelings-opdracht
│   ├── isae-opdrachten
│   └── overeengekomen-procedures
├── vennootschapsrecht
├── beroep-en-deontologie
└── bedrijfseconomie-en-management

Cross-cutting (eigen stammen, niet onder een discipline)
├── Entiteiten           — alle Entiteit-records
├── Gebeurtenissen       — alle Gebeurtenis-records
└── Regelingen           — alle Regeling-records (geen "die niet aan één discipline vasthangen"-onderscheid; alle Regelingen zijn cross-cutting via perspectieven)
```

**Belangrijke simplificatie (2026-05-23)**: de discipline-stam bevat **alleen Kader-records** (disciplines, sub-disciplines, technieken, principes). Alle Regelingen + Entiteiten + Gebeurtenissen leven in de cross-cutting stammen. Discipline-binding gebeurt via `accountant_perspectieven[]` en `relaties[]`. Eén record hangt op één plek; kruisverbindingen via perspectieven en relaties. Zie rationale-log.

### Thema's — orthogonale tagging

Naast de tree-positie krijgt elk record een lijst **thema's** (vrije tags). Records uit verschillende stammen kunnen onder hetzelfde thema vallen. Voorbeelden voorlopige thema's:

- `mobiliteit` (autokosten, mobiliteitsbudget, cash-for-car, woon-werkverkeer-km-vergoeding, fietsvergoeding)
- `werknemers-vergoedingen` (loon, VAA-records, maaltijdcheques, sportcultuurcheques, ecocheques, geschenken-aan-werknemers, premies, opzegvergoedingen)
- `fiscale-voordelen-vennootschap` (DBI, NIA, innovatie-aftrek, investeringsaftrek, ...)
- `anti-misbruik` (algemene anti-misbruik-bepaling, transfer-pricing-correcties, simulatie, ...)
- `bestuurdersaansprakelijkheid`
- ...

Voorlopig vrije lijst; later eventueel gesloten vocabulaire vastleggen via ADR-update. Schema-veld: `thema: []` (string-lijst).

### Officiële naam + synoniemen

Elk record draagt:
- **`naam`** (record-id) = praktijkterm, accountant-spraak (`autokosten`, `dbi-aftrek`, `cash-for-car`)
- **`naam_officieel`** (optioneel) = wettelijke benaming als die afwijkt (`cash-for-car` → "mobiliteitsvergoeding")
- **`synoniemen: []`** = andere gangbare benamingen (afkortingen, oude termen, jargon)

Doel: zoek/RAG-treffers + houvast voor stagiairs die een wettekst-term tegenkomen + extractie-ankers voor LLM.

### Notatie in tree

- `└── X` = eigen record
- `▸ X` = sub-sectie met `#anchor` binnen ouder-record (Regel F)
- `· X` = `accountant_perspectieven[]`-item binnen ouder-record

### Hybride records (E+R+G) — categorie als lijst

Een record dat meerdere super-categorieën coherent combineert (Regel A — 1+1=1) draagt ze alle in `categorie[]`. De **naam** kiest de gangbaarste accountantsterm (niet "de primaire categorie"). De **plek in de cluster-tree** volgt het thema, niet de categorie. Vindbaarheid via `synoniemen[]` (kan ook namen uit andere categorieën bevatten).

Voorbeelden:
- `oprichting-vennootschap` → `categorie: [gebeurtenis, regeling]`. Naam = de verrichting.
- `leasing` → `categorie: [entiteit, gebeurtenis, regeling]`. Naam = het instrument; divergente Regelingen kunnen apart afsplitsen als hun mechaniek substantieel verschilt.
- `afschrijving` → `categorie: [entiteit, gebeurtenis, regeling]`. Naam = het mechanisme (gangbaarst); synoniemen: `vast-actief`, `aankoop-vast-actief`, `afschrijvingsmethode`.

### Tree-nesting tussen records

- **Binnen dezelfde stam** toegestaan: een sub-Gebeurtenis kan onder een ouder-Gebeurtenis hangen (specialisatie of compositie). Bv `kapitaalverhoging-in-natura` onder `kapitaalverhoging`, of `vereffening-binnen-3-maanden` onder `vereffening`.
- **Cross-stam niet via tree-nesting** — Regeling onder Gebeurtenis hangen zou ambigu zijn. `quasi-inbreng` (Regeling die op kapitaalinbreng werkt) hangt in Regelingen-stam met `relaties[]` naar `kapitaalverhoging`, niet onder `kapitaalverhoging`-knoop.
- **Schema-aspect**: tree-nesting is alleen voor het skelet-document (leesbaarheid + extractie-hints). Het record-schema heeft geen `parent`-veld; alle records zijn plat met `relaties[]` als binding. Een geneste record kan in `relaties[]` een `is-onderdeel-van` / `specialisatie-van` relatie dragen.

### Rationale per knoop

**`boekhouding`** — Discipline. Geen sub-tree op laag 1 (technieken zoals jaarrekening-opmaak, waarderingsregels, consolidatie-techniek leven op laag 2 als Kader-techniek-records onder deze discipline). *Alternatief verworpen*: `boekhouding` splitsen in `BE-GAAP` en `IFRS` — verworpen want IFRS is een waarderings-stelsel binnen boekhouding, geen eigen discipline. Analoog: `fiscaliteit` splitst wel in sub-disciplines, `boekhouding` niet (BE-GAAP/IFRS = Regeling-keuze, geen sub-discipline).

**`fiscaliteit`** met sub-tree — keuze (1) uit laag-1-sparring. Cross-fiscale principes (rechtsgrondslag, fiscaal-rechtelijke methode, gerechtelijke procedure, bezwaar-en-geschil) leven in `fiscaliteit` als parent-Kader. Sub-disciplines (PB, VenB, BTW, ...) hangen daar onder met eigen technieken (`aangifte-vennootschapsbelasting-opmaken` onder VenB). *Te toetsen*: of cross-fiscale principes substantieel genoeg zijn om de parent-Kader te dragen — zo niet, valt `fiscaliteit` weg als parent en worden PB/VenB/BTW top-disciplines.

**`audit-en-assurance`** met sub-tree per opdrachttype — keuze (4) uit laag-1-sparring. Eén discipline, sub-Kaders per opdrachttype (controle / beoordeling / ISAE / overeengekomen procedures). *Alternatief verworpen*: aparte top-disciplines per opdrachttype — verworpen want ISA-normen, onafhankelijkheidsregels en risico-aanpak zijn gedeeld over opdrachttypes; één parent-discipline houdt die als gedeelde basis.

**`vennootschapsrecht`** als top-discipline — keuze (2) uit laag-1-sparring. Andere juridische topics (insolventie, arbeidsrecht, contractenrecht) zijn perifeer in de examenscope en leven als Regelingen of cross-cutting (faillissement = cross-cutting Gebeurtenis). *Te herzien*: als bij uitwerking blijkt dat insolventierecht een substantieel eigen blok wordt, kan `juridisch` als parent worden ingevoegd.

**`beroep-en-deontologie`** als top-discipline — bevat ITAA-normen, beroepsplichten, onafhankelijkheid, witwasplicht-deontologisch-deel. *Te beslissen*: AML als cross-cutting Regeling (omdat ze alle opdrachttypes raakt) of binnen `beroep-en-deontologie`. Voorlopige keuze: AML als cross-cutting Regeling met perspectieven naar `audit`, `boekhouding`, `beroep-en-deontologie` — sluit aan bij Regel J (één fenomeen, alle dimensies).

**`bedrijfseconomie-en-management`** als top-discipline — bevat financiële analyse (ratio's, kasstroom), waardering van ondernemingen, M&A-economie, treasury-basics. Twijfelpunt: deze discipline is meer "tool-kit" dan "discipline met eigen normen". *Te toetsen* bij laag-2-uitwerking of dit niet beter als Kader-techniek-blok onder `boekhouding` (financiële analyse) + apart `M&A-en-waardering` blok elders kan.

**Cross-cutting Entiteiten + Gebeurtenissen** — keuze (3) uit laag-1-sparring. Niet onder een discipline ophangen. Hun perspectieven verwijzen via `accountant_perspectieven[]` naar disciplines. Analogie: `aandeel` heeft een `vennootschapsrecht`-perspectief (definitie, overdracht), `boekhouding`-perspectief (waardering), `fiscaal`-perspectief (DBI, RV, meerwaarden), `audit`-perspectief (aandeelhoudersregister-controle).

**Cross-Regelingen** — Regelingen die niet aan één discipline vasthangen. Voorbeelden te toetsen: `witwasplicht-aml` · `getrouw-beeld-principe` (of woont dit in `boekhouding`?) · `verbonden-vennootschappen-begrip` (cross WVV + fiscaal + IAS24).

### Open punten laag 1

- **OP-1.1** Cross-fiscale principes — zijn ze substantieel genoeg om `fiscaliteit` als parent-Kader te dragen? Verifiëren bij laag-2-uitwerking PB+VenB+BTW.
- **OP-1.2** AML als cross-Regeling of als sub-Kader onder `beroep-en-deontologie`? Voorkeur cross-Regeling.
- **OP-1.3** `bedrijfseconomie-en-management` als eigen discipline of opsplitsen? Verifiëren bij laag-2.
- **OP-1.4** Diepte van `vennootschapsrecht` — als insolventierecht en arbeidsrecht substantieel blijken, parent `juridisch` invoegen.

---

## Laag 2 — sub-disciplines + technieken per discipline

(in opbouw — start met `vennootschapsbelasting` + cross-cutting Gebeurtenissen)

### vennootschapsbelasting (sub-discipline onder fiscaliteit)

Te ontwikkelen. Vertrekpunt: PO 2.3 (21 anchors in `data/programma/anchors.json`) + bestaande VenB-records + pilot-rapport (`granulariteit-pilot-venb-draft.md`).

### Overdracht-onderneming-cluster

Thema: `overdracht-onderneming`. *Eigen cluster (user-keuze 2026-05-24). Vervangt `vs`-smell `overname-handelsfonds-vs-aandelen`.*

```
overdracht-onderneming
├── overdracht-onderneming               [R, Σ]   share-deal · asset-deal
└── overnameovereenkomst-spa             [E]      (bestaand)
```

**`overdracht-onderneming`** [R, Σ] (PO 3.0.V + 2.x.taak.2 "overdracht of ontbinding van de onderneming")
- inhoud: overkoepelend keuzekader voor overdracht van een onderneming — 2 fundamentele modaliteiten + gedeelde aspecten. **Vergelijkingsmatrix**: fiscale impact (meerwaarde-belasting verkoper vs goodwill-afschrijving koper) · btw-impact (overdracht algemeenheid art 11/18 Wbtw vs btw op activa) · registratierechten · overdracht van passiva (automatisch bij share-deal, niet bij asset-deal) · garanties (representations & warranties) · due diligence-scope · personeels-overdracht (CAO 32bis ⚠️).
- sub-secties: `#share-deal-aandelenovername` (= verwerving aandelen — koper verkrijgt vennootschap met al haar activa/passiva/contracten; verkoper realiseert meerwaarde aandelen) · `#asset-deal-handelsfonds-overname` (= verwerving handelsfonds — koper kiest activa cherry-pick; verkoper realiseert meerwaarde op activa, vennootschap blijft bestaan)
- gedeelde aspecten: `#waardering-onderneming` (DCF, EBITDA-multiple, NAV, vergelijkbare transacties) · `#due-diligence` (financieel/fiscaal/juridisch/operationeel) · `#garanties-en-vrijwaring` (R&W, escrow, MAC-clausule)
- perspectieven: `advies` (modaliteit-keuze, prijsstructuur, fiscale optimalisatie verkoper+koper) · `fiscaal-VenB` (meerwaarde-realisatie verkoper, monetaire vs in-natura tegenprestatie) · `fiscaal-PB` (meerwaarde-aandelen privé-vermogen — vrijgesteld normaal beheer) · `fiscaal-BTW` (overdracht-algemeenheid-regime bij asset-deal) · `audit` (due diligence-uitvoering)
- naam_officieel: overdracht van een onderneming · synoniemen: M&A-transactie, bedrijfsoverdracht, exit-transactie, share deal vs asset deal
- relaties: `overnameovereenkomst-spa` (instrument), `aandeel` (object share-deal), `inbreng-bedrijfstak-of-algemeenheid` (alternatieve structurering), `aandeelhoudersovereenkomsten` (pre-overdracht-context), `meerwaarde-aandelen-venb` (verkoperskant)

**`overnameovereenkomst-spa`** [E] — bestaand record (PO 3.0.V)
- inhoud: contractueel instrument dat de overdracht regelt — partijen, voorwerp (aandelen of activa), prijs + prijsaanpassingsmechanisme, R&W-catalogus, voorwaarden opschortend/ontbindend, garanties, MAC-clausule, post-closing-verplichtingen, geschillenbeslechting.
- perspectieven: `advies` (opstellen + onderhandelen) · `audit` (kennisname bij audit + due diligence)
- naam_officieel: overnameovereenkomst, share purchase agreement (SPA), asset purchase agreement (APA) · synoniemen: SPA, APA, koop-verkoop-overeenkomst onderneming
- relaties: `overdracht-onderneming`, `aandeelhoudersovereenkomsten`

**Open punten overdracht-onderneming-cluster**:
- **OP-O.1** Is `overdracht-onderneming` Σ groot genoeg of zou share-deal en asset-deal beter aparte records zijn? Voorlopig 1 Σ-record (anti-versplinterings-principe + PO 3.0.V.B vraagt expliciet het *verschil* tussen beide, dus de vergelijkingsmatrix is de kern).
- **OP-O.2** Ontbinding/vereffening (PO 2.x.taak.2 "overdracht of ontbinding") als 2e Σ-record in dit cluster of als eigen `ontbinding-en-vereffening`-cluster? Voorlopig: eigen cluster (raakt insolventie + WVV Boek 2 Titel 8).

### Schuldfinanciering-cluster

Thema: `schuldfinanciering`. *Eigen cluster (user-keuze 2026-05-24). Bundelt vreemd-vermogen-instrumenten.*

```
schuldfinanciering
├── banklening-investeringskrediet                [E]      (bestaand)
├── achtergestelde-lening                         [E+R]    (bestaand)
├── obligatielening                               [E]      (nieuw — PO 1.1.II.V)
├── leasing                                       [E+R]    (bestaand — ook in mobiliteit-perspectief)
│   ├── financiele-leasing                        [E+R]    (bestaand)
│   └── operationele-leasing                      [E+R]    (bestaand)
└── (schuldfinanciering)                          [Σ ⏳]   verzamelconcept — TBD (OP-S.1)
```

**Details** (alleen nieuwe + skelet-relevante; bestaande records hebben al inhoud, mapping later):

**`obligatielening`** [E] (PO 1.1.II.V)
- inhoud: schuldinstrument waarbij vennootschap obligaties uitgeeft aan beleggers tegen vooraf bepaalde rente + terugbetalingstermijn. Modaliteiten: gewone vs converteerbare vs achtergestelde vs warrant-obligatie. Uitgifte vereist (NV) bestuursbesluit + soms AV; prospectus-plicht boven drempel (FSMA ⚠️). Boekhoudkundig op rekening 17. RV op interest (30% standaard ⚠️). Aflossing volgens schema (bullet vs amortizing).
- perspectieven: `boekhouding` (uitgifte-boeking, interest-toerekening pro rata, agio/disagio amortizatie) · `fiscaal-VenB` (interest-aftrekbaarheid; thin-cap-regels ATAD ⚠️) · `fiscaal-PB` (RV-inhouding beleggers) · `audit` (controle convenanten + waardering) · `advies` (uitgifte-structurering, alternatief bank vs publiek)
- naam_officieel: obligatielening · synoniemen: obligatie-uitgifte, bond issue, schuldbewijs
- relaties: `eigen-vermogen` (afbakening vreemd vs eigen), `kapitaalverhoging` (alternatief financieringsbron), `achtergestelde-lening` (variant), `converteerbare-obligatie` (variant)

**`leasing` / financiele-leasing / operationele-leasing`** [E+R] — bestaande records
- positionering: primair in schuldfinanciering-cluster (= financiering vast actief via huur-koop). Heeft mobiliteit-perspectief voor bedrijfswagen-context (relatie naar `autokosten`).
- kwalificatie-Regeling: BE-GAAP-criteria (lease > 50% looptijd actief + koopoptie + ...) ⚠️ vs IFRS 16 (alle lease op balans behalve short-term/low-value). Deze kwalificatie-keuze maakt het hybride [E+R].
- mapping-actie later: bestaande records bevatten al de inhoud — hier alleen positioneringsbevestiging.

**Open punten schuldfinanciering-cluster**:
- **OP-S.1** ⏳ Is een Σ-record `schuldfinanciering` gerechtvaardigd? Vergelijkingsmatrix (bank vs obligatie vs leasing vs achtergesteld) + thin-cap + ATAD + interest-aftrekbaarheid-Regels zou daarin landen. Of laten we het bij de individuele records + flag dat een keuzekader-record nuttig zou zijn? Voorlopig TBD.
- **OP-S.2** `leasing` primair in dit cluster (financierings-perspectief) of in mobiliteit (auto-perspectief)? Voorlopig: schuldfinanciering primair, mobiliteit-relatie via `autokosten`-record. Te valideren.
- **OP-S.3** `rekening-courant-zaakvoerder` als E in dit cluster (= interne kortlopende schuld vennootschap-aan-zaakvoerder of omgekeerd)? Bestaand record te checken; raakt ook `vaa-renteloze-lening` (werknemers-vergoedingen-cluster).
- **OP-S.4** Ontbreekt nog: handelsschulden, korte-termijn-financiering (factoring, kaskrediet)? PO 1.1.II.K "schulden op korte termijn" suggereert van wel. Triangulatie nodig.

### Werknemers-vergoedingen-cluster

Thema: `werknemers-vergoedingen`. *(Auto-gerelateerde VAA leeft in mobiliteit-cluster — `autokosten`-perspectief `fiscaal-PB`.)*

```
werknemers-vergoedingen
├── bedrijfsleidersbezoldiging                       [R]     (overkoepelend advies-regime — zie OP-W.4)
├── tantième                                         [G+R]   (ook thema: winstuitkering)
├── forfaitaire-onkostenvergoeding                   [R]
├── maaltijdcheques                                  [R]
├── ecocheques                                       [R]
├── sport-cultuur-cheques                            [R]
├── geschenken-aan-werknemers                        [R]
├── groepsverzekering-ipt                            [R]
├── warrants-en-aandelenopties                       [R]
├── niet-recurrente-resultaatsgebonden-bonus         [R]     (CAO 90)
├── vaa-woning                                       [R]
├── vaa-pc-en-communicatie                           [R]     (PC, laptop, tablet, gsm, internet)
├── vaa-renteloze-lening                             [R]
├── vaa-verwarming-en-elektriciteit                  [R]
└── (loon-werknemer)                                 ⏳      eigen sub-cluster (zie OP-W.2)
```

**Details per record** (hints voor extractie; ⚠️ = te verifiëren bij claims_checken):

**`werknemers-vergoedingen`** [R, Σ — cluster-record]
- inhoud: overkoepelend keuzekader voor alle vergoedingsvormen werkgever → werknemer/bedrijfsleider. **Afbakeningsvraag** "wanneer is iets loon (BV + RSZ + aftrekbaar 100%) vs vrijgesteld/bevoordeeld?" — onderscheid (a) cash-loon · (b) cheques (MC/ECO/SC/geschenken) · (c) VAA · (d) extra-legaal pensioen (groepsverzekering/IPT) · (e) aandelenoptie/warrant · (f) bonusplan (CAO 90) · (g) onkostenvergoeding. **Vergelijkingsmatrix** per vorm: PB-behandeling werknemer · RSZ-werknemer · RSZ-werkgever · VenB-aftrekbaarheid werkgever · plafonds · administratieve discipline (fiche/CAO/toetreding). Geen eigen wettelijke verankering — verzamelt en vergelijkt.
- perspectieven: `advies` (loonpakket-optimalisatie; trade-off werkgeverkost vs nettoresultaat werknemer) · `fiscaal-PB` + `fiscaal-VenB` (overkoepelende vergelijking, niet per-vorm-detail) · `boekhouding` (waar elke vorm landt: 62 vs 61 vs voorzieningen)
- naam_officieel: — · synoniemen: loonpakket, vergoedingspakket, alternatieve verloning, salary package
- relaties (= leden): alle records in dit cluster — `bedrijfsleidersbezoldiging`, `loon-en-payroll`, `forfaitaire-onkostenvergoeding`, `maaltijdcheques`, `ecocheques`, `sport-cultuur-cheques`, `geschenken-aan-werknemers`, `groepsverzekering-ipt`, `warrants-en-aandelenopties`, `niet-recurrente-resultaatsgebonden-bonus`, `vaa-woning`, `vaa-pc-en-communicatie`, `vaa-renteloze-lening`, `vaa-verwarming-en-elektriciteit`, plus oplijsting van `tantième` (primair cluster: winstuitkering)

**`bedrijfsleidersbezoldiging`** [R]
- inhoud: overkoepelend advies-regime over de bezoldigingsmix van een bedrijfsleider (cat 1: bestuurder/zaakvoerder). Bevat 4 bouwblokken: (1) maandelijks loon + BV; (2) tantième na AV-winstbestemming; (3) voordelen-alle-aard (woning, auto, lening, ...); (4) onrechtstreekse vergoeding via huur, groepsverzekering, dividend. **45.000-EUR-bezoldigingsregel** ⚠️ voor KMO-tarief (verlaagd VenB-tarief 20% op eerste schijf vereist min. bezoldiging aan ten minste één bedrijfsleider).
- perspectieven: `advies` (optimale mix, fiscale planning, KMO-tarief-borging) · `fiscaal-VenB` (aftrekbaarheid + KMO-tarief-voorwaarde) · `fiscaal-PB` (belastbaarheid in hoofde van bedrijfsleider) · `boekhouding` (rekening 618 / 62)
- naam_officieel: bezoldiging van bedrijfsleiders · synoniemen: bedrijfsleidersloon, zaakvoerdersbezoldiging
- relaties: `tantième`, `vaa-woning`, `vaa-renteloze-lening`, `groepsverzekering-ipt`, `huur-onroerend-goed-vennootschap` (cross-cluster), `dividend-uitkering` (alternatief), `kmo-tarief-vennootschapsbelasting`

**`tantième`** [G+R, **primair thema: winstuitkering**; secundair: werknemers-vergoedingen (oplijsting bedrijfsleider-vergoeding)]
- inhoud: winstgebonden vergoeding toegekend door AV bij winstbestemming aan bestuurder(s); aftrekbaar in het boekjaar waarop het betrekking heeft (mits AV-besluit en boeking) ⚠️ – speciale aftrekbaarheidsregel; belastbaar als bedrijfsleidersbezoldiging in PB; vermindert belastbaar resultaat VenB.
- perspectieven: `boekhouding` (voorziening / schuld; tijdige boeking) · `fiscaal-VenB` (aftrekbaarheid op resultaat boekjaar X via AV jaar X+1 ⚠️) · `fiscaal-PB` (bezoldiging cat 1) · `advies` (planning rond winstbestemming + KMO-tarief)
- naam_officieel: tantième · synoniemen: bestuurderstantième, winstbonus-bestuurder
- relaties: `bedrijfsleidersbezoldiging`, `winstbestemming`, `dividend-uitkering`

**`forfaitaire-onkostenvergoeding`** [R]
- inhoud: vergoeding "kosten eigen aan de werkgever" → niet-belastbaar voor werknemer, aftrekbaar voor werkgever, mits dubbele bewijslast (forfaitaire raming op redelijke gronden + werkelijk bestemd voor werkgeverskosten). Forfait-bedragen per categorie ⚠️ (parkeer, kleine kosten, verblijfsvergoeding binnen-/buitenland, ...). Fiche 281.10 melding ⚠️.
- perspectieven: `fiscaal-PB` (niet-belastbaar mits voorwaarden) · `fiscaal-VenB` (aftrekbaar) · `boekhouding` (rekening 61) · `advies` (raming opstellen, fiche-discipline, ruling)
- naam_officieel: terugbetaling van kosten eigen aan de werkgever · synoniemen: kostenforfait, onkostenvergoeding, KEW
- relaties: `loon-werknemer` (afbakening), `bedrijfsleidersbezoldiging`

**`maaltijdcheques`** [R]
- inhoud: dagelijkse cheque voor werknemers; max nominaal €8 ⚠️; werkgevertussenkomst max €6,91 ⚠️; werknemerbijdrage min €1,09 ⚠️. Bij naleving voorwaarden: vrijgesteld van RSZ + PB; werkgevertussenkomst gedeeltelijk aftrekbaar (€2/cheque ⚠️). Elektronische cheques verplicht.
- perspectieven: `fiscaal-PB` (vrijstelling werknemer) · `fiscaal-VenB` (gedeeltelijke aftrekbaarheid) · `boekhouding` (rekening 62/61) · `advies` (alternatief voor loonopslag)
- naam_officieel: maaltijdcheques · synoniemen: lunch-cheques, MC
- relaties: `loon-werknemer`, `ecocheques`, `sport-cultuur-cheques`, `geschenken-aan-werknemers`

**`ecocheques`** [R]
- inhoud: cheques voor ecologische aankopen, max €250/jaar ⚠️; vrijgesteld van RSZ + PB; **niet aftrekbaar** voor werkgever ⚠️ (in tegenstelling tot maaltijdcheques). Lijst toegelaten producten/diensten via CAO 98.
- perspectieven: `fiscaal-PB` (vrijstelling) · `fiscaal-VenB` (niet-aftrekbaar → verworpen uitgave) · `boekhouding` · `advies`
- naam_officieel: ecocheques · synoniemen: groene cheques
- relaties: `maaltijdcheques`, `verworpen-uitgaven-overzicht` (filter-sectie)

**`sport-cultuur-cheques`** [R]
- inhoud: cheques voor sport/cultuur-activiteiten, max €100/jaar ⚠️; vrijgesteld onder voorwaarden; aftrekbaarheidsregime verifiëren ⚠️.
- perspectieven: `fiscaal-PB` · `fiscaal-VenB` · `boekhouding` · `advies`
- naam_officieel: sport- en cultuurcheques · synoniemen: SC-cheques
- relaties: `maaltijdcheques`, `ecocheques`

**`geschenken-aan-werknemers`** [R]
- inhoud: gelegenheidsgeschenken vrijgesteld onder grenzen — Sinterklaas/Kerst/Nieuwjaar: max €40/werknemer + €40/kind ⚠️; eervolle onderscheiding: €120 ⚠️; pensionering: €40/dienstjaar (min €120, max €1.000) ⚠️. Boven grens: belastbaar loon. Werkgever aftrekbaar mits binnen grenzen + collectief karakter.
- perspectieven: `fiscaal-PB` (vrijstelling onder grens) · `fiscaal-VenB` (aftrekbaarheid onder voorwaarden) · `boekhouding` · `advies`
- naam_officieel: geschenken en geschenkcheques · synoniemen: gelegenheidsgeschenken, jaarlijkse geschenken
- relaties: `verworpen-uitgaven-overzicht`, `receptiekosten` (cross — andere VU-regel)

**`groepsverzekering-ipt`** [R]
- inhoud: extra-legaal pensioen-spaar-vehikel — werkgever (groepsverzekering werknemers) of vennootschap (IPT = Individuele Pensioentoezegging bedrijfsleider) betaalt premies; **80%-regel** ⚠️ begrenst aftrek werkgeverspremies (premies + wettelijk pensioen ≤ 80% laatste normale brutoloon); kapitaaluitkering belast aan 10%/16,5%/18%/20% bij pensionering ⚠️; bijzondere 4,4%-premie taks. Backservice-mogelijkheid.
- perspectieven: `fiscaal-VenB` (aftrekbaarheid premies — 80%-regel) · `fiscaal-PB` (belastbaarheid kapitaal/rente bij uitkering) · `boekhouding` (premiekost; geen voorziening op balans tenzij intern-pensioenfonds) · `advies` (planning kapitaal-uitkering, backservice, vergelijking met dividend-route)
- naam_officieel: groepsverzekering / individuele pensioentoezegging (IPT) · synoniemen: tweede pijler, aanvullend pensioen, EIP, IPT
- relaties: `bedrijfsleidersbezoldiging`, `loon-werknemer`, `pensioenstelsel` (cross)

**`warrants-en-aandelenopties`** [R]
- inhoud: toekenning recht om aandelen te kopen aan vooraf bepaalde prijs; wet 26 maart 1999 ⚠️; **belastbaar bij toekenning** (niet uitoefening) op forfaitair voordeel = 18% × waarde onderliggend aandeel × verminderingsfactor looptijd ⚠️; bij beursgenoteerde aandelen + voorwaarden: lager forfait; geen RSZ als voorwaarden vervuld. Warrant = afzonderlijk effect (vaak in fondsen), aandelenoptie = recht op specifiek aandeel.
- perspectieven: `fiscaal-PB` (forfaitair voordeel bij toekenning) · `boekhouding` (geen impact bij toekenning werkgever, behalve waardering eigen aandelen bij latere uitoefening) · `advies` (alternatief voor cash-bonus; planningsdiscussie)
- naam_officieel: aandelenoptie (wet 26 maart 1999); warrant · synoniemen: stock options, ESOP, optieplan
- relaties: `loon-werknemer`, `bedrijfsleidersbezoldiging`, `aandeel`, `kapitaalverhoging` (bij uitoefening met nieuwe aandelen)

**`niet-recurrente-resultaatsgebonden-bonus`** [R]
- inhoud: collectief bonus-systeem op basis van objectief meetbare doelstellingen, CAO 90 ⚠️; vrijgesteld van PB tot max €4.020 (geïndexeerd) ⚠️; aan RSZ-werkgever (33%) + RSZ-solidariteitsbijdrage werknemer (13,07%) ⚠️ ; werkgever aftrekbaar; toetreding via toetredingsakte (geen bestaande werknemers) of CAO.
- perspectieven: `fiscaal-PB` (vrijstelling tot grens) · `fiscaal-VenB` (aftrekbaarheid) · `boekhouding` (loonkost) · `advies` (plan-opmaak, doelstelling-formulering)
- naam_officieel: niet-recurrente resultaatsgebonden voordelen · synoniemen: CAO 90-bonus, salary-bonus-plan, bonusplan
- relaties: `loon-werknemer`, `tantième` (alternatief, andere logica)

**`vaa-woning`** [R]
- inhoud: voordeel-alle-aard wanneer werkgever/vennootschap een gebouw gratis ter beschikking stelt aan bedrijfsleider/werknemer; forfait = kadastraal-inkomen × 100/60 × 2 (geïndexeerd) ⚠️ — sinds wet 2018 ⚠️ geen onderscheid meer rechtspersoon/natuurlijke persoon. Verhoging bij gemeubileerd (5/3) ⚠️. Wanneer een vennootschap eigenaar is + privégebruik: belast op werknemer + geen impact aftrekbaarheid mits bezoldigingstheorie.
- perspectieven: `fiscaal-PB` (forfait-formule, VAA) · `fiscaal-VenB` (aftrekbaarheid kosten woning — bezoldigingstheorie ⚠️) · `boekhouding` (eigenaarskosten + afschrijving) · `advies` (privégebruik-clausule, alternatief huurconstructie)
- naam_officieel: voordeel van alle aard — kosteloze terbeschikkingstelling onroerend goed · synoniemen: VAA woning, woon-VAA
- relaties: `bedrijfsleidersbezoldiging`, `huur-onroerend-goed-vennootschap` (alternatief constructie)

**`vaa-pc-en-communicatie`** [R]
- inhoud: gebundeld VAA-record voor digitale werkmiddelen met forfait-logica: PC/laptop €72/jaar ⚠️, tablet/gsm €36/jaar ⚠️, internet €60/jaar ⚠️, telefoon-abonnement €48/jaar ⚠️ (per stuk, per gebruiker). Vrijstelling bij beroepsgebruik > x% (te verifiëren). Schema: één forfait per ter beschikking gesteld element (cumuleerbaar).
- perspectieven: `fiscaal-PB` (forfait per element) · `fiscaal-VenB` (aftrekbaarheid bedrijfsmiddel) · `boekhouding` (afschrijving / abonnementskost)
- naam_officieel: voordeel van alle aard — PC, gsm, tablet, internet, telefoonabonnement · synoniemen: VAA PC, VAA gsm, VAA laptop, ICT-VAA
- relaties: `bedrijfsleidersbezoldiging`, `loon-werknemer`

**`vaa-renteloze-lening`** [R]
- inhoud: lening van werkgever/vennootschap aan bedrijfsleider/werknemer onder marktrente → VAA = verschil tussen marktrente (referentierentevoet) en werkelijk aangerekende rente; jaarlijks referentierentevoet vastgesteld bij KB ⚠️ (apart voor hypothecair vs niet-hypothecair, vast vs variabel). Negatieve rekening-courant zaakvoerder = klassiek toepassingsgeval.
- perspectieven: `fiscaal-PB` (VAA-berekening) · `boekhouding` (rekening-courant zaakvoerder/bestuurder 416/489) · `audit` (controle rekening-courant-stand) · `advies` (afbouw-strategie)
- naam_officieel: voordeel van alle aard — kosteloze of goedkope lening · synoniemen: VAA lening, rekening-courant-VAA, RC-zaakvoerder-VAA
- relaties: `bedrijfsleidersbezoldiging`, `rekening-courant-zaakvoerder` (cross)

**`vaa-verwarming-en-elektriciteit`** [R]
- inhoud: VAA wanneer werkgever verwarming/elektriciteit kosteloos verstrekt — forfait per jaar (verwarming ~€2.090/€990 ⚠️ afhankelijk leidinggevend of niet; elektriciteit ~€1.040/€470 ⚠️). Naast VAA-woning toepasbaar als nutsvoorzieningen mee zijn.
- perspectieven: `fiscaal-PB` (forfait) · `fiscaal-VenB` (aftrekbaarheid kost werkgever) · `boekhouding`
- naam_officieel: voordeel van alle aard — verwarming en elektriciteit · synoniemen: VAA nutsvoorzieningen
- relaties: `vaa-woning` (vaak samen)

**Open punten werknemers-vergoedingen-cluster** (na sparring-ronde 2026-05-24):
- **OP-W.1** ✅ **Beslist**: `vaa-pc-en-communicatie` = 1 record met cumulatieve forfaits per element. Regel A (1+1=1: gedeelde forfait-logica + gedeeld toepassingscontext). Forfait-tabel als sub-sectie/anchor in het record.
- **OP-W.2** ✅ **Beslist (2-traps)**: (a) alle loon-Regelingen apart (10 records: `bruto-loon`, `bedrijfsvoorheffing`, `rsz-werknemer`, `rsz-werkgever`, `werkbonus`, `eindejaarspremie`, `enkel-en-dubbel-vakantiegeld`, `dertiende-maand`, `opzegvergoeding`, `outplacementkost`). (b) `loon-en-payroll` als **K-techniek** (geen Σ — geen keuze, wel methodologie: bruto → BV → RSZ → netto-flow). (c) `werknemers-vergoedingen` als **Σ-cluster-record** dat alle vergoedingsvormen oplijst + vergelijkt. Drie verschillende vragen: HR-keuze (Σ-werknemers-vergoedingen) · payroll-techniek (K-loon-en-payroll) · bedrijfsleider-mix (Σ-bedrijfsleidersbezoldiging). Zie nieuw onderscheid Σ vs K-techniek in sectie "Verzamelconcept-pattern".
- **OP-W.3** ✅ **Beslist**: `tantième` primair thema = `winstuitkering` (meest gebruikt voor zaakvoerders, leeft in de winstbestemming-volgorde). Wordt secundair geoplijst in het `werknemers-vergoedingen`-verzamelconcept (en in `bedrijfsleidersbezoldiging`-lijst).
- **OP-W.4** ✅ **Beslist + uitgebreid**: verzamelconcept-pattern formeel ingevoerd (zie sectie "Verzamelconcept-pattern" boven). `bedrijfsleidersbezoldiging`, `autokosten`, `loon-en-payroll`, `winstuitkering`, eventueel `werknemers-vergoedingen` zelf — allemaal verzamelconcepten met `[Σ]`-tag, verplicht: lijst leden + keuze-criteria + overkoepelende stof.
- **OP-W.5** ✅ **Al beslist** in rationale-log (entry 2026-05-23 `voordelen-alle-aard géén bundel — filter-categorie`): `verworpen-uitgaven` = filter-sectie in `fiscaliteit/vennootschapsbelasting`, geen bundel + geen verzamelconcept. Geen verdere actie. Cross-link vanuit ecocheques / geschenken / receptiekosten / autokosten / autokosten-VU-deel.

### Cross-cutting Gebeurtenissen — kapitaal- en reorganisatie-events

Te ontwikkelen. Vertrekpunt: bestaande records + Regel J + PO-anchor-cohort-anti-pattern (kapitaalverhoging + -vermindering blijven 2 records).

### Mobiliteit-cluster

Thema: `mobiliteit`. *(Herzien zonder juridisch/sociaal-zekerheid-perspectieven — verplaatst naar inhoud.)*

```
mobiliteit
├── autokosten                              [R]
├── mobiliteitsbudget                       [R]
│   ▸ pijler-1-milieuvriendelijke-wagen
│   ▸ pijler-2-duurzame-mobiliteit
│   ▸ pijler-3-cash-saldo
├── cash-for-car                            [R, status: uitdovend]
└── woon-werkverkeer-en-km-vergoeding       [R]
```

**Details per record**:

**`autokosten`** [R]
- inhoud: kosten van voertuig in beroeps-/vennootschaps-context (gekocht/geleased/eigen wagen + km-vergoeding); personenwagen + lichte vracht; out-of-scope = puur privé zonder beroepsgebruik
- perspectieven: `boekhouding` (kost-boeking 61x, afschrijving, brandstof, onderhoud, verzekering, BIV, verkeersbelasting) · `fiscaal-VenB` (verworpen uitgaven CO2-formule 40-100%; brandstof apart; lichte vracht apart) · `fiscaal-PB` (VAA-auto-formule cat × CO2 × leeftijd × 6/7 ⚠️) · `btw` (aftrek max 50%; drie methodes: semi-forfaitair / forfaitair / werkelijk via km-admin) · `advies` (keuze: bedrijfswagen vs mobiliteitsvergoeding vs mobiliteitsbudget vs eigen wagen + km-vergoeding)
- naam_officieel: — · synoniemen: wagenkost, voertuigkost, bedrijfswagen-kosten
- relaties: `mobiliteitsbudget`, `cash-for-car`, `woon-werkverkeer-en-km-vergoeding`, `vast-actief`

**`mobiliteitsbudget`** [R]
- inhoud: federale wet 17 maart 2019 ⚠️; werknemer geeft bedrijfswagen-recht op → jaarlijks budget = TCO van die wagen; bestedingsmodel in 3 pijlers (zie sub-secties); voorwaarden-toegang: anciënniteit werknemer + werkgever-toekenning ⚠️
- sub-secties: `#pijler-1-milieuvriendelijke-wagen` (kleinere/elektrische wagen onder CO2-norm — autokosten-regime + VAA blijft van toepassing) · `#pijler-2-duurzame-mobiliteit` (OV, fiets, deelauto, stapvergoeding, huur/hypotheek binnen 10 km — vrijgesteld) · `#pijler-3-cash-saldo` (restbedrag cash; bijzondere bijdrage 38,07% ⚠️; geen PB, geen RSZ-werknemer)
- perspectieven: `fiscaal-PB` (vrijstellings-/heffingsregime per pijler) · `boekhouding` (loonkost-vervanging) · `advies` (wanneer aantrekkelijk voor werkgever/werknemer; samenspel met cao)
- naam_officieel: mobiliteitsbudget · synoniemen: federaal mobiliteitsbudget
- relaties: `autokosten` (pijler 1), `cash-for-car` (alternatief)

**`cash-for-car`** [R, status: uitdovend ⚠️]
- inhoud: officieel "mobiliteitsvergoeding" — wet 30 maart 2018 ⚠️. Werknemer levert bedrijfswagen in → vast maandelijks cash-bedrag (formule ~ VAA-equivalent). Regeling vernietigd door Grondwettelijk Hof januari 2023 ⚠️ (arrest 23/2023); overgangsregime voor lopende vergoedingen.
- perspectieven: `fiscaal-PB` (heffingsregime gunstiger dan loon) · `advies` (historisch alternatief; in lopende dossiers nog relevant)
- naam_officieel: mobiliteitsvergoeding · synoniemen: cash for car, CfC
- relaties: `autokosten` (alternatief), `mobiliteitsbudget` (alternatief)

**`woon-werkverkeer-en-km-vergoeding`** [R]
- inhoud: verzamel-Regeling voor verplaatsings-vergoedingen die NIET via bedrijfswagen gaan; raakt werknemers + bedrijfsleiders + zelfstandigen; bevat sub-regelingen voor wagen-km, fiets-km, OV-tussenkomst
- perspectieven: `fiscaal-PB` (vrijstellingsgrenzen werknemer, forfaitair vs werkelijk; werkgevertussenkomst OV) · `fiscaal-VenB` (aftrekbaarheid werkgever; 120%-aftrek fiets ⚠️) · `advies` (fietsleasing, mobiliteitsplan)
- naam_officieel: — · synoniemen: woon-werkvergoeding, verplaatsingsvergoeding, fietsvergoeding, OV-tussenkomst
- relaties: `autokosten` (afbakening), `mobiliteitsbudget` (pijler 2 overlap)

**Open punten mobiliteit-cluster**:
- **OP-M.1** Status `cash-for-car` in programma 2026 — checken in `data/programma/programma.json`. Voorlopig behouden als `status: uitdovend`.
- **OP-M.2** `woon-werkverkeer-en-km-vergoeding` als één Regeling vs splitsen per vervoermiddel. Voorlopig één Regeling (gedeelde fiscale logica forfait/werkelijk).
- **OP-M.3** Sub-secties van `mobiliteitsbudget` (3 pijlers) — anchor of gewoon kern-sub-sectie? Regel F bedoelt anchors voor Entiteiten-in-bundel; hier zijn het pijler-niveaus binnen één Regeling. Voorlopig: noteren als sub-secties met `#`-anchor maar zonder bundel-status.

### Kapitaalstructuur-cluster

Thema: `kapitaalstructuur`. *Tree-skelet eerst, daarna details.*

```
kapitaalstructuur
├── oprichting-vennootschap                       [G+R]    ▸ oprichtingskosten
├── kapitaalverhoging                             [G+R]
│   └── kapitaalverhoging-in-natura               [G+R]    ▸ inbreng-onroerend
├── kapitaalvermindering                          [G+R]
├── inbreng-bedrijfstak-of-algemeenheid           [G+R]    (1 record; ook thema: reorganisatie)
├── quasi-inbreng                                 [R]      (ook thema: anti-misbruik)
├── inkoop-eigen-aandelen                         [G+R]    (bestaand record)
├── voorkeurrecht                                 [R]      (ook thema: aandeelhoudersbescherming)
├── volstortingsplicht                            [R]
├── aandeel                                       [E]
├── algemene-vergadering                          [E-orgaan]  (bestaand record)
├── aandeelhoudersovereenkomsten                  [E]      ▸ stand-still ▸ voorkooprecht ▸ exit ▸ board-vertegenwoordiging ▸ controle-verwerving
├── eigen-vermogen                                [E-bundel]
│   ▸ kapitaal ▸ uitgiftepremies ▸ herwaarderingsmeerwaarden
│   ▸ reserves ▸ overgedragen-resultaat ▸ kapitaalsubsidies(?)
├── financieel-plan                               [E]
└── kapitaalbescherming                           [K-principe ⏳]  (positionering TBD — OP-K.5)
```

**Details per record** (hints voor extractie; ⚠️ markers = te verifiëren bij claims_checken):

**`oprichting-vennootschap`** [G+R]
- inhoud: vennootschap-tot-stand-komen — keuze ondernemingsvorm + statutenopmaak + notariële akte (BV/NV/CV; eenmanszaak niet) + initiële inbreng (in geld of natura) + RPR-inschrijving + bestuursorgaan-aanstelling + btw-identificatie. Financieel plan verplicht bij BV/NV/CV.
- sub-sectie `#oprichtingskosten`: notariskosten, RPR, publicatiekosten, eerste boekhoudkundige verwerking → activeren als oprichtingskosten of direct ten laste (CBN-advies 2011/9 ⚠️); afschrijven over max 5 jaar
- perspectieven: `boekhouding` (openingsbalans + oprichtingskosten-activering/afschrijving) · `fiscaal-VenB` (registratie, eerste boekjaar, fiscaal gestort kapitaal vanaf dag 1) · `fiscaal-BTW` (btw-identificatie, regime keuze) · `advies` (vormkeuze, financieel-plan-opmaak, optimalisatie startkapitaal)
- relaties: `ondernemingsvormen` (E-bundel), `financieel-plan` (E), `kapitaalverhoging` (latere modaliteit), `quasi-inbreng` (anti-misbruik bij latere transacties)

**`kapitaalverhoging`** [G+R]
- inhoud: latere verhoging van het kapitaal — AV-besluit (gewone vs versterkte meerderheid afhankelijk vorm) + statutenwijziging + notariële akte; modaliteiten: in geld, in natura (zie child), incorporatie reserves, capitalisatie schuldvordering; mogelijkheid van toegestaan kapitaal (machtiging aan bestuur)
- perspectieven: `boekhouding` (rekeningen 10/11/12; uitgiftepremie) · `fiscaal-VenB` (impact op fiscaal gestort kapitaal; geen winstrealisatie) · `audit` (revisor-verslag bij inbreng-in-natura) · `advies` (timing, modaliteit-keuze, voorkeurrecht-strategie, kapitaalreductie nadien)
- relaties: `kapitaalvermindering` (tegenhanger), `voorkeurrecht` (R), `volstortingsplicht` (R), `quasi-inbreng` (anti-misbruik), `eigen-vermogen#kapitaal`, `aandeel`

**`kapitaalverhoging-in-natura`** [G+R, child van kapitaalverhoging]
- inhoud: kapitaalverhoging waarbij inbreng = niet-geld (goederen, vorderingen, aandelen); revisor-verslag verplicht (BV/NV); evaluatie-methodes; risico overwaardering; latente meerwaarden fiscaal gerealiseerd bij inbreng vanuit eigen patrimonium
- sub-sectie `#inbreng-onroerend`: inbreng van onroerend goed — registratierechten 0% bij inbreng tegen aandelen (vrijstelling art 115bis Wb Reg ⚠️ — natuurlijke persoon naar vennootschap; gemengde betaling = pro-rata); btw-impact bij nieuw gebouw; revisor-evaluatie methodologisch zwaarder
- perspectieven: `audit` (revisor-evaluatie, methodologie) · `fiscaal-VenB` (meerwaarde-realisatie regels) · `fiscaal-PB` (impact inbrenger) · `registratie` (115bis-vrijstelling onroerend) · `advies` (wanneer aantrekkelijk; valkuilen — bv woning-inbreng-controverse)
- relaties: `kapitaalverhoging` (parent), `quasi-inbreng` (sterk verwant — quasi-inbreng is anti-misbruik tegen verkapte natura-inbreng)

**`kapitaalvermindering`** [G+R]
- inhoud: vermindering van het kapitaal — AV-besluit + statutenwijziging + wachttermijn 2 maanden voor schuldeisers (verzetsrecht); modaliteiten: terugbetaling kapitaal, aanzuivering verlies, vrijstelling volstortingsplicht. **Bevat pro-rata-toerekening** (sinds wet 25 dec 2017 ⚠️): bedrag pro rata toegerekend aan gestort kapitaal én aan reserves; reserve-deel belast als dividend (RV).
- perspectieven: `boekhouding` (debetboeking 10; impact reserves) · `fiscaal-VenB` (pro-rata-herkwalificatie; RV op reserve-deel) · `audit` (revisor-verslag bij aanzuivering verlies) · `advies` (optimale modaliteit; alarmbel-link bij vermindering door verlies)
- relaties: `kapitaalverhoging` (tegenhanger), `alarmbel-procedure` (trigger), `dividend-uitkering` (herkwalificatie)

**`inbreng-bedrijfstak-of-algemeenheid`** [G+R, primair thema: reorganisatie] — 1 record (triangulatie 2026-05-24 bevestigd door bestaand record `inbreng-van-bedrijfstak-of-algemeenheid.json`)
- inhoud: 2 verwante modaliteiten in 1 record. **Inbreng-bedrijfstak**: zelfstandig functionerend onderdeel van een vennootschap in een andere vennootschap, tegen uitgifte van aandelen. **Inbreng-algemeenheid**: volledige vermogen van een vennootschap in een andere vennootschap (variant — volledig ipv onderdeel). Gedeelde fiscaal-neutraliteits-regime (geen meerwaarde-realisatie mits voorwaarden), btw-vrijstelling (overdracht algemeenheid art 11/18 Wbtw ⚠️), registratierechten-vrijstelling.
- sub-secties: `#inbreng-bedrijfstak` (onderdeel) · `#inbreng-algemeenheid` (volledig) — verschillen in voorwaarden + scope
- perspectieven: `fiscaal-VenB` (neutraliteits-voorwaarden, latere realisatie) · `fiscaal-BTW` (overdracht-algemeenheid-regime — zie `overdracht-algemeenheid-btw.json` bestaand) · `audit` (revisor-verslag op de inbreng) · `advies` (reorganisatie-planning)
- naam_officieel: inbreng van bedrijfstak; inbreng van algemeenheid · synoniemen: TOGS, transfer of going concern, partial demerger by contribution
- relaties: `fusie`, `splitsing`, `kapitaalverhoging` (modaliteit van), `overdracht-algemeenheid-btw` (BTW-perspectief)

**`quasi-inbreng`** [R]
- inhoud: aankoop binnen 2 jaar na oprichting van een actief > 10% van het kapitaal van oprichter/zaakvoerder/bestuurder = behandeld als verkapte inbreng-in-natura → revisor-verslag + AV-toestemming verplicht (BV/NV). Anti-misbruik tegen ontwijken van inbreng-revisor-controle.
- perspectieven: `audit` (revisor-verslag) · `advies` (transactie-planning bij jonge vennootschap)
- relaties: `oprichting-vennootschap`, `kapitaalverhoging-in-natura`

**`inkoop-eigen-aandelen`** [G+R] — bestaand record (PO 3.0.IV.C)
- inhoud: vennootschap koopt haar eigen aandelen terug van aandeelhouders — AV-toestemming (versterkte meerderheid), max-grens (20% van uitstaand kapitaal ⚠️ NV; BV anders), netto-actief-test + uitkeringstest (BV) ⚠️, ingekochte aandelen → reserve onbeschikbaar of vernietiging. Fiscale herkwalificatie als dividend mogelijk bij niet-naleving voorwaarden ⚠️.
- perspectieven: `boekhouding` (rekening 12-eigen-aandelen, onbeschikbare reserve) · `fiscaal-VenB` (mogelijk RV als dividend bij niet-naleving) · `audit` (controle voorwaarden, netto-actief-test) · `advies` (gebruik als exit-mechanisme aandeelhouders; alternatief voor dividend)
- naam_officieel: inkoop van eigen aandelen · synoniemen: terugkoop eigen aandelen, share buyback
- relaties: `eigen-aandelen` (E — aandelen in portefeuille als balanspositie), `kapitaalbescherming` (netto-actief-test), `dividend-uitkering` (alternatief; herkwalificatie-risico), `aandeel`

**`algemene-vergadering`** [E-orgaan] — bestaand record (PO 3.0.III)
- inhoud: orgaan van de vennootschap dat samengesteld is uit de aandeelhouders; bevoegdheden (statutenwijziging, winstbestemming, bestuurder-benoeming, kwijting, ontbinding); soorten (gewone vs bijzondere/buitengewone); bijeenroeping + agenda + meerderheidsregels; aanwezigheid (advocaat, gecertificeerd accountant — PO 3.0.III.B); volmachten (PO 3.0.III.C).
- perspectieven: `vennootschapsrecht`-inhoud van het orgaan (procedure-aspecten) · `audit` (notulen-verificatie, kwijting-implicaties) · `advies` (statutaire bijzondere meerderheden, schriftelijke besluiten)
- naam_officieel: algemene vergadering van aandeelhouders · synoniemen: AVA, AV, shareholders' meeting
- relaties: `kapitaalverhoging`, `kapitaalvermindering`, `winstbestemming`, `aandeelhoudersovereenkomsten`, `bestuurdersaansprakelijkheid` (kwijting)

**`aandeelhoudersovereenkomsten`** [E] (PO 3.0.VI + 4 sub-anchors VI.A-D)
- inhoud: contractuele overeenkomsten tussen aandeelhouders (niet statutair) over uitoefening van hun rechten — controle, exit, beslissingsstructuur. Vrij van vormvereisten maar onderworpen aan WVV-bepalingen en gemeenrecht. Bindt alleen ondertekenaars (niet de vennootschap, tenzij statutair verankerd).
- sub-secties: `#stand-stillclausule` (overdracht-beperking gedurende termijn) · `#voorkooprecht` (right of first refusal) · `#exit-clausule` (drag-along / tag-along / put-call) · `#board-vertegenwoordiging` (waarborg zetels in raad van bestuur) · `#controle-verwerving` (stemgedrag-coördinatie, syndicaatsovereenkomst)
- perspectieven: `advies` (opstellen, evenwicht zoeken, anticipatie conflicten) · `vennootschapsrecht`-inhoud (afdwingbaarheid, sanctie bij schending) · `audit` (kennisname bij due diligence + bij audit van controle-relaties)
- naam_officieel: aandeelhoudersovereenkomst · synoniemen: shareholders agreement, SHA, syndicaatsovereenkomst, aandeelhouderspact
- relaties: `aandeel`, `algemene-vergadering`, `overnameovereenkomst-spa` (raakvlak), `overdracht-onderneming`

**`voorkeurrecht`** [R]
- inhoud: bij kapitaalverhoging in geld hebben bestaande aandeelhouders preferent inschrijvingsrecht (anti-verwatering); termijn voor uitoefening; afschaffing mogelijk door AV onder voorwaarden (rapport bestuur + commissaris); overdraagbaarheid van het recht.
- perspectieven: `audit` (controle naleving bij verhoging) · `advies` (afschaffing-strategie; impact op aandeelhouders-coalities)
- relaties: `kapitaalverhoging`, `aandeel`

**`volstortingsplicht`** [R]
- inhoud: aandeelhouder is verplicht zijn toegezegde inbreng effectief te volstorten; timing afhankelijk van vorm (BV: vrij door statuten; NV: minimum 25% gestort bij inschrijving); opvraagbaarheid door bestuur; sanctie bij niet-volstorting (intrest, verlies stemrecht, gedwongen verkoop aandelen)
- perspectieven: `boekhouding` (opvraagbaar kapitaal rekening 101) · `audit` (controle solvabiliteit) · `advies` (statutaire opvraag-clausule, niet-volstorte aandelen overdracht)
- relaties: `aandeel`, `kapitaalverhoging`, `oprichting-vennootschap`

**`aandeel`** [E]
- inhoud: deelbewijs in het kapitaal van een vennootschap; categorieën (gewone, preferente, met meervoudig stemrecht, zonder stemrecht); overdraagbaarheid (vrij vs beperkt afhankelijk vorm); aandeelhoudersregister; opbrengsten (dividend) en plichten (volstorting); waarde-aspecten (nominale waarde, fractiewaarde, marktwaarde)
- sub-sectie `aandeelhouders-rechten-en-plichten` (overzicht naar Regelingen: voorkeurrecht, volstortingsplicht, stemrecht, dividend-recht)
- perspectieven: `boekhouding` (waardering bij houder; deelnemingen) · `fiscaal-VenB` (DBI, meerwaarden, RV) · `fiscaal-PB` (RV op dividend; meerwaarden privé-vermogen) · `audit` (aandeelhoudersregister-controle) · `advies` (overdrachtsplanning, successie)
- relaties: `eigen-vermogen#kapitaal`, `dividend-uitkering`, `voorkeurrecht`, `volstortingsplicht`, `kapitaalverhoging`

**`eigen-vermogen`** [E-bundel]
- inhoud: balans-zijde van de financiering — som van componenten op rekeningen 10-15; samenhang van componenten bepaalt solvabiliteit; toename via inbreng + winstreservering; afname via vermindering + uitkering + verlies
- anchors: `#kapitaal` · `#uitgiftepremies` · `#herwaarderingsmeerwaarden` · `#reserves` · `#overgedragen-resultaat` · `#kapitaalsubsidies` (zie OP-K.3)
- perspectieven: `boekhouding` (jaarrekening-presentatie, reserveringsstroom) · `fiscaal-VenB` (fiscaal eigen vermogen vs boekhoudkundig; NIA-grondslag historisch) · `audit` (samenhang met resultaat, hervorming statuten) · `advies` (kapitaalstructuur-optimalisatie, alarmbel-prognose)
- relaties: `kapitaalverhoging`, `kapitaalvermindering`, `dividend-uitkering`, `alarmbel-procedure`, `winstbestemming`

**`financieel-plan`** [E]
- inhoud: document met prognose van middelen + behoeften over min. 2 jaar (BV) of 3 jaar (CV); verplicht bij oprichting BV/NV/CV; in bewaring bij notaris; gebruikt om aansprakelijkheid oprichter te beoordelen als vennootschap binnen 3 jaar failliet gaat met kennelijk ontoereikend startvermogen (oprichtersaansprakelijkheid)
- perspectieven: `advies` (opmaak, realisme-toets, scenario's) · `audit` (consistency-check met openingsbalans)
- relaties: `oprichting-vennootschap`, `bestuurdersaansprakelijkheid` (cross-cluster)

**`kapitaalbescherming`** [K-principe ⏳ — positionering TBD, OP-K.5]
- inhoud: systeem-concept dat alle vermogensonttrekkings-mechanismen beheerst — **netto-actief-test** (art 5:142 BV / 7:212 NV ⚠️: netto-actief na uitkering ≥ kapitaal + onbeschikbare reserves) + **uitkeringstest** (liquiditeit min. 12 maanden, BV alleen ⚠️) + **schuldeiserbescherming** (wachttermijn 2 maand bij kapitaalvermindering) + **alarmbel-koppeling** (bij netto-actief < helft kapitaal). Vervangt bestaand `kapitaalbescherming-en-winstverdeling.json` (winstverdeling-deel migreert naar winstuitkering-cluster).
- perspectieven: `vennootschapsrecht`-inhoud (juridische ratio) · `audit` (controle test-uitkomsten) · `boekhouding` (berekeningsgrondslag) · `advies` (uitkering-mogelijkheid screenen)
- naam_officieel: kapitaalbescherming · synoniemen: vermogensbescherming, netto-actief-test, dubbele-test, uitkeringsbeperking
- relaties: `kapitaalvermindering`, `inkoop-eigen-aandelen`, `dividend-uitkering`, `tussentijdse-dividenden`, `alarmbel-procedure`, `quasi-inbreng`

**Open punten kapitaalstructuur-cluster**:
- **OP-K.1** ✅ **Beslist door triangulatie**: `inbreng-bedrijfstak-of-algemeenheid` = 1 record (bestaand record bevestigt). 2 sub-secties voor de verschillen.
- **OP-K.2** `aandeelhouders-rechten-en-plichten` als sub-sectie van `aandeel` (filter-categorie, geen bundel) — bevestigen.
- **OP-K.3** `kapitaalsubsidies` als anchor in `eigen-vermogen`-bundel OF apart Regeling-record (eigen mechaniek: opname winstresultaat over tijd parallel aan afschrijving subsidie-object). Te valideren.
- **OP-K.4** `winstbestemming` (wettelijke reserve, vrije reserves, overdracht, dividend) — eigen Gebeurtenis-record of perspectief binnen `eigen-vermogen`? Volgt in winstuitkering-cluster.
- **OP-K.5** ⏳ **Open (TBD)**: `kapitaalbescherming` [K-principe] positionering — past in `kapitaalstructuur`-cluster (omdat het de mechanismen daar bindt) of in `vennootschapsrecht`-discipline (omdat het een Kader-principe is)? Voorlopig in kapitaalstructuur opgenomen pending user-beslissing.
- **OP-K.6** ⏳ **Open (TBD)**: `meerwaarde-aandelen-venb` als perspectief van `aandeel` (fiscaal-VenB) OF eigen Regeling-record (eigen mechaniek: vrijstellingsvoorwaarden + houdperiode + onderworpenheid). Bestaand record `meerwaarde-aandelen-venb.json` suggereert eigen record; te valideren.

**Triangulatie-resultaten kapitaalstructuur** (2026-05-24):
- 5 records aligned met bestaande (kapitaalverhoging, -vermindering, oprichting, quasi-inbreng, eigen-vermogen)
- 4 records toegevoegd na triangulatie: `inkoop-eigen-aandelen` (bestaand, PO 3.0.IV.C), `algemene-vergadering` (bestaand, PO 3.0.III), `aandeelhoudersovereenkomsten` (nieuw, PO 3.0.VI), `kapitaalbescherming` (herpositionering bestaand)
- 3 verschoven naar andere clusters: `obligatielening` → schuldfinanciering · `overdracht-onderneming` → eigen cluster · `tussentijdse-dividenden` → winstuitkering
- 2 absorbed: `oprichtingskosten` → sub-sectie van `oprichting-vennootschap` · `inbreng-onroerend` → sub-sectie van `kapitaalverhoging-in-natura`

---

## Test-cases (per laag-2-uitwerking)

Concrete fenomenen die de structuur moeten kunnen dragen zonder geforceerd te worden:

- **autokosten** (cross-dimensie Regeling: boekhouding + VenB-verworpen + BTW + voordeel-alle-aard + advies)
- **dividend-uitkering** (cross-cutting Gebeurtenis: vennootschapsrecht + VenB + PB + boekhouding)
- **kapitaalverhoging / kapitaalvermindering** (2 aparte Gebeurtenissen met eigen Regeling-aspect, ondanks gedeelde PO-anchor)
- **dbi-aftrek** (VenB-Regeling met meerdere voorwaarden-clusters)
- **leasing** (Entiteit met divergente Regelingen — al opgelost in iter. 2 stress-test: Entiteit-record + apart kwalificatie-Regeling-record voor BE-GAAP/IFRS)
- **ondernemingsvormen** (Entiteit-bundel met BV/NV/CommV/CV/SE/eenmanszaak-anchors)
- **eigen-vermogen** (Entiteit-bundel — samenhang-criterium)
- **consolidatiekring** (Entiteit met inclusie-Regeling-aspect)
- **fusie / splitsing** (Gebeurtenissen met fiscaal-neutraliteits-Regelingen)
- **alarmbel-procedure** (Regeling onder vennootschapsrecht, met perspectieven naar bestuurdersaansprakelijkheid + audit)

---

## Rationale-log (chronologisch)

| Datum | Beslissing | Verworpen alternatief | Reden | Analoge gevallen |
|---|---|---|---|---|
| 2026-05-23 | `Kader` blijft umbrella-naam; `discipline` is sub-type voor top-laag | `Discipline` als super-categorie-naam | Niet elke Kader-knoop is een discipline — `consolidatie-techniek` (techniek), `getrouw-beeld-principe` (principe) zijn ook Kaders. Eén umbrella + sub-types houdt schema simpel én laat juiste woord per record toe. | Synoniemen-tabel voor de 3 andere super-categorieën volgens dezelfde logica. |
| 2026-05-23 | `fiscaliteit` met sub-tree | `personenbelasting`/`vennootschapsbelasting`/`btw` als platte top-disciplines | Cross-fiscale principes (rechtsgrondslag, gerechtelijke procedure) leven in parent-Kader. Wordt geverifieerd in laag-2. | Idem voor `audit-en-assurance` met sub-Kaders per opdrachttype. |
| 2026-05-23 | `vennootschapsrecht` top-discipline (geen `juridisch` parent) | `juridisch` parent met `vennootschapsrecht`/`insolventierecht`/`arbeidsrecht` als sub-Kaders | Andere juridische topics zijn perifeer in examenscope. Te herzien als laag-2 anders aantoont. | — |
| 2026-05-23 | Entiteiten + Gebeurtenissen cross-cutting (eigen stammen) | Onder discipline ophangen | Eén Entiteit/Gebeurtenis leeft tegelijk in meerdere disciplines (Regel J — aandeel: VR + B + F + A). Perspectieven verwijzen via `accountant_perspectieven[]`. | Cross-Regelingen volgen dezelfde logica (witwasplicht). |
| 2026-05-23 | AML voorlopig cross-Regeling, niet onder `beroep-en-deontologie` | Sub-Kader onder `beroep-en-deontologie` | Raakt alle opdrachttypes + boekhouding + deontologie — Regel J. | Te bevestigen bij laag-2. |
| 2026-05-23 | `autokosten` als hoofd-naam (niet `bedrijfswagenkosten` of `bedrijfsvoertuig-en-autokosten`) | `bedrijfswagenkosten` (preciezer) | Accountant-spraakgebruik. Scoping (privé/zaak, bedrijfswagen/eigen wagen) staat in record-definitie en boekhouding-perspectief, niet in naam. | `dividend-uitkering` (niet `dividend-vennootschap-aan-aandeelhouder`), `kapitaalverhoging` (niet `kapitaalverhoging-vennootschap`). |
| 2026-05-23 | `mobiliteitsbudget` en `cash-for-car` als eigen Regeling-records, niet als sub-anchors van `autokosten` | Sub-anchors `autokosten#mobiliteitsbudget` etc. | Elk regime heeft eigen wettekst en eigen voorwaarden (anciënniteit, plafonds, pijlers); ze zijn alternatieven, geen sub-instanties. Keuze-afweging woont in `autokosten`-perspectief `advies`. | `bedrijfsleidersbezoldiging` vs `dividend-uitkering` als alternatieven (bedrijfsleider-vergoeding) — beide eigen records. |
| 2026-05-23 | `voordelen-alle-aard` géén bundel — filter-categorie | Bundel met `#vaa-auto`, `#vaa-woning`, `#vaa-pc`, `#vaa-lening` | VAA-formules zijn fenomeen-specifiek (geen samenhang of keuze). VAA-overzicht woont als sectie in `fiscaliteit/personenbelasting`. Elk fenomeen blijft eigen Regeling met VAA als één van de perspectieven. Regel I anti-pattern (filter-categorie) + Regel J (één fenomeen × alle dimensies). | `verworpen-uitgaven` analoog (autokosten + receptie + geschenken = elk eigen fenomeen-Regeling met VenB-perspectief). |
| 2026-05-23 | Alle Regelingen leven cross-cutting (geen Regelingen onder een discipline-Kader hangen) | "Cross-Regelingen" als aparte categorie naast "discipline-eigen Regelingen" | Onderscheid is willekeurig: bijna elke Regeling heeft via Regel J meerdere discipline-perspectieven (DBI = VenB + boekhouding + advies). Discipline-binding gebeurt via `accountant_perspectieven[]` en `relaties[]`, niet via tree-positie. | Idem voor Entiteiten + Gebeurtenissen (al cross-cutting). |
| 2026-05-23 | Thema-tagging als orthogonaal mechanisme (`thema: []`) | Tree-clustering forceren ("mobiliteit-cluster" als tree-knoop) | Thema's snijden door categorie-stammen heen (mobiliteit raakt Regelingen + Gebeurtenissen + Entiteiten); tree-positie blijft één-op-één per record; thema's bieden orthogonale view. | `werknemers-vergoedingen`, `fiscale-voordelen-vennootschap`, `anti-misbruik`, `bestuurdersaansprakelijkheid`. |
| 2026-05-23 | `naam_officieel` + `synoniemen[]` als record-velden; record-id blijft praktijk-accountantsterm | Officiële naam als record-id forceren | Stagiairs en accountants zoeken op praktijkterm; wettekst-term moet wel als alias gevonden worden. Record-id stabiel, aliassen voor zoek+RAG+LLM-extractie. | `cash-for-car` (id) = "mobiliteitsvergoeding" (officieel); `autokosten` zonder één officiële naam; later: `dbi-aftrek` (id) = "aftrek voor definitief belaste inkomsten" (officieel). |
| 2026-05-23 | `categorie: []` als **lijst** in schema | Eén `categorie`-waarde + de andere als "ook"-veld | Hybride records (E+R+G zoals `afschrijving`, `kapitaalverhoging`) zijn vindbaar via elk van hun identiteiten zonder kunstmatige primary-keuze. Naam volgt accountant-spraak, niet "primaire categorie". Schema-update later via ADR-030-revisie of mini-ADR. | `afschrijving`=[E,G,R]; `kapitaalverhoging`=[G,R]; `oprichting-vennootschap`=[G,R]; `eigen-vermogen`=[E] (puur). |
| 2026-05-23 | Scherpe lijn **inhoud** (wat het IS) vs **`accountant_perspectieven[]`** (wat accountant DOET). `juridisch` / `vennootschapsrecht` / `notarieel` / `civielrechtelijk` zijn GEEN perspectieven. | Pseudo-perspectief `juridisch` voor wettelijke verankering + formaliteiten | Notariële akte bij BV-oprichting is een eigenschap van de gebeurtenis, geen werk van de accountant. Door dit naar `inhoud` te trekken worden records slanker en wordt `accountant_perspectieven[]` echt een werk-checklist. Legitiem zijn: boekhouding · fiscaal-PB/VenB/btw/registratie · audit · advies · beroep-en-deontologie. | Pijler-1/2/3-info bij `mobiliteitsbudget`: regelgeving in inhoud, niet als pseudo-perspectief "sociaal-zekerheid"; aandeelhoudersregister-bestaan = inhoud van `aandeel`, audit-controle = perspectief. |
| 2026-05-23 | `pro-rata-toerekening` bij kapitaalvermindering = sub-aspect in `kapitaalvermindering`, **geen eigen record** | Eigen Regeling-record `pro-rata-toerekening-kapitaalvermindering` of `terugbetaling-kapitaal-vs-dividend` | Pro-rata is een toerekenings-mechanisme dat alleen bij kapitaalvermindering bestaat — Regel J (geïntegreerde Regeling: één fenomeen × N dimensies = één record met meerdere perspectieven). Vermijdt smell-naam met `vs`. | `alarmbel-trigger` bij `kapitaalvermindering` (link, geen apart record); `revisor-verslag-vereiste` bij `kapitaalverhoging-in-natura` (inhoud-aspect, niet eigen Regeling). |
| 2026-05-23 | `vs` in een record-naam = **smell** (twee dingen tegelijk) | `terugbetaling-kapitaal-vs-dividend`, `huur-vs-leasing` | Naam met `vs` betekent ofwel één fenomeen-met-toerekeningsregel (→ inhoud van de overkoepelende Regeling) ofwel twee aparte concepten met onderlinge relatie (→ 2 records + `relaties[]`). Nooit één record. Te integreren in ADR-030 §Naamgeving (Regel-naam-`vs`-anti-pattern). | Toekomstige sparring: kandidaat-smells zoeken in mapping-fase. |
| 2026-05-23 | `financieel-plan` is **Entiteit** (instrument), niet Regeling | `financieel-plan-vereiste` als Regeling | Wettelijke verankering ≠ Regeling. Het plan is een document-instrument; de oprichtersaansprakelijkheid bij ontoereikend plan is een eigenschap van de oprichting (`inhoud` van `oprichting-vennootschap`) + relatie naar `bestuurdersaansprakelijkheid`. Meta-regel: kijk naar het *ding zelf*, niet naar de wet eromheen. | `aandeelhoudersregister` = Entiteit (niet "register-houdingsplicht" als Regeling); `commissarisverslag` = Entiteit (niet "verslagverplichting" als Regeling). |
| 2026-05-23 | Tree-nesting binnen dezelfde stam toegelaten (skelet-doc), schema blijft plat (`relaties[]`) | Geneste records ook in schema via `parent`-veld | Tree-nesting is lees/extractie-hulp voor mensen; schema-flat houdt records onafhankelijk en queryable. Hiërarchie wordt uitgedrukt in `relaties[].soort: specialisatie-van` of `is-onderdeel-van`. | `kapitaalverhoging-in-natura` onder `kapitaalverhoging` (skelet) → in schema relatie `specialisatie-van`. |
| 2026-05-23 | Compact-tree-first + details-na format voor skelet-doc | Proza-doorlopend per record | User-feedback: "ik wil daar vooral graag 'de tree' inspecteren, niet door alle proza gaan". Cluster begint met ASCII-tree (categorie-tags `[R]`/`[G+R]`/`[E]`/`[E-bundel]` + ▸ anchors), gevolgd door details-per-record (inhoud / perspectieven / naam_officieel / synoniemen / relaties). Sub-concepten en anchors al expliciet in tree als extractie-hints. | Toegepast op mobiliteit + kapitaalstructuur; standaard voor alle volgende clusters. |
| 2026-05-24 | **Verzamelconcept-pattern** (`[Σ]`) formeel ingevoerd: een record dat primair een lijst + keuzekader/vergelijking is voor een familie van alternatieven, met overkoepelende stof | Alleen losse Regelingen + perspectief `advies` op elk record (geen overkoepelend record) | Stagiair heeft "welke modaliteit kies ik?"-houvast nodig; 45.000-EUR-regel + bezoldigingstheorie (in bedrijfsleidersbezoldiging) hebben geen ander thuis. Onderscheid met bundel (= samenhang-Entiteiten, `#anchor`-sub-records) en filter-categorie (= geen overkoepelende stof, zoals verworpen-uitgaven). Schema-formalisatie via `is_verzamelconcept: true` (later via ADR-update). | `bedrijfsleidersbezoldiging` · `autokosten` · `loon-en-payroll` (⏳) · `winstuitkering` (⏳). Eventueel ook cluster-niveau `werknemers-vergoedingen` zelf. |
| 2026-05-24 | Compact top-level snapshot = één lijn per concept, sub-concepten/anchors op dezelfde lijn ernaast | Multi-line blok per cluster met record-namen op aparte lijnen zonder structuur | User-feedback: "kan je één lijntje per concept houden (en daarnaast misschien een oplijsten van zijn subconcepten?)". Snapshot moet record-niveau inspecteerbaar zijn, niet alleen cluster-niveau. | Standaard voor alle volgende cluster-toevoegingen aan snapshot. |
| 2026-05-24 | `loon-en-payroll` = verzamelconcept-record + alle componenten als aparte Regelingen | Eén mega-record `loon-werknemer` met componenten als sub-secties | Elke component heeft eigen wettekst + eigen tarief-tabel + eigen toepassingsvoorwaarden (Regel C: vindbaarheid + focused content). Verzamelconcept-pattern bewaart het overzicht zonder samenklontering. | `bedrijfsleidersbezoldiging` (Σ) + losse records voor bouwblokken (al toegepast); `autokosten` (Σ) + losse records voor mobiliteitsbudget/cash-for-car (al toegepast). |
| 2026-05-24 | `tantième` primair thema = `winstuitkering` (woont in winstbestemmings-volgorde); secundair in werknemers-vergoedingen-lijst | Primair `werknemers-vergoedingen` (omdat het een persoonsvergoeding is) | Praktijk: tantième leeft in AV-winstbestemming-flow; meest gebruikt voor zaakvoerders; aftrekbaarheidsregel hoort bij winstbestemming-mechaniek. Wordt als lid opgelijst in `bedrijfsleidersbezoldiging`-Σ + cluster `werknemers-vergoedingen`-Σ. | Toekomstig analoog: een record kan in meerdere Σ-lijsten verschijnen zonder zijn primair-cluster te verlaten. |
| 2026-05-24 | Onderscheid **Σ (verzamelconcept)** vs **K-techniek**: Σ = "welke kies ik" (advies, vergelijkingsmatrix), K-techniek = "hoe doe ik dit deterministisch" (procesflow zonder keuze) | Eén Σ-type voor zowel keuze-clusters als procesflows | Loonfiche-berekening is geen keuze (BV/RSZ/netto = dwingend); zou onterecht als Σ gelabeld worden. Onderscheid maakt schema-tags eerlijker en stuurt latere render-laag (Σ-record krijgt vergelijkingsmatrix-template; K-techniek krijgt stappenplan-template). | `loon-en-payroll` = K-techniek; `werknemers-vergoedingen` = Σ (parallel, niet hiërarchisch). Toekomst: andere K-techniek-kandidaten in `boekhouding` (waarderingsregels-toepassing), `audit` (risicogerichte-aanpak), `fiscaliteit` (aangifte-VenB-opmaak). |
| 2026-05-24 | `werknemers-vergoedingen` als eigen cluster-record (R, Σ) — naast cluster-tag/thema | Alleen cluster-tag + thema, geen overkoepelend record | Genuinely overkoepelende stof bestaat (afbakeningsvraag "wanneer is iets loon?" + cash-vs-cheque-vs-VAA-vergelijkingsmatrix) die nergens anders thuishoort. Drie geneste Σ's (cluster-Σ + bedrijfsleidersbezoldiging-Σ + autokosten-Σ in mobiliteit) beantwoorden drie verschillende vragen — geen overlap, geen dubbele content. | Toekomst: niet elk cluster krijgt een Σ-record; alleen als overkoepelende advies-stof bestaat die geen ander thuis heeft. Test: probeer de overkoepelende stof in een individueel lid te plaatsen — als dat niet natuurlijk lukt, is een Σ-record gerechtvaardigd. |
| 2026-05-24 | **Triangulatie-discipline** vóór elke cluster: PO-anchors-check + records+candidates-check + gap-analyse (aligned · skelet-only · PO-only) | Direct uitvinden zonder check tegen ground-truth | Tot nu primair "ik weet dat dit bestaat, dus bouw ik het" → risico op gemiste topics (PO vereist, skelet voorziet niet) en overontwikkeling (marginale topics). Triangulatie kost 5-10 min via MCP-tools `zoek_kandidaten` / `zoek_concepten` + Read `anchors.json`. Per cluster één triangulatie-blok bovenaan voor traceability. | Standaard vanaf nu. Retro-triangulatie op mobiliteit + kapitaalstructuur + werknemers-vergoedingen volgt vóór nieuwe cluster. |
| 2026-05-24 | `vs` in record-naam blijft smell (zie eerdere entry); `en` ook smell — wijst op chapter-heading-bundeling | `overname-handelsfonds-vs-aandelen` als naam; `kapitaalbescherming-en-winstverdeling` als 1 record | `vs` = vergelijking → Σ-record met modaliteit-secties (`overdracht-onderneming` met share-deal/asset-deal sub-secties). `en` = PO-chapter-heading-overerving → split per coherent sub-thema (`kapitaalbescherming` als K-principe; winstverdeling → eigen winstuitkering-cluster). | Toekomst: scan alle bestaande records op `-vs-` en `-en-` patronen tijdens mapping-fase. |
| 2026-05-24 | Triangulatie-resultaten kapitaalstructuur leidt tot 3 cluster-verschuivingen (`obligatielening` → schuldfinanciering, `overdracht-onderneming` → eigen cluster, `tussentijdse-dividenden` → winstuitkering) + 2 absorptions (`oprichtingskosten` in oprichting, `inbreng-onroerend` in -in-natura) | Alle items dwingen in 1 kapitaalstructuur-cluster | "Niet versplinteren maar ook niet over-bundelen": items met eigen logica + andere thuiscontext gaan naar eigen cluster (obligatielening = financierings-perspectief, niet kapitaal-perspectief); items zonder eigen overkoepelende stof worden sub-sectie van een groter record (oprichtingskosten = boekhoud-aspect van oprichting, geen advies-keuze). | Toepasbaar voor toekomst: 4-stappentest per record-kandidaat — (1) eigen wettekst/PO-anchor? (2) eigen overkoepelende stof? (3) gedeelde scope met ander cluster? (4) zou een Σ-vergelijkingsmatrix de "vs"/"en" vervangen? |
| 2026-05-24 | `overdracht-onderneming` als 1 Σ-record met share-deal + asset-deal als sub-secties | 2 aparte records `share-deal-aandelenovername` + `asset-deal-handelsfonds-overname` | PO 3.0.V.B vraagt expliciet het *verschil* — de vergelijkingsmatrix is de kern. User-keuze "niet versplinteren". Voldoende overkoepelende stof (waardering, due diligence, garanties, personeels-overdracht CAO 32bis) die in beide gedeeld is. | Analoog: `autokosten`-Σ met eigen-wagen/bedrijfswagen/leasing/km-vergoeding modaliteiten. |
| 2026-05-24 | `kapitaalbescherming` als K-principe-record (zonder `-en-winstverdeling`); winstverdeling-aspect migreert naar winstuitkering-cluster | Bestaand `kapitaalbescherming-en-winstverdeling.json` behouden zoals het is | "En"-smell wijst op PO-chapter-heading-overerving (PO 3.0.IV is een chapter). Splitsen op coherent sub-thema: kapitaalbescherming = systeem-principe (netto-actief-test + uitkeringstest + schuldeisersbescherming); winstverdeling = eigen Σ-cluster. | Mapping-actie: bestaand record hernoemen + scope inkrimpen tijdens fase 5 (mapping 396 records op skelet). |
