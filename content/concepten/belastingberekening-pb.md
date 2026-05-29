---
title: "Belastingberekening personenbelasting"
concept_type: "procedure"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 2.2.III
  - 2.2.IV
  - 2.2.taak.1
tags:
  - concept
  - schema-2.2
  - type-procedure
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/belastingberekening-pb.json"
---

_Procedure_ · afk: **BB PB** · ook: PB-berekening · calcul de l'impôt IPP

## Definitie

De belastingberekening personenbelasting is de procedure waarbij — vertrekkend van de in de aangifte gerapporteerde belastbare inkomsten — de wettelijke cascade van WIB92 wordt toegepast om de netto-aanslag PB te bepalen. De cascade verloopt in 7 hoofdstappen: (1) belastbaar inkomen vaststellen per echtgenoot (afzonderlijke vaststelling bij gemeenschappelijke aanslag — art. 126 §1); (2) tariefschijven art. 130 toepassen (5 progressieve schijven 25-40-45-50 %); (3) belastingvrije som + gezinslast-verhogingen verminderen; (4) federale belastingverminderingen (giften, pensioensparen, ...); (5) gewest-verminderingen; (6) afzonderlijke tarieven art. 171 voor bijzondere inkomsten; (7) aanvullende gemeentebelasting (% × federale belasting Staat) + voorheffingen-aanrekening = netto-aanslag.

<small>📖 WIB92 — art. 6 — _wettekst_ · WIB92 — art. 130 — _wettekst_ · WIB92 — art. 126 §1 — _wettekst_ · WIB92 — art. 466 — _wettekst_</small>

## Substantie

De PB-cascade is sequentieel en niet-omkeerbaar: elke stap voedt de volgende. Het opvallende kenmerk vs VenB is de progressiviteit (5 oplopende schijven) gecombineerd met gezinscorrecties (belastingvrije som verhoogt per kind ten laste) en bron-differentiatie (stopzettingsmeerwaarden of dividenden krijgen afzonderlijk tarief om confiscatoir effect te vermijden). Voor gehuwden/wettelijk-samenwonenden geldt het beginsel 'afzonderlijke vaststelling, gemeenschappelijke aanslag' (art. 126 §1): elke echtgenoot heeft zijn eigen tariefschijven en eigen belastingvrije som, maar de aanslag wordt op één enkel biljet gevestigd. Daarop kan dan het huwelijksquotient grijpen om asymmetrische inkomens te corrigeren. Het samenspel met gewest-bevoegdheid (6de staatshervorming): een deel van de verminderingen valt onder gewestelijke bevoegdheid (woon-bonus historisch Vlaanderen) — vandaar verschillen in netto-aanslag tussen gewesten bij gelijk inkomen.

<small>🔗 WIB92 — art. 130 — _wettekst_ · WIB92 — art. 126 §1 — _wettekst_ · WIB92 — art. 171 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

De berekening is een mathematische vertaling van de fiscale principes: progressiviteit (steeds hogere tarieven op hogere inkomensgedeelten) + gezinsfilter (belastingvrije som corrigeert voor minimum-bestaansniveau) + bron-correctie (afzonderlijke tarieven voorkomen dat 'occasionele' inkomsten zoals stopzettingsmeerwaarden in de hoogste schijf vallen) + autonome niveaus (gemeente-opcentiemen geven lokale democratische controle op fiscale druk). De cascade is wettelijk vastgelegd in een precieze volgorde — afwijking is niet toegestaan. Voor de fiscus is dit een gestandaardiseerde berekening die in software (Tax-Calc) wordt uitgevoerd; voor de accountant is het belangrijk de stappen te kennen om aanslagbiljetten te controleren én cliënten te kunnen adviseren over het marginaal tarief-effect van extra inkomen of aftrek.

<small>🔗 WIB92 — art. 130 — _wettekst_ · WIB92 — art. 131 — _wettekst_ · WIB92 — art. 171 — _wettekst_ · WIB92 — art. 468 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: WIB92 art. 6-178 (PB-berekening) + KB/WIB92 (indexering)

Stabiele cascade-structuur sinds WIB92. Jaarlijkse indexering van schijf-grenzen + BVS + verminderingsplafonds via Cijferzakboekje. Belangrijke wijziging: 6de staatshervorming (BW 6-1-2014) — gewest-bevoegdheid voor woon-bonus + gewestelijke verminderingen sinds AJ 2015.

**✅ Voor**
- 🔗 Elke PB-aangifte: de fiscus voert de berekening uit, de accountant kan ze controleren of vooraf simuleren in advies-context (bv. 'wat is de fiscale impact van een loonsverhoging?').

**▶️ Trigger start**
- 🔗 Indiening van aangifte triggert de berekening door fiscus. Voor de accountant: voorbereiding van de aangifte triggert al een simulatie via boekhoud-/aangifte-software (Tax-Calc-equivalent).

**⏹ Trigger einde**
- 🔗 Berekening eindigt met de netto-aanslag = vertrekpunt inkohiering + aanslagbiljet.

## Bouwstenen

### 👣 Stap 1: belastbaar inkomen vaststellen

Vertrekpunt: het belastbaar inkomen — vastgesteld als totaal netto-inkomen (som van 4 categorieën, art. 6) minus aftrekbare bestedingen (onderhoudsuitkeringen, etc.). Bij gemeenschappelijke aanslag: afzonderlijke vaststelling per echtgenoot (art. 126 §1) — de inkomsten worden per echtgenoot toegerekend conform de aangifte; daarna kan het huwelijksquotient grijpen om asymmetrische beroepsinkomens te corrigeren (toerekening max 30 % van het beroepsinkomen van de hoogstverdiener aan de minst-verdienende, begrensd door geïndexeerd plafond).

<small>📖 WIB92 — art. 6 — _wettekst_ · WIB92 — art. 87 — _wettekst_ · WIB92 — art. 126 §1 — _wettekst_</small>

### 👣 Stap 2: tariefschijven art. 130 toepassen

Op het belastbaar inkomen (per echtgenoot) worden 5 progressieve tariefschijven toegepast (art. 130 WIB92, jaarlijks geïndexeerd). Niet-geïndexeerde basisbedragen (AJ 2026 illustratief): 25 % tot ~10.580 EUR, 40 % van 10.580 tot ~15.000, 45 % van 15.000 tot ~26.830, 50 % boven ~26.830. De exacte geïndexeerde schijven raadplegen in het Cijferzakboekje. Resultaat = 'basisbelasting Staat' (vóór verminderingen).

<small>📖 WIB92 — art. 130 — _wettekst_</small>

### 👣 Stap 3: belastingvrije som + gezinslast-verhogingen

Op de basisbelasting wordt een vermindering toegepast die overeenkomt met de belasting die zou verschuldigd zijn op de belastingvrije som (BVS — art. 131 WIB92, geïndexeerd basisbedrag ~10.150 EUR AJ 2026). De BVS wordt verhoogd per kind ten laste (art. 132 — voor 1 kind +1.690, voor 2 kinderen +4.340, voor 3 +9.730, oplopend) en voor andere persoonsgebonden situaties (handicap, ouderdom > 65, alleenstaande met kind ten laste). Berekening: BVS wordt belast volgens de OMGEKEERDE schijven-volgorde — eerste 'gratis' tegen 25 %-tarief, daarna 40 %, etc. Deze vermindering wordt afgetrokken van de basisbelasting → 'federale basisbelasting na BVS'. Verhoging per kind wordt toegerekend aan de echtgenoot met hoogste belastbaar inkomen (art. 134 §4) — niet aan de keuze van de belastingplichtige.

<small>📖 WIB92 — art. 131 — _wettekst_ · WIB92 — art. 132 — _wettekst_ · WIB92 — art. 134 — _wettekst_</small>

### 👣 Stap 4: federale belastingverminderingen

Federale verminderingen op de federale basisbelasting na BVS (art. 145/1 e.v.): pensioensparen (30 % × storting max ~990/1.270 EUR), giften (45 % × bedrag ≥ 40 EUR per organisatie), dienstencheques (gewestelijk — geïntegreerd), kinderoppas, energiebesparende investeringen, etc. Elke vermindering heeft eigen voorwaarden + plafond. Cumulatie mogelijk, maar nooit méér dan de federale basisbelasting (geen 'negatieve belasting' behalve voor specifieke fiscale werkbonus art. 289ter). Vermindering werknemers + werklozen + pensioenen art. 154 (bijkomende vermindering bij lage inkomens) wordt afzonderlijk berekend.

<small>📖 WIB92 — art. 145/1 e.v. — _wettekst_ · WIB92 — art. 154 — _wettekst_</small>

### 👣 Stap 5: gewestelijke belastingverminderingen

Sinds de 6de staatshervorming (BW 6-1-2014) heeft elk gewest bevoegdheid over bepaalde belastingverminderingen + kortingen op de PB. Vlaanderen: woon-bonus geleidelijk uitgedoofd (eigen woning gekocht ≥ 2020 = geen woon-bonus meer), gewestelijke jobkorting. Wallonië: vermindering eigen woning verschillende voorwaarden. Brussel: hypotheekbonus afgeschaft sinds AJ 2017. De gewest-vermindering wordt afgetrokken van het 'gewestelijk gedeelte' van de federale belasting — een rekentechnisch onderscheid dat de fiscus automatisch verwerkt. Resultaat = totale federale basisbelasting na alle verminderingen.

<small>🔗 Bijzondere Wet 6 januari 2014 — art. 5/1 e.v. — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 👣 Stap 6: afzonderlijke tarieven art. 171

Bepaalde inkomsten worden NIET tegen het progressieve tarief belast maar tegen een vlak afzonderlijk tarief (art. 171 WIB92) — om confiscatoire effecten van occasionele/grote inkomsten te vermijden. Belangrijkste afzonderlijke tarieven: (a) 33 % — diverse inkomsten art. 90 1° (occasionele winst, prijzen), korte-termijn-meerwaarden binnen 5 jaar, achterstallen door overheidsschuld; (b) 16,5 % — stopzettingsmeerwaarden op niet-immateriële vaste activa bij stopzetting > 60 jaar of overlijden, kapitalen pensioenkapitaal indien aan voorwaarden voldaan; (c) 10 % — bepaalde groepsverzekering-kapitalen; (d) 8 % — pensioensparen-kapitaal bij normale uitkering; (e) gemiddelde aanslagvoet — bij vergoedingen tot herstel van tijdelijke derving (art. 171 5°). De afzonderlijke aanslag wordt geïsoleerd berekend en toegevoegd aan de globaal-berekende belasting.

<small>📖 WIB92 — art. 171 1° — _wettekst_ · WIB92 — art. 171 2° — _wettekst_ · WIB92 — art. 171 5° — _wettekst_</small>

### 👣 Stap 7: aanvullende gemeentebelasting + voorheffingen

Aanvullende gemeentebelasting: berekeningsgrondslag (art. 466 WIB92) = federale belasting Staat na ALLE verminderingen — daarop wordt het gemeentelijk tarief (uniform, max 1 decimaal, typisch 0-9 %) toegepast (art. 468). Geen vermindering toepasbaar op gemeentebelasting (art. 468 lid 3). Resultaat = totaal verschuldigd. Daarop worden verrekend: bedrijfsvoorheffing (BV — aan bron geheven op lonen/pensioenen), roerende voorheffing (RV — indien geopteerd voor globale belasting van dividenden via aangifte), voorafbetalingen (zelfstandigen/bedrijfsleiders), dienstcheque-attesten als belastingkrediet, etc. Netto-saldo = wat de belastingplichtige effectief moet betalen of terugkrijgen.

<small>📖 WIB92 — art. 466 — _wettekst_ · WIB92 — art. 468 — _wettekst_</small>

### 📜 Samenvoeging echtgenoten + wettelijk-samenwonenden

Beginsel art. 126 §1: bij gemeenschappelijke aanslag wordt de belasting afzonderlijk vastgesteld per echtgenoot (eigen belastingvrije som, eigen schijven), maar in één enkele aanslag samengebracht. Wettelijk samenwonenden (art. 2 — 2° WIB92, voor het PB-fiscaal gelijkgesteld met gehuwden sinds AJ 2005) krijgen dezelfde behandeling. Uitsluitingen gemeenschappelijke aanslag (art. 126 §2): jaar van huwelijk/verklaring, jaar van scheiding, jaar van overlijden, jaar na feitelijke scheiding indien afzonderlijk gehuisvest — in die jaren afzonderlijke aanslagen. Tijdens gemeenschappelijke aanslag kan het huwelijksquotient grijpen om asymmetrische inkomens te corrigeren.

<small>📖 WIB92 — art. 126 §1 — _wettekst_ · WIB92 — art. 126 §2 — _wettekst_ · WIB92 — art. 2 — 2° — _wettekst_</small>

### ⚙️ Vrijstelling met progressievoorbehoud art. 155

Wanneer een rijksinwoner buitenlands inkomen heeft dat onder een dubbelbelastingverdrag (DBV) is vrijgesteld in België (typisch arbeidsinkomen art. 15 OESO-modelverdrag): art. 155 WIB92 past 'vrijstelling met progressievoorbehoud' toe. Berekenings-techniek: (a) berekening 1 = belasting op TOTAAL inkomen (Belgisch + vrijgesteld buitenlands); (b) berekening 2 = belasting op enkel Belgisch inkomen tegen het gemiddelde tarief van berekening 1. Resultaat: het buitenlandse inkomen 'duwt' het Belgisch inkomen in hogere schijven, maar wordt zelf niet effectief belast. Voor de stagiair: dit is een veelvoorkomend examenvalkuilpunt bij grensarbeiders.

<small>📖 WIB92 — art. 155 — _wettekst_</small>

## Voorbeelden

> [!example]- Werknemer alleenstaande — illustratieve cascade AJ 2026
> _Dhr. Maes, alleenstaande, brutoloon 50.000 EUR (BV 9.500). Geen andere inkomsten. Geen kinderen. Pensioensparen 990 EUR gestort. Woont in Antwerpen (gemeentebelasting 8 %)._
>
> **Berekening:**
>
> - Stap 1 — belastbaar inkomen: brutoloon 50.000 − forfait beroepskosten 5.520 = 44.480 EUR (afzonderlijke aanslag, geen huwelijksquotient)
> - Stap 2 — tariefschijven art. 130 (illustratieve geïndexeerde schijven AJ 2026): 25 % × 16.320 = 4.080 + 40 % × 12.500 = 5.000 + 45 % × 6.000 = 2.700 + 50 % × 9.660 = 4.830 = 16.610 EUR basisbelasting
> - Stap 3 — belastingvrije som: BVS ≈ 10.150 EUR → vermindering ≈ 25 % × 10.150 = 2.538 EUR; federale basisbelasting na BVS = 14.072
> - Stap 4 — federale vermindering pensioensparen: 30 % × 990 = 297 EUR; subtotaal = 13.775
> - Stap 5 — geen gewest-vermindering toepasbaar (geen woon-bonus voor huurder)
> - Stap 6 — geen afzonderlijke tarieven (alle inkomsten in globaal tarief)
> - Stap 7 — aanvullende gemeentebelasting Antwerpen 8 %: 13.775 × 8 % = 1.102 EUR; totaal verschuldigd = 14.877 EUR
> - Stap 8 — verrekening bedrijfsvoorheffing 9.500 EUR; saldo bij te betalen = 14.877 − 9.500 = 5.377 EUR
>
> → **Resultaat**: Effectief totaal tarief = 14.877 / 44.480 ≈ 33,4 %. Marginaal tarief op laatste euro = 54 % (50 % federaal + 8 % × 50 % gemeentelijk effectief). Cliënt-advies: extra brutoloon van 1.000 EUR kost in nominale termen 540 EUR aan belasting + sociale bijdragen — moeilijk economisch te rechtvaardigen. Stortting pensioensparen bracht 297 EUR vermindering = netto-kost 693 EUR voor 990 EUR sparen.
>
> <small>🔗 WIB92 — art. 130 — _wettekst_ · WIB92 — art. 131 — _wettekst_ · WIB92 — art. 145/8 — _wettekst_ · WIB92 — art. 466 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!example]- Tweeverdieners-gezin — huwelijksquotient + samenvoeging
> _Gezin Verboven: A (echtgenoot) brutoloon 70.000 EUR (BV 18.500), B (echtgenote) brutoloon 12.000 EUR (BV 800). 1 kind ten laste. Wonen in Brugge (gemeentebelasting 8 %)._
>
> | Stap | Echtgenoot A | Echtgenote B |
>
> | --- | --- | --- |
>
> | Beroepsinkomen netto na forfait | 64.480 (70.000 − 5.520) | 6.480 (12.000 − 5.520) |
>
> | Totaal beroepsinkomen samen | 70.960 EUR | — |
>
> | B's aandeel = 6.480 / 70.960 = 9,1 % → < 30 % → huwelijksquotient | — | — |
>
> | Aanvulling B tot 30 % = 21.288 − 6.480 = 14.808; geplafond op geïndexeerd plafond ≈ 13.050 | −13.050 | +13.050 |
>
> | Belastbaar inkomen na quotient | 51.430 | 19.530 |
>
> | Tarief art. 130 (illustratief) | 20.250 | 5.310 |
>
> | − BVS + verhoging 1 kind (toegerekend aan A = hoogstverdiener) | −4.000 | −2.540 |
>
> | Federale basisbelasting na BVS | 16.250 | 2.770 |
>
> | + Aanvullende gemeentebelasting 8 % | +1.300 | +222 |
>
> | Totaal per echtgenoot | 17.550 | 2.992 |
>
> | Gemeenschappelijke aanslag totaal | — | 20.542 |
>
> | − Bedrijfsvoorheffingen samen 19.300 | — | 1.242 bij te betalen |
>
> Belangrijk inzicht: zonder huwelijksquotient zou A 64.480 hebben en belast worden volledig in zijn hoogste schijven. Met quotient verschuift 13.050 EUR naar B die het tegen lagere schijven belast. Geschat voordeel huwelijksquotient hier ≈ 1.500-2.000 EUR per jaar. Verhoging BVS voor het kind wordt automatisch toegerekend aan A (hoogstverdiener, art. 134 §4) — de cliënt heeft hier geen keuze in.
>
> <small>🔗 WIB92 — art. 87 — _wettekst_ · WIB92 — art. 126 §1 — _wettekst_ · WIB92 — art. 132 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!example]- Zelfstandige stopzetting + meerwaarde — afzonderlijk tarief 16,5 %
> _Mevr. Lemoine, zelfstandige bakker, 62 jaar, verkoopt haar bakkerij bij stopzetting. Stopzettingsmeerwaarde op materiële vaste activa: 80.000 EUR. Daarnaast pensioen 18.000 EUR + winsten laatste jaar (afzonderlijk belast want stopzetting): 5.000 EUR._
>
> **Berekening:**
>
> - Globaal belast: pensioen 18.000 EUR (= belastbaar inkomen)
> - Tarief art. 130 op 18.000: 25 % × 16.320 + 40 % × 1.680 = 4.080 + 672 = 4.752
> - − BVS 25 % × 10.150 = 2.538 → federale basisbelasting na BVS = 2.214
> - − vermindering art. 154 voor pensioenen: ~440 EUR → federale basisbelasting = 1.774
> - + gemeentebelasting (stel 7 %) = 124 → globaal tarief deel = 1.898 EUR
> - Afzonderlijk belast: stopzettingsmeerwaarde 80.000 × 16,5 % = 13.200 EUR (art. 171 2° a — ≥ 60 jaar)
> - Afzonderlijk belast: stopzettingswinst laatste jaar 5.000 EUR — wordt belast tegen gemiddelde aanslagvoet (art. 171 5° c → c.q. tegen tarief van een vorig 'normaal' jaar) — vereenvoudigd hier illustratief 25 % = 1.250 EUR
> - Gemeentebelasting opcentiemen op afzonderlijke aanslag eveneens: 7 % × (13.200 + 1.250) = 1.012 EUR
> - Totaal verschuldigd PB = 1.898 + 13.200 + 1.250 + 1.012 = 17.360 EUR
>
> → **Resultaat**: Zonder afzonderlijke tarieven zou de stopzettingsmeerwaarde van 80.000 EUR volledig in de hoogste 50 %-schijf vallen → ~40.000 EUR belasting + opcentiemen ≈ 42.800 EUR. Het 16,5 %-tarief bespaart ca. 27.000 EUR — bedoeld om levenswerk-verkoop niet confiscatoir te belasten.
>
> <small>🔗 WIB92 — art. 171 2° a — _wettekst_ · WIB92 — art. 130 — _wettekst_ · aangifte-PB-2025-stopzetting — Tariefsamenvatting stopzettingsmeerwaarden vak XXI — _aangifte_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

> [!warning]- Marginaal tarief = effectief tarief verwarring
> **Verkeerde assumptie**: Bij een inkomen in de 50 %-schijf zit men globaal aan 50 % belasting.
>
> **Kernpunt**: Het marginaal tarief (op de laatste euro) ≠ effectief tarief (op totaal inkomen). Iemand met 70.000 EUR belastbaar inkomen zit marginaal aan 50 %, maar effectief rond 35 % (omdat lage schijven aan 25-40-45 % worden belast). Bij advisering: het marginaal tarief is wat telt voor extra-euro-beslissingen (loonsverhoging, optimalisatie); het effectief tarief is wat 'het kost' globaal.
>
> <small>🔗 WIB92 — art. 130 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!warning]- Vermindering op afzonderlijke aanslag toepassen
> **Verkeerde assumptie**: De belastingvrije som vermindert zowel de globale als de afzonderlijke aanslag.
>
> **Kernpunt**: De BVS-vermindering grijpt enkel op de globale aanslag (art. 130). De afzonderlijke aanslag (art. 171) wordt geïsoleerd berekend zonder BVS-vermindering. Dit verklaart waarom een 80.000 EUR stopzettingsmeerwaarde aan 16,5 % effectief 13.200 EUR kost zonder verdere reductie — geen 'gratis BVS' bovenop.
>
> <small>📖 WIB92 — art. 171 — _wettekst_</small>

> [!warning]- Niet-geïndexeerde bedragen uit WIB92 gebruiken in berekening
> **Verkeerde assumptie**: De schijven van art. 130 WIB92 (15.880 EUR, 28.080, etc. — niet-geïndexeerde basisbedragen) zijn de schijven die gelden in een berekening.
>
> **Kernpunt**: Alle bedragen in WIB92 (schijven, BVS, kindverhogingen, plafonds) zijn niet-geïndexeerde basisbedragen. Voor effectieve berekening MOET het Cijferzakboekje van het betrokken AJ geraadpleegd worden voor de geïndexeerde bedragen. Voor AJ 2026 zijn de schijven materieel hoger dan in WIB92 letterlijk.
>
> <small>🔗 WIB92 — art. 178 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!warning]- Vrijstelling DBV verwarren met aftrek
> **Verkeerde assumptie**: Buitenlands inkomen vrijgesteld door DBV wordt afgetrokken van het belastbaar inkomen.
>
> **Kernpunt**: Bij vrijstelling-met-progressievoorbehoud (art. 155): het buitenlands inkomen wordt MEE-GENOMEN in de berekening om het gemiddeld tarief te bepalen; het effectief belast Belgisch inkomen wordt dan tegen dat gemiddeld tarief belast. Niet aftrekken, maar tariefverhogend laten doorwerken. Dit is mathematisch fundamenteel verschillend van een aftrek.
>
> <small>📖 WIB92 — art. 155 — _wettekst_</small>

## Syntheses

### 🧩 Matrix

Belangrijkste tarieven personenbelasting AJ 2026 (illustratief — exacte cijfers Cijferzakboekje)

| Type tarief | Tarief | Toepassing |
| --- | --- | --- |
| Globaal art. 130 schijf 1 | 25 % | Eerste schijf belastbaar inkomen (~10.500 EUR) |
| Globaal art. 130 schijf 2 | 40 % | Tot ~15.000 EUR |
| Globaal art. 130 schijf 3 | 45 % | Tot ~26.800 EUR |
| Globaal art. 130 schijf 4 | 50 % | Boven ~26.800 EUR |
| Afzonderlijk art. 171 1° | 33 % | Diverse inkomsten art. 90 1°, korte-termijn-meerwaarden < 5 jaar |
| Afzonderlijk art. 171 2° a | 16,5 % | Stopzettingsmeerwaarden ≥ 60 jaar of overlijden, op materiële activa |
| Afzonderlijk art. 171 2° | 10 % | Bepaalde aanvullende pensioenkapitalen bij normale uitkering |
| Afzonderlijk pensioensparen | 8 % | Pensioenspaar-kapitaal bij wettelijke pensionering |
| Bevrijdend RV | 30 % | Dividenden, interesten (boven plafond) — meestal niet aan te geven |
| Gemeentebelasting | 0-9 % | Opslag op federale belasting Staat na verminderingen (art. 466-468) |

## Accountant-perspectieven

### Eigen kantoor — simulatie + advies

_De accountant die de berekening simuleert via boekhoud-/aangifte-software om cliënten te adviseren of aanslagbiljetten te controleren._

#### 💰 Fiscaal adviseur

##### 👣 Simulatie via Tax-Calc-equivalent software

Aangifte-software (Adsolut, BoB, Yuki, Octopus) heeft een ingebouwde Tax-Calc-module die de FOD-berekening reproduceert. Bij voorbereiding aangifte: vóór indiening de berekening simuleren om het verwachte saldo te kennen — vooral nuttig bij zelfstandigen (vermeerdering geen VA?), bij eerste-aangifte-na-pensioen (overgang BV → eigen voorheffing), bij internationale dimensie (progressievoorbehoud). Communiceer simulatie-resultaat aan cliënt vóór indiening om verrassingen te vermijden.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 🧭 Adviseur

##### 🧭 Adviseren op basis van marginaal tarief

Bij elke fiscale advies-vraag (loonsverhoging, optimalisatie via giften/pensioensparen, vrijwillige verhoging belastbaar inkomen door verkoop ...) eerst het marginaal tarief van de cliënt bepalen — dat is het tarief op de 'volgende euro'. Een cliënt in de 50 %-schijf met 50 % gemeentelijk × hoog effectief gemeentebelasting-tarief zit marginaal aan ~54 %. Bij sparen via pensioensparen: 30 % federale vermindering minus 54 % marginaal effect = netto 24 % winst — typisch wel aantrekkelijk. Bij een dividend-keuze (RV bevrijdend 30 % vs globaal): vergelijk marginaal globaal tarief met de 30 % RV-tarief.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

##### 📜 Advies stopzetting na 60 — afzonderlijk tarief 16,5 %

Bij zelfstandige cliënten die overweegen te stoppen met hun activiteit: leeftijd 60 is fiscaal scharniermoment. Stopzettingsmeerwaarden op niet-immateriële activa worden boven 60 belast aan 16,5 % afzonderlijk tarief (art. 171 2° a) — onder 60 aan 33 % of globaal. Een stopzetting net vóór 60-ste verjaardag kan dus aanzienlijk duurder zijn. Adviseer om het stopzettings-moment te plannen rekening houdend met dit drempeleffect — eventueel met overdracht via successiestructuur of vennootschap als alternatief.

<small>📖 WIB92 — art. 171 2° a — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Aangifte als input (vakken/codes) → [[aangifte-pb]] _(moet-verwijzen)_
- → Aanslagbiljet als output → [[aanslagbiljet-pb]] _(moet-verwijzen)_
- → Belastingvrije som-mechaniek + gezinslast → [[belastingvrije-som]] _(moet-verwijzen)_
- → Aanvullende gemeentebelasting + gewest-decimes → [[aanvullende-gemeentebelasting-pb]] _(moet-verwijzen)_
- → Huwelijksquotient (sub-mechanisme samenvoeging) → [[huwelijksquotient]] _(moet-verwijzen)_
- ↪ Concrete schijfbedragen + tarieven (Cijferzakboekje) _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[personenbelasting]]
### `vereist`
- [[aangifte-pb]] — Aangifte-data (4 inkomenscategorieën, gezinslast, verminderingen) is input voor berekening.
### `triggert`
- [[aanslagbiljet-pb]] — Berekening resulteert in netto-aanslag die wordt ingekohierd + gecommuniceerd via aanslagbiljet.
### `bevat`
- [[huwelijksquotient]] — Sub-mechanisme in stap 1 (vaststelling belastbaar inkomen per echtgenoot).
- [[belastingvrije-som]] — Sub-mechanisme in stap 3.
- [[aanvullende-gemeentebelasting-pb]] — Sub-mechanisme in stap 7.
### `vergelijkbaar_met`
- [[belastbare-grondslag-vennootschapsbelasting]]
    - **Gelijkenissen**:
        - Beide concepten beschrijven de cascade van grondslag naar verschuldigde belasting
        - Beide kennen voorheffingen-aanrekening + voorafbetalingen + saldering
    - **Verschillen**:
        - PB-berekening = 7 stappen progressief + gezinsfilter + afzonderlijke tarieven; VenB = 8 bewerkingen + proportioneel tarief + DBI/innovatie-aftrek
        - PB heeft schijven 25-50 %; VenB heeft uniform 25 % (of 20 % KMO)
        - PB kent gemeentebelasting + gewest-verminderingen; VenB niet
        - PB-cascade is op fiscaal individu (afzonderlijk per echtgenoot) of fiscaal gezin; VenB op één rechtspersoon
    - ⚠️ **Verwarringsrisico**: Stagiair die VenB-cascade overdraagt naar PB-berekening of omgekeerd: structureel verschillende logica's, ondanks oppervlakkige analogieën.
