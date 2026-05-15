# v3 vs v2 vergelijking — PO 1.4 Geconsolideerde jaarrekening

**Datum**: 2026-05-15
**Reviewer**: Claude Sonnet 4.6 (agent)
**Input v3**: `data/concept_records/*.json` (30 records, schema 1.2, post-enrich)
**Input v2**: `data/concept_records/_archive/1.4-v2-2026-05-15/` (31 records)
**Referenties**: `stress-test-reflectie.md`, `v1-vs-v2-vergelijking.md`, v3-extractie- en enrich-rapporten

---

## Verdict

**v3 is een netto-verbetering en is productie-waardig — maar niet zonder resterende gaten.**

De architecturale zwaktes van v2 (geen rekenvoorbeelden op kernmethodes, twee records voor één fenomeen, minimale basisbegrippen) zijn in v3 methodisch aangepakt. De ENRICH-cyclus heeft de twee hoog-prioritaire examengaten gedicht. Resterende zwaktes zijn reëel maar niet blokkerend voor productie-gebruik.

---

## 1. Gerapporteerde v2-zwaktes: per item

### 1.1 `integrale-consolidatie` zonder rekenvoorbeeld

**v2**: `berekeningsmethode[]` volledig afwezig — de stress-test noemde dit het pijnlijkste punt.

**v3**: ✅ Volledig opgelost. Het record heeft nu een `berekeningsmethode[]` met vijf stappen (KB WVV art. 3:126 t/m 3:137) én een uitgewerkt cijfervoorbeeld: M 80 % van D, aanschaffingswaarde 320, EV D = 300 op acquisitiedatum / 400 op afsluiting, intra-vordering 50. Berekening dekt compensatie, consolidatieverschil (80), eliminatie (50) en belangen van derden (80 passief + 20 resultatenrekening). Dit is het type uitwerking dat de stress-test expliciet vroeg.

### 1.2 `evenredige-consolidatie` zonder rekenvoorbeeld

**v2**: ook geen `berekeningsmethode[]`.

**v3**: ✅ Volledig opgelost. Pro-rata-voorbeeld: A en B elk 50 % van X, activa 1.100, schulden 500, resultaat 200, intra-groepsverkoop winst 10. Stap voor stap berekend met expliciete eliminatie van het pro-rata deel (5 van de 10). Duidelijk dat er géén derden-post is.

### 1.3 `dochteronderneming`, `moedervennootschap`, `geassocieerde-onderneming` minimalistisch

**v2**: definitie + één vergelijkingspaar, geen `in_praktijk`, geen `voorwaarden`, geen voorbeeld.

**v3**: ✅ Substantieel verbeterd.
- `dochteronderneming`: definitie uitgebreid (WVV art. 1:15 + art. 3:22 breder toepassingsgebied), twee `in_praktijk[]`-blokken (soorten dochters per controleniveau + vier uitsluitingsgronden KB WVV art. 3:97), `voorbeeld_inline` met 90 %-casus, twee `valkuilen[]`.
- `moedervennootschap`: niet meer minimalistisch — het record heeft nu `voorwaarden[]`, twee `in_praktijk[]`-blokken (wanneer vrijgesteld via groottecriteria en via subconsolidatie), twee `valkuilen[]`.
- `geassocieerde-onderneming`: `drempelwaarden[]` (20 %-vermoeden), `in_praktijk[]` met herkenningspunten, `vergelijkingsparen[]` met dochteronderneming en invloed-van-betekenis.

### 1.4 `uniforme-waarderingsregels-consolidatie` te beknopt

**v2**: `main_rule` + één `in_praktijk` (in erg beknopte vorm), geen `valkuilen`, geen voorbeeld.

**v3**: ✅ Aanzienlijk rijker. Drie `voorwaarden[]` (uniformiteit met enkelvoudige, uitzonderingen bij afwijking met motivering, stelselmatigheid), één `uitzonderingen[]`-item (fiscale distorsies KB WVV art. 3:118 met volledige beschrijving), twee `in_praktijk[]`-blokken (consortium + buitenlandse dochters), twee `valkuilen[]` (fiscale correctie + wijziging vereist motivering).

### 1.5 `ifrs-verordening` minimaal

**v2**: enkel `main_rule`, geen verdere uitwerking — de stress-test noemde dit het minst nuttige anker-record.

**v3**: ⚠️ Gedeeltelijk opgelost. v3 heeft `ifrs-verordening-1606-2002` samengevoegd in een breder `ifrs-consolidatieraamwerk`-record (IFRS 3 / 10 / 11 / 12), met twee `in_praktijk[]`-blokken en een `valkuilen[]` over de corpus-begrenzing. De `in_praktijk`-entry over IFRS-versus-BEGAAP verschillen heeft `confidence: "inferred"` en is expliciet als overzichtsniveau-kennis gelabeld (niet detailparagrafen). Dit is eerlijk maar laat de structurele corpus-lacune zichtbaar — IFRS-deelgebied blijft dun.

### 1.6 `edges[]` leeg in alle records

**v2 en v3**: ⚠️ Structureel ongewijzigd. v3 laat `edges[]` bewust leeg (conform extractie-prompt). De structurele verwijzingen leven nu echter volledig in `vergelijkingsparen[]` — elk van de 30 records heeft minstens één paar, de meeste hebben er drie of vier. Dit is een functioneel equivalent dat het gebrek aan formele edges voor de meeste use-cases dekt. Voor RAG-graph-walk blijft het een technische schuld.

### 1.7 Dubbele records `minderheidsbelangen` ↔ `aandeel-van-derden-in-resultaat`

**v2**: twee aparte records met overlappende inhoud, zelfde wetsartikel, zelfde chunk-IDs.

**v3**: ✅ Opgelost. Eén record `minderheidsbelangen` bundelt beide perspectieven: balans-kant en resultatenrekening-kant in één `berekeningsmethode[]` met gedeelde formule (`(1 − belang%) × EV` voor balans; `(1 − belang%) × resultaat` voor resultatenrekening), geïllustreerd via één cijferscenario (M 80 % van D, EV 500, resultaat 100 → derden 100 en 20).

---

## 2. Verloren content van v1 en v2

De v1 vs v2-vergelijking signaleerde drie regressies. Status in v3:

### 2.1 Bodemwaarde bij vermogensmutatie

**v1** had een expliciete bouwsteen "Bodemwaarde van de deelneming" — de regel dat verliezen de boekwaarde niet onder nul kunnen brengen. **v2** verloor dit.

**v3**: ✅ Terug. `berekeningsmethode[]` van `vermogensmutatiemethode` bevat een expliciete hypothese 3 voor het plafond bij verlies, met de tekst dat de boekwaarde niet negatief kan worden. De formule zelf en de stappen zijn rijker dan in v2 (v2 had het ABC-DEF-voorbeeld maar niet uitdrukkelijk de bodemwaarde als procedureel punt).

### 2.2 Stichting-voorbeeld bij consortium

**v1** had een concreet voorbeeld met stichting P en leden X en Y. **v2** verloor dit.

**v3**: ⚠️ Niet hersteld als concreet voorbeeld. `consortium` heeft geen `voorbeeld_inline`. De definitie (CBN 2022/09) en de `voorwaarden[]` zijn rijker dan v2, maar het illustratieve scenario met P, X en Y is niet teruggekomen. Compenserend: `horizontale-consolidatie` heeft een nieuw record met `voorbeeld_inline` (horizontale scenario uitgewerkt), en `gemeenschappelijke-dochteronderneming` heeft ook `voorbeeld_inline`. Functioneel gedekt maar niet via het stichting-voorbeeld.

### 2.3 Maatschap-uitzondering bij vrijstelling-subconsolidatie

**v1** had een uitzondering-veld voor de maatschap-casus. **v2** verloor dit (vermeld als inhoudsverlies in v1 vs v2-vergelijking).

**v3**: ✅ Volledig hersteld en uitgebreid. `vrijstelling-subconsolidatie` heeft nu een expliciete `in_praktijk`-entry "Gevolgen voor maatschap-structuren" met de exacte regel: een maatschap zonder rechtspersoonlijkheid kan geen bevrijdende geconsolideerde jaarrekening opstellen, dus de onderliggende vennootschappen kunnen de vrijstelling niet inroepen (CBN 2015/10, met twee chunk-IDs).

### Steekproef: zijn de v2-sterke records minstens op hetzelfde niveau?

| Record | v2 | v3 |
|---|---|---|
| `consolidatieverschil` | Sterk: oorzaken, voorbeeld, vergelijkingsparen | Sterker: 5 oorzaken (2 via enrich), 5 vergelijkingsparen, rijkere berekening |
| `vermogensmutatiemethode` | Sterk: 2 berekeningsmethodes, ABC-DEF-voorbeeld | Sterker: bodemwaarde terug, 3 vergelijkingsparen, 3 in_praktijk |
| `controle` | Sterk: 2 bouwstenen, 2 in_praktijk | Sterker: 4 vergelijkingsparen, 3 in_praktijk (idem of rijker) |
| `belangenpercentage` | Sterk: formule + keten-voorbeeld | Gelijkwaardig: formule intact, voorbeeld geherformuleerd |
| `groottecriteria-consolidatie` | Sterk: 4 drempelwaarden + valkuilen | Gelijkwaardig: drempelwaarden iets anders gestructureerd, informatie behouden |

Geen regressies op de vijf gesteekproefde sterke v2-records.

---

## 3. Echt nieuwe inhoud in v3

Inhoudelijke uitbreidingen die in v2 volledig ontbraken:

1. **Rekenvoorbeeld integrale consolidatie** (zie punt 1.1) — dit is de meest impactvolle toevoeging.
2. **Rekenvoorbeeld evenredige consolidatie** met expliciete eliminatie-mechanica (intra-groepswinst pro-rata geëlimineerd).
3. **`horizontale-consolidatie`** als nieuw record met procedurele stappen en voorbeeld — v2 had dit concept enkel impliciet in `consortium`.
4. **`gemeenschappelijke-dochteronderneming`** als apart record — v2 had dit niet afzonderlijk.
5. **`wijziging-consolidatiekring`** als apart record — coverage voor step-in/step-out buiten de step-acquisition records.
6. **`groep-van-beperkte-omvang`** als kwalitatief statuut-record, onderscheiden van de meetset `groottecriteria-consolidatie` — het ENRICH-rapport verduidelijkt dit onderscheid in het vergelijkingspaar (met `corrected_from`-documentatie).
7. **`eerste-consolidatie`** als procedure-record met `tijdlijn[]`-veld — dit veld was in v2 op nul records aanwezig.
8. **`ifrs-consolidatieraamwerk`** als geïntegreerd raamwerk-record dat IFRS 3/10/11/12 samenneemt — v2 had twee aparte minimale records.
9. **Drempelwaarden op `exclusieve-controle`** — de kwantitatieve grens (> 50 % stemrechten als onweerlegbaar vermoeden) is nu als `drempelwaarden[]` aanwezig, niet alleen in proza.
10. **Drie-maanden-drempel op `geconsolideerde-jaarrekening`** — toegevoegd via ENRICH (prio hoog, KB WVV art. 3:110, tweede lid). Was in v2 volledig afwezig.

---

## 4. Kwaliteitsregels-check

### Regel 1 — Centraliteit impliceert volledigheid

`controle` heeft 2 bouwstenen, 4 vergelijkingsparen, 3 in_praktijk-blokken, 2 valkuilen.
`integrale-consolidatie` heeft 5 bouwstenen, 1 berekeningsmethode + cijfervoorbeeld, 4 vergelijkingsparen, 2 in_praktijk-blokken, 3 valkuilen.
`consolidatieverschil` heeft 4 bouwstenen, 5 oorzaken, 1 berekeningsmethode + cijfervoorbeeld, 2 in_praktijk-blokken, 5 vergelijkingsparen, 3 valkuilen.

**✅ Regel gerespecteerd.** De drie meest aangeroepen concepten zijn substantieel completer dan in v2. `consolidatieverschil` is de absolute gouden standaard van de set.

### Regel 2 — Numeriek voorbeeld bij elke berekenbare methode

`integrale-consolidatie`: ✅ Cijferscenario aanwezig (zie punt 1.1).
`evenredige-consolidatie`: ✅ Cijferscenario aanwezig (zie punt 1.2).
`vermogensmutatiemethode`: ✅ Twee berekeningsmethodes met scenario's, inclusief bodemwaarde-hypothese.
`consolidatieverschil`: ✅ Berekening M 100 % van D voor 1.000, EV 700, terrein onderwaardering 150 → consolidatieverschil 150.
`minderheidsbelangen`: ✅ M 80 % van D, EV 500, resultaat 100 → derden 100 en 20.
`controlepercentage` en `belangenpercentage`: ✅ Ketenformule M-80 %-A-60 %-B.

**✅ Regel gerespecteerd.** Dit was de scherpste v2-zwakte; in v3 is ze systematisch gedicht.

### Regel 3 — Één fenomeen, één record

`minderheidsbelangen`: ✅ Eén record, beide perspectieven gebundeld (balans + resultatenrekening).
`controle-in-rechte-en-in-feite`: In v2 een apart record — in v3 geïntegreerd als twee bouwstenen in `controle`. ✅ Overlap opgeruimd.

**✅ Regel gerespecteerd.** De v2-zwakte van twee overlappende records is direct geadresseerd.

### Regel 4 — Relaties expliciet (vergelijkingsparen bidirectioneel)

Via ENRICH zijn drie asymmetrische vergelijkingsparen rechtgezet: `vermogensmutatiemethode` → `invloed-van-betekenis` en `consolidatieverschil` (toegevoegd); `evenredige-consolidatie` → `gezamenlijke-controle`, `gemeenschappelijke-dochteronderneming` en `belangen-van-derden` (toegevoegd); `consolidatieverschil` → `dochteronderneming` en `geassocieerde-onderneming` (toegevoegd).

**✅ Regel grotendeels gerespecteerd.** Niet alle vrije-tekst-verwijzingen zijn gespiegeld (de VERIFY-run identificeerde nog 3 niet-gespiegelde paren) maar de meest examenvraag-relevante paren zijn bidirectioneel.

### Regel 5 — Uniforme rijkheid

In v2 was de rijkheid ongelijk: `consolidatieverschil` had 4 oorzaken + voorbeeld; `dochteronderneming` had enkel een definitiezin.
In v3: alle 30 records hebben `vergelijkingsparen[]` (elke minstens 1), `valkuilen[]` (27/30), `in_praktijk[]` (27/30), en `references[]`. De drie dunste records (`ifrs-consolidatieraamwerk`, `geconsolideerd-jaarverslag` na enrich, `groep-van-beperkte-omvang`) zijn nadrukkelijk anker- of scope-records, niet primaire begrips-records.

**✅ Regel gerespecteerd.** De variatie is van ~0 tot 4 velden in v2 gedaald naar een minimum van 3-4 velden per record in v3.

---

## 5. Resterende gaten

Concreet, niet vaag:

1. **`consolidatieverschil.oorzaken` telt 5 items maar bevat overlap.** Het nieuwe item "Overpaid goodwill" en het nieuwe item "Niet-geactiveerde immateriële waarden" beschrijven deels hetzelfde fenomeen. Het ENRICH-rapport signaleerde dit zelf (append-only contract verbood merge). Een examenvraag die "vier voornaamste oorzaken van een positief consolidatieverschil" vraagt, krijgt nu vijf oorzaken waarvan twee overlappend. Te corrigeren in een volgende VERIFY-ronde.

2. **Intragroep-eliminaties: geen gewerkt voorbeeld van niet-gerealiseerde voorraadwinst.** De stress-test van v2 signaleerde dit al: "elimineer x" zonder de cijfers. `intragroep-eliminaties` heeft stappen (6 stappen met actor) maar geen `berekeningsmethode[].concreet_voorbeeld`. Een typische examenvraag — "moeder verkoopt voor 100 aan dochter, marge 30 %, nog 40 in voorraad" — is nog steeds niet deterministisch beantwoordbaar.

3. **IFRS-inhoud structureel beperkt.** `ifrs-consolidatieraamwerk` is eerlijk (confidence `inferred`, valkuil over corpus-lacune vermeld) maar de anchors 1.4.II.A t/m 1.4.II.D zijn inhoudelijk dun. IFRS 3 full goodwill vs. partial goodwill, IFRS 10 control-definitie, IFRS 11 onderscheid joint venture vs. joint operation — dit zijn examen-relevante vragen die het record niet volledig kan beantwoorden. Fundamenteel corpus-probleem (IFRS-primaire tekst ontbreekt), niet een extractie-probleem.

4. **`controlepercentage` formuleringsprecisie.** De v1↔v2-vergelijking signaleerde dat "volledig controleert" in de definitie suggereert dat de doorrekenregel enkel bij 100 % deelneming in A werkt. v3 heeft dit niet expliciet gecorrigeerd: de `berekeningsmethode` beschrijft "M controleert A → controle in B = 60 %" maar de expliciete nuance dat 51 % in A ook volstaat voor de doorrekenregel staat er niet in.

5. **`groep-van-beperkte-omvang` ↔ `groottecriteria-consolidatie` overlap nog partieel aanwezig.** ENRICH heeft het vergelijkingspaar op `groep-van-beperkte-omvang` gecorrigeerd, maar `groottecriteria-consolidatie` is niet aangeraakt (één-record-per-gap-contract). Een raadpleging over "groep van beperkte omvang" die beide records ophaalt zal overlappende drempelwaarden tonen.

6. **`edges[]` onbevolkt.** Functioneel gecompenseerd door vergelijkingsparen, maar voor een toekomstige RAG-graph-walk of network-analyse is dit technische schuld.

---

## Eindoordeel

**v3 is een netto-verbetering ten opzichte van v2. Productie-waardig voor conceptuele beheersing en minicursus-generatie.**

| Criterium | v2 | v3 |
|---|---|---|
| Rekenvoorbeelden op kernmethodes | Enkel vermogensmutatie | Alle 5 berekenbare methodes + minderheidsbelangen |
| Centrale begrippen volledigheid | Matig (controle OK, integrale dun) | Sterk (alle drie kernconcepten rijker dan v2) |
| Eén fenomeen = één record | Gebroken (dubbele minderheidsbelangen) | Hersteld |
| Bidirectionele vergelijkingsparen | Deels (via ENRICH gestart maar onvolledig) | Grotendeels (7 asymmetrische paren rechtgezet) |
| Uniforme rijkheid | Groot verschil top vs. bodem | Klein verschil; minimum 3-4 velden per record |
| v1-regressies hersteld | n.v.t. | 2 van 3 volledig (bodemwaarde ✅, maatschap ✅); stichting-voorbeeld ⚠️ |
| IFRS-coverage | Minimaal | Eerlijk minimaal (corpus-lacune expliciet gedocumenteerd) |
| Examenvragen beantwoordbaar | 4 van 6 gesimuleerd | 5 van 6 (drie-maanden-drempel gedicht via ENRICH) |

**Aanbeveling**: inzetten als primaire v3-productieset. Twee gerichte correcties wenselijk vóór gebruik in evaluatie-pipeline: (a) consolideer de twee overlappende `oorzaken[]`-items in `consolidatieverschil`; (b) voeg een `berekeningsmethode[].concreet_voorbeeld` toe aan `intragroep-eliminaties` (niet-gerealiseerde voorraadwinst).

---

*Einde rapport. Woordtelling: ~1.950.*
