---
bijgewerkt: 24.12.2025
bron: ejustice.just.fgov.be (gecoördineerde versie)
bron_rol: itaa_lex
chunk:
  level: 5
  sub_strategy:
  type: Art.
itaa-lex-sectie: II
provenance:
  inputs:
    - id: resources/raw/wetteksten/KB-WIB92.pdf
      sha256: 16156af9b49f6a5968dd3c818f3cb0ac36a1c2a60ad68fe9b273aafde371749c
      version: 24.12.2025
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: 11f9196
    model:
    prompt_version:
  generated_at: '2026-05-11T16:21:30Z'
  stale: false
  stale_reason:
  trust:
    status: needs-rework
    confirmed_at: '2026-05-11T16:30:30Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "B4/A6: Losse 'Titel' (regel 55) en 'Inhoudstafel' (regel 67) als plain-text regels zonder heading-prefix. Verder staan enkele artikel-koppen gesplitst: de ##### heading bevat alleen het artikelnummer en de eigenlijke tekst staat direct erna op de volgende regel zonder witruimte (bv. 'Art. 2.De'). De bijlagentabel (BIJLAGE I, regels 1966+) is als ASCII-spatie-uitlijning weergegeven (C3, pseudo-tabel) in plaats van markdown pipe-syntax. Laag-1 pass zonder flags — qua structuur is de body grotendeels in orde."
    layer1:
      status: pass
      run_id: 20260511-162232
      run_at: '2026-05-11T16:22:33Z'
      heading_count: 468
      max_section_chars: 8860
      file_size_chars: 216919
      flags: []
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-11T16:30:30Z'
      rationale: "B4/A6: Losse 'Titel' (regel 55) en 'Inhoudstafel' (regel 67) als plain-text regels zonder heading-prefix. Verder staan enkele artikel-koppen gesplitst: de ##### heading bevat alleen het artikelnummer en de eigenlijke tekst staat direct erna op de volgende regel zonder witruimte (bv. 'Art. 2.De'). De bijlagentabel (BIJLAGE I, regels 1966+) is als ASCII-spatie-uitlijning weergegeven (C3, pseudo-tabel) in plaats van markdown pipe-syntax. Laag-1 pass zonder flags — qua structuur is de body grotendeels in orde."
      concrete_problemen:
        - regel: 55
          categorie: B4
          type: other
          voorbeeld: "### Titel\n\n27 AUGUSTUS 1993. - KONINKLIJK BESLUIT..."
        - regel: 67
          categorie: B4
          type: other
          voorbeeld: "Inhoudstafel\n\n## HOOFDSTUK I."
        - regel: 1966
          categorie: C3
          type: pseudo-table
          voorbeeld: '----------------- ------------ --------- --------- --------- --------- --------'
        - regel: 2004
          categorie: A7
          type: scrambled-words
          voorbeeld: '<KB 1996-03-06/3 4, art. 4, 0 27; Inwerkingtreding : 01-01-199 5>'
status: beschikbaar
tags:
  - II
  - '2.2'
  - '2.3'
wet: Koninklijk besluit tot uitvoering van het Wetboek van de Inkomstenbelastingen 1992 (KB/WIB92)
---

# Koninklijk besluit tot uitvoering van het Wetboek van de Inkomstenbelastingen 1992 (KB/WIB92)

*Bijgewerkt tot en met 24.12.2025 — gecoördineerde versie.*

Dossiernummer : 1993-08-27/49

### Titel

27 AUGUSTUS 1993. - KONINKLIJK BESLUIT TOT UITVOERING VAN HET WETBOEK VAN DE INKOMSTENBELASTINGEN 1992, AFGEKORT ALS "KB/WIB 92". (OPGELET : het bijwerken van deze tekst is tijdelijk uitgesteld : gelieve de laatste wijzigingsreferentie in de tabel na te kijken, of de databank "FisconetPlus" raad te plegen)

Situatie : De van kracht zijnde wijzigingen, gepubliceerd tot en met 04-04-2003, zijn verwerkt.

Bron : FINANCIEN

Publicatie : Belgisch Staatsblad van 13-09-1993 bladzijde : 20105

Inwerkingtreding : 01-01-1992

Inhoudstafel

## HOOFDSTUK I. - GRONDSLAG EN BEREKENING VAN DE BELASTINGEN.

### Afdeling I. - Kadastraal inkomen. - Revalorisatiecoëfficiënt. (Wetboek van de inkomstenbelastingen 1992, artikel 13)

##### Art. 1

### Afdeling II. - Fiscale voorwaarden inzake spaardeposito's. (Wetboek van de inkomstenbelastingen 1992, artikel 21, 5°)

##### Art. 2

### Afdeling III. - Forfaitaire raming van de kosten die aftrekbaar zijn van het bruto-inkomen uit verhuring, verpachting, gebruik en concessie van roerende goederen. (Wetboek van de inkomstenbelastingen 1992, artikel 22, § 3)

### Afdeling IV. - Vaststelling van het nettobedrag van de beroepsinkomsten. (Wetboek van de inkomstenbelastingen 1992, artikelen 23, § 3, en 77)

### Afdeling V. - Optiestelsel van landbouwvennootschappen. (Wetboek van de inkomstenbelastingen 1992, artikel 29, § 2, 2°)

### Afdeling VI. - Bezoldigingen van volledig, hoofdzakelijk of bijkomend met fooien bezoldigde werknemers - Belastbare minimumbezoldiging. (Wetboek van de inkomstenbelastingen 1992, artikel 31, vierde lid)

##### Art. 17

### Afdeling VIII. - (Afdeling VIII. PC-privé-plannen. (Wetboek van de inkomstenbelastingen 1992, artikel 38, eerste lid, 17°).)

### Afdeling IX. - Grenzen en voorwaarden voor belastingvrijstelling van waardeverminderingen en voorzieningen voor risico's en kosten. (Wetboek van de inkomstenbelastingen 1992, artikel 48)

### Afdeling X. - Forfaitaire aftrek voor uitzonderlijke beroepskosten ten gevolge van de afstand tussen de woonplaats en de plaats van tewerkstelling. (Wetboek van de inkomstenbelastingen 1992, artikel 51, vierde lid)

##### Art. 28

### Afdeling XI. - Interesten van obligaties, leningen, schulden, deposito's en andere effecten ter vertegenwoordiging van leningen. (Wetboek van de inkomstenbelastingen 1992, artikel 55, eerste lid)

##### Art. 29

### Afdeling XII. - Verantwoording van sommige beroepskosten. (Wetboek van de inkomstenbelastingen 1992, artikel 57)

### Afdeling XIII. - (Werkgeversbijdragen voor aanvullende verzekering tegen ouderdom en vroegtijdige dood (Wetboek van de inkomstenbelastingen 1992, artikel 59, tweede en vierde lid).)

### Afdeling XIV. - Degressieve afschrijvingen. (Wetboek van de inkomstenbelastingen 1992, artikel 64)

### Afdeling XIVbis. Beroepskosten met betrekking tot de verplaatsing tussen de woonplaats en de plaats van tewerkstelling (Wetboek van de inkomstenbelastingen 1992, artikel 66bis, tweede lid).

##### Art. 43.1

### Afdeling XV. - (Vrijstelling voor bijkomend personeel dat voor wetenschappelijk onderzoek, technologisch potentieel, uitvoer en integrale kwaliteitszorg wordt tewerkgesteld in België (Wetboek van de inkomstenbelastingen 1992, artikel 67, § 5);)

### Afdeling XVI. - Investeringsaftrek. ((Wetboek van de inkomstenbelastingen 1992, artikelen 69, § 2, 3e lid en 77))

##### Art. 47, 47bis, 48-49, 49bis

### Afdeling XVII. - (...)

### Afdeling XVIII. - Belastingvrijstelling van prijzen en subsidies betaald of toegekend aan geleerden, schrijvers of kunstenaars. (Wetboek van de inkomstenbelastingen 1992, artikel 90, 2°, tweede lid)

##### Art. 53

### Afdeling XIX. - (Meerwaarden op onroerende goederen. (Wetboek van de inkomstenbelastingen 1992, artikel 101, § 3))

##### Art. 54

### Afdeling XXI. - Aanrekening van de van het totale netto-inkomen aftrekbare bestedingen. (Wetboek van de inkomstenbelastingen 1992, artikel 106)

##### Art. 56

### Afdeling XXII. - (Instellingen die giften ontvangen. (Wetboek van de inkomstenbelastingen 1992, artikelen 108 en 110))

##### Art. 57-59, 59bis, 59ter, 59quater, 59quinquies, 60

### Afdeling XXIII. - Aftrek van uitgaven voor kinderoppas. (Wetboek van de inkomstenbelastingen 1992, artikel 113, § 2)

##### Art. 61

### Afdeling XXIV. - Aftrek van interest van hypothecaire leningen aangegaan voor het vernieuwen van een woning. (Wetboek van de inkomstenbelastingen 1992, artikel 115, 2°, b)

##### Art. 62

### Afdeling XXV. - Aanrekening van de verliezen van één van de echtgenoot op de inkomsten van de andere echtgenoot. (Wetboek van de inkomstenbelastingen 1992, artikel 129)

##### Art. 63

### Afdeling XXVbis. - (Persoonlijke bijdragen voor aanvullende verzekering tegen ouderdom en vroegtijdige dood (Wetboek van de inkomstenbelastingen 1992, artikel 145.3, derde lid).)

##### Art. 63.1

### Afdeling XXVter. - (Voorwaarden en wijze waarop de vermindering voor het lange termijnsparen wordt toegepast met betrekking tot premies van individuele levensverzekeringen en betalingen voor de aflossing of wedersamenstelling van hypotheekleningen (Wetboek van de inkomstenbelastingen 1992, artikel 145.6, derde lid).)

##### Art. 63. 2-63.4

### Afdeling XXVquater. - (Inlichtingen te verstrekken betreffende betalingen voor pensioensparen (artikelen 21, 8°, 145.10, tweede lid, 145.12, zesde lid, en 263, tweede lid, van het Wetboek van de inkomstenbelastingen 1992).)

##### Art. 63.5

### Afdeling XXVquinquies. - (Voorwaarden tot toekenning en behoud van de erkenning van pensioenspaarfondsen (artikel 145.16, 1°, Wetboek van de inkomstenbelastingen 1992).)

##### Art. 63. 6-63.9

### Afdeling XXVsexies. - Vermindering voor uitgaven betaald voor prestaties in het kader van plaatselijke werkgelegenheidsagentschappen en voor prestaties betaald met dienstencheques (Wetboek van de inkomstenbelastingen 1992, artikel 14522)

##### Art. 63.10

### Afdeling XXVsepties. - Vermindering voor energiebesparende uitgaven (Wetboek van de inkomstenbelastingen 1992, artikel 145.24)

##### Art. 63.11

### Afdeling XXVI. - Voorafbetalingen - Belastingvermeerdering - Bonificatie. (Wetboek van de inkomstenbelastingen 1992, artikelen 162, eerste lid, 167, 175 en 376, § 4)

### Afdeling XXVIIbis. - Voorwaarden en grenzen van de vrijstelling van de technische voorzieningen (Wetboek van de inkomstenbelastingen 1992, artikel 194bis).

##### Art. 73. 1-73.4

### Afdeling XXVIIter. - Investeringsmodaliteiten in het kader van de investeringsreserve ingeval van inbreng van een tak van werkzaamheid of een bedrijfsafdeling of van een algemeenheid van goederen of ingeval van fusie of splitsing (Wetboek van de inkomstenbelastingen 1992, artikel 194quater , § 6, eerste lid)

##### Art. 73.4bis

### Afdeling XXVIIquater. - (Definitief belaste inkomsten (Wetboek van de inkomstenbelastingen 1992, artikelen 202, § 2, tweede lid en 203, § 1, derde lid en § 2, zesde lid, 2°)) (NOTA 1: Ingevoegd bij KB 2000-11-29/33, art. 1; ED : 28-11-2000 onder de titel "Erkenningsvoorwaarden waaraan een gecentraliseerd systeem voor het lenen en ontlenen van aandelen dat geïntegreerd is in een betalings- en afwikkelingssysteem van effectenverrichtingen moet voldoen en de periode gedurende dewelke de erkenning kan worden verleend (Wetboek van de inkomstenbelastingen 1992, artikel 203, § 2, 6de lid, 2°)") (NOTA 2 : oude afdeling XXVIIter, hernummerd XXVIIquater door KB 2003-02-06/30)

##### Art. 73. 4ter, 73.4quater, 73.5-73.12

### Afdeling XXVIII. - Vaststelling van het belastbare inkomen inzake vennootschapsbelasting. (Wetboek van de inkomstenbelastingen 1992, artikel 207)

### Afdeling XXIX. - Vaststelling van het maatschappelijk kapitaal en van de waardeverminderingen, voorzieningen, reserves en meerwaarden ingeval de inbrengen niet volledig worden vergoed met nieuwe aandelen die naar aanleiding van de in artikel 21, § 1, van het Wetboek van de inkomstenbelastingen 1992 vermelde verrichtingen worden uitgegeven. (Wetboek van de inkomstenbelastingen 1992, artikel 214, tweede lid)

## HOOFDSTUK II. - VOORHEFFINGEN EN VERREKENING VAN VOORHEFFINGEN.

### Afdeling I. - Roerende voorheffing. (Wetboek van de inkomstenbelastingen 1992, artikelen 250, 300, § 1 en 312)

### Afdeling II. - Bedrijfsvoorheffing. (Wetboek van de inkomstenbelastingen 1992, artikelen (57,) 250, 271, 275, §§ 1 en 2, 300, § 1, en 312)

### Afdeling III. - Roerende voorheffing op inkomsten van roerende goederen en kapitalen en op sommige diverse inkomsten.

#### Onderafdeling I. - Inkomsten van vreemde waarden, van schuldvorderingen op of van gelddeposito's in het buitenland. - Controlemaatregelen. (Wetboek van de inkomstenbelastingen 1992, artikel 263, eerste lid)

#### Onderafdeling II. - (Vrijstelling van de roerende voorheffing). (Wetboek van de inkomstenbelastingen 1992, artikel 264)

##### Art. 101bis, 101ter, 102-104

#### Onderafdeling III. - Volledige of gedeeltelijke verzaking van de inning van roerende voorheffing. (Wetboek van de inkomstenbelastingen 1992, artikel 266)

### Afdeling IV. - Verrekening van voorheffingen.

#### Onderafdeling I. - Fictieve onroerende voorheffing. (Wetboek van de inkomstenbelastingen 1992, artikel 278)

##### Art. 120

#### Onderafdeling II. - Fictieve roerende voorheffing. (Wetboek van de inkomstenbelastingen 1992, artikel 284)

#### Onderafdeling III. - Mate van verrekening. (Wetboek van de inkomstenbelastingen 1992, artikel 295)

## HOOFDSTUK III. - VESTIGING EN INVORDERING VAN DE BELASTING.

### Afdeling I. - (Aangiften. (Wetboek van de inkomstenbelastingen 1992, artikelen 297, tweede lid en 300, § 1))

##### Art. 125bis, 126-127

### Afdeling II. - Kohieren. (Wetboek van de inkomstenbelastingen 1992, artikelen 251 en 300, § 1)

### Afdeling III. - Betalingen en kwitanties. (Wetboek van de inkomstenbelastingen 1992, artikelen 250 en 300, § 1)

### Afdeling IV. - Verjaring. (Wetboek van de inkomstenbelastingen 1992, artikel 300, § 1)

##### Art. 145

### Afdeling V. - Vervolgingen. (Wetboek van de inkomstenbelastingen 1992, artikel 300, § 1)

#### Onderafdeling I. - Inleidende bepaling - Indeling van de vervolgingen.

#### Onderafdeling II. - Rechtstreekse vervolgingen.

##### Art. 148

A. Dwangbevel.

B. Uitvoerend beslag op roerend goed.

C. Beslag op tak- en wortelvaste vruchten.

##### Art. 157

D. Uitvoerend beslag op zeeschepen en binnenschepen.

##### Art. 158

E. Uitvoerend beslag op onroerend goed.

F. Aan de vier soorten van beslag gemene bepalingen.

#### Onderafdeling III. - Onrechtstreekse vervolgingen.

A. Vervolgingen tegen derden-houders.

B. Aanwending van sommen die aan een belastingschuldige moeten worden teruggegeven of betaald.

##### Art. 166

#### Onderafdeling IV. - Met de vervolgingen belaste personen.

#### Onderafdeling V. - Vervolgingskosten.

#### Onderafdeling VI. - Algemene bepalingen.

##### Art. 175

### Afdeling VI. - Opsporing van inbreuken. (Wetboek van de inkomstenbelastingen 1992, artikel 300, § 1)

##### Art. 176

### Afdeling VII. - Vestiging en invordering door de administratie van de belasting over de toegevoegde waarde, registratie en domeinen, van de belasting van niet-inwoners op meerwaarden op (...) onroerende goederen. (Wetboek van de inkomstenbelastingen 1992, artikel 301)

##### Art. 177

### Afdeling VIII. - (Vrijstelling van de aangifteverplichting in de personenbelasting. (Wetboek van de inkomstenbelastingen 1992, artikel 306))

### Afdeling IX. - Aanwijzing van derden om mededeling te verkrijgen van informatiegegevens voor de uitvoering van een opdracht van algemeen belang. (Wetboek van de inkomstenbelastingen 1992, artikel 314, § 4)

### Afdeling IXbis. - (Aanwijzing van ambtenaren van andere fiscale administraties die bevoegd zijn om onderzoekingen uit te voeren (Wetboek van de inkomstenbelastingen 1992, artikel 334bis).)

##### Art. 181bis

### Afdeling X. - Minimumwinst van buitenlandse firma's. (Wetboek van de inkomstenbelastingen 1992, artikel 342, § 2)

##### Art. 182

### Afdeling XI. - Fiscale Commissies. (Wetboek van de inkomstenbelastingen 1992, artikel 347)

### Afdeling XII. - Bepaling van het belastbare tijdperk voor de personenbelasting, vennootschapsbelasting, rechtspersonenbelasting, belasting van niet-inwoners en voorheffingen, en van de inkomsten die daartoe behoren. (Wetboek van de inkomstenbelastingen 1992, artikel 360, tweede lid)

### Afdeling IIIBis. - (Inning door de administratie van de belasting over de toegevoegde waarde, registratie en domeinen, van de bedrijfsvoorheffing op meerwaarden verwezenlijkt op onroerende goederen door niet- inwoners in het kader van hun beroepswerkzaamheid.)

##### Art. 210bis, 210ter

### Afdeling XIV. - Zakelijke zekerheid en persoonlijke borgstelling. (Wetboek van de inkomstenbelastingen 1992, artikel 420, § 1)

### Afdeling XV. - Verplichtingen van kredietinstellingen of -inrichtingen. (Wetboek van de inkomstenbelastingen 1992, artikel 443)

### Afdeling XVI. - Schaal van de belastingverhogingen. (Wetboek van de inkomstenbelastingen 1992, artikel 444)

## HOOFDSTUK IV. - BELASTINGWEZEN VAN DE PROVINCIES, DE AGGLOMERATIES EN DE GEMEENTEN. (Wetboek van de inkomstenbelastingen 1992, artikelen 300 en 469)

### Afdeling I. - Provinciale belastingen.

##### Art. 230

### Afdeling II. - Aanvullende agglomeratie- en gemeentebelastingen.

## HOOFDSTUK V. - OVERGANGSBEPALINGEN.

### Afdeling I. - Inhouding van een gedeelte van de roerende voorheffing. (Wetboek van de inkomstenbelastingen 1992, artikel 507, derde lid)

## HOOFDSTUK IVbis. - Bijzondere invorderingsregels inzake de toekenningen aan de provincies, de agglomeraties en de gemeenten (Wetboek van de inkomstenbelastingen 1992, art. 470bis).

##### Art. 233bis

## HOOFDSTUK V. - OVERGANGSBEPALINGEN.

### Afdeling I. - Inhouding van een gedeelte van de roerende voorheffing. (Wetboek van de inkomstenbelastingen 1992, artikel 507, derde lid)

##### Art. 234

### Afdeling II. - Herschatting voor de berekening van de afschrijving van bepaalde activa die zijn verkregen of tot stand gebracht voor de normale datum van afsluiting van de laatste jaarbalans opgemaakt voor 31 december 1940 en die nog in gebruik waren op de normale datum van afsluiting van de laatste jaarbalans opgemaakt voor 31 december 1946. (Wetboek van de inkomstenbelastingen 1992, artikel 511, § 2)

Bijlagen.

##### Art. N1-25N2, N2bis, N3-N5

OVEREENSTEMMINGSTABELLEN.

Tekst

## HOOFDSTUK I. - GRONDSLAG EN BEREKENING VAN DE BELASTINGEN.

### Afdeling I. - Kadastraal inkomen. - Revalorisatiecoëfficiënt. (Wetboek van de inkomstenbelastingen 1992, artikel 13)

##### Art. 1

De in artikel 13 van het Wetboek van de inkomstenbelastingen 1992 vermelde revalorisatiecoëfficiënt voor kadastrale inkomens wordt per aanslagjaar vastgesteld zoals in de volgende tabel is aangegeven :

Aanslagjaar Revalorisatiecoefficient

1985 2,25

1986 2,40

1987 2,50

1988 2,50

1989 2,55

1990 2,60

1991 2,70

1992 2,80

1993 2,88

[1994 2,95]

<KB 1993-10-22/33, art. 1; Inwerkingtreding : 01-01-1994>

[1995 3]

<KB 1994-02-18/35, art. 1, 003; Inwerkingtreding : 01-01-19 95>

[1996 3]

<KB 1995-03-20/36, art. 1, 015; Inwerkingtreding : 01-01-19 96>

[1997 3,05]

<KB 1996-03-06/34, art. 1, 027; Inwerkingtreding : 01-01-19 97>

[1998 3,10]

<KB 1997-02-26/30, art. 1, 035; Inwerkingtreding : 01-01-19 98>

[1999 3,12]

<KB 1998-12-17/63, art. 1, 050; Inwerkingtreding : 01-01-19 99>

[2000 3,15]

<KB 1999-10-29/33, art. 1, 058; Inwerkingtreding : 01-01-20 00>

[2001 3,19]

<KB 2000-11-23/32, art. 1, 070; Inwerkingtreding : 01-01-20 01>

[2002 3,26]

<KB 2002-02-04/30, art. 1, 085; Inwerkingtreding : 01-01-20 02>

[2003 3,35]

<KB 2003-01-23/30, art. 1, 090; Inwerkingtreding : 01-01-20 03>

### Afdeling II. - Fiscale voorwaarden inzake spaardeposito's. (Wetboek van de inkomstenbelastingen 1992, artikel 21, 5°)

### Afdeling III. - Forfaitaire raming van de kosten die aftrekbaar zijn van het bruto-inkomen uit verhuring, verpachting, gebruik en concessie van roerende goederen. (Wetboek van de inkomstenbelastingen 1992, artikel 22, § 3)

##### Art. 4

Het in artikel 3 vermelde forfait wordt gebracht op :  1° 50 pct. wanneer het verhuring betreft van :  a) toneeldecors en -kostuums;  b) roerende goederen die gemeubileerde woningen, kamers of appartementen stofferen; ingeval een gezamenlijke huurprijs voor de roerende en onroerende goederen is bedongen, wordt het bruto-bedrag van de belastbare inkomsten van de roerende goederen geacht 2/5 van die huurprijs te bedragen;  2° 85 pct. wanneer het gaat om :  a) verhuring van partituren, libretto's en andere gelijkaardige voorwerpen die deel uitmaken van orkestmaterieel voor schouwburgvoorstellingen;  b) concessie van het recht handelsgrammofoonplaten te persen;  c) (concessie van het recht om bioscoopfilms en gelijksoortige audiovisuele werken te distribueren of te vertonen en concessie van het recht om radio- en televisieprogramma's uit te zenden of gelijktijdig en onverkort door te geven.) <KB 1994-08-12/48, art. 1, 006; Inwerkingtreding : 01-01-1992>

##### Art. 5

De normaal ten laste van de verkrijger van de inkomsten vallende kosten die, al of niet volgens overeenkomst, door de schuldenaar van de inkomsten zijn gedragen, moeten bij de werkelijk verleende of toegekende sommen worden gevoegd om het brutobedrag te bepalen.  In het in artikel 4, 2°, c, vermelde geval worden kosten van kopieën, van onderschriften en van nasynchronisatie van films en van voorfilms, kosten voor vervoer van films naar het buitenland, tolgelden, belasting op roerende verhuring en transferkosten op huurgelden, zomede alle andere gelijkaardige kosten, aan het belastbare brutobedrag toegevoegd ingeval zij door de schuldenaar van de inkomsten zijn gedragen.

### Afdeling IV. - Vaststelling van het nettobedrag van de beroepsinkomsten. (Wetboek van de inkomstenbelastingen 1992, artikelen 23, § 3, en 77)

##### Art. 6

(De aftrekken bedoeld in de artikelen 23, § 2, en 68 tot 80 van het Wetboek van de inkomstenbelastingen 1992, worden verricht volgens de in de artikelen 7 tot 10 vastgestelde wijze en in de hierna vermelde volgorde :) <KB 1995-09-01/42, art. 2, 1°, 019; Inwerkingtreding : 01-01-1993>  1° (de bijdragen bedoeld in artikel 52, 7° (...), van hetzelfde Wetboek, ingehouden door de schuldenaar van de beroepsinkomsten en de sommen bedoeld in artikel 52, 8°, van hetzelfde Wetboek, gestort door de belastingplichtige;) <KB 1995-09-01/42, art. 1, 1°, 019; Inwerkingtreding : 01-01-1992> <KB 1995-09-01/42, art. 2, 2°, 020; Inwerkingtreding : 01-01-1994>  2° de andere beroepskosten dan de in 1° vermelde bijdragen (en sommen), die op de beroepsinkomsten drukken; <KB 1995-09-01/42, art. 1, 2°, 019; Inwerkingtreding : 01-01-1992>  3° de investeringsaftrek;  4° de gedurende het belastbare tijdperk geleden beroepsverliezen;  5° de tijdens de vorige belastbare tijdperken geleden beroepsverliezen;  6° (...) <KB 1995-09-01/42, art. 2, 3°, 019; Inwerkingtreding : 01-01-1993>

##### Art. 8

§ 1. Wanneer een beroepswerkzaamheid in verschillende landen wordt uitgeoefend, worden de overeenkomstig artikel 7 berekende nettoresultaten van het belastbare tijdperk in 3 groepen ingedeeld :  1° die behaald in België;  2° die behaald in landen waarmede België geen overeenkomst ter voorkoming van dubbele belasting heeft gesloten;  3° die behaald in andere landen.  § 2. Binnen elk van de groepen 1 en 2 worden de negatieve resultaten eerst afgetrokken van de gezamenlijk belastbare beroepsinkomsten van de groep; het eventuele saldo wordt evenredig afgetrokken van de afzonderlijk belastbare beroepsinkomsten van de groep.  § 3. Wanneer het eindresultaat van groep 1 negatief is, wordt dat resultaat evenredig afgetrokken van de gezamenlijk belastbare beroepsinkomsten van groep 2 en de beroepsinkomsten van groep 3; het eventuele saldo wordt evenredig afgetrokken van de afzonderlijk belastbare beroepsinkomsten van groep 2.  § 4. Wanneer het eindresultaat van groep 2 negatief is, wordt dat resultaat evenredig afgetrokken van de gezamenlijk belastbare beroepsinkomsten van groep 1 en de beroepsinkomsten van groep 3; het eventuele saldo wordt evenredig afgetrokken van de afzonderlijke belastbare beroepsinkomsten van groep 1.  § 5. Wanneer het eindresultaat van groep 3 negatief is, wordt dat resultaat evenredig afgetrokken van de gezamenlijk belastbare beroepsinkomsten van de groepen 1 en 2; het eventuele saldo wordt evenredig afgetrokken van de afzonderlijk belastbare beroepsinkomsten van die groepen.

##### Art. 9

Het tijdens het belastbare tijdperk in een bepaalde beroepswerkzaamheid geleden beroepsverlies wordt evenredig aangerekend op de beroepsinkomsten uit de andere beroepswerkzaamheden die gezamenlijk worden belast of die krachtens artikel 155 van het Wetboek van de inkomstenbelastingen 1992 zijn vrijgesteld; het eventuele saldo wordt evenredig aangerekend op de beroepsinkomsten die afzonderlijk worden belast.

##### Art. 10

De tijdens vorige belastbare tijdperken geleden beroepsverliezen worden evenredig aangerekend op de overblijvende beroepsinkomsten van de verschillende beroepswerkzaamheden die gezamenlijk worden belast of die krachtens artikel 155 van het Wetboek van de inkomstenbelastingen 1992 zijn vrijgesteld; het eventuele saldo wordt evenredig aangerekend op de beroepsinkomsten die afzonderlijk worden belast.

##### Art. 11. (Opgeheven) <KB 1995-09-01/42, art. 4, 019; Inwerkingtreding : 01-01-1993>

### Afdeling V. - Optiestelsel van landbouwvennootschappen. (Wetboek van de inkomstenbelastingen 1992, artikel 29, § 2, 2°)

##### Art. 12

De landbouwvennootschappen mogen voor de rechtspersoonlijkheid en voor het stelsel van de vennootschapsbelasting kiezen wanneer zij op de eerste dag van het eerste belastbare tijdperk waarvoor de optie wordt uitgeoefend, tenminste 3 vennoten tellen en wanneer het maatschappelijk kapitaal op diezelfde datum tenminste (30.950 EUR) bedraagt. <KB 2001-07-13/52, art. 2, 083; Inwerkingtreding : 01-01-2002>

##### Art. 13

De optie kan slechts geldig worden uitgeoefend indien de beslissing daartoe met eenparigheid van stemmen is genomen door de personen die op de eerste dag van het eerste belastbare tijdperk waarvoor de optie uitwerking moet hebben, vennoten waren en, in geval van overlijden van één hunner, door hun rechthebbenden.

##### Art. 14

Om het optierecht te kunnen uitoefenen, moet de vennootschap een afschrift van de in artikel 13 vermelde beslissing inzenden.  Dat document moet alle gegevens bevatten die voor het beoordelen van de geldigheid van de beslissing nodig zijn en moet worden ondertekend door alle personen die hebben medebeslist.  Het moet, op straffe van nietigheid, bij aangetekende brief aan de controleur van de belastingen of aan de leider van het centraal taxatiekantoor van het gebied van de vennootschap worden gezonden uiterlijk binnen de eerste 30 dagen van het eerste belastbare tijdperk waarvoor de optie uitwerking moet hebben.

##### Art. 15

Onverminderd de toepassing van artikel 16, is het optiestelsel onherroepelijk voor een cyclus van 3 opeenvolgende belastbare tijdperken in de vennootschapsbelasting. Het wordt telkens ambtshalve hernieuwd voor een nieuwe cyclus van 3 opeenvolgende belastbare tijdperken, behalve :  1° wanneer de in artikel 13 vermelde personen onder de daarin bepaalde voorwaarden een nieuwe beslissing treffen die een einde aan de optie maakt en wanneer een afschrift van die beslissing, waarin alle voor de beoordeling van de geldigheid ervan nodige gegevens voorkomen, bij aangetekende brief aan de controleur van de belastingen of aan de leider van het centraal taxatiekantoor van het gebied van de vennootschap wordt gezonden uiterlijk binnen de eerste 30 dagen van het eerste belastbare tijdperk dat volgt op de cyclus waarvoor de optie uitwerking heeft gehad; dat afschrift wordt ondertekend door alle personen die hebben medebeslist;  2° wanneer aan de voorwaarden met betrekking tot het aantal vennoten en het bedrag van het maatschappelijk kapitaal, op de datum van het verstrijken van het belastbare tijdperk dat volgt op de cyclus waarvoor de optie laatst uitwerking heeft gehad, sinds ten minste 1 jaar niet meer is voldaan.

### Afdeling VI. - Bezoldigingen van volledig, hoofdzakelijk of bijkomend met fooien bezoldigde werknemers - Belastbare minimumbezoldiging. (Wetboek van de inkomstenbelastingen 1992, artikel 31, vierde lid)

##### Art. 17

De belastbare brutobezoldiging van volledig, hoofdzakelijk of bijkomend met fooien bezoldigde werknemers, mag niet minder bedragen dan de forfaitaire bezoldiging die tot grondslag heeft gediend voor de berekening van de bijdragen welke die werknemers en hun werkgevers verschuldigd zijn ter uitvoering van de wetgeving betreffende de sociale zekerheid.

### Afdeling VII. - Forfaitaire raming van anders dan in geld verkregen voordelen van alle aard. (Wetboek van de inkomstenbelastingen 1992, artikel 36, tweede lid)

##### Art. 18

§ 1. De anders dan in geld verkregen voordelen van alle aard en vermeld in de §§ 2 en 3, worden forfaitair geraamd volgens de in die paragrafen bepaalde regels.  § 2. Voor de voordelen waarvan de waarde wordt vastgesteld door een sociale of economische reglementering, is de in aanmerking te nemen waarde gelijk aan de door die reglementering vastgestelde waarde.  § 3. Bij gebrek aan een dergelijke sociale of economische reglementering, wordt met betrekking tot de hierna vermelde voordelen de in aanmerking te nemen waarde als volgt forfaitair vastgesteld :  1. Renteloze lening of lening tegen verminderde rentevoet :  a) Het voordeel wordt berekend op basis van het verschil tussen :  - eensdeels, de referentierentevoet die hierna per type van lening (...) is aangegeven; <KB 1996-03-06/34, art. 2, 1°, 027; Inwerkingtreding : 01-01-1995>  - anderdeels, de rentevoet aan de ontlener aangerekend, de renteverlaging wegens kinderlast buiten beschouwing gelaten.  b) Voor hypothecaire leningen geldt de hierna aangegeven referentierentevoet van het jaar waarin de leningsovereenkomst is gesloten, (...) : <KB 1996-03-06/34, art. 2, 2°, 027; Inwerkingtreding : 01-01-1995>

Jaar waarin de  leningsovereenkomst is gesloten

In aanmerking te nemen  referentievoet

---- ----

Leningen waarvan de

terugbetaling door een

gemengde evensverzekering Andere

is gewaarborgd leningen

---- ----

pct.

1950 en 1951 5,50

1952 en 1953 5,75

1954 tot 1956 5,50

1957 5,75

1958 6,00

1959 en 1960 5,50

1961 en 1962 5,75

1963 5,25

1964 5,50

1965 en 1966 6,25

1967 6,50

1968 7,25

1969 7,50

1970 8,00

1971 8,75

1972 7,00

1973 6,75

1980 9,50

1981 12,00

1982 13,50

1983 11,50

1984 (tot 31.5.1984 11,50

1984 (vanaf 1.6.1984 10,75 11,75

1985 9,50 [9,75]

<KB 1994-02-18/35, art. 2, 1°, 003; Inwerkingtreding : 01-01-1992>

1986 7,50 7,50

1987 7,25 7,25

1988 7,25 7,00

1989 7,25 7,00

1990 9,50 9,25

1991 10,25 10,25

[1992 9,25 8,25]

<KB 1993-10-22/33, art. 2, 1°; Inwerkingtreding : 01-01-1992>

[1993 8,00 7,65]

<KB 1994-02-18/35, art. 2, 2°, 003; Inwerkingtreding : 01-01-1993>

[1994 7,25 7,10]

<KB 1995-03-07/31, art. 1, 1°, 013; Inwerkingtreding : 01-01-1994>

[1995 7,00 6,75]

<KB 1996-03-06/34, art. 2, 3°, 027; Inwerkingtreding : 01-01-1995>

[1996 6,50 6,50]

<KB 1997-03-17/31, art. 1, 1°, 036; Inwerkingtreding : 01-01-1996>

[1997 6,00 6,00]

<KB 1998-06-02/34, art. 1, 043; Inwerkingtreding : 01-01-1997>

[1998 5,75 5,75]

<KB 1999-04-21/36, art. 1, 052; Inwerkingtreding : 01-01-1998>

[1999 5,75 5,50]

<KB 2000-04-25/32, art. 1, 065; Inwerkingtreding : 01-01-1999>

[2000 5,75 6,50]

<KB 2001-03-16/38, art. 1, 081; Inwerkingtreding : 01-01-2000>

[2001 5,60 6,10]

<KB 2002-03-08/33, art. 1, 087; Inwerkingtreding : 01-01-2001>

[2002 5,75 5,60]

<KB 2003-02-21/36, art. 1, 091; Inwerkingtreding : 01-01-2002>

Maandelijks lastenpercent age

-

Jaarwaarin de Leningen om de aankoop Andere

leningsovereenkomst van een wagen te leningen

is gesloten financieren

1985 0,62 0,62

1986 0,44 0,49

1987 0,40 0,49

1988 0,38 0,46

1989 0,38 0,46

1990 0,45 0,54

1991 0,55 0,60

[1992 0,46 0,46]

<KB 1993-10-22/33, art. 2, 2° ; Inwerkingtreding : 01-01-1992>

[1993 0,42 0,48]

<KB 1994-02-18/35, art. 2, 3° , 003; Inwerkingtreding : 01-01-1993>

[1994 0,40 0,47]

<KB 1995-03-07/31, art. 1, 2° , 013; Inwerkingtreding : 01-01-1994>

[1995 0,35 0,40]

<KB 1996-03-06/34, art. 2, 6° , 027; Inwerkingtreding : 01-01-1995>

[1996 0,30 0,35]

<KB 1997-03-17/31, art. 1, 2° , 036; Inwerkingtreding : 01-01-1996>

[1997 0,25 0,30]

<KB 1998-06-02/34, art. 1, 04 3; Inwerkingtreding : 01-01-1997>

[1998 0,25 0,35]

<KB 1999-04-21/36, art. 1, 05 2; Inwerkingtreding : 01-01-1998>

[1999 0,23 0,30]

<KB 2000-04-25/32, art. 1, 06 5; Inwerkingtreding : 01-01-1999>

[2000 0,28 0,33]

<KB 2001-03-16/38, art. 1, 08 1; Inwerkingtreding : 01-01-2000>

[2001 0,26 0,32]

<KB 2002-03-08/33, art. 1, 08 7; Inwerkingtreding : 01-01-2001>

[2002 0,26 0,33]

<KB 2003-02-21/36, art. 1, 09 1; Inwerkingtreding : 01-01-2002>

- ofwel op basis van het reële jaarlijks lastenpercentage voor het betreffende jaar berekend met de formule :

i = p x 24 x n

----------

i = reeel jaarlijks lastenpercentage

p = maandelijks lastenpercentage

n = terugbetalingstermijn in maanden

d) Voor niet-hypothecaire leningen zonder welbepaalde looptijd geldt de hierna aangegeven referentierentevoet van het jaar waarin de ontlener over de geleende bedragen heeft beschikt :

Jaar waarin de ontlener In aanmerking te

over de geleende bedragen nemen referentievoet

heeft beschikt

---------------------------------- -----------------------------

1981 11

1982 13

1983 13

1984 13

1985 12

1986 9,75

1987 8,75

1988 8,25

1989 9,50

1990 12,75

1991 12,75

[1992 12]

<KB 1993-10-22/33, art. 2, 3°; ED : 01-01-1992>

[1993 10,50]

<KB 1994-02-18/35, art. 2, 4°, 003 ; Inwerkingtreding : 01-01-1992>

[1994 9,25]

<KB 1995-03-07/31, art. 1, 3°, 013 ; Inwerkingtreding : 01-01-1994>

[1995 8,25]

<KB 1996-03-06/34, art. 2, 7°, 027 ; Inwerkingtreding : 01-01-1995>

[1996 7,25]

<KB 1997-03-17/31, art. 1, 3°, 036 ; Inwerkingtreding : 01-01-1996>

[1997 7,00]

<KB 1998-06-02/34, art. 1, 043; ED : 01-01-1997>

[1998 7,25]

<KB 1999-04-21/36, art. 1, 052; ED : 01-01-1998>

[1999 6,75]

<KB 2000-04-25/32, art. 1, 065; ED : 01-01-1999>

[2000 7,9]

<KB 2001-03-16/38, art. 1, 081; ED : 01-01-2000>

[2001 8,60]

<KB 2002-03-08/33, art. 1, 087; ED : 01-01-2001>

[2002 8,00]

<KB 2003-02-21/36, art. 1, 091; ED : 01-01-2002>

[Aard van de voordelen Per dag Per jaar

- - -

Eerste maaltijd (ontbijt) 0,55 EUR 198,00 EUR

Tweede maaltijd (hoofdmaaltijd) 1,09 EUR 392,40 EUR

Derde maaltijd (avondmaal) 0,84 EUR 302,40 EUR

Huisvesting, verwarming, verlichting 0,74 EUR 266,40 EUR

De forfaitaire raming van de huisvesting, verwarming, verlichting geldt evenwel slechts voor het huispersoneel dat over één enkele kamer beschikt.  Wanneer de belanghebbenden het genot hebben van verscheidene woonvertrekken, wordt het voordeel vastgesteld zoals bepaald sub 2 en 4.  7. Kosteloze verstrekking van voeding aan zeelieden en aan bouwvakarbeiders wegens de verwijdering van de werf  Het voordeel wordt forfaitair op (2,48 EUR) per dag effectieve vaart of per effectieve werkdag geraamd. <KB 2001-07-13/52, art. 2, 083; Inwerkingtreding : 01-01-2002>  8. Kosteloze verstrekking van sociale maaltijden  Voor de maaltijden die kosteloos worden verstrekt, dienen de sub 6 vermelde bedragen als grondslag voor de raming van de voordelen.  (9. Persoonlijk gebruik van een kosteloos ter beschikking gesteld voertuig:  Het voordeel is gelijk aan het aantal voor persoonlijk gebruik afgelegde kilometers vermenigvuldigd met het voordeel (in euro) per afgelegde kilometer dat, rekening houdend met de belastbare kracht van het voertuig inzake verkeersbelasting, aangegeven is in de tabel opgenomen onder afdeling III van bijlage I. <KB 2001-07- 13/52, art. 5, 083; Inwerkingtreding : 01-01-2002>  Voor de vaststelling van het voordeel mag het aantal kilometers voor een jaar evenwel niet lager zijn dan 5.000.) <KB 1998-12-07/36, art. 1, 046; Inwerkingtreding : 01-01-1997>  (De basisbedragen vermeld in kolom 2 van de tabel opgenomen onder afdeling III van bijlage I worden gekoppeld aan de spilindex 99,14. De geïndexeerde bedragen zullen van toepassing zijn vanaf 1 januari van het jaar volgend op dat waarin de spilindex is overschreden.  Het geïndexeerde bedrag wordt (afgerond tot het hogere of lagere tienduizendste euro naargelang het cijfer van de honderdduizendste euro al of niet 5 bereikt).) <KB 1998-12-07/36, art. 3, 047; Inwerkingtreding : 01-01- 1998> <KB 2000-07-20/63, art. 5, 076; Inwerkingtreding : 01-01-2002>  (10. Persoonlijk gebruik van een kosteloos ter beschikking gestelde PC of internetaansluiting :  Het voordeel wordt forfaitair vastgesteld op :  - 180 EUR per jaar voor een kosteloos ter beschikking gestelde PC;  - 60 EUR per jaar voor de internetaansluiting en het internetabonnement.) <KB 2003-03-25/37, art. 1, 093; Inwerkingtreding : 01-01-2003>  § 4. In de gevallen als vermeld in § 3, punten 2 tot 9, en wanneer het voordeel niet kosteloos wordt toegestaan, is het in aanmerking te nemen voordeel datgene dat overeenkomstig § 3, punten 2 tot 9, is vastgesteld verminderd met de bijdrage van de verkrijger van dat voordeel.  <Bij arrest nr. 58.169 van 16 februari 1996 (B.St. 07.05.1996, p. 11239) vernietigt de Raad van State, VIe Kamer, in artikel 18, § 3, punt 2, 2e lid, b, de woorden " waarbij dat voordeel niet lager mag zijn dan de huurwaarde van het onroerend goed of het gedeelte van het onroerend goed "; Opheffing : 01-01-1994>

### Afdeling VIII. - (Afdeling VIII. PC-privé-plannen. (Wetboek van de inkomstenbelastingen 1992, artikel 38, eerste lid, 17°).) <Hersteld bij KB 2003-03-25/37, art. 1, 093; Inwerkingtreding : 01-01-2003>

##### Art. 19

<Hersteld bij KB 2003-03-25/37, art. 1, 093; Inwerkingtreding : 01-01-2003> Opdat de tussenkomst van de werkgever in het kader van een PC-privé-plan in aanmerking kan komen voor de vrijstelling als bedoeld in artikel 38, eerste lid, 17°, van het Wetboek van de inkomstenbelastingen 1992, moeten de volgende voorwaarden zijn vervuld :  1. het aanbod van de werkgever waarmee hij zich ertoe verbindt om tussen te komen in de aankoopprijs van een geheel van PC, randapparatuur en printer, internetaansluiting en internetabonnement, alsook de voor de bedrijfsvoering dienstige software, wordt beschreven in het PC-privé-plan;  2. de voorwaarden die in het plan zijn opgenomen moeten dezelfde zijn voor alle werknemers;  3. de minimumvoorwaarden waaraan het plan moet voldoen zijn de volgende :  a) het plan moet de beschrijving geven van het geheel van PC, randapparatuur en printer, internetaansluiting en internetabonnement, alsook de voor de bedrijfsvoering dienstige software;  b) het plan bepaalt dat het de werknemer vrij staat het geheel of slechts een gedeelte van het beschreven materieel te kiezen;  c) de tussenkomst van de werkgever moet per onderdeel van het aanbod worden opgegeven;  d) de tussenkomst kan enkel geschieden bij aankoop van materieel in nieuwe staat;  e) de tussenkomst door de werkgever geschiedt tegen afgifte van een door de werknemer eensluidend verklaard afschrift van de aankoopfactuur of van het aankoopbewijs op naam van de werknemer;  f) wat de materiëlen betreft, die een werknemer voorheen in het kader van een PC-privé-plan heeft aangeschaft, moet het plan bepalen dat slechts in de loop van het derde jaar volgend op het jaar van aanschaf opnieuw mag worden ingegaan op een aanbod van de werkgever.

##### Art. 20. (Opgeheven) <KB 1994-08-12/48, art. 2, 006; Inwerkingtreding : 27-03-1992>

##### Art. 21. (Opgeheven) <KB 1994-08-12/48, art. 2, 006; Inwerkingtreding : 27-03-1992>

##### Art. 22

§ 1. Uit de winst van het krachtens artikel 360 van het Wetboek van de inkomstenbelastingen 1992 bepaalde belastbare tijdperk worden de bij het verstrijken van dat tijdperk geboekte waardeverminderingen gesloten, (...) onder de voorwaarden die hierna volgen : <KB 1995-12-20/33, art. 1, 1°, 021; Inwerkingtreding : 01-01-1996>  1° de verliezen, ter bestrijding waarvan die waardeverminderingen bestemd zijn, moeten uiteraard als beroepsverliezen aftrekbaar zijn en uitsluitend betrekking hebben op niet in obligaties of andere gelijkaardige effecten op naam of aan toonder verdeelde vorderingen;  2° die verliezen moeten scherp omschreven zijn en de waarschijnlijkheid ervan moet voor iedere vordering blijken uit bijzondere tijdens het belastbare tijdperk voorgekomen en op het einde daarvan nog bestaande omstandigheden, en niet uit een louter algemeen risico;  3° de waardeverminderingen moeten geboekt zijn bij de afsluiting van de boekhouding van het belastbare tijdperk en hun bedrag moet in één of meer afzonderlijke rekeningen voorkomen;  4° het bij het verstrijken van enig belastbaar tijdperk overblijvend totaal van de vrijgestelde waardeverminderingen, moet per onderwerp verantwoord en uiteengezet worden in een staat waarvan het model door de Minister van Financiën of zijn gedelegeerde wordt vastgesteld; die staat moet worden ingediend binnen de termijn die gesteld is voor het overleggen van de aangifte in de inkomstenbelastingen over het belastbare tijdperk en bij die aangifte worden gevoegd;  5° (...) <KB 1995-12-20/33, art. 1, 2°, 021; Inwerkingtreding : 01-01-1996>  6° (...) <KB 1995-12-20/33, art. 1, 1°, 021; Inwerkingtreding : 01-01-1996>  § 2. (...) <KB 1995-12-20/33, art. 1, 3°, 021; Inwerkingtreding : 01-01-1996>  § 3. (...) <KB 1995-12-20/33, art. 1, 3°, 021; Inwerkingtreding : 01-01-1996>

##### Art. 23

Werkelijk geleden verliezen op de vordering, waarop een overeenkomstig artikel 22 geboekte waardevermindering betrekking heeft, moeten op die waardevermindering worden aangerekend wanneer zij uit fiscaal oogpunt definitief aanneembaar worden.  (Vrijgestelde waardeverminderingen op vorderingen die niet meer aan de in artikel 22 gestelde voorwaarden (...) beantwoorden, moeten worden teruggenomen.) <KB 1995-12-20/33, art. 2, 021; Inwerkingtreding : 01-01- 1996> <KB 1996-03-06/34, art. 3, 027; Inwerkingtreding : 01-01-1996>

##### Art. 24

Uit de winst van het in artikel 22 vermelde tijdperk worden eveneens de voorzieningen voor risico's en kosten gesloten die bij het verstrijken van dat tijdperk zijn aangelegd, wanneer :  1° de kosten, ter bestrijding waarvan de voorzieningen bestemd zijn, uiteraard aftrekbaar zijn als beroepskosten en geacht worden normaal op de uitslagen van dat tijdperk te drukken;  2° de voorzieningen voldoen aan de voorwaarden die in artikel 22, § 1, 3° en 4°, ten aanzien van waardeverminderingen gesteld zijn.

##### Art. 25

Voor de toepassing van artikel 24 worden geacht normaal op de uitslagen van het belastbare tijdperk te drukken, de kosten die het gevolg zijn van de in dat tijdperk uitgeoefende beroepswerkzaamheid of van alsdan voorgekomen gebeurtenissen, of die bij voorbaat gedekt zijn door tijdens hetzelfde tijdperk verkregen vergoedingen wegens schadegevallen, onteigeningen, opeisingen in eigendom of andere gelijkaardige gebeurtenissen, of die, evenredig met de duur van het belastbare tijdperk, betrekking hebben op grote herstellingen aan gebouwen, materieel en outillage die periodiek met regelmatige tussenpozen van niet meer dan 10 jaar worden uitgevoerd, met uitsluiting van enige vernieuwing.  Worden eveneens geacht normaal op de uitslagen van het belastbare tijdperk te drukken, de kosten die, evenredig met de duur van het belastbare tijdperk, inherent zijn aan de ontmanteling van kerncentrales en aan de ontsmetting van de vestigingsplaatsen ervan.

##### Art. 26

De kosten waarop een overeenkomstig artikel 24 aangelegde voorziening betrekking heeft, moeten op die voorziening worden afgeboekt op het ogenblik dat zij werkelijk worden gedragen.

##### Art. 27

De vrijstelling van elke in de artikelen 22 tot 26 vermelde waardevermindering of voorziening blijft behouden zolang de belastingplichtige aantoont dat het verlies of de kost waaraan die waardevermindering of voorziening beantwoordt, waarschijnlijk blijft; bij gebrek aan verantwoording bij het verstrijken van enig belastbaar tijdperk wordt de waardevermindering of voorziening als een winst van dat tijdperk beschouwd.

### Afdeling X. - Forfaitaire aftrek voor uitzonderlijke beroepskosten ten gevolge van de afstand tussen de woonplaats en de plaats van tewerkstelling. (Wetboek van de inkomstenbelastingen 1992, artikel 51, vierde lid)

##### Art. 28

Het in artikel 51, vierde lid, van het Wetboek van de inkomstenbelastingen 1992 vermelde bedrag wordt vastgesteld op respectievelijk (75,00 EUR), (125,00 EUR) of (175,00 EUR), naargelang de afstand tussen de woonplaats van de belastingplichtige en de plaats van zijn tewerkstelling op 1 januari van het aanslagjaar 75 km tot 100 km, 101 km tot 125 km of meer dan 125 km bedraagt. <KB 2000-07-20/63, art. 2, 075; Inwerkingtreding : 01-01-2002>

### Afdeling XII. - Verantwoording van sommige beroepskosten. (Wetboek van de inkomstenbelastingen 1992, artikel 57)

##### Art. 30

Op het einde van elk jaar moeten de schuldenaars van de in artikel 57, 1°, van het Wetboek van de inkomstenbelastingen 1992 vermelde kosten :  1° voor iedere verkrijger van inkomsten een fiche invullen waarvan het model door de Minister van Financiën of zijn gedelegeerde wordt vastgesteld;  2° voor de sub 1° vermelde fiches een samenvattende opgave opstellen en ondertekenen waarvan het model door de Minister van Financiën of zijn gedelegeerde wordt vastgesteld.  Diezelfde schuldenaars moeten de fiches en de samenvattende opgave waarvan in het voorgaande lid sprake is, voor 30 juni van het jaar na dat waarop deze documenten betrekking hebben, inleveren (bij de bevoegde dienst). <KB 1999-05-03/39, art. 1, 053; Inwerkingtreding : 06-04-1999>

##### Art. 31

Op aanvraag verstrekt de administratie der directe belastingen aan de in artikel 30 vermelde schuldenaars kosteloos exemplaren voor het opstellen van de in dat artikel vermelde fiches en samenvattende opgaven.  Voor zover zij alle vermeldingen bevatten die voorkomen in de door de Minister van Financiën of zijn gedelegeerde vastgestelde modellen, mogen fiches en samenvattende opgaven worden gebruikt waarvan het formaat niet van dat van de voormelde modellen afwijkt.

##### Art. 32

De individuele fiches en de samenvattende opgaven met betrekking tot de in artikel 57, 2°, van het Wetboek van de inkomstenbelastingen 1992 vermelde kosten zijn die waarvan in de artikelen 92 en 93 sprake is.

##### Art. 33

De in artikel 57, 3°, van het Wetboek van de inkomstenbelastingen 1992 vermelde kosten moeten worden vermeld in de daartoe voorziene rubriek van de individuele fiches en de samenvattende opgaven waarvan in artikel 32 sprake is.

### Afdeling XIII. - (Werkgeversbijdragen voor aanvullende verzekering tegen ouderdom en vroegtijdige dood (Wetboek van de inkomstenbelastingen 1992, artikel 59, tweede en vierde lid).) <KB 1995-09-01/42, art. 5; Inwerkingtreding : 01-01-1994>

##### Art. 34

Voor de toepassing van (de artikelen 52, 3°, b, en 5°, en 59), van het Wetboek van de inkomstenbelastingen 1992 en van deze afdeling, wordt verstaan : <KB 1995-09-01/42, art. 6, 019; Inwerkingtreding : 01-01-1994>  1° onder normale brutojaarbezoldiging : het totale brutobedrag van al de sommen die, voor aftrek van de verplichte inhoudingen ter uitvoering van de sociale wetgeving of van een ermede gelijkgesteld wettelijk of reglementair statuut, aan de werknemer anders dan uitzonderlijk of toevallig toegekend of betaald zijn gedurende een bepaald jaar;  2° onder laatste normale brutojaarbezoldiging : de brutojaarbezoldiging die gelet op de vorige bezoldigingen van de werknemer als normaal kan worden beschouwd en die hem betaald of toegekend werd gedurende het laatste jaar voor zijn oppensioenstelling waarin hij een normale beroepswerkzaamheid heeft gehad;  3° onder normale duur van een beroepswerkzaamheid : 40 jaar of, voor beroepen waarvoor de betrokken werkgever en werknemer aantonen dat de volledige loopbaan minder of meer dan 40 jaar bestrijkt, het aantal jaren van die volledige loopbaan.

Tabel die, zonder rekening te houden met overdraag baarheid of indexering

van de rente, voor ondersch eiden leeftijden bij aa nvang van de rente het,

nodig geachte kapitaal verm eldt voor een per twaal fden na vervallen

termijn beta albare rente van 1 e uro.

-

Leeftijd bij de aanvang van de rente Kapitaal in franken nodig  1 euro

- -

40 jaar en minder 17,7063

41 jaar 17,5247

42 jaar 17,3371

43 jaar 17,1434

44 jaar 16,9436

45 jaar 16,7376

46 jaar 16,5254

47 jaar 16,3069

48 jaar 16,0821

49 jaar 15,8510

50 jaar 15,6137

51 jaar 15,3701

52 jaar 15,1203

53 jaar 14,8644

54 jaar 14,6025

55 jaar 14,3347

56 jaar 14,0612

57 jaar 13,7820

58 jaar 13,4974

59 jaar 13,2077

60 jaar 12,9130

61 jaar 12,6137

62 jaar 12,3100

§ 3. De in § 2, 2°, bepaalde grens geldt niet voor bijdragen die gestort zijn om :  1° een ontoereikendheid van vroegere stortingen aan te vullen die voortvloeit uit een verhoging van de bezoldigingen of een verbetering van de gevestigde toekenningen;  2° voor werknemers die bij de onderneming gepresteerd hebben voor er een in § 1, 1°, vermeld verzekerings- of pensioenstelsel werd ingevoerd, voor het aldus gepresteerde aantal jaren van de normale duur van de beroepswerkzaamheid, de ontbrekende stortingen te compenseren;  3° werknemers die bij de onderneming een onvolledige loopbaan hebben, een pensioen toe te kennen berekend in verhouding tot een langere duur van beroepswerkzaamheid dan die welke zij bij de onderneming zullen vervullen, op voorwaarde dat die bijdragen slaan op maximaal 10 jaar van een vroeger werkelijk uitgeoefende beroepswerkzaamheid of op maximaal 5 jaar van een tot de normale pensioenleeftijd nog uit te oefenen beroepswerkzaamheid en dat het aldus in aanmerking genomen totaal aantal jaren het aantal jaren van de normale duur van hun beroepswerkzaamheid niet overtreft;  4° een verhoging toe te staan van de uitgestelde renten binnen de grens van 2 pct. per jaar te rekenen vanaf hun aanvang, evenals van de lopende renten, zonder dat die verhoging meer bedraagt dan die welke wordt verkregen door die renten te indexeren overeenkomstig de regeling die geldt voor de indexering van de pensioenen van de overheidssector.

### Afdeling XIV. - Degressieve afschrijvingen. (Wetboek van de inkomstenbelastingen 1992, artikel 64)

##### Art. 36. Wanneer een belastingplichtige die onderworpen is aan de personenbelasting, de

vennootschapsbelasting of de belasting van niet-inwoners, gekozen heeft voor het stelsel van degressieve afschrijving vermeld in artikel 64 van het Wetboek van de inkomstenbelastingen 1992, wordt het bedrag van de degressieve afschrijvingsannuiteit met betrekking tot elke groep van naar hetzelfde degressieve percent afschrijfbare vaste activa van gelijke aard, die als beroepskost aanneembaar is, bepaald :  1° voor het belastbare tijdperk dat loopt op de datum van het verkrijgen of tot stand brengen van die vaste activa, door, ongeacht die datum, op de aanschaffings- of beleggingswaarde een percent toe te passen dat niet meer bedraagt dan tweemaal het met de normale gebruiksduur van dezelfde vaste activa overeenstemmende lineaire afschrijvingspercent;  2° voor ieder volgend belastbaar tijdperk, door het overeenkomstig 1° vastgestelde percent toe te passen op de residuwaarde van de voormelde vaste activa, met andere woorden op de aanschaffings- of beleggingswaarde verminderd met de tot op het einde van het vorige belastbare tijdperk gedane en aangenomen afschrijvingen.

##### Art. 37

Voor de toepassing van artikel 36 wordt het lineaire afschrijvingspercent verkregen door het cijfer 100 te delen door het aantal jaren normale gebruiksduur van de afschrijfbare vaste activa. De lineaire afschrijvingsannuiteit is die welke tegen dat percent op de aanschaffings- of beleggingswaarde berekend is.

##### Art. 38

Met ingang van het belastbare tijdperk waarin de op een groep vaste activa toepasselijke degressieve afschrijvingsannuïteit de lineaire afschrijvingsannuïteit niet meer overtreft, heeft de belastingplichtige de mogelijkheid, tot wanneer de aanschaffings- of beleggingswaarde is bereikt, jaarlijks een lineaire toe te passen berekend overeenkomstig artikel 37.

##### Art. 39

Afschrijvingstekorten die voor enig belastbaar tijdperk betrekking hebben op een aan degressieve afschrijving onderworpen groep vaste activa, kunnen worden gecompenseerd door aanwending van voorheen belaste afschrijvingsexcedenten die op dezelfde groep vaste activa betrekking hebben.

##### Art. 40

Afschrijvingstekorten die tijdens de normale gebruiksduur niet zijn gecompenseerd op de in artikel 39 bepaalde wijze, kunnen na het verstrijken van die duur worden gecompenseerd door een of meer jaarlijkse afschrijvingen te doen die niet meer mogen bedragen dan de overeenkomstig artikel 37 berekende lineaire afschrijving.

##### Art. 41

Belastingplichtigen die het stelsel van degressieve afschrijving kiezen voor tijdens enig belastbaar tijdperk verkregen of tot stand gebrachte vaste activa, moeten die keuze aan de controle van de belastingen of aan het centraal taxatiekantoor van het ambtsgebied betekenen binnen de termijn die gesteld is voor het overleggen van de aangifte in de personenbelasting, de vennootschapsbelasting of de belasting van niet- inwoners over dat tijdperk; de betekening moet bij de aangifte worden gevoegd en vergezeld gaan van een opgave waarin voor elke groep van naar hetzelfde degressieve percent afschrijfbare vaste activa van gelijke aard die tijdens gezegd tijdperk zijn verkregen of tot stand gebracht, de volgende vermeldingen moeten voorkomen :  1° de aard van de verschillende aldus gegroepeerde vaste activa;  2° hun aanschaffings- of beleggingswaarde;  3° hun normale vermoedelijke gebruiksduur;  4° het degressieve afschrijvingspercent.

##### Art. 43

Het keuzestelsel van degressieve afschrijving is niet van toepassing op de volgende vaste activa :  1° personenauto's, auto's voor dubbel gebruik en minibussen, zoals deze zijn omschreven in de reglementering inzake inschrijving van motorvoertuigen, behoudens wanneer het voertuigen betreft die uitsluitend worden gebruikt voor een taxidienst of voor verhuring met bestuurder en op grond daarvan van de verkeersbelasting op de autovoertuigen zijn vrijgesteld;  2° vaste activa waarvan het gebruik aan derden is afgestaan door de belastingplichtige die de vaste activa afschrijft.

### Afdeling XIVbis. <Ingevoegd bij KB 2002-08-22/36, art. 1; Inwerkingtreding : 01-01-2003 (aanslagjaar 2003)> Beroepskosten met betrekking tot de verplaatsing tussen de woonplaats en de plaats van tewerkstelling (Wetboek van de inkomstenbelastingen 1992, artikel 66bis, tweede lid).

##### Art. 43.1


### Afdeling XV. - (Vrijstelling voor bijkomend personeel dat voor wetenschappelijk onderzoek, technologisch potentieel, uitvoer en integrale kwaliteitszorg wordt tewerkgesteld in België (Wetboek van de inkomstenbelastingen 1992, artikel 67, § 5);) <KB 1999-06-09/46, art. 1, 055; Inwerkingtreding : 01-01-1997>

##### Art. 44

<KB 1999-06-09/46, art. 2, 055; Inwerkingtreding : 01-01-1997> § 1. Onder hooggekwalificeerd onderzoeker moet worden verstaan ieder persoon die wordt tewerkgesteld voor wetenschappelijk onderzoek in de zin van artikel 67 van het Wetboek van de inkomstenbelastingen 1992 en die bovendien :  - houder is van een diploma van doctor, bekomen na de openbare verdediging van een verhandeling, of van geaggregeerde van het hoger onderwijs;  - en een totale anciënniteit van minstens 10 jaar kan rechtvaardigen, hetzij als persoon tewerkgesteld voor wetenschappelijk onderzoek in de zin van artikel 67 van voormeld Wetboek, hetzij in de zin van de wetenschappelijke anciënniteit vastgelegd in het koninklijk besluit van 21 april 1965 tot vaststelling van het statuut van het wetenschappelijk personeel der wetenschappelijke inrichtingen van de Staat.  § 2. De hooggekwalificeerd onderzoeker zoals bepaald in § 1, moet voltijds worden tewerkgesteld voor onderzoek en experimentele ontwikkeling.  Onder onderzoek en experimentele ontwikkeling verstaat men, creatief werk ondernomen op een systematische wijze met het doel de kennisvoorraad te verhogen en de aanwending van deze kennisvoorraad om nieuwe toepassingen te bedenken zoals de ontwikkeling van nieuwe produkten en procédés. Worden eveneens bedoeld, de bouw, de ontwikkeling en het testen van een prototype alsmede softwareontwikkeling voor zover het wetenschappelijke en technologische vooruitgang omvat.

##### Art. 45

<AR 1999-06-09/47, art. 1, 056; Inwerkingtreding : 01-01-1997> § 1. Voor de toepassing van artikel 67, § 1, 1° en 2° van het Wetboek van de inkomstenbelastingen 1992, worden de leden van het administratief personeel die niet rechtstreeks te maken hebben met opzoekingswerkzaamheden of de uitbouw van het technologisch potentieel van de onderneming, en van het toezichts-, onderhouds- en keukenpersoneel niet in aanmerking genomen.  § 2. Met betrekking tot het personeel dat wordt overgenomen naar aanleiding van verrichtingen als vermeld in de artikelen 46, § 1, eerste lid, 1° en 2°, 211, § 1 en 214, § 1, eerste lid, van hetzelfde Wetboek, zijn de bepalingen van artikel 67 van voormeld Wetboek, van toepassing bij de nieuwe belastingplichtige of overnemende, verkrijgende of uit de omzetting ontstane vennootschappen, alsof die verrichtingen niet hadden plaatsgevonden.  § 3. Er wordt voor de toepassing van artikel 67, § 1 van hetzelfde Wetboek, geen rekening gehouden met de tewerkstelling die het gevolg is van een overname van personeelsleden die voorheen waren tewerkgesteld door een belastingplichtige hetzij waarmee de onderneming zich rechtstreeks of onrechtstreeks in enigerlei band van wederzijdse afhankelijkheid bevindt, hetzij waarvan zij de beroepswerkzaamheid geheel of gedeeltelijk voortzet ingevolge een gebeurtenis die niet bedoeld is in § 2.

### Afdeling XVI. - Investeringsaftrek. ((Wetboek van de inkomstenbelastingen 1992, artikelen 69, § 2, 3e lid en 77)) <KB 2000-09-21/33, art. 1, 068; Inwerkingtreding : 01-01-1999>

##### Art. 47

Om de in de artikelen 68 tot 70 van het Wetboek van de inkomstenbelastingen 1992 vermelde investeringsaftrek te kunnen genieten moeten de belastingplichtigen bij hun aangifte in de inkomstenbelastingen van het belastbare tijdperk waarin de vaste activa zijn aangeschaft of tot stand gebracht :  1° een ingevuld, gedateerd en ondertekend formulier voegen, waarvan het model door de Minister van Financiën of zijn gedelegeerde wordt vastgelegd;  2° per categorie van de in de artikelen 69 en 70 van hetzelfde Wetboek vermelde vaste activa, een opgave voegen die voor elk activum vermeldt :  a) de datum van aanschaffing of totstandkoming;  b) de juiste benaming;  c) de aanschaffings- of beleggingswaarde;  d) de normale gebruiksduur en de afschrijvingsduur.

##### Art. 47bis


##### Art. 49

§ 1. Vaste activa (als vermeld in artikel 69, § 1, eerste lid, 2°,) van het Wetboek van de inkomstenbelastingen 1992 die dienen voor een rationeler energieverbruik, voor de verbetering van de industriële processen uit energetische overwegingen en voor de terugwinning van energie in de industrie, zijn de vaste activa die, blijkens een attest van de Executieve van het Gewest waar de investering plaatsvindt, behoren tot de vaste activa waarvan de lijst voorkomt in bijlage II. <KB 2000-09-21/33, art. 4, 068; Inwerkingtreding : 01-01- 1999>  § 2. Het attest moet door de belastingplichtige worden gevraagd :  - op straffe van verval binnen 3 maanden na de laatste dag van het belastbare tijdperk waarin de vaste activa zijn aangeschaft of tot stand gebracht;  - door middel van een formulier dat schriftelijk moet worden gevraagd bij de in § 1 vermelde Executieve, waaraan het behoorlijk ingevuld, gedagtekend en ondertekend moet worden teruggezonden.  Wanneer de belastingplichtige vaste activa heeft aangeschaft of tot stand gebracht die onder verschillende in bijlage II vermelde categorieën vallen, moet hij, per categorie een formulier indienen.  § 3. De belanghebbende belastingplichtigen moeten het in § 1 vermelde attest voorleggen, hetzij tot staving van de in artikel 47 vermelde stukken, hetzij, zo dit niet mogelijk is, binnen een termijn van maximaal 30 dagen te rekenen vanaf de dag waarop het attest is uitgereikt.

### Afdeling XVII. - (...) <KB 1995-09-01/42, art. 8, 019; Inwerkingtreding : 01-01-1993>

##### Art. 50. (Opgeheven) <KB 1995-09-01/42, art. 8, 019; Inwerkingtreding : 01-01-1993>

##### Art. 51. (Opgeheven) <KB 1995-09-01/42, art. 8, 019; Inwerkingtreding : 01-01-1993>

##### Art. 52. (Opgeheven) <KB 1995-09-01/42, art. 8, 019; Inwerkingtreding : 01-01-1993>

### Afdeling XVIII. - Belastingvrijstelling van prijzen en subsidies betaald of toegekend aan geleerden, schrijvers of kunstenaars. (Wetboek van de inkomstenbelastingen 1992, artikel 90, 2°, tweede lid)

### Afdeling XIX. - (Meerwaarden op onroerende goederen. (Wetboek van de inkomstenbelastingen 1992, artikel 101, § 3)) <KB 1997-05-20/39, art. 2; Inwerkingtreding : 01-01-1997>

### Afdeling XX. - Aftrek van uitgaven voor onderhoud en restauratie van beschermde onroerende goederen. (Wetboek van de inkomstenbelastingen 1992, (artikel 104,) 8°) <KB 2000-10-16/32, art. 1, 069; Inwerkingtreding : 09-11-2000>

##### Art. 55

§ 1. Voor de toepassing van (artikel 104,) 8°, van het Wetboek van de inkomstenbelastingen 1992 : <KB 2000-10-16/32, art. 2, 069; Inwerkingtreding : 09-11-2000>  1° worden beschouwd als uitgaven voor onderhoud en restauratie van beschermde gebouwde onroerende goederen, delen van gebouwde onroerende goederen of landschappen, de uitgaven die, met voorafgaand gunstig advies van de bevoegde Executieve betreffende de aard van de werken, gedaan zijn om die goederen of delen ervan in stand te houden of in hun vroegere staat te herstellen of om ze te valoriseren op historisch, artistiek, wetenschappelijk of esthetisch vlak of om ze voor het publiek toegankelijk te maken;  2° worden diezelfde goederen of delen ervan beschouwd voor het publiek toegankelijk te zijn wanneer zij, rekening houdend met hun specifiek karakter en op advies van de bevoegde Executieve, als zodanig erkend zijn bij beslissing van de Minister van Financiën of zijn gedelegeerde.  § 2. Belastingplichtigen die om de toepassing van voormeld artikel 104, eerste lid, 8°, verzoeken, voegen bij hun aangifte :  a) het beschermingsbesluit van het betreffende onroerend goed en de beslissing waarbij de toegankelijkheid ervan overeenkomstig § 1, 2°, is erkend;  b) de facturen en de betalingsbewijzen van de onderhouds- of restauratiewerken en een attest van de Executieve blijkens hetwelk die werken stroken met haar advies vermeld in § 1, 1°;  c) een verklaring op eer vermeldend of voor de onderhouds- of restauratiewerken subsidies zijn toegezegd, toegekend of betaald en, in bevestigend geval, het bedrag ervan.  § 3. (...) <KB 1994-08-12/48, art. 3, 006; Inwerkingtreding : 01-01-1992>

### Afdeling XXI. - Aanrekening van de van het totale netto-inkomen aftrekbare bestedingen. (Wetboek van de inkomstenbelastingen 1992, artikel 106)

##### Art. 56

De krachtens artikel 104 van het Wetboek van de inkomstenbelastingen 1992 van het totale netto- inkomen aftrekbare bestedingen worden evenredig aangerekend op de verschillende inkomstencategorieën.

### Afdeling XXII. - (Instellingen die giften ontvangen. (Wetboek van de inkomstenbelastingen 1992, artikelen 108 en 110)) <KB 2001-03-04/30, art. 1; Inwerkingtreding : 24-03-2001>

##### Art. 59

§ 1. Voor de toepassing van (artikel 104,) 3°, g, van het Wetboek van de inkomstenbelastingen 1992, kunnen worden erkend de instellingen opgericht voor hulpverlening aan slachtoffers van rampen die de toepassing rechtvaardigen van de wet betreffende het herstel van schade veroorzaakt aan private goederen door natuurrampen, op voorwaarde : <KB 2000-10-16/32, art. 5, 069; Inwerkingtreding : 09-11-2000>  1° dat zij rechtspersoonlijkheid bezitten krachtens het Belgisch publiekrecht of privaatrecht;  2° dat zij generlei gewin bejagen, noch voor zichzelf, noch voor hun leden als zodanig;  3° dat hun werkzaamheden uitsluitend gericht zijn op hulpverlening aan de hierboven vermelde slachtoffers.  De erkenning wordt voor een periode van ten hoogste (6 opeenvolgende kalenderjaren) toegestaan. <KB 2000- 10-16/32, art. 5, 069; Inwerkingtreding : 09-11-2000>  § 2. Om te worden erkend moeten de instellingen als vermeld in § 1 daartoe een schriftelijke aanvraag indienen in de vorm en binnen de termijnen als hierna bepaald.  § 3. De aanvragen om erkenning moeten uiterlijk op 31 december van het jaar dat voorafgaat aan de periode waarvoor de erkenning wordt aangevraagd, bij de Minister van Financiën worden ingediend; de termijn mag evenwel niet korter zijn dan 3 maanden vanaf de datum van de oprichting van de aanvragende instelling.  (In afwijking van het voorgaande lid, kan een aanvraag om erkenning eveneens geldig worden ingediend binnen een termijn van 3 maanden vanaf de datum van de aanvang van de hulpverlening door de betrokken instelling. In dat geval wordt de erkenning toegestaan voor een periode van ten hoogste 3 kalenderjaren. Wat het eerste kalenderjaar betreft, geldt de erkenning pas vanaf de aanvang van de hulpverlening.) <KB 2000-10-16/32, art. 5, 069; Inwerkingtreding : 09-11-2000>  § 4. Die aanvragen om erkenning moeten worden gestaafd met een voor eensluidend verklaard afschrift van de rekening van de ontvangsten en uitgaven van het laatst afgesloten boekjaar en van de begroting van het lopende boekjaar, en moeten omvatten :  1° alle nuttige gegevens om te kunnen onderzoeken of de aanvragende instelling aan de in § 1 gestelde voorwaarden voldoet;  2° een verklaring waarbij de aanvragende instelling de verbintenis aangaat :  a) tot het dekken van kosten van algemeen beheer geen hoger bedrag te zullen besteden dan 20 pct. van haar bestaansmiddelen van alle aard, vooraf verminderd met die welke voortkomen van andere erkende instellingen;  b) aan de schenkers een ontvangstbewijs uit te reiken waarvan het model door de Minister van Financiën of zijn gedelegeerde wordt vastgesteld en bij de administratie der directe belastingen binnen 2 maanden na het einde van ieder kalenderjaar van de periode waarvoor de erkenning is toegestaan een afschrift van de tijdens dat jaar uitgereikte ontvangstbewijzen en een verzamelstaat of -attest daarvan in te leveren;  c) de ambtenaren van de administratie der directe belastingen toe te staan haar boekhouding te controleren telkens als zij dat nuttig achten;  d) aan de diensten die worden aangewezen door de Minister van Financiën, binnen een maand na het eerste verzoek van die diensten, alle inlichtingen te verstrekken die voor het onderzoek van de aanvraag om erkenning nuttig zijn.  § 5. De Minister van Financiën beslist over de aanvraag om erkenning.  Zijn beslissing wordt aan de aanvragende instelling betekend.  § 6. Ingeval een instelling één van de voor haar erkenning gestelde voorwaarden niet nakomt, kan haar erkenning ambtshalve worden ingetrokken of geweigerd door een beslissing van de Minister van Financiën.  De intrekking van de erkenning treedt in werking vanaf de 1e januari die volgt op de datum van betekening van de beslissing.

##### Art. 59quinquies

(Ingevoegd bij KB 2001-03-04/30, art. 3; Inwerkingtreding : 01-01-2000) § 1. Voor de toepassing van artikel 104, 3°, j, van het Wetboek van de inkomstenbelastingen 1992, zoals ingevoegd door de wet van 21 april 1999 tot wijziging van artikel 104 van hetzelfde Wetboek teneinde de giften in geld aan erkende dierenasielen fiscaal aftrekbaar te maken, moeten de werkzaamheden van de VZW rechtstreeks en uitsluitend gericht zijn op het beheer van dierenasielen zoals gedefinieerd door het koninklijk besluit van 17 februari 1997 houdende de erkenningsvoorwaarden voor hondenkwekerijen, kattenkwekerijen, dierenasielen, dierenpensions en handelszaken voor dieren, en de voorwaarden inzake de verhandeling van dieren.  § 2. Teneinde de machtiging te verkrijgen om voor een periode van ten hoogste zes opeenvolgende kalenderjaren ontvangstbewijzen uit te reiken die recht geven op de aftrek van de giften die zijn gedaan aan de in § 1 bedoelde VZW, moeten deze laatsten daartoe een schriftelijke aanvraag indienen in de vorm en binnen de termijnen als hierna bepaald.  § 3. (NOTA van Justel : Zie afwijking van onderhavig artikel 59quinquies, § 3, in KB 2001-03-04/30, art. 5.) De aanvragen om machtiging moeten uiterlijk op 31 december van het jaar dat voorafgaat aan de periode waarvoor de machtiging wordt aangevraagd, bij de Minister van Financiën worden ingediend; de termijn mag evenwel niet korter zijn dan drie maanden vanaf de datum van de oprichting van de aanvragende VZW.  § 4. De aanvragen om machtiging moeten omvatten :  1° een voor eensluidend verklaard afschrift van het gedateerde en gehandtekende erkenningsbewijs afgeleverd overeenkomstig het koninklijk besluit van 17 februari 1997 houdende de erkenningsvoorwaarden voor hondenkwekerijen, kattenkwekerijen, dierenasielen, dierenpensions en handelszaken voor dieren, en de voorwaarden inzake de verhandeling van dieren;  2° alle nuttige gegevens die de diensten, belast met de behandeling van de machtigingsaanvraag, in de mogelijkheid stellen te onderzoeken of de aanvragende VZW aan de in § 1 gestelde voorwaarden voldoet;  3° een verklaring waarbij de aanvragende VZW de verbintenis aangaat :  a) tot het dekken van kosten van algemeen beheer geen hoger bedrag te zullen besteden dan 20 pct. van haar bestaansmiddelen van alle aard, vooraf verminderd met die welke voortkomen van andere erkende instellingen;  b) aan de schenkers een ontvangstbewijs uit te reiken waarvan het model door de Minister van Financiën of zijn gedelegeerde wordt vastgesteld, en bij de administratie van de ondernemings- en inkomensfiscaliteit binnen de twee maanden na het einde van ieder kalenderjaar van de periode waarvoor de machtiging is verkregen een afschrift van de tijdens dat jaar uitgereikte ontvangstbewijzen en een verzamelstaat of -attest daarvan in te leveren;  c) de ambtenaren van de administratie van de ondernemings- en inkomensfiscaliteit toe te staan haar boekhouding te controleren telkens als zij dat nuttig achten;  d) aan de diensten bevoegd voor de machtiging, binnen een maand na het eerste verzoek van die diensten, alle inlichtingen te verstrekken die voor het onderzoek van de aanvraag om machtiging nuttig zijn.  Die aanvragen moeten bovendien worden gestaafd met een eensluidend verklaard afschrift van de rekening van de ontvangsten en uitgaven van het laatst afgesloten boekjaar en van de begroting van het lopende boekjaar.  § 5. De beslissing van de Minister van Financiën wordt aan de aanvragende VZW betekend.  § 6. Ingeval een VZW de voor haar machtiging gestelde voorwaarden niet nakomt, kan haar machtiging ambtshalve worden ingetrokken of geweigerd door een beslissing van de Minister van Financiën.  De intrekking van de machtiging treedt in werking vanaf de 1 januari die volgt op de datum van betekening van de beslissing.

##### Art. 60

<KB 1994-01-20/37, art. 1, 002; Inwerkingtreding : 01-01-1994> De Minister van Financiën of zijn gedelegeerde kan vergunning verlenen om de in de artikelen 57, § 4, 2°, b, 58, § 4, 2°, b, (, 59, § 4, 2°, b en 59bis, § 4, 2°, b en 59ter, § 4, 2°, b, 59quater, § 4, 2°, b, en 59quinquies, § 4, 3°, b,) vermelde afschriften van de uitgereikte ontvangstbewijzen evenals de verzamelstaat of het verzamelattest daarvan te vervangen door een magnetische informatiedrager. <KB 2001-03-04/30, art. 4, 080; Inwerkingtreding : 24-03-2001>  De vergunning vermeldt de na te leven voorwaarden en kan steeds worden ingetrokken.

### Afdeling XXIII. - Aftrek van uitgaven voor kinderoppas. (Wetboek van de inkomstenbelastingen 1992, artikel 113, § 2)

##### Art. 61

Het hoogst aftrekbare bedrag van de uitgaven voor kinderoppas vermeld in artikel 113, § 1, van het Wetboek van de inkomstenbelastingen 1992, is, na de toepassing van de door (artikel 104, 7°), van hetzelfde Wetboek ingestelde beperking tot 80 pct., bepaald (op (11,20 EUR) per oppasdag en kind). <KB 2000-01-27/30, art. 1, 060; Inwerkingtreding : 01-01-1999> <KB 2000-07-20/63, art. 2, 075; Inwerkingtreding : 01-01-2002>

### Afdeling XXIV. - Aftrek van interest van hypothecaire leningen aangegaan voor het vernieuwen van een woning. (Wetboek van de inkomstenbelastingen 1992, artikel 115, 2°, b)

##### Art. 63

§ 1. Het door één van de echtgenoten tijdens het belastbare tijdperk of tijdens een vorig belastbaar tijdperk geleden beroepsverlies, dat krachtens artikel 129 van het Wetboek van de inkomstenbelastingen 1992 geheel of gedeeltelijk op de beroepsinkomsten van de andere echtgenoot kan worden aangerekend, wordt evenredig afgetrokken van de overeenkomstig artikel 23 van hetzelfde Wetboek vastgestelde beroepsinkomsten uit de verschillende beroepswerkzaamheden van deze echtgenoot, die gezamenlijk worden belast of die overeenkomstig artikel 155 van hetzelfde Wetboek zijn vrijgesteld krachtens internationale overeenkomsten ter voorkoming van dubbele belasting; het eventuele saldo wordt evenredig aangerekend op de beroepsinkomsten die afzonderlijk worden belast.  § 2. De aanrekening van de respectievelijk (in de §§ 1, 2 en 3) van artikel 103 van hetzelfde Wetboek vermelde verliezen op de diverse inkomsten van de andere echtgenoot, gebeurt evenredig binnen de in dat artikel gestelde grenzen. <KB 1997-05-20/39, art. 4, 039; Inwerkingtreding : 01-01-1997>

### Afdeling XXVbis. - (Persoonlijke bijdragen voor aanvullende verzekering tegen ouderdom en vroegtijdige dood (Wetboek van de inkomstenbelastingen 1992, artikel 145.3, derde lid).) <Ingevoegd bij KB 1995-09-01/42, art. 9; Inwerkingtreding : 01-01-1994>

##### Art. 63.1


### Afdeling XXVter. - (Voorwaarden en wijze waarop de vermindering voor het lange termijnsparen wordt toegepast met betrekking tot premies van individuele levensverzekeringen en betalingen voor de aflossing of wedersamenstelling van hypotheekleningen (Wetboek van de inkomstenbelastingen 1992, artikel 145.6, derde lid).) <Ingevoegd bij KB 1995-09-01/42, art. 10; Inwerkingtreding : 01-01-1993>

##### Art. 63.2


##### Art. 63.3

<KB 2001-01-30/38, art. 1, 079; Inwerkingtreding : 01-01-2001> Betalingen voor de aflossing of wedersamenstelling van een hypothecaire lening die is aangegaan om een in België gelegen woning te bouwen, te verwerven of te verbouwen, worden, binnen de grenzen gesteld in artikel 1456, eerste en tweede lid van het Wetboek van de inkomstenbelastingen 1992, slechts in aanmerking genomen voor de vermindering van het lange termijnsparen indien de belastingplichtige het bewijs van die betalingen overlegt, zomede een attest waarvan het model door de Minister van Financiën of zijn gedelegeerde wordt vastgesteld, waarbij de instelling die de lening heeft toegestaan :  a) bevestigt dat het leningscontract aan de in artikel 1455 van hetzelfde Wetboek gestelde voorwaarden voldoet;  b) er zich toe verbindt de taxatiedienst van het ambtsgebied van de belastingplichtige in kennis te stellen van alle wijzigingen die aan het contract worden aangebracht.

##### Art. 63.4


### Afdeling XXVquater. - (Inlichtingen te verstrekken betreffende betalingen voor pensioensparen (artikelen 21, 8°, 145.10, tweede lid, 145.12, zesde lid, en 263, tweede lid, van het Wetboek van de inkomstenbelastingen 1992).) <Ingevoegd bij KB 1995-09-01/42, art. 11; Inwerkingtreding : 01-01-1993>

### Afdeling XXVquinquies. - (Voorwaarden tot toekenning en behoud van de erkenning van pensioenspaarfondsen (artikel 145.16, 1°, Wetboek van de inkomstenbelastingen 1992).) <Ingevoegd bij KB 1995-09-01/42, art. 12; Inwerkingtreding : 01-01-1993>

##### Art. 63.6


##### Art. 63.8


##### Art. 63.9


### Afdeling XXVsexies. - <KB 2002-04-02/41, art. 1, 088; Inwerkingtreding : 01-01-2002> Vermindering voor uitgaven betaald voor prestaties in het kader van plaatselijke werkgelegenheidsagentschappen en voor prestaties betaald met dienstencheques (Wetboek van de inkomstenbelastingen 1992, artikel 14522)

##### Art. 63.10

<KB 2002-04-02/41, art. 1, 088; Inwerkingtreding : 01-01-2002> De in artikel 14521 van het Wetboek van de inkomstenbelastingen 1992 vermelde uitgaven komen slechts voor belastingvermindering in aanmerking :  1° wat de uitgaven betaald voor prestaties in het kader van plaatselijke werkgelegenheidsagentschappen betreft :  a) ten belope van de nominale waarde van de PWA-cheques die op naam van de belastingplichtige zijn uitgegeven en die hij tijdens het belastbaar tijdperk bij de uitgever heeft aangekocht, verminderd met de nominale waarde van die PWA-cheques die in de loop van datzelfde belastbaar tijdperk aan de uitgever zijn terugbezorgd;  b) op voorwaarde dat de belastingplichtige tot staving van zijn aangifte in de inkomstenbelastingen het attest overlegt vermeld in de reglementering betreffende de plaatselijke werkgelegenheidsagentschappen en uitgereikt door de uitgever van de PWA-cheques;  2° wat de uitgaven betaald voor prestaties betaald met dienstencheques betreft :  a) ten belope van de aanschafprijs van de dienstencheques die op naam van de belastingplichtige zijn uitgegeven en die hij tijdens het belastbaar tijdperk bij het uitgiftebedrijf heeft aangekocht, verminderd met de aanschafprijs van die dienstencheques die in de loop van datzelfde belastbaar tijdperk door het uitgiftebedrijf aan de belastingplichtige werden terugbetaald;  b) op voorwaarde dat de belastingplichtige tot staving van zijn aangifte in de inkomstenbelastingen het attest overlegt vermeld in de reglementering betreffende de buurtdiensten en -banen en uitgereikt door de uitgever van de dienstencheques.

### Afdeling XXVsepties. - <Ingevoegd bij KB 2002-12-20/36, art. 1; Inwerkingtreding : 01-01-2004> Vermindering voor energiebesparende uitgaven (Wetboek van de inkomstenbelastingen 1992, artikel 145.24)

### Afdeling XXVI. - Voorafbetalingen - Belastingvermeerdering - Bonificatie. (Wetboek van de inkomstenbelastingen 1992, artikelen 162, eerste lid, 167, 175 en 376, § 4)

##### Art. 64

Overeenkomstig artikel 162, eerste lid, van het Wetboek van de inkomstenbelastingen 1992 wordt het vermeerderingspercentage vastgesteld in verhouding tot de basisrentevoet die in de tabel hierna is aangegeven :

Aanslagjaar Basisrentevoet

- -

1993 9

[1996 7]

<KB 1995-03-16/30, art. 1, 014; Inwerkingtreding : 01-01-1996>

##### Art. 65

Voor de aan de personenbelasting of de overeenkomstig artikel 227, 1°, van het Wetboek van de inkomstenbelastingen 1992 aan de belasting van niet-inwoners onderworpen belastingplichtigen die winst, baten of bezoldigingen (van bedrijfsleiders) behalen en die voorafbetalingen doen als vermeld in de artikelen 157 tot 166 en 175 tot 177 van hetzelfde Wetboek, worden die voorafbetalingen ten belope van het bedrag dat nodig is om de in voormeld artikel 157 bepaalde vermeerdering te vermijden, bij voorrang als in voormelde artikelen 157 tot 166 vermelde voorafbetalingen beschouwd. <KB 1997-05-20/39, art. 5, 039; Inwerkingtreding : 01-01- 1997>  Voor de berekening van die vermeerdering worden de in het vorige lid vermelde inkomsten geacht betrekking te hebben op een volledig kalenderjaar, zelfs wanneer het tijdperk van de uitoefening van de beroepswerkzaamheid waaruit de inkomsten voortkomen niet volledig samenvalt met dat kalenderjaar.

##### Art. 67

<KB 1995-01-03/30, art. 1, 011; Inwerkingtreding : 01-01-1995> § 1. (Voorafbetalingen als vermeld in de artikelen 157 tot 166 en 175 tot 177 van het Wetboek van de inkomstenbelastingen 1992 kunnen uitsluitend worden gedaan bij de "Dienst der Voorafbetalingen" door storting of overschrijving op postrekeningen:  a) nr. 679-2002340-66, voor voorafbetalingen betreffende natuurlijke personen;  b) nr. 679-2002330-56, voor voorafbetalingen betreffende rechtspersonen.) <KB 1999-11-09/33, art. 1, 059; Inwerkingtreding : 17-12-1999>  § 2. Voor de in § 1 vermelde stortingen of overschrijvingen mogen alleen betaalformulieren worden gebruikt :  - waarvan het model door de Minister van Financiën of zijn gedelegeerde is vastgesteld in overleg met de Minister, of zijn gedelegeerde, tot wiens bevoegdheid de Post behoort;  - die op aanvraag of ambtshalve door de " Dienst der Voorafbetalingen " worden uitgereikt en de naam van de belastingplichtige en een registratienummer bij die dienst vermelden.  § 3. Betalingen op de in § 1 vermelde (postrekeningen) met vermelding van een als in § 3 bedoeld registratienummer worden geacht gedaan te zijn voor rekening van de belastingplichtige die bij de " Dienst der Voorafbetalingen " door dat nummer is geïdentificeerd. <KB 1999-11-09/33, art. 3, 059; Inwerkingtreding : 17- 12-1999>

##### Art. 68

De artikelen 139, § 3, en 142, zijn van toepassing op de stortingen of overschrijvingen van voorafbetalingen.

##### Art. 69

Uit het oogpunt van de rijkscomptabiliteit, worden voorafbetalingen gelijkgesteld met de in de artikelen 270 tot 275 van het Wetboek van de inkomstenbelastingen 1992 vermelde bedrijfsvoorheffing.

##### Art. 71

§ 1. Na het verstrijken van het belastbare tijdperk zendt (de "Dienst der Voorafbetalingen") aan de betrokken belastingplichtigen een ontvangstbewijs van de gedane stortingen of overschrijvingen, dat hierna "rekeninguittreksel VA" wordt genoemd. <KB 1995-01-03/30, art. 2, 011; Inwerkingtreding : 01-01-1995>  § 2. Vanaf de verzending van het rekeninguittreksel VA beschikt de belastingplichtige over een termijn van 1 maand om de toepassing van artikel 70 te vragen, voor zover die termijn eindigt na die welke in datzelfde artikel 70 zijn bepaald.  Daartoe moet het rekeninguittreksel VA ter vervanging worden teruggezonden aan de dienst waarvan het is uitgegaan.  § 3. Wanneer die dienst de oorspronkelijke bestemming van de voorafbetalingen overeenkomstig artikel 70 en § 2, van onderhavig artikel, heeft gewijzigd en, in voorkomend geval, het rekeninguittreksel VA heeft vervangen, zijn de aanvankelijk gedane stortingen of overschrijvingen, in zover zij van bestemming zijn veranderd, van rechtswege nietig en worden de eraan verbonden voordelen opgeheven.

##### Art. 72. (Opgeheven) <KB 1997-05-20/39, art. 6, 039; Inwerkingtreding : 01-01-1996>

### Afdeling XXVII. - Omzetting in rente van kapitalen en afkoopwaarden. (Wetboek van de inkomstenbelastingen 1992, artikel 169, § 1)

##### Art. 73

Kapitalen en afkoopwaarden als vermeld in artikel 169 van het Wetboek van de inkomstenbelastingen 1992, worden voor de vaststelling van de belastbare grondslag slechts in aanmerking genomen tot het bedrag van de lijfrente die verkregen wordt door hun omzetting tegen het percent dat in de onderstaande tabel is vermeld tegenover de leeftijd van de verkrijger op de datum waarop het kapitaal of de afkoopwaarde hem wordt betaald of toegekend; die leeftijd wordt in volle jaren en met weglating van de gedeelten van een jaar vastgesteld.

Leeftijd van de verkrijger op de Percent voor omzetting van

datum van betaling of toekenning kapitalen of afkoopwaarden

van het kapitaal of de afkoopwaarde in lijfrente

(1) (2)

- -

40 jaar en minder 1

41 tot 45 jaar 1,5

46 tot 50 jaar 2

51 tot 55 jaar 2,5

56 tot 58 jaar 3

59 en 60 jaar 3,5

61 en 62 jaar 4

63 en 64 jaar 4,5

65 jaar en meer 5

### Afdeling XXVIIbis. <Ingevoegd bij KB 1999-05-13/44, art. 1; Inwerkingtreding : 01-01-2000> - Voorwaarden en grenzen van de vrijstelling van de technische voorzieningen (Wetboek van de inkomstenbelastingen 1992, artikel 194bis).

##### Art. 73.1


##### Art. 73.3


##### Art. 73.4


### Afdeling XXVIIter. <Ingevoegd bij AR 2003-02-06/30, art. 1; Inwerkingtreding : 01-01-2004> - Investeringsmodaliteiten in het kader van de investeringsreserve ingeval van inbreng van een tak van werkzaamheid of een bedrijfsafdeling of van een algemeenheid van goederen of ingeval van fusie of splitsing (Wetboek van de inkomstenbelastingen 1992, artikel 194quater , § 6, eerste lid)

##### Art. 73.4bis


### Afdeling XXVIIquater. - (Definitief belaste inkomsten (Wetboek van de inkomstenbelastingen 1992, artikelen 202, § 2, tweede lid en 203, § 1, derde lid en § 2, zesde lid, 2°)) <KB 2003-02-13/33, art. 1, Inwerkingtreding : 01-01-2004> (NOTA 1: Ingevoegd bij KB 2000-11-29/33, art. 1; Inwerkingtreding : 28-11-2000 onder de titel "Erkenningsvoorwaarden waaraan een gecentraliseerd systeem voor het lenen en ontlenen van aandelen dat geïntegreerd is in een betalings- en afwikkelingssysteem van effectenverrichtingen moet voldoen en de periode gedurende dewelke de erkenning kan worden verleend (Wetboek van de inkomstenbelastingen 1992, artikel 203, § 2, 6de lid, 2°)") (NOTA 2 : oude afdeling XXVIIter, hernummerd XXVIIquater door KB 2003-02-06/30)

##### Art. 73.4quater


##### Art. 73.6


##### Art. 73.7


##### Art. 73.9


##### Art. 73.10


##### Art. 73.11


### Afdeling XXVIII. - Vaststelling van het belastbare inkomen inzake vennootschapsbelasting. (Wetboek van de inkomstenbelastingen 1992, artikel 207)

##### Art. 74

Om het aan de vennootschapsbelasting te onderwerpen resultaat vast te stellen, wordt het resultaat van het belastbare tijdperk, waarin niet zijn begrepen de krachtens de artikelen 48, 190, 191 en 194 van het Wetboek van de inkomstenbelastingen 1992 vrijgestelde waardeverminderingen, voorzieningen of meerwaarden, vooraf volgens bestemming in de volgende categorieën onderverdeeld :  1° reserves;  2° verworpen uitgaven;  3° dividenden.  Voor de toepassing van het eerste lid moet worden verstaan :  1° onder "reserves", het gereserveerde resultaat, verminderd met :  - het gedeelte van de meerwaarde op in artikel 66 van hetzelfde Wetboek vermelde voertuigen dat niet in aanmerking wordt genomen krachtens artikel 24, derde lid, van hetzelfde Wetboek en artikel 40, § 1, van de wet van 7 december 1988 houdende hervorming van de inkomstenbelasting en wijziging van de met het zegel gelijkgestelde taksen;  - de krachtens de artikelen 192 en 521 van hetzelfde Wetboek vrijgestelde meerwaarden op aandelen en de tijdens het belastbare tijdperk teruggenomen waardeverminderingen op aandelen die voorheen krachtens artikel 198, 7°, van hetzelfde Wetboek als verworpen uitgaven zijn belast, in zover die waardeverminderingen op het einde van dat belastbare tijdperk niet meer verantwoord zijn;  - de opnemingen van gestort kapitaal in de zin van artikel 184 van hetzelfde wetboek, met uitsluiting van de terugbetalingen van gestort kapitaal ter uitvoering van een regelmatige beslissing tot vermindering van het maatschappelijke kapitaal, getroffen overeenkomstig de bepalingen van de gecoördineerde wetten op de handelsvennootschappen;  - de winst die voortvloeit uit tijdens het belastbare tijdperk verkregen terugbetalingen van belastingen die vroeger niet als beroepskosten zijn aangenomen en de regulariseringen van geraamde belastingschulden die voorheen als verworpen uitgaven zijn belast, in zover die terugbetalingen en regulariseringen niet kunnen worden afgetrokken van de niet-aftrekbare belastingen die bij de verworpen uitgaven van het belastbare tijdperk moeten worden gevoegd;  2° onder "verworpen uitgaven" :  - de niet als beroepskosten aftrekbare bedragen;  - het bedrag - voor aftrek van het vrijgestelde gedeelte - van de giften als zijn vermeld (in artikel 104, 3° tot 4°bis en 5°, a,) van hetzelfde Wetboek; <KB 1998-10-29/37, art. 3, 2°, 045; Inwerkingtreding : 1995-04-10>  - de voorheen vrijgestelde winst die belastbaar wordt in de loop van het belastbare tijdperk, voor zover ze niet in het gereserveerde resultaat is begrepen;  - onder "dividenden", de dividenden vermeld in artikel 18 van hetzelfde Wetboek.

##### Art. 76

Van het saldo van de winst dat overeenkomstig de artikelen 74 en 75 is vastgesteld en onderverdeeld, worden achtereenvolgens afgetrokken, in zover ze er nog in voorkomen :  1° de bij verdrag vrijgestelde winst;  2° in globo :  a) het gedeelte van de winst dat ingevolge artikel 67 van het Wetboek van de inkomstenbelastingen 1992 is vrijgesteld wegens zijn aanwending voor bijkomend personeel voor wetenschappelijk onderzoek;  b) het vrijgestelde gedeelte van giften als zijn vermeld (in artikel 104, 3° tot 4°bis en 5°, a,) van hetzelfde Wetboek; <KB 1998-10-29/37, art. 4, 2°, 045; Inwerkingtreding : 1995-04-10>  c) de andere niet-belastbare bestanddelen die in de winst voorkomen en niet in dit artikel zijn vermeld.  De som van de in het eerste lid, 2°, vermelde bedragen wordt bij voorrang van de Belgische winst van het belastbare tijdperk afgetrokken en, tot het eventuele overschot, van de tegen verlaagd tarief belastbare winst van dat tijdperk.

##### Art. 77

De in de artikelen 202 tot 205 van het Wetboek van de inkomstenbelastingen 1992 omschreven bedragen die als definitief belaste inkomsten of als vrijgestelde roerende inkomsten aftrekbaar zijn, worden, tot het bedrag van de restwinst na toepassing van artikel 76 afgetrokken; die aftrek gebeurt met inachtneming van de oorsprong van de winst en bij voorrang van de winst waarin die bedragen voorkomen.

##### Art. 78

Van de overeenkomstig de artikelen 74 tot 77 vastgestelde winst worden de in artikel 206 van het Wetboek van de inkomstenbelastingen 1992 vermelde vorige beroepsverliezen afgetrokken in zover die verliezen, vastgesteld overeenkomstig de wetgeving die van toepassing is voor de betreffende belastbare tijdperken, niet vroeger konden worden afgetrokken of voorheen niet door bij verdrag vrijgestelde winst waren gedekt of niet vroeger onder de vennoten werden verdeeld.  Die aftrek gebeurt volgens de regelen van artikel 75, tweede lid, met dien verstande dat verliezen die geleden zijn in landen waarvoor de winst bij verdrag is vrijgesteld, slechts worden afgetrokken in zover ze de bij verdrag vrijgestelde winst overtreffen.

##### Art. 79

De in de artikelen 68 tot 77 en 201 van het Wetboek van de inkomstenbelastingen 1992 vermelde investeringsaftrek, wordt vervolgens afgetrokken van het bedrag van de Belgische winst dat overblijft na toepassing van artikel 78.

### Afdeling XXIX. - Vaststelling van het maatschappelijk kapitaal en van de waardeverminderingen, voorzieningen, reserves en meerwaarden ingeval de inbrengen niet volledig worden vergoed met nieuwe aandelen die naar aanleiding van de in artikel 21, § 1, van het Wetboek van de inkomstenbelastingen 1992 vermelde verrichtingen worden uitgegeven. (Wetboek van de inkomstenbelastingen 1992, artikel 214, tweede lid)

##### Art. 80. (Opgeheven) <KB 1994-08-12/48, art. 6, 006; Inwerkingtreding : 01-10-1993>

##### Art. 81. (Opgeheven) <KB 1994-08-12/48, art. 6, 006; Inwerkingtreding : 01-10-1993>

##### Art. 82. (Opgeheven) <KB 1994-08-12/48, art. 6, 006; Inwerkingtreding : 01-10-1993>

## HOOFDSTUK II. - VOORHEFFINGEN EN VERREKENING VAN VOORHEFFINGEN.

### Afdeling I. - Roerende voorheffing. (Wetboek van de inkomstenbelastingen 1992, artikelen 250, 300, § 1 en 312)

##### Art. 84

De roerende voorheffing is betaalbaar (bij de bevoegde) ontvanger van de directe belastingen volgens de regels van hoofdstuk III, afdeling III. <KB 1999-05-03/39, art. 2, 053; Inwerkingtreding : 06-04-1999>

##### Art. 85

Bij iedere storting van roerende voorheffing of ten laatste binnen 15 dagen na de toekenning of betaalbaarstelling van de belastbare inkomsten, overhandigt de belastingschuldige aan de in artikel 84 vermelde ontvanger een aangifte van die inkomsten waarvan het model door de Minister van Financiën of zijn gedelegeerde wordt vastgesteld.  Tot staving van die aangifte kan de administratie der directe belastingen een tot bewijs strekkend uittreksel uit de boeken of rekeningen van de belastingschuldige, door hem of zijn vertegenwoordiger gedateerd, getekend en echt verklaard, doen overleggen.

### Afdeling II. - Bedrijfsvoorheffing. (Wetboek van de inkomstenbelastingen 1992, artikelen (57,) 250, 271, 275, §§ 1 en 2, 300, § 1, en 312) <KB 1994-08-12/48, art. 7; Inwerkingtreding : 20-09-1994>

##### Art. 86

Natuurlijke en rechtspersonen, zomede alle personen die geheel of ten dele, uit welken hoofde ook, de leiding of het beheer van vennootschappen, verenigingen, instellingen of lichamen zonder rechtspersoonlijkheid waarnemen, moeten de bedrijfsvoorheffing die aan de bron verschuldigd is op de door hen betaalde of toegekende en in artikel 87 vermelde inkomsten, in de Schatkist storten.

##### Art. 87

Behoudens de door de wet en door internationale overeenkomsten bepaalde vrijstellingen, is de bedrijfsvoorheffing aan de bron verschuldigd op :  1° (a) beroepsinkomsten als vermeld in artikel 23, § 1, 4° en 5°, van het Wetboek van de inkomstenbelastingen 1992 die de in de artikelen 3, 179 of 220 van hetzelfde Wetboek vermelde personen als schuldenaar, bewaarder, mandataris of tussenpersoon in België of in het buitenland betalen of toekennen;  b) beroepsinkomsten als vermeld in artikel 23, § 1, 4° en 5°, van voormeld Wetboek die de in artikel 227 van hetzelfde Wetboek vermelde niet-inwoners in België of in het buitenland betalen of toekennen, voor wie die inkomsten beroepskosten zijn in de zin van artikel 237 van hetzelfde Wetboek;) <KB 1999-06-24/34, art. 1, 057; Inwerkingtreding : 1999-08-24>  2° bezoldigingen die volledig of hoofdzakelijk bestaan uit fooien of dienstpercenten, door de cliënteel betaald aan personen die in België krachtens een arbeidsovereenkomst tewerkgesteld zijn door belastingschuldigen als vermeld in artikel 86;  3° prijzen, subsidies, renten of pensioenen als vermeld in artikel 90, 2°, van hetzelfde Wetboek;  4° uitkeringen of kapitalen als vermeld in artikel 90, 3° en 4°, van hetzelfde Wetboek, die rijksinwoners betalen of toekennen aan niet-rijksinwoners;  5° hierna vermelde inkomsten wanneer zij aan niet-inwoners als vermeld in artikel 227 van hetzelfde Wetboek, worden betaald of toegekend :  a) winst en baten als vermeld in artikel 90, 1°, van hetzelfde Wetboek;  b) commissielonen, provisies, vacatiegelden, toelagen, erelonen en alle andere vergoedingen wegens prestaties of diensten van welke aard ook, zomede auteurs-reproduktie- en andere gelijkaardige rechten, die in artikel 86 vermelde personen toevallig of niet in België, in het kader van hun beroepswerkzaamheid of van hun maatschappelijk, statutair of conventioneel doel, betalen of toekennen aan welke personen ook voor wie die retributies in artikel 23, § 1, 2°, van hetzelfde Wetboek vermelde baten zijn;  c) winst als vermeld in artikel 228, § 2, 3°, b, van hetzelfde Wetboek;  d) (inkomsten vermeld in artikel 228, § 2, 8°, van hetzelfde Wetboek); <KB 1993-08-27/48, art. 4, 1°; Inwerkingtreding : 08-10-1992>  e) winst als vermeld in artikel 228, § 2, 3°, d, van hetzelfde Wetboek;  6° presentiegelden door in artikel 86 vermelde personen betaald of toegekend aan welke personen ook voor wie die presentiegelden baten zijn als vermeld in artikel 23, § 1, 2°, van hetzelfde Wetboek.  (7° het geheel van de winst en de baten die overeenkomstig de bepalingen van de artikelen 29, § 1, en 364 van het Wetboek van de inkomstenbelastingen 1992 worden geacht te zijn toegekend aan niet-inwonende vennoten of leden van burgerlijke vennootschappen of verenigingen zonder rechtspersoonlijkheid, vermeld in artikel 229, § 3, van hetzelfde Wetboek.) <KB 1993-10-22/33, art. 5; Inwerkingtreding : 01-01-1992>  (8° meerwaarden die door niet-inwoners als vermeld in artikel 227, 1° of 2°, van hetzelfde Wetboek worden verwezenlijkt bij de overdracht onder bezwarende titel van in België gelegen onroerende goederen of van zakelijke rechten met betrekking tot zulke goederen, voor zover die meerwaarden begrepen zijn in de in artikel 228, § 2, 3°, a, en 4°, van hetzelfde Wetboek vermelde winst of baten.) <KB 1997-01-10/42, art. 1, 033; Inwerkingtreding : 01-01-1997>  (9° vergoedingen tot volledig of gedeeltelijk herstel van een tijdelijke derving van winst of van baten, zelfs indien ze op een vorige beroepswerkzaamheid betrekking hebben.) <KB 1997-05-20/39, art. 7, 039; Inwerkingtreding : 01-06-1997>

##### Art. 88

Het bedrag van de aan de bron verschuldigde bedrijfsvoorheffing wordt vastgesteld volgens de schalen en de erbij horende regels vermeld in bijlage III.

##### Art. 90

§ 1. (De schuldenaars van bedrijfsvoorheffing, die in artikel 87, 1° tot 7°, vermelde belastbare inkomsten hebben betaald of toegekend, moeten binnen de in artikel 412, van het Wetboek van de inkomstenbelastingen 1992 gestelde termijn een aangifte in de bedrijfsvoorheffing overleggen bij de bevoegde ontvanger van de directe belastingen en de verschuldigde bedrijfsvoorheffing bij dezelfde ambtenaar betalen volgens de regels van hoofdstuk III, afdeling III.) <KB 1999-05-03/39, art. 3, 053; Inwerkingtreding : 06-04- 1999>  Door de schuldenaars van bedrijfsvoorheffing moet eveneens een aangifte worden overgelegd ingeval :  - zij voor een bepaalde periode geen in (artikel 87, 1° tot 7°,) vermelde belastbare inkomsten hebben betaald of toegekend; <KB 1997-01-10/42, art. 2, 1°, 033; Inwerkingtreding : 01-01-1997>  - zij in (artikel 87, 1° tot 7°,) vermelde belastbare inkomsten hebben betaald of toegekend waarop echter volgens de schalen en de regels waarvan sprake in artikel 88 geen bedrijfsvoorheffing verschuldigd is. <KB 1997-01-10/42, art. 2, 1°, 033; Inwerkingtreding : 01-01-1997>  Het model van de aangifte in de bedrijfsvoorheffing wordt vastgesteld door de Minister van Financiën of zijn gedelegeerde.  (De schuldenaars van bedrijfsvoorheffing die zijn bedoeld in artikel 4 van de Wet van 24 december 1999 houdende fiscale en diverse bepalingen, moeten voor de periode waarin zij bezoldigingen hebben toegekend waarvoor zij de verschuldigde bedrijfsvoorheffing niet in de Schatkist moeten storten, twee afzonderlijke aangiften in de bedrijfsvoorheffing overleggen volgens het hierna volgend onderscheid :  - de eerste aangifte in de bedrijfsvoorheffing bevat de door de werkgever betaalde of toegekende belastbare inkomsten van werknemers die niet in artikel 4 van de genoemde wet zijn bedoeld en de daarop verschuldigde bedrijfsvoorheffing die in de Schatkist moet worden gestort;  - de tweede aangifte in de bedrijfsvoorheffing bevat uitsluitend de voor die periode betaalde of toegekende belastbare inkomsten van de werknemers die wel in het voornoemd artikel 4 zijn bedoeld, zonder vermelding van de niet aan de schatkist te storten bedrijfsvoorheffing. In de rubriek "verschuldigde bedrijfsvoorheffing" moet het cijfer "0" worden ingevuld.) <KB 2000-12-05/30, art. 1, 071; Inwerkingtreding : 01-01-2000>  § 2. (Iedere niet in artikel 270, 5°, van hetzelfde Wetboek vermelde schuldenaar) van bedrijfsvoorheffing moet bij de in § 1 vermelde ontvanger een registratienummer aanvragen dat hij bij iedere aangifte in de bedrijfsvoorheffing, alsook bij iedere betaling van bedrijfsvoorheffing dient te vermelden. <KB 1997-01-10/42, art. 2, 2°, 033; Inwerkingtreding : 01-01-1997>  Wanneer een geregistreerde schuldenaar van bedrijfsvoorheffing niet langer als schuldenaar van bedrijfsvoorheffing kan worden aangemerkt, dient hij onmiddellijk de ambtenaar bij wie hij in die hoedanigheid is geregistreerd daarvan in kennis te stellen en moet hij terzelfdertijd de schrapping van het registratienummer vragen.  Het registratienummer omvat eventueel het nummer dat de schuldenaar van de bedrijfsvoorheffing heeft gekregen voor de toepassing van de belasting over de toegevoegde waarde.  § 3. (De Minister van Financiën of zijn gedelegeerde kan toelaten, binnen de door hem bepaalde voorwaarden, de aangifte van de bedrijfsvoorheffing in te dienen bij de door hem aangewezen dienst door middel van een procedure waarbij informatica- of telegeleidingstechnieken worden gebruikt.) <KB 2002-10-21/33, art. 1, 089; Inwerkingtreding : 31-10-2002>  (§ 4. Voor de toepassing van § 1 moeten de in artikel 270, 4°, van het Wetboek van de inkomstenbelastingen 1992 vermelde schuldenaars van de bedrijfsvoorheffing binnen vijftien dagen na het verstrijken van de maand waarin de in artikel 87, 7° vermelde inkomsten overeenkomstig artikel 364 van hetzelfde Wetboek geacht worden te zijn toegekend, een aangifte in de bedrijfsvoorheffing overleggen bij de ontvanger van de directe belastingen te Brussel "Buitenland" en de verschuldigde bedrijfsvoorheffing door storting of overschrijving (op postrekening 679-2002400-29) van de voormelde ontvanger betalen volgens de regels van hoofdstuk III, afdeling III.) <KB 1993-10-22/33, art. 6; Inwerkingtreding : 01-01-1992> <KB 1999-11-09/33, art. 2, 059; Inwerkingtreding : 17-12-1999>

##### Art. 91

Ingeval vergoedingen in globo aan een in artikel 87, 5°, vermelde niet-inwoner die leider is van een orkest, gezelschap of ploeg en die alleen persoonlijk jegens de schuldenaar van de inkomsten gebonden is, worden betaald of toegekend ter beloning van de prestaties van het orkest, het gezelschap of de ploeg, rust de verplichting tot aangifte en storting van de bedrijfsvoorheffing op de schuldenaar van de totale vergoeding, zowel voor het deel dat de leider van het orkest, het gezelschap of de ploeg voor zich houdt, als voor het deel dat hij aan de leden daarvan afstaat.

##### Art. 93

<KB 1993-10-22/33, art. 8; Inwerkingtreding : 01-01-1992> § 1. (Tot staving van de overeenkomstig de artikelen 90 en 91 overgelegde aangiften moeten de in artikel 270, 1° tot 4° en 6°, van het Wetboek van de inkomstenbelastingen 1992 vermelde schuldenaars van bedrijfsvoorheffing al de fiches en de samenvattende opgave of de magnetische informatiedrager waarvan sprake is in artikel 92, voor 1 maart van het jaar na dat waarop die fiches en die opgave of die magnetische informatiedrager betrekking hebben, inleveren bij de bevoegde dienst.) <KB 1999-05-03/39, art. 4, 053; Inwerkingtreding : 06-04-1999>  (De in het eerste lid vermelde schuldenaars) van bedrijfsvoorheffing moeten voor 1 maart een afschrift van het fiche, behoorlijk ingevuld, aan iedere verkrijger van inkomsten overhandigen om hem in staat te stellen eventueel zijn aangifte in de personenbelasting of in de belasting van niet-inwoners in te vullen. <KB 1997-01-10/42, art. 4, 2°, 033; Inwerkingtreding : 01-01-1997>  § 2. In afwijking van § 1 moeten de in artikel 270, 4°, van het Wetboek van de inkomstenbelastingen 1992 vermelde schuldenaars van de bedrijfsvoorheffing, tot staving van de overeenkomstig artikel 90, § 4, overgelegde aangifte, de in artikel 92, § 2, vermelde bijzondere opgave uiterlijk vier maand na het verstrijken van de periode waarop die opgave betrekking heeft, inleveren bij de overeenkomstig artikel 297 van hetzelfde Wetboek aangewezen controle "Buitenland".

##### Art. 94

Op aanvraag verstrekt de administratie der directe belastingen aan de schuldenaars van bedrijfsvoorheffing kosteloos exemplaren van de in bijlage III neergelegde schalen en toepassingsregels en van de aangiften, de fiches en samenvattende opgaven, die vermeld zijn in de artikelen 90 tot 92.  Voor zover zij alle vermeldingen bevatten, mogen fiches en samenvattende opgaven worden gebruikt waarvan het formaat niet afwijkt van het formaat van de door de Minister van Financiën of zijn gedelegeerde vastgestelde modellen.

##### Art. 95

Voor de berekening van de bedrijfsvoorheffing wordt het bedrag van de belastbare inkomsten (in euro vastgesteld en afgerond op de cent). <KB 2000-07-20/63, art. 5, 076; Inwerkingtreding : 01-01-2002>

### Afdeling III. - Roerende voorheffing op inkomsten van roerende goederen en kapitalen en op sommige diverse inkomsten.

#### Onderafdeling I. - Inkomsten van vreemde waarden, van schuldvorderingen op of van gelddeposito's in het buitenland. - Controlemaatregelen. (Wetboek van de inkomstenbelastingen 1992, artikel 263, eerste lid)

##### Art. 96

§ 1. Voor de regelmatige inning van de roerende voorheffing zijn vennootschappen, instellingen, bankiers, notarissen, rentmeesters, zaakvoerders en andere personen die in België inkomsten van buitenlandse oorsprong uitbetalen of op enigerlei wijze bij de incassering van zulke inkomsten optreden, verplicht gezegde verrichtingen, naarmate zij zich voordoen, te boeken in een bijzonder register dat door de controleur van de directe belastingen van het ambtsgebied is genummerd en geparafeerd en dat alle door de Minister van Financiën voorgeschreven vermeldingen inhoudt.  § 2. Het ter voldoening van § 1 gehouden register moet onmiddellijk op elk verzoek van de in artikel 101 aangewezen ambtenaren voorgelegd worden.

##### Art. 97

De Minister van Financiën kan het gebruik van fiscale zegels ten bewijze van de inning van de roerende voorheffing voorschrijven.

##### Art. 98

Elke zending binnen het land of naar het buitenland van coupons of middelen tot inning waarop verrichtingen als vermeld in artikel 96 betrekking hebben, moet vergezeld gaan van een uittreksel uit het bij § 1 van dat artikel voorgeschreven register, waarin de door de Minister van Financiën voorgeschreven vermeldingen voorkomen.

##### Art. 99

Tenzij de in artikel 98 gestelde formaliteiten vervuld zijn, is het verboden coupons of andere middelen tot inning van inkomsten van buitenlandse oorsprong, al dan niet afgeknipt van de effecten waartoe zij behoren, naar het buitenland te zenden.

#### Onderafdeling II. - (Vrijstelling van de roerende voorheffing). (Wetboek van de inkomstenbelastingen 1992, artikel 264) <KB 2003-04-04/40, art. 1, Inwerkingtreding : 01-01-2001>

##### Art. 101bis

<KB 2003-04-04/40, art. 1, Inwerkingtreding : 01-01-2001> Voor de toepassing van artikel 264, eerste lid, 2°bis van het Wetboek van de inkomstenbelastingen 1992, moeten worden gelijkgesteld met de gereglementeerde markten bedoeld in artikel 2, 5° en 6°, van de wet van 2 augustus 2002 betreffende het toezicht op de financiële sector en de financiële diensten, de gereglementeerde secundaire markten voor financiële instrumenten, al dan niet voor het publiek toegankelijk, die zijn geplaatst onder het toezicht van een toezichthouder welke een gewoon lid is van de "Internationale Organisatie van Effectentoezichthouders" (IOSCO), indien de maatschappelijke zetel van de marktonderneming welke de gereglementeerde secundaire markt organiseert, is gevestigd in een Staat, niet bedoeld in artikel 2, 6°, van voormelde wet van 2 augustus 2002 :  - die een overeenkomst ter voorkoming van dubbele belasting heeft gesloten met België;  - of waarvan de toezichthouder van de gereglementeerde markten met de Commissie voor het Bank- en Financiewezen een samenwerkingsovereenkomst over het toezicht op de financiële markten heeft gesloten.

##### Art. 101ter

<KB 2003-04-04/40, art. 1, Inwerkingtreding : 01-01-2001> De Federale overheidsdienst Financiën stelt elk jaar, voor de toepassing van artikel 101bis, een lijst op van de landen waarmee België een overeenkomst ter voorkoming van dubbele belasting heeft gesloten alsmede, op voorstel van de Commissie voor het Bank- en Financiewezen, een lijst van de toezichthouders welke gewoon lid zijn van de IOSCO en een lijst van de toezichthouders met dewelke de Commissie voor het Bank- en Financiewezen een samenwerkingsovereenkomst over het toezicht op de financiële markten heeft gesloten.  Deze lijsten en alle tijdens het jaar daarin aangebrachte wijzigingen worden in het Belgisch Staatsblad bekendgemaakt.

##### Art. 102

Voor de toepassing van artikel 264, eerste lid, 3°, van het Wetboek van de inkomstenbelastingen 1992, wordt het geheel van de reserves bepaald volgens artikel 74 en van de winst die is gereserveerd onder het stelsel van wetgevingen voor de wet van 20 november 1962 houdende hervorming van de inkomstenbelastingen, in de volgende categorieën onderverdeeld :  1° reserves overeenstemmend met winst die voorheen ten name van de vennoten is belast;  2° reserves overeenstemmend met bedragen die ingevolge artikel 202 van het Wetboek van de inkomstenbelastingen 1992 of artikel 52, § 1, eerste lid, van de op 15 januari 1948 samengeordende wetten betreffende de inkomstenbelastingen, zijn afgetrokken van gereserveerde winst die voor de aanslagjaren 1973 en vorige belastbaar was;  3° reserves overeenstemmend met alle andere maatschappelijke winst.

##### Art. 103

Wanneer op het einde van het belastbare tijdperk een vermindering van het totaal van de reserves wordt vastgesteld wordt de ermede overeenstemmende opneming achtereenvolgens aangerekend, eerst op de in artikel 102, 2°, vermelde reserves, daarna, indien die reserves ontoereikend zijn, op de in 3° van dat artikel vermelde reserves en tenslotte op de in 1° vermelde reserves.

##### Art. 104

De opnemingen vermeld in artikel 103 worden geacht in de in dat artikel aangegeven volgorde te hebben gediend :  1° tot betaling van dividenden;  2° tot alle andere doeleinden.

#### Onderafdeling III. - Volledige of gedeeltelijke verzaking van de inning van roerende voorheffing. (Wetboek van de inkomstenbelastingen 1992, artikel 266)

##### Art. 108

Van de inning van de roerende voorheffing wordt volledig afgezien met betrekking tot inkomsten van obligaties, kasbons of andere soortgelijke effecten waarvan de schuldenaar een niet-inwoner is, wanneer de verkrijger wordt geïdentificeerd als een binnenlandse vennootschap of een belastingplichtige die volgens artikel 233 van het Wetboek van de inkomstenbelastingen 1992 aan de belasting van niet-inwoners is onderworpen en de rentegevende kapitalen voor het uitoefenen van zijn beroepswerkzaamheid in België gebruikt.

##### Art. 109

<KB 1995-05-30/31, art. 1, 018; Inwerkingtreding : 02-06-1995> Er wordt volledig afgezien van de inning van de roerende voorheffing op inkomsten uit certificaten van Belgische beleggingsfondsen, met uitsluiting van de inkomsten verleend of toegekend door Belgische fondsen voor belegging in schuldvorderingen als bedoeld in artikel 119quater van de wet van 4 december 1990 op de financiële transacties en de financiële markten.  (Er wordt volledig afgezien van de inning van de roerende voorheffing op inkomsten van roerende waarden van buitenlandse oorsprong gedeponeerd in België en op inkomsten bekomen als gevolg van transacties met die waarden, toegekend of betaalbaar gesteld aan collectieve beleggingsinstellingen naar buitenlands recht die een onverdeeld vermogen zijn dat wordt beheerd door een beheersvennootschap voor rekening van deelnemers, wanneer hun rechten van deelneming in België niet openbaar worden uitgegeven en niet in België worden verhandeld.) <KB 1996-12-17/36, art. 1, 031; Inwerkingtreding : 31-12-1996>

##### Art. 111

Met betrekking tot inkomsten van verhuring, verpachting, gebruik en concessie van roerende goederen, en inkomsten verkregen, buiten het uitoefenen van een beroepswerkzaamheid, uit de onderverhuring of de overdracht van huur van al dan niet gemeubileerde onroerende goederen of uit de concessie van het recht om een plaats die van nature onroerend is en niet is gelegen binnen de omheining van een sportinrichting te gebruiken om er plakbrieven of andere reclamedragers te plaatsen, zomede met betrekking tot opbrengsten uit de verhuring van jacht-, vis- en vogelvangstrecht, wordt van de inning van de roerende voorheffing volledig afgezien indien de verkrijgers :  a) aan de personenbelasting onderworpen rijksinwoners zijn;  b) binnenlandse vennootschappen zijn;  c) internationale of supranationale instellingen zijn als vermeld in artikel 105, 2°, c.

##### Art. 112

Van de inning van de roerende voorheffing wordt volledig afgezien met betrekking tot inkomsten die begrepen zijn in de in artikel 17, § 1, 4°, van het Wetboek van de inkomstenbelastingen 1992 vermelde lijfrenten of tijdelijke renten waarvan de verkrijgers aan de personenbelasting onderworpen rijksinwoners zijn.

##### Art. 114

§ 1. Met betrekking tot inkomsten van deposito's met vaste termijn of met opzeggingstermijn die voor 1 december 1962 aan depositarissen zijn toevertrouwd, wordt van de inning van de roerende voorheffing volledig of gedeeltelijk afgezien volgens het in §§ 2 tot 6 gemaakte onderscheid.  § 2. Van de inning van de roerende voorheffing wordt volledig afgezien met betrekking tot inkomsten van deposito's, die worden verleend of toegekend :  a) aan parastatale instellingen voor sociale zekerheid of aan ermede gelijkgestelde instellingen;  b) door in België gevestigde banken aan in het buitenland gevestigde banken;  c) door in België gevestigde banken, Belgische openbare kredietinstellingen, spaarkassen die van een andere openbare instelling dan de Commissie voor het Bank- en Financiewezen afhangen, privé-spaarkassen die aan de controle van gezegde commissie zijn onderworpen of in artikel 1, tweede lid, 2°, van het koninklijk besluit nr. 185 van 9 juli 1935 vermelde financiële ondernemingen, aan spaarders niet-inwoners.  § 3. Met betrekking tot inkomsten waarvoor krachtens voorgaande § 2 niet van de inning van de roerende voorheffing wordt afgezien, wordt de roerende voorheffing geheven tegen een tarief van 12,5 pct.  § 4. Met betrekking tot inkomsten die worden verleend of toegekend ter uitvoering van overeenkomsten die de last van de mobiliënbelasting op de schuldenaar van de belastbare inkomsten leggen, heeft deze laatste het recht op die inkomsten het overeenkomstig artikel 234 bepaalde gedeelte van de voorheffing in te houden.  § 5. De in §§ 2 tot 4 bepaalde volledige of gedeeltelijke verzaking van de inning van de roerende voorheffing is van toepassing op de inkomsten die zijn behaald tot het vervallen van de in de overeenkomst bepaalde vaste termijn of tot het verstrijken van een tijdperk dat, aanvangend op 5 december 1962, gelijk is aan de in het contract van deposito bedongen opzeggingstermijn; die termijn of dat tijdperk wordt beoordeeld ongeacht de clausules van na 1 december 1962 verstrijkende overeenkomsten die eventueel stilzwijgend uitstel of verlenging ervan bedingen.  § 6. Worden niet als opzeggingstermijn in de zin van dit artikel aangemerkt, de wettelijke of overeengekomen termijnen die slechts een waarborg uitmaken die de depositaris wenst aan te voeren.

##### Art. 115

§ 1. Van de inning van de roerende voorheffing wordt volledig afgezien met betrekking tot de in de artikelen 17, § 1, en 90, 6°, van het Wetboek van de inkomstenbelastingen 1992 vermelde inkomsten die worden verleend of toegekend aan (ter uitvoering van artikel 145.16, 1°, van hetzelfde Wetboek erkende pensioenspaarfondsen). <KB 1995-09-01/42, art. 14, 1°, 019; Inwerkingtreding : 01-01-1993>  § 2. Van de inning van de roerende voorheffing wordt volledig afgezien met betrekking tot de in de artikelen 17, § 1, en 90, 6°, van het Wetboek van de inkomstenbelastingen 1992 vermelde inkomsten die worden verleend of toegekend aan houders van een in (artikel 145.16, 2°), van hetzelfde Wetboek bedoelde individuele spaarrekening, met betrekking tot de in die rekening begrepen activa. <KB 1995-09-01/42, art. 14, 2°, 019; Inwerkingtreding : 01-01-1993>

##### Art. 116

<KB 2000-12-04/31, art. 3, 072; Inwerkingtreding : 28-11-2000> Van de inning van de roerende voorheffing wordt volledig afgezien met betrekking tot de in de artikelen 17 en 90, 6°, van het Wetboek van de inkomstenbelastingen 1992 vermelde inkomsten, andere dan dividenden van Belgische oorsprong die niet zijn bedoeld in artikel 18, eerste lid, 3°, van hetzelfde Wetboek, die worden verleend of toegekend aan beleggingsvennootschappen als bedoeld in de artikelen 114, 118 en 119quinquies van de wet van 4 december 1990 op de financiële transacties en de financiële markten.  De verzaking voorzien in het eerste lid is eveneens uitgesloten met betrekking tot de vergoedingen als bedoeld in artikel 18, eerste lid, 3°, van hetzelfde Wetboek, verleend of toegekend naar aanleiding van een lening van aandelen van een Belgische vennootschap, buiten de in artikel 106, § 11 bedoelde gevallen.

#### Onderafdeling IV. - (In België in open bewaring gegeven aandelen aan toonder uitgegeven vanaf 1 januari 1994 - Voorwaarden en toepassingswijze voor het verkrijgen van een verlaagd tarief inzake roerende voorheffing (Wetboek van de inkomstenbelastingen 1992, artikel 269, derde lid, b)). <Ingevoegd bij KB 1995-09-01/41, art. 1; Inwerkingtreding : 28-09-1995>

##### Art. 119bis


### Afdeling IV. - Verrekening van voorheffingen.

#### Onderafdeling I. - Fictieve onroerende voorheffing. (Wetboek van de inkomstenbelastingen 1992, artikel 278)

##### Art. 120

Een fictieve onroerende voorheffing wordt toegekend met betrekking tot de inkomsten uit onroerende goederen die ingevolge artikel 253, 3°, van het Wetboek van de inkomstenbelastingen 1992 of ingevolge bijzondere wetsbepalingen van onroerende voorheffing zijn vrijgesteld.  Die fictieve onroerende voorheffing is gelijk aan 12,5 pct. van het kadastrale inkomen van de voormelde onroerende goederen; zij mag echter niet meer bedragen dan 5 pct. van het kadastrale inkomen wanneer het belastingplichtigen betreft als vermeld in artikel 216, 2°, van hetzelfde Wetboek.

#### Onderafdeling II. - Fictieve roerende voorheffing. (Wetboek van de inkomstenbelastingen 1992, artikel 284)

##### Art. 122

Artikel 121 is van toepassing op de in § 1 van dat artikel vermelde inkomsten die in de belastbare grondslag van de inkomstenbelastingen zijn opgenomen.

#### Onderafdeling III. - Mate van verrekening. (Wetboek van de inkomstenbelastingen 1992, artikel 295)

##### Art. 123

De onroerende voorheffing, de fictieve onroerende voorheffing, de roerende voorheffing, de fictieve roerende voorheffing en het forfaitaire gedeelte van buitenlandse belasting worden, in de mate bepaald in de artikelen 276 tot 294 van het Wetboek van de inkomstenbelastingen 1992, met de personenbelasting, de vennootschapsbelasting of de belasting van niet-inwoners verrekend voor zover zij betrekking hebben op inkomsten die in de belastbare grondslag van die belastingen zijn opgenomen.

##### Art. 124

Voor de toepassing van artikel 125 verstaat men :  1° onder "samengeteld gedeelte van het belastbare inkomen" : het gedeelte van het inkomen dat belast wordt volgens (de artikelen 130 tot 170, 178, 515bis, vierde lid, 516, 517 en 518) van het Wetboek van de inkomstenbelastingen 1992; <KB 1995-09-01/42, art. 18, 1°, 019; Inwerkingtreding : 01-01-1993>  2° onder "afzonderlijk belast gedeelte van het inkomen" : het gedeelte van het belastbare inkomen waarop de belasting afzonderlijk wordt berekend overeenkomstig (de artikelen 171 tot 174, 515bis, vijfde lid, 515ter en 519, van hetzelfde Wetboek); <KB 1995-09-01/42, art. 18, 3°, 020; Inwerkingtreding : 01-01-1993>  3° onder "samengetelde nettoberoepsinkomsten" : de nettoberoepsinkomsten die onder het in 1° vermelde samengetelde gedeelte van het belastbare inkomen opgenomen zijn;  4° onder "afzonderlijk belaste nettoberoepsinkomsten" : de nettoberoepsinkomsten die in het in 2° vermelde afzonderlijk belaste gedeelte van het inkomen begrepen zijn;  5° onder "totaal van de samengetelde netto-inkomsten" : de gezamenlijke netto-inkomsten van de verschillende categorieën, uitgezonderd het in 2° vermelde afzonderlijk belaste gedeelte.

##### Art. 125

Het in artikel 290, 2°, van het Wetboek van de inkomstenbelastingen 1992 vermelde deel van de personenbelasting dat evenredig betrekking heeft op de beroepsinkomsten, is gelijk aan de som van de personenbelasting die betrekking heeft op de afzonderlijk belaste nettoberoepsinkomsten, en het produkt dat wordt verkregen door het bedrag van de personenbelasting dat betrekking heeft op het samengetelde gedeelte van het belastbare inkomen, te vermenigvuldigen met een breuk waarvan de teller het bedrag is van de samengetelde nettoberoepsinkomsten en de noemer het totaal van de samengetelde netto-inkomsten.

## HOOFDSTUK III. - VESTIGING EN INVORDERING VAN DE BELASTING.

### Afdeling I. - (Aangiften. (Wetboek van de inkomstenbelastingen 1992, artikelen 297, tweede lid en 300, § 1)) <KB 1997-07-06/35, art. 1, 1°; Inwerkingtreding : 01-01-1997>

##### Art. 126

De bepalingen van de artikelen 305 en 307, § 2, van het Wetboek van de inkomstenbelastingen 1992 betreffende de aangifte inzake personenbelasting, vennootschapsbelasting, rechtspersonenbelasting en belasting van niet-inwoners, zijn van toepassing op de aangiften inzake roerende voorheffing en bedrijfsvoorheffing vermeld in de artikelen 85, 90 en 91 van dit besluit.

##### Art. 127

De gemeenten moeten :  1° periodiek en tenminste eenmaal per jaar, voor 15 januari, aan de controleur van de directe belastingen van het ambtsgebied een opgave verstrekken van de in het vorige jaar in de bevolking opgetreden veranderingen : binnengekomen en vertrokken personen, veranderingen binnen de gemeente zelf; die opgave mag worden vervangen door fiches ad hoc of door duplicaten van de bij de bevolkingsdienst gedane aangiften;  2° op aanvraag een uitvoerige lijst verstrekken van de personen die door hun bemiddeling bepaalde formaliteiten hebben vervuld welke ook fiscaal van belang zijn;  3° de plaatselijke politie gelasten eventueel, tegen vergoeding, deel te nemen aan de uitreiking en de inzameling van de aangiften in de directe belastingen;  4° een behoorlijk lokaal, zo nodig verwarmd en verricht, ter beschikking van de ambtenaren van de belastingen stellen op de zitdagen die, voor de vestiging en inning van de directe belastingen, nu en dan noodzakelijk zijn in de gemeenten waar de belastingdienst over geen voldoende ruim kantoor beschikt.  De agglomeraties zijn verplicht tot het verstrekken, op aanvraag, van de lijst vermeld in 2° van het eerste lid.

### Afdeling II. - Kohieren. (Wetboek van de inkomstenbelastingen 1992, artikelen 251 en 300, § 1)

##### Art. 128

De kohieren mogen afzonderlijk per soort van belasting of voorheffing of ineens voor verschillende soorten van belastingen of voorheffingen worden aangelegd.

##### Art. 129

Zo nodig mogen de kohieren voor verscheidene aanslagjaren opgemaakt worden mits zij jaarlijks met een nieuwe uitvoerbaarverklaring worden bekleed.

##### Art. 130

Kohieren met aanslagen van belastingen of voorheffingen worden verbonden aan het begrotingsjaar dat loopt op de datum waarop ze uitvoerbaar worden verklaard; de belastingtarieven en eventueel de opcentiemen in verband met de respectieve aanslagjaren zijn van toepassing.

##### Art. 131

De kohieren van de directe belastingen worden opgemaakt per gemeente, per groep gemeenten of per ontvangkantoor.

##### Art. 132

De kohieren worden op door de administratie of door haar gedelegeerden bepaalde tijdstippen opgemaakt.

##### Art. 133

De aanslagen worden op naam van de betrokken belastingschuldigen ten kohiere gebracht.  Aanslagen ten laste van overleden belastingschuldigen worden ten kohiere gebracht op hun naam voorafgegaan van het woord "Nalatenschap" en eventueel gevolgd van de vermelding van de persoon of personen die zich aan de administratie der directe belastingen hebben bekend gemaakt als erfgenaam, legataris, begiftigde of bijzondere lasthebber.  De identiteit van die personen wordt omstandig vermeld. Wanneer een van de erfgenamen formeel is aangewezen om de nalatenschap te vertegenwoordigen, geschiedt het ten kohiere brengen als volgt : "Nalatenschap X ..., de erfgenamen vertegenwoordigd door ...".  In geval van aanslag van ambtswege, moet de naam van de overleden belastingschuldige (Nalatenschap X ...) slechts gevolgd worden door de vermelding van een van de erfgenamen die aan de controleur van de belastingen bekend is.

##### Art. 134

Voor de berekening van de aanslagen in de personenbelasting, de vennootschapsbelasting, de rechtspersonenbelasting en de belasting van niet-inwoners wordt de belastbare grondslag (in euro vastgesteld en afgerond op de cent). <KB 2000-07-20/63, art. 5, 076; Inwerkingtreding : 01-01-2002>

##### Art. 135

De verschillende aanslagen, met inbegrip van de opcentiemen, worden in elk stadium van de berekening (in euro vastgesteld en afgerond op de cent). <KB 2000-07-20/63, art. 5, 076; Inwerkingtreding : 01- 01-2002>

##### Art. 136

Zodra de kohieren uitvoerbaar verklaard zijn, wordt aan de betrokken belastingschuldigen een aanslagbiljet gezonden.

### Afdeling III. - Betalingen en kwitanties. (Wetboek van de inkomstenbelastingen 1992, artikelen 250 en 300, § 1)

##### Art. 139

§ 1. Inkomstenbelastingen en voorheffingen moeten worden betaald :  - ofwel door storting of overschrijving op de (postrekening) van de ontvanger; <KB 1999-11-09/33, art. 3, 059; Inwerkingtreding : 17-12-1999>  - ofwel met een postwissel ten gunste van de ontvanger;  - ofwel met een gecertifieerde of gewaarborgde vooraf gekruiste cheque, ten gunste van de ontvanger getrokken op een financiële instelling die aangesloten of vertegenwoordigd is bij een verrekenkamer van het land.  De Minister van Financiën of zijn gedelegeerde kan, in bijzondere omstandigheden, andere wijzen van betaling toestaan.  § 2. De belastingschuldige moet op het betaalformulier de aard van de gekweten belasting of voorheffing vermelden en, voor ingekohierde belastingen of voorheffingen, ook de gemeente en het kohierartikel.  § 3. Behoudens tegenbewijs gelden als bewijs van betaling :  - voor stortingen of postwissels, de (door de Post) gedagtekende ontvangstbewijzen; <KB 1994-08-12/48, art. 9, 006; Inwerkingtreding : 01-10-1992>  - voor overschrijvingen en cheques, de rekeninguittreksels en erbij horende stukken.

##### Art. 140

<KB 1995-01-03/30, art. 4, 011; Inwerkingtreding : 01-01-1995> § 1. In afwijking van artikel 139 kan bedrijfsvoorheffing uitsluitend worden betaald door storting of overschrijving op de (postrekening) van de ontvanger. Daarbij mogen alleen betaalformulieren worden gebruikt : <KB 1999-11-09/33, art. 3, 059; Inwerkingtreding : 17-12-1999>  - waarvan het model door de Minister van Financiën of zijn gedelegeerde is vastgesteld in overleg met de Minister, of zijn gedelegeerde, tot wiens bevoegdheid de Post behoort;  - die op aanvraag of ambtshalve door het betrokken ontvangkantoor worden afgegeven en de naam van de belastingschuldige en zijn in artikel 90, § 2, bedoelde registratienummer vermelden.  § 2. Betalingen verricht op de (postrekening) van de ontvanger met vermelding van een als in § 1 vermeld registratienummer, worden geacht gedaan te zijn voor rekening van de belastingschuldige die bij het kantoor van die ontvanger door dat nummer wordt geïdentificeerd. <KB 1999-11-09/33, art. 3, 059; Inwerkingtreding : 17- 12-1999>

##### Art. 141

Inkomstenbelastingen en voorheffingen waarvoor een gerechtsdeurwaarder in opdracht van de ontvanger vervolgingen instelt, kunnen in afwijking van de artikelen 137 en 139 betaald worden in handen van die gerechtsdeurwaarder.

##### Art. 142

§ 1. Betalingen van inkomstenbelastingen en voorheffingen hebben uitwerking :  - voor stortingen via een postkantoor en voor overschrijvingen, op de datum die door (de Post) als bevrijdende datum op het rekeninguittreksel wordt vermeld; <KB 1994-08-12/48, art. 11, 006; Inwerkingtreding : 01-10- 1992>  - voor betalingen met een postwissel of met een gecertificeerde of gewaarborgde cheque, op de datum waarop de postwissel of de cheque door de ontvanger is ontvangen;  - voor in artikel 141 vermelde betalingen, op de datum van de afgifte van de fondsen in handen van de gerechtsdeurwaarder.  § 2. De Minister van Financiën of zijn gedelegeerde bepaalt de datum waarop de betaling uitwerking heeft wanneer hij krachtens artikel 139, § 1, tweede lid, een andere betaalwijze toestaat.

##### Art. 143

§ 1. De belastingschuldige die verschillende belastingen of voorheffingen te betalen heeft, mag bij elke betaling vermelden wat hij wil vereffenen.  Bij gebreke van dergelijke vermelding worden de betalingen aangerekend naar de keuze van de ontvanger, onverminderd de toepassing van § 2. Zulks geldt eveneens wanneer de aan te rekenen som voortkomt van een teruggave van belastingen, voorheffingen en toebehoren, of van een toekenning van moratoriuminteresten.  § 2. Betalingen, teruggaven en moratoriuminteresten als vermeld in § 1 worden eerst aangerekend :  1° op de kosten van alle aard, met inbegrip van het inningsrecht, ongeacht de aanslagen waarop zij betrekking hebben;  2° op de nalatigheidsinteresten betreffende de voorheffingen of aanslagen die de belastingschuldige wil vereffenen of die de ontvanger wil aanzuiveren.

##### Art. 144

De ontvangkantoren van de directe belastingen zijn open de eerste 5 werkdagen van de week, van 9 u. tot 12 u., behalve op de officiële verlofdagen in de Rijksbesturen.

### Afdeling IV. - Verjaring. (Wetboek van de inkomstenbelastingen 1992, artikel 300, § 1)

### Afdeling V. - Vervolgingen. (Wetboek van de inkomstenbelastingen 1992, artikel 300, § 1)

#### Onderafdeling I. - Inleidende bepaling - Indeling van de vervolgingen.

##### Art. 146

De invordering van de directe belastingen, zomede van de voorheffingen die niet binnen de wettelijke termijnen voldaan zijn, mag overeenkomstig het bepaalde in de artikelen 147 tot 175 vervolgd worden.

##### Art. 147

De vervolgingen zijn rechtstreeks of onrechtstreeks : de eerste zijn gericht tegen de belastingschuldigen die bij name in het kohier vermeld zijn of hun vertegenwoordiger; de tweede worden krachtens het bij de wet toegestane verhaal tegen derden ingesteld. Beide worden ingesteld ingevolge persoonlijke of gemeenschappelijke dwangschriften, uitgevaardigd door de ontvangers die in het bezit zijn van de kohieren of met de inning voor rekening van ambtgenoten belast zijn.

#### Onderafdeling II. - Rechtstreekse vervolgingen.

##### Art. 148

De rechtstreekse vervolgingen omvatten :  1° het dwangbevel;  2° het uitvoerend beslag op roerend goed;  3° het beslag op taken wortelvaste vruchten;  4° het uitvoerend beslag op zeeschepen en binnenschepen;  5° het uitvoerend beslag op onroerend goed.  Die vervolgingen zijn gerechtelijk en de geldigverklaring behoort tot de bevoegdheid van de gewone rechtbanken.

A. Dwangbevel.

##### Art. 149

Ingeval een belastingschuldige zijn belastingen niet heeft gekweten binnen de termijnen van artikel 413 van het Wetboek van de inkomstenbelastingen 1992, doet de ontvanger hem een dwangbevel betekenen tot betaling binnen 24 uren, op straffe van tenuitvoerlegging door beslag.  Het dwangbevel moet bovenaan een uittreksel bevatten uit het kohierartikel betreffende de belastingschuldige en een afschrift van de uitvoerbaarverklaring.

##### Art. 150

Ingevolge de betekening van een dwangbevel gedane gedeeltelijke betalingen verhinderen niet de voortzetting van de vervolgingen.

B. Uitvoerend beslag op roerend goed.

##### Art. 151

Wanneer de termijn van het dwangbevel verstreken is, doet de ontvanger overgaan tot uitvoerend beslag op roerend goed, hetwelk geschiedt op de wijze bepaald in het Gerechtelijk Wetboek, behoudens de afwijkingen vastgesteld in de hierna volgende artikelen 152 tot 154.

##### Art. 152

Voor de inbeslagneming verzoekt de instrumenterende deurwaarder de belastingschuldige hem de kwitantie te vertonen van de op zijn aanslagen gestorte afkortingen en vermeldt dit verzoek in het proces-verbaal van beslag.

##### Art. 153

Uitvoerend beslag op roerend goed wordt gelegd niettegenstaande verzet tegen het dwangbevel, tenzij de instrumenterende deurwaarder het nuttig mocht achten daaromtrent de mening van de ontvanger in te winnen die, naar gelang van het geval, de schorsing of de voortzetting van verdere vervolgingen gelast.  Alleen verzet aangaande de vorm van de akten schorst de tenuitvoerlegging, met dien verstande dat de verkoop van de in beslag genomen voorwerpen slechts kan geschieden na een gerechtelijke beslissing, welke zodra mogelijk moet worden gewezen.

##### Art. 154

Tegenover belastingschuldigen die door wegneming van roerende voorwerpen of anderszins pogen de waarborgen van de Schatkist te doen verdwijnen of gewoon te verminderen, kan de ontvanger rechtstreeks uitvoerend beslag op roerend goed doen leggen zonder voorafgaande betekening van een dwangbevel.  In dat geval behelst het exploot van inbeslagneming het dwangbevel voor beslag en bevat het de diverse vermeldingen bedoeld in artikel 149, tweede lid, zomede de gronden voor het niet vooraf betekenen van een dwangbevel.

C. Beslag op tak- en wortelvaste vruchten.

##### Art. 157

Beslag op tak- en wortelvaste vruchten geschiedt op de wijze bepaald in het Gerechtelijk Wetboek.

D. Uitvoerend beslag op zeeschepen en binnenschepen.

##### Art. 158

Uitvoerend beslag op zeeschepen en binnenschepen geschiedt op de wijze bepaald in het Gerechtelijk Wetboek.

E. Uitvoerend beslag op onroerend goed.

##### Art. 159

Uitvoerend beslag op onroerend goed geschiedt op de wijze bepaald in het Gerechtelijk Wetboek.

##### Art. 160

Tot uitvoerend beslag op onroerend goed kan slechts worden overgegaan nadat de ontvanger, die in het bezit is van de kohieren of met de invordering van belastingen voor rekening van ambtgenoten belast is, door tussenkomst van de directeur van de directe belastingen daarvoor machtiging van de Minister van Financiën heeft verkregen.  De ontvanger voegt bij het verzoek om machtiging :  1° een getuigschrift, uitgereikt door de hypotheekbewaarder, van de inschrijvingen die de te onteigenen goederen bezwaren;  2° een staat vermeldende :  a) de naam van de achterstallige belastingschuldige;  b) de aard en het bedrag van de in te vorderen belastingen;  c) de begrote verkoopwaarde van gezegde goederen;  d) het kadastrale inkomen daarvan;  e) de benaderende waarde van de roerende voorwerpen die tot voorrecht van de openbare Schatkist dienen en waarop beslag gelegd is of kan gelegd worden.  In spoedeisende gevallen mag de ontvanger evenwel het dwangbevel voor uitvoerend beslag op onroerend goed doen betekenen en overschrijven zonder in het bezit te zijn van de machtiging vermeld in het eerste lid. In dat geval behelst het dwangbevel een bondige vermelding van de dringende redenen en wordt de vereiste machtiging ten spoedigste door de ontvanger gevraagd.

F. Aan de vier soorten van beslag gemene bepalingen.

##### Art. 161

Het is de ontvangers en instrumenterende deurwaarders verboden, rechtstreeks of onrechtstreeks enig voorwerp, waarvan zij de verkoop bewerkstelligen, te kopen of voor zich te doen kopen op straffe van nietigheid van de verkoop en van ontzetting voor de deurwaarders van de directe belastingen of toepassing van de bij artikel 533 van het Gerechtelijk Wetboek bepaalde tuchtstraffen voor de gerechtsdeurwaarders.

G. Aan het uitvoerend beslag op roerend goed en het beslag op tak- en wortelvaste vruchten gemene bepalingen.

##### Art. 162

§ 1. Wanneer geen andere schuldeisers beslag of verzet hebben gedaan, wordt de bruto-opbrengst van de verkoop gestort in handen van de ontvanger.  De gerechtsdeurwaarder trekt evenwel eerst de vervolgingskosten af die hem toekomen.  § 2. Wanneer andere schuldeisers beslag of verzet hebben gedaan, voert de gerechtsdeurwaarder of de deurwaarder van de directe belastingen de evenredige verdeling uit op de wijze bepaald in het Gerechtelijk Wetboek.

##### Art. 163

De ontvanger rekent de hem gestorte sommen aan volgens de in artikel 143 gestelde regelen; hij geeft aan de belastingschuldige bij ter post aangetekende brief kennis van de aldus gedane aanrekeningen en betaalt hem het eventuele overschot terug.

#### Onderafdeling III. - Onrechtstreekse vervolgingen.

A. Vervolgingen tegen derden-houders.

##### Art. 165

§ 1. Wanneer uit de verklaring van de derden-houders blijkt, hetzij dat de uitvoering van het in artikel 164, § 1, vermelde verzoek belemmerd wordt door verzet van de belastingschuldige, hetzij dat de derden- houders hun verplichtingen ten opzichte van de belastingschuldige betwisten, hetzij dat de inkomsten, sommen en zaken het voorwerp zijn van enig verzet of beslag onder derden, voor het verzoek gedaan door andere schuldeisers, hetzij dat de zaken te gelde moeten worden gemaakt, doet de ontvanger tot uitvoerend beslag onder derden overgaan, onverminderd de bewarende uitwerking van het gezegde verzoek.  § 2. Dit uitvoerend beslag onder derden moet worden gelegd binnen de maand van de afgifte ter post van de in artikel 164, § 4, vermelde verklaring of kennisgeving; zo zulks niet geschiedt wordt het in artikel 164, § 1, vermelde verzoek als niet bestaande beschouwd.  § 3. Uitvoerend beslag onder derden geschiedt op de wijze bepaald in het Gerechtelijk Wetboek, behoudens eventuele naleving van de formaliteiten voorgeschreven voor het beslag in handen van ontvangers en beheerders van openbare gelden; voor het overige wordt gehandeld overeenkomstig de artikelen 162 en 163.

B. Aanwending van sommen die aan een belastingschuldige moeten worden teruggegeven of betaald.

##### Art. 166

§ 1. Het bepaalde van Boek III, Titel III, Hoofdstuk V, afdeling IV, van het Burgerlijk Wetboek, is inzake directe belastingen niet van toepassing.  § 2. Elke som die aan een belastingschuldige moet worden teruggegeven of betaald in het kader van de toepassing van de wettelijke bepalingen inzake de inkomstenbelastingen en de ermee gelijkgestelde belastingen of krachtens de bepalingen van het burgerlijk recht met betrekking tot de onverschuldigde betaling, kan door de ontvanger van de directe belastingen zonder formaliteit, overeenkomstig artikel 143, worden aangezuiverd op de door die belastingschuldige verschuldigde voorheffingen, belastingen en ermee gelijkgestelde belastingen in hoofdsom, opcentiemen, verhogingen, interesten en kosten.  § 3. (In geval van bezwaar, van een in artikel 376 van het Wetboek van de inkomstenbelastingen 1992 bedoelde aanvraag om ontheffing of van een vordering in rechte) en in zover het geen zekere en vaststaande schuld in de zin van artikel 410 van het Wetboek van de inkomstenbelastingen 1992 betreft, wordt de aanzuivering ingevolge § 2 verricht als bewarende maatregel in de zin van artikel 409 van hetzelfde Wetboek. <KB 1999-05-03/39, art. 7, 053; Inwerkingtreding : 06-04-1999>

#### Onderafdeling IV. - Met de vervolgingen belaste personen.

##### Art. 167

De vervolgingen inzake directe belastingen worden ingesteld door gerechtsdeurwaarders of door deurwaarders van de directe belastingen in dienst op 1 mei 1967.  Beiden doen in die hoedanigheid de dwangbevelen, de beslagleggingen en de verkopingen.  Uit hoofde van de uitoefening van vervolgingen inzake directe belastingen mogen gerechtsdeurwaarders geen aanspraak maken op hogere of andere rechten of kosten dan die welke in artikel 172 vastgesteld zijn, op straffe van terugbetaling, schadevergoeding en, desnoods, toepassing van de bij artikel 533 van het Gerechtelijk Wetboek bepaalde tuchtstraffen.

##### Art. 168

Bij het uitoefenen van hun ambt moeten de deurwaarders van de directe belastingen voorzien zijn van hun aanstellingsbrief en deze op elk verzoek vertonen; zij vermelden zulks in alle akten van hun ambt.

##### Art. 171

De deurwaarders van de directe belastingen zijn hun gehele tijd verschuldigd aan het kantoor waaraan zij verbonden zijn; zij mogen derhalve geen collega's bijstaan als getuige.  Niettegenstaande hun bijzondere opdracht blijven zij aan de administratieve tucht onderworpen.

#### Onderafdeling V. - Vervolgingskosten.

##### Art. 172

De vervolgingskosten worden bepaald volgens de regelen die gelden voor de akten van de gerechtsdeurwaarders in burgerlijke en handelszaken.

##### Art. 173

De vervolgingskosten vallen ten laste van de achterstallige belastingschuldigen.  Die kosten komen volledig toe aan de instrumenterende deurwaarders die de hoedanigheid van gerechtsdeurwaarder hebben. Ze komen aan de Schatkist toe, voor vervolgingen die door deurwaarders van de directe belastingen zijn gedaan; de Minister van Financiën is evenwel gemachtigd om een gedeelte daarvan aan die deurwaarders toe te kennen.  In uitzonderlijke gevallen kan de ontvanger gemachtigd worden aan de instrumenterende deurwaarder de vervolgingskosten voor te schieten.

##### Art. 174

Ter vereffening worden niet aanvaard :  1° kosten van akten die niet met de oorspronkelijke stukken gestaafd zijn;  2° kosten die het gevolg zijn van vervolgingen die willekeurig, zonder dwangschrift of in een met onderhavige reglementering strijdige orde gedaan zijn;  3° kosten gedaan tegen kennelijk onvermogende belastingschuldigen.

#### Onderafdeling VI. - Algemene bepalingen.

##### Art. 175

De wettelijke bepalingen betreffende de inhoud en de betekening van exploten zijn van toepassing op de akten van gerechtelijke vervolgingen inzake directe belastingen.

### Afdeling VI. - Opsporing van inbreuken. (Wetboek van de inkomstenbelastingen 1992, artikel 300, § 1)

##### Art. 176

Onverminderd de bevoegdheden van de gerechtelijke officieren bij de parketten, zijn de ambtenaren van de administratie der directe belastingen, van de administratie der douane en accijnzen, van de administratie van het kadaster, de beëdigde gemeenteambtenaren, de rijkswacht, de gerechtelijke agenten bij de parketten, de speciale controleurs van de administratie van het vervoer en de leden van het toezichtspersoneel van het Hoog Comité van toezicht bevoegd om overtredingen op te sporen en om, zelfs alleen, processen-verbaal inzake directe belastingen op te stellen.  Die processen-verbaal, waarbij eventueel de schriftelijke uitleg van de overtreders wordt gevoegd, worden opgesteld ten verzoeke van de Minister van Financiën, op vervolging en benaarstiging van de directeur van de directe belastingen, domicilie kiezend in zijn kantoren; zij zijn van bevestiging of visum en van betekening vrijgesteld.  De processen-verbaal worden toegezonden aan de ambtenaren die daartoe door de Minister van Financiën zijn aangewezen.

### Afdeling VII. - Vestiging en invordering door de administratie van de belasting over de toegevoegde waarde, registratie en domeinen, van de belasting van niet-inwoners op meerwaarden op (...) onroerende goederen. (Wetboek van de inkomstenbelastingen 1992, artikel 301) <KB 1997-05-20/39, art. 10; Inwerkingtreding : 01-06- 1997>

### Afdeling VIII. - (Vrijstelling van de aangifteverplichting in de personenbelasting. (Wetboek van de inkomstenbelastingen 1992, artikel 306)) <KB 1994-05-09/40, art. 1; Inwerkingtreding : 01-01-1994>

##### Art. 178

<KB 1994-05-09/40, art. 2, 004; Inwerkingtreding : 01-01-1994> § 1. De belastingplichtingen zonder beroepswerkzaamheid worden van aangifteplicht in de personenbelasting vrijgesteld ingeval hun belastbare inkomsten minder bedragen dan :  1° de belastingvrije som indien het om een alleenstaande gaat;  2° de samengetelde belastingvrije sommen indien het om echtgenoten gaat.  § 2. Van aangifteplicht in de personenbelasting worden eveneens vrijgesteld de belastingplichtigen die geen andere belastbare inkomsten moeten aangeven dan :  1° inkomsten van onroerende goederen die belastbaar zijn ten belope van het kadastraal inkomen;  2° pensioenen, renten en als zodanig geldende toelagen, met uitzondering van :  a) kapitalen en afkoopwaarden;  b) omzettingsrenten van kapitalen en afkoopwaarden;  c) inkomsten van pensioensparen.  In afwijking van het eerste lid geldt de vrijstelling van aangifteplicht niet voor de volgende belastingplichtigen :  1° niet-hertrouwde weduwen of weduwnaars die één of meer kinderen ten laste hebben;  2° ongehuwde vaders of moeders die één of meer kinderen ten laste hebben;  3° belastingplichtigen met één of meer kinderen van minder dan 3 jaar ten laste;  4° belastingplichtigen voor het jaar van huwelijk indien hun echtgenoot geen bestaansmiddelen van meer dan (1.690,00 EUR) netto heeft; <KB 2000-07-20/63, art. 2, 075; Inwerkingtreding : 01-01-2002>  5° weduwen of weduwnaars voor het jaar van hun overlijden van hun echtgenoot indien die echtgenoot geen bestaansmiddelen van meer dan (1.690,00 EUR) netto heeft gehad. <KB 2000-07-20/63, art. 2, 075; Inwerkingtreding : 01-01-2002>  In afwijking van het eerste lid geldt de vrijstelling van aangifteplicht evenmin voor de belastingplichtigen die :  1° inkomsten van buitenlandse oorsprong hebben;  2° aftrekbare interesten betalen;  3° uitgaven doen die recht geven op een belastingvermindering;  4° aftrekbare bestedingen doen;  5° voorafbetalingen verrichten.  § 3. De vrijstelling van aangifteplicht is van toepassing voor het aanslagjaar waarvan het belastbaar tijdperk volgt op een kalenderjaar waarin aan de in § 1 of § 2 vermelde voorwaarden is voldaan.

##### Art. 179. (Opgeheven) <KB 1994-05-09/40, art. 3, 004; Inwerkingtreding : 01-01-1994>

### Afdeling IX. - Aanwijzing van derden om mededeling te verkrijgen van informatiegegevens voor de uitvoering van een opdracht van algemeen belang. (Wetboek van de inkomstenbelastingen 1992, artikel 314, § 4)

##### Art. 181

§ 1. De naamloze vennootschap Joos gebruikt de in artikel 180, § 1, vermelde gegevens uitsluitend in haar werkplaatsen te Turnhout voor het adresseren van de aangifteformulieren inzake personenbelasting en met inachtneming van de bepalingen van artikel 314, § 4, laatste lid, van het Wetboek van de inkomstenbelastingen 1992.  § 2. Op straffe van toepassing van de bepalingen van artikel 314, § 5, van hetzelfde Wetboek neemt de naamloze vennootschap Joos de nodige maatregelen met het oog op de naleving van de voorschriften van § 1.

### Afdeling IXbis. - (Aanwijzing van ambtenaren van andere fiscale administraties die bevoegd zijn om onderzoekingen uit te voeren (Wetboek van de inkomstenbelastingen 1992, artikel 334bis).) <Ingevoegd bij KB 1995-04-04/34, art. 1; Inwerkingtreding : 01-01-1993>

##### Art. 181bis


### Afdeling X. - Minimumwinst van buitenlandse firma's. (Wetboek van de inkomstenbelastingen 1992, artikel 342, § 2)

##### Art. 182

§ 1. De minimumwinst die belastbaar is ten name van buitenlandse firma's die in België werkzaam zijn en volgens de vergelijkingsprocedure neergelegd in artikel 342, § 1, eerste lid, van het Wetboek van de inkomstenbelastingen 1992 belastbaar zijn, wordt bepaald als volgt :  1° landbouwbedrijven, tuinbouwbedrijven of boomkwekerijen : forfaitaire schaal vastgesteld voor de Belgische belastingplichtigen die in dezelfde landbouwstreek een soortgelijk beroep uitoefenen;  2° ondernemingen behorend tot de :  a) scheikundige nijverheid : (22.000,00 EUR) per personeelslid (gemiddeld aantal over het beschouwde jaar); <KB 2000-07-20/63, art. 2, 075; Inwerkingtreding : 01-01-2002>  b) voedingsnijverheid : (12.000,00 EUR) per personeelslid (gemiddeld aantal over het beschouwde jaar); <KB 2000-07-20/63, art. 2, 075; Inwerkingtreding : 01-01-2002>  c) metaalnijverheid, fijn mechanische nijverheid en bedrijven, ondernemingen die niet-energetische delfstoffen winnen en verwerken, bouwnijverheid en alle andere niet sub a en b, hierboven vermelde nijverheidsbedrijven en - ondernemingen : (7.000,00 EUR) per personeelslid (gemiddeld aantal over het beschouwde jaar); <KB 2000-07- 20/63, art. 2, 075; Inwerkingtreding : 01-01-2002>  3° ondernemingen uit de handelssector en de dienstverlenende sector :  a) groothandel, kleinhandel, vervoer, horeca, ingenieurs- en studiebureaus, informatica en electronica en andere diensten aan ondernemingen : (2,50 EUR) per (25,00 EUR) omzet, met een minimum van (7.000,00 EUR) per personeelslid (gemiddeld aantal over het beschouwde jaar); <KB 2000-07-20/63, art. 2, 075; Inwerkingtreding : 01-01-2002>  b) tussenpersonen in handel en vervoer : (2,50 EUR) per (25,00 EUR) omzet, met een minimum van (14.500,00 EUR) per personeelslid (gemiddeld aantal over het beschouwde jaar); <KB 2000-07-20/63, art. 2, 075; Inwerkingtreding : 01-01-2002>  c) banken, krediet- en wisselinstellingen : (24.000,00 EUR) per personeelslid (gemiddeld aantal over het beschouwde jaar); <KB 2000-07-20/63, art. 2, 075; Inwerkingtreding : 01-01-2002>  d) verzekeringen : (2,50 EUR) per (25,00 EUR) geïnde premies; <KB 2000-07-20/63, art. 2, 075; Inwerkingtreding : 01-01-2002>  e) alle andere bedrijven en ondernemingen uit de handelssector en de dienstverlenende sector : (2,50 EUR) per (25,00 EUR) omzet, met een minimum van (7.000,00 EUR) per personeelslid (gemiddeld aantal over het beschouwde jaar). <KB 2000-07-20/63, art. 2, 075; Inwerkingtreding : 01-01-2002>  § 2. Het bedrag van de overeenkomstig § 1 vastgestelde belastbare winst mag in geen geval lager zijn dan (9.500,00 EUR). <KB 2000-07-20/63, art. 2, 075; Inwerkingtreding : 01-01-2002>  § 3. De overeenkomstig § 1 vastgestelde belastbare inkomsten omvatten niet de (in artikel 228, § 2, 9°, g,) van hetzelfde Wetboek vermelde meerwaarden. <KB 1997-05-20/39, art. 12, 1°, 039; Inwerkingtreding : 01-01- 1993>

### Afdeling XI. - Fiscale Commissies. (Wetboek van de inkomstenbelastingen 1992, artikel 347)

##### Art. 183

Het ambtsgebied van elk van de commissies waarvan sprake is in artikel 347 van het Wetboek van de inkomstenbelastingen 1992 wordt vastgesteld in bijlage IV.  De zetel van elk van die commissies wordt gevestigd in de gemeente die voorkomt in de linkerkolom van bijlage IV.

##### Art. 184

De bevoegdheid van de commissie strekt zich uit tot de gevallen die haar worden voorgelegd betreffende de natuurlijke personen en rechtspersonen belastbaar in haar ambtsgebied.

##### Art. 186

De inspecteur-voorzitter mag advies verstrekken; de andere leden van de commissie zijn stemgerechtigd.

##### Art. 187

§ 1. De commissie wordt voorgezeten door de inspecteur belast met het toezicht op de taxatiewerkzaamheden betreffende de belastingplichtige of door een ambtenaar van dezelfde graad die door de gewestelijk directeur van de directe belastingen, in wiens ambtsgebied de zetel van de commissie gevestigd is, aangewezen is om in de vervanging van de inspecteur te voorzien.  § 2. De andere commissieleden worden benoemd, ontslagen en, in geval van zware tekortkomingen in de uitoefening van hun mandaat, bij met redenen omklede beslissing ontzet door de in § 1 vermelde directeur.  Van die beslissing wordt kennis gegeven aan het betrokken lid zomede aan de overheid of aan de organisatie die het betrokken lid heeft voorgedragen.  § 3. Onder voorbehoud van de bepalingen van § 4 hierna, worden de stemgerechtigde commissieleden benoemd voor een termijn van 6 kalenderjaren.  Het mandaat van de uittredende leden kan worden hernieuwd.  § 4. Het stemgerechtigde commissielid dat wordt ontslagen of ontzet voor het verstrijken van de duur van zijn mandaat, wordt vervangen door een nieuw lid gekozen uit de kandidaten van dezelfde categorie die bij de laatste hernieuwing van de commissie zijn voorgedragen; dat lid voltooit het mandaat van zijn voorganger.  § 5. Wanneer de voordracht van de kandidaten voor de functie van stemgerechtigd commissielid door de daartoe bevoegde overheid of organisatie niet geschiedt binnen een maand na de aanvraag die de administratie te dien einde bij aangetekende brief heeft gedaan, kan de commissie niettemin geldig vergaderen en besluiten, ongeacht het aantal en de hoedanigheid van de in functie zijnde leden.

##### Art. 188

Het mandaat van commissielid is onbezoldigd.  Een reisvergoeding wordt toegekend aan de stemgerechtigde commissieleden die hun woonplaats hebben buiten de gemeente of agglomeratie waar de zetel van de commissie gevestigd is.  Die vergoeding wordt berekend volgens de regelen en tarieven die voor de gewone getuigen zijn vastgesteld overeenkomstig de artikelen 32, 33 en 146 tot 149 van het Algemeen Reglement op de gerechtskosten in strafzaken.

##### Art. 189

§ 1. Alvorens de stemgerechtigde commissieleden hun functie aanvaarden, leggen zij de volgende eed af in handen van de inspecteur-voorzitter :  "Ik zweer mij in volle onpartijdigheid van mijn opdracht te kwijten en de beraadslagingen waaraan ik deelneem geheim te houden".  § 2. De leden van wie het mandaat wordt verlengd, moeten geen nieuwe eed afleggen.

##### Art. 190

De commissie kan onder de aanwezige leden een secretaris aanwijzen om de notulen van de beraadslagingen op te stellen.  Indien de commissie geen secretaris aanwijst, neemt de inspecteur-voorzitter of een door hem gekozen ambtenaar van de directe belastingen die functie waar. Die ambtenaar maakt geen deel uit van de commissie en is niet stemgerechtigd; hij mag evenmin advies verstrekken.

##### Art. 191

De commissie vergadert op initiatief van de inspecteur-voorzitter.

##### Art. 194

De inspecteur-voorzitter mag de termijn van 15 dagen waarvan sprake is in de artikelen 192 en 193 tot minimum 5 dagen inkorten, ingeval hij die maatregel noodzakelijk acht om de belangen van de Schatkist te vrijwaren.

##### Art. 195

§ 1. De commissie vergadert en beraadslaagt rechtsgeldig ongeacht het aantal aanwezige leden.  § 2. De commissie neemt kennis van de stukken of memories neergelegd door de belastingplichtige.  Zij hoort de controleur en, eventueel, de ambtenaar die de verificatie heeft verricht, zomede de belastingplichtige of zijn lasthebber, eventueel bijgestaan door een consulent of deskundige.  § 3. Het debat is op tegenspraak, tenzij de belastingplichtige of zijn lasthebber verstek laat gaan.  § 4. De controleur en de belastingplichtige of zijn lasthebber mogen de beraadslaging en de stemming van de commissie niet bijwonen.

##### Art. 196

De besluiten van de commissie worden door de aanwezige stemgerechtigde leden bij meerderheid van stemmen genomen. Ze moeten met redenen omkleed zijn.

##### Art. 197

§ 1. Van de beraadslagingen worden, voor elke zaak, notulen opgesteld met vermelding van :  - de plaats en de datum van de vergadering;  - de naam, de voornamen en het adres, of de rechtsvorm, de firmanaam en het adres van de maatschappelijke zetel van de belastingplichtige;  - de naam, de voornamen, het beroep en het adres van de stemgerechtigde commissieleden, zomede hun hoedanigheid waarin zij op grond van artikel 185 van de commissie deel uitmaken.  De notulen vermelden, bij voorkomend geval :  - dat de commissie de belastingplichtige of zijn lasthebber heeft gehoord;  - dat ze kennis heeft genomen van de door de belastingplichtige neergelegde stukken of memories;  - dat artikel 194 is toegepast.  De notulen behelzen het met redenen omklede advies van de commissie en vermelden het aantal stemmen dat voor of tegen de in stemming gebrachte besluiten zijn uitgebracht, zomede het aantal onthoudingen, zonder enige precisering over het door elk van de leden tijdens de stemming ingenomen standpunt.  § 2. De notulen worden in drievoud opgesteld. Elk exemplaar wordt door alle aanwezige leden ondertekend; de handtekeningen worden gevolgd door de naam van de ondertekenaar.

##### Art. 198

De inspecteur-voorzitter zendt 2 exemplaren van de notulen aan de controleur vermeld in artikel 192. Deze zendt één exemplaar aan de belastingplichtige bij ter post aangetekende brief.

### Afdeling XII. - Bepaling van het belastbare tijdperk voor de personenbelasting, vennootschapsbelasting, rechtspersonenbelasting, belasting van niet-inwoners en voorheffingen, en van de inkomsten die daartoe behoren. (Wetboek van de inkomstenbelastingen 1992, artikel 360, tweede lid)

##### Art. 199

Het belastbare tijdperk valt samen met het jaar waarnaar het aanslagjaar wordt genoemd, voor de toepassing :  a) van de onroerende voorheffing;  b) van de roerende voorheffing;  c) van de bedrijfsvoorheffing vermeld in de artikelen 270 tot 275 van het Wetboek van de inkomstenbelastingen 1992.

##### Art. 200

Het belastbare tijdperk valt samen met het jaar voor dat waarnaar het aanslagjaar wordt genoemd, voor de toepassing :  a) van de personenbelasting en van de belasting van niet-inwoners die overeenkomstig de artikelen 243, 244, 245 en 248 van het Wetboek van de inkomstenbelastingen 1992 wordt gevestigd;  b) van de vennootschapsbelasting en van de belasting van niet-inwoners die overeenkomstig de artikelen 233 en 248 van hetzelfde Wetboek wordt gevestigd, wanneer de betrokkenen niet of per kalenderjaar boekhouden;  c) van de rechtspersonenbelasting en van de belasting van niet-inwoners die overeenkomstig de artikelen 234 en 248 van hetzelfde Wetboek wordt gevestigd.

##### Art. 203

Met betrekking tot belastingplichtigen voor wie de gronden voor belastbaarheid overeenkomstig artikel 200 slechts na 1 januari aanwezig zijn of voor 31 december zijn weggevallen, stemt het belastbare tijdperk overeen met het gedeelte van het jaar waarin die gronden aanwezig zijn geweest.  In afwijking van gezegd artikel 200 wordt het aanslagjaar genoemd naar het jaar waarin de gronden voor belastbaarheid weggevallen zijn.

##### Art. 204

Inkomsten van het in de artikelen 199 tot 203 vermelde belastbare tijdperk zijn :  1° inkomsten van gebouwde of ongebouwde onroerende goederen die op dat tijdperk betrekking hebben;  2° inkomsten en opbrengsten van roerende goederen en kapitalen die overeenkomstig de artikelen 261, 2°, 263, eerste lid, en 267 van het Wetboek van de inkomstenbelastingen 1992 aan de roerende voorheffing onderworpen zijn en tijdens dat tijdperk aan de belastingplichtige zijn betaald of toegekend;  3° beroepsinkomsten, bestaande uit :  a) vastgestelde of vermoede winst of baten van dat tijdperk;  b) tijdens dat tijdperk aan de belastingplichtige betaalde of toegekende bezoldigingen;  c) tijdens dat tijdperk aan de belastingplichtige betaalde of toegekende pensioenen, renten en toelagen;  4° diverse inkomsten, bestaande uit :  a) vastgestelde of vermoede winst of baten van dat tijdperk, vermeld in artikel 90, 1°, van hetzelfde Wetboek;  b) tijdens dat tijdperk aan de belastingplichtige betaalde of toegekende sommen vermeld in artikel 90, 2° tot 7°, van hetzelfde Wetboek;  c) vastgestelde of vermoede meerwaarden van dat tijdperk vermeld in artikel 90, 8°, van hetzelfde Wetboek;  d) meerwaarden vermeld in artikel 90, 9°, van hetzelfde Wetboek;  (e) vastgestelde of vermoede meerwaarden van dat tijdperk vermeld in artikel 90, 10°, van hetzelfde Wetboek;) <KB 1997-05-20/39, art. 13, 1°, 039; Inwerkingtreding : 01-01-1997>  5° de kosten, bijdragen, pensioenen, renten en toelagen vermeld (in de artikelen 222 en 223, 4° en 5°) van hetzelfde Wetboek, die door de belastingplichtige tijdens dat tijdperk zijn betaald of toegekend. <KB 1997-05- 20/39, art. 13, 2°, 039; Inwerkingtreding : 01-01-1998>

##### Art. 205

Voor de toepassing :  1° van artikel 204, 3°, a, worden winst of baten die uit een boekhouding blijken, geacht verkregen te zijn op de datum van afsluiting van het boekjaar waarop zij betrekking hebben;  2° van artikel 204, 3°, b, wordt het bedrag vermeld in artikel 31, derde lid, van het Wetboek van de inkomstenbelastingen 1992 geacht te zijn betaald of toegekend op de datum waarop de aandelen zijn overgedragen;  3° (...) <KB 1995-09-01/42, art. 19, 019; Inwerkingtreding : 01-01-1993>

##### Art. 206

De bijzondere aanslag in de vennootschapsbelasting vermeld in artikel 219 van het Wetboek van de inkomstenbelastingen 1992, de bijzondere aanslag in de belasting van niet-inwoners gevestigd volgens artikel 246, 2°, en de aanslagen vermeld in artikel 247, 2° en 3°, van hetzelfde Wetboek, worden verbonden aan het aanslagjaar betreffende het belastbare tijdperk bepaald overeenkomstig de artikelen 200 tot 203, in de loop waarvan de omstandigheid, waarin gezegde aanslagen hun grond vinden, zich heeft voorgedaan.

### Afdeling XIII. - (Maatregelen betreffende de werkzaamheden van koppelbazen. (Wetboek van de inkomstenbelastingen 1992, artikelen 403, 404 en 406)). <KB 1998-12-26/31, art. 20, 049; Inwerkingtreding : 01-01-1999>

##### Art. 207

<KB 1998-12-26/31, art. 21, 049; Inwerkingtreding : 01-01-1999> Het krachtens artikel 403, van hetzelfde Wetboek ingehouden bedrag moet worden gestort bij de ontvanger die door de directeur-generaal van de directe belastingen wordt aangewezen.  De betaling van het ingehouden bedrag moet worden verricht op hetzelfde tijdstip als de betaling aan de aannemer en uitsluitend door storting of overschrijving op de postrekening van de aangewezen ontvanger.  Op het stortings- of overschrijvingsbewijs moet naast de naam, het adres en het BTW-nummer van de in het vorig lid bedoelde aannemer, de vermelding "Art. 403 WIB 92", voorkomen, zomede de verwijzing naar de factuur waarop de betaling betrekking heeft.  Gelijktijdig met de vermelde storting of overschrijving, zendt degene die de storting moet verrichten, aan de ontvanger een afschrift van de facturen waarop de betaling betrekking heeft.

##### Art. 209

<KB 1998-12-26/31, art. 23, 049; Inwerkingtreding : 01-01-1999> § 1. De persoon op wiens schuldvordering het gestorte bedrag werd ingehouden kan, voor zover en in de mate dat hij geen achterstallige belastingen verschuldigd is, bij de in artikel 207 bedoelde ontvanger een aanvraag om teruggaaf indienen.  De aanvraag dient inzonderheid te vermelden:  1° de naam, het adres en in voorkomend geval het BTW-nummer van degene die de inhouding en de storting heeft gedaan, de datum van die storting, alsmede de datum, het nummer en het bedrag, exclusief belasting over de toegevoegde waarde, van de factuur waarop de storting betrekking had;  2° de naam, het adres en het BTW-nummer van de onderaannemers op wie de aanvrager, voor de uitvoering van de met de in 1° bedoelde persoon gesloten overeenkomst, een beroep heeft gedaan voor in artikel 1 van het koninklijk besluit van 26 december 1998 tot uitvoering van de artikelen 400, 401, 404 en 406 van het Wetboek van de inkomstenbelastingen 1992 en van artikel 30bis van de wet van 27 juni 1969 tot herziening van de besluitwet van 28 december 1944 betreffende de maatschappelijke zekerheid der arbeiders, bedoelde werkzaamheden.  De aanvraag om teruggaaf geschiedt door middel van een formulier waarvan het model wordt vastgesteld door de directeur-generaal van de directe belastingen.  § 2. In de mate dat het niet wordt aangewend tot betaling van achterstallige belastingschulden overeenkomstig artikel 406, §§ 1 en 2, van hetzelfde Wetboek, wordt het gestorte bedrag ten spoedigste en uiterlijk binnen een termijn van zes maanden te rekenen vanaf de regelmatig ingediende aanvraag om teruggaaf, door de ontvanger aan de aanvrager overgemaakt.  § 3. Wanneer het gestorte bedrag geheel of gedeeltelijk aangewend overeenkomstig het voornoemde artikel 406, §§ 1 en 2, geeft de ontvanger daarvan binnen de in § 2 bedoelde termijn kennis aan de aanvrager met vermelding van alle gegevens omtrent de aangezuiverde schulden.

##### Art. 210

<KB 1998-12-26/31, art. 28, 049; Inwerkingtreding : 01-01-1999> Wanneer degene die de in artikel 403, van hetzelfde Wetboek opgelegde storting niet heeft verricht, alsnog de vereiste storting uitvoert op verzoek van de administratie en binnen de door haar opgelegde termijn en wanneer het bewijs van storting wordt overgelegd, wordt de in artikel 404, § 1, van dat Wetboek bedoelde administratieve boete, voor ten hoogste drie overtredingen, verminderd tot een achtste, een vierde of de helft van die boete naargelang het respectievelijk een eerste, een tweede of een derde overtreding betreft.

### Afdeling IIIBis. - (Inning door de administratie van de belasting over de toegevoegde waarde, registratie en domeinen, van de bedrijfsvoorheffing op meerwaarden verwezenlijkt op onroerende goederen door niet- inwoners in het kader van hun beroepswerkzaamheid.) <Ingevoegd bij KB 1997-01-10/42, art. 5; Inwerkingtreding : 01-01-1997>  (Wetboek van de inkomstenbelastingen 1992 - artikel 412bis)

##### Art. 210ter


### Afdeling XIV. - Zakelijke zekerheid en persoonlijke borgstelling. (Wetboek van de inkomstenbelastingen 1992, artikel 420, § 1)

##### Art. 211

De hoegrootheid van de in artikel 420, § 1, van het Wetboek van de inkomstenbelastingen 1992 voorgeschreven waarborg wordt bij beslissing van de directeur van de directe belastingen vastgelegd. Zij moet gelijk zijn aan het vermoedelijke bedrag van de verplichtingen over één jaar die op grond van voormeld Wetboek aan de betrokken natuurlijke of rechtspersoon kunnen worden opgelegd, onder aftrek van de netto- verkoopwaarde van zijn goederen die het pand van de Schatkist vormen en die gelegen zijn in België of in een land waarmede België een overeenkomst heeft gesloten tot regeling van de wederzijdse bijstand inzake de invordering van de belastingen waaraan de belanghebbende is onderworpen.  De waarborg mag evenwel in geen geval minder dan (750,00 EUR) bedragen. <KB 2000-07-20/63, art. 3, 075; Inwerkingtreding : 01-01-2002>

##### Art. 212

§ 1. Indien de waarborg wordt geëist van een belastingschuldige die reeds een beroepswerkzaamheid heeft waarvan de uitoefeningsvoorwaarden niet aanzienlijk zullen worden gewijzigd, wordt hij vastgesteld in verhouding tot de belastingen en bijbehoren verschuldigd voor de 3 belastbare tijdperken die voorafgaan aan deze waarin de beslissing wordt genomen, zonder meer te mogen bedragen dan tweemaal het hoogste bedrag aan belastingen in hoofdsom verschuldigd voor één van deze 3 belastbare tijdperken, verminderd met de netto- verkoopwaarde van de goederen van belanghebbende die de waarborg van de Schatkist vormen en die gelegen zijn in België of in een land waarmede België een overeenkomst heeft gesloten tot regeling van de wederzijdse bijstand inzake de invordering van de belastingen waaraan de belanghebbende is onderworpen.  Voor de toepassing van het voorgaande lid moet onder verschuldigde belastingen worden verstaan de belastingen en voorheffingen die zijn ingekohierd en, bij gebrek aan inkohiering, de belastingen en voorheffingen die betrekking hebben op de aangegeven inkomsten of op die waarmee de belastingschuldige zich in de loop van de aanslagverrichtingen akkoord heeft verklaard.  § 2. Indien de waarborg wordt geëist naar aanleiding van een toekomstige beroepswerkzaamheid of van een beroepswerkzaamheid die sedert minder dan één jaar begonnen is of waarvan de uitoefeningsvoorwaarden aanzienlijk zullen worden gewijzigd of sedert minder dan één jaar gewijzigd zijn, raamt de directeur het vermoedelijke bedrag van de verplichtingen van de betrokken natuurlijke of rechtspersoon op basis van de beroepsinkomsten vastgelegd volgens de bij artikel 342, § 1, van het Wetboek van de inkomstenbelastingen 1992 vastgelegde criteria.

##### Art. 213

De te verstrekken waarborg bestaat hetzij uit een zakelijke zekerheid in de vorm van een borgtocht in geld of in overheidsfondsen of van een hypotheekvestiging, hetzij uit een persoonlijke borgstelling.  De in artikel 219 vermelde ontvanger van de directe belastingen mag andere wijzen van waarborgstelling aanvaarden.  Indien nodig mogen de voormelde wijzen gelijktijdig worden aangewend om de totale zekerheid te verstrekken.

##### Art. 216

Zonder afbreuk te doen aan de mogelijkheid voor de ontvanger om andere wijzen van waarborgstelling te aanvaarden zijn de aanneembare overheidsfondsen die welke aangenomen worden voor het stellen van borgtochten van aannemers. De lijst en de aannemingsvoet ervan worden bepaald bij de jongste desbetreffende besluiten door de Minister van Financiën genomen en door diens toedoen gepubliceerd.  Effecten aan toonder worden gedeponeerd in handen van de Staatskassier of van diens agenten; inschrijvingen op naam worden, zowel in het Grootboek als op het uittreksel, in de rand aangetekend met een vermelding waarbij wordt vastgesteld dat zij niet zonder geschreven toestemming van de ontvanger van de directe belastingen mogen worden vervreemd of te gelde gemaakt.

##### Art. 217

De persoonlijke borg moet bekwaam zijn, volgens de Belgische wet, om verbintenissen aan te gaan en aangenomen worden door de ontvanger van de directe belastingen vermeld in artikel 219.

##### Art. 218

Indien de zakelijke zekerheid of de gegoedheid van de persoonlijke borg wegens enige oorzaak - zoals waardevermindering van de tot zekerheid dienende onroerende goederen of overheidsfondsen of merkelijke vermindering van het fortuin van de borg - ongenoegzaam wordt geacht, is de belastingschuldige op het eerste verzoek van de ontvanger van de directe belastingen gehouden een nieuwe zakelijke zekerheid of een nieuwe persoonlijke borg te stellen.

##### Art. 219

In de akten wordt de administratie vertegenwoordigd door de ontvanger van de directe belastingen vermeld in de beslissing van de directeur of, bij gebrek aan zulke vermelding, door de ontvanger van de plaats van aanslag.  Samen met de nodige inlichtingen en bewijsstukken en binnen de termijn gesteld in artikel 421 van het Wetboek van de inkomstenbelastingen 1992, overhandigt de belastingschuldige aan deze ambtenaar hetzij het ontwerp van akte van hypotheekvestiging, van verpanding van een inschrijving op naam of van verbintenis van de persoonlijke borg, hetzij het stortingsbewijs of het bewijs van deponering voor borgtochten in geld of in effecten aan toonder.

### Afdeling XV. - Verplichtingen van kredietinstellingen of -inrichtingen. (Wetboek van de inkomstenbelastingen 1992, artikel 443)

##### Art. 220

De ambtenaar vermeld in artikel 443 van het Wetboek van de inkomstenbelastingen 1992 is :  1° de ontvanger van de directe belastingen in wiens ambtsgebied de natuurlijke persoon of rechtspersoon aan wie een in dat artikel vermeld krediet, lening of voorschot wordt toegekend, zijn woonplaats, zijn maatschappelijke zetel of zijn voornaamste inrichting van bestuur heeft;  2° de ontvanger van de directe belastingen belast met de inning van de belasting van niet-inwoners indien de betrokken natuurlijke persoon of rechtspersoon zijn woonplaats, zijn maatschappelijke zetel of zijn voornaamste inrichting van bestuur in het buitenland heeft.

##### Art. 221

Het attest vermeld in artikel 443 van het Wetboek van de inkomstenbelastingen 1992 wordt uitgereikt nadat door de belanghebbende natuurlijke persoon of rechtspersoon een aanvraag, in 3 exemplaren, is ingediend. De aanvraag en het attest worden gesteld op een formulier waarvan het model wordt vastgesteld door de directeur-generaal van de directe belastingen. Het attest wordt uitgereikt binnen 8 dagen na de indiening van de aanvraag.

##### Art. 222

Per krediet, lening of voorschot, waarvoor een voordeel inzake economische expansie is aangevraagd, moeten de kredietinstellingen en -inrichtingen vermeld in artikel 443 van het Wetboek van de inkomstenbelastingen 1992, in principe, in het bezit zijn van slechts 1 attest.  De datum van uitreiking van dat attest mag niet vroeger zijn dan 1 maand voor de datum van de aanvraag tot verkrijging van het voordeel, noch later dan deze datum.  Er moet evenwel een nieuw attest worden voorgelegd wanneer de beslissing tot toekenning van het voordeel niet is genomen binnen 6 maanden te rekenen van de datum van het attest.

##### Art. 223

Een exemplaar van het attest vermeld in artikel 443 van het Wetboek van de inkomstenbelastingen 1992 wordt door de in artikel 220 aangewezen ambtenaar gezonden aan de overheid vermeld in de aanvraag van het attest.  Wanneer uit het attest blijkt dat een bedrag als belastingen of bijbehoren eisbaar is ten name van de natuurlijke persoon of rechtspersoon die een voordeel inzake economische expansie heeft aangevraagd, bepaalt de beslissing tot toekenning van het voordeel dat de kredietinstelling of -inrichting de fondsen niet geheel mag vrijgeven tenzij de betrokkene zijn belastingschuld heeft betaald.

### Afdeling XVI. - Schaal van de belastingverhogingen. (Wetboek van de inkomstenbelastingen 1992, artikel 444)

##### Art. 225

De schaal van de belastingverhogingen bij niet-aangifte, andere dan inzake roerende voorheffing en bedrijfsvoorheffing, wordt als volgt vastgesteld :

Aard van de overtredingen Verhogingen

------------------------- -----------

A. Niet-aangifte te wijten aan omstandigheden

onafhankelijk van de wil van de belastingplichtige : Nihil

B. Niet-aangifte zonder het opzet de belasting te

ontduiken :

- 1e overtreding (zonder inachtneming van de in A

vermelde gevallen van niet-aangifte) : 10 pct.

- 2e overtreding : 20 pct.

- 3e overtreding : 30 pct.

Vanaf de 4e overtreding worden de overtredingen

van deze aard bij C ingedeeld en als zodanig bestraft.

C. Niet-aangifte met het opzet de belasting te ontduiken :

- 1e overtreding : 50 pct.

- 2e overtreding : 100 pct.

- 3e overtreding en volgende overtredingen : 200 pct.

D. Niet-aangifte gepaard gaande met ofwel onjuistheid

of verwijzing door valsheid of gebruik van valse stukken

tijdens de verificatie van de belastingstoestand, ofwel

met een omkoping of een poging tot omkopen van

ambtenaren :

in alle gevallen : 200 pct.

##### Art. 226

De schaal van de belastingverhogingen bij onvolledige of onjuiste aangifte, andere dan inzake roerende voorheffing en bedrijfsvoorheffing, wordt als volgt vastgesteld :

Aard van de overtredingen Verhogingen

-------------------------- -----------

A. Onvolledig of onjuiste aangifte te wijten aan

omstandigheden onafhankelijk van de wil van de

belastingplichtige : Nihil

B. Onvolledige of onjuiste aangifte zonder het

opzet de belasting te ontduiken :

- 1e overtreding (zonder inachtneming van de in A

vermelde gevallen) : 10 pct.

- 2e overtreding : 20 pct.

- 3e overtreding : 30 pct.

Vanaf de 4e overtreding worden de overtredingen

opzet de belasting te ontduiken :

- 1e overtreding : 50 pct.

- 2e overtreding : 100 pct.

- 3e overtreding en volgende overtredingen : 200 pct.

D. Onvolledige of onjuiste aangifte gepaard gaande

met valsheid of gebruik van valse stukken of met een

omkoping of een poging tot omkopen van ambtenaren :

in alle gevallen : 200 pct.

##### Art. 227

Voor de vaststelling van het toe te passen percent van de belastingverhogingen worden de vorige overtredingen die bedoeld zijn in B en C van de artikelen 225 en 226 niet in aanmerking genomen wanneer geen enkele overtreding inzake aangifte in de inkomstenbelastingen is bestraft voor de laatste 4 aanslagjaren die het aanslagjaar voorafgaan waarvoor de nieuwe overtreding moet worden bestraft.

##### Art. 228

De schaal van de belastingverhogingen bij niet-aangifte of bij onvolledige of onjuiste aangifte inzake roerende voorheffing en bedrijfsvoorheffing, gepaard gaande met niet-betaling of ontoereikende betaling van de voormelde voorheffingen, wordt als volgt vastgesteld :

Aard van de overtredingen Verhogingen

------------------------- -----------

A. Overtreding te wijten aan omstandigheden

onafhankelijk van de wil van de belastingschuldige : Nihil

B. Overtreding zonder het opzet de belasting te ontduiken :

- 1e overtreding : Nihil

- 2e overtreding : 10 pct.

- 3e overtreding : 20 pct.

- 4e en 5e overtreding : 30 pct.

Vanaf de 6e overtreding worden de overtredingen van

deze aard bij C ingedeeld en als zodanig bestraft.

C. Overtreding met het opzet de belasting te ontduiken :

- 1e overtreding : 50 pct.

- 2e en 3e overtreding : 75 pct.

- 4e en 5e overtreding : 100 pct.

- 6e en 7e overtreding : 150 pct.

- 8e overtreding en volgende overtredingen : 200 pct.

D. Overtreding gepaard gaande met valsheid of gebruik van

valse stukken of met een omkoping of een poging tot

omkopen van ambtenaren :

in alle gevallen : 200 pct.

Voor de vaststelling van het toe te passen percent van de belastingverhogingen worden de vorige overtredingen die bedoeld zijn in B en C niet in aanmerking genomen wanneer geen enkele overtreding inzake aangifte en betaling van de roerende voorheffing en de bedrijfsvoorheffing, afzonderlijk beschouwd, is bestraft voor 4 opeenvolgende maandelijkse, driemaandelijkse of jaarlijkse vervaldagen.

##### Art. 229

Voor de vaststelling van het krachtens de artikelen 225, 226 en 228 toe te passen percent van de belastingverhogingen, is een tweede of een volgende overtreding aanwezig wanneer op het ogenblik waarop een nieuwe overtreding wordt begaan, aan de overtreder kennis is gegeven van de verhoging die de vorige overtreding heeft bestraft.

##### Art. 230

§ 1. Voor zover zij niet inzonderheid de inkomstenbelastingen betreffen, zijn de bepalingen van de artikelen 126, 127 en 128 tot 176, van toepassing op de provinciale belastingen.  § 2. In afwijking van artikel 139 mogen niet ten kohiere gebrachte provinciale belastingen waarvoor een plaat, penning of ander kenteken wordt uitgereikt, ook betaald worden in munten of bankbiljetten die in België wettig betaalmiddel zijn.

### Afdeling II. - Aanvullende agglomeratie- en gemeentebelastingen.

##### Art. 231

De kohieren van de aanvullende agglomeratiebelasting op de personenbelasting en de kohieren van de aanvullende gemeentebelasting op de personenbelasting worden opgemaakt volgens de door de directeur- generaal van de directe belastingen gestelde regelen.  Die aanvullende belastingen worden opgenomen in kohieren verbonden aan het begrotingsjaar dat loopt op de datum waarop ze uitvoerbaar worden verklaard; toegepast worden de tarieven in verband met de desbetreffende aanslagjaren.

##### Art. 232

(...) (Opgeheven) <KB 2000-07-20/63, art. 7, 078; Inwerkingtreding : 01-01-2002>  De aanvullende belastingen worden (in euro gevestigd en afgerond op de cent). <KB 2000-07-20/63, art. 5, 076; Inwerkingtreding : 01-01-2002>

##### Art. 233

Het bepaalde in de artikelen 133, 136 tot 176 en 207 tot 230 is op de in artikel 231 vermelde aanvullende belastingen van toepassing.

## HOOFDSTUK V. - OVERGANGSBEPALINGEN.

### Afdeling I. - Inhouding van een gedeelte van de roerende voorheffing. (Wetboek van de inkomstenbelastingen 1992, artikel 507, derde lid)

## HOOFDSTUK IVbis. - Bijzondere invorderingsregels inzake de toekenningen aan de provincies, de agglomeraties en de gemeenten (Wetboek van de inkomstenbelastingen 1992, art. 470bis). <ingevoegd bij KB 1999-03-10/41, art. 1, Inwerkingtreding : 1999-04-17>

##### Art. 233bis


## HOOFDSTUK V. - OVERGANGSBEPALINGEN.

### Afdeling I. - Inhouding van een gedeelte van de roerende voorheffing. (Wetboek van de inkomstenbelastingen 1992, artikel 507, derde lid)

### Afdeling II. - Herschatting voor de berekening van de afschrijving van bepaalde activa die zijn verkregen of tot stand gebracht voor de normale datum van afsluiting van de laatste jaarbalans opgemaakt voor 31 december 1940 en die nog in gebruik waren op de normale datum van afsluiting van de laatste jaarbalans opgemaakt voor 31 december 1946. (Wetboek van de inkomstenbelastingen 1992, artikel 511, § 2)

##### Art. 235

Voor de toepassing van de artikelen 236 tot 252, worden onder aanschaffings- of beleggingswaarde van de activa de kosten van aankoop of oprichting verstaan, met inbegrip van de rechten en taksen die er betrekking op hebben, de eventuele kosten van vervoer, van montage en andere gelijkaardige.

##### Art. 236

Als activa waarvan de aanschaffings- of beleggingswaarde voor de berekening van de vrij van belasting toegestane afschrijving mag worden herschat, gelden outillage en ermee gelijkgestelde nijverheidsgebouwen, dat wil zeggen al dan niet vaste machines, werktuigen en toestellen met toebehoren, zomede nijverheidsgebouwen en tot nijverheids- en handelsdoeleinden gebruikt meubilair, die als het ware deel uitmaken van de outillage en aan snelle slijtage of verval onderhevig zijn.  De outillage omvat inzonderheid de in handelsbedrijven gebezigde voorwerpen die door intensief gebruik, of onder invloed van technische vooruitgang, mode en gewoonten, aan snelle slijtage blootstaan of vaak moeten worden vervangen.

##### Art. 237

Van het voordeel van afschrijving op de herschatte aanschaffings- of beleggingswaarde zijn over het algemeen de terreinen uitgesloten, zomede gebouwen die geen met outillage gelijkgestelde nijverheidsgebouwen zijn en inzonderheid tot woning of kantoor dienen; dit geldt eveneens voor het meubilair waarvan woningen en kantoren voorzien zijn, voor portefeuille, octrooien, fabrieksmerken, handelsfonds, cliënteel en firma. De afschrijving van die activa moet uit fiscaal oogpunt verder op grond van de niet herziene aanschaffings- of beleggingswaarde geschieden.

##### Art. 238

§ 1. De herschatting mag slechts slaan op outillage en ermee gelijkgestelde nijverheidsgebouwen, die de belastingplichtige heeft verkregen of tot stand gebracht voor de normale datum van afsluiting van de laatste jaarbalans opgemaakt voor 31 december 1940 en die nog werkelijk in gebruik waren op de normale datum van afsluiting van de laatste jaarbalans opgemaakt voor 31 december 1946.  Met betrekking tot outillage en ermee gelijkgestelde nijverheidsgebouwen van ondernemingen die zijn opgericht door omzetting, fusie, opslorping, splitsing of overname van vroeger bestaande ondernemingen of bedrijfsafdelingen van zulke ondernemingen, wordt evenwel met de datum van verkrijging of totstandbrenging van die activa door de omgezette, overgenomen of gesplitste ondernemingen rekening gehouden, voor zover die mutaties niet ten gevolge hebben gehad de tijdens de bezetting van het land gebruikte produktiemiddelen in hun geheel te verhogen. Onder hetzelfde voorbehoud worden outillage en ermee gelijkgestelde nijverheidsgebouwen die zijn geleverd of opgericht ter uitvoering van contracten of overeenkomsten gesloten voor de uiterste datum van verkrijging of totstandbrenging bepaald in het eerste lid, voor de toepassing van deze bepaling beschouwd als verkregen of tot stand gebracht op de datum van gezegde contracten of overeenkomsten.  De bovenbedoelde activa die in eigendom zijn opgeëist of ingevolge oorlogsfeiten verloren, vernield of buiten gebruik gesteld zijn, worden voor de toepassing van de artikelen 236 tot 252 gelijkgesteld met activa die nog werkelijk in gebruik waren op de uiterste datum bepaald op het einde van het eerste lid.  § 2. Degene van gezegde activa die na de uiterste datum vermeld in § 1 van dit artikel zijn verkregen of tot stand gebracht, worden verder afgeschreven volgens de werkelijke aanschaffings- of beleggingswaarde bepaald in artikel 235.

##### Art. 240

De nieuwe aanschaffings- of beleggingswaarde van iedere categorie activa vermeld in de artikelen 236, 238, § 1, en 239, mag niet meer bedragen dan twee en een halve maal hun waarde geschat naar de per 31 augustus 1939 geldende normale prijzen en met inachtneming van hun toestand van stoffelijke slijtage en van hun werkelijke waardevermindering op de normale datum van afsluiting van de laatste jaarbalans opgemaakt voor 31 december 1946 of, in voorkomend geval, op de datum van opeising in eigendom of van verlies, vernieling, of buitengebruikstelling ingevolge oorlogsfeiten.  De aan elk herschat activum toegekende nieuwe aanschaffings- of beleggingswaarde mag niet meer bedragen dan zijn industriële- of handelswaarde op de normale datum van afsluiting van de laatste jaarbalans opgemaakt voor 31 december 1946.

##### Art. 241

Om het bepaalde in de artikelen 236 tot 252 te genieten, stelt de belastingplichtige, per categorie of per boekhoudrubriek, een omstandige inventaris op van de te herschatten activa.  Voorwerpen van geringe waarde worden in een post "allerlei voorwerpen" begrepen voor een benaderende en te goeder trouw vastgestelde waarde in ronde cijfers.  De inventaris vermeldt respectievelijk :  a) de aard van elk geïnventariseerd activum;  b) voor zover mogelijk de datum van verkrijging of van totstandbrenging, behalve voor de post "allerlei voorwerpen";  c) voor elk geïnventariseerd activum en voor elke categorie activa, de waarde 1939 vastgesteld overeenkomstig het bepaalde in artikel 240, eerste lid;  d) de industriële of handelswaarde van elk activum op de normale datum van afsluiting van de laatste jaarbalans opgemaakt voor 31 december 1946, voor zover gezegde waarde meer of minder bedraagt dan twee en een halve maal de waarde vermeld in c;  e) de nieuwe aanschaffings- of beleggingswaarde voor de berekening van de afschrijving, zijnde maximaal voor elke categorie activa twee en een halve maal de waarde vermeld in c, en voor elk activum de waarde vermeld in d.  De activa die in eigendom zijn opgeëist, of ingevolge oorlogsfeiten vernield, verloren of buiten gebruik gesteld zijn, worden afzonderlijk in gezegde inventaris ingeschreven.

##### Art. 242

De in artikel 241 vermelde inventaris wordt in duplo opgesteld en een exemplaar ervan wordt aan de controleur van de directe belastingen of aan de taxatiedienst van het ambtsgebied overhandigd tot staving van de aangifte in de inkomstenbelastingen over het boekjaar in de balans waarvan de herschatting is opgenomen, of ten laatste op 24 januari 1948 ingeval de afschrijving op die grondslag is berekend met ingang van het aanslagjaar 1947; hij moet ondertekend zijn door de gedelegeerde bestuurders en door de commissarissen in kapitaalvennootschappen en door de verschillende personen die de vennootschap, firma of vereniging kunnen verbinden in anders dan in de vorm van kapitaalvennootschappen geëxploiteerde ondernemingen.

##### Art. 243

De herschatting van outillage en ermee gelijkgestelde nijverheidsgebouwen moet opgenomen worden in de boeken of balansen die van 31 december 1947 af en ten laatste op 30 december 1948 zijn afgesloten; zij moet afzonderlijk in het actief en in het passief van iedere jaarbalans voorkomen onder de volgende rubrieken of onder enige andere soortgelijke benaming :  - in het actief :  "Outillage en ermee gelijkgestelde nijverheidsgebouwen (herschatting)";  - in het passief :  "Meerwaarde van herschatting van outillage en ermee gelijkgestelde nijverheidsgebouwen". Deze meerwaarde mag evenwel in rekening "Kapitaal" ingelijfd worden.

##### Art. 244

De nieuwe aanschaffings- of beleggingswaarde, bepaald overeenkomstig de artikelen 235 tot 240 en in het actief opgenomen, dient tot grondslag voor de berekening van de afschrijving; deze mag vrij van belasting gedaan worden tot die waarde volledig bereikt is - eventueel verminderd met de opeisings- of herstelvergoedingen betreffende herschatte activa - en dit ongeacht de datum van verkrijging van de outillage of de ermee gelijkgestelde nijverheidsgebouwen of ongeacht de reeds op die activa voor de normale afsluiting van de laatste jaarbalans opgemaakt voor 31 december 1946 gedane afschrijving.

##### Art. 245

De belastingplichtige verdeelt de herschatte activa in 3 of 4 categorieën naar hun vermoedelijke gebruiksduur.  Gemiddelde jaarlijkse afschrijvingspercenten worden in overleg tussen de belanghebbende en de bevoegde ambtenaren van de administratie der directe belastingen vastgesteld; die percenten kunnen inzonderheid verschillen naar de aard van de activa, de intensiteit van het gebruik ervan en hun staat van slijtage of van economische efficiëntie bij de herschatting. Behoudens herziening van gezegde percenten op schriftelijke en met redenen omklede aanvraag van de belastingplichtige, dienen deze tot grondslag voor de berekening van de vrij van belasting toe te passen jaarlijkse afschrijving.  De aldus in overleg vastgestelde regelen worden bevestigd in een door beide partijen ondertekend stuk; dat stuk wordt bij het fiscaal dossier van de belanghebbende gevoegd, die er een afschrift kan van verkrijgen.

##### Art. 247

Ingeval een herschat activum tijdens een boekjaar is vervreemd, vernield of definitief buiten gebruik gesteld, kan het op de herschatte waarde van dat activum nog af te schrijven saldo, onder eventuele aftrek van de realisatieprijs, slechts vrij van belasting worden afgeschreven tot aan de afsluiting van gezegd boekjaar.

##### Art. 248

Met betrekking tot activa die in eigendom zijn opgeëist of ingevolge oorlogsfeiten zijn vernield, verloren of buiten gebruik gesteld, kan afschrijving van de herschatte waarde, onder aftrek van de opeisings- of herstelvergoedingen betreffende die activa, niet geschieden dan na definitieve vaststelling van het bedrag van gezegde vergoedingen.  Met betrekking tot activa die ingevolge oorlogsfeiten zijn vernield, verloren of buiten gebruik gesteld, kan afschrijving van de herschatte waarde niettemin vrij van belasting voor de definitieve vaststelling van de herstelvergoeding geschieden, zo de belastingplichtige sedert de verkrijging van de voorwerpen die voor herschatting in aanmerking komen, regelmatig boekhoudt overeenkomstig het Wetboek van Koophandel.  Die afschrijving dient te geschieden volgens de gebruikelijke jaarlijkse afschrijvingspercenten die in gewone omstandigheden voor activa van dezelfde aard toegepast worden. Bedoelde percenten worden in overleg tussen de belastingplichtige en de administratie der directe belastingen vastgesteld en bevestigd zoals bepaald is in artikel 245, derde lid.  Wanneer de aldus gedane en aangenomen afschrijvingen meer bedragen dan het nadelig verschil tussen de herschatte waarde en de herstelvergoeding, of wanneer de herstelvergoeding gelijk is aan of meer bedraagt dan de herschatte waarde, is het gedeelte van de som van die afschrijvingen dat gezegd verschil overtreft, of de som van die afschrijvingen, een belastbaar inkomen van het jaar waarin het bedrag van de herstelvergoeding definitief is vastgesteld.

##### Art. 249

De afschrijving van de nieuwe aanschaffings- of beleggingswaarde moet afzonderlijk in het passief van iedere jaarbalans voorkomen onder de rubriek "Afschrijving van de herschatte waarde van outillage en ermee gelijkgestelde nijverheidsgebouwen" of onder enige andere soortgelijke benaming.

##### Art. 250

De afschrijving van de nieuwe aanschaffings- of beleggingswaarde wordt slechts vrij van inkomstenbelastingen toegestaan onder de uitdrukkelijke voorwaarde dat zij niet wordt gebruikt voor enigerlei opneming, uitkering of verdeling en niet tot grondslag dient voor de berekening van de jaarlijkse dotatie aan de wettelijke reserve of van enigerlei beloning of toekenning.

##### Art. 251

De uit de herschatting van outillage of ermee gelijkgestelde nijverheidsgebouwen voortvloeiende meerwaarde is vrijgesteld van belasting onder de voorwaarden bepaald in artikel 190 van het Wetboek van de inkomstenbelastingen 1992.  Evenwel kunnen, bij vervreemding van overeenkomstig de artikelen 236 tot 250 van dit besluit herschatte activa, op aanvraag van de belastingplichtige of indien hij in gebreke blijft de nodige verduidelijkingen te verstrekken, voor de toepassing van artikel 44, § 1, van hetzelfde Wetboek, beschouwd worden als verkregen of tot stand gebracht op de normale datum van afsluiting van de laatste jaarbalans opgemaakt voor 31 december 1946 en voor een prijs gelijk aan de herschatte waarde.

##### Art. 252

De herschatting van outillage en ermee gelijkgestelde nijverheidsgebouwen mag voor de berekening van de afschrijving slechts in aanmerking komen indien de belastingplichtige sedert de verkrijging van de voorwerpen die voor herschatting in aanmerking komen, regelmatig boekhoudt overeenkomstig het Wetboek van Koophandel.  Mits bewijskrachtige bescheiden worden voorgelegd, zoals die welke gediend hebben voor de definitieve vaststelling van de opeisings- of herstelvergoedingen, is deze voorwaarde echter niet gesteld voor de toepassing van artikel 251 en van dit artikel met betrekking tot activa die in eigendom zijn opgeëist, of ingevolge oorlogsfeiten zijn vernield, verloren of buiten gebruik gesteld.

##### Art. 253

Het koninklijk besluit van 12 oktober 1930, tot berekening van de afschrijvingen op een herschatte kostprijs inzake inkomstenbelastingen blijft van toepassing voor het vaststellen van de vrij van belasting aanvaardbare afschrijving op outillage en ermee gelijkgestelde nijverheidsgebouwen waarvan de kostprijs, herschat overeenkomstig het bepaalde in dat besluit en opgenomen in de balansen afgesloten sedert 1931, niet opnieuw herschat is overeenkomstig de artikelen 235 tot 252.

Bijlagen.

##### Art. N1 . BIJLAGE I. (Afdeling I. - Maandelijkse referteïndexen voor hypothecaire leningen, toegestaan vanaf 1 januari 1995, waarin een veranderlijke rentevoet is bedongen. (Koninklijk besluit tot uitvoering van het Wetboek van de inkomstenbelastingen 1992, artikel 18, § 3, 1, b, 3e lid).

----------------- ------------ --------- --------- --------- --------- --------

Juli 1994 30.07.1994 5,979 6,295 6,600 6,937 7,165

Augustus 1994 31.08.1994 5,958 6,564 6,849 7,125 7,299

September 1994 30.09.1994 6,293 6,897 7,225 7,476 7,612

Oktober 1994 29.10.1994 6,391 7,207 7,599 7,849 7,960

November 1994 30.11.1994 6,068 7,177 7,577 7,850 7,941

December 1994 31.12.1994 5,989 7,055 7,369 7,675 7,773

[Januari 1995 31.01.1995 6,153 7,102 7,360 7,681 7,808

Februari 1995 28.02.1995 6,234 7,141 7,409 7,725 7,868

Maart 1995 31.03.1995 6,454 7,143 7,417 7,660 7,793

April 1995 29.04.1995 6,210 6,976 7,242 7,413 7,565

Mei 1995 31.05.1995 6,047 6,620 6,891 7,067 7,257

Juni 1995 30.06.1995 5,533 6,073 6,350 6,580 6,811

Juli 1995 29.07.1995 5,057 5,650 5,931 6,220 6,543

Augustus 1995 31.08.1995 4,826 5,442 5,762 6,062 6,467

September 1995 30.09.1995 4,629 5,159 5,523 5,827 6,273

Oktober 1995 31.10.1995 4,460 4,881 5,259 5,599 6,109

November 1995 30.11.1995 4,345 4,674 5,110 5,440 5,958

December 1995 31.12.1995 4,076 4,452 5,008 5,316 5,744]

<KB 1996-03-06/3 4, art. 4, 0 27; Inwerkingtreding : 01-01-199 5>

[januari 1996 31.01.1996 3,782 4,186 4,790 5,152 5,544

februari 1996 29.02.1996 3,486 3,921 4,534 4,977 5,347

maart 1996 30.03.1996 3,334 4,003 4,643 5,148 5,445

april 1996 30.04.1996 3,356 4,159 4,821 5,383 5,644

mei 1996 31.05.1996 3,306 3,990 4,662 5,257 5,540

juni 1996 29.06.1996 3,266 3,849 4,517 5,130 5,412

juli 1996 31.07.1996 4,439 4,057 4,657 5,295 5,544

augustus 1996 31.08.1996 3,578 4,203 4,703 5,370 5,612

september 1996 28.09.1996 3,480 4,020 4,489 5,185 5,442

oktober 1996 31.10.1996 3,262 3,695 4,164 4,899 5,151

november 1996 30.11.1996 3,157 3,557 3,944 4,669 4,905

december 1996 31.12.1996 3,153 3,597 3,940 4,549 4,770]

<KB 1997-03-17/3 1, art. 2, 0 36; Inwerkingtreding : 01-01-199 6>

[januari 1997 31.01.1997 3,151 3,552 3,969 4,465 4,790

februari 1997 28.02.1997 3,115 3,454 3,937 4,347 4,795

maart 1997 29.03.1997 3,200 3,530 3,984 4,308 4,719

april 1997 30.04.1998 3,394 3,745 4,194 4,497 4,871

mei 1997 31.05.1997 3,420 3,770 4,252 4,563 4,952

juni 1997 28.06.1997 3,378 3,682 4,155 4,464 4,682

juli 1997 31.07.1997 3,376 3,619 4,108 4,382 4,752

augustus 1997 30.08.1997 3,478 3,689 4,180 4,384 4,705

september 1997 30.09.1997 3,697 3,908 4,370 4,538 4,824

oktober 1997 31.10.1997 3,866 4,083 4,523 4,667 4,930

err. 5.11.1997

november 1997 29.11.1997 4,074 4,326 4,734 4,846 5,094

december 1997 31.12.1997 4,169 4,478 4,808 4,912 5,158]

<KB 1998-06-02/3 4, art. 2, 0 36; Inwerkingtreding : 0 1-01-1997 >

[januari 1998 31.01.1998 4,019 4,348 4,602 4,758 4,957

februari 1998 28.02.1998 3,821 4,150 4,371 4,602 4,733

juni 1998 30.06.1998 3,932 4,197 4,371 4,557 4,636

juli 1998 31.07.1998 3,891 4,129 4,279 4,448 4,535

augustus 1998 29.08.1998 3,849 4,069 4,183 4,334 4,424

september 1998 30.09.1998 3,729 3,858 3,943 4,073 4,159

october 1998 31.10.1998 3,569 3,610 3,674 3,802 3,884

november 1998 28.11.1998 3,478 3,512 3,568 3,732 3,840

december 1998 31.12.1998 3,391 3,416 3,465 3,645 3,800]

<KB 1999-04-21/36 , art. 2, 05 2; Inwerkingtreding : 01 -01-1998>

Gewijzigd bij :

<KB 2000-04-25/32 , art. 2, Inwerkingtreding : 01-01- 1999; wijzigingen niet opgenomen om  technische redenen, zie B.St. 09-05-20 00, p. 14 431>

<KB 2001-03-16/38 , art. 2, Inwerkingtreding : 01-01-2 000 ; wijzigingen niet opgenomen om  technische redene , zie B.St. 10-04-20 01, p. 11 931 en p. 11932>

<KB 2002-03-08/33 , art. 2, Inwerkingtreding : 01-01- 2001; wijzigingen niet opgenomen om  technische redenen, zie B.St. 19-03-20 02, p. 11 574>

<KB 2003-02-21/36 , art. 2, Inwerkingtreding : 01-01- 2002; wijzigingen niet opgenomen om  technische redenen, zie B.St. 06-03-20 03, p. 11 050>

(Afdeling II. -) Maandelijks lastenpercentage voor niet-hypothecaire leningen gesloten tijdens de jaren 1981 tot 1984 met een vaste looptijd van meer dan 60 maanden. (Koninklijk besluit tot uitvoering van het Wetboek van de inkomstenbelastingen 1992, artikel 18, § 3, 1, c, 1°) <KB 1996-03-06/34, art. 4, 027; Inwerkingtreding : 01-01- 1995>

[ Bedrag van de lening Jaar waarin de leningsovereenkomst is gesloten

-------------------- ------------- -------------- -------------

1981 1982 1983 en 1984

------------- -------------- -------------

Tot 123,95 EUR 1,05 1,19 1,16

van 123,96 EUR tot 371,84 EUR 1,03 1,17 1,16

van 371,85 EUR tot 619,73 EUR 0,96 1,10 1,08

van 619,74 EUR tot 1239,47 EUR 0,92 1,06 1,05

van 1239,48 EUR tot 2478,94 EUR 0,88 1,02 1,01

van 2478,75 EUR tot 3718,40 EUR 0,86 1,00 0,99

van 3718,41 EUR tot 5577,60 EUR 0,84 0,98 0,97

van 5577,61 EUR tot 7436,81 EUR 0,83 0,97 0,96

van 7436,82 EUR tot 9915,74 EUR 0,82 0,96 0,95

van 9915,75 EUR tot 14873,61 EUR 0,81 0,95 0,94

meer dan 14873,61 EUR 0,81 0,95 0,93 ]

<KB 2001-07-13/52, art. 6, 083 ; Inwerkingtreding : 01-01-2 002>

(Afdeling III. - Forfaitair geraamd voordeel van alle aard voortvloeiend uit het persoonlijk gebruik van een kosteloos ter beschikking gesteld voertuig (artikel 18, § 3, punt 9, eerste lid, KB/WIB 92).) <KB 1998-12-07/36, art. 2, 046; Inwerkingtreding : 01-01-1997>

Belastbare kracht in PK Voordeel in EUR p er afgelegde kilometer

- -

Basisbedrag Geindexeerd bedrag

(1) (2) (3)

7 0,1980 0,2186

8 0,2160 0,2385

9 0,2350 0,2595

10 0,2600 0,2871

11 0,2850 0,3147

12 0,3020 0,3334

13 0,3210 0,3544

14 0,3330 0,3677

15 0,3470 0,3831

16 0,3570 0,3942

17 0,3640 0,4019

18 0,3730 0,4118

19 en meer 0,3800 0,4196

12 0,3020 0,3269

13 0,3210 0,3475

14 0,3330 0,3604

15 0,3470 0,3756

16 0,3570 0,3864

17 0,3640 0,3940

18 0,3730 0,4037

19 en meer 0,3800 0,4113]

<KB 2002-03-04/32, art. 1, 0 86; Inwerkingtreding : 01-01-2 002>

<KB 2003-02-28/31, art. 1, 092; Inwerkingtreding : 01-01-2003>

##### Art. N2 . BIJLAGE II. Lijst van activa (die bedoeld zijn in artikel 69, § 1, eerste lid, 2°,) van het Wetboek van de inkomstenbelastingen 1992 en die dienen voor een rationeler energieverbruik, de verbetering van de industriële processen uit energetische overwegingen en de terugwinning van energie in de industrie. (Koninklijk besluit tot uitvoering van het Wetboek van de inkomstenbelastingen 1992, artikel 49) <KB 2000-09-21/33, art. 6, 068; Inwerkingtreding : 01-01-1999>

##### Art. 1N2 . Categorie 1. - Doelmatiger isolatie van gebouwen opgericht voor 1 januari 1980.  De volgende investeringen komen in aanmerking, mits materialen worden gebruikt waarvan de warmtegeleidbaarheid volgens de Belgische normen NBN van de reeks B 62 of volgens bijzondere Belgische normen of dito technische goedkeuringen, kleiner is dan of gelijk is aan 0,080 watt per meter en per Kelvin :  a) opspuiten van spouwmuren met isolatiemateriaal;  b) isoleren van buitenmuren, van buitendeuren en -poorten, van schuine of platte daken, van vloeren en muren die de scheiding vormen tussen een verwarmd en niet-verwarmd vertrek of van vloeren die de scheiding vormen tussen een verwarmd vertrek en de buitenlucht, met materiaal waarvan de thermische weerstand groter is dan of gelijk is aan 1,2 vierkante meter Kelvin per watt, evenals het aanbrengen van de nodige bescherming of van een bekleding om het isolatiemateriaal tegen het binnendringen van stof, lucht of waterdamp te beschermen, materiaal en loonkosten voor afwerking en versiering niet inbegrepen;  c) vervangen van enkel vensterglas door dubbel of drievoudig vensterglas waarvan de warmtetransmissiecoëfficiënt k kleiner is dan of gelijk is aan 3,2 watt per vierkante meter en per Kelvin, evenals het aanpassen van de ramen of het vervangen ervan door houten of kunststoframen of door aluminiumramen met thermische onderbreking;  d) plaatsen van voorzetramen in onbuigzaam materiaal met toebehoren.

##### Art. 4N2 . Categorie 4. - Beperking van energieverlies door in gebruik zijnde apparaten, leidingen, afsluiters en kanalen te isoleren of in gebruik zijnde warme of koude vloeistofbaden af te dekken.  Alleen investeringen komen in aanmerking waarbij isolatiemateriaal is gebruikt waarvan de warmtegeleidbaarheid volgens de Belgische normen NBN van de reeks B 62 of volgens bijzondere Belgische normen of dito technische goedkeuringen, kleiner is dan of gelijk is aan 0,080 watt per meter en per Kelvin.

##### Art. 5N2 . Categorie 5. - Beperking van energieverlies in bestaande ovens.  Alleen investeringen voor het binnenin bijkomend isoleren van de ovens komen in aanmerking, waarbij het vervangen van vuurvaste bekleding als energiebesparend wordt geteld in verhouding tot de erdoor bekomen vermindering van warmteverlies.

##### Art. 6N2 . Categorie 6. - Beperking van ventilatieverlies in gebouwen opgericht voor 1 januari 1980.  De volgende investeringen komen in aanmerking :  a) aanbrengen van tochtsluizen, tochtgordijnen of automatisch sluitende deuren en poorten tussen de binnen- en buitenkant van het gebouw;  b) aanbrengen van automatisch sluitende deuren tussen bestaande koel- of diepvrieskamers en de rest van het gebouw.

##### Art. 7N2 . Categorie 7. - Terugwinnen van afvalwarmte.  De volgende investeringen komen in aanmerking wanneer zij het, in een bestaand systeem voor het bedrijf mogelijk maken eigen afvalwarmte op te vangen en aan derden te leveren of afvalwarmte van derden op te vangen :  a) plaatsen van geïsoleerde leidingen en circulatiepompen voor het transport van de teruggewonnen warmte;  b) plaatsen van geïsoleerde opslagvaten die uitsluitend dienen voor het tijdelijk opslaan van de teruggewonnen warmte;  c) plaatsen van warmtewisselaars voor warmterecuperatie, toestellen om teruggewonnen warmte rechtstreeks aan te wenden niet inbegrepen.

##### Art. 8N2 . Categorie 8. - Terugwinnen van afvalwarmte van in gebruik zijnde produktie- of klimaatregelingsapparatuur.  De volgende investeringen, andere dan het plaatsen van warmterecuperatoren van krachtopwekkingsinstallaties met stoom die een onderdeel vormen van de krachtopwekkingscyclus, komen in aanmerking wanneer zij niet nodig zijn voor het produktie- of klimaatregelingsproces :  a) plaatsen van warmtewisselaars die nodig zijn om afvalwarmte terug te winnen, toestellen om teruggewonnen warmte rechtstreeks aan te wenden niet inbegrepen;  b) aanbrengen van apparatuur voor :  - het opnieuw in circulatie brengen van afvallucht of -vloeistof;  - het terugwinnen van condensaat;  c) plaatsen van :  - naverdampingsvaten voor condensaat of spuiwater;  - geïsoleerde opslagvaten die uitsluitend dienen voor het tijdelijk opslaan van teruggewonnen warmte;  - geïsoleerde leidingen voor het transport van teruggewonnen warmte;  - warmtepompen.

##### Art. 9N2 . Categorie 9. - Rendementsverhoging van in gebruik zijnde verbrandingsapparatuur.  De volgende investeringen komen in aanmerking :  a) aanbrengen van automatische brandstof- en luchtregelingen werkend op basis van de in de rookgassen gemeten O2 - of CO2 -concentraties of met behulp van een opacimeter;  b) vervangen van atmosferische branders en van branders met ventilatoren door recuperatieve branders;  c) plaatsen of verbeteren van schakel-, meet- of regelapparatuur.

##### Art. 12N2 . Categorie 12. - Opvangen van directe of diffuse zonnestraling.  Als investeringen komen in aanmerking, mits zij uitsluitend voor het opvangen van die zonnestraling dienen, het plaatsen van :  a) zonnecollectoren;  b) geïsoleerde opslagvaten, met inbegrip van de warmtewisselaars;  c) circulatiepompen in de collectorkringlopen;  d) beveiligingsapparatuur tegen bevriezing of oververhitting;  e) apparatuur die met een fotovoltaïsch systeem zorgt voor rechtstreekse produktie van elektriciteit, met name :  - foto-voltaïsche cellen;  - spanningsregelaars;  - ondulators en gelijkrichters;  - batterijen voor het opslaan van de geproduceerde elektrische energie;  - elektrotechnische uitrusting voor aansluiting op het interne elektriciteitsnet.

##### Art. 13N2 . Categorie 13. - Aanwenden van windenergie.  Als investeringen komen in aanmerking, het plaatsen van :  a) windturbines;  b) spanningsregelaars;  c) ondulators en gelijkrichters:  d) batterijen voor het opslaan van de geproduceerde energie;  e) generatoren en elektrotechnische uitrusting voor aansluiting op het interne elektriciteitsnet.

##### Art. 14N2 . Categorie 14. - Waterkrachtcentrales om energie voort te brengen met een vermogen van maximum 1 MW.  Als investeringen komen in aanmerking het plaatsen, de nodige infrastructuurwerken daarin niet begrepen, van :  a) turbines;  b) spanningregelaars;  c) ondulators en gelijkrichters;  d) generatoren en elektrotechnische uitrusting voor de aansluiting op het interne elektriciteitsnet.

##### Art. 17N2 . Categorie 17. - Aanwenden van gassen ontstaan uit anaërobe fermentatie van afval.  In aanmerking komen, de investeringen in :  a) uitrusting, binnen de inrichting, voor voorbewerking, opslag en transport van het afval;  b) fermentatietanks, met inbegrip van materiaal en apparatuur om ze te isoleren en te verwarmen;  c) gasopslagtanks;  d) ketels, of het ombouwen ervan, om het gebruik van biogas mogelijk te maken;  e) meet- of regelapparatuur;  f) krachtwerktuigen om biogas te verbranden.

##### Art. 18N2 . Categorie 18. - Energiebesparend vervoer.  In aanmerking komen, de investeringen, binnen de inrichting, in nieuwe los- en laadinrichtingen voor vervoer via spoor- of waterweg of in nieuwe uitrustingen voor aansluiting op het spoorwegnet.

##### Art. 19N2 . Categorie 19. - Verbetering van het energetisch rendement van in gebruik zijnde installaties.  Als investeringen komen in aanmerking, het aanbrengen of verbeteren, uitsluitend met het oog op een betere controle van het energetisch rendement, van meet- en regelapparatuur.

##### Art. 20N2 . Categorie 20. - Verbetering van het energetisch rendement van bestaande verdampings- of distilliatietoestellen en stoomdistributienetten gebruikt bij produktieprocessen.  In aanmerking komen, de investeringen :  - in apparatuur voor thermocompressie of mechanische recompressie van stoom;  - om het aantal verdampingstrappen te verhogen;  - om in de distillatie-installaties het aantal droogplaten te verhogen of het refluxgehalte te verminderen;  - om meet- of regelapparatuur te plaatsen of te verbeteren.

##### Art. 21N2 . Categorie 21. - Verbetering van het energetisch rendement van bestaande droogtoestellen gebruikt bij produktieprocessen.  In aanmerking komen, de investeringen om :  - systemen van indirect drogen te vervangen door systemen van direct drogen;  - systemen voor mechanische voordroging toe te voegen;  - de hoeveelheid drooglucht te regelen door het meten van de relatieve vochtigheid;  - meet- en regelapparatuur te plaatsen of te verbeteren.

##### Art. 22N2 . Categorie 22. - Verbetering van het energetisch rendement van bestaande koel-, pasteurisatie- of sterilisatietoestellen gebruikt bij produktieprocessen.  In aanmerking komen, de investeringen om :  - meet- en regelapparatuur te plaatsen of te verbeteren;  - toestellen te plaatsen waarmee omgekeerde osmose kan gerealiseerd worden.

##### Art. 23N2 . Categorie 23. - Verbetering van het rendement van bestaande toestellen van elektrochemische of elektrometallurgische aard gebruikt bij produktieprocessen.  In aanmerking komen, de investeringen om :  - nieuwe types van elektroden of membranen te plaatsen;  - meet- en regelapparatuur te plaatsen.

##### Art. 24N2 . Categorie 24. - Energiebesparing bij vacuümpompen.  In aanmerking komen de investeringen om vacuümstoomstraalpompen door vacuümpompen te vervangen.

##### Art. 25N2 . Categorie 25. - Regeling van de aandrijving van machines.  In aanmerking komen, de investeringen voor het toevoegen van elektronische toerentalregelaars en van systemen voor automatisch stoppen waardoor nullastwerking van draaiende machines wordt vermeden.

##### Art. 1N4 . Tabel 1. Directie Antwerpen I.

Benaming van de commissie Ambtsgebied van de commissie

Antwerpen Antwerpen

Sint-Niklaas Beveren, Hamme, Kruibeke, Sint-Gillis-Waas,

Sint-Niklaas, Stekene, Temse, Waasmunster en

Zwijndrecht

##### Art. 2N4 . Tabel 2. Directie Antwerpen II.

Benaming Ambtsgebied

Boom Aartselaar, Boechout, Boom, Bornem, Borsbeek,

Edegem, Hemiksem, Hove, Kontich, Lint,

Mortsel, Niel, Puurs, Rumst, Schelle,

Schilde, Sint-Amands, Wijnegem, Willebroek

en Wommelgem

Herentals Balen, Beerse, Dessel, Geel, Herentals,

Herenthout, Herselt, Laakdal, Lille, Malle,

Meerhout, Mol, Olen, Schoten, Vorselaar,

Westerlo en Zoersel

Mechelen Berlaar, Bonheiden, Duffel, Grobbendonk,

Heist-op-den-Berg, Hulshout, Lier, Mechelen,

Nijlen, Putte, Ranst, Sint-Katelijne-Waver

en Zandhoven

Turnhout Arendonk, Baarle-Hertog, Brasschaat, Brecht,

Essen, Hoogstraten, Kalmthout, Kapellen,

Kasterlee, Merksplas, Oud-Turnhout, Ravels,

Retie, Rijkevorsel, Stabroek, Turnhout,

Vosselaar en Wuustwezel

##### Art. 3N4 . Tabel 3. Directie Brussel I.

Benaming van de commissie Ambtsgebied van de commissie

Brussel Brussel

Elsene Elsene

Vorst Etterbeek, Sint-Gillis en Vorst

Ukkel Ukkel

##### Art. 4N4 . Tabel 4. Directie Brussel II.

Benaming Ambtsgebied

Schaarbeek Evere, Schaarbeek en Sint-Joost-ten-Node

Sint-Agatha-Berchem, Sint-Genesius-Rode,

Wemmel en Wezembeek-Oppem

Sint-Jans-Molenbeek Anderlecht en Sint-Jans-Molenbeek

Woluwe Oudergem, Sint-Lambrechts-Woluwe,

Sint-Pieters-Woluwe en Watermaal-Bosvoorde

##### Art. 5N4 . Tabel 5. Directie Leuven.

Benaming Ambtsgebied

Halle Beersel, Dilbeek, Galmaarden, Gooik, Halle,

Herne, Lennik, Pepingen, Roosdaal en

Sint-Pieters-Leeuw

Leuven Bertem, Boortmeerbeek, Haacht, Hoeilaart,

Huldenberg, Kampenhout, Keerbergen, Leuven,

Overijse en Tervuren

Tienen Aarschot, Begijnendijk, Bekkevoort, Bierbeek,

Boutersem, Diest, Geetbets, Glabbeek,

Herent, Hoegaarden, Holsbeek, Kortenaken,

Landen, Linter, Lubbeek, Oud-Heverlee,

Rotselaar, Scherpenheuvel-Zichem,

Tielt-Winge, Tienen, Tremelo en Zoutleeuw

Vilvoorde Affligem, Asse, Grimbergen,

Kapelle-op-den-Bos, Kortenberg, Liedekerke,

Londerzeel, Machelen, eise, Merchtem,

Opwijk, Steenokkerzeel, Ternat, Vilvoorde,

Zaventem en Zemst

##### Art. 6N4 . Tabel 6. Directie Brugge.

Benaming Ambtsgebied

Brugge Beernem, Brugge, Damme, Jabbeke, Oostkamp,

Zedelgem en Zuienkerke

Ieper Alveringem, Heuvelland, Hooglede, Ieper,

Langemark-Poelkapelle, Menen, Mesen,

Moorslede, Poperinge, Vleteren, Wervik,

Wevelgem en Zonnebeke

Kortrijk Anzegem, Avelgem, Deerlijk, Kortrijk, Kuurne,

Ledegem, Spiere-Helkijn, Waregem en

Zwevegem

Oostende Bredene, Gistel, Middelkerke, Oostende en

Commissie I Oudenburg

Oostende Blankenberge, De Haan, De Panne, Diksmuide,

Commissie II Houthulst, Ichtegem, Knokke-Heist,

Koekelare, Koksijde, Kortemark, Lichtervelde,

Lo-Reninge, Nieuwpoort, Torhout en Veurne

Staden, Tielt, Wielsbeke en Wingene

##### Art. 7N4 . Tabel 7. Directie Gent.

Benaming Ambtsgebied

Aalst Aalst, Denderleeuw, Erpe-Mere, Haaltert en

Ninove

Dendermonde Berlare, Buggenhout, Dendermonde, Laarne,

Lebbeke, Lede, Lokeren, Melle, Merelbeke,

Wetteren, Wichelen en Zele

Gent Gent

Commissie I

Gent Aalter, Assenede, De Pinte, Destelbergen,

Commissie II Eeklo, Evergem, Kaprijke, Knesselare,

Lochristi, Lovendegem, Maldegem, Moerbeke,

Nazareth, Nevele, Sint-Laureins,

Sint-Martens-Latem, Waarschoot, Wachtebeke,

Zelzate en Zomergem

Oudenaarde Brakel, Deinze, Gavere, Geraardsbergen,

Herzele, Horebeke, Kluisbergen,

Kruishoutem, Lierde, Maarkedal, Oosterzele,

Oudenaarde, Ronse, Sint-Lievens-Houtem,

Wortegem-Petegem, Zingem, Zottegem, Zulte

en Zwalm

##### Art. 8N4 . Tabel 8. Directie Charleroi.

Benaming Ambtsgebied

Charleroi Anderlues, Beaumont, Binche,

Commissie I Chapelle-lez-Herlaimont, Charleroi, Chimay,

Erquelinnes, Estinnes, Fontaine-l'Eveque,

Froidchapelle, Gerpinnes,

Ham-sur-Heure-Nalinnes, Lobbes,

Merbes-le-Chateau, Momignies,

Montigny-le-Tilleul, Morlanwelz, Sivry-Rance

en Thuin

Charleroi Aiseau-Presles, Chatelet, Courcelles,

Commissie II Farciennes, Fleurus, Les Bons Villers en

Pont-a-Celles

La Louviere La Louviere, Le Roeulx, Manage en Seneffe

##### Art. 9N4 . Tabel 9. Directie Bergen.

Elzele, Hensies, Honnelles, Jurbeke, Lens,

Lessen, Opzullik, Peruwelz, Quievrain,

Saint-Ghislain en Vloesberg

Bergen Bergen, Boussu, Ecaussinnes, Frameries,

Quaregnon, Quevy, 's-Gravenbrakel en Zinnik

Doornik Antoing, Brunehaut, Celles, Doornik,

Estaimpuis, Frasnes-lez-Anvaing,

Komen-Waasten, Leuze-en-Hainaut, Moeskroen,

Mont-de-l'Enclus, Pecq en Rumes

##### Art. 10N4 . Tabel 10. - Directie Luik.

Benaming Ambtsgebied

Hoei Amay, Anthisnes, Aywaille, Berloz, Borgworm,

Braives, Burdinne, Clavier, Comblain-au-Pont,

Crisnee, Donceel, Engis, Esneux, Faimes,

Ferrieres, Fexhe-le-Haut-Clocher,

Flemalle, Geer, Grace-Hollogne, Hamoir,

Hannuit, Heron, Hoei, Lierneux, Lincent,

Marchin, Modave, Nandrin, Neupre, Oreye,

Ouffet, Remicourt, Saint-Georges-sur-Meuse,

Saint-Nicolas, Sprimont, Stoumont, Tinlot,

Verlaine, Villers-le-Bouillet, Wanze en

Wasseiges

Luik Luik

Commissie I

Luik Ans, Awans, Beyne-Heusay, Bitsingen, Blegny,

Commissie II Chaudfontaine, Dalhem, Fleron, Herstal,

Juprelle, Olne, Oupeye, Seraing, Soumagne,

Trooz en Wezet

Sankt Vith Amel, Bullingen, Burg-Reuland, Butgenbach,

Eupen, Kelmis, Lontzen, Raeren en Sankt-Vith

Verviers Aubel, Baelen, Dison, Herve, Jalhay,

Limbourg, Malmedy, Pepinster, Plombieres,

Spa, Stavelot, Theux, Thimister-Clermont,

Trois-Ponts, Verviers, Waimes en

Welkenraedt

##### Art. 11N4 . Tabel 11. - Directie Hasselt.

Benaming Ambtsgebied

Hasselt Beringen, Bocholt, Bree, Diepenbeek, Ham,

Hamont-Achel, Hasselt, Hechtel-Eksel,

Heusden-Zolder, Houthalen-Helchteren,

Leopoldsburg, Lommel, Lummen,

Gingelom, Halen, Heers, Herk-de-Stad,

Herstappe, Hoeselt, Kinrooi, Kortessem,

Lanaken, Maaseik, Maasmechelen,

Nieuwerkerken, Opglabbeek, Riemst,

Sint-Truiden, Tongeren, Voeren, Wellen en

Zutendaal

##### Art. 12N4 . Tabel 12. - Directie Aarlen.

Benaming Ambtsgebied

Aarlen Aarlen, Attert, Aubange, Bertrix, Bouillon,

Chiny, Etalle, Florenville, Habay,

Herbeumont, Leglise, Meix-devant-Virton,

Messancy, Musson, Neufchateau, Paliseul,

Rouvroy, Saint-Leger, Tintigny en Virton

Marche-en-Famenne Bastenaken, Bertogne, Daverdisse, Durbuy,

Erezee, Fauvillers, Gouvy, Hotton,

Houffalize, La Roche-en-Ardenne, Libin,

Libramont-Chevigny, Manhay,

Marche-en-Famenne, Martelange, Nassogne,

Rendeux, Sainte-Ode, Saint-Hubert, Tellin,

Tenneville, Vaux-sur-Sure, Vielsalm en

Wellin

##### Art. 13N4 . Tabel 13. - Directie Namen.

Benaming Ambtsgebied

Namen Andenne, Anhee, Assesse, Beauraing, Bievre,

Ciney, Dinant, Eghezee, Fernelmont, Gedinne,

Gesves, Hamois, Hastiere, Havelange, Houyet,

La Bruyere, Namen, Ohey, Onhaye,

Profondeville, Rochefort, Somme-Leuze,

Vresse-sur-Semois en Yvoir

Nijvel Cerfontaine, Couvin, Doische, Eigenbrakel,

Floreffe, Florennes, Fosses-la-Ville,

Genepien, Ittre, Kasteelbrakel, Mettet,

Nijvel, Philippeville, Rebecq, Tubeke,

Viroinval, Walcourt en Waterloo

Waver Bevekom, Chastre, Chaumont-Gistoux,

Court-Saint-Etienne, Geldenaken, Gembloux,

Graven, Helecine, Incourt,

Jemeppe-sur-Sambre, Lasne,

Mont-Saint-Guibert, Orp-Jauche,

Ottignies-Louvain-la-Neuve, Perwijs,

Ramillies, Rixensart, Sambreville,

##### Art. N5 . BIJLAGE V. Rentevoeten die in aanmerking komen voor de vaststelling van de als beroepskosten aftrekbare interesten van obligaties, leningen, schulden, deposito's en andere effecten ter vertegenwoordiging van leningen. (Koninklijk besluit tot uitvoering van het Wetboek van de inkomstenbelastingen 1992, artikel 29)  (Opgeheven) <KB 1993-10-22/33, art. 15; ED 01-01-1992; Voor de tekst, zie B.St. 13-09-1993, p. 20280- 20285>

OVEREENSTEMMINGSTABELLEN.

##### Art. N6 . DEEL I. KB/WIB en andere bepalingen -- KB/WIB 92.

Artikel KB/WIB Artikel KB/WIB 92

1 1

1bis 3

2 4

3 5

3bis 2

4 22

5 23

6 24

7 25

8 26

9 27

9bis --

9ter --

9quater 18

10 19

11 20

12 21

12bis 44

12ter 45

12quater 46

12quinquies --

12sexies 47

12septies 49

12octies 48

12novies --

13 6

13bis 7

13ter 8

13quater 9

13quinquies 10

13sexies 11

13septies --

14 17

14bis 30

14ter 31

14quater 32

14quinquies 33

14sexies --

18 238

19 239

20 240

21 241

22 242

23 243

24 244

25 245

26 246

27 247

28 248

29 249

30 250

31 251

32 252

33 253

33bis --

33ter --

33quater --

33quinquies 34

33sexies 35

34 36

35 37

36 38

37 39

38 40

39 41

40 42

41 43

42 29

43 28

44 50

45 51

46 52

47 53

47bis 54

47ter 57

47quater 59

47quinquies 58

47quinquies/1 60

47sexies 55

47septies 62

47octies 56

47novies 63

48 --

48bis 64

49 65

49bis 66

49ter --

53 70

54 71

55 72

56 --

57 73

57bis --

58 --

59 --

60 --

61 --

62 --

63 --

64 --

64bis --

64ter 12

64quater 13

64quinquies 14

64sexies 15

64septies 16

64octies --

65 74

66 75

67 76

68 77

69 78

69bis 79

70 --

71 102

72 103

73 104

74 80

75 81

76 82

77 --

78 --

79 96

80 97

81 98

82 99

83 100

84 --

85 --

86 101

87 105

88 106

89 107

89bis 108

90 109

91 110

93 112

94 113

95 114

96 115

96bis 116

97 117

97bis 118

97ter 119

98 83

99 84

100 85

101 --

102 --

103 --

104 --

105 --

106 --

107 --

108 --

109 --

110 --

111 --

112 86

113 87

114 88

115 89

116 90

116bis --

117 91

118 92

119 93

120 94

121 --

122 --

123 --

124 95

125 120

126 --

127 --

128 --

129 --

130 --

131 --

132 121

133 122

134 --

135 --

136 --

137 123

141 125

142 126

143 127

144 178

145 --

145bis 179

146 182

147 183

148 184

149 185

150 186

151 187

152 188

153 189

154 190

155 191

156 192

157 193

158 194

159 195

160 196

161 197

162 198

163 199

164 200

164bis 201

165 202

166 203

167 204

168 205

169 --

170 206

170bis 177

171 128

172 129

173 130

174 131

175 132

176 133

177 134

178 135

179 --

180 136

181 137

182 138

183 139

184 140

185 141

186 142

190 --

191 --

192 --

193 --

194 145

195 146

196 147

197 148

198 149

199 150

200 151

201 152

202 153

203 154

204 --

205 155

206 156

207 157

208 158

209 159

210 160

211 161

212 162

213 163

214 --

215 164

216 165

217 --

217bis 166

218 167

219 --

220 168

221 169

222 170

223 171

224 172

225 173

226 174

227 175

227bis 207

227ter 208

227quater 209

227quinquies 210

228 211

229 212

230 213

231 214

232 215

237 220

237bis 221

237ter 222

237quater 223

237quinquies 224

238 176

238bis 225

238ter 226

238quater 227

238quinquies 228

238sexies 229

239 230

240 231

241 232

242 233

243 --

244 --

245 --

246 --

247 --

247bis 234

247ter --

247quater --

247quinquies --

247sexies --

247septies --

247octies --

247nonies --

248 --

249 --

250 --

Bijlage KB/WIB Bijlage KB/WIB 92

I ---

II V

III III

IV ---

V IV

VI I

VII ---

VIII ---

IX ---

X II

KB 6.2.1989, art. 1 180

KB 6.2.1989, art. 2 181

##### Art. N7. DEEL II. KB/WIB 92 -- KB/WIB en andere bepalingen.

KB/WIB 92 KB/WIB Andere bepalingen

1 1

2 3bis

3 1bis

4 2

5 3

6 13

7 13bis

8 13ter

9 13quater

10 13quinquies

11 13sexies

12 64ter

13 64quater

14 64quinquies

15 64sexies

16 64septies

17 14

18 9quater

19 10

20 11

21 12

22 4

23 5

24 6

25 7

26 8

27 9

28 43

29 42

30 14bis

31 14ter

32 14quater

33 14quinquies

34 33quinquies

35 33sexies

36 34

37 35

38 36

39 37

40 38

41 39

45 12ter

46 12quater

47 12sexies

48 12octies KB 17.4.1990

49 12septies

50 44

51 45

52 46

53 47

54 47bis

55 47sexies

56 47octies

57 47ter

58 47quinquies

59 47quater

60 47quinquies/1

61 KB 17.1.1989, art. 1

62 47septies

63 47novies

64 48bis

65 49

66 49bis

67 50

68 51

69 52

70 53

71 54

72 55

73 57

74 65

75 66

76 67

77 68

78 69

79 69bis

80 74

81 75

82 76

83 98

84 99

85 100

86 112

87 113

88 114

89 115

90 116

91 117

92 118

93 119

97 80

98 81

99 82

100 83

101 86

102 71

103 72

104 73

105 87

106 88

107 89

108 89bis

109 90

110 91

111 92

112 93

113 94

114 95

115 96

116 96bis

117 97

118 97bis

119 97ter

120 125

121 132

122 133

123 137

124 138

125 141

126 142

127 143

128 171

129 172

130 173

131 174

132 175

133 176

134 177

135 178

136 180

137 181

138 182

139 183

140 184

141 185

142 186

143 187

144 188

145 194

149 198

150 199

151 200

152 201

153 202

154 203

155 205

156 206

157 207

158 208

159 209

160 210

161 211

162 212

163 213

164 215

165 216

166 217bis

167 218

168 220

169 221

170 222

171 223

172 224

173 225

174 226

175 227

176 238

177 170bis

178 144

179 145bis

180 KB 6.2.1989, art. 1

181 KB 6.2.1989, art. 2

182 146

183 147

184 148

185 149

186 150

187 151

188 152

189 153

190 154

191 155

192 156

193 157

194 158

195 159

196 160

200 164

201 164bis

202 165

203 166

204 167

205 168

206 170

207 227bis

208 227ter

209 227quater

210 227quinquies

211 228

212 229

213 230

214 231

215 232

216 233

217 234

218 235

219 236

220 237

221 237bis

222 237ter

223 237quater

224 237quinquies

225 238bis

226 238ter

227 238quater

228 238quinquies

229 238sexies

230 239

231 240

232 241

233 242

234 247bis

235 15

236 16

237 17

238 18

239 19

240 20

241 21

242 22

243 23

244 24

245 25

246 26

247 27

251 31

252 32

253 33

Bijlage KB/WIB 92 Bijlage KB/WIB

I VI

II X

III III

IV V

V II
