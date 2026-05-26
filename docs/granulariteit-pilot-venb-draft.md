# Granulariteit-pilot K-fiscaal/VenB — voorstel

**Status**: Draft (2026-05-23). Pilot-uitvoering van ADR-030 §Migratie-aanpak op PO 2.3 Vennootschapsbelasting. Doel: tree-skelet + dispositie per huidig VenB-record ter validatie cluster-per-cluster. Geen records aangeraakt.

**Input**:
- [ADR-030](adr/ADR-030-granulariteit-typologie.md) — canonieke regels A-I + bundel-criterium (Regel I) + casussen
- [`granulariteit-typologie-draft.md`](granulariteit-typologie-draft.md) §6 — DBI/moeder-dochter, consolidatiekring, ondernemingsvormen
- `data/programma/programma.json` — PO 2.3 taken/doelstellingen/kenniselementen (21 anchors)
- `data/concepten/records/` — 396 records (huidige snapshot)

---

## A. Scope-afbakening pilot

**Binnen scope PO 2.3**: alles wat conceptueel onder vennootschapsbelasting valt (taken 1-5 + kennisniveaus 2.3.I/II/III). Resultaat-set ≈ 70 records (zie clusters hieronder).

**Buiten scope (laat staan voor andere PO's, ook al raken ze taak 1-2)**:
- WVV/vennootschapsrecht-records: `bestuur-vennootschap`, `kapitaalbescherming-en-winstverdeling`, `alarmbel`, `aansprakelijkheid-oprichters-bestuurders`, `bijzondere-verslagen-vennootschapsverrichtingen`, `controle-vennootschapsrecht`, `vennootschapsgeschillen`, `vennootschapsrechtelijk-kader-wvv`, `algemene-vergadering`, `commissaris-mandaat-en-statuut` → PO 1.4 vennootschapsrecht
- Pure PB-records, BTW-records, audit-records: niet aangeroerd
- Successie (`holding-successieplanning`, `maatschap-successieplanning`): horen primair PO 2.4 successie — wel via `relaties[]` linken

**Grijs gebied (raken meerdere PO's, behandeld als "support-record" voor PO 2.3 maar canoniek elders)**:
- `aanslag-cyclus`, `aanslagtermijnen-fiscaal`, `bedrijfsvoorheffing`, `fiscale-controle`, `bezwaarprocedure-fiscaal`, `dubbelbelastingverdrag`, `fiscale-residentie`, `juridische-constructie-cayman` → blijven waar ze zijn; niet meegerekend in de pilot-reductie.

---

## B. Tree-skelet PO 2.3 (top-down)

```
PO 2.3 Vennootschapsbelasting
│
├── Kader-domein (koepel, navigatie — licht)
│   └── vennootschapsbelasting (bestaat)
│
├── Kader-techniek (uit PO-taken — DRAGER van integratie-leerstof, DIEP)
│   ├── aangifte-vennootschapsbelasting (bestaat — taak 4 + 2.3.II.B/G/H/J)
│   │     Draagt: aftrekvolgorde · korf · stap-voor-stap · biztax-indiening
│   ├── reorganisatie-vennootschap-fiscaal (NIEUW — taak 2 + 2.3.III.B)
│   │     Bundelt fiscale aspecten van fusie/splitsing/inbreng/ontbinding
│   ├── exit-planning-vennootschap (bestaat — taak 2 + 2.3.III.B optimaliseren vereffening)
│   ├── internationale-structurering-vennootschap (bestaat — taak 3 advies)
│   ├── holding-successieplanning (bestaat — overlap PO 2.4)
│   └── patrimoniumvennootschap (bestaat — taak 3 advies)
│
├── Kader-techniek "structurerend" (niet uit één taak maar didactisch noodzakelijk)
│   ├── belastbare-grondslag-vennootschapsbelasting (bestaat — 2.3.II.B kern-structuur,
│   │     "vertrekpunt → correcties → aftrekken → tarief"; verwijst naar Regelingen)
│   └── toepassingsgebied-vennootschapsbelasting (bestaat — 2.3.II.A;
│       BV/NV-rijksinwoner-toets, fiscaal-transparante vennootschappen, art. 179)
│
├── Entiteit-bundel
│   └── ondernemingsvormen (NIEUW — Regel I keuze-bundel; consolideert bv-rechtsvorm + cv +
│       maatschap + eenmanszaak + nv etc. tot één bundel met anchors per vorm)
│
├── Entiteit-solo
│   ├── deelneming (NIEUW — consolidatie van 3 deelneming-records)
│   ├── groep · consortium · consolidatiekring (bestaan los — blijven licht, secties in
│       Kader-techniek `consolidatie-techniek` uit PO 1.2)
│
├── Gebeurtenis (corporate events met fiscale + WVV-perspectief)
│   ├── oprichting-vennootschap (bestaat)
│   ├── kapitaalverhoging · kapitaalvermindering (bestaan)
│   ├── inbreng-onroerend-in-vennootschap (bestaat)
│   ├── inbreng-van-bedrijfstak-of-algemeenheid (bestaat)
│   ├── fusie · splitsing (bestaan)
│   ├── omzetting-vennootschap (bestaat)
│   ├── ontbinding-en-vereffening (bestaat)
│   ├── inkoop-eigen-aandelen (bestaat)
│   └── uitkering-aan-aandeelhouders (bestaat — dividend)
│
└── Regeling (atomair, losse mechanismes — Regel I "NIET-bundelen")
    ├── Aftrekken/verminderingen
    │   ├── dbi-aftrek (NU sub-element → wordt top-level — exacte ADR-030 §6 casus)
    │   ├── notionele-interestaftrek (bestaat)
    │   ├── investeringsaftrek (bestaat)
    │   ├── overgedragen-verliezen (bestaat)
    │   ├── verlaagd-tarief-kleine-vennootschap (bestaat — starterstarief incl.)
    │   ├── korf-beperking (NU sub-element → wordt top-level Regeling)
    │   └── liquidatiereserve (bestaat)
    │
    ├── Verworpen-uitgaven & kostenbeperkingen
    │   ├── verworpen-uitgaven (bestaat — als samenhang-bundel? of bundel met sub-secties
    │   │     per VU-type; OPEN — zie cluster F)
    │   ├── aftrekbare-beroepskosten-venb (bestaat — pendant van VU, blijft)
    │   ├── ebitda-aftrekbeperking (bestaat)
    │   ├── abnormale-goedgunstige-voordelen (bestaat)
    │   └── algemene-anti-misbruik-bepaling (bestaat — GAAR)
    │
    ├── Bijzondere aanslagregelingen (2.3.II.I — als bundel blijven of opsplitsen)
    │   └── bijzondere-aanslagen-venb (bestaat — bundel met 5 sub-aanslagen;
    │       OPEN — zie cluster E)
    │
    ├── Reorganisatie-Regelingen
    │   ├── fiscale-fusie-splitsing (bestaat — belastingvrije reorganisatie-regime)
    │   ├── quasi-inbreng (bestaat — al WVV-overlap)
    │   ├── exit-belasting (bestaat)
    │   └── vereffening-fiscaal (bestaat — fiscale aspecten ontbinding)
    │
    ├── Internationaal/EU
    │   ├── moeder-dochterrichtlijn (bestaat 21KB hybride →
    │   │   distilleer bron + behoud lichte Regeling-record voor DBI-rechtsgrondslag)
    │   ├── fiscale-fusierichtlijn (bestaat — idem distilleer-actie)
    │   ├── interest-royalty-richtlijn (bestaat — idem)
    │   ├── atad-richtlijn (bestaat — idem)
    │   ├── forfaitair-gedeelte-buitenlandse-belasting (bestaat — FBB)
    │   ├── buitenlandse-winst-en-verlies (bestaat)
    │   ├── beps-actieplan (bestaat)
    │   ├── country-by-country-reporting (bestaat)
    │   ├── belasting-niet-inwoners (bestaat — raakt toepassingsgebied)
    │   └── bijzonder-regime-buitenlandse-kaderleden (bestaat — overlap PB)
    │
    ├── Voorheffingen & aanslag-mechanica VenB-specifiek
    │   ├── voorafbetalingen-vennootschapsbelasting (bestaat)
    │   └── voorheffingen-en-verrekeningen-venb (bestaat)
    │
    └── Boekhoud-fiscaal interface (2.3.I)
        ├── boekhoudkundig-fiscaal-attachment (bestaat)
        ├── be-gaap-vs-ifrs-verschillen (bestaat — overlap PO 1.2)
        ├── boekhoudplichtige-onderneming (bestaat — overlap PO 1.1)
        └── groottecategorie-vennootschap (bestaat — criterium-Regeling)
```

---

## C. Mapping per cluster (huidig → nieuw)

Legenda: **BLIJFT** · **SMELT** in record X · **SUB#anchor** (sub-sectie met anchor binnen bundel) · **NIEUW** · **WORDT TOP-LEVEL** · **DISTILLEER** (bron-inhoud uit record naar `resources/bronnen/`).

### Cluster 1 — Aftrekken & korf (Regel I "losse mechanismes")

| Huidig | Dispositie |
|---|---|
| `belastbare-grondslag-vennootschapsbelasting.inhoud.elementen[dbi-aftrek]` | **WORDT TOP-LEVEL** `dbi-aftrek.json` (ADR-030 §6 casus) |
| `belastbare-grondslag-vennootschapsbelasting.inhoud.elementen[korf-beperking]` | **WORDT TOP-LEVEL** `korf-beperking.json` |
| `notionele-interestaftrek` · `investeringsaftrek` · `overgedragen-verliezen` · `liquidatiereserve` · `verlaagd-tarief-kleine-vennootschap` | **BLIJVEN** (5 records) |
| `belastbare-grondslag-vennootschapsbelasting` | **BLIJFT** als Kader-techniek; behoudt sub-elementen `vertrekpunt-boekhoudkundige-winst`, `verworpen-uitgaven`, `aftrekken-in-volgorde`, `afzonderlijk-belastbare-bestanddelen`, `belastbaar-tijdperk` als kern-secties (geen eigen records); verwijst naar de top-level Regelingen i.p.v. inhoud te dupliceren |

**Effect**: 1 record (grondslag) + 5 bestaande + 2 nieuwe top-level = 8. Geen reductie, wel ontklemming uit sub-element-positie.

### Cluster 2 — Deelneming (consolidatie volgens ADR-030 §6 casus 1)

| Huidig | Dispositie |
|---|---|
| `deelneming-financieel-vast-actief` · `kwalificatie-controle-deelneming` · `controle-test-deelneming` | **SMELTEN** tot 1 nieuw `deelneming.json` (Entiteit met aspect-secties: boekhouding/fiscaal/audit/advies) |
| `meerwaarde-aandelen-venb` | **BLIJFT** als aparte Regeling (eigen mechanisme: art. 192-vrijstelling) |

**Effect**: 4 → 2 records (−2).

### Cluster 3 — Internationaal (richtlijnen — distillatie volgens ADR-030 §6 casus 1)

| Huidig | Dispositie |
|---|---|
| `moeder-dochterrichtlijn` (21KB hybride) | **DISTILLEER**: bron → `resources/bronnen/wetteksten/eu/moeder-dochterrichtlijn.md`; record blijft als lichte Regeling/grondslag-stub of vervalt (→ `dbi-aftrek.grondslag.bronnen[]`) |
| `fiscale-fusierichtlijn` | **DISTILLEER** idem; grondslag-bron voor `fiscale-fusie-splitsing` |
| `interest-royalty-richtlijn` | **DISTILLEER** idem; grondslag-bron voor relevant Regeling |
| `atad-richtlijn` | **DISTILLEER** idem; grondslag-bron voor `ebitda-aftrekbeperking`, exit-belasting, CFC |
| `forfaitair-gedeelte-buitenlandse-belasting` · `buitenlandse-winst-en-verlies` · `beps-actieplan` · `country-by-country-reporting` · `belasting-niet-inwoners` · `bijzonder-regime-buitenlandse-kaderleden` · `exit-belasting` | **BLIJVEN** als aparte Regelingen |

**Effect**: 4 richtlijn-records → 0-2 records (rest wordt bron). Reductie −2 à −4.

### Cluster 4 — Reorganisatie-cluster (taak 2 + 2.3.III.B/C)

| Huidig | Dispositie |
|---|---|
| `fiscale-aandachtspunten-herstructurering` | **SMELT** in nieuwe Kader-techniek `reorganisatie-vennootschap-fiscaal` (kern-sectie + perspectieven) |
| `fiscale-fusie-splitsing` | **BLIJFT** als Regeling (belastingvrije reorganisatie-regime) — verwijst-naar nieuwe Kader-techniek |
| `vereffening-fiscaal` | **BLIJFT** als Regeling (fiscale aspecten ontbinding/liquidatiereserve-interactie) |
| `exit-planning-vennootschap` | **BLIJFT** als Kader-techniek (optimalisering vereffening) |
| `gerechtelijke-reorganisatie` | **BLIJFT** (raakt vooral PO 2.7 insolventie — niet primair VenB) |
| `fusie` · `splitsing` · `omzetting-vennootschap` · `ontbinding-en-vereffening` · `inbreng-van-bedrijfstak-of-algemeenheid` · `inbreng-onroerend-in-vennootschap` · `kapitaalverhoging` · `kapitaalvermindering` · `oprichting-vennootschap` · `inkoop-eigen-aandelen` · `uitkering-aan-aandeelhouders` · `quasi-inbreng` | **BLIJVEN** als Gebeurtenissen/Regelingen (hub-rol; krijgen fiscaal-perspectief uit `accountant_perspectieven[]`); zijn deels WVV-records, met VenB-aspect-sectie |

**Effect**: −1 (samensmelting `fiscale-aandachtspunten-herstructurering`) +1 nieuwe Kader-techniek = 0 netto, +1 als de Kader-techniek écht nieuw wordt gemaakt naast de bestaande aandachtspunten-record. **Open beslissing**: heeft `reorganisatie-vennootschap-fiscaal` voldoende eigen verhaal naast `exit-planning-vennootschap` + `fiscale-fusie-splitsing` om eigen record te zijn? Voorstel: ja, want bundelt fusie+splitsing+inbreng+ontbinding-perspectieven en draagt de "wanneer welke route"-afweging.

### Cluster 5 — Bijzondere aanslagregelingen (2.3.II.I)

`bijzondere-aanslagen-venb` is een bundel met 5 sub-aanslagen. **Open vraag (zie §D)**: bundel houden of opsplitsen?
- **Optie A** (bundel houden, samenhang-bundel): blijft 1 record. 0 extra records.
- **Optie B** (opsplitsen): 5 nieuwe Regelingen, bundel vervalt. +4 records.

ADR-030 Regel I: aftrekken-cluster is "losse mechanismes" → niet bundelen. Symmetrie zou zeggen: ook bijzondere aanslagen opsplitsen. Maar er is geen Kader-techniek waar de integratie woont (geen "aangifte-bijzondere-aanslag"). Voorstel: **Optie A** (bundel houden) — laag risico, behoudt didactische cohesie, geen kunstmatige Kader-techniek nodig.

### Cluster 6 — Verworpen uitgaven & kostenbeperkingen

| Huidig | Dispositie |
|---|---|
| `verworpen-uitgaven` | **BLIJFT** als bundel-concept (samenhang-bundel — alle VU's worden in aangifte VAK N samen bijgeteld; je studeert ze als categorie) — met sub-secties per VU-type |
| `verworpen-uitgaven-autokosten` | **SMELT** als `verworpen-uitgaven#autokosten` |
| `aftrekbare-beroepskosten-venb` | **BLIJFT** (Regeling — algemene aftrekbaarheidstoets art. 49 voor VenB-context) |
| `ebitda-aftrekbeperking` · `abnormale-goedgunstige-voordelen` · `algemene-anti-misbruik-bepaling` | **BLIJVEN** (eigen mechanismes) |

**Effect**: −1 (autokosten in bundel). **Open**: is `verworpen-uitgaven` echt een samenhang-bundel of moeten de bestanddelen (geen-bedrijfsmatige-kosten, autokosten, restaurantkosten, sociale-voordelen, geldboetes, etc.) elk eigen Regeling worden? Voorstel: **bundel houden** want behandeld als één hoofdstuk in praktijkgidsen.

### Cluster 7 — Ondernemingsvormen (nieuw bundel — ADR-030 §6 casus 3)

| Huidig | Dispositie |
|---|---|
| `bv-rechtsvorm` · `cv-rechtsvorm` · `maatschap-rechtsvorm` | **SMELTEN** tot nieuwe bundel `ondernemingsvormen.json` met anchors `#bv`, `#cv`, `#maatschap`, `#nv` (toevoegen), `#commv` (toevoegen), `#eenmanszaak` (toevoegen) |
| Andere records die naar BV/NV linken (bv. `kapitaalverhoging`, `alarmbel`, `kapitaalbescherming-en-winstverdeling`) | `relaties[].target` update naar `ondernemingsvormen#bv` enz. |

**Effect**: 3 → 1 record (−2). **Let op**: technisch eerst de `#anchor`-suffix in schema/records-API/render-laag landen voordat we deze migratie doen.

### Cluster 8 — Consolidatie (overlap PO 1.2 — niet pilot-kern)

Records `consolidatiekring`, `consolidatiemethoden`, `consolidatieverplichting-bgaap`, `consolidatieverschil-goodwill`, `eerste-consolidatie`, `evenredige-consolidatie`, `integrale-consolidatie`, `uniforme-waarderingsregels-consolidatie`, `wijziging-consolidatiekring`: horen primair onder PO 1.2 boekhoudrecht/consolidatie. **Laat staan in pilot**; krijgen eigen pilot in tweede ronde (K-boekhouding).

---

## D. Open beslissingen waar bevestiging nodig is

1. **`reorganisatie-vennootschap-fiscaal` als nieuwe Kader-techniek?** — of de drie bestaande records (`fiscale-aandachtspunten-herstructurering`, `exit-planning-vennootschap`, `fiscale-fusie-splitsing`) volstaan?
2. **`bijzondere-aanslagen-venb`: bundel houden (Optie A) of opsplitsen (Optie B)?**
3. **`verworpen-uitgaven`: bundel houden (voorstel) of opsplitsen per VU-type?**
4. **Internationale richtlijn-records**: distilleer-actie nu doen (deel van pilot) of als aparte vervolgactie?
5. **`toepassingsgebied-vennootschapsbelasting`**: blijft eigen Kader-techniek, of smelt als sectie #toepassingsgebied in koepel `vennootschapsbelasting`?

---

## E. Reductie-balans

| Cluster | Δ records |
|---|---|
| 1. Aftrekken & korf | +2 (sub→top), 0 reductie |
| 2. Deelneming | −2 |
| 3. Internationaal (distillatie) | −2 à −4 |
| 4. Reorganisatie | 0 à +1 |
| 5. Bijzondere aanslagen (Optie A) | 0 |
| 6. Verworpen uitgaven | −1 |
| 7. Ondernemingsvormen | −2 |

**Pilot-totaal** (PO 2.3-kern): ~70 records → ~63-66 records (−5 à −10).

Dat is **veel minder dan de ADR-030 streefcijfer ~25-35**. Belangrijke oorzaak: ADR-030's "~80 VenB-records → ~25-35" rekende een ruimere VenB-scope (incl. consolidatie + WVV-overlap + lichte Entiteiten) en veronderstelde agressievere bundeling. In deze afbakening:
- Consolidatie-cluster (9 records) zit in PO 1.2-pilot
- WVV-records (~10) liggen buiten pilot
- Reorganisatie-Gebeurtenissen (fusie, splitsing, inbreng, …) blijven los want elk heeft eigen WVV+fiscaal-verhaal

**Signaal richting design-modus**: of (a) de ADR-030-schatting moet bijgesteld worden, of (b) de Gebeurtenis-records moeten alsnog bundelen (bv. `reorganisatie-gebeurtenissen` als bundel met anchors per type). Vraagt bevestiging — geen autonome beslissing in werk-modus.

---

## F. Validatie-volgorde voorstel

1. **Cluster 7 ondernemingsvormen** (kleinste, schoonste casus — gelijk aan ADR-030 §6)
2. **Cluster 2 deelneming** (klassieke consolidatie — gelijk aan ADR-030 §6)
3. **Open vragen §D** (vooral 1+5 — afbakening Kader-techniek-records)
4. **Cluster 4 reorganisatie** + **Cluster 5 bijzondere aanslagen** (complexer)
5. **Cluster 3 internationaal** (distillatie-actie — hangt af van bronnen-pipeline beschikbaarheid)
6. **Cluster 1 + 6** (mechanisch — uitvoering na §D-beslissingen)
