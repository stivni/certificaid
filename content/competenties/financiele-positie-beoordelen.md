---
tags: ["1.2", "1.3", wip, competentie]
niveau: integratie
status: draft
programmaonderdelen: ["1.2", "1.3"]
itaa-lex-secties:
  - XV (WVV Boek 3)
bouwversie: 0
---

# Financiële positie beoordelen

Aan de hand van een jaarrekening de financiële gezondheid van een onderneming beoordelen: ratio's en kasstromen berekenen, interpreteren in context, en een gemotiveerd oordeel formuleren.

> [!info]- Grondslag van deze werkwijze (🤖 100%)
> Er bestaat geen ITAA-norm die de financiële beoordeling als taakprocedure beschrijft. Alle stappen zijn gebaseerd op **analytische beroepspraktijk** 🤖 (NBB sectoranalyses, academische standaard). De stappen zijn logisch maar niet normatief vastgelegd.
>
> Uitzondering: als de beoordeling leidt tot vaststelling van [[continuiteitsrisico|continuïteitsrisico]], gelden de wettelijk genormeerde verplichtingen uit [[continuiteit-beoordelen]] (WVV en WER).

## Aanbevolen werkwijze

### 1. 🎯 Analysedoel bepalen

> 📥 **Nodig**:
> - De opdracht of analyseaanvraag: wie is de opdrachtgever en wat is de vraag?
>
> 📤 **Uitkomst**:
> - Geformuleerd analysedoel, eventueel met subvragen

Het analysedoel bepaalt welke ratio's relevant zijn en wat het verwachte eindoordeel is. Stel dit vast vóór je berekent — een analyse zonder doel leidt tot een opsomming van getallen zonder conclusie.

| Doel | Focus | Typische opdrachtgever |
|---|---|---|
| **Kredietbeoordeling** | Solvabiliteit, schuldaflossing, kasstroom | Bank, leverancier met krediet |
| **Liquiditeitsdiagnose** | Werkkapitaal, kortetermijndruk | Interne controle, cash management |
| **Winstgevendheidsoordeel** | Rentabiliteit, marges | Aandeelhouder, investeerder |
| **Brede financiële diagnose** | Alle dimensies, alarmsignalen | Adviseur, overnameonderzoek |


### 2. 📋 Herstructureer de jaarrekening

> 📥 **Nodig**:
> - Wettelijke jaarrekening (balans, resultatenrekening, toelichting) van de te analyseren entiteit
>
> 📤 **Uitkomst**:
> - Hergestructureerde balans en resultatenrekening

De wettelijke jaarrekening is opgesteld voor juridische en fiscale doeleinden, niet voor analyse. Gebruik ze nooit rechtstreeks voor ratioberekening — zet ze eerst om naar een analytisch formaat via [[jaarrekening-herwerken|jaarrekening herwerken]].


> [!warning]- Ratio's berekenen op de ongeherstructureerde wettelijke posten
> ❌ *"Ik neem gewoon de wettelijke balansposten voor de berekening."*
>
> De wettelijke indeling groepeert posten op juridische basis, niet op economische. Wie niet herstructureert, berekent ratio's op een vertekend beeld en trekt verkeerde conclusies.
>
> 🤖 *AI-aanvulling*

### 3. 🔀 Relevante ratio's selecteren

> 📥 **Nodig**:
> - Analysedoel uit stap 1
> - Hergestructureerde jaarrekening uit stap 2
>
> 📤 **Uitkomst**:
> - Geselecteerde ratio's met motivering van de keuze

Kies de [[financiele-ratios|ratio's]] (en eventuele [[kasstroomanalyse|kasstroomratio's]]) op basis van het analysedoel uit stap 1. Er bestaat geen universele set — de keuze is een professioneel oordeel dat je motiveert.

| Analysedoel | Aanbevolen ratio's |
|---|---|
| Kredietbeoordeling | Debt-to-equity, interestdekking, [[financiele-ratios#-solvabiliteitsratio-s\|schuldgraad]], vrije [[kasstroomanalyse\|kasstroom]] |
| Liquiditeitsdiagnose | [[financiele-ratios#-liquiditeitsratio-s\|Current ratio, quick ratio]], nettowerkkapitaal, debiteurendagen, crediteurendagen |
| Winstgevendheidsoordeel | [[financiele-ratios#-rentabiliteitsratio-s\|ROE, ROA, nettomarge, brutomarge]] |
| Brede diagnose | [[financiele-ratios\|Ratio's uit alle categorieën]] + [[kasstroomanalyse\|kasstroomanalyse]] |


> [!tip]- Bij een brede diagnose
> Begin met één ratio per categorie (liquiditeit, solvabiliteit, rentabiliteit, activiteit) om een globaal beeld te krijgen. Verdiep daarna waar de signalen het zwakst zijn.

### 4. 🔢 Bereken de ratio's en kasstromen

> 📥 **Nodig**:
> - Geselecteerde ratio's uit stap 3
> - Hergestructureerde cijfers uit stap 2
>
> 📤 **Uitkomst**:
> - Berekende waarden per geselecteerde ratio

Pas de [[financiele-ratios|formules per ratio]] (en [[kasstroomanalyse|indirecte methode kasstroom]]) toe op de hergestructureerde cijfers uit stap 2.


### 5. 📊 Uitkomsten interpreteren

> 📥 **Nodig**:
> - Berekende ratiowaarden uit stap 4
> - Sectorgemiddelden of benchmarks (NBB Balanscentrale of vuistregels)
>
> 📤 **Uitkomst**:
> - Interpretatie per ratio-categorie met benchmarkreferentie of trendduiding

Dit is de diagnose. Een getal zonder referentiepunt zegt niets. Vergelijk langs drie assen:

**Benchmark**: vergelijk met sectorgemiddelden of vuistregels. Dezelfde ratio kan normaal zijn in één sector en alarmerend in een andere. [[financiele-ratios#-benchmarks-per-sector]]

**Trend**: één jaar is een momentopname. Vergelijk met vorige jaren — verslechtert of verbetert de positie?

**Interne samenhang**: ratio's spreken elkaar soms tegen — dat is zelf informatie.

Typische spanningsvelden die om interpretatie vragen:

| Patroon | Mogelijke verklaring |
|---|---|
| Goede rentabiliteit + slechte liquiditeit | Groei zonder voldoende cashfinanciering (overtrading) |
| Hoge solvabiliteit + lage rentabiliteit | Onderbenutting van vreemd vermogen als hefboom |
| Stijgende voorraden + dalende liquiditeit | Mogelijke afzetproblemen of overkoop |
| Hoge brutomarge + lage nettomarge | Hoge overheadkosten of financieringslasten |


> [!warning]- Eén ratio als afdoend beschouwen
> ❌ *"De current ratio is goed, dus de liquiditeit is in orde."*
>
> Geen enkele ratio geeft een volledig beeld. Een goede current ratio met stijgende voorraden en dalende kasstroom kan nog steeds een liquiditeitsrisico verbergen.
>
> 🤖 *AI-aanvulling*

> [!warning]- Éénmalige effecten niet herkennen
> ❌ *"De rentabiliteit daalde sterk — de onderneming presteert slecht."*
>
> Een uitzonderlijke afschrijving, desinvestering of eenmalige kost vertekent de ratio's van dat jaar. Herken wanneer een afwijking structureel is versus toevallig — en vermeld dit in het oordeel.
>
> 🤖 *AI-aanvulling*

### 6. 💬 Oordeel formuleren

> 📥 **Nodig**:
> - Interpretaties per dimensie uit stap 5
>
> 📤 **Uitkomst**:
> - Gemotiveerd oordeel per dimensie + overkoepelende conclusie + aanbevelingen

Synthese van alle bevindingen. Een volledig oordeel:
- Beoordeelt elke dimensie afzonderlijk (sterk / zwak / gemengd)
- Noemt de twee of drie meest bepalende signalen
- Formuleert een overkoepelende conclusie over de financiële gezondheid
- Sluit af met concrete aanbevelingen of aandachtspunten

Formuleer met gepaste voorzichtigheid: een jaarrekening is historische data en geeft geen kwalitatieve informatie over management, markt of strategie.


## Voorbeelden

> [!example]- Integrale financiële beoordeling: alle stappen doorlopen
>
> **Situatie**: een handelsbv vraagt haar accountant om een brede financiële diagnose. Gegevens (in €):
>
> ```
> BALANS (analytisch herwerkt)
> ─────────────────────────────────────────   ──────────────────────────────────────
> Vaste activa          1.500.000             Eigen vermogen           800.000
> Voorraden               400.000             Schulden LT              600.000
> Handelsvorderingen      350.000             Schulden KT              900.000
> Liquide middelen         50.000
> ─────────────────────────────────────────   ──────────────────────────────────────
> Totaal activa         2.300.000             Totaal passief         2.300.000
>
> RESULTATENREKENING (selectie)
> ─────────────────────────────────────────
> Netto-omzet                  3.600.000
> Toegevoegde waarde (TAW)     1.260.000   (35% omzet)
> EBIT                           420.000   (11,7% omzet)
> Financiële kosten               70.000
> EBT                            350.000
> Nettowinst                     262.500
> Afschrijvingen                 180.000
> EBITDA                         600.000   (16,7% omzet)
> ```
>
> **Stap 1 — Analysedoel**: brede financiële diagnose (kredietwaardigheid + winstgevendheid + liquiditeit).
>
> **Stap 2 — Herstructurering**: al gedaan (zie balans analytisch formaat hierboven).
>
> **Stap 3–4 — Ratio's berekenen**:
>
> | Ratio | Berekening | Waarde |
> |---|---|---|
> | **NBK** | (400+350+50) − 900 | **−100.000** ⚠️ |
> | **WKB** | 400 + 350 − leveranciersschuld* | ⚠️ te verifiëren* |
> | **Current ratio** | 800 / 900 | **0,89** ⚠️ |
> | **Quick ratio** | (800−400) / 900 | **0,44** ⚠️ |
> | **Solvabiliteitsratio** | 800 / 2.300 | **34,8%** |
> | **Dekking fin. schulden** | (600) / 600* | zie toelichting* |
> | **Brutoverkoopmarge** | 1.260.000 / 3.600.000 | **35,0%** |
> | **ROE** | 262.500 / 800.000 | **32,8%** |
> | **ROA** | (350.000 + 70.000) / 2.300.000 | **18,3%** |
>
> **Stap 5 — Interpretatie per dimensie**:
>
> - **Liquiditeit — zwak**: current ratio 0,89 (< 1) en quick ratio 0,44 (heel laag). NBK is negatief (−€ 100.000). De onderneming kan haar kortlopende schulden niet dekken vanuit haar vlottende activa. Zonder voorraadomzetting is de situatie kritisch.
> - **Solvabiliteit — matig**: 34,8% eigen vermogen is voor een handelsbedrijf aan de lage kant (sectorgemiddelde handelsondernemingen ≈ 40–50% ⚠️ te verifiëren). De schuldenlast is draagbaar gezien de EBITDA van € 600.000 tegenover de LT-schuld van € 600.000.
> - **Rentabiliteit — sterk**: ROE van 32,8% is hoog; ROA van 18,3% is solide. De operationele winstgevendheid is gezond — het probleem zit niet in de winst maar in de liquiditeit.
>
> **Patroon**: hoge rentabiliteit + slechte liquiditeit → klassiek "overtrading"-profiel: de onderneming groeit of presteert goed maar heeft haar werkkapitaal onvoldoende gefinancierd. De winst wordt niet omgezet in kasreserves.
>
> **Stap 6 — Oordeel en aanbevelingen**:
>
> **Conclusie**: financieel gezond qua rentabiliteit en solvabiliteit, maar structureel kwetsbaar op liquiditeit. De vennootschap is winstgevend maar kan op korte termijn in betalingsmoeilijkheden komen als de voorraadomzetting vertraagt of klanten trager betalen.
>
> **Aanbevelingen**:
> 1. Kortlopende lening herfinancieren als langetermijnschuld → NBK stijgt (schulden KT dalen)
> 2. Debiteurendagen verkorten via strikter incassobeleid
> 3. Voorraadbeheer doorlichten: zijn er trage of verouderde voorraden die de liquiditeit blokkeren?
>
> **Grondslag**: analytische beroepspraktijk 🤖; sectorgemiddelden NBB ⚠️ te verifiëren via Balanscentrale
>
> 🤖 *AI-aanvulling*

> [!example]- Liquiditeitsdiagnose van een productiebedrijf
>
> **Situatie**: een kleine productiebv toont current ratio 0,75, quick ratio 0,40, stijgende voorraden ten opzichte van vorig jaar, en een negatieve vrije kasstroom.
>
> **Conclusie**: de liquiditeitspositie is zwak en verslechtert. De vennootschap is sterk afhankelijk van voorraadomzetting voor haar kortetermijnbetalingen.
>
> **Grondslag**: benchmarkwaarden voor productiebedrijven (current ratio ≥ 1,5 als vuistregel); intern consistente signalen (current ratio én quick ratio laag, negatieve kasstroom, stijgende voorraden).
>
> **Redenering**: current ratio < 1 → vlottende activa dekken kortlopende schulden niet. Quick ratio van 0,40 → zonder voorraden nog zorgwekkender. Stijgende voorraden bij dalende kasstroom → mogelijk afzetproblemen. Alle signalen wijzen in dezelfde richting → structureel, niet toevallig. Aanbeveling: werkkapitaalbeheer doorlichten, debiteurendagen en crediteurendagen vergelijken.
>
> 🤖 *AI-aanvulling*

## Motiveren op het examen

**Een volledig antwoord bevat:**
1. Expliciet analysedoel + motivering van de gekozen ratio's
2. Berekeningen op de hergestructureerde cijfers (niet de wettelijke posten)
3. Interpretatie per dimensie met benchmarkreferentie of trendvergelijking
4. Concreet oordeel per dimensie én overkoepelende conclusie
5. Bij conflicterende signalen: expliciete afweging

Bij een analytische competentie is de "grondslag" geen wetsartikel maar een benchmark, een patroon of een redenering. Vermeld dan expliciet waarop je je baseert: "op basis van de sectorgemiddelden..." / "gezien de interne samenhang van..."

**Typische vraagvormen**

> [!question]- Beoordeel de liquiditeitspositie
>
> Een handelsbedrijf heeft een current ratio van 1,1 en een quick ratio van 0,3. De voorraden zijn het afgelopen jaar met 40% gestegen. Beoordeel de liquiditeitspositie en formuleer een aanbeveling.
>
> > [!success]- Antwoord
> >
> > **Zwak, ondanks de current ratio boven 1.**
> >
> > De current ratio van 1,1 lijkt aanvaardbaar, maar de quick ratio van 0,3 toont dat bijna alle vlottende activa uit voorraden bestaan. Die voorraden zijn bovendien sterk gestegen (+40%), wat wijst op mogelijke afzetproblemen of overkoop. Zonder vlotte voorraadomzetting dreigt een liquiditeitscrisis. Aanbeveling: controleer de ouderdom van de voorraden en vergelijk de debiteurendagen met de crediteurendagen om de werkkapitaalbehoefte in kaart te brengen.
>
> 🤖 *AI-aanvulling*
