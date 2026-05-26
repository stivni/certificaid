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
controle                                 [K]   *hernoemd van `audit-en-assurance` 2026-05-26 (omvat zowel externe als interne controle)*
├── controle-opdracht                    [K]   ✅ uitgewerkt
├── beoordelings-opdracht                [K]
├── isae-opdrachten                      [K]
├── overeengekomen-procedures            [K]
├── interne-controle                     [K]   ✅ uitgewerkt
├── bijzondere-mandaten                  [K]   ✅ uitgewerkt   *shared thema beroepsbeoefening — wettelijke voorbehouden opdrachten per WVV-verrichting*
└── *Overige sub-Kaders compact uitgewerkt:* beoordelings-opdracht (ISRE 2400) · isae-opdrachten (ISAE 3000-serie) · overeengekomen-procedures (ISRS 4400) — telkens 1 mini-record + cross naar `opdracht-types`-Σ in controle-opdracht-cluster
vennootschapsrecht                       [K]
beroep-en-deontologie                    [K]
bedrijfseconomie-en-management           [K]
```

**Uitgewerkte clusters**

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
    └── outplacementkost                 [R, ⏳ NIEUW]      werkgever-verplichting bij collectief ontslag + 45+


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

reorganisatie                            [Σ-cluster, 4 records — cross PO 3.0.taak.2/3 + 2.3.III.B + 2.8.XVI + 1.4]
├── reorganisatie                        [R, Σ]              keuzekader · vergelijkingsmatrix · WVV boek 12 + fiscale-neutraliteit
├── fusie                                [G+R]               3 modaliteiten · ruilverhouding · revisor-verslag (bijzonder mandaat)
├── splitsing                            [G+R]               3 modaliteiten incl. partiële splitsing
└── fiscale-fusie-splitsing              [R]                 fiscale neutraliteit-regime · voorwaarden · EU-context

fiscale-voordelen-vennootschap           [Σ-cluster, 10 records — cross PO 2.3]
├── fiscale-voordelen-vennootschap       [Σ]                 keuzekader · aftrek-volgorde art 207 WIB · korf-regime
├── verlaagd-tarief-kleine-vennootschap  [R]                 KMO-tarief 20% + bezoldigingsregel
├── dbi-aftrek                           [R, ⏳ NIEUW]        100% vrijstelling deelnemings-dividenden
├── notionele-interestaftrek             [R]                 afgeschaft 2024 (overgang + historiek)
├── innovatie-aftrek                     [R, ⏳ NIEUW]        85% octrooi-inkomsten
├── investeringsaftrek                   [R]                 eenmalig vs gespreid per categorie
├── gespreide-belasting-meerwaarden      [R, ⏳ NIEUW]        art 47 WIB herinvestering
├── liquidatiereserve                    [R]                 10%/5%-anti-liquidatie-tarief (cross winstuitkering)
├── vvprbis                              [R]                 15% RV kleine venn nieuw kapitaal (cross winstuitkering)
└── meerwaarde-aandelen-venb             [R]                 (OP-K.6 opgelost) vrijstellings-voorwaarden

anti-misbruik                            [Σ-cluster, 6 records — cross PO 2.1 + 2.8]
├── anti-misbruik                        [Σ]                 keuzekader · onderscheid simulatie/AAMB/verboden · bewijslast
├── algemene-anti-misbruik-bepaling      [R]                 AAMB art 344§1 WIB
├── simulatie-leer                       [R, ⏳ NIEUW]        herkwalificatie werkelijke bedoeling
├── transfer-pricing                     [K]                 arm's length · TP-doc · OESO
├── thin-cap-regime                      [R, ⏳ NIEUW]        ATAD interest-aftrekbaarheid 30% EBITDA / 3M€
├── atad-richtlijn                       [K]                 EU GAAR + CFC + thin-cap + exit-tax + hybride
└── verboden-constructies                [R, ⏳ NIEUW]        specifieke anti-misbruik-bepalingen (art 18 etc.)

controle-opdracht                        [sub-Kader `controle`, 7 records — PO 1.6]
├── controleopdracht                     [K-techniek-Σ]    ▸ 4 fases (aanvaarden→plannen→bewijswerk→afronden+oordeel) ▸ prof skepticism ▸ delegatie-en-supervisie
├── opdracht-types                       [Σ]               4 types: controle · beoordeling · samenstelling · AUP  ▸ normenkader-piramide
├── audit-planning                       [K-techniek]      ▸ kennis-entiteit (ISA 315) ▸ auditrisicomodel (IR×CR×DR) ▸ materialiteit ▸ strategie+werkprogramma
├── audit-bewijs                         [K-techniek]      ▸ beweringen ▸ 7 procedures ▸ steekproef ▸ LOR ▸ IT-bewijs ▸ schattingen ▸ NOCLAR
├── revisiedossier                       [E-instrument]    ▸ permanent dossier ▸ lopend dossier
├── audit-afronding                      [K-techniek]      ▸ subsequent events ▸ misstatements ▸ analytical review ▸ communicatie governance + management letter
└── controleverklaring                   [E-instr, Σ]      4 oordelen (zonder voorbehoud · met voorbehoud · afkeurend · onthouding) ▸ verslag-componenten ▸ KAM ▸ andere-verslagstypes

bestuur-en-aansprakelijkheid             [thema-cluster vennootschapsrecht, 4 records — PO 3.0.II + VII]
├── bestuur-vennootschap                 [K]               organisatie · bevoegdheidsgrenzen · binding · dagelijks bestuur
├── belangenconflict-bestuur             [R-procedure]     kennisgeving · onthouding · bijzondere verslaggeving · sancties
├── oprichtersaansprakelijkheid          [K]               financieel-plan-toets bij faillissement < 3j
└── bestuurdersaansprakelijkheid         [K]               3 sporen · kennelijk onbehoorlijk bestuur · cap · #kwijting · #ontslag-bekendmaking

vennootschapsgeschillen                  [thema-cluster vennootschapsrecht, 1 record — PO 3.0.VIII]
└── vennootschapsgeschillen              [K]   ▸ types · contractuele preventie · bewijswaarde · minnelijke schikking · nietigheid besluiten · perspectief beroep-en-deontologie

insolventie                              [thema-cluster, 7 records — PO 3.0.IX + X]
├── insolventierecht-wer-boek-xx         [K]               WER boek XX framework · 3 procedures · Regsol · functionarissen
├── kamers-voor-ondernemingen-in-moeilijkheden  [R]       vroegtijdige opsporing · meldingsplicht accountant
├── ondernemingsbemiddelaar              [E-actor]         neutrale tussenpersoon · buitengerechtelijk
├── gerechtelijke-reorganisatie          [R-procedure]     opschorting · 3 modaliteiten (individueel/collectief akkoord/overdracht)
├── faillissement                        [R-procedure, NIEUW]   duurzame staking · curator · boedel · rangorde
├── ontbinding-en-vereffening            [G+R]             vrijwillig (WVV) vs gerechtelijk (WER) · vereffenaar · #boekenstaat-bij-ontbinding (bijzonder mandaat) · #vereffenaarsaansprakelijkheid
└── rehabilitatie-en-beroepsverbod       [R]               #rehabilitatie · #beroepsverbod (`-en-`-smell, split-overweging OP-INS.A)

ondernemingsvormen                       [thema-cluster vennootschapsrecht, 9 records — PO 3.0.I + taak.1]
├── ondernemingsvormen                   [E-bundel + Σ]    overzicht + vergelijkingsmatrix + WVV-systematiek + fiscale-keuze (perspectief)
├── besloten-vennootschap                [E-instrument]    (BV/BVBA/SRL) — default WVV-vorm sinds 2019; flexibel statutair
├── naamloze-vennootschap                [E-instrument]    (NV/SA) — beursgenoteerd-vriendelijk; rigide bestuur
├── cooperatieve-vennootschap            [E-instrument]    (CV/SC) — coöperatief-doel; uittredingsregime
├── vennootschap-onder-firma             [E-instrument]    (VOF/SNC) — volle aansprakelijkheid alle vennoten
├── commanditaire-vennootschap           [E-instrument]    (CommV/SComm) — gecommanditeerden + commandités
├── maatschap                            [E-instrument]    geen rechtspersoonlijkheid; fiscaal-transparant
├── vereniging-zonder-winstoogmerk       [E-instrument]    (VZW/ASBL) — zonder winstoogmerk; WVV boek 9-11
└── vennootschap-groottecategorieen      [E + R]           drempels art 1:24-1:27 WVV + cascade van gevolgen

interne-controle                         [sub-Kader `controle`, 7 records + 3 shared — PO 1.7]
├── interne-controle                     [K-techniek]      ▸ definitie ▸ 4 doelstellingen ▸ dubbele dimensie ▸ 3 lines of defense ▸ referentiekaders ▸ afbakening
├── ontwerp-interne-controle             [K-techniek]      proces-mapping → risico-identificatie → controle-selectie → documentatie → uitrol
├── functiescheiding                     [K-techniek]      4 onverenigbare functies (autoriseren/uitvoeren/registreren/bewaren) + IT-RBAC
├── it-controles                         [K-techniek]      ITGC + application controls + fysieke beveiliging + audittrail
├── interne-audit                        [E+K-techniek]    3rd line of defense — mandaat + functie + auditcharter
├── evaluatie-interne-controle           [K-techniek]      walkthroughs · tests of controls · self-assessment; design vs operating effectiveness
└── fouten-en-fraude                     [K]               afbakening fouten/fraude/verspilling + fraudedriehoek

beroepsbeoefening                        [thema-cluster onder beroep-en-deontologie-discipline, 11 records + 2 shared — PO 4.0.I + taken 1-3]
├── --- I. STATUUT VAN HET BEROEP ---
├── gecertificeerd-accountant            [E-actor, NIEUW]  beroep · toelatingsvereisten · monopolieopdrachten · stagiair → gecertificeerd
├── itaa-beroepsorganisatie              [E-orgaan]        structuur · raden · publiek toezicht · openbaar register
├── normbronnen                          [K-overzicht]     wet → KB → reglement → norm → deontologische code → ITAA-normen + ISA
├── --- II. DEONTOLOGISCHE BEGINSELEN ---
├── deontologie                          [K]               5 beginselen: integriteit · objectiviteit · vakbekwaamheid · vertrouwelijkheid · professioneel gedrag
├── beroepsgeheim                        [K-principe + R]  wat valt onder · uitzonderingen · samenloop met AML-melding
├── beroepsaansprakelijkheid             [K-principe]      3 sporen (burgerlijk · strafrechtelijk · tuchtrechtelijk) — dekt accountant + bedrijfsrevisor
├── tuchtprocedure-itaa                  [R-procedure]     wie · sancties (waarschuwing/schorsing/schrapping) · beroep
├── kwaliteitstoetsing-itaa              [R-procedure]     externe peer review · frequentie · scope
├── permanente-vorming                   [R-procedure]     puntenstelsel · ITAA-norm · sancties
├── --- III. AML / WITWASPREVENTIE ---
├── antiwitwaspreventie                  [R-overkoepelend] AML-wet 18-09-2017 + WER + ITAA-norm-aww  ▸ cliëntenonderzoek (KYC) ▸ ubo-register ▸ risicogebaseerde benadering ▸ melding-cfi (tipping-off-verbod) ▸ intern beleid
├── --- IV. KANTOOR-PRAKTIJK ---
├── opdrachtaanvaarding-en-opdrachtbrief [E + R]           (verhuisd uit controle-opdracht, OP-EC.A) — ITAA-norm-opdrachtbrief
└── kantoor-organisatie                  [K]               ▸ team-coordinatie + supervisie ▸ communicatie-met-stakeholders ▸ digitale werkomgeving

Shared records (thema's `controle-opdracht` + `interne-controle` + `beroepsbeoefening`)
├── coso-framework                       [K-techniek-Σ]    5 componenten: controle-omgeving · risico-inschatting · controle-activiteiten · informatie-en-communicatie · monitoring  + ERM-variant
├── cyclus-analyse                       [Σ]               5 cycli: aankoop(P2P) · productie · verkoop(O2C) · HR(H2R) · voorraad
├── auditcomite                          [E-orgaan]        schakel bestuur ↔ interne auditor ↔ commissaris  (ook thema beroepsbeoefening)
├── onafhankelijkheid                    [K-principe + R]  (shared beroepsbeoefening + controle-opdracht) — geesteshouding + naar-buiten-toe + cooling-off
└── kwaliteitsmanagement-opdracht        [K-techniek + R]  (shared beroepsbeoefening + controle-opdracht) — ISQM kantoor + EQR opdracht
```

**Leesregel**: een record hangt op één plek in deze tree (zijn thuis-cluster). Verbindingen naar andere clusters via `relaties[]`. Discipline-binding via `accountant_perspectieven[]`. Thema-tag `thema: []` is orthogonaal (een record kan meerdere thema's dragen, één primair-cluster).

### Uitgewerkte clusters — navigatie

| Cluster | Records | PO-aanknoping | Sectie |
|---|---|---|---|
| mobiliteit | 4 | PO 2.1 (PB) · PO 1.1 (boekhouding) · PO 1.5 (jaarrekening-toelichting) | [§Mobiliteit-cluster](#mobiliteit-cluster) |
| kapitaalstructuur | 16 | PO 3.0 (WVV) · PO 1.1 (boekhouding) · PO 2.3 (VenB) | [§Kapitaalstructuur-cluster](#kapitaalstructuur-cluster) |
| werknemers-vergoedingen | 15 | PO 2.1 (PB-bezoldigingen) · PO 2.3 (VenB-aftrekbaarheid) · PO 1.1 (boekhouding) | [§Werknemers-vergoedingen-cluster](#werknemers-vergoedingen-cluster) |
| overdracht-onderneming | 2 | PO 3.0 (WVV) · PO 2.3 (VenB) · PO 2.7 (BTW) | [§Overdracht-onderneming-cluster](#overdracht-onderneming-cluster) |
| schuldfinanciering | 4 | PO 1.1 (boekhouding) · PO 3.0 (WVV-obligaties) · PO 2.3 (VenB-interest) | [§Schuldfinanciering-cluster](#schuldfinanciering-cluster) |
| controle-opdracht | 7 | PO 1.6 | [§Controle-opdracht-cluster](#controle-opdracht-cluster) |
| interne-controle | 7 + 3 shared | PO 1.7 | [§Interne-controle-cluster](#interne-controle-cluster) |
| ondernemingsvormen | 9 | PO 3.0.I + taak.1 + cross PO 1.1 + 2.3 | [§Ondernemingsvormen-cluster](#ondernemingsvormen-cluster) |
| bestuur-en-aansprakelijkheid | 4 | PO 3.0.II + VII | [§Bestuur-en-aansprakelijkheid-cluster](#bestuur-en-aansprakelijkheid-cluster) |
| vennootschapsgeschillen | 1 | PO 3.0.VIII | [§Vennootschapsgeschillen-cluster](#vennootschapsgeschillen-cluster) |
| insolventie | 7 (incl. nieuwe `faillissement`) | PO 3.0.IX + X | [§Insolventie-cluster](#insolventie-cluster) |
| winstuitkering | 3 (NIEUW Σ + winstbestemming + tantième; 4 cross-records) | PO 3.0.IV.B + cross 2.3 + 2.1 | [§Winstuitkering-cluster](#winstuitkering-cluster) |
| reorganisatie | 4 (Σ + fusie + splitsing + fiscale-fusie-splitsing) | cross PO 3.0.taak.2/3 + 2.3.III.B + 2.8.XVI + 1.4 | [§Reorganisatie-cluster](#reorganisatie-cluster) |
| fiscale-voordelen-vennootschap | 10 (Σ + 9 regimes — 4 nieuw) | cross PO 2.3.II + III + taak.3 | [§Fiscale-voordelen-vennootschap-cluster](#fiscale-voordelen-vennootschap-cluster) |
| **anti-misbruik** | **6** (Σ + AAMB + simulatie + TP + thin-cap + ATAD + verboden — 3 nieuw) | **cross PO 2.1.IX + 2.8.XVI + XVII** | [**§Anti-misbruik-cluster**](#anti-misbruik-cluster) |
| loon-en-payroll | K-techniek + 10 component-records (deels nieuw) | cross PO 2.1 + werknemers-vergoedingen | [§Loon-en-payroll-cluster (K-techniek)](#loon-en-payroll-cluster-k-techniek) |
| **beoordelings-opdracht** + **isae-opdrachten** + **overeengekomen-procedures** | 3 × 1 mini-record (allemaal ⏳) | sub-Kaders van `controle` — gedragen via `opdracht-types`-Σ | [§Overige sub-Kaders van controle-discipline (compact)](#overige-sub-kaders-van-controle-discipline-compact) |
| beroepsbeoefening | 11 + 2 shared (`onafhankelijkheid` · `kwaliteitsmanagement-opdracht`) | PO 4.0.I + taken 1-3 | [§Beroepsbeoefening-cluster](#beroepsbeoefening-cluster) |
| bijzondere-mandaten | 1 (klein record, detail bij Gebeurtenissen) | PO 3.0.taak.3 + 3.0.IV.A + cross PO 1.6.IV.C | [§Bijzondere-mandaten-cluster](#bijzondere-mandaten-cluster) |

*PO-aanknoping = welk(e) examenonderdeel/-onderdelen het cluster primair raakt. Het onderscheid "cross-cutting" vs "discipline-cluster" uit eerdere sparring is geschrapt 2026-05-26 — alle clusters zijn clusters; verschil zit alleen in PO-mapping-breedte (1 PO vs meerdere), niet in structuur-type. Zie rationale-log.*

**Shared records** (leven met meerdere thema's, zichtbaar in meerdere clusters):
- `coso-framework` [K-techniek] — thema's: `controle-opdracht` + `interne-controle` (audit-perspectief = ISA 315 controle-risico-inschatting; advies-perspectief = IC-design KMO)
- `cyclus-analyse` [Σ] — thema's: `controle-opdracht` + `interne-controle` (audit-perspectief = bewijswerk per cyclus; advies-perspectief = cyclus-ontwerp)
- `auditcomite` [E-orgaan] — thema's: `controle-opdracht` + `interne-controle` + `beroepsbeoefening` (schakel bestuur ↔ interne auditor ↔ commissaris)
- `fraude` [G+K] — al cross-cutting van controle-opdracht-werk
- `auditrisicomodel` — sub-sectie van `audit-planning` (zichtbaar voor 1.7.V.E via cross-link)

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

**Belangrijke simplificatie (2026-05-23, versoepeld 2026-05-26)**: laag-1 disciplines + sub-Kaders zijn primair Kader-records. **Versoepeling**: laag-2 cluster-uitwerkingen onder een sub-Kader (zoals `controle-opdracht`, `interne-controle`) mogen records van alle categorieën (K, E, G, R, Σ) bevatten zolang die conceptueel bij dat sub-Kader horen. Discipline-binding gebeurt via `accountant_perspectieven[]` en `relaties[]`. Eén record hangt op één plek; kruisverbindingen via perspectieven en relaties + thema-tags. *Originele formulering was "discipline-stam = alleen Kader-records, alle E/G/R cross-cutting" — bleek te restrictief bij confrontatie met PO 1.6 + 1.7 (revisiedossier = E in controle-opdracht-cluster; interne-audit = E+K in interne-controle-cluster).*

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

**Mapping-actie 2026-05-26**: `oprichting-vennootschap` krijgt nieuwe sub-sectie `#initiele-inbreng` — modaliteiten (geld/natura) · revisorverslag bij natura · min-storting bij authentieke akte (BV/NV) · volstortings-eisen · cross-relatie naar `kapitaalverhoging-in-natura` (analoge mechaniek). Beslissing genomen bij ondernemingsvormen-cluster-sparring: initiële inbreng = sub-aspect van oprichting (gelijktijdig + geen aparte gebeurtenis), niet aparte Gebeurtenis-record.

### Ondernemingsvormen-cluster

Thema: `ondernemingsvormen`. *Thema-cluster onder `vennootschapsrecht`-discipline. Eerste cluster uit PO 3.0-werk (2026-05-26). Lost gelijktijdig OP-EC.7 op (vennootschap-groottecategorieen krijgt thuis hier) en absorbeert bestaand kader-record vennootschapsrechtelijk-kader-wvv + bestaand kader-record keuze-rechtsvorm-fiscaal (= perspectief, geen apart record).*

```
ondernemingsvormen                            [thema-cluster vennootschapsrecht]
├── ondernemingsvormen                        [E-bundel + Σ, hoofdrecord]
│   ▸ overzicht WVV-vormen + niet-WVV-vormen
│   ▸ vergelijkingsmatrix: kapitaal · aansprakelijkheid · beheer · winstdeling · fiscale-aanknoping
│   ▸ wanneer welke vorm? (3.0.I.C)
│   ▸ #wvv-systematiek (absorbeert `vennootschapsrechtelijk-kader-wvv`: WVV boek 1-7 + boek 9-11 vzw)
│   ▸ #fiscale-keuze (absorbeert `keuze-rechtsvorm-fiscaal`: eenmanszaak/PB vs vennootschap/VenB, KMO-tarief, afschrijvingsregimes)
├── besloten-vennootschap                     [E-instrument]   (BV) — default WVV-vorm sinds 2019; flexibel statutair
├── naamloze-vennootschap                     [E-instrument]   (NV) — beursgenoteerd-vriendelijk; rigide bestuur
├── cooperatieve-vennootschap                 [E-instrument]   (CV) — coöperatief-doel; uittredingsregime
├── vennootschap-onder-firma                  [E-instrument]   (VOF) — volle aansprakelijkheid alle vennoten
├── commanditaire-vennootschap                [E-instrument]   (CommV) — 2 vennoten-typen
├── maatschap                                 [E-instrument]   geen rechtspersoonlijkheid; fiscaal-transparant
├── vereniging-zonder-winstoogmerk            [E-instrument]   (VZW) — zonder winstoogmerk; WVV boek 9-11
└── vennootschap-groottecategorieen           [E + R]          drempels art 1:24-1:27 WVV + cascade van gevolgen
```

**Schrappen als zelfstandig record / herleiden tot sub-sectie**:
- `vennootschapsrechtelijk-kader-wvv` → sub-sectie `#wvv-systematiek` in `ondernemingsvormen` (overkoepelend WVV-kader heeft zelfstandig weinig waarde zonder vormen-context)
- `keuze-rechtsvorm-fiscaal` → perspectief `advies` + `fiscaal-PB/VenB` op `ondernemingsvormen`-record (= twee perspectieven op zelfde fenomeen, geen aparte as)
- `groottecategorie-vennootschap` → hernoemd `vennootschap-groottecategorieen` (meervoud = klopt; 4 categorieën: micro/klein/middelgroot/groot)
- `bv-rechtsvorm` → hernoemd `besloten-vennootschap` (`-rechtsvorm`-suffix-smell weg)
- `nv-rechtsvorm` → hernoemd `naamloze-vennootschap`
- `cv-rechtsvorm` → hernoemd `cooperatieve-vennootschap`
- `vof-commv-rechtsvorm` → **gesplitst** in `vennootschap-onder-firma` + `commanditaire-vennootschap` (2 verschillende fenomenen — VOF heeft alleen volle aansprakelijkheid, CommV heeft 2 vennoten-typen met verschillende aansprakelijkheid)
- `maatschap-rechtsvorm` → hernoemd `maatschap`
- `vzw-rechtsvorm` → hernoemd `vereniging-zonder-winstoogmerk`

**Cross-cluster** (eigen plek elders, relaties hierheen):
- `oprichting-vennootschap` [G+R] — blijft in `kapitaalstructuur`-cluster (oprichting = kapitaal-relevant moment + initiële vermogenscomponent; vorm-keuze precedeert). Cross-relatie hierheen + nieuwe sub-sectie `#initiele-inbreng` (zie mapping-actie hierboven).
- `aansprakelijkheid-oprichters-bestuurders` → toekomstig `bestuur-en-aansprakelijkheid`-cluster (PO 3.0.VII ⏳). Cross-relatie hier (vorm bepaalt aansprakelijkheidsregime).
- `financieel-plan` [E, in kapitaalstructuur] — verplicht bij BV/NV/CV. Cross-relatie naar vorm-records.

**Triangulatie-resultaten ondernemingsvormen** (2026-05-26):
- ~13 PO 3.0.I + 3.0.taak.1-anchors → **0 PO-only gaps**
- 11 bestaande records met relevante PO 3.0-anker → **9 cluster-eigen records** (1 Σ + 7 vormen + groottecategorieen) + 2 absorpties (vennootschapsrechtelijk-kader-wvv, keuze-rechtsvorm-fiscaal) + 1 split (vof-commv → 2)
- 12 kandidaten in DB voor dit blok (alle `gerealiseerd: 0` voor de hernoemde — markering-backlog)
- Belangrijkste smell-oplossing: `-rechtsvorm`-suffix als schema-artefact (analoog aan `-cluster`-smell uit PO 1.7); 6 records hernoemd

**Bronnen-pin voor cluster**:
- ✅ **WVV** (Wetboek Vennootschappen en Verenigingen, 2019) — primaire bron voor BV/NV/CV/VOF/CommV/maatschap + boek 9-11 VZW. ITAA-LEX bevat WVV — check `resources/bronnen/wetteksten/`.
- ✅ `MvT-WVV-2018` (Memorie van Toelichting) — interpretatieve bron, untracked in resources
- ⏳ ITAA-norm-omzetting-vennootschap (al trusted) — bij vorm-wissel; cross-relatie naar `omzetting-vennootschap`-record
- ⏳ CBN-adviezen over jaarrekening-schema per vorm — voor `vennootschap-groottecategorieen` cascade

**Details per record** (hints voor extractie):

**`ondernemingsvormen`** [E-bundel + Σ]
- inhoud: overkoepelend record voor de keuze + vergelijking van rechtsvormen. **Vergelijkingsmatrix** met 5 dimensies: (a) **kapitaal** — min-storting bij oprichting + statutaire vrijheid + soort effecten; (b) **aansprakelijkheid** — beperkt tot inbreng (BV/NV/CV) vs volle aansprakelijkheid (VOF) vs gemengd (CommV) vs natuurlijk persoon (maatschap); (c) **beheer** — wie bestuurt + welke organen + welke meerderheden; (d) **winstdeling** — vrij statutair (BV) vs evenredig aandeelhoudersschap (NV) vs coöperatief (CV); (e) **fiscale-aanknoping** — vennootschap (VenB) vs fiscaal-transparant (maatschap) vs eenmanszaak (PB). Sub-sectie `#wanneer-welke-vorm` (3.0.I.C): keuze-criteria voor stagiair (omvang + risico + vermogensplanning + bestuursvormen + fiscaal). Sub-sectie `#wvv-systematiek`: WVV-boekstructuur (boek 1 algemeen · 2-7 vennootschappen · 9-11 verenigingen) + relatie WVV ↔ vroegere wetboeken (W.Venn., wet 27 juni 1921 voor VZW). Sub-sectie `#fiscale-keuze`: vergelijking eenmanszaak/PB vs vennootschap/VenB (KMO-tarief 20% op eerste 100k mits bezoldigingsregel, anders 25%); afschrijvingsregimes; sociale bijdragen; uittredings-fiscaliteit; "wanneer kantelen?" criterium ⚠️.
- perspectieven: `advies` (vorm-keuze + planning, omvorming-advies) · `fiscaal-VenB` (KMO-tarief-context per vorm) · `fiscaal-PB` (eenmanszaak vs vennootschap) · `boekhouding` (jaarrekening-schema afhankelijk van vorm + grootte)
- naam_officieel: ondernemingsvormen / vennootschapsvormen · synoniemen: rechtsvormen, juridische ondernemingsvormen, business entity types, company forms
- relaties: alle 7 vorm-records, `vennootschap-groottecategorieen` (cascade van gevolgen per vorm), `oprichting-vennootschap` (kapitaalstructuur — oprichtingsketen), `omzetting-vennootschap` (vorm-wissel), `aansprakelijkheid-oprichters-bestuurders` (vorm bepaalt regime)

**`besloten-vennootschap`** [E-instrument] — *(was `bv-rechtsvorm`)*
- inhoud: meest gebruikte vennootschapsvorm sinds WVV (2019). **Geen minimumkapitaal** meer (vóór 2019 was dit 18.550€ voor BVBA); **toereikend aanvangsvermogen** vereist (financieel-plan-toets). **Aandelen**: vrij overdraagbaar (kan statutair beperkt); geen nominale waarde verplicht. **Bestuur**: één of meerdere zaakvoerders (statutair vrij); college mogelijk; raad van bestuur niet verplicht (kan statutair); dagelijks bestuur facultatief. **AV**: gewone meerderheid voor standaardbeslissingen; bijzondere meerderheid (3/4) voor statutenwijziging. **Kapitaalbescherming strenger**: dubbele test (netto-actief-test + uitkeringstest, 12-maand-liquiditeits-prognose ⚠️). **Statutaire vrijheid**: één van WVV's grote vernieuwingen — veel zaken zijn aanvullend recht. **Alarmbel**: aangepast aan kapitaal-loos systeem (netto-actief-criterium).
- perspectieven: `vennootschapsrecht`-inhoud (statuten + bestuur + AV-procedures) · `boekhouding` (jaarrekening-schema volgens grootte) · `fiscaal-VenB` (KMO-tarief mits voorwaarden) · `advies` (vorm-keuze + statutair maatwerk)
- naam_officieel: besloten vennootschap · synoniemen: BV, BVBA (pre-WVV), besloten venootschap met beperkte aansprakelijkheid (BVBA), SRL (Frans: société à responsabilité limitée), private limited company
- relaties: `ondernemingsvormen` (parent-Σ), `oprichting-vennootschap`, `kapitaalstructuur` (eigen-vermogen, kapitaalverhoging), `kapitaalbescherming`, `alarmbel-procedure`, `financieel-plan`, `vennootschap-groottecategorieen`

**`naamloze-vennootschap`** [E-instrument] — *(was `nv-rechtsvorm`)*
- inhoud: traditioneel "grote vennootschap"-vorm; **min-kapitaal 61.500€** ⚠️ blijft (anders dan BV); **min-storting 25% bij oprichting** (volstortingsplicht voor rest). **Aandelen**: vrij overdraagbaar (kan statutair beperkt, bv. goedkeuringsclausule); nominale waarde of fractiewaarde; effecten aan toonder uitgedoofd, alleen op naam of gedematerialiseerd. **Bestuur**: 3 modaliteiten — (a) raad van bestuur (min 3 leden, of 2 indien max 2 aandeelhouders); (b) enige bestuurder; (c) duaal bestuur (raad van toezicht + directieraad — eerder uitzonderlijk). **AV**: aanwezigheids-quorum + meerderheidsregels per type beslissing. **Beursgenoteerd-vriendelijk**: emissieprospectus-regime, KAM, externe audit verplicht. Rigider dan BV qua statutaire vrijheid.
- perspectieven: `vennootschapsrecht`-inhoud · `boekhouding` (jaarrekening verplicht volledig schema bij beursgenoteerd) · `fiscaal-VenB` · `audit` (commissaris-verplicht boven grootte-drempels, soms statutair eerder)
- naam_officieel: naamloze vennootschap · synoniemen: NV, SA (Frans: société anonyme), public limited company, joint-stock company
- relaties: `ondernemingsvormen`, `oprichting-vennootschap`, `kapitaalstructuur` (kapitaal-mechanismen), `commissaris` (beroepsbeoefening — vaak verplicht), `kapitaalbescherming`

**`cooperatieve-vennootschap`** [E-instrument] — *(was `cv-rechtsvorm`)*
- inhoud: **coöperatief-doel verplicht** sinds WVV (2019) — bevrediging van behoeften van vennoten (consumeren, produceren, financieren samen) ⚠️ ; loutere belegging in CV is uitgesloten. **Variabel kapitaal**: vennoten kunnen toetreden + uittreden zonder statutenwijziging; gevolg is variabele samenstelling. **Erkende coöperatie**: optioneel statuut met fiscale voordelen (vrijstelling van interest tot bedrag op spaarboekjes-niveau ⚠️). **Bestuur**: één of meerdere bestuurders. **Uittreding**: vennoot heeft uittredingsrecht (statutair geregeld) — vertrek met scheidingsaandeel.
- perspectieven: `vennootschapsrecht`-inhoud · `fiscaal-VenB` (erkende-CV-regime) · `advies` (geschikt voor coöperatie-projecten, niet voor klassieke onderneming)
- naam_officieel: coöperatieve vennootschap · synoniemen: CV, SC (Frans: société coopérative), cooperative society
- relaties: `ondernemingsvormen`, `oprichting-vennootschap`

**`vennootschap-onder-firma`** [E-instrument] — *(was `vof-commv-rechtsvorm`, gesplitst — OP-VOV.F)*
- inhoud: **personenvennootschap met rechtspersoonlijkheid**. **Volle, onbeperkte en hoofdelijke aansprakelijkheid** van alle vennoten voor schulden van de vennootschap ⚠️ — verschilt fundamenteel met BV/NV. **Geen minimumkapitaal**. **Bestuur**: vennoten zijn van rechtswege bestuurder tenzij statutair anders. **Beslissingen**: bij eenparigheid tenzij statutair anders. Wordt gebruikt bij kleine ondernemingen + vrije beroepen + family business waar vertrouwen tussen partijen hoog is.
- perspectieven: `vennootschapsrecht`-inhoud · `fiscaal-VenB` · `advies` (afgeraden bij significant risico — volle aansprakelijkheid)
- naam_officieel: vennootschap onder firma · synoniemen: VOF, SNC (Frans: société en nom collectif), general partnership
- relaties: `ondernemingsvormen`, `commanditaire-vennootschap` (verwante vorm), `aansprakelijkheid-oprichters-bestuurders`

**`commanditaire-vennootschap`** [E-instrument] — *(was `vof-commv-rechtsvorm`, gesplitst — OP-VOV.F)*
- inhoud: **personenvennootschap met 2 typen vennoten** — (a) **gecommanditeerden** (beherende vennoten): volle aansprakelijkheid + besturen actief; (b) **commandités** (stille vennoten): aansprakelijkheid beperkt tot inbreng + mogen niet besturen ⚠️ (verboden om risico stille-vennoot-statuut te verliezen). Geen minimumkapitaal. Gebruikt bij familie-vermogensplanning (oudere generatie als commandité, jongere als gecommanditeerde) of bij investeringsfondsen-structuren.
- perspectieven: `vennootschapsrecht`-inhoud · `fiscaal-VenB` · `advies` (vermogensplanning + investeringsstructuren) · `fiscaal-PB` (cross — successie/schenking-impact)
- naam_officieel: commanditaire vennootschap · synoniemen: CommV, SComm (Frans: société en commandite), limited partnership
- relaties: `ondernemingsvormen`, `vennootschap-onder-firma` (verwante vorm), `aansprakelijkheid-oprichters-bestuurders`

**`maatschap`** [E-instrument] — *(was `maatschap-rechtsvorm`)*
- inhoud: **vennootschap zonder rechtspersoonlijkheid** ⚠️ — meest fundamentele afwijking. Geen RPR-inschrijving, geen jaarrekening-publicatieplicht. **Fiscaal-transparant**: geen VenB; inkomsten worden rechtstreeks belast bij vennoten (PB) volgens hun inbreng-aandeel. **Aansprakelijkheid**: vennoten persoonlijk aansprakelijk voor maatschappelijke verbintenissen (mate afhankelijk statuten). **Bestuur**: vennoten besturen samen tenzij statutair anders. **Populair bij vermogensplanning**: ouders brengen aandelen in maatschap, schenken delen aan kinderen (controle behouden via maatschapsstatuten). Sinds 2019 verplichte inschrijving in KBO + UBO-register (sinds 2019 wet AML).
- perspectieven: `vennootschapsrecht`-inhoud · `fiscaal-PB` (transparant doorrekening) · `advies` (vermogensplanning + estate planning) · `beroep-en-deontologie` (UBO-register-discipline)
- naam_officieel: maatschap · synoniemen: société simple (Frans), simple partnership, vennootschap van gemeen recht (oude term pre-WVV)
- relaties: `ondernemingsvormen`, `aansprakelijkheid-oprichters-bestuurders` (vennoten persoonlijk), `erfrecht`/`huwelijksvermogensrecht` (vermogensplanning-context)

**`vereniging-zonder-winstoogmerk`** [E-instrument] — *(was `vzw-rechtsvorm`)*
- inhoud: rechtspersoon **zonder winstoogmerk** — winst mag bestaan maar mag niet uitgekeerd worden aan leden. WVV boek 9-11 (sinds 2019; vroeger eigen wet 27 juni 1921). **Bestuur**: algemene vergadering van leden + bestuursorgaan (min 3 bestuurders, of 2 indien max 3 leden). **Doelstelling**: niet-economische of belangeloze activiteit; "secundaire" economische activiteiten mogen mits ondergeschikt aan doel. **Aansprakelijkheid**: VZW heeft eigen rechtspersoonlijkheid, leden in principe niet persoonlijk aansprakelijk; bestuurders wel bij fout-aansprakelijkheid. **Jaarrekening**: vereenvoudigd of dubbel volgens grootte (eigen drempels art 3:47 WVV).
- perspectieven: `vennootschapsrecht`-inhoud (WVV boek 9-11) · `boekhouding` (eigen schema vereenvoudigd vs dubbel) · `fiscaal-VenB` (rechtspersonenbelasting RPB tenzij commerciële activiteit, dan VenB) · `advies` (vorm voor non-profit, sport, cultuur, beroepsfederaties)
- naam_officieel: vereniging zonder winstoogmerk · synoniemen: VZW, ASBL (Frans: association sans but lucratif), non-profit organization, NPO
- relaties: `ondernemingsvormen`, `vennootschap-groottecategorieen` (eigen drempels voor VZW), `aansprakelijkheid-oprichters-bestuurders` (bestuurders-aansprakelijkheid bij VZW)

**`vennootschap-groottecategorieen`** [E + R, hybride] — *(was `groottecategorie-vennootschap` — hernoemd naar meervoud)*
- inhoud: 4 grootte-categorieën onder WVV — **micro** · **klein** · **middelgroot** · **groot** — gedefinieerd door drempels balans/omzet/personeel (art 1:24-1:27 WVV ⚠️) met 2-jaar-overschrijdings-regel; bij groepen op geconsolideerd niveau. **Cascade van gevolgen**: (a) `#jaarrekening-schema` — micro/verkort/volledig (boekhouding-perspectief); (b) `#commissaris-verplicht` — vanaf middelgroot (audit-perspectief; trigger voor wettelijke controle); (c) `#consolidatieplicht` — groot-criterium op groepsbasis (boekhouding-perspectief); (d) `#publicatieformaliteiten` — verkort vs volledig neerleggen; (e) `#kmo-controlenorm-toepasselijkheid` — voor controle/beoordeling KMO's vs algemene controlenorm (audit-perspectief); (f) `#fiscaal-kmo-flag` ⚠️ — fiscale KMO-criteria (art 1:24-1:25 WIB) **niet identiek** met WVV-criteria, aparte sectie of cross-link naar `kmo-tarief-vennootschapsbelasting`.
- perspectieven: `boekhouding` (schema-keuze, publicatie, consolidatie) · `audit` (commissaris-trigger, KMO-norm-toepasselijkheid) · `advies` (drempel-management, groei-overweging, structurering)
- naam_officieel: grootte-categorieën van vennootschappen (art 1:24-1:27 WVV) · synoniemen: KMO-criteria, grootte-criteria vennootschap, art 1:24 WVV-drempels, klein vs middelgroot vs groot, micro-onderneming
- relaties: `ondernemingsvormen` (parent), `jaarrekening`, `commissaris` (audit-cluster), `controleopdracht`, `opdracht-types` (controle vs beoordeling KMO-context), `kmo-tarief-vennootschapsbelasting` (cross fiscaal — aparte criteria-set)

**Open punten ondernemingsvormen-cluster**:
- **OP-VOV.A** ✅ **Beslist**: cluster-naam `ondernemingsvormen` (breedst — omvat ook VZW + maatschap die geen "vennootschap" stricto sensu zijn).
- **OP-VOV.B** ✅ **Beslist**: hernoemen `groottecategorie-vennootschap` → `vennootschap-groottecategorieen` (meervoud klopt voor 4 categorieën). Mapping-actie.
- **OP-VOV.C** ✅ **Beslist**: `vennootschapsrechtelijk-kader-wvv` absorberen als sub-sectie `#wvv-systematiek` in `ondernemingsvormen` (overkoepelend WVV-kader heeft zelfstandig weinig waarde zonder vormen-context).
- **OP-VOV.D** ✅ **Beslist**: `keuze-rechtsvorm-fiscaal` schrappen als eigen record; wordt perspectief `advies` + `fiscaal-VenB`/`fiscaal-PB` op `ondernemingsvormen`-record. User-feedback: "zijn dat niet net twee verschillende perspectieven over dezelfde concepten?" — ja.
- **OP-VOV.E** ✅ **Beslist**: `oprichting-vennootschap` blijft in `kapitaalstructuur`-cluster met nieuwe sub-sectie `#initiele-inbreng` (niet eigen record). Initiële inbreng = sub-aspect van oprichting (gelijktijdig + geen aparte gebeurtenis).
- **OP-VOV.F** ✅ **Beslist** (user 2026-05-26): `vof-commv-rechtsvorm` **splitsen** in `vennootschap-onder-firma` + `commanditaire-vennootschap` — 2 verschillende fenomenen onder 1 oude record-naam (VOF heeft alleen volle aansprakelijkheid; CommV heeft 2 vennoten-typen met verschillende aansprakelijkheidsregimes). `en`-smell-pattern uit rationale-log 2026-05-24 bevestigd.
- **OP-VOV.G** ⏳ **Naam-smell-scan-actie uitbreiden**: `-rechtsvorm`-suffix toevoegen aan bestaande `-cluster`-suffix-scan voor mapping-fase. Algemene regel: record-id = conceptnaam, geen schema-categorie-marker als suffix.
- **OP-VOV.H** ⏳ Cross-relatie naar PO 1.1-bedrijfsvorm-keuze-financiering (boekhouding-context) — uit te werken bij PO 1.1-cluster.

**Test-case-validatie** (2026-05-26): 6 representatieve PO 3.0-examen-vragen rond vorm + oprichting:

| Vraag | Concept | Tree-pad | Resultaat |
|---|---|---|---|
| 2003-bibf-vrI2 | Omzetting eenmanszaak → BVBA | `ondernemingsvormen#wanneer-welke-vorm` + `besloten-vennootschap` + cross `omzetting-vennootschap` (G) | ✅ |
| 2008-bibf-vrI2 | Financieel plan bij oprichting | `financieel-plan` (kapitaalstructuur) + `oprichting-vennootschap#initiele-inbreng` (nieuwe sub-sectie) + relatie naar BV/NV/CV (verplicht) | ✅ (mits sub-sectie #initiele-inbreng wordt toegevoegd) |
| 2008-bibf-vrI5 | Oprichtersaansprakelijkheid BVBA vs NV | `besloten-vennootschap` + `naamloze-vennootschap` (vergelijking) + cross `aansprakelijkheid-oprichters-bestuurders` (PO 3.0.VII ⏳) | ✅ |
| 2013-1-vr14 | Aandeelhouderschap BVBA bij overlijden vennoot | `besloten-vennootschap#statutaire-flexibiliteit` + `aandeel` (kapitaalstructuur) + cross erfrecht | ✅ |
| 2013-2-vr15 | Alarmbelprocedure bij BVBA met overgedragen verlies | `besloten-vennootschap` + cross `alarmbel-procedure` + `kapitaalbescherming` (kapitaalstructuur) | ✅ |
| 2013-2-vr16 | Toegestaan kapitaal + oprichtersaansprakelijkheid NV | `naamloze-vennootschap` + cross `kapitaalverhoging#toegestaan-kapitaal` + cross `aansprakelijkheid-oprichters-bestuurders` | ✅ |

Alle 6 vragen passen door de tree. **Bevestigingen**: (a) splits VOF/CommV bevestigd door geen specifieke testvraag op CommV-only — beide bestaan apart maar worden hier niet getest; (b) `#initiele-inbreng` sub-sectie in `oprichting-vennootschap` is concreet nodig (vr 2008-bibf-vrI2); (c) cross-relaties naar `aansprakelijkheid-oprichters-bestuurders` bevestigen dat dit cluster nodig wordt (PO 3.0.VII open punt — opgelost via `bestuur-en-aansprakelijkheid`-cluster).

### Bestuur-en-aansprakelijkheid-cluster

Thema: `bestuur-en-aansprakelijkheid`. *Thema-cluster vennootschapsrecht (PO 3.0.II + VII, 2026-05-26). Klein cluster — 4 records — maar substantieel didactisch (bestuursorganisatie + persoonlijke aansprakelijkheid zijn examen-kritisch). Lost OP-BB.E gedeeltelijk op (commissaris ↔ bestuurder-context) en flagt OP-BA.C (tantième-controle als bijzonder mandaat).*

```
bestuur-en-aansprakelijkheid              [thema-cluster vennootschapsrecht]
│
├── --- BESTUUR (PO 3.0.II) ---
├── bestuur-vennootschap                  [K]
│   ▸ organisatie: enige bestuurder · raad van bestuur · dualistisch (raad van toezicht + directieraad) · college zaakvoerders
│   ▸ #bevoegdheidsgrenzen — individueel vs collegiaal (3.0.II.A)
│   ▸ #binding-bij-bevoegdheidsoverschrijding — bescherming derden te goeder trouw (3.0.II.B)
│   ▸ #dagelijks-bestuur — afgeleide bevoegdheid
│   ▸ statutaire flexibiliteit per vorm (BV vs NV vs CV)
├── belangenconflict-bestuur              [R-procedure]
│   ▸ WVV-procedure: kennisgeving · onthouding · bijzondere verslaggeving
│   ▸ toepassingen: persoonlijk strijdig belang · groepscontext · enige bestuurder
│   ▸ sancties: nietigheid besluit + persoonlijke aansprakelijkheid
│
├── --- AANSPRAKELIJKHEID (PO 3.0.VII) ---
├── oprichtersaansprakelijkheid           [K — split van `aansprakelijkheid-oprichters-bestuurders`]
│   ▸ kennelijk ontoereikend financieel plan + 3j-faillissementstoets
│   ▸ solidair vermoeden (BV/NV/CV); financieel-plan bij notaris als bewijs-instrument
│   ▸ context: sinds WVV BV geen min-kapitaal → financieel-plan-toets nog cruciaaler
└── bestuurdersaansprakelijkheid          [K — split + uitgebreid]
    ▸ 3 sporen: contractueel (vennootschap) · buitencontractueel (derden) · strafrechtelijk
    ▸ kennelijk grove fout · kennelijk onbehoorlijk bestuur · schending wet/statuten
    ▸ #faillissementsaansprakelijkheid (WER XX:225 — kennelijk onbehoorlijk bestuur dat bijdroeg aan faillissement)
    ▸ #wettelijke-cap (aansprakelijkheidsbeperking sinds WVV — bedragen volgens omzet/balanstotaal ⚠️)
    ▸ #kwijting (PO 3.0.VII.B — reikwijdte: alleen bekende feiten; geen wisselgeld voor toekomstige claims)
    ▸ #ontslag-bekendmaking (bestuurder blijft aansprakelijk tot publicatie ontslag)
```

**Cross-cluster**:
- `oprichting-vennootschap` + `financieel-plan` (kapitaalstructuur) — oprichtersaansprakelijkheid-trigger
- `algemene-vergadering` (kapitaalstructuur) — kwijting-besluit + ontslag-beslissing
- `alarmbel-procedure` + `kapitaalbescherming` (kapitaalstructuur) — bestuurder-actie bij netto-actief < helft → relevant voor bestuurdersaansprakelijkheid (niet-naleving = trigger)
- `beroepsaansprakelijkheid` (beroepsbeoefening) — parallel concept: accountant ↔ bestuurder; beide 3 sporen + verzekering
- `bijzondere-mandaten` (controle) — OP-BA.C tantième-controle als bijzonder mandaat
- `faillissement` (insolventie ⏳) — faillissementsaansprakelijkheid-cross + bestuurder-aansprakelijkheid bij verlatenheid

**Schrappen / herleiden tot sub-sectie**:
- `aansprakelijkheid-oprichters-bestuurders` → **gesplitst** in `oprichtersaansprakelijkheid` + `bestuurdersaansprakelijkheid` (`-en-`-naam-smell weg, precedent `vof-commv`)
- `kwijting` blijft sub-sectie van `bestuurdersaansprakelijkheid` (start gebundeld; potentiële split bij content-zwaarte → OP-BA.B)

**Triangulatie 2026-05-26**:
- 16 PO 3.0.II + VII anchors → 0 PO-only gaps
- 3 bestaande records met anker → 4 cluster-eigen records (1 split + 3 behouden waarvan 2 hernoemd via split)
- 1 naam-smell-oplossing (`-en-`-pattern)

**Bronnen-pin**:
- ✅ WVV (boek 5 BV + boek 7 NV + boek 6 CV) — bestuur + belangenconflict + kwijting per vorm
- ⏳ WER boek XX — faillissementsaansprakelijkheid (te valideren als trusted bron)

**Test-case-validatie** (2026-05-26): 3 representatieve PO 3.0.II/VII-examen-vragen:

| Vraag | Concept | Tree-pad | Resultaat |
|---|---|---|---|
| 2008-bibf-vrI3 | Belangenconflict enige vennoot-zaakvoerder BVBA | `belangenconflict-bestuur` (enige-bestuurder-context — kennisgeving aan AV ipv RvB) | ✅ |
| 2008-bibf-vrI5 | Oprichtersaansprakelijkheid BVBA vs NV | `oprichtersaansprakelijkheid` + cross `besloten-vennootschap` + `naamloze-vennootschap` (vergelijking financieel-plan-vereiste) | ✅ (nu écht volledig — split bevestigd nuttig: 2 vormen × 1 fenomeen) |
| 2013-2-vr16 | Toegestaan kapitaal + oprichtersaansprakelijkheid NV | `naamloze-vennootschap` + `oprichtersaansprakelijkheid` + cross `kapitaalverhoging#toegestaan-kapitaal` | ✅ |

Alle 3 passen zonder forceren. **Bevestiging**: split `aansprakelijkheid-oprichters-bestuurders` rechtvaardigt zich — 2 van 3 testvragen raken alleen `oprichtersaansprakelijkheid`, niet bestuurdersaansprakelijkheid.

**Open punten**:
- **OP-BA.A** ✅ Split `-en-`-smell uitgevoerd
- **OP-BA.B** ⏳ `kwijting` als sub-sectie van `bestuurdersaansprakelijkheid` — splitten indien bij content-uitwerking didactisch te zwaar
- **OP-BA.C** ⏳ Tantième-controle (PO 3.0.II.C / VII context) als bijzonder mandaat — flag voor `bijzondere-mandaten`-types-tabel-uitbreiding indien tantième-toekenning systematisch revisor-verslag vereist (te verifiëren bij content-uitwerking)
- **OP-BA.D** ⏳ Vertegenwoordigingsbevoegdheid (3.0.II.B) — sub-sectie van `bestuur-vennootschap` (huidig voorstel) of eigen klein record? Voorlopig sub-sectie (anti-versnippering); split-overweging als WVV-binding-regel substantieel blijkt.

### Vennootschapsgeschillen-cluster

Thema: `vennootschapsgeschillen`. *Thema-cluster vennootschapsrecht (PO 3.0.VIII, 2026-05-26). Klein cluster — 1 bestaand record dat alle 5 anchors dekt. Geen splits, geen renames. Wel een perspectief-verfijning: 3.0.VIII.A ("beroepsbeoefenaar-rol bij geschillen") hoort in `accountant_perspectieven[]`, niet in `inhoud` (toepassing van perspectief-vs-record-principe op intra-record-niveau).*

```
vennootschapsgeschillen                   [thema-cluster vennootschapsrecht, 1 record]
└── vennootschapsgeschillen               [K]
    inhoud:
      ▸ #types-geschillen — deadlocks aandeelhouders · bestuurder-conflicten · besluit-betwistingen (3.0.VIII)
      ▸ #contractuele-preventie — geschillenbedingen · mediation-clausules · arbitrage (3.0.VIII.A)
      ▸ #bewijswaarde-moderne-communicatie — e-mails · online vergaderingen · opnames; authenticiteit + integriteit + verkrijging (3.0.VIII.B)
      ▸ #minnelijke-schikking — duidelijkheid aanspraken · fiscale gevolgen · vertrouwelijkheid · rechtsgeldigheid partijen (3.0.VIII.C)
      ▸ #nietigheid-besluiten — gronden (procedurefouten · machtsmisbruik · strijd statuten/wet) + gevolgen (3.0.VIII.D)
    accountant_perspectieven:
      ▸ audit — kennisname bij audit (lopende geschillen → potentiële voorzieningen + disclosure); audit van betrokken contracten
      ▸ advies — contractuele preventie + bewijs-discipline + minnelijke-schikking-begeleiding
      ▸ beroep-en-deontologie — beroepsgeheim bij confrontatie + conflict-of-interest bewaking + bewijsverzameling-grenzen (3.0.VIII.A)
```

**Cross-cluster**:
- `algemene-vergadering` (kapitaalstructuur) — nietigheid AV-besluit (VIII.D)
- `bestuur-vennootschap` (bestuur-en-aansprakelijkheid) — nietigheid RvB-besluit + bestuurder-conflicten
- `aandeelhoudersovereenkomsten` (kapitaalstructuur) — geschillenbedingen vaak hierin
- `beroepsgeheim` (beroepsbeoefening) — beroepsbeoefenaar-rol bij geschillen
- `onafhankelijkheid` (beroepsbeoefening) — conflict-of-interest bij geschillen

**Triangulatie 2026-05-26**:
- 5 PO 3.0.VIII anchors → 0 PO-only gaps
- 1 bestaand record dekt alle anchors (vennootschapsgeschillen) — geen herstructurering nodig
- Perspectief-verfijning: VIII.A verhuist van inhoud-sub-sectie naar `accountant_perspectieven[]` (geen inhoudelijke verandering, wel structurele)

**Bronnen-pin**:
- ✅ WVV (algemene-vergadering-procedure + nietigheidsgronden, boek 2)
- ⏳ Gerechtelijk Wetboek (bewijswaarde + minnelijke-schikking-mechaniek)
- ⏳ Wet 21 februari 2005 (mediation) + WVV-specifieke arbitrage

**Test-case-validatie** (kort — klein cluster):
- 2003-bibf-vrK1 + 2008-bibf-vrK2 (overdracht dossier confraters, ronselen) raken `vennootschapsgeschillen` slechts indirect — primair beroepsbeoefening. Geen specifieke PO 3.0.VIII-testvraag in `_programmaonderdeel_classificatie.json` opgemerkt; mogelijk afgedekt door 2013-1-vr14 (aandeelhouderschap BVBA bij overlijden — deadlock-context).

**Open punten**:
- **OP-VG.A** ⏳ Mediation/arbitrage als sub-sectie of als eigen procedure-records (cross naar `gerechtelijke-reorganisatie` voor pre-insolventie-bemiddeling)? Voorlopig sub-sectie.
- **OP-VG.B** ⏳ Tantième-betwisting als specifiek geschil-type (cross naar `bestuurdersaansprakelijkheid#kwijting`)? Mogelijk sub-sectie indien examen-relevant.

### Insolventie-cluster

Thema: `insolventie`. *Thema-cluster vennootschapsrecht/economisch-recht (PO 3.0.IX + X, 2026-05-26). Combineert ontbinding-vereffening (WVV) + insolventiewetgeving (WER boek XX). Cluster-naam `insolventie` is iets enger dan inhoud (ontbinding kan ook gezonde-venn-context zijn — vrijwillige ontbinding), maar volgt PO-groepering + de top-level snapshot ⏳-marker.*

```
insolventie                              [thema-cluster, 7 records — PO 3.0.IX + X]
│
├── insolventierecht-wer-boek-xx         [K — overkoepelend kader]
│   ▸ WER boek XX als framework — 3 hoofdprocedures: gerechtelijke-reorganisatie · faillissement · vereffening (gerechtelijk)
│   ▸ #ondernemingsrechtbank — bevoegdheid · samenstelling
│   ▸ #regsol — centraal digitaal platform voor insolventieprocedures
│   ▸ #insolventiefunctionarissen — curator · gerechtelijke bewindvoerder · ondernemingsbemiddelaar
│   ▸ #ondernemingen-in-moeilijkheden — knipperlichten + signalen (cross naar kamers-voor-ondernemingen-in-moeilijkheden)
├── kamers-voor-ondernemingen-in-moeilijkheden  [R-procedure]
│   ▸ vroegtijdige opsporing via signalen (CAW: ontoereikende continuïteit · niet-betaalde RSZ/BTW · ...)
│   ▸ rol gecertificeerd-accountant: meldingsplicht bij vaststellingen — cross naar antiwitwaspreventie-systematiek
│   ▸ confidentiële bemiddeling vóór formele procedure
├── ondernemingsbemiddelaar              [E-actor]
│   ▸ neutrale tussenpersoon door rechtbank aangesteld
│   ▸ buitengerechtelijke fase · vertrouwelijkheid · doel: minnelijk akkoord
│   ▸ onderscheid met curator/bewindvoerder
├── gerechtelijke-reorganisatie          [R-procedure]
│   ▸ adempauze + opschorting tegen schuldeisers
│   ▸ 3 modaliteiten: individueel akkoord (afspraak met schuldeisers individueel) · collectief akkoord (plan goedgekeurd door meerderheid) · overdracht onder gerechtelijk gezag (verkoop ondernemings(deel))
│   ▸ voorwaarden + procedure + gevolgen + termijnen
│   ▸ cross naar bestuurdersaansprakelijkheid (verlatenheid → aansprakelijkheid)
├── faillissement                        [R-procedure, NIEUW]
│   ▸ voorwaarden: duurzame staking van betaling + geschokt krediet
│   ▸ procedure: aangifte (door schuldenaar of dagvaarding door schuldeiser/openbaar ministerie) · vonnis · publicatie
│   ▸ curator-aanstelling: beheer boedel · realisatie activa · uitkering schuldeisers volgens rangorde (voorrechten, hypotheken, ...)
│   ▸ termijnen: aangifte schuldvorderingen · sluiting · doorhaling
│   ▸ #faillissementsaansprakelijkheid (cross naar bestuurdersaansprakelijkheid#faillissementsaansprakelijkheid)
│   ▸ verschoonbaarheid (natuurlijk persoon) → cross rehabilitatie
├── ontbinding-en-vereffening            [G+R, breder dan alleen insolventie]
│   ▸ vrijwillige ontbinding (AV-besluit, WVV) vs gerechtelijke vereffening (WER boek XX)
│   ▸ vereffenaar-aanstelling (statutair of door AV; bij gerechtelijke vereffening door rechtbank)
│   ▸ procedure: vereffeningsbesluit → staat van actief en passief → realisatie activa → betaling schuldeisers → saldo aan aandeelhouders → afsluiting + doorhaling
│   ▸ #boekenstaat-bij-ontbinding (cross naar bijzondere-mandaten — staat A/P + continuïteits-evaluatie door accountant)
│   ▸ #vereffenaarsaansprakelijkheid (PO 3.0.IX.B — plichten + sancties)
│   ▸ context: bij gezonde venn (uitkering aandeelhouders) vs insolvente venn (overgang naar faillissement)
└── rehabilitatie-en-beroepsverbod       [R — `-en-`-smell, behouden tot content-uitwerking]
    ▸ #rehabilitatie — natuurlijke persoon na faillissement: rechten herwinnen na bepaalde periode + voorwaarden
    ▸ #beroepsverbod — verbod uit te oefenen + procedure tot opheffing (cross naar tuchtprocedure-itaa)
    ▸ Splits-overweging: 2 fenomenen onder 1 naam (rehabilitatie = positief, beroepsverbod = negatief); WVV-context wel verwant. Behouden tot content-uitwerking duidelijk maakt of split nodig.
```

**Cross-cluster**:
- `bestuurdersaansprakelijkheid` (bestuur-en-aansprakelijkheid) — faillissementsaansprakelijkheid + verlatenheid
- `alarmbel-procedure` + `kapitaalbescherming` (kapitaalstructuur) — pre-insolventie-signalen
- `bijzondere-mandaten` (controle) — boekenstaat-bij-ontbinding als bijzonder mandaat (ITAA-norm-ontbinding-vereffening)
- `algemene-vergadering` (kapitaalstructuur) — ontbindingsbesluit + vereffenaar-aanstelling
- `antiwitwaspreventie` (beroepsbeoefening) — meldingsplicht-systematiek raakt kamers-voor-ondernemingen-in-moeilijkheden
- `tuchtprocedure-itaa` (beroepsbeoefening) — beroepsverbod-mechaniek-parallel
- `commissaris` (beroepsbeoefening ⏳) — continuïteits-attest bij alarmbel

**Schrappen / nieuwe records**:
- `faillissement` **nieuw record** te creëren (kandidaat in DB, nog niet gerealiseerd — daemon-blocker geldt voor uitvoering, mapping-fase werk)
- Geen renames/splits in deze ronde — `rehabilitatie-en-beroepsverbod` blijft (split-overweging open)

**Triangulatie 2026-05-26**:
- 10 PO 3.0.IX + X anchors → 0 PO-only gaps
- 6 bestaande records + 1 kandidaat → 7 cluster-eigen records
- Geen herstructurering naast `faillissement`-creatie
- Cross-relatie naar `bijzondere-mandaten` is kritisch (ontbinding-boekenstaat = expliciet voorbeeld bijzonder mandaat)

**Bronnen-pin**:
- ✅ WER boek XX (insolventie) — primair, te valideren in resources
- ✅ ITAA-norm-ontbinding-vereffening (trusted) — voor accountant-rol bij ontbinding
- ✅ WVV (boek 2 titel 8) — ontbinding-vereffening per vorm

**Test-case-validatie** (2026-05-26):

| Vraag | Concept | Tree-pad | Resultaat |
|---|---|---|---|
| 2013-1-vr16 | externe accountant bij ontbinding | `ontbinding-en-vereffening#boekenstaat-bij-ontbinding` + cross `bijzondere-mandaten` (categorisch) + cross `continuiteit-going-concern` | ✅ |
| 2015-1-vr54 | Vereffening NV TRIAL + onafhankelijkheid + AWW | `ontbinding-en-vereffening` + cross `onafhankelijkheid` + `antiwitwaspreventie#cliëntenonderzoek` | ✅ |
| (PO 3.0.X.D vragen) | GRP-procedure | `gerechtelijke-reorganisatie` (3 modaliteiten) + cross `faillissement` (alternatief uitkomst) | ✅ |

**Open punten**:
- **OP-INS.A** ⏳ `rehabilitatie-en-beroepsverbod`-split te beslissen bij content-uitwerking (rehabilitatie = positief; beroepsverbod = negatief; verwant in WVV-context maar conceptueel apart)
- **OP-INS.B** ⏳ `faillissement` als nieuw record creëren — wacht op daemon-fix (Fase 1.0 BLOCKER)
- **OP-INS.C** ⏳ `boekenstaat-bij-ontbinding` als sub-sectie van `ontbinding-en-vereffening` (huidig) vs eigen klein record? Voorlopig sub-sectie (anti-versnippering); split-overweging als verslag-format substantieel detail vereist
- **OP-INS.D** ⏳ Verschoonbaarheid (faillissement natuurlijk persoon) als sub-sectie van `faillissement` vs cross-link naar `rehabilitatie-en-beroepsverbod#rehabilitatie`? Mogelijk dubbel-flag in beide records.

### Winstuitkering-cluster

Thema: `winstuitkering`. *Thema-cluster (PO 3.0.IV.B + cross PO 2.3 VenB-mechanismen + cross PO 2.1 RV-PB, 2026-05-26). Σ-cluster: keuzekader voor uitkeringsvormen. Materialiseert mapping-actie uit rationale-log 2026-05-24 (`kapitaalbescherming-en-winstverdeling` splitsen). Lost OP-K.4 op (winstbestemming positionering).*

```
winstuitkering                            [Σ-cluster, 3 records — PO 3.0.IV.B + cross 2.3 + 2.1]
│
├── winstuitkering                        [R, Σ-hoofdrecord — NIEUW; absorbeert winstverdeling-deel van `kapitaalbescherming-en-winstverdeling`]
│   ▸ overkoepelend keuzekader: hoe geeft venn winst aan aandeelhouders?
│   ▸ #vergelijkingsmatrix-uitkeringsvormen:
│       - dividend (regulier — AV-besluit · RV 30%)
│       - tussentijdse/interim dividenden (op tussentijdse staat · dubbele test BV/NV)
│       - tantième (winstgebonden bestuurdersvergoeding · cross werknemers-vergoedingen)
│       - inkoop eigen aandelen (alternatief — uittreding-uitkering · cross kapitaalstructuur)
│       - liquidatie-uitkering (eind-uitkering · cross fiscale-voordelen + insolventie)
│       - liquidatiereserve (= "voorgekookte liquidatie" via VenB · cross fiscale-voordelen)
│       - VVPR-bis (verlaagd RV-tarief voor kleine venn · cross fiscale-voordelen)
│   ▸ keuze-criteria: RV-tarief · timing · winstbestemmings-volgorde · netto-actief-test
│   ▸ #wettelijke-beperkingen — netto-actief-test (BV/NV) + uitkeringstest (BV ⚠️ dubbele test sinds WVV)
│   ▸ #av-procedure — winstbestemmings-besluit
│   ▸ absorbeert `uitkering-aan-aandeelhouders`-content (bestaand record, mogelijk hernoemen naar dit cluster-Σ)
│
├── winstbestemming                       [G+R, NIEUW — opent OP-K.4]
│   ▸ AV-besluit jaarrekening + winstbestemming (na goedkeuring jaarrekening)
│   ▸ #wettelijke-reserve — 5% tot 10% van kapitaal/eigen-vermogen bereikt (verplichte aanleg)
│   ▸ #vrije-reserves — statutair vrij + AV-besluit
│   ▸ #overgedragen-resultaat — naar volgend boekjaar
│   ▸ #tantième-toekenning — winstgebonden bestuurdersvergoeding (cross naar tantième-record)
│   ▸ #dividend-toewijzing — saldo naar dividend (regulier of interim)
│   ▸ wettelijke volgorde: wettelijke reserve eerst · dan andere · dan dividend/overdracht
│
└── tantième                              [G+R, NIEUW losstaand record — primair-thema-keuze 2026-05-24]
    ▸ winstgebonden vergoeding toegekend door AV bij winstbestemming aan bestuurder(s)
    ▸ aftrekbaarheidsregel ⚠️: aftrekbaar in het boekjaar waarop het betrekking heeft (mits AV-besluit en boeking binnen termijn) — speciale aftrekbaarheidsregel ten opzichte van gewone bestuurderskosten
    ▸ belastbaar als bedrijfsleidersbezoldiging in PB (categorie bedrijfsleider)
    ▸ #cao-90-bonus afbakening (niet hetzelfde — CAO 90 is werknemersbonus, geen tantième)
    ▸ secundair thema: werknemers-vergoedingen (als lid van bedrijfsleidersbezoldiging-Σ)
    ▸ cross: bedrijfsleidersbezoldiging (bouwblok) · winstbestemming (toekenningsmoment) · KMO-tarief-VenB (45.000-EUR-regel-context)
```

**Cross-cluster** (records met primair-thuis elders, thema-shared winstuitkering):
- `liquidatiereserve` (fiscale-voordelen-vennootschap ⏳) — VenB-mechanisme (10% afzonderlijke heffing → later 5% RV bij uitkering)
- `vvprbis` (fiscale-voordelen-vennootschap ⏳) — verlaagd RV-tarief 15% voor kleine venn met nieuw kapitaal na 3j wachtperiode
- `inkoop-eigen-aandelen` (kapitaalstructuur) — alternatief uitkeringsvorm
- `kapitaalvermindering` (kapitaalstructuur) — pro-rata-toerekening (winstverdeling-aspect)
- `bedrijfsleidersbezoldiging` (werknemers-vergoedingen) — bevat tantième als bouwblok
- `kapitaalbescherming` (kapitaalstructuur ⏳ OP-K.5) — netto-actief-test + uitkeringstest = wettelijke beperking op winstuitkering

**Mapping-acties** (materialisatie rationale-log 2026-05-24):
- `kapitaalbescherming-en-winstverdeling` → **splitsen**: kapitaalbescherming-deel naar `kapitaalbescherming` (kapitaalstructuur, OP-K.5); winstverdeling-deel absorbed in `winstuitkering` (Σ-hoofdrecord)
- `uitkering-aan-aandeelhouders` → mogelijk hernoemen naar `winstuitkering` (Σ-overzicht) en absorbeert; of behouden als sub-record voor reguliere dividend-vorm. Beslissing bij content-uitwerking (OP-WU.A)

**Schrappen / nieuwe records**:
- 2 nieuwe records: `winstbestemming` + `tantième` (losstaand — was niet als record, alleen vermeld in werknemers-vergoedingen-cluster)
- 1 nieuw Σ-record `winstuitkering` (vervangt + absorbeert)
- 1 split (`kapitaalbescherming-en-winstverdeling` → 2)

**Triangulatie 2026-05-26**:
- PO 3.0.IV.B + cross 2.3 (VenB-mechanismen) + cross 2.1 (RV PB)
- 2 bestaande records met directe relevantie (`uitkering-aan-aandeelhouders`, `kapitaalbescherming-en-winstverdeling`) + 2 fiscale records cross (`liquidatiereserve`, `vvprbis`) → 3 cluster-eigen records (Σ + 2 nieuwe) + 4 cross
- Opent open punten `tussentijdse-dividenden` (was kandidaat ⏳ uit kapitaalstructuur-triangulatie 2026-05-24) — als sub-sectie van Σ ipv eigen record (anti-versnippering)

**Bronnen-pin**:
- ✅ WVV (boek 5 BV + boek 7 NV — winstbestemming + uitkeringsbeperkingen)
- ✅ WIB (Wetboek Inkomstenbelasting) — RV-tarieven · liquidatiereserve · VVPR-bis (cross fiscale-voordelen)
- ⏳ KB ter uitvoering WIB (RV-modaliteiten)

**Test-case-validatie**: te doen — gerelateerde examen-vragen rond dividend-uitkering + winstbestemming nog niet specifiek opgezocht; over te slaan deze ronde (klein-cluster precedent).

**Open punten**:
- **OP-WU.A** ⏳ `uitkering-aan-aandeelhouders` (bestaand) — hernoemen naar `winstuitkering`-Σ of behouden als sub-record voor regulier-dividend? Content-uitwerking-beslissing
- **OP-WU.B** ⏳ `tussentijdse-dividenden` als sub-sectie van Σ (huidig) of eigen record? Voorlopig sub-sectie (anti-versnippering); split bij content-zwaarte (BV-mechaniek substantieel verschillend van NV)
- **OP-WU.C** ⏳ `winstbestemming`-positionering — eigen record (huidig) of sub-sectie van `winstuitkering`-Σ? Voorlopig eigen want AV-procedure + wettelijke reserve substantieel; cross-link in Σ
- **OP-WU.D** ⏳ `dividend-uitkering` als eigen record creëren? Voorlopig: regulier dividend = sub-sectie van Σ + RV-aspecten in `uitkering-aan-aandeelhouders` hernoemd. Splitsen indien content-zwaarte rechtvaardigt

### Reorganisatie-cluster

Thema: `reorganisatie`. *Σ-cluster (cross PO 3.0.taak.2 + 3.0.taak.3 + 2.3.III.B + 2.8.XVI + 1.4.II.A/D, 2026-05-26). Vennootschapsrechtelijke reorganisaties + fiscale neutraliteit. Cross-cluster met `bijzondere-mandaten` (revisor-verslag-vereisten per type) + `overdracht-onderneming` (alternatieve structurering).*

```
reorganisatie                             [Σ-cluster, 4 records]
│
├── reorganisatie                         [R, Σ-hoofdrecord — NIEUW]
│   ▸ overkoepelend keuzekader voor herstructureringen
│   ▸ #vergelijkingsmatrix-modaliteiten:
│       - fusie (door overneming · door oprichting · zuster-fusie)
│       - splitsing (door overneming · door oprichting · partiële-splitsing)
│       - inbreng-bedrijfstak-of-algemeenheid (alternatieve structurering — cross naar Geb-record)
│       - omzetting (cross naar omzetting-vennootschap)
│       - geruisloze fusie (vereenvoudigde procedure dochter)
│   ▸ #fiscale-neutraliteit (cross naar fiscale-fusie-splitsing) — voorwaarden voor vrijstelling realisatie meerwaarden
│   ▸ #wettelijke-procedure (WVV boek 12) — voorstel-tot-fusie · revisor-verslag · AV-besluit · notariële akte · publicatie
│   ▸ #bijzonder-mandaat (cross naar bijzondere-mandaten) — controle ruilverhouding + waardering inbreng
│   ▸ keuze-criteria: fiscale impact · operationele context · timing · arbeidsrecht (CAO 32bis)
│
├── fusie                                 [G+R, bestaand]
│   ▸ 3 modaliteiten (overneming · oprichting · zuster) · uitwisseling aandelen · ruilverhouding
│   ▸ algemene rechtsopvolging — automatische overgang activa+passiva
│   ▸ revisor-verslag (cross bijzondere-mandaten + ITAA-norm-fusie-splitsing)
│   ▸ accountant_perspectieven[].audit: bijzonder mandaat controle ruilverhouding
│
├── splitsing                             [G+R, bestaand]
│   ▸ 3 modaliteiten: zuivere splitsing (oude venn verdwijnt → 2 nieuwe) · door overneming · partiële splitsing (deel-vermogen naar bestaande/nieuwe venn)
│   ▸ partiële splitsing onderscheid met inbreng-bedrijfstak: rechts-opvolging vs contractuele inbreng
│   ▸ accountant_perspectieven[].audit: bijzonder mandaat
│
└── fiscale-fusie-splitsing               [R, bestaand]
    ▸ fiscale neutraliteit-regime VenB — vrijstelling realisatie meerwaarden mits voorwaarden
    ▸ #voorwaarden: continuïteit · bedrijfsmatige redenen (anti-misbruik) · binnen-EU
    ▸ EU fusierichtlijn (cross naar fiscale-fusierichtlijn voor grensoverschrijdend)
    ▸ #latente belasting overdracht (overgenomen venn neemt fiscale schoenen over)
    ▸ cross-thema: anti-misbruik (motivering-toets) ⏳
```

**Cross-cluster** (records met primair-thuis elders):
- `inbreng-van-bedrijfstak-of-algemeenheid` (kapitaalstructuur) — verwante structureringsvorm; cross-thema reorganisatie
- `omzetting-vennootschap` (ondernemingsvormen — bestaand-record? te checken) — vorm-wissel binnen zelfde rechtspersoon
- `overdracht-onderneming` (overdracht-onderneming-cluster) — alternatieve route (share-deal/asset-deal)
- `bijzondere-mandaten` (controle) — categorisch begrip; fusie/splitsing zijn types
- `fiscale-aandachtspunten-herstructurering` (fiscale-voordelen-vennootschap ⏳?) — pre-/post-deal fiscale due diligence
- `fiscale-fusierichtlijn` (cross PO 2.8) — grensoverschrijdend EU
- `gerechtelijke-reorganisatie` (insolventie) — andere context (insolventie-aanloop, niet vrijwillige reorganisatie); naam-overlap maar conceptueel verschillend (te flaggen via cross-relatie + scope.out)

**Schrappen / nieuwe records**:
- 1 nieuw Σ-record `reorganisatie` (overkoepelend)
- Bestaande records behouden: `fusie`, `splitsing`, `fiscale-fusie-splitsing`
- Splits-overweging: `fusie` × 3 modaliteiten (overneming/oprichting/zuster) — voorlopig sub-secties (anti-versnippering)
- Idem `splitsing` × 3 modaliteiten — voorlopig sub-secties; **partiële-splitsing** mogelijk eigen record indien substantieel (cross naar inbreng-bedrijfstak)

**Triangulatie 2026-05-26**:
- Cross PO 3.0.taak.2 (overdracht/ontbinding) + 3.0.taak.3 (bijzondere mandaten) + 2.3.III.B (VenB-fusie/splitsing) + 2.8.XVI (EU-fusierichtlijn) + 1.4.II.A/D (consolidatie-context)
- 4 bestaande records + 1 nieuw Σ = 5; netto cluster-eigen = 4 (incl. Σ)
- Geen split, geen rename

**Bronnen-pin**:
- ✅ WVV boek 12 (vennootschapsrechtelijke reorganisaties)
- ✅ ITAA-norm-fusie-splitsing (trusted) — bijzonder-mandaat-context
- ✅ WIB art 211 ev (fiscale neutraliteit)
- ✅ EU Fusierichtlijn 2009/133/EG

**Mapping-actie OP-EC.E** voor `fusie` + `splitsing`:
- `accountant_perspectieven[].audit` met cross-link naar `bijzondere-mandaten`
- ITAA-norm-fusie-splitsing pin
- Oordeel-onderwerp: ruilverhouding + waardering inbreng

**Open punten**:
- **OP-RE.A** ⏳ `partiële-splitsing` als sub-sectie van `splitsing` (huidig) of eigen record (cross naar `inbreng-bedrijfstak`)? Substantie-vraag bij content-uitwerking
- **OP-RE.B** ⏳ `geruisloze-fusie` (vereenvoudigde dochter-fusie) als eigen record of sub-sectie van `fusie`? Voorlopig sub-sectie
- **OP-RE.C** ⏳ `gerechtelijke-reorganisatie` vs `reorganisatie` — naam-overlap maar conceptueel verschillend (insolventie-context vs vrijwillig). Scope.out + cross-relatie volstaat; geen rename nodig

### Fiscale-voordelen-vennootschap-cluster

Thema: `fiscale-voordelen-vennootschap`. *Σ-cluster (cross PO 2.3.II + 2.3.III + 2.3.taak.3, 2026-05-26). VenB-tarief-modulerende aftrekken + regimes. Absorbeert `liquidatiereserve` + `vvprbis` als primaire-thuis (waren cross-thema winstuitkering). Lost open punt OP-K.6 op (`meerwaarde-aandelen-venb` als eigen record bevestigd).*

```
fiscale-voordelen-vennootschap            [Σ-cluster, 10 records — cross PO 2.3]
│
├── fiscale-voordelen-vennootschap        [Σ-hoofdrecord — NIEUW]
│   ▸ overkoepelend keuzekader VenB-tarief-modulatie
│   ▸ #vergelijkingsmatrix: KMO-tarief · DBI · NIA · innovatie · investering · gespreide-belasting · liquidatiereserve · VVPR-bis · meerwaarde-aandelen
│   ▸ #aftrek-volgorde (fiscaal vastgelegde sequentie: art 207 WIB — DBI → innovatie → investering → overgedragen verliezen → NIA → gespreide belastingen → ...)
│   ▸ #korf-regime sinds 2018 (beperking aftrekken boven 1.000.000€)
│   ▸ keuze-criteria: voorwaarden · plafonds · termijnen · combineerbaarheid
│
├── verlaagd-tarief-kleine-vennootschap   [R]               KMO-tarief 20% eerste schijf 100k · voorwaarden kleine venn + 45.000-EUR-bezoldiging
├── dbi-aftrek                            [R, ⏳ NIEUW]      aftrek Definitief Belaste Inkomsten — dividenden uit gekwalificeerde deelnemingen 100% vrijstelling
├── notionele-interestaftrek              [R]               afgeschaft 2024 · nog relevant voor overdracht restant + examen-historiek
├── innovatie-aftrek                      [R, ⏳ NIEUW]      85% vrijstelling netto-octrooi-inkomsten (oude: octrooi-aftrek 80%)
├── investeringsaftrek                    [R]               verhoogde percentages per categorie · eenmalig vs gespreid · KMO-tarief
├── gespreide-belasting-meerwaarden       [R, ⏳ NIEUW]      art 47 WIB — herinvestering binnen termijn = gespreide belasting
├── liquidatiereserve                     [R]               10% afzonderlijke heffing nu + 5% RV bij uitkering ≥ 5j (anti-liquidatie-tarief uitwijking)
├── vvprbis                               [R]               15% RV nieuw kapitaal kleine venn · 3j wachtperiode
└── meerwaarde-aandelen-venb              [R]               (lost OP-K.6 op — eigen record bevestigd) vrijstelling onder voorwaarden · houdperiode · onderworpenheid · taxatie 25%/40% bij niet-naleving
```

**Cross-cluster**:
- `vennootschap-groottecategorieen` (ondernemingsvormen) — bepaalt KMO-tarief-toepasselijkheid
- `winstuitkering` — `liquidatiereserve` + `vvprbis` thema-shared
- `aandeel` (kapitaalstructuur) — `meerwaarde-aandelen-venb` is fiscale dimensie van aandeel
- `eigen-vermogen` (kapitaalstructuur) — NIA-historisch (afgeschaft maar grondslag was eigen-vermogen)
- `dividend-uitkering` (winstuitkering) — DBI raakt ontvangen dividenden bij deelnemingen
- `kapitaalverhoging` (kapitaalstructuur) — VVPR-bis triggert bij nieuw kapitaal
- `reorganisatie` — `fiscale-fusie-splitsing` is verwante neutraliteits-regeling (apart cluster)
- `aangifte-vennootschapsbelasting` — uitvoeringscontext van aftrek-volgorde
- `anti-misbruik` ⏳ — voorwaarden + motivering bij aftrekken (algemene anti-misbruik-bepaling)

**Schrappen / nieuwe records**:
- 4 nieuwe records: `fiscale-voordelen-vennootschap` (Σ) + `dbi-aftrek` + `innovatie-aftrek` + `gespreide-belasting-meerwaarden`
- 6 bestaande records absorberen als leden van Σ (geen rename, geen split)

**Triangulatie 2026-05-26**:
- Cross PO 2.3.II (VenB-aftrekken) + 2.3.III (fiscale verrichtingen) + 2.3.taak.3 (advies)
- 6 bestaande regimes + 4 nieuwe = 10 cluster-eigen
- Lost OP-K.6 (`meerwaarde-aandelen-venb`) op — eigen record bevestigd via Σ-positionering

**Bronnen-pin**:
- ✅ WIB art 192-217 (VenB-tarief + aftrekken + meerwaarden)
- ✅ KB-WIB (uitvoeringsbesluiten)
- ⏳ Circulaires en parl. vragen (interpretatieve bronnen)

**Open punten**:
- **OP-FV.A** ⏳ `notionele-interestaftrek` na 2024-afschaffing — behouden als historisch record (overgangsregime + examen-stof) of legacy-archiveren? Voorlopig behouden.
- **OP-FV.B** ⏳ `korf-regime` (aftrek-beperking) als eigen sub-sectie van Σ vs eigen record? Voorlopig sub-sectie
- **OP-FV.C** ⏳ Aftrek-volgorde (art 207 WIB) als zelfstandig algoritme/K-techniek-record? Voorlopig sub-sectie in Σ (anti-versnippering)

### Anti-misbruik-cluster

Thema: `anti-misbruik`. *Σ-cluster (cross PO 2.1.IX.B + 2.8.XVI + 2.8.XVII + 2.8.taak.3, 2026-05-26). Fiscale anti-misbruik-toolbox van de overheid + EU. Bestrijken: algemene anti-misbruik (AAMB) · simulatie · TP-correcties · thin-cap/ATAD · misbruik-bestrijdingsmaatregelen.*

```
anti-misbruik                             [Σ-cluster, 6 records — cross PO 2.1 + 2.8]
│
├── anti-misbruik                         [Σ-hoofdrecord — NIEUW]
│   ▸ overkoepelend keuzekader: hoe bestrijdt fiscus kunstmatige constructies?
│   ▸ #vergelijkingsmatrix-instrumenten: AAMB · simulatie-leer · TP-correcties · thin-cap · CFC-regels · GAAR (EU)
│   ▸ #onderscheid simulatie (rechtshandeling niet wat ze lijkt) vs ABM-fiscaal (rechtshandeling echt maar fiscaal misbruik) vs verboden constructies
│   ▸ #bewijslast — fiscus toont gebrek aan niet-fiscale motieven (bedrijfsmatige redenen)
│   ▸ keuze-criteria: aard transactie · grensoverschrijdend · grootte · context
│
├── algemene-anti-misbruik-bepaling       [R]               AAMB art 344§1 WIB — vermoeden van misbruik bij rechtshandeling die fiscaal voordeel als hoofddoel heeft + tegenstrijdig met doel wettekst; bedrijfsmatige redenen als tegenbewijs
├── simulatie-leer                        [R, ⏳ NIEUW]      pre-AAMB-instrument: rechtshandeling wordt geherkwalificeerd op basis van werkelijke bedoeling partijen; smaller toepassingsgebied maar nog actief
├── transfer-pricing                      [K]               arm's length-beginsel · verrekenprijsdocumentatie · masterfile/lokaal dossier/CbCR · OESO-richtlijnen
├── thin-cap-regime                       [R, ⏳ NIEUW]      ATAD-implementatie: interest-aftrekbaarheid-beperking 30% EBITDA / 3M€ drempel (art 198/1 WIB)
├── atad-richtlijn                        [K]               EU-anti-tax-avoidance directive overzicht: GAAR · thin-cap (interest limitation) · CFC · exit-tax · hybride mismatches
└── verboden-constructies                 [R, ⏳ NIEUW?]     specifieke anti-misbruik-bepalingen (bv. 3-jaar-vermoeden art 18 WIB, opname WIB 90 5° voor effecten-omzeiling)
```

**Cross-cluster**:
- `fiscale-voordelen-vennootschap` — AAMB-toets bij aftrekken (bedrijfsmatige redenen)
- `reorganisatie` — neutraliteits-regime vraagt bedrijfsmatige redenen (cross naar AAMB)
- `dividend-uitkering` (winstuitkering) — herkwalificatie verkapte dividenden
- `inkoop-eigen-aandelen` (kapitaalstructuur) — fiscale herkwalificatie als dividend bij niet-naleving
- `quasi-inbreng` (kapitaalstructuur) — anti-misbruik op zichzelf (verkapte natura-inbreng)
- `kapitaalvermindering` (kapitaalstructuur) — pro-rata-toerekening = anti-misbruik
- `verbonden-partijen` (cross-cutting) — TP-context

**Schrappen / nieuwe records**:
- 1 nieuw Σ + 3 nieuwe regimes (simulatie · thin-cap · verboden-constructies)
- 3 bestaande records absorberen als leden

**Triangulatie 2026-05-26**:
- Cross PO 2.1.IX.B (PB-anti-misbruik) + 2.8.XVI (EU-fiscaliteit + ATAD) + 2.8.XVII (anti-misbruik internationaal)
- 3 bestaande + 3 nieuw = 6 cluster-eigen (+ 1 Σ)
- Smell-check: `algemene-anti-misbruik-bepaling`-naam is descriptief lang maar accuraat; behouden

**Bronnen-pin**:
- ✅ WIB art 344 (AAMB) + art 198/1 (thin-cap) + art 18 (3-jaar-vermoeden)
- ✅ ATAD I + II (EU-richtlijnen)
- ✅ OESO TP Guidelines + MLI (cross PO 2.8) — bestaande resources

**Open punten**:
- **OP-AM.A** ⏳ `verboden-constructies` als eigen record (overzichts-cluster van specifieke anti-misbruik-bepalingen) vs sub-sectie van Σ? Voorlopig eigen klein record; te beslissen bij content-uitwerking
- **OP-AM.B** ⏳ `transfer-pricing` is breed (TP-documentatie + masterfile + CbCR) — splits-overweging als sub-onderwerpen zelfstandig substantieel groeien

### Loon-en-payroll-cluster (K-techniek)

Thema: `loon-en-payroll`. *K-techniek-cluster (cross PO 2.1 PB + werknemers-vergoedingen, 2026-05-26). Was al beslist in werknemers-vergoedingen-werk 2026-05-24 (OP-W.2): loon-en-payroll als K-techniek (deterministisch proces, geen Σ-keuze). Hier formeel uitgewerkt.*

```
loon-en-payroll                           [K-techniek-cluster, 1 K-techniek + 10 component-records]
│
├── loon-en-payroll                       [K-techniek-hoofdrecord — NIEUW]
│   ▸ deterministische bruto-naar-netto-flow:
│       bruto-loon → BV → RSZ-werknemer → netto-loon (kant werknemer)
│       bruto-loon + RSZ-werkgever → totale loonkost (kant werkgever)
│   ▸ #flow-overzicht (stap-voor-stap, geen keuzevariant)
│   ▸ #referentie-tabellen (RSZ-percentages, BV-schalen — Cijferzakboekje)
│   ▸ #correcties (werkbonus, fiscale aftrekken)
│   ▸ ITAA-norm permanente vorming-relevantie (compleet payroll-onderwerp)
│
├── bruto-loon                            [R, ⏳ NIEUW]      barema's · maandloon · loonsverhogingen
├── bedrijfsvoorheffing                   [R, bestaand?]   schalen + categorieën + verminderingen — afhouding bij werkgever
├── rsz-werknemer                         [R, ⏳ NIEUW]      13,07% standaard · maandelijkse afhouding
├── rsz-werkgever                         [R, ⏳ NIEUW]      ~25% (sector-afhankelijk) · structurele verminderingen + doelgroep-verminderingen
├── werkbonus                             [R, ⏳ NIEUW]      RSZ-vermindering werknemer + fiscale werkbonus (lage lonen)
├── eindejaarspremie                      [R, ⏳ NIEUW]      sectorale CAO · 1/12 of vast bedrag
├── enkel-en-dubbel-vakantiegeld          [R, ⏳ NIEUW]      bedienden (jaarlijks) vs arbeiders (RJV)
├── dertiende-maand                       [R, ⏳ NIEUW]      sectoraal · onderscheid eindejaarspremie
├── opzegvergoeding                       [R, ⏳ NIEUW]      eenheidsstatuut · termijnen Wet Eenheidsstatuut 2014 · forfait
└── outplacementkost                      [R, ⏳ NIEUW]      werkgever-verplichting bij collectief ontslag + 45+
```

**Cross-cluster** — leden van `werknemers-vergoedingen`-Σ (al vermeld):
- `werknemers-vergoedingen` (parent-Σ-cluster) — alle componenten zijn ook leden van die vergelijkingsmatrix
- `bedrijfsleidersbezoldiging` (werknemers-vergoedingen) — analoog payroll-onderwerp voor bedrijfsleider (geen RSZ-werknemer maar wel BV + sociale bijdragen zelfstandigen)

**Schrappen / nieuwe records**:
- 1 nieuw K-techniek-hoofdrecord + 9 component-records (deels bestaand, deels nieuw)
- Mogelijk `bedrijfsvoorheffing` bestaat al — te valideren

**Triangulatie 2026-05-26**:
- Cross PO 2.1 (PB-bezoldigingen + BV) + werknemers-vergoedingen (al uitgewerkt)
- Klein cluster qua hoofdrecord; veel ⏳-componenten (mapping-fase werk)

**Open punten**:
- **OP-LP.A** ⏳ Hoeveel van de 10 component-records bestaat al vs nieuw? Te scannen
- **OP-LP.B** ⏳ Splits `enkel-en-dubbel-vakantiegeld` (`-en-`-smell?) — voorlopig 1 record want gedeelde regeling

### Overige sub-Kaders van controle-discipline (compact)

*Drie sub-Kaders van `controle` met klein-substantieel volume. Inhoud grotendeels gedragen via `opdracht-types`-Σ (controle-opdracht-cluster) + ITAA-norm-pin per type. Per sub-Kader 1 mini-record voor type-specifieke methodologie/verslag-stijl. Alle delen de fase-cyclus uit `controleopdracht`.*

#### beoordelings-opdracht (sub-Kader, 1 record)

```
beoordelings-opdracht                     [sub-Kader, 1 record]
└── beoordeling-cyclus                    [K-techniek-mini, ⏳ NIEUW]
    ▸ limited assurance · ISRE 2400 (jaarrekening) + ISRE 2410 (tussentijds)
    ▸ negatief geformuleerd oordeel ("Niets is ons onder de aandacht gekomen waaruit blijkt dat ...")
    ▸ scope: voornamelijk navraag + analytische procedures · geen volledig bewijswerk
    ▸ KMO-context: ITAA-KMO-controlenorm deel 2
    ▸ cross: opdracht-types (controle-opdracht) als parent-Σ · controleopdracht voor gemeenschappelijke cyclus · ITAA-KMO-controlenorm
```

#### isae-opdrachten (sub-Kader, 1 record)

```
isae-opdrachten                           [sub-Kader, 1 record]
└── isae-opdracht                         [K-techniek-mini, ⏳ NIEUW]
    ▸ assurance ANDERS DAN jaarrekening-audit
    ▸ voorbeelden: EBITDA-certificatie · prospectus-attest · service-organisatie-rapport (SOC) · duurzaamheidsrapport-assurance
    ▸ ISAE 3000-serie (algemeen 3000 + specifiek 3400-3402)
    ▸ contractuele basis · scope + criteria per opdracht
    ▸ assurance-niveau: redelijke OF beperkte zekerheid (per opdracht)
    ▸ cross: bijzondere-mandaten (sommige bijzondere mandaten zijn ISAE-engagements: bv. EBITDA-attest bij overname)
```

#### overeengekomen-procedures (sub-Kader, 1 record)

```
overeengekomen-procedures                 [sub-Kader, 1 record]
└── overeengekomen-procedures-opdracht    [K-techniek-mini, ⏳ NIEUW]
    ▸ ISRS 4400 — Agreed-upon procedures
    ▸ geen assurance · geen oordeel · alleen feitelijke bevindingen
    ▸ cliënt specificeert procedures vooraf · verslag in vorm feitenrelaas
    ▸ context: due diligence-light · subsidie-controle · specifieke verklaring op vraag bank
    ▸ scope-limitatie: gebruikers zijn alleen partijen die procedures hebben overeengekomen (geen derde-partij-distributie)
```

**Cluster-strategie**: deze 3 sub-Kaders blijven slank — inhoud leeft primair via `opdracht-types`-Σ (controle-opdracht) en cross naar `controleopdracht` (cyclus) + ITAA-normen. Mini-records bevatten alleen type-specifieke afwijkingen. Geen aparte test-case-validatie noodzakelijk — afgedekt door `opdract-types`-Σ-validatie (al 6 test-cases in controle-opdracht-cluster).

**Open punten**:
- **OP-OK.A** ⏳ 3 mini-records (`beoordeling-cyclus`, `isae-opdracht`, `overeengekomen-procedures-opdracht`) wachten op daemon-fix voor creatie (Fase 1.0 BLOCKER). Allemaal kandidaten ⏳.

### Boekhouding-discipline — compact cluster-mapping

Thema: `boekhouding` (top-discipline laag-1). *Compact-mapping voor PO 1.1 (Algemene boekhouding, 29 anchors) + cross PO 1.2 (jaarrekeningrecht) + 1.4 (consolidatie) + 1.5 (correctie/herwerking) + 1.8 (boekhoudkundige expertise) + 1.9 (financiële analyse). Veel content cross-leeft al via uitgewerkte thema-clusters; deze sectie identificeert de **boekhouding-eigen sub-clusters** + verzamelt bestaande records.*

PO 1.1 organiseert zich op **balans-volgorde** (vaste activa → vlottend → eigen vermogen → schulden → resultatenrekening → bijzondere verrichtingen). Veel raakt al cross-uitgewerkte clusters:

| PO 1.1-anker | Inhoud | Primaire cluster |
|---|---|---|
| I.A · I.B | Boekhoudkundige principes + MAR + dubbele boekhouding | **boekhoudbeginselen** (nieuw cluster) |
| II.A | Oprichtingskosten | absorbed in `oprichting-vennootschap` (kapitaalstructuur) |
| II.B-D | Immateriële/materiële/financiële vaste activa + afschrijvingen | **vaste-activa** (nieuw cluster) |
| II.E | Voorraden | **voorraden-vorderingen** (nieuw cluster) |
| II.F | Bedrijfsvorderingen + waardecorrecties | idem |
| II.G | Geldbeleggingen + liquide middelen | **liquide-middelen-en-effecten** (mini-cluster) |
| II.H | Eigen middelen | ✅ `kapitaalstructuur`-cluster (al uitgewerkt) |
| II.I | Voorzieningen + uitgestelde belastingen | **voorzieningen-en-overlopende** (cluster) |
| II.J-K | Schulden lange + korte termijn | ✅ `schuldfinanciering`-cluster (al uitgewerkt) |
| II.L | Overlopende rekeningen | idem voorzieningen-en-overlopende |
| II.M | Bedrijfskosten + bezoldigingen | ✅ `werknemers-vergoedingen` + `loon-en-payroll` |
| II.N | Bedrijfsopbrengsten | **resultatenrekening-boekhouding** (cluster) |
| II.O · II.P | Financiële + niet-recurrente verrichtingen | idem |
| II.Q | Winstbestemming | ✅ `winstuitkering`-cluster (al uitgewerkt) |
| II.R | Rechten + verplichtingen (off-balance) | sub-sectie of klein record `niet-in-balans-rechten-en-verplichtingen` (bestaand) |
| II.S | Synthesedocumenten (jaarrekening) | **jaarrekening-en-synthesedocumenten** (cluster) |
| II.T | Kapitaalwijzigingen + fusies + splitsingen + overnames + vereffeningen | ✅ `kapitaalstructuur` + `reorganisatie` + `overdracht-onderneming` + `insolventie` (al uitgewerkt) |
| II.U | Beheer eigen aandelen | ✅ `kapitaalstructuur` (inkoop-eigen-aandelen) |
| II.V | Obligatieleningen | ✅ `schuldfinanciering` |
| II.W | Leasing | ✅ `schuldfinanciering` + `mobiliteit` |
| II.X | Opsplitsing eigendom (vruchtgebruik/naakte eigendom) | **opsplitsing-eigendom** (mini-cluster, 1 record) |

#### Boekhouding-eigen clusters (nieuw of compact)

```
boekhoudbeginselen                        [cluster, ~4 records — PO 1.1.I.A + I.B + taak.1]
├── boekhoudbeginselen                   [K — bestaand]    voorzichtigheid · continuïteit · matching · realisatie · consistentie
├── bgaap                                [K — bestaand]    Belgische GAAP — wettelijk kader (KB 29-04-2019 + BCBoekhouding-regels)
├── dubbele-boekhouding                  [K — bestaand]    debet/credit + journaal/grootboek + balans/resultatenrekening
└── be-gaap-vs-ifrs-verschillen          [K — bestaand]    vergelijking met IFRS (waardering · presentatie · keuze)

vaste-activa                              [Σ-cluster, ~5 records — PO 1.1.II.A-D]
├── vaste-activa                         [Σ — NIEUW]       overkoepelend keuzekader · afschrijvings-methodologie · waardeverminderingen · herwaardering
├── immateriele-vaste-activa             [E+balanspost — bestaand]   goodwill · ontwikkelingskosten · concessies · merken
├── materiele-vaste-activa               [E+balanspost — bestaand]   gebouwen · machines · meubilair · rollend materieel
├── deelneming-financieel-vast-actief    [E+instrument — bestaand]   participatie ≥ 10% · waardering kostprijs vs vermogensmutatie
└── herwaardering-vast-actief            [G+R — bestaand]  uitzonderlijke waardestijging · herwaarderingsmeerwaarde in eigen vermogen

voorraden-vorderingen                     [cluster, ~4 records — PO 1.1.II.E-F]
├── voorraden                            [E+balanspost — ⏳ NIEUW]   FIFO/LIFO/gewogen gemiddelde · waardecorrecties · onderhanden werk
├── handelsvorderingen                   [E+balanspost — bestaand]   waardeverminderingen · oninbaarheid · ageing
├── vorderingen-op-meer-dan-een-jaar     [E+balanspost — bestaand]   discontering · presentatie balans
└── (cyclus-analyse#aankoopcyclus + #verkoopcyclus shared van interne-controle)

liquide-middelen-en-effecten              [mini-cluster, 1 record — PO 1.1.II.G]
└── geldbeleggingen-en-liquide-middelen  [E+balanspost — bestaand]   kasgeld · banken · termijnrekeningen · korte-termijn-effecten

voorzieningen-en-overlopende              [cluster, ~3 records — PO 1.1.II.I + L]
├── voorzieningen-en-uitgestelde-belastingen [E+R — bestaand]   pensioen · grote herstellingen · litigatie · UB
├── overlopende-rekeningen               [E+balanspost — bestaand]   accrual-principe · pro-rata-toerekening
└── eindejaarsverrichtingen              [procedure — bestaand]   afsluitingsverrichtingen voor jaarrekening (cross PO 1.1.taak.1 + II.L + II.Q)

resultatenrekening-boekhouding            [cluster, ~5 records — PO 1.1.II.M-P]
├── bedrijfskosten-en-bedrijfsopbrengsten [K — bestaand]   `-en-`-smell ⚠️ → splitsen later? Schema klasse 6/7
├── kostencomponenten                    [K — bestaand]    direct/indirect · vast/variabel · per kostenplaats
├── kostentypologie                      [K — bestaand]    materiële · loon · diensten · afschrijving · voorzieningen
├── opbrengstverantwoording              [K — bestaand]    realisatie-principe · cut-off · multi-period contracten
└── personeelskosten                     [E+balanspost — bestaand]   1.1.II.M-specifiek · klasse 62 · cross werknemers-vergoedingen

jaarrekening-en-synthesedocumenten        [cluster, ~3 records — PO 1.1.II.S + cross PO 1.2]
├── jaarrekening                         [E+instrument — bestaand]   balans · resultatenrekening · toelichting · sociale balans
├── openbaarmaking-jaarrekening          [procedure — bestaand]   neerlegging KBO/NBB · termijnen · sanctie
└── niet-in-balans-rechten-en-verplichtingen [K — bestaand]   off-balance commitments · garanties · operationele leasing pre-IFRS-16

opsplitsing-eigendom                      [mini-cluster, 1 record — PO 1.1.II.X]
└── opsplitsing-eigendom                 [K — bestaand]    vruchtgebruik · blote eigendom · waardering · cross naar erfrecht + estate planning

consolidatie                              [cluster, ~8 records — PO 1.4]
├── consolidatiekring                    [E+R — bestaand]
├── consolidatiemethoden                 [K — bestaand]    integraal · vermogensmutatie · evenredig
├── consolidatieverschil-goodwill        [K+R — bestaand]
├── eerste-consolidatie                  [G — bestaand]
├── evenredige-consolidatie              [G — bestaand]
├── integrale-consolidatie               [G — bestaand]
├── uniforme-waarderingsregels-consolidatie [R — bestaand]
└── wijziging-consolidatiekring          [G — bestaand]
```

**Cross-cluster** (records primair elders, raken boekhouding):
- `kapitaalstructuur`-cluster (II.H + II.T + II.U) — eigen vermogen + kapitaalwijzigingen + eigen aandelen
- `schuldfinanciering`-cluster (II.J + II.K + II.V + II.W) — schulden + obligaties + leasing
- `werknemers-vergoedingen` + `loon-en-payroll` (II.M) — bezoldigingen
- `winstuitkering` (II.Q) — winstbestemming
- `reorganisatie` + `overdracht-onderneming` + `insolventie` (II.T) — bijzondere verrichtingen
- `mobiliteit` (autokosten) — boekhoudkundige verwerking + waardering

**Totaaltelling boekhouding-discipline**: ~30 records over 9 sub-clusters (waarvan 3 ⏳ nieuw + 27 bestaand). Veel cross-coverage via thema-clusters.

**Open punten**:
- **OP-BH.A** ⏳ `bedrijfskosten-en-bedrijfsopbrengsten` heeft `-en-`-smell (precedent rationale-log 2026-05-24). Splits later in 2 records of behoud als bundel-record? Voorlopig behouden (volgt MAR-klasse-6/7-koppeling).
- **OP-BH.B** ⏳ `voorraden`-record bestaat nog niet (alleen `omloopsnelheid-voorraad` ratio + `voorraadcyclus-ic` procedure). Te creëren in mapping-fase.
- **OP-BH.C** ⏳ MAR-stelsel-record (Minimum Algemeen Rekeningenstelsel) als zelfstandig record of sub-sectie van `bgaap`/`boekhoudbeginselen`? Voorlopig sub-sectie.
- **OP-BH.D** ⏳ Per sub-cluster diepe uitwerking nog te doen indien substantieel didactisch werk nodig (vaste-activa-Σ-vergelijkingsmatrix · afschrijvingsmethoden · waardeverminderings-mechaniek).

### Fiscaliteit-discipline — compact cluster-mapping

Thema: `fiscaliteit` (top-discipline laag-1). *Compact-mapping over 8 PO 2.x-blokken (2.1 algemene beginselen + 2.2 PB + 2.3 VenB + 2.4 BTW + 2.5 procedure + 2.6 registratie+successie + 2.7 lokale+regionale + 2.8 internationaal). Veel content al cross-uitgewerkt via thema-clusters (fiscale-voordelen-vennootschap · winstuitkering · werknemers-vergoedingen · anti-misbruik · mobiliteit). Deze sectie identificeert sub-disciplines + bestaande record-volumes.*

#### Sub-disciplines van fiscaliteit

```
fiscaliteit                               [discipline]
├── algemene-beginselen-fiscaliteit       [sub-K, cross 2.1 — ~9 records]
│   ▸ belastingdefinitie · doelfuncties · bronnen + hiërarchie · actoren · indeling
│   ▸ records: belasting-definitie-en-functies · fiscaal-rechtelijk · fiscale-actoren · fiscale-beginselen · interpretatie-fiscale-wet · indeling-belastingen
│   ▸ cross naar anti-misbruik (incl. AAMB 2.1.IX.B)
│
├── personenbelasting                     [sub-K, PO 2.2 — ~31 records]
│   ▸ basisbegrippen (rijksinwoner · belastingplichtige · gezinslast)
│   ▸ inkomenscategorieën (onroerend · roerend · beroepsinkomsten · diverse)
│   ▸ aftrekken + verminderingen (federaal + gewestelijk)
│   ▸ aangifte + aanslag
│   ▸ records cross-vermeld: bedrijfsleidersbezoldiging-pb · beroepsinkomen-pb · beroepskosten-regime-pb · inkomstencategorieen-pb · aangifte-pb · aanslagbiljet-pb · diverse-inkomsten-pb · kadastraal-inkomen · huwelijksquotient
│   ▸ cross: werknemers-vergoedingen (alle VAA · bedrijfsleidersbezoldiging) · mobiliteit (autokosten-VAA)
│
├── vennootschapsbelasting                [sub-K, PO 2.3 — ~34 records]
│   ▸ belastbare grondslag + correctieronde
│   ▸ aftrekken (✅ uitgewerkt in `fiscale-voordelen-vennootschap`)
│   ▸ specifieke regimes (verworpen uitgaven · abnormale + goedgunstige voordelen · bijzondere aanslagen)
│   ▸ aangifte (Biztax) + tarief + voorafbetalingen
│   ▸ records cross-vermeld: aangifte-vennootschapsbelasting · abnormale-goedgunstige-voordelen · aftrekbare-beroepskosten-venb · belastbare-grondslag-vennootschapsbelasting · bijzondere-aanslagen-venb
│   ▸ cross: fiscale-voordelen-vennootschap · winstuitkering · anti-misbruik
│
├── btw                                   [sub-K, PO 2.4 — ~34 records]
│   ▸ BTW-plichtige + categorieën
│   ▸ leveringen + diensten + IC + invoer/uitvoer
│   ▸ aftrek + herziening + bedrijfsmiddelen
│   ▸ tarieven + vrijstellingen
│   ▸ aangifte + IC-listing + jaarlijkse opgave
│   ▸ specifieke regelingen: forfait · margeregeling · kleine ondernemingen
│   ▸ records cross-vermeld: btw-aangifte · btw-aftrek · btw-belastingplichtige · btw-bedrijfswagen · btw-bonnen-vouchers · btw-controle-en-geschillen · btw-eenheid · btw-grensoverschrijdend · btw-herziening-bedrijfsmiddelen · btw-stelsel · btw-tarieven · btw-vastgoed · btw-vrijstellingen
│   ▸ cross: mobiliteit (btw-bedrijfswagen) · ondernemingsvormen (btw-eenheid)
│
├── registratie-en-successierechten       [sub-K, PO 2.6 — ~18 records]
│   ▸ registratieverplichting + soorten registratierechten
│   ▸ evenredige rechten (verkoop onroerend goed · schenkingen)
│   ▸ erfbelasting (Vlaanderen/Wallonië/Brussel gewestelijk)
│   ▸ vrijstellingen + gunstregimes (gezinswoning · familiale onderneming)
│   ▸ fictiebepalingen
│   ▸ records cross-vermeld: aangifte-nalatenschap · erfbelasting + erfbelasting-tarieven-en-vrijstellingen · erfrecht · fictiebepalingen-erfbelasting · gunstregime-familiale-onderneming · huwelijksvermogensrecht
│   ▸ cross: ondernemingsvormen (maatschap = vermogensplanning) · opsplitsing-eigendom
│
└── lokale-en-regionale-belastingen       [sub-K, PO 2.7 — ~18 records]
    ▸ gewestelijke fiscaliteit (Vlaams + Waals + Brussels)
    ▸ lokale belastingen (gemeente + provincie)
    ▸ verkeersbelasting + onroerende voorheffing + opcentiemen
    ▸ leegstandsheffing · belasting inverkeerstelling
    ▸ records cross-vermeld: aanvullende-gemeentebelasting-pb · belasting-inverkeerstelling · gemeentebelastingen-sui-generis · gemeentelijke-opcentiemen-onroerende-voorheffing · gewest-fiscaliteit-registratie-en-successie · gewestelijke-belastingverminderingen-pb · gewestelijke-en-lokale-fiscaliteit · leegstandsheffing-bedrijfsruimten · lokale-fiscale-autonomie
```

#### Cross-cutting fiscale clusters (niet sub-discipline-specifiek)

```
fiscale-procedure                         [cross-cutting cluster, PO 2.5 — ~16 records]
   geldt voor PB/VenB/BTW: taxatieprocedure · aangifte · onderzoeksbevoegdheden · bewijsmiddelen · aanslag + termijnen · bezwaar + beroep · sancties + boetes · fiscale bemiddeling
   records cross-vermeld: aangifteplicht-fiscaal · aanslag-cyclus · aanslagtermijnen-fiscaal · administratieve-boete-fiscaal · beginselen-behoorlijk-bestuur-fiscaal · bezwaarprocedure-fiscaal · fiscale-bemiddelingsprocedure · fiscale-bewijsmiddelen · fiscale-controle · fiscale-procedure-belastingplichtige · fiscale-procedure-pb · fiscale-sancties · fiscale-strafrechtelijke-sanctie · gerechtelijke-fase-fiscaal · invorderingsprocedure-fiscaal · mandaat-accountant-fiscus

internationaal-fiscaal                    [cross-cutting cluster, PO 2.8 — ~30 records]
   dubbele belasting (oorzaken + vormen + voorkoming via DBV + unilaterale methodes)
   bilaterale verdragen + OESO-modelverdrag + MLI · EU-recht (fiscale-fusierichtlijn · ATAD · DAC-richtlijnen)
   transfer-pricing + verrekenprijzen + thin-cap (✅ uitgewerkt in `anti-misbruik`)
   internationale structurering · CFC · BEPS · Pijler-2-minimumbelasting
   records cross-vermeld: belasting-niet-inwoners · beps-actieplan · bijzonder-regime-buitenlandse-kaderleden · buitenlandse-winst-en-verlies · dubbelbelastingverdrag · eu-fiscale-richtlijnen · exit-belasting · forfaitair-gedeelte-buitenlandse-belasting · internationaal-fiscaal · internationaal-onroerend-goed · internationale-structurering-vennootschap · mli-instrument · moeder-dochterrichtlijn · onroerende-voorheffing-internationaal · winst-naar-herkomst
   cross: anti-misbruik (✅ uitgewerkt) · reorganisatie (fiscale-fusierichtlijn)
```

**Totaaltelling fiscaliteit-discipline**:
- ~190 records met PO 2.x-anker (incl. cross-records)
- 5 sub-disciplines + 2 cross-cutting clusters = 7 cluster-eenheden
- Veel content cross-leeft via thema-clusters (fiscale-voordelen · winstuitkering · werknemers-vergoedingen · mobiliteit · anti-misbruik · reorganisatie)
- Nieuwe Σ-overzicht-records per sub-discipline kunnen later toegevoegd worden indien didactisch nuttig (bv. `personenbelasting-overzicht` als Σ van inkomenscategorieën)

**Open punten**:
- **OP-FS.A** ⏳ Per sub-discipline mogelijk eigen Σ-overzicht-record voor inkomenscategorieën (PB) · aftrekken-volgorde (VenB) · BTW-aftrek-keuze · etc. Te beslissen bij PO-specifieke uitwerking.
- **OP-FS.B** ⏳ `fiscale-procedure` en `internationaal-fiscaal` als cross-cutting clusters apart of als sub-discipline-clusters? Voorlopig cross-cutting (raken alle 4 hoofd-belastingen).
- **OP-FS.C** ⏳ Sub-discipline-uitwerking per PO blijft TBD — deze compact-mapping is voldoende voor structuur-overzicht; diepe Σ-records per sub-discipline volgen indien didactisch zwaar.

### Fiscale-procedure-cluster

Thema: `fiscale-procedure`. *Eerste diepe PO 2.x-uitwerking (PO 2.5, 2026-05-26). Cross-cutting voor alle belastingsoorten — taxatie · aangifte · controle · bezwaar · bemiddeling · invordering. Lost 5 `-fiscaal`-suffix-smells op + sanctie-bundeling (3 records) + 2 duplicaat-absorpties + 1 perspectief-vermommings-absorptie + 1 naam-disambiguatie.*

```
fiscale-procedure                         [thema-cluster fiscaliteit, 13 records — PO 2.5]
│
├── fiscale-procedure                     [Σ-hoofdrecord — NIEUW]
│   ▸ overkoepelend keuzekader: aangifte → controle → taxatie → aanslag → bezwaar → bemiddeling/rechter → invordering
│   ▸ #flow-overzicht · #bewijslast-verdeling · #accountant-rol-vertegenwoordiging (overzicht; detail via perspectieven)
│   ▸ absorbeert: `fiscale-procedure-pb` + `fiscale-procedure-belastingplichtige`
│
├── taxatieprocedure                      [K]
├── aanslag-cyclus                        [procedure]
├── aanslagtermijnen                      [K, was `-fiscaal`]   gewone (3j) · verlengde (5j) · 10j-fraude
├── beginselen-behoorlijk-bestuur         [K-principes, was `-fiscaal`]   rechtszekerheid · zorgvuldigheid · redelijkheid · vertrouwen · motivering
├── fiscale-beginselen                    [K, cross PO 2.1]   legaliteit · annaliteit · territorialiteit
├── aangifteplicht                        [K, was `-fiscaal`]   wie · wat · wanneer · gevolgen niet-indiening
├── fiscale-sancties                      [Σ-bundel, absorbeert 3 records: administratieve-boete + belastingverhoging + strafrechtelijke-sancties]
├── fiscale-controle                      [procedure]   accountant_perspectieven[].advies: vertegenwoordigt cliënt (was `mandaat-accountant-fiscus`)
├── fiscale-bewijsmiddelen                [K]   geschriften · getuigen · vermoedens · bekentenis · tekenen+indiciën
├── bezwaarprocedure                      [procedure, was `-fiscaal`]   accountant_perspectieven[].advies: bezwaarschrift + advisering
├── gerechtelijke-fase-belasting          [procedure, was `gerechtelijke-fase-fiscaal` — disambiguatie met `gerechtelijke-reorganisatie`]   accountant_perspectieven[].advies: voorbereiding (daarna advocaat)
├── fiscale-bemiddelingsprocedure         [procedure]   FBD · vrijwillig · vertrouwelijk   accountant_perspectieven[].advies: bemiddeling-voorbereiding
├── invorderingsprocedure                 [procedure, was `-fiscaal`]   betalingsherinnering · dwangbevel · beslag
├── voorafgaande-beslissing-dvb           [procedure]   DVB-rulings (cross PO 2.1)
└── geheime-commissielonen                [R, cross VenB]   bijzondere aanslag 100/50% bij niet-fichering
```

**Cross-cluster**:
- `aangifte-pb` · `aangifte-vennootschapsbelasting` · `btw-aangifte` · `aangifte-nalatenschap` (cross uit PB/VenB/BTW/registratie-clusters)
- `fiscale-beginselen` (primair PO 2.1)
- `voorafgaande-beslissing-dvb` (cross PO 2.1)
- `geheime-commissielonen` (cross VenB)

**Renames + absorpties + nieuw**:

| Oud | Nieuw / actie |
|---|---|
| aangifteplicht-fiscaal | aangifteplicht |
| aanslagtermijnen-fiscaal | aanslagtermijnen |
| beginselen-behoorlijk-bestuur-fiscaal | beginselen-behoorlijk-bestuur |
| bezwaarprocedure-fiscaal | bezwaarprocedure |
| invorderingsprocedure-fiscaal | invorderingsprocedure |
| gerechtelijke-fase-fiscaal | **gerechtelijke-fase-belasting** (disambiguatie) |
| administratieve-boete-fiscaal | absorbed → `fiscale-sancties#administratieve-boete` |
| belastingverhoging-fiscaal | absorbed → `fiscale-sancties#belastingverhoging` |
| fiscale-strafrechtelijke-sanctie | absorbed → `fiscale-sancties#strafrechtelijke-sancties` |
| fiscale-procedure-pb | absorbed → cluster-Σ |
| fiscale-procedure-belastingplichtige | absorbed → cluster-Σ |
| **mandaat-accountant-fiscus** | **absorbed als perspectief** → `accountant_perspectieven[].advies` op fiscale-controle/bezwaarprocedure/bemiddelingsprocedure/gerechtelijke-fase-belasting (perspectief-vermommings-correctie) |
| (nieuw) | **fiscale-procedure** (Σ-overzicht) |

**Triangulatie 2026-05-26**:
- 12 PO 2.5-anchors → 0 PO-only gaps
- 23 records → 13 cluster-eigen (5 renames + 6 absorpties + 1 perspectief-correctie + 1 nieuw Σ + 1 disambiguatie)

**Bronnen-pin**: WIB · KB-WIB · AWGB (beginselen behoorlijk bestuur) · FBD-procedureregels.

**Test-case-validatie** (2026-05-26): 5 representatieve fiscale-procedure-vragen — alle gedekt zonder forceren; bevestigt o.a. perspectief-absorptie `mandaat-accountant-fiscus` (vr "accountant als gevolmachtigde bij fiscale controle" → `fiscale-controle.accountant_perspectieven[].advies`).

**Open punten**:
- **OP-FP.A** ✅ Naam-smell-scan-pattern uitgebreid met `-pb`/`-venb`/`-fiscus`/`-fiscaal`-suffixen
- **OP-PV.A** ⏳ **Cross-cluster perspectief-vermommings-scan** (nieuw): scan alle 396 records op `-pb`/`-venb`/`-fiscus`-suffixen. Litmus: bestaat onderliggend fenomeen-record? Zo ja → absorberen als perspectief. Al gespotte kandidaten:
  - `bedrijfsleidersbezoldiging-pb` → perspectief op `bedrijfsleidersbezoldiging` (werknemers-vergoedingen)
  - `aftrekbare-beroepskosten-venb` + `beroepskosten-regime-pb` → 2 perspectieven op (ontbrekend) `beroepskosten`-fenomeen → mogelijk nieuw `beroepskosten`-record creëren
  - `verworpen-uitgaven-autokosten` → VenB-perspectief op `autokosten` (mobiliteit-cluster)
  Mapping-fase-actie.
- **OP-FP.B** ⏳ Aanslag-procedure-detail vs `aanslag-cyclus`-record — eventueel nuance bij content-uitwerking

### Overige PO 1.x-blokken (1.2 · 1.3 · 1.4 · 1.5 · 1.8 · 1.9) — compact

*Resterende PO 1.x-onderwerpen die conceptueel onder `boekhouding`-discipline of `bedrijfseconomie-en-management`-discipline vallen. Veel records al cross-uitgewerkt of in zicht via boekhouding-compact-mapping.*

```
PO 1.2 — Boekhoudrecht en jaarrekeningrecht       [~17 records]
   wettelijk + reglementair kader voor boekhouding + jaarrekening (KB 29-04-2019 + Boekhoudwet 17-07-1975)
   cross naar: jaarrekening-en-synthesedocumenten-cluster (boekhouding) · boekhoudbeginselen-cluster
   primair-cluster: integreren in `jaarrekening-en-synthesedocumenten` (boekhouding)
   key records: jaarrekening · openbaarmaking-jaarrekening · sociale-balans · jaarverslag · boekhoudplichtige-onderneming · autoriteiten-boekhoudrecht

PO 1.3 — Analyse en kritische beoordeling jaarrekening   [~20 records]
   verticale + horizontale analyse · ratios (liquiditeit · solvabiliteit · rentabiliteit) · faillissementspredictie
   primair-cluster: `jaarrekeninganalyse` (eigen cluster onder bedrijfseconomie-en-management of boekhouding-cross)
   key records: jaarrekeninganalyse · current-ratio · cash-ratio · interest-coverage-ratio · brutomarge · ebitda-marge · nettomarge · cash-conversion-cycle · faillissementspredictie-modellen
   open: eigen `jaarrekeninganalyse`-cluster met Σ-overzicht-ratios — substantieel onderwerp

PO 1.4 — Geconsolideerde jaarrekening                    [~21 records]
   ✅ grotendeels uitgewerkt via `consolidatie`-cluster (boekhouding-discipline-mapping)
   cross naar: consolidatiekring · consolidatiemethoden · consolidatieverschil-goodwill · eerste-consolidatie · evenredige-consolidatie · integrale-consolidatie · uniforme-waarderingsregels-consolidatie · wijziging-consolidatiekring · geconsolideerde-jaarrekening · opmaak-geconsolideerde-jaarrekening · minderheidsbelangen

PO 1.5 — EU + internationale boekhoudkundige normen      [~7 records]
   EU richtlijnen + IAS/IFRS-context
   cross naar: ifrs · be-gaap-vs-ifrs-verschillen (al in boekhoudbeginselen)
   primair: sub-sectie van `boekhoudbeginselen`-cluster (geen eigen cluster — content cross al gedekt)

PO 1.8 — Analytische boekhouding + management accounting [~13 records]
   primair-discipline: `bedrijfseconomie-en-management` (zie volgende sectie)
   kostencalculatie · ABC · standaardkosten · variantie-analyse · budgettering · KPI-rapportering
   key records: managementcontrole-fiche (verhuisd uit interne-controle PO 1.7) · kostprijsmethoden · standaardkostenmethode · marginale-analyse · masterbudget · budgetbeheer · direct-costing · full-costing · analytische-boekhouding · abc-methode

PO 1.9 — Financiële analyse + financieel bedrijfsbeheer  [~5 records]
   primair-discipline: `bedrijfseconomie-en-management`
   kapitaalstructuur-keuze · investeringsbeslissing (NPV/IRR) · kasplanning · treasury · werkkapitaal-management · waardering ondernemingen
   key records: jaarrekeninganalyse · faillissementspredictie-modellen · cash-conversion-cycle · communicatie-met-stakeholders (cross beroepsbeoefening)
   cross naar: `kapitaalstructuur` · `schuldfinanciering` · `overdracht-onderneming` (waardering bij overname)
```

### Bedrijfseconomie-en-management-discipline — compact mapping

Thema: `bedrijfseconomie-en-management` (top-discipline laag-1). *PO 1.8 + PO 1.9 + cross PO 4.0.taak.5 + taak.6. Verzamelt management-accounting + financiële-analyse + strategie-onderwerpen. Veel records bestaan al; primair-cluster-positionering te bepalen.*

```
bedrijfseconomie-en-management            [discipline]
├── management-accounting                 [sub-K, ~9 records — PO 1.8]
│   ▸ kostencalculatie (ABC · standaard · marginal · full · direct)
│   ▸ budgettering (master + sub-budgetten)
│   ▸ KPI-rapportering + variantie-analyse
│   ▸ records: managementcontrole-fiche · kostprijsmethoden · standaardkostenmethode · marginale-analyse · masterbudget · budgetbeheer · direct-costing · full-costing · abc-methode · analytische-boekhouding
│
├── financiele-analyse                    [sub-K, ~10 records — PO 1.9 + PO 1.3]
│   ▸ ratio-analyse (liquiditeit · solvabiliteit · rentabiliteit · activiteit)
│   ▸ trend-analyse + benchmarking
│   ▸ faillissementspredictie + early-warning
│   ▸ records: jaarrekeninganalyse · current-ratio · cash-ratio · interest-coverage-ratio · brutomarge · ebitda-marge · nettomarge · cash-conversion-cycle · faillissementspredictie-modellen · omloopsnelheid-voorraad
│   ▸ open: eigen `ratios`-Σ-record met vergelijkingsmatrix?
│
├── corporate-finance-en-treasury         [sub-K, ⏳ NIEUW — PO 1.9]
│   ▸ investeringsbeslissing (NPV · IRR · payback · DCF)
│   ▸ kapitaalstructuur-keuze · WACC
│   ▸ kasplanning + werkkapitaal-management
│   ▸ waardering ondernemingen (DCF · vergelijkbare transacties · multiples)
│   ▸ records ⏳: alle nieuw
│   ▸ cross naar: kapitaalstructuur · schuldfinanciering · overdracht-onderneming (waardering)
│
├── digitale-werkomgeving                 [sub-K, ⏳ NIEUW — PO 4.0.taak.5 cross]
│   ▸ digitale transformatie kantoor · cybersecurity · samenwerkingsplatformen
│   ▸ verwijst naar beroepsbeoefening#kantoor-organisatie#digitale-werkomgeving (al gedekt)
│
└── bedrijfsstrategie-en-businessmodel    [sub-K, ⏳ NIEUW — PO 4.0.taak.6 cross]
    ▸ businessmodellen + waardeketens + Porter's 5 forces + SWOT
    ▸ strategie-as-gesprekspartner-zaakvoerder
    ▸ records: businessmodel-en-strategie-inzicht-accountant (al cross verhuisd uit PO 4.0)
```

**Totaaltelling bedrijfseconomie-en-management**:
- ~20 records al bestaand + 2 sub-K-blokken ⏳ nieuw (corporate-finance-en-treasury · bedrijfsstrategie)
- Verzamelt veel kleine technische records (ratios, kostprijsmethoden) — mogelijk sub-Σ-records per cluster bij content-uitwerking

**Open punten**:
- **OP-BM.E** ⏳ Per sub-discipline 1 Σ-record (bv. `ratios` voor financiële analyse · `kostprijsmethoden`-Σ voor management accounting · `investeringsmethoden`-Σ voor corporate finance) — te beslissen bij PO-specifieke uitwerking
- **OP-BM.F** ⏳ Voor PO 1.9-corporate-finance moeten ~5-8 nieuwe records gecreëerd worden (NPV-IRR · WACC · DCF-waardering · kasplanning · werkkapitaal-mgmt · investeringsbeslissing-Σ)
- **OP-BM.G** ⏳ Relatie tot `controle-en-assurance`-discipline-context: managementcontrole onderscheidt zich expliciet van interne-controle (afbakening al in interne-controle-cluster) — confirmatie scope-grens

### Beroepsbeoefening-cluster

Thema: `beroepsbeoefening`. *Thema-cluster onder `beroep-en-deontologie`-discipline. Resulteert uit PO 4.0-werk (2026-05-26). PO 4.0 = "Deontologische beginselen + antiwitwaswetgeving" met dubbele functie: deel I + taken 1-3 = kern (eigen cluster); deel II + taken 4-6 = competentie-overzicht (cross-naar-andere-PO's, geen eigen records). Absorbeert meerdere records die in eerdere cluster-sparring waren voorzien om hier te verhuizen (commissaris-blok, kwaliteitsmanagement, opdrachtbrief, AML).*

```
beroepsbeoefening                             [thema-cluster onder beroep-en-deontologie-discipline]
│
├── --- I. STATUUT VAN HET BEROEP ---
├── gecertificeerd-accountant                 [E-actor, NIEUW]
│       beroep met toelatingsvereisten · monopolieopdrachten · stagiair → gecertificeerd · onverenigbaarheden
├── itaa-beroepsorganisatie                   [E-orgaan]
│       structuur · raden · publiek toezicht · openbaar register
├── normbronnen                               [K-overzicht]
│       hiërarchie: wet → KB → reglement → norm → deontologische code → ITAA-normen + ISA (audit-context)
│
├── --- II. DEONTOLOGISCHE BEGINSELEN ---
├── deontologie                               [K — was `deontologie-accountant`, suffix-smell weg]
│       5 fundamentele beginselen: integriteit · objectiviteit · vakbekwaamheid · vertrouwelijkheid · professioneel gedrag
├── beroepsgeheim                             [K-principe + R — was `beroepsgeheim-accountant`]
│       wat valt onder · uitzonderingen · samenloop met AML-melding (anti-collision-regel)
├── beroepsaansprakelijkheid                  [K-principe — was `aansprakelijkheid-accountant-revisor`, compacter]
│       3 sporen: burgerlijk · strafrechtelijk · tuchtrechtelijk; dekt accountant + bedrijfsrevisor
├── tuchtprocedure-itaa                       [R-procedure]
│       wie · sancties (waarschuwing / schorsing / schrapping) · beroep · KvT/IBR-tuchtorganen
├── kwaliteitstoetsing-itaa                   [R-procedure]
│       externe peer review door ITAA · frequentie · scope · resultaat-categorieën
├── permanente-vorming                        [R-procedure — was `permanente-vorming-accountant`]
│       puntenstelsel · ITAA-norm-permanente-vorming · sancties bij niet-naleving
│
├── --- III. AML / WITWASPREVENTIE ---
└── antiwitwaspreventie                       [R-overkoepelend — was `antiwitwas-verplichtingen-accountant`]
    ▸ #cliëntenonderzoek (KYC) — was `clientenonderzoek-aww`
    ▸ #ubo-register — was `ubo-register`
    ▸ #risicogebaseerde-benadering — was `risicogebaseerde-benadering-aww`
    ▸ #melding-verdachte-transactie-cfi — was `melding-verdachte-transactie-cfi` (CFI = Cel voor Financiële Informatieverwerking, eigennaam — geen suffix-smell)
    ▸ #intern-beleid-en-procedures (NIEUW sub-sectie — risk officer, opleiding, gegevensbewaring 10j ⚠️)
│
├── --- IV. KANTOOR-PRAKTIJK ---
├── opdrachtaanvaarding-en-opdrachtbrief      [E + R]
│       (verhuisd uit controle-opdracht per OP-EC.A) — wettelijk + ITAA-norm-opdrachtbrief; geldt voor élk opdrachttype
└── kantoor-organisatie                       [K — was `kantoor-organisatie-accountant`]
    ▸ #team-coordinatie-en-supervisie (4.0.taak.4)
    ▸ #communicatie-met-stakeholders (4.0.taak.2 — was `communicatie-met-stakeholders` record, geabsorbeerd)
    ▸ #digitale-werkomgeving (4.0.taak.5 — was `digitalisering-accountantskantoor` record, geabsorbeerd; cyber + samenwerkingsplatformen + digital workplace)
```

**Cross-cluster** (eigen plek elders, relaties hierheen):
- `onafhankelijkheid` [K-principe + R-regime, **shared**] — leeft in beroepsbeoefening **én** controle-opdracht-cluster; thema's beide
- `kwaliteitsmanagement-opdracht` [K-techniek + R, **shared**] — idem (ISQM kantoor-niveau + EQR opdracht-niveau)
- `commissaris` [E] — bijzondere hoedanigheid van `gecertificeerd-accountant`, eigen record gerechtvaardigd door wettelijk + statutair regime; cross-relatie hier
- `auditcomite` [E-orgaan, **shared**] — al cross-cutting (controle-opdracht + interne-controle); voegt thema beroepsbeoefening toe
- `fraude` [G, cross-cutting] — raakt AML maar leeft als eigen Gebeurtenis (PO 1.6/1.7/4.0/witwas)
- `vennootschap-groottecategorieen` [E + R] — bepaalt commissaris-trigger; cross-relatie

**Schrappen als zelfstandig record / herleiden tot sub-sectie**:
- `deontologie-accountant` → hernoemd `deontologie` (`-accountant`-suffix-smell weg; cluster zegt al dat het over accountant gaat)
- `beroepsgeheim-accountant` → hernoemd `beroepsgeheim`
- `aansprakelijkheid-accountant-revisor` → hernoemd `beroepsaansprakelijkheid` (compacter, dekt beide beroepen, geen suffix-smell)
- `permanente-vorming-accountant` → hernoemd `permanente-vorming`
- `kantoor-organisatie-accountant` → hernoemd `kantoor-organisatie`
- `antiwitwas-verplichtingen-accountant` → hernoemd `antiwitwaspreventie` (compacter)
- `clientenonderzoek-aww`, `ubo-register`, `risicogebaseerde-benadering-aww`, `melding-verdachte-transactie-cfi` → sub-secties van `antiwitwaspreventie` (anti-versnippering, 5 records → 1 hoofdrecord; `-aww`-suffix-smell weg waar bestaande)
- `communicatie-met-stakeholders` → sub-sectie van `kantoor-organisatie`
- `digitalisering-accountantskantoor` → sub-sectie van `kantoor-organisatie`
- `businessmodel-en-strategie-inzicht-accountant` → **cross naar `bedrijfseconomie-en-management`-discipline** (4.0.taak.6 is meta-competentie, niet deontologie-domein)

**Triangulatie-resultaten beroepsbeoefening** (2026-05-26):
- 17 PO 4.0-anchors (6 taken + 11 kenniselementen) waarvan 9 in scope (4.0.I + taken 1-3) + 8 cross naar andere PO's (4.0.II + taken 4-6)
- 19 bestaande records met PO 4.0-anker → **11 cluster-eigen records** (reductie van 19 → 11 + 2 shared) + 7 absorpties in sub-secties + 1 cross-discipline-verhuis (businessmodel-en-strategie-inzicht)
- 15 kandidaten in DB (alle `gerealiseerd: 0` vóór hernoemen)
- 3 belangrijke smell-oplossingen: (a) `-accountant`-suffix op 5 records geruimd; (b) `-aww`-suffix-smell (= afkorting-suffix, schendt regel 8 CLAUDE.md) op 3 records weggewerkt via AML-bundeling; (c) 5 versnipperde AML-records → 1 Σ-overkoepelend record (anti-preventieve-versnippering)

**Bronnen-pin voor cluster**:
- ✅ ITAA-norm-aww-reglement (trusted) — AML-uitvoering accountancy
- ✅ ITAA-norm-aww-procedurereglement (trusted)
- ✅ ITAA-norm-aww-richtlijn-bibf (trusted)
- ✅ ITAA-norm-aww-geconsolideerd (trusted)
- ✅ ITAA-norm-opdrachtbrief (trusted)
- ✅ ITAA-norm-permanente-vorming (trusted)
- ✅ ITAA-norm-gedragslijnen-relaties-IBR (trusted)
- ✅ ITAA-norm-intern-kwaliteitsmanagement (trusted)
- ⏳ AML-wet 18 september 2017 (Wet ter voorkoming van witwassen) — primaire bron, te verifiëren in `resources/bronnen/wetteksten/`
- ⏳ ITAA-Handleiding interne procedures AWW 2019 (al in resources, untracked)

**Details per record** (kort — hints voor extractie):

**`gecertificeerd-accountant`** [E-actor, NIEUW]
- inhoud: gereglementeerd beroep met toelatingsvereisten (universitair diploma + 3j stage + bekwaamheidsexamen) · inschrijving in openbaar register ITAA · monopolieopdrachten (wettelijk voorbehouden: opdrachtbrief, fiscale aangiften namens cliënt, attestopdrachten) · onverenigbaarheden (bv. handelszaak in eigen naam, bestuursfunctie cliënt) · stagiair-statuut (proefperiode, beperkt opdrachtenpakket, supervisor-vereiste)
- perspectieven: `beroep-en-deontologie` (eigen statuut)
- relaties: `itaa-beroepsorganisatie`, `commissaris` (bijzondere hoedanigheid), `tuchtprocedure-itaa`, `permanente-vorming`

**`itaa-beroepsorganisatie`** [E-orgaan]
- inhoud: structuur ITAA (Instituut van de Belastingadviseurs en de Accountants) · raden + voorzitters · publiek toezicht door FOD Economie · openbaar register (online raadpleegbaar) · samenwerking met IBR (bedrijfsrevisoren) · Wet 17 maart 2019 als oprichtingswet
- relaties: `gecertificeerd-accountant`, `tuchtprocedure-itaa`, `kwaliteitstoetsing-itaa`

**`normbronnen`** [K-overzicht]
- inhoud: hiërarchie van rechtsbronnen voor accountancy: wet (federaal/gewestelijk) → KB → reglement (gemeenschappelijk reglement KB 9-12-2009) → beroepsnormen (ITAA + IBR) → deontologische code → internationale standaarden (ISA, ISRE, ISRS, ISAE — via verwijzing in normen) · onderscheid hard law vs soft law · bindende kracht tuchtrechtspraak
- relaties: `deontologie`, `tuchtprocedure-itaa`, alle normen-cross naar `controle-opdracht`-cluster

**`deontologie`** [K — overzicht 5 beginselen]
- inhoud: 5 fundamentele beginselen (IFAC + ITAA): **integriteit** (eerlijk handelen) · **objectiviteit** (geen vooroordeel) · **vakbekwaamheid + zorgvuldigheid** (technische + ethische competentie + due care) · **vertrouwelijkheid** (= beroepsgeheim, eigen record) · **professioneel gedrag** (wet + reputatie). Threats-and-safeguards-model: self-interest, self-review, advocacy, familiarity, intimidation → mitigerende maatregelen.
- relaties: `onafhankelijkheid` (specifiek geval objectiviteit), `beroepsgeheim`, `beroepsaansprakelijkheid`

**`beroepsgeheim`** [K-principe + R]
- inhoud: wettelijk verankerd (art 458 Strafwetboek + ITAA-deontologische code) · wat valt onder (alles wat in opdrachtuitvoering wordt gekend) · uitzonderingen (wettelijke verplichting, rechterlijke vordering, AML-melding aan CFI ⚠️ — getuigt boven beroepsgeheim) · samenloop met AML: tipping-off-verbod (cliënt niet inlichten over CFI-melding) · cross naar belastingadvies-context
- relaties: `antiwitwaspreventie` (samenloop), `deontologie` (vertrouwelijkheidsbeginsel), `aansprakelijkheid` (strafrechtelijke sanctie)

**`beroepsaansprakelijkheid`** [K-principe]
- inhoud: 3 sporen — (a) **burgerlijk**: contractuele aansprakelijkheid t.o.v. cliënt + buitencontractuele t.o.v. derden; bewijslast schade + fout + causaal verband; verzekering beroepsaansprakelijkheid verplicht via ITAA-reglement ⚠️; (b) **strafrechtelijk**: medeplichtigheid valsheid in geschriften, witwassen, oplichting, ...; specifieke fiscale strafmiscdrijven; (c) **tuchtrechtelijk**: deontologische overtreding → tuchtkamer → sancties. Dekt accountant + bedrijfsrevisor (beide beroepen onderworpen aan analoog regime).
- relaties: `tuchtprocedure-itaa`, `deontologie`, `commissaris` (bijzondere aansprakelijkheid bij wettelijke controle)

**`tuchtprocedure-itaa`** [R-procedure]
- inhoud: procedure bij overtreding deontologie · klacht (cliënt, derde, eigen initiatief Raad ITAA) · onderzoek door Auditeur · Kamer voor Tuchtonderzoek → Tuchtkamer · sancties: **waarschuwing · berisping · schorsing (max 1j) · schrapping** (definitief verlies titel) · beroep bij Hof van Beroep Brussel · publicatie tuchtrechtspraak
- relaties: `itaa-beroepsorganisatie`, `beroepsaansprakelijkheid`, `deontologie`

**`kwaliteitstoetsing-itaa`** [R-procedure]
- inhoud: periodieke externe peer review door ITAA (verplicht alle gecertificeerde leden) · frequentie typisch 5-6 jaar · scope: organisatie-niveau (kantoor) + opdracht-niveau (steekproef) · 3 resultaten: conform / met opmerkingen / niet-conform · niet-conform-gevolgen: actieplan + heronderzoek + eventueel tucht · ITAA-norm-intern-kwaliteitsmanagement als kader
- relaties: `kwaliteitsmanagement-opdracht`, `tuchtprocedure-itaa`, `itaa-beroepsorganisatie`

**`permanente-vorming`** [R-procedure]
- inhoud: ITAA-norm permanente vorming (verplicht voor inschrijving) · puntenstelsel: 120u/3j of 40u/jaar ⚠️ · types: erkende vorming + zelfstudie + lesgeven · jaarlijkse aangifte aan ITAA · sancties: bij niet-naleving → tucht
- relaties: `tuchtprocedure-itaa`, `gecertificeerd-accountant`

**`antiwitwaspreventie`** [R-overkoepelend]
- inhoud: AML-regime voor accountants — gebaseerd op **Wet 18 september 2017** (Wet ter voorkoming van witwassen + financiering terrorisme) + **WER boek XI** + EU-richtlijn (5e + 6e AML-richtlijn). 5 verplichtingen-blokken:
  - `#cliëntenonderzoek` (KYC) — identificatie cliënt + uiteindelijke begunstigde + doel zakenrelatie + monitoring; vereenvoudigd / standaard / verscherpt onderzoek (afhankelijk van risico)
  - `#ubo-register` (wet 26 juni 2020) — Ultimate Beneficial Owner; KBO-link; cliënt moet UBO-gegevens registreren; accountant raadpleegt + valideert
  - `#risicogebaseerde-benadering` — risico-categorisering cliënt (laag/middel/hoog) + transactie (drempels) → matig of verscherpt onderzoek; documentatie-plicht
  - `#melding-verdachte-transactie-cfi` (Cel voor Financiële Informatieverwerking) — wanneer melden (indicatoren), tipping-off-verbod ⚠️ (niet vertellen aan cliënt), bescherming melder, samenloop met beroepsgeheim
  - `#intern-beleid-en-procedures` — risk officer/AML-compliance-officer aanwijzen, intern protocol, opleiding medewerkers, gegevensbewaring 10j ⚠️
- perspectieven: `beroep-en-deontologie` (verplicht regime) · `audit` (cross-relatie naar `fraude` Gebeurtenis-record)
- naam_officieel: antiwitwaspreventie / lutte contre le blanchiment · synoniemen: AML, anti-money-laundering, witwasplicht-accountant, AWW-discipline
- relaties: `beroepsgeheim` (tipping-off-anti-collision), `fraude` (cross-cutting Gebeurtenis), `ubo-register` (geabsorbeerd), `gecertificeerd-accountant`

**`opdrachtaanvaarding-en-opdrachtbrief`** [E + R] (verhuisd uit controle-opdracht)
- inhoud: opdrachtbrief = contractueel + deontologisch begin van elke opdracht (geldt voor élk opdrachttype, niet enkel controle — vandaar hier in beroepsbeoefening per OP-EC.A). Aanvaardingsproces: (a) cliëntenonderzoek + integriteits-check (overlap met AML KYC); (b) competentie-check (kan kantoor de opdracht aan?); (c) onafhankelijkheidsverklaring; (d) opdrachtbrief-opmaak (scope · honoraria · termijnen · verantwoordelijkheden · vertrouwelijkheid · klachtenprocedure · ITAA-norm-opdrachtbrief).
- perspectieven: `beroep-en-deontologie` (eigen plicht), `advies` (opmaak met cliënt)
- relaties: `gecertificeerd-accountant`, `antiwitwaspreventie#cliëntenonderzoek` (overlap), `onafhankelijkheid` (verklaring), `commissaris` (specifieke opdrachtbrief bij wettelijke controle)

**`kantoor-organisatie`** [K] (was `kantoor-organisatie-accountant`)
- inhoud: drie operationele aspecten van een accountantskantoor: (a) `#team-coordinatie-en-supervisie` (4.0.taak.4) — opdrachtenverdeling op basis van competentie + ervaring, voortgang + kwaliteitsbewaking, review-piramide; (b) `#communicatie-met-stakeholders` (4.0.taak.2) — afstemming op doelpubliek (cliënt/voorganger/banken/fiscus/sociale zekerheid/rechtbank/toezichthouder); scheiding publiek toelaatbaar vs beroepsgeheim vs vertrouwelijke informatie; (c) `#digitale-werkomgeving` (4.0.taak.5) — gegevensstromen cliënt↔kantoor, samenwerkingsplatformen, cybersecurity, audittrails, AVG-discipline.
- perspectieven: `advies` (kantoor-management)
- relaties: `kwaliteitsmanagement-opdracht` (ISQM-overlap), `beroepsgeheim` (communicatie-discipline), `gecertificeerd-accountant`

**Open punten beroepsbeoefening-cluster**:
- **OP-BB.A** ✅ **Beslist** (2026-05-26): `-accountant`-suffix-smell geruimd op 5 records (deontologie · beroepsgeheim · permanente-vorming · kantoor-organisatie + via rename `beroepsaansprakelijkheid`). `-aww`-suffix-smell geruimd via AML-bundeling.
- **OP-BB.B** ✅ **Beslist** (2026-05-26): AML = 1 overkoepelend record `antiwitwaspreventie` met 5 sub-secties; absorbeert 4 oude records.
- **OP-BB.C** ✅ **Beslist** (2026-05-26): `gecertificeerd-accountant` als nieuw overkoepelend E-actor-record voor "wie is de accountant" + statuut.
- **OP-BB.D** ✅ **Beslist** (2026-05-26): `kantoor-organisatie` absorbeert `communicatie-met-stakeholders` + `digitalisering-accountantskantoor` als sub-secties.
- **OP-BB.E** ⏳ `commissaris`-record (uit PO 1.6-werk verhuisd) — apart record of sub-sectie van `gecertificeerd-accountant`? Mijn voorkeur: **apart record** want wettelijke + statutaire context substantieel verschillend (KMO-controlenorm-toepasselijkheid, mandaat-modaliteit, onafzetbaarheid). Te valideren bij commissaris-uitwerking.
- **OP-BB.F** ⏳ AML-bron-pin: 4 ITAA-AWW-normen + AML-wet 18-09-2017 + ITAA-handleiding AWW-2019. Cross-validatie of wet effectief in `resources/bronnen/wetteksten/` als trusted.
- **OP-BB.G** ⏳ `businessmodel-en-strategie-inzicht-accountant` cross-discipline-verhuis naar `bedrijfseconomie-en-management` — bij die discipline-uitwerking bevestigen of het daar past, anders herzien.

**Test-case-validatie** (2026-05-26): 6 representatieve PO 4.0-examen-vragen door de tree gevoerd:

| Vraag | Concept | Tree-pad | Resultaat |
|---|---|---|---|
| 2003-bibf-vrK1 | Overdracht dossier tussen confraters | `kantoor-organisatie#communicatie-met-stakeholders` (voorganger ↔ opvolger) + `beroepsgeheim` (overdrachts-discipline) | ✅ |
| 2008-bibf-vrK1 | Onafhankelijkheid: bestuursmandaat + boekhouder zelfde NV | `onafhankelijkheid` (shared) + `gecertificeerd-accountant#onverenigbaarheden` | ✅ |
| 2008-bibf-vrK4 | Schorsing 3 maand + lidgeld/verzekering/PV-naleving | `tuchtprocedure-itaa#sancties` + `permanente-vorming` + `beroepsaansprakelijkheid#verzekering` | ✅ |
| 2008-bibf-vrK5 | Boekhoudvennootschap: doelomschrijving/zaakvoerder/aandelen/stagiair | `gecertificeerd-accountant#stagiair-statuut` + cross `ondernemingsvormen` (zaakvoerder/aandelen) + `itaa-beroepsorganisatie` | ✅ |
| 2013-1-vr33 | AWW compliance officer / witwasverantwoordelijke | `antiwitwaspreventie#intern-beleid-en-procedures` (risk officer) | ✅ |
| 2024-1-vr6 | Erelonen + AWW-contantengrens (2.500/3.000) | `antiwitwaspreventie#cliëntenonderzoek` (contantgeldgrens als KYC-trigger) | ✅ |

Alle 6 vragen passen door de tree. **Belangrijke bevestigingen**: (a) AML-bundeling werkt — 2 testvragen (vr33 + vr6) raken verschillende sub-secties van `antiwitwaspreventie` zonder forceren; (b) `gecertificeerd-accountant` als nieuw record bewijst zijn nut (vr K1 onverenigbaarheden + vr K5 stagiair-statuut); (c) shared records (`onafhankelijkheid` + `kwaliteitsmanagement-opdracht`) leveren cross-cluster-coverage zonder duplicatie; (d) `beroepsaansprakelijkheid`-rename (van `aansprakelijkheid-accountant-revisor`) houdt stand (verzekering-aspect in vr K4).

**Mapping-actie 2026-05-26**: `gecertificeerd-accountant` krijgt sub-sectie `#monopolieopdrachten` met cross-link naar `bijzondere-mandaten` (= 6e sub-Kader controle-discipline) — wettelijke voorbehouden opdrachten zijn statuut-aspect dat cross-leeft naar controle-discipline.

### Bijzondere-mandaten-cluster

Thema: `bijzondere-mandaten`. *6e sub-Kader van `controle`-discipline (toegevoegd 2026-05-26 op user-vraag). **Shared thema** met `beroepsbeoefening`-cluster (wettelijk monopolie-aspect leeft daar via `gecertificeerd-accountant#monopolieopdrachten`). Categorisch begrip met klein hoofdrecord; concrete uitvoering per type woont als `accountant_perspectieven[].audit` op de betrokken Gebeurtenis-records (Regel J + perspectief-vs-record-principe). Lost PO 3.0.taak.3 + 3.0.IV.A op + scherpt OP-EC.E mapping-actie aan.*

```
bijzondere-mandaten                           [sub-Kader van `controle`, 1 record]
└── bijzondere-mandaten                       [R + K, hoofdrecord — klein, categorisch]
    ▸ #definitie + onderscheid met commissaris-opdracht (eenmalig vs doorlopend)
    ▸ #wettelijk-regime (wet 17 maart 2019 + WVV per type)
    ▸ #context — bij vennootschappen ZONDER commissaris (= klein/middelgroot per `vennootschap-groottecategorieen`)
    ▸ #types-vergelijkingstabel (cross-relaties naar Gebeurtenissen):
        - inbreng-in-natura (WVV 5:133/7:179) → ITAA-norm-effectennorm
        - quasi-inbreng (WVV 5:138/7:8) → ITAA-norm-effectennorm
        - inkoop-eigen-aandelen (controle netto-actief + uitkeringstest)
        - kapitaalvermindering-aanzuivering-verlies → WVV-procedure
        - fusie · splitsing · partiële-splitsing → ITAA-norm-fusie-splitsing
        - omzetting-vennootschap → ITAA-norm-omzetting-vennootschap
        - ontbinding-vereffening (boekenstaat + continuïteits-evaluatie) → ITAA-norm-ontbinding-vereffening
    ▸ #verslag-componenten-gedeeld (verwijst naar `controleverklaring#andere-verslagstypes`)
    ▸ #honoraria-en-transparantie-discipline (ITAA-norm)
    ▸ #aanvaardingsproces (overlap met `opdrachtaanvaarding-en-opdrachtbrief`)
```

**Cross-cluster**:
- `gecertificeerd-accountant` (beroepsbeoefening) — uitvoerder bij vennootschap zonder commissaris; sub-sectie `#monopolieopdrachten` cross-link
- `commissaris` (beroepsbeoefening ⏳) — alternatief uitvoerder als die wel benoemd is
- `controleverklaring#andere-verslagstypes` (controle-opdracht) — verslag-vorm-overzicht, cross-link hierheen
- `vennootschap-groottecategorieen` (ondernemingsvormen) — bepaalt commissaris-trigger → bepaalt wie het mandaat uitvoert
- `opdrachtaanvaarding-en-opdrachtbrief` (beroepsbeoefening) — overlap aanvaardingsproces
- Alle 8 Gebeurtenis-records (zie types-tabel) — primair-detail van uitvoering woont daar via `accountant_perspectieven[].audit`

**Perspectief-mapping-actie** (verfijning van OP-EC.E, voorheen "audit-perspectief toevoegen met revisor-verslag-vereiste"):

Voor elke Gebeurtenis-record die een bijzonder mandaat triggert, voeg `accountant_perspectieven[]`-entry toe met:
- `rol: auditor` (of `accountant` indien geen commissaris)
- `perspectief: audit`
- Kern-element met **cross-link naar `bijzondere-mandaten`** (categorisch begrip)
- **Specifieke ITAA-norm-pin** (per type — zie types-tabel)
- Oordeel-onderwerp specifiek voor deze verrichting
- Verslag-componenten specifiek voor deze verrichting (gedeelde elementen via cross-link)

Voorbeeld `kapitaalverhoging-in-natura.accountant_perspectieven`:
```
- rol: auditor
  perspectief: audit
  elementen:
    - kern: "Bijzonder mandaat: revisor-verslag bij inbreng-in-natura"
      relaties: [{soort: cross-link, target: bijzondere-mandaten}]
    - kern: "ITAA-norm: ITAA-norm-effectennorm (waar van toepassing)"
    - kern: "Oordeel-onderwerp: waardering van de inbreng + redelijkheid van het aantal toegekende aandelen"
    - kern: "Verslag-componenten: omschrijving inbreng · waarderingsmethode · oordeel · waarschuwingsclausules"
```

**Schrappen als zelfstandig record**:
- (geen — `bijzondere-mandaten` is een nieuw concept dat niet bestond als zelfstandig record; eerdere `bijzondere-verslagen-vennootschapsverrichtingen`-record is al weg-gemapt naar Gebeurtenissen — zie OP-EC.E)

**Triangulatie 2026-05-26**: 
- PO 3.0.taak.3 + PO 3.0.IV.A + cross PO 1.6.IV.C (= "andere verslagstypes" sub-sectie van `controleverklaring`)
- Geen bestaand record met deze precieze scope — concept verspreid over 8 Gebeurtenis-records + sub-sectie van `controleverklaring` zonder centraal huis
- 1 nieuw record → primair-thuis voor de **categorische dimensie** van bijzondere mandaten

**Bronnen-pin**: 
- ✅ ITAA-norm-fusie-splitsing (trusted)
- ✅ ITAA-norm-ontbinding-vereffening (trusted)
- ✅ ITAA-norm-omzetting-vennootschap (trusted)
- ✅ ITAA-norm-effectennorm (trusted)
- ⏳ Wet 17 maart 2019 (basiswet beroep) — te valideren in resources

**Test-case-validatie** (2026-05-26): aansluiting op 2 PO 1.6-test-cases die we al deden:

| Vraag | Concept | Tree-pad (incl. nieuw cluster) | Resultaat |
|---|---|---|---|
| 2013-1-vr16 | externe accountant bij ontbinding (staat A/P + continuïteit) | `ontbinding-vereffening` (⏳ Geb) + `bijzondere-mandaten` (categorisch — type ontbinding) + `accountant_perspectieven[].audit` op Gebeurtenis met ITAA-norm-ontbinding-vereffening cross | ✅ (nu ÉCHT volledig — categorisch begrip + concrete uitvoering apart vindbaar) |
| 2013-1-vr19 | opdrachtbrief bij omzetting | `opdrachtaanvaarding-en-opdrachtbrief` (beroepsbeoefening) + `omzetting-vennootschap` (⏳ Geb) + `bijzondere-mandaten#aanvaardingsproces` (overlap) + ITAA-norm-omzetting-vennootschap | ✅ |

**Open punten**:
- **OP-BM.A** ⏳ Wanneer alle 8 Gebeurtenis-records `accountant_perspectieven[].audit` gekregen hebben met cross-link naar `bijzondere-mandaten`, kan `controleverklaring#andere-verslagstypes` versmald worden tot pure cross-link (geen inhoud nodig). Mapping-fase-werk.
- **OP-BM.B** ⏳ `commissaris`-record (uit OP-BB.E) — uitwerking moet `bijzondere-mandaten` als parallel-uitvoeringsroute behandelen (wanneer commissaris is aangesteld, voert die de mandaten uit; als geen commissaris, dan gecertificeerd-accountant).
- **OP-BM.C** ⏳ Tantième-controle is een bijzonder mandaat-kandidaat dat nog niet in types-tabel staat (PO 3.0.II.C belangenconflict / tantième-toekenning) — te valideren bij `bestuur-en-aansprakelijkheid`-cluster.

---

### Controle-opdracht-cluster

Thema: `controle-opdracht`. *Eerste laag-2 discipline-cluster (sub-Kader van `audit-en-assurance`). Vs cross-cutting thema-clusters tot nu (mobiliteit/kapitaalstructuur/werknemers/overdracht/schuldfinanciering). Cluster-naam volgt laag-1-sub-Kader-naam, niet PO-titel "Externe controle" — user-keuze 2026-05-26, omdat PO inhoudelijk ook beoordeling/samenstelling/AUP omvat naast wettelijke controle.*

```
controle-opdracht                       [sub-Kader van audit-en-assurance]
├── controleopdracht                    [K-techniek-Σ, ruggengraat]
│   ▸ 4 fases: aanvaarden ▸ plannen ▸ bewijswerk ▸ afronden+oordeel
│   ▸ delegatie-en-supervisie ▸ professionele oordeelsvorming + skepticism (basisattitude)
├── opdracht-types                      [Σ]  4 types: controle · beoordeling · samenstelling · AUP
│   ▸ normenkader-piramide (ISA/ISRE/ISRS + ITAA-normen) per type
├── audit-planning                      [K-techniek]
│   ▸ kennis-entiteit-en-omgeving (ISA 315)
│   ▸ auditrisicomodel (IR × CR × DR)
│   ▸ materialiteit (overall · performance · specific · kwalitatief)
│   ▸ audit-strategie + werkprogramma
├── audit-bewijs                        [K-techniek]
│   ▸ audit-beweringen (assertions — object van het bewijs)
│   ▸ 7 procedures (inspectie · observatie · navraag · externe-bevestiging · herrekening · herperformance · analytische-procedures)
│   ▸ steekproef (statistisch vs niet-statistisch)
│   ▸ LOR (schriftelijke bevestiging management, ISA 580)
│   ▸ bewijs in IT-omgeving (audittrail · IT-controls · CAATs)
│   ▸ boekhoudkundige schattingen (ISA 540)
│   ▸ NOCLAR (niet-naleving wet+regelgeving, ISA 250)
├── revisiedossier                      [E-instrument]
│   ▸ permanent dossier ▸ lopend dossier
├── audit-afronding                     [K-techniek]
│   ▸ subsequent events (ISA 560)
│   ▸ misstatements-evaluatie
│   ▸ overall analytical review
│   ▸ communicatie governance (ISA 260) + management letter (ISA 265)
└── controleverklaring                  [E-instrument, Σ-oordelen]
    ▸ 4 oordelen: zonder voorbehoud · met voorbehoud · afkeurend · onthouding
    ▸ verslag-componenten + KAM (key audit matters)
    ▸ andere-verslagstypes (overzicht → relaties naar Gebeurtenis-records)
```

**Cross-cluster** (eigen plek elders, relaties hierheen):
- `vennootschap-groottecategorieen` [E+R, cross-cutting] — bepaalt commissaris-trigger + jaarrekening-schema + consolidatieplicht + KMO-norm-toepasselijkheid; thema-cluster TBD (OP-EC.7)
- `commissaris` [E] — beroepsbeoefening-cluster (laag-1 ⏳)
- `onafhankelijkheid` [K-principe + R-regime] — beroepsbeoefening (Lezing A: kader-record + perspectief `beroep-en-deontologie` op werk-fenomenen)
- `aansprakelijkheid-accountant-revisor` [K-principe] — beroepsbeoefening (3 sporen: burgerlijk/strafrechtelijk/tuchtrechtelijk)
- `kwaliteitsmanagement-opdracht` [K-techniek + R-regime] — beroepsbeoefening (ISQM, kantoor-niveau)
- `opdrachtaanvaarding-en-opdrachtbrief` [E + R] — beroepsbeoefening voorstel (geldt voor élk opdrachttype, niet enkel controle) — OP-EC.A
- `continuiteit-going-concern` [K-principe] — eigen K-principe-record cross 1.3/1.6/1.9
- `verbonden-partijen` [E] — cross-cutting E, thema-cluster TBD — OP-EC.B
- `fraude` [G+K] — cross-cutting Gebeurtenis cross 1.6/4.0/witwas — OP-EC.C
- `interne-controle-coso` — blijft primair PO 1.7-cluster, relatie hier

**Schrappen als zelfstandig record / herleiden tot sub-sectie**:
- `controleopdracht-cyclus` → hernoemd `controleopdracht` (cyclus impliciet)
- `assurance-opdracht-types` → hernoemd `opdracht-types`
- `wettelijke-controle-jaarrekening` → opgenomen als gevolg-sectie in `vennootschap-groottecategorieen`
- `commissaris-mandaat-en-statuut` → hernoemd `commissaris` (in beroepsbeoefening)
- `normenkader-audit` → sub-sectie van `opdracht-types`
- `professionele-oordeelsvorming-en-skepticism` → sub-sectie van `controleopdracht` (basisattitude doordringt alle fases)
- `bijzondere-verslagen-vennootschapsverrichtingen` → mapping-actie naar de Gebeurtenissen (Regel J) + sub-sectie `andere-verslagstypes` in `controleverklaring`
- `controleplanning` · `materialiteit-audit` · `auditrisicomodel` · `risicoanalyse-audit` → bundel in `audit-planning`
- `audit-bewijs-verzamelen` · `externe-bevestiging` · `cijferanalyse` · `schriftelijke-bevestiging-management` · `steekproef-audit` · `werkprogramma-audit` · `audit-it-omgeving` · `boekhoudkundige-schattingen` · `niet-naleving-wet-regelgeving-audit` → bundel in `audit-bewijs`
- `delegatie-en-supervisie-audit` → sub-sectie in `controleopdracht`
- `communicatie-met-governance` → sub-sectie in `audit-afronding`
- `kantoor-organisatie-accountant` → beroepsbeoefening-cluster

**Triangulatie-resultaten controle-opdracht** (2026-05-26):
- 20 PO 1.6-anchors (1 taak + 19 kenniselementen) → **0 PO-only gaps** (alles gedekt door minstens 1 bestaand record)
- 34 bestaande records met PO 1.6-anker → **7 records voor cluster zelf** (5× reductie) + 5 records verhuisd naar beroepsbeoefening + 3 cross-thematische + 1 cross-cutting (groottecategorieen) + 14 geabsorbeerd in sub-secties
- 31 kandidaten in DB (alle `gerealiseerd: 0` — 28 ervan bestaan al als record; markering-backlog voor mapping-fase)
- 5 smell-clusters opgelost: (1) `controleopdracht-cyclus`-mega-record bevestigd OK als K-techniek-ruggengraat · (2) planning-versplintering (5 records) gebundeld in `audit-planning` · (3) bewijs-versplintering (5 records) gebundeld in `audit-bewijs` · (4) beroepsbeoefenings-fenomenen verhuisd · (5) bijzondere-verslagen weggemapt naar Gebeurtenis-records (Regel J)

**Mapping-actie — audit-perspectief op Gebeurtenis-records** (in scope, niet uitgesteld):

| Gebeurtenis-record | Audit-perspectief toevoegen | Bron-pin |
|---|---|---|
| `kapitaalverhoging-in-natura` | revisor-verslag-vereiste · inhoud verslag (waardering inbreng) | WVV art 5:133-134 BV / 7:179-181 NV · ITAA-norm-effectennorm (waar relevant) |
| `quasi-inbreng` | revisor-verslag (anti-misbruik) | WVV art 5:138-140 / 7:8-9 |
| `inkoop-eigen-aandelen` | controle netto-actief-test + uitkeringstest | WVV |
| `kapitaalvermindering` (aanzuivering verlies) | revisor-verslag bij aanzuivering | WVV |
| `fusie` ⏳ | revisor-controle ruilverhouding | ITAA-norm-fusie-splitsing |
| `splitsing` / `partiële-splitsing` ⏳ | idem | ITAA-norm-fusie-splitsing |
| `ontbinding-vereffening` ⏳ | revisor/accountant-verslag | ITAA-norm-ontbinding-vereffening |
| `omzetting-vennootschap` ⏳ | revisor-verslag | ITAA-norm-omzetting-vennootschap |

**Bronnen-pin voor cluster**:
- ✅ `ITAA-norm-kmo-controlenorm` (trusted) — hoofdbron, dekt ratione personae/materiae + onafhankelijkheid + planning + voorbeeldverslagen — relevant voor KMO-stagiair-doelpubliek
- ✅ `ITAA-norm-algemene-controlenorm` (trusted) — algemene tegenhanger (niet-KMO)
- ✅ `ITAA-norm-opdrachtbrief` (trusted)
- ✅ `ITAA-norm-samenstellingsopdrachten-isrs4410` (trusted) — compilatie-tak
- ✅ `ITAA-norm-intern-kwaliteitsmanagement` (trusted) — ISQM
- ⏳ ISA-standaarden integraal niet geladen — KMO-norm verwijst "voor zover van toepassing" — beslissingspunt OP-EC.G

**Details per record** (hints voor extractie):

**`controleopdracht`** [K-techniek-Σ]
- inhoud: dwingende 4-fase-flow van een assurance-opdracht — aanvaarden → plannen → bewijswerk → afronden+oordeel. Pedagogische ruggengraat van het cluster. Geen keuze tussen alternatieven (≠ Σ), wel een dwingende methodologie. **Absorbeert**: (a) `#prof-skepticism` als basisattitude-sectie die alle fases doordringt; (b) `#delegatie-en-supervisie` als teamorganisatie-sectie (engagement partner eindverantwoordelijk, review-piramide). Cross-link naar `opdracht-types` (type bepaalt verslag-stijl in fase 4) en `kwaliteitsmanagement-opdracht` (kantoor-niveau-overlay).
- perspectieven: `audit` (uitvoering) · `beroep-en-deontologie` (skepticism, kwaliteit, dossier-discipline) · `advies` (cliënt-communicatie)
- naam_officieel: controleopdracht / assurance-opdracht · synoniemen: audit-cyclus, audit-aanpak, opdracht-uitvoering, engagement lifecycle
- relaties: `opdracht-types`, `audit-planning`, `audit-bewijs`, `audit-afronding`, `controleverklaring`, `revisiedossier`, `opdrachtaanvaarding-en-opdrachtbrief` (start), `commissaris` (uitvoerder bij wettelijke controle), `kwaliteitsmanagement-opdracht`

**`opdracht-types`** [Σ]
- inhoud: 4 fundamentele opdrachttypes geordend op zekerheidsniveau: (a) **controle** (reasonable assurance, positief oordeel — ISA + ITAA-KMO-controlenorm); (b) **beoordeling** (limited assurance, negatief geformuleerd oordeel — ISRE 2400/2410); (c) **samenstelling** (no assurance, geen oordeel — ISRS 4410 + ITAA-samenstellingsnorm); (d) **overeengekomen procedures** (no assurance, feitelijke bevindingen — ISRS 4400). Vergelijkingsmatrix: zekerheidsniveau · oordeelsstijl · verslag-type · toepasselijke norm · typische cliëntcontext. Sub-sectie `#normenkader-piramide` — ISA/ISRE/ISAE/ISRS-internationaal + ITAA-normen-Belgische-overlay.
- perspectieven: `audit` (uitvoering per type) · `advies` (type-keuze met cliënt) · `beroep-en-deontologie` (juiste norm toepassen per type)
- naam_officieel: opdrachten met assurance-niveau · synoniemen: opdrachttypes, assurance-opdrachten, types audit-opdracht, scope of engagement
- relaties: `controleopdracht`, `opdrachtaanvaarding-en-opdrachtbrief`, `controleverklaring`, `commissaris` (wettelijke-controle-context)

**`audit-planning`** [K-techniek]
- inhoud: planningsfase van een controle-opdracht — wat doet de auditor vóór bewijsverzameling. Sub-secties: (a) `#kennis-entiteit-en-omgeving` (ISA 315) — sector, governance, IT, regelgeving; (b) `#auditrisicomodel` — RMM (inherent × controle-risico) + hoe detectie-risico bijsturen via aard/omvang/timing van procedures; (c) `#materialiteit` — overall (5% pre-tax profit / 1% omzet als startpunten ⚠️) + performance (buffer voor cumulatie) + specific (gevoelige posten) + kwalitatief (fraude/classificatie/wettelijk-materiaal); (d) `#audit-strategie-en-werkprogramma` — output van de planning, vertaalt risico-inschatting naar concrete procedures per cyclus/post. **Grens-geval qua grootte (~3-4 pagina's)** — potentiële didactische splits later: `risico-en-materialiteit` afsplitsen.
- perspectieven: `audit` (uitvoering) · `advies` (engagement-letter-finalisatie)
- naam_officieel: planning van de opdracht · synoniemen: audit planning, controleplanning, engagement planning, planningsfase
- relaties: `controleopdracht` (fase 2), `audit-bewijs` (planning bepaalt bewijswerk), `opdrachtaanvaarding-en-opdrachtbrief` (planning na aanvaarding), `verbonden-partijen` (planning-risico), `fraude` (fraude-risico-inschatting), `interne-controle-coso` (controle-risico-inschatting)

**`audit-bewijs`** [K-techniek]
- inhoud: bewijsverzamelings-fase — wat onderbouwt het audit-oordeel. Begint met `#audit-beweringen` (assertions, ISA 315): wat beweert het management impliciet over balans-saldi (bestaan/volledigheid/waardering/rechten) · transacties (occurrence/volledigheid/juistheid/cut-off/classificatie) · toelichtingen. Elke audit-procedure test één of meer beweringen. 7 procedures (ISA 500/505/520): `#inspectie` · `#observatie` · `#navraag` · `#externe-bevestiging` (banken/klanten/leveranciers — ISA 505) · `#herrekening` · `#herperformance` · `#analytische-procedures` (cijferanalyse — ratio's, trends, plausibiliteit). Plus `#steekproef` (ISA 530 — statistisch vs niet-statistisch) · `#schriftelijke-bevestiging-management` (LOR ISA 580) · `#it-bewijs` (audittrail · IT-controls · CAATs — ISA 315/330) · `#boekhoudkundige-schattingen` (ISA 540 — voorzieningen, fair value, going concern) · `#noclar` (niet-naleving wet+regelgeving — ISA 250). **Grens-geval qua grootte (~3-4 pagina's)** — potentiële didactische splits later: `audit-beweringen` afsplitsen.
- perspectieven: `audit` (uitvoering)
- naam_officieel: controle-informatie / audit-bewijs · synoniemen: audit evidence, controlebewijs, controle-instrumenten, audit procedures, audit techniques
- relaties: `audit-planning` (werkprogramma stuurt), `audit-afronding` (input voor oordeel), `revisiedossier` (bewijs gedocumenteerd), `interne-controle-coso` (controls-testen), `verbonden-partijen` (specifieke procedures), `fraude` (fraude-procedures)

**`revisiedossier`** [E-instrument]
- inhoud: gestructureerde verzameling werkdocumenten + controlebewijzen + conclusies opgebouwd tijdens de opdracht — bewijst dat werkzaamheden zijn uitgevoerd + onderbouwt het oordeel. Sub-secties: (a) `#permanent-dossier` — statuten, contracten, governance-structuur, IT-architectuur (multi-jaar relevant); (b) `#lopend-dossier` — planning + werkpapieren + conclusies van het lopende boekjaar. Bewaarplicht — relatie naar `archiefplicht` (beroepsbeoefening). ITAA-norm-intern-kwaliteitsmanagement bevat dossiervorming-eisen.
- perspectieven: `audit` (opmaak) · `beroep-en-deontologie` (bewaartermijn, vertrouwelijkheid, dossier-review bij peer review of tucht)
- naam_officieel: revisiedossier / werkdossier · synoniemen: audit working papers, auditdossier, werkdocumenten, audit file, controledossier
- relaties: `controleopdracht`, `audit-bewijs`, `audit-planning`, `archiefplicht`, `kwaliteitsmanagement-opdracht`

**`audit-afronding`** [K-techniek]
- inhoud: laatste fase vóór ondertekening verslag. Sub-secties: (a) `#subsequent-events` (ISA 560) — gebeurtenissen tussen balansdatum en verslag-datum (eventueel daarna); twee types: adjusting (raken jaarrekening) vs disclosing (alleen toelichting); (b) `#misstatements-evaluatie` — clearing memo, vergelijking met materialiteit, geaccumuleerde fouten; (c) `#overall-analytical-review` — laatste plausibiliteits-check op jaarrekening als geheel; (d) `#communicatie-governance` (ISA 260 — significante bevindingen → bestuur) + (e) `#management-letter` (ISA 265 — interne-controle-deficiencies → management).
- perspectieven: `audit` (uitvoering) · `advies` (management letter = hybride audit-advies)
- naam_officieel: afronding van de opdracht · synoniemen: audit completion, opdrachtafronding, eindfase audit, audit closing
- relaties: `audit-bewijs` (input), `controleverklaring` (output), `continuiteit-going-concern` (going-concern-evaluatie hoort hier), `interne-controle-coso` (deficiencies-communicatie)

**`controleverklaring`** [E-instrument, Σ-oordelen]
- inhoud: schriftelijk eindproduct van een controle-opdracht — communiceert het oordeel aan stakeholders. Σ-aspect: **4 oordelen** geordend op assurance-niveau: (a) `#zonder-voorbehoud` (unqualified) — getrouw beeld in alle materiële opzichten; (b) `#met-voorbehoud` (qualified) — getrouw beeld behalve voor specifiek probleem; (c) `#afkeurend` (adverse) — géén getrouw beeld; (d) `#onthouding` (disclaimer) — onvoldoende bewijs om oordeel te vormen. Sub-secties: `#verslag-componenten` (titel · ontvanger · verantwoordelijkheden bestuur+auditor · basis voor oordeel · oordeel zelf · paragrafen ter benadrukking/andere zaak); `#KAM` (key audit matters — verplicht bij beursgenoteerde + grote onderneming sinds 2016 ⚠️); `#andere-verslagstypes` — overzicht bijzondere revisor-verslagen voor vennootschapsverrichtingen (inbreng-in-natura, quasi-inbreng, fusie, splitsing, ontbinding, omzetting, kapitaalvermindering-aanzuivering) → **primaire verslag-mechanica woont in elke Gebeurtenis-record zelf (Regel J)**; deze sub-sectie geeft alleen overzicht + cross-links + gedeelde verslag-structuur-elementen.
- perspectieven: `audit` (opmaak)
- naam_officieel: controleverklaring · synoniemen: auditverslag, controleverslag, audit report, rapport du commissaire, audit opinion
- relaties: `audit-afronding` (input), `controleopdracht`, alle Gebeurtenis-records voor bijzondere verslagen (kapitaalverhoging-in-natura, quasi-inbreng, fusie, splitsing, ontbinding-vereffening, omzetting-vennootschap, kapitaalvermindering)

**Open punten controle-opdracht-cluster**:
- **OP-EC.A** ⏳ `opdrachtaanvaarding-en-opdrachtbrief` — beroepsbeoefening (geldt voor élk opdrachttype) of controle-opdracht? Voorlopig: beroepsbeoefening. Te valideren bij beroepsbeoefening-cluster-uitwerking.
- **OP-EC.B** ⏳ Primair thema-cluster van `verbonden-partijen` — boekhouding-disclosure (cross PO 2.3 + 2.8 + 1.6) of cross-cutting E zonder primair-thema? Te beslissen bij boekhouding-cluster-uitwerking.
- **OP-EC.C** ⏳ `fraude` primair thema — cross-cutting Gebeurtenis (cross 1.6 audit + 4.0 deontologie + AML witwas)? Bevestigen bij beroepsbeoefening-cluster.
- **OP-EC.D** Potentiële didactische record-splits later: `audit-planning` → `risico-en-materialiteit` afsplitsen; `audit-bewijs` → `audit-beweringen` afsplitsen. Beslissen tijdens content-uitwerking (niet preventief).
- **OP-EC.E** Mapping-actie audit-perspectief op 8 Gebeurtenis-records (zie tabel boven). **Verfijnd 2026-05-26**: niet zomaar "audit-perspectief + revisor-verslag-vereiste", maar specifiek `accountant_perspectieven[].audit` met (a) cross-link naar `bijzondere-mandaten`-record (categorisch begrip, 6e sub-Kader controle), (b) ITAA-norm-pin per type, (c) oordeel-onderwerp specifiek voor de verrichting. Zie §Bijzondere-mandaten-cluster voor volledig schema. In scope, werkpunt voor extractie/operatie-fase per record. Niet uitstellen.
- **OP-EC.F** `interne-controle-coso` blijft primair PO 1.7-cluster — relatie hierheen vanuit `audit-planning` (controle-risico-inschatting) + `audit-bewijs` (controls-testen) volstaat. Bij PO 1.7-cluster te valideren.
- **OP-EC.G** Bron-pin: ISA-standaarden integraal niet geladen. ITAA-normen verwijzen "voor zover van toepassing" — voldoende voor examen-scope? Of kern-ISA's (315, 330, 500, 540, 570, 700) als trusted bron laden? Mappingsbeslissing.
- **OP-EC.7** ⏳ Thema-cluster voor `vennootschap-groottecategorieen` [E+R] — eigen klein cluster `vennootschap-typologie` (samen met `ondernemingsvormen` + `financieel-plan`) of opnemen in `kapitaalstructuur`-cluster? Voorlopig: eigen kandidaat-cluster, te beslissen bij volgende sparring.

**Test-case-validatie** (2026-05-26): 6 representatieve PO 1.6-examen-vragen uit `_programmaonderdeel_classificatie.json` (2008-bibf-vrB3 · 2013-1-vr13/16/19 · 2013-2-vr9/11) door de tree gevoerd:

| Vraag | Concept | Tree-pad | Resultaat |
|---|---|---|---|
| 2013-2-vr9 | 4 soorten auditmethodes | `audit-bewijs#procedures` (de 7 ISA-procedures) | ✅ |
| 2013-2-vr11 | wanneer onthoudende verklaring | `controleverklaring#onthouding` (4e oordeel) | ✅ |
| 2013-1-vr13 | klantenconfirmaties → fraude blootleggen | `audit-bewijs#externe-bevestiging` + cross `fraude` (G) | ✅ |
| 2013-1-vr16 | externe accountant bij ontbinding (staat A/P + continuïteit) | `ontbinding-vereffening` (⏳ Geb) + `continuiteit-going-concern` (cross K-principe) + `controleverklaring#andere-verslagstypes` | ✅ (mits OP-EC.E mapping) |
| 2013-1-vr19 | opdrachtbrief bij omzetting | `opdrachtaanvaarding-en-opdrachtbrief` (beroepsbeoefening per OP-EC.A) + `omzetting-vennootschap` (⏳ Geb) | ✅ (mits OP-EC.E + OP-EC.A) |
| 2008-bibf-vrB3 | bezoldiging commissaris (rubriek+toelichting) | `commissaris` (beroepsbeoefening, vergoeding-aspect) + `jaarrekening`-toelichting | ✅ |

Alle 6 vragen passen in de tree zonder forceren. **Kritische bevestiging**: OP-EC.E (mapping-actie audit-perspectief op Gebeurtenis-records) is geen optionele afronding maar **structureel kritisch** — vr16 + vr19 hangen ervan af. Tree houdt steek alleen als die mapping correct uitgevoerd wordt. Geen structurele gaten ontdekt; geen herziening van cluster-opzet nodig.

### Interne-controle-cluster

Thema: `interne-controle`. *Tweede laag-2 discipline-cluster (sub-Kader van `controle` — discipline hernoemd van `audit-en-assurance` 2026-05-26 om interne controle als 5e sub-Kader te kunnen omvatten). User-keuze: kort `controle` boven `externe-en-interne-controle` of `controle-en-assurance`. Cluster zelf bevat alleen wat IC-eigen is; gedeelde concepten met `controle-opdracht`-cluster leven als **shared records** (zie §Shared records hieronder).*

```
interne-controle                              [sub-Kader van `controle`]
├── interne-controle                          [K-techniek, hoofdrecord]
│   ▸ definitie (1.7.I.A) + 4 doelstellingen (informatie/bescherming/efficiëntie/naleving)
│   ▸ dubbele dimensie (preventief + detectief — 1.7.III.A)
│   ▸ inherente beperkingen + kenmerken (1.7.III.B)
│   ▸ actoren — 3 lines of defense (1.7.IV)
│   ▸ referentiekaders-overzicht (sub-sectie → cross naar coso-framework + COBIT + ISO 31000)
│   ▸ afbakening met externe controle / managementcontrole / interne audit (1.7.I.B-D)
├── ontwerp-interne-controle                  [K-techniek]
│   ▸ methodologie: proces-mapping → risico-identificatie → controle-selectie → documentatie → uitrol (1.7.VIII.A)
├── functiescheiding                          [K-techniek]
│   ▸ 4 onverenigbare functies (autoriseren/uitvoeren/registreren/bewaren — 1.7.VII + VIII.B)
│   ▸ IT-functiescheiding (RBAC — 1.7.X.C)
├── it-controles                              [K-techniek]
│   ▸ ITGC (toegangsbeheer, change management, backup)
│   ▸ application controls (input/processing/output validaties)
│   ▸ fysieke beveiliging (1.7.X.B)
│   ▸ audittrail + logmonitoring (1.7.VIII.E + X.A + X.D)
├── interne-audit                             [E + K-techniek]
│   ▸ 3rd line of defense — onafhankelijke beoordelingsfunctie binnen organisatie
│   ▸ mandaat + functie auditor (1.7.V.A-B)
│   ▸ rapporteert aan auditcomité
├── evaluatie-interne-controle                [K-techniek]
│   ▸ walkthroughs · tests of controls · self-assessments (1.7.VIII.F + XI + XIII)
│   ▸ design effectiveness vs operating effectiveness
│   ▸ cross-link naar audit-planning#kennis-entiteit-en-omgeving (gebruikt door externe auditor)
└── fouten-en-fraude                          [K — lokaal in IC-context]
    ▸ afbakening fouten (onbedoeld) vs fraude (intentioneel) vs verspilling (1.7.VI.A-C)
    ▸ fraudedriehoek (druk + gelegenheid + rationalisatie)
    ▸ cross naar `fraude` Gebeurtenis-record (cross-cutting van controle-opdracht-werk)
```

**Shared records** (leven cross-cutting met thema's `controle-opdracht` + `interne-controle`; details in §Shared records):
- `coso-framework` [K-techniek, NIEUW] — 5 COSO-componenten + ERM (geabsorbeerde 5 oude COSO-records)
- `cyclus-analyse` [Σ, geherbruikt] — 5 cycli (geabsorbeerde 5 oude cyclus-records)
- `auditcomite` [E-orgaan, geherbruikt] — schakel bestuur ↔ interne auditor ↔ commissaris
- `fraude` [G+K, al cross-cutting] — fraude als Gebeurtenis
- `auditrisicomodel` [K, al in audit-planning sub-sectie] — cross-link voor 1.7.V.E

**Cross-cluster** (eigen plek elders, relaties hierheen):
- `managementcontrole` → `bedrijfseconomie-en-management`-discipline (PO 1.7.I.C contrasteert IC met MC — niet hetzelfde; MC = sturing, IC = beheersing)
- `antiwitwas-verplichtingen-accountant` → `beroepsbeoefening`-cluster (al ⏳ daar — primair AML-domein PO 4.0)
- `deontologie-accountant` → `beroepsbeoefening`-cluster
- `externe-audit-commissaris` → gedekt door `commissaris` (beroepsbeoefening) + `controleopdracht` (controle-opdracht-cluster) — schrappen als zelfstandig record
- `bijzondere-verslagen-vennootschapsverrichtingen` → al weg-gemapt naar Gebeurtenis-records (Regel J, OP-EC.E mapping-actie)

**Schrappen als zelfstandig record / herleiden tot sub-sectie**:
- `interne-controle-coso` → samengetrokken met `interne-controle` (hoofdrecord) — verwijst naar `coso-framework` shared record
- `controle-omgeving-coso` · `controle-activiteiten-coso` · `risico-inschatting-coso` · `informatie-communicatie-coso` · `monitoring-coso` → 5 sub-secties van `coso-framework` (shared)
- `aankoopcyclus-ic` · `productiecyclus-ic` · `verkoopcyclus-ic` · `hr-cyclus-ic` · `voorraadcyclus-ic` → 5 sub-secties van `cyclus-analyse` (shared)
- `referentiestelsels-ic` → sub-sectie `interne-controle#referentiekaders` (cross naar `coso-framework`)
- `controlemaatregelen` → sub-sectie van `coso-framework#controle-activiteiten`
- `governance-actoren-ic` → opdelen: (a) 3-lines-of-defense in `interne-controle#actoren`; (b) raadcomité-aspecten in `auditcomite`
- `fouten-en-fraude-cluster` → hernoemd `fouten-en-fraude` (`-cluster`-naam-smell weggewerkt)
- `it-controles-cluster` → hernoemd `it-controles` (idem naam-smell)

**Triangulatie-resultaten interne-controle** (2026-05-26):
- 58 PO 1.7-anchors (1 taak + 57 kenniselementen) → **0 PO-only gaps** (1.7.II.A "begrip onderneming" is te abstract om eigen record te zijn, geen content-gap)
- 28 bestaande records met PO 1.7-anker → **7 records voor cluster zelf** + 3 nieuwe shared (coso-framework, cyclus-analyse, auditcomite) + 5 verhuizingen + 13 geabsorbeerd in sub-secties
- 28 kandidaten in DB (alle `gerealiseerd: 0` — markering-backlog)
- 4 smell-clusters opgelost: (1) COSO-versplintering (6 records) → 1 shared K-techniek met 5+1 sub-secties · (2) cyclus-versplintering (6 records) → 1 shared Σ met 5 sub-secties · (3) `-cluster`-naam-smell op 3 records → hernoemd · (4) audit-functies-cluster (5 records) → verhuisd of geconsolideerd

**Bronnen-pin voor cluster**:
- ✅ `ITAA-norm-intern-kwaliteitsmanagement` (trusted) — ISQM, raakt IC-design
- ⏳ COSO Internal Control-Integrated Framework (2013) — geen primaire bron in `resources/bronnen/`, te overwegen
- ⏳ COSO ERM (2017) — idem
- ⏳ COBIT (IT-governance) — niet kritisch voor examen, overslaan
- ✅ `ITAA-norm-kmo-controlenorm` (trusted) — bevat IC-evaluatie-eisen voor KMO-controle (cross-relatie controle-opdracht)

**Details per record** (hints voor extractie):

**`interne-controle`** [K-techniek, hoofdrecord]
- inhoud: definitie (1.7.I.A: "geheel van procedures, gedragsregels en organisatorische maatregelen dat een onderneming opzet om redelijke zekerheid te krijgen over..."); 4 doelstellingen (informatie betrouwbaar · middelen beschermd · werking doeltreffend · wet/regelgeving nageleefd); **dubbele dimensie** (preventief = vooraf voorkomen + detectief = achteraf vaststellen + correctief = herstellen — 1.7.III.A); **inherente beperkingen** (samenspanning, management override, kosten-baten, menselijke factor — 1.7.III.B); **actoren** = 3 lines of defense (1e lijn management/operationeel · 2e lijn risk+compliance = interne controle · 3e lijn interne audit — 1.7.IV). Sub-sectie `#afbakening` met de 3 verwante functies (externe controle, managementcontrole, interne audit — 1.7.I.B-D). Sub-sectie `#referentiekaders` met overzicht (COSO dominantt → cross naar `coso-framework` shared; COBIT voor IT; ISO 31000 voor risicobeheer — 1.7.XII).
- perspectieven: `advies` (IC-ontwerp bij KMO-cliënt) · `audit` (IC-begrip noodzakelijk voor controle-risico-inschatting via ISA 315)
- naam_officieel: interne controle / système de contrôle interne · synoniemen: internal control, interne beheersing, controleomgeving, beheersingssysteem
- relaties: `coso-framework` (shared, primair referentiekader), `cyclus-analyse` (shared, operationele invulling), `controleopdracht` (extern bouwt op IC), `audit-planning` (controle-risico-inschatting via IC-begrip), `interne-audit` (3rd line), `auditcomite` (shared, governance-toezicht)

**`ontwerp-interne-controle`** [K-techniek]
- inhoud: methodologie voor het opzetten van een IC-systeem in 5 stappen — (1) proces-mapping per cyclus + as-is-analyse; (2) risico-identificatie per processtap; (3) controle-selectie per risico (preventief/detectief, manueel/geautomatiseerd, sleutelcontrole/aanvullend); (4) documentatie in procedures + rolbeschrijvingen + autorisatiematrix; (5) implementatie + training + monitoring. Bevat verwijzing naar COSO-componenten als design-input.
- perspectieven: `advies` (uitvoering voor cliënt) · `audit` (design-effectiveness-evaluatie)
- naam_officieel: ontwerp van interne controle · synoniemen: control design, IC-implementatie, control framework design, uitwerking interne controle
- relaties: `interne-controle` (kader), `coso-framework` (componenten-input), `cyclus-analyse` (per cyclus toepassen), `functiescheiding` (kerntechniek)

**`functiescheiding`** [K-techniek]
- inhoud: organisatorisch principe — onverenigbare functies door verschillende personen laten uitvoeren om fraude + fouten te beperken. **4 functies** (klassieke ACR-IH-leer): (a) Autoriseren — toestemming geven voor een verrichting; (b) Uitvoeren — de verrichting werkelijk doen; (c) Registreren — boeken in administratie; (d) Bewaren — toegang tot activa/voorraden. Eén persoon mag max 2 niet-aangrenzende functies hebben. **Toepassingen**: aankoopcyclus (besteller ≠ ontvanger ≠ betaler), HR (loonsadministratie ≠ uitbetaling), kassa (registratie ≠ controle). **IT-functiescheiding** (1.7.X.C): RBAC = Role-Based Access Control — rollen + rechten in software splitsen tussen aanvrager/goedkeurder/uitvoerder; voorkomt dat één gebruiker complete transactie kan afwerken zonder externe controle.
- perspectieven: `advies` (ontwerp bij cliënt) · `audit` (sleutelcontrole testen)
- naam_officieel: scheiding van functies / segregation of duties · synoniemen: separation of duties, SoD, functie-onverenigbaarheid, rolscheiding, taakverdeling
- relaties: `interne-controle` (kerntechniek), `ontwerp-interne-controle` (toepassing), `cyclus-analyse` (concrete toepassing per cyclus), `it-controles` (RBAC)

**`it-controles`** [K-techniek]
- inhoud: digitale controle-architectuur in geautomatiseerde omgevingen. **ITGC** (IT General Controls): toegangsbeheer (user management, password policy, MFA), change management (development → test → productie + segregation), backup + recovery, operations monitoring. **Application controls** (per applicatie ingebouwd): input controls (validaties, mandatory fields, dropdowns), processing controls (totalen, herrekening, edit checks), output controls (rapportering, distributielijsten). **Fysieke beveiliging** (1.7.X.B): datacenters, toegangscontrole servers, milieubeheer (brand/klimaat). **IT-functiescheiding** → cross naar `functiescheiding`. **Audittrail + logmonitoring** (1.7.VIII.E): wie deed wat wanneer, anomalie-detectie, SIEM. **Specifieke risico's** (1.7.X.A): cyberaanvallen, datalekken, systeemuitval, manipulatie geautomatiseerde verwerking, gebrek audit trail.
- perspectieven: `advies` (IT-controle-ontwerp) · `audit` (IT-bewijs verzamelen — cross naar `audit-bewijs#it-bewijs`)
- naam_officieel: IT-controles / IT controls · synoniemen: ITGC, IT general controls, application controls, geautomatiseerde controles, cyber internal control
- relaties: `interne-controle` (component), `functiescheiding` (IT-RBAC-aspect), `audit-bewijs` (cross-cluster — bewijs in IT-omgeving)

**`interne-audit`** [E + K-techniek]
- inhoud: onafhankelijke + objectieve beoordelingsfunctie binnen de organisatie — **3rd line of defense** (na 1e lijn management + 2e lijn risk/compliance). Toetst of IC + risicobeheer + governance behoorlijk werken. **Mandaat**: vastgelegd in audit charter goedgekeurd door auditcomité; rapporteert aan auditcomité (of bij afwezigheid aan hoogste bestuursorgaan). **Functie auditor** (1.7.V.B): plant audits op risicobasis, voert uit volgens vakinhoudelijke standaarden (IIA-standards), rapporteert bevindingen + remediërings-aanbevelingen, bewaakt objectiviteit (vermijdt operationele beslissingen). **Afbakening**: ≠ externe audit (geen wettelijke assurance over jaarrekening); ≠ compliance (focus op IC-effectiviteit, niet wet-naleving alleen); ≠ interne controle zelf (= 2e lijn).
- perspectieven: `advies` (functie ontwerpen bij grotere cliënt) · `audit` (externe accountant kan steunen op interne-audit-werk via ISA 610)
- naam_officieel: interne audit · synoniemen: internal audit, 3rd line of defense, interne auditfunctie, interne controleurs, objectieve interne beoordeling
- relaties: `interne-controle` (object), `auditcomite` (shared, rapporteringslijn), `controleopdracht` (cross — externe accountant kan steunen via ISA 610), `kwaliteitsmanagement-opdracht` (beroepsbeoefening, parallel concept voor externe-audit-firms)

**`evaluatie-interne-controle`** [K-techniek]
- inhoud: periodieke beoordeling van IC-opzet + IC-bestaan + IC-werking. **Methodes**: (a) `#walkthrough` — één transactie door cyclus volgen om procedures te verifiëren; (b) `#test-of-controls` — controleren of een sleutel-controle effectief werkt over een periode (sample); (c) `#self-assessment` — process owners beoordelen eigen controles. **Twee dimensies** (ISA 315 + ITAA-KMO §3.x): (a) **design effectiveness** — is de controle voldoende ontworpen om risico te mitigeren? (b) **operating effectiveness** — werkt de controle ook effectief in de praktijk over de hele periode? **Output**: input voor bestuur (welke remediërings-acties) en voor externe auditor (steunen op IC of er rond werken — controle-risico-inschatting). **Cross-link kritisch**: dit is dezelfde activiteit als `audit-planning#kennis-entiteit-en-omgeving` (controle-opdracht-cluster) — verschillende rol (intern voor bestuur vs extern voor audit) maar zelfde mechaniek.
- perspectieven: `advies` (interne evaluatie + remediëring) · `audit` (externe accountant doet zelfde activiteit voor controle-risico-inschatting)
- naam_officieel: evaluatie van interne controle / IC-doeltreffendheidstoets · synoniemen: internal control evaluation, control assessment, control self-assessment, operating effectiveness testing, design effectiveness review
- relaties: `interne-controle` (object), `audit-planning` (cross-cluster — externe accountant doet dit ook), `interne-audit` (uitvoerder), `auditcomite` (rapportering)

**`fouten-en-fraude`** [K — lokaal in IC-context]
- inhoud: drievoudige afbakening van afwijkingen — (a) **fouten** (1.7.VI.A): onbedoelde afwijkingen door vergissing, onachtzaamheid, gebrek aan kennis; mitigatie via opleiding + duidelijke procedures + IC-validaties; (b) **fraude** (1.7.VI.B): bewust handelen om misleiding te bewerkstelligen met financieel voordeel — **fraudedriehoek** (druk + gelegenheid + rationalisatie) van Cressey; mitigatie via functiescheiding + onafhankelijke controles + ethisch klimaat; (c) **verspilling** (1.7.VI.C): onnodig of inefficiënt gebruik van middelen zonder fout of fraude — mitigatie via budgetdiscipline + efficiency-indicatoren. **Cross-link**: detail fraude (mechaniek, ISA 240, fraud risk factors) zit in `fraude` Gebeurtenis-record (cross-cutting van controle-opdracht-werk); dit IC-record geeft alleen de afbakening + IC-mitigatie-aanpak.
- perspectieven: `advies` (preventieve maatregelen + bewustwording bij cliënt) · `audit` (fraude-risico-inschatting via ISA 240)
- naam_officieel: fouten en fraude (en verspilling) · synoniemen: errors and fraud, anomalies, irregularities, intentional vs unintentional misstatements
- relaties: `fraude` (cross-cutting Gebeurtenis), `interne-controle` (mitigatie-context), `functiescheiding` (preventief), `evaluatie-interne-controle` (detectie), `antiwitwas-verplichtingen-accountant` (cross — fraude raakt AML)

**Open punten interne-controle-cluster**:
- **OP-IC.A** ⏳ Cluster van COSO en andere frameworks — voorlopig `coso-framework` met sub-sectie `#andere-frameworks` (COBIT, ISO 31000); te valideren tijdens content-uitwerking of COBIT eigen record verdient.
- **OP-IC.B** ⏳ Naam `cyclus-analyse` (K-techniek) of `bedrijfscycli` (E + R)? Conceptueel: bedrijfscycli = het object, cyclus-analyse = de techniek om ze te onderzoeken. Voor Σ-record met sub-cycli is `bedrijfscycli` mogelijk correcter. Voorlopig: `cyclus-analyse` (huidige naam).
- **OP-IC.C** `governance-actoren-ic` opdelen tussen `interne-controle#actoren` en `auditcomite` — ✅ beslist 2026-05-26.
- **OP-IC.D** `interne-audit` in IC-cluster (vs eigen klein cluster) — ✅ beslist 2026-05-26. PO 1.7.I.D + V.A-B plaatsen het hier; technisch is het 3rd line of defense en hoort het bij IC-ecosysteem.
- **OP-IC.E** Mapping-actie 28 PO 1.7-anker-records → nieuwe cluster-structuur. Werkpunt voor extractie/operatie-fase (parallel aan OP-EC.E voor controle-opdracht-mapping).
- **OP-IC.F** COSO-bronnen niet als trusted bron geladen (Engelstalig + behoorlijk groot). Beslissing of we COSO Internal Control-Integrated Framework + COSO ERM toevoegen aan `resources/bronnen/normen/` — relevant voor PO 1.7 maar mogelijk niet noodzakelijk voor examen-scope (ITAA-context is leidend).

**Test-case-validatie** (2026-05-26): 6 representatieve PO 1.7-examen-vragen door de tree gevoerd:

| Vraag | Concept | Tree-pad | Resultaat |
|---|---|---|---|
| 2013-1-vr8 | 4 elementen IC-definitie noemen | `interne-controle#definitie` + `interne-controle#doelstellingen` | ✅ |
| 2013-1-vr11 | Belang budget IC-afdeling | `interne-audit#mandaat` (objectiviteit, prioriteitstelling) | ✅ |
| 2013-1-vr12 | Waarom leveranciersconfirmaties naast boekhouding | `cyclus-analyse#aankoopcyclus` (shared) + `audit-bewijs#externe-bevestiging` (cross-cluster) | ✅ |
| 2013-1-vr13 | Fraudecasus (cheques/leveranciersschulden/dubbele betalingen) | `fouten-en-fraude` + `functiescheiding` + `cyclus-analyse#aankoopcyclus` + cross `fraude` | ✅ |
| 2013-2-vr10 | IC-zwakheden bij specifieke proces | `evaluatie-interne-controle` + `coso-framework#controle-activiteiten` (shared) | ✅ |
| 2013-2-vr12 | Preventieve/repressieve/corrigerende IC-maatregelen | `interne-controle#dubbele-dimensie` + `coso-framework#controle-activiteiten` (shared) | ✅ |

Alle 6 vragen passen zonder forceren. Shared records (`cyclus-analyse`, `coso-framework`, `auditcomite`) bewijzen hun nut — voorkomt duplicatie tussen IC-cluster en controle-opdracht-cluster. Geen structurele gaten.

### Shared records — controle-opdracht ↔ interne-controle

*Records met thema's `controle-opdracht` + `interne-controle` (en eventueel beroepsbeoefening). Leven cross-cutting in beide clusters zichtbaar. Geen duplicatie van inhoud — record bestaat 1×, perspectieven en sub-secties leggen de twee gebruikswijzen vast.*

**`coso-framework`** [K-techniek-Σ, shared] — *absorbeert: `interne-controle-coso`, `controle-omgeving-coso`, `risico-inschatting-coso`, `controle-activiteiten-coso`, `informatie-communicatie-coso`, `monitoring-coso`, `controlemaatregelen`*
- inhoud: het Committee of Sponsoring Organizations-raamwerk = wereldwijd dominante referentie voor IC-design en IC-evaluatie. **5 geïntegreerde componenten** (COSO IC-IF 2013): (a) `#controle-omgeving` — tone at the top, integriteit + ethische waarden, commitment to competence, board governance, structuur + bevoegdheden, accountability (1.7.II.G + IV); (b) `#risico-inschatting` — risico-identificatie, risico-analyse, fraude-risico-overweging, change management (1.7.XII.F + VIII.A); (c) `#controle-activiteiten` — preventief vs detectief vs correctief; manueel vs geautomatiseerd; sleutelcontrole vs aanvullend (1.7.VIII.C-D + X.D); (d) `#informatie-en-communicatie` — kwaliteit informatie, interne communicatie, externe communicatie (1.7.II.B + II.D); (e) `#monitoring` — ongoing monitoring (in processen ingebouwd) + separate evaluations (interne audit, externe assurance) (1.7.VIII.F + XI). Sub-sectie `#coso-erm-variant` — COSO ERM 2017 verbreedt naar strategie + performance, met risk appetite + risico-portefeuille-aanpak (1.7.XII.E). Sub-sectie `#andere-frameworks` (OP-IC.A): COBIT voor IT-governance; ISO 31000 voor risicobeheer-only.
- perspectieven: `audit` (controle-risico-inschatting via ISA 315 — externe auditor begrijpt IC via COSO-lens) · `advies` (IC-design KMO + verbeterpunten)
- naam_officieel: COSO Internal Control-Integrated Framework / COSO IC-IF · synoniemen: COSO 2013, vijf componenten van interne controle, COSO-kubus, COSO-piramide, Internal Control Integrated Framework
- thema's: `controle-opdracht`, `interne-controle`
- relaties: `interne-controle` (kerntechniek + referentiekader), `audit-planning` (controle-risico-inschatting via componenten), `evaluatie-interne-controle` (evaluatie-aspect = component "monitoring"), `cyclus-analyse` (controle-activiteiten worden per cyclus toegepast)

**`cyclus-analyse`** [Σ, shared] — *absorbeert: `aankoopcyclus-ic`, `productiecyclus-ic`, `verkoopcyclus-ic`, `hr-cyclus-ic`, `voorraadcyclus-ic`*
- inhoud: methodische opsplitsing van de bedrijfsvoering in **5 typische cycli** met elk eigen risico's + sleutel-controles + drie-way-matching-patronen. Vergelijkingsmatrix: per cyclus de typische processtappen · risico's · sleutelcontroles · IT-systemen · KPI's. Sub-secties: (a) `#aankoopcyclus` (P2P, procure-to-pay) — behoefte → bestelling → ontvangst → factuur → betaling; sleutel: three-way matching (PO + GR + invoice); risico's: ongeoorloofde aankopen, dubbele betalingen, fictieve leveranciers (1.7.IX.A); (b) `#productiecyclus` — grondstoffen → WIP → afgewerkt product; kostprijsallocatie + voorraad-mutaties; risico's: rendementsverlies, schrootverwerking, foute kostenverdeling (1.7.IX.B); (c) `#verkoopcyclus` (O2C, order-to-cash) — order → kredietcheck → levering → facturatie → inning; risico's: fictieve verkopen, cut-off-fouten, oneigenlijke kortingen; sleutel: prijslijst-discipline + kredietgrenzen (1.7.IX.C); (d) `#hr-cyclus` (hire-to-retire) — aanwerving → contract → loonberekening → uitbetaling → uitdiensttreding; sleutel: functiescheiding payroll-administratie vs uitbetaling; risico's: fictieve werknemers, foute loonparameters (1.7.IX.D); (e) `#voorraadcyclus` — perpetual inventory + periodieke fysieke tellingen; cut-off rond balansdatum; magazijnbeveiliging + bin cards (1.7.IX.E).
- perspectieven: `audit` (externe auditor controleert per cyclus — substantive testing + tests of controls) · `advies` (cyclus-ontwerp + IC-design per cyclus voor cliënt)
- naam_officieel: cyclus-analyse / cyclus-aanpak · synoniemen: business cycle analysis, cyclusbenadering, transaction cycles, P2P/O2C/H2R, process cycles
- thema's: `controle-opdracht`, `interne-controle`
- relaties: `interne-controle` (operationele invulling), `coso-framework` (controle-activiteiten worden per cyclus toegepast), `functiescheiding` (per cyclus concreet), `audit-bewijs` (cross-cluster — substantive testing per cyclus), `it-controles` (cyclus-specifieke applicatiecontroles)

**`auditcomite`** [E-orgaan, shared]
- inhoud: gespecialiseerd raadcomité binnen het bestuursorgaan — **toezicht op**: (a) financiële verslaggeving (jaarrekening-kwaliteit, accounting policies, schattingen); (b) interne controle + risicobeheer (IC-effectiviteit, deficiency-remediëring); (c) externe audit (commissaris-benoeming-voorstel, onafhankelijkheid-bewaking, fee-bespreking, KAM-discussie); (d) interne audit (audit charter, plan, key findings). **Samenstelling**: minimum aantal niet-uitvoerende bestuurders met financiële expertise; voorzitter onafhankelijk (1.7.V.D). **Schakel** tussen bestuur ↔ interne auditor ↔ commissaris — driehoek-overleg waarborgt onafhankelijke informatiestromen. **Verplichting**: in België voor beursgenoteerde + bepaalde grote/middelgrote vennootschappen (WVV art X ⚠️); voor andere optioneel maar best practice.
- perspectieven: `audit` (commissaris communiceert met auditcomité — ISA 260) · `advies` (charter-ontwerp + samenstellings-advies) · `beroep-en-deontologie` (vertrouwelijkheid + onafhankelijkheid-bewaking)
- naam_officieel: auditcomité · synoniemen: audit committee, audit commissie, toezichtscomité audit, raadcomité financiële verslaggeving, comité voor audit en risico
- thema's: `controle-opdracht`, `interne-controle`, `beroepsbeoefening`
- relaties: `interne-audit` (rapporteringslijn), `commissaris` (beroepsbeoefening — externe communicatielijn), `interne-controle` (toezichtsobject), `audit-afronding` (cross — communicatie governance gaat hierheen), `bestuur` (parent-orgaan)

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
| 2026-05-26 | Cluster-naam `controle-opdracht` (=laag-1-sub-Kader-naam onder `audit-en-assurance`), niet PO-titel "externe controle" | Cluster-naam = `externe-controle` letterlijk volgen PO 1.6 | PO-titel suggereert "alleen wettelijke controle" terwijl PO inhoudelijk ook beoordeling/samenstelling/AUP omvat. Sub-Kader-naam is conceptueel correcter en mapt 1-op-1 op laag-1-structuur. | Toekomst: andere PO-clusters die laag-1-sub-Kaders uitwerken volgen zelfde naam-conventie (PO 1.7 → `interne-controle`, PO 2.3 → `vennootschapsbelasting`, etc.). |
| 2026-05-26 | **Anti-preventieve-versnippering-principe**: nieuwe K-techniek/Σ-records starten gebundeld met sub-secties; splitsen alleen op didactische gronden (grootte, voorbeelden, vraag-patronen) tijdens content-uitwerking | Pre-splitsen per ISA-norm of per PO-anchor-sub-stap (record-per-sub-concept) | User-principe 2026-05-26: "het kan zijn dat we om didactische redenen nog gaan moeten splitsen, maar dat zal gegronder zijn dan op voorhand versnipperen". Versplintering is precies wat de tree wou tegengaan; gebundelde-start preserveert samenhang + sub-secties zijn al expliciet als extractie-hints zichtbaar. Latere splits zijn beslissingen op feitelijke zwaarte, niet op a-priori-categorisatie. | Toegepast op `audit-planning` (1 record + 4 sub-secties ipv 5 records) en `audit-bewijs` (1 record + 11 sub-secties ipv 9 records). Toekomst: alle nieuwe clusters volgen dit principe als default. |
| 2026-05-26 | Beroepsbeoefenings-fenomenen (onafhankelijkheid, aansprakelijkheid, kwaliteitsmanagement, commissaris) verhuizen uit `controle-opdracht`-cluster naar `beroepsbeoefening`-cluster (laag-1 ⏳) — **Lezing A**: kader-records + perspectief `beroep-en-deontologie` naast elkaar | Lezing B (alleen perspectief, geen aparte records) of Lezing C (gedeeltelijke absorptie in werk-fenomenen) | Stagiair heeft centrale blokken nodig voor onafhankelijkheid + aansprakelijkheid + AML als zelfstandige examen-onderwerpen. User-keuze 2026-05-26: "er mag een kader zijn rond deontologie etc., maar 'de praktijk'/'hoe uit zich dat' zal terugkomen in de perspectieven". Perspectief verwijst naar het kader-record (geen content-duplicatie). | Toekomst: alle deontologische principes (witwasplicht-aml, archiefplicht, permanente-vorming, tuchtprocedure-itaa) leven primair in `beroepsbeoefening`-cluster; werk-fenomenen krijgen `beroep-en-deontologie`-perspectief met verwijzing. |
| 2026-05-26 | `wettelijke-controle-jaarrekening` als zelfstandig record schrappen; commissaris-verplicht-trigger + KMO-norm-toepasselijkheid + jaarrekening-schema-keuze + consolidatieplicht opnemen als gevolgen-cascade in `vennootschap-groottecategorieen` [E+R, cross-cutting] | Aparte Regeling-record `commissaris-verplichting` of `wettelijke-controle-regime` | Grootte-criteria art 1:24-1:27 WVV zijn één fenomeen met cascade van gevolgen (Regel J: één fenomeen × alle dimensies). Aparte Regeling-record zou één gevolg uit de cluster lostrekken en samenhang breken. User-observatie 2026-05-26: "waarom zetten we die regeling niet mee op de groottecriteria → de gevolgen ervan?" | Te flaggen: fiscale KMO-criteria art 1:24-1:25 WIB hebben eigen criteria (gedeeltelijk overlappend, niet identiek met WVV) — apart te behandelen of als sectie in `vennootschap-groottecategorieen` met "let op: fiscaal-KMO ≠ vennootschapsrechtelijk-KMO". |
| 2026-05-26 | Bijzondere revisor-verslagen (inbreng-natura, quasi-inbreng, fusie, splitsing, ontbinding, omzetting, kapitaalvermindering-aanzuivering) wonen als `audit`-perspectief in de Gebeurtenis-records zelf; sub-sectie `andere-verslagstypes` in `controleverklaring` voor overzicht + cross-links | Eigen Σ-record `bijzondere-verslagen-vennootschapsverrichtingen` met sub-secties per type | Regel J — verplichting + verslag-inhoud + audit-werk zit bij de Gebeurtenis (één fenomeen × alle dimensies). User-observatie 2026-05-26: "zouden we de wettelijke verplichting niet bij de gebeurtenissen zelf hangen?". Bron-pin staat klaar (ITAA-norm-fusie-splitsing, -ontbinding-vereffening, -omzetting, -effectennorm — alle trusted). Mapping-actie expliciet: 8 Gebeurtenis-records krijgen `audit`-perspectief met revisor-verslag-vereiste — niet uitgesteld, werkpunt voor extractie/operatie-fase. | Analoog: andere wettelijk-vereiste-revisor-verslagen die we later vinden (effecten-uitgifte, omzetting in andere vennootschapsvorm, ...) volgen zelfde principe — verplichting bij het fenomeen, niet bij audit-cluster. |
| 2026-05-26 | `ITAA-norm-kmo-controlenorm` als hoofdbron-pin voor controle-opdracht-cluster — KMO-norm dekt ratione personae/materiae + onafhankelijkheid + planning + voorbeeldverslagen voor het examen-doelpubliek (KMO-stagiair) | Integrale ISA-standaarden-load als primaire bron | KMO-norm is de Belgische geconcretiseerde norm voor het examen-doelpubliek; ISA's worden er "voor zover van toepassing" doorgegeven. Andere ITAA-normen (algemene-controlenorm, opdrachtbrief, ISRS-4410-samenstelling, intern-kwaliteitsmanagement) vullen aan. Beslissing of integraal-ISA-load nodig is = OP-EC.G voor mapping-fase. | Toekomst: per cluster expliciete bronnen-pin-sectie. Voor PO 1.7 (interne controle) wellicht ander pin (CBN-advies + ITAA-norm-intern-kwaliteitsmanagement); voor PO 2.3 (VenB) wettekstenbundel + circulaires. |
| 2026-05-26 | ~~Discipline-clusters niet in compact snapshot~~ → **HERZIEN later 2026-05-26**: discipline-clusters worden óók in compact snapshot opgenomen, als aparte sub-blok "Discipline-cluster-uitwerkingen" na cross-cutting thema-clusters | (oorspronkelijk) Discipline-clusters opnemen in compact snapshot (zou snapshot opblazen) | User-observatie 2026-05-26: cross-cutting clusters tonen wél records in snapshot, discipline-clusters niet → inconsistente leeswijzer. Snapshot moet *alle* uitgewerkte werk-eenheden tonen ongeacht categorie. Compact-tree-format (1 lijn per record + sub-secties op zelfde lijn) is al schaalbaar genoeg. | Toekomst: alle uitgewerkte clusters (cross-cutting thema's én discipline-sub-Kaders) in compact snapshot. Aparte sub-blok-headers voor leeswijzer (Cross-cutting clusters · Discipline-cluster-uitwerkingen). |
| 2026-05-26 | Discipline `audit-en-assurance` hernoemd naar **`controle`**; `interne-controle` toegevoegd als 5e sub-Kader naast `controle-opdracht` / `beoordelings-opdracht` / `isae-opdrachten` / `overeengekomen-procedures` | Behoud `audit-en-assurance` (4 sub-Kaders, IC elders) of langere naam `externe-en-interne-controle` | "audit-en-assurance" omvatte conceptueel alleen externe assurance-opdrachten; PO 1.7 (interne controle) past daar niet onder (IC = wat de onderneming zelf opzet, geen assurance-opdracht). Maar PO 1.7 raakt audit + IC samen via uitgebreide overlap (auditcomité, COSO, cyclus-analyse, fraude, IC-evaluatie). User-keuze 2026-05-26: kort `controle` boven `externe-en-interne-controle` (volgt minimalistische naam-conventie zoals `boekhouding`, `fiscaliteit`). | Toekomst: andere disciplines mogen analoog hernoemd worden bij sub-Kader-uitbreiding indien naam scope niet meer dekt. |
| 2026-05-26 | **Shared records** als pattern formeel ingevoerd: records die met meerdere thema's leven en in meerdere clusters zichtbaar zijn (record bestaat 1×, perspectieven/sub-secties leggen verschillende gebruikswijzen vast) | (a) Inhoud dupliceren tussen clusters; (b) Mega-cluster bouwen dat overlap absorbeert (60+ records); (c) Sterke versplintering per PO | User-observatie 2026-05-26: "ik lees toch dat er een grote overlap is met externe controle? valt het dan niet allemaal onder 'controle'?". Overlap PO 1.6 ↔ PO 1.7 is reëel + groot (COSO, cyclus-analyse, fraude, auditcomité, audit-functies). Maar mega-cluster (78 anchors gecombineerd) breekt leeswijzer; aparte clusters met shared records erkent overlap zonder versmelting. Schema-impact: `thema: []` is al lijst, dus shared records leven al; navigatie-tabel in skelet-doc maakt ze expliciet. | Toekomst: andere PO's die elkaar deels overlappen volgen zelfde patroon (bv. PO 2.1 BTW-basisbeginselen + PO 2.7 BTW-controle; PO 1.1 boekhouding + PO 1.4 consolidatie; PO 1.8 boekhoudkundige expertise + PO 1.9 jaarrekening-analyse). |
| 2026-05-26 | **Anti-versnippering toegepast op PO 1.7**: 6 COSO-component-records → 1 shared `coso-framework` K-techniek met 5+1 sub-secties; 6 cyclus-records → 1 shared `cyclus-analyse` Σ met 5 sub-secties; cluster-eigen records ~7 (28 → 7 cluster + 3 nieuwe shared + 5 verhuizingen + 13 absorpties) | Behoud 28 aparte records of pas alleen kleinere consolidaties toe | Past entry "anti-preventieve-versnippering" toe op concreet werk. PO 1.7.XII.D zegt expliciet "5 geïntegreerde componenten" → bundelen volgt PO-structuur. Cycli zijn klassiek Σ-pattern (5 alternatieven met vergelijkings-/keuze-vraag). User-feedback "veel veel veel logischer": consolidatie werkt. Latere splits per COSO-component of per cyclus blijven mogelijk op didactische gronden. | Voor PO 1.7 specifiek: latere splits-kandidaten zijn `coso-framework#risico-inschatting` (zwaar onderwerp, ook aparte ISO 31000-context) en `cyclus-analyse#hr-cyclus` (overlap payroll-K-techniek bij werknemers-vergoedingen-cluster). Beslissen tijdens content-uitwerking. |
| 2026-05-26 | `-cluster`-suffix in record-naam = **smell** (schema-artefact, geen conceptnaam). Vermijden in record-id; gebruik thema-tag of skelet-cluster-positionering | Behoud `fouten-en-fraude-cluster`, `it-controles-cluster`, `*-cluster` als record-namen | Record-id moet conceptnaam zijn (`fouten-en-fraude`, `it-controles`), niet duiden op verzamel-aard (`-cluster` doet dat). Verzamel-aard wordt gedragen via tags `[Σ]` of `[K-techniek]` of via cluster-positionering in skelet-doc — niet via record-naam. Naam-smell scan tijdens mapping-fase. | Mapping-actie: scan bestaande 396 records op `-cluster`/`-cluster.json` suffix; hernoemen via `tools/lib/records_api.py rename_record`. |
| 2026-05-26 | `managementcontrole` verhuist naar `bedrijfseconomie-en-management`-discipline (niet onder `controle`); PO 1.7.I.C contrasteert IC met managementcontrole en plaatst MC pedagogisch in IC-context, maar inhoudelijk is MC sturingsgericht (budget/KPI) ≠ beheersingsgericht (IC) | Behoud `managementcontrole` in interne-controle-cluster (volgt PO 1.7-presentatie) | PO 1.7.I.C is **afbakeningsanchor** ("MC is wat anders dan IC"), geen inhoudelijk MC-anchor. Inhoudelijke MC-stof (budget, kpi, variance, balanced scorecard) hoort in `bedrijfseconomie-en-management`-discipline (laag-1 ⏳). Afbakening blijft als sub-sectie `interne-controle#afbakening` met cross-link. | Analoog: `interne-audit` blijft wel in IC-cluster (anders dan MC) want het is structureel onderdeel van het IC-ecosysteem (3rd line of defense — PO 1.7.IV+V). Afbakening ≠ wegverhuizen. |
| 2026-05-26 | **Cluster-typen-onderscheid geschrapt** (cross-cutting thema-cluster vs discipline-cluster). Alle uitgewerkte clusters zijn voortaan "clusters" — verschil zit alleen in PO-mapping-breedte (1 PO vs meerdere), niet in structuur-type. Regel mei 2026 "discipline-stam = alleen Kader-records, alle E/G/R cross-cutting" **versoepeld**: cluster-uitwerkingen mogen K + E + G + R + Σ bevatten zolang conceptueel coherent. | (a) Behoud 2 sub-blokken in snapshot met PO-mapping-rationale; (b) Originele restrictieve regel handhaven en E/G/R uit discipline-clusters eruit halen (zou clusters breken — `revisiedossier` E in controle-opdracht; `interne-audit` E+K in interne-controle; etc.) | User-observatie 2026-05-26: "waarom maak jij een verschil tussen Cross-cutting clusters (per thema) en de Discipline-cluster-uitwerkingen (laag-2 sub-Kaders)?" Onderscheid was artefact van eerdere ontstaansgeschiedenis (eerst werkten we thema-clusters uit, daarna PO-gebaseerde clusters) + originele restrictieve regel die niet stand hield bij PO 1.6 + 1.7 (revisiedossier, controleverklaring, interne-audit, auditcomite zijn E maar horen conceptueel in hun cluster). Versimpeling: één cluster-begrip; PO-mapping als metadata-kolom in navigatie-tabel. | Toekomst: alle volgende clusters volgen één model; geen distinction nodig. ADR-030 dienovereenkomstig bij te werken (Regel-bepaling over disciplinestam vs cross-cutting moet weg of versoepeld). Eerdere rationale-log-entries 2026-05-23 over "Entiteiten + Gebeurtenissen cross-cutting (eigen stammen)" + "alle Regelingen leven cross-cutting" + "discipline-stam = alleen Kader" blijven gelden voor laag-1 (top-disciplines mogen alleen Kader zijn) — versoepeling alleen voor laag-2 cluster-uitwerkingen. |
| 2026-05-26 | **`-rechtsvorm`-suffix als naam-smell** (analoog aan `-cluster`-smell uit PO 1.7). Record-id = conceptnaam, geen schema-categorie-marker als suffix. Hernoemen: `bv-rechtsvorm` → `besloten-vennootschap`, `nv-rechtsvorm` → `naamloze-vennootschap`, etc. Volledige naam in id, afkorting in synoniemen[] (regel 8 CLAUDE.md). | Behoud `-rechtsvorm`-suffix (duidt schema-categorie) of gebruik korte afkortingen als id (`bv`, `nv`) | User-vraag 2026-05-26: "heeft elke vorm wel een aparte fiche nodig? gingen we niet wegblijven van suffixen?". Suffix verwijst naar schema-functie (= rechtsvorm-type) niet conceptnaam — geen toegevoegde info. Afkortingen als id botsen met CLAUDE.md regel 8 ("geen afkortingen in code/docs/schema's"). Volledige naam + synoniemen-lijst is consistent met `cash-for-car`-pattern (id = praktijk, synoniemen = officieel + afkortingen). | Naam-smell-scan-actie uitgebreid: suffixen `-rechtsvorm`, `-cluster`, `-ic` (zoals `aankoopcyclus-ic`) toevoegen aan scan-lijst voor mapping-fase. Algemene regel: scan alle 396 records op suffix-patroon dat schema-categorie aanduidt zonder conceptuele waarde. |
| 2026-05-26 | `vof-commv-rechtsvorm` **splitsen** in `vennootschap-onder-firma` (VOF) + `commanditaire-vennootschap` (CommV) — 2 verschillende fenomenen onder 1 oude record-naam | Behoud `vof-commv` als 1 record (volgt WVV-boek-4 dat beide samen behandelt) | User-keuze 2026-05-26 + rationale-log 2026-05-24 `en`-smell-pattern: VOF heeft alleen volle aansprakelijkheid; CommV heeft 2 vennoten-typen met verschillende aansprakelijkheidsregimes (gecommanditeerden vol + commandités beperkt). Gedeelde context (personenvennootschap) blijft via `ondernemingsvormen`-vergelijkingsmatrix; sub-secties per vorm zouden inconsistent zijn met BV/NV/CV-aparte-records-patroon. | Analoog: andere `en`-namen bij vorm/categorisering opnieuw bekijken bij mapping-fase. Voor PO 3.0 nog: `aansprakelijkheid-oprichters-bestuurders` — zit dit goed als 1 record of moeten oprichters + bestuurders apart (verschillende personen, verschillende aansprakelijkheidsregimes)? Te beslissen bij `bestuur-en-aansprakelijkheid`-cluster. |
| 2026-05-26 | `keuze-rechtsvorm-fiscaal` schrappen als eigen record; wordt **perspectief** `advies` + `fiscaal-VenB/PB` op `ondernemingsvormen`-Σ-record | Behoud `keuze-rechtsvorm-fiscaal` als eigen record (fiscale keuze ≠ juridische keuze) | User-observatie 2026-05-26: "zijn dat niet net twee verschillende perspectieven over dezelfde concepten?" — ja. Fenomeen = vormkeuze; perspectieven = juridisch (record-inhoud) + fiscaal (perspectief). Aparte records voor "juridische versie" + "fiscale versie" van zelfde keuze = duplicatie. Dit is precies wat `accountant_perspectieven[]` doet — zelfde fenomeen, andere werk-as. | **Algemeen principe formaliseren**: 2 perspectieven op zelfde fenomeen ≠ 2 records. Alleen apart record als 2 verschillende fenomenen of substantieel-andere kennisbron. Smell: "X-fiscaal" / "X-juridisch" / "X-boekhoudkundig" record-namen = perspectief-vermomming-smell. Toekomst: scan op deze namen tijdens mapping-fase. |
| 2026-05-26 | Initiële inbreng = **sub-sectie van `oprichting-vennootschap`**, geen aparte Gebeurtenis-record | Eigen Gebeurtenis-record `initiele-inbreng` als pendant van `kapitaalverhoging` (= latere inbreng) | User-vraag 2026-05-26: "misschien gebeurtenis opsplitsen in oprichting en initiële inbreng?". Praktisch: gelijktijdig (initiële inbreng vóór notariële akte als bewijs van volstorting). Geen aparte vragen rond elk — initiële inbreng is sub-thema van oprichting. Geen symmetrie met `kapitaalverhoging` (=latere fase met eigen context). Volgt rationale-log 2026-05-23 `pro-rata-toerekening`-pattern: sub-aspect ≠ eigen record. | Sub-sectie `#initiele-inbreng` in `oprichting-vennootschap` (kapitaalstructuur-cluster): modaliteiten (geld/natura/arbeid voor CV) · revisorverslag bij natura · min-storting bij authentieke akte (BV/NV) · volstortings-eisen · cross-relatie naar `kapitaalverhoging-in-natura` (analoge mechaniek). Mapping-actie. |
| 2026-05-26 | `-accountant`-suffix als naam-smell (analoog aan `-cluster`/`-rechtsvorm`/`-ic`/`-fiscaal`). Hernoemd: `deontologie-accountant` → `deontologie`, `beroepsgeheim-accountant` → `beroepsgeheim`, `permanente-vorming-accountant` → `permanente-vorming`, `kantoor-organisatie-accountant` → `kantoor-organisatie`. `aansprakelijkheid-accountant-revisor` → `beroepsaansprakelijkheid` (compacter, dekt beide beroepen). `antiwitwas-verplichtingen-accountant` → `antiwitwaspreventie` (compacter). | Behoud `-accountant`-suffixen als beroep-marker | Cluster `beroepsbeoefening` zegt al expliciet dat alle records over de beroepsbeoefenaar gaan — suffix is redundant. Voor `aansprakelijkheid-accountant-revisor` was de suffix dubbel-info maar onhandig lang; samenstelling `beroepsaansprakelijkheid` dekt beide beroepen en is conform `boekhoudaansprakelijkheid`/`fiscale-aansprakelijkheid`-patronen die elders kunnen ontstaan. User-keuze 2026-05-26: "OP-BB.A ja, opruimen". | Naam-smell-scan voor mapping-fase uitgebreid: suffixen `-cluster` · `-rechtsvorm` · `-ic` · `-fiscaal` · `-accountant` · `-aww` (= afkorting-suffix, schendt regel 8 CLAUDE.md). Algemene regel: suffix die schema-categorie / cluster-context / beroeps-marker dupliceert = smell. |
| 2026-05-26 | AML als **1 overkoepelend record** `antiwitwaspreventie` met 5 sub-secties (cliëntenonderzoek · ubo-register · risicogebaseerde-benadering · melding-cfi · intern-beleid) | 5 aparte records (huidige situatie: clientenonderzoek-aww + ubo-register + risicogebaseerde-benadering-aww + melding-verdachte-transactie-cfi + antiwitwas-verplichtingen-accountant) | Anti-preventieve-versnippering-principe (rationale-log 2026-05-26). User-keuze "OP-BB.B aml : beginnen met één record". AML-regime is één coherent wettelijk kader (AML-wet 18-09-2017) met deelverplichtingen — geen aparte alternatieven (≠ Σ). Sub-secties kunnen later splitsen indien een aspect didactisch te zwaar wordt. Plus: `-aww`-suffix-smell (afkorting) op 3 records weggewerkt door bundeling. | Pattern: andere wettelijke regimes met meerdere verplichtingen-blokken kunnen analoog bundelen (bv. `bezwaarprocedure-fiscaal` met sub-secties bezwaar/beroep/cassatie ipv aparte records). |
| 2026-05-26 | `gecertificeerd-accountant` als **nieuw E-actor-record** voor het beroep zelf (statuut · toelatingsvereisten · monopolieopdrachten · stagiair-regime · onverenigbaarheden) | Beroepsinfo verdelen tussen `itaa-beroepsorganisatie` + `deontologie` zonder centrale actor-record | User-keuze "OP-BB.C gecertificeerd-accountant, ja steek hem er maar thuis". Analoog aan `commissaris`-E-record (bijzondere hoedanigheid) — `gecertificeerd-accountant` is de generieke variant. Test-case-validatie bevestigt: 2 van 6 testvragen (K1 onverenigbaarheden + K5 stagiair) raken specifiek deze record-inhoud, die nergens anders thuishoort. | Pattern: actor-records voor gereglementeerde beroepen (`bedrijfsrevisor` ⏳ als parallel + cross-relatie, eventueel `belastingadviseur` ⏳, ...) volgen zelfde patroon — eigen statuut + verplichtingen. |
| 2026-05-26 | `kantoor-organisatie` als overkoepelend record **absorbeert** `communicatie-met-stakeholders` + `digitalisering-accountantskantoor` als sub-secties | 3 aparte records voor 4.0.taak.2 + 4.0.taak.4 + 4.0.taak.5 | User-keuze "OP-BB.D kantoor-organisatie -> probeer maar te combineren". 3 thema's hangen samen rond "hoe runt het kantoor zijn praktijk?" — team-coördinatie + stakeholder-communicatie + digitale werkomgeving zijn 3 perspectieven op zelfde fenomeen (kantoor-praktijk). Anti-versnippering. `digitalisering`-sub-sectie kan later splitsen indien cyber/AVG/digitale-archief substantieel groeit. | `businessmodel-en-strategie-inzicht-accountant` daarentegen verhuist cross naar `bedrijfseconomie-en-management`-discipline — dat is geen kantoor-praktijk-thema maar een meta-competentie (4.0.taak.6) die elders thuishoort. |
| 2026-05-26 | **`bestuur-en-aansprakelijkheid`-cluster** voor PO 3.0.II + VII; split bestaand record `aansprakelijkheid-oprichters-bestuurders` in `oprichtersaansprakelijkheid` + `bestuurdersaansprakelijkheid` (`-en-`-naam-smell, precedent `vof-commv`). Kwijting blijft sub-sectie van `bestuurdersaansprakelijkheid` (anti-preventieve-versnippering); split mogelijk later op didactische zwaarte (OP-BA.B). | (a) Behoud `aansprakelijkheid-oprichters-bestuurders` als 1 record; (b) Kwijting als eigen record | Test-case-validatie: 2 van 3 PO 3.0.VII-testvragen raken alleen `oprichtersaansprakelijkheid`, niet `bestuurdersaansprakelijkheid` — bevestigt dat het 2 verschillende fenomenen zijn (verschillende personen, verschillende triggers, verschillende wettelijke grondslag). Vergelijking BV-vs-NV bij oprichtersaansprakelijkheid (vr K5) leeft natuurlijker als eigen record. | Pattern: bij elke `-en-`-naam scan systematisch of 2 fenomenen onder 1 naam geforceerd zijn. Voor PO 3.0 nog te checken: `aandeelhoudersovereenkomsten-en-methodes-om-de-controle-te-verwerven` (3.0.VI-titel) — al opgelost via aparte clausule-sub-secties. |
| 2026-05-26 | **`bijzondere-mandaten`** als 6e sub-Kader van `controle`-discipline + **shared thema** met `beroepsbeoefening`. Eén klein hoofdrecord (categorisch overzicht); concrete uitvoering per type woont als `accountant_perspectieven[].audit` op de betrokken Gebeurtenis-records. **OP-EC.E mapping-actie verfijnd**: niet zomaar "audit-perspectief", maar perspectief met cross-link naar `bijzondere-mandaten` (categorisch) + ITAA-norm-pin (per type) + oordeel-onderwerp specifiek. | (a) `bijzondere-mandaten` als perspectief-only op Gebeurtenissen (geen eigen record) — verliest categorisch overzicht; (b) als 5e item in `opdracht-types`-Σ — breekt assurance-niveau-as; (c) als sub-sectie van `gecertificeerd-accountant` in beroepsbeoefening — verliest opdracht-categorie-status | User-observatie 2026-05-26: "zit dat niet dicht bij onze discipline `controle` ook?" + "moet het geen perspectief worden op de betrokken gebeurtenissen?" — beide raken precies. Bijzondere mandaten zijn opdracht-categorie (= record naast andere sub-Kaders van controle) ÉN concrete uitvoering bij elke Gebeurtenis (= perspectief). Drie-niveau-toepassing van perspectief-vs-record-principe: categorisch begrip (record) + concrete uitvoering (perspectief) + wettelijke verankering (inhoud van Gebeurtenis). Shared thema beroepsbeoefening houdt monopolie-aspect zichtbaar zonder duplicatie. | Pattern: andere wettelijk-voorbehouden-opdracht-categorieën die door meerdere PO's heen leven kunnen analoog. Bv. `commissaris`-mandaat zelf is geen "bijzonder mandaat" maar wel een aparte opdracht-categorie — al deels in beroepsbeoefening voorzien (OP-BB.E).  |
