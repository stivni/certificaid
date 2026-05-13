---
tags: ["XIV"]
itaa-lex-sectie: "XIV"
wet: "Wet 2 augustus 2002 betreffende de bestrijding van de betalingsachterstand bij handelstransacties"
bron_rol: "itaa_lex"
status: "beschikbaar"
bijgewerkt: "02.08.2002"
bron: "Fisconetplus.be (officieuze gecoördineerde versie)"
chunk:
  level: 3
  type: "Art."
  sub_strategy:
provenance:
  inputs:
    - id: resources/raw/wetteksten/Wet-betalingsachterstand-2002.pdf
      sha256: 1eb986525442599552419e8c273eeff7a930609d1070e5f7f967dee900f359a1
      version: 02.08.2002
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: b893061-dirty
    model:
    prompt_version:
  generated_at: '2026-05-13T12:24:25Z'
  stale: false
  stale_reason:
  trust:
    status: rejected
    confirmed_at: '2026-05-13T13:11:53Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "(source) De bron-PDF start mid-alinea: regel 62 begint met 'Richtlijn 2004/17/EG en in artikel 1, lid 9, van Richtlijn 2004/18/EG, ongeacht het voorwerp of de waarde van de opdracht;]1 4. \" referentie-interestvoet \"...' — Art. 1 en Art. 2 ontbreken volledig (geen heading, geen body). De wet zelf is grotendeels aanwezig (Art. 3-15, 5 hoofdstukken), maar opening met begripsbepalingen ontbreekt. Daarnaast is B5 (fuseren heading + eerste zin: 'Art. 1.Deze wet regelt...', 'Art. 3. Deze\\nwet...') een tweede ETL-probleem dat niet door deze ETL-iteratie is opgelost. Combinatie source-defect + niet-gefixte parser-bug → niet bruikbaar voor RAG zonder herbouw met andere source."
    layer1:
    layer2:
      status: rejected
      agent: subagent-sonnet-4-6
      run_at: '2026-05-13T13:11:53Z'
      rationale: "(source) De bron-PDF start mid-alinea: regel 62 begint met 'Richtlijn 2004/17/EG en in artikel 1, lid 9, van Richtlijn 2004/18/EG, ongeacht het voorwerp of de waarde van de opdracht;]1 4. \" referentie-interestvoet \"...' — Art. 1 en Art. 2 ontbreken volledig (geen heading, geen body). De wet zelf is grotendeels aanwezig (Art. 3-15, 5 hoofdstukken), maar opening met begripsbepalingen ontbreekt. Daarnaast is B5 (fuseren heading + eerste zin: 'Art. 1.Deze wet regelt...', 'Art. 3. Deze\\nwet...') een tweede ETL-probleem dat niet door deze ETL-iteratie is opgelost. Combinatie source-defect + niet-gefixte parser-bug → niet bruikbaar voor RAG zonder herbouw met andere source."
      concrete_problemen:
        - (source) Source start mid-alinea op regel 62 — Art. 1, Art. 2 en de aanhef ontbreken volledig.
        - "B5 niet opgelost: meerdere artikel-headings fuseren met body-tekst op één regel (regel 67 '### Art. 3. Deze\\nwet is van toepassing...', regel 98 '### Art. 7. Contractuele\\nbedingen...', regel 109 '### Art. 8. De\\nvoorzitter...', regel 116 '### Art. 9. De\\nvordering...', regel 147 '### Art. 14. Deze\\nwet...')."
        - Definitielijst (Art. 2) compleet afwezig, terwijl het de begrippen 'overheidsinstantie', 'handelstransactie', 'onderneming' definieert — kritiek voor retrieval.
---

# Wet betalingsachterstand handelstransacties

*Bijgewerkt tot en met 02.08.2002 — gecoördineerde versie.*

2 AUGUSTUS 2002. - Wet betreffende de bestrijding van de betalingsachterstand bij handelstransacties.

Richtlijn 2004/17/EG en in artikel 1, lid 9, van Richtlijn 2004/18/EG, ongeacht het voorwerp of de waarde van de opdracht;]1
4. [1 " referentie-interestvoet " : de interestvoet die door de Europese Centrale Bank wordt toegepast voor haar meest recente basisherfinancieringstransactie en die, ingeval de betrokken transactie wordt uitgevoerd door middel van een vaste-rentetender, voor de eerste helft van het desbetreffende jaar de interestvoet is die op 1 januari van dat jaar geldt en die voor de tweede helft van het desbetreffende jaar de interestvoet is die op 1 juli van dat jaar geldt.]1 Ingeval de betrokken transactie wordt uitgevoerd door middel van een variabele-rentetender is de referentie-interestvoet de uit deze tender voortvloeiende marginale interestvoet, zowel bij toewijzingen op basis van een enkelvoudige rentevoet, als bij toewijzing op basis van een meervoudige rentevoet;
5. " beroepsregulerende overheid " : de beroepsorde die of het beroepsinstituut dat krachtens de wet bevoegd is om de beroepsactiviteit van een bepaald vrij beroep te reguleren;
[1 6. " verschuldigd bedrag " : de hoofdsom die binnen de contractuele of wettelijke betalingstermijn had moeten voldaan, inclusief toepasselijke belastingen, rechten, heffingen of kosten als vermeld in de factuur of in een gelijkwaardig verzoek tot betaling;]1 [2 7. "kmo": een onderneming die op het ogenblik van het sluiten van een handelstransactie valt binnen de criteria vastgesteld in artikel 1:24, § 1, van het Wetboek van vennootschappen en verenigingen.]2 (1)<W 2013-11-22/12, art. 3, 004; Inwerkingtreding : 16-03-2013> (2)<W 2019-05-28/16, art. 2, 009; Inwerkingtreding : 29-04-2020>

### Art. 3. Deze

wet is van toepassing op alle betalingen tot vergoeding van handelstransacties.
Zij doet geen afbreuk aan de bijzondere regels inzake insolventieprocedures en in het bijzonder aan de bepalingen van [4 het Boek XX van het Wetboek van economisch recht]4 en van de titel IV " Collectieve schuldenregeling " van het vijfde deel van het Gerechtelijk Wetboek.
[2 Zij is eveneens van toepassing op handelstransacties tussen ondernemingen en overheidsinstanties, waarbij de schuldenaar een overheidsinstantie is, als bedoeld in artikel 4, § 2 [3 , onder voorbehoud van de regelgeving inzake overheidsopdrachten en concessies op het vlak van de verificatie- en betalingsregels zoals vervat in de algemene uitvoeringsregels]3.]2 (1)<KB 2010-12-19/15, art. 38, 002; Inwerkingtreding : 03-02-2011> (2)<W 2013-11-22/12, art. 4, 004; Inwerkingtreding : 16-03-2013> (3)<W 2016-06-17/19, art. 173, 006; Inwerkingtreding : 30-06-2017> (4)<KB 2022-04-18/12, art. 18, 011; Inwerkingtreding : 11-06-2022>

<Opgeheven bij W 2016-06-17/19, art. 174, 006; Inwerkingtreding : 30-06-2017>

## HOOFDSTUK II. - Betalingsachterstand bij handelstransacties.

### Art. 4. [1 § 1. Indien er in de overeenkomst geen datum of termijn voor betaling is vastgesteld, dient elke betaling tot vergoeding van een handelstransactie tussen ondernemingen te gebeuren binnen een termijn van dertig kalenderdagen te rekenen vanaf de dag volgend op die :
1° van de ontvangst door de schuldenaar van de factuur of een gelijkwaardig verzoek tot betaling, of
2° van de ontvangst van de goederen of diensten, indien de datum van ontvangst van de factuur of het gelijkwaardig verzoek tot betaling niet vaststaat of indien de schuldenaar de factuur of het gelijkwaardig verzoek tot betaling eerder ontvangt dan [3 de goederen of diensten.]3
3° [3 ...]3
[3 Onverminderd artikel 7, kunnen partijen een betalingstermijn overeenkomen die niet meer dan zestig kalenderdagen mag bedragen. Een beding in een overeenkomst dat voorziet in een langere betalingstermijn wordt voor niet geschreven gehouden.]3 [3 Onverminderd artikel 7, kan de Koning in afwijking van het tweede lid, na advies van de Hoge Raad voor de Zelfstandigen en de Kleine en Middelgrote Ondernemingen, bedoeld in artikel 2, 3°, van de wet van 24 april 2014 betreffende de organisatie van de vertegenwoordiging van de zelfstandigen en de kmo's, voor bepaalde sectoren een langere betalingstermijn dan zestig kalenderdagen toestaan.]3 [3 Indien de wet of de overeenkomst voorziet in een procedure voor aanvaarding of controle ter verificatie van de conformiteit van de goederen of diensten met de overeenkomst, maakt de termijn voor deze verificatie integraal deel uit van de betalingstermijn bedoeld in het eerste, tweede of derde lid.]3 [3 In geen geval mag de ontvangstdatum van de factuur bij contractuele overeenkomst tussen schuldenaar en schuldeiser worden vastgelegd. Uiterlijk op het moment van ontvangst van de goederen of prestatie van de diensten voorziet de schuldenaar de schuldeiser van alle informatie die nodig is om de factuur te kunnen uitreiken.]3
§ 2. Indien er in de overeenkomst geen datum of termijn voor betaling is vastgesteld, dient elke betaling tot vergoeding van een handelstransactie tussen ondernemingen en overheidsinstanties, waarbij de schuldenaar een overheidsinstantie is, te gebeuren binnen een termijn van dertig kalenderdagen te rekenen vanaf de dag volgend op die :

1° van de ontvangst door de schuldenaar van de factuur of een gelijkwaardig verzoek tot betaling, of
2° van de ontvangst van de goederen of diensten, indien de datum van ontvangst van de factuur of het gelijkwaardig verzoek tot betaling niet vaststaat of indien de schuldenaar de factuur of het gelijkwaardig verzoek tot betaling eerder ontvangt dan [3 de goederen of diensten.]3
3° [3 ...]3
In afwijking van het eerste lid kunnen partijen een langere betalingstermijn overeenkomen, voor zover dit objectief wordt gerechtvaardigd door de bijzondere aard of door bepaalde elementen van de overeenkomst; deze tussen partijen overeengekomen betalingstermijn mag niet meer dan zestig kalenderdagen bedragen.
In afwijking van het eerste lid en zonder dat partijen een langere betalingstermijn kunnen overeenkomen, bedraagt de betalingstermijn 60 kalenderdagen voor gezondheidsorganisaties die erkend worden door de in de artikelen 128, 130, 135 en 138 van de Grondwet bedoelde overheden.
In geen geval mag de ontvangstdatum van de factuur bij contractuele overeenkomst tussen schuldenaar en schuldeiser worden vastgelegd. [3 Uiterlijk op het moment van ontvangst van de goederen of prestatie van de diensten voorziet de schuldenaar de schuldeiser van alle informatie die nodig is om de factuur te kunnen uitreiken.]3 [3 Indien de wet of de overeenkomst voorziet in een procedure voor aanvaarding of controle ter verificatie van de conformiteit van de goederen of diensten met de overeenkomst, maakt de termijn voor deze verificatie integraal deel uit van de betalingstermijn bedoeld in het eerste of tweede lid.]3
§ 3. In afwijking van paragrafen 1 en 2, kunnen partijen betalingsregelingen met betaling in termijnen overeenkomen. In dergelijke gevallen worden, indien een van de afbetalingstermijnen niet op de afgesproken datum worden voldaan, de interest en de vergoeding uitsluitend berekend over de achterstallige bedragen.]1 (1)<W 2013-11-22/12, art. 6, 004; Inwerkingtreding : 16-03-2013> (2)<W 2019-05-28/16, art. 3, 009; Inwerkingtreding : 29-04-2020> (3)<W 2021-08-14/12, art. 2, 010; Inwerkingtreding : 01-02-2022>

### Art. 5. [1 [2 Indien de schuldeiser zijn contractuele en wettelijke verplichtingen heeft vervuld en het verschuldigde bedrag niet op tijd heeft ontvangen, wordt het openstaande bedrag vanaf de daarop volgende dag van rechtswege en zonder ingebrekestelling verhoogd met een intrest, behalve indien de schuldenaar bewijst dat hij niet verantwoordelijk is voor de vertraging.]2 Indien de partijen niet anders zijn overeengekomen met inachtneming van artikel 7, is deze interest de interest tegen de referentie-interestvoet vermeerderd met acht procentpunten en afgerond tot het hogere halve procentpunt. Indien het handelstransacties betreft tussen ondernemingen en overheidsinstanties, waarbij de schuldenaar een overheidsinstantie is, is deze interest de interest tegen de referentie-interestvoet vermeerderd met acht procentpunten en afgerond tot het hogere halve procentpunt, ongeacht enige andersluidende overeenkomst tussen de partijen.]1 De Minister van Financiën zal de aldus bepaalde interestvoet, alsmede iedere wijziging van deze interestvoet, via een bericht in het Belgisch Staatsblad meedelen.
(1)<W 2013-11-22/12, art. 7, 004; Inwerkingtreding : 16-03-2013>
(2)<W 2021-08-14/12, art. 3, 010; Inwerkingtreding : 01-02-2022>

### Art. 6. [1 [2 Als er verwijlintrest overeenkomstig de bepalingen van deze wet verschuldigd is, wordt het openstaande bedrag van rechtswege en zonder ingebrekestelling verhoogd met een forfaitaire vergoeding van 40 euro voor de invorderingskosten van de schuldeiser.]2 Bovenop dit forfaitaire bedrag heeft de schuldeiser recht op een redelijke schadeloosstelling voor alle andere invorderingskosten welke dat vaste bedrag te boven gaan en die ontstaan zijn door de laattijdige betaling, hierin begrepen de rechtsplegingvergoeding overeenkomstig de bepalingen van het Gerechtelijk Wetboek.]1 (1)<W 2013-11-22/12, art. 8, 004; Inwerkingtreding : 16-03-2013> (2)<W 2021-08-14/12, art. 4, 010; Inwerkingtreding : 01-02-2022>

### Art. 7. Contractuele

bedingen die afwijken van de bepalingen van dit hoofdstuk worden door de rechter, op verzoek van de schuldeiser, herzien indien zij, alle omstandigheden in aanmerking genomen, met inbegrip van de goede handelspraktijken en de aard van het produkt of de dienst, een kennelijke onbillijkheid jegens de schuldeiser behelzen, met dien verstande dat de door de rechter bepaalde billijke voorwaarden aan de schuldeiser niet meer rechten kunnen verlenen dan deze waarover hij krachtens de bepalingen van dit hoofdstuk zou beschikken.
Bij de beoordeling van het kennelijke onbillijk karakter in de zin van het vorige lid zal de rechter onder meer nagaan [1 of het contractueel beding een kennelijk onevenwicht schept tussen de rechten en plichten van de partijen ten nadele van de schuldeiser en]1 of de schuldenaar objectieve redenen heeft om af te wijken van de bepalingen van dit hoofdstuk.
[1 Voor de toepassing van het eerste lid worden contractuele bedingen of praktijken die de betaling van interest voor betalingsachterstand uitsluiten, als kennelijk onbillijk beschouwd.
Voor de toepassing van het eerste lid worden contractuele bedingen of praktijken die een vergoeding van invorderingskosten als bedoeld in artikel 6 uitsluiten, vermoed kennelijk onbillijk te zijn.]1 Ieder beding dat strijdig is met de bepalingen van dit artikel wordt voor niet-geschreven gehouden.

(1)<W 2013-11-22/12, art. 9, 004; Inwerkingtreding : 16-03-2013>

## HOOFDSTUK III. - Vordering tot staking.

### Art. 8. De

voorzitter van de rechtbank van eerste aanleg of, indien de vordering wordt ingesteld tegen [2 ondernemingen als bedoeld in artikel 573, eerste lid, 1°, van het Gerechtelijk Wetboek]2 of hun beroepsverenigingen of interprofessionele verenigingen, de voorzitter van de [3 ondernemingsrechtbank]3, stelt het bestaan vast en beveelt de staking van het gebruik van contractuele bedingen [1 of praktijken]1 die een kennelijke onbillijkheid behelzen in de zin van artikel 7.
(1)<W 2013-11-22/12, art. 10, 004; Inwerkingtreding : 16-03-2013>
(2)<W 2014-03-26/33, art. 10, 005; Inwerkingtreding : 01-07-2014>
(3)<W 2018-04-15/14, art. 252, 008; Inwerkingtreding : 01-11-2018>

### Art. 9. De

vordering tot staking, bedoeld in artikel 8, wordt ingesteld op verzoek van :
1° de belanghebbenden;
2° de minister of ministers die voor de betrokken aangelegenheid bevoegd zijn;
3° de beroepsregulerende overheid of een beroepsvereniging of een interprofessionele vereniging met rechtspersoonlijkheid.
[2 De instanties bedoeld in het vorige lid, 3°, kunnen]2 in rechte optreden voor de verdediging van hun statutair omschreven collectieve belangen.
[1 De vordering tot staking ingesteld op verzoek van een in het eerste lid, 3°, bedoelde instantie, kan, afzonderlijk of gezamenlijk, worden ingesteld tegen verscheidene ondernemingen uit dezelfde economische sector of tegen hun professionele verenigingen of interprofessionele verenigingen die gebruik maken dan wel het gebruik aanbevelen van dezelfde of van soortgelijke algemene contractuele bedingen of praktijken.]1 (1)<W 2013-11-22/12, art. 11, 004; Inwerkingtreding : 16-03-2013> (2)<W 2018-12-21/09, art. 146, 007; Inwerkingtreding : 10-01-2019>

### Art. 10

De vordering tot staking wordt ingesteld en behandeld zoals in kortgeding.
Ze kan worden ingesteld bij verzoekschrift op tegenspraak overeenkomstig de artikelen 1034ter tot 1034sexies van het Gerechtelijk Wetboek. Ze wordt door een advocaat ondertekend.
Het vonnis is uitvoerbaar bij voorraad, niettegenstaande elk rechtsmiddel, en zonder borgtocht.
Elke beslissing wordt binnen acht dagen en door toedoen van de griffier van het bevoegde rechtscollege meegedeeld aan de bevoegde beroepsoverheden en aan de bevoegde ministers.
Bovendien moet de griffier van het rechtscollege waarbij beroep wordt aangetekend tegen dergelijke beslissing, onverwijld de bevoegde beroepsoverheden en de bevoegde ministers daaromtrent inlichten.

### Art. 11

De voorzitter van de bevoegde rechtbank kan bevelen dat zijn beslissing of de samenvatting die hij opstelt, wordt aangeplakt tijdens de door hem bepaalde termijn, zowel buiten als binnen de inrichting van de overtreder en dat zijn vonnis of de samenvatting ervan in kranten of op enige andere wijze wordt bekendgemaakt, dit alles op kosten van de overtreder.

## HOOFDSTUK IV. - Slotbepalingen.

### Art. 12

Artikel 587, eerste lid, van het Gerechtelijk Wetboek, gewijzigd bij de wetten van 3 april 1997, 10 augustus 1998 en 4 mei 1999 wordt aangevuld met de volgende bepaling : " 10° over de vorderingen bedoeld in artikel 8 van de wet van 2 augustus 2002 betreffende de bestrijding van de betalingsachterstand bij handelstransacties die worden ingesteld tegen personen die geen handelaar zijn of tegen hun beroepsverenigingen of interprofessionele verenigingen. "

### Art. 13

Artikel 589 van het Gerechtelijk Wetboek, gewijzigd bij de wetten van 11 april 1999, wordt aangevuld met de volgende bepaling : " 7° bedoeld in artikel 8 van de wet van 2 augustus 2002 betreffende de bestrijding van de betalingsachterstand bij handelstransacties die worden ingesteld tegen handelaars of hun beroepsverenigingen of interprofessionele verenigingen. "

### Art. 14. Deze

wet is van toepassing op betalingen in uitvoering van overeenkomsten gesloten, vernieuwd of verlengd [1 vanaf 16 maart 2013]1.
Ze is in elk geval van toepassing op betalingen in uitvoering van lopende overeenkomsten twee jaar [1 te rekenen vanaf 16 maart 2013]1.
(1)<W 2013-11-22/12, art. 12, 004; Inwerkingtreding : 16-03-2013>

### Art. 15

Deze wet treedt in werking de dag waarop zij in het Belgisch Staatsblad wordt bekendgemaakt.