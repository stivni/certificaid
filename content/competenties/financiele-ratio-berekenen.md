---
tags: ["1.3", wip, competentie]
niveau: toepassen
status: draft
programmaonderdelen: ["1.3"]
itaa-lex-secties:
  - XIII KB 21/10/2018 (MAR — genormaliseerde rekeningcodes)
  - XV (WVV schema-vereisten volledig/verkort/micro)
---

# Financiële ratio berekenen

Gegeven een balans en resultatenrekening — en eventuele toelichting — de correcte waarde berekenen voor een gevraagde financiële ratio, inclusief het identificeren van de juiste brongegevens en het toepassen van de noodzakelijke correcties.

## Aanbevolen werkwijze

### 1. 🔍 Ratio en formule identificeren

> 📥 **Nodig**:
> - De taakomschrijving of examenopdracht met de naam van de gevraagde ratio

> 📤 **Uitkomst**:
> - Formule met teller en noemer (in woorden en NBB-codes)

Sla dit eerste nooit over. Dezelfde term kan op meerdere manieren gedefinieerd zijn — het examen gebruikt soms "nettorentabiliteit van de activa" en soms "nettorentabiliteit van het totaal der activa vóór belastingen en financiële kosten". Die zijn niet identiek.

Voorbeelden van hoe ratio-namen eruitzien en wat de formule is:
- Liquiditeit in ruime zin = vlottende activa (`29/58`) / schulden KT (`42/48`)
- Nettorentabiliteit totaal der activa = (resultaat vóór belastingen + fin. kosten − intrestsubsidies) / totaal activa × 100
- Brutoverkoopmarge = toegevoegde waarde (`9900`) / netto-omzet (`70`) × 100

Volledige formules per ratio met NBB-codes: [[financiele-ratios]]

> [!warning]- Naam van de ratio verwisselen met een gelijkaardige
> ❌ *"Nettorentabiliteit van de activa en ROE zijn allebei een rentabiliteitsratio — ik gebruik dezelfde formule."*
>
> ROA meet rendement op het totale vermogen (teller: EBIT of EBIT + fin. kosten − intrestsubsidies; noemer: totaal activa). ROE meet rendement voor de aandeelhouder (teller: nettowinst; noemer: eigen vermogen vóór winstverdeling). Ze meten een ander aspect van rentabiliteit en zijn niet uitwisselbaar.
>
> 📝 *Terugkerende valkuil in voorbeeldexamens 2013–2015*

---

### 2. 🔀 Schema-beschikbaarheid controleren

> 📥 **Nodig**:
> - Schema-type: volledig, verkort of micro (staat doorgaans vermeld in de opdracht)
> - Formule uit stap 1

> 📤 **Uitkomst**:
> - Bevestiging dat de ratio berekenbaar is, of een expliciete melding dat de vereiste gegevens ontbreken

Sommige ratio's vereisen detailgegevens die niet beschikbaar zijn in het verkort of microschema. Als de gevraagde ratio niet berekenbaar is, zeg dat dan expliciet — het examen toetst soms net dit inzicht.

Zie [[financiele-ratios#-schema-beperkingen|Schema-beperkingen]] voor het overzicht per ratio.

> [!warning]- N-dagen klantenkrediet berekenen op een verkort schema
> ❌ *"Ik bereken de klantenbetalingstermijn op basis van de beschikbare vorderingspost."*
>
> In het verkort schema zijn handelsvorderingen niet apart opgegeven — ze zijn samengevoegd met andere vorderingen. De ratio "n-dagen klantenkrediet" is daardoor **niet berekenbaar** op basis van een verkort schema. De correcte respons is dit expliciet te vermelden.
>
> 📝 *Voorbeeldexamen 2024: "welke ratio kan je niet berekenen op basis van een verkort schema → n-dagen klantenkrediet"*

---

### 3. 🔍 Toelichting lezen op correcties

> 📥 **Nodig**:
> - Toelichting bij de jaarrekening (meegeleverd in de opdracht)
> - Formule uit stap 1

> 📤 **Uitkomst**:
> - Lijst van correcties (bedragen en hun effect op teller of noemer), of bevestiging dat geen correcties nodig zijn

Het examen bevat soms extra informatie in de toelichting die de berekening beïnvloedt. Lees de volledige toelichting vóór je berekent. Typische correcties:

| Correctie | Effect | Typische toelichting |
|---|---|---|
| Exploitatiesubsidies | Verhogen toegevoegde waarde maar zijn geen omzet | "Er werden exploitatiesubsidies aangerekend voor X EUR" |
| Intrestsubsidies | Worden afgetrokken bij ROA | "De vennootschap ontving intrestsubsidies van X EUR" |
| Gemiddeld aantal VTE | Noemer bij productiviteitsratio's | "Het gemiddeld aantal werknemers bedraagt X VTE" |
| Gemiddelde voorraad | Noemer bij voorraadrotatie | "Openingsvoorraad X, sluitingsvoorraad Y" |
| Btw-factor | Noemer n-dagen klantenkrediet | "Omzet excl. btw is X; toepasselijk btw-tarief 21%" |

> [!warning]- Toelichting niet lezen vóór de berekening
> ❌ *"De formule is duidelijk — ik gebruik de getallen rechtstreeks uit de balans en resultatenrekening."*
>
> Exploitatiesubsidies (rubriek 740) staan in de resultatenrekening maar wijzigen de teller van de brutoverkoopmarge alleen als ze in de toegevoegde waarde zijn opgenomen. Intrestsubsidies moeten bij ROA in mindering worden gebracht. Deze informatie staat altijd expliciet in de toelichting — wie ze overslaat, berekent de ratio op foute gegevens.
>
> 📝 *Terugkerende valkuil in voorbeeldexamens 2013–2015*

---

### 4. 🔢 Extraheer de juiste getallen uit de jaarrekening

> 📥 **Nodig**:
> - Hergestructureerde of wettelijke jaarrekening
> - Formule met NBB-codes uit stap 1
> - Correcties uit stap 3

> 📤 **Uitkomst**:
> - Waarden voor teller en noemer, inclusief de gebruikte posten

Gebruik de NBB-codes als zoekinstrument in de jaarrekening. Let op rubrieken die meerdere sub-codes bundelen (bv. schulden KT = 42/48).

**Bij ROE**: gebruik het eigen vermogen **vóór** winstverdeling (= beginbalans van het boekjaar, of eindbalans minus de gereserveerde winst van dat jaar). Het eigen vermogen ná winstverdeling bevat al de winst die gemeten wordt — dat geeft een kunstmatig lage ratio.

**Bij voorraadrotatie**: gebruik de **gemiddelde voorraad** ((openingsvoorraad + sluitingsvoorraad) / 2), niet de eindvoorraad. De eindvoorraad is een momentopname die gevoelig is voor seizoenseffecten.

> [!warning]- EV ná winstverdeling gebruiken bij ROE
> ❌ *"Ik gebruik het eigen vermogen na winstverdeling — dat is het meest actuele cijfer."*
>
> ROE meet het rendement op het vermogen dat bij het begin van het boekjaar werd ingezet. Als de winst al aan het eigen vermogen is toegevoegd (winstverdeling), gebruik je als noemer een bedrag dat de te meten winst al bevat — wat de ratio verlaagt zonder dat de onderneming minder presteert. Gebruik altijd het EV vóór winstverdeling.
>
> 📝 *Voorbeeldexamen 2015: EV vóór winstverdeling = € 8.177.941 (niet € 10.274.000 na winstverdeling)*

> [!warning]- Eindvoorraad vs. gemiddelde voorraad bij rotatie
> ❌ *"Ik gebruik de eindvoorraad als noemer — dat zijn de meest recente gegevens."*
>
> De eindvoorraad is een momentopname. De gemiddelde voorraad geeft een representatiever beeld van de voorraad die gedurende het jaar aangehouden werd. Gebruik (openingsvoorraad + sluitingsvoorraad) / 2 als noemer.
>
> 📝 *Voorbeeldexamen 2015: antwoorden A en B gebruiken eindvoorraad en geven te hoge rotatie; correct antwoord C gebruikt gemiddelde voorraad*

---

### 5. 🔢 Voer de berekening uit

> 📥 **Nodig**:
> - Teller en noemer uit stap 4
> - Eenheid (getal, percentage, of dagen)

> 📤 **Uitkomst**:
> - Berekende waarde, afgerond op 2 decimalen tenzij anders gevraagd

Schrijf de volledige berekening uit, inclusief de gebruikte getallen. Het examen vraagt dit expliciet: "motiveer met de gebruikte cijfers". Een antwoord dat alleen de uitkomst vermeldt zonder de teller en noemer te tonen, is onvolledig.

**Eenheden**:
- Ratio's (current ratio, schuldgraad, ...): decimaal getal (bv. 1,47)
- Percentages (ROE, brutoverkoopmarge, ...): afronden op 2 decimalen + % (bv. 11,85%)
- Dagen (klantenbetalingstermijn, rotatie in dagen): geheel getal of 2 decimalen (bv. 42,35 dagen)

> [!tip]- Tussenresultaten noteren
> Schrijf bij samengestelde ratio's de tussenresultaten afzonderlijk op. Bv. bij ROA: bereken eerst het teller (resultaat vóór belastingen + financiële kosten − intrestsubsidies) en de noemer (totaal activa) apart — en schrijf beide waarden op vóór je deelt. Zo kun je bij een rekenfout snel zien waar het mis gaat, en toont de corrector dat je de juiste methode gevolgd hebt.

---

## Voorbeelden

> [!example]- Nettorentabiliteit activa (ROA) met intrestsubsidie
>
> **Situatie**: resultaat vóór belastingen = € 877.279; financiële kosten = € 46.934; bedrijfsresultaat financiële activiteiten = € 211.950; intrestsubsidies = € 6.000; totaal activa = € 9.081.054.
>
> **Conclusie**: ROA = 12,45%
>
> **Grondslag**: [[financiele-ratios#-rentabiliteitsratio-s|ROA-formule]] — Resultaat vóór belastingen + financiële kosten − intrestsubsidies / totaal activa × 100
>
> **Redenering**: (877.279 + 46.934 + 211.950 − 6.000) / 9.081.054 × 100 = 1.130.163 / 9.081.054 × 100 = **12,45%**. De intrestsubsidie van € 6.000 wordt afgetrokken omdat ze de werkelijke financiële kost verlaagt — zonder aftrek zou de ROA kunstmatig hoog zijn.
>
> 📝 *Uit voorbeeldexamen 2014*

> [!example]- Bruto toegevoegde waarde per werknemer
>
> **Situatie**: netto-omzet = € 7.441.663; handelsgoederen en diensten = € 3.185.295; verbruikte grondstoffen = € 1.192.317; gemiddeld aantal VTE = 38,20.
>
> **Conclusie**: bruto TAW per werknemer = € 80.210,76
>
> **Grondslag**: [[financiele-ratios#-activiteitsratio-s-en-kengetallen|TAW per werknemer]] = Toegevoegde waarde / Aantal VTE
>
> **Redenering**: Toegevoegde waarde = 7.441.663 − 3.185.295 − 1.192.317 = 3.064.051; per werknemer = 3.064.051 / 38,20 = **€ 80.210,76**. Het gemiddeld aantal VTE staat in de toelichting of sociale balans.
>
> 📝 *Uit voorbeeldexamen 2014*

---

## Motiveren op het examen

**Een volledig antwoord bevat:**
1. De formule in woorden (teller / noemer)
2. De gebruikte cijfers naast de formule (expliciete koppeling)
3. Eventuele correcties op basis van de toelichting, met vermelding van het bedrag
4. De berekende waarde met eenheid

**Typische vraagvormen**

> [!question]- Brutoverkoopmarge met subsidiekorting
>
> Een vennootschap heeft in het boekjaar: netto-omzet € 5.000.000; aankopen € 2.800.000; wijziging in voorraden gereed product +€ 200.000; diensten en diverse goederen € 400.000; exploitatiesubsidies € 120.000. De toegevoegde waarde (rubriek 9900) bedraagt € 2.120.000. Bereken de brutoverkoopmarge.
>
> > [!success]- Antwoord
> >
> > **Brutoverkoopmarge = 42,40%**
> >
> > Formule: toegevoegde waarde / netto-omzet × 100.
> > Teller: rubriek 9900 = € 2.120.000 (exploitatiesubsidies zijn reeds opgenomen in de toegevoegde waarde via rubriek 740).
> > Noemer: netto-omzet = € 5.000.000.
> > Berekening: 2.120.000 / 5.000.000 × 100 = **42,40%**.
> >
> > Aandachtspunt: of exploitatiesubsidies in de teller worden meegenomen, hangt af van hoe de toelichting dit specificeert. Als de examenopdracht vraagt om de brutoverkoopmarge *excl.* subsidies te berekenen, corrigeer je de teller: 2.120.000 − 120.000 = 2.000.000 → 40,00%.
> >
> > *Zie: [[financiele-ratios#-rentabiliteitsratio-s|Brutoverkoopmarge]]*
>
> 📝 *Terugkerend vraagtype voorbeeldexamens 2013–2015*

> [!question]- Liquiditeit in enge zin (quick ratio)
>
> Een onderneming (volledig schema) heeft: voorraden (rubriek 3) € 1.739.806; handelsvorderingen KT € 2.200.000; overige vorderingen KT € 2.548.415; liquide middelen € 2.704; leveranciersschulden (rubriek 44) € 1.210.536; kortlopende leningen (rubriek 43) € 39.932. Bereken de liquiditeit in enge zin.
>
> > [!success]- Antwoord
> >
> > **Quick ratio = 5,57**
> >
> > Formule: (vlottende activa − voorraden) / schulden KT.
> > Teller: (1.739.806 + 2.200.000 + 2.548.415 + 2.704) − 1.739.806 = **€ 5.011.119**
> > Noemer: 1.210.536 + 39.932 = **€ 1.250.468**
> > Berekening: 5.011.119 / 1.250.468 = **5,57** (afgerond op 2 decimalen)
> >
> > Let op: de noemer omvat twee aparte schuldenrubrieken (44 + 43). Een veelgemaakte fout is slechts één rubriek meenemen.
> >
> > *Zie: [[financiele-ratios#-liquiditeitsratio-s|Liquiditeitsratio's]]*
>
> 📝 *Uit voorbeeldexamen 2014*

> [!question]- Schema-beperking identificeren
>
> Een analist wil de n-dagen klantenbetalingstermijn berekenen op basis van de gepubliceerde jaarrekening van een kleine vennootschap die het verkort schema gebruikt. Is dit mogelijk?
>
> Juist of fout?
>
> > [!success]- Antwoord
> >
> > **Fout — de ratio is niet berekenbaar op basis van het verkort schema.**
> >
> > In het verkort schema worden handelsvorderingen niet apart gepubliceerd. Ze zijn samengevoegd in een bredere vorderingspost. De formule n-dagen klantenkrediet = handelsvorderingen / omzet incl. btw × 365 vereist de afzonderlijke post "handelsvorderingen KT" (rubriek 40), die in het verkort schema niet beschikbaar is.
> >
> > *Zie: [[financiele-ratios#-schema-beperkingen|Schema-beperkingen]]*
>
> 📝 *Uit voorbeeldexamen 2024*

---

## Relevant voor

**[[1.3-analyse-en-kritische-beoordeling-jaarrekening|1.3 Analyse en kritische beoordeling van de jaarrekening]]**

Taken:
- *Analyse en beoordeling van de financiële situatie aan de hand van de jaarrekeningen, ratio's en kengetallen*
  - In staat zijn om ratio's en kengetallen correct te berekenen

Kenniselementen:
- I.C.2 — Andere documenten: ratio's, financieringstabel, boordtabel
- II.C.4 — Ratio's en kengetallen berekenen
