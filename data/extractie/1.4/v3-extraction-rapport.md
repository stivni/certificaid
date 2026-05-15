# PO 1.4 — Concept-extractie v3 — Rapport

**Run-id**: `concept-extractie-v3-2026-05-15T13:36Z`
**Datum**: 2026-05-15
**Programmaonderdeel**: 1.4 — Geconsolideerde jaarrekening
**Schema**: ADR-007 v1.2
**Werkprompt**: `prompts/concept-extractie-v3.md`

---

## 1. Cijfermatige samenvatting

| Maat | Aantal |
|---|---|
| Nieuwe concept-records geschreven (flat `data/concept_records/`) | 30 |
| Bijgewerkte bestaande records | 0 (v1/v2 gearchiveerd, schone start) |
| Dangling-references gelogd | 9 |
| Nieuwe bron-voorstellen toegevoegd | 1 (v3-herbevestiging IFRS-tekst-gap) |
| Anchors verwerkt | 13 / 13 (alle PO 1.4-anchors) |

Doelinterval volgens taakomschrijving was 25-35 records — uitkomst valt midden in dat interval.

## 2. Aanwezigheid must-have-begrippen

Onderstaande "mens-must-haves" uit de taakomschrijving zijn alle geleverd:

| Must-have | Record-id | Aanwezig |
|---|---|---|
| controle | `controle.json` | ✅ |
| controlepercentage | `controlepercentage.json` | ✅ |
| belangenpercentage | `belangenpercentage.json` | ✅ |
| exclusieve-controle | `exclusieve-controle.json` | ✅ |
| gezamenlijke-controle | `gezamenlijke-controle.json` | ✅ |
| invloed-van-betekenis | `invloed-van-betekenis.json` | ✅ |
| geassocieerde-onderneming | `geassocieerde-onderneming.json` | ✅ |
| integrale-consolidatie | `integrale-consolidatie.json` | ✅ |
| evenredige-consolidatie | `evenredige-consolidatie.json` | ✅ |
| vermogensmutatiemethode | `vermogensmutatiemethode.json` | ✅ |
| consolidatieverschil | `consolidatieverschil.json` | ✅ |
| consolidatiekring | `consolidatiekring.json` | ✅ |
| consolidatieverplichting | `consolidatieverplichting.json` | ✅ |
| groottecriteria | `groottecriteria-consolidatie.json` | ✅ |
| consortium | `consortium.json` | ✅ |
| vrijstelling-subconsolidatie | `vrijstelling-subconsolidatie.json` | ✅ |
| uniforme-waarderingsregels-consolidatie | `uniforme-waarderingsregels-consolidatie.json` | ✅ |
| intragroep-eliminaties | `intragroep-eliminaties.json` | ✅ |

Aanvullende records (uit recursive deepening + cross-bron synthese):

- `moedervennootschap`, `dochteronderneming`, `gemeenschappelijke-dochteronderneming`
- `minderheidsbelangen` (op opmerking uit taak: één record voor zowel balans- als resultaatperspectief)
- `wijziging-consolidatiekring`, `eerste-consolidatie`, `step-acquisition`
- `geconsolideerde-jaarrekening`, `geconsolideerd-jaarverslag`
- `horizontale-consolidatie`
- `groep-van-beperkte-omvang`
- `ifrs-consolidatieraamwerk` (anker-record met gap-log)

## 3. Toepassing van de v3-kwaliteitsregels

### Regel 1 — Centraliteit impliceert volledigheid

De vier kernconcepten die door alle andere records worden aangeroepen zijn diepgewerkt:
- **`controle.json`** — bouwstenen (in rechte / in feite), 4 vergelijkingsparen, drie in_praktijk-aspecten, 2 valkuilen.
- **`integrale-consolidatie.json`** — 5 bouwstenen (KB WVV art. 3:126, 3:127, 3:130, 3:134, 3:137), 1 berekeningsmethode met cijfervoorbeeld, 4 vergelijkingsparen, 3 valkuilen.
- **`vermogensmutatiemethode.json`** — 4 bouwstenen (eerste consolidatie, latere consolidatie, presentatie balans, presentatie resultatenrekening), 2 berekeningsmethodes met cijfervoorbeelden (eerste consolidatie + latere consolidatie incl. hypothese verlies > boekwaarde), 3 in_praktijk-aspecten, 3 vergelijkingsparen, 3 valkuilen.
- **`consolidatieverschil.json`** — 4 bouwstenen, 3 oorzaken (overpaid goodwill, onder-/overgewaardeerde activa, verwachte ongunstige resultaatsontwikkeling), 1 berekeningsmethode met cijfervoorbeeld, 2 in_praktijk-aspecten, 3 vergelijkingsparen, 3 valkuilen.

### Regel 2 — Berekenbaar concept verplicht numeriek voorbeeld

Alle records met `berekeningsmethode[]` bevatten een `concreet_voorbeeld` met scenario + berekening + resultaat:

| Record | Methode | Voorbeeld |
|---|---|---|
| `controlepercentage` | Controlepercentage in keten | M-80 %-A-60 %-B → controle% = 60 %, belang% = 48 % |
| `belangenpercentage` | Belangenpercentage in keten | Idem maar pro-rata vermenigvuldigend: 48 %, derden 52 % |
| `integrale-consolidatie` | Integrale stappen | M 80 %/D, EV D 300 op acquisitie/400 op afsluiting, intra-vord. 50, resultaat D 100 → derden balans 80, derden resultaat 20 |
| `evenredige-consolidatie` | Pro-rata opname | A 50 %/X, EV 600, omzet 1000, intra-verkoop 60/winst 10 → pro-rata 50 %, eliminatie 5 |
| `vermogensmutatiemethode` (eerste cons.) | Herwaardering + consolidatieverschil | ABC 20 % in DEF, aanschaffing 200, EV 600 → pro-rata 120 + consolidatieverschil 80 |
| `vermogensmutatiemethode` (latere cons.) | Pro-rata winst/verlies + plafond | Hyp 1: +300 winst; Hyp 2: −300 verlies; Hyp 3: verlies plafond op 2.600 |
| `consolidatieverschil` | Berekening + toerekening | M 100 %/D, prijs 1.000, EV 700, terrein +150 onder → consolidatieverschil 150 |
| `minderheidsbelangen` | Aandeel van derden | M 80 %/D, EV D 500 → derden balans 100; resultaat 100 → derden 20 |

Dit is een directe correctie van de v2-zwakte (alleen vermogensmutatie had cijfervoorbeelden).

### Regel 3 — Eén fenomeen, één record

- `minderheidsbelangen.json` bundelt zowel balanskant ('Belangen van derden') als resultatenrekening-kant ('Aandeel van derden in het resultaat') in één record met aparte velden — geen twee aparte records meer (v2-zwakte).
- Begrippen die nauw aansluiten bij elkaar zijn als `vergelijkingsparen` met expliciete verschil-tekst gelinkt (bv. controle ↔ exclusieve-controle ↔ gezamenlijke-controle ↔ invloed-van-betekenis ↔ controlepercentage).

### Regel 4 — Vrije-tekst-verwijzing = structurele verwijzing

Elke vermelding in vrije tekst van een ander record is ofwel in `vergelijkingsparen[]` opgenomen (met expliciete record-id), ofwel in `references[]` als wetstekst. Het 'edges[]'-veld wordt expliciet niet door v3 gevuld (apart pass volgens de prompt-instructie); de structurele verwijzingen leven in `vergelijkingsparen[]` en in de `references[]` van bouwstenen.

Voorbeelden van consistent toegepaste cross-linking:
- `controle ⇄ exclusieve-controle ⇄ gezamenlijke-controle ⇄ invloed-van-betekenis ⇄ controlepercentage ⇄ belangenpercentage`
- `integrale-consolidatie ⇄ evenredige-consolidatie ⇄ vermogensmutatiemethode ⇄ consolidatieverschil ⇄ minderheidsbelangen`
- `consolidatieverplichting ⇄ groottecriteria-consolidatie ⇄ groep-van-beperkte-omvang ⇄ vrijstelling-subconsolidatie ⇄ consolidatiekring`
- `consortium ⇄ horizontale-consolidatie ⇄ gemeenschappelijke-dochteronderneming`

### Regel 5 — Uniforme rijkheid binnen node-type

| node_type | Aantal records | Standaardvelden gerespecteerd |
|---|---|---|
| `begrip` | 11 | Allen: definitie + in_praktijk + vergelijkingsparen + valkuilen |
| `actor` | 4 | Allen: definitie + in_praktijk + vergelijkingsparen + valkuilen |
| `fenomeen` | 4 | Allen: definitie + bouwstenen + vergelijkingsparen + valkuilen |
| `regel` | 4 | Allen: main_rule + voorwaarden/uitzonderingen + vergelijkingsparen + valkuilen |
| `drempel` | 1 | main_rule + drempelwaarden (≥1) + vergelijkingsparen + valkuilen |
| `procedure` | 2 | verplichting + stappen (≥4) + in_praktijk + vergelijkingsparen + valkuilen |
| `methode` | 3 | doel + bouwstenen + berekeningsmethode + concreet_voorbeeld + vergelijkingsparen + valkuilen |

Alle 30 records bevatten minimum 2-3 van de "sterk aanbevolen" velden uit het v3-protocol.

## 4. Cross-bron synthese — voorbeelden

Records met `confidence: "inferred-from-aggregation"` synthesiseren over 2+ bronnen:

- **`controle.definitie`** — combineert WVV art. 1:14 (formele definitie) + CBN 2022/11 (operationele omschrijving) + CBN 2017/02 (gezamenlijke controle als variant).
- **`controlepercentage.definitie`** — synthese van CBN 2017/02 + CBN 2022/09 (ketenstructuren in voorbeeld 7).
- **`belangenpercentage.berekeningsmethode`** — bouwt op KB WVV art. 3:137 (logica derden) + CBN 2017/02 (ketenvoorbeeld).
- **`integrale-consolidatie.berekeningsmethode`** — aggregeert 5 KB WVV-artikelen tot één werkstroom.
- **`consolidatieverschil.oorzaken`** — drie oorzaken (goodwill, ondergewaardeerde activa, ongunstige verwachtingen) cross-bron geaggregeerd.
- **`consolidatieverplichting.main_rule`** — combineert WVV (basisplicht), CBN 2022/11 (toepassingsgebied), CBN 2022/09 (consortium-specifiek), CBN 2011/5 (consolidatiekring-aanvulling).

## 5. Schema-veld-gebruik (v1.2-velden)

| Veld | Gebruikt in (records) |
|---|---|
| `drempelwaarden[]` | 4 — exclusieve-controle, invloed-van-betekenis, geassocieerde-onderneming, groottecriteria-consolidatie |
| `oorzaken[]` | 1 — consolidatieverschil |
| `tijdlijn[]` | 1 — eerste-consolidatie |
| `vergelijkingsparen[]` | 30 — elk record minstens 1 paar |
| `berekeningsmethode[]` | 8 — alle methode-records + helpers + consolidatieverschil + minderheidsbelangen |
| `in_praktijk[]` | 27 — bijna elk substantieel record |
| `valkuilen[]` | 27 — bijna elk record |
| `voorbeeld_inline` | 5 — horizontale-consolidatie, gemeenschappelijke-dochteronderneming, step-acquisition, dochteronderneming, gezamenlijke-controle |
| `bouwstenen[]` | 10 — controle, integrale-consolidatie, evenredige-consolidatie, vermogensmutatiemethode, consolidatieverschil, consolidatiekring, wijziging-consolidatiekring, ifrs-consolidatieraamwerk, step-acquisition, horizontale-consolidatie |
| `voorwaarden[]` | 6 — moedervennootschap, gemeenschappelijke-dochteronderneming, gezamenlijke-controle, exclusieve-controle, vrijstelling-subconsolidatie, uniforme-waarderingsregels-consolidatie |
| `uitzonderingen[]` | 2 — consolidatieverplichting, uniforme-waarderingsregels-consolidatie |
| `stappen[]` (in procedure) | 2 — intragroep-eliminaties (6 stappen), horizontale-consolidatie (5 stappen) |
| `linked_anchors[]` | 30 — elk record |
| `references[]` op definitie of main_rule | 30 — elk record |

Geen veld `voorbeeld_inline` op de drie hoofdmethodes — bewust: voor methode-records is `berekeningsmethode[].concreet_voorbeeld` de schema-correcte locatie van numerieke uitwerkingen (Regel 2). Het bredere `voorbeeld_inline` is voor begripsrecords gebruikt waar een illustratief scenario het concept dekt zonder dat er een methode wordt toegepast (bv. gemeenschappelijke-dochteronderneming, step-acquisition).

## 6. Confidence-distributie

Op claim-niveau (gemiddeld over alle blok-objects in alle records, schatting):

| confidence | %-aandeel | Voorbeeldgebruik |
|---|---|---|
| `grounded` | ~75 % | Direct uit één KB WVV-artikel of één CBN-secties traceerbaar |
| `inferred-from-aggregation` | ~22 % | Synthese over 2+ chunks/bronnen (typisch ketenvoorbeelden, definitie-synthese) |
| `inferred` | ~3 % | Redenering buiten chunk-inhoud (typisch in valkuilen of bij IFRS-overzichten) |

Geen claim zonder `_provenance.inputs` met chunk_id(s).

## 7. Bron-voorstellen toegevoegd

Eén nieuwe entry in `data/extractie/_bron_voorstellen.json`:

- **PO 1.4, anchor 1.4.II.A** — herbevestiging van de v2-bevinding dat de IFRS 3 / 10 / 11 / 12 primaire tekst niet in het corpus zit. Het v3-record `ifrs-consolidatieraamwerk.json` is bewust een **anker-record** met `confidence: "inferred"` voor de IFRS-specifieke claims, en de gap wordt expliciet in zijn valkuilen-veld gemeld.

## 8. Dangling-references gelogd

`data/quality_checks/1.4/dangling-references-v3-2026-05-15.json` bevat 9 items:

| Term | Oordeel |
|---|---|
| verbonden vennootschappen | Voldoende vermeld — eigen record in PO 1.x aanbevolen |
| centrale leiding | Voldoende vermeld — overlap met `consortium` |
| going-concernveronderstelling | Bewust uit scope — PO 1.1 |
| common control transactions | Voldoende vermeld — record bij latere corpus-uitbreiding |
| buitenlandse dochter — omrekening vreemde valuta | Bewust uit scope — geavanceerd |
| geconsolideerde belastingen | Bewust uit scope — geavanceerd |
| groepsbijdrage (CBN 2019/06) | Bewust uit scope — PO 1.7 fiscaal |
| transfervergoedingen (CBN 2010/21) | Bewust uit scope — sectorspecifiek |
| tijdelijke handelsvennootschap | Bewust uit scope — buiten KB WVV titel 2 |

## 9. Aandachtspunten / observaties

1. **IFRS-context** — De huidige bundle-samenstelling voor PO 1.4.II (anchors II, II.A, II.B, II.C, II.D) is duidelijk arm aan primaire IFRS-tekst. Vier van de zes II-anchors zijn vrijwel uitsluitend gedekt door BEGAAP-content. Aanbeveling: hoge prioriteit aan importeren van IFRS 3, IFRS 10, IFRS 11, IFRS 12 (Nederlandstalig via EUR-Lex / Verordening 1126/2008 met opvolgers).

2. **Cijferzakboekje-koppeling** — De groottecriteria (WVV art. 1:24, art. 1:26) worden periodiek geïndexeerd. Records bevatten cijfers met expliciete `confidence: "grounded"` voor de actuele cijfers in CBN 2017/15 en CBN 2024/07, maar verwijzen voor het examen door naar het Cijferzakboekje. Aanbeveling: bij elke release van het Cijferzakboekje een aangepaste check op de groottecriteria-records.

3. **Common control transactions** — CBN 2017/15 verschijnt in de bundles maar grotendeels via één sectie (over groottecriteria). De boekhoudkundige verwerking zelf van common-control-transacties (geen nieuwe goodwill, doorzetten historische cijfers) is in de huidige extractie als bouwsteen van `wijziging-consolidatiekring` opgenomen maar verdient bij volgende iteratie een eigen record, mits bijkomende chunks beschikbaar zijn.

4. **Stappen[]-shape** — Voor procedure-records (`intragroep-eliminaties`, `horizontale-consolidatie`) is het optionele `actor`-veld per stap gebruikt om de "wie doet wat"-toetsing mogelijk te maken. Dit is een nieuwe v1.2-mogelijkheid die in alle procedure-records consistent is toegepast.

5. **Edges[]** — Conform de prompt-instructie ("NIET edges produceren — apart pass na alle records") werd dit veld leeg gelaten. Een toekomstige edge-pass zou kunnen putten uit de `vergelijkingsparen[]` (al expliciet gestructureerd) en uit de cross-record-verwijzingen die nu in `references[]` zitten.

6. **Geen overlap met archief geconsulteerd** — Conform de taakopdracht is de extractie volledig "from scratch" uitgevoerd; v1/v2-bestanden in `data/concept_records/_archive/` zijn niet geopend tijdens deze run.

## 10. Klaar-criteria — check

- [x] 25+ concept-records in `data/concept_records/*.json` (flat) — **30**
- [x] Elk record heeft `linked_anchors[]` + schema 1.2-conform
- [x] Centrale methodes hebben `concreet_voorbeeld` — integrale + evenredige + vermogensmutatie met numerieke uitwerking
- [x] `v3-extraction-rapport.md` geschreven
- [x] Géén commit (mens reviewt eerst)

---

Einde rapport.
