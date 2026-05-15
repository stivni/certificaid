# Mens-calibratie: 20 random needs-rework adviezen

Voor elke bron: rationale + 5 voorbeelden van problemen + 8 regels uit body.
Markeer per bron: A = acceptabel voor RAG | F = echte fix nodig | S = source-issue

## 1. CBN-0137-04-renteloze-vorderingen-schulden-en-vorderingen-schulden-met-een-abnormaal-lage-rente-op.md

**Rationale**: B5 op L95: derde subsectie 'Renteloze vordering of vordering met een abnormaal lage rente, terugbetaalbaar anders dan op vaste termijn...' staat als plain tekst terwijl de twee andere subsecties (L86, L91) wél als ### headings zijn opgemaakt. D2 op L163-189: het voorbeeldgedeelte bevat berekenings- 

**Concrete problemen** (max 3):
  - `B5` (other): Renteloze vordering of vordering met een abnormaal lage rente, terugbetaalbaar a
  - `C3` (pseudo-table): 20 000 op 31 december 1986 30 000 op 31 december 1987 50 000 op 31 december 1988
  - `D2` (missing-section): ### Actuele waarde van de kasstromen — sectie heeft geen tabelinhoud, alleen (1)

**Body sample** (eerste 8 niet-blanke regels):
  # CBN-advies 137/4 - Renteloze vorderingen (schulden) en vorderingen (schulden) met een abnormaal la
  Overeenkomstig artikel 27*bis*, § 2, eerste lid,* litt*. c) van het koninklijk besluit van 8 oktober
  Artikel 27*bis*, § 4, stelt dat deze bepaling op overeenkomstige wijze van toepassing is op de rente
  Aan de Commissie werden verschillende vragen gesteld in verband met de berekeningswijze van het disc
  ## Berekening van het disconto
  Voor de berekening van het disconto moet de methode van het disconto bij samengestelde interest word
  De berekening mag niet tegen enkelvoudige interest gebeuren. Vooral voor vorderingen op middellange 
  Het op de overlopende rekening te boeken disconto (E) is gelijk aan het verschil tussen de nominale 

**Beoordeling**: [A / F / S]  ← markeer hier

---

## 2. CBN-0107-08-boekhoudkundige-verwerking-van-de-voorzieningen-voor-risicos-en-kosten.md

**Rationale**: G2: frontmatter themas-veld op regel 45 bevat ongeparseerde HTML-entity '&#039;' ('voorzieningen voor risico&#039;s en kosten') — ETL-bug, HTML niet gedecode. Body-tekst is volledig clean en goed leesbaar.

**Concrete problemen** (max 3):
  - `G2` (other): voorzieningen voor risico&#039;s en kosten — HTML-entity &#039; niet gedecode in

**Body sample** (eerste 8 niet-blanke regels):
  # CBN-advies 107/8 - Boekhoudkundige verwerking van de voorzieningen voor risico's en kosten
  Als gevolg van concrete vragen daaromtrent heeft de Commissie een algemeen onderzoek verricht met be
  Zij is van oordeel dat in de regel de wijziging - van een boekjaar naar een ander - van de passiefpo
  Op deze regel werden een drietal uitzonderingen vastgesteld.
  Een eerste uitzondering slaat op de voorzieningen met een financieel karakter. Inderdaad, daar waar 
  De Commissie is van oordeel dat deze uitzondering een vrij beperkte draagwijdte heeft, daar de voorz
  In het algemeen rekeningenstelsel komt een bijzondere rekening voor met betrekking tot de tenlastene
  Een derde uitzondering slaat op de boekhoudkundige verwerking van lijfrente[^4].

**Beoordeling**: [A / F / S]  ← markeer hier

---

## 3. CBN-2011-17-boekhoudkundige-verwerking-van-onderzoeksfondsen-in-de-jaarrekening-van-grote-en-zeer.md

**Rationale**: E2: meerdere tabelrijen zijn gefragmenteerd. Regel 219-222: rekening 6620 en de omschrijving 'en kosten' staan als aparte rijen buiten de tabelcel. Regels 241-243: rekening 168 en 'met terugnemingsrecht' idem. Regels 269-270 en 277-278: 'Aanschaffingswaarde' als losse tabelrij na de hoofd-rekeningri

**Concrete problemen** (max 3):
  - `E2` (pseudo-table): | | 6620 | Voorzieningen voor uitzonderlijke risico's | | |
| | en kosten | 100.
  - `E2` (pseudo-table): | | 168 | Voorzieningen voor schenkingen en legaten | | |
| | met terugnemingsre
  - `E2` (pseudo-table): | aan | 7170 | Wijziging in de bestellingen in uitvoering: | | 70.000 |
| | Aans

**Body sample** (eerste 8 niet-blanke regels):
  # CBN-advies 2011/17 - Boekhoudkundige verwerking van “onderzoeksfondsen” in de jaarrekening van gro
  Verenigingen en stichtingen ontvangen geregeld “onderzoeksfondsen” met het oog op de uitvoering van 
  De boekhoudkundige verwerking van dergelijke onderzoeksfondsen is afhankelijk van de modaliteiten wa
  ## Onderzoeksfondsen zonder exclusief gebruiksrecht
  Een eerste mogelijkheid is dat de toekennende instantie[^2] middelen ter beschikking stelt met het o
  De vereniging of stichting mag de gelden die zij ontvangt onmiddellijk in resultaat boeken als ‘expl
  Indien de onderzoeksfondsen in één keer worden uitbetaald, maar betrekking hebben op een onderzoek d
  ## Voorbeeld 1

**Beoordeling**: [A / F / S]  ← markeer hier

---

## 4. CBN-2010-12-de-toepassing-van-de-algemene-boekhoudprincipes-op-afgeleide-financiele-instrumenten.md

**Rationale**: A9: H1-titel (r74) bevat 'instrumenten1' — superscript voetnootnummer niet geparsed als [^1], plus '2010/12 -De' zonder spatie. B2/D4: r78 heeft '*Het ontbreken van een conceptueel kader...*' als standalone italic-regel die als subsectietitel fungeert — PDF-artefact, niet als heading gemarkeerd. All

**Concrete problemen** (max 3):
  - `A9` (other): instrumenten1 Advies van 8 september 2010 (superscript [^1] niet geparsed)
  - `B4` (other): *Het ontbreken van een conceptueel kader inzake de boekhoudkundige verwerking...
  - `B2` (other): ### *Doelstelling van het advies* (italic wrapper in ### heading)

**Body sample** (eerste 8 niet-blanke regels):
  # CBN-advies 2010/12 -De toepassing van de algemene boekhoudprincipes op afgeleide financiële instru
  ## Inleiding
  *Het ontbreken van een conceptueel kader inzake de boekhoudkundige verwerking van afgeleide financië
  Het dynamisch karakter van de internationale financiële markten heeft tot gevolg dat vandaag de dag 
  De tijd dat deze producten enkel door professionals werden gebruikt, ligt ver achter ons. Hun toepas
  De Richtlijnen 2001/65/EG[^2], 2003/51/EG[^3] en 2006/46/EG[^4] hebben in de Vierde Richtlijn[^5] de
  Zoals echter wordt uiteengezet in het Verslag aan de Koning bij het koninklijk besluit van 10 august
  Bij gebrek aan specifieke regels dient de boekhoudkundige verwerking van afgeleide financiële instru

**Beoordeling**: [A / F / S]  ← markeer hier

---

## 5. CBN-2009-04-model-van-ongesplitst-dagboek-zoals-bedoeld-in-artikel-2-van-het-koninklijk-besluit-van-26.md

**Rationale**: D4 bevestigd r.64: 'beperkt is tot* "de registratie van de verrichtingen' — sluitende asterisk van italic staat direct vóór een aanhalingsteken zonder spatie-na-asterisk (malformed italic). Aanvullend nieuw in deze ronde: B4 r.56/70: twee ##-headings in all-caps ('## SCHRAPPING VAN HET WOORD « MINIM

**Concrete problemen** (max 3):
  - `D4` (other): beperkt is tot* "de registratie van de verrichtingen met betrekking tot de mutat
  - `B4` (other): ## SCHRAPPING VAN HET WOORD « MINIMAAL » IN ARTIKEL 2 EN BIJLAGE A VAN HET BESLU
  - `B4` (other): ## HET ONGESPLITSTE DAGBOEK HOUDEN DOOR MIDDEL VAN GEINFORMATISEERDE SYSTEMEN (a

**Body sample** (eerste 8 niet-blanke regels):
  # CBN-advies 2009/4 - Model van ongesplitst dagboek zoals bedoeld in artikel 2 van het koninklijk be
  ## INLEIDING
  Met het koninklijk besluit van 15 september 2006 tot wijziging van het koninklijk besluit van 26 jun
  De vragen die hieromtrent werden gesteld, kwamen erop neer te weten of, enerzijds, de schrapping van
  ## SCHRAPPING VAN HET WOORD « MINIMAAL » IN ARTIKEL 2 EN BIJLAGE A VAN HET BESLUIT
  Ingevolge de wijzigingen die met het voornoemde koninklijk besluit van 15 september 2006 zijn aangeb
  Met deze wijziging is gevolg gegeven aan een aantal concrete vragen in verband met de voorstelling e
  De schrapping van het woord « minimaal » in artikel 2 en bijlage A van het besluit biedt, naar het a

**Beoordeling**: [A / F / S]  ← markeer hier

---

## 6. CBN-0148-04-boeking-van-de-prorata-van-gelopen-interest-op-obligaties-en-kasbons.md

**Rationale**: Vier ETL-bugs ongewijzigd t.o.v. ronde 2: E2 (regel 234) 'aan' als losse cel breekt tabelstructuur; A9 (regel 280) 'Kreditinstellingen' i.p.v. 'Kredietinstellingen'; D3 (regels 292-294) voetnoten [^3] en [^4] zonder inline-referentie in body; B1 (regel 189) heading bevat enkel datum en bedrag zonder

**Concrete problemen** (max 3):
  - `E2` (other): | aan | | 52 | Vastrentende effecten | 1.000.000 |
  - `A9` (ocr-confusion): | | 55 | Kreditinstellingen | 1.351.975 | |
  - `D3` (other): [^3]: Roerende voorheffing van 25 %.  (geen inline-referentie in body)

**Body sample** (eerste 8 niet-blanke regels):
  # CBN advies 148-4 - Boeking van de prorata van gelopen interest op obligaties en kasbons
  Krachtens de boekhoudwetgeving moeten de kosten en opbrengsten steeds worden toegerekend aan het boe
  Dit beginsel krijgt in het algemeen rekeningenstelsel gestalte met volgende overlopende rekeningen :
  ## 490 Over te dragen kosten
  491 Verkregen opbrengsten 
  492 Toe te rekenen kosten 
  493 Over te dragen opbrengsten 
  die, naar gelang van het geval, op het actief of het passief in de balans moeten worden geboekt in d

**Beoordeling**: [A / F / S]  ← markeer hier

---

## 7. CBN-0133-03-schulden-voortvloeiend-uit-de-bestemming-van-het-resultaat.md

**Rationale**: Drie ETL-artefacten bevestigd: D4 op L75: '*Belastingen *' heeft een spatie vóór de sluitende asterisk. A6 op L75: 'bruto- bedrag' is een hyphen-spatie word-split. A4 op L89: eerdere claim over U+00AC-teken in 'bruto¬schulden' niet visueel bevestigd in leesuitvoer maar niet weerlegbaar zonder binair

**Concrete problemen** (max 3):
  - `D4` (other): rubriek IX, E, 1 *Belastingen *en in het algemeen rekeningenstelsel (spatie voor
  - `A6` (other): of het bruto- bedrag moet worden vermeld (hyphen-spatie word-split)
  - `A4` (other): bruto¬schulden — mogelijk U+00AC als koppelteken (niet visueel bevestigd, wel ee

**Body sample** (eerste 8 niet-blanke regels):
  # CBN-advies 133/3 - Schulden voortvloeiend uit de bestemming van het resultaat
  Dit advies vervangt advies 133/1, verschenen in *Bull. CBN* nr. 9 van december 1981. 
  Overeenkomstig artikel 11, eerste lid van het koninklijk besluit van 8 oktober 1976, wordt de balans
  Omvat de voorgestelde bestemming van het resultaat ook een uitkering aan vennoten, bestuurders, zaak
  De vraag is gerezen of in deze rubriek, in deze rekening, het bruto- bedrag moet worden vermeld van 
  In advies 133/1 opgenomen in *Bull. CBN* nr. 9 van december 1981 heeft de Commissie zich uitgesproke
  Een nieuw onderzoek van deze vraag in het licht van de hervorming van september 1983, heeft echter g
  Deze bruto-boeking wordt door volgende argumenten gerechtvaardigd : 

**Beoordeling**: [A / F / S]  ← markeer hier

---

## 8. CBN-2021-01-uitgiftepremie-0.md

**Rationale**: F1: H1-titel luidt '# COMMISSIE VOOR BOEKHOUDKUNDIGE NORMEN' zonder advies-nummer of -titel — bron-identificatie ontbreekt in body (frontmatter heeft het correct als 'CBN-advies 2021/01' maar body-kop klopt niet). D4: Regel 97 bevat ':* I.B. Inbreng - Onbeschikbaar*.' met spatie na het dubbele punt 

**Concrete problemen** (max 3):
  - `F1` (other): # COMMISSIE VOOR BOEKHOUDKUNDIGE NORMEN (geen advies-nummer of titel in H1)
  - `D4` (other): - bij de andere dan de NV, SE, SCE:* I.B. Inbreng - Onbeschikbaar*.
  - `B5` (other): b) Indien de statuten niets vermelden... (plain text, geen heading — terwijl a) 

**Body sample** (eerste 8 niet-blanke regels):
  # COMMISSIE VOOR BOEKHOUDKUNDIGE NORMEN
  ## Inleiding
  Onderhavig advies heeft betrekking op de boekhoudkundige verwerking van de uitgiftepremie zijnde, in
  Het advies houdt een actualisering in van het CBN-advies 142 – Uitgiftepremie. De Commissie geeft hi
  De hier beoogde uitgiftepremie bestaat uiteraard niet bij de vereniging zonder winstoogmerk (VZW), i
  ## Schema van de jaarrekening en minimumindeling van het algemeen rekeningenstelsel
  De balansschema’s die bij het koninklijk besluit van 29 april 2019 tot uitvoering van het Wetboek va
  De minimumindeling van het algemeen rekeningenstelsel (MAR) werd aangepast[^4] opdat ook passende re

**Beoordeling**: [A / F / S]  ← markeer hier

---

## 9. CBN-0132-04-termijnovereenkomsten-op-handelsgoederen.md

**Rationale**: A6 op meerdere regels: hyphen-spatie word-splits 'in-resultaat- neming' (L101, L113), 'prijs- risico' (L117), 'niet- gerealiseerde' (L129) — PDF-regelbreuk-artefacten consistent door het bestand. Heading-hiërarchie in de huidige body is correct (H1→H2→H3), dus B2 van eerdere ronde is niet meer van t

**Concrete problemen** (max 3):
  - `A6` (other): niet voor in-resultaat- neming vatbaar is
  - `A6` (other): niet voor in-resultaat- neming vatbaar is
  - `A6` (other): het hieraan verbonden prijs- risico gedekt

**Body sample** (eerste 8 niet-blanke regels):
  # CBN-advies 132/4 - Termijnovereenkomsten op handelsgoederen
  ## Beginselen
  1. Handelsgoederen in voorraad worden krachtens artikel 27, § 1 van het koninklijk besluit van 8 okt
  2. Krachtens artikel 19, 3de lid van het koninklijk besluit van 8 oktober 1976 moet rekening worden 
  Artikel 19, 5de lid van dit besluit bepaalt : «Voorzieningen moeten, onder meer, gevormd worden met 
  1. ... 
  2. ... 
  3. de verlies- of kostenrisico's die voortvloeien uit ... termijnposities of -overeenkomsten op goed

**Beoordeling**: [A / F / S]  ← markeer hier

---

## 10. CBN-2022-06-verslaggeving-bij-onmiddellijke-sluiting-van-de-vereffening-van-een-vennootschap.md

**Rationale**: D2: regel 144 kondigt 'Schematisch kunnen de volgende termijnen worden onderscheiden:' aan maar het tijdslijn-schema ontbreekt volledig — de tekst gaat direct verder met een bullet-opsomming zonder de beloofde schematische voorstelling. Geen TOC-fragmenten of andere artefacten aangetroffen.

**Concrete problemen** (max 3):
  - `D2` (missing-section): Schematisch kunnen de volgende termijnen worden onderscheiden: [tijdslijn-schema

**Body sample** (eerste 8 niet-blanke regels):
  # CBN-advies 2022/06 – Verslaggeving bij onmiddellijke sluiting van de vereffening van een vennootsc
  ## Onderwerp van het advies
  Aan de Commissie werd de vraag gesteld welke verslaggevingsverplichtingen moeten worden nageleefd bi
  ## Analyse
  ### Preliminair
  De ontbinding en de sluiting van de vereffening in één akte laat toe om de ontbindingsprocedure van 
  De Commissie wijst erop dat de procedure van de ontbinding en de sluiting van de vereffening in één 
  De procedure van de ontbinding en de vereffening in één akte is van toepassing op een BV, CV, NV[^8]

**Beoordeling**: [A / F / S]  ← markeer hier

---

## 11. CBN-2016-25-kapitaalvermindering-voor-vorming-van-een-reserve-voor-een-voorzienbaar-verlies.md

**Rationale**: D4: regel 63 (body) bevat '*Reserve voor voorzienbaar verlies[^5]*  om na te gaan' — dubbele spatie na de sluitende asterisk is een broken italic-markering, consistent ETL-artefact uit dezelfde pipeline. Overige structuur (9 headings hiërarchisch correct, 3 boekingstabellen in pipe-syntax, voetnoten

**Concrete problemen** (max 3):
  - `D4` (other): *Reserve voor voorzienbaar verlies[^5]*  om na te gaan of de wettelijke voorwaar

**Body sample** (eerste 8 niet-blanke regels):
  # CBN-advies 2016/25 – Kapitaalvermindering voor vorming van een reserve voor een voorzienbaar verli
  ## Inleiding
  In onderhavig advies wordt de boekhoudkundige verwerking naar Belgisch boekhoudrecht behandeld van e
  In dit advies worden uitsluitend de Belgische boekhoudkundige aspecten onderzocht en niet de specifi
  ## Analyse
  ### Wettelijk en reglementair kader
  Het Wetboek van vennootschappen (hierna: W.Venn.) regelt de vorming van een reserve om een voorzienb
  Het betreft een onbeschikbare reserve[^3], die niet mag worden uitgekeerd aan de aandeelhouders en d

**Beoordeling**: [A / F / S]  ← markeer hier

---

## 12. CBN-0108-02-aanvragen-tot-afwijking-overzicht.md

**Rationale**: De eerder gerapporteerde B2-bug (heading-hiërarchie #### zonder ##) is OPGELOST — regels 69, 91 en 126 zijn nu correct ## headings. Echter: A6 op regels 112-114: zin 'Ze werd echter afhankelijk gemaakt ... met het oog op de statistische verwerking, van' (r112) eindigt midden in een bijzin, gevolgd d

**Concrete problemen** (max 3):
  - `A6` (other): ...met het oog op de statistische verwerking, van [lege regel] het bedrag der ve

**Body sample** (eerste 8 niet-blanke regels):
  # CBN-advies 108/2 - Aanvragen tot afwijking : overzicht
  Voor het eerste boekjaar waarop het koninklijk besluit van 8 oktober 1976 van toepassing was, heeft 
  De aanvragen tot afwijking kunnen als volgt worden onderverdeeld :
  ## AANVRAGEN TOT AFWIJKING DIE EEN AANPASSING BEOGEN VAN HET SCHEMA GEHECHT AAN HET K.B. VAN 8 OKTOB
  In deze eerste groep worden de afwijkingen vermeld die er niet toe strekken minder informatie te ver
  Vier steenkoolmijnen in werking werden toegelaten hun balans en resultatenrekening te blijven voorst
  Vijftien portefeuillemaatschappijen die buiten het toepassingsveld vallen van het koninklijk besluit
  Aan een vennootschap die een ziekenhuis beheert, werd toegestaan haar jaarrekening op te stellen ove

**Beoordeling**: [A / F / S]  ← markeer hier

---

## 13. CBN-0107-11-opbrengsten-waarover-betwisting-bestaat-update.md

**Rationale**: G2: frontmatter themas-veld op regel 45 bevat ongeparseerde HTML-entity '&#039;' ('voorzieningen voor risico&#039;s en kosten') — ETL-bug, HTML niet gedecode. Body-tekst is volledig clean en inhoudelijk correct.

**Concrete problemen** (max 3):
  - `G2` (other): voorzieningen voor risico&#039;s en kosten — HTML-entity &#039; niet gedecode in

**Body sample** (eerste 8 niet-blanke regels):
  # Advies van september 1989, bijgewerkt op 10 september 2025
  Krachtens het eerste lid van artikel 3:11 van het koninklijk besluit van 29 april 2019 tot uitvoerin
  Met andere woorden, wanneer − op basis van de criteria van voorzichtigheid, oprechtheid en goede tro
  Is de opbrengst geïnd maar bestaat daarover betwisting, dan is dit geen reden om de boeking in de re
  Voor het bedrag van de voorziening moet, op grond van voornoemde criteria van voorzichtigheid, oprec
  Wanneer een voorziening wordt gevormd, moet deze, naargelang van de evolutie van het effectieve risi
  In deze context werd gevraagd naar de mogelijke weerslag van een rechtsvordering in verband met een 
  Naar het oordeel van de Commissie is het instellen van een gerechtelijke procedure niet doorslaggeve

**Beoordeling**: [A / F / S]  ← markeer hier

---

## 14. CBN-0132-05-rechten-tot-vertoning-van-films.md

**Rationale**: D4 op L85: 'wanneer de uitzendrechten onder* Diensten en diverse goederen* werden geboekt' — openende asterisk staat direct tegen 'onder' geplakt zonder spatie, wat de italic-span niet correct parseert. Eerdere A6-claim over L75 niet bevestigd: [^1] mid-zin is standaard markdown-voetnootnotatie, gee

**Concrete problemen** (max 3):
  - `D4` (other): wanneer de uitzendrechten onder* Diensten en diverse goederen* werden geboekt (s

**Body sample** (eerste 8 niet-blanke regels):
  # CBN-advies 132/5 - Rechten tot vertoning van films
  De Commissie werd om advies gevraagd over de boekhoudkundige verwerking van het bedrag dat een onder
  De vraag of de sommen betaald voor dergelijke vertoningsrechten - die een beperkte draagwijdte hebbe
  Hier moeten inderdaad twee hypothesen worden onderscheiden. 
  Wanneer voor een onderneming het uitzenden of vertonen van films het hoofdbedrijf uitmaakt, lijkt he
  In de andere hypothese adviseert de Commissie de betrokken uitzendrechten te boeken onder *Diensten 
  Het spreekt echter vanzelf dat de Commissie in casu niet adviseert het beginsel van de kosten-en opb
  Het lijkt de Commissie derhalve noodzakelijk dat de betrokken kostenboekingen voor de opstelling van

**Beoordeling**: [A / F / S]  ← markeer hier

---

## 15. CBN-0179-01-boekhoudkundige-verwerking-van-broeikasgasemissierechten.md

**Rationale**: B4 bevestigd r.73: '(Update november 2008)' als plain tekst direct na de H1-titel in plaats van als subkopje. D4 bevestigd r.163/165: 'Bij de* Interpretation 3 Emission Rights*' en 'In verband met de* Interpretation 3 Emission Rights*' — opening asterisk grenst direct aan 'de' zonder spatie (malform

**Concrete problemen** (max 3):
  - `B4` (other): (Update november 2008) — plain tekst direct na H1-titel, geen heading-prefix
  - `D4` (other): Bij de* Interpretation 3 Emission Rights* worden ook voorbeelden gegeven
  - `D4` (other): In verband met de* Interpretation 3 Emission Rights* werden een aantal kritieken

**Body sample** (eerste 8 niet-blanke regels):
  # Boekhoudkundige verwerking van broeikasgasemissierechten
  (Update november 2008)
  ## Inleiding
  Met het Kyotoprotocol dat op 16 februari 2005 in werking is getreden en sindsdien een dwingend karak
  Daartoe beschikt Europa over de Richtlijn 2003/87/EG van het Europees Parlement en de Raad van 13 ok
  De richtlijn organiseert een markt voor broeikasgasemissierechten, zodanig dat ondernemingen die de 
  In België werd de richtlijn omgezet met o.a. de volgende regionale wetgeving:
  - Decreet van 2 april 2004 tot vermindering van de uitstoot van broeikasgassen in het Vlaamse Gewest

**Beoordeling**: [A / F / S]  ← markeer hier

---

## 16. CBN-2009-15-de-boekhoudkundige-verwerking-van-de-inbreng-van-een-bedrijfstak-of-van-een-algemeenheid.md

**Rationale**: A9: H1-titel (r62) bevat 'bedrijfstak1' — superscript voetnootnummer [^1] niet geparsed, kleeft aan het woord als cijfer. B3/A6: r64 bevat 'of van een algemeenheid van goederen' als losstaande plain-text regel direct na de H1-titel — dit is een extractie-duplicaatfragment van de H1-titel. Beide zijn

**Concrete problemen** (max 3):
  - `A9` (other): bedrijfstak1 or van een algemeenheid van goederen (superscript [^1] niet geparse
  - `B3` (other): of van een algemeenheid van goederen (losstaand titelfragment duplicate)

**Body sample** (eerste 8 niet-blanke regels):
  # CBN-advies 2009/15 - De boekhoudkundige verwerking van de inbreng van een bedrijfstak1 of van een 
  ## Inleiding
  Door het Koninklijk Besluit van 3 december 1993 (B.S., 23 december 1993) werd met betrekking tot de 
  In het Verslag aan de Koning werd hierbij inderdaad gesteld dat het verkieslijk leek om het boekhoud
  Voor de boekhoudkundige verwerking van fusies en splitsingen werd – voor verrichtingen vanaf 1 oktob
  Aangezien de vennootschapsrechtelijke regeling voor de inbreng van een bedrijfstak of van een algeme
  Met het Koninklijk Besluit tot uitvoering van het Wetboek van vennootschappen (KB/W.Venn.) werd – vo
  Van zodra vanaf 6 februari 2001 een inbreng van een bedrijfsafdeling of van een algemeenheid van goe

**Beoordeling**: [A / F / S]  ← markeer hier

---

## 17. CBN-2019-06-groepsbijdrage.md

**Rationale**: D4: regel 64 heeft `*groepsbijdrage*regeling` — ontbrekende spatie tussen italic-sluit en aangrenzend woord. B2: `## Bij de eindejaarsverrichtingen op 31/12/N` (regels 124, 140) en `## Bij het sluiten van de groepsbijdrage-overeenkomst` (regels 131, 144) staan op ##-niveau terwijl hun logische ouder

**Concrete problemen** (max 3):
  - `D4` (other): de *groepsbijdrage*regeling[^2] in de statutaire jaarrekening
  - `B2` (other): ## Bij de eindejaarsverrichtingen op 31/12/N (kind van ### In hoofde van vennoot
  - `B2` (other): ## Bij het sluiten van de groepsbijdrage-overeenkomst (in boekjaar N+1)

**Body sample** (eerste 8 niet-blanke regels):
  # COMMISSIE VOOR BOEKHOUDKUNDIGE NORMEN
  ## Algemeen
  Met onderhavig advies verduidelijkt de Commissie de boekhoudkundige verwerking van de *groepsbijdrag
  De groepsbijdrageregeling steunt op het beginsel van de fiscale neutraliteit volgens hetwelk de fisc
   De groepsbijdrageregeling is een vorm van fiscale consolidatie.
  ## Beknopte beschrijving van de groepsbijdrageregeling
  Met de groepsbijdrage-regeling wordt beoogd om aan vennootschapsgroepen de mogelijkheid te bieden om
  Fiscaaltechnisch wordt deze fiscale winstverschuiving bekomen door een vermindering[^4] van het bela

**Beoordeling**: [A / F / S]  ← markeer hier

---

## 18. CBN-2022-11-vermogensmutatiemethode.md

**Rationale**: E1: de resultatenrekening-tabellen ('Invloed van de vermogensmutatiemethode') zijn geen echte markdown-pipe-tabellen — labels en getallen staan elk op een aparte regel, omringd door losse |---| fragmenten (bv. regels 214-239, 285-300), een typisch PDF-extractie-artefact. B2: de heading '## Herbereke

**Concrete problemen** (max 3):
  - `E1` (pseudo-table): | \n\nKosten\n\n  | | \n|---|\n\nOpbrengsten\n\n  | (resultatenrekening als loss
  - `E1` (pseudo-table): Financiële kosten – Afschrijving 'Consolidatieverschillen'\n\n  | | \n|---|\n\n2
  - `B2` (other): ## Herberekening van het bedrag van de deelneming... (H2 binnen Hypothese-subblo

**Body sample** (eerste 8 niet-blanke regels):
  # CBN-advies 2022/11 – Vermogensmutatiemethode
  ## Toepassingsgebied
  Elke moedervennootschap die onderworpen is aan de bepalingen van het gemeen recht inzake consolidati
  Een vennootschap wordt vrijgesteld van de verplichting om een geconsolideerde jaarrekening en een ja
   Dat betekent dat de vennootschap op geconsolideerde of geaggregeerde basis niet meer dan één van de
  Onder “controle” over een vennootschap wordt verstaan, de bevoegdheid in rechte of in feite om een b
  Onder “geassocieerde vennootschap” wordt verstaan, elke andere vennootschap dan een dochtervennootsc
   Geassocieerde vennootschappen worden doorgaans opgenomen in de consolidatie via de vermogensmutatie

**Beoordeling**: [A / F / S]  ← markeer hier

---

## 19. CBN-2021-10-boekhoudkundige-verwerking-van-fusies-tussen-vennootschappen.md

**Rationale**: E2/A7: Op meerdere plaatsen zijn complexe tabellen met sublijsten niet correct als markdown weergegeven — regels 561-576 tonen een gebroken tabelrij waarbij bullet-list items buiten de tabelcellen vallen met losse |---|---| separators op eigen regels, wat een extractie-artefact is van een geneste ta

**Concrete problemen** (max 3):
  - `E2` (other): tabelrij met sublijst-items buiten cellen: '- Geplaatst kapitaal / Beschikbare i
  - `E2` (other): | | | 18.380 | | |

18.380

  | — tabelslot gesplitst over 3 regels
  - `E2` (other): | | | 18.380 | | |

18.380

  | — idem voor voorbeeld 12

**Body sample** (eerste 8 niet-blanke regels):
  # CBN-advies 2021/10 – Boekhoudkundige verwerking van fusies tussen vennootschappen
  ## Inleiding
  Naar aanleiding van de aanneming van het Wetboek van vennootschappen en verenigingen (hierna: WVV), 
  Het toepassingsgebied van onderhavig advies is beperkt tot fusies tussen vennootschappen met rechtsp
  Bovendien wordt enkel de fusie door overneming behandeld aangezien deze fusievorm zowel vennootschap
  In onderhavig advies wordt er eerst een definitie gegeven van fusies door overneming en wordt het co
  Onderhavig advies vervangt CBN-advies 2009/6 – *De boekhoudkundige verwerking van fusies*.
  ## Algemene principes

**Beoordeling**: [A / F / S]  ← markeer hier

---

## 20. CBN-0173-06-verrekening-van-vorderingen-en-schulden-die-oorspronkelijk-zijn-uitgedrukt-in-munten-die.md

**Rationale**: A6 bevestigd r.85-87: de zin 'Die schulden en vorderingen mogen dus niet' eindigt zonder leesteken, gevolgd door een lege regel, waarna 'langer, voor het overeenstemmende bedrag...' begint — een PDF-regelbreuk midden in een logische alinea. Frontmatter thema 'erfpa' (r.49) is een afgekapt scraping-a

**Concrete problemen** (max 3):
  - `A6` (other): Die schulden en vorderingen mogen dus niet 

langer, voor het overeenstemmende b
  - `F1` (source-typo): - erfpa (afgekapt thema-label in frontmatter — source-typo, niet ETL)

**Body sample** (eerste 8 niet-blanke regels):
  # CBN-advies 173/6 - Verrekening van vorderingen en schulden die oorspronkelijk zijn uitgedrukt in m
  De vraag werd gesteld of een onderneming haar wederzijdse vorderingen en schulden met eenzelfde tege
  Gesteld dat een onderneming naar Belgisch recht op 31 december 1998 een onmiddellijk opeisbare vorde
  Veronderstel dat de omrekeningskoers van DEM en BEF in euro is vastgesteld op respectievelijk 1,88 e
  Mag zij - moet zij - die schuld en die vordering die oorspronkelijk in verschillende munten waren ui
  ## In het Europese recht
  Het reglement van de Europese Raad over de invoering van de euro dat als bijlage gaat bij de resolut
  Aangezien het Europese recht verwijst naar de nationale wettelijke bepalingen, moeten, enerzijds, he

**Beoordeling**: [A / F / S]  ← markeer hier

---
