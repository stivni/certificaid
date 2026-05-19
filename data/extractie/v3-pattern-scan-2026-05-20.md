# v3 pattern-scan voorbeeldexamens

Datum: 2026-05-20
PDFs gescand: 8

## Overzicht — counts per PDF per patroon

| Patroon | 2003-bibf | 2008-bibf | 2013-1 | 2013-2 | 2014-1 | 2015-1 | 2024-1 | 2025-1 | totaal |
|---|---|---|---|---|---|---|---|---|---|
| _pdfplumber_tabellen | 1 | 7 | 39 | 58 | 41 | 56 | 0 | 0 | 202 |
| aanpassing | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| balans_rubrieken_actief | 7 | 4 | 7 | 16 | 8 | 9 | 0 | 0 | 51 |
| balans_rubrieken_passief | 13 | 8 | 28 | 18 | 76 | 33 | 3 | 3 | 182 |
| berekening_in_optie | 0 | 0 | 0 | 0 | 2 | 4 | 0 | 0 | 6 |
| bijlage_verwijzing | 0 | 1 | 3 | 3 | 1 | 2 | 0 | 0 | 10 |
| casus_intro_zin | 1 | 0 | 9 | 1 | 8 | 5 | 0 | 0 | 24 |
| inventaris_bullet | 9 | 0 | 2 | 5 | 0 | 0 | 0 | 0 | 16 |
| marktwaarde | 1 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 3 |
| mc_optie | 12 | 20 | 70 | 79 | 53 | 210 | 109 | 109 | 662 |
| proef_saldibalans_regel | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| punten_lowercase | 0 | 0 | 37 | 123 | 47 | 108 | 0 | 0 | 315 |
| punten_uppercase | 40 | 0 | 12 | 12 | 13 | 13 | 0 | 0 | 90 |
| rr_rubrieken | 4 | 7 | 3 | 4 | 13 | 7 | 8 | 8 | 54 |
| subvraag_marker | 2 | 12 | 70 | 79 | 53 | 60 | 0 | 0 | 276 |
| vraag_instructie | 8 | 26 | 33 | 46 | 40 | 45 | 9 | 9 | 216 |
| vraag_prefix | 0 | 0 | 37 | 38 | 46 | 61 | 0 | 0 | 182 |

## Voorbeelden per patroon (max 3 per PDF)

### aanpassing

Regex: `(afgeprijsd|afprijzing|opwaardering|waardevermindering|herwaardering)(?:[^.]{0,120}?bedrag(?:en)?\s+van)?\s*([\d\.]+,\d{2})`

**2003-bibf** (1 voorkomens)

- `lde goederen moeten afgeprijsd worden voor een totaal bedrag van 75,00 euro. Vraag : geef de afsluit`

### balans_rubrieken_actief

Regex: `\b(?:Vaste\s+activa|Vlottende\s+activa|Voorraden|Liquide\s+middelen|Materiële\s+vaste\s+activa)\b`

**2003-bibf** (7 voorkomens)

- `: … 4 PUNTEN ACTIVA Vaste activa 150.040,00 Vlottende activa V`
- `e activa 150.040,00 Vlottende activa Voorraden 41.000,00 Vordering`
- `00 Vlottende activa Voorraden 41.000,00 Vorderingen op -1 j`

**2008-bibf** (4 voorkomens)

- `PSD|66343307 A.3 De voorraden bedragen op 1 januari N: 12.0`
- `2 Afschrijvingen op materiële vaste activa 3.683,33 2009 Aan Afschrijvin`
- `financiële beperkte vlottende activa en, anderzijds, de niet finan`

**2013-1** (7 voorkomens)

- `2012 2011 2012 2011 Materiële vaste activa 105.000 100.000 Kapitaal 65.0`
- `erves 15.000 15.000 Liquide middelen 25.000 30.000 Overgedragen 5.`
- `ar investeringen in materiële vaste activa werden gedaan voor 451 692,38`

**2013-2** (16 voorkomens)

- `bij de immateriële vaste activa op te nemen? b) Aankoop van b`
- `nemen in de rubriek materiële vaste activa? Kan zij dit opnemen in de ru`
- `rubriek immateriële vaste activa? c) Zij koopt software X aan,`

**2014-1** (8 voorkomens)

- `ar investeringen in materiële vaste activa werden gedaan voor 361 869,98`
- `/12/2013 31/12/2012 Materiële vaste activa 450.000,00 455.000,00 Kapitaa`
- `45.000,00 43.000,00 Liquide middelen 80.000,00 45.000,00 640.000,0`

**2015-1** (9 voorkomens)

- `ar investeringen in materiële vaste activa werden gedaan voor 452 835 EU`
- `punten Code Ja Neen Materiële vaste activa 22/27 Financiële vaste activa`
- `va 22/27 Financiële vaste activa 28 Vorderingen op meer dan éé`

### balans_rubrieken_passief

Regex: `\b(?:Eigen\s+vermogen|Kapitaal|Schulden|Voorzieningen|Reserves|Overgedragen)\b`

**2003-bibf** (13 voorkomens)

- `281.240,00 PASSIVA Kapitaal 100.000,00 Reserves 50.400,00`
- `Kapitaal 100.000,00 Reserves 50.400,00 Overgedragen winst`
- `Reserves 50.400,00 Overgedragen winst 2.750,00 Schulden op +`

**2008-bibf** (8 voorkomens)

- `= 19.176,00 EUR 623 Voorzieningen vakantiegeld 19.176,00 456 Aa`
- `de niet financiële schulden op ten hoogste één jaar. (3 +`
- `aste reserve in het kapitaal geïncorporeerd in 2000 voor e`

**2013-1** (28 voorkomens)

- `iva 105.000 100.000 Kapitaal 65.000 65.000 Vorderingen < j`
- `jaar 45.000 40.000 Reserves 15.000 15.000 Liquide middele`
- `delen 25.000 30.000 Overgedragen 5.000 10.000 resultaat Schuld`

**2013-2** (18 voorkomens)

- `2.000,00 Geplaatst kapitaal 20.000,00 Materiële vaste act`
- `,00 Niet opgevraagd kapitaal -12.000,00 Goederenvoorraad 3`
- `envoorraad 3.500,00 Overgedragen resultaat 1.000,00 Liquide mi`

**2014-1** (76 voorkomens)

- `het vastklikken van reserves. Op 20 december 2013 heeft ee`
- `een gedeelte van de reserves uit te keren. Het gaat om een`
- `een opname van deze reserves in kapitaal voor een bedrag v`

**2015-1** (33 voorkomens)

- `en op rekening 753 “Kapitaal- en interestsubsidies”. B. El`
- `en op rekening 753 “Kapitaal- en interestsubsidies”. D. De`
- `ntabiliteit van het eigen vermogen na belastingen A. 968 829 x 1`

**2024-1** (3 voorkomens)

- `n het niet volstort kapitaal. Liquidatietest nodig? B. Qua`
- `khouding van A = 20 Overgedragen fiscale verliezen van B = 30`
- `kort model NBB voor kapitaal vennootschap wordt EV als vol`

**2025-1** (3 voorkomens)

- `n het niet volstort kapitaal. Liquidatietest nodig? B. Qua`
- `khouding van A = 20 Overgedragen fiscale verliezen van B = 30`
- `kort model NBB voor kapitaal vennootschap wordt EV als vol`

### berekening_in_optie

Regex: `[(\[][\d\.\,\s\+\-\*/x×]+[)\]]\s*[=×x]\s*[\d\.,]+`

**2014-1** (2 voorkomens)

- `548 415 + 2 704) : (1 210 536 + 39 932) = 6,29  (1 739 806 + 2 200 000 + 2`
- `548 415 + 2 704) : (1 210 536 + 39 932) = 5,19 Downloaded by Stijn Vannieuwe`

**2015-1** (4 voorkomens)

- `rutoverkoopmarge A. (1 479 283 + 425 554 + 804) x 100 / (8 034 747 + 344 153) = 22,`
- `554 + 804) x 100 / (8 034 747 + 344 153) = 22,74 B. (1 417 747 + 425 554 + 804`
- `344 153) = 22,74 B. (1 417 747 + 425 554 + 804) x 100 / (8 365 788 - 1 600 244) = 2`

### bijlage_verwijzing

Regex: `(in\s+bijlage|als\s+bijlage|zie\s+bijlage|bijlage(?:n)?\s+\d|bijgevoegd)`

**2008-bibf** (1 voorkomens)

- `elde gegevens en de bijgevoegde jaarrekening. Het betreft de`

**2013-1** (3 voorkomens)

- `raag 1 … / 9 punten In bijlage vindt u de balans na winstver`
- `Antwoord b) Vul de bijgevoegde onderdelen van de aangifte i`
- `en modelaangifte is in bijlage toegevoegd. U mag er van uit`

**2013-2** (3 voorkomens)

- `raag 1 … / 6 punten In bijlage vindt u de balans na winstver`
- `saldi balans zoals in bijlage? Verklaar uw antwoord. Antwoo`
- `es van het ACTIEF) (in bijlage de afschrijvingstabel, detail`

**2014-1** (1 voorkomens)

- `raag 1 … / 8 punten In bijlage vindt U de balans na winstver`

**2015-1** (2 voorkomens)

- `raag 1 … / 8 punten In bijlage vindt U de balans na winstver`
- `teformulier vindt u in bijlage)? Zijn er nog andere verplich`

### casus_intro_zin

Regex: `(?:^|\n)(?:De\s+vennootschap|De\s+NV|De\s+BV|De\s+BVBA|De\s+CV|NV\s+[A-Z]|BV\s+[A-Z]|BVBA\s+[A-Z]|CV\s+[A-Z]|De\s+heer|Mevrouw)\s+[A-Z]`

**2003-bibf** (1 voorkomens)

- `PUNTEN G.1 Situatie: De BVBA Albert legt volgende balans, af`

**2013-1** (9 voorkomens)

- `raag 1 … / 12 punten De heer André, een loodgieter van 58 ja`
- `30.367 2007 € 21.784 De heer André had een gespecialiseerde`
- `van € 117.500 (10%). De heer André heeft netto dus € 1.057.5`

**2013-2** (1 voorkomens)

- `raag 2 … / 10 punten De vennootschap GOODLUCK heeft een deel van haa`

**2014-1** (8 voorkomens)

- `Vraag 4 … / 4 punten De heer KALO Ric gedelegeerd bestuurder`
- `ouder, raadpleegt u. De heer KALO Ric heeft een aanzienlijk`
- `Vraag 5 … / 4 punten De heer LEGRAND Alexandre is samen met`

**2015-1** (5 voorkomens)

- `Vraag 1 … / 4 punten De heer DUPONT, zaakvoerder en hoofdaan`
- `Vraag 5 … / 4 punten De heer POULAIN, enig vennoot, zaakvoer`
- `Vraag 1 … / 8 punten De vennootschap ABC heeft een beleggingsportefe`

### inventaris_bullet

Regex: `(?:^|\s)[-•]\s+([A-Za-zéèêëàâäôöûüçïî][\wéèêëàâäôöûüçïî\s\-/&\.,()'\"]{2,80}?)\s+([\d\.]+,\d{2})`

**2003-bibf** (9 voorkomens)

- `einde boekjaar geeft - goederen in bewerking 400,00 - handelsgoederen 8.500,00 De`
- `in bewerking 400,00 - handelsgoederen 8.500,00 De marktprijs van de handelsg`
- `tatenrekening 1 PUNT - winst van het boekjaar 2.750,00 - afschrijvingen 12.100,00 -`

**2013-1** (2 voorkomens)

- `uitgaven, te weten: - Schilderwerken (om de 10 jaar) waarvan de kostprijs 8 900,00 euro (excl. btw) bedraagt; Do`
- `lOMoARcPSD|66343307 - Uitbreiding van de garage voor de vrachtwagens, waarvan de kostprijs 18 000,00 euro (exclusief btw) bedraagt`

**2013-2** (5 voorkomens)

- `en uitrusting 230000 - Installaties 32.000,00 230900 - Afschrijving install`
- `ies 32.000,00 230900 - Afschrijving installaties Financiële vaste activa 280000 - Aandelen O'Cool 30.000,00 Vlottende activa Vorderingen`
- `lsvorderingen 400000 - Handelsdebiteuren 215.100,00 Overige vorderingen 411000 -`

### marktwaarde

Regex: `(?:marktprijs|marktwaarde|reële\s+waarde)(?:\s+van[^.]{0,80}?)?\s+(?:bedraagt|is|=)?\s*([\d\.]+,\d{2})\s*(?:EUR|euro)?`

**2003-bibf** (1 voorkomens)

- `oederen 8.500,00 De marktprijs van de handelsgoederen bedraagt 8.250,00 euro. Er werd ook vastgesteld dat`

**2015-1** (2 voorkomens)

- `cember 2013 nog een marktwaarde van 280,00 EUR per artikel. Per 30 april 201`
- `30 april 2014 is de marktwaarde 300,00 EUR. De algemene vergadering van`

### mc_optie

Regex: `^\s*([A-D]|[a-d])[.)]\s+(.{2,200})$`

**2003-bibf** (12 voorkomens)

- `EKHOUDING 35 PUNTEN A. ALGEMENE BOEKHOUDING 10 PUNTEN A.1. Kapitaalsubsidies. Gedur`
- `boekingen. 5 PUNTEN B. WETGEVING OP DE BOEKHOUDING EN DE JAARREKENING VAN DE ONDERNEMING + OPSTELLEN, ANALYSE EN KRITISC`
- `7 mei 2003 – vragen C. ALGEMENE BEGINSELEN VAN HET FINANCIEEL BEHEER 5 PUNTEN C.1. Op de balans staan volge`

**2008-bibf** (20 voorkomens)

- `IN BOEKHOUDING …/40 A. ALGEMENE BOEKHOUDING …/15 A.1 In 2007 bedragen de bruto`
- `maximum vijf jaar. B. WETGEVING OP DE BOEKHOUDING EN DE JAARREKENING VAN DE ONDERNEMING + OPSTELLEN, ANAL`
- `aan het seminarie. C. ALGEMENE BEGINSELEN VAN HET FINANCIEEL BEHEER …/5 C.1 Wat verstaat men met “beh`

**2013-1** (70 voorkomens)

- `dragen winst 5.000 a) Dient deze vennootschap haar waarderingsregels te verantwoorden in haar jaarverslag, en indien zij ge`
- `jaar 2012? Antwoord b) Motiveer uw antwoord. Antwoord Downloaded by Stijn`
- `ord aan te kruisen. a) Onderneming A heeft een openstaande leveranciersschuld ten opzichte van onderneming X voor een bedrag`

**2013-2** (79 voorkomens)

- `uiste antwoord aan. a) Aankoop van 10 laptops met software Windows 8 Antwoord … / 1 punt Dient zij`
- `activa op te nemen? b) Aankoop van boekhoudsoftware bij firma XYZ. Antwoord … / 1 punt Kan zij d`
- `riële vaste activa? c) Zij koopt software X aan, die zij zonder enige wijziging doorverkoopt aan haar klanten Antwoord … / 1 punt Te verwer`

**2014-1** (53 voorkomens)

- `tegen 100.000 EUR. a) Wat gebeurt er met de in 1980 geboekte herwaarderingsmeerwaarde? Antwoord  de meerwaarde word`
- `taat genomen worden b) Welke zijn de mogelijke bestemmingen van deze herwaarderingsmeerwaarde? Antwoord Downloaded by Stijn`
- `ng naar de reserves c) Wat is het bedrag van de herwaarderingsmeerwaarde dat naar de reserves mag worden overgeboekt? Antwoord`

**2015-1** (210 voorkomens)

- `aats op 5 mei 2014. a) Voor welke waarde neemt zij dit artikel op in haar voorraad per 31 december 2013? A. 465.000 EUR B. 470.000 EUR`
- `r 31 december 2013? A. 465.000 EUR B. 470.000 EUR C. 392.000 EUR`
- `013? A. 465.000 EUR B. 470.000 EUR C. 392.000 EUR D. 420.000 EUR`

**2024-1** (109 voorkomens)

- `Vennootschapsrecht A. BVBA naar BV volgens nieuw WVV. Aandeelhouder vrij van volstorting van het niet volstort kapitaal. Liquidatie`
- `quidatietest nodig? B. Quasi inbreng in NV. Wie kan dit doen? C. Vennootschap verliest rech`
- `. Wie kan dit doen? C. Vennootschap verliest rechtspersoonlijkheid: A. a. Bij ontbinding B. b. Bi`

**2025-1** (109 voorkomens)

- `Vennootschapsrecht A. BVBA naar BV volgens nieuw WVV. Aandeelhouder vrij van volstorting van het niet volstort kapitaal. Liquidatie`
- `quidatietest nodig? B. Quasi inbreng in NV. Wie kan dit doen? C. Vennootschap verliest rech`
- `. Wie kan dit doen? C. Vennootschap verliest rechtspersoonlijkheid: A. a. Bij ontbinding B. b. Bi`

### proef_saldibalans_regel

Regex: `\b(\d{2,6})\s+([A-ZÉÈÊËÀÂÄÔÖÛÜÇÏÎ][\wéèêëàâäôöûüçïî\s\-/&\.,()'\"]{2,80}?)\s+([DC])\s+([\d\.]+,\d{2})(?:\s*(?:EUR|euro))?`

**2003-bibf** (2 voorkomens)

- `volgende bedragen: 32 Goederen in bewerking D 500,00 euro 34 Handelsgoederen D 7.000,00`
- `rking D 500,00 euro 34 Handelsgoederen D 7.000,00 euro De inventaris per einde boekj`

### punten_lowercase

Regex: `/\s*([\d,]+)\s*punt(?:en)?`

**2013-1** (37 voorkomens)

- `15 PUNTEN Vraag 1 … / 4 punten De besloten vennootschap met`
- `|66343307 Vraag 2 … / 6 punten Gelieve voor de onderstaande`
- `|66343307 Vraag 3 … / 5 punten Een onderneming heeft een nie`

**2013-2** (123 voorkomens)

- `15 PUNTEN Vraag 1 … / 3 punten Onderneming “Softy” BVBA is é`
- `indows 8 Antwoord … / 1 punt Dient zij de Windows software`
- `rma XYZ. Antwoord … / 1 punt Kan zij dit opnemen in de rub`

**2014-1** (47 voorkomens)

- `15 PUNTEN Vraag 1 … / 2 punten Vennootschap PETRUS BVBA slui`
- `.000 EUR. Vraag 2 … / 2 punten Downloaded by Stijn Vannieuwe`
- `passief. Vraag 3 … / 8 punten Vennootschap Immo-C had in 19`

**2015-1** (108 voorkomens)

- `2 2 2 2 2 Vraag 1 … / 3 punten Een onderneming XYZ verkoopt`
- `7.000 EUR Vraag 2 … / 2 punten Een werknemer, de heer Jansse`
- `ggenomen. Vraag 3 … / 2 punten Een vennootschap XYZ heeft ee`

### punten_uppercase

Regex: `\b(\d{1,3})\s+PUNTEN\b`

**2003-bibf** (40 voorkomens)

- `LDOMEIN BOEKHOUDING 35 PUNTEN A. ALGEMENE BOEKHOUDING 10 PU`
- `LGEMENE BOEKHOUDING 10 PUNTEN A.1. Kapitaalsubsidies. Gedur`
- `jaren 2002 en 2003. 5 PUNTEN Op de proef- en saldibalans s`

**2013-1** (12 voorkomens)

- `AKE DE JAARREKENING 15 PUNTEN Vraag 1 … / 4 punten De beslo`
- `BEOORDELING VAN DE 25 PUNTEN JAARREKENING - CONSOLIDATIE V`
- `CCOUNTANTSONDERZOEK 50 PUNTEN Vraag 1 … / 4 punten De inter`

**2013-2** (12 voorkomens)

- `AKE DE JAARREKENING 15 PUNTEN Vraag 1 … / 3 punten Ondernem`
- `twoord … / 2 punten 25 PUNTEN ANALYSE EN KRITISCHE BEOORDEL`
- `CCOUNTANTSONDERZOEK 50 PUNTEN Vraag 1 … / 8 punten Een audi`

**2014-1** (13 voorkomens)

- `AKE DE JAARREKENING 15 PUNTEN Vraag 1 … / 2 punten Vennoots`
- `BEOORDELING VAN DE 25 PUNTEN JAARREKENING - CONSOLIDATIE V`
- `07 INTERNE CONTROLE 25 PUNTEN Vraag 1 … / 10 punten Duid me`

**2015-1** (13 voorkomens)

- `AKE DE JAARREKENING 15 PUNTEN Plaats de letter van het juis`
- `BEOORDELING VAN DE 25 PUNTEN JAARREKENING - CONSOLIDATIE B`
- `en INTERNE CONTROLE 25 PUNTEN Vraag 1 … / 12 punten De cont`

### rr_rubrieken

Regex: `\b(?:Omzet|Bedrijfsopbrengsten|Bedrijfskosten|Te\s+bestemmen\s+winst|Afschrijvingen|Financiële\s+opbrengsten|Financiële\s+kosten)\b`

**2003-bibf** (4 voorkomens)

- `boekjaar 2.750,00 - afschrijvingen 12.100,00 - toevoegingen aan`
- `bare reserve 16.000 Te bestemmen winst van het boekj 62.000 Schulden`
- `Autokosten 1.500 63 Afschrijvingen auto 3.800 61 Representatieko`

**2008-bibf** (7 voorkomens)

- `richtingen. Boek de afschrijvingen. Antwoord: 200 Oprichtingskos`
- `RcPSD|66343307 6300 Afschrijvingen op oprichtingskosten 200,00 6`
- `skosten 200,00 6302 Afschrijvingen op materiële vaste activa 3.6`

**2013-1** (3 voorkomens)

- `rwerking Jaar 2011: Te bestemmen winst van het boekjaar 15.000 Overg`
- `en ontvangen; 4. De te bestemmen winst van het boekjaar integraal ge`
- `aan 84 750,00 euro: Omzet 1 775,00/stuk x 250 stuks = 4`

**2013-2** (4 voorkomens)

- `ge boekjaren; 6) De te bestemmen winst van het boekjaar integraal ge`
- `voor belastingen en financiële kosten (%) Antwoord … / 2 punten c)`
- `ur gebouwen -25.000 Omzet 256.000 Afschrijvingen -5.000`

**2014-1** (13 voorkomens)

- `meerwaarde geboekte afschrijvingen, ofwel inlijving in het kapit`
- `meerwaarde geboekte afschrijvingen, ofwel, bij latere minderwaar`
- `bedrag zult u in de omzet opnemen (boeking op 5 februar`

**2015-1** (7 voorkomens)

- `an 1 665 EUR; 7. De te bestemmen winst van het boekjaar integraal ge`
- `ige 250,00 goederen bedrijfsopbrengsten Lonen 0,00 Afschrijvingen 250`
- `rengsten Lonen 0,00 Afschrijvingen 250,00 Overige bedrijfskosten`

**2024-1** (8 voorkomens)

- `epaald op basis van omzet van de 2 laatste jaren D. d.`
- `fout a. Degressieve afschrijvingen zijn toegestaan b. Kosten voo`
- `ten) a. Elektricien omzet 10.000 b. Kapper omzet 15.000`

**2025-1** (8 voorkomens)

- `epaald op basis van omzet van de 2 laatste jaren D. d.`
- `fout a. Degressieve afschrijvingen zijn toegestaan b. Kosten voo`
- `ten) a. Elektricien omzet 10.000 b. Kapper omzet 15.000`

### subvraag_marker

Regex: `^\s*([a-d])\)\s+`

**2003-bibf** (2 voorkomens)

- `ijkomende Gegevens: a) De opbrengsten bevatten de inn`
- `voorheffing 400 €. b) In de kosten noteert men: reke`

**2008-bibf** (12 voorkomens)

- `elastbaar tijdperk? a) Een uitgave in 2006 met betrek`
- `bare winst van 2007 b) Een tantième dat op 15.04.2008`
- `tbaar tijdperk 2007 c) Wanneer ingevolge een geschil`

**2013-1** (70 voorkomens)

- `dragen winst 5.000 a) Dient deze vennootschap haar w`
- `jaar 2012? Antwoord b) Motiveer uw antwoord. Antwoord`
- `ord aan te kruisen. a) Onderneming A heeft een openst`

**2013-2** (79 voorkomens)

- `uiste antwoord aan. a) Aankoop van 10 laptops met sof`
- `activa op te nemen? b) Aankoop van boekhoudsoftware b`
- `riële vaste activa? c) Zij koopt software X aan, die`

**2014-1** (53 voorkomens)

- `tegen 100.000 EUR. a) Wat gebeurt er met de in 1980`
- `taat genomen worden b) Welke zijn de mogelijke bestem`
- `ng naar de reserves c) Wat is het bedrag van de herwa`

**2015-1** (60 voorkomens)

- `aats op 5 mei 2014. a) Voor welke waarde neemt zij di`
- `EUR E. 452.000 EUR b) Welke waarde gaat zij weerhoud`
- `oord Punten 2 2 2 2 a) Brutoverkoopmarge A. (1 479 28`

### vraag_instructie

Regex: `\b(Geef|Bereken|Bepaal|Motiveer|Verklaar|Beschrijf|Leg\s+uit|Schrijf|Boek|Maak|Stel\s+op|Vermeld|Noem|Welke|Wat\s+is|Hoe)\b`

**2003-bibf** (8 voorkomens)

- `PUNTEN B.1. Vraag: Welke ondernemingen mogen een veree`
- `PUNTEN B.3. Vraag: Welke activa mogen geherwaardeerd w`
- `PUNTEN B.5. Vraag: Welke meldingen moeten in de toelic`

**2008-bibf** (26 voorkomens)

- `eindejaarspremies. Boek het vakantiegeld verschuldigd`
- `EUR handelsgoederen Boek de voorraadwijzigingen. Antwo`
- `duur van vijf jaar. Boek beide verrichtingen. Boek de`

**2013-1** (33 voorkomens)

- `r 2012? Antwoord b) Motiveer uw antwoord. Antwoord Downloa`
- `ng voor activering? Motiveer uw antwoord. Antwoord b) Zo j`
- `ing van een cliënt. Bereken de gevraagde ratio’s telkens`

**2013-2** (46 voorkomens)

- `d … / 3 punten Ja / Verklaar uw keuze met verwijzing naar`
- `ing van een cliënt. Bereken de gevraagde ratio’s telkens`
- `itaal kan verhogen. Geef drie voorbeelden. Antwoord Vr`

**2014-1** (40 voorkomens)

- `edragen winst 1.000 Hoe zal de jaarrekening per 31 de`
- `oreerd in kapitaal. Hoe dient zij de kapitaalverhogin`
- `t genomen worden b) Welke zijn de mogelijke bestemminge`

**2015-1** (45 voorkomens)

- `R E. 452.000 EUR b) Welke waarde gaat zij weerhouden op`
- `UR bruto per maand. Hoe wordt dit stelsel werklooshei`
- `diet 15-237584-22”. Welke van onderstaande instructies`

**2024-1** (9 voorkomens)

- `de verkoopcyclus B. Wat is de hoofddoelstelling van de i`
- `0 euro per kwartaal Welke bedragen waar opnemen in de a`
- `in de aangifte? D. Welke beroepsinkomsten zijn niet aa`

**2025-1** (9 voorkomens)

- `de verkoopcyclus B. Wat is de hoofddoelstelling van de i`
- `0 euro per kwartaal Welke bedragen waar opnemen in de a`
- `in de aangifte? D. Welke beroepsinkomsten zijn niet aa`

### vraag_prefix

Regex: `\bVraag\s*[:.]?\s*(\d+|[A-Z](?:\.\d+)?)\b`

**2013-1** (37 voorkomens)

- `RREKENING 15 PUNTEN Vraag 1 … / 4 punten De besloten venn`
- `lOMoARcPSD|66343307 Vraag 2 … / 6 punten Gelieve voor de`
- `lOMoARcPSD|66343307 Vraag 3 … / 5 punten Een onderneming`

**2013-2** (38 voorkomens)

- `RREKENING 15 PUNTEN Vraag 1 … / 3 punten Onderneming “Sof`
- `riële vaste activa? Vraag 2 … / 4 punten Gelieve voor de`
- `n en het resultaat. Vraag 3 … / 4 punten Vennootschap “ F`

**2014-1** (46 voorkomens)

- `RREKENING 15 PUNTEN Vraag 1 … / 2 punten Vennootschap PET`
- `ag van 900.000 EUR. Vraag 2 … / 2 punten Downloaded by St`
- `an op haar passief. Vraag 3 … / 8 punten Vennootschap Imm`

**2015-1** (61 voorkomens)

- `1,5 1,5 2 2 2 2 2 2 Vraag 1 … / 3 punten Een onderneming`
- `EUR E. 637.000 EUR Vraag 2 … / 2 punten Een werknemer, d`
- `ening teruggenomen. Vraag 3 … / 2 punten Een vennootschap`

## Pagina-/karakter-statistiek

| PDF | n_pages | n_chars | pdfplumber-tabellen |
|---|---|---|---|
| 2003-bibf | 8 | 16335 | 1 |
| 2008-bibf | 23 | 37932 | 7 |
| 2013-1 | 25 | 42615 | 39 |
| 2013-2 | 26 | 40812 | 58 |
| 2014-1 | 31 | 55884 | 41 |
| 2015-1 | 37 | 66592 | 56 |
| 2024-1 | 6 | 9253 | 0 |
| 2025-1 | 6 | 9253 | 0 |
