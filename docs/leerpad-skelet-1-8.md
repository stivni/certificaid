# Leerpad-skelet PO 1.8 — Analytische boekhouding en management accounting

**Status**: voorstel (2026-05-30)
**Volgende stap (na sparring)**: voorbeeldgroep `productie-mock` (nieuw, productie-context met kostendragers) in `data/voorbeeldgroepen/` + scripts per leerstuk in `data/leerstukken/`.

---

## 1. Programma-analyse

### Officiële taken en doelstellingen

PO 1.8 heeft **één hoofdtaak** met **11 doelstellingen** — een ongewoon breed pakket dat onder één taak-label is gegroepeerd:

> **Taak 1.8.1**: *Analyseren van de financiële situatie van een onderneming* (anchor-rol)

| Doel | Tekst (kort) | Anchor-rol |
|---|---|---|
| 1.8.1.1 | Arbeidskosten + beloningssystemen + arbeidstijdmeting verwerken | context |
| 1.8.1.2 | Kostenberekening voor alle soorten ondernemingen (incl. diensten) | context |
| 1.8.1.3 | Gemiddelde + marginale kosten gedetailleerd analyseren | context |
| 1.8.1.4 | Kostprijsinformatie organiseren + boekhoudkundig verwerken (IT-tool) | context |
| 1.8.1.5 | Boekhoudplan + boekingen specifiek voor management accounting gebruiken | context |
| 1.8.1.6 | Verschillen berekenen en analyseren | context |
| 1.8.1.7 | Het budget herzien | context |
| 1.8.1.8 | Rendabele/onrendabele segmenten identificeren + voorstellen voor reductie | context |
| 1.8.1.9 | Een of meer managementsbeslissingen aanbevelen | context |
| 1.8.1.10 | Onderneming adviseren volgens aangenomen strategie | context |
| 1.8.1.11 | Alle budgetten opstellen (incl. investerings- en managementbegroting) | context |

**Vereist niveau**: *integratie* (volgens PO-metadata `niveau: integratie`) — hoger dan "toepassen" (1.4). Dit signaleert dat het PO bewust *over* meerdere kennisvelden draait: kostprijsmethodes + budget + variantieanalyse + advies, samen tot één coherente managerial-toolkit. Integratie-niveau impliceert dat de stagiair niet alleen elke techniek apart kent, maar ze gericht inzet voor *één* beslissingsvraag.

**Kenniselementen** (zes hoofdsecties): `1.8.I` Presentatie · `1.8.II` Kostencomponenten (materialen, arbeid, overige) · `1.8.III` Methodes (full · direct · standaard · BEP · marginale · ABC) · `1.8.IV` Boekhoudkundige organisatie · `1.8.V` Budgetbeheer (kader) · `1.8.VI` Budget + variantieboekhouding.

### Cruciale observatie: het PO is een *toolkit*, geen procedure

In tegenstelling tot 1.4 (één opmaak-procedure met varianten) is 1.8 een **breed methodologisch landschap** waar de stagiair leert *kiezen* welk instrument voor welke vraag. De officiële doelstellingen springen van techniek (1.8.1.3 marginale kost) naar boekhoudkundige verwerking (1.8.1.5 klasse 9) naar advies (1.8.1.10 strategisch advies). Het verbindende thema is: *kostprijs- en margebeeld bouwen om beslissingen te onderbouwen*.

Tweede cruciale observatie: **analytische boekhouding is niet wettelijk verplicht**. CBN-advies 132/7 (bevestigd in concept-record `analytische-boekhouding`) erkent meerdere geldige varianten, maar de vorm is *vrij*. Dit kleurt het hele PO — er is geen "juiste" methode; keuze volgt het doel. Dit is een rode draad voor de minicursus.

### Kern vs rakend

- **Kern (uniek aan 1.8)**: kostprijsberekening + kostenmodel (klassen 8/9, registratie­systemen) + kostprijsmethoden (full · direct · ABC · standaard) + break-even/marginale analyse + budget + variantieanalyse
- **Rakend met andere PO's**:
  - **PO 1.1 (Algemene boekhouding)** — klassen 6X (kosten naar aard) als bron; spiegelrekeningen-mechaniek raakt dubbele boekhouding
  - **PO 1.9 (Financiële analyse)** — beide bouwen op kosten/marges, maar 1.9 vertrekt vanuit *de jaarrekening* (ex-post extern), 1.8 vanuit *cost-data* (intern, vaak ex-ante). Risico: overlap in "marge-analyse" en "rentabiliteitsanalyse per segment" (doel 1.8.1.8)
  - **PO 4.0 (Cabinet management)** — KPI's, dashboards, boordtabel (kenniselement `1.8.III.C.3`) raken de management-side van 4.0
  - **PO 1.5 (IFRS)** — IAS 2 voorraadwaardering bepaalt mee hoe vaste overhead wordt gealloceerd (volume-correctie, materiële varianties → pro-rata voorraad/KGV)
  - **PO 2.x (Fiscaliteit)** — niet direct rakend, maar kostenberekening voor diensten-ondernemingen (1.8.1.2) kan in een fiscale aangifte-context terugkomen

---

## 2. Voorbeeldexamen-patronen

### Gap: geen voorbeeldexamen-vragen geclassificeerd voor PO 1.8

Check van `data/programma/examen_vragen/_programmaonderdeel_classificatie.json` op 2026-05-30 vindt **geen enkele examenvraag** met PO 1.8 in `programmaonderdelen`. Twee vragen noemen "analyse" of "budget", maar zijn beide naar 1.7 (interne controle) geclassificeerd:

- `2013-1-vr10` — analytische test door interne controleafdeling → 1.7
- `2013-1-vr11` — belang van een budget voor interne controle → 1.7

Er bestaat **geen `content/studiemateriaal/1-8/voorbeeldexamenvragen.md`**. De directory bevat alle PO's behalve 1.8 en 1.10+ (`po-1.1.md` t/m `po-1.7.md`, `po-1.9.md`, dan 2.x).

**Conclusie**: voorbeeldexamen-bron ontbreekt voor dit PO. Het skelet steunt op:

1. Het officiële programma (taken/doelstellingen/kenniselementen) — de autoritaire scope
2. De vier bestaande themafiches (`analytische-boekhouding-stelsel`, `kostprijsmethoden`, `break-even-en-marginale-analyse`, `budget-en-variantieanalyse`) — al gestructureerd door iemand met examenintuïtie
3. De 11 PO-1.8-tagged concept-records — al pedagogisch gefilterd

**Implicaties voor §4 minicursus**:
- §4 "Examen-radar" kan **niet** een tabel met patronen leveren zoals voor PO 1.4. Voorstel: vervang door een sectie "**Examen-verwachting (heuristisch)**" die expliciet markeert dat geen voorbeeldexamens beschikbaar zijn, en die op basis van de themafiches + integratie-niveau-status voorspelt welk type vragen waarschijnlijk is (begrip + kleine berekening + interpretatie + advies — geen volledige kostprijs- of budget-uitwerking).
- Bij latere vrijgave van examenmateriaal: minicursus en eventueel leerstuk-scripts updaten (Stap 5 in `leerstuk-procedure.md`).

### Heuristische examenverwachting

Op basis van *integratie*-niveau + breed scope + de praktijk-aanpak van de ITAA voor andere management-onderwerpen, verwachten we eerder:

| Vermoed type | Onderbouwing |
|---|---|
| Begripsvraag "verschil X vs Y" (full vs direct, budget vs forecast, BEP-eenheden vs -omzet) | Klassiek voor breed-pakket-PO's; analoog aan 1.4 consolidatieverschil-vraag |
| Mini-berekening contributiemarge / BEP / variantie-decompositie | Past in een 30-minuten-vak en toetst integratie van formule + interpretatie |
| Case "welke methode kies je en waarom" (kort) | Sluit aan bij doelstelling 1.8.1.9 (managementsbeslissing aanbevelen) |
| Eventueel: identificatie verlieslatend segment (doel 1.8.1.8) | Past bij accountancy-praktijk |

Verzin **geen** concrete vragen — dit is heuristiek, geen voorbeeldexamen.

---

## 3. Leerstuk-voorstel

**Vier leerstukken**, één-op-één gespiegeld op de vier bestaande themafiches. De cluster-structuur is door de themafiche-auteur al pedagogisch gevalideerd (vier sub-clusters die elkaar niet overlappen) en de stagiair vindt elk leerstuk natuurlijk terug via zijn themafiche-kapstok.

Granulariteits-overweging: had je dit kunnen splitsen in 5-7 leerstukken? Ja — "Hoe registreer je analytische boekhouding" (1.8.IV) kon als 5e apart. Maar het stuk is sterk verweven met "Wat is analytische boekhouding" (klassen 8/9 zijn allebei *kader* én *registratie*) en past beter als sub-sectie van leerstuk 1. Stelregel "eerder samen dan splitsen" toegepast.

### Leerstuk 1 — `wat-is-analytische-boekhouding`

- **Vraag**: Wat is analytische boekhouding, waarom doe je het, en hoe registreer je ze naast de algemene boekhouding?
- **Type**: entry + kader-fiche
- **Gedekte doelstellingen**: 1.8.1.4 (organiseren + boekhoudkundig verwerken), 1.8.1.5 (boekhoudplan management accounting), gedeeltelijk 1.8.1.1 (kostentypologie + arbeid-deel)
- **Gedekte kenniselementen**: 1.8.I (Presentatie) · 1.8.II (Kostencomponenten — kort, met doorklik voor detail) · 1.8.IV (Boekhoudkundige organisatie + registratiesystemen)
- **Gedekte concepten**: `analytische-boekhouding` (hoofdconcept) + indirect: `bedrijfskosten`, `personeelskosten`
- **Rationale**: De stagiair moet eerst snappen *wat* het is + *waarom* (vrij keuze, niet wettelijk) + *hoe het zich verhoudt tot de algemene boekhouding* (klassen 8/9, spiegelrekeningen) vóór hij kostprijsmethodes of budgetten kan plaatsen. Klassen 8/9, drie registratiesystemen en kostentypologie horen pedagogisch in één beweging — het is allemaal "het stelsel". Themafiche `analytische-boekhouding-stelsel` is de natuurlijke kapstok.

### Leerstuk 2 — `kostprijsmethoden-kiezen`

- **Vraag**: Welke kostprijsmethode kies je wanneer, en hoe pak je elk van de vier aan (full · direct · ABC · standaard)?
- **Type**: techniek-fiche (zwaarste leerstuk van het pakket — vier methodes naast elkaar met formules + mini-cases)
- **Gedekte doelstellingen**: 1.8.1.2 (kostprijs voor alle ondernemingen incl. diensten), 1.8.1.4 (kostprijsmodel organiseren), 1.8.1.5 (boekingen managementboekhouding)
- **Gedekte kenniselementen**: 1.8.III.A (volledige kosten) · 1.8.III.B (gedeeltelijke kosten — direct + marginal) · 1.8.III.C (voorafbepaalde kosten — standaard, deels) · 1.8.III.F (ABC) · 1.8.IV.B.1 (effect van methode op voorraadwaardering)
- **Gedekte concepten**: `kostprijsmethoden` (keuze-kader) + `full-costing` + `direct-costing` + `activity-based-costing` + `standaardkostenmethode` (basis-introductie; verdieping in leerstuk 4)
- **Rationale**: De vier methodes vragen om naast-elkaar-uitleg met vergelijkingsmatrix, beslisboom en doorgewerkte mini-case per methode op dezelfde voorbeeldgroep. Splitsen in vier leerstukken-per-methode breekt de essentie ("geen methode is intrinsiek juist — keuze volgt doel") en verdubbelt de voorbeeld-set. Mag tot ~3500-4000 woorden lopen omdat het vier technieken integreert; valt onder "hoe"-uitzondering in leerstuk-schrijfregels (tot 4500). Themafiche `kostprijsmethoden` is de kapstok.

### Leerstuk 3 — `break-even-en-marginale-beslissing`

- **Vraag**: Hoe gebruik je break-even-analyse en marginale analyse om concrete beslissingen te onderbouwen (volume, special order, make-or-buy, knelpunt, productmix)?
- **Type**: techniek + beslissingsfiche
- **Gedekte doelstellingen**: 1.8.1.3 (gemiddelde + marginale kosten), 1.8.1.8 (rendabele/onrendabele segmenten), 1.8.1.9 (managementsbeslissing aanbevelen)
- **Gedekte kenniselementen**: 1.8.III.D (break-evenpunt + projectrentabiliteit) · 1.8.III.E (gemiddelde + marginale kosten-analyse) · 1.8.III.B.4 (marginale kosten)
- **Gedekte concepten**: `break-even-analyse` + `marginale-analyse` + linkt terug naar `direct-costing` (contributiemarge als bouwsteen)
- **Rationale**: BEP en marginale analyse delen één bouwsteen (contributiemarge uit direct costing) en worden op het examen wellicht samen of in soortgelijke vraagstelling getoetst ("vanaf welk volume?" of "zou je deze order aannemen?"). Beide instrumenten leiden tot *een beslissing* — sluit naadloos aan bij doelstelling 1.8.1.9. Themafiche `break-even-en-marginale-analyse` is de kapstok. Knelpuntanalyse (CM per knelpunt-uur) krijgt expliciete sectie — het is een examen-favoriet in andere accountancy-curricula en niet triviaal.

### Leerstuk 4 — `budget-en-variantieanalyse`

- **Vraag**: Hoe bouw je een masterbudget, hoe analyseer je achteraf de varianties, en wanneer herzie je het budget?
- **Type**: proces + techniek-fiche
- **Gedekte doelstellingen**: 1.8.1.6 (verschillen berekenen + analyseren), 1.8.1.7 (budget herzien), 1.8.1.11 (alle budgetten opstellen)
- **Gedekte kenniselementen**: 1.8.V (Budgetbeheer — kader) · 1.8.VI.A-D (definitie, begrippen, procedure, deelbudgetten + variantieanalyse) · 1.8.III.C.2 (verschillen-berekening — standaardkosten)
- **Gedekte concepten**: `budgetbeheer` (kader) + `masterbudget` + `variantieanalyse` + `standaardkostenmethode` (verdieping vanuit leerstuk 2)
- **Rationale**: Budget (vooraf) en variantieanalyse (achteraf) zijn één sturings-cyclus en pedagogisch onlosmakelijk. Masterbudget = integratie van zes deelbudgetten (commercieel · investering · productie · bevoorrading · administratie · kas) met pro-forma JR als toets; varianties zijn de feedback-lus. Budget-herziening (1.8.1.7) sluit de cyclus. Themafiche `budget-en-variantieanalyse` is de kapstok. Standaardkostenmethode wordt hier dieper uitgewerkt (was alleen geïntroduceerd in leerstuk 2) — natuurlijk want variantieanalyse vereist een norm.

### Niet als apart leerstuk

- **"Strategisch advies" (doel 1.8.1.10)** — te abstract voor een apart leerstuk. Wordt verweven als afsluit-sub-sectie in leerstuk 3 (beslissing) en leerstuk 4 (budget als strategisch instrument), via accountant-perspectief-beats ("hoe vertaal je dit naar een aanbeveling aan de directie?"). Past bij ADR-037 amendement: accountant-rol leeft *in* het leerstuk, niet apart.
- **"Boordtabel / dashboard" (1.8.III.C.3)** — sub-sectie in leerstuk 4 (variantierapportering = dashboard-vorm), met cross-PO-noot naar PO 4.0 (cabinet management).
- **"Personeelskosten + arbeidstijdmeting" (1.8.1.1)** — kort behandeld in leerstuk 1 (kostencomponenten) en leerstuk 2 (directe arbeid als kostencomponent). Het is geen zelfstandig examen-onderwerp; het ondersteunt de andere doelstellingen.

---

## 4. Gap-check

Matrix officiële doelstelling × leerstuk. Cellen geven aan welk leerstuk de doelstelling primair (P) of ondersteunend (O) dekt.

| Doelstelling | Lstk 1 (stelsel) | Lstk 2 (methodes) | Lstk 3 (BEP/marginaal) | Lstk 4 (budget/variantie) | Status |
|---|---|---|---|---|---|
| 1.8.1.1 Arbeidskosten + beloning + tijdregistratie | O (kostencomponenten + arbeid-as) | O (direct loon) | — | — | Volledig (verspreid; geen apart leerstuk nodig) |
| 1.8.1.2 Kostenberekening alle types (incl. diensten) | O (kader) | **P** (vier methodes + diensten-sectie) | — | — | Volledig |
| 1.8.1.3 Gemiddelde + marginale kosten | — | O (in direct costing-blok) | **P** (kern-leerstuk) | — | Volledig |
| 1.8.1.4 Kostprijsinformatie organiseren + IT | **P** (registratiesystemen + ERP) | O (kostprijsmodel-opzet) | — | — | Volledig |
| 1.8.1.5 Boekhoudplan management accounting | **P** (klassen 8/9 + spiegelrekeningen + boekingen) | O (kort: methode-effect op voorraadboeking) | — | — | Volledig |
| 1.8.1.6 Verschillen berekenen + analyseren | — | O (introductie standaardkosten) | — | **P** (variantieanalyse + decompositie) | Volledig |
| 1.8.1.7 Budget herzien | — | — | — | **P** (rolling forecast + herziening-sectie) | Volledig |
| 1.8.1.8 Rendabele/onrendabele segmenten + reductievoorstellen | — | O (marge per product via full vs direct) | **P** (keep-or-drop · marge-per-knelpunt) | O (variantie-onderzoek leidt tot kosten-reductie) | Volledig |
| 1.8.1.9 Managementsbeslissing aanbevelen | — | O (methode-keuze-rationale) | **P** (special order · make-or-buy · productmix) | O (budget-actie) | Volledig |
| 1.8.1.10 Strategisch advies | — | O (impliciet) | O (afsluit-aside) | O (afsluit-aside + budget-als-kompas) | **Risico-flag**: verweven, geen primair leerstuk. Bewuste keuze (te abstract). Bij review checken of stagiair de doelstelling herkent. |
| 1.8.1.11 Alle budgetten opstellen (operationeel + investering + management) | — | — | — | **P** (zes deelbudgetten + masterbudget) | Volledig |

**Gaten / risico-flags**:

- **1.8.1.10 (strategisch advies)** — niet primair. Mitigatie: in leerstuk 3 + 4 expliciet een sub-sectie "Wanneer dit een advies wordt aan de directie" met blockquote-aside. Sparring-moment.
- **Geen voorbeeldexamen-bron** — geen voorbeeldexamen-fiche; minicursus §4 wordt "Examen-verwachting (heuristisch)" met expliciete gap-vermelding.
- **Overlap met PO 1.9 (financiële analyse)** — "rendabiliteitsanalyse" en "marge per segment" leven in beide PO's. Beslissing: 1.8 = *ex-ante cost-data* + *interne sturing*; 1.9 = *ex-post jaarrekening-analyse* + *externe stakeholder*. Markeren in §1 minicursus tabel + in leerstuk 3 (cross-PO-noot).

---

## 5. Minicursus-skelet

Volgt de canonieke 5-secties-structuur. Vier leerstukken → vier wikilinks in §2, vier-stappen-leesroute in §3.

### §1 — Waarom dit vak?

- **Motivatie-paragraaf**: De analytische boekhouding is *intern* — geen jaarrekening voor de fiscus, maar cijferinzicht om beslissingen te nemen: welke prijs zet ik? Welke productlijn schrap ik? Welke afdeling slokt overhead op? Het is *niet wettelijk verplicht* (CBN 132/7 erkent meerdere geldige vormen), maar wie het niet heeft, vliegt blind. Voor de gecertificeerd accountant is dit *advies-terrein*.
- **Bredere-programma-tabel**:

| Andere PO | Relatie tot dit vak |
|---|---|
| **PO 1.1 — Algemene boekhouding** | De klassen 6X (kosten naar aard) zijn de input voor de analytische sfeer. Het stelsel klasse 8/9 koppelt eraan via spiegelrekeningen. |
| **PO 1.5 — IFRS** | IAS 2 bepaalt voorraadwaardering — bepaalt mee hoe vaste overhead wordt geactiveerd en hoe materiële varianties worden gedispenseerd. |
| **PO 1.9 — Financiële analyse** | Analoge thema's (marge, rentabiliteit) maar tegenovergesteld vertrekpunt: 1.9 vertrekt vanuit de gepubliceerde jaarrekening, 1.8 vanuit interne cost-data. Sterke complementariteit. |
| **PO 4.0 — Cabinet management** | KPI's en dashboards (boordtabel) zijn het zichtbare gezicht van de analytische sturing in een cabinet of bij een cliënt. |
| **PO 3.0 — Vennootschapsrecht** | Niet direct rakend — analytische boekhouding heeft geen wettelijke vorm. Wel relevant via rapportering aan bestuur en commissaris. |

### §2 — Wat is dit vak?

Vier compacte sub-secties, elk met wikilink naar het leerstuk:

- **"Twee assen op dezelfde euro"** → De algemene boekhouding ordent een loonkost als *620 Bezoldigingen* (naar aard); de analytische als *kost van afdeling productiehal A, toegerekend aan product X* (naar bestemming). Dezelfde euro, twee verhalen — één voor de fiscus, één voor de directie. → [[wat-is-analytische-boekhouding]]
- **"Vier kostprijs-instrumenten"** → Geen methode is intrinsiek juist; de keuze volgt het doel. Full costing voor de jaarrekening; direct costing voor beslissingen; ABC voor strategisch inzicht bij complexe overhead; standaardkosten voor sturing. → [[kostprijsmethoden-kiezen]]
- **"Wanneer wordt het een beslissing?"** → Break-even-analyse (vanaf welk volume?) en marginale analyse (verandert deze beslissing iets ten goede?) bouwen beide op contributiemarge — twee toepassingen van direct costing op operationele vragen. → [[break-even-en-marginale-beslissing]]
- **"Vooraf plannen, achteraf evalueren"** → Het masterbudget is de cijfermatige afspraak voor het komende jaar (zes deelbudgetten + pro-forma jaarrekening). Variantieanalyse decomposeert het verschil tussen norm en realiteit naar prijs en hoeveelheid. Samen vormen ze de sturings-cyclus. → [[budget-en-variantieanalyse]]

### §3 — Wat moet je kunnen + hoe pak je het aan

Hoofdtaak (parafrase): *Op basis van interne cost-data inzicht geven in winstgevendheid en kostenstructuur, beslissingen ondersteunen, en het management adviseren.* Elf doelstellingen samen — breed pakket, *integratie*-niveau.

**Leesroute door de leerstukken (vier stappen)**:

1. **Stelsel + registratie** — [[wat-is-analytische-boekhouding]]. Zonder begrip van klassen 8/9, spiegelrekeningen en de drie registratiesystemen kun je geen kostprijsmodel plaatsen. Hier woont ook de kostentypologie (vast/variabel, direct/indirect) als gemeenschappelijke woordenschat voor alles wat volgt.
2. **Methodes — kies en pas toe** — [[kostprijsmethoden-kiezen]] (zwaarste leerstuk). Vier methodes naast elkaar met vergelijkingsmatrix, beslisboom en mini-cases. Examen-zwaarte zit hier.
3. **Beslissingen onderbouwen** — [[break-even-en-marginale-beslissing]]. Concretiseert hoe je vanuit kost-cijfers naar een aanbeveling gaat. Knelpuntanalyse is sub-onderwerp.
4. **Plannen + evalueren** — [[budget-en-variantieanalyse]]. Masterbudget bouwen + varianties decompoeren + budget herzien.

Elke leerstuk bundelt zijn eigen accountant-perspectief (adviseur die het opzet bij een cliënt · interne controller die rapporteert · commissaris die de analytische methode bevraagt voor de audit-keten) in zijn eigen sectie. Niet apart op te zoeken hier.

**Voor de herhaling — vier themafiches**:

| Themafiche | Rol voor dit vak |
|---|---|
| [[themafiches/analytische-boekhouding-stelsel\|Stelsel & registratie]] | Klassen 8/9, drie registratiesystemen, kostentypologie — kapstok voor leerstuk 1 |
| [[themafiches/kostprijsmethoden\|Kostprijsmethoden]] | Vergelijkingsmatrix + beslisboom + formules — kapstok voor leerstuk 2 |
| [[themafiches/break-even-en-marginale-analyse\|Break-even & marginale analyse]] | Twee instrumenten, formules, valkuilen — kapstok voor leerstuk 3 |
| [[themafiches/budget-en-variantieanalyse\|Budget & variantieanalyse]] | Masterbudget-flow + variantie-decompositie — kapstok voor leerstuk 4 |

### §4 — Examen-verwachting (heuristisch — geen voorbeeldexamens beschikbaar)

Geen examenvragen voor PO 1.8 in onze classificatie (toestand 2026-05-30). Op basis van het PO-niveau (*integratie*), de breedte van het pakket en de manier waarop verwante PO's getoetst zijn:

- Verwacht **begripsvragen** ("verschil full vs direct costing", "wat is contributiemarge", "wat is masterbudget vs forecast")
- Verwacht **mini-berekeningen** (BEP-volume, contributiemarge, variantie-decompositie) — niet een hele kostprijs uit-bouwen
- Verwacht **methode-keuze-cases** kort ("welke methode voor deze beslissing en waarom") — sluit aan bij doelstelling 1.8.1.9
- Mogelijk: **identificatie verlieslatend segment** uit een korte case (doelstelling 1.8.1.8)

Status van deze sectie: **te updaten** wanneer ITAA-voorbeeldexamens voor PO 1.8 vrijgegeven of geclassificeerd worden.

### §5 — Concepten cross-PO

Tabel met concepten die ook elders relevant zijn:

| Concept | Andere PO('s) |
|---|---|
| `bedrijfskosten` (MAR-context) | 1.1 (algemene boekhouding) |
| `personeelskosten` | 1.1 · 2.x (loonfiscaliteit perifeer) |
| Kostentypologie (vast/variabel) | 1.9 (analyse jaarrekening — break-even via gepubliceerde cijfers) |
| `break-even-analyse` | 1.9 (financiële analyse-toepassing) |
| `masterbudget` | 4.0 (cabinet management — KPI's, dashboards) |
| `variantieanalyse` | 4.0 (performance-rapportering) |
| Voorraadwaardering (full vs direct effect) | 1.5 (IFRS — IAS 2) · 1.1 |

---

## 6. Voorbeeldgroep

**Voorstel**: **nieuwe voorbeeldgroep `meridia-meubel`** — *niet* Aurelia hergebruiken.

### Rationale voor nieuwe groep

Aurelia (PO 1.4) is een **holding-structuur** met dochters en deelnemingen — perfect voor consolidatie, maar leeg op het *productie-niveau* dat 1.8 vereist. Analytische boekhouding heeft een ondernemingscontext nodig met:

- Eén of meer **productlijnen** met grondstoffen + arbeid + machine-uren (voor kostprijsmethodes en variantie)
- **Vaste en variabele kosten** op operationeel niveau (voor break-even)
- **Capaciteit** (machine-uren, productie-uren) als knelpunt-context
- Cijfers voor **deelbudgetten** (verkoop · productie · bevoorrading · investering · administratie · kas)

Aurelia hergebruiken zou meer storend dan helpend zijn: de holding-context past niet bij de productie-vragen die 1.8 stelt.

### Schets `meridia-meubel`

**Naam**: Meridia Meubel BV
**Sector**: meubelproductie (referentie aan het `analytische-boekhouding`-record dat al een meubelmaker-voorbeeld gebruikt; consistentie en herbruikbaarheid van de mentale beeld-omgeving)
**Rechtsvorm**: BV, middelgrote vennootschap
**Productlijnen**: twee — `tafel-eik` (standaard) + `kast-op-maat` (job-order). Bewust *twee productie-types* gekozen omdat kenniselement `1.8.III.A.3` expliciet vraagt naar enkelvoudige vs job-order vs continuproductie.
**Balansdatum**: 31/12/2025 · boekjaar 2026 voor budget-leerstuk

### Te genereren data

- **Kostenmodel**:
  - Kostenplaatsen: productiehal · afwerkatelier · magazijn · verkoop · algemeen beheer
  - Cost-drivers: machine-uren (CNC) · directe arbeidsuren (afwerking) · m² (huur) · aantal opstellingen (setup)
  - Verdelingssleutels per indirecte kostencategorie
- **Kostprijs-berekeningen** (voor leerstuk 2):
  - Full costing van `tafel-eik` (per eenheid) — alle kosten via sleutels
  - Direct costing van `tafel-eik` — contributiemarge
  - ABC-vergelijking van `tafel-eik` vs `kast-op-maat` — laat zien hoe ABC de cross-subsidie ontmaskert (kast slokt opstellingen, krijgt onevenredig lage overhead in full costing)
  - Standaardkost-kaart met norm-prijzen en -hoeveelheden per `tafel-eik`
- **Break-even + marginale data** (voor leerstuk 3):
  - BEP-eenheden en BEP-omzet voor `tafel-eik`
  - Multi-product BEP (gewogen-CM voor mix `tafel-eik` + `kast-op-maat`)
  - Special-order-case: korting-vraag van retailer (350 EUR ipv 500) — accept of weigeren?
  - Make-or-buy-case: laden bijbestellen vs zelf maken
  - Knelpunt-case: CNC-machine als bottleneck, mix-keuze op CM/CNC-uur
- **Budget + varianties** (voor leerstuk 4):
  - Verkoopbudget 2026 (volume × prijs per productlijn × kwartaal)
  - Productiebudget afgeleid + bevoorradingsbudget + investeringsbudget (nieuwe afwerkmachine)
  - Administratie- en kasbudget
  - Pro-forma RR + balans (die sluit!) + KSO
  - Variantierapport Q1 2026: prijsvariantie eik (markt-stijging) + hoeveelheidsvariantie arbeid (onervaren nieuwe medewerker)
- **Boekingen** (voor leerstuk 1 + 4):
  - Spiegelboeking voorbeeld (kost-aard 60X → klasse 9X) volgens CBN 132/7-mechaniek
  - Standaardkosten-boeking met variantie-rekening

**Belangrijk**: cijfers consistent over leerstukken heen (totalen kloppen, variantie's optellen). Productie-volumes zo gekozen dat BEP-berekening getallen geeft die niet absurd zijn.

### Hergebruiks-overweging

Eenmaal `meridia-meubel` bestaat, kan ze later ook bruikbaar zijn voor:
- PO 1.9 (financiële analyse) — een gepubliceerde JR van Meridia kan dezelfde getallen externalize
- PO 4.0 (cabinet management) — KPI-dashboard rond Meridia

Niet als hard ontwerpdoel nu, wel als bonus.

---

## 7. Themafiche-mapping

**Vier bestaande themafiches** dekken alle vier leerstukken één-op-één. Geen nieuwe themafiche nodig.

| Leerstuk | Bestaande themafiche | Tweelaags-doorklik-update nodig? |
|---|---|---|
| `wat-is-analytische-boekhouding` | [[themafiches/analytische-boekhouding-stelsel]] | **Ja** — huidige "Doorklik" sectie noemt alleen concept (`[[analytische-boekhouding]]`). Update naar ADR-037-amendement: sectie "Verdieping" met sub-secties "Leerstuk — voor pedagogische opfris" (→ `[[wat-is-analytische-boekhouding]]`) + "Concept-fiches — voor definitorisch detail" (huidige lijst). |
| `kostprijsmethoden-kiezen` | [[themafiches/kostprijsmethoden]] | **Ja** — analoge update; leerstuk als primaire doorklik, vier methode-concepten als secundaire. |
| `break-even-en-marginale-beslissing` | [[themafiches/break-even-en-marginale-analyse]] | **Ja** — analoge update; leerstuk primair, twee analyse-concepten + direct/full costing als secundaire. |
| `budget-en-variantieanalyse` | [[themafiches/budget-en-variantieanalyse]] | **Ja** — analoge update; leerstuk primair, budgetbeheer/masterbudget/variantieanalyse/standaardkosten als secundaire. |

**Werk-overweging**: update van vier themafiches is mechanisch (één sectie-vervanging per fiche), valt in Stap 6 van `leerstuk-procedure.md`. Tegelijk markeren themafiches' status van "voorgesteld" naar "actief" of vergelijkbaar.

---

## 8. Open vragen voor sparring

1. **Doelstelling 1.8.1.10 (strategisch advies) verweven of apart?** — Voorstel: verweven via accountant-perspectief-blockquotes in leerstuk 3 + 4. Alternatief: een vijfde dun leerstuk `accountant-als-management-adviseur` (~1200 woorden) dat de advies-vaardigheid expliciet maakt en de schakel naar PO 4.0 legt. Risico: te abstract om didactisch te dragen; voordeel: zichtbaarheid van de doelstelling in de leerstuk-lijst.

2. **Voorbeeldgroep — `meridia-meubel` nieuw of bestaand laten waar mogelijk?** — Productie-context lijkt onontkoombaar. Maar: heeft de gebruiker een voorkeur voor een dienstenondernemings-context (advocatenkantoor, IT-consultancy) om kenniselement `1.8.III.A.5` "dienstverlenende ondernemingen" expliciet te eren? Beslissing-as: productie geeft rijkere demonstratie van methodes (machine-uren, knelpunten, voorraad); diensten zou meer aansluiten bij de cabinet-realiteit van de stagiair. Mogelijke compromis: productie als hoofd, dienst-mini-case in leerstuk 2 (kostprijs voor dienst-onderneming via uurtarief-berekening).

3. **Leerstuk 2 (kostprijsmethoden) — vier-in-één of opsplitsen?** — Voorstel volgt granulariteits-stelregel (alles in één, mag tot ~4000 woorden). Sparring-moment of de gebruiker liever twee leerstukken ziet (`full-vs-direct-costing` + `abc-en-standaardkosten`). Tegen-argument: de vier methodes worden door de leerstof-auteur al systematisch *vergeleken* — een tabel met vier kolommen wint door bijeen te staan, niet door gesplitst.

4. **Voorbeeldexamen-gap** — Naast de "Examen-verwachting"-sectie in de minicursus, ook actief op zoek gaan naar examenvragen die ergens anders verschuilen (BIBF-vragen, dubbel-getagde vragen die we misclassificeerd hebben)? Dat is niet in scope van deze ronde, maar wel een aandachtspunt voor latere update van het leerpad.

5. **Cross-PO links naar 1.9** — Het PO 1.9-leerpad is nog niet gebouwd. Beslissen we nu al om vooruit-links te leggen (die ofwel breken of dood-eind zijn tot 1.9 bestaat), of wachten we tot 1.9 er is en updaten we dan? Voorstel: in dit skelet en in de leerstuk-scripts geen `[[1.9-leerstuk]]`-wikilinks; alleen verwijzing in lopende tekst ("zie ook PO 1.9 — financiële analyse").

6. **ADR-037 granulariteit** — Vier leerstukken is binnen het 4-7-bereik, maar aan de ondergrens. Voor een *integratie*-niveau-PO met 11 doelstellingen is dat misschien te grof. Tegen-argument: de themafiche-auteur heeft al expliciet voor vier sub-clusters gekozen — pedagogische pre-validatie. Bij twijfel houden we vier; bij review na render kunnen we splitsen.

---

## Rapport (terug naar de mens)

- **4 leerstukken voorgesteld**, één-op-één gespiegeld op de vier bestaande themafiches: `wat-is-analytische-boekhouding`, `kostprijsmethoden-kiezen`, `break-even-en-marginale-beslissing`, `budget-en-variantieanalyse`.
- **Hoofdtaak**: één — *Analyseren van de financiële situatie van een onderneming*. Onder die ene taak hangen **11 doelstellingen** die effectief een methodologisch landschap dekken (kostprijs → BEP/marginaal → budget/variantie → advies). Niveau: *integratie* (hoger dan 1.4's *toepassen*).
- **Gaten**:
  - **Geen voorbeeldexamens** voor PO 1.8 (geen `po-1.8.md`, geen vragen in classificatie). §4 minicursus wordt "Examen-verwachting (heuristisch)" met expliciete gap-vermelding.
  - **Doelstelling 1.8.1.10 (strategisch advies)** wordt verweven (geen primair leerstuk) — risico-flag.
  - Overlap met PO 1.9 (financiële analyse) op rentabiliteitsanalyse — door scheiding "ex-ante intern" vs "ex-post extern" af te grenzen.
- **Voorbeeldgroep**: **nieuw — `meridia-meubel`** (productie-context met twee productlijnen). Aurelia (holding) past structureel niet bij dit PO. Optie om diensten-mini-case in leerstuk 2 toe te voegen voor kenniselement 1.8.III.A.5.
- **Belangrijkste onzekerheid voor sparring**: granulariteit van leerstuk 2 (vier methodes in één — tot ~4000 woorden — vs splitsen in twee). Tweede onzekerheid: of doelstelling 1.8.1.10 een vijfde leerstuk verdient of verweven blijft.
- **Volgende stap**: na sparring → **Stap 2** uit `leerstuk-procedure.md`: `meridia-meubel.yaml` voorbeeldgroep schrijven (1-2 uur, kloppende cijfers), daarna **Stap 3** scripts per leerstuk.
