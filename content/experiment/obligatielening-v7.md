---
title: "Obligatielening — v7 (kanonieke template)"
tags:
  - experiment
  - mockup
status: experimental
mockup: true
linked_anchors:
  - "1.1.II.V"
  - "1.1.II.J"
  - "1.4.III.B"
---

> **Kanonieke template v7** — boekingen + balans volledig onder Rol van de
> accountant per perspectief × rol (chronologisch). Rekening-codes weg uit
> "Hoe het werkt". Generieke valkuilen verwezen naar kader-fiches.
> Element-vocabulaire toegepast (één concept · meerdere weergaven).
> Vergelijk met [[obligatielening-v4|v4]] · [[obligatielening-v5|v5]] ·
> [[obligatielening-v6|v6]]; overzicht: [[obligatielening-v2-mockup|alle versies]].
>
> **Confidence-tekens** (per claim):
> ⚖️ uit wet · KB · CBN · norm (grounded)
> 🔗 redenering uit bronnen-context (inferred)
> 🧭 beroepswijsheid, geen harde regel (vuistregel)
> ⚠️ bron ontbreekt of nog te verifiëren

# Obligatielening

Een **obligatielening** is een schuldfinanciering waarbij een vennootschap
**verhandelbare schuldbewijzen** (obligaties) uitgeeft aan meerdere
beleggers — in plaats van te lenen bij één bank. De vennootschap ontvangt
het kapitaal bij uitgifte, betaalt jaarlijkse **coupons** (rente) tijdens
de looptijd, en betaalt het **nominale bedrag** terug op vervaldag.

*Bron: [[CBN-2019-07]] · [[WVV#art-7-54]] e.v.* ⚖️

## Wat er economisch echt gebeurt

De vennootschap leent geld van **veel kleine investeerders** in plaats
van één bank. Investeerders krijgen een **verhandelbaar** schuldbewijs:
ze kunnen hun positie verkopen aan derden zonder dat de vennootschap iets
merkt. Voor de vennootschap blijft het **pure schuld** — de obligatiehouder
wordt geen mede-eigenaar, krijgt een vaste of variabele rente, en moet
op vervaldag worden terugbetaald *ongeacht* de winstgevendheid.

Het verschil met een banklening zit dus niet in de boekhoudkundige *aard*
(beide zijn schulden), wel in drie eigenschappen die de hele advisering
bepalen:

1. **Verhandelbaarheid** — de schuldeiser kan veranderen tijdens de looptijd.
2. **Versplintering** — geen vaste tegenpartij om mee te onderhandelen.
3. **Niet-renegotieerbaarheid** — voorwaarden liggen vast in het prospectus;
   wijzigingen vereisen een vergadering van obligatiehouders.

## Voorkennis & leespad

- **Lees eerst** (voorvereisten): [[matching-beginsel]] · [[oprichtingskosten]]
  · [[jaarrekening-structuur]]
- **Past binnen kader**: [[lange-termijn-financiering]]
- **Naast deze fiche relevant**: [[banklening]] (eenvoudiger alternatief)
  · [[converteerbare-obligatie]] (hybride variant)
- **Bij vervolgvragen** lees: [[winstdelende-lening]] · [[achtergestelde-lening]]
  · [[kapitaalverhoging]] (eigen-vermogen-alternatief)

## Wanneer kies je dit?

### Voor wie

🧭 Middelgrote tot grote vennootschap met voldoende reputatie of
investeerderskring; voorspelbare cashflow over de hele looptijd.

🧭 *Niet voor KMO* — uitgifte-overhead (notariskosten, prospectus,
bankcommissies) maakt het onrendabel onder ongeveer € 5 miljoen; de
vaste kosten worden te zwaar t.o.v. de opbrengst.

### Wanneer wel inzetten

- 🔗 **Bank-financiering verzadigd of strategisch ongewenst** —
  obligatieleningen werken op een andere markt dan bankkrediet en
  spreiden tegenpartij-risico; geen enkele schuldeiser kan de onderneming
  klemzetten.
- 🔗 **Lange investeringshorizon (5–15 jaar)** past bij vastgoed,
  infrastructuur, R&D-portefeuille — banken bieden zelden looptijden
  boven 7–10 jaar zonder zware zekerheidseisen; de obligatiemarkt wel.
- 🧭 **Vaste rente vastleggen wanneer marktrente laag staat** — je locked
  je financieringskost in voor 5+ jaar; bij een banklening is je rente
  vaak variabel of moet je hertekenen.

### Wanneer niet

- 🧭 **Cashflow volatiel of seizoengebonden** — coupon is *vast*, geen
  renegotiatie zoals bij bank. Eén misser op een coupondatum kan leiden
  tot opeisbaarheid van de hele lening.
- 🧭 **Behoefte onder ~€ 5 miljoen of looptijd onder 3 jaar** — uitgiftekosten
  + administratieve overhead per houder maken het onrendabel.
- 🔗 **Wens tot flexibiliteit in vervroegde aflossing** — tenzij een
  call-clausule wordt onderhandeld, zit je vast aan de looptijd.

### Hoofdrisico voor de klant

**Liquiditeitsklem op een coupondatum** — anders dan bij een banklening
kan de vennootschap niet onderhandelen over uitstel; bij **wanbetaling**
(missed coupon of hoofdsom) treedt de vergadering van obligatiehouders
bijeen en kan **versnelde opeisbaarheid** van de hele lening worden
ingeroepen.

*Bron: [[WVV#art-7-62]]* ⚖️

### Hoofdvoordeel voor de klant

**Vaste financieringskost over lange periode** + **volledig aftrekbare
rentelast** bij de vennootschap, in tegenstelling tot dividend dat uit
beschikbare winst moet en niet aftrekbaar is.

*Bron: [[WIB92#art-49]]* ⚖️
🔗 Interactie met de **EBITDA-regel** ([[WIB92#art-198-1]]) bij hoge
schuldgraad — ⚠️ effect te verifiëren.

## Hoe het werkt

*Conceptuele uitleg per onderdeel. De boekhoudkundige uitwerking met
cijfers, boekingen en balans-snapshots staat in
[Rol van de accountant](#rol-van-de-accountant), chronologisch per
moment-in-tijd.*

### Drie hoofdelementen: nominaal, coupon, looptijd

Bij uitgifte beslist de vennootschap over drie parameters die de cashflow
volledig vastleggen. Alle drie staan in het **emissieprospectus**.

🔗 De drie parameters interageren. Hoger coupon → aantrekkelijker voor
beleggers → minder agio of disagio nodig (zie verder). Langere looptijd →
hogere onzekerheid voor de belegger → meestal hoger coupon vereist. De
adviseur stuurt op de **combinatie**, niet op één parameter afzonderlijk.

#### Nominale waarde

De nominale waarde is het bedrag dat op het obligatiebewijs staat en dat
de vennootschap op vervaldag terugbetaalt — typisch **€ 1.000 per obligatie**
of een veelvoud daarvan.

🧭 *Marktconventie, geen wettelijke verplichting.*

**Speelruimte**: kleine nominale waardes (€ 100) maken brede
retail-distributie mogelijk maar verhogen administratie per houder. Grote
nominale (€ 100.000) beperkt het publiek tot professionele beleggers en
kan onder vrijstelling van prospectusplicht vallen — ⚠️ drempels uit
Prospectusverordening te verifiëren.

#### Couponrente

De **coupon** is de jaarlijkse vergoeding aan de belegger, uitgedrukt
als percentage van het nominale bedrag. Kan **vast** of **variabel** zijn,
en wordt **jaarlijks** of **semi-jaarlijks** betaald.

- 🔗 **Vaste coupon** — voorspelbare last bij de vennootschap, voorspelbaar
  rendement bij de belegger. Aangewezen wanneer de onderneming budgettaire
  zekerheid wil.
- 🔗 **Variabele coupon** (typisch Euribor + spread) — renterisico verschuift
  van belegger naar vennootschap. Aangewezen wanneer onderneming verwacht
  dat marktrente daalt of een natuurlijke hedge heeft.

**Speelruimte**: ook **stapcoupon** (oplopend percentage over de jaren,
om de last in beginjaren te beperken) en **nulcoupon** (geen tussentijdse
betaling — beleggers krijgen rendement enkel via aankoop onder pari +
terugbetaling aan pari op vervaldag). Inflatie-gekoppelde coupons bestaan
ook maar zijn in België zeldzaam.

#### Looptijd

Typisch **5 tot 15 jaar**; kan oplopen tot 30 jaar bij infrastructuurfinanciering.

- 🔗 **Korter** → lager renterisico voor de belegger, maar **herfinancieringsrisico**
  voor de vennootschap op vervaldag.
- 🔗 **Langer** → hoger coupon vereist (om beleggers te compenseren voor
  renterisico), maar **financiële zekerheid** voor de vennootschap.

#### Voorbeeld (drie parameters samen)

> **Uitgeverij Ukkel NV** geeft 1.000 obligaties uit van € 1.000 nominaal =
> € 1.000.000 totaal. **Couponrente 4 % vast** per jaar = € 40.000
> jaarlijkse intrestlast. **Looptijd 8 jaar.**

---

### Uitgiftekosten

Bij elke obligatie-uitgifte komen kosten kijken: **notariskosten**,
**publicatie in Belgisch Staatsblad**, **bankcommissies** voor de
plaatsing, en eventueel **kosten van het prospectus**.

**Bijzondere afschrijvingsregel.** De algemene regel voor oprichtingskosten
is afschrijving over **maximaal 5 jaar**. Voor kosten van uitgifte van een
obligatielening geldt een **uitzondering**: ze mogen worden gespreid over
de **hele looptijd** van de obligatielening — ook wanneer die langer is dan
5 jaar. *Bron: [[KB-WVV#art-3-37]]* ⚖️

> Deze regel is een **uitzondering op oprichtingskosten** — zie ook
> [[oprichtingskosten]] (sectie "uitzonderingen") en de edge
> `is_uitzondering_op` onderaan.

**Verplichting in toelichting jaarrekening** — de **keuze voor spreiding
over de looptijd** (i.p.v. de standaard 5-jaarsregel) moet **expliciet
vermeld** worden in de waarderingsregels en de toelichting bij de
jaarrekening. *Bron: [[KB-WVV#art-3-37]]* ⚖️

---

### Uitgifte aan pari, beneden pari (disagio) of boven pari (agio)

De obligatie heeft een **nominale waarde** (pari, bv. € 1.000) die op het
bewijs vermeld staat. Dat is het bedrag dat op vervaldag wordt terugbetaald.
Maar de **uitgifteprijs** — wat beleggers daadwerkelijk betalen bij uitgifte —
kan daarvan afwijken: **lager** (disagio) of **hoger** (agio).

#### Wat er economisch echt gebeurt

🔗 De couponrente die op het bewijs staat is *niet* het werkelijke rendement
voor de belegger noch de werkelijke financieringskost voor de vennootschap.
Zodra de uitgifteprijs afwijkt van pari, schuift het echte rendement weg
van de couponrente:

- **Disagio** (uitgifte < pari) — vennootschap ontvangt minder dan ze
  terugbetaalt → belegger krijgt extra rendement bovenop de coupon →
  vennootschap betaalt **méér** dan de couponrente doet vermoeden.
- **Agio** (uitgifte > pari) — omgekeerd: belegger betaalt premium en
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

#### Agio (uitgifte boven pari)

De belegger betaalt méér dan nominaal. Het verschil is een **uitgestelde
opbrengst** die de vennootschap spreidt; die opbrengst **verlaagt** de
werkelijke couponlast.

#### Speelruimte

- 🔗 **Spreidingsmethode** agio/disagio: **lineair** (eenvoudig, in BGAAP
  algemeen aanvaard) versus **effective interest** (actuarieel zuiverder,
  beter aansluitend bij IFRS). Eenmaal gekozen: consistent toepassen.
- 🔗 **Pari, agio of disagio zelf**: geen wettelijke keuze maar een
  **marktonderhandeling** — bepaald door de verhouding tussen couponrente
  en marktrente bij uitgifte.

#### Conceptuele valkuilen (denkfouten)

- 🧭 **Couponrente verwarren met werkelijk rendement**: bij uitgifte buiten
  pari is de couponrente niet gelijk aan het werkelijk rendement
  (yield-to-maturity). Wie alleen op coupon vergelijkt met banklening,
  zit fout — werkelijke kost (incl. agio/disagio + uitgiftekosten-spreiding)
  is wat telt.

> Uitvoerings-valkuilen (boekhouder vergeet spreiden, auditor controle
> consistency) staan onder
> [Rol van de accountant](#rol-van-de-accountant) per relevante rol-cel.

---

### Coupons en prorata-intrest

Couponbetalingen worden geboekt als financiële kosten. Tussen twee
couponbetalingen door — als de balansdatum niet samenvalt met een
coupondatum — moet de **gelopen-maar-nog-niet-vervallen rente** prorata
worden geboekt.

*Bron: [[CBN-148-4]] · [[KB-WVV#art-3-60]]* ⚖️

#### Wat er economisch echt gebeurt

🔗 Het **matching-beginsel** vereist dat de rentelast in het juiste boekjaar
staat, óók als ze pas later cash wordt betaald. Anders verschuift een hap
rentelast naar het verkeerde jaar en wordt het resultaat artificieel hoger
of lager. Cashstromen volgen het contract; boekhoudkundige kost volgt het
gebruik van de financiering in de tijd.

#### Formule

**Prorata-intrest** = *coupon × (dagen sinds laatste couponbetaling / 365)*

Equivalent op maandbasis als de couponbetaling op een vaste maand-datum
valt.

---

### Terugbetaling op vervaldag

Op vervaldag betaalt de vennootschap het **nominale bedrag** terug aan
de obligatiehouders. Schuld wordt nul; liquide middelen verminderen.

#### Aflossing in tranches (sinking fund)

In plaats van het volle bedrag op vervaldag terug te betalen, kan de
vennootschap een **aflossingsschema** opnemen in het prospectus: jaarlijks
of periodiek wordt een deel van de obligaties uitgeloot en afgelost.

🧭 Spreidt het cashflow-pieken-risico op vervaldag, maar maakt de
obligatie minder aantrekkelijk voor beleggers (kortere gemiddelde looptijd).

#### Call- en put-clausules

- **Call** = de **uitgever** heeft recht op vervroegde aflossing (vaak met
  premie boven pari). 🧭 Aangewezen wanneer onderneming flexibiliteit wil
  bij dalende marktrente — kan herfinancieren goedkoper.
- **Put** = de **belegger** heeft recht op vervroegde verkoop terug aan
  de uitgever. Maakt obligatie aantrekkelijker voor beleggers, maar geeft
  een **liquiditeitsrisico** bij de vennootschap (mogelijk vervroegde
  uitgave).

---

## Rol van de accountant

*De accountant zet verschillende hoeden op afhankelijk van voor wie hij
werkt. Hieronder per klant-perspectief de relevante rollen + takenpakket.*

### 🏢 Voor de uitgever-vennootschap

**Doorlopend voorbeeld** dat hieronder wordt uitgewerkt:

> **NV ABC** geeft 1.000 obligaties uit van € 1.000 nominaal = € 1.000.000.
> **Coupon 3 % vast**, jaarlijks betaalbaar op 1 juli. **Looptijd 5 jaar**.
> **Uitgiftekosten € 12.000** (notaris + publicatie + bankcommissie).
> Drie varianten van uitgifteprijs gerekend: pari (€ 1.000) · disagio
> (€ 950) · agio (€ 1.050).

#### 🎯 Adviseur

**Wat doe je**:
- 🧭 Keuze instrument vs alternatieven (banklening · kapitaalverhoging) op
  basis van looptijd-behoefte, cashflow-stabiliteit, schuldgraad
- 🧭 Structuur-advies: vast vs variabele coupon · looptijd · al-of-niet
  agio/disagio · call/put-clausules · sinking fund
- 🧭 Timing van uitgifte i.f.v. marktrente
- 🔗 Vergelijking op **werkelijke kost (YTM-niveau)**, niet alleen coupon
- 🧭 Stress-test op coupon-verplichting over hele looptijd

**Vergelijken met alternatieven**: zie kader [[lange-termijn-financiering]]
voor cross-instrument-keuze.

#### 📋 Boekhouder

##### Bij uitgifte (T₀)

**Variant 1 — uitgifte aan pari** (€ 1.000.000 ontvangen)

*Boeking*

| Rekening | Naam | Debet | Credit |
|---:|---|---:|---:|
| 550 | Zichtrekening | 1.000.000 | — |
| 170 | Obligatielening | — | 1.000.000 |

**Variant 2 — uitgifte met disagio** (€ 950.000 ontvangen, € 50.000 disagio)

*Berekening*

| | Bedrag |
|---|---:|
| Ontvangen cash | € 950.000 |
| Schuld op balans (terug te betalen) | € 1.000.000 |
| **Disagio** (over te dragen, spreiding 5 jaar) | **€ 50.000** |
| Jaarlijkse couponuitgave | € 30.000 |
| Jaarlijkse disagio-amortisatie (lineair) | € 10.000 |
| **Werkelijke jaarlijkse financieringskost** | **€ 40.000** |
| **Werkelijke kost (≈ YTM)** | **≈ 4,2 %** |

*Boeking*

| Rekening | Naam | Debet | Credit |
|---:|---|---:|---:|
| 550 | Zichtrekening | 950.000 | — |
| 4901 | Over te dragen disagio | 50.000 | — |
| 170 | Obligatielening | — | 1.000.000 |

**Variant 3 — uitgifte met agio** (€ 1.050.000 ontvangen, € 50.000 agio)

*Berekening*

| | Bedrag |
|---|---:|
| Ontvangen cash | € 1.050.000 |
| Schuld op balans | € 1.000.000 |
| **Agio** (over te dragen opbrengst) | **€ 50.000** |
| Jaarlijkse couponuitgave | € 30.000 |
| Jaarlijkse agio-afname (vermindert kost) | − € 10.000 |
| **Werkelijke jaarlijkse financieringskost** | **€ 20.000** |
| **Werkelijke kost (≈ YTM)** | **≈ 1,9 %** |

*Boeking*

| Rekening | Naam | Debet | Credit |
|---:|---|---:|---:|
| 550 | Zichtrekening | 1.050.000 | — |
| 170 | Obligatielening | — | 1.000.000 |
| 4902 | Over te dragen agio | — | 50.000 |

**Boeking uitgiftekosten** (alle varianten, € 12.000 op 5 jaar)

| Rekening | Naam | Debet | Credit |
|---:|---|---:|---:|
| 201 | Kosten uitgifte leningen | 12.000 | — |
| 550 | Zichtrekening | — | 12.000 |

*Balans-snapshot — direct na uitgifte (variant disagio)*

**Actief**

| Code | Naam | Bedrag |
|---:|---|---:|
| 55 | Liquide middelen | +938.000 |
| 201 | Kosten uitgifte leningen | +12.000 |
| 4901 | Over te dragen disagio | +50.000 |

**Passief**

| Code | Naam | Bedrag |
|---:|---|---:|
| 17 | Schulden > 1 jaar (rek. 170) | +1.000.000 |

*(950.000 ontvangen − 12.000 uitgiftekosten = 938.000 netto cash)*

##### Jaarlijks

**Coupon-betaling op 1 juli** (variant disagio, € 30.000 cash)

| Rekening | Naam | Debet | Credit |
|---:|---|---:|---:|
| 650 | Rentekosten obligatielening | 30.000 | — |
| 550 | Zichtrekening | — | 30.000 |

**Prorata-intrest op balansdatum 31/12** (6 maanden gelopen sinds 1 juli)

*Berekening*: 30.000 × (6/12) = **€ 15.000**

| Rekening | Naam | Debet | Credit |
|---:|---|---:|---:|
| 650 | Rentekosten obligatielening | 15.000 | — |
| 492 | Toe te rekenen kosten | — | 15.000 |

**Disagio-spreiding** (lineair, € 10.000/jaar)

| Rekening | Naam | Debet | Credit |
|---:|---|---:|---:|
| 650 | Rentelasten — disagio-spreiding | 10.000 | — |
| 4901 | Over te dragen disagio | — | 10.000 |

**Agio-amortisatie** (alleen variant 3, € 10.000/jaar — verlaagt rentelast)

| Rekening | Naam | Debet | Credit |
|---:|---|---:|---:|
| 4902 | Over te dragen agio | 10.000 | — |
| 650 | Rentelasten — agio-amortisatie | — | 10.000 |

**Afschrijving uitgiftekosten** (€ 12.000 / 5 = € 2.400/jaar)

| Rekening | Naam | Debet | Credit |
|---:|---|---:|---:|
| 6300 | Afschrijvingen oprichtingskosten | 2.400 | — |
| 201 | Kosten uitgifte leningen | — | 2.400 |

##### Op vervaldag (T₅)

| Rekening | Naam | Debet | Credit |
|---:|---|---:|---:|
| 170 | Obligatielening | 1.000.000 | — |
| 550 | Zichtrekening | — | 1.000.000 |

##### Uitvoerings-valkuilen voor de boekhouder

- ⚖️ Uitgiftekosten **niet of niet correct spreiden** bij looptijd > 5 j →
  resultaat van jaar 1 vertekend met grote eenmalige kost; spreidingskeuze
  niet vermeld in toelichting. *Bron: [[KB-WVV#art-3-37]]* ⚖️
- ⚖️ Agio/disagio **niet correct spreiden** → resultaat van jaar 1 vertekend.
- 🔗 **Prorata vergeten** → matching-beginsel gebroken, rentelast in
  verkeerd jaar.
- 🔗 Bij **variabele coupon**: prorata herrekenen op basis van de
  **geldende rentevoet op balansdatum**, niet op basis van de vorige
  coupon-uitbetaling.
- 🔗 Bij **call-clausule activering**: de premie boven pari is geen rente
  maar een **kapitaalverlies**, vraagt eigen behandeling.

#### ⚖️ Begeleider — stappenplan bij uitgifte

De accountant begeleidt typisch de boekhoudkundige en fiscale aspecten;
notaris en bank verzorgen de juridische uitgifte zelf. Het is wel nuttig
om de volledige sequentie te kennen.

1. **Voorbereiding** — bestuur analyseert financieringsbehoefte; prospectus
   of informatienota wordt opgesteld door bank/advocaat; accountant levert
   input voor de financiële paragrafen.
2. **Besluit bestuursorgaan** — formeel goedgekeurd voorstel met nominaal,
   coupon, looptijd, eventuele agio/disagio en aflossingsmodaliteiten.
3. **Publicatie en plaatsing** — bekendmaking in *Belgisch Staatsblad*
   bij publieke uitgifte; effectieve plaatsing bij beleggers via
   bank-syndicaat.
4. **Ontvangst kapitaal en uitgifteboeking** — zie [Bij uitgifte (T₀)](#bij-uitgifte-t).
5. **Eerste boekingsroutine** — opzet spreidingstabel agio/disagio en
   uitgiftekosten; opzet prorata-aanslag in jaarafsluiting.
6. **Jaarlijkse routine** — zie [Jaarlijks](#jaarlijks).
7. **Toelichting jaarrekening** — eerste boekjaar vermeldt de spreidings-
   en waarderingskeuzes.
8. **Vervaldag** — zie [Op vervaldag (T₅)](#op-vervaldag-t).

⚖️ *Bron:* [[WVV#art-7-54]] e.v.

##### Formaliteiten

- ⚖️ Besluit van het bestuursorgaan
- ⚖️ Emissieprospectus of informatienota bij publieke uitgifte
  ⚠️ drempels uit Prospectusverordening te verifiëren
- ⚖️ Vergadering van obligatiehouders bij wijziging voorwaarden
  *Bron: [[WVV#art-7-62]]* ⚖️

#### 💰 Fiscaal

**Aftrekbaarheid rentelasten** (coupon + disagio-spreiding):
aftrekbare beroepskost. *Bron: [[WIB92#art-49]]* ⚖️
Agio-opname vermindert aftrekbare last symmetrisch.
Edge → [[aftrekbaarheid-financieringskosten]]

⚠️ **EBITDA-regel** ([[WIB92#art-198-1]]): bij hoge schuldgraad kan het
netto-financieringskost-saldo de EBITDA-drempel overschrijden, met
beperking aftrekbaarheid tot gevolg. Te verifiëren.

**Toelichting jaarrekening** (fiscale impact gevolgd):
- vermelding obligatielening in toelichting bij rubriek 17
- spreidingsmethode agio/disagio in waarderingsregels
- vervalkalender van de schuld
- keuze voor spreiding uitgiftekosten over hele looptijd
  (zie [[oprichtingskosten]])

### 👤 Voor de belegger — natuurlijke persoon (privé)

#### 🎯 Adviseur

🧭 Obligatie als beleggingscomponent in portefeuille — risico/return,
diversificatie t.o.v. aandelen, looptijd-matching met cashbehoefte.

#### 💰 Fiscaal

**Tijdens looptijd**: coupon = **roerend inkomen**.
- ⚖️ Roerende voorheffing ingehouden door uitbetalende instelling →
  **bevrijdend** (geen aangifte vereist als RV correct ingehouden).
- ⚠️ Tarief RV: zie [Cijferzakboekje §X].
- Edge → [[roerende-voorheffing-rente]]

⚠️ **Aangifte personenbelasting** — Deel 2, Vak VII (roerende inkomsten),
codes 1444/2444 voor opbrengsten *zonder* ingehouden RV (bv. buitenlandse
obligaties). Te verifiëren.

**Op vervaldag**: ontvangt nominaal. Verschil met aankoopprijs
(€ 50 meerwaarde bij disagio, € 50 verlies bij agio):
- ⚠️ behandeling als roerend inkomen of als (vrijgestelde) meerwaarde —
  afhankelijk van houderschapsregeling. Te verifiëren.
- Edge → [[meerwaarde-obligaties-prive]]

### 🏢💰 Voor de belegger-vennootschap

#### 🎯 Adviseur

🧭 Obligatie als financiële belegging vs aandelen vs liquide reserves —
rendement, looptijd-matching, balans-impact.

#### 📋 Boekhouder

*Rekening 51 "Vastrentende effecten"* — let op: deze MAR-benaming omvat
ook obligaties met variabele coupon. Zie [Veelvoorkomende verwarringen](#veelvoorkomende-verwarringen).

**Boeking bij aankoop met disagio** (belegger betaalt € 950 voor nominaal
€ 1.000):

| Rekening | Naam | Debet | Credit |
|---:|---|---:|---:|
| 51 | Vastrentende effecten — nominaal | 1.000 | — |
| 550 | Zichtrekening | — | 950 |
| 4902 | Over te dragen agio (op belegging) | — | 50 |

*De € 50 wordt over de looptijd als financiële opbrengst geboekt
(spiegel van uitgever-disagio).*

**Boeking jaarlijkse spreiding** (€ 10 / 5 jaar):

| Rekening | Naam | Debet | Credit |
|---:|---|---:|---:|
| 4902 | Over te dragen agio (op belegging) | 10 | — |
| 750 | Financiële opbrengsten | — | 10 |

#### 💰 Fiscaal

Coupons + spreiding belastbaar als financiële opbrengst in
vennootschapsbelasting. Edge → [[vennootschapsbelasting-fin-opbrengst]]

**Geen DBI** — *DBI geldt voor dividenden, niet voor rente*. Zie
[Veelvoorkomende verwarringen](#veelvoorkomende-verwarringen).

### 🔍 Als auditor / commissaris (extern perspectief)

De auditor werkt niet voor uitgever of belegger maar voor de **externe
gebruikers** van de jaarrekening (aandeelhouders, kredietverstrekkers,
fiscus).

#### Controle-aandachtspunten

- ⚖️ **Spreidingsmethode** agio/disagio consistent toegepast over de jaren
  (wisselen tussen lineair en effective interest breekt consistency-beginsel)
- ⚖️ **Prorata-intrest** correct berekend op balansdatum
- ⚖️ **Toelichting jaarrekening** volledig: spreidingskeuze + waarderingsregels +
  vervalkalender
- ⚠️ **EBITDA-regel** correct toegepast (eventuele aftrek-beperking gerapporteerd)
- 🔗 Bij **call-clausule activering**: premie correct als kapitaalverlies
  behandeld, niet als rentekost

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
  niet gelijk aan de coupon. Gebruik *yield-to-maturity* of equivalent
  voor vergelijking.
- **"Default" in obligatie-context.** Verwijst hier naar **wanbetaling**
  (missed coupon of hoofdsom), niet naar een standaardinstelling.

## Algemene aandachtspunten

> Generieke aandachtspunten over **financieringskeuze** (matching looptijd-investering,
> aftrekbaarheid rente vs dividend, schuld-EV-verhouding) staan in kader
> [[lange-termijn-financiering]] — niet hier herhaald.

- 🧑‍💼 *Bestuur* — 🧭 stress-test op coupon-verplichting bij meerjaren-budget;
  veel ondernemingen onderschatten cumulatieve last over hele looptijd.
- 🧑‍💼 *Bestuur* — 🧭 plan herfinanciering minstens 12–18 maanden vóór
  vervaldag, of overweeg sinking fund van bij uitgifte.
- ⚖️ Bij **wijziging van voorwaarden** (uitstel, restructuring): vergadering
  van obligatiehouders verplicht — niet onderhandelbaar per individuele
  houder. *Bron: [[WVV#art-7-62]]* ⚖️

## Alternatieven (zelfde doel)

Voor lange-termijn-financiering buiten bankkrediet:
- [[banklening]] — eenvoudiger maar één vaste tegenpartij
- [[achtergestelde-lening]] — schuld met conventionele achterstelling
- [[converteerbare-obligatie]] — hybride met conversierecht naar aandelen
- [[winstdelende-lening]] — hybride met winst-gekoppelde coupon
- [[kapitaalverhoging]] — eigen vermogen i.p.v. schuld

> Cross-instrument keuze-logica: zie kader [[lange-termijn-financiering]].

## Wat dit record dekt

*Een check-lijst voor de stagiair. Competenties chronologisch (volgorde
van uitvoeren); termen alfabetisch.*

### Behandelde competenties (chronologisch)

1. **Klant adviseren over keuze** obligatielening vs alternatieven — zie
   [🎯 Adviseur](#-adviseur).
2. **Fiscale gevolgen inschatten** voor elk perspectief (uitgever ·
   belegger NP · belegger venn.) — zie
   [Rol van de accountant](#rol-van-de-accountant).
3. **Stappen begeleiden bij uitgifte** (besluit · prospectus · plaatsing
   · publicatie) — zie [⚖️ Begeleider](#-begeleider--stappenplan-bij-uitgifte).
4. **Uitgifte boekhoudkundig verwerken** (drie varianten + uitgiftekosten) —
   zie [Bij uitgifte (T₀)](#bij-uitgifte-t).
5. **Werkelijk rendement (YTM) berekenen** bij agio/disagio.
6. **Jaarlijkse routine boekhoudkundig verwerken** (coupon · prorata ·
   spreiding · afschrijving) — zie [Jaarlijks](#jaarlijks).
7. **Toelichting jaarrekening opstellen** (spreidingskeuze + waarderingsregels) —
   zie [💰 Fiscaal](#-fiscaal).
8. **Terugbetaling op vervaldag boekhoudkundig verwerken** — zie
   [Op vervaldag (T₅)](#op-vervaldag-t).
9. **Aangekochte obligatielening verwerken** (belegger-vennootschap) —
   zie [🏢💰 Voor de belegger-vennootschap](#-voor-de-belegger-vennootschap).
10. **Auditor-controle** op spreidingsmethode + prorata + toelichting —
    zie [🔍 Als auditor / commissaris](#-als-auditor--commissaris-extern-perspectief).

### Behandelde termen (alfabetisch)

agio · call-clausule · coupon · coupondatum · disagio · emissieprospectus ·
nominale waarde / pari · nulcoupon · prorata-intrest · put-clausule ·
sinking fund · stapcoupon · vergadering van obligatiehouders · vervaldag ·
wanbetaling · werkelijk rendement (YTM)

### Behandelde formules

- **Prorata-intrest** = *coupon × (dagen sinds laatste betaling / 365)*
- **Werkelijke financieringskost bij disagio** = (coupon + lineaire
  amortisatie disagio) / ontvangen kapitaal
- **Werkelijke financieringskost bij agio** = (coupon − lineaire afname
  agio) / ontvangen kapitaal

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
- `onderdeel_van` → [[lange-termijn-financiering]] *(kader)* · [[schulden-op-meer-dan-een-jaar]]
- `is_uitzondering_op` → [[oprichtingskosten]] *(uitgiftekosten mogen
  gespreid over hele looptijd)*
- `verward_met` → [[DBI]] *(rente valt niet onder DBI)* · [[MAR#rubriek-51]]
  *("vastrentende" omvat ook variabel)*
- `gerelateerd` → [[converteerbare-obligatie]], [[banklening]],
  [[kapitaalverhoging]], [[oprichtingskosten]]
- `valt_onder_regime` → [[aftrekbaarheid-financieringskosten]],
  [[ebitda-regel-198-1]], [[roerende-voorheffing-rente]],
  [[meerwaarde-obligaties-prive]], [[vennootschapsbelasting-fin-opbrengst]]

---

## Iteratie-log

**v7 (huidige)** — kanonieke template, wijzigingen t.o.v. v5/v6:

- **Rol × perspectief matrix-structuur** — per klant-perspectief de
  relevante accountant-rollen; geen lege rollen tonen. Vier perspectieven:
  uitgever · NP-belegger · venn-belegger · auditor (extern).
- **Rekening-codes weg uit "Hoe het werkt"** — daar alleen conceptuele
  uitleg. Rekening-codes verschijnen onder Rol > Boekhouder (waar de
  boekingen zijn).
- **Valkuilen-taxonomie**: conceptuele valkuilen (denkfouten) in body bij
  het concept; uitvoerings-valkuilen onder de relevante rol-cel.
- **Generieke valkuilen verwezen** naar kader [[lange-termijn-financiering]] —
  in dit record alleen instrument-specifieke valkuilen.
- **Leespad-suggestie** als eigen sectie nabij top — voorvereisten, kader,
  volgkennis. Geen anchor-codes (alleen in frontmatter).
- **Element-vocabulaire** toegepast: een mechanisme als disagio krijgt
  meerdere weergaven (berekening + boeking + balans-snapshot) onder één
  sectie i.p.v. losse rubrieken.
- **Concept-snippets weg** uit "Hoe het werkt": geen volledige boekingen
  meer; alleen "wat is het, hoe gedraagt het zich" plus speelruimte.

**Open punten**:
- Render-laag moet de "Voor wie zit accountant aan tafel"-structuur
  visueel duidelijk tonen (h3-h4-h5 of cards).
- Validatie of de stagiair de fiche begrijpt zonder eerst door
  Rol-sectie te scrollen.
- Wikilinks naar kader [[lange-termijn-financiering]] vereisen dat dat
  record bestaat (gepland in deze ronde).
