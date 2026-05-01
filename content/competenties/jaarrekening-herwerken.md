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

## Aanbevolen werkwijze

### 1. 🔍 Schema vaststellen

> 📥 **Nodig**:
> - De jaarrekening of de vermelding van het toepasselijke schema

> 📤 **Uitkomst**:
> - Schema-type (volledig, verkort of micro) en het beschikbare detailniveau

Het schema bepaalt hoever de herwerking kan gaan. Bij een volledig schema zijn alle rubrieken beschikbaar. Bij een verkort schema ontbreken sommige subrubrieken — bepaalde hergroeperingen en ratio's zijn dan niet mogelijk.

→ Zie [[financiele-ratios#-schema-beperkingen|Schema-beperkingen]] voor het overzicht van welke ratio's per schema beschikbaar zijn.

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

De wettelijke balans is geordend naar juridische categorieën (immaterieel, materieel, financieel, ...). Voor analyse wordt ze omgezet naar een **functionele indeling**:

**Activazijde** — gegroepeerd naar liquiditeit:

| Herwerkte rubriek | Inhoud | NBB-codes |
|---|---|---|
| Vaste activa | Immaterieel + materieel + financieel | 20/28 |
| Voorraden | Voorraden en bestellingen in uitvoering | 3 |
| Handelsvorderingen KT | Vorderingen op korte termijn op klanten | 40 |
| Overige vorderingen KT | Andere kortlopende vorderingen | 41 |
| Liquide middelen | Geldbeleggingen + kassen | 50/58 |
| Overlopende rekeningen actief | Toe te rekenen opbrengsten, over te dragen kosten | 490/1 |

**Passivazijde** — geordend naar toenemende eisbaarheid (→ zie [[jaarrekeninganalyse#-volgorde-van-de-rubrieken-op-het-passief|Volgorde rubrieken passief]]):

| Herwerkte rubriek | Inhoud | NBB-codes |
|---|---|---|
| Eigen vermogen | Kapitaal + reserves + overgedragen resultaat + herwaarderingsmeerwaarden | 10/15 |
| Voorzieningen | Toekomstige verplichtingen | 16 |
| Schulden op lange termijn | Schulden met looptijd > 1 jaar | 17 |
| Schulden op korte termijn | Leveranciersschulden + belastingschulden + kortlopende leningen | 42/48 |
| Overlopende rekeningen passief | Toe te rekenen kosten, over te dragen opbrengsten | 492/3 |

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

→ Zie [[jaarrekeninganalyse#-herstructurering-van-de-resultatenrekening|Herstructurering resultatenrekening]] voor toelichting per niveau.

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

De kernbalansaggregaten condenseren de herstructurering tot drie kerncijfers die de financiering van de bedrijfscyclus beschrijven.

→ Formules en betekenis: [[jaarrekeninganalyse#-balansaggregaten|Balansaggregaten]]

**NBK** = Vlottende activa − Schulden KT → meet de globale kortetermijnbuffer

**WKB** = Voorraden + Handelsvorderingen − Leveranciersschulden → meet de financieringsbehoefte uit de bedrijfscyclus

**Nettokaspositie** = Liquide middelen − Kortlopende financiële schulden → meet de nettokaspositie

De relatie: NBK = WKB + nettokaspositie. Als NBK > WKB: overschot aan liquide middelen. Als NBK < WKB: de bedrijfscyclus vreet meer dan de kortetermijnbuffer aankan — de onderneming leunt op kaskrediet.

> [!tip]- Herwerking is voorbereiding, geen doel op zich
> Hoe ver je herstructureert, hangt af van welke ratio's en aggregaten je daarna wil berekenen. Voor een pure liquiditeitsanalyse volstaat het berekenen van NBK en de quick ratio. Voor een volledige beoordeling (→ [[financiele-positie-beoordelen]]) werk je alle niveaus uit.

---

## Voorbeelden

> [!example]- NBK, WKB en nettokaspositie vanuit een gestructureerde balans
>
> **Situatie**: handelsonderneming (in €): voorraden 300.000; handelsvorderingen 400.000; liquide middelen 80.000; leveranciersschulden 250.000; kortlopende leningen 220.000; overige KT-schulden 210.000; vaste activa 1.200.000; langetermijnschulden 500.000; eigen vermogen 800.000.
>
> **Conclusie**: NBK = € 100.000 (positief maar smal); WKB = € 450.000 (hoge bedrijfscyclusfinanciering); nettokaspositie = −€ 140.000 (leunt op kaskrediet)
>
> **Grondslag**: [[jaarrekeninganalyse#-balansaggregaten|Balansaggregaten]]
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
> **Grondslag**: [[jaarrekeninganalyse#-eigen-vermogen-in-het-kortmodel-nbb|EV kortmodel NBB]]
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
> > *Zie: [[jaarrekeninganalyse#-nbk-verhogen-hoe|NBK verhogen]]*
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
> > *Zie: [[jaarrekeninganalyse#-volgorde-van-de-rubrieken-op-het-passief|Volgorde rubrieken passief]]*
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
