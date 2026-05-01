---
tags: ["1.2", "1.3", wip, materie]
niveau: integratie
status: draft
bronnen: []
itaa-lex: ""
---

# Jaarrekeninganalyse — begrippen en structuurkennis

Deze fiche bevat de **begrippen en analytische structuren** die de basis vormen voor jaarrekeninganalyse: wat zijn de analytische categorieën, wat betekenen de aggregaten, welke patronen zijn kenmerkend. De **techniek** om de jaarrekening stap voor stap te herstructureren staat in [[jaarrekening-herwerken]]; de techniek om te beoordelen en te adviseren staat in [[financiele-positie-beoordelen]].

---

## 📌 Analytische indeling van de balans

De wettelijke jaarrekening groepeert rubrieken op juridische basis. Voor analyse herschik je die naar **economische functie**: wat is snel beschikbaar (vlottend), wat blijft lang (vast), wie heeft het langst recht op terugbetaling (eigen vermogen), wie het kortst (schulden KT).

De herstructurering is in de meeste gevallen een **optelling van bestaande rubrieken** — niet een nieuwe berekening. Het NBB-schema geeft al subtotalen per rubriek; je hergroepeert die naar analytische categorieën.

### Activazijde

| Analytische categorie | Omschrijving | NBB-code |
|---|---|---|
| **Vaste activa** | Immateriële + materiële + financiële vaste activa | 20/28 |
| &nbsp;&nbsp;↳ Immateriële vaste activa | Ontwikkelingskosten, concessies, goodwill | 20/21 |
| &nbsp;&nbsp;↳ Materiële vaste activa | Terreinen, gebouwen, installaties, rollend materieel | 22/27 |
| &nbsp;&nbsp;↳ Financiële vaste activa | Deelnemingen, vorderingen LT | 28 |
| **Vlottende activa** | Omzetbaar binnen één bedrijfscyclus | 29/58 |
| &nbsp;&nbsp;↳ Voorraden | Goederen, grondstoffen, onderhanden werk | 3 |
| &nbsp;&nbsp;↳ Handelsvorderingen KT | Klanten die nog moeten betalen | 40/41 |
| &nbsp;&nbsp;↳ Geldbeleggingen | Kortlopende beleggingen | 50/53 |
| &nbsp;&nbsp;↳ Liquide middelen | Kas en bankrekeningen | 54/58 |
| &nbsp;&nbsp;↳ Overlopende rekeningen actief | Over te dragen kosten, verkregen opbrengsten | 490/1 |

### Passivazijde (volgorde: toenemende eisbaarheid)

| Analytische categorie | Omschrijving | NBB-code |
|---|---|---|
| **Eigen vermogen** | Geen terugbetalingsverplichting | 10/15 |
| **Voorzieningen en uitgestelde belastingen** | Toekomstige risico's en verplichtingen | 16 |
| **Vreemd vermogen LT** | Schulden met looptijd > 1 jaar | 17 |
| **Vreemd vermogen KT** | Schulden vervallend binnen 12 maanden | 42/48 |
| &nbsp;&nbsp;↳ incl. overlopende rekeningen passief | Toe te rekenen kosten, over te dragen opbrengsten | 492/3 |

> [!info]- Voorbeeld: een vereenvoudigde balans voor en na herstructurering
>
> 🤖 *AI-aanvulling*
>
> **Wettelijk schema (verkort)**
> ```
> ACTIEF                              PASSIEF
> ─────────────────────────────────   ──────────────────────────────────
> 20/28  Vaste activa     200.000     10/15  Eigen vermogen     180.000
>   22/27  Mat. VA        150.000     16     Voorzieningen       15.000
>   28     Fin. VA         50.000     17     Schulden > 1 jr     90.000
>                                     42/48  Schulden ≤ 1 jr    145.000
> 3      Voorraden         80.000
> 40/41  Vorderingen KT  100.000
> 54/58  Liquide midd.    50.000
> ─────────────────────────────────   ──────────────────────────────────
>                         430.000                                430.000
> ```
>
> **Analytisch formaat**
> ```
> ACTIEF                              PASSIEF
> ─────────────────────────────────   ──────────────────────────────────
> Vaste activa         200.000        Eigen vermogen         180.000
>                                     Vreemd verm. LT        105.000  (17+16)
> Vlottende activa     230.000        Vreemd verm. KT        145.000
>   Voorraden  80.000
>   Vord. KT  100.000
>   Liquide    50.000
> ─────────────────────────────────   ──────────────────────────────────
>                         430.000                                430.000
> ```
>
> **Berekeningen:**
> - NBK = Vlottende activa − Vreemd verm. KT = 230.000 − 145.000 = **€ 85.000** ✓
> - WKB = Voorraden + Handelsvorderingen − Leveranciersschulden
>   (leveranciersschulden zijn deel van 42/48 — hier niet apart gegeven)
> - Nettokaspositie = Liquide middelen − Financiële schulden KT
>   (financiële schulden KT zijn deel van 42/48 — hier niet apart gegeven)

---

## 📌 Resultaatniveaus

De resultatenrekening kent functionele niveaus, van bruto naar netto:

| Niveau | Omschrijving |
|--------|-------------|
| **Brutomarge** | Omzet − kostprijs van verkochte goederen |
| **Bedrijfsresultaat (EBIT)** | Brutomarge − bedrijfskosten (personeel, [[afschrijvingen\|afschrijvingen]], [[waardeverminderingen\|waardeverminderingen]], overige) |
| **Financieel resultaat** | Financiële opbrengsten − financiële kosten (intresten, wisselkoersverschillen) |
| **Resultaat vóór belastingen (EBT)** | EBIT + financieel resultaat |
| **Nettowinst** | EBT − belastingen op het resultaat |
| **EBITDA** | EBIT + [[afschrijvingen\|afschrijvingen]] + [[waardeverminderingen\|waardeverminderingen]] *(niet-kaskosten worden terug opgeteld — zie [[kasstroomanalyse\|kasstroomanalyse]])* |

EBITDA-toelichting: afschrijvingen en waardeverminderingen worden in EBIT als kost afgetrokken, maar zijn geen effectieve kasuitstroom. Ze worden terug opgeteld om een proxy te krijgen voor de operationele kascreatie vóór financiering en belastingen.

---

## 📌 Balansaggregaten

Kernaggregaten die voortvloeien uit de herstructurering:

**Netto bedrijfskapitaal (NBK)**
= Vlottende activa − Kortlopend vreemd vermogen

Het NBK geeft aan in welke mate de onderneming haar vlottende activa kan financieren zonder op kortlopend vreemd vermogen te moeten rekenen. Een positief NBK is een buffer; een negatief NBK wijst op een financieringsspanning.

**Werkkapitaalbehoefte (WKB)**
= Voorraden + Handelsvorderingen − Leveranciersschulden

De WKB is de financieringsbehoefte die voortvloeit uit de bedrijfscyclus zelf: hoeveel geld is er nodig om de kloof te overbruggen tussen betalen van leveranciers en ontvangen van klanten?

**Nettokaspositie**
= Liquide middelen − Kortlopende financiële schulden

De nettokaspositie toont of de beschikbare kassen de kortlopende financiële verplichtingen kunnen dekken.

> [!info]- In de praktijk: NBK, WKB en nettokaspositie berekenen
>
> Een handelsonderneming heeft (in €):
>
> | Actief | | Passief | |
> |--------|---|---------|---|
> | Voorraden | 300.000 | Eigen vermogen | 800.000 |
> | Handelsvorderingen | 400.000 | Langetermijnschulden | 500.000 |
> | Liquide middelen | 80.000 | Leveranciersschulden | 250.000 |
> | Vaste activa | 1.200.000 | Kortlopende leningen | 220.000 |
> | | | Overige KT-schulden | 210.000 |
>
> - **NBK** = Vlottende activa − Kortlopend vreemd vermogen = (300 + 400 + 80) − (250 + 220 + 210) = **780.000 − 680.000 = € 100.000** → kleine buffer
> - **WKB** = Voorraden + Handelsvorderingen − Leveranciersschulden = 300 + 400 − 250 = **€ 450.000** → de bedrijfscyclus vraagt € 450.000 aan financiering
> - **Nettokaspositie** = Liquide middelen − Kortlopende financiële schulden = 80 − 220 = **− € 140.000** → de kassen dekken de kortlopende financiering niet
>
> Interpretatie: het NBK is positief maar smal (€ 100.000); de WKB is aanzienlijk (€ 450.000) — er is een structurele financieringskloof van € 350.000 (WKB − NBK) die door de kortlopende leningen (€ 220.000) en overschot op andere KT-schulden wordt gedekt. De nettokaspositie is negatief: de onderneming leunt op haar kaskrediet.
>
> 🤖 *AI-aanvulling*

---

## 📌 Volgorde van de rubrieken op het passief

Het passief van de balans is geordend naar **toenemende eisbaarheid**: van het minst eisbare (eigen vermogen — geen terugbetalingsverplichting) naar het meest eisbare (schulden op korte termijn — onmiddellijk opeisbaar).

| Volgorde | Rubriek | Eisbaarheid |
|---|---|---|
| 1 | Eigen vermogen | Geen — alleen bij liquidatie of dividendbeslissing |
| 2 | Voorzieningen en uitgestelde belastingen | Onzeker — afhankelijk van toekomstige gebeurtenissen |
| 3 | Schulden op meer dan één jaar | Laag — vervalt pas na meer dan 12 maanden |
| 4 | Schulden op ten hoogste één jaar | Hoog — vervalt binnen 12 maanden |
| 5 | Overlopende rekeningen passief | Hoog — toe te rekenen kosten en over te dragen opbrengsten |

📝 *Voorbeeldexamen 2024: "In welke volgorde zijn rubrieken op Passief van de Balans gerangschikt? → Toenemende eisbaarheid"*

## 🔢 Eigen vermogen in het kortmodel (NBB)

Voor een **kapitaalvennootschap** in het **verkort schema** wordt het eigen vermogen als volgt berekend:

> EV = Geplaatst kapitaal + Uitgiftepremies + Herwaarderingsmeerwaarden + Reserves + Overgedragen winst (of − verlies) + Kapitaalsubsidies

In het kortmodel is het eigen vermogen één gecombineerde rubriek — de afzonderlijke componenten (kapitaal, reserves, enz.) worden niet apart vermeld zoals in het volledig schema.

📝 *Voorbeeldexamen 2024: "JR kort model NBB voor kapitaal vennootschap wordt EV als volgt berekend"*

🤖 *AI-aanvulling — exacte NBB-coderingen: ⚠️ verifieer via KB 21/10/2018 MAR*

## 🔢 Effect van boekhoudkundige keuzes op ratio's

Boekhoudkundige keuzes beïnvloeden de ratio's zonder de economische realiteit te veranderen. De brutoverkoopmarge is een veelgetoetst voorbeeld.

**Brutoverkoopmarge = Toegevoegde waarde / Netto-omzet**

Afschrijvingen maken deel uit van de **bedrijfskosten** — ze liggen **onder** de brutoverkoopmarge in de resultatenrekening. Een verhoging van afschrijvingen verlaagt het bedrijfsresultaat (EBIT) maar heeft **geen effect** op de brutoverkoopmarge.

| Keuze | Effect op brutoverkoopmarge | Effect op EBIT |
|---|---|---|
| Afschrijving verhogen | ❌ Geen | Daalt |
| Voorraadwaardering verlagen | ✓ Daalt | Daalt |
| Omzet verhogen | ✓ Stijgt (als marge > 0) | Stijgt |

📝 *Voorbeeldexamen 2024: "Verhoging van de afschrijving op gebouwen heeft het volgende effect op de bruto verkoopmarge → Geen"*

> [!warning]- Afschrijving verhogen verlaagt de brutoverkoopmarge
> ❌ *"Als Alfa verlieslatend is en de afschrijving verhoogt, zal de brutoverkoopmarge dalen."*
>
> Afschrijvingen liggen structureel **onder** het brutomargepeil in de resultatenrekening. De brutoverkoopmarge = (omzet − kostprijs goederen) / omzet. Afschrijvingen zijn bedrijfskosten die pas ná de brutomarge in mindering komen. Ze verlagen EBIT, niet de brutomarge.
>
> 📝 *Voorbeeldexamen 2024*

## 🔎 NBK verhogen: hoe?

Een laag netto-bedrijfskapitaal (NBK = vlottende activa − schulden KT) kan verbeterd worden door de teller te verhogen of de noemer te verlagen:

**Vlottende activa verhogen:**
- Kapitaalverhoging in cash → meer liquide middelen
- Langetermijnlening aantrekken voor werkkapitaalfinanciering → schulden verschuiven van KT naar LT
- Vorderingen sneller innen (kortere klantenbetalingstermijn)

**Schulden op korte termijn verlagen:**
- Kortlopende leningen herfinancieren als langetermijnschuld
- Leveranciersschulden verlengen (langere betalingstermijnen bedingen)
- Kortetermijnschulden aflossen met eigen middelen of langetermijnfinanciering

📝 *Voorbeeldexamen 2013/2: "Het netto bedrijfskapitaal van zijn vennootschap is zeer laag. Geef drie voorbeelden hoe hij het kan verhogen."*

🤖 *AI-aanvulling*

## ⚖️ Contextualisering

Cijfers krijgen pas betekenis wanneer ze worden vergeleken:

- **Sectorgemiddelden**: een brutomarge van 15% kan hoog zijn in de detailhandel maar laag in de industrie
- **Historische trend**: is de marge stijgend, stabiel of dalend over drie jaar?
- **Nationale en internationale context**: recessie, rentestijgingen, sectorspecifieke wetgeving
- **Bedrijfsdomein**: een kapitaalintensieve onderneming heeft hoge afschrijvingen die EBIT drukken — vergelijking via EBITDA is dan zinvoller

---

> [!warning]- Een hogere winst betekent altijd een betere financiële positie
> ❌ *"De onderneming boekt een stevige winst — de financiële situatie is dus gezond."*
>
> Winst en liquiditeit zijn twee verschillende dingen. Een winstgevende onderneming kan in betalingsmoeilijkheden verkeren als haar werkkapitaalbehoefte snel stijgt — bijvoorbeeld doordat klanten trager betalen of voorraden oplopen. De [[kasstroomanalyse|kasstroomanalyse]] en de [[jaarrekeninganalyse#-balansaggregaten|balansaggregaten]] (NBK, WKB) geven een completere gezondheidscheck dan winst alleen.
>
> 🤖 *AI-aanvulling*

> [!warning]- EBIT en EBITDA zijn hetzelfde
> ❌ *"EBIT en EBITDA zijn twee namen voor hetzelfde — het bedrijfsresultaat voor belastingen."*
>
> EBIT is het bedrijfsresultaat ná [[afschrijvingen|afschrijvingen]] en [[waardeverminderingen|waardeverminderingen]]. EBITDA voegt die niet-kaskosten terug bij voor een proxy van de operationele kascreatie. Voor kapitaalintensieve sectoren (bouw, industrie, telecom) is EBITDA zinvoller voor vergelijking, omdat afschrijvingsbeleid sterk kan verschillen. EBIT en EBITDA kunnen voor dezelfde onderneming sterk van elkaar afwijken.
>
> 🤖 *AI-aanvulling*

---

## Relevant voor

**[[1.2-boekhoudrecht-en-jaarrekeningenrecht|1.2 Boekhoudrecht en jaarrekeningenrecht]]**

Kenniselementen:
- Herstructurering van de balans en resultatenrekening
- Balansaggregaten (NBK, WKB, nettokaspositie)

**[[1.3-analyse-en-kritische-beoordeling-jaarrekening|1.3 Analyse en kritische beoordeling van de jaarrekening]]**

Taken:
- *Analyse en beoordeling van de financiële situatie aan de hand van de jaarrekeningen, ratio's en kengetallen*
  - In staat zijn om de jaarrekeningen kritisch te bekijken

Kenniselementen:
- II.B — Jaarrekening: activa, passiva, resultatenrekening, toelichting
- II.C.1 — Herwerking van de jaarrekening
- II.C.2 — Netto-bedrijfskapitaal

### Voorbeeldvragen

> [!question]- Netto bedrijfskapitaal (NBK) berekenen
>
> Een onderneming heeft: vlottende activa € 450.000; kortlopend vreemd vermogen € 300.000; langlopende schulden € 500.000. Wat is het netto bedrijfskapitaal?
>
> > [!success]- Antwoord
> >
> > **NBK = € 150.000.**
> >
> > NBK = Vlottende activa − Kortlopend vreemd vermogen = € 450.000 − € 300.000 = **€ 150.000**. Langlopende schulden tellen niet mee. Een positief NBK van € 150.000 betekent dat de vlottende activa ruimer zijn dan de kortlopende verplichtingen — er is een buffer.
> >
> > *Zie: [[jaarrekeninganalyse#-balansaggregaten|Balansaggregaten]]*
>
> 🤖 *AI-aanvulling*

> [!question]- EBIT vs. EBITDA
>
> Een onderneming heeft een EBIT van € 300.000 en jaarlijkse afschrijvingen van € 80.000. Haar EBITDA bedraagt € 220.000.
>
> Juist of fout?
>
> > [!success]- Antwoord
> >
> > **Fout.**
> >
> > EBITDA = EBIT + afschrijvingen + waardeverminderingen. Afschrijvingen worden bij EBIT **opgeteld** (ze waren al als kost afgetrokken en worden terug bijgeteld voor de cashproxy). EBITDA = € 300.000 + € 80.000 = **€ 380.000**, niet € 220.000.
> >
> > *Zie: [[jaarrekeninganalyse#-herstructurering-van-de-resultatenrekening|Resultatenrekening herstructurering]]*
>
> 🤖 *AI-aanvulling*

Taken:
- *Opstellen van de individuele jaarrekening*
  - Herstructureren van de balans en de resultatenrekening (doelstelling 1)
  - Identificeren en interpreteren van de balansaggregaten (doelstelling 2)
  - Contextualiseren van de interpretaties (doelstelling 5)
