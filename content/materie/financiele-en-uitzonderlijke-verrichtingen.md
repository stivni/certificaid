---
tags: ["1.1", wip, materie]
niveau: toepassen
status: draft
bouwversie: 2
bronnen:
  - KB WVV 29 april 2019 art. 3:90 (definitie rubrieken resultatenrekening incl. financieel resultaat)
  - KB WVV 29 april 2019 art. 3:11 (matching)
  - CBN-advies 2016/24
---

# Financiële en niet-recurrente verrichtingen

De resultatenrekening is opgebouwd in drie lagen: het [[bedrijfsresultaat-kosten-opbrengsten|bedrijfsresultaat]], het **financieel resultaat** en het **niet-recurrent resultaat**. Samen leiden ze tot het resultaat vóór belastingen, zoals weergegeven in de [[resultaatniveaus|resultaatniveaus]]. Deze fiche behandelt de financiële verrichtingen (klassen 65 en 75) en de niet-recurrente verrichtingen (klassen 66 en 76).

---

## 📌 Financieel resultaat

Het financieel resultaat is het saldo van de financiële opbrengsten (klasse 75) en de financiële kosten (klasse 65). Het staat structureel **ná** het [[bedrijfsresultaat-kosten-opbrengsten|bedrijfsresultaat]] in de resultatenrekening en beïnvloedt het resultaat vóór belastingen.

**Berekening:**

```
Financieel resultaat = financiële opbrengsten (klasse 75)
                     − financiële kosten (klasse 65)
```

Het financieel resultaat weerspiegelt de kost van de schuldfinanciering, de opbrengsten uit beleggingen, en de resultaten van wisselkoersbewegingen en realisaties van vlottende activa.

---

## 📌 Financiële kosten (klasse 65)

Financiële kosten zijn kosten van financiële aard die verbonden zijn aan de gewone bedrijfsvoering maar buiten het eigenlijke bedrijfsproces vallen. De rubrieken zijn gedefinieerd in de bijlage van art. 3:90 KB WVV:

| Rekening | Benaming | Inhoud |
|---|---|---|
| **650** | Kosten van schulden | Interesten, commissies en kosten verbonden aan schulden; afschrijving kosten bij uitgifte leningen en disagio — geactiveerde interesten worden afgetrokken ([[bronnen/wetteksten/XV-KB-wvv#art-390|KB WVV art. 3:90 — rubriek V.A.]]) |
| **651** | Waardeverminderingen op vlottende activa (andere dan voorraden en bestellingen) | Waardeverminderingen op vorderingen (andere dan handelsvorderingen), geldbeleggingen en liquide middelen — terugnemingen worden hier ook geboekt ([[bronnen/wetteksten/XV-KB-wvv#art-390|KB WVV art. 3:90 — rubriek V.B.]]) |
| **652** | Minderwaarden op realisatie van vlottende activa | Minderwaarden bij realisatie van vorderingen (andere dan handelsvorderingen), geldbeleggingen en liquide middelen ([[bronnen/wetteksten/XV-KB-wvv#art-390|KB WVV art. 3:90 — rubriek V.C. 1°]]) |
| **653** | Discontokosten op vorderingen | Het disconto ten laste van de vennootschap bij het verhandelen van vorderingen (wissel, warrant, factuur) ([[bronnen/wetteksten/XV-KB-wvv#art-390|KB WVV art. 3:90 — rubriek V.C. 2°]]) |
| **654** | Wisselresultaten | Wisselresultaten en resultaten uit omrekening van vreemde valuta, tenzij specifiek verbonden aan een andere post ([[bronnen/wetteksten/XV-KB-wvv#art-390|KB WVV art. 3:90 — rubriek V.C. 3°]]) |
| **657** | Andere financiële kosten | Kosten betreffende posten van eigen vermogen (kosten bij inbreng, kapitaalverhoging), taksen op effecten, commissies en andere financiële kosten ([[bronnen/wetteksten/XV-KB-wvv#art-390|KB WVV art. 3:90 — rubriek V.C. 4°–5°]]) |

> [!info]- In de praktijk: bankrentekosten boeken
>
> Een onderneming betaalt € 3.500 rente op een bankkrediet.
>
> ```
> D  650  Kosten van schulden       3.500
>     C  550  Kredietinstellingen        3.500
> ```
>
> De rentekost verlaagt het financieel resultaat (en daarmee het resultaat vóór belastingen), maar heeft geen invloed op het [[bedrijfsresultaat-kosten-opbrengsten|bedrijfsresultaat]] (EBIT).
>
> 🤖 *AI-aanvulling*

---

## 📌 Financiële opbrengsten (klasse 75)

Financiële opbrengsten vloeien voort uit financiële activa en activiteiten — niet uit het eigenlijke productie- of dienstverleningsproces. De rubrieken zijn gedefinieerd in de bijlage van art. 3:90 KB WVV:

| Rekening | Benaming | Inhoud |
|---|---|---|
| **750** | Opbrengsten van financiële vaste activa | Dividenden, interesten en andere opbrengsten van [[vaste-activa-waardering#-financiële-vaste-activa-fva|financiële vaste activa]] |
| **751** | Opbrengsten van vlottende activa | Interesten, dividenden en andere opbrengsten uit [[vlottende-activa-waardering#-geldbeleggingen-en-liquide-middelen|geldbeleggingen en liquide middelen]] — ook van vorderingen andere dan handelsvorderingen ([[bronnen/wetteksten/XV-KB-wvv#art-390|KB WVV art. 3:90 — rubriek IV.B.]]) |
| **752** | Meerwaarden op realisatie van vlottende activa | Meerwaarden bij realisatie van vorderingen (andere dan handelsvorderingen), geldbeleggingen en liquide middelen ([[bronnen/wetteksten/XV-KB-wvv#art-390|KB WVV art. 3:90 — rubriek IV.C. 1°]]) |
| **754** | Wisselresultaten | Wisselresultaten en resultaten uit omrekening van vreemde valuta — dezelfde tegenhanger als rekening 654, maar dan in het voordeel ([[bronnen/wetteksten/XV-KB-wvv#art-390|KB WVV art. 3:90 — rubriek IV.C. 3°]]) |
| **757** | Andere financiële opbrengsten | Als opbrengst geboekte kapitaal- en interestsubsidies (volledig schema); alle overige opbrengsten van financiële aard zonder verband met welbepaalde activa ([[bronnen/wetteksten/XV-KB-wvv#art-390|KB WVV art. 3:90 — rubriek IV.C. 2° en 4°]]) |

> [!info]- In de praktijk: verkoop effecten met meerwaarde
>
> Een onderneming verkoopt geldbeleggingen (aankoopwaarde € 10.000) voor € 11.500.
>
> ```
> D  550  Bank                           11.500
>     C  510  Geldbeleggingen (aankoopwaarde) 10.000
>     C  752  Meerwaarden op realisatie vl. activa  1.500
> ```
>
> De meerwaarde van € 1.500 verhoogt het financieel resultaat. Had men met verlies verkocht (bv. € 9.000), dan boekt men de minderwaarde op rekening 652 als financiële kost.
>
> 🤖 *AI-aanvulling*

---

## 📌 Niet-recurrente verrichtingen (klassen 66 en 76)

Niet-recurrente verrichtingen zijn kosten en opbrengsten die een **bedrijfs- of financieel karakter** hebben, maar **geen verband houden met de gewone bedrijfsuitoefening** van de vennootschap. Ze worden apart getoond in de resultatenrekening om de lezer in staat te stellen het gewone bedrijfsresultaat te onderscheiden van eenmalige of bijzondere elementen.

Het criterium is inhoudelijk: verricht de vennootschap dit type transactie regelmatig in haar normale activiteit, of is het eerder eenmalig of uitzonderlijk? Dit is een **feitelijke beoordeling** per vennootschap — dezelfde handeling (bv. verkoop van een voertuig) kan recurrent zijn voor een leasingmaatschappij maar niet-recurrent voor een productiebedrijf.

**Vier groepen:**

| Groep | Kosten | Opbrengsten |
|---|---|---|
| **Niet-recurrente bedrijfskosten** | 660–669 | 760–769 |
| **Niet-recurrente financiële kosten** | 661, 6621, 6631, 668, 6691 | 761, 7621, 7631, 769 |

De meest voorkomende rubrieken (CBN-advies 2016/24):

| Rekening | Benaming |
|---|---|
| **660** | Niet-recurrente afschrijvingen en waardeverminderingen op vaste activa |
| **6620** | Voorzieningen voor niet-recurrente bedrijfsrisico's en kosten (toevoeging) |
| **6630** | Minderwaarde op realisatie van immateriële en materiële vaste activa |
| **664–667** | Andere niet-recurrente bedrijfskosten |
| **6690** | Als herstructureringskosten geactiveerde niet-recurrente bedrijfskosten (−) |
| **661** | Waardeverminderingen op financiële vaste activa (toevoeging) |
| **6631** | Minderwaarde op realisatie van financiële vaste activa |
| **668** | Andere niet-recurrente financiële kosten |
| **760–7601** | Terugneming van afschrijvingen op vaste activa |
| **7620** | Terugneming voorzieningen voor niet-recurrente bedrijfsrisico's |
| **7630** | Meerwaarde op realisatie van immateriële en materiële vaste activa |
| **764–768** | Andere niet-recurrente bedrijfsopbrengsten |
| **761** | Terugneming waardeverminderingen op financiële vaste activa |
| **7631** | Meerwaarde op realisatie van financiële vaste activa |
| **769** | Andere niet-recurrente financiële opbrengsten |

---

## ⚖️ Historiek: van "uitzonderlijk resultaat" naar "niet-recurrent"

Vóór boekjaren vanaf 1 januari 2016 kende de resultatenrekening een aparte rubriek **"Uitzonderlijk resultaat"** (klassen 66/76 onder het oude KB W.Venn.). Die stond structureel ná het bedrijfsresultaat én het financieel resultaat als derde laag.

Het KB van 18 december 2015 — ter omzetting van EU-Richtlijn 2013/34 — schafte die aparte rubriek af. De uitzonderlijke resultaten worden sindsdien **ondergebracht bij het bedrijfsresultaat of het financieel resultaat**, naargelang hun aard, en aangeduid als **niet-recurrente resultaten**.

De CBN benadrukt uitdrukkelijk dat dit **enkel een wijziging in presentatie en benaming** betreft — op **inhoudelijk vlak, wat de kwalificatie betreft, is er geen wijziging**. De grens van wat "niet-recurrent" is, is identiek aan die van wat vroeger "uitzonderlijk" was. ([[bronnen/adviezen/CBN-2016-24-uitzonderlijke-resultaten-wijzigingen-door-het-koninklijk-besluit-van-18-december-2015|CBN-advies 2016/24]])

> [!warning]- Niet-recurrent en uitzonderlijk zijn inhoudelijk equivalent — alleen de presentatie verschilt
> ❌ *"Niet-recurrente kosten zijn iets anders dan vroeger uitzonderlijke kosten — de nieuwe term heeft een engere definitie."*
>
> De CBN stelt expliciet: "in de praktijk geen verschil moet worden gezocht tussen de bewoordingen *uitzonderlijk* en *niet-recurrent*." Het gaat om eenzelfde kwalificatiecriterium, enkel de indeling in de resultatenrekening is aangepast. Verouderde jaarrekeningen (vóór 2016) vermelden het bedrag onder de rubriek "uitzonderlijke resultaten" — het is hetzelfde concept.
>
> 📝 *Op basis van CBN-advies 2016/24*

---

## 📋 Boekingen — financiële verrichtingen

### Kosten van schulden (bankrenten)

```
D  650  Kosten van schulden           X
     C  550  Bank (of 499 Over te dragen k.)  X
```

### Realisatie geldbeleggingen met meerwaarde

```
D  550  Bank                              realisatieprijs
     C  510  Geldbeleggingen (aankoopwaarde)  aankoopwaarde
     C  752  Meerwaarden op realisatie vl. activa  meerwaarde
```

### Realisatie geldbeleggingen met minderwaarde

```
D  550  Bank                              realisatieprijs
D  652  Minderwaarden op realisatie vl. activa  minderwaarde
     C  510  Geldbeleggingen (aankoopwaarde)  aankoopwaarde
```

### Wisselverlies bij afsluiting (leverancier in vreemde valuta)

Bij afsluiting worden schulden in vreemde valuta herrekend aan de slotkoers. Een koersstijging van de vreemde munt betekent een verlies voor de schuldenaar:

```
D  654  Wisselresultaten (kost)     koersverlies
     C  440  Leveranciers                koersverlies
```

Een wisselwinst wordt gespiegeld:

```
D  440  Leveranciers                koerswinst
     C  754  Wisselresultaten (opbrengst)    koerswinst
```

---

## 📋 Boekingen — niet-recurrente verrichtingen

### Verkoop vaste activa met meerwaarde

Stel: een machine met aanschaffingswaarde € 50.000, gecumuleerde [[afschrijvingen|afschrijvingen]] € 35.000 (boekwaarde € 15.000), wordt verkocht voor € 20.000.

```
Stap 1 — uitboeken actief en gecumuleerde afschrijvingen:
D  239  Gecumuleerde afschrijvingen MVA     35.000
     C  230  Materiële vaste activa (aanschaffingswaarde)  35.000

Stap 2 — realisatie boeken:
D  550  Bank                               20.000
     C  230  Materiële vaste activa (boekwaarde)  15.000
     C  7630  Meerwaarden op realisatie MVA  5.000
```

De meerwaarde van € 5.000 wordt geboekt als niet-recurrente bedrijfsopbrengst — het betreft de realisatie van een vast actief, geen gewone verkooptransactie.

### Verkoop vaste activa met minderwaarde

Zelfde actief, maar nu verkocht voor € 12.000:

```
D  550  Bank                               12.000
D  6630  Minderwaarden op realisatie MVA    3.000
     C  230  Materiële vaste activa (boekwaarde)  15.000
```

### Herstructureringskost via voorziening

```
D  6620  Voorzieningen niet-rec. bedrijfsrisico's  X
     C  160  Voorzieningen voor risico's en kosten  X
```

Bij effectieve betaling van de herstructureringskost:

```
D  160  Voorzieningen voor risico's en kosten  X
     C  440/550  Leverancier / Bank              X
```

---

## 🔎 Patroon — wat is typisch een niet-recurrente verrichting

Niet-recurrente verrichtingen zijn structureel zeldzaam of éénmalig voor de specifieke vennootschap. Typische voorbeelden:

- **Verkoop van vaste activa** (immaterieel of materieel): meer- of minderwaarde op realisatie — het actief was niet bestemd voor verkoop in het kader van de gewone bedrijfsuitoefening
- **Herstructureringskosten**: studiekosten bij reorganisatie, ontslagvergoedingen buiten de normale personeelsrotatie, kosten voor herscholing bij stopzetting activiteit
- **Bijzondere waardeverminderingen op vaste activa**: wegens structurele ontwaarding van een bedrijfstak, niet de jaarlijkse [[afschrijvingen|afschrijving]]
- **Bijzondere [[voorzieningen|voorzieningen]]** voor niet-recurrente risico's: rechtszaken, milieusaneringen, reorganisatiekosten
- **Schade door catastrofen**: brand, overstroming — onverwacht en niet-jaarlijks
- **Stopzetting bedrijfsactiviteit**: afwikkeling van een verlieslatend segment, incl. mogelijke meerwaarden op het afgestoten deel
- **Kwijtschelding van schulden bij vereffening** — als niet-recurrente financiële opbrengst ([[bronnen/adviezen/CBN-0170-01-boekhoudkundige-verwerking-van-niet-betaalde-schulden-wegens-ontoereikend-actief-bij-het|CBN-advies 170/1]])
- **Realisatie van financiële vaste activa**: meer- of minderwaarde bij verkoop van deelnemingen

> [!info]- In de praktijk: herstructurering van een productieafdeling
>
> Een industrie-onderneming sluit een afdeling. Ze boekt:
> - Ontslagvergoedingen buiten de normale loonkost: 660 (niet-recurrente bedrijfskost)
> - Consultantkosten reorganisatie: 664 (andere niet-recurrente bedrijfskosten)
> - Restwaarde achtergelaten machines: 6630 (minderwaarde op realisatie MVA)
> - Huurkost van stopgezette site die doorloopt: 61 (gewone bedrijfskost — recurrent zolang het contract loopt)
>
> De laatste kost is recurrent — ook al hangt hij samen met de herstructurering, de aard ervan (huur) is gewone bedrijfsvoering.
>
> 🤖 *AI-aanvulling*

---

## 🚩 Antipatroon — recurrente kost als niet-recurrent boeken om bedrijfsresultaat op te poetsen

Een bestuurder wil de [[resultaatniveaus|EBIT (bedrijfsresultaat)]] verbeteren door kosten die eigenlijk tot de gewone bedrijfsuitoefening behoren, te herclassificeren als niet-recurrent.

**Voorbeeld van misclassificatie:**
- Jaarlijkse onderhoudskosten die "wat hoger uitvallen dit jaar" → niet-recurrent boeken
- Gewone waardeverminderingen op handelsvorderingen → als niet-recurrente financiële kost boeken
- Personeelskost bij een eenmalig project dat elk jaar opduikt → als niet-recurrente bedrijfskost boeken

**Waarom problematisch:** De analyse-gebruiker (bank, investeerder, commissaris) leest de EBIT als maat voor de herhalende operationele prestatie. Een geconstrueerde EBIT die structureel hogere kosten uitsluit, geeft een vertekend beeld van de duurzame winstgevendheid.

> [!warning]- Niet-recurrent vereist een feitelijk oordeel, geen budgettair motief
> ❌ *"De kost was hoger dan verwacht — dus is het niet-recurrent."*
>
> Het criterium is de **aard van de verrichting**: heeft de vennootschap dit type transactie regelmatig in haar gewone bedrijfsactiviteit, of is het werkelijk eenmalig of uitzonderlijk? Het feit dat een kost hoog of onverwacht is, maakt hem niet niet-recurrent. Een hoge onderhoudsrekening blijft een gewone bedrijfskost (klasse 61). ([[bronnen/wetteksten/XV-KB-wvv|KB WVV art. II. I.]])
>
> 🤖 *AI-aanvulling*

---

## 🚩 Antipatroon — wisselresultaten niet herrekenen bij afsluiting

Schulden en vorderingen uitgedrukt in vreemde valuta moeten op balansdatum worden omgerekend tegen de **slotkoers**. Het resulterende wisselresultaat wordt geboekt op rekening 654 (verlies) of 754 (winst).

Een courante fout is om de oorspronkelijke boekwaarde te behouden bij de afsluiting, waardoor het wisselresultaat pas bij de effectieve betaling zichtbaar wordt — in een ander boekjaar dan waarop het economisch thuishoort.

Dit schendt het **matching-beginsel** van [[boekhoudkundige-beginselen|KB WVV art. 3:11]]: kosten en opbrengsten die betrekking hebben op het boekjaar, moeten in dat boekjaar worden geboekt, ongeacht het moment van betaling.

> [!warning]- Wisselresultaten horen op de datum van de afsluiting, niet bij de betaling
> ❌ *"We hebben de schuld in vreemde valuta nog niet betaald, dus we boeken het wisselresultaat pas volgend jaar."*
>
> Op balansdatum worden schulden in vreemde valuta herrekend aan de slotkoers. Het wisselresultaat — verlies (654) of winst (754) — behoort tot het huidige boekjaar, ongeacht wanneer de betaling plaatsvindt. Dit volgt uit het [[boekhoudkundige-beginselen|matchingbeginsel]] ([[bronnen/wetteksten/XV-KB-wvv#art-311|KB WVV art. 3:11]]). ([[bronnen/wetteksten/XV-KB-wvv#art-312|Art. 3:12]] beschrijft de omrekeningsmethoden voor vreemde valuta.)
>
> 🤖 *AI-aanvulling*

---

## ↔️ Recurrent vs. niet-recurrent

| Kenmerk | Recurrent (klassen 65/75) | Niet-recurrent (klassen 66/76) |
|---|---|---|
| **Verband met gewone bedrijfsvoering** | Ja — behoort tot de normale jaarlijkse cyclus | Nee — valt buiten de gewone bedrijfsuitoefening |
| **Frequentie** | Regelmatig terugkerend | Eenmalig of uitzonderlijk |
| **Voorbeelden kosten** | Bankrenten (650), waardevermindering vlottende activa (651), disconto op wissels (653), wisselverliezen (654) | Verlies op verkoop vaste activa (6630), herstructureringskosten (664), bijzondere afschrijving vaste activa (660) |
| **Voorbeelden opbrengsten** | Dividenden op deelnemingen (750), interesten spaarrekening (751), winst op realisatie belegging (752) | Winst op verkoop vaste activa (7630), terugneming bijzondere afschrijving (7600–7601), terugneming voorziening niet-rec. risico (7620) |
| **Impact op EBIT** | Neen — financieel resultaat staat ná EBIT | Deels — niet-recurrente bedrijfsresultaten zijn onderdeel van het bedrijfsresultaat |
| **Schema-positie** | IV (opbrengsten) en V (kosten) — volledig schema | I.E / II.I (bedrijf) en IV.D / V.D (financieel) — volledig schema |

> [!warning]- Niet-recurrente bedrijfsresultaten zitten wél in het bedrijfsresultaat
> ❌ *"Niet-recurrente resultaten staan altijd ná het bedrijfsresultaat en financieel resultaat — ze beïnvloeden de EBIT niet."*
>
> Vóór 2016 stonden uitzonderlijke resultaten als afzonderlijke derde laag ná EBIT. **Sindsdien niet meer.** Niet-recurrente **bedrijfs**kosten en -opbrengsten (660–669 / 760–769) zitten nu in de resultaatposten II.I en I.E — die behoren structureel tot het bedrijfsresultaat. Alleen niet-recurrente **financiële** kosten en opbrengsten (661, 668 / 761, 769) zitten in de financiële posten V.D en IV.D. ([[bronnen/adviezen/CBN-2016-24-uitzonderlijke-resultaten-wijzigingen-door-het-koninklijk-besluit-van-18-december-2015|CBN-advies 2016/24]])
>
> 🤖 *AI-aanvulling*

---

## Relevant voor

**[[1.1-algemene-boekhouding|1.1 Algemene boekhouding]]**

Taken:
- *Het voeren van een boekhouding van financiële en uitzonderlijke verrichtingen*
  - De student kan financiële kosten en opbrengsten correct classificeren en boeken
  - De student kan niet-recurrente verrichtingen identificeren en boeken

Kenniselementen:
- II.O — [[financiele-en-uitzonderlijke-verrichtingen#-financieel-resultaat|Financiële verrichtingen]] (klassen 65 en 75)
- II.P — [[financiele-en-uitzonderlijke-verrichtingen#-niet-recurrente-verrichtingen-klassen-66-en-76|Niet-recurrente verrichtingen]] (klassen 66 en 76)

---

### Voorbeeldvragen

> [!question]- Classificatie wisselresultaat
>
> Een onderneming heeft een schuld in USD. Bij de afsluiting van het boekjaar stijgt de dollar t.o.v. de euro, waardoor de schuld in euro hoger wordt. Hoe wordt dit wisselresultaat geboekt, en wanneer?
>
> > [!success]- Antwoord
> >
> > **Het wisselresultaat wordt geboekt op balansdatum**, niet bij de betaling.
> >
> > Een stijging van de USD t.o.v. de euro is een verlies voor de schuldenaar: de schuld in euro neemt toe. Dit wordt geboekt op:
> > ```
> > D  654  Wisselresultaten (kost)     koersverlies
> >      C  440  Leveranciers (aanpassing)    koersverlies
> > ```
> > Dit volgt uit het [[boekhoudkundige-beginselen|matchingbeginsel]] ([[bronnen/wetteksten/XV-KB-wvv#art-311|KB WVV art. 3:11]]): kosten die betrekking hebben op het boekjaar worden in dat boekjaar geboekt, ongeacht het moment van betaling.
> >
> > *Zie: [[financiele-en-uitzonderlijke-verrichtingen#-boekingen--financiële-verrichtingen|Boekingen financiële verrichtingen]]*
>
> 🤖 *AI-aanvulling*

> [!question]- Verkoop machine: welke rekening?
>
> Een onderneming verkoopt een machine (boekwaarde € 8.000) voor € 11.000. Op welke rekening wordt de meerwaarde geboekt, en is dit een recurrente of niet-recurrente post?
>
> > [!success]- Antwoord
> >
> > **Rekening 7630 — Meerwaarden op realisatie van immateriële en materiële vaste activa**, een **niet-recurrente bedrijfsopbrengst**.
> >
> > De verkoop van een vast actief behoort niet tot de gewone bedrijfsuitoefening van een productie- of dienstverleningsbedrijf. Het is een eenmalige verrichting die buiten de normale cyclus valt → niet-recurrent ([[bronnen/wetteksten/XV-KB-wvv|KB WVV art. I.E. 3°]]). Boeking:
> > ```
> > D  550  Bank                   11.000
> >      C  230  MVA (boekwaarde)       8.000
> >      C  7630  Meerwaarden realisatie MVA  3.000
> > ```
> > **Uitzondering**: als de vennootschap regelmatig vaste activa verkoopt in het kader van haar gewone bedrijfsuitoefening (bv. een leasingmaatschappij), dan mogen meerwaarden op materiële vaste activa onder "Andere bedrijfsopbrengsten" (rubriek I.D) worden geboekt.
> >
> > *Zie: [[financiele-en-uitzonderlijke-verrichtingen#-boekingen--niet-recurrente-verrichtingen|Boekingen niet-recurrente verrichtingen]]*
>
> 🤖 *AI-aanvulling*

> [!question]- Niet-recurrente kost of gewone bedrijfskost?
>
> Een onderneming koopt jaarlijks nieuwe computers voor haar medewerkers. Dit jaar zijn er veel meer computers aangekocht omdat een nieuwe afdeling is opgestart. De CFO wil de extra computers als niet-recurrente bedrijfskost boeken om de gewone bedrijfskosten laag te houden.
>
> Is dit boekhoudkundig correct?
>
> > [!success]- Antwoord
> >
> > **Nee.**
> >
> > Aankopen van computers zijn een gewone bedrijfskost (of [[vaste-activa-waardering|activering als vaste activa]] bij een bepaalde drempel). Het feit dat de aankoop "groter dan normaal" is, maakt de kost niet niet-recurrent. De kwalificatie "niet-recurrent" berust op de **aard van de transactie** — behoort dit type activiteit tot de gewone bedrijfsvoering? Ja: aankopen voor de bedrijfsuitrusting zijn gewoon. De omvang bepaalt niet de classificatie.
> >
> > Door dit ten onrechte als niet-recurrent te boeken, wordt het [[resultaatniveaus|bedrijfsresultaat (EBIT)]] kunstmatig hoger voorgesteld.
> >
> > *Zie: [[financiele-en-uitzonderlijke-verrichtingen#-antipatroon--recurrente-kost-als-niet-recurrent-boeken-om-bedrijfsresultaat-op-te-poetsen|Antipatroon — recurrente kost als niet-recurrent boeken]]*
>
> 🤖 *AI-aanvulling*
