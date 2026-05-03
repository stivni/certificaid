---
tags: ["1.1", wip, materie]
niveau: toepassen
status: draft
bouwversie: 2
bronnen:
  - KB WVV 2019 art. 3:90 (inhoud rubrieken resultatenrekening)
  - KB WVV 2019 art. 3:81 (schema resultatenrekening)
  - KB WVV 2019 art. 3:11 (matching)
---

# Bedrijfsresultaat: kosten en opbrengsten

De resultatenrekening bestaat uit drie lagen: het bedrijfsresultaat, het financieel resultaat en het niet-recurrent resultaat. Deze fiche behandelt de eerste laag — de **operationele activiteit** van de onderneming. Bedrijfskosten en bedrijfsopbrengsten zijn de posten die voortkomen uit de gewone bedrijfsuitoefening; ze bepalen het [[resultaatniveaus#-resultaatniveaus|bedrijfsresultaat (EBIT)]].

De resultatenrekening wordt opgesteld overeenkomstig het schema in bijlage 3 van het KB WVV. ([[bronnen/wetteksten/XV-KB-wvv#art-381|ITAA-LEX XV (KB) · KB WVV 2019 art. 3:81]])

---

## 📌 Bedrijfsopbrengsten

De bedrijfsopbrengsten zijn alle opbrengsten die voortvloeien uit de gewone bedrijfsuitoefening. Ze vormen rubriek I van de resultatenrekening (volledig schema) en omvatten klasse 70–74 van het minimumrekeningenstelsel (MAR).

Het volledig schema onderscheidt de volgende posten:

| Post | Omschrijving | MAR |
|---|---|---|
| **I.A Omzet** | Verkoop van goederen en levering van diensten aan derden, na kortingen (afslag, ristorno, rabat), excl. btw | 70 |
| **I.B Voorraadwijziging** | Wijziging in de voorraad goederen in bewerking, gereed product en bestellingen in uitvoering (positief = toename = opbrengst) | 71 |
| **I.C Geproduceerde vaste activa** | Kosten van vaste activa die de vennootschap zelf heeft vervaardigd, als opbrengst geneutraliseerd | 72 |
| **I.D Andere bedrijfsopbrengsten** | Overige bedrijfsverbonden opbrengsten: exploitatiesubsidies, meerwaarden op handelsvorderingen | 74 |
| **I.E Niet-recurrente bedrijfsopbrengsten** | Opbrengsten buiten de gewone bedrijfsuitoefening | 76 |

([[bronnen/wetteksten/XV-KB-wvv#art-390|ITAA-LEX XV (KB) · KB WVV 2019 art. 3:90]])

---

## 📌 Omzet (post I.A)

De omzet omvat het bedrag van de **verkoop van goederen en de levering van diensten aan derden**, in het kader van de gewone bedrijfsuitoefening, na aftrek van in de handel toegestane kortingen. De omzet bevat **geen btw** en geen andere rechtstreeks met de omzet verbonden belastingen. ([[bronnen/wetteksten/XV-KB-wvv#art-390|KB WVV 2019 art. 3:90]])

Overheidstegemoetkomingen als compensatie voor lagere ontvangsten in het kader van een tariferingspolitiek vallen ook onder de omzet.

---

## 📌 Voorraadwijziging in goederen in bewerking en gereed product (post I.B)

*Variation de stocks de produits en cours de fabrication et de produits finis*

De voorraadwijziging neutraliseert het verschil tussen wat de onderneming **heeft aangekocht of geproduceerd** en wat ze **heeft verkocht**. Ze past de resultatenrekening aan zodat enkel de kosten van **verkochte** goederen ten laste vallen.

- **Toename van de voorraad** (eindvoorraad > beginvoorraad): meer geproduceerd dan verkocht → de extra productie is nog in voorraad → **positief effect** op de resultatenrekening (rubriek I.B, klasse 71 credit)
- **Afname van de voorraad** (eindvoorraad < beginvoorraad): meer verkocht dan geproduceerd → voorraad is aangesproken → **negatief effect** op de resultatenrekening (rubriek I.B, klasse 71 debet)

De voorraadwijziging staat in het volledig schema **aan de opbrengstenzijde** (post I.B), maar kan zowel positief als negatief zijn.

> [!warning]- Voorraadwijziging toename is een opbrengst, afname een kost
> ❌ *"Een voorraadwijziging staat altijd aan de kostenzijde."*
>
> De voorraadwijziging staat in het volledig schema aan de opbrengstenzijde (post I.B). Een **toename** vergroot de opbrengsten (credit 71 → positief saldo post I.B). Een **afname** verkleint de opbrengsten (debet 71 → negatief saldo post I.B, weergegeven als minteken). De logica: als je meer produceerde dan verkocht, is die productie-inspanning nog niet als kost "gedekt" door een opbrengst — de activering in voorraad compenseert de aankoopkosten.
>
> 🤖 *AI-aanvulling*

---

## 📌 Geproduceerde vaste activa (post I.C)

Wanneer een onderneming **zelf vaste activa vervaardigt** — bv. een installatie bouwen met eigen personeel en materiaal — worden de gemaakte kosten geactiveerd als vast actief. Om te vermijden dat die kosten twee keer ten laste vallen (eenmaal als loonkost of materiaalinkoop én later via afschrijving), boekt de onderneming een tegenprestatie in de resultatenrekening: **klasse 72 Geproduceerde vaste activa**.

Boeking:
```
22-23 Vaste activa (actief ↑)    xxx
    aan 72 Geproduceerde vaste activa (opbrengst ↑)    xxx
```

Het netto-effect is nul op het resultaat op het moment van productie; de kostenspreiding verloopt via [[afschrijvingen|afschrijvingen]] over de levensduur van het actief.

> [!warning]- Geproduceerde vaste activa niet activeren vergroot de kost onterecht
> ❌ *"Als we de machine zelf bouwen, boeken we gewoon de loonkost en materiaalinkoop — dat is alles."*
>
> Wie de zelfgebouwde vaste activa **niet activeert**, laat de kosten (bezoldigingen, grondstoffen) volledig ten laste van het boekjaar vallen terwijl het actief jarenlang nut oplevert. Dat schendt het [[boekhoudkundige-beginselen#-matching-overeenstemming-van-kosten-en-opbrengsten|matchingbeginsel]]: de kost moet worden toegerekend aan de perioden van gebruik. Activeren en afschrijven is de correcte aanpak.
>
> 🤖 *AI-aanvulling*

---

## 📌 Andere bedrijfsopbrengsten (post I.D)

Bedrijfsverbonden opbrengsten die:
- **niet** hun oorsprong vinden in een verkoop of dienstverlening aan derden in het kader van de gewone bedrijfsuitoefening, en
- **niet** als niet-recurrente bedrijfsopbrengst of financiële opbrengst kunnen worden aangemerkt.

Voorbeelden ([[bronnen/wetteksten/XV-KB-wvv#art-390|KB WVV 2019 art. 3:90]]): exploitatiesubsidies, compenserende bedragen bij in- of uitvoer, meerwaarden bij de realisatie van handelsvorderingen.

---

## 📌 Bedrijfskosten

De bedrijfskosten zijn alle kosten die voortvloeien uit de gewone bedrijfsuitoefening. Ze vormen rubriek II van de resultatenrekening (volledig schema) en omvatten klasse 60–64 en 66 van het MAR.

| Post | Omschrijving | MAR |
|---|---|---|
| **II.A Handelsgoederen, grond- en hulpstoffen** | Aankopen van handelsgoederen, grondstoffen en hulpstoffen, na kortingen en aftrekbare btw | 60 |
| **II.B Diensten en diverse goederen** | Kosten voor dienstverlening of levering van goederen door derden | 61 |
| **II.C Bezoldigingen, sociale lasten en pensioenen** | Personeelskosten in de ruime zin | 62 |
| **II.D Afschrijvingen en waardeverminderingen op vaste activa** | Planmatige afschrijvingen op MVA en IVA en incidentele waardeverminderingen | 630/631 |
| **II.E Waardeverminderingen op voorraden en handelsvorderingen** | Toevoegingen (+) en terugnemingen (-) | 632/634 |
| **II.F Voorzieningen voor risico's en kosten** | Toevoegingen (+), bestedingen en terugnemingen (-) | 635/637 |
| **II.G Andere bedrijfskosten** | Overige bedrijfsverbonden kosten: belastingen als bedrijfskost (onroerende voorheffing), minderwaarden op handelsvorderingen | 640/641 |
| **II.I Niet-recurrente bedrijfskosten** | Kosten buiten de gewone bedrijfsuitoefening | 66 |

([[bronnen/wetteksten/XV-KB-wvv#art-390|ITAA-LEX XV (KB) · KB WVV 2019 art. 3:90]])

---

## 📌 Aankopen handelsgoederen, grond- en hulpstoffen (post II.A)

Na aftrek van in de handel toegestane kortingen en van de **aftrekbare btw**. Worden eveneens onder deze post geboekt: ingekochte diensten, werken en studies met een rechtstreekse invloed op de vervaardigingsprijs, algemene onderaannemingen en aankopen van onroerende goederen bestemd voor verkoop. ([[bronnen/wetteksten/XV-KB-wvv#art-390|KB WVV 2019 art. 3:90]])

Standaard aankoop handelsgoederen (btw aftrekbaar):

```
60  Aankopen handelsgoederen         1.000
411 Aftrekbare btw (21%)               210
        aan 44 Leveranciers                    1.210
```

---

## 📌 Diensten en diverse goederen (post II.B)

Kosten verbonden met dienstverlening of levering van goederen door derden in het kader van de bedrijfsuitoefening, tenzij die kosten onder rubriek II.A of II.C moeten worden geboekt. ([[bronnen/wetteksten/XV-KB-wvv#art-390|KB WVV 2019 art. 3:90]])

Hieronder vallen ook:
- Vergoedingen van uitzendkrachten en ter beschikking gestelde personen
- Bezoldigingen en pensioenen van **bestuurders, zaakvoerders en werkende vennoten** die **niet** uit hoofde van een arbeidsovereenkomst worden toegekend (→ niet in post II.C maar in II.B)

> [!warning]- Bezoldigingen van bestuurders zonder arbeidsovereenkomst horen in post II.B, niet in II.C
> ❌ *"Alle bezoldigingen van personen die werken voor de vennootschap, staan in post II.C Bezoldigingen."*
>
> Bezoldigingen en pensioenen van bestuurders, zaakvoerders en werkende vennoten die **geen arbeidsovereenkomst** hebben, staan in **post II.B Diensten en diverse goederen**. Post II.C is bestemd voor personeel onder arbeidsovereenkomst. Het onderscheid is relevant voor de loonmassa-analyse en voor de sociale balans. ([[bronnen/wetteksten/XV-KB-wvv#art-390|KB WVV 2019 art. 3:90]])
>
> 🤖 *AI-aanvulling*

---

## 📌 Bezoldigingen, sociale lasten en pensioenen (post II.C)

*Rémunérations, charges sociales et pensions*

De personeelskosten voor werknemers onder arbeidsovereenkomst. Post II.C (klasse 62 MAR) omvat alle componenten van de loonkost voor de werkgever.

**Componenten van de loonkost:**

| Component | Wie draagt het? | Boeking |
|---|---|---|
| Brutoloon | Werkgever (uitbetaald aan werknemer) | Debet 62 |
| RSZ-bijdrage werknemer | Werknemer (ingehouden door werkgever) | Credit 454 RSZ (vermindering op nettoloon) |
| RSZ-bijdrage werkgever | Werkgever (extra kost bovenop brutoloon) | Debet 62, credit 454 |
| Bedrijfsvoorheffing | Werknemer (ingehouden door werkgever), doorgestort aan FOD Financiën | Credit 453 BV |
| Nettoloon | Werknemer (wat effectief uitbetaald wordt) | Credit 455 Te betalen bezoldigingen |
| Vakantiegeld | Werkgever (gecumuleerd via voorziening of vakantiekas) | Debet 62, credit [[voorzieningen|621/635]] |
| Eindejaarspremie | Werkgever | Debet 62 |
| Voordelen alle aard (bv. bedrijfswagen, maaltijdcheques) | Werkgever | Debet 62 |

Boeking lonen bij uitbetaling:

```
62  Bezoldigingen (brutoloon + werkgeversbijdragen RSZ)   xxx
        aan 453 Bedrijfsvoorheffing (te storten aan FOD)         xxx
        aan 454 RSZ (te storten aan RSZ-instelling)               xxx
        aan 455 Nettolonen (te betalen aan werknemers)            xxx
```

Bij uitbetaling van het nettoloon:
```
455 Nettolonen                      xxx
        aan 55 Bank                               xxx
```

**Vakantiegeld bij afsluiting** — het vakantiegeld voor het lopende boekjaar dat pas in het volgende boekjaar wordt uitbetaald, wordt via een [[voorzieningen|voorziening]] (of overlopende rekening) toegerekend aan het boekjaar waarop het betrekking heeft, in toepassing van het [[boekhoudkundige-beginselen#-matching-overeenstemming-van-kosten-en-opbrengsten|matchingbeginsel]]. ([[bronnen/wetteksten/XV-KB-wvv#art-311|KB WVV 2019 art. 3:11]])

---

## 📌 Afschrijvingen en waardeverminderingen op vaste activa (post II.D)

Planmatige [[afschrijvingen|afschrijvingen]] op oprichtingskosten, immateriële en materiële vaste activa, én incidentele [[waardeverminderingen|waardeverminderingen]] op vaste activa — tenzij die wegens hun uitzonderlijk karakter als niet-recurrente bedrijfskost moeten worden geboekt (post II.I). ([[bronnen/wetteksten/XV-KB-wvv#art-390|KB WVV 2019 art. 3:90]])

Terugnemingen van afschrijvingen of waardeverminderingen worden **niet** onder post II.D geboekt maar onder de niet-recurrente bedrijfsopbrengsten (post I.E).

MAR-codes: 630 (afschrijvingen op oprichtingskosten en immateriële vaste activa), 631 (afschrijvingen op materiële vaste activa), 6320/6340 (waardeverminderingen).

---

## 📌 Waardeverminderingen op voorraden, bestellingen in uitvoering en handelsvorderingen (post II.E)

Toevoegingen (+) en terugnemingen (−) van [[waardeverminderingen|waardeverminderingen]] op de activa in de balansposten voorraden (rubriek V.A) en handelsvorderingen (rubriek VII.A). ([[bronnen/wetteksten/XV-KB-wvv#art-390|KB WVV 2019 art. 3:90]])

MAR-codes: 6321/6331 (voorraden), 6340/6350 (handelsvorderingen).

---

## 📌 Voorzieningen voor risico's en kosten (post II.F)

Toevoegingen (+) aan [[voorzieningen|voorzieningen]] voor **bedrijfsrisico's en -verplichtingen**, en bestedingen en terugnemingen (−) van eerder gevormde voorzieningen voor gewone bedrijfsrisico's. ([[bronnen/wetteksten/XV-KB-wvv#art-390|KB WVV 2019 art. 3:90]])

MAR-codes: 635/637.

---

## 📌 Andere bedrijfskosten (post II.G)

Bedrijfsverbonden kosten betaald aan derden die:
- niet hun oorsprong vinden in een dienstverlening of levering in het kader van de gewone bedrijfsuitoefening, en
- niet als financiële of niet-recurrente bedrijfskost kunnen worden aangemerkt.

In het bijzonder: **belastingen als bedrijfskost** (onroerende voorheffing, belasting op voertuigen, belasting op drijfkracht, accijnsrechten, uitvoerheffingen) en minderwaarden op handelsvorderingen (tenzij gelijk aan disconto). ([[bronnen/wetteksten/XV-KB-wvv#art-390|KB WVV 2019 art. 3:90]])

MAR-codes: 640 (bedrijfsbelastingen en -taksen), 641 (minderwaarden op realisatie van handelsvorderingen).

---

## 📌 Niet-recurrente bedrijfskosten (post II.I)

Kosten met een bedrijfskarakter maar **buiten de gewone bedrijfsuitoefening**. Zie [[financiele-en-uitzonderlijke-verrichtingen#-niet-recurrente-verrichtingen-klassen-66-en-76|Niet-recurrente verrichtingen]] voor een volledige behandeling.

Voorbeelden: niet-recurrente afschrijvingen en waardeverminderingen op vaste activa, voorzieningen voor niet-recurrente bedrijfsrisico's, minderwaarden bij realisatie van vaste activa, herstructureringskosten.

---

## ⚖️ Realisatieprincipe

Een **opbrengst** wordt geboekt wanneer ze **gerealiseerd** is — dat wil zeggen wanneer de prestatie is geleverd of de goederen zijn overgedragen en de tegenprestatie zeker is — niet wanneer de cash binnenkomt.

Een factuur die in december wordt opgesteld maar pas in januari geïnd, is een **opbrengst van december**: ze is gerealiseerd bij de levering. Het geld is pas een kasbeweging in januari. De ontvangen maar niet-gefactureerde prestatie einde boekjaar wordt via een [[overlopende-rekeningen#regularisatie-491-verkregen-opbrengsten-nog-te-factureren|overlopende rekening]] toegerekend.

---

## ⚖️ Matchingbeginsel

Kosten vallen in het boekjaar waarop ze **economisch betrekking hebben**, ongeacht wanneer de cash vloeit. Dit vereist bij jaarafsluiting: ([[bronnen/wetteksten/XV-KB-wvv#art-311|KB WVV 2019 art. 3:11]])

- **Toe te rekenen kosten** (kosten van dit boekjaar, nog niet gefactureerd) → [[overlopende-rekeningen#regularisatie-492-toe-te-rekenen-kosten-nog-te-ontvangen-factuur|overlopende rekening passief]]
- **Over te dragen kosten** (vooruitbetaald voor volgend boekjaar) → [[overlopende-rekeningen#regularisatie-490-over-te-dragen-kosten-vooruitbetaald|overlopende rekening actief]]
- **Vakantiegeld, eindejaarspremie**: kosten lopend boekjaar, uitbetaling volgend jaar → [[voorzieningen|voorziening]] of overlopende rekening

---

## ⚖️ Voorraadwijziging als correctie op aankoopkosten

Het mechanisme van voorraadwijziging maakt dat de resultatenrekening de **kostprijs van de verkochte goederen** weerspiegelt, niet de kostprijs van de **aangekochte** goederen.

```
Kostprijs verkochte goederen = Aankopen (II.A) + Beginvoorraad − Eindvoorraad
                              = Aankopen (II.A) − Voorraadwijziging (I.B)
```

Als een onderneming meer aankoopt dan verkoopt, stijgt de voorraad. Post I.B is dan positief → compenseert de te hoge aankoopkost → netto effect = enkel de verkochte goederen komen ten laste.

---

## 🔢 Brutomarge

```
Brutomarge = Omzet (I.A) + Voorraadwijziging (I.B) + Geproduceerde vaste activa (I.C)
           + Andere bedrijfsopbrengsten (I.D) − Aankopen (II.A) − Diensten en div. goederen (II.B)
```

In het verkort en microschema wordt dit als één post gepubliceerd: **I.A.B. Brutomarge (+/−)**. ([[bronnen/wetteksten/XV-KB-wvv#art-390|KB WVV 2019 art. 3:90]])

**Voorbeeld doorrekening:**

```
Netto-omzet (I.A)                          500.000
+ Toename voorraad gereed product (I.B)    +30.000
+ Andere bedrijfsopbrengsten (I.D)          +5.000
− Aankopen handelsgoederen (II.A)         -200.000
− Diensten en diverse goederen (II.B)      -80.000
─────────────────────────────────────────────────
= Brutomarge / Toegevoegde waarde           255.000   (51% van omzet)

− Bezoldigingen en soc. lasten (II.C)     -120.000
− Afschrijvingen MVA (II.D)                -30.000
− Waardeverminderingen vorderingen (II.E)   -5.000
− Andere bedrijfskosten (II.G)             -10.000
─────────────────────────────────────────────────
= Bedrijfsresultaat EBIT (9901)             90.000   (18% van omzet)
```

---

## 📋 Aankoop handelsgoederen — boeking

Aankoop van handelsgoederen van een btw-plichtige leverancier (btw 21%, volledig aftrekbaar):

```
Debet:
  60  Aankopen handelsgoederen        1.000
  411 Aftrekbare btw                    210

Credit:
  44  Leveranciers                    1.210
```

---

## 📋 Bezoldigingen — boeking

Maandelijkse loonverwerking (brutoloon € 3.000, RSZ-werknemer € 450, RSZ-werkgever € 700, BV € 480):

```
Debet:
  620 Bezoldigingen                   3.700   (brutoloon 3.000 + werkgever RSZ 700)

Credit:
  453 Bedrijfsvoorheffing               480   (te storten aan FOD Financiën)
  454 RSZ                             1.150   (450 werknemer + 700 werkgever)
  455 Nettolonen te betalen           2.070   (3.000 − 450 − 480)
```

Uitbetaling nettoloon:
```
Debet:
  455 Nettolonen te betalen           2.070

Credit:
  55  Bank                            2.070
```

---

## 📋 Voorraadwijziging — afsluitboeking

**Bij toename van de voorraad** (eindvoorraad > beginvoorraad, bv. +10.000):
```
30  Voorraad handelsgoederen         10.000
        aan 71 Voorraadwijziging                10.000
```
→ Klasse 71 heeft een credit-saldo → post I.B is positief → opbrengst

**Bij afname van de voorraad** (eindvoorraad < beginvoorraad, bv. −5.000):
```
71  Voorraadwijziging                 5.000
        aan 30 Voorraad handelsgoederen          5.000
```
→ Klasse 71 heeft een debet-saldo → post I.B is negatief → kost (extra aanspraak op voorraad)

> [!warning]- Vergeten de voorraadwijziging te boeken bij jaarafsluiting vertekent het resultaat
> ❌ *"We hebben dit jaar geen aankopen in de voorraad — de voorraadwijziging is nul."*
>
> De voorraadwijziging vergelijkt de **eindvoorraad** met de **beginvoorraad**. Als de eindvoorraad lager is dan de beginvoorraad — ook zonder nieuwe aankopen — is er een afname die als kost in de resultatenrekening thuishoort. Het vergeten van deze boeking overschat het resultaat (bij afname) of onderschat het (bij toename). Correcte inventarisatie aan het jaareinde is een vereiste voor een getrouwe resultatenrekening.
>
> 🤖 *AI-aanvulling*

---

## 📋 Geproduceerde vaste activa — boeking

Een onderneming bouwt met eigen personeel een installatie (loonkosten €8.000, grondstoffen €5.000 reeds geboekt in klasse 6):

```
23  Installaties, machines              13.000
        aan 72 Geproduceerde vaste activa       13.000
```

De kosten (62 en 60) zijn al geboekt. De tegenprestatie via klasse 72 neutraliseert ze in het resultaat. Daarna volgen [[afschrijvingen|afschrijvingen]] over de levensduur van de installatie.

---

## 🚩 Voorraadwijziging vergeten bij jaarafsluiting

Als de [[inventaris-en-jaarafsluiting#-jaarlijkse-inventaris|jaarlijkse inventaris]] aantoont dat voorraden zijn gedaald, maar de aanpassing wordt niet geboekt, staat de resultatenrekening onjuist:
- De aankoopkosten (II.A) zijn al geboekt
- Maar de voorraadafname compenseert geen aankoopkost → het resultaat is overschat

Herkenbaar in de analyse: de voorraadrubrieken op de balans wijzigen maar post I.B ontbreekt of is nul terwijl dat economisch onwaarschijnlijk is.

---

## 🚩 Geproduceerde vaste activa als kost laten staan

Wanneer een onderneming eigen vaste activa vervaardigt maar de activering vergeet (geen boeking op klasse 72), worden de gemaakte kosten integraal ten laste van het boekjaar genomen. Het gevolg:
- Resultaat van het bouwjaar is te laag
- Het actief staat niet op de balans → geen [[afschrijvingen|afschrijvingen]] in de volgende jaren
- Kosten worden niet gespreid over de economische levensduur → schending matchingbeginsel

Herkenbaar: substantiële loonkosten en grondstofaankopen terwijl geen overeenkomstige post I.C of kapitaalinvestering zichtbaar is op de balans.

---

> [!info]- In de praktijk: loonkost vs. nettoloon
>
> Een onderneming telt de lonen op en ziet dat het brutoloon voor alle werknemers samen €100.000 bedraagt. De effectieve kost voor de werkgever is echter hoger: de werkgeversbijdrage RSZ (ca. 25–27% in 2025) voegt nog eens €25.000–€27.000 bij. Post II.C van de resultatenrekening toont dus ca. €125.000–€127.000. Wat de werknemer netto ontvangt is nog lager: zijn RSZ-bijdrage (ca. 13,07%) en de bedrijfsvoorheffing worden van het brutoloon ingehouden.
>
> Bij de beoordeling van personeelskosten in een jaarrekening kijkt de analist naar het **totale bedrag van post II.C** als maatstaf voor de reële loonlast — niet naar de uitbetaalde nettolonen.
>
> ```
> Brutoloon per werknemer                        3.000
> + Werkgeversbijdrage RSZ (ca. 25%)              +750
> ────────────────────────────────────────────────────
> = Totale kost voor de werkgever (post II.C)    3.750
>
> Brutoloon                                      3.000
> − RSZ-bijdrage werknemer (13,07%)               -392
> − Bedrijfsvoorheffing (variabel, bv.)           -480
> ────────────────────────────────────────────────────
> = Nettoloon (uitbetaald aan werknemer)         2.128
> ```
>
> 🤖 *AI-aanvulling*

---

## Relevant voor

**[[1.1-algemene-boekhouding|1.1 Algemene boekhouding]]**

Taken:
- *Boekhoudkundige verwerking van courante verrichtingen*
  - Verwerking van lonen en bezoldigingen inclusief sociale lasten
  - Verwerking van aankopen, verkopen en voorraadwijzigingen
  - Activering van zelf geproduceerde vaste activa

Kenniselementen:
- II.M — [[bedrijfsresultaat-kosten-opbrengsten#-bedrijfskosten|Bedrijfskosten incl. bezoldigingen van het personeel]]
- II.N — [[bedrijfsresultaat-kosten-opbrengsten#-bedrijfsopbrengsten|Bedrijfsopbrengsten]]

### Voorbeeldvragen

> [!question]- Voorraadtoename: opbrengst of kost?
>
> Een handelsvennootschap koopt in 2025 voor €200.000 aan handelsgoederen en verkoopt voor €280.000. De eindvoorraad stijgt met €30.000 ten opzichte van de beginvoorraad.
>
> Welk bedrag staat in post II.A (Aankopen) en welk bedrag in post I.B (Voorraadwijziging)?
>
> > [!success]- Antwoord
> >
> > **Post II.A: €200.000 (kost). Post I.B: +€30.000 (opbrengst, positief saldo).**
> >
> > De aankopen worden integraal geboekt in II.A. De toename van de voorraad (+€30.000) wordt aan de opbrengstenzijde geboekt als post I.B — een positief bedrag dat de aankoopkost gedeeltelijk neutraliseert. Netto effect op het resultaat vanuit aankopen en voorraad: −€200.000 + €30.000 = −€170.000 (kostprijs verkochte goederen).
> >
> > *Zie: [[bedrijfsresultaat-kosten-opbrengsten#-voorraadwijziging-in-goederen-in-bewerking-en-gereed-product-post-ib|Voorraadwijziging]]* en *[[bedrijfsresultaat-kosten-opbrengsten#-brutomarge|Brutomarge]]*
>
> 🤖 *AI-aanvulling*

> [!question]- Bestuurdersbezoldiging: post II.B of II.C?
>
> Een zaakvoerder van een bv ontvangt maandelijks €5.000 vergoeding. Hij heeft geen arbeidsovereenkomst met de vennootschap.
>
> Onder welke post van de resultatenrekening valt deze vergoeding?
>
> > [!success]- Antwoord
> >
> > **Post II.B Diensten en diverse goederen.**
> >
> > Bezoldigingen en pensioenen van bestuurders, zaakvoerders en werkende vennoten die niet worden toegekend uit hoofde van een arbeidsovereenkomst, vallen onder post II.B — niet onder II.C Bezoldigingen. Post II.C is bestemd voor personeel onder arbeidsovereenkomst. ([[bronnen/wetteksten/XV-KB-wvv#art-390|KB WVV 2019 art. 3:90]])
> >
> > *Zie: [[bedrijfsresultaat-kosten-opbrengsten#-diensten-en-diverse-goederen-post-iib|Diensten en diverse goederen]]*
>
> 🤖 *AI-aanvulling*

> [!question]- Terugneming afschrijving: welke post?
>
> Een vennootschap herzieft haar afschrijvingsplan en stelt vast dat een afschrijving die in 2022 geboekt werd, te hoog was. Ze neemt een deel terug in 2025.
>
> Op welke post van de resultatenrekening wordt deze terugneming geboekt?
>
> > [!success]- Antwoord
> >
> > **Post I.E Niet-recurrente bedrijfsopbrengsten.**
> >
> > Terugnemingen van afschrijvingen of waardeverminderingen worden **niet** geboekt onder post II.D (Afschrijvingen) maar onder de niet-recurrente bedrijfsopbrengsten (post I.E in het volledig schema). ([[bronnen/wetteksten/XV-KB-wvv#art-390|KB WVV 2019 art. 3:90]])
> >
> > *Zie: [[bedrijfsresultaat-kosten-opbrengsten#-afschrijvingen-en-waardeverminderingen-op-vaste-activa-post-iid|Post II.D]]*
>
> 🤖 *AI-aanvulling*
