# Skeleton-overzicht — alle 19 programmaonderdelen (Wave 0 pre-extract)

**Datum**: 2026-05-21 03:42 UTC
**Bron**: `data/extractie/candidates.sqlite3` na 5 parallelle skeleton-batches (19 Opus-subagents)
**Totaal looptijd**: ~80 min wall-clock (alle batches sequentieel; agents binnen batch parallel)

---

## 1. Eindstats

| Metric | Waarde |
|---|---|
| Totaal kandidaten | **425** |
| Cross-PO (cross_po=1) | 177 (~42%) |
| Met embedding | 425 (100%) |
| Gerealiseerd | 0 |
| Openstaand | 425 |

### Per-kind verdeling

| Kind | Aantal | Aandeel |
|---|---|---|
| kader | 96 | 22.6% |
| procedure | 96 | 22.6% |
| begripscluster | 67 | 15.8% |
| regime | 51 | 12.0% |
| fiscale-regeling | 30 | 7.1% |
| instrument | 25 | 5.9% |
| operatie | 19 | 4.5% |
| ratio | 16 | 3.8% |
| familie | 15 | 3.5% |
| balanspost | 10 | 2.4% |

**Opmerking**: `fiscale-regeling` is een nieuwe kind die niet in de oorspronkelijke ADR-025-set zat. Agents (2.2, 2.3, 2.6, 2.8) hebben 'm spontaan toegevoegd voor regelingen die te specifiek zijn voor "regime" en te conceptueel voor "procedure" (DBI-aftrek, VVPRbis, innovatie-aftrek, schenking-met-voorbehoud-vruchtgebruik, etc.). Conform "open tag-set"-regel uit ADR-025 (§Kind als open tag-set).

### Per primary_po

| PO | # | Onderwerp |
|---|---|---|
| 1.1 | 40 | Algemene boekhouding |
| 1.2 | 14 | Boekhoudrecht en jaarrekeningenrecht |
| 1.3 | 24 | Analyse en kritische beoordeling van de jaarrekening |
| 1.4 | 25 | Geconsolideerde jaarrekening |
| 1.5 | 12 | EU + internationale boekhoudkundige normen |
| 1.6 | 32 | Externe controle |
| 1.7 | 26 | Interne controle |
| 1.8 | 13 | Analytische boekhouding |
| 1.9 | 5 | Financiële analyse + financieel bedrijfsbeheer |
| 2.1 | 9 | Algemene beginselen fiscaal recht |
| 2.2 | 31 | Personenbelasting |
| 2.3 | 30 | Vennootschapsbelasting |
| 2.4 | 33 | BTW |
| 2.5 | 16 | Fiscale procedure |
| 2.6 | 25 | Registratie- en successierechten |
| 2.7 | 17 | Regionale en lokale belastingen |
| 2.8 | 27 | Europees en internationaal fiscaal recht |
| 3.0 | 31 | Vennootschaps- en verenigingsrecht + insolventie |
| 4.0 | 14 | Deontologie + antiwitwas |
| 1.0 | 1 | (cross-PO surfaced — `deontologie-accountant`) |

---

## 2. Top-15 cross-PO kandidaten

Gerangschikt op breedte van anchor-spreiding (aantal verschillende PO-prefixes in `linked_anchors`). Reden voor deze proxy: `voorgesteld_door_pos` werd in de praktijk vaak niet ge-extend door `aanvul_kandidaat`-calls (zie §6 bugs). Anchor-spreiding is de eerlijkste maat voor cross-PO-relevantie.

| Rang | Fiche | Kind | Primary | Anchor-PO's |
|---|---|---|---|---|
| 1 | `jaarrekening` | kader | 1.1 | 1.1, 1.2, 1.5, 1.9, 3.0 |
| 2 | `continuiteit-going-concern` | kader | 1.4 | 1.3, 1.6, 1.9 |
| 3 | `exit-planning-vennootschap` | kader | 2.3 | 2.3, 2.8, 3.0 |
| 4 | `fiscale-beginselen` | kader | 2.1 | 2.1, 2.3, 2.5 |
| 5 | `fusie` | operatie | 1.1 | 1.1, 2.3, 3.0 |
| 6 | `geconsolideerde-jaarrekening-bgaap` | kader | 1.4 | 1.2, 1.4, 1.5 |
| 7 | `groottecategorie-vennootschap` | begripscluster | 1.2 | 1.2, 2.3, 3.0 |
| 8 | `inbreng-van-bedrijfstak-of-algemeenheid` | operatie | 1.1 | 1.1, 2.4, 3.0 |
| 9 | `inkoop-eigen-aandelen` | operatie | 1.1 | 1.1, 2.3, 3.0 |
| 10 | `keuze-rechtsvorm-fiscaal` | kader | 2.3 | 2.3, 2.8, 3.0 |
| 11 | `ontbinding-en-vereffening` | operatie | 1.1 | 1.1, 2.3, 3.0 |
| 12 | `splitsing` | operatie | 1.1 | 1.1, 2.3, 3.0 |
| 13 | `uitkering-aan-aandeelhouders` | operatie | 1.1 | 1.1, 2.3, 3.0 |
| 14 | `auditrisicomodel-kader` | kader | 1.6 | 1.6, 1.7 |
| 15 | `audit-groepsrekening-isa-600` | procedure | 1.4 | 1.4, 1.6 |

**Inzicht**: vennootschapsrechtelijke operaties (fusie, splitsing, inbreng, inkoop, ontbinding) zijn structureel cross-PO-1.1↔2.3↔3.0. Cross-PO-completeness binnen die fiches moet rol-perspectief boekhouder + fiscaal + jurist gelijktijdig behandelen.

---

## 3. Kaders per PO (96 totaal)

Kaders zijn de "top-down anchors" — vertrek-punt voor wave-volgorde.

| PO | Kaders |
|---|---|
| 1.1 | boekhoudbeginselen · dubbele-boekhouding · jaarrekening · vaste-activa-kader |
| 1.2 | boekhoudrechtelijk-kader |
| 1.3 | jaarrekeninganalyse · kasstroom-analyse · jaarverslag · niet-in-balans-rechten-en-verplichtingen · doelstellingen-financiele-analyse · instrumenten-financiele-analyse |
| 1.4 | geconsolideerde-jaarrekening-bgaap · ifrs-consolidatieraamwerk · continuiteit-going-concern |
| 1.5 | eu-jaarrekeningenrichtlijn · ifrs-verordening · ifrs-conceptueel-raamwerk · ias-1-presentatie · be-gaap-vs-ifrs-verschillen · ias-16/38/2 (3 stuks) · ifrs-16-leases · ifrs-15-opbrengsten |
| 1.6 | controleopdracht-cyclus · auditrisicomodel · aansprakelijkheid-accountant-revisor · onafhankelijkheid-en-deontologie · auditrisicomodel-kader · kwaliteitsmanagement-opdracht · professionele-oordeelsvorming-en-skepticism |
| 1.7 | interne-controle-coso-kader · cyclus-analyse-kader · referentiestelsels-ic-kader · bijzondere-verslagen-accountant |
| 1.8 | analytische-boekhouding · budgetbeheer |
| 1.9 | faillissementspredictie-modellen |
| 2.1 | fiscaal-rechtelijk-kader · fiscale-beginselen · interpretatie-fiscale-wet |
| 2.2 | personenbelasting-kader · beroepskosten-regime-pb · voordelen-alle-aard · federale/gewestelijke-belastingverminderingen-pb |
| 2.3 | vennootschapsbelasting-kader · aftrekbare-beroepskosten-venb · fiscale-procedure-belastingplichtige · keuze-rechtsvorm-fiscaal · exit-planning-vennootschap · boekhoudkundig-fiscaal-attachment |
| 2.4 | btw-stelsel · plaats-van-handeling-btw · btw-aftrek · factuur-btw · btw-vastgoed · btw-grensoverschrijdend · douaneprocedures-btw-invoer |
| 2.5 | taxatieprocedure-kader · beginselen-behoorlijk-bestuur-fiscaal · aanslagtermijnen-fiscaal · aangifteplicht-fiscaal · fiscale-bewijsmiddelen |
| 2.6 | registratiebelasting-kader · erfbelasting-kader · gewest-fiscaliteit-registratie-en-successie · huwelijksvermogensrecht-kader · erfrecht-kader · successieplanning-kader |
| 2.7 | gewestelijke-en-lokale-fiscaliteit-kader · gewestelijke-fiscale-autonomie · lokale-fiscale-autonomie |
| 2.8 | internationaal-fiscaal-kader · belasting-niet-inwoners · atad-richtlijn · beps-actieplan · transfer-pricing · internationale-tewerkstelling · roerend-inkomen-internationaal · internationale-structurering-vennootschap |
| 3.0 | vennootschapsrechtelijk-kader-wvv · bestuur-vennootschap-kader · algemene-vergadering · kapitaalbescherming-en-winstverdeling · aansprakelijkheid-oprichters-bestuurders · aandeelhoudersovereenkomst · vennootschapsgeschillen-kader · overnameovereenkomst-spa-kader · insolventierecht-wer-boek-xx-kader |
| 4.0 | beroepsgeheim-accountant · onafhankelijkheid-accountant · risicogebaseerde-benadering-aww · communicatie-met-stakeholders · kantoor-organisatie-accountant |
| 1.0 | deontologie-accountant (cross-PO surfaced) |

---

## 4. Families + hun leden

Families ⇒ wave-volgorde-implicatie: schrijf de familie-fiche **gelijktijdig** met haar leden (om vergelijkingsmatrix consistent te krijgen).

| Familie | Primary | Leden |
|---|---|---|
| `consolidatiemethoden` | 1.4 | integrale-, evenredige-consolidatie · vermogensmutatiemethode |
| `leasing` | 1.1 | (leden nog niet ge-edged — zie §6 bug) |
| `opsplitsing-eigendom` | 1.1 | (idem) |
| `kostprijsmethoden` | 1.8 | full-/direct-costing · standaardkosten · abc-methode |
| `controlemaatregelen-familie` | 1.7 | (preventief/detectief/correctief — te edgen) |
| `assurance-opdracht-types` | 1.6 | wettelijke-controle · contractuele-controle · ISRE-beoordeling · ISAE-assurance · ISRS-4400 · compilatie |
| `bijzondere-verslagen-vennootschapsverrichtingen` | 1.6 | inbreng-natura · quasi-inbreng · fusie-splitsing · omzetting · ontbinding-vereffening · effecten · kapitaalvermindering |
| `inkomstencategorieen-pb-familie` | 2.2 | onroerend · roerend · beroeps · diverse-inkomsten-pb |
| `verworpen-uitgaven` | 2.3 | autokosten · geheime-commissielonen |
| `bijzondere-aanslagen-venb` | 2.3 | geheime-commissielonen · liquidatiereserve |
| `fiscale-sancties` | 2.5 | (te edgen — administratieve boete · belastingverhoging · strafrechtelijk) |
| `gemeentebelastingen-sui-generis` | 2.7 | (te edgen) |
| `oeso-modelverdrag-familie` | 2.8 | dubbelbelastingverdrag · vaste-inrichting · tie-breaker-woonplaats · 5× toewijzingsregels · MAP-procedure · MLI-instrument |
| `rechtsvormen-belgie` | 3.0 | bv · nv · cv · vof-commv · maatschap · vzw |
| `eu-fiscale-richtlijnen-familie` | 2.8 | moeder-dochter · interest-royalty · fiscale-fusie · ATAD · DAC-uitwisseling |

---

## 5. Dependency-graph (top-10 diepste)

Fiches met meeste `depends_on_fiches` (= laatste in wave-volgorde):

| # deps | Fiche | Kind | Primary | Hangt af van |
|---|---|---|---|---|
| 5 | `roerend-inkomen-internationaal` | kader | 2.8 | dbi-aftrek · DBV · moeder-dochter · interest-royalty · FBB |
| 5 | `internationale-structurering-vennootschap` | kader | 2.8 | vaste-inrichting · moeder-dochter · dbi-aftrek · exit-belasting · transfer-pricing |
| 4 | `resultaatverwerking` | procedure | 1.1 | eindejaarsverrichtingen · eigen-vermogen · uitkering · jaarrekening |
| 4 | `faillissementspredictie-modellen` | kader | 1.9 | jaarrekeninganalyse · solvabiliteit · interest-coverage · continuiteit |
| 4 | `cash-conversion-cycle` | ratio | 1.3 | jaarrekeninganalyse · 3× omloopsnelheden |
| 3 | `waarderingsregels-vastlegging` | procedure | 1.2 | boekhoudbeginselen · jaarrekening · jaarlijkse-inventaris |
| 3 | `uitkering-aan-aandeelhouders` | operatie | 1.1 | eigen-vermogen · oprichtingskosten · resultaatverwerking |
| 3 | `roerend-inkomen-pb` | regime | 2.2 | personenbelasting-kader · inkomstencategorieën-familie · roerende-voorheffing |
| 3 | `opmaak-geconsolideerde-jaarrekening` | procedure | 1.4 | geconsolideerde-jaarrekening-bgaap · integrale-consolidatie · eliminatie-intercompany |
| 3 | `ontbinding-en-vereffening` | operatie | 1.1 | jaarrekening · eigen-vermogen · uitkering |

**252/425 fiches hebben minstens 1 dependency** (59%).

---

## 6. Voorgestelde wave-volgorde

### Wave 0 (foundation kaders — 30 fiches zonder dependencies)

| PO | Kader |
|---|---|
| 1.0 | deontologie-accountant |
| 1.1 | boekhoudbeginselen · dubbele-boekhouding |
| 1.2 | boekhoudrechtelijk-kader |
| 1.6 | aansprakelijkheid- · auditrisicomodel-kader · controleopdracht-cyclus · onafhankelijkheid- |
| 1.7 | referentiestelsels-ic-kader |
| 1.8 | analytische-boekhouding |
| 2.1 | fiscaal-rechtelijk-kader · fiscale-beginselen · interpretatie-fiscale-wet |
| 2.2 | personenbelasting-kader |
| 2.5 | aanslagtermijnen-fiscaal · beginselen-behoorlijk-bestuur · fiscale-bewijsmiddelen |
| 2.6 | erfbelasting-/registratiebelasting-/successieplanning-/erfrecht-/huwelijksvermogensrecht-/gewest-fisc-kader |
| 2.7 | 3 autonomie-kaders |
| 2.8 | internationaal-fiscaal-kader |
| 3.0 | vennootschapsrechtelijk-kader-wvv |
| 4.0 | communicatie-met-stakeholders · kantoor-organisatie-accountant |

### Wave 1 — domein-kaders die afhangen van Wave 0

`jaarrekening` (depends_on geen, maar inherent boven boekhoudbeginselen) · `vaste-activa-kader` · vennootschapsbelasting-kader · btw-stelsel · etc.

### Wave 2 — families (na hun kader)

`rechtsvormen-belgie` · `consolidatiemethoden` · `inkomstencategorieen-pb-familie` · `oeso-modelverdrag-familie` · ...

### Wave 3 — instances & operaties

Alle instrument/operatie/balanspost/ratio die familie + kader nodig hebben.

### Wave 4 — diepe regimes & procedures

`roerend-inkomen-internationaal` · `internationale-structurering-vennootschap` · `cash-conversion-cycle` · `faillissementspredictie-modellen`.

**Aanbeveling**: Wave 0 in één bulk (30 fiches × ~6 agents = 5 fiches/agent), maar **Wave 0a-pilot** eerst om EXTRACT v5 te valideren.

---

## 7. Pilot Wave 0a-selectie — 6 fiches

| # | Fiche | Kind | Primary | Reden |
|---|---|---|---|---|
| 1 | `obligatielening` | instrument | 1.1 | Canonical mockup `obligatielening-v7.md` — referentie-baseline |
| 2 | `solvabiliteitsratio` | ratio | 1.3 | Mockup `solvabiliteitsratio-v2.md` — drempels conceptueel + acties per rol |
| 3 | `inkoop-eigen-aandelen` | operatie | 1.1 | Mockup `inkoop-eigen-aandelen-nv-v1.md` — wettelijke voorwaarden + procedure (note: kandidaat is rechtsvormneutraal, mockup is NV-specifiek — test pair-trap-aanpak) |
| 4 | `jaarrekening` | kader | 1.1 | Mockup `jaarrekening-v1.md` + cross-PO #1 — test kader-with-cyclus-inside |
| 5 | `oprichtingskosten` | balanspost | 1.1 | Mockup `oprichtingskosten-v1.md` — balanspost-skelet (MAR/componenten/waardering/afschr/toelichting) |
| 6 | `dbi-aftrek` | fiscale-regeling | 2.3 | **Gap-stress-test** — geen mockup, geen v1-seed, nieuwe kind `fiscale-regeling`, cross-PO met 2.8 (BEPS/moeder-dochter). Test of agent zonder mockup-leidraad een kwaliteits-fiche kan bouwen vanuit alleen schema 2.0 + bronnen + skeleton-kandidaat-context. |

### Toewijzing aan 3 parallelle Opus-subagents (2 fiches per agent)

| Agent | Fiches |
|---|---|
| A | obligatielening · oprichtingskosten (beide 1.1 — boekhoud-context bundelen) |
| B | solvabiliteitsratio · jaarrekening (1.3 + 1.1 kader-context) |
| C | inkoop-eigen-aandelen · dbi-aftrek (1.1 operatie + 2.3 fiscale-regeling — stress-test variatie) |

---

## 8. Bekende issues vóór Wave 0a

### MCP-server bugs

| Bug | Impact | Workaround |
|---|---|---|
| `aanvul_kandidaat(veld='edge', waarde={...})` blokkeert met schema-error | Edges op bestaande kandidaten kunnen niet via MCP worden toegevoegd; alleen via initiële `voorstel_kandidaat`-call | Agents documenteerden gewenste edges in rapport (sectie "open punten"). Spawn-task aangemaakt door PO 1.5-subagent. |
| `voorgesteld_door_pos` wordt niet ge-extend bij `aanvul_kandidaat` | Cross-PO-ranking via dit veld onderschat realiteit; alleen 1 PO per fiche zichtbaar | Anchor-PO-breedte als proxy gebruikt (zie §2) |
| `aanvul_kandidaat` op v1-records (geen kandidaten) faalt stilzwijgend | Bij `kleine-vennootschap` (v1-record, geen 2.0-kandidaat) gemerkt door PO 2.3-agent | Niet kritisch — actiepunt voor extract-agent bij realisatie |

### Worktree-issue

PO 1.6 ran in een Claude-Code worktree (`.claude/worktrees/agent-a46ef98c834e241d5/`). Rapport stond daar; gekopieerd naar main. Toekomst: pin sub-agents aan main-cwd of accept worktree-routing en kopieer automatisch.

### Open vragen (samengevoegd uit alle 19 rapporten — niet uitputtend)

Veel agents formuleerden open vragen voor mens-review. Belangrijkste cross-cutting thema's:

- **Granulariteit kaders**: één breed kader vs uitsplitsen (bv. `boekhoudrechtelijk-kader` één-fiche of opsplitsen autoriteiten/bronnen/regels?)
- **Familie vs kader**: edge cases zoals leasing-familie in lange-termijn-financiering-kader (PO 1.1) en `auditrisicomodel(-kader)` dubbel in PO 1.6+1.7
- **Primary_po-shifts**: bv. `wettelijke-controle-jaarrekening` (nu 1.2, mogelijk → 1.6); `onroerende-voorheffing` (nu 2.2, mogelijk → 2.7); `fiscale-procedure-belastingplichtige` (nu 2.3, mogelijk → 2.1)
- **Gewestelijke-fiscaliteit-anti-pair-trap**: drie gewesten als één-fiche-met-vergelijkingsmatrix consistent toegepast in PO 2.6/2.7
- **Nieuwe kind `fiscale-regeling`**: 30 fiches gebruiken het; ADR-025 zegt "open tag-set" — bevestiging gewenst dat we 'm officieel adopteren
- **2.x rol-perspectieven**: PO 2.1-agent suggereerde dat rol-set voor fiscale PO's moet uitbreiden (`adviseur-fiscaal` · `vertegenwoordiger` · `compliance-medewerker` i.p.v. boekhouder/auditor-triade van 1.x)

---

## 9. Wat dit overzicht NIET dekt

- **Volledig dependency-grafiek** (visueel): 252 edges over 425 nodes — render-tool nog te bouwen
- **TDK-dekking globaal**: agents melden 100% dekking per PO, maar nog geen globale audit dat élke unieke TDK uit `programma.json` wordt geraakt door minstens één fiche
- **Cijferzakboekje-koppeling**: PO 2.3-agent identificeerde 5 tarief-records die naar Cijferzakboekje moeten linken — wacht op user-bronnenwerk
- **VERIFY-pass**: nog niet gedraaid — komt na Wave 0a-extract

---

## 10. Volgende stappen

1. **Mens-review** (deze sessie): user beoordeelt §7 pilot-selectie en §8 open vragen
2. **Archief v1.x** voor pilot-fiches: `python3 -m tools.extractie.archive_voor_migratie --anchor-prefix 1.1` (én 1.3 én 2.3 voor de pilot)
3. **Fase 3 — pilot Wave 0a**: 3 parallelle Opus-subagents met EXTRACT v5
4. **Fase 4 — STOP**: pilot-rapport met kwaliteitsanalyse vóór bulk-extract over rest
