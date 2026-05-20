---
title: "Obligatielening — v6 (geen rekeningen in onderdelen, alleen wikilinks)"
tags:
  - experiment
  - mockup
status: experimental
mockup: true
---

> **Vergelijkings-versie v6** — "Hoe het werkt" bevat **geen
> rekeningen-codes meer**, zelfs niet als hint. Aan het einde van elk
> onderdeel een **wikilink** naar de plaats in Perspectieven waar de
> boekhoudkundige uitwerking staat. Sterkste scheiding: concept-laag vs
> uitvoeringslaag. Vergelijk met [[obligatielening-v4|v4]] (alles samen)
> en [[obligatielening-v5|v5]] (met hints); overzicht:
> [[obligatielening-v2-mockup|alle versies]].
>
> **Confidence-tekens** (per claim):
> ⚖️ *dit vond ik letterlijk in een bron* — wet · KB · CBN · norm + bron
> 🔗 *dit heb ik afgeleid uit verschillende bronnen* + eventueel bronnen
> 🧭 *dit zegt mijn intuïtie (voelt als een goede vuistregel) maar is niet te verifiëren* — beroepswijsheid
> ⚠️ *te verifiëren* — bron ontbreekt of nog te checken

# Obligatielening

Een obligatielening is een **schuldfinanciering** waarbij een vennootschap
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

## Wanneer kies je dit?

### Voor wie

🧭 Middelgrote tot grote vennootschap met voldoende reputatie of
investeerderskring; voorspelbare cashflow over de hele looptijd.

🧭 *Niet voor KMO* — uitgifte-overhead (notariskosten, prospectus,
bankcommissies) maakt het onrendabel onder ongeveer € 5 miljoen; de
vaste kosten worden te zwaar t.o.v. de opbrengst.

### Wanneer wel inzetten

- 🔗 **Bank-financiering verzadigd of strategisch ongewenst** — obligatieleningen
  werken op een andere markt dan bankkrediet en spreiden tegenpartij-risico;
  geen enkele schuldeiser kan de onderneming klemzetten.
- 🔗 **Lange investeringshorizon (5–15 jaar)** past bij vastgoed,
  infrastructuur, R&D-portefeuille — banken bieden zelden looptijden boven
  7–10 jaar zonder zware zekerheidseisen; de obligatiemarkt wel.
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
  call-clausule wordt onderhandeld (zie [Call- en put-clausules](#call--en-put-clausules)
  onder Terugbetaling), zit je vast aan de looptijd.

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
schuldgraad — ⚠️ nog te verifiëren.

## Hoe het werkt

*De **boekings- en balans-uitwerking** met cijfervoorbeelden staat per
moment-in-tijd onder [🏢 Vennootschap-uitgever](#-vennootschap-uitgever)
en [🏢💰 Belegger — vennootschap](#-belegger--vennootschap). Hier alleen
het concept en de relevante rekeningen-codes.*

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
of een veelvoud daarvan. 🧭 *Marktconventie, geen wettelijke verplichting.*

**Speelruimte:** kleine nominale waardes (€ 100) maken brede retail-distributie
mogelijk maar verhogen administratie per houder. Grote nominale (€ 100.000)
beperkt het publiek tot professionele beleggers en kan onder vrijstelling
van prospectusplicht vallen — ⚠️ drempels uit Prospectusverordening te
verifiëren.

#### Couponrente

De **coupon** is de jaarlijkse vergoeding aan de belegger, uitgedrukt als
percentage van het nominale bedrag. Kan **vast** of **variabel** zijn,
en wordt **jaarlijks** of **semi-jaarlijks** betaald.

- 🔗 **Vaste coupon** — voorspelbare last bij de vennootschap, voorspelbaar
  rendement bij de belegger. Aangewezen wanneer de onderneming budgettaire
  zekerheid wil.
- 🔗 **Variabele coupon** (typisch Euribor + spread) — renterisico verschuift
  van belegger naar vennootschap. Aangewezen wanneer onderneming verwacht
  dat marktrente daalt of een natuurlijke hedge heeft.

**Speelruimte:** ook **stapcoupon** (oplopend percentage over de jaren,
om de last in beginjaren te beperken) en **nulcoupon** (geen tussentijdse
betaling — beleggers krijgen rendement enkel via aankoop onder pari +
terugbetaling aan pari op vervaldag). Inflatie-gekoppelde coupons bestaan
ook maar zijn in België zeldzaam.

#### Looptijd

Typisch **5 tot 15 jaar**; kan oplopen tot 30 jaar bij infrastructuurfinanciering.

- 🔗 **Korter** → lager renterisico voor de belegger, maar
  **herfinancieringsrisico** voor de vennootschap op vervaldag.
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
5 jaar.

*Bron: [[KB-WVV#art-3-37]]* ⚖️

> Deze regel is een **uitzondering op oprichtingskosten** — zie ook
> [[oprichtingskosten]] (sectie "uitzonderingen") en de edge
> `is_uitzondering_op` onderaan.

**Verplichting in toelichting jaarrekening** — de **keuze voor spreiding
over de looptijd** (i.p.v. de standaard 5-jaarsregel) moet **expliciet
vermeld** worden in de waarderingsregels en de toelichting bij de
jaarrekening. *Bron: [[KB-WVV#art-3-37]]* ⚖️

**Valkuilen**

- 📋 *Boekhouder* — uitgiftekosten **niet of niet correct spreiden** bij
  looptijd > 5 jaar → resultaat van jaar 1 vertekend met grote eenmalige
  kost; spreidingskeuze niet vermeld in toelichting. *Bron: [[KB-WVV#art-3-37]]* ⚖️

> 📊 **Boekhoudkundige uitwerking** (boekingen, voorbeeld, afschrijving):
> zie [Vennootschap-uitgever → Boeking uitgiftekosten](#boekingen--bij-uitgifte-t).

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

#### Valkuilen

- 📋 *Boekhouder* — agio/disagio **niet correct spreiden** → resultaat
  van jaar 1 vertekend. *Bron: [[KB-WVV#art-3-37]]* ⚖️
- 🔍 *Auditor* — **spreidingsmethode niet consistent** toegepast over
  de jaren (wisselen tussen lineair en effective interest) → inbreuk op
  het consistency-beginsel.
- 📋 *Boekhouder* — bij **call-clausule activering**: de premie boven pari
  is geen rente maar een **kapitaalverlies**, vraagt eigen behandeling.

> 📊 **Boekhoudkundige uitwerking** (3 varianten met cijfers, boekingen
> bij uitgifte, jaarlijkse spreiding, balans-snapshots): zie
> [Vennootschap-uitgever → Boekingen bij uitgifte](#boekingen--bij-uitgifte-t).
> Voor aankoop-zijde: [Belegger-vennootschap → Boekingen](#boekingen-1).

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

#### Valkuilen

- 📋 *Boekhouder* — **prorata vergeten** → matching-beginsel gebroken,
  rentelast in verkeerd jaar.
- 📋 *Boekhouder* — bij **variabele coupon**: prorata herrekenen op basis
  van de **geldende rentevoet op balansdatum**, niet op basis van de vorige
  coupon-uitbetaling.

> 📊 **Boekhoudkundige uitwerking** (coupon-boeking, prorata-boeking 31/12
> en 1/7 met cijfers): zie [Vennootschap-uitgever → Boekingen jaarlijks](#boekingen--jaarlijks).

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

#### Valkuilen

- 🧑‍💼 *Bestuurder* — 🧭 **liquiditeitsklem op vervaldag** bij één grote
  terugbetaling → plan herfinanciering minstens 12–18 maanden vooraf,
  of overweeg sinking fund van bij uitgifte.
- 📋 *Boekhouder* — bij **call-clausule activering**: premie boven pari
  is geen rente maar **kapitaalverlies**; afzonderlijke behandeling.

> 📊 **Boekhoudkundige uitwerking** (aflossingsboeking, balans-snapshot
> na aflossing): zie [Vennootschap-uitgever → Boeking op vervaldag](#boeking--op-vervaldag-t).

---

## Perspectieven per actor

*Hier de **uitvoering** per actor — boekingen, balans-snapshots, fiscaal,
formaliteiten. Chronologisch geordend per moment-in-tijd.*

### 🏢 Vennootschap-uitgever

**Rekeningen-overzicht**: 170 schuld · 201 uitgiftekosten · 4901/4902
agio/disagio · 492 prorata · 650 rentelasten · 6300 afschrijving
uitgiftekosten.

**Doorlopend voorbeeld** dat hieronder wordt uitgewerkt:

> **NV ABC** geeft 1.000 obligaties uit van € 1.000 nominaal = € 1.000.000.
> **Coupon 3 % vast**, jaarlijks betaalbaar op 1 juli. **Looptijd 5 jaar**.
> **Uitgiftekosten € 12.000** (notaris + publicatie + bankcommissie).
> Drie varianten van uitgifteprijs gerekend: pari (€ 1.000) · disagio
> (€ 950) · agio (€ 1.050).

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
3. **Publicatie en plaatsing** — bekendmaking in *Belgisch Staatsblad* bij
   publieke uitgifte; effectieve plaatsing bij beleggers via bank-syndicaat.
4. **Ontvangst kapitaal en uitgifteboeking** — zie [Boekingen bij uitgifte](#boekingen-bij-uitgifte-t).
5. **Eerste boekingsroutine** — opzet spreidingstabel agio/disagio en
   uitgiftekosten; opzet prorata-aanslag in jaarafsluiting.
6. **Jaarlijkse routine** — zie [Boekingen jaarlijks](#boekingen-jaarlijks).
7. **Toelichting jaarrekening** — eerste boekjaar vermeldt de spreidings-
   en waarderingskeuzes.
8. **Vervaldag** — zie [Boeking op vervaldag](#boeking-op-vervaldag-t).

#### Boekingen — bij uitgifte (T₀)

**Variant 1 — uitgifte aan pari** (€ 1.000.000 ontvangen)

| Rekening | Naam | Debet | Credit |
|---:|---|---:|---:|
| 550 | Zichtrekening | 1.000.000 | — |
| 170 | Obligatielening | — | 1.000.000 |

**Variant 2 — uitgifte met disagio** (€ 950.000 ontvangen, € 50.000 disagio)

Berekening eerst:

| | Bedrag |
|---|---:|
| Ontvangen cash | € 950.000 |
| Schuld op balans (terug te betalen) | € 1.000.000 |
| **Disagio** (over te dragen, spreiding 5 jaar) | **€ 50.000** |
| Jaarlijkse couponuitgave | € 30.000 |
| Jaarlijkse disagio-amortisatie (lineair) | € 10.000 |
| **Werkelijke jaarlijkse financieringskost** | **€ 40.000** |
| **Werkelijke kost (≈ YTM)** | **≈ 4,2 %** |

Boeking bij uitgifte:

| Rekening | Naam | Debet | Credit |
|---:|---|---:|---:|
| 550 | Zichtrekening | 950.000 | — |
| 4901 | Over te dragen disagio | 50.000 | — |
| 170 | Obligatielening | — | 1.000.000 |

**Variant 3 — uitgifte met agio** (€ 1.050.000 ontvangen, € 50.000 agio)

Berekening:

| | Bedrag |
|---|---:|
| Ontvangen cash | € 1.050.000 |
| Schuld op balans | € 1.000.000 |
| **Agio** (over te dragen opbrengst) | **€ 50.000** |
| Jaarlijkse couponuitgave | € 30.000 |
| Jaarlijkse agio-afname (vermindert kost) | − € 10.000 |
| **Werkelijke jaarlijkse financieringskost** | **€ 20.000** |
| **Werkelijke kost (≈ YTM)** | **≈ 1,9 %** |

Boeking bij uitgifte:

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

#### Balans-snapshot — T₀ (vóór uitgifte, verkort)

**Actief**

| Code | Naam | Bedrag |
|---:|---|---:|
| 55 | Liquide middelen | 0 |

**Passief**

| Code | Naam | Bedrag |
|---:|---|---:|
| 17 | Schulden op meer dan 1 jaar | 0 |

#### Balans-snapshot — T₀ (direct na uitgifte met disagio + uitgiftekosten)

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

#### Boekingen — jaarlijks

**Coupon-betaling** (variant disagio — € 30.000 cash op 1 juli)

| Rekening | Naam | Debet | Credit |
|---:|---|---:|---:|
| 650 | Rentekosten obligatielening | 30.000 | — |
| 550 | Zichtrekening | — | 30.000 |

**Prorata-intrest op balansdatum 31/12** (6 maanden gelopen sinds 1 juli)

Berekening: 40.000 × (6/12) = **€ 20.000** *(o.b.v. coupon 4 %; bij coupon
3 % zou de prorata 15.000 zijn — dit voorbeeld gebruikt 4 % voor de prorata
om aan te sluiten bij Uitgeverij Ukkel NV in [Hoe het werkt](#coupons-en-prorata-intrest)).*

| Rekening | Naam | Debet | Credit |
|---:|---|---:|---:|
| 650 | Rentekosten obligatielening | 20.000 | — |
| 492 | Toe te rekenen kosten | — | 20.000 |

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

#### Boeking — op vervaldag (T₅)

| Rekening | Naam | Debet | Credit |
|---:|---|---:|---:|
| 170 | Obligatielening | 1.000.000 | — |
| 550 | Zichtrekening | — | 1.000.000 |

#### Balans-snapshot — T₅ (na laatste coupon en aflossing, variant disagio)

**Actief**

| Code | Naam | Bedrag |
|---:|---|---:|
| 55 | Liquide middelen | netto cumul. −62.000* |
| 4901 | Over te dragen disagio | 0 |
| 201 | Kosten uitgifte leningen | 0 |

**Passief**

| Code | Naam | Bedrag |
|---:|---|---:|
| 17 | Schulden > 1 jaar | 0 |

*\*Berekening: ontvangen +950.000 − 12.000 uitgiftekosten − 5 × coupon
30.000 − 1.000.000 aflossing = − 212.000. Plus 5 × 30.000 coupon
weergegeven hierboven; cumul totale uitgave aan financiering ≈ totaalkost
200.000 + 12.000 = 212.000.*

#### Fiscaal

Rentelasten (coupon + disagio-spreiding) zijn aftrekbare beroepskost;
agio-opname vermindert de aftrekbare last symmetrisch.
*Bron: [[WIB92#art-49]]* ⚖️
Edge → [[aftrekbaarheid-financieringskosten]]

⚠️ **Te verifiëren**: interactie met de **EBITDA-regel**
([[WIB92#art-198-1]]) bij hoge schuldgraad — overschrijdt het
netto-financieringskost-saldo de EBITDA-drempel, dan beperking
aftrekbaarheid.

#### Toelichting jaarrekening

*Bron: [[KB-WVV]]* ⚖️
- vermelding obligatielening in toelichting bij rubriek 17
- spreidingsmethode agio/disagio in waarderingsregels
- vervalkalender van de schuld (afzonderlijk per tranche bij sinking fund)
- keuze voor spreiding uitgiftekosten over hele looptijd (zie [[oprichtingskosten]])

#### Formaliteiten bij uitgifte

*Bron: [[WVV#art-7-54]] e.v.* ⚖️
- besluit van het bestuursorgaan
- emissieprospectus of informatienota bij publieke uitgifte
  ⚠️ drempels uit Prospectusverordening te verifiëren
- vergadering van obligatiehouders bij wijziging voorwaarden
  *Bron: [[WVV#art-7-62]]* ⚖️

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

#### Boekingen

*Rekeningen:* **51** Vastrentende effecten (kostprijs) · **4902/4901**
gespiegeld aan uitgever · **750/650** spreidings-opbrengst of -last.

*🔗 De MAR-rubriek 51 heet "vastrentende effecten" maar omvat ook
obligaties met variabele coupon — zie [Veelvoorkomende verwarringen](#veelvoorkomende-verwarringen).*

**Boeking bij aankoop met disagio** (belegger betaalt € 950 voor nominaal
€ 1.000):

| Rekening | Naam | Debet | Credit |
|---:|---|---:|---:|
| 51 | Vastrentende effecten — nominaal | 1.000 | — |
| 550 | Zichtrekening | — | 950 |
| 4902 | Over te dragen agio (op belegging) | — | 50 |

*De € 50 wordt over de looptijd als financiële opbrengst geboekt (spiegel
van de uitgever-disagio).*

**Boeking jaarlijkse spreiding** (€ 10 / 5 jaar = belegger ontvangt extra
opbrengst boven coupon):

| Rekening | Naam | Debet | Credit |
|---:|---|---:|---:|
| 4902 | Over te dragen agio (op belegging) | 10 | — |
| 750 | Financiële opbrengsten | — | 10 |

#### Fiscaal

Coupons + spreiding belastbaar als financiële opbrengst in
vennootschapsbelasting.
Edge → [[vennootschapsbelasting-fin-opbrengst]]

**Geen DBI** — *DBI geldt voor dividenden, niet voor rente.* Zie ook
[Veelvoorkomende verwarringen](#veelvoorkomende-verwarringen).

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

## Alternatieven (zelfde doel)

Voor het doel **lange-termijn-financiering buiten bankkrediet**:
- [[banklening]] — eenvoudiger maar één vaste tegenpartij
- [[achtergestelde-lening]] — schuld met conventionele achterstelling
- [[converteerbare-obligatie]] — hybride met conversierecht naar aandelen
- [[winstdelende-lening]] — hybride met winst-gekoppelde coupon
- [[kapitaalverhoging]] — eigen vermogen i.p.v. schuld

→ Vergelijkingsmatrix: [[vergelijking-lange-termijn-financieringsinstrumenten]]

## Wat dit record dekt

*Een check-lijst voor toetsing. Competenties **chronologisch** (volgorde
van uitvoeren); termen **alfabetisch**. Per programmaonderdeel kan een
script deze labels aggregeren om een PO-overzicht te bouwen.*

### Behandelde competenties (chronologisch)

1. **Klant adviseren over keuze obligatielening vs alternatieven** — zie
   [Wanneer kies je dit?](#wanneer-kies-je-dit) en [Alternatieven](#alternatieven-zelfde-doel).
2. **Fiscale gevolgen inschatten voor elk perspectief** (uitgever ·
   belegger NP · belegger venn.) — zie [Perspectieven per actor](#perspectieven-per-actor).
3. **Boekhoudkundige stappen begeleiden bij uitgifte** (incl. formaliteiten,
   prospectus-vereisten) — zie [Stappenplan bij uitgifte](#stappenplan-bij-uitgifte).
4. **Werkelijk rendement (YTM) berekenen** bij uitgifte buiten pari — zie
   berekeningstabellen onder [Boekingen — bij uitgifte](#boekingen--bij-uitgifte-t).
5. **Uitgifte boekhoudkundig verwerken** (alle varianten pari/disagio/agio
   + uitgiftekosten) — zie [Boekingen — bij uitgifte](#boekingen--bij-uitgifte-t).
6. **Jaarlijkse routine boekhoudkundig verwerken** (coupon · prorata ·
   spreiding agio/disagio · afschrijving uitgiftekosten) — zie
   [Boekingen — jaarlijks](#boekingen--jaarlijks).
7. **Toelichting jaarrekening opstellen** (spreidingskeuze + waarderingsregels) —
   zie [Toelichting jaarrekening](#toelichting-jaarrekening).
8. **Terugbetaling op vervaldag boekhoudkundig verwerken** — zie
   [Boeking — op vervaldag](#boeking--op-vervaldag-t).
9. **Aangekochte obligatielening boekhoudkundig verwerken** (vanuit
   belegger-vennootschap) — zie [🏢💰 Belegger — vennootschap](#-belegger--vennootschap).

### Behandelde termen (alfabetisch)

[agio](#agio-uitgifte-boven-pari) · call-clausule ([zie](#call--en-put-clausules)) ·
coupon ([zie](#couponrente)) · coupondatum · default ([→ wanbetaling](#veelvoorkomende-verwarringen)) ·
[disagio](#disagio-uitgifte-beneden-pari) · emissieprospectus ·
[nominale waarde / pari](#nominale-waarde) · nulcoupon ([zie](#couponrente)) ·
[prorata-intrest](#coupons-en-prorata-intrest) ·
put-clausule ([zie](#call--en-put-clausules)) ·
[sinking fund](#aflossing-in-tranches-sinking-fund) ·
stapcoupon ([zie](#couponrente)) ·
vergadering van obligatiehouders · vervaldag · wanbetaling · werkelijk
rendement (YTM)

### Behandelde formules

- **Prorata-intrest** = *coupon × (dagen sinds laatste betaling / 365)* —
  zie [Coupons en prorata-intrest](#coupons-en-prorata-intrest).
- **Werkelijke financieringskost bij disagio** = (coupon + lineaire
  amortisatie disagio) / ontvangen kapitaal — zie variant 2 onder
  [Boekingen — bij uitgifte](#boekingen--bij-uitgifte-t).
- **Werkelijke financieringskost bij agio** = (coupon − lineaire afname
  agio) / ontvangen kapitaal — zie variant 3 idem.

### Behandelde regimes (via edges)

[aftrekbaarheid-financieringskosten](#fiscaal) ·
[ebitda-regel-198-1](#fiscaal) ⚠️ ·
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
- `verward_met` → [[DBI]] *(rente valt niet onder DBI)* · [[MAR#rubriek-51]]
  *("vastrentende" omvat ook variabel)*
- `gerelateerd` → [[converteerbare-obligatie]], [[banklening]],
  [[kapitaalverhoging]], [[oprichtingskosten]]
- `valt_onder_regime` → [[aftrekbaarheid-financieringskosten]],
  [[ebitda-regel-198-1]], [[roerende-voorheffing-rente]],
  [[meerwaarde-obligaties-prive]], [[vennootschapsbelasting-fin-opbrengst]]

---

## Iteratie-log

**v6 (huidige)** — wijzigingen t.o.v. v5:

- **Rekeningen-codes volledig weg uit "Hoe het werkt"** — geen
  *Rekeningen: 4901, 6500…*-regels meer. Sterkste scheiding tussen
  concept-laag en uitvoeringslaag.
- **Wikilink per onderdeel** naar de plaats in Perspectieven waar de
  boekhoudkundige uitwerking staat (📊 callout).
- Voor de rest identiek aan v5.

---

**v5** — wijzigingen t.o.v. v4:

- **Definitie schoongemaakt** — boekhoudkundige rekening-vermelding
  weggehaald (geen rekening 170 in definitie); rekeningen-codes nu enkel
  bij de betrokken onderdelen.
- **Legenda met jouw frasering** ("dit vond ik letterlijk in een bron",
  "dit heb ik afgeleid", "intuïtie zonder verifieerbare bron").
- **`*Waarom:*` labels weg** — rationale integreert nu via em-dash in
  natuurlijke taal. In de JSON blijft `waarom` een apart veld; alleen de
  render verandert.
- **Boekingen-tabel** herformatteerd: `Rekening | Naam | Debet | Credit`
  (i.p.v. checkmark-kolommen). Lege zijde wordt `—`.
- **Balans-tabellen** met **Code-kolom apart**; Actief en Passief als
  twee losse mini-tabellen onder elkaar.
- **Boekingen + balans-snapshots verplaatst** van "Hoe het werkt" naar
  [🏢 Vennootschap-uitgever](#-vennootschap-uitgever) — chronologisch
  geordend per moment-in-tijd (uitgifte · jaarlijks · vervaldag). In
  "Hoe het werkt" alleen nog **rekeningen-codes als hint** per onderdeel.
- **"Wat dit record dekt"** — competenties chronologisch herordend; termen
  alfabetisch.
- **Belegger-vennootschap** krijgt ook een boekings-tabel + voorbeeld
  (was te kort in v4).

**🤖 Confidence-icoon-alternatief**: 🧭 hier behouden, maar 🤖 was overwogen
als alternatief ("LLM-redenering"). Je voorkeur?

**Open punt (mijn pushback)** — ik heb alle cijferboekingen verplaatst naar
Perspectieven zoals je vroeg. Maar bij sub-onderdelen zoals disagio toont
de boeking *wat het concept is* (de rekening 4901 maakt zichtbaar dat
disagio een uitgestelde kost is). Wie "Hoe het werkt > Disagio" nu leest,
moet doorklikken naar Perspectieven om de boeking te zien. Test of dat
voor je werkt of dat we toch korte boekings-snippets in "Hoe het werkt"
willen houden voor pedagogische directheid.

**Plan voor volgende iteratie**:
- 4 nieuwe concept-mockups om patronen te ontdekken:
  *inkoop-eigen-aandelen-nv* (operatie) · *financiele-leasing* (instrument
  + alternatief vergelijking) · *VVPRbis* (regime) · *solvabiliteitsratio*
  (ratio met formule + drempels).
- Bij elk: meer stappenplannen integreren (jaarlijkse uitkering,
  eindafrekening, accountant-acties bij beleggers).

**v4** — confidence-iconen aangepast (🔗/🧭), stappenplan-uitgifte
geïntegreerd, sectie "Wat dit record dekt", forward-links, taalcorrecties.

**v3** — accountant-bril vooraan, recursieve onderdelen, perspectieven
per actor, confidence op claim-niveau, drie balansen apart,
veelvoorkomende verwarringen, uitzondering-edges.
