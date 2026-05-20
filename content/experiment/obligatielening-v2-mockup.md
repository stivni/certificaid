---
title: "Obligatielening (mockup v4)"
tags:
  - experiment
  - mockup
status: experimental
mockup: true
---

> **Dit is een mockup** ter sparring — vergelijk met [[obligatielening]].
> We testen accountant-bril vooraan, recursie in onderdelen, perspectieven
> per actor, en bronvermelding-na-blok.
>
> **Confidence-tekens** (per claim):
> ⚖️ uit wet · KB · CBN · norm (grounded)
> 🔗 redenering uit bronnen-context (inferred)
> 🧭 beroepswijsheid, geen harde regel (vuistregel)
> ⚠️ bron ontbreekt of nog te verifiëren

# Obligatielening

Een obligatielening is een **schuldfinanciering** waarbij een vennootschap
**verhandelbare schuldbewijzen** (obligaties) uitgeeft aan meerdere
beleggers — in plaats van te lenen bij één bank. De vennootschap ontvangt
het kapitaal bij uitgifte, betaalt jaarlijkse **coupons** (rente) tijdens
de looptijd, en betaalt het **nominale bedrag** terug op vervaldag.
Boekhoudkundig: schuld op rekening **170** onder schulden op meer dan
één jaar.

*Bron: [[CBN-2019-07]] · [[WVV#art-7-54]] e.v. · [[MAR#rubriek-17]]* ⚖️

## Wat er economisch echt gebeurt

De vennootschap leent geld van **veel kleine investeerders** in plaats
van één bank. Investeerders krijgen een **verhandelbaar** schuldbewijs:
ze kunnen hun positie verkopen aan derden zonder dat de vennootschap iets
merkt. Voor de vennootschap blijft het **pure schuld** — de obligatiehouder
wordt geen mede-eigenaar, krijgt een vaste of variabele rente, en moet
op vervaldag worden terugbetaald *ongeacht* de winstgevendheid.

Het verschil met een banklening zit dus **niet** in de boekhoudkundige aard
(beide zijn schulden op rekening 170), wel in drie eigenschappen die de
hele advisering bepalen:

1. **Verhandelbaarheid** — de schuldeiser kan veranderen tijdens de looptijd.
2. **Versplintering** — geen vaste tegenpartij om mee te onderhandelen.
3. **Niet-renegotieerbaarheid** — voorwaarden liggen vast in het prospectus;
   wijzigingen vereisen een vergadering van obligatiehouders.

## Wanneer kies je dit?

### Voor wie

🧭 middelgrote tot grote vennootschap met voldoende reputatie
of investeerderskring; voorspelbare cashflow over de hele looptijd.

*Niet voor KMO*: uitgifte-overhead (notariskosten, prospectus, bankcommissies)
maakt het onrendabel onder ongeveer € 5 miljoen — de vaste kosten worden
te zwaar t.o.v. de opbrengst.

### Wanneer wel inzetten

- **Bank-financiering verzadigd of strategisch ongewenst.**
  *Waarom:* obligatieleningen werken op een andere markt dan bankkrediet,
  en spreiden tegenpartij-risico — geen enkele schuldeiser kan de
  onderneming klemzetten.
- **Lange investeringshorizon (5–15 jaar) past bij vastgoed,
  infrastructuur, R&D-portefeuille.**
  *Waarom:* banken bieden zelden looptijden boven 7–10 jaar zonder zware
  zekerheidseisen; de obligatiemarkt wel.
- 🧭 **vaste rente vastleggen wanneer marktrente laag staat.**
  *Waarom:* je locked je financieringskost in voor 5+ jaar; bij een banklening
  is je rente vaak variabel of moet je hertekenen.

### Wanneer niet

- **Cashflow volatiel of seizoengebonden.**
  *Waarom:* coupon is *vast* — geen renegotiatie zoals bij bank. Eén misser
  op een coupondatum kan leiden tot opeisbaarheid van de hele lening.
- **Behoefte onder ~€ 5 miljoen of looptijd onder 3 jaar.**
  *Waarom:* uitgiftekosten + administratieve overhead per houder maken
  het onrendabel.
- **Wens tot flexibiliteit in vervroegde aflossing.**
  *Waarom:* tenzij een **call-clausule** wordt onderhandeld (zie
  [Call- en put-clausules](#call--en-put-clausules) onder Terugbetaling),
  zit je vast aan de looptijd.

### Hoofdrisico voor de klant

**Liquiditeitsklem op een coupondatum.** Anders dan bij een banklening kan
de vennootschap niet onderhandelen over uitstel; bij **betalingsverzuim**
(wanbetaling op een coupon of op de hoofdsom) treedt de vergadering van
obligatiehouders bijeen en kan **versnelde opeisbaarheid** van de hele
lening worden ingeroepen. *Bron: [[WVV#art-7-62]]* ⚖️

### Hoofdvoordeel voor de klant

**Vaste financieringskost over lange periode** + **volledig aftrekbare
rentelast** bij de vennootschap, in tegenstelling tot dividend dat uit
beschikbare winst moet en niet aftrekbaar is. *Bron: [[WIB92#art-49]]* ⚖️
⚠️ Interactie met **EBITDA-regel** ([[WIB92#art-198-1]]) bij hoge schuldgraad
nog te verifiëren.

## Hoe het werkt

### Drie hoofdelementen: nominaal, coupon, looptijd

Bij uitgifte beslist de vennootschap over drie parameters die de cashflow
volledig vastleggen. Alle drie staan in het **emissieprospectus**.

De drie parameters interageren. Hoger coupon → aantrekkelijker voor
beleggers → minder agio of disagio nodig (zie verder). Langere looptijd →
hogere onzekerheid voor de belegger → meestal hoger coupon vereist. De
adviseur stuurt op de **combinatie**, niet op één parameter afzonderlijk.

#### Nominale waarde

De nominale waarde is het bedrag dat op het obligatiebewijs staat en dat
de vennootschap op vervaldag terugbetaalt — typisch **€ 1.000 per obligatie**
of een veelvoud daarvan. 🧭 *Marktconventie, geen wettelijke verplichting.*

**Speelruimte:** kleine nominale waardes (€ 100) maken brede retail-distributie
mogelijk maar verhogen administratie per houder. Grote nominale (€ 100.000)
beperkt het publiek tot professionele beleggers en kan onder vrijstelling van
prospectusplicht vallen — ⚠️ drempels uit Prospectusverordening te verifiëren.

#### Couponrente

De **coupon** is de jaarlijkse vergoeding aan de belegger, uitgedrukt als
percentage van het nominale bedrag. Kan **vast** of **variabel** zijn,
en wordt **jaarlijks** of **semi-jaarlijks** betaald.

- **Vaste coupon:** voorspelbare last bij de vennootschap, voorspelbaar
  rendement bij de belegger. Aangewezen wanneer de onderneming
  budgettaire zekerheid wil.
- **Variabele coupon** (typisch Euribor + spread): renterisico verschuift
  van belegger naar vennootschap. Aangewezen wanneer onderneming verwacht
  dat marktrente daalt of een natuurlijke hedge heeft.

**Speelruimte:** ook **stapcoupon** mogelijk (oplopend percentage over de
jaren, om de last in beginjaren te beperken) en **nulcoupon** (geen tussentijdse
betaling — beleggers krijgen rendement enkel via aankoop onder pari + terugbetaling
aan pari op vervaldag). Inflatie-gekoppelde coupons bestaan ook maar zijn in
België zeldzaam.

#### Looptijd

Typisch **5 tot 15 jaar**; kan oplopen tot 30 jaar bij infrastructuurfinanciering.

- **Korter** → lager renterisico voor de belegger, maar **herfinancieringsrisico**
  voor de vennootschap op vervaldag.
- **Langer** → hoger coupon vereist (om beleggers te compenseren voor renterisico),
  maar **financiële zekerheid** voor de vennootschap.

#### Voorbeeld (drie parameters samen)

> **Uitgeverij Ukkel NV** geeft 1.000 obligaties uit van € 1.000 nominaal =
> € 1.000.000 totaal. **Couponrente 4 % vast** per jaar = € 40.000
> jaarlijkse intrestlast. **Looptijd 8 jaar.**

---

### Uitgiftekosten

Bij elke obligatie-uitgifte komen kosten kijken: **notariskosten**,
**publicatie in Belgisch Staatsblad**, **bankcommissies** voor de
plaatsing, en eventueel **kosten van het prospectus**. Boekhoudkundig
komen die op rekening **201 "Kosten uitgifte leningen"** (een subrubriek
van oprichtingskosten).

**Bijzondere afschrijvingsregel.** Algemene regel voor oprichtingskosten
is afschrijving over **maximaal 5 jaar**. Voor kosten van uitgifte van een
obligatielening geldt een **uitzondering**: ze mogen worden gespreid over
de **hele looptijd** van de obligatielening — ook wanneer die langer is dan
5 jaar. *Bron: [[KB-WVV#art-3-37]]* ⚖️

> Deze regel is een **uitzondering op oprichtingskosten** —
> zie ook [[oprichtingskosten]] (sectie "uitzonderingen").

#### Voorbeeld + boekingen

> Uitgeverij Ukkel NV: uitgiftekosten **€ 12.000**, looptijd 8 jaar →
> jaarlijkse afschrijving **€ 1.500** (lineair).

**Bij uitgifte:**

| Debet | Credit | Rekening | Naam | Bedrag |
|:---:|:---:|---|---|---:|
| ✓ | | 201 | Kosten uitgifte leningen | 12.000 |
| | ✓ | 550 | Zichtrekening | 12.000 |

**Elk boekjaar:**

| Debet | Credit | Rekening | Naam | Bedrag |
|:---:|:---:|---|---|---:|
| ✓ | | 6300 | Afschrijvingen oprichtingskosten | 1.500 |
| | ✓ | 201 | Kosten uitgifte leningen | 1.500 |

#### Verplichting in toelichting jaarrekening

De **keuze voor spreiding over de looptijd** (i.p.v. de standaard
5-jaarsregel) moet **expliciet vermeld** worden in de waarderingsregels
en de toelichting bij de jaarrekening. *Bron: [[KB-WVV#art-3-37]]* ⚖️

#### Valkuilen

- 📋 *Boekhouder* — uitgiftekosten **niet of niet correct spreiden** bij looptijd
  > 5 jaar → resultaat van jaar 1 vertekend met grote eenmalige kost; spreiding
  in toelichting niet vermeld. *Bron: [[KB-WVV#art-3-37]]* ⚖️

---

### Uitgifte aan pari, beneden pari (disagio) of boven pari (agio)

De obligatie heeft een **nominale waarde** (pari, bv. € 1.000) die op het
bewijs vermeld staat. Dat is het bedrag dat op vervaldag wordt terugbetaald.
Maar de **uitgifteprijs** — wat beleggers daadwerkelijk betalen bij uitgifte —
kan daarvan afwijken: **lager** (disagio) of **hoger** (agio).

#### Wat er economisch echt gebeurt

De couponrente die op het bewijs staat is **niet** het werkelijke rendement
voor de belegger noch de werkelijke financieringskost voor de vennootschap.
Zodra de uitgifteprijs afwijkt van pari, schuift het echte rendement weg
van de couponrente:

- **Disagio** (uitgifte < pari): vennootschap ontvangt minder dan ze
  terugbetaalt → belegger krijgt extra rendement bovenop de coupon →
  vennootschap betaalt **méér** dan de couponrente doet vermoeden.
- **Agio** (uitgifte > pari): omgekeerd — belegger betaalt premium en
  krijgt minder rendement; vennootschap krijgt extra cash bij uitgifte
  en de werkelijke financieringskost ligt **lager** dan de coupon suggereert.

De couponrente is **het rapporteringsgezicht**; de uitgifteprijs is **de
correctie naar de marktwaarde**. Wat de markt eist als rendement bepaalt
welke combinatie van coupon + uitgifteprijs nodig is om de obligatie
geplaatst te krijgen.

#### Disagio (uitgifte beneden pari)

De belegger betaalt minder dan nominaal; de vennootschap betaalt op
vervaldag het volle nominale bedrag terug. Het verschil is een
**uitgestelde financieringskost** die de vennootschap **spreidt over de
looptijd**. *Bron: [[KB-WVV#art-3-37]]* ⚖️

##### Voorbeeld + berekening

NV ABC geeft 1.000 obligaties uit, nominaal € 1.000/stuk, coupon 3 %,
looptijd 5 jaar, uitgifteprijs **€ 950** (95 % van pari):

| | Bedrag |
|---|---:|
| Ontvangen cash bij uitgifte | € 950.000 |
| Schuld op balans (terug te betalen) | € 1.000.000 |
| **Disagio** (over te dragen, te spreiden 5 jaar) | **€ 50.000** |
| Jaarlijkse couponuitgave | € 30.000 |
| Jaarlijkse disagio-amortisatie (lineair) | € 10.000 |
| **Werkelijke jaarlijkse financieringskost** | **€ 40.000** |

Werkelijke kost ≈ € 40.000 / € 950.000 ≈ **4,2 %** — niet de 3 % die op
het bewijs staat.

##### Voorbeeld boeking — bij uitgifte

| Debet | Credit | Rekening | Naam | Bedrag |
|:---:|:---:|---|---|---:|
| ✓ | | 550 | Zichtrekening | 950.000 |
| ✓ | | 4901 | Over te dragen disagio | 50.000 |
| | ✓ | 170 | Obligatielening | 1.000.000 |

##### Voorbeeld boeking — elk boekjaar

| Debet | Credit | Rekening | Naam | Bedrag |
|:---:|:---:|---|---|---:|
| ✓ | | 6500 | Rentelasten — disagio | 10.000 |
| | ✓ | 4901 | Over te dragen disagio | 10.000 |
| ✓ | | 6500 | Rentelasten — coupon | 30.000 |
| | ✓ | 550 | Zichtrekening | 30.000 |

##### Balans — snapshots

**T₀ — vóór uitgifte (verkort, relevante rubrieken)**

| Actief | | Passief | |
|---|---:|---|---:|
| 55 Liquide middelen | 0 | 17 Schulden > 1 j | 0 |
| 49 Overlopende rek. | 0 | | |

**T₀ — onmiddellijk na uitgifte**

| Actief | | Passief | |
|---|---:|---|---:|
| 55 Liquide middelen | +950.000 | 17 Schulden > 1 j (170) | +1.000.000 |
| 490x Over te dragen disagio | +50.000 | | |

**T₅ — na laatste coupon + aflossing**

| Actief | | Passief | |
|---|---:|---|---:|
| 55 Liquide middelen | −50.000 cumul.* | 17 Schulden > 1 j | 0 |
| 490x Over te dragen disagio | 0 | | |

*cumulatief netto: ontvangen 950.000 − 5×coupon 150.000 − aflossing 1.000.000.
RR-kost cumul over 5 jaar = 5 × 40.000 = 200.000.*

#### Agio (uitgifte boven pari)

De belegger betaalt méér dan nominaal. Het verschil is een **uitgestelde
opbrengst** die de vennootschap spreidt; die opbrengst **verlaagt** de
werkelijke couponlast.

##### Voorbeeld + berekening

Zelfde NV ABC, uitgifte aan **€ 1.050/stuk**:

| | Bedrag |
|---|---:|
| Ontvangen cash bij uitgifte | € 1.050.000 |
| Schuld op balans | € 1.000.000 |
| **Agio** (over te dragen opbrengst) | **€ 50.000** |
| Jaarlijkse couponuitgave | € 30.000 |
| Jaarlijkse agio-afname (vermindert kost) | − € 10.000 |
| **Werkelijke jaarlijkse financieringskost** | **€ 20.000** |

Werkelijke kost ≈ € 20.000 / € 1.050.000 ≈ **1,9 %**, ondanks coupon 3 %.

##### Voorbeeld boeking — bij uitgifte

| Debet | Credit | Rekening | Naam | Bedrag |
|:---:|:---:|---|---|---:|
| ✓ | | 550 | Zichtrekening | 1.050.000 |
| | ✓ | 170 | Obligatielening | 1.000.000 |
| | ✓ | 4902 | Over te dragen agio | 50.000 |

#### Speelruimte

- **Spreidingsmethode** agio/disagio: **lineair** (eenvoudig, in BGAAP
  algemeen aanvaard) versus **effective interest** (actuarieel zuiverder,
  beter aansluitend bij IFRS). Eenmaal gekozen: consistent toepassen.
- **Pari, agio of disagio zelf**: geen wettelijke keuze maar een
  **marktonderhandeling** — bepaald door de verhouding tussen couponrente
  en marktrente bij uitgifte.

#### Valkuilen

- 📋 *Boekhouder* — agio/disagio **niet correct spreiden** → resultaat van
  jaar 1 vertekend. *Bron: [[KB-WVV#art-3-37]]* ⚖️
- 🔍 *Auditor* — **spreidingsmethode niet consistent** toegepast over de
  jaren (wisselen tussen lineair en effective interest) → inbreuk op het
  consistency-beginsel.
- 📋 *Boekhouder* — bij **call-clausule activering**: de premie boven pari
  is geen rente maar een **kapitaalverlies**, vraagt eigen behandeling.

---

### Coupons en prorata-intrest

Couponbetalingen worden geboekt als financiële kosten op rekening **650**.
Tussen twee couponbetalingen door — als de balansdatum niet samenvalt met
een coupondatum — moet de **gelopen-maar-nog-niet-vervallen rente** prorata
worden geboekt op rekening **492 "Toe te rekenen kosten"**. *Bron:
[[CBN-148-4]] · [[KB-WVV#art-3-60]]* ⚖️

#### Wat er economisch echt gebeurt

Het **matching-beginsel** vereist dat de rentelast in het juiste boekjaar
staat, óók als ze pas later cash wordt betaald. Anders verschuift een hap
rentelast naar het verkeerde jaar en wordt het resultaat artificieel hoger
of lager. Cashstromen volgen het contract; boekhoudkundige kost volgt het
gebruik van de financiering in de tijd.

#### Voorbeeld + berekening

> Uitgeverij Ukkel NV: obligatie 4 % × € 1.000.000 = **€ 40.000 jaarlijkse
> coupon**, betaalbaar elke **1 juli**. Op **31 december** is 6 maanden
> gelopen sinds laatste betaling → **€ 20.000 toe te rekenen**.

Formule: *coupon × (dagen sinds laatste betaling / 365)* of equivalent
op maandbasis.

#### Voorbeeld boeking — balansdatum 31/12

| Debet | Credit | Rekening | Naam | Bedrag |
|:---:|:---:|---|---|---:|
| ✓ | | 6500 | Rentekosten obligatielening | 20.000 |
| | ✓ | 492 | Toe te rekenen kosten | 20.000 |

#### Voorbeeld boeking — volgende couponbetaling 1/7

| Debet | Credit | Rekening | Naam | Bedrag |
|:---:|:---:|---|---|---:|
| ✓ | | 6500 | Rentekosten (2e helft jaar) | 20.000 |
| ✓ | | 492 | Toe te rekenen kosten (afboeken) | 20.000 |
| | ✓ | 550 | Zichtrekening | 40.000 |

#### Valkuilen

- 📋 *Boekhouder* — **prorata vergeten** → matching-beginsel gebroken,
  rentelast in verkeerd jaar.
- 📋 *Boekhouder* — bij **variabele coupon**: prorata herrekenen op basis
  van de **geldende rentevoet op balansdatum**, niet op basis van de vorige
  coupon-uitbetaling.

---

### Terugbetaling op vervaldag

Op vervaldag betaalt de vennootschap het **nominale bedrag** terug aan
de obligatiehouders. Schuld wordt nul; liquide middelen verminderen.

#### Voorbeeld boeking

| Debet | Credit | Rekening | Naam | Bedrag |
|:---:|:---:|---|---|---:|
| ✓ | | 170 | Obligatielening | 1.000.000 |
| | ✓ | 550 | Zichtrekening | 1.000.000 |

#### Aflossing in tranches (sinking fund)

In plaats van het volle bedrag op vervaldag terug te betalen, kan de
vennootschap een **aflossingsschema** opnemen in het prospectus: jaarlijks
of periodiek wordt een deel van de obligaties uitgeloot en afgelost.

🧭 spreidt het cashflow-pieken-risico op vervaldag, maar maakt
de obligatie minder aantrekkelijk voor beleggers (kortere gemiddelde looptijd).

#### Call- en put-clausules

- **Call** = de **uitgever** heeft recht op vervroegde aflossing (vaak met
  premie boven pari). Aangewezen wanneer onderneming flexibiliteit wil bij
  dalende marktrente — kan herfinancieren goedkoper.
- **Put** = de **belegger** heeft recht op vervroegde verkoop terug aan de
  uitgever. Maakt obligatie aantrekkelijker voor beleggers, maar geeft een
  **liquiditeitsrisico** bij de vennootschap (mogelijk vervroegde uitgave).

#### Valkuilen

- 🧑‍💼 *Bestuurder* — **liquiditeitsklem op vervaldag** bij één grote
  terugbetaling → plan herfinanciering minstens 12–18 maanden vooraf, of
  overweeg sinking fund van bij uitgifte. 🧭
- 📋 *Boekhouder* — bij **call-clausule activering**: premie boven pari is
  geen rente maar **kapitaalverlies**; afzonderlijke behandeling.

---

## Perspectieven per actor

*De boekhoudkundige aspecten staan in detail bij elk onderdeel hierboven.
Hieronder per actor de samenvattende positie en fiscale gevolgen.*

### 🏢 Vennootschap-uitgever

**Globaal**: schuld op 170, uitgiftekosten op 201, agio/disagio op 4901/4902,
prorata op 492, rentelasten op 650.

**Fiscaal**: rentelasten (coupon + disagio-spreiding) zijn aftrekbare
beroepskost; agio-opname vermindert de aftrekbare last symmetrisch.
*Bron: [[WIB92#art-49]]* ⚖️ · Edge → [[aftrekbaarheid-financieringskosten]]

⚠️ **Te verifiëren**: interactie met **EBITDA-regel** ([[WIB92#art-198-1]])
bij hoge schuldgraad — overschrijdt het netto-financieringskost-saldo de
EBITDA-drempel, dan beperking aftrekbaarheid.

**Toelichting jaarrekening** *Bron: [[KB-WVV]]* ⚖️:
- vermelding obligatielening in toelichting bij rubriek 17
- spreidingsmethode agio/disagio in waarderingsregels
- vervalkalender van de schuld (afzonderlijk per tranche bij sinking fund)
- keuze voor spreiding uitgiftekosten over hele looptijd (zie [[oprichtingskosten]])

**Formaliteiten bij uitgifte** *Bron: [[WVV#art-7-54]] e.v.* ⚖️:
- besluit van het bestuursorgaan
- emissieprospectus of informatienota bij publieke uitgifte
  ⚠️ drempels uit Prospectusverordening te verifiëren
- vergadering van obligatiehouders bij wijziging voorwaarden
  *Bron: [[WVV#art-7-62]]* ⚖️

#### Stappenplan bij uitgifte

De accountant begeleidt typisch de boekhoudkundige en fiscale aspecten;
notaris en bank verzorgen de juridische uitgifte zelf. Het is wel nuttig
om de volledige sequentie te kennen — boekhoudkundige momenten zitten
verspreid over de hele stroom.

1. **Voorbereiding** — bestuur beslist over financieringsbehoefte;
   prospectus of informatienota wordt opgesteld door bank/advocaat;
   accountant levert input voor de financiële paragrafen (jaarrekeningen,
   cashflow-projecties).
2. **Besluit bestuursorgaan** — formeel goedgekeurd voorstel met nominaal,
   coupon, looptijd, eventuele agio/disagio en aflossingsmodaliteiten.
3. **Publicatie en plaatsing** — bekendmaking in *Belgisch Staatsblad*
   bij publieke uitgifte; effectieve plaatsing bij beleggers via bank-syndicaat.
4. **Ontvangst kapitaal en uitgifteboeking** *(zie [Voorbeeld + boekingen](#voorbeeld--boekingen)
   onder Uitgiftekosten en [Voorbeeld boeking — bij uitgifte](#voorbeeld-boeking--bij-uitgifte)
   onder Disagio/Agio).*
5. **Eerste boekingsroutine** — opzet spreidingstabel agio/disagio en
   uitgiftekosten; opzet prorata-aanslag in jaarafsluiting.
6. **Jaarlijkse routine** — couponbetaling, prorata, amortisatie agio/disagio,
   afschrijving uitgiftekosten *(zie onderdelen [Coupons en prorata-intrest](#coupons-en-prorata-intrest)
   en [Uitgiftekosten](#uitgiftekosten)).*
7. **Toelichting jaarrekening** — eerste boekjaar vermeldt de spreidings-
   en waarderingskeuzes (zie hierboven).
8. **Vervaldag** — terugbetaling nominaal *(zie [Terugbetaling op vervaldag](#terugbetaling-op-vervaldag)).*

🧭 *Deze stappen zijn een afzonderlijke competentie (`uitgeven-obligatielening
boekhoudkundig begeleiden`) maar geïntegreerd in dit record voor studie-overzicht
— zie [Wat dit record dekt](#wat-dit-record-dekt) onderaan.*

### 👤 Belegger — natuurlijke persoon (privé)

**Bij aankoop**: betaalt de uitgifteprijs (€ 950 / € 1.000 / € 1.050 in
ons voorbeeld). De aankoop zelf heeft geen aangifte-implicatie in de
personenbelasting.

**Tijdens looptijd**: ontvangt coupon = **roerend inkomen**. De
**roerende voorheffing** wordt ingehouden door de uitbetalende instelling
en is in principe **bevrijdend** (geen aangifte vereist als RV correct
ingehouden). *Bron: [[WIB92]] (artikel-precies te verifiëren)* ⚠️
Edge → [[roerende-voorheffing-rente]]

⚠️ **Tarief RV**: zie [Cijferzakboekje §X] — bron nog te laden.

⚠️ **Aangifte personenbelasting** — Deel 2, Vak VII (roerende inkomsten),
codes 1444/2444 voor opbrengsten *zonder* ingehouden RV (bv. buitenlandse
obligaties). Te verifiëren.

**Op vervaldag**: ontvangt het nominale bedrag terug. Verschil met de
aankoopprijs (€ 50 meerwaarde bij disagio, € 50 verlies bij agio):
⚠️ behandeling als roerend inkomen of als (vrijgestelde) meerwaarde —
afhankelijk van houderschapsregeling. Te verifiëren met fiscale bron.
Edge → [[meerwaarde-obligaties-prive]]

### 🏢💰 Belegger — vennootschap

**Boekhouding**: aankoop op rekening **51** (Vastrentende effecten — *noot:
"vastrentende" is de MAR-benaming maar omvat ook obligaties met variabele
coupon; te verifiëren bij CBN-advies*). Aan kostprijs; agio/disagio
**gespiegeld** aan de uitgever (over te dragen opbrengst/kost).

**Voorbeeld boeking — aankoop met disagio** (belegger betaalt € 950 voor
nominaal € 1.000):

| Debet | Credit | Rekening | Naam | Bedrag |
|:---:|:---:|---|---|---:|
| ✓ | | 51 | Vastrentende effecten — nominaal | 1.000 |
| | ✓ | 550 | Zichtrekening | 950 |
| | ✓ | 4902 | Over te dragen agio (op belegging) | 50 |

*De € 50 wordt over de looptijd als financiële opbrengst geboekt.*

**Fiscaal**: coupons + spreiding belastbaar als financiële opbrengst in
vennootschapsbelasting. Edge → [[vennootschapsbelasting-fin-opbrengst]]

## Veelvoorkomende verwarringen

- **DBI en rente.** [[DBI]] (Definitief Belaste Inkomsten — uitsluiting
  van dubbele belasting op dividenden) geldt **niet** voor rente uit
  obligaties. Rente is een gewone belastbare financiële opbrengst bij de
  ontvangende vennootschap, ongeacht de schuldenaar. Edge bij [[DBI]]:
  `niet_van_toepassing_op` → obligatielening-rente.
- **"Vastrentende effecten" (MAR rubriek 51).** De benaming impliceert
  niet dat de coupon vast is — ook obligaties met variabele coupon staan
  op deze rubriek. ⚠️ CBN-precisering te zoeken.
- **Couponrente ≠ werkelijk rendement.** Bij uitgifte buiten pari is het
  rendement voor de belegger (en de financieringskost voor de vennootschap)
  niet gelijk aan de coupon. Gebruik *yield-to-maturity* of equivalent voor
  vergelijking.
- **"Default" in obligatie-context.** "Default" verwijst hier naar
  **wanbetaling** (missed coupon of hoofdsom), niet naar een
  standaardinstelling.

## Alternatieven (zelfde doel)

Voor het doel **lange-termijn-financiering buiten bankkrediet**:
- [[banklening]] — eenvoudiger maar één vaste tegenpartij
- [[achtergestelde-lening]] — schuld met conventionele achterstelling
- [[converteerbare-obligatie]] — hybride met conversierecht naar aandelen
- [[winstdelende-lening]] — hybride met winst-gekoppelde coupon
- [[kapitaalverhoging]] — eigen vermogen i.p.v. schuld

→ Vergelijkingsmatrix: [[vergelijking-lange-termijn-financieringsinstrumenten]]

## Wat dit record dekt

*Een check-lijst voor toetsing — wat moet je hier na lezing kunnen? Elk
item linkt naar de plek waar het behandeld wordt. Per programmaonderdeel
kan een automatisch overzicht worden gebouwd uit deze labels.*

### Behandelde competenties

- **Een uitgegeven obligatielening boekhoudkundig verwerken** (uitgifte ·
  jaarlijkse routine · vervaldag) — zie [Hoe het werkt](#hoe-het-werkt) en
  [🏢 Vennootschap-uitgever](#-vennootschap-uitgever).
- **Een aangekochte obligatielening boekhoudkundig verwerken** (vanuit
  belegger-vennootschap) — zie [🏢💰 Belegger — vennootschap](#-belegger--vennootschap).
- **Prorata-intrest correct berekenen en boeken** — zie [Coupons en
  prorata-intrest](#coupons-en-prorata-intrest).
- **Uitgiftekosten correct spreiden** (uitzondering op 5-jaarsregel) — zie
  [Uitgiftekosten](#uitgiftekosten).
- **Agio en disagio correct verwerken** (lineaire vs effective interest
  spreiding) — zie [Uitgifte aan pari, beneden pari (disagio) of boven
  pari (agio)](#uitgifte-aan-pari-beneden-pari-disagio-of-boven-pari-agio).
- **Werkelijk rendement (YTM) berekenen** bij uitgifte buiten pari — zie
  berekeningen onder Disagio en Agio.
- **Een klant adviseren** over keuze obligatielening vs banklening en
  andere alternatieven — zie [Wanneer kies je dit?](#wanneer-kies-je-dit)
  en [Alternatieven](#alternatieven-zelfde-doel).
- **De boekhoudkundige stappen begeleiden bij uitgifte** — zie
  [Stappenplan bij uitgifte](#stappenplan-bij-uitgifte).
- **Fiscale gevolgen van een obligatielening inschatten** voor elk
  perspectief (uitgever · belegger NP · belegger venn.) — zie
  [Perspectieven per actor](#perspectieven-per-actor).

### Behandelde termen

[obligatie](#obligatielening) · [coupon](#couponrente) ·
[nominale waarde / pari](#nominale-waarde) · [agio](#agio-uitgifte-boven-pari) ·
[disagio](#disagio-uitgifte-beneden-pari) · [prorata-intrest](#coupons-en-prorata-intrest) ·
[stapcoupon](#couponrente) · [nulcoupon](#couponrente) ·
[sinking fund](#aflossing-in-tranches-sinking-fund) ·
[call-clausule · put-clausule](#call--en-put-clausules) ·
emissieprospectus · vergadering van obligatiehouders ·
wanbetaling (default) · werkelijk rendement (YTM)

### Behandelde formules

- **Prorata-intrest** = *coupon × (dagen sinds laatste betaling / 365)* —
  zie [Coupons en prorata-intrest](#coupons-en-prorata-intrest).
- **Werkelijke financieringskost bij disagio** = (coupon + lineaire
  amortisatie disagio) / ontvangen kapitaal — zie [Disagio](#disagio-uitgifte-beneden-pari).
- **Werkelijke financieringskost bij agio** = (coupon − lineaire afname
  agio) / ontvangen kapitaal — zie [Agio](#agio-uitgifte-boven-pari).

### Behandelde regimes (edges)

[aftrekbaarheid-financieringskosten](#-vennootschap-uitgever) ·
[ebitda-regel-198-1](#-vennootschap-uitgever) ⚠️ ·
[roerende-voorheffing-rente](#-belegger--natuurlijke-persoon-prive) ·
[meerwaarde-obligaties-prive](#-belegger--natuurlijke-persoon-prive) ⚠️ ·
[vennootschapsbelasting-fin-opbrengst](#-belegger--vennootschap)

## Bronnen en verwijzingen

**Bronnen (grounded)** ⚖️:
- [[CBN-2019-07]] — Boekhoudkundige verwerking obligatielening
- [[CBN-148-4]] — Prorata-intrest op schulden
- [[WVV#art-7-54]] e.v. — Uitgifte obligaties NV
- [[WVV#art-7-62]] — Vergadering obligatiehouders
- [[KB-WVV#art-3-37]] — Spreiding uitgiftekosten + agio/disagio
- [[KB-WVV#art-3-60]] — Toe te rekenen kosten
- [[MAR#rubriek-17]] — Schulden > 1 jaar
- [[MAR#rubriek-51]] — Vastrentende effecten
- [[WIB92#art-49]] — Aftrekbaarheid beroepskosten

**Te verifiëren** ⚠️:
- [[WIB92#art-198-1]] — EBITDA-regel, interactie met obligatie-rente
- RV-tarief op rente → [Cijferzakboekje]
- Prospectus-drempels uit EU-Prospectusverordening
- Meerwaarde-behandeling obligaties privé

**Cross-record edges**:
- `onderdeel_van` → [[schulden-op-meer-dan-een-jaar]]
- `is_uitzondering_op` → [[oprichtingskosten]] *(uitgiftekosten mogen
  gespreid over hele looptijd, niet 5 jaar)*
- `verward_met` → [[DBI]] *(rente valt niet onder DBI)*
- `gerelateerd` → [[converteerbare-obligatie]], [[banklening]],
  [[kapitaalverhoging]], [[oprichtingskosten]]
- `valt_onder_regime` → [[aftrekbaarheid-financieringskosten]],
  [[ebitda-regel-198-1]], [[roerende-voorheffing-rente]],
  [[meerwaarde-obligaties-prive]], [[vennootschapsbelasting-fin-opbrengst]]

---

## Iteratie-log

**v4 (huidige)** — wijzigingen t.o.v. v3:

- **Confidence-iconen passender**: ⚖️ blijft, 🔗 voor inferred (vervangt
  impliciet-redenering), 🧭 voor vuistregel (vervangt "*Vuistregel —*"
  prefix), ⚠️ blijft. Geen tekst-prefixes meer.
- **Stappenplan bij uitgifte** geïntegreerd als sub-sectie van het
  perspectief uitgever, met forward-links naar boekings-onderdelen.
  *Niet meer naar aparte competentie-fiche.*
- **Sectie "Wat dit record dekt"** toegevoegd: behandelde competenties,
  termen, formules, regimes — elk gelinkt naar de plek in het record.
  Per PO kan een script deze labels aggregeren.
- **Forward-link** bij "call-clausule" (eerste vermelding bij wanneer-niet)
  naar latere sub-sectie.
- **Stapcoupon · nulcoupon** krijgen 1-zins-uitleg ter plekke; sinking
  fund + call/put zijn elders al uitgewerkt — link via "Wat dit record
  dekt".
- **`verwart_met` → `verward_met`** (taalcorrectie).
- **"Vuistregel uit marktconventie"** notatie compacter (🧭 inline).

**v3 (vorige)** — t.o.v. v2:

- Volgorde: definitie → economische substantie → wanneer kies je dit →
  hoe het werkt → perspectieven → verwarringen → alternatieven → bronnen.
- Geen schema-jargon in body (geen `node_type`/`kind`-frontmatter zichtbaar).
- Bronvermelding na het blok (cursief, wikilinks).
- Rationale bij elke wanneer-regel en vuistregel.
- Boekingen in tabel-formaat met Debet/Credit-kolommen.
- Drie balansen apart (T₀ vóór, T₀ na, T_n).
- Speelruimte per onderdeel, niet als losse tabel.
- Verplichtingen formeel per onderdeel; valkuilen strikt als fouten.
- Veelvoorkomende verwarringen als eigen rubriek.
- Uitzondering op oprichtingskosten expliciet benoemd met edge.
- "Default" → "wanbetaling".
- PB-aangifte met deel/vak/code-placeholders bij belegger NP.
- Actor-emoji's consistent.
- MAR/CBN/WVV/WIB92 als wikilinks.
