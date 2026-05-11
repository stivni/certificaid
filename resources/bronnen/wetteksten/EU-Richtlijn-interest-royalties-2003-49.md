---
bijgewerkt: 26.06.2003
bron: ejustice.just.fgov.be (gecoördineerde versie)
bron_rol: itaa_lex
chunk:
  level: 2
  sub_strategy:
  type: Art.
itaa-lex-sectie: X
provenance:
  inputs:
    - id: resources/raw/wetteksten/EU-Richtlijn-interest-royalties-2003-49.pdf
      sha256: c84f67e63325e8fac7258bd751f5feef71fef11e23d6c5c0885349e65b5faf58
      version: 26.06.2003
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: 11f9196
    model:
    prompt_version:
  generated_at: '2026-05-11T16:56:15Z'
  stale: false
  stale_reason:
  trust:
    status: needs-rework
    confirmed_at: '2026-05-11T16:56:58Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "A1: paginakoppen van het Publicatieblad ('26.6.2003 L 157/49 Publicatieblad van de Europese Unie NL', idem /50, /51, /52, /53, /54) staan als plain-text regels in de body verspreid — klassiek PDF-kolom-artefact. A7: de aanhef-tekst op regel 55 ('betreffende een gemeenschappelijke belastingregeling ...') is een duplicaat van de H1-titel: bij 2-kolom extractie is de richtlijn-koptekst na de pagina-header opnieuw binnengelopen. Verder is artikel 1 lid 2 volledig ontbrekend (spring van lid 1 naar lid 3 op regel 105)."
    layer1:
      file_size_chars: 23404
      flags: []
      heading_count: 11
      max_section_chars: 6633
      run_at: '2026-05-11T16:52:50Z'
      run_id: 20260511-165250
      status: pass
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-11T16:56:58Z'
      rationale: "A1: paginakoppen van het Publicatieblad ('26.6.2003 L 157/49 Publicatieblad van de Europese Unie NL', idem /50, /51, /52, /53, /54) staan als plain-text regels in de body verspreid — klassiek PDF-kolom-artefact. A7: de aanhef-tekst op regel 55 ('betreffende een gemeenschappelijke belastingregeling ...') is een duplicaat van de H1-titel: bij 2-kolom extractie is de richtlijn-koptekst na de pagina-header opnieuw binnengelopen. Verder is artikel 1 lid 2 volledig ontbrekend (spring van lid 1 naar lid 3 op regel 105)."
      concrete_problemen:
        - regel: 53
          categorie: A1
          type: form-feed
          voorbeeld: 26.6.2003 L 157/49 Publicatieblad van de Europese Unie NL
        - regel: 55
          categorie: A7
          type: scrambled-words
          voorbeeld: betreffende een gemeenschappelijke belastingregeling inzake uitkeringen van interest en royalty's...
        - regel: 83
          categorie: A7
          type: scrambled-words
          voorbeeld: "RICHTLIJN 2003/49/EG VAN DE RAAD\n\nvan 3 juni 2003\n\nbron of door aanslag wordt geïnd..."
        - regel: 103
          categorie: A1
          type: form-feed
          voorbeeld: 26.6.2003 L 157/50 Publicatieblad van de Europese Unie NL
        - regel: 105
          categorie: D2
          type: missing-section
          voorbeeld: Artikel 1 lid 2 ontbreekt volledig (spring van lid 1 naar lid 3)
        - regel: 139
          categorie: A1
          type: form-feed
          voorbeeld: 26.6.2003 L 157/51 Publicatieblad van de Europese Unie NL
        - regel: 211
          categorie: A1
          type: form-feed
          voorbeeld: 26.6.2003 L 157/52 Publicatieblad van de Europese Unie NL
        - regel: 269
          categorie: A1
          type: form-feed
          voorbeeld: 26.6.2003 L 157/53 Publicatieblad van de Europese Unie NL
        - regel: 307
          categorie: A1
          type: form-feed
          voorbeeld: 26.6.2003 L 157/54 Publicatieblad van de Europese Unie NL
status: beschikbaar
tags:
  - X
  - '2.8'
wet: Richtlijn 2003/49/EG van de Raad van 3 juni 2003 betreffende een gemeenschappelijke belastingregeling inzake uitkeringen van interest en royalty's tussen verbonden ondernemingen van verschillende lidstaten
---

# Richtlijn 2003/49/EG van de Raad van 3 juni 2003 betreffende een gemeenschappelijke belastingregeling inzake uitkeringen van interest en royalty's tussen verbonden ondernemingen van verschillende lidstaten

*Bijgewerkt tot en met 26.06.2003 — gecoördineerde versie.*

26.6.2003 L 157/49 Publicatieblad van de Europese Unie NL

betreffende een gemeenschappelijke belastingregeling inzake uitkeringen van interest en royalty's tussen verbonden ondernemingen van verschillende lidstaten

DE RAAD VAN DE EUROPESE UNIE,

Gelet op het Verdrag tot oprichting van de Europese Gemeen- schap, en met name op artikel 94,

Gezien het voorstel van de Commissie ( 1 ),

Gezien het advies van het Europees Parlement ( 2 ),

Gezien het advies van het Europees Economisch en Sociaal Comité ( 3 ),

Overwegende hetgeen volgt:

(1) In een interne markt die de kenmerken van een binnen- landse markt heeft, zouden transacties tussen onderne- mingen van verschillende lidstaten niet aan minder gunstige belastingvoorschriften onderworpen moeten zijn dan die welke voor soortgelijke transacties tussen ondernemingen van eenzelfde lidstaat gelden.

(2) Met betrekking tot uitkeringen van interest en royalty's wordt thans niet aan deze eis voldaan; de nationale belastingwetten, in voorkomend geval in samenhang met bilaterale of multilaterale overeenkomsten, kunnen niet altijd waarborgen dat dubbele belasting wordt geëlimi- neerd en de toepassing ervan plaatst de betrokken onder- nemingen vaak voor belastende administratieve formali- teiten en kasmiddelenproblemen.

(3) Er moet worden gewaarborgd dat uitkeringen van inte- rest en royalty's eenmaal in een lidstaat worden belast.

(4) De afschaffing van de belasting op uitkeringen van inte- rest en royalty's in de lidstaat waar zij ontstaan, ongeacht of deze door inhouding aan de bron of door aanslag wordt geïnd, is het geschiktste middel om deze formali- teiten en problemen uit te bannen en een gelijke fiscale behandeling van nationale en transnationale transacties te waarborgen. Deze belasting moet met name worden afgeschaft voor uitkeringen tussen verbonden onderne- mingen van verschillende lidstaten en tussen vaste inrichtingen van deze ondernemingen.

(5) De regelingen dienen uitsluitend van toepassing te zijn op het eventuele bedrag aan interest of royalty's dat zonder een bijzondere verhouding tussen de betaler en de uiteindelijk gerechtigde zou zijn overeengekomen.

(6) Het mag de lidstaten bovendien niet worden belet passende maatregelen ter bestrijding van fraude of misbruik te nemen.

(7) Aan Griekenland en Portugal moet om begrotingsre- denen een overgangsperiode worden toegestaan gedu- rende welke zij de belasting op uitkeringen van interest en royalty's, ongeacht of deze door inhouding aan de

RICHTLIJN 2003/49/EG VAN DE RAAD

van 3 juni 2003

bron of door aanslag wordt geïnd, geleidelijk kunnen verlagen, totdat zij het bepaalde in artikel 1 kunnen toepassen.

(8) Spanje heeft een plan ter bevordering van het Spaanse technologische potentieel gelanceerd en moet om begro- tingsredenen de mogelijkheid krijgen tijdens een over- gangsperiode het bepaalde in artikel 1 inzake uitkeringen van royalty's niet toe te passen.

(9) De Commissie moet drie jaar na de datum waarop de richtlijn moet zijn omgezet, verslag aan de Raad uitbrengen over de werking van deze richtlijn, in het bijzonder met het oog op uitbreiding van de werkings- sfeer tot andere vennootschappen en ondernemingen en om de strekking van de definitie van interest en royalty's te herzien in het belang van de noodzakelijke conver- gentie van de bepalingen betreffende interest en royalty's in de nationale wetgeving en in bilaterale of multilaterale overeenkomsten ter voorkoming van dubbele belasting.

(10) Aangezien de doelstelling van het overwogen optreden, namelijk het opstellen van een gemeenschappelijke belastingregeling inzake uitkeringen van interest en royalty's tussen verbonden ondernemingen van verschil- lende lidstaten, niet voldoende door de lidstaten kan worden verwezenlijkt en derhalve beter op het niveau van de Gemeenschap kan geschieden, kan de Gemeen- schap maatregelen vaststellen, overeenkomstig het beginsel van subsidiariteit zoals bedoeld in artikel 5 van het Verdrag. Overeenkomstig het beginsel van evenredig- heid zoals bedoeld in genoemd artikel, gaat deze richtlijn niet verder dan hetgeen noodzakelijk is om die doelstel- ling te bereiken,

HEEFT DE VOLGENDE RICHTLIJN VASTGESTELD:

###### Artikel 1

Werkingssfeer en procedure

1. Uitkeringen van interest of royalty's die ontstaan in een lidstaat, worden vrijgesteld van alle belastingen in die bronstaat (door inhouding dan wel door aanslag), op voorwaarde dat een onderneming van een andere lidstaat, of een in een andere lidstaat gelegen vaste inrichting van een onderneming van een lidstaat, de uiteindelijk gerechtigde tot de interest of de royalty's is.

26.6.2003 L 157/50 Publicatieblad van de Europese Unie NL

3. Een vaste inrichting wordt alleen als uitbetaler van inte- rest of royalty's behandeld voorzover de betrokken uitkeringen voor die vaste inrichting in de lidstaat waar zij gelegen is, een aftrekbare bedrijfsuitgave vormen.

4. Een onderneming van een lidstaat wordt alleen als uitein- delijk gerechtigde tot interest of royalty's behandeld indien zij de betrokken uitkeringen te eigen gunste ontvangt, en niet als bemiddelende instantie, bijvoorbeeld als tussenpersoon, trustee of gemachtigde van een derde.

5. Een vaste inrichting wordt behandeld als uiteindelijk gerechtigde tot interest of royalty's:

a) voorzover de schuldvordering, het recht, het gebruik of de informatie ten aanzien waarvan uitkeringen van interest of royalty's ontstaan, daadwerkelijk verband houdt met die vaste inrichting, en

b) voorzover de uitkeringen van interest of royalty's inkomsten zijn ten aanzien waarvan zij in de lidstaat waarin zij gelegen is, onderworpen is aan één van de in artikel 3, onder a), punt iii), genoemde belastingen of, in het geval van België, aan de belasting der niet-verblijfhouders/impôt des non-rési- dents, en in het geval van Spanje aan de Impuesto sobre la Renta de no Residentes, dan wel aan ongeacht welke gelijke of in wezen gelijksoortige belasting die na de datum van inwerkingtreding van deze richtlijn in aanvulling op of in de plaats van die bestaande belastingen wordt geheven.

6. Indien een vaste inrichting van een onderneming van een lidstaat als betaler van of als uiteindelijk gerechtigde tot interest of royalty's wordt behandeld, wordt geen ander deel van de onderneming voor de toepassing van dit artikel als betaler van of als uiteindelijk gerechtigde tot de betrokken interest of royal- ty's behandeld.

7. Dit artikel vindt alleen toepassing indien de onderneming die de betaler van interest of royalty's is, of de onderneming waarvan de vaste inrichting als zodanig wordt behandeld, een verbonden onderneming is van de onderneming die de uitein- delijk gerechtigde is of waarvan de vaste inrichting wordt behandeld als de uiteindelijk gerechtigde tot de betrokken inte- rest of royalty's.

8. Dit artikel vindt geen toepassing wanneer interest of royalty's wordt respectievelijk worden uitbetaald door of aan een in een derde land gelegen vaste bedrijfsvestiging van een onderneming van een lidstaat en de onderneming haar bedrijf geheel of gedeeltelijk uitoefent door middel van die vaste bedrijfsvestiging.

10. Een lidstaat heeft de mogelijkheid om deze richtlijn niet toe te passen op een onderneming van een andere lidstaat of op een vaste inrichting van een onderneming van een andere lidstaat indien de in artikel 3, onder b), genoemde voorwaarden niet vervuld waren gedurende een ononderbroken periode van ten minste twee jaar.

11. De bronstaat kan eisen dat op het tijdstip van uitbetaling van de interest of royalty's door middel van een attest wordt aangetoond dat de voorwaarden van dit artikel en van artikel 3 vervuld zijn. Indien op het tijdstip van uitbetaling niet is aange- toond dat de voorwaarden van dit artikel vervuld zijn, staat het de lidstaat vrij inhouding van bronbelasting op te leggen.

12. De bronstaat mag aan vrijstelling uit hoofde van deze richtlijn de voorwaarde verbinden dat hij ingevolge een attest dat de voorwaarden van dit artikel en van artikel 3 zijn vervuld, een besluit heeft genomen op grond waarvan op dat ogenblik vrijstelling kan worden verleend. Het vrijstellingsbesluit moet uiterlijk drie maanden na de afgifte van het attest en de verstrekking van de bewijsstukken waarom de bronstaat redelij- kerwijze kan verzoeken, worden genomen en heeft vervolgens een geldigheidsduur van ten minste een jaar.

13. Voor de toepassing van de leden 11 en 12 heeft het attest voor elke overeenkomst die aan de uitkering ten grond- slag ligt, een geldigheidsduur van ten minste een jaar tot ten hoogste drie jaar vanaf de datum van afgifte; het behelst de volgende gegevens:

a) een bewijs van de fiscale woonplaats van de ontvangende onderneming en, in voorkomend geval, van het bestaan van een vaste inrichting, afgegeven door de belastingautoriteit van de lidstaat waar de ontvangende onderneming haar fiscale woonplaats heeft of waar de vaste inrichting gelegen is;

b) een verklaring dat de ontvangende onderneming de uitein- delijk gerechtigde is zoals bedoeld in lid 4, dan wel dat de voorwaarden van lid 5 vervuld zijn indien de ontvanger van de uitkering een vaste inrichting is;

c) een verklaring dat de voorwaarden van artikel 3, onder a), punt iii), voor de ontvangende onderneming vervuld zijn;

d) een verklaring dat de ontvangende onderneming houdster is van een minimumdeelneming dan wel van een minimum- percentage van de stemrechten overeenkomstig artikel 3, onder b);

e) de vermelding hoelang die deelneming of stemrechten bestaan.

26.6.2003 L 157/51 Publicatieblad van de Europese Unie NL

14. Indien de voorwaarden voor vrijstelling niet langer vervuld zijn, meldt de ontvangende onderneming of vaste inrichting dit onverwijld aan de uitbetalende onderneming of vaste inrichting en, indien de bronstaat dit eist, aan de bevoegde autoriteit van die staat.

15. Indien de uitbetalende onderneming of vaste inrichting bronbelasting waarvoor op grond van dit artikel vrijstelling moet worden verleend, heeft ingehouden, kan een vordering tot teruggave van die bronbelasting worden ingesteld. De lidstaat kan de in lid 13 genoemde gegevens opeisen. Het verzoek om teruggave moet binnen de gestelde termijn worden ingediend. Die termijn bedraagt ten minste twee jaar en gaat in op de datum waarop de interest of royalty's uitgekeerd zijn.

16. De bronstaat gaat binnen een jaar na ontvangst van het verzoek en van de bewijsstukken waarom hij redelijkerwijze kan verzoeken, over tot teruggave van de ten onrechte inge- houden bronbelasting. Indien de bronbelasting niet binnen die termijn is teruggegeven, heeft de ontvangende onderneming of vaste inrichting bij het verstrijken van dat jaar recht op rente over de terug te geven belasting tegen de nationale rentevoet die in vergelijkbare gevallen krachtens het nationaal recht van de bronstaat wordt toegepast.

###### Artikel 2

Definitie van interest en royalty's

Voor de toepassing van deze richtlijn wordt verstaan onder:

a) „interest”: inkomsten uit schuldvorderingen van welke aard dan ook, al dan niet verzekerd door hypotheek en al dan niet aanspraak gevend op een aandeel in de winst van de schuldenaar, en in het bijzonder inkomsten uit leningen en inkomsten uit obligaties of schuldbewijzen, daaronder begrepen de aan zodanige leningen, obligaties of schuldbe- wijzen verbonden premies en prijzen. In rekening gebrachte boete voor te late betaling wordt niet als interest aange- merkt;

b) „royalty's”: vergoedingen van welke aard dan ook voor het gebruik van, of voor het recht van gebruik van, een auteurs- recht op een werk op het gebied van letterkunde, kunst of wetenschap — daaronder begrepen bioscoopfilms en soft- ware — van een octrooi, een fabrieks- of handelsmerk, een tekening of model, een plan, een geheim recept of een geheime werkwijze, of voor inlichtingen omtrent ervaringen op het gebied van nijverheid, handel of wetenschap; vergoe- dingen voor het gebruik van of voor het recht van gebruik van industriële, commerciële of wetenschappelijke uitrusting worden als royalty's aangemerkt.

###### Artikel 3

Definitie van onderneming, verbonden onderneming en vaste inrichting

Voor de toepassing van deze richtlijn wordt verstaan onder:

a) „onderneming van een lidstaat”, elke onderneming:

ii) die volgens de belastingwetgeving van een lidstaat wordt geacht in die lidstaat haar fiscale woonplaats te hebben en die niet volgens een met een derde land gesloten overeenkomst ter vermijding van dubbele inkomstenbe- lasting wordt geacht haar fiscale woonplaats buiten de Gemeenschap te hebben, en

iii) die onderworpen is aan een van de volgende belastingen of aan ongeacht welke gelijke of in wezen gelijksoortige belasting die na de datum van inwerkingtreding van deze richtlijn in aanvulling op of in de plaats van die bestaande belastingen wordt geheven:

— vennootschapsbelasting/impôt des sociétés in België;

— selskabsskat in Denemarken;

— Körperschaftsteuer in Duitsland;

— Φόρος εισοδήµατος νοµικών προσώπων in Grieken- land;

— impuesto sobre sociedades in Spanje;

— impôt sur les sociétés in Frankrijk;

— corporation tax in Ierland;

— imposta sul reddito delle persone giuridiche in Italië;

— impôt sur le revenu des collectivités in Luxemburg;

— vennootschapsbelasting in Nederland;

— Körperschaftsteuer in Oostenrijk;

— imposto sobre o rendimento das pessoas colectivas in Portugal;

— yhteisöjen tulovero/inkomstskatten för samfund in Finland;

— statlig inkomstskatt in Zweden;

— corporation tax in het Verenigd Koninkrijk;

b) iedere onderneming die ten minste daardoor met een tweede onderneming verbonden is doordat:

i) de eerste onderneming rechtstreeks een deelneming van ten minste 25 % in het kapitaal van de tweede onderne- ming heeft, dan wel

ii) de tweede onderneming rechtstreeks een deelneming van ten minste 25 % in het kapitaal van de eerste onder- neming heeft, dan wel

iii) een derde onderneming rechtstreeks een deelneming van ten minste 25 % in het kapitaal van zowel de eerste onderneming als de tweede onderneming heeft.

De deelnemingen mogen enkel ondernemingen betreffen die binnen de Gemeenschap gevestigd zijn.

De lidstaten hebben echter de mogelijkheid om het crite- rium van een minimumdeelneming in het kapitaal te vervangen door dat van een minimumpercentage van de stemrechten;

26.6.2003 L 157/52 Publicatieblad van de Europese Unie NL

###### Artikel 4

Uitsluiting van niet als interest of royalty's aan te merken uitkeringen

1. In de volgende gevallen behoeft de bronstaat de voordelen van deze richtlijn niet toe te kennen:

a) uitkeringen die volgens het recht van de bronstaat als winst- uitkering of terugbetaling van kapitaal worden behandeld;

b) uitkeringen uit schuldvorderingen die het recht geven deel te nemen in de winst van de schuldenaar;

c) uitkeringen uit schuldvorderingen die de schuldeiser het recht verlenen zijn recht op interest in te ruilen tegen het recht deel te nemen in de winst van de schuldenaar;

d) uitkeringen uit schuldvorderingen die geen bepalingen betreffende terugbetaling van de hoofdsom bevatten of waarvan de terugbetaling meer dan 50 jaar na de uitgifte- datum verschuldigd is.

2. Wanneer, ten gevolge van een bijzondere verhouding tussen de uitbetaler en de uiteindelijk gerechtigde van de inte- rest of royalty's of tussen hen beiden en een derde, het bedrag van de interest of royalty's hoger is dan het bedrag dat zonder een dergelijke verhouding door de uitbetaler en de uiteindelijk gerechtigde zou zijn overeengekomen, vindt deze richtlijn slechts toepassing op dit eventuele laatstgenoemde bedrag.

###### Artikel 5

Fraude en misbruiken

1. Deze richtlijn vormt geen beletsel voor de toepassing van nationale of verdragsrechtelijke voorschriften ter bestrijding van fraude en misbruiken.

2. Een lidstaat kan het genot van deze richtlijn ontzeggen of weigeren de richtlijn toe te passen in het geval van transacties met als voornaamste beweegreden of een van de voornaamste beweegredenen belastingfraude, belastingontwijking of misbruik.

###### Artikel 6

Overgangsregels voor Griekenland en Portugal

1. Griekenland en Portugal hebben de mogelijkheid om artikel 1 niet toe te passen tot de toepassingsdatum bedoeld in artikel 17, leden 2 en 3, van Richtlijn 2003/48/EG van de Raad van 3 juni 2003 betreffende belastingheffing op inkomsten uit spaargelden in de vorm van rentebetaling ( 1 ). Gedurende een overgangsperiode van acht jaar die op de genoemde datum begint, mag de belasting op uitkeringen van interest of royalty's aan een verbonden onderneming van een andere lidstaat of een in een andere lidstaat gelegen vaste inrichting van een verbonden onderneming van een lidstaat gedurende de eerste vier jaar ten hoogste 10 % en gedurende de laatste vier jaar ten hoogste 5 % bedragen.

Spanje heeft, alleen voor de uitkeringen van royalty's, de moge- lijkheid om artikel 1 niet toe te passen tot de toepassingsdatum bedoeld in artikel 17, leden 2 en 3, van Richtlijn 2003/48/EG. Gedurende een overgangsperiode van zes jaar die op de genoemde datum begint, mag de belasting op uitkeringen van royalty's aan een verbonden onderneming van een andere lidstaat of een in een andere lidstaat gelegen vaste inrichting van een verbonden onderneming van een lidstaat ten hoogste 10 % bedragen.

Hieraan is echter de voorwaarde verbonden dat belastingta- rieven die eventueel lager zijn dan die genoemd in de eerste twee alinea's en waarin wordt voorzien door bilaterale overeen- komsten tussen Griekenland, Spanje of Portugal en andere lidstaten, van toepassing blijven. Vóór het einde van elk van de genoemde overgangsperiodes kan de Raad, op voorstel van de Commissie, met eenparigheid van stemmen besluiten deze te verlengen.

2. Indien een onderneming van een lidstaat of een in die lidstaat gelegen vaste inrichting van een onderneming van een lidstaat interest of royalty's ontvangt van:

— een verbonden onderneming van Griekenland of Portugal,

— een verbonden onderneming van Spanje,

— een in Griekenland of Portugal gelegen vaste inrichting van een verbonden onderneming van een lidstaat, of

— een in Spanje gelegen vaste inrichting van een verbonden onderneming van een lidstaat,

staat de eerstgenoemde lidstaat toe dat een bedrag, gelijk aan de belasting die overeenkomstig lid 1 in Griekenland, Spanje of Portugal over die inkomsten is betaald, in mindering wordt gebracht op de belasting over de inkomsten van de onderne- ming of de vaste inrichting die deze inkomsten heeft ontvangen.

3. De in lid 2 bedoelde vermindering behoeft niet hoger te zijn dan het laagste van de volgende twee bedragen:

a) de belasting die in Griekenland, Spanje of Portugal verschul- digd is op grond van lid 1, of

b) het gedeelte van de belasting over de inkomsten van de onderneming of vaste inrichting die de interest of de royal- ty's heeft ontvangen, berekend voordat de vermindering is toegestaan, dat volgens de nationale wetgeving van de lidstaat van de onderneming of waar de vaste inrichting gelegen is, aan deze uitkeringen kan worden toegerekend.

###### Artikel 7

Uitvoering

26.6.2003 L 157/53 Publicatieblad van de Europese Unie NL

Wanneer de lidstaten deze bepalingen aannemen, wordt in die bepalingen naar de onderhavige richtlijn verwezen of wordt hiernaar verwezen bij de officiële bekendmaking van die bepa- lingen. De regels voor deze verwijzing worden vastgesteld door de lidstaten.

2. De lidstaten delen de Commissie de tekst van de belang- rijkste bepalingen van intern recht mee die zij op het onder deze richtlijn vallende gebied vaststellen. In deze mededeling verstrekken de lidstaten een concordantietabel, waaruit blijkt welke vastgestelde nationale bepalingen overeenkomen met de bepalingen van deze richtlijn.

###### Artikel 8

Herziening

Uiterlijk op 31 december 2006 brengt de Commissie aan de Raad verslag uit over de werking van de richtlijn, in het bijzonder met het oog op uitbreiding van de werkingssfeer tot andere vennootschappen en ondernemingen dan die bedoeld in artikel 3 en in de bijlage.

###### Artikel 9

Vrijwaringsclausule

Deze richtlijn laat de toepassing onverlet van nationale of verdragsbepalingen die verder reiken dan de bepalingen van deze richtlijn en gericht zijn op de afschaffing of matiging van dubbele belasting van interest en royalty's.

###### Artikel 10

Inwerkingtreding

Deze richtlijn treedt in werking op de dag van haar bekendma- king in het Publicatieblad van de Europese Unie .

###### Artikel 11

Adressaten

Deze richtlijn is gericht tot de lidstaten.

Gedaan te Luxemburg, 3 juni 2003.

Voor de Raad

De voorzitter

N. CHRISTODOULAKIS

26.6.2003 L 157/54 Publicatieblad van de Europese Unie NL

Lijst van ondernemingen die onder artikel 3, onder a), van de richtlijn vallen

a) Ondernemingen naar Belgisch recht, geheten naamloze vennootschap/société anonyme, commanditaire vennoot- schap op aandelen/société en commandite par actions, besloten vennootschap met beperkte aansprakelijkheid/société privée à responsabilité limitée, alsmede de publiekrechtelijke lichamen die privaatrechtelijk werkzaam zijn.

b) Ondernemingen naar Deens recht, geheten aktieselskab, anpartsselskab.

c) Ondernemingen naar Duits recht, geheten Aktiengesellschaft, Kommanditgesellschaft auf Aktien, Gesellschaft mit beschränkter Haftung, bergrechtliche Gewerkschaft.

d) Ondernemingen naar Grieks recht, geheten ανώνυµη εταιρία .

e) Ondernemingen naar Spaans recht, geheten sociedad anónima, sociedad comanditaria por acciones, sociedad de responsabilidad limitada, alsmede de publiekrechtelijke lichamen die privaatrechtelijk werkzaam zijn.

f) Ondernemingen naar Frans recht, geheten société anonyme, société en commandite par actions, société à responsabi- lité limitée, alsmede de openbare instellingen en ondernemingen met een industrieel of commercieel karakter.

g) Ondernemingen naar Iers recht, geheten public companies limited by shares or by guarantee, private companies limited by shares or by guarantee, institutions registered under the Industrial and Provident Societies Acts, of buil- ding societies registered under the Building Societies Acts.

h) Ondernemingen naar Italiaans recht, geheten: società per azioni, società in accomandita per azioni, società a respon- sabilità limitata, alsmede openbare en particuliere lichamen die industriële en commerciële activiteiten uitoefenen.

i) Ondernemingen naar Luxemburgs recht, geheten société anonyme, société en commandite par actions, société à responsabilité limitée.

j) Ondernemingen naar Nederlands recht, geheten naamloze vennootschap, besloten vennootschap met beperkte aansprakelijkheid.

k) Ondernemingen naar Oostenrijks recht, geheten Aktiengesellschaft, Gesellschaft mit beschränkter Haftung.

l) Handelsvennootschappen, burgerlijke vennootschappen met handelsvorm, coöperaties en openbare bedrijven opge- richt naar Portugees recht.

m) Ondernemingen naar Fins recht, geheten osakeyhtiö/aktiebolag, osuuskunta/andelslag, säästöpankki/sparbank en vakuutusyhtiö/försäkringsbolag.

n) Ondernemingen naar Zweeds recht, geheten aktiebolag, försäkringsaktiebolag.

o) Ondernemingen naar het recht van het Verenigd Koninkrijk.
