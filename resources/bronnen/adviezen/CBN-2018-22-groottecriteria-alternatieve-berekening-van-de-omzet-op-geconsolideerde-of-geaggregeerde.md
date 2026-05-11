---
bron: https://www.cbn-cnc.be/nl/adviezen/groottecriteria-alternatieve-berekening-van-de-omzet-op-geconsolideerde-of-geaggregeerde
datum: 2018-12-03
gerelateerde_adviezen:
  - datum: '2024-09-19'
    titel: Gevolgen verhoging groottecriteria voor (I)VZW’s en stichtingen
    url: https://www.cbn-cnc.be/nl/adviezen/gevolgen-verhoging-groottecriteria-voor-ivzws-en-stichtingen
  - datum: '2022-03-15'
    titel: Beoordeling van de groottecriteria overeenkomstig artikelen 1:24 en 1:25 van het Wetboek van vennootschappen en verenigingen
    url: https://www.cbn-cnc.be/nl/adviezen/beoordeling-van-de-groottecriteria-overeenkomstig-artikelen-124-en-125-van-het-wetboek-van
  - datum: '2017-04-19'
    titel: Groottecriteria artikel 15 W.Venn. – Verbonden vennootschappen – Verschillende afsluitingsdata - Wijziging van consolidatiekring
    url: https://www.cbn-cnc.be/nl/adviezen/groottecriteria-artikel-15-wvenn-verbonden-vennootschappen-verschillende-afsluitingsdata
  - datum: '2017-02-01'
    titel: Groottecriteria – Boekjaar korter of langer dan 12 maanden (update)
    url: https://www.cbn-cnc.be/nl/adviezen/groottecriteria-boekjaar-korter-of-langer-dan-12-maanden-update
nummer: CBN-advies 2018/22
provenance:
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/groottecriteria-alternatieve-berekening-van-de-omzet-op-geconsolideerde-of-geaggregeerde
      sha256: e8239fb06e706232d9098b2caebfc6f6cf3844c3bac3088e4d6e403cb306efac
      version:
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: 3b788cd
    model:
    prompt_version:
  generated_at: '2026-05-11T15:15:32Z'
  stale: false
  stale_reason:
  trust:
    status: needs-rework
    confirmed_at: '2026-05-11T15:23:43Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: 'Nieuw verdict (was unreviewed). E1/E2: alle voorbeeldtabellen (Voorbeeld 1–4, regels 95–640) zijn gefragmenteerd als single-cell blokken — identieke extractor-bug als CBN-2018-16/17. B5: de subsectiekopjes `### Vennootschap A: 205.000` op regels 177 en vergelijkbare regels (473, 555, 621) zijn feitelijk rekenresultaten als pseudo-heading gerenderd; en `## Geconsolideerd bedrag` op regel 268 en `## Geaggregeerde cijfers` op regels 372 en 456 dienen als tabelrij-labels maar staan als `##`-headings. B2: `## Geconsolideerd bedrag` en `## Geaggregeerde cijfers` als niveau-2-headings terwijl ze logisch sub-tabelrijen zijn.'
    layer1:
      file_size_chars: 19071
      flags: []
      heading_count: 28
      max_section_chars: 6236
      run_at: '2026-05-11T15:05:53Z'
      run_id: 20260511-150547
      status: pass
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-11T15:23:43Z'
      rationale: 'Nieuw verdict (was unreviewed). E1/E2: alle voorbeeldtabellen (Voorbeeld 1–4, regels 95–640) zijn gefragmenteerd als single-cell blokken — identieke extractor-bug als CBN-2018-16/17. B5: de subsectiekopjes `### Vennootschap A: 205.000` op regels 177 en vergelijkbare regels (473, 555, 621) zijn feitelijk rekenresultaten als pseudo-heading gerenderd; en `## Geconsolideerd bedrag` op regel 268 en `## Geaggregeerde cijfers` op regels 372 en 456 dienen als tabelrij-labels maar staan als `##`-headings. B2: `## Geconsolideerd bedrag` en `## Geaggregeerde cijfers` als niveau-2-headings terwijl ze logisch sub-tabelrijen zijn.'
      concrete_problemen:
        - regel: 95
          categorie: E1
          type: other
          voorbeeld: "| \n\n  | | \n|---|\n\n**Rekening 70[^9]** \n\n  | | \n|---|\n\n**Rekening 74[^10]**"
        - regel: 268
          categorie: B2
          type: other
          voorbeeld: '## Geconsolideerd bedrag[^19] (staat als ##-heading, is tabelrij-label)'
        - regel: 177
          categorie: B5
          type: other
          voorbeeld: '### Vennootschap A: 205.000 (d.i. 200.000 + 5.000)[^12]'
themas:
  - criteria
  - groottecriteria
  - omzet
  - berekening op geconsolideerde basis
  - berekening op geaggregeerde basis
  - geconsolideerde methode
  - geaggregeerde methode
---

# CBN-advies 2018/22 – Groottecriteria – Alternatieve berekening van de omzet op geconsolideerde of geaggregeerde basis

## Algemeen

De Commissie heeft in haar advies 2016/3 – *Beoordeling groottecriteria artikelen 15 en 15/1 W.Venn.* verduidelijkt op welke basis de groottecriteria van artikel 15 en 15/1 W.Venn. moeten worden beoordeeld. 

Na het uitbrengen van het voormelde advies heeft de Commissie de vraag gekregen op welke wijze de criteria voor een moedervennootschap moeten worden beoordeeld wanneer het bedrag van de in aanmerking te nemen omzet op een alternatieve wijze moet worden vastgesteld doordat de opbrengsten uit het gewoon bedrijf voor meer dan de helft bestaan uit opbrengsten die niet aan de omschrijving beantwoorden van de post ‘omzet’.[^2]
 De alternatieve berekeningswijze van de in aanmerking te nemen omzet luidt als volgt: 

“Wanneer de opbrengsten die voortspruiten uit het gewoon bedrijf van een vennootschap voor meer dan de helft bestaan uit opbrengsten die niet aan de omschrijving beantwoorden van de post ‘omzet’, dan moet voor de toepassing van paragraaf 1 [van artikel 15 W.Venn.] onder omzet worden verstaan: het totaal van de bedrijfs- en financiële opbrengsten met uitsluiting van de niet-recurrente opbrengsten.”
## Vrije keuze tussen de geconsolideerde en geaggregeerde methode

Voor een moedervennootschap vindt de beoordeling van de groottecriteria plaats hetzij op geconsolideerde[^3] basis, hetzij op geaggregeerde[^4] basis. De moedervennootschap heeft de vrije keuze welke[^5] van beide methodes zij hanteert voor de beoordeling van de groottecriteria.[^6]
 Indien de vennootschap verplicht is een jaarrekening op geconsolideerde basis op te maken en te publiceren kan zij er toch nog voor kiezen om, voor de beoordeling van de groottecriteria, zich te baseren op de geaggregeerde cijfers in plaats van op de geconsolideerde cijfers.

### Berekening op geconsolideerde basis

Indien de vennootschap ervoor kiest om de beoordeling van de groottecriteria toe te passen op de geconsolideerde gegevens, moet[^7] de vennootschap hiertoe de geconsolideerde cijfers vaststellen volgens de consolidatiebepalingen van het KB W.Venn., hetgeen onder meer betekent dat de weglatingen en verrekeningen vermeld in de artikelen 137, 144 en 146 KB W.Venn. worden toegepast.[^8] 

Indien, berekend op geconsolideerde basis, het totaal van de opbrengsten die voortspruiten uit het gewoon bedrijf voor meer dan de helft bestaan uit opbrengsten die *niet* beantwoorden aan de omschrijving van de post ‘omzet’, dan moet voor de beoordeling van de groottecriteria onder ‘omzet’ worden verstaan: het totaal van de geconsolideerde bedrijfs- en financiële opbrengsten met uitsluiting van de niet-recurrente opbrengsten.

### Berekening op geaggregeerde basis (+ 20%-methode)

Indien de vennootschap ervoor kiest om de beoordeling van de groottecriteria toe te passen op de *geaggregeerde gegevens*, kan zij er zich toe beperken om de cijfers van de enkelvoudige jaarrekeningen op te tellen en vervolgens de aldus bekomen bedragen te vergelijken met het grensbedrag van de maximale jaaromzet, verhoogd met 20 procent.

Indien, berekend op geaggregeerde basis, het totaal van de opbrengsten die voortspruiten uit het gewoon bedrijf voor meer dan de helft bestaan uit opbrengsten die *niet* aan de omschrijving beantwoorden van de post ‘omzet’, dan moet voor de beoordeling van de groottecriteria onder omzet worden verstaan: het totaal van de bedrijfs- en financiële opbrengsten, berekend op geaggregeerde basis, met uitsluiting van de niet-recurrente opbrengsten.

### Voorbeelden

#### Voorbeeld 1

Vennootschap C is een moedervennootschap met de vennootschappen A en B als dochtervennootschappen. De vennootschappen A en B zijn zelf geen moedervennootschappen. De opbrengstengegevens van deze drie vennootschappen zijn als volgt:
| 

  | | 
|---|

**Rekening 70[^9]** 

  | | 
|---|

**Rekening 74[^10]** 

  | | 
|---|

**Rekening 75[^11]** 

  | 
| 

**Vennootschap A**

  | | 
|---|

5.000

  | | 
|---|

200.000

  | | 
|---|

0

  | 
| 

**Vennootschap B**

  | | 
|---|

8.700.000

  | | 
|---|

1.000

  | | 
|---|

10

  | 
| 

**Vennootschap C**

  | | 
|---|

100.000

  | | 
|---|

1.500

  | | 
|---|

6.500.000

  | 

### Berekening op enkelvoudige basis

Op enkelvoudige basis is de in aanmerking te nemen omzet voor de berekening van de groottecriteria voor de betreffende vennootschappen als volgt:
### Vennootschap A: 205.000 (d.i. 200.000 + 5.000)[^12]

Vennootschap B: 8.700.000 

Vennootschap C: 6.601.500 (d.i. 100.000 + 1.500 + 6.500.000)[^13] 

De vennootschap C is echter een moedervennootschap zodat voor de bepaling van de groottecriteria de in aanmerking te nemen omzet plaatsvindt op geconsolideerde basis of op geaggregeerde basis.[^14]
### Moedervennootschap: berekening op geconsolideerde basis

In het voorbeeld wordt er hypothetisch vanuit gegaan dat de omzet van vennootschap B een intragroepsomzet omvat van 46.000 euro. Deze intragroepsomzet wordt op geconsolideerde basis niet aangemerkt als omzet.[^15]
Op geconsolideerde basis zijn de in aanmerking te nemen opbrengsten als volgt:
| 

  | | 
|---|

**Rekening 70[^16]** 

  | | 
|---|

**Rekening 74[^17]** 

  | | 
|---|

**Rekening 75[^18]** 

  | 
| 

**Vennootschap A**

  | | 
|---|

5.000

  | | 
|---|

200.000

  | | 
|---|

0

  | 
| 

**Vennootschap B**

  | | 
|---|

8.700.000

  | | 
|---|

1.000

  | | 
|---|

10

  | 
| 

**Vennootschap C**

  | | 
|---|

100.000

  | | 
|---|

1.500

  | | 
|---|

6.500.000

  | 
| 

## Geconsolideerd bedrag[^19]

  | | 
|---|

8.759.000[^20] 

  | | 
|---|

202.500

  | | 
|---|

6.500.010

  | 

Op geconsolideerde basis bedraagt de omzet 8.759.000 euro. Dit bedrag is samengesteld uit de omzet van vennootschap A (5.000) + de omzet van vennootschap B (8.700.000) + de omzet van vennootschap C (100.000), verminderd met de hogervermelde intragroepsomzet van 46.000 euro. Op geconsolideerde basis bestaan de opbrengsten die voortspruiten uit het gewoon bedrijf dus voor meer dan de helft uit opbrengsten die beantwoorden aan de omschrijving van de post omzet.
Indien het bestuursorgaan opteert voor een berekening van de groottecriteria op geconsolideerde basis (en niet op geaggregeerde basis) bedraagt, voor de beoordeling van de groottecriteria, de in aanmerking te nemen omzet 8.759.000[^21].
### Moedervennootschap: Berekening op geaggregeerde basis

Op geaggregeerde basis zijn de in aanmerking te nemen opbrengsten als volgt:
| 

  | | 
|---|

**Rekening 70[^22]** 

  | | 
|---|

**Rekening 74[^23]** 

  | | 
|---|

**Rekening 75[^24]** 

  | 
| 

**Vennootschap A**

  | | 
|---|

5.000

  | | 
|---|

200.000

  | | 
|---|

0

  | 
| 

**Vennootschap B**

  | | 
|---|

8.700.000

  | | 
|---|

1.000

  | | 
|---|

10

  | 
| 

**Vennootschap C**

  | | 
|---|

100.000

  | | 
|---|

1.500

  | | 
|---|

6.500.000

  | 
| 

## Geaggregeerde cijfers

  | | 
|---|

8.805.000

  | | 
|---|

202.500

  | | 
|---|

6.500.010

  | 

De (geaggregeerde) opbrengsten die voortspruiten uit het gewoon bedrijf bestaan voor meer dan de helft uit opbrengsten die beantwoorden aan de omschrijving van de post ‘omzet’.
Indien het bestuursorgaan opteert voor een berekening van de groottecriteria op geaggregeerde basis (en niet op geconsolideerde op basis) bedraagt, voor de beoordeling van de groottecriteria, de in aanmerking te nemen omzet 8.805.000.
#### Voorbeeld 2

Vennootschap C is een moedervennootschap met de vennootschap B als dochtervennootschap. Vennootschap A is op haar beurt een dochtervennootschap van vennootschap B. De vennootschap B is dus zelf ook een moedervennootschap. De opbrengstengegevens van deze drie vennootschappen zijn als volgt:
| 

  | | 
|---|

**Rekening 70[^25]** 

  | | 
|---|

**Rekening 75[^26]** 

  | 
| 

**Vennootschap A**

  | | 
|---|

1.000.000

  | | 
|---|

500.000

  | 
| 

**Vennootschap B**

  | | 
|---|

200.000

  | | 
|---|

9.200.000

  | 
| 

**Vennootschap C**

  | | 
|---|

9.100.000

  | | 
|---|

5.000

  | 
| 

## Geaggregeerde cijfers

  | | 
|---|

10.300.000

  | | 
|---|

9.705.000

  | 

### Berekening op enkelvoudige basis

Op enkelvoudige basis is de in aanmerking te nemen omzet voor de berekening van de groottecriteria voor de betreffende vennootschappen als volgt:
### Vennootschap A: 1.000.000

Vennootschap B: 9.400.000 (d.i. 200.000 + 9.200.000)[^27] 

Vennootschap C: 9.100.000

De vennootschappen B en C zijn echter moedervennootschappen zodat voor de bepaling van de groottecriteria de in aanmerking te nemen omzet plaatsvindt op geconsolideerde basis of op geaggregeerde basis.[^28]
### Moedervennootschap: berekening op geconsolideerde basis

In het voorbeeld wordt er hypothetisch vanuit gegaan dat de vennootschappen A, B en C geen intragroepsomzet hebben gerealiseerd.
Op geconsolideerde basis bestaan de opbrengsten die voortspruiten uit het gewoon bedrijf voor meer dan de helft uit opbrengsten die beantwoorden aan de omschrijving van de post ‘omzet’.
Indien het bestuursorgaan opteert voor een berekening van de groottecriteria op geconsolideerde basis (en niet op geaggregeerde basis) bedraagt, voor de beoordeling van de groottecriteria, de in aanmerking te nemen omzet van de vennootschappen B en C 10.300.000.
### Moedervennootschap: berekening op geaggregeerde basis

De (geaggregeerde) opbrengsten die voortspruiten uit het gewoon bedrijf bestaan voor meer dan de helft uit opbrengsten die beantwoorden aan de omschrijving van de post ‘omzet’.
Indien het bestuursorgaan opteert voor een berekening van de groottecriteria op geaggregeerde basis (en niet op geconsolideerde op basis) bedraagt, voor de beoordeling van de groottecriteria, de in aanmerking te nemen omzet van de vennootschappen B en C 10.300.000.
De Commissie stelt vast dat voor de moedervennootschappen B en C het grensbedrag van 9.000.000 aan omzet vermeld in artikel 15 W.Venn. bij een berekening op enkelvoudige basis overschreden wordt. Ook bij een berekening op geconsolideerde basis wordt dit grensbedrag overschreden. Door gebruik te maken van de geaggregeerde methode, waarbij de in aanmerking te nemen grensbedragen verhoogd worden met twintig procent, overschrijden noch de moedervennootschap C noch de moedervennootschap B de gestelde maximumgrenzen.
#### Voorbeeld 3

Vennootschap C is een moedervennootschap met de vennootschap B als dochtervennootschap. Vennootschap A is op haar beurt een dochtervennootschap van vennootschap B. De vennootschap B is dus zelf ook een moedervennootschap. De opbrengstengegevens van deze drie vennootschappen zijn als volgt:
| 

  | | 
|---|

**Rekening 70[^29]** 

  | | 
|---|

**Rekening 75[^30]** 

  | 
| 

**Vennootschap A**

  | | 
|---|

1.000.000

  | | 
|---|

500.000

  | 
| 

**Vennootschap B**

  | | 
|---|

200.000

  | | 
|---|

9.200.000

  | 
| 

**Vennootschap C**

  | | 
|---|

9.100.000

  | | 
|---|

2.000.000

  | 

### Berekening op enkelvoudige basis

Op enkelvoudige basis is de in aanmerking te nemen omzet voor de berekening van de groottecriteria voor de betreffende vennootschappen als volgt:
### Vennootschap A: 1.000.000

Vennootschap B: 9.400.000 (d.i. 200.000 + 9.200.000)[^31] 

Vennootschap C: 9.100.000

De vennootschappen B en C zijn echter moedervennootschappen zodat voor de bepaling van de groottecriteria de in aanmerking te nemen omzet plaatsvindt op geconsolideerde basis of op geaggregeerde basis.[^32]
### Moedervennootschap: berekening op geconsolideerde basis

In het voorbeeld wordt er hypothetisch vanuit gegaan dat de vennootschappen A, B en C geen intragroepsomzet hebben gerealiseerd.
Op geconsolideerde basis bestaan de opbrengsten die voortspruiten uit het gewoon bedrijf niet voor meer dan de helft uit opbrengsten die beantwoorden aan de omschrijving van de post ‘omzet’.
Indien het bestuursorgaan opteert voor een berekening van de groottecriteria op geconsolideerde basis (en niet op geaggregeerde basis) is, voor de beoordeling van de groottecriteria, de in aanmerking te nemen omzet van de vennootschappen B en C het totaal van de bedrijfs- en de financiële opbrengsten met uitsluiting van de niet-recurrente opbrengsten, zijnde 22.000.000[^33].
### Moedervennootschap: berekening op geaggregeerde basis

De (geaggregeerde) opbrengsten die voortspruiten uit het gewoon bedrijf bestaan niet voor meer dan de helft uit opbrengsten die beantwoorden aan de omschrijving van de post ‘omzet’.
Indien het bestuursorgaan opteert voor een berekening van de groottecriteria op geaggregeerde basis (en niet op geconsolideerde op basis) is, voor de beoordeling van de groottecriteria, de in aanmerking te nemen omzet van de vennootschappen B en C het totaal van de bedrijfs- en de financiële opbrengsten met uitsluiting van de niet-recurrente opbrengsten, zijnde 22.000.000[^34].
#### Voorbeeld 4

Vennootschap A is een moedervennootschap met de vennootschap B als dochtervennootschap. De vennootschap B is zelf geen moedervennootschap. De opbrengstengegevens van deze twee vennootschappen zijn als volgt:
| 

  | | 
|---|

**Rekening 70[^35]** 

  | | 
|---|

**Rekening 75[^36]** 

  | 
| 

**Vennootschap A**

  | | 
|---|

1.000

  | | 
|---|

100

  | 
| 

**Vennootschap B**

  | | 
|---|

12.000.000

  | | 
|---|

50

  | 

### Berekening op enkelvoudige basis

Op enkelvoudige basis is de in aanmerking te nemen omzet voor de berekening van de groottecriteria voor de betreffende vennootschappen als volgt:
### Vennootschap A: 1.000

Vennootschap B: 12.000.000

De vennootschap A is een moedervennootschappen zodat voor de bepaling van de groottecriteria de in aanmerking te nemen omzet plaatsvindt op geconsolideerde basis of op geaggregeerde basis.[^37]
### Berekening op geconsolideerde basis

In het voorbeeld wordt er hypothetisch vanuit gegaan dat de omzet van de vennootschap B een intragroepsomzet omvat van 7.000.000 euro die geëlimineerd wordt voor de bepaling van de opbrengsten op geconsolideerde basis[^38]. De geconsolideerde omzet bedraagt aldus 5.001.000 (d.i. 1.000 + 12.000.000 – 7.000.000).
Op geconsolideerde basis bestaan de opbrengsten die voortspruiten uit het gewoon bedrijf voor meer dan de helft uit opbrengsten die beantwoorden aan de omschrijving van de post ‘omzet’.
Indien het bestuursorgaan opteert voor een berekening van de groottecriteria op geconsolideerde basis (en niet op geaggregeerde basis) bedraagt, voor de beoordeling van de groottecriteria, de in aanmerking te nemen omzet van de vennootschap A 5.001.000.
### Berekening op geaggregeerde basis

De (geaggregeerde) opbrengsten die voortspruiten uit het gewoon bedrijf bestaan voor meer dan de helft uit opbrengsten die beantwoorden aan de omschrijving van de post ‘omzet’.
Indien het bestuursorgaan opteert voor een berekening van de groottecriteria op geaggregeerde basis (en niet op geconsolideerde op basis) bedraagt, voor de beoordeling van de groottecriteria, de in aanmerking te nemen omzet van de vennootschap A 12.001.000.
[^1]: Onderhavig advies is tot stand gekomen nadat een ontwerpadvies op 7 juni 2018 ter publieke consultatie werd gepubliceerd op de website van de CBN.

[^2]: Artikel 15, § 5, derde lid W.Venn.

[^3]: Artikel 15, § 6, eerste lid W.Venn.

[^4]: Artikel 15, § 6, tweede lid W.Venn.

[^5]: Deze gemaakte keuze geldt dan zowel voor de beoordeling van de omzet als van het balanstotaal. Een beoordeling van de omzet op geaggregeerde basis kan aldus niet gecombineerd worden met een beoordeling van het balanstotaal op geconsolideerde basis.

[^6]: Zie ook randnummer 25 tot 28 van het voormelde CBN-advies 2016/3.

[^7]: De Commissie merkt op dat een vennootschap die behoort tot een groep van beperkte omvang vrijgesteld is van de verplichting om een geconsolideerde jaarrekening op te maken (artikel 112 W.Venn.). Een vennootschap kan er evenwel vrijwillig voor kiezen om een geconsolideerde jaarrekening op te maken voor de beoordeling van de groottecriteria op geconsolideerde basis.

[^8]: Zie ook randnummer 22 van het voormelde CBN-advies 2016/3.

[^9]: Omzet.

[^10]: Andere bedrijfsopbrengsten met uitzondering van niet-recurrente bedrijfsopbrengsten.

[^11]: Financiële opbrengsten met uitzondering van niet-recurrente financiële opbrengsten.

[^12]: De opbrengsten die voortspruiten uit het gewoon bedrijf bestaan voor meer dan de helft uit andere opbrengsten dan omzet zodat het totaal van de bedrijfs- en financiële opbrengsten met uitsluiting van de niet-recurrente opbrengsten in rekening moet worden gebracht (toepassing van artikel 15, § 5, derde lid W.Venn.).

[^13]: De opbrengsten die voortspruiten uit het gewoon bedrijf bestaan voor meer dan de helft uit andere opbrengsten dan omzet zodat het totaal van de bedrijfs- en financiële opbrengsten met uitsluiting van de niet-recurrente opbrengsten in rekening moet worden gebracht (toepassing van artikel 15, § 5, derde lid W.Venn.).

[^14]: Artikel 15, § 6 W.Venn.

[^15]: Eliminatie in toepassing van artikel 146, 1° KB W.Venn.

[^16]: Omzet.

[^17]: Andere bedrijfsopbrengsten met uitzondering van niet-recurrente bedrijfsopbrengsten.

[^18]: Financiële opbrengsten met uitzondering van niet-recurrente financiële opbrengsten.

[^19]: Dit zijn de bedragen na de weglatingen en verrekeningen vermeld in de artikelen 137, 144 en 146 KB W.Venn.

[^20]: In dit voorbeeld gaan we er hypothetisch vanuit dat de omzet van vennootschap B een intragroepsomzet omvat van 46.000 euro, dus 5.000 + 8.700.000 + 100.000 – 46.000 = 8.759.000.

[^21]: Het bedrag van de omzet van vennootschap B gerealiseerd binnen de groep voor een bedrag van 46.000 euro wordt ingevolge de toepassing van artikel 146, 1° KB W.Venn. geëlimineerd. 8.759.000 = 5.000 + (8.700.000 – 46.000) + 100.000.

[^22]: Omzet.

[^23]: Andere bedrijfsopbrengsten met uitzondering van niet-recurrente bedrijfsopbrengsten.

[^24]: Financiële opbrengsten met uitzondering van niet-recurrente financiële opbrengsten.

[^25]: Omzet.

[^26]: Financiële opbrengsten met uitzondering van niet-recurrente financiële opbrengsten.

[^27]: De opbrengsten die voortspruiten uit het gewoon bedrijf bestaan voor meer dan de helft uit andere opbrengsten dan omzet zodat het totaal van de bedrijfs- en financiële opbrengsten met uitsluiting van de niet-recurrente opbrengsten in rekening moet worden gebracht (toepassing van artikel 15, § 5, derde lid W.Venn.).

[^28]: Artikel 15, § 6 W.Venn.

[^29]: Omzet.

[^30]: Financiële opbrengsten met uitzondering van niet-recurrente financiële opbrengsten.

[^31]: De opbrengsten die voortspruiten uit het gewoon bedrijf bestaan voor meer dan de helft uit andere opbrengsten dan omzet zodat het totaal van de bedrijfs- en financiële opbrengsten met uitsluiting van de niet-recurrente opbrengsten in rekening moet worden gebracht (toepassing van artikel 15, § 5, derde lid W.Venn.).

[^32]: Artikel 15, § 6 W.Venn.

[^33]: 10.300.000 + 11.700.000.

[^34]: 10.300.000 + 11.700.000.

[^35]: Omzet.

[^36]: Financiële opbrengsten met uitzondering van niet-recurrente financiële opbrengsten.

[^37]: Artikel 15, § 6 W.Venn.

[^38]: Artikel 146 KB W.Venn.
