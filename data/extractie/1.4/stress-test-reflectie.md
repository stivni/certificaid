# Stress-test reflectie — minicursus PO 1.4 op basis van 31 v2-records

**Datum**: 2026-05-15
**Schrijver**: Claude (Opus 4.7) als "stagiair-die-de-cursus-moet-schrijven"
**Input**: `data/concept_records/1.4-v2/` (31 records, schema 1.2)
**Output**: `content/studiemateriaal/1.4-geconsolideerde-jaarrekening/minicursus.md` (~4.700 woorden)

---

## 1. Tijdens-het-schrijven gaps

Het schrijven verliep grotendeels vlot. Op een handvol punten miste ik
specifieke informatie. Concreet, in volgorde van zwaarte:

1. **Cijfervoorbeeld voor integrale consolidatie ontbreekt volledig.** Het
   record `integrale-consolidatie` heeft alleen bouwstenen, geen
   `berekeningsmethode[]` en geen `concreet_voorbeeld`. Voor
   vermogensmutatie was er wél een rijk numeriek voorbeeld (ABC verwerft 20 %
   in DEF voor 200, netto-activa 600). Een vergelijkbaar voorbeeld voor
   integrale consolidatie ontbreekt — bv. "M koopt 80 % van D voor 1000;
   netto-activa D op fair value = 1100; → consolidatieverschil = 1000 −
   880 = 120; belangen van derden = 220." Ik moest dit numerieke voorbeeld
   bewust *niet* zelf verzinnen (CLAUDE.md regel 1) en heb het in §6.1 dus
   alleen kwalitatief beschreven. **Pijnpunt** voor de student die wil leren
   *rekenen* aan een integrale consolidatie.

2. **Eliminatie-mechanica is te abstract.** `intragroep-eliminaties` zegt
   *wat* geëlimineerd wordt (vorderingen ↔ schulden, etc.) maar geeft geen
   gewerkt voorbeeld van een niet-gerealiseerde intercompany-winst op een
   levering die nog in voorraad zit. Bijvoorbeeld: "Moeder verkoopt
   handelsgoederen aan dochter voor 100 met 30 % marge; eind boekjaar zit nog
   40 in dochter-voorraad → te elimineren niet-gerealiseerde winst = 40 ×
   30/130." Voor de student is dat type calculatie typisch examen-stof, en de
   record kan het niet leveren. Ik heb dat in §8 dus alleen conceptueel
   beschreven.

3. **Concrete presentatie van de geconsolideerde balans/RR.** Er is
   regelmatig sprake van rubrieken ('Belangen van derden', 'Aandeel van derden
   in het resultaat', 'Vennootschappen waarop vermogensmutatie is toegepast')
   maar nergens staat een geschematiseerde voorbeeldbalans of -RR met de
   volgorde van rubrieken. Voor wie nooit een geconsolideerde rekening heeft
   gezien is dat een gemis. Een schema-record (bv. een `methode`-node
   "Geconsolideerde balans — rubriekenstructuur") zou veel waarde toevoegen.

4. **Wettelijke vermoedens van controle in rechte (art. 1:14 §2 WVV).** De
   record `controle` heeft een `references[]` met de rol
   `wettelijk-vermoeden-controle-in-rechte` maar zonder de **volledige
   opsomming**: "(a) meerderheid stemrechten, (b) recht meerderheid bestuurders
   benoemen, (c) statutaire/contractuele bevoegdheid, (d) ...". De passage is
   te beknopt. Voor een student die wil oefenen op casussen ("Heeft M
   controle?") moet hij vier of vijf duidelijk gescheiden gevallen kunnen
   nalopen. Nu blijft het bij "etc.".

5. **Numerieke voorbeelden van step acquisition / step disposal.** De records
   geven kwalitatieve scenario's ("20 → 30 %", "30 → 60 %", "80 → 60 %") maar
   geen volledige rekenuitwerking met aanschaffingsprijzen, dividenden,
   afschrijvingen op het oude verschil, etc. Voor een examen waarin step
   acquisitions klassiek met cijfers worden getoetst, is dat thin. De record
   `step-acquisition` had baat bij een `concreet_voorbeeld` in zijn
   stappenplan (zoals bij `vermogensmutatiemethode — berekeningsmethode` wél
   aanwezig).

6. **Onderscheid tussen "evenredige" en "proportionele" terminologie.** Beide
   termen worden gebruikt; nergens staat expliciet dat ze synoniem zijn (al is
   het impliciet uit de naam van de record `evenredige-consolidatie` met
   subtitel "proportionele methode"). Een record-veld `synoniemen[]` of een
   note in de definitie zou helpen.

7. **Goodwill-impairment ontbreekt.** KB WVV art. 3:131 spreekt over
   aanvullende of niet-recurrente afschrijvingen bij wijziging van economische
   omstandigheden. De record `consolidatieverschil` noemt dit kort maar geeft
   geen handvat voor *wanneer* en *hoe* (geen triggertest, geen voorbeelden).
   IFRS-impairment (IAS 36) zou hier in een IFRS-extensie passen, maar zelfs
   in BE-GAAP-kader was meer praktische gids nuttig geweest.

8. **Wat als de moeder zelf geen geconsolideerde rekening moet maken — wat
   moet de dochter dan?** De groottecriteria-record beoordeelt of de moeder
   moet consolideren, maar zegt niets over de positie van een dochter in een
   "uitvrijgestelde" groep. 🤖 In de praktijk: moet die dochter dan wél haar
   eigen enkelvoudige rekening op de gewone manier publiceren? (Vermoedelijk
   ja, maar dat is buiten de bronnen om.) Een edge of cross-ref naar
   "enkelvoudige jaarrekening" zou de student helpen niet te verdwalen.

---

## 2. Schema-velden in gebruik — wat werkte, wat niet

### 2.1 Erg nuttig in mijn schrijfproces

- **`definitie` / `main_rule` / `doel` / `verplichting`** (type-specifieke
  hoofdvelden): dragen het hele verhaal. Goed gevuld, goed bronaangegeven.
  Zonder deze velden was er niets te schrijven.
- **`vergelijkingsparen[]`**: gouden veld. Drie van mijn hoofdstuk-secties
  (§3.1, §6.4, §7.4) konden ik in essentie kopiëren uit
  `vergelijking_met` + `verschil` + `trigger`. Met name §6.4 (de drie
  methode-verwarringen) werd quasi rechtstreeks afgeleid. Trigger-velden
  ("Bij verhoging tot >50 % → integraal") gaven me het juiste
  beslissingsmoment.
- **`berekeningsmethode[]`** (vooral het sub-veld `concreet_voorbeeld`):
  fantastisch. Het ABC-DEF-voorbeeld in `vermogensmutatiemethode` en
  `consolidatieverschil` heeft mij toegelaten een rekenvoorbeeld neer te
  zetten zonder zelf cijfers te bedenken. Hetzelfde voor
  `belangenpercentage` (0,70 × 0,60 = 0,42). Dit is exact het type info dat
  de student nodig heeft.
- **`drempelwaarden[]`**: compact en specifiek. De drie maanden in
  `geconsolideerde-jaarrekening`, de groottecriteria, de 20 %-vermoeden — ik
  kon ze direct in tabelvorm gieten.
- **`stappen[]`** met `volgorde`: voor de procedures
  (werkelijke-waarde-toerekening, intragroep-eliminaties, step-acquisition,
  step-disposal) was dit essentieel. Het maakte het schrijven van §16
  (synthese-stappenplan) bijna mechanisch.
- **`oorzaken[]`** met confidence `inferred-from-aggregation`: de vier
  oorzaken van een consolidatieverschil (§7.1) zijn een prachtige toepassing
  van dit veld. De student krijgt zo niet alleen *wat* een
  consolidatieverschil is, maar ook *waarom* het ontstaat.
- **`in_praktijk[]`**: nuttig vooral voor `aspect` + `betekenis` +
  `herkenningspunt`. Bij `controle` gaf "Aandeelhoudersregister + statuten
  tonen >50 % stemrechten" mij een concreet examen-handvat. Bij
  `controlepercentage` gaf het `herkenningspunt`
  "Tabelopgaven in examens met 'M 70 % A; A 60 % B'-structuren" letterlijk
  de juiste voorbeeld-trigger.
- **`valkuilen[]`**: gebruikt op cruciale plaatsen — de 3-maanden-as ("zowel
  vóór als na", niet zes maanden), het wel/niet proportioneel elimineren bij
  evenredige consolidatie, uitgestelde belastingen vergeten bij eerste
  consolidatie. Zonder dit veld zou ik dezelfde fouten maken die de student
  maakt.

### 2.2 Niet of nauwelijks gebruikt

- **`edges[]`**: leeg in álle 31 records. Dit is in v2 nog niet ingevuld. De
  cross-record-coherentie heb ik dus volledig zelf moeten reconstrueren door
  op id's te scannen (zie §5).
- **`references[]`**: gebruikt in slechts ~5 records (controle, consortium,
  consolidatiekring, consolidatieverschil, controlepercentage,
  invloed-van-betekenis, geconsolideerde-jaarrekening,
  groottecriteria-geconsolideerde-basis, gezamenlijke-controle). Waar
  aanwezig waren ze nuttig (bv. de doorrekenregel art. 1:14 §2 WVV bij
  `controlepercentage`), maar veelal te kort om iets concreets mee te doen.
  De "rol"-naamgeving (`wettelijk-vermoeden-controle-in-rechte`,
  `kwantitatief-vermoeden`) is goed; de `passage`-tekst zou meer detail mogen
  bevatten.
- **`voorbeeld_inline`**: enkel ingevuld bij `consolidatieverschil`. Voor de
  andere records had ik veel willen aanvullen met een eenregelig voorbeeld
  bij de definitie (bv. bij `minderheidsbelangen`: "M heeft 80 % van D, D
  realiseert 100 winst → belang van derden = 20"). De record
  `aandeel-van-derden-in-resultaat` heeft dit wél via
  `berekeningsmethode.concreet_voorbeeld` — best practice die te repliceren
  is.
- **`bouwstenen[]`** met sub-veld `confidence` ontbreekt af en toe (bv. in
  `integrale-consolidatie` zijn er bouwstenen mét source, wat goed is, maar
  geen `_provenance` op stap-niveau telkens). Wisselvallig ingevuld.
- **`tijdlijn[]`**: niet aangetroffen in de records die ik heb gebruikt. Voor
  PO 1.4 logisch — er zijn weinig pure procedurele termijnen — maar het
  3-maanden-criterium had eventueel als `tijdlijn[]`-item in
  `geconsolideerde-jaarrekening` gekund. Nu zit het in `drempelwaarden[]`,
  wat ook werkt.
- **`subvaardigheden[]`**: niet gebruikt (geen skill-records).
- **`uitzonderingen[]`**: keurig gebruikt in `consolidatiekring`,
  `consolidatieverplichting`, `uniforme-waarderingsregels-consolidatie`.
  Werkte goed.

### 2.3 Velden die ik wenste te hebben

- **`synoniemen[]`** zou helpen voor terminologie-disambiguatie
  (evenredig/proportioneel, equity/vermogensmutatie, belangen van
  derden/minderheidsbelangen).
- **`berekeningsmethode[].concreet_voorbeeld` op alle methode-records**, niet
  alleen vermogensmutatie. Integrale consolidatie en evenredige consolidatie
  hebben *geen* numeriek voorbeeld.
- **Een `presentatie[]`-veld** met de balansrubriek + plaats in de structuur
  (passief na eigen vermogen voor minderheidsbelangen; één lijn onder
  financiële vaste activa voor vermogensmutatie-deelneming). Nu zit dit
  verspreid in `in_praktijk[].betekenis`, waar het nuttig is, maar niet
  goed doorzoekbaar.

---

## 3. Records die ondervuld bleken — top-5 zwakste

In volgorde van zwakste eerst:

### 3.1 `integrale-consolidatie.json` — ondervuld op rekenvoorbeelden

- **Wat ontbreekt**: `berekeningsmethode[]` is volledig afwezig. Geen
  numeriek voorbeeld voor de drie bouwstenen "Eliminatie deelneming tegen
  aandeel in eigen vermogen", "Eliminatie intragroep-transacties",
  "Afzonderlijke vermelding belangen van derden".
- **Impact op cursus**: ik kon §6.1 alleen kwalitatief schrijven. Ironisch,
  want dit is dé centrale methode in PO 1.4.
- **Aanbeveling**: voeg een `berekeningsmethode` toe met scenario "M koopt
  80 % van D; aanschaffingswaarde 1000; netto-activa D op fair value 1100;
  → aandeel = 880; consolidatieverschil = 120; belangen van derden = 220 op
  passief".

### 3.2 `dochteronderneming.json` — minimalistisch

- **Wat ontbreekt**: alleen `definitie` + één `vergelijkingsparen`. Geen
  `in_praktijk`, geen `voorwaarden`, geen `voorbeeld_inline`. Ondanks dat dit
  *het* basisbegrip is.
- **Impact**: ik moest in §3.2 de hele behandeling van dochters bouwen op
  fragmenten uit `controle`, `exclusieve-controle`, `geassocieerde-onderneming`.
  Voor de student lijkt dit een nevenconcept terwijl het centraal hoort.
- **Aanbeveling**: voeg `in_praktijk[]` toe met "Wanneer is een onderneming
  een dochter?" + herkenningspunten (KB WVV art. 1:15 §1 + §2 met
  controle-vermoedens).

### 3.3 `moedervennootschap.json` — sterk maar incompleet

- **Wat ontbreekt**: geen `voorwaarden[]` voor wanneer een moeder ook moet
  consolideren versus wanneer ze vrijgesteld is. Alleen één
  vergelijkingsparen (vennoot-van-consortium). Geen verwijzing naar de
  groottecriteria of subconsolidatie-vrijstelling die voor de
  consolidatie-verplichting beslissend zijn.
- **Impact**: ik moest §3.2 + §13 + §11 zelf samenbinden uit drie verschillende
  records. Een nodevisualisatie van de moedervennootschap met afhankelijkheden
  zou veel waard zijn.

### 3.4 `uniforme-waarderingsregels-consolidatie.json` — te beknopt

- **Wat ontbreekt**: geen voorbeeld van een typische afwijking (bv. een
  dochter die LIFO toepast terwijl de groep FIFO hanteert), geen
  `berekeningsmethode` of `in_praktijk` over hoe je in de praktijk de
  cijfers herrekent. Geen valkuilen.
- **Impact**: §9 in de cursus is bijna een herhaling van het main_rule —
  weinig diepgang mogelijk.

### 3.5 `ifrs-verordening-1606-2002.json` — minimaal

- **Wat ontbreekt**: alleen `main_rule`, geen verdere uitwerking. Geen
  voorbeeld van welke lidstaten de verplichting uitbreidden, geen
  `vergelijkingsparen` met BE-GAAP, geen `in_praktijk` over welke entiteiten
  effectief geraakt worden.
- **Impact**: §14.1 is daardoor erg kort.
- **Nuance**: deze record dient vooral als "anker" voor de IFRS-keuze-record;
  in die rol is hij voldoende. Maar als kennisbron op zichzelf zwak.

**Eervolle vermeldingen**:

- `geassocieerde-onderneming.json` — alleen `definitie` + één
  `in_praktijk`. Erg dun gegeven het belang van het concept.
- `aandeel-van-derden-in-resultaat.json` — heeft alleen `definitie` +
  `berekeningsmethode`. Geen `vergelijkingsparen` met "belangen van derden"
  (de balans-kant) terwijl die twee letterlijk de spiegel van elkaar zijn.
- `vrijstelling-subconsolidatie.json` — `valkuilen` zijn er, maar geen
  `voorwaarden_toepassing` of `stappen` voor *hoe* je de vrijstelling inroept
  (toelichting + openbaarmaking-procedure).

---

## 4. Records die juist sterk waren — top-5

### 4.1 `consolidatieverschil.json` — de gouden standaard

- **Sterk**: `definitie` + `references[]` + `oorzaken[]` (4 met
  inferred-from-aggregation) + `voorwaarden[]` (3) + `drempelwaarden[]` +
  `vergelijkingsparen[]` (verwarring met statutaire goodwill!) +
  `voorbeeld_inline` met cijfers.
- **Waarom**: dit ene record droeg §7 quasi alleen. Alle aspecten —
  definitie, oorzaken, behandeling, valkuilen, voorbeelden — zaten al
  voorgestructureerd in het record.
- **Te volgen patroon voor andere centrale begrippen**.

### 4.2 `vermogensmutatiemethode.json` — perfecte methode-record

- **Sterk**: `doel` + `voorwaarden_toepassing` + twee
  `berekeningsmethode[]`-blokken (eerste consolidatie + latere consolidaties)
  mét formules, stappen én een `concreet_voorbeeld` + `vergelijkingsparen` +
  `in_praktijk` met presentatie.
- **Waarom**: §6.3 kon ik in essentie directly uitschrijven uit deze record.
  Twee aparte berekeningsmethodes (eerste + latere) is een didactisch sterke
  splitsing.

### 4.3 `controle.json` — anker-record

- **Sterk**: `definitie` met substantiële `references[]` (twee rollen, voor
  rechte en feite) + `vergelijkingsparen` (met invloed van betekenis,
  trigger-veld is uitstekend) + twee `in_praktijk[]`-blokken met
  herkenningspunten ("Aandeelhoudersregister", "AV-aanwezigheidslijsten").
- **Waarom**: het hele hoofdstuk 3 hangt aan deze record. De
  `herkenningspunten` waren een traktatie — exact wat een student nodig heeft
  om casussen te kunnen oplossen.

### 4.4 `belangenpercentage.json` — compact maar volledig

- **Sterk**: `definitie` + `berekeningsmethode[]` met formule, stappen en
  `concreet_voorbeeld` (0,70 × 0,60 = 0,42) + `vergelijkingsparen` met
  controlepercentage.
- **Waarom**: ik kon §5.2 volledig opbouwen rond dit ene record. Het
  vergelijkingsparen-paar met `controlepercentage` is bidirectioneel
  ingericht (beide records verwijzen naar elkaar) — een mooi voorbeeld van
  cross-record-coherentie zonder echte edges.

### 4.5 `groottecriteria-geconsolideerde-basis.json` — drempel-record af

- **Sterk**: `main_rule` + `references[]` + vier `drempelwaarden[]` (3
  echte drempels + 1 modificatie "+20 %") + twee `valkuilen[]` (waarvan één
  met `inferred` over indexering) + `in_praktijk` (balansdatum-toets).
- **Waarom**: §11 kon volledig getabuleerd op basis van deze record. De
  combinatie van harde drempels met een waarschuwing over indexering is
  precies wat de student moet meenemen.

---

## 5. Cross-record-coherentie

**Conclusie**: de coherentie is **conceptueel goed** maar **mechanisch zwak**.

### 5.1 Conceptueel goed

De records *verwijzen naar elkaar* op verschillende manieren:

- via `vergelijkingsparen[].vergelijking_met` met record-id (bv.
  `"vergelijking_met": "evenredige-consolidatie"`);
- via narratieve verwijzing in de tekst ("zie afzonderlijk record",
  "geassocieerde onderneming", "consolidatieverschil");
- via gemeenschappelijke source.short (KB WVV art. 3:127, 3:134, 3:137
  duiken op in zowel `integrale-consolidatie` als `minderheidsbelangen` als
  `intragroep-eliminaties` — dat helpt de coherentie passief).

Bij vrijwel elke overgang in mijn cursus kon ik een record vinden die het
verband expliciteerde. **Niet één keer** moest ik een verband zelf van
toetsen maken op een controversiële manier; de zes vergelijkingsparen die ik
gebruikte (in `controle`, `controlepercentage`, `belangenpercentage`,
`integrale-consolidatie`, `vermogensmutatiemethode`, `consolidatieverschil`)
waren stuk voor stuk goud waard.

### 5.2 Mechanisch zwak

- **`edges[]` is leeg in alle 31 records.** Schema 1.2 staat edges toe maar
  ze worden niet gepopuleerd. Bijgevolg moet ik *grep-style* zoeken in de
  bestanden om te zien welke records elkaar noemen — niet schaalbaar.
- **Geen reverse-index.** Wanneer ik wilde weten "welke records noemen
  *consolidatieverschil*?" was er geen efficiënte zoekstrategie behalve
  bestandsgewijs scannen.
- **Verwarrend veld**: `controlepercentage.json` heeft een veld
  `vergelijking_with_label_correctie` (nul, vermoedelijk een
  schrijffout/leftover) — laat zien dat de extractor zelf wat ruis
  achterlaat. Cleanup nodig.

**Edges zou ik wensen voor**:

- `controle` → `dochteronderneming` (definieert)
- `exclusieve-controle` → `integrale-consolidatie` (triggert)
- `gezamenlijke-controle` → `evenredige-consolidatie` (triggert)
- `invloed-van-betekenis` → `vermogensmutatiemethode` (triggert)
- `step-acquisition` → `consolidatieverschil` (genereert)
- `intragroep-eliminaties` → `integrale-consolidatie` (onderdeel-van)
- `consolidatieverplichting` → `groottecriteria-geconsolideerde-basis`
  (uitzondering-trigger)
- `consortium` → `consolidatieverplichting` (specialiseert)

Deze edges zijn allemaal *impliciet* aanwezig — uit de teksten,
vergelijkingsparen en source-overlap. Maar voor een RAG-systeem of een
graph-walk zijn ze onbruikbaar zolang `edges[]` leeg blijft.

---

## 6. Productie-oordeel — kan een kandidaat-accountant hiermee PO 1.4 beheersen?

**Kort antwoord**: voor de **begripsmatige** beheersing van PO 1.4 is dit
voldoende — voor 70 à 75 %. Voor de **rekenmatige** beheersing zit het op
50 à 60 %.

### 6.1 Wat de cursus afdekt (sterk)

- De juridische architectuur (controle/moeder/dochter/geassocieerd).
- De keuze van consolidatiemethode in functie van controleniveau.
- Het verschil controle ↔ belang en de doorrekenregels.
- De drempels: 20 %, 50 %, 3 maanden, groottecriteria.
- De begripsmatige opbouw van een geconsolideerde balans en RR.
- Consolidatieverschil: oorzaken, behandeling, valkuil-met-statutaire-goodwill.
- Bijzondere figuren: consortium, vrijstelling subconsolidatie.
- IFRS verplicht/keuze.

### 6.2 Wat ontbreekt voor volwaardige beheersing

1. **Numerieke casus-vaardigheid voor integrale consolidatie**. Een student
   die de cursus leest, zal de bouwstenen kunnen *opnoemen* maar niet
   *uitwerken* op een nieuwe casus zonder bijkomende oefeningen. Voorbeelden
   zijn er voor vermogensmutatie en belangenpercentage; voor integrale
   consolidatie en evenredige consolidatie niet.
2. **Intercompany-eliminatie van niet-gerealiseerde winsten op leveringen
   die nog in voorraad/vaste activa zitten** — een typisch examenonderwerp.
   De record vermeldt het bestaan, niet de techniek.
3. **Boekingen.** De cursus blijft volledig op het niveau van bedragen en
   rubrieken. Geen enkel record geeft een *journaalboeking*. Ik vermoed dat
   de bronrecords (CBN-adviezen) wél boekingen bevatten maar dat de
   extractie ze niet heeft opgenomen. Voor een kandidaat-accountant is
   "Debet X / Credit Y" deel van de gevraagde competentie.
4. **IFRS-specifieke kennis** is bijna afwezig. De cursus zegt enkel wanneer
   IFRS verplicht/optioneel is, niet *wat* IFRS anders doet (bv. impairment
   ipv afschrijving van goodwill, geen evenredige consolidatie meer onder
   IFRS 11 maar enkel equity, full goodwill vs. partial goodwill). Voor
   PO 1.4 II ('IFRS-keuze en -verplichting') is dit een gap.
5. **Verslagvereisten in de toelichting** zijn niet gestructureerd uitgewerkt.
   We weten dát motivering nodig is bij > 5 jaar goodwill-afschrijving en bij
   afwijkende waarderingsregels en bij vrijstelling subconsolidatie, maar er
   is geen overzichtelijke "checklist toelichting".
6. **M&A casus-vaardigheid**: hoe je een acquisitie boekhoudkundig begeleidt
   (purchase price allocation in technische zin, due-diligence-input,
   eerste-consolidatie-werkprogramma) zit er niet in. Mogelijk hoort dat
   meer in PO 1.1 of in een audit-PO.

### 6.3 Verdict

**Voor een eerste leesronde, samenvatting en concept-overzicht is deze cursus
productie-waardig.** Voor *examenklaarheid* moet ze worden gecomplementeerd
met:

- 5-10 numerieke oefencases (waarvan minstens 3 integrale consolidatie met
  intercompany, 2 step acquisition, 2 step disposal);
- een korte IFRS-extensie voor PO 1.4 II;
- een checklist toelichting / verslag.

---

## 7. NotebookLM/ChatGPT-bruikbaarheid

**Oordeel**: zeer bruikbaar.

Concrete argumenten:

- **Heldere kopstructuur** (17 hoofdstukken, sub-secties, tabellen, lijsten):
  NotebookLM kan hieruit zonder reorganisatie een hoorbare podcast genereren
  van ~30-45 minuten. Elk hoofdstuk staat op zichzelf.
- **Confidence-labels** (⚖️ / 🤖) en **bronverwijzingen** in de tekst geven
  NotebookLM een betrouwbaarheids-signaal om scharnierpunten ("dit moet je
  echt onthouden") te onderscheiden van afgeleide redeneringen.
- **Tabellen** zijn klaar voor infographic-generatie (3-percentages-tabel,
  drempel-tabel, BE-GAAP/IFRS-tabel, drie-methodes-tabel).
- **Vergelijkingsparen** uit de records leveren *ready-made* multiple-choice
  oefenvragen ("Welk verschil tussen X en Y?").
- **Stappenplannen** (§16, §12, §7.2, §8) zijn perfect voor
  flashcards/checklists.

**Verbeterpunten voor NotebookLM/ChatGPT-gebruik**:

- Voeg een **JSON-companion-bestand** toe met de drempels en formules
  (machine-leesbaar). NotebookLM is dan ook bruikbaar voor cijfer-Q&A.
- Voor **podcast-formaat**: een lijst suggestieve discussievragen aan het
  einde zou helpen ("Casus: M heeft 65 % van A en 45 % van B; welke
  methodes?").
- Voor **oefenvragen-generatie via ChatGPT**: een aparte sectie "vraagstof
  per onderdeel" met de 7-8 typische vraagstijlen (open-uitleg,
  controlepercentage-keten, methode-keuze, intercompany-eliminatie,
  consolidatieverschil-berekening, goodwill-vs-statutair, drempel-toets,
  consortium-toets) zou de prompts-engineering vergemakkelijken.

---

## 8. Hoe pijnlijk was het om te schrijven?

Eerlijk: **niet pijnlijk**, maar ook **niet zonder schuurmomenten**.

- De juridische opbouw (hoofdstukken 1-5) ging vlot. De records leveren een
  rijke begrippenladder.
- De methodes (hoofdstuk 6) gingen ongelijk: vermogensmutatie was zalig om te
  schrijven (numeriek voorbeeld klaar), integrale en evenredige bleven
  abstract.
- Consolidatieverschil (hoofdstuk 7) was de meest *bevredigende* sectie om
  te schrijven — de record gaf me oorzaken, behandeling, valkuilen en een
  voorbeeld.
- Intragroep-eliminaties (hoofdstuk 8) waren frustrerend: de stappen waren
  er, maar ik bleef de hele tijd "elimineer X" zeggen zonder ooit te kunnen
  laten *zien* hoe.
- IFRS (hoofdstuk 14) is dun. De records geven minimale dekking.
- Cheatsheet (hoofdstuk 17) was makkelijk — alle hooks zaten al in eerdere
  hoofdstukken klaar.

**Geen enkel record was zo zwak dat ik moest weglaten wat ik had willen
zeggen**, behalve op het niveau van numerieke voorbeelden. De cursus heeft
nergens "⚠️ te verifiëren" moeten typen — dat is een goed teken voor de
conceptlaag.

---

## 9. Samenvattend oordeel over de conceptlaag

| Vraag | Oordeel |
|---|---|
| Is de conceptlaag rijk genoeg voor productie-waardige studiematerie? | **Ja**, voor concept-overzicht en eerste leesronde. |
| Voor examen-klaarheid? | **Bijna**: rekencasussen, intercompany-eliminatie-techniek en boekingen ontbreken. |
| Is de coherentie tussen records goed? | **Conceptueel ja, mechanisch niet** — `edges[]` is leeg. |
| Is het v1.2-schema voldoende? | **Ja, maar inconsequent toegepast**. `berekeningsmethode.concreet_voorbeeld` en `voorbeeld_inline` zijn de game-changers; ze moeten op meer records terechtkomen. |
| Welk veld levert het meeste schrijfwaarde op? | `vergelijkingsparen[]` — het structureert het hele examenvalkuilen-niveau. |
| Welk veld zou ik schrappen? | Geen. Alle gebruikte velden hadden minstens één toepassing. `tijdlijn[]` was niet nodig voor PO 1.4 maar kan voor andere PO's logisch zijn. |

**Aanbeveling voor v2-prompt-evolutie**: investeer in (a) numerieke
`concreet_voorbeeld`-bouwers voor *elke* methode-record, (b)
`edges[]`-populatie, (c) gelijktrekken van `in_praktijk[]`-rijkheid (sommige
records hebben 0, sommige 2-3 blokken — variatie is nu te groot).

---

*Einde reflectie. Geschat aantal woorden: ~1.450.*
