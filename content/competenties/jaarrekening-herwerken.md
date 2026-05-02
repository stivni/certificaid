---
tags: ["1.2", "1.3", wip, competentie]
niveau: toepassen
status: draft
programmaonderdelen: ["1.2", "1.3"]
itaa-lex-secties:
  - XIII KB 21/10/2018 (MAR — schema's volledig/verkort/micro)
  - XV (WVV Boek 3 — jaarrekeningvereisten)
---

# Jaarrekening herwerken

De officiële jaarrekening (wettelijk schema) omvormen naar een analytisch bruikbaar formaat: functionele hergroepering van balans en resultatenrekening, en berekening van de kernbalansaggregaten.

> [!info]- Grondslag van deze werkwijze (🤖 50% · ⚖️ 50%)
> Er bestaat geen ITAA-norm die de herstructurering van de jaarrekening als taakprocedure beschrijft. De procedure volgt uit twee bronnen:
> - **Schema en codes** (stap 1–2): de rubrieksindeling en NBB-codes zijn vastgelegd in het **[[wetteksten/XIII-KB-wer-boekhouding|KB 21/10/2018]]** (MAR). Dit deel is niet vrij te kiezen.
> - **Analytische hergroepering** (stap 2–4): welke rubrieken bij vlottend actief, schulden KT of EBITDA horen, is gebaseerd op **NBB-documentatie en beroepspraktijk** 🤖 — niet in een norm vastgelegd.

## Aanbevolen werkwijze

### 1. 🔍 Schema vaststellen

> 📥 **Nodig**:
> - De jaarrekening of de vermelding van het toepasselijke schema

> 📤 **Uitkomst**:
> - Schema-type (volledig, verkort of micro) en het beschikbare detailniveau

Het schema bepaalt hoever de herwerking kan gaan. Bij een volledig schema zijn alle rubrieken beschikbaar. Bij een verkort schema ontbreken sommige subrubrieken — bepaalde hergroeperingen en [[financiele-ratios#-schema-beperkingen|ratio's]] zijn dan niet mogelijk.

> [!warning]- Microschema herstructureren alsof het een volledig schema is
> ❌ *"Ik herstructureer het microschema op dezelfde manier als het volledig schema."*
>
> Het microschema bevat minder rubrieksdetail dan het verkort schema. Hergroeperingen die een onderscheid vereisen tussen bv. handelsvorderingen en overige vorderingen zijn niet mogelijk. Vermeld dit expliciet als het de gevraagde analyse beperkt.
>
> 🤖 *AI-aanvulling*

---

### 2. 📋 Herstructureer de balans

> 📥 **Nodig**:
> - Balans uit de jaarrekening (activazijde en passivazijde)

> 📤 **Uitkomst**:
> - Hergestructureerde balans met functionele groepering: vaste activa / vlottende activa aan actief; eigen vermogen / vreemd vermogen LT / vreemd vermogen KT aan passief

De wettelijke balans is geordend naar juridische categorieën. Je hergroepeert de bestaande rubrieken — dit is in de meeste gevallen **bestaande subtotalen kopiëren of optellen**, geen nieuwe berekening.

**Actief** (naar liquiditeit):
- `20/28` = vaste activa — staat al als subtotaal in de jaarrekening
- `29/58` = vlottende activa — ook al als subtotaal aanwezig

**Passief** (toenemende eisbaarheid):
- `10/15` = eigen vermogen → `16` = voorzieningen → `17` = schulden LT → `42/48` + `492/3` = schulden KT

Volledige NBB-code mapping per rubriek + voor/na-voorbeeld: [[balansaggregaten#-analytische-indeling-van-de-balans|Analytische indeling van de balans]]

> [!warning]- Overlopende rekeningen passief vergeten bij schulden KT
> ❌ *"Schulden op korte termijn zijn rubrieken 42 tot 48 — overlopende rekeningen zijn iets aparts."*
>
> Overlopende rekeningen passief (rubriek 492/3) bevatten toe te rekenen kosten en over te dragen opbrengsten — dat zijn reële kortetermijnverplichtingen. Bij het berekenen van het netto bedrijfskapitaal (vlottende activa − schulden KT) moeten ze als deel van de kortetermijnpassiva worden meegerekend. Ze worden ook meegenomen in de NBB-code 42/48 in brede zin.
>
> 🤖 *AI-aanvulling*

---

### 3. 📋 Herstructureer de resultatenrekening

> 📥 **Nodig**:
> - Resultatenrekening uit de jaarrekening

> 📤 **Uitkomst**:
> - Resultatenrekening met functionele niveaus: brutomarge → bedrijfsresultaat (EBIT) → EBT → nettowinst; en EBITDA als aanvullend aggregaat

De resultatenrekening wordt gereorganiseerd van bruto naar netto:

| Niveau | Berekening | NBB-codes |
|---|---|---|
| **Netto-omzet** | Omzet | 70 |
| **Toegevoegde waarde (TAW)** | Omzet + andere bedrijfsopbrengsten − aankopen − diensten en div. goederen ± voorraadwijzigingen | 9900 |
| **Bedrijfsresultaat (EBIT)** | TAW − personeelskosten − afschrijvingen − waardeverminderingen − andere bedrijfskosten | 9901 |
| **Resultaat vóór belastingen (EBT)** | EBIT + financieel resultaat + uitzonderlijk resultaat | 9903 |
| **Nettowinst** | EBT − belastingen | 9905/9906 |
| **EBITDA** | EBIT + afschrijvingen + waardeverminderingen | 9901 + 630/634 |

Definitie en toelichting per niveau: [[resultaatniveaus#-resultaatniveaus|Resultaatniveaus]]

> [!warning]- EBITDA berekenen door belastingen en rente bij nettowinst op te tellen
> ❌ *"EBITDA = nettowinst + belastingen + rente + afschrijvingen."*
>
> EBITDA = EBIT + afschrijvingen + waardeverminderingen. Vertrekpunt is het bedrijfsresultaat (EBIT), niet de nettowinst. Wie vanuit de nettowinst werkt, moet belastingen én financieel resultaat corrigeren — dat geeft hetzelfde eindresultaat, maar is gevoeliger voor fouten. Vertrek altijd vanuit EBIT als dat beschikbaar is.
>
> 🤖 *AI-aanvulling*

---

### 4. 🔢 Bereken de kernbalansaggregaten

> 📥 **Nodig**:
> - Hergestructureerde balans uit stap 2

> 📤 **Uitkomst**:
> - Netto bedrijfskapitaal (NBK), werkkapitaalbehoefte (WKB) en nettokaspositie

De [[balansaggregaten#-balansaggregaten|kernbalansaggregaten]] condenseren de herstructurering tot drie kerncijfers die de financiering van de bedrijfscyclus beschrijven.

**NBK** = Vlottende activa − Schulden KT → meet de globale kortetermijnbuffer

**WKB** = Voorraden + Handelsvorderingen − Leveranciersschulden → meet de financieringsbehoefte uit de bedrijfscyclus

**Nettokaspositie** = Liquide middelen − Kortlopende financiële schulden → meet de nettokaspositie

De relatie: NBK = WKB + nettokaspositie. Als NBK > WKB: overschot aan liquide middelen. Als NBK < WKB: de bedrijfscyclus vreet meer dan de kortetermijnbuffer aankan — de onderneming leunt op kaskrediet.

> [!tip]- Herwerking is voorbereiding, geen doel op zich
> Hoe ver je herstructureert, hangt af van welke ratio's en aggregaten je daarna wil berekenen. Voor een pure liquiditeitsanalyse volstaat het berekenen van NBK en de quick ratio. Voor een volledige beoordeling ([[financiele-positie-beoordelen]]) werk je alle niveaus uit.

---

## Voorbeelden

> [!example]- Resultatenrekening herwerken: van wettelijk schema naar analytisch formaat
>
> **Situatie**: onderstaande resultatenrekening (volledig schema, in €). Gevraagd: bereken TAW, EBIT, EBT, nettowinst en EBITDA.
>
> ```
> Wettelijk schema (selectie)
> ─────────────────────────────────────────────────────────────────
> 70   Omzet                                              6.000.000
> 74   Andere bedrijfsopbrengsten (excl. subsidies)          50.000
> 60   Aankopen handelsgoederen                          -2.400.000
> 61   Diensten en diverse goederen                        -600.000
> 3    Voorraadwijziging (stijging = +)                    +150.000
> 62   Bezoldigingen en soc. lasten                      -1.800.000
> 630  Afschrijvingen MVA                                  -400.000
> 634  Waardeverminderingen handelsvorderingen              -30.000
> 64   Andere bedrijfskosten                               -120.000
> 65   Financiële kosten (interesten)                       -90.000
> 75   Financiële opbrengsten                                10.000
> 67   Belastingen op het resultaat                        -190.000
> ─────────────────────────────────────────────────────────────────
> ```
>
> **Analytisch herwerkt:**
>
> ```
> Netto-omzet (70)                              6.000.000
> + Andere bedrijfsopbrengsten (74)                50.000
> − Aankopen (60)                              -2.400.000
> − Diensten en div. goederen (61)               -600.000
> + Voorraadwijziging (3)                        +150.000
> ─────────────────────────────────────────────────────────
> = Toegevoegde waarde (TAW)                    3.200.000   (53,3% omzet)
>
> − Personeelskosten (62)                      -1.800.000
> − Afschrijvingen (630)                         -400.000
> − Waardeverminderingen (634)                    -30.000
> − Andere bedrijfskosten (64)                   -120.000
> ─────────────────────────────────────────────────────────
> = EBIT                                          850.000   (14,2% omzet)
>
> + Financiële opbrengsten (75)                    10.000
> − Financiële kosten (65)                        -90.000
> ─────────────────────────────────────────────────────────
> = EBT                                           770.000
>
> − Belastingen (67)                             -190.000
> ─────────────────────────────────────────────────────────
> = Nettowinst                                    580.000   (9,7% omzet)
>
> EBITDA = EBIT + afschrijvingen + wverm.
>        = 850.000 + 400.000 + 30.000 =        1.280.000   (21,3% omzet)
> ```
>
> **Conclusie**: EBITDA € 1.280.000; EBIT € 850.000; nettowinst € 580.000.
>
> **Grondslag**: [[resultaatniveaus#-resultaatniveaus|Resultaatniveaus]]
>
> **Redenering**: startpunt is altijd de omzet (70). De TAW wordt berekend door alle directe kosten (60, 61, 3) af te trekken en andere bedrijfsopbrengsten (74) bij te tellen. Afschrijvingen (630) en waardeverminderingen (634) worden bij EBIT afgetrokken maar bij EBITDA terug opgeteld — ze zijn geen kasuitstroom. Financiële kosten liggen ónder EBIT en beïnvloeden de EBITDA niet.
>
> 🤖 *AI-aanvulling*

> [!example]- NBK, WKB en nettokaspositie vanuit een gestructureerde balans
>
> **Situatie**: handelsonderneming (in €): voorraden 300.000; handelsvorderingen 400.000; liquide middelen 80.000; leveranciersschulden 250.000; kortlopende leningen 220.000; overige KT-schulden 210.000; vaste activa 1.200.000; langetermijnschulden 500.000; eigen vermogen 800.000.
>
> **Conclusie**: NBK = € 100.000 (positief maar smal); WKB = € 450.000 (hoge bedrijfscyclusfinanciering); nettokaspositie = −€ 140.000 (leunt op kaskrediet)
>
> **Grondslag**: [[balansaggregaten#-balansaggregaten|Balansaggregaten]]
>
> **Redenering**:
> - Vlottende activa = 300 + 400 + 80 = 780.000
> - Schulden KT = 250 + 220 + 210 = 680.000
> - NBK = 780.000 − 680.000 = **€ 100.000**
> - WKB = 300 + 400 − 250 = **€ 450.000**
> - Nettokaspositie = 80 − 220 = **−€ 140.000**
> - Controle: NBK = WKB + nettokaspositie → 450.000 + (−140.000) = 310.000 ≠ 100.000 → verschil = overige KT-schulden (210.000) die niet in WKB zitten maar wel in NBK-noemer
>
> 🤖 *AI-aanvulling*

> [!example]- Eigen vermogen berekenen in het kortmodel
>
> **Situatie**: een kleine nv gebruikt het verkort schema. Geplaatst kapitaal: € 250.000; uitgiftepremies: € 0; herwaarderingsmeerwaarden: € 30.000; reserves: € 120.000; overgedragen winst: € 45.000; kapitaalsubsidies: € 15.000.
>
> **Conclusie**: eigen vermogen = € 460.000
>
> **Grondslag**: [[balansaggregaten#-eigen-vermogen-in-het-kortmodel-nbb|EV kortmodel NBB]]
>
> **Redenering**: EV = 250.000 + 0 + 30.000 + 120.000 + 45.000 + 15.000 = **€ 460.000**. In het kortmodel is eigen vermogen één gecombineerde rubriek — de opsomming van de componenten geeft het totaal.
>
> 📝 *Uit voorbeeldexamen 2024*

---

## Motiveren op het examen

**Een volledig antwoord bevat:**
1. Vermelding van het schema-type en eventuele beperkingen
2. Hergestructureerde balans met expliciete rubrieksgroepering (geen doorlinken vanuit de wettelijke posten)
3. Berekening van NBK, WKB en nettokaspositie met de gebruikte getallen
4. Bij EBITDA: vertrekpunt EBIT, niet nettowinst

**Typische vraagvormen**

> [!question]- NBK verhogen: welke maatregelen?
>
> Een student-ondernemer vraagt zijn accountant: "Het netto bedrijfskapitaal van mijn vennootschap is zeer laag. Geef drie voorbeelden hoe ik het kan verhogen."
>
> > [!success]- Antwoord
> >
> > **Drie mogelijke maatregelen (elke maatregel verhoogt vlottende activa of verlaagt schulden KT):**
> >
> > 1. **Langetermijnlening aantrekken voor werkkapitaalfinanciering** — kortetermijnschuld schuift naar langetermijnschuld: noemer daalt, NBK stijgt.
> > 2. **Kapitaalverhoging in cash** — eigen vermogen stijgt, liquide middelen stijgen: teller stijgt, NBK stijgt.
> > 3. **Kortlopende leningen herfinancieren als langetermijnschuld** — schulden KT dalen: noemer daalt, NBK stijgt.
> >
> > Andere geldige antwoorden: vorderingen sneller innen (debiteurendagen verkorten), langere betalingstermijnen bij leveranciers bedingen.
> >
> > *Zie: [[balansaggregaten#-nbk-verhogen-hoe|NBK verhogen]]*
>
> 📝 *Uit voorbeeldexamen 2013/2*

> [!question]- Volgorde rubrieken op het passief
>
> In welke volgorde staan de rubrieken op het passief van de balans gerangschikt?
>
> A. Toenemende eisbaarheid (eigen vermogen eerst, schulden KT het laatste)
> B. Afnemende eisbaarheid (schulden KT eerst, eigen vermogen het laatste)
> C. Alfabetische volgorde
> D. Op basis van liquiditeit
>
> > [!success]- Antwoord
> >
> > **A — Toenemende eisbaarheid.**
> >
> > Het passief is geordend van het minst eisbare (eigen vermogen — geen terugbetalingsverplichting) naar het meest eisbare (schulden op korte termijn — onmiddellijk opeisbaar). Daartussen: voorzieningen (onzeker), langetermijnschulden (laag), kortetermijnschulden (hoog), overlopende rekeningen passief (hoog).
> >
> > *Zie: [[balansaggregaten#-volgorde-van-de-rubrieken-op-het-passief|Volgorde rubrieken passief]]*
>
> 📝 *Uit voorbeeldexamen 2024*

---

## Relevant voor

**[[1.2-boekhoudrecht-en-jaarrekeningenrecht|1.2 Boekhoudrecht en jaarrekeningenrecht]]**

Taken:
- *Opstellen van de individuele jaarrekening*
  - Herstructureren van de balans en de resultatenrekening

Kenniselementen:
- II.B — Jaarrekening: activa, passiva, resultatenrekening, toelichting
- II.C.1 — Herwerking van de jaarrekening

**[[1.3-analyse-en-kritische-beoordeling-jaarrekening|1.3 Analyse en kritische beoordeling van de jaarrekening]]**

Taken:
- *Analyse en beoordeling van de financiële situatie aan de hand van de jaarrekeningen, ratio's en kengetallen*
  - In staat zijn om de jaarrekeningen kritisch te bekijken

Kenniselementen:
- II.C.1 — Herwerking van de jaarrekening
- II.C.2 — Netto-bedrijfskapitaal
