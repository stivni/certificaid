# Leerpad-skelet PO 1.3 — Analyse en kritische beoordeling van de jaarrekening

**Status**: voorstel (2026-05-31). Sparring-document voor de bouw van het volledige leerpad-pakket (minicursus + leerstukken + samenvatting + oefening).
**Volgende stap**: na sparring → voorbeeldgroep-YAML + scripts per leerstuk + render per leerstuk.

---

## 1. Programma-analyse

### Officiële taken en doelstellingen

PO 1.3 heeft **één hoofdtaak** met **2 doelstellingen** (niveau: **integratie** — het hoogste cognitieve niveau in het programma):

> **Taak 1.3.1**: Analyse en beoordeling van de financiële situatie van een vennootschap of vereniging aan de hand van de jaarrekeningen, ratio's en kengetallen.

| Doel | Tekst (kort) | Anchor-rol |
|---|---|---|
| 1.3.1.1 | Kritisch lezen van een jaarrekening na verzamelen, selecteren, analyseren en samenvatten van informatie | context |
| 1.3.1.2 | Voorstellen formuleren om de situatie te verbeteren, waakzamer te zijn of te controleren | context |

**Cruciale observatie**: doel 1.3.1.2 is een **adviesverlenings-doelstelling** — het PO eindigt niet bij de analyse, maar bij **wat de accountant er aan aanbevelingen uit haalt**. Dit beïnvloedt de leerstuk-keuze: pure ratio-rekenwerk volstaat niet; er moet één leerstuk zijn waarin de student leert van getallen naar voorstellen te gaan.

### Kenniselementen-tree

Twee hoofdblokken (1.3.I + 1.3.II) met 21 sub-items in totaal:

- **1.3.I — DOELSTELLINGEN EN BASISINSTRUMENTEN**
  - 1.3.I.A — Doelstellingen (basis, specifiek, getrouw beeld, informatie)
  - 1.3.I.B — Betrokken partijen (stakeholders)
  - 1.3.I.C — Instrumenten en schema's
    - 1.3.I.C.1 — Wettelijke documenten (JR, beheersverslag, commissarisverslag, geconsolideerde rekeningen)
    - 1.3.I.C.2 — Andere documenten (ratio's, financieringstabel, boordtabel)
  - 1.3.I.D — Toezichtsorganen
    - 1.3.I.D.1 — Vennoten/aandeelhouders
    - 1.3.I.D.2 — Commissaris
    - 1.3.I.D.3 — Ondernemingsraad
    - 1.3.I.D.4 — Ondernemingsrechtbank/KOM
    - 1.3.I.D.5 — Financiële instanties (covenants)
  - 1.3.I.E — Verslag bestuursorgaan
- **1.3.II — ANALYSE EN KRITISCHE BEOORDELING JAARREKENING**
  - 1.3.II.A — Inleiding (boekhoudprincipes + waarderingsregels)
  - 1.3.II.B — Jaarrekening (Activa · Passiva · RR · Toelichting structuur)
  - 1.3.II.C — Analyse van de structuur: ratio's
    - 1.3.II.C.1 — Jaarrekening herwerking (analytische balans)
    - 1.3.II.C.2 — Netto-bedrijfskapitaal (functionele balans NBK · BBK · NT)
    - 1.3.II.C.3 — Vermogensstroomtabel
    - 1.3.II.C.4 — Operationele en financiële hefbomen
    - 1.3.II.C.5 — Falingspredictie / going concern
  - 1.3.II.D — Bijzondere informatie (niet-balans-rechten/verplichtingen)

### Kern vs rakend

- **Kern (eigen aan 1.3)**: 1.3.II — de analyse-techniek zelf (herwerking, NBK, ratio's, kasstroomtabel, hefbomen, falingspredictie). Plus 1.3.I.A-C (waarom + instrumenten).
- **Rakend met andere PO's**:
  - **1.3.I.D.2 Commissaris** → grondig in PO 1.6 (externe controle) en PO 3.0 (vennootschapsrecht). In 1.3 alleen "wat doet hij met ratio's?".
  - **1.3.I.D.3 Ondernemingsraad** → PO 3.0 (sociale wetgeving). In 1.3 alleen "welke financiële info krijgen werknemers?".
  - **1.3.I.D.4 KOM** → grondig in PO 1.9 (insolventie). In 1.3 alleen "welke signalen triggeren detectie?".
  - **1.3.I.D.5 Financiële instanties / covenants** → raakt PO 1.5 (financiering) of als sub-aspect bij solvabiliteit.
  - **1.3.II.A waarderingsregels** → PO 1.1 + 1.2.
  - **1.3.II.C.5 falingspredictie + alarmbel** → grondig in PO 1.9 (insolventie); in 1.3 als **trigger-instrument** binnen de diagnose.

---

## 2. Voorbeeldexamen-patronen

Uit `content/studiemateriaal/1-3/voorbeeldexamenvragen.md`: **13 unieke vraag-eenheden** uit 6 examens (2010-2, 2013-1, 2013-2, 2014-1, 2015-1, 2024-1).

| Onderwerp | Hoe vaak | Vraag-type | Centraal concept |
|---|---|---|---|
| Ratio's berekenen op samengevatte JR (NBK · current · zelffinanciering · ROE · OBR) | 3× cluster (2013-1, 2014-1, 2015-1) | Berekening met motivering van rubrieken, 2 decimalen | 4 ratio-families + NBK |
| Brutoverkoopmarge + nettorentabiliteit totaal activa + liquiditeit ruime zin | 1× (2013-2) | Berekening + motivering | rentabiliteit + liquiditeit |
| Begripsomschrijvingen: intrinsieke waarde · fractiewaarde · nettorend. bedrijfsactiva · algemene schuldgraad · operationele cashflow vóór belastingen | 1× (2015-1) | Definities | EV-componenten + ratio-formules |
| BBK — welke rubrieken meetellen? Ja/nee per balanscode | 1× (2015-1) | Selectievraag op 20 balansposten | activiteits-ratios + functionele balans |
| Nettothesaurie — definitie + positief saldo interpreteren | 1× (2014-1) | Begrip + interpretatie | functionele balans NT |
| Liquiditeit ruime/enge zin — verschil + interpretatie | 1× (2013-2) | Open vraag | liquiditeits-ratios |
| Ratio niet berekenbaar in verkort schema | 1× (2024-1) | Identificeren (omloopsnelheid klanten) | activiteit + schema-bewustzijn |
| Rangschikking passief (toenemende eisbaarheid) | 1× (2024-1) | Volgorde | JR-structuur |
| EV berekening verkort NBB-model kapitaalvennootschap | 1× (2024-1) | Formule | JR-structuur EV-rubrieken |
| Effect hogere afschrijving op brutoverkoopmarge (verlieslatend) | 1× (2024-1) | MC, geen effect | rentabiliteit + schema-positie |
| Stellingen financiële onafhankelijkheid | 1× (2024-1) | J/F | solvabiliteit |

**Patroon dat opvalt**:
1. **Formule + motivering van rubriek-codes** is de absolute kern (10+ vragen). Cijfers zelf hoef je niet uit het hoofd, maar wél welke rubrieken in welke formule horen.
2. **Schema-bewustzijn** (verkort vs volledig) is een terugkerende valkuil-vraag — wat ontbreekt of staat anders in het verkort schema?
3. **Begripsdefinities scherp** — intrinsieke waarde ≠ fractiewaarde ≠ beurswaarde; ROE ≠ ROCE; bruto ≠ netto in twee betekenissen (vóór belasting vs vóór niet-kaskosten).
4. **Functionele balans-drieluik** (NBK / BBK / NT) komt 2× expliciet op met selectie-vragen.
5. **Geen volledig uitgewerkte diagnoses gevraagd** — de examen-vragen toetsen fragmenten van het pad, niet de hele synthese. De oefening moet dat hele pad wél laten doorlopen.

**Doctrine-bron in modelantwoorden**: KB-WVV art. 3:89 e.v. (balansschema), MAR (KB 21.10.2018), CBN-advies 2011/14 (rentabiliteit totaal activa) en 2017/08 (verkort schema), Ooghe & Van Wymeersch (functionele balansanalyse), NBB-balanscentrale.

---

## 3. Leerstuk-voorstel

**Granulariteits-stelregel toegepast**: eerder samen dan splitsen. Voorstel: **5 leerstukken**, geen aparte fiche voor "toezichtsorganen" (1.3.I.D) want die organen leven grondig in 1.6 / 1.9 / 3.0 — in 1.3 alleen kort vermelden in §1 van de minicursus + in §1 van het entry-leerstuk.

### Leerstuk 1 — `wat-is-jaarrekeninganalyse` (entry)

- **Vraag**: Wat is jaarrekeninganalyse, voor wie, met welke instrumenten, en waarom doet de accountant dit?
- **Type**: entry-fiche (kort, doorklik-zwaar)
- **Gedekte kenniselementen**: 1.3.I.A · 1.3.I.B · 1.3.I.C (volledig) · 1.3.I.D (kort, doorverwijzend) · 1.3.I.E
- **Gedekte concepten**: `jaarrekeninganalyse` (koepel) + `financiele-analyse-software` (instrumenten) + `financiele-diagnose` (eindresultaat)
- **Rationale**: Stagiair moet eerst snappen dat dit vak **vier categorieën** ratio's combineert met **kasstroom + diagnose**, dat het document een **publieke + adviserende rol** heeft, en wie de stakeholders zijn (5 partijen + 5 toezichthouders). Zonder entry verspilt de stagiair tijd in technische fiches die hij nog niet kan plaatsen.

### Leerstuk 2 — `jaarrekening-herwerken-en-functionele-balans` (techniek 1)

- **Vraag**: Hoe maak je een ruwe JR analyse-klaar — herrangschikking, schema-correcties, en het NBK/BBK/NT-drieluik berekenen?
- **Type**: techniek-fiche (mid-zwaar)
- **Gedekte kenniselementen**: 1.3.II.A · 1.3.II.B (rubrieken-structuur) · 1.3.II.C.1 (herwerking) · 1.3.II.C.2 (NBK)
- **Gedekte concepten**: `jaarrekening` (cross-PO; structuur) + `jaarrekeninganalyse` (sub-concept "Herstructurering balans voor analyse") + `activiteits-ratios` (sub: werkkapitaalbehoefte)
- **Rationale**: Twee voorbeeldexamen-vragen (2015-1 BBK + 2014-1 NT) testen letterlijk welke rubrieken meetellen — dat is per definitie een herwerkingsvraag. Plus: 2024-1 vraagt EV-berekening en passief-volgorde — beide testen JR-structuurkennis. Eén leerstuk bundelt herwerking + functionele balans want pedagogisch zijn ze één beweging.

### Leerstuk 3 — `ratios-en-kengetallen` (techniek 2, zwaar)

- **Vraag**: Hoe bereken en interpreteer je de vier ratio-families + DuPont + hefboomanalyse?
- **Type**: techniek-fiche (zwaarste leerstuk in het pakket — analoog aan `hoe-consolideren` in PO 1.4)
- **Gedekte kenniselementen**: 1.3.II.C (geheel, behalve C.2 die in leerstuk 2 zit en C.5 die naar leerstuk 5 gaat)
- **Gedekte concepten**: `liquiditeits-ratios` · `solvabiliteits-ratios` · `rentabiliteits-ratios` · `activiteits-ratios` · `ratio-interpretatie` (DuPont, sector-benchmark, cross-categorie verbanden) + `financiele-verrichtingen` (rubriek-65/75 voor hefboomanalyse)
- **Rationale**: Vier families samen behandelen + DuPont + hefboomanalyse = de technische kern van het PO. Examen-favoriet (10 van 13 vragen raken dit). Splitsen in vier leerstukken zou versnipperen en de cross-categorie-verbanden (DuPont = rentabiliteit × omloopsnelheid × hefboom) breken. Verdient extra lengte-budget (schrijfregels-cap zoals `hoe-consolideren`, ~4500-5500 woorden). Tabel-dominant: per ratio: formule + rubrieken + interpretatie + valkuilen.

### Leerstuk 4 — `kasstroom-en-financieringstabel` (techniek 3)

- **Vraag**: Hoe lees of bouw je een kasstroomoverzicht — drie IAS 7-categorieën, indirecte methode, FCF?
- **Type**: techniek-fiche (kort-middel)
- **Gedekte kenniselementen**: 1.3.II.C.3 (vermogensstroomtabel) + 1.3.II.D (bijzondere informatie — voor zover relevant voor cashanalyse)
- **Gedekte concepten**: `kasstroom-analyse` + `jaarrekening` (sub: kasstroomoverzicht onder IFRS verplicht / B-GAAP optioneel)
- **Rationale**: Kasstroomanalyse wordt door het examen weinig direct getoetst (impliciet via "operationele cashflow vóór belastingen" in 2015-1), maar is wél een aparte instrumentenclass die de student moet beheersen voor doel 1.3.1.2 (advies → cash-tekort-signalen). Apart leerstuk omdat de logica (drie categorieën, indirecte methode) anders is dan ratio-analyse. Niet samenvoegen met ratios — andere techniek.

### Leerstuk 5 — `kritische-beoordeling-en-diagnose` (synthese)

- **Vraag**: Hoe ga je van getallen naar een onderbouwd financieel oordeel + voorstellen tot verbetering, en welke continuïteits-signalen herken je?
- **Type**: synthese-fiche
- **Gedekte kenniselementen**: 1.3.II.C.4 (hefbomen voor diagnose) · 1.3.II.C.5 (falingspredictie + going concern) · 1.3.1.2 (voorstellen formuleren, integratie-niveau)
- **Gedekte concepten**: `financiele-diagnose` (procedure-koepel) + `ratio-interpretatie` (methodologie) + `window-dressing` (valkuil bij analyse) + `kasstroom-analyse` (going-concern-signalen)
- **Rationale**: Doelstelling 1.3.1.2 — voorstellen formuleren — is integratie-niveau. Vereist een eigen leerstuk waar de techniek samenkomt: ratio's + kasstroom + sector-benchmark → diagnose + aanbeveling + alarmbel-trigger. Plus: window-dressing herkennen (analist-perspectief) is een aparte vaardigheid. Falingspredictie (Altman Z-score) en alarmbel-procedure (WVV art. 5:153 / 7:228) raken sterk PO 1.9 maar zitten hier als **trigger**-instrument binnen de diagnose. Hier komt ook 1.3.I.D.4 (KOM) terug als doorklik.

### Geen aparte fiche voor 1.3.I.D-toezicht

De vijf toezichtsorganen (aandeelhouders / commissaris / ondernemingsraad / KOM / banken) leven grondig in:
- PO 1.6 (commissaris-werkzaamheden)
- PO 1.9 (KOM + insolventiesignalen)
- PO 3.0 (sociale wetgeving — OR)
- PO 1.5 of cross-record (covenants)

In 1.3 worden ze kort vermeld in **§1 (Waarom dit vak?) van de minicursus** + in de eerste sectie van **leerstuk 1 (entry)**. Aparte fiche levert duplicatie op met andere PO's.

---

## 4. Gap-check

| Kenniselement | Gedekt door | Status |
|---|---|---|
| 1.3.I.A doelstellingen | Leerstuk 1 (§ "Waarom analyseren?") | ✅ |
| 1.3.I.B betrokken partijen | Leerstuk 1 (§ "Voor wie?") + minicursus §1 | ✅ |
| 1.3.I.C.1 wettelijke documenten | Leerstuk 1 + leerstuk 2 (JR-structuur) | ✅ |
| 1.3.I.C.2 andere documenten (ratio's, FT, boordtabel) | Leerstuk 1 (instrumenten-overzicht) + leerstuk 3 (ratio's) + leerstuk 4 (FT) | ✅ |
| 1.3.I.D.1-5 toezichtsorganen | Leerstuk 1 (kort, doorverwijzend) + minicursus §1 | ⚠️ deels — diepte ligt in PO 1.6/1.9/3.0 |
| 1.3.I.E bestuursverslag | Leerstuk 1 (§ "Instrumenten") + leerstuk 5 (interpretatie) | ✅ |
| 1.3.II.A boekhoudprincipes + waarderingsregels | Leerstuk 2 (§ "Lezen van de toelichting") | ✅ rakend (PO 1.1/1.2) |
| 1.3.II.B JR-structuur | Leerstuk 2 (§ "De drie documenten + rubrieken") | ✅ |
| 1.3.II.C.1 JR herwerking | Leerstuk 2 (§ "Analytische balans") | ✅ |
| 1.3.II.C.2 NBK + functionele balans | Leerstuk 2 (§ "Functionele balans NBK/BBK/NT") | ✅ |
| 1.3.II.C.3 vermogensstroomtabel | Leerstuk 4 (kasstroom + financieringstabel) | ✅ |
| 1.3.II.C.4 operationele + financiële hefbomen | Leerstuk 3 (§ DuPont-decompositie + hefboom) + leerstuk 5 (toepassen) | ✅ |
| 1.3.II.C.5 falingspredictie / going concern | Leerstuk 5 (§ "Continuïteits-signalen + Altman") | ✅ rakend (PO 1.9) |
| 1.3.II.D bijzondere informatie niet-balans-rechten/verplichtingen | Leerstuk 4 (off-balance items voor cash) + leerstuk 5 (risico-signalen uit toelichting) | ⚠️ klein onderwerp, geen aparte sectie |

**Geen kritieke gaten.** Twee zwakke dekkingen (1.3.I.D toezicht + 1.3.II.D bijzondere info) zijn bewust beperkt gehouden — beide leven dieper in andere PO's of zijn kleine sub-aspecten.

---

## 5. Minicursus-skelet

Volgt canonieke 5-secties-structuur van ADR-036.

### §1 — Waarom dit vak?

- Motivatie: JR opstellen ≠ JR lezen; pas met ratio's + sectorbenchmark + diagnose krijg je een oordeel.
- Brede-programma-tabel: relatie tot 1.1 (boekhouding levert cijfers), 1.2 (schema-keuze bepaalt wat berekenbaar), 1.4 (geconsolideerd analyseren), 1.5 (IFRS), 1.6 (going-concern in audit), 1.9 (Altman + alarmbel).
- 5 stakeholders + 5 toezichthouders kort genoemd (doorklik naar leerstuk 1).

### §2 — Wat is dit vak?

Vijf compacte sub-secties, elk eindigend met wikilink:

- "Het probleem — 60 pagina's, één oordeel" → context voor [[wat-is-jaarrekeninganalyse]]
- "De oplossing — vier ratio-families + kasstroom + diagnose" → [[wat-is-jaarrekeninganalyse]]
- "Eerst herwerken, dan rekenen — analytische + functionele balans" → [[jaarrekening-herwerken-en-functionele-balans]]
- "De vier ratio-families als familie" → [[ratios-en-kengetallen]]
- "Van getal naar oordeel — diagnose en voorstellen" → [[kritische-beoordeling-en-diagnose]] + [[kasstroom-en-financieringstabel]]

### §3 — Wat moet je kunnen + hoe pak je het aan

Leerstukken-leesroute in 4 stappen (entry → herwerken → ratio's + kasstroom → diagnose) + verwijzing naar samenvatting voor herhaling. Geen rol-blokken meer (die zitten in leerstukken zelf via accountant-perspectieven).

### §4 — Examen-radar

Tabel met 13 vraag-eenheden + observatie:
- Patroon: "formule + rubrieken motiveren" >> volledig uitgewerkte analyses
- Schema-bewustzijn (verkort vs volledig) is examen-favoriet
- Functionele balans (NBK/BBK/NT) is 2× expliciet getoetst
- Begrips-definities scherp (intrinsieke ≠ fractie ≠ beurs; bruto in 2 betekenissen)

### §5 — Concepten cross-PO

Tabel:

| Concept | Cross-PO | Waarom relevant elders |
|---|---|---|
| `jaarrekening` (structuur) | 1.1 · 1.2 · 1.4 | Bron van de cijfers |
| `kasstroom-analyse` | 1.5 (IFRS) · 1.9 | IFRS-verplicht; insolventie-signaal |
| `liquiditeits-ratios` · `solvabiliteits-ratios` | 1.9 · 3.0 | Alarmbel-trigger WVV art. 5:153/7:228 |
| `rentabiliteits-ratios` | 1.5 · 4.x (waardering) | EBITDA-marge in IFRS; ROIC voor bedrijfswaardering |
| `financiele-diagnose` | 1.6 · 1.9 | Going-concern-audit (ISA 570); insolventie |
| `window-dressing` | 1.6 (audit) | Risico-analyse audit-planning |

---

## 6. Voorbeeldgroep

### Voorstel: **nieuwe voorbeeldgroep** — niet hergebruiken

Reden:
- **Aurelia** (1.4) is een groep van 4 dochters, gebouwd voor consolidatie. Voor 1.3 wil je één enkelvoudige onderneming met **volledige JR + meerjarige cijfers** — een groep voegt complexiteit toe die niets oplevert.
- **Meridia** (1.8) is voor analytische boekhouding (kostprijscalculatie); geen jaarrekening-volledig-schema-data.

### Voorstel: **"Belova NV"** — Belgische KMO productie/handel, volledig schema

**Karakteristieken**:
- Rechtsvorm: NV (zodat passief-rubriek "Inbreng/Kapitaal" klassiek blijft, anders dan BV-zonder-kapitaal die in 2024-1 als valkuil verschijnt)
- Sector: groothandel meubilair (sector-benchmark beschikbaar via NBB) — bewuste keuze om met **Meridia (1.8 meubel)** een didactische echo te leggen
- Omvang: groot genoeg om volledig schema te vereisen (>50 medewerkers / >9 M€ omzet) → grondtoon voor volledig-vs-verkort-bewustzijn
- Balansdatum: 31/12/N
- Boekjaar N + N-1 + N-2 (3 jaar voor trend-analyse, zoals doctrine voorschrijft)
- Eén commissaris (referentie naar 1.3.I.D.2)
- Eén bankkrediet met covenanten (referentie naar 1.3.I.D.5)

**Te genereren documenten**:
- Balans N + N-1 + N-2 (volledig schema, alle rubrieken)
- Resultatenrekening N + N-1 + N-2
- Toelichting: waarderingsregels (FIFO voorraad, lineaire afschr. 5 jaar), niet-in-balans rechten/verplichtingen, vervallen schulden, verstrekte waarborgen
- Sociale balans (kort)
- Sector-benchmark-tabel (NBB-balanscentrale stijl)
- Analytische balans (herrangschikt)
- Functionele balans NBK/BBK/NT (uitgewerkt)
- Volledige ratio-tabel (vier families, 12+ ratio's) met 3-jaar evolutie
- Kasstroomoverzicht (indirecte methode)
- Mini-DuPont decompositie
- Mini hefboomanalyse
- **Diagnose-paragraaf**: 3 sterktes + 3 alarmsignalen + 3 aanbevelingen

**Cijfers-strategie**: zorg dat sommige ratio's gezond zijn en andere zwak — anders heb je niets om over te diagnoseren. Voorgesteld profiel: rentabiliteit dalend (margedruk), liquiditeit comfortabel (cash-overschot), solvabiliteit middelmatig, activiteit met stijgende DSO (klantenrisico). Eén alarmsignaal voor going-concern: een covenant-schending in jaar N.

### Alternatief: hergebruik examen-tabellen 2013-1/2014-1/2015-1

De examens 2013-1, 2014-1 en 2015-1 hebben dezelfde tabel (377.872 totaal-activa NBB-stijl) waaruit ratio's berekend worden. Dat is een **kant-en-klare didactische case**. Hergebruiken zou tijd besparen maar geen N-1/N-2/sector-benchmark/toelichting bevatten — dus net wat een student voor échte analyse nodig heeft mist.

**Aanbeveling**: nieuwe voorbeeldgroep Belova, maar voor de **oefening** kunnen we de examen-cijfers als inspiratie nemen (kleinere fictieve onderneming "Tessera BV" — zie sectie 8 hieronder).

---

## 7. Samenvatting + oefening

### Samenvatting (`data/samenvattingen/1-3.yaml` + `content/studiemateriaal/1-3/samenvatting.md`)

Volgens ADR-039 / samenvatting-procedure: 2-4 A4 printbaar, visueel-dominant.

**Voorgestelde blokken**:
1. Intro-callout (no-print)
2. Take-away (5 bullets: 4 families samen + functionele balans + schema-bewust)
3. **Tabel-blok "Vier ratio-families"** — kolom: formule | rubrieken | richtwaarde | valkuilen
4. **Drempel-blok "Verkort vs volledig schema"** — welke ratio's vallen weg + waarom
5. **Beslisboom (mermaid)** "Welke ratio bij welke vraag?" — liquiditeits-/solvabiliteits-/rentabiliteits-/activiteits-as
6. **Tabel-blok "NBK / BBK / NT"** — formules + interpretatie + welke rubrieken
7. **Tabel-blok "Begrippen scherp"** — intrinsieke vs fractie vs beurs; bruto vs netto in 2 betekenissen; EBIT vs EBITDA; solvabiliteit vs zelffinanciering
8. Valkuilen (3-koloms: Valkuil · Wat klopt niet · Wat klopt wel) — bv. window-dressing, "netto = na belasting", BBK rubriek-42-meetellen, verlies-impact-op-brutomarge
9. Verdieping (no-print): doorklik naar leerstukken + concept-fiches

### Oefening (`data/oefeningen/<slug>.yaml` + `content/studiemateriaal/1-3/oefening.md`)

Volgens oefening-procedure: 60-75 min, één pad volledig doorgewerkt, geen hints in opgave.

**Voorstel**: "**Tessera BV** — financiële diagnose in 5 stappen"

- **Case**: KMO meubel-detailhandel; balans N en N-1 + RR + minimale toelichting (verkort schema, om de schema-valkuil te oefenen)
- **Stappen** (60-75 min):
  1. Herrangschik de balans + bereken NBK · BBK · NT (eenvoudig). Hint-vrije instructie.
  2. Bereken 8 ratio's (2 per familie). Motiveer met rubrieken.
  3. DuPont-decompositie ROE.
  4. Identificeer 3 alarmsignalen (bewust ingebouwde signalen: dalende margine, stijgende DSO, daling cash). 
  5. Formuleer 3 voorstellen aan het bestuur.
- **Niet-doelstelling**: geen kasstroomoverzicht (te complex voor 75 min); afsplitsen naar facultatieve "verder oefenen"-doorklik.

**Cijfers**: kleiner dan Belova (totaal-activa ~500 K€), ronde cijfers, eindbalans klopt, tussenstappen consistent. Cijfers gekozen om elke ratio een didactisch interessant resultaat te geven.

---

## 8. Open vragen voor sparring

1. **Voorbeeldgroep — Belova NV (volledig schema, productie/handel meubel, 3 jaar) of variant?**
   - Aanbevolen: Belova zoals beschreven. Geeft alle ingrediënten voor 5 leerstukken.
   - Alternatief: kleinere KMO + verkort schema (om schema-valkuilen prominent te maken). Maar dan kun je sommige ratio's niet berekenen — leerstuk 3 mist materiaal.

2. **Leerstuk-aantal — 5 of 6?**
   - 5 zoals voorgesteld (entry · herwerken · ratio's · kasstroom · diagnose).
   - Alternatief: 6 met **`kasstroom-en-financieringstabel`** + **`toezicht-en-stakeholders`** apart. Maar 1.3.I.D leeft echt elders → liever niet.
   - Alternatief: 4 door `kasstroom-en-financieringstabel` te integreren in `ratios-en-kengetallen`. Maar dat maakt leerstuk 3 te zwaar.

3. **Cross-PO-status voor leerstuk 4 (`kasstroom-en-financieringstabel`)?**
   - Mogelijk cross-PO want IFRS-relevant (PO 1.5) en insolventie-relevant (PO 1.9). Maar voor 1.3 ligt het in 1-3/-folder; bij 1.5/1.9-bouw beslis dan over verplaatsing.
   - Aanbevolen: nu in `content/studiemateriaal/1-3/`, later eventueel verhuizen.

4. **Falingspredictie (Altman) — in leerstuk 5 of doorklik naar PO 1.9?**
   - Voorgesteld: in leerstuk 5 als **trigger-instrument** voor de accountant + doorklik naar PO 1.9 voor de insolventie-procedure-zijde.

5. **Oefening — Tessera BV verkort schema (om schema-valkuil te oefenen) of volledig schema (volledige ratio-set)?**
   - Voorgesteld: verkort, om examen-2024-1-valkuil ("welke ratio kan je niet berekenen?") expliciet te integreren in de oefening.

6. **DuPont + hefboomanalyse — in leerstuk 3 ratio's of leerstuk 5 diagnose?**
   - Voorgesteld: techniek in leerstuk 3 (cross-categorie verband), toepassing in leerstuk 5 (gebruiken voor oordeel).

7. **Bestaande `content/studiemateriaal/1-3/index.md`** (huidige minicursus): verplaatsen naar `1-3/index.md` + bijwerken, of opnieuw schrijven?
   - Voorgesteld: gebruiken als bron voor verhaal-secties (de §1+§2-inhoud is hergebruikbaar), maar §3 herstructureren naar nieuw leerstuk-leesroute. Oude `1.3.md` wordt verwijderd in stap 8 (cleanup).

---

## Rapport

- **5 leerstukken voorgesteld** (entry · herwerken+functionele balans · 4 ratio-families+DuPont+hefboom · kasstroom · diagnose+continuïteit).
- **Hoofdtaak**: financiële analyse + voorstellen formuleren — niveau **integratie** (hoogst in programma).
- **Geen kritieke gaten**; twee zwakke dekkingen bewust (1.3.I.D toezicht + 1.3.II.D bijz. info) — leven in andere PO's.
- **Nieuwe voorbeeldgroep** "Belova NV" voorgesteld; oefening met aparte kleinere case "Tessera BV" (verkort schema voor schema-valkuil).
- **Belangrijkste onzekerheid**: voorbeeldgroep-omvang (volledig vs verkort) en of leerstuk 4 (kasstroom) als apart leerstuk de moeite waard is gezien de beperkte examen-frequentie.
- **Volgende stap**: na sparring → voorbeeldgroep-YAML schrijven (Belova) + scripts voor alle 5 leerstukken (Opus-pass).
