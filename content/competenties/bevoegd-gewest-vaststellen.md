---
tags: ["2.7", wip, competentie]
niveau: integratie
status: draft
bouwversie: 2
programmaonderdelen: ["2.7"]
itaa-lex-secties:
  - IV.A (VCF) — Vlaamse codex
  - IV.B (Brusselse Codex Fiscale Procedure)
  - IV.C (Décret W.R. 6 mei 1999)
procedure-grondslag: "Bijzondere Financieringswet 16 januari 1989 + sectorale wetgeving (VCF, Wb. Reg., Wb. Succ., WIB92) — analytische uitwerking 🤖"
---

# Bevoegd gewest voor een gewestelijke belasting vaststellen

Bij elke transactie of situatie die een gewestelijke belasting kan triggeren (overlijden, verkoop onroerend goed, schenking, inschrijving voertuig, vestiging onderneming) moet eerst worden bepaald **welk gewest bevoegd is** om te heffen. De Bijzondere Financieringswet bepaalt **per belastingtype** een afzonderlijke **lokaliseringsfactor** — er is geen uniforme regel. Wie de verkeerde codex of het verkeerde tarief toepast, geeft fout advies en aangiftes vertrekken naar de verkeerde administratie.

Deze competentie is de eerste stap voor zowat elke gewestelijke fiscaalkundige tussenkomst — voor de eigenlijke belastingberekening of aangifte verwijst ze naar de specifieke materie- of taakcompetenties (bv. [[aangifte-nalatenschap-opmaken|aangifte nalatenschap]]).

> [!info]- Grondslag van deze werkwijze (🤖 70% · ⚖️ 30%)
> De **lokaliseringsfactoren per belasting** zijn bindend gecodificeerd in de [[bronnen/wetteksten/IVA-vcf|VCF]] (Vlaanderen), de Brusselse Codex Fiscale Procedure en federale wetten (Wb. Succ., Wb. Reg., WIB92 art. 249) — dat is het wettelijke deel. De **stappen om die factoren systematisch toe te passen** in een concreet dossier zijn analytische praktijk: wij hebben hier geen ITAA-norm of CBN-advies dat de procedure gecodificeerd vastlegt. De stappen volgen de redeneerlogica die elke fiscaal raadgever zou volgen.

## Aanbevolen werkwijze

### 1. 🎯 Doel en belastingtype identificeren

> 📥 **Nodig**:
> - Beschrijving van de transactie/situatie van de cliënt (overlijden, verkoop, inschrijving voertuig, schenking, …)
> - Vraagstelling cliënt (welk advies/welke aangifte)
>
> 📤 **Uitkomst**:
> - Lijst van mogelijk verschuldigde gewestelijke belastingen
> - Per belasting: het belastbaar feit en bijhorende lokaliseringsfactor

**Waarom**: zonder duidelijke identificatie van *welke* gewestelijke belasting in het geding is, kun je geen lokaliseringsfactor toepassen — de factor verschilt per belasting.

Per situatie kan **één** of **meerdere** gewestelijke belastingen verschuldigd zijn. Voorbeeld: een verkoop van een appartement triggert tegelijk verkooprecht (registratie) en heeft impact op de OV (eigenaar wijzigt op 1 januari volgende). Een verhuis triggert geen heffing maar wijzigt de aanvullende GB op de PB en de bevoegdheid voor de OV.

| Situatie | Mogelijke gewestelijke belastingen |
|---|---|
| **Overlijden rijksinwoner** | [[tarieven-erfbelasting\|Erfbelasting/successierechten]] |
| **Verkoop onroerend goed** | [[registratierecht-onroerend-goed\|Verkooprecht/registratierechten]] |
| **Schenking** | [[schenking-fiscaal\|Schenkbelasting/schenkingsrechten]] |
| **Inschrijving voertuig** | [[verkeersbelasting#-belasting-op-de-inverkeerstelling-biv\|BIV]] (eenmalig) + [[verkeersbelasting#-verkeersbelasting-vb\|VB]] (jaarlijks) |
| **Bezit onroerend goed op 1/1** | [[onroerende-voorheffing\|Onroerende voorheffing]] |
| **Verhuis tussen gewesten** | Wijzigt bevoegdheid voor VB (vanaf volgend AJ) en aanvullende GB op PB |

> [!info]- Concreet: verhuis van Brussel naar Antwerpen
>
> Een cliënt verhuist op 15 oktober 2025 van Brussel naar Antwerpen. Hij heeft (i) een appartement in Brussel, (ii) een wagen op zijn naam, en (iii) een tweedehandshuis dat hij in december 2025 aankoopt. Te identificeren belastingen:
> - **OV op het Brusselse appartement** (peildatum 1 jan): Brussel int voor AJ 2025 én AJ 2026 (eigenaar Brussels op 1/1/2026 nog steeds, want pand niet verkocht). De **woonplaats** speelt geen rol voor de OV — alleen de **ligging van het pand**.
> - **VB op de wagen**: Brussel int VB voor AJ 2025; Vlabel wordt bevoegd vanaf AJ 2026.
> - **Verkooprecht op het Antwerpse huis**: Vlaanderen — bepaald door **ligging van het onroerend goed**.
> - **Aanvullende GB op de PB**: Brusselse gemeente voor AJ 2025; Antwerpse gemeente voor AJ 2026 (bepaald door [[lokale-belastingen#aanvullende-gemeentebelasting-op-de-pb|woonplaats op 1 januari]]).
>
> 🤖 *AI-aanvulling*

### 2. 🔀 Lokaliseringsfactor opzoeken per belasting

> 📥 **Nodig**:
> - Lijst van mogelijk verschuldigde gewestelijke belastingen (uit stap 1)
>
> 📤 **Uitkomst**:
> - Per belasting: de wettelijk vastgelegde lokaliseringsfactor (woonplaats / ligging goed / zetel / inschrijvingsdatum)

**Waarom**: de federale wetgever heeft per belastingtype een verschillend **aanknopingspunt** vastgelegd. Een verkoper raden op basis van zijn woonplaats het verkooprecht te bepalen leidt tot foute conclusie — want het criterium is de ligging van het pand, niet de woonplaats van de verkoper. *(Grondslag: [[bronnen/wetteksten/IVA-vcf|VCF]] + Wb. Reg., Wb. Succ., WIB92 — verschilt per belasting)*

| Belasting | Lokaliseringsfactor | Bron |
|---|---|---|
| **OV** | Ligging van het onroerend goed | [[bronnen/wetteksten/IVA-vcf#art-21101\|VCF art. 2.1.1.0.1]]; WIB92 art. 249 |
| **Erfbelasting (rijksinwoner)** | **Fiscale woonplaats overledene** op datum overlijden — bij verhuis: het gewest waar overledene de **langste fiscale woonplaats** had in de **laatste 5 jaar** vóór overlijden | BFW art. 5 §2; [[bronnen/wetteksten/IVA-vcf#art-27101\|VCF art. 2.7.1.0.1]] (belastbaar feit); Wb. Succ. art. 1 |
| **Schenkbelasting (schenker rijksinwoner)** | **Fiscale woonplaats schenker** op datum schenking — bij verhuis: gewest waar schenker langst woonde in laatste 5 jaar | BFW art. 5 §2; [[bronnen/wetteksten/IVA-vcf#art-28101\|VCF art. 2.8.1.0.1]]; Wb. Reg. |
| **Verkooprecht / verdeelrecht** | **Ligging van het onroerend goed** | [[bronnen/wetteksten/IVA-vcf#art-29101\|VCF art. 2.9.1.0.1]]; Wb. Reg. |
| **Verkeersbelasting (natuurlijke persoon)** | **Fiscale woonplaats** op 1 januari aanslagjaar | [[bronnen/wetteksten/IVA-vcf#art-22101\|VCF art. 2.2.1.0.1]] |
| **Verkeersbelasting (rechtspersoon)** | **Statutaire zetel** | Idem |
| **BIV** | Bij inschrijving: woonplaats / zetel op datum inschrijving | [[bronnen/wetteksten/IVA-vcf#art-23101\|VCF art. 2.3.1.0.1]] |
| **Aanvullende GB op PB** | **Fiscale woonplaats op 1 januari** aanslagjaar | WIB92 art. 466 |

> [!warning]- Statutaire zetel ≠ werkelijke leiding voor de VB op rechtspersonen
> ❌ *"De vennootschap heeft haar werkelijke leiding in Antwerpen, dus Vlabel is bevoegd voor de VB op haar wagenpark."*
>
> Voor de **VB op rechtspersonen** is de **statutaire** (maatschappelijke) zetel doorslaggevend — niet de werkelijke leiding (zetel van werkelijke leiding speelt wél in andere fiscale contexten zoals territorialiteit Ven.B). Een vennootschap met statutaire zetel in BHG en werkelijke leiding in Antwerpen blijft VB betalen aan Brussel Fiscaliteit. Voor het examen: bij twijfel wordt naar de **statutaire** zetel verwezen tenzij de vraag uitdrukkelijk om de werkelijke leiding gaat.
>
> 🤖 *AI-aanvulling*

### 3. 🔍 Concrete situatie evalueren

> 📥 **Nodig**:
> - Lokaliseringsfactor per belasting (uit stap 2)
> - Feiten van het dossier: woonplaatsen, ligging goed, datum, zetels
>
> 📤 **Uitkomst**:
> - Per belasting: bevoegd gewest + bevoegde administratie (Vlabel / Brussel Fiscaliteit / FOD Financiën / SPW)

**Waarom**: de lokaliseringsfactor toepassen vereist dat je de relevante feiten consequent op de juiste **peildatum** of voor de juiste **periode** verifieert. Een woonplaatsverandering 3 dagen vóór overlijden, een verkoop op 31 december, een inschrijving op de eerste werkdag van januari: de exacte datum bepaalt soms het bevoegde gewest.

```
Peildatums per belasting (samenvatting):
- OV:                  1 januari aanslagjaar (eigendomstoestand op die dag)
- Erfbelasting:        datum overlijden (+ 5-jaars terugtelregel bij verhuis)
- Schenkbelasting:     datum schenking      (+ 5-jaars terugtelregel bij verhuis)
- Verkooprecht:        datum authentieke akte
- VB:                  inschrijvingsdatum (jaarlijkse hernieuwing)
- BIV:                 datum eerste inschrijving op naam
- Aanvullende GB PB:   1 januari aanslagjaar
```

> [!warning]- Vijf-jaarsregel bij erfbelasting en schenkbelasting
> ❌ *"De overledene woonde op datum overlijden in Vlaanderen, dus Vlaanderen int de erfbelasting."*
>
> Bij erfbelasting (rijksinwoner): wanneer de overledene in de **laatste 5 jaar vóór overlijden** in **meerdere gewesten** heeft gewoond, is het **gewest van de langste fiscale woonplaats** in die periode bevoegd (BFW art. 5 §2). De VCF en het federale Wb. Succ. regelen het belastbaar feit en de tarieven; de **gewestbevoegdheid bij verhuis** is gecodificeerd in de Bijzondere Financieringswet zelf. Voorbeeld: woonde 4 jaar in Brussel en 1 jaar in Vlaanderen vóór overlijden → **Brussel** is bevoegd, niet Vlaanderen, ondanks de woonplaats op datum overlijden in Vlaanderen.
>
> Voor schenkbelasting geldt dezelfde regel: gewest van langste fiscale woonplaats van schenker in 5 jaar vóór schenking.
>
> 🤖 *AI-aanvulling*

> [!info]- Concreet: overlijden na verhuis
>
> Mevrouw V. overlijdt op **10 maart 2025** in Knokke. Haar fiscale woonplaatsen vóór overlijden:
> - **1/1/2018 – 31/12/2021**: Sint-Gillis (BHG)
> - **1/1/2022 – 10/3/2025**: Knokke (Vlaanderen)
>
> Berekening peilperiode (10/3/2020 – 10/3/2025 = 5 jaar):
>
> | Gewest | Begin in peilperiode | Einde in peilperiode | Duur |
> |---|---|---|---|
> | BHG | 10/3/2020 | 31/12/2021 | ≈ 1 jaar 9 maanden |
> | Vlaanderen | 1/1/2022 | 10/3/2025 | ≈ 3 jaar 2 maanden |
>
> Vlaanderen wint → **Vlabel** is bevoegd voor de erfbelasting. De [[bronnen/wetteksten/IVA-vcf|VCF]] en de Vlaamse tarieven zijn van toepassing — niet de Brusselse, ondanks de langere absolute aanwezigheid in BHG (vóór de peilperiode telt niet mee).
>
> 🤖 *AI-aanvulling*

### 4. 💬 Conclusie formuleren met administratieve gevolgen

> 📥 **Nodig**:
> - Per belasting: bevoegd gewest + administratie (uit stap 3)
>
> 📤 **Uitkomst**:
> - Klant-conclusie: welke aangifte/aanslag wordt door welke administratie verwacht, op basis van welk regime
> - Vermelding van afwijkende termijnen of procedures per administratie

**Waarom**: het volstaat niet om te weten "Brussel is bevoegd" — de cliënt heeft baat bij een actiegerichte conclusie: welke termijnen, welke administratie, welke aangifteformulieren. Procedures verschillen substantieel tussen Vlabel (eigen termijnen VCF), Brussel Fiscaliteit (BCFP) en FOD Financiën (federale termijnen).

| Bevoegd gewest | Administratie | Bezwaartermijn | Specifieke aandachtspunten |
|---|---|---|---|
| **Vlaanderen** | Vlabel | 3 maanden ([[bronnen/wetteksten/IVA-vcf#art-35201\|VCF art. 3.5.2.0.1]]) | VCF-procedure |
| **Brussel** | Brussel Fiscaliteit (overgedragen overheveling sinds 2018) of FOD Financiën (rest) | Per belasting verschillend; check BCFP | NL/FR taalkeuze |
| **Wallonië** | SPW (eigen Waalse) of FOD Financiën (federaal geïnde overgedragen) | Per belasting verschillend | FR-talige administratie |

> [!info]- Concreet: na stap 3 → klant-conclusie voor erfbelasting
>
> "Voor de nalatenschap van mevrouw V. is **Vlabel** bevoegd op grond van de regel van de langste fiscale woonplaats in de laatste 5 jaar (Vlaanderen 3j2m vs. BHG 1j9m). De aangifte moet binnen **4 maanden** na overlijden (verlengbaar met 2 maanden) worden ingediend bij Vlabel via MyMinfin/Vlabel-portaal. Tarief volgens [[bronnen/wetteksten/IVA-vcf|VCF]] Titel 2 Hfdst 7 — voor de specifieke berekening: zie [[aangifte-nalatenschap-opmaken|aangifte nalatenschap]]."
>
> 🤖 *AI-aanvulling*

## Voorbeelden

> [!example]- Verhuis met meerdere belastinggevolgen
>
> **Situatie**: Een cliënt (rijksinwoner) verhuist op 15 september 2024 zijn fiscale woonplaats van Sint-Gillis (BHG) naar Knokke (Vlaanderen). Hij bezit:
> 1. Een appartement in Knokke (eigendom sinds 2018)
> 2. Een wagen op zijn naam
>
> Hij vraagt: "Welke gewestelijke belastingen ga ik voor 2025 betalen, en aan welke administratie?"
>
> **Conclusie**: voor AJ 2025 betaalt hij OV aan Vlabel (ligging pand), VB aan Vlabel (woonplaats op 1/1/2025), en aanvullende GB van de Vlaamse gemeente Knokke-Heist (woonplaats op 1/1/2025).
>
> **Grondslag**: [[bronnen/wetteksten/IVA-vcf#art-21101|VCF art. 2.1.1.0.1]] (OV — ligging); [[bronnen/wetteksten/IVA-vcf#art-22101|VCF art. 2.2.1.0.1]] (VB — fiscale woonplaats); WIB92 art. 466 (aanvullende GB — woonplaats 1/1).
>
> **Redenering**:
> - **OV**: peildatum 1/1/2025; pand in Vlaanderen → Vlabel int. (Was overigens al zo in 2024 — ligging is altijd bepalend, woonplaats irrelevant voor OV.)
> - **VB**: peildatum 1/1/2025; fiscale woonplaats sinds 15/9/2024 in Knokke → Vlabel bevoegd vanaf AJ 2025. (Voor AJ 2024 heeft hij voor het volledige jaar VB betaald aan Brussel Fiscaliteit, want woonplaats op 1/1/2024 was nog Sint-Gillis.)
> - **Aanvullende GB**: peildatum 1/1/2025; gemeente Knokke-Heist → Vlaams gemeentepercentage van toepassing op zijn federaal vastgestelde PB voor AJ 2025.
>
> 🤖 *AI-aanvulling*

> [!example]- Vennootschap met statutaire zetel in BHG, werkelijke leiding in Vlaanderen
>
> **Situatie**: Een bv heeft statutaire zetel in 1000 Brussel, werkelijke leiding in 2000 Antwerpen, en een wagenpark van 8 voertuigen ingeschreven op naam van de bv. De bv overweegt de statutaire zetel te verhuizen naar Antwerpen om de fiscale druk te optimaliseren.
>
> **Conclusie**: vandaag betaalt de bv VB aan **Brussel Fiscaliteit** voor alle 8 voertuigen (statutaire zetel doorslaggevend). Verhuis van de statutaire zetel naar Antwerpen maakt **Vlabel** bevoegd vanaf het volgende aanslagjaar — wat voordelig of nadelig kan zijn naargelang de voertuigcategorieën (Vlaamse vergroeningsformule vs. Brussels regime).
>
> **Grondslag**: [[bronnen/wetteksten/IVA-vcf#art-22101|VCF art. 2.2.1.0.1]] — voor rechtspersonen is de statutaire zetel doorslaggevend (analoog in BCFP voor BHG-bevoegdheid).
>
> **Redenering**: de werkelijke leiding speelt geen rol voor de gewestelijke VB op een rechtspersoon — de wettelijke aanknoping is uitsluitend de statutaire zetel. Dit is het tegenovergestelde van de **federale Ven.B** waar de werkelijke leiding kan doorslaggevend zijn voor onbeperkte fiscale aansprakelijkheid (WIB92 art. 2 §1, 5°). Voor de gewestelijke heffing telt de zetel zoals ingeschreven in het KBO en in de aangifte van de bv.
>
> Voor de BIV: enkel relevant bij **nieuwe** inschrijvingen — bestaande voertuigen ondergaan geen herinschrijving bij verhuis statutaire zetel; Brussel-BIV blijft definitief verworven.
>
> 🤖 *AI-aanvulling*

## Motiveren op het examen

**Een volledig antwoord bevat:**
1. **Identificatie van de gewestelijke belasting** in geding (welk type heffing wordt geactiveerd door de feiten?)
2. **Bron** (artikel of codex) waarin de lokaliseringsfactor staat
3. **Toepassing op de feiten** met expliciete vermelding van de **peildatum**
4. **Bevoegde administratie** (Vlabel / Brussel Fiscaliteit / FOD Financiën / SPW) en eventueel de **bezwaartermijn**

**Voorbeeldvragen**

> [!question]- Welk gewest is bevoegd voor de erfbelasting?
>
> Mijnheer P. overlijdt op 5 mei 2025. In de laatste 5 jaar vóór overlijden woonde hij:
> - 1/4/2020 – 30/9/2022 in Etterbeek (BHG)
> - 1/10/2022 – 31/3/2024 in Hasselt (Vlaanderen)
> - 1/4/2024 – overlijden in Verviers (Wallonië)
>
> Welk gewest is bevoegd voor de erfbelasting/successierechten?
>
> > [!success]- Antwoord
> >
> > **Brussels Hoofdstedelijk Gewest.**
> >
> > Op grond van de **5-jaarsregel** (BFW art. 5 §2; aanknoping ook in [[bronnen/wetteksten/IVA-vcf#art-27101|VCF art. 2.7.1.0.1]] en Wb. Succ. art. 1) is het bevoegd gewest dat waar de overledene in de **laatste 5 jaar** vóór overlijden de **langste fiscale woonplaats** had.
> >
> > Berekening (peilperiode 5/5/2020 – 5/5/2025):
> > - Etterbeek (BHG): van 5/5/2020 tot 30/9/2022 = ongeveer 2 jaar 5 maanden
> > - Hasselt (Vl): van 1/10/2022 tot 31/3/2024 = ongeveer 1 jaar 6 maanden
> > - Verviers (W): van 1/4/2024 tot 5/5/2025 = ongeveer 1 jaar 1 maand
> >
> > BHG heeft de langste duur → **Brussel Fiscaliteit / FOD Financiën** int de successierechten op basis van het Wb. Succ. + Brusselse tariefdecreten.
> >
> > De woonplaats op datum overlijden (Verviers) is **niet** doorslaggevend.
> >
> > *Zie: [[#2-lokaliseringsfactor-opzoeken-per-belasting|Lokaliseringsfactor opzoeken]], [[gewestelijke-belastingen#-belastingregeling-brussels-hoofdstedelijk-gewest|Belastingregeling BHG]]*
>
> 🤖 *AI-aanvulling*

> [!question]- Pand in Wallonië, eigenaar in Vlaanderen
>
> Een Vlaamse rijksinwoner bezit een vakantiewoning in de Ardennen. Welke gewestelijke OV-tarieven gelden, en wie int?
>
> > [!success]- Antwoord
> >
> > **Waalse OV-tarieven; FOD Financiën int (in het overgangsregime).**
> >
> > De OV volgt de **ligging van het onroerend goed** (WIB92 art. 249) — de woonplaats van de eigenaar speelt geen rol. Het pand ligt in Wallonië, dus het Waals tariefregime is van toepassing. In het overgangsregime is dat **WIB92 art. 249-260** + Waalse tariefdecreten; de inning gebeurt door de **FOD Financiën** (Wallonië heeft de OV-inning niet zelf overgenomen — anders dan Vlaanderen via Vlabel sinds 1999).
> >
> > De Vlaamse OV-tarieven en de Vlabel-procedure (VCF) zijn **niet** van toepassing — toepassing van VCF op een pand buiten Vlaanderen is een typische beginnersfout.
> >
> > *Zie: [[onroerende-voorheffing#-tarief-van-de-ov-per-gewest|OV-tarief per gewest]], [[gewestelijke-belastingen#-belastingregeling-waals-gewest|Belastingregeling Wallonië]]*
>
> 🤖 *AI-aanvulling*
