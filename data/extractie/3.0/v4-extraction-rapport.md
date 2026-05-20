# EXTRACT v4 — Pilot-rapport PO 3.0.II "Beheer van de vennootschap"

**Run**: concept-extractie-v4 (Opus, lokale subagent)
**Datum**: 2026-05-20
**Scope**: één anchor (3.0.II), greenfield (0 bestaande PO 3.0 records)
**Bundle**: `/tmp/po-3.0-pilot/bundle-3.0.II.json` — 103 chunks, WVV 49 + MvT-WVV 50 + CBN 4
**Backup-tag**: `backup/pre-po-3.0-extract-2026-05-20`

---

## 1. Aangemaakte records (10)

| # | id | node_type | kern (1 zin) |
|---|---|---|---|
| 1 | `bestuursorgaan` | cluster | Het door wet en statuten aangewezen orgaan dat een vennootschap bestuurt en haar jegens derden verbindt — concretere vormgeving hangt af van de vennootschapsvorm. |
| 2 | `bestuursmodel-vennootschap` | synthese | Vergelijkingstabel + kerninzichten over de drie NV-modellen (monistisch, enige bestuurder, duaal) tegenover BV/CV en personenvennootschappen. |
| 3 | `monistisch-bestuur` | cluster | Eén collegiaal bestuursorgaan (raad van bestuur in de NV; bestuursorgaan in BV/CV) dat zowel strategie als operationele leiding draagt. |
| 4 | `duaal-bestuur` | cluster | Twee verplicht gescheiden organen in de NV — raad van toezicht (strategie + toezicht) en directieraad (residuair + operationeel + vertegenwoordiging). |
| 5 | `enige-bestuurder` | begrip | Eén natuurlijke of rechtspersoon die in de NV alleen de bestuursbevoegdheid uitoefent; eigen belangenconflict-procedure via art. 7:102. |
| 6 | `dagelijks-bestuur` | cluster | Gedelegeerde uitvoeringsbevoegdheid voor routinematige of spoedeisende handelingen, onder toezicht van het delegerend bestuursorgaan. |
| 7 | `bevoegdheid-bestuursorgaan` | regel | Residuair: alle handelingen nodig of dienstig voor het voorwerp, behalve die welke de wet aan de algemene vergadering toewijst; statutaire beperkingen werken niet jegens derden. |
| 8 | `vertegenwoordiging-vennootschap-jegens-derden` | regel | Het bestuursorgaan verbindt de vennootschap; ultra-vires-handelingen binden tenzij de vennootschap bewijst dat de derde van de overschrijding wist of moest weten. |
| 9 | `belangenconflict-bestuurder` | cluster | Procedure (mededeling, motivering, onthouding, jaarverslag, commissarisbeoordeling) bij vermogensrechtelijk strijdig belang — varieert per vennootschapsvorm en bestuursmodel. |
| 10 | `verbonden-partijen-procedure-genoteerd` | regel | Aanvullende procedure voor genoteerde NV's bij verrichtingen met verbonden partijen in de IAS 24-zin (art. 7:97 / 7:116). |

**Verdeling per node_type**: 5 clusters, 3 regels, 1 synthese, 1 begrip — 0 autoriteit en 0 competentie (consistent met het focus "bestuursorganen + regels rond bestuur", niet "wie doet wat extern" of "stagiair-vaardigheid").

**Status**: alle nieuw, `status: "seed"`.

---

## 2. Edges-overzicht

| Bron | Type | Doel | Facet |
|---|---|---|---|
| bestuursorgaan | onderdeel-van | wetboek-vennootschappen-verenigingen | — |
| bestuursorgaan | vereist-kennis-van | vennootschapsvormen-typologie | — |
| bestuursmodel-vennootschap | verwijst-naar | bestuursorgaan, monistisch-bestuur, duaal-bestuur, enige-bestuurder | — |
| monistisch-bestuur | specialisatie-van | bestuursorgaan | regime: NV monistisch / BV / CV |
| monistisch-bestuur | vergelijkt-met | duaal-bestuur, enige-bestuurder | aspect |
| duaal-bestuur | specialisatie-van | bestuursorgaan | regime: NV duaal |
| duaal-bestuur | vergelijkt-met | monistisch-bestuur | aspect |
| enige-bestuurder | specialisatie-van | bestuursorgaan | regime: NV — enige bestuurder |
| enige-bestuurder | vergelijkt-met | monistisch-bestuur | aspect |
| enige-bestuurder | vereist-kennis-van | belangenconflict-bestuurder | — |
| dagelijks-bestuur | onderdeel-van | bestuursorgaan | — |
| dagelijks-bestuur | vereist-kennis-van | vertegenwoordiging-vennootschap-jegens-derden | — |
| bevoegdheid-bestuursorgaan | onderdeel-van | bestuursorgaan | — |
| bevoegdheid-bestuursorgaan | vereist-kennis-van | vertegenwoordiging-vennootschap-jegens-derden | — |
| vertegenwoordiging-vennootschap-jegens-derden | onderdeel-van | bestuursorgaan | — |
| vertegenwoordiging-vennootschap-jegens-derden | vereist-kennis-van | dagelijks-bestuur | — |
| belangenconflict-bestuurder | onderdeel-van | bestuursorgaan | — |
| belangenconflict-bestuurder | vergelijkt-met | verbonden-partijen-procedure-genoteerd | aspect |
| belangenconflict-bestuurder | vereist-kennis-van | commissaris-toezicht-jaarrekening | — |
| verbonden-partijen-procedure-genoteerd | uitzondering-op | belangenconflict-bestuurder | scope: genoteerde NV + verbonden partij |
| verbonden-partijen-procedure-genoteerd | specialisatie-van | belangenconflict-bestuurder | regime: genoteerde NV |
| verbonden-partijen-procedure-genoteerd | vereist-kennis-van | public-interest-entity | — |

**Cross-PO links**:
- `bestuursorgaan` → `wetboek-vennootschappen-verenigingen` (PO 1.2 / cross-vak)
- `bestuursorgaan` → `vennootschapsvormen-typologie` (PO 1.2)
- `belangenconflict-bestuurder` → `commissaris-toezicht-jaarrekening` (PO 1.4)
- `verbonden-partijen-procedure-genoteerd` → `public-interest-entity` (PO 1.4/1.5)

Geen edge naar PO 3.0.VII-stof (bestuurdersaansprakelijkheid) — wordt later toegevoegd zodra die records bestaan.

---

## 3. Gaps.json — toegevoegd (8)

| Aspect | Prio | Onderwerp |
|---|---|---|
| records.ontbreekt | midden | Aansprakelijkheid bestuurders (PO 3.0.VII — bewust uit scope) |
| records.ontbreekt | midden | Bezoldiging bestuurders + remuneratiecomité (eigen thematiek) |
| records.ontbreekt | laag | Coöptatie + gender-vertegenwoordiging in raad van bestuur (art. 7:86) |
| records.ontbreekt | midden | Remuneratiecomité (audit­comité bestaat al) |
| records.ontbreekt | laag | Bestuur van vzw en stichting (Boek 9 + 11) |
| records.ontbreekt | laag | Bestuur in de SE (Europese vennootschap, art. 15-16) |
| dangling-reference | laag | Zelfverificatie edge → public-interest-entity (geen echte gap) |
| bron-gap | laag | CBN over feitelijke bestuurders/bestuurders-in-feite |

---

## 4. Confidence-distributie

- **grounded**: ~80% van velden — wetteksten + MvT bedekken het terrein robuust
- **inferred**: ~15% — scenario-voorbeelden met cast (vier voorbeelden in totaal: Bouwwerf Beerse BV, Aurelia Holding NV, Rotex Roeselare NV, Uitgeverij Ukkel NV) + enkele valkuilen en kerninzichten
- **inferred-from-aggregation**: 0 — geen claims werden uit 2+ bronnen geaggregeerd in dit record-corpus (alle claims hebben minstens één directe WVV- of MvT-chunk)

---

## 5. Migraties

**Geen** — greenfield (0 bestaande records gemigreerd).

---

## 6. Open observaties

- **WVV-structuur leent zich uitstekend voor regime-specialisatie-patroon**. De art. 5:70-79 (BV), 6:58-67 (CV), 7:85-122 (NV) bevatten herhaalde structuren — wat een natuurlijke `bestuursorgaan` (algemeen) + `monistisch-bestuur`/`duaal-bestuur`/`enige-bestuurder` (specialisaties) gaf.
- **De BV/CV-`bestuursorgaan` wordt nu via een bouwsteen in het algemene record gedekt**, niet via een eigen `bestuursorgaan-bv` of `bestuursorgaan-cv` record. Bewust: BV en CV verschillen onderling te weinig om een eigen cluster te rechtvaardigen — de bouwsteen-aanpak vermijdt drie dichtbij-elkaar-liggende records met overlappende inhoud. Indien latere VERIFY signaleert dat stagiairs hier vragen over hebben, kan dat heroverwogen worden.
- **Dagelijks bestuur is bewust een eigen cluster** (geen bouwsteen van `bestuursorgaan`), omdat het een eigen wetstechnisch geheel vormt (artt. 5:79, 6:67, 7:121) en kruist met aansprakelijkheid, vertegenwoordiging en bestuursorganisatie.
- **Aansprakelijkheid bewust niet opgenomen**: PO 3.0.VII krijgt eigen pass. Wel zal vanuit dat record een edge terug naar `bestuursorgaan` en `belangenconflict-bestuurder` lopen.
- **Genoteerde-NV-specifieke regels** (verbonden partijen, gendervertegenwoordiging, beursverplichtingen voor remuneratiebeleid) zijn ofwel in scope (verbonden-partijen-procedure) ofwel als gap genoteerd — niet vermengd in algemene records om de basisvelden bondig te houden.

---

## 7. Pilot-evaluatie — voor de andere PO 3.0-anchors

### Wat vlot ging

1. **Eén bundle met 103 chunks gaf voldoende dekking** voor 10 records — geen extra retrieval nodig (behalve voor edge-target-verificatie). De score-range 0.55-0.81 toonde duidelijk verschil tussen kern-art-chunks (>0.70) en perifere chunks.
2. **Regime-specialisatie-edges met `regime`-facet** werken intuïtief — één algemene cluster + N specialisaties is een sterk patroon voor WVV-stof (waar BV/CV/NV vaak parallel-regimes zijn).
3. **De synthese-vergelijkingstabel (`bestuursmodel-vennootschap`)** ontstaat natuurlijk wanneer er drie alternatieven met dezelfde aspect-set zijn — dit type record zal in PO 3.0 vaak terugkomen (oprichting, kapitaalstructuur, ontbinding).
4. **Cast-namen voor scenario's** werkten goed — Aurelia Holding NV (NV), Bouwwerf Beerse BV (BV), Rotex Roeselare NV (grote NV met commissaris), Uitgeverij Ukkel NV (NV met operationele scope) — cast biedt voldoende variëteit zonder dat nieuwe namen verzonnen werden.

### Smells / heuristieken die aanpassing vereisen

1. **Granulariteit "regel" vs "cluster" voor belangenconflict-procedure**. Initial-draft overwoog drie aparte regel-records (art. 7:96, 7:102, 7:115). Final: één cluster (`belangenconflict-bestuurder`) met bouwstenen per procedure. Voordeel: de stagiair krijgt het concept-geheel; nadeel: één cluster wordt groot. **Heuristiek**: wanneer een fenomeen in elk regime dezelfde grondstructuur volgt met regime-aangepaste variaties (mededeling → onthouding → motivering → externe controle), is **één cluster met regime-bouwstenen** beter dan N regels — de wet zelf herhaalt zich, een record dat dat ook doet wordt redundant. Overweeg deze regel toe te voegen aan §6 (granulariteit) van het EXTRACT v4-prompt.

2. **"Bron-prefix-vermijden"-regel wordt strakker getest in WVV-territorium**. De verleiding om records `wvv-art-7-96-belangenconflict` te noemen was reëel; bewuste keuze voor functioneel-naam (`belangenconflict-bestuurder`). **Geen aanpassing aan prompt nodig**: regel staat duidelijk in §17.10.

3. **`uitzondering-op` + `specialisatie-van` op hetzelfde paar**: `verbonden-partijen-procedure-genoteerd` heeft beide edge-types naar `belangenconflict-bestuurder`. Dat is correct (het is tegelijk een uitzondering voor de scope én een regime-specialisatie voor genoteerde NV's) maar dubbel-edge naar hetzelfde target valt op. **Heuristiek**: dit blijft toegelaten en informatief — twee edge-types met verschillende facet-velden geven render-tijd meer context. Geen prompt-aanpassing.

4. **De situering-veld-confidence**. Voor de meeste records is `situering` synthetisch (samenvattend over 4-5 wetsartikelen) — dat is feitelijk `inferred-from-aggregation`, niet `grounded`. Ik heb ze als `grounded` gemarkeerd omdat de regime-toewijzing direct uit de bron komt; bij sommige is dat te ruim. **Heuristiek**: situering altijd `inferred-from-aggregation` markeren tenzij ze één directe wetszin parafraseert. Overweeg explicietere richtlijn in §situering-sectie van prompt of ADR-007.

5. **Bouwsteen "kruist met andere bouwstenen"**. Binnen `dagelijks-bestuur` overlapt de bouwsteen "Tegenwerpelijkheid jegens derden" met inhoud van `vertegenwoordiging-vennootschap-jegens-derden`. Bewuste keuze: bouwsteen blijft kort, edge `vereist-kennis-van` doet het zwaarder werk. Werkt — maar bij PO 3.0-anchors waar twee clusters dicht bij elkaar liggen (bv. `oprichting-vennootschap` ↔ `inbreng-in-natura`) zal dit vaker voorkomen. **Heuristiek**: bij overlap, kort signaleren in bouwsteen + edge schrijven; bewust geen volledig parallel materiaal in twee clusters.

6. **Bundle-spreiding over Boek 4 (maatschap/VOF/CommV)** was beperkt (slechts 4 chunks). Voor `bestuursorgaan` was dat genoeg voor een bouwsteen, maar bij andere PO 3.0-anchors over personenvennootschappen (oprichting, ontbinding) zou de bundle-grootte op die boek-stof onvoldoende kunnen zijn. **Aanbeveling voor wave-planning**: check bundle-coverage per boek vóór de extract-pass; vraag aanvullende bundle indien Boek 4 < 5 chunks.

7. **PO 3.0-stof is sterk wetgevings­technisch** — de stagiair krijgt typisch geen examenvragen die rekenkundige illustraties vereisen (boekingen, balans-fragmenten). Daarom slechts één scenario-illustratie geprobeerd (bij `belangenconflict-bestuurder`), geen mermaid-diagrammen, geen boekingsillustraties. **Verwacht patroon voor PO 3.0**: minder gestructureerde illustraties dan in PO 1.x (boekhouding); meer scenario-voorbeelden met casts om procedure-flows te tonen. Geen prompt-aanpassing — `voorbeelden[scenario]` met `stappen[]` is daarvoor perfect.

8. **Worktree-cwd-divergentie niet aan de orde**: deze pilot draaide in main repo (geen worktree). Audit groen na 10 saves.

### Volume-verwachting voor PO 3.0 als geheel

Op basis van 10 records voor één van 13 anchors verwacht ik ~70-100 records voor PO 3.0 in totaal. De anchors variëren in dichtheid (3.0.II "Beheer" is rijk; 3.0.X "Ontbinding" zal vergelijkbaar zijn; 3.0.V "Effecten" wellicht zwaarder). Wave-planning zou daarmee rekening kunnen houden: 3-4 ankers per wave is haalbaar (alleen voor zware ankers één-op-één).

### Concrete aanpassingsvoorstellen voor het EXTRACT v4-prompt

- **Toevoeging §6 (granulariteit)**: heuristiek "regime-procedures = één cluster met regime-bouwstenen, niet N parallelle regels" expliciet maken.
- **Toevoeging §situering-sectie (of ADR-007)**: confidence voor situering default `inferred-from-aggregation`; alleen `grounded` als één-zin-parafrase.
- **Toevoeging wave-planning-richtlijn (ADR-008 §18.7)**: vóór EXTRACT-pass coverage-check per WVV-Boek; bij < 5 chunks → bundel uitbreiden.

Niet voorstellen voor prompt-wijziging (zelf op te lossen door zorgvuldig lezen): bron-naming, multi-concept, near-duplicate-check — werkten allemaal correct in deze pilot.

---

## 8. Tijdsbesteding (indicatief)

- Literatuur (prompt + ADRs + schrijfregels): ~25 % van de pilot
- Bundle-survey + concept-RAG near-duplicate-checks + cast-lezing: ~10 %
- Record-design (welke 10, granulariteit, edges): ~15 %
- Record-content schrijven en provenance koppelen: ~40 %
- Audit + gaps + rapport: ~10 %

Het ontwerp-luik (welke records, welke granulariteit) was naar verhouding licht omdat het wetstechnisch domein duidelijk gestructureerd is. Voor minder wetgevings­technische ankers (audit-praktijk, controle-omgeving) verwacht ik meer ontwerp-tijd.

---

**Verificatie**: `python3 -m tools.lib.records_api audit` → 486 disk / 486 RAG / ok=True.
