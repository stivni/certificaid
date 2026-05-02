---
tags: ["2.2", wip, competentie]
niveau: integratie
status: draft
programmaonderdelen: ["2.2"]
itaa-lex-secties:
  - II (WIB92 art. 126-178)
  - II (KB/WIB92 — uitvoering)
procedure-grondslag: "Wettelijk berekeningsschema (WIB92 art. 126-178); de stappen volgen de structuur van de wet maar de uitvoeringsmethode (handmatig of via Tax-on-web) is beroepspraktijk."
bouwversie: 2
---

# Belastingberekening personenbelasting uitvoeren

Deze competentie zet een **volledig ingevulde aangifte** om in een **te betalen of te ontvangen bedrag**. In de praktijk doet Tax-on-web dit automatisch, maar de mandataris moet **kunnen reproduceren waarom** een berekening de gegeven uitkomst geeft — om afwijkende resultaten te diagnosticeren, fouten op te sporen, en de cliënt te adviseren over optimalisaties die de berekening beïnvloeden (bv. globalisatie van roerende inkomsten, keuze huwelijksquotiënt, verhuis tussen gemeenten).

Onderscheid met aangrenzende competenties:
- **[[aangifte-personenbelasting-invullen|Aangifte invullen]]**: invoeren van de gegevens; deze competentie kan niet starten zonder een ingevulde aangifte
- **[[fiscaal-advies-personenbelasting-formuleren|Fiscaal advies]]**: vooraf — adviseren welke keuzes te maken; deze competentie voert de berekening uit
- **[[fiscale-optimalisatie-personenbelasting-beoordelen|Optimalisatie]]**: vergelijkt scenario's via deze berekening

> [!info]- Grondslag van deze werkwijze (🤖 30% · ⚖️ 70%)
> De berekeningsstappen zelf zijn **wettelijk** vastgelegd in [[bronnen/wetteksten/II-wib92|WIB92 art. 126-178]] en het [[bronnen/wetteksten/II-KB-wib92|KB/WIB92]]. De **uitvoeringsmethode** (handmatige berekening, gebruik van Tax-on-web simulator, vergelijking globalisatie/bevrijdend) is geen genormeerde procedure maar gangbare beroepspraktijk.

## Aanbevolen werkwijze

### 1. 🎯 Belastbaar inkomen vaststellen

> 📥 **Nodig**:
> - Volledig ingevulde [[aangifte-personenbelasting-invullen|aangifte personenbelasting]]
>
> 📤 **Uitkomst**:
> - Belastbaar inkomen, opgesplitst in **gezamenlijk belastbaar** (progressieve tarieven) en **afzonderlijk belastbaar** (vast tarief)
> - Voor partners: per persoon afzonderlijk berekend (decumul)

**Waarom**: zonder duidelijke scheiding tussen progressief en afzonderlijk belastbare inkomsten wordt het verkeerde tarief toegepast — bv. een stopzettingsmeerwaarde aan progressieve tarieven i.p.v. 16,5% kan duizenden euro's verschil maken.

Bouw het belastbaar inkomen op volgens [[personenbelasting-basisbegrippen#-belastbaar-inkomen|basisbegrippen — belastbaar inkomen]]:

```
Bruto-inkomsten per categorie (OG, beroeps, roerend, divers)
−  Aftrekbare kosten en sociale bijdragen (per categorie)
=  Netto-inkomsten per categorie
+  Sommatie tot globaal inkomen
−  Aftrekbare uitgaven (onderhoudsuitkeringen)
=  Belastbaar inkomen — gesplitst gezamenlijk vs. afzonderlijk
```

> [!info]- Concreet: dividend bevrijdend vs. globaliseren
>
> Cliënt: gepensioneerd, € 25 000 pensioen + € 1 500 dividenden (RV ingehouden 30%). Beslissing om te globaliseren of niet:
> - **Bevrijdend**: gezamenlijk belastbaar = € 25 000 (lage marginale tarief 25%); dividenden niet meer belast
> - **Globaliseren**: gezamenlijk belastbaar = € 25 000 + € 667 (€ 1 500 − € 833 vrijstelling) = € 25 667 → marginale 25% × € 667 = € 167; min RV € 450 verrekenbaar = teruggave € 283
>
> Globalisatie levert € 283 voordeel — beslis dus voor globalisatie en pas dat aan in stap 1.
>
> 🤖 *AI-aanvulling*

---

### 2. 🔢 Federale basisbelasting berekenen

> 📥 **Nodig**:
> - [[#-1--belastbaar-inkomen-vaststellen|Gezamenlijk belastbaar inkomen]] (per persoon)
> - Tarievenschijven (cijferzakboekje aj. 2026)
>
> 📤 **Uitkomst**:
> - Federale basisbelasting per persoon — vóór belastingvrije som en verminderingen

**Waarom**: het is de fundamentele basisberekening waarop alle latere verminderingen werken. Wie de schijfberekening niet correct uitvoert, krijgt elke volgende stap fout.

Pas het [[belastingberekening-personenbelasting#-tarieven-en-belastingberekening|progressieve tariefschema]] toe per schijf:

```
Schijf            Tarief    Belasting
€ 0 – € 15 820     25%      0,25 × min(I, 15 820)
€ 15 820 – € 27 920  40%    0,40 × max(0, min(I, 27 920) − 15 820)
€ 27 920 – € 48 320  45%    0,45 × max(0, min(I, 48 320) − 27 920)
> € 48 320         50%      0,50 × max(0, I − 48 320)

Federale basisbelasting = som van alle schijven
```

**Voor partners onder gezamenlijke aanslag**: deze stap wordt **per persoon afzonderlijk** uitgevoerd (decumul).

```
Voorbeeld: A (€ 50 000) en B (€ 18 000) gezamenlijk belast

Belastbaar A : € 50 000
   25% × € 15 820       =  € 3 955
 + 40% × € 12 100       =  € 4 840
 + 45% × € 20 400       =  € 9 180
 + 50% × € 1 680        =  €   840
                          ─────────
Federaal A              :  € 18 815

Belastbaar B : € 18 000
   25% × € 15 820       =  € 3 955
 + 40% × € 2 180        =  €   872
                          ─────────
Federaal B              :  € 4 827
```

---

### 3. 🔢 Belastingvrije som en gezinslast-toeslagen toepassen

> 📥 **Nodig**:
> - Federale basisbelasting per persoon (stap 2)
> - Gezinssituatie (uit aangifte): aantal personen ten laste, persoon met handicap, alleenstaande ouder
>
> 📤 **Uitkomst**:
> - Federaal verschuldigde belasting — vóór verminderingen

**Waarom**: de belastingvrije som is **niet-ondergeschikt** aan andere voordelen — ze is altijd van toepassing en ze wordt niet "vergeten". Elk vergeten kind ten laste = directe verlies van honderden tot duizenden euro's.

Bereken het **belastbaar bedrag** = basisbedrag belastingvrije som + alle toeslagen voor [[gezinsfiscaliteit#-personen-ten-laste|personen ten laste]]:

```
Basisbedrag (per persoon, cijferzakboekje aj. 2026)         : ~ € 10 570
+ Toeslag 1 kind ten laste                                   : + € 1 920
+ Toeslag 2 kinderen ten laste (cumulatief)                  : + € 3 030 extra
+ Toeslag 3 kinderen ten laste (cumulatief, niet-lineair)    : + € 6 140 extra
...

Belastbare som = basisbedrag + toeslagen
```

Bereken de **vermindering** = belastbare som × tarief van laagste schijven (begint bij 25%, schuift mee):

```
Vermindering = ∑ (belastbare som per schijf × tarief schijf)

Federaal verschuldigde belasting = Federale basisbelasting − Vermindering
```

> [!warning]- Bij gezamenlijke aanslag: belastingvrije som per persoon — niet één som
> ❌ *"Een echtpaar krijgt één belastingvrije som van € 10 570 voor het gezin."*
>
> Door [[personenbelasting-basisbegrippen#️-decumul|decumul]] krijgt **elke partner** zijn **eigen** belastingvrije som van ~ € 10 570 — er zijn dus twee belastingvrije sommen in een gezamenlijke aanslag. Toeslagen voor kinderen worden in beginsel toegerekend aan de partner met **het hoogste belastbare inkomen** (om maximaal voordeel te halen). Bij twijfel: simulator vergelijken voor toerekening aan partner A vs. partner B.
>
> 🤖 *AI-aanvulling*

---

### 4. 🔢 Federale belastingverminderingen aftrekken

> 📥 **Nodig**:
> - Federaal verschuldigde belasting (stap 3)
> - Federale verminderingsuitgaven uit aangifte (pensioensparen, giften, kinderoppas, …)
>
> 📤 **Uitkomst**:
> - Federaal te betalen belasting

**Waarom**: federale verminderingen zijn **non-refundable** — ze werken enkel als er voldoende belasting is. Bij lage inkomens of bij meerdere cumul-uitsluitingen (bv. kinderoppas vs. verhoogde toeslag) is de juiste volgorde van toepassing van belang voor de eindberekening.

Pas de federale verminderingen toe — zie [[belastingverminderingen-federaal|Federale belastingverminderingen]] voor tarieven:

```
Vermindering pensioensparen        : 30% × bestedingen (max plafond)
+ Vermindering langetermijnsparen   : 30% × bestedingen (max plafond)
+ Vermindering giften               : 45% × bestedingen erkende instellingen
+ Vermindering kinderoppas          : 45% × bestedingen erkende kinderopvang (max € 16,80/dag)
+ Vermindering vervangingsinkomsten : automatisch (formule)
+ Vermindering Tax Shelter          : 25-45% × inschrijvingen
+ ...

Federaal te betalen = Federaal verschuldigde belasting − ∑ federale verminderingen (≥ € 0)
```

**Begrenzing**: de verminderingen kunnen de federaal te betalen belasting niet onder nul brengen. Eventueel niet-gebruikt overschot van de federale vermindering gaat verloren (geen overdracht).

---

### 5. 🔢 Gewestelijke opcentiemen en verminderingen toepassen

> 📥 **Nodig**:
> - Federaal te betalen belasting (stap 4)
> - Gewest van fiscale woonplaats op 1 januari aanslagjaar
> - Gewestelijke verminderingsuitgaven uit aangifte

> 📤 **Uitkomst**:
> - Hoofdsom van de belasting (federaal + gewestelijk, vóór gemeentebelasting)

**Waarom**: sinds de zesde staatshervorming verschilt de fiscale druk fors per gewest — een Vlaams of Brussels of Waals dossier wordt verschillend behandeld.

Pas opeenvolgend toe (vereenvoudigd):

```
1. Federale verminderingsfactor toepassen op federaal te betalen belasting
   (vermindert de federale belasting met een vast %, eigen aan elk gewest)
2. Gewestelijke opcentiemen toepassen
   (vast %, gewestelijk vastgesteld — bv. ~ 33% in Vlaanderen)
3. Gewestelijke verminderingen aftrekken (woonbonus / Chèque habitat, dienstencheques, …)
```

Voor de exacte percentages per gewest: zie [[belastingberekening-personenbelasting#-gewestelijke-opcentiemen-en-verminderingen|Gewestelijke opcentiemen]] en [[belastingverminderingen-gewestelijk|Belastingverminderingen gewestelijk]].

```
Hoofdsom = (Federaal te betalen − federale verminderingsfactor) × (1 + gewestelijke opcentiem)
         − ∑ gewestelijke verminderingen
```

> [!info]- Concreet: dienstencheques in Vlaanderen
>
> Federaal te betalen na federale verminderingen: € 8 000.
> Vlaamse opcentiemen ~ 33% → tussenresultaat ~ € 10 640 (vereenvoudigd).
> Dienstencheques 2 × € 175 = € 350 vermindering.
> Hoofdsom = € 10 640 − € 350 = € 10 290.
>
> 🤖 *AI-aanvulling*

---

### 6. 🔢 Gemeentebelasting en bijzondere bijdrage toevoegen

> 📥 **Nodig**:
> - Hoofdsom van de belasting (stap 5)
> - Gemeentelijk opcentiem van de fiscale woonplaats
> - Bijzondere bijdrage sociale zekerheid (BBSZ) berekend op basis belastbaar inkomen

> 📤 **Uitkomst**:
> - Eindbelasting vóór verrekening van voorheffingen en VA

**Waarom**: het gemeentelijk opcentiem is een aanzienlijke component (typisch 6-9% van de hoofdsom). Verschillen tussen gemeenten (Knokke-Heist 0% vs. Antwerpen 8%) kunnen een belastingverschil van duizenden euro's per jaar maken.

```
Aanvullende gemeentebelasting = Hoofdsom × gemeentelijk opcentiem (%)
+ Eventuele agglomeratiebelasting (1% in Brussel)
+ Bijzondere bijdrage sociale zekerheid (BBSZ — formule per inkomenstrap)

Eindbelasting vóór verrekening = Hoofdsom + Gemeente + BBSZ
```

> [!warning]- Gemeente van fiscale woonplaats op 1 januari telt — niet de gemeente waar inkomen verdiend werd
> ❌ *"Ik werk in Antwerpen maar woon in Knokke-Heist — ik betaal Antwerpse gemeentebelasting (8%)."*
>
> De aanvullende gemeentebelasting wordt bepaald door **het gemeentelijk opcentiem van de fiscale woonplaats op 1 januari van het aanslagjaar** ([[bronnen/wetteksten/II-wib92|WIB92 art. 466]]) — niet door de werkplek of inkomstenbron. Wonen in Knokke-Heist op 1 januari → 0% aanvullende gemeentebelasting, ongeacht waar het loon verdiend wordt. Bij verhuis tijdens het inkomstenjaar telt de woonplaats op 1 januari van het volgend jaar (= aanslagjaar).
>
> 🤖 *AI-aanvulling*

---

### 7. 🔢 Voorheffingen en voorafbetalingen verrekenen

> 📥 **Nodig**:
> - Eindbelasting vóór verrekening (stap 6)
> - Bedrijfsvoorheffing reeds ingehouden (loonfiches 281.10/281.20)
> - Roerende voorheffing (indien geglobaliseerd)
> - Voorafbetalingen gestort

> 📤 **Uitkomst**:
> - Te betalen of te ontvangen saldo

**Waarom**: de verrekening is de laatste rekenkundige stap maar **kritisch** voor de cliëntcommunicatie — de cliënt wil weten **hoeveel** hij moet betalen of terugkrijgt, en **wanneer**.

```
Eindbelasting vóór verrekening                 : € X
−  Bedrijfsvoorheffing (volledig verrekenbaar) : € Y
−  Roerende voorheffing (bij globalisatie)     : € Z
−  Voorafbetalingen                            : € VA
+  Vermeerdering wegens onvoldoende VA         : € VermVA
−  Bonificatie wegens vroegtijdige VA          : € BonVA
                                               ─────────
TE BETALEN of TE ONTVANGEN                     : € Saldo
```

**Vermeerdering en bonificatie**: zie [[voorafbetalingen-personenbelasting]] voor de exacte berekening.

```
Voorbeeld vereenvoudigd (zelfstandige):
Eindbelasting                              : € 18 000
−  BV                                      : € 0       (zelfstandige)
−  RV                                      : € 0       (geen geglobaliseerde RV)
−  VA1+VA2+VA3+VA4                         : € 16 000
+  Vermeerdering (vereenvoudigd)           : € 0       (VA dekt > 90% × belasting)
−  Bonificatie                             : € 0
                                            ─────────
TE BETALEN                                 : € 2 000
```

---

### 8. ✅ Resultaat valideren tegenover voorgaande jaren

> 📥 **Nodig**:
> - Eindresultaat berekening (stap 7)
> - Aanslagbiljet vorig jaar
> - Bewuste wijzigingen in inkomsten / situatie

> 📤 **Uitkomst**:
> - Bevestiging dat berekening klopt of identificatie van afwijking met root cause

**Waarom**: een berekening die afwijkt van wat redelijk te verwachten is, signaleert een **fout in de aangifte** (vergeten code, verkeerde toewijzing) — niet noodzakelijk een fout in de berekening. De validatie tegenover voorgaande jaren is de laatste verdediging tegen een verkeerde aanslag.

**Vragen om te stellen**:
- Belasting fors hoger dan vorig jaar → welke nieuwe inkomstenbron, of welke vermindering verloren?
- Belasting fors lager dan vorig jaar → vergeten inkomsten? extra gewonnen vermindering?
- Sprong in marginale aanslagvoet → grensoverschrijding tariefschijf → cliënt informeren over impact

```
Vergelijkingstabel:
                       Vorig jaar     Dit jaar      Δ
Belastbaar inkomen     € 60 000       € 65 000     +€ 5 000
Federaal te betalen    € 18 800       € 21 050     +€ 2 250
Gewestelijke opcent.   € 5 850        € 6 530      +€ 680
Gemeentebelasting      € 1 980        € 2 200      +€ 220
                       ──────────     ──────────   ────────
Eindbelasting          € 26 630       € 29 780     +€ 3 150
```

> [!info]- Concreet: onverwacht hoge aanslag
>
> Vorig jaar: te ontvangen € 1 200. Dit jaar simulator: te betalen € 4 800 — vergelijkbaar inkomen (€ 60 000). Onderzoek wijst uit:
> 1. Werkelijke kosten gekozen voor de werknemer (i.p.v. forfait — fout) → € 2 000 verlies
> 2. Pensioensparen vergeten in te vullen → € 306 vermindering verloren
> 3. Dienstencheques niet ingevuld → € 175 vermindering verloren
> 4. Onderhoudsuitkering aan ex (€ 6 000) vergeten af te trekken → € 2 400 belasting bespaard
>
> Na correctie: te ontvangen € 1 100 — consistent met vorig jaar. Stap 8 redde de cliënt van € 5 900 verkeerde belasting.
>
> 🤖 *AI-aanvulling*

---

## Voorbeelden

> [!example]- Werknemer met partner zonder inkomen — huwelijksquotiënt
>
> **Situatie**: Gehuwd koppel, A werkt voltijds (€ 70 000 brutoloon), B is huisvrouw zonder eigen inkomen, 2 kinderen ten laste (Vlaanderen, gemeente Antwerpen 8% opcentiem).
>
> **Conclusie**: Eindbelasting ~ € 17 800 — te ontvangen ~ € 1 200 (na BV ingehouden ~ € 19 000).
>
> **Grondslag**: [[bronnen/wetteksten/II-wib92|WIB92 art. 87 (huwelijksquotiënt), art. 130 (tarieven), art. 132 (gezinslast), art. 466 (gemeentebelasting)]]
>
> **Redenering**:
> - Stap 1: Belastbaar A € 65 000 (na sociale bijdragen en forfait); B € 0
> - Stap 2: Toepassing huwelijksquotiënt → overheveling € 13 050 van A naar B → A belast op € 51 950, B op € 13 050
> - Stap 3: Federale basisbelasting A ~ € 18 815, B ~ € 3 263. Belastingvrije som per persoon + toeslag 2 kinderen aan A
> - Stap 4: Geen federale verminderingen
> - Stap 5: Gewestelijke opcentiemen Vlaanderen
> - Stap 6: Gemeentebelasting Antwerpen 8%
> - Stap 7: BV ingehouden door werkgever ~ € 19 000 → te ontvangen ~ € 1 200
> - Stap 8: Consistent met vorig jaar (kleine teruggave)
>
> 🤖 *AI-aanvulling*

> [!example]- Bedrijfsleider met gemengde inkomsten
>
> **Situatie**: Alleenstaande zaakvoerder van een bv. Bezoldiging € 80 000, dividend € 15 000 (RV 30% ingehouden — keuze niet globaliseren), 1 huurpand verhuurd aan derde voor beroepsgebruik (huur € 18 000, KI € 1 200, geïndexeerd KI × 5/3 × revalorisatie = € 10 920 als maximum onroerend inkomen). Wallonië, gemeente Marche-en-Famenne 8,5% opcentiem.
>
> **Conclusie**: Eindbelasting ~ € 35 200 — VA's van € 30 000 → te betalen ~ € 5 200.
>
> **Grondslag**: [[bronnen/wetteksten/II-wib92|WIB92 art. 30 (bezoldiging), art. 7 (OG), art. 17 (RV), art. 130, art. 466]]
>
> **Redenering**:
> - Stap 1: Belastbaar = € 80 000 (bezoldiging na sociale bijdragen en forfait 3% bedrijfsleider) + onroerend inkomen werkelijke nettohuur ~ € 10 800 = € 90 800. Dividend bevrijdend → niet in belastbaar.
> - Stap 2: Federale basisbelasting tariefschema → ~ € 35 215
> - Stap 3: Belastingvrije som alleenstaande → vermindering ~ € 2 643
> - Stap 4: Geen federale verminderingen
> - Stap 5: Wallonië opcentiemen + geen gewestelijke verminderingen
> - Stap 6: Marche-en-Famenne 8,5%
> - Stap 7: VA's € 30 000 (gespreid 4 × € 7 500) — geen vermeerdering. Te betalen € 5 200.
> - Stap 8: Belasting hoger dan vorig jaar door verhoogde bezoldiging — consistent.
>
> 🤖 *AI-aanvulling*

## Motiveren op het examen

**Een volledig antwoord bevat:**
1. Belastbaar inkomen opgesplitst (gezamenlijk + afzonderlijk)
2. Federale basisbelasting — schijfberekening
3. Belastingvrije som + toeslagen → federaal verschuldigd
4. Federale verminderingen → federaal te betalen
5. Gewestelijke opcentiemen + verminderingen → hoofdsom
6. Gemeentebelasting + BBSZ → eindbelasting
7. Verrekening BV / RV / VA → te betalen of te ontvangen
8. Validatie tegenover vorig jaar

### Voorbeeldvragen

> [!question]- Marginale vs. gemiddelde aanslagvoet
>
> Een belastingplichtige met belastbaar inkomen € 100 000. Hoeveel is zijn marginale aanslagvoet? En zijn gemiddelde federale aanslagvoet?
>
> > [!success]- Antwoord
> >
> > **Marginaal: 50%. Gemiddeld federaal: ~ 43%.**
> >
> > De marginale aanslagvoet is het tarief op de **laatste euro** = 50% (boven schijf € 48 320). De gemiddelde aanslagvoet = totale federale belasting / belastbaar inkomen. Berekening: € 3 955 (25% × € 15 820) + € 4 840 (40% × € 12 100) + € 9 180 (45% × € 20 400) + € 25 840 (50% × € 51 680) = € 43 815. Gemiddeld federaal: € 43 815 / € 100 000 = **43,8%**. Wie de marginale aanslagvoet (50%) als totale belasting presenteert, overschat met ~ € 6 000.
> >
> > *Zie: [[belastingberekening-personenbelasting#-tarieven-en-belastingberekening|Tarieven en belastingberekening]]*
>
> 🤖 *AI-aanvulling*

> [!question]- Globalisatie wel of niet
>
> Een gepensioneerde (€ 22 000 pensioen, marginale schijf 25%) ontvangt € 2 000 dividenden van zijn bv (RV 30% = € 600 ingehouden). Globaliseren of bevrijdend laten?
>
> > [!success]- Antwoord
> >
> > **Globaliseren — levert teruggave op.**
> >
> > **Bevrijdend**: niets aangeven, RV € 600 = totale belasting op dividend (effectief 30%).
> >
> > **Globaliseren**: aangeven in vak VII bruto € 2 000. Vrijstelling eerste schijf ~ € 833 → belastbaar € 1 167 × 25% (marginale) = € 292. Min RV verrekenbaar € 600. Saldo: **€ 308 te ontvangen**.
> >
> > Voordeel globalisatie: € 308. Algemene regel: voor lage marginale tarieven (< 30%) en/of bij gebruik van vrijstelling eerste schijf — globaliseren is voordeliger.
> >
> > *Zie: [[roerende-inkomsten-personenbelasting#-wanneer-globaliseren|Wanneer globaliseren?]] en [[belastingberekening-personenbelasting#️-bedrijfsvoorheffing-en-roerende-voorheffing-verrekening|RV-verrekening]]*
>
> 🤖 *AI-aanvulling*

> [!question]- Verhuis naar gemeente zonder opcentiem
>
> Een belastingplichtige met geraamde belasting hoofdsom € 25 000 verhuist op 15 december 2025 van Antwerpen (8% opcentiem) naar Knokke-Heist (0%). Wat is het effect op zijn aj. 2026 aanvullende gemeentebelasting?
>
> > [!success]- Antwoord
> >
> > **Aanvullende gemeentebelasting = 0 — besparing € 2 000.**
> >
> > Aanvullende gemeentebelasting wordt bepaald door de gemeente van fiscale woonplaats **op 1 januari van het aanslagjaar**. Op 1 januari 2026 woont hij in Knokke-Heist (0% opcentiem) → aanvullende gemeentebelasting = 0% × € 25 000 = **€ 0**. In Antwerpen zou dat € 25 000 × 8% = € 2 000 geweest zijn. Verhuis 2 weken vóór 1 januari = € 2 000 fiscaal voordeel — een aanzienlijk argument bij verhuis-overwegingen voor hoge inkomens.
> >
> > *Zie: [[belastingberekening-personenbelasting#-gemeentelijke-en-agglomeratiebelasting|Gemeentebelasting]]*
>
> 🤖 *AI-aanvulling*
