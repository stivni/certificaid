---
tags: ["VI.B", "2.4"]
itaa-lex-sectie: "VI.B"
wet: "K.B. nr. 24 van 29 december 1992, met betrekking tot de voldoening van de belasting over de toegevoegde waarde"
bron_rol: "itaa_lex"
status: "beschikbaar"
bijgewerkt: "29.12.1992"
bron: "Afgesplitst uit Fisconet-compilatie (pdftotext_compilatie_btw)"
chunk:
  level: 4
  type: "Art."
  sub_strategy:
provenance:
  inputs:
    - id: resources/raw/wetteksten/btw-kbs/WBTW-KB-compilatie.pdf
      sha256: 5f1bad7278d1f8e1f5c00efb5d792f61342d3f7a14a7950caca2937924bfa91c
      version: 06.03.2020
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: d4b4775
    model:
    prompt_version:
  generated_at: '2026-05-13T10:58:05Z'
  stale: false
  stale_reason:
  trust:
    status: needs-rework
    confirmed_at: '2026-05-13T10:59:42Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: Heeft een uitgebreide TOC bij start met afdelings- en artikel-ranges ('Art. 1 - 8', 'Art. 9 - 13', 'Art. 13bis') die als plain text dwars door de heading-hierarchie staan. Het TOC-blok bevat ook spurious linebreaks waardoor headings over twee regels lopen ('Betalingen op de rekeningen van "btw-ontvangsten"\nBrussel', 'Onderafdeling 2. Betaling op de financiële rekening van "Inning en\nInvordering"'). Bovendien staat een Franse string 'Disposition temporaire' (regel 66) ongetag'd midden in een NL-tekst — dit is een ETL-leak van de bilingue bron.
    layer1:
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-13T10:59:42Z'
      rationale: Heeft een uitgebreide TOC bij start met afdelings- en artikel-ranges ('Art. 1 - 8', 'Art. 9 - 13', 'Art. 13bis') die als plain text dwars door de heading-hierarchie staan. Het TOC-blok bevat ook spurious linebreaks waardoor headings over twee regels lopen ('Betalingen op de rekeningen van "btw-ontvangsten"\nBrussel', 'Onderafdeling 2. Betaling op de financiële rekening van "Inning en\nInvordering"'). Bovendien staat een Franse string 'Disposition temporaire' (regel 66) ongetag'd midden in een NL-tekst — dit is een ETL-leak van de bilingue bron.
      concrete_problemen:
        - Franse plain-text fragment 'Disposition temporaire' (regel 66) tussen NL-content — bilingue residu
        - "Spurious linebreaks midden in heading-tekst: '\"Inning en\\nInvordering\"' (regels 58-59), '\"Mini One Stop Shop\\n- VAT BE\"' (regels 61-62), 'Brussel,\\n\"Inning en Invordering\"' (regels 53-54)"
        - "Smart-quote inconsistentie: 'VAT BE' opent met \" maar sluit met ” (regels 62, 64) — OCR/PDF-glyph artefact"
        - TOC-blok aan begin (regels 52-74) bevat artikel-ranges 'Art. 1 - 8', 'Art. 9 - 13' als plain text i.p.v. echte navigatiemarkup
        - "Mid-paragraaf linebreaks in artikel-content: '8(1)', '8(2)' en dubbele linebreaks tussen alinea's op tal van plaatsen (regel 87-95)"
        - "'AFDELING'/'Onderafdeling' staan inconsistent — soms als ## of ###, soms als plain text in TOC"
---

# K.B. nr. 24 van 29 december 1992, met betrekking tot de voldoening van de belasting over de toegevoegde waarde

*Bijgewerkt tot en met 29.12.1992 — gecoördineerde versie.*

Koninklijk besluit nr. 24, van 29 december 1992, met betrekking tot de voldoening van de belasting over de toegevoegde waarde.

(Uitvoering van de artikelen 52, 53, 53ter, 53octies, 53nonies, 54, 58, 70 en 91 van het Wetboek. Officieuze coördinatie)

Laatstelijk gewijzigd met ingang van 01.01.2020 (KB 09.12.2019, B.S. 16.12.2019 – Ed. 2, pg. 113850)

## AFDELING 1. Betalingen op de rekeningen van "btw-ontvangsten"
Brussel, "Inning en Invordering", "Mini One Stop Shop - btw BE" en "btw on E-Services".

### Onderafdeling 1. Betaling op de postrekening van "BTW-Ontvangsten"
Brussel Art. 1 - 8

### Onderafdeling 2. Betaling op de financiële rekening van "Inning en
Invordering". Art. 9 - 13

### Onderafdeling 3. Betaling op de postrekening van "Mini One Stop Shop
- VAT BE” Art. 13bis

### Onderafdeling 4. Betaling op de postrekening van "VAT on E-Services”

Disposition temporaire Art. 13ter

## AFDELING 2. Betaling vastgesteld door middel van het elektronische systeem PLDA van de Algemene Administratie van de Douane en Accijnzen. Art. 14 - 15

## AFDELING 3. Betaling bestemd voor het kantoor van de door of vanwege de Minister van Financiën met de invordering belaste ambtenaar. Art. 16 - 19

## AFDELING 4. Betaling op een douane of accijnskantoor voor andere dan bij invoer verschuldigde belasting over de toegevoegde waarde. Art. 20 - 21

## AFDELING 5. Slotbepalingen. Art. 22 - 24

## AFDELING 1
Betalingen op de rekeningen van "btw-ontvangsten" Brussel,
"Inning en Invordering", "Mini One Stop Shop - btw BE" en
"btw on E-Services".

(Het opschrift van Afdeling 1, werd vervangen met ingang van 01.12.2019 (Art. 31, KB 17.02.2019, B.S. 08.03.2019, pg. 25174))

### Onderafdeling 1
Betaling op de postrekening van "BTW-Ontvangsten" Brussel.

#### Art. 1
(De tekst van KB nr. 24, artikel 1, inleidende zin, werd gewijzigd met ingang van 05.12.2019 (Art. 4, KB 07.11.2019, B.S. 25.11.2019, pg 108072))

Onder voorbehoud van de toepassing van de artikelen 8, § 1, en 10, 1°/1 van dit besluit worden op de in de artikelen 2 tot 7 aangegeven wijze betaald:
1° de belasting over de toegevoegde waarde waarvan de opeisbaarheid blijkt uit de periodieke aangifte bedoeld in artikel 53, § 1, eerste lid, 2°, van het Wetboek;

2° de fiscale geldboeten voor het te laat indienen van die aangifte;

3° de fiscale geldboeten en de nalatigheidsinteresten verschuldigd overeenkomstig artikel 91, § 1 van het Wetboek, voor het te laat betalen van de belasting waarvan de opeisbaarheid uit diezelfde aangifte blijkt;

4° het voorschot waarvan de opeisbaarheid blijkt uit artikel 19 van het koninklijk besluit nr.
1 van 29 december 1992 met betrekking tot de regeling voor de voldoening van de belasting over de toegevoegde waarde.

#### Art. 2
(De tekst van KB nr. 24, artikel 2, is van toepassing met ingang van 01.01.1999 (Art.1, KB 12.11.1998))

De betaling wordt gedaan op de postrekening nr. 679-2003000-47 van "BTW-Ontvangsten" Brussel door storting of overschrijving.

#### Art. 3
(De tekst van KB nr. 24, artikel 3, § 1, eerste lid, werd gewijzigd met ingang van 16.05.2014 (Art. 21, KB 24.01.2015, B.S. 20.02.2015 – Ed. 2, pg. 13872))

§ 1. Voor de betaling moet de belastingplichtige hetzij de formulieren gebruiken die hem door de administratie belast met de belasting over de toegevoegde waarde worden bezorgd, hetzij, bij gebrek aan een dergelijk gebruik, de gestructureerde mededeling vermelden die hem werd ter kennis gebracht door de administratie.

Het model van het door de administratie bezorgde formulier wordt bepaald door of vanwege de Minister van Financiën en moet beantwoorden aan het model voorgeschreven door de interbancaire overeenkomst met betrekking tot overschrijvings- of stortingsformulieren.

§ 2. De betaalformulieren bezorgd door de administratie worden geïndividualiseerd door op elk ervan de naam van de belastingplichtige en het BTW-identificatienummer dat hem werd toegekend, te vermelden.

Ze mogen alleen worden gebruikt om de door die bepaalde belastingplichtige verschuldigde bedragen te betalen.

In geen geval mag het op het betaalformulier gedrukte BTW-identificatienummer worden gewijzigd.

#### Art. 4
(De tekst van KB nr. 24, artikel 4 is van toepassing met ingang van 01.01.1999 (Art.1, KB 12.11.1998))

§ 1. De betaling, verricht op een van de in artikel 2 bepaalde wijzen, heeft uitwerking:

1° voor een storting op een postkantoor, op de datum van de storting;

2° voor een overschrijving, de laatste werkdag die voorafgaat aan de datum van creditering van de postrekening nr. 679-2003000-47 van "BTW-Ontvangsten" Brussel. Als werkdagen worden aangemerkt alle andere dagen dan de zaterdagen, de zondagen en de wettelijke feestdagen.

§ 2. Door of vanwege de Minister van Financiën worden, in overleg met de Minister onder wie de Post ressorteert of diens afgevaardigde, de voorwaarden, de formaliteiten en de termijnen bepaald, die door de kredietinstellingen die aangesloten of vertegenwoordigd zijn bij een verrekenkamer van het land moeten worden nageleefd, voor de uitvoering van de ontvangen betalingsorders en voor de overmaking van het geld ten bate van de Schatkist.

#### Art. 5
(De tekst van KB nr. 24, artikel 5, § 1, 2°, a) en § 2, werd gewijzigd met ingang van 01.04.2019 (Art. 11, KB 17.03.2019, B.S. 08.04.2019, pg. 35699). Dit besluit (KB 17.03.2019) is niet van toepassing op het dwangbevel dat werd kennisgegeven of betekend vóór de datum van zijn inwerkingtreding – 01.04.2019 (Art. 23, KB 17.03.2019))

§ 1. De administratie houdt voor iedere belastingplichtige die periodieke aangiften moet indienen, een rekening-courant bij waarin worden opgenomen, naarmate van de boeking ervan:

1° op de creditzijde:

a) het bedrag van alle betalingen op de postrekening nr. 679-2003000-47, die op naam van de belastingplichtige worden geboekt;

b) het batig maand- of kwartaalsaldo dat blijkt uit de door de belastingplichtige ingediende aangiften;

2° op de debetzijde:

a) het bedrag van de in artikel 1, 1° tot 3° bedoelde belasting, nalatigheidsinteresten en fiscale geldboeten;

b) de bedragen die aan de belastingplichtige werden teruggegeven overeenkomstig artikel 7 van dit besluit.

§ 2. Door of vanwege de Minister van Financiën kan onder de voorwaarden die zij bepalen, worden beslist dat andere dan de onder § 1 van dit artikel vermelde verrichtingen in de rekening-courant worden geboekt als een door de belastingplichtige verschuldigd bedrag van belasting over de toegevoegde waarde, fiscale geldboeten, nalatigheidsinteresten en kosten, als

een verrichting gelijkgesteld met een betaling bedoeld in artikel 2 van dit besluit of als een verbetering van verrichtingen die vroeger reeds werden geboekt.

§ 3. Alleen het BTW-identificatienummer dat voorkomt op het formulier dat werd bezorgd door de administratie of in de gestructureerde mededeling ter kennis gebracht door de administratie bepaalt, voor de betaling op de postrekening nr. 679-2003000-47, de belastingplichtige wiens rekening-courant moet worden gecrediteerd.

Iedere betaling op de postrekening nr. 679-2003000-47 met vermelding van het BTWidentificatienummer van een belastingplichtige die periodieke aangiften moet indienen, wordt, niettegenstaande elke strijdige verklaring, geacht te zijn gedaan om te worden ingeschreven op de rekening-courant van die belastingplichtige.

#### Art. 6
(De tekst van KB nr. 24, artikel 6, eerste lid, werd gewijzigd met ingang van 01.04.2019 (Art. 12, KB 17.03.2019, B.S. 08.04.2019, pg. 35699). Dit besluit (KB 17.03.2019) is niet van toepassing op het dwangbevel dat werd kennisgegeven of betekend vóór de datum van zijn inwerkingtreding – 01.04.2019 (Art. 23, KB 17.03.2019))

De op de creditzijde van de in artikel 5, § 1 en § 2, bedoelde ingeschreven bedragen worden, niettegenstaande elke strijdige verklaring van de belastingplichtige, in de navolgende volgorde toegerekend: eerst op de kosten, daarna op de nalatigheidsinteresten, vervolgens op de fiscale geldboeten en tenslotte op de nog verschuldigde belasting.

De toerekening gebeurt:

1° voor de betalingen, op de datum waarop ze uitwerking hebben;

2° voor het in artikel 5, § 1, 1°, b, bedoelde maand- of kwartaalsaldo, op de uiterste datum bepaald voor het indienen van de aangifte waaruit dat saldo blijkt;

3° voor de in artikel 5, § 2, bedoelde inschrijvingen, op de datum bepaald door of vanwege de Minister van Financiën.

#### Art. 7
(De tekst van KB nr. 24, artikel 7, is van toepassing met ingang van 01.01.1993 (KB 29.12.1992))

Het saldo in het voordeel van de belastingplichtige dat uit de rekening-courant blijkt nadat de toerekeningen zijn gedaan overeenkomstig artikel 6, wordt teruggegeven op de tijdstippen, onder de voorwaarden en volgens de modaliteiten bepaald bij de artikelen 8(1), 12, § 1, en 13, van het koninklijk besluit nr. 4 met betrekking tot de teruggaven inzake belasting over de toegevoegde waarde.

De aanvraag om teruggaaf moet door de belastingplichtige worden ingesteld op de wijze aangeduid in artikel 8(1), § 4, van het koninklijk besluit nr. 4 met betrekking tot de teruggaven inzake belasting over de toegevoegde waarde.

#### Art. 8
(De tekst van KB nr. 24, artikel 8, is van toepassing met ingang van 01.01.1993 (KB 29.12.1992))

§ 1. Door of vanwege de Minister van Financiën kan worden beslist dat handelingen, die vóór een door of vanwege hem te bepalen datum worden verricht, aan de in artikel 5 bedoelde rekening-courant worden onttrokken en dat een bijzondere rekening zal worden bijgehouden voor het tijdvak dat aan die datum voorafgaat.

In dat geval maakt de beslissing melding van de toestand van de rekening-courant op die datum, alsmede van het tijdvak waarvoor die bijzondere rekening wordt bijgehouden.
Van die beslissing wordt aan de belastingplichtige kennis gegeven bij aangetekende brief. De afgifte van het stuk ter post geldt als kennisgeving vanaf de daaropvolgende dag.
De betalingen die op de bijzondere rekening moeten worden toegerekend, moeten worden gedaan op de door of vanwege de Minister van Financiën bepaalde wijze.
Indien de bijzondere rekening sluit met een overschot in het voordeel van de belastingplichtige, wordt dat overschot ingeschreven op de creditzijde van de overeenkomstig artikel 5 voor die belastingplichtige bijgehouden rekening-courant. Door of namens de Minister van Financiën wordt de datum bepaald waarop die inschrijving uitwerking heeft. Het voornoemde overschot kan echter op uitdrukkelijk verzoek van de belastingplichtige worden teruggegeven, overeenkomstig artikel 8(2) van het koninklijk besluit nr. 4 met betrekking tot de teruggaven inzake belasting over de toegevoegde waarde en slechts in de gevallen en onder de voorwaarden die door of vanwege de Minister van Financiën worden bepaald.
Indien de bijzondere rekening sluit met een overschot in het voordeel van de belastingplichtige en de hiervoor bedoelde rekening-courant voor hem niet meer wordt bijgehouden, wordt dat overschot aan de belastingplichtige teruggegeven overeenkomstig artikel 8(2) van voornoemd koninklijk besluit nr. 4 en slechts in de gevallen en onder de voorwaarden bepaald door of vanwege de Minister van Financiën.

§ 2. Iedere betaling of verrichting gelijkgesteld met een betaling overeenkomstig artikel 5, § 2, van dit besluit, die wordt ingeschreven op de rekening-courant en die uitwerking heeft na de in § 1 van dit artikel bedoelde kennisgeving, worden, niettegenstaande elke strijdige verklaring, geacht te zijn gedaan ter voldoening van de in artikel 1 en artikel 5, § 2, bedoelde bedragen, die de belastingplichtige verschuldigd is of zal worden voor het tijdvak dat volgt op dat waarvoor het bijhouden van een bijzondere rekening werd voorgeschreven.

### Onderafdeling 2
Betaling op de financiële rekening van "Inning en Invordering".

(Het opschrift van Onderafdeling 2, werd vervangen met ingang van 01.12.2019 (Art. 32, KB 17.02.2019, B.S. 08.03.2019, pg. 25174))

#### Art. 9
(De tekst van KB nr. 24, artikel 9, werd gewijzigd met ingang van 01.01.2020 (Art. 31, KB 09.12.2019, B.S. 16.12.2019 - Ed. 2, pg. 113850))

Onverminderd de toepassing van artikel 5, § 2, wordt de betaling van de belasting over de toegevoegde waarde, administratieve geldboeten, interesten en kosten die verschuldigd zijn wegens inbreuken op de bepalingen van het Wetboek of de uitvoeringsbepalingen, gedaan overeenkomstig hetgeen voorzien is in de artikelen 15 tot 17 van het Wetboek van de minnelijke en gedwongen invordering van fiscale en niet-fiscale schuldvorderingen.

#### Art. 10
(De tekst van KB nr. 24, artikel 10, inleidende zin, werd gewijzigd met ingang van 01.01.2020 (Art. 32, KB 09.12.2019, B.S. 16.12.2019, pg. 113850))

Onverminderd de toepassing van artikel 20, wordt de betaling eveneens gedaan overeenkomstig hetgeen voorzien is in de artikelen 15 tot 17 van het Wetboek van de minnelijke en gedwongen invordering van fiscale en niet-fiscale schuldvorderingen voor:
1° de belasting over de toegevoegde waarde waarvan de opeisbaarheid blijkt uit de aangifte bedoeld in artikel 53ter, 1° van het Wetboek;

1°/1 de belasting over de toegevoegde waarde waarvan de opeisbaarheid blijkt uit de aangifte bedoeld in artikel 18, § 8, eerste lid, van het koninklijk besluit nr. 1 van 29 december 1992 met betrekking tot de voldoening van de belasting over de toegevoegde waarde;

2° de administratieve geldboeten voor het te laat indienen van die aangiften;

3° de administratieve geldboeten en de interest verschuldigd overeenkomstig artikel 91, § 1 van het Wetboek, voor het laattijdig betalen van de belasting waarvan de opeisbaarheid uit die aangiften blijkt.

#### Art. 11
(De tekst van KB nr. 24, artikel 11, werd gewijzigd met ingang van 01.01.2020 (Art. 33, KB 09.12.2019, B.S. 16.12.2019 – Ed. 2, pg. 113850))

De betalingen, andere dan diegene die op de postrekening van "btw-ontvangsten Brussel" moeten worden gedaan, andere dan deze bedoeld in de artikelen 9 en 10, of anderen dan diegene die moeten worden gedaan aan de Algemene Administratie van de Douane en Accijnzen overeenkomstig artikel 7, § 1, eerste lid van het koninklijk besluit nr. 7 met betrekking tot de invoer van goederen voor de toepassing van de belasting over de toegevoegde waarde, onder voorbehoud van de toepassing van artikel 1 van het koninklijk besluit nr. 13 met betrekking tot de regeling voor tabaksfabrikaten op het stuk van de belasting over de toegevoegde waarde, worden eveneens gedaan overeenkomstig hetgeen voorzien is in de artikelen 15 tot 17 van het Wetboek van de minnelijke en gedwongen invordering van fiscale en niet-fiscale schuldvorderingen.

#### Art. 12
(De tekst van KB nr. 24, artikel 12, werd opgeheven met ingang van 01.12.2019 (Art. 36, KB 17.02.2019, B.S. 08.03.2019, pg. 25174))

#### Art. 13
(De tekst van KB nr. 24, artikel 13, werd opgeheven met ingang van 01.12.2019 (Art. 36, KB 17.02.2019, B.S. 08.03.2019, pg. 25174))

### Onderafdeling 3
Betaling op de postrekening van "Mini One Stop Shop - VAT BE”.

(De tekst van Onderafdeling 3, werd vervangen met ingang van 01.01.2015 (Art. 7, KB 05.07.2015, B.S. 10.07.2015, pg. 45614))

#### Art. 13bis
(De tekst van KB nr. 24, artikel 13bis, werd vervangen met ingang van 01.01.2015 (Art. 7, KB 05.07.2015, B.S. 10.07.2015, pg. 45614))

De betaling van de belasting bedoeld in de artikelen 58ter, § 5, derde lid en 58quater, § 5, vierde lid, van het Wetboek waarvan de opeisbaarheid blijkt uit de aangifte bedoeld in de

artikelen 58ter, § 5 en 58quater, § 5, van het Wetboek wordt gedaan op de postrekening BE78 6792 0036 2186 van "Mini One Stop Shop - VAT BE".

De betaling door de belastingschuldige op de postrekening BE78 6792 0036 2186 van "Mini One Stop Shop - VAT BE" wordt gedaan door storting of overschrijving met vermelding van de gestructureerde mededeling die hem werd ter kennis gebracht door de administratie. Zij heeft uitwerking op de datum bepaald overeenkomstig artikel 4, § 1.

### Onderafdeling 4
Betaling op de postrekening van "VAT on E-Services".

(De tekst van Onderafdeling 4, werd ingevoegd met ingang van 01.01.2015. (Art. 8, KB 05.07.2015, B.S. 10.07.2015, pg. 45614))

#### Art. 13ter
(De tekst van KB nr. 24, artikel 13ter, werd ingevoegd met ingang van 01.01.2015 (Art. 8, KB 05.07.2015, B.S. 10.07.2015, pg. 45614))

De betaling van de belasting bedoeld in artikel 58bis, § 2, 5°, van het Wetboek, waarvan de opeisbaarheid blijkt uit een aangifte bedoeld in artikel 58bis, § 2, 4°, van het Wetboek, zoals deze bepalingen van toepassing zijn tot en met 31 december 2014, met betrekking tot een tijdvak voorafgaand aan 1 januari 2015, moet worden gedaan op de postrekening BE89 6792 0034 2685 van "VAT on E-Services".

Wanneer een aangifte bedoeld in artikel 58bis, § 2, 4°, van het Wetboek wordt ingediend na 1 januari 2015 en betrekking heeft op een tijdvak dat deze datum voorafgaat, moet de betaling van de belasting worden gedaan op de in het eerste lid vermelde postrekening.

Wanneer verbeteringen moeten worden aangebracht aan een aangifte met betrekking tot een tijdvak voorafgaand aan 1 januari 2015, waardoor de belasting aan de Schatkist moet worden gestort, wordt de betaling eveneens gedaan op de in het eerste lid daartoe voorziene postrekening.

## AFDELING 2
Betaling vastgesteld door middel van het elektronische systeem PLDA van de Algemene Administratie van de Douane en Accijnzen.

(Het opschrift van KB nr. 24, afdeling 2, werd gewijzigd met ingang van 16.05.2014 (Art. 23, KB 24.01.2015, B.S. 20.02.2015 – Ed. 2, pg. 13872))

#### Art. 14
(De tekst van KB nr. 24, artikel 14, is opgeheven met ingang van 01.01.2002 (Art.10, 2°, KB 13.07.2001))

#### Art. 15
(De tekst van KB nr. 24, artikel 15, § 1, inleidende zin, werd gewijzigd met ingang van 16.05.2014 (Art. 24, KB 24.01.2015, B.S. 20.02.2015 – Ed. 2, pg. 13872))

§ 1. De betaling van de ter zake van invoer verschuldigde belasting aan de Algemene Administratie van de Douane en Accijnzen wordt vastgesteld aan de hand van één van de navolgende vermeldingen die op de aangifte voor het verbruik wordt aangebracht door middel van het elektronisch systeem PLDA dat die administratie gebruikt om invoeraangiften te aanvaarden:

- de vermelding ″contant betaald″ gevolgd door het totaalbedrag van de betaalde belastingen, wanneer de belasting contant wordt betaald;

- de vermelding ″uitstel van betaling″ gevolgd door het totaalbedrag van de betaalde belastingen, wanneer de betaling van de belasting wordt uitgesteld met toepassing van artikel 5, § 2, van het koninklijk besluit nr. 7 met betrekking tot de invoer van goederen voor de toepassing van de belasting over de toegevoegde waarde.

§ 2. Door of vanwege de Minister van Financiën mag echter, in de bijzondere gevallen en onder de voorwaarden door hen te bepalen, worden toegestaan dat de voldoening van de ter zake van invoer verschuldigde BTW op een andere wijze wordt vastgesteld.

## AFDELING 3
Betaling bestemd voor het kantoor van de door of vanwege de
Minister van Financiën met de invordering belaste ambtenaar.

#### Art. 16
(De tekst van KB nr. 24, artikel 16, wordt opgeheven met ingang van 01.12.2019 (Art. 37, KB 17.02.2019, B.S. 08.03.2019, pg. 25174))

#### Art. 17
(De tekst van KB nr. 24, artikel 17, wordt opgeheven met ingang van 01.12.2019 (Art. 37, KB 17.02.2019, B.S. 08.03.2019, pg. 25174))

#### Art. 18
(De tekst van KB nr. 24, artikel 18, wordt opgeheven met ingang van 01.12.2019 (Art. 37, KB 17.02.2019, B.S. 08.03.2019, pg. 25174))

#### Art. 19
(De tekst van KB nr. 24, artikel 19, wordt opgeheven met ingang van 01.12.2019 (Art. 37, KB 17.02.2019, B.S. 08.03.2019, pg. 25174))

## AFDELING 4
 Betaling op een douane of accijnskantoor voor andere dan bij invoer verschuldigde belasting over de toegevoegde waarde.

#### Art. 20
(De tekst van KB nr. 24, artikel 20, is van toepassing met ingang van 01.01.1993 (KB 29.12.1992))

De betaling van de verschuldigde belasting die ter uitvoering van het koninklijk besluit nr. 46 tot regeling van de aangifte van de intracommunautaire verwerving van vervoermiddelen en van de betaling van de ter zake verschuldigde BTW en het koninklijk besluit nr. 51 met betrekking tot de vereenvoudigingsregeling voor intracommunautaire verwervingen van accijnsprodukten op het stuk van de belasting over de toegevoegde waarde, op een douane of accijnskantoor moet worden verricht geschiedt in speciën of door overschrijving op de postrekening van dit kantoor of op een andere wijze bepaald door of vanwege de Minister van Financiën in de door of namens hem te bepalen gevallen.

#### Art. 21
(De tekst van KB nr. 24, artikel 21, is van toepassing met ingang van 01.01.1993 (KB 29.12.1992))

De in artikel 20 bedoelde betalingen hebben uitwerking:

1° voor een betaling in speciën, op de datum van de betaling;

2° voor een overschrijving, de laatste werkdag die voorafgaat aan de datum van creditering van de postrekening van het kantoor volgens de documenten van de Post. Als werkdagen worden aangemerkt, alle andere dagen dan de zaterdagen, de zondagen en de wettelijke feestdagen;

Indien door of vanwege de Minister van Financiën overeenkomstig artikel 20 van dit besluit, een andere wijze van betalen wordt toegestaan, wordt door of vanwege hem eveneens de datum bepaald waarop de betaling uitwerking heeft.

## AFDELING 5
Slotbepalingen.

#### Art. 22
(De tekst van KB nr. 24, artikel 22, is van toepassing met ingang van 01.01.1993 (KB 29.12.1992))

Dit besluit vervangt het koninklijk besluit nr. 24 van 23 oktober 1970 met betrekking tot de voldoening van de belasting over de toegevoegde waarde.

#### Art. 23
(De tekst van KB nr. 24, artikel 23, is van toepassing met ingang van 01.01.1993 (KB 29.12.1992))

Dit besluit treedt in werking op 1 januari 1993.

#### Art. 24
(De tekst van KB nr. 24, artikel 24, is van toepassing met ingang van 01.01.1993 (KB 29.12.1992))

Onze Minister van Financiën is belast met de uitvoering van dit besluit.
