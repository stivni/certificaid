---
tags:
  - norm
  - itaa
naam: Norm Algemene Vereisten Intern Kwaliteitsmanagement
datum: 2025-09-03
type: norm
itaa-lex-sectie: XXI
toepassingsgebied: Alle ITAA-leden — kwaliteitssysteem voor het beroepskantoor
themas:
  - kwaliteitsmanagement
  - intern kwaliteitssysteem
  - kantoororganisatie
bron: beexcellentnl.itaa.be
bron_rol: interpretatief
chunk:
  level: 2
  type: '##'
  sub_strategy:
provenance:
  inputs:
    - id: beexcellentnl.itaa.be
      sha256:
      version:
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: 66b51a5-dirty
    model:
    prompt_version:
  generated_at: '2026-05-13T00:08:08Z'
  stale: false
  stale_reason:
  trust:
    status: needs-rework
    confirmed_at: '2026-05-13T00:12:30Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "A6/B5: de preamble (r50-99) bevat fragmentarische tekst met afgebroken zinnen door kolom-extractie (bv. 'belastingadviseur, en in het bijzonder de artikelen 3, 5, 6, 62 en 72 voor wat het' op r50 eindigt mid-zin). B4: 'CABINET' als all-caps label op r141 zonder ## prefix. B4: 'KANTOORNIVEAU' op r148 als standalone label. A6: r57 eindigt mid-zin 'cliëntenbestand en evenredig met de complexiteit van de opdrachten die hij uitvoert.' — zin begint elders. Secties als ## headings aanwezig maar de preamble is substantieel aangetast."
    layer1:
      status: pass
      run_id: 20260513-000913
      run_at: '2026-05-13T00:09:13Z'
      heading_count: 8
      max_section_chars: 3781
      file_size_chars: 13164
      flags: []
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-13T00:12:30Z'
      rationale: "A6/B5: de preamble (r50-99) bevat fragmentarische tekst met afgebroken zinnen door kolom-extractie (bv. 'belastingadviseur, en in het bijzonder de artikelen 3, 5, 6, 62 en 72 voor wat het' op r50 eindigt mid-zin). B4: 'CABINET' als all-caps label op r141 zonder ## prefix. B4: 'KANTOORNIVEAU' op r148 als standalone label. A6: r57 eindigt mid-zin 'cliëntenbestand en evenredig met de complexiteit van de opdrachten die hij uitvoert.' — zin begint elders. Secties als ## headings aanwezig maar de preamble is substantieel aangetast."
      concrete_problemen:
        - regel: 50
          categorie: A6
          type: other
          voorbeeld: belastingadviseur, en in het bijzonder de artikelen 3, 5, 6, 62 en 72 voor wat het (zin afgekapt mid-phrase)
        - regel: 141
          categorie: B4
          type: other
          voorbeeld: 'CABINET (all-caps label na ## ALGEMENE VEREISTEN VAN INTERN KWALITEITSMANAGEMENT OP)'
        - regel: 148
          categorie: B4
          type: other
          voorbeeld: KANTOORNIVEAU (standalone label als continuation van heading op r139-141)
---
## NORM ALGEMENE VEREISTEN VAN INTERN KWALITEITSMANAGEMENT

Inleiding RAAD VAN HET INSTITUUT VAN DE BELASTINGADVISEURS EN DE ACCOUNTANTS, belastingadviseur, en in het bijzonder de artikelen 3, 5, 6, 62 en 72 voor wat het

## Overwegende

- dat alle beroepsbeoefenaars hun beroepsactiviteit uitoefenen met toepassing van het wettelijk, normatief en reglementair
kader dat op hen van toepassing is (artikel 36, §1 van de wet van 17 maart 2019);

- dat de beroepsbeoefenaar hierbij zijn beroepsactiviteiten dient cliëntenbestand en evenredig met de complexiteit van de opdrachten die hij uitvoert.
Hij voorziet de gepaste organisatorische en financiële middelen. Hij zet personeel met
gepaste beroepskwalificaties adequaat in (artikel 38 van de wet van 17 maart 2019);

- dat in het kader van de kwaliteitstoetsing uitgevoerd door het ITAA, wordt nagegaan of de beroepsbeoefenaar over een systeem van interne kwaliteitsbeheersing beschikt (art. 27
juncto art. 34, 1° van het koninklijk besluit van 9 december 2019
tot vastlegging van een reglement inzake de kwaliteitstoetsing de belastingconsulenten en tot nadere regeling van het gebruik van de opdrachtbrief);

Deze norm beoogt de creatie van een normatief kader omtrent intern kwaliteitsmanagementsysteem voor de opdrachten in
overeenstemming met deze norm moeten gebeurd zijn uiterlijk op 1 januari 2026.

actieplan ontwikkeld om de beroepsbeoefenaars bij te staan bij het
implementeren van deze norm, meer bepaald door middel van artikels,
vormingen, video’s en niet-bindende tools die geleidelijk beschikbaar worden gesteld op de website van het IBA.

(IBA) heeft op 7 november 2023 een eerste versie van de ontwerpnorm Intern kwaliteitsmanagement goedgekeurd en per mail van 13
november 2023 aan de Hoge Raad bezorgd. Deze ontwerpnorm bestond uit twee delen: een Deel 1 (“Algemene vereisten van interne
kwaliteitsbeheersing op kantoorniveau”) en een Deel 2 (“Aanvullende
kwaliteitsdoelstellingen en vereisten ten aanzien van assurance opdrachten en aan assurance verwante opdrachten”).

Op 14 februari 2024 ontving het IBA het negatief advies van 13 februari
2024 van de Hoge Raad over het geheel van deze ontwerpnorm en het
verzoek om een aan zijn advies aangepaste versie opnieuw aan de Hoge Raad over te maken.

Op 19 juli 2024 bezorgde het IBA een tweede verzoek tot advies aan ontwerpnorm (Deel 1 en Deel 2).

Op 26 september 2024 vond een gedachtenwisseling plaats, waaruit
een aantal beleidsmatige punten naar voren kwamen op basis waarvan het IBA de ontwerpnorm wou aanpassen.

Op 6 januari 2025 bezorgde het IBA een derde verzoek tot advies aan

Op 3 februari 2025 ontving het IBA bijkomende vragen van de Hoge
Raad, welke door het ITAA bij brief van 10 maart 2025 beantwoord werden.

Op 2 juni 2025 ontving het IBA een gunstig advies omtrent het
zogenaamde Deel 1 van de ontwerpnorm (“Algemene vereisten van
intern kwaliteitsmanagement op kantoorniveau”), maar een negatief advies over Deel 2 van de ontwerpnorm (Aanvullende
kwaliteitsdoelstellingen en vereisten ten aanzien van assurance
opdrachten en aan assurance verwante opdrachten”). Met betrekking
ontving het IBA op 11 juli een schrijven van de HREB inzake de
precisering omtrent het begrip “level playing field”. Bij schrijven van 22 het begrip “level playing field” in het kader van een kwaliteitsmanagementssysteem ingeval van assurance en aan assurance verwante opdrachten.

vereisten van intern kwaliteitsmanagement op kantoorniveau, het Deel 1 van de aan de Hoge Raad bezorgde ontwerpnorm waarover een gunstig advies werd verleend door deze Hoge Raad.

## Definities

Beroepsbeoefenaar: de persoon bedoeld in artikel 2, 3° van de wet van 17 maart
2019 betreffende de beroepen van accountant en belastingadviseur.

Kantoor: de organisatorische eenheid waarbinnen een beroepsbeoefenaar
werkzaam is of waaraan een beroepsbeoefenaar verbonden is bedoeld in artikel
2, 12° van de wet van 17 maart 2019 betreffende de beroepen van accountant en belastingadviseur.

Kwaliteitsdoelstellingen: De gewenste resultaten met betrekking tot de
componenten van het kwaliteitsmanagementsysteem die door het kantoor moeten worden bereikt.

Kwaliteitsrisico: Een risico dat een redelijke kans heeft op:

(i) voorkomen; en
(ii) afzonderlijk, of in combinatie met andere risico's, het bereiken van één of meer kwaliteitsdoelstellingen negatief beïnvloedt.

Netwerk: Een grotere structuur bedoeld in artikel 2, 13° van de wet van 17 maart
2019 betreffende de beroepen van accountant en belastingadviseur:

a. die gericht is op samenwerking; en b. die duidelijk gericht is op winst- of kostendeling, of het delen van gemeenschappelijke eigendom, zeggenschap of bestuur, gemeenschappelijk beleidslijnen en procedures inzake
kwaliteitsmanagement, een gemeenschappelijke bedrijfsstrategie, het
gebruik van een gemeenschappelijke merknaam, of een aanzienlijk deel van de bedrijfsmiddelen.

Personeel: De vennoten en het personeel van het kantoor.

Kwaliteitsmanagementsysteem
1. Het kantoor dient een kwaliteitsmanagementsysteem op te zetten, te
implementeren en in werking te stellen. Het kantoor dient daarbij rekening te van de opdrachten die hij uitvoert.

## Eindverantwoordelijke(n) voor het kwaliteitsmanagementsysteem

2. Indien het kantoor bestaat uit een zelfstandige beroepsbeoefenaar, dan heeft
deze beroepsbeoefenaar deontologisch de eindverantwoordelijkheid en de verantwoordingsplicht voor het vaststellen en onderhouden van het kwaliteitsmanagementsysteem.

3. Indien het kantoor een erkende rechtspersoon is, dan dragen alle bestuurders
– beroepsbeoefenaars – deontologisch de eindverantwoordelijkheid en de verantwoordingsplicht voor het vaststellen en onderhouden van het kwaliteitsmanagementsysteem.

## ALGEMENE VEREISTEN VAN INTERN KWALITEITSMANAGEMENT OP

CABINET Doelstelling

4. De doelstelling van het kantoor is het opzetten, implementeren en in werking
stellen van een kwaliteitsmanagementsysteem dat aan het kantoor een redelijke
mate van zekerheid verschaft dat het kantoor en zijn personeel de
beroepsactiviteiten uitoefenen in overeenstemming met het van toepassing zijnde wettelijk, reglementair en normatief kader.

KANTOORNIVEAU

Vereisten

Governance en leiderschap

5. Het kantoor dient beleidslijnen en procedures vast te stellen om een interne
cultuur te stimuleren waarbinnen kwaliteit centraal staat bij de uitvoering van de opdrachten.

Relevante ethische voorschriften

6. Het kantoor dient zijn kwaliteitsmanagementsysteem zo in te richten dat dit een redelijke mate van zekerheid geeft dat:

(i) het kantoor en zijn personeel bij het vervullen van de aan hen toevertrouwde activiteiten of opdrachten handelen in volledige onafhankelijkheid;

(ii) het kantoor en zijn personeel bij het vervullen van de aan hen toevertrouwde opdrachten handelen met respect voor de beginselen van de deontologie, die minstens betrekking hebben op de
verantwoordelijkheid voor het openbaar belang, de integriteit en
objectiviteit, de vakbekwaamheid en zorgvuldigheid, het respect voor de vertrouwelijkheid en de professionaliteit;
(iii) er geen opdrachten worden aanvaard onder voorwaarden die een objectieve uitvoering daarvan in het gedrang zouden brengen of een belangenconflict zouden teweegbrengen.

Netwerkeisen of netwerkdiensten

7. Wanneer het kantoor tot een netwerk behoort, dient het kantoor een inzicht te verkrijgen, in voorkomend geval, in:

(a) de door het netwerk vastgestelde eisen met betrekking tot het kwaliteitsbeheersingssysteem van het kantoor, met inbegrip van eisen
voor het kantoor om middelen of diensten te implementeren of te
gebruiken die bedoeld zijn om te worden verstrekt, of anderszins worden verstrekt, door of via het netwerk (d.w.z. netwerkeisen);

(b) alle door het netwerk geleverde diensten of middelen die het kantoor verkiest te implementeren of te gebruiken bij de opzet, implementatie of
werking van het kwaliteitsmanagementsysteem van het kantoor (d.w.z. netwerkdiensten); en in

(c) de verantwoordelijkheden van het kantoor voor alle maatregelen die nodig zijn om netwerkeisen te implementeren of gebruik te maken van netwerkdiensten.

Het kantoor blijft verantwoordelijk voor zijn kwaliteitsmanagementsysteem. Het
kantoor mag niet toestaan dat de naleving van de netwerkeisen of het gebruik van

8. Het kantoor dient:

(a) te bepalen hoe de netwerkeisen of netwerkdiensten relevant zijn voor, en in overweging worden genomen in, het kwaliteitsmanagementsysteem
van het kantoor, met inbegrip van de wijze waarop zij moeten worden geïmplementeerd; en

(b) te evalueren of, en zo ja hoe, de netwerkeisen of -diensten door het kantoor moeten worden aangepast of aangevuld om op passende wijze te worden gebruikt in het kwaliteitsmanagementsysteem.

Organisatie van de beroepsactiviteiten
9. Het kantoor richt zijn kwaliteitsmanagementsysteem zo in dat dit een redelijke mate van zekerheid geeft dat:

(i) de gepaste organisatorische en financiële middelen worden voorzien in

(ii) het personeel over de gepaste beroepskwalificaties beschikt om adequaat ingezet te worden.

Bekwaamheid

10. Het kantoor richt zijn kwaliteitsmanagementsysteem zo in dat dit een redelijke
mate van zekerheid geeft dat de beroepsbeoefenaars aan wie activiteiten of opdrachten kunnen worden toegewezen of worden toegewezen:

(i) over de nodige beroepsbekwaamheid beschikken;
(ii) op regelmatige basis en op continue wijze een permanente vorming voortzetten om hun beroepskennis en -bekwaamheid en hun beroepsethiek op voldoende peil te houden, in overeenstemming met de Wet en met de Norm Permanente Vorming.

## Aanvaarding van opdrachten Acceptation de missions

11. Het kantoor richt zijn kwaliteitsmanagementsysteem zo in dat dit een redelijke mate van zekerheid geeft dat:

(i) het kantoor over de nodige bekwaamheid, medewerking en tijd beschikt om de opdracht behoorlijk uit te voeren;
(ii) er, voorafgaandelijk aan de uitvoering van iedere opdracht en in overleg met de cliënt, een opdrachtbrief wordt opgemaakt die op een het kantoor omschrijft, in overeenstemming met de toepasselijke regelgeving;
(iii) als een opdracht aan het kantoor als rechtspersoon gegeven wordt,  er een vertegenwoordiger natuurlijke persoon aangeduid wordt, die de hoedanigheid heeft om deze opdracht uit te voeren;
(iv) er geen opdrachten aanvaard worden onder voorwaarden die een objectieve uitvoering daarvan in gedrang zouden brengen of een belangenconflict zouden teweegbrengen.

Beëindigen van cliëntenrelaties

12. Het kantoor richt zijn kwaliteitsmanagementsysteem zo in dat dit een redelijke
mate van zekerheid geeft dat alle boeken, documenten en elektronische of andere
gegevens die toebehoren aan de cliënt onverwijld uit handen worden gegeven, wanneer deze erom verzoekt.

## Fin des relations clients

demande.
Verzekering burgerlijke beroepsaansprakelijkheid
13. Het kantoor richt zijn kwaliteitsmanagementsysteem zo in dat dit een redelijke mate van zekerheid geeft dat:

- het kantoor, zijn beroepsbeoefenaars en zijn medewerkers, verzekerd zijn
overeenkomstig artikel 44  van de Wet en het KB van 11 september 2020
tot vaststelling van de nadere regels van het openbaar register van het voorwaarden inzake de beroepsverzekering;

- jaarlijks een bewijs van het respecteren van hun verzekeringsverplichting aan het Instituut wordt bezorgd.

Beroepsgeheim en geheimhouding

14. Het kantoor richt zijn kwaliteitsmanagementsysteem zo in dat dit een redelijke mate van zekerheid geeft dat:

(i) het beroepsgeheim wordt nageleefd;
(ii) de verplichting tot geheimhouding wordt gerespecteerd van gegevens die uitdrukkelijk of stilzwijgend in de uitoefening van het beroep aan het
kantoor zijn toevertrouwd en van de feiten met een vertrouwelijk karakter die in de uitoefening van het beroep werden vastgesteld;
(iii) het vertrouwelijk karakter wordt geëerbiedigd van vertrouwelijke informatie die gedeeld wordt met personeelsleden, stagiairs, of met andere beroepsbeoefenaars.

Proces van monitoren en remediëren

15. Het kantoor dient een jaarlijks proces van monitoren en remediëren vast te stellen om:

(a) relevante, betrouwbare en tijdige informatie te verstrekken over de opzet, implementatie en werking van het kwaliteitsmanagementsysteem;
(b) passende maatregelen te nemen om te reageren op geïdentificeerde tekortkomingen, zodat tekortkomingen tijdig worden geremedieerd en

## Documentatie Documentation

16.
Het kantoor dient documentatie op te stellen over zijn kwaliteitsmanagementsysteem die voldoende is:

(a) om een samenhangend inzicht in het kwaliteitsmanagementsysteem bij het personeel te bevorderen, met inbegrip van het verkrijgen van inzicht
in hun taken en verantwoordelijkheden met betrekking tot het
kwaliteitsmanagementsysteem en de uitvoering van de opdrachten;
(b) om in het kader van een kwaliteitstoetsing de Raad inzicht te geven in de omvang van het cliëntenbestand en evenredig met de opdrachten die
worden uitgevoerd, mits voorzien van de gepaste organisatorische en financiële middelen.

Inwerkingtreding

Deze norm treedt overeenkomstig artikel 72 laatste lid van de Wet van 17 maart
2019 betreffende de beroepen van accountant en belastingadviseur in werking op 3 september 2025.
