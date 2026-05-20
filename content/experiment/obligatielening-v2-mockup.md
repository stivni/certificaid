---
title: "Mockup v2 — Obligatielening (volledig record)"
tags:
  - experiment
  - mockup
status: experimental
mockup: true
---

> **Dit is een mockup**, geen echte concept-record. We testen hier hoe
> een instrument-cluster eruit kan zien met de **accountant-bril vooraan**,
> recursieve bouwstenen, perspectieven per actor, en consistente
> confidence-labels op claim-niveau. Vergelijk met [[obligatielening]].

> **Legenda confidence-labels** (op claim-niveau toegepast)
> ⚖️ `grounded` — direct uit wet/KB/CBN/norm
> 🧮 `inferred` — combinatie of mechanisme-redenering uit bronnen
> 💼 `vuistregel` — beroepswijsheid, geen harde regel
> ⚠️ `te_verifiëren` — onzeker

---

# Obligatielening

`node_type: cluster` · `kind: instrument, lange-termijn-schuld` ·
`dient_doelen: werkkapitaal-financieren · lange-termijn-investering-financieren · bank-onafhankelijkheid-vergroten`

## ⭐ Accountant-perspectief

**Voor wie** 💼 vuistregel: middelgrote tot grote vennootschap met
voldoende reputatie of investeerderskring; voorspelbare cashflow over
de hele looptijd. Niet voor KMO — uitgifte-overhead (notaris, prospectus,
bankcommissies) maakt het onrendabel onder ~€5 M.

**Wanneer inzetten**
- 🧮 bank-financiering verzadigd of strategisch ongewenst (klant wil
  bank-onafhankelijkheid)
- 🧮 lange investeringshorizon (5–15 j) past bij vastgoed, infrastructuur,
  R&D-portefeuille
- 💼 vuistregel: vaste rente vastleggen wanneer marktrente laag staat —
  je locked in financieringskost voor 5+ jaar
- 💼 vuistregel: voldoende cashflow-comfort op couponvervaldagen

**Wanneer niet**
- 💼 vuistregel: cashflow volatiel of seizoengebonden — coupon is *vast*,
  geen renegotiatie zoals bij bank
- 💼 vuistregel: behoefte < ~€5 M of looptijd < 3 j — kost niet waard
- 🧮 bij wens tot maximale flexibiliteit in vervroegde aflossing — tenzij
  je een call-clausule onderhandelt (zie [[#Bouwsteen Terugbetaling op vervaldag]])

**Hoofdrisico voor klant** ⚖️ `WVV art. 7:62`: **liquiditeitsklem op
couponvervaldagen**. Anders dan bij banklening: geen onderhandeling
mogelijk over uitstel. Default leidt tot vergadering van obligatiehouders
met versnelde opeisbaarheid van de hele lening.

**Hoofdvoordeel voor klant** 🧮 (uit `art. 49 WIB92`): vaste financieringskost
over lange periode + volledig aftrekbare rentelast bij de vennootschap
(vs dividend dat niet aftrekbaar is uit beschikbare winst).

## 🧭 Economische substantie ("wat gebeurt er echt")

🧮 De vennootschap leent geld van veel kleine investeerders in plaats
van één bank. Investeerders krijgen een **verhandelbaar schuldbewijs** —
ze kunnen hun positie verkopen aan derden zonder dat de vennootschap iets
merkt. Voor de vennootschap blijft het pure schuld: ⚖️ de obligatiehouder
wordt geen eigenaar, krijgt vaste rente, en moet op vervaldag terugbetaald
worden ongeacht de winstgevendheid. ⚖️ `WVV art. 7:54`

🧮 Het verschil met een banklening zit dus niet in de boekhoudkundige
*aard* (beide zijn schulden op rekening 170), maar in de **verhandelbaarheid**,
de **versplintering van de schuldeisers**, en de **niet-renegotieerbaarheid**
tijdens de looptijd.

## Definitie *(klassiek — voor toetsing)*

⚖️ Een leningsovereenkomst waarbij de vennootschap obligaties uitgeeft aan
beleggers — verhandelbare schuldbewijzen met vaste of variabele rente en
vooraf bepaalde looptijd (typisch 5–15 jaar). De vennootschap ontvangt
het kapitaal en betaalt jaarlijkse coupons + terugbetaling op vervaldag.
Boekhoudkundig: rekening 170 onder schulden op meer dan één jaar.
⚖️ `CBN 2019/07; WVV art. 7:54 e.v.; MAR rubriek 17`

---

## Bouwstenen

### Bouwsteen — Drie hoofdelementen: nominaal, coupon, looptijd

⚖️ Bij uitgifte beslist de vennootschap over drie parameters die de cashflow
volledig vastleggen. Alle drie staan in het emissieprospectus.
⚖️ `WVV art. 7:54; CBN 2019/07`

🧮 **Economische substantie**: de drie parameters interageren. Hoger coupon →
aantrekkelijker voor beleggers → minder agio/disagio nodig. Langere looptijd →
hogere onzekerheid → meestal hoger coupon vereist. De adviseur stuurt op de
*combinatie*, niet op één parameter.

#### Sub-bouwsteen — Nominale waarde

⚖️ Standaard € 1.000 per obligatie of veelvoud daarvan; in België typisch
€ 1.000 (retail) tot € 100.000 (institutioneel).

💼 **Speelruimte**: nominaal van € 100 maakt brede retail-distributie mogelijk
maar verhoogt admin-overhead per houder; nominaal € 100.000 beperkt het
publiek tot professionele beleggers (en kan onder prospectusvrijstelling
vallen ⚠️ MiFID/Prospectus-verordening — te verifiëren).

#### Sub-bouwsteen — Couponrente

⚖️ Vast of variabel; jaarlijks of semi-jaarlijks betaalbaar.

💼 **Vast coupon**: voorspelbare last bij vennootschap, voorspelbaar
rendement bij belegger. Aangewezen wanneer onderneming budgettaire
zekerheid wil.

💼 **Variabel coupon** (typisch Euribor + spread): risico bij vennootschap
verschuift naar de marktrente-beweging. Aangewezen wanneer onderneming
verwacht dat marktrente daalt of natuurlijke hedge heeft.

💼 **Speelruimte**: ook stapcoupon (oplopend), nulcoupon (geen coupon,
volledige opbrengst via disagio + terugbetaling pari), inflatie-gekoppeld.

#### Sub-bouwsteen — Looptijd

⚖️ Typisch 5–15 jaar; kan oplopen tot 30 jaar bij infrastructuurfinanciering.

🧮 **Korter** = lager renterisico voor belegger maar **herfinancieringsrisico
voor vennootschap** op vervaldag.

🧮 **Langer** = hoger coupon vereist (om beleggers te compenseren voor
renterisico) maar **financiële zekerheid** voor de vennootschap.

#### Voorbeeld

> Uitgeverij Ukkel NV: 1.000 obligaties × € 1.000 nominaal = € 1.000.000
> totaal. Couponrente 4 % vast per jaar = € 40.000 jaarlijkse intrestlast.
> Looptijd 8 jaar.

---

### Bouwsteen — Uitgiftekosten

⚖️ Notaris, publicatie in Belgisch Staatsblad, bankcommissies, eventueel
prospectus-kosten. Boekhoudkundig op rekening **201 "Kosten uitgifte
leningen"** (sub van oprichtingskosten). ⚖️ `KB WVV art. 3:37`

🧮 **Bijzonderheid**: deze kosten mogen *gespreid* worden over de hele
looptijd van de obligatielening — een **uitzondering** op de algemene
5-jaars-regel voor oprichtingskosten. ⚖️ `KB WVV art. 3:37`

#### Berekening (voorbeeld)

> Uitgiftekosten € 12.000 op 8-jarige looptijd → jaarlijkse afschrijving
> **€ 1.500** (lineair).

#### Illustratie — boekingen

```
Bij uitgifte:
D  201   Kosten uitgifte leningen        12.000
                            C  550  Bank             12.000

Elk jaar:
D  6300  Afschrijvingen oprichtingskosten 1.500
                            C  201            1.500
```

#### Valkuilen

- 📋 **Boekhouder** ⚖️: vergeten te spreiden bij uitgifte > 5 j → resultaat
  van jaar 1 vertekend met grote eenmalige kost. Toelichting in
  jaarrekening vermeldt de keuze voor spreiding.
- 💼 **Adviseur** vuistregel: uitgiftekosten meetellen bij vergelijking met
  banklening — anders lijkt obligatielening kunstmatig goedkoper.

---

### Bouwsteen — Uitgifte beneden of boven pari (disagio / agio)

⚖️ De obligatie heeft een *nominale waarde* (pari, bv. € 1.000) die op het
bewijs vermeld staat — dat is het bedrag dat de vennootschap op vervaldag
moet terugbetalen. Maar de prijs *waaraan beleggers de obligatie kopen*
bij uitgifte kan daarvan afwijken: lager (**disagio**) of hoger (**agio**).
⚖️ `WVV art. 7:54; CBN 2019/07`

🧮 **Economische substantie**: de couponrente die op het bewijs staat is
*niet* het werkelijke rendement voor de belegger noch de werkelijke
financieringskost voor de vennootschap. Zodra de uitgifteprijs afwijkt
van pari, schuift het echte rendement weg van de couponrente. De
couponrente is *het rapporteringsgezicht*; de uitgifteprijs is *de
correctie naar de marktwaarde*.

#### Sub-bouwsteen — Disagio (uitgifte beneden pari)

⚖️ Belegger betaalt minder dan nominaal; vennootschap betaalt op vervaldag
het volle nominale bedrag terug. Het verschil is een **uitgestelde
financieringskost** die de vennootschap spreidt over de looptijd.
⚖️ `KB WVV art. 3:37`

##### Berekening (voorbeeld)

NV ABC geeft 1.000 obligaties uit, nominaal € 1.000/stuk, coupon 3 %,
looptijd 5 jaar, uitgifteprijs **€ 950** (95 % van pari):

| | Bedrag |
|---|---|
| Ontvangen cash bij uitgifte | € 950.000 |
| Schuld op balans | € 1.000.000 |
| **Disagio** *(over te dragen, te spreiden 5 jaar)* | **€ 50.000** |
| Jaarlijkse couponuitgave | € 30.000 |
| Jaarlijkse disagio-amortisatie (lineair) | € 10.000 |
| **Werkelijke jaarlijkse financieringskost** | **€ 40.000** |

🧮 Werkelijke kost ≈ € 40.000 / € 950.000 ≈ **4,2 %** — niet de 3 % die
op het bewijs staat.

##### Illustratie — boekingen bij de uitgever

```
Bij uitgifte:
D  550   Bank                          950.000
D  4901  Over te dragen disagio         50.000
                            C  170  Obligatielening   1.000.000

Elk jaar:
D  6500  Rentelasten — disagio          10.000
                            C  4901                    10.000
D  6500  Rentelasten — coupon           30.000
                            C  550                     30.000

Op vervaldag:
D  170   Obligatielening             1.000.000
                            C  550                  1.000.000
```

##### Illustratie — balanseffect (verkort)

| Rubriek | T₀ (vóór) | T₀ (na uitgifte) | T₅ (na aflossing) |
|---|---|---|---|
| 55 Liquide middelen | 0 | +950.000 | cumulatief −50.000 |
| 490x Overlopende rek. — disagio | 0 | +50.000 | 0 |
| 170 Obligatielening (> 1 j) | 0 | +1.000.000 | 0 |
| 65 Financiële kosten (RR cumul) | 0 | 0 | 200.000 |

#### Sub-bouwsteen — Agio (uitgifte boven pari)

⚖️ Belegger betaalt méér dan nominaal. Het verschil is een **uitgestelde
opbrengst** die de vennootschap spreidt en die de werkelijke couponlast
verlaagt.

##### Berekening (voorbeeld)

Zelfde NV ABC, uitgifte aan **€ 1.050/stuk**:

| | Bedrag |
|---|---|
| Ontvangen cash bij uitgifte | € 1.050.000 |
| Schuld op balans | € 1.000.000 |
| **Agio** *(over te dragen opbrengst)* | **€ 50.000** |
| Jaarlijkse couponuitgave | € 30.000 |
| Jaarlijkse agio-afname (vermindert kost) | − € 10.000 |
| **Werkelijke jaarlijkse financieringskost** | **€ 20.000** |

🧮 Werkelijke kost ≈ € 20.000 / € 1.050.000 ≈ **1,9 %**, ondanks coupon 3 %.

##### Illustratie — boekingen bij de uitgever

```
Bij uitgifte:
D  550   Bank                        1.050.000
                            C  170  Obligatielening   1.000.000
                            C  4902 Over te dragen agio   50.000
```

#### Valkuilen

- 📋 **Boekhouder** ⚖️ `KB WVV 3:37`: agio/disagio niet (correct) spreiden →
  resultaat van jaar 1 vertekend.
- 💼 **Bestuurder/ondernemer** vuistregel: alleen naar de couponrente
  kijken bij vergelijking met banklening. Werkelijke financieringskost
  (incl. agio/disagio + uitgiftekosten) is wat moet vergeleken worden.
- 💼 **Adviseur** vuistregel: gebruik **werkelijke rendementskost** (YTM)
  bij scenario-vergelijking, niet nominale coupon.
- 📋 **Auditor/revisor** 🧮: spreidingsmethode consistent toegepast over
  jaren (lineair vs effective interest)? Wisselen breekt consistency.
- 💰 **Belegger** vuistregel: nominaal coupon ≠ werkelijk rendement bij aan-
  of verkoop buiten pari. Gebruik YTM.

---

### Bouwsteen — Coupons en prorata-intrest

⚖️ Couponbetalingen worden geboekt als financiële kosten op rekening **650**.
Tussen couponbetalingen en balansdatum: de gelopen-maar-nog-niet-vervallen
rente wordt prorata geboekt via rekening **492 "Toe te rekenen kosten"**.
⚖️ `CBN 148/4 + KB WVV art. 3:60`

🧮 **Economische substantie**: het matching-beginsel vereist dat de
rente-last in het juiste boekjaar staat, ook al wordt ze pas later cash
betaald. Anders verschuift een hap rentelast naar het verkeerde jaar en
wordt het resultaat artificieel hoger/lager.

#### Berekening — prorata (voorbeeld)

> Uitgeverij Ukkel NV: obligatie 4 % × € 1.000.000 = € 40.000 jaarlijkse
> coupon, betaalbaar elke 1 juli. Op 31 december is 6 maanden gelopen
> sinds laatste couponbetaling → **€ 20.000 toe te rekenen**.

🧮 Formule: `coupon × (dagen sinds laatste betaling / 365)` of equivalent
op maand-basis.

#### Illustratie — boekingen

```
31/12 (balansdatum):
D  6500  Rentekosten obligatielening   20.000
                            C  492  Toe te rekenen kosten   20.000

01/07 (volgende coupondatum):
D  6500  Rentekosten obligatielening   20.000  (2e helft jaar Y2)
D  492   Toe te rekenen kosten         20.000  (afboeken Y1-prorata)
                            C  550  Bank                    40.000
```

#### Valkuilen

- 📋 **Boekhouder** ⚖️: prorata vergeten = matching-beginsel gebroken,
  resultaat verkeerd jaar.
- 📋 **Boekhouder** 💼 vuistregel: bij variabele coupon — herrekening op
  basis van de geldende rentevoet op balansdatum, niet de vorige.

---

### Bouwsteen — Terugbetaling op vervaldag

⚖️ Op vervaldag betaalt de vennootschap het nominale bedrag terug aan de
obligatiehouders.

#### Illustratie — boekingen

```
D  170   Obligatieleningen           1.000.000
                            C  550  Bank                  1.000.000
```

#### Sub-bouwsteen — Aflossing in tranches (sinking fund)

💼 In plaats van het volle bedrag op vervaldag terug te betalen, kan de
vennootschap een **aflossingsschema** opnemen in het prospectus: jaarlijks
of periodiek een deel van de obligaties uitloten en aflossen.

🧮 **Economische substantie**: spreidt het cashflow-piek-risico op vervaldag,
maar maakt de obligatie minder aantrekkelijk voor sommige beleggers (kortere
gemiddelde looptijd).

#### Sub-bouwsteen — Call/put-clausules

💼 **Call** = uitgever heeft recht op vervroegde aflossing (vaak met premie
boven pari). Aangewezen wanneer onderneming flexibiliteit wil bij dalende
marktrente — kan herfinancieren goedkoper.

💼 **Put** = belegger heeft recht op vervroegde verkoop terug aan uitgever.
Maakt obligatie aantrekkelijker maar geeft liquiditeitsrisico aan
vennootschap.

#### Valkuilen

- 💼 **Bestuurder** vuistregel: één grote terugbetaling kan
  **liquiditeitsklem** veroorzaken — plan refinancing minstens 12–18 maanden
  vooraf, of overweeg sinking fund van bij uitgifte.
- 📋 **Boekhouder** 🧮: bij vervroegde aflossing met premie — de premie is
  geen rente maar een **kapitaalverlies** dat eigen behandeling vraagt.

---

## 🎯 Perspectieven per actor (transactie-zijden)

### Vennootschap-uitgever

**Boekhouding** ⚖️: alle boekingen hierboven; 170 schuld + 201
uitgiftekosten + 490x agio/disagio + 492 prorata + 650 rentelasten.

**Fiscaal** 🧮: rentelasten (coupon + disagio-spreiding) zijn aftrekbare
beroepskost ⚖️ `art. 49 WIB92`. Agio-opname vermindert aftrekbare last
symmetrisch. → edge `valt_onder_regime: aftrekbaarheid-financieringskosten`

⚠️ **Te verifiëren**: interactie met **thin cap-regels** / **EBITDA-regel
art. 198/1 WIB92** bij hoge schuldgraad.

**Toelichting jaarrekening** ⚖️ `KB WVV` (artikel-precies te verifiëren):
- vermelding obligatielening per rubriek 17
- spreidingsmethode agio/disagio in waarderingsregels
- looptijd-vervalkalender (afzonderlijk per tranche indien sinking fund)

**Formaliteiten** ⚖️ `WVV art. 7:54 e.v.`:
- besluit van het bestuursorgaan
- emissieprospectus of informatienota (bij publieke uitgifte —
  ⚠️ drempel/voorwaarden uit Prospectusverordening te verifiëren)
- vergadering obligatiehouders bij wijziging voorwaarden ⚖️ `WVV art. 7:62`

### Belegger — natuurlijke persoon (privé)

**Bij aankoop**: betaalt aan uitgifteprijs (€ 950 / € 1.000 / € 1.050).

**Tijdens looptijd**:
- ⚖️ ontvangt coupon = roerend inkomen → **RV** ingehouden bij
  uitbetalende instelling → edge `valt_onder_regime: roerende-voorheffing-rente`
- ⚠️ Tarief: zie [Cijferzakboekje §X] — nog niet als bron geladen

**Op vervaldag**: ontvangt nominaal. Verschil met aankoopprijs (€ 50
meerwaarde bij disagio, € 50 verlies bij agio):
- → edge `valt_onder_regime: meerwaarde-obligaties-privé`
- ⚠️ Behandeling als financiële roerende inkomsten? — te verifiëren met
  fiscale bron

### Belegger — vennootschap

**Boekhouding** ⚖️ `MAR rubriek 51` (vastrentende effecten): aankoop op
rekening 51 aan kostprijs; agio/disagio gespiegeld aan de uitgever
(over te dragen opbrengst/kost).

**Fiscaal** 🧮: coupons + spreiding belastbaar als financiële opbrengst
in vennootschapsbelasting. **Geen DBI** — DBI geldt voor dividenden, niet
voor rente.

---

## 💰 Fiscale gevolgen (samenvatting)

| Actor | Behandeling | Edge naar regime |
|---|---|---|
| Vennootschap-uitgever | Rentelasten aftrekbaar (⚖️ art. 49 WIB92); ⚠️ EBITDA-regel te verifiëren | `aftrekbaarheid-financieringskosten`, `ebitda-regel-198-1` |
| Belegger — NP — coupon | RV ingehouden | `roerende-voorheffing-rente` |
| Belegger — NP — meerwaarde | ⚠️ Te verifiëren | `meerwaarde-obligaties-privé` |
| Belegger — vennootschap | Financiële opbrengst belastbaar; geen DBI | `vennootschapsbelasting-fin-opbrengst` |

*(Tarieven en drempels: zie [Cijferzakboekje] — nog niet als bron geladen.)*

---

## 🎯 Speelruimte vs regelgeving

| Hard kader (regelgeving) | Speelruimte (keuze) |
|---|---|
| ⚖️ Boeking op 170 + 490x + 492 (MAR) | Spreidingsmethode agio/disagio: lineair (eenvoudig) of effective interest (zuiverder) |
| ⚖️ Aftrekbaarheid rente bij vennootschap | Vast vs variabel coupon — beïnvloedt timing belastbare basis |
| ⚖️ RV inhouding bij belegger | Pari / disagio / agio — twee knoppen voor één marktrendement |
| ⚖️ Spreidingsplicht agio/disagio + uitgiftekosten | Looptijd-keuze (5–30 j) |
| ⚖️ Toelichtingsplicht in jaarrekening | Nominaal per obligatie (retail vs institutioneel) |
| ⚖️ Prospectus-/informatienota-plicht boven drempel | Aflossingsstructuur: bullet, sinking fund, call/put |

---

## ⚠️ Valkuilen (overall, na de beslissing)

*Bouwsteen-specifieke valkuilen staan bij elke bouwsteen. Hier alleen
overkoepelende.*

- 📋 **Bestuurder** ⚖️ `WVV art. 7:62`: bij wijziging van voorwaarden
  (uitstel, restructuring) is een vergadering van obligatiehouders verplicht —
  niet onderhandelbaar per individuele houder.
- 📋 **Bestuurder** 💼: stress-test op couponverplichting bij meerjaren-budget;
  veel ondernemingen onderschatten cumulatieve last over hele looptijd.
- 💼 **Adviseur** vuistregel: bij vergelijking met banklening — toon altijd
  *totale jaarlijkse kost* (coupon + agio/disagio-spreiding +
  uitgiftekosten-spreiding) en *werkelijke rente* (YTM-niveau), niet alleen
  couponrente.
- 📋 **Boekhouder** ⚖️: bij call-clausule activering — premie boven pari is
  geen rente maar kapitaalverlies; aparte behandeling.

---

## Alternatieven (zelfde doel)

→ synthese: `vergelijking-lange-termijn-financieringsinstrumenten`
  *(banklening · obligatielening · achtergestelde lening · converteerbare
  obligatie · kapitaalverhoging · winstdelende lening)*

→ synthese: `vergelijking-vreemd-vs-eigen-vermogen-financiering`

---

## Edges & bronnen

**Bronnen** (`valt_onder_bron`):
- ⚖️ `CBN-2019-07` — Boekhoudkundige verwerking van uitgifte obligatielening
- ⚖️ `CBN-148-4` — Prorata-intrest schulden
- ⚖️ `WVV art. 7:54 e.v.` — Uitgifte obligaties NV
- ⚖️ `WVV art. 7:62` — Vergadering obligatiehouders
- ⚖️ `KB WVV art. 3:37` — Spreiding uitgifte-kosten en agio/disagio
- ⚖️ `KB WVV art. 3:60` — Toe te rekenen kosten
- ⚖️ `MAR rubriek 17` — Schulden op meer dan één jaar
- ⚖️ `art. 49 WIB92` — Aftrekbaarheid beroepskosten
- ⚠️ `art. 198/1 WIB92` — EBITDA-regel (interactie te verifiëren)

**Regimes** (`valt_onder_regime`):
- `aftrekbaarheid-financieringskosten`
- `ebitda-regel-198-1` ⚠️
- `roerende-voorheffing-rente`
- `meerwaarde-obligaties-privé` ⚠️
- `vennootschapsbelasting-fin-opbrengst`

**Gerelateerde concepten** (`gerelateerd`):
- `converteerbare-obligatie` *(hybride met conversierecht — andere
  behandeling, deels eigen-vermogen)*
- `banklening`
- `kapitaalverhoging`
- `oprichtingskosten`

**Onderdeel-van**:
- `schulden-op-meer-dan-een-jaar` (rubriek 17 MAR)

---

## Wat deze mockup test

1. **Accountant-bril vooraan** — voor wie / wanneer wel / wanneer niet /
   hoofdrisico / hoofdvoordeel staat *vóór* de definitie.
2. **Recursie** — bouwsteen → sub-bouwsteen → berekening + illustratie +
   voorbeeld + valkuilen, max 3 niveaus diep.
3. **Confidence op claim-niveau** — ⚖️ / 🧮 / 💼 / ⚠️ per zin/bewering,
   niet alleen per rubriek.
4. **Perspectieven per actor** in één record — uitgever, belegger NP,
   belegger venn., elk met boekhouding + fiscaal + formaliteiten — geen
   mirror-records.
5. **Illustraties** (T-rekeningen, balans-tabellen) naast voorbeelden
   (proza) en berekeningen (formule + cijfers) — drie aparte rubriek-types.
6. **Speelruimte** als tabel hard-kader-vs-keuze met concrete keuzes,
   niet vaag.
7. **Open rubrieken**: niet alles ingevuld waar irrelevant (bv. geen
   personenbelasting bij eenmanszaak-belegger — dat scenario speelt
   hier niet).
8. **`⚠️ te_verifiëren`-markeringen** waar bronnen ontbreken (Cijferzakboekje,
   EBITDA-regel) — eerlijk over wat we niet zeker weten.

## Wat nog schurt

- **Lengte**: ~3× het oude record. Bij 460 records wordt het project nóg
  groter. Mitigatie: presentatielaag maakt rubrieken collapsible (zoals jij
  noemde).
- **Cijferzakboekje**: tarieven blijven "[zie zakboekje]" — blokkerend voor
  echte mechaniek-uitleg op fiscale uitkomst-rubriek.
- **Schema-terminologie**: `kind` als tag-set vs node_type — moet nog
  formeel landen in ADR-024. We hebben nu *praktisch* getoond hoe een
  instrument eruitziet, niet *formeel* gedefinieerd.
- **YTM** wordt vier keer vernoemd als vuistregel zonder uitwerking. Eigen
  ratio-record `yield-to-maturity` of als sub-bouwsteen in deze record?
- **Converteerbare obligatie**: had vorige record als "in_praktijk"
  vermelding. Hier verwijzing via edge — voldoende, of eigen mini-bouwsteen?
