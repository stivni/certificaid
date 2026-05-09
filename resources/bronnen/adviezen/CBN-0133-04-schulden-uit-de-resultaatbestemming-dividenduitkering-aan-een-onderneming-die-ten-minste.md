---
nummer: "CBN-advies 133/4"
datum: 1998-03-01
themas:
  - bestemming van het resultaat van het boekjaar
  - deelneming
  - dividenden
  - dividenduitkering
  - ingehouden voorheffing
  - roerende voorheffing
  - schulden
  - schulden uit bestemming van het resultaat
bron: https://www.cbn-cnc.be/nl/adviezen/schulden-uit-de-resultaatbestemming-dividenduitkering-aan-een-onderneming-die-ten-minste
provenance:
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/schulden-uit-de-resultaatbestemming-dividenduitkering-aan-een-onderneming-die-ten-minste
      sha256: 91e4ca11a7177d32fb69fb0526c84ed29cae2683cb3bdb8c0797556e9eb8e5f7
      version:
  tooling:
    pipeline: tools/etl/scrape_cbn_advies.py
    pipeline_version: uncommitted
    model:
    prompt_version:
  generated_at: '2026-05-08T18:34:54Z'
  stale: false
  stale_reason:
  trust:
    status: trusted
    qa_version:
    confirmed_at: '2026-05-08T18:40:03Z'
    confirmed_by: qa-laag1-auto
    rationale: Laag 1 QA pass na re-scrape via scrape_cbn_advies.py (2026-05-08)
gerelateerde_adviezen:
  - titel: Schulden voortvloeiend uit de bestemming van het resultaat
    url: https://www.cbn-cnc.be/nl/adviezen/schulden-voortvloeiend-uit-de-bestemming-van-het-resultaat
    datum: '1985-04-01'
  - titel: Voorstelling van een tabel met de wijzigingen in het eigen vermogen en de bestemming van het resultaat van het boekjaar
    url: https://www.cbn-cnc.be/nl/adviezen/voorstelling-van-een-tabel-met-de-wijzigingen-in-het-eigen-vermogen-en-de-bestemming-van
    datum: '1995-03-01'
---

# CBN-advies 133/4 - Schulden uit de resultaatbestemming : dividenduitkering aan een onderneming die ten minste 25 % bezit van het kapitaal van de vennootschap die het dividend uitkeert

Met toepassing van het koninklijk besluit van 6 juli 1997[^1] tot wijziging van artikel 106, §§ 5 en 6 van het Koninklijk Besluit tot uitvoering van het Wetboek van de Inkomstenbelastingen (KB/WIB 92), wordt geen roerende voorheffing ingehouden op het dividend dat een Belgische vennootschap uitkeert aan een andere Belgische of Europese vennootschap, op voorwaarde dat laatstgenoemde vennootschap tijdens een ononderbroken periode van ten minste één jaar een deelneming van minimaal 25 % bezit in het kapitaal van eerstgenoemde vennootschap, zelfs indien, op het ogenblik waarop het dividend wordt toegekend, de termijn van één jaar nog niet is verstreken. 

In laatstgenoemd geval moet de vennootschap die het dividend uitkeert, echter een bedrag dat overeenstemt met de roerende voorheffing, inhouden tot op het ogenblik waarop vaststaat dat al dan niet is voldaan aan de voorwaarde dat de deelneming ten minste één jaar ononderbroken moet worden behouden[^2]. 

De Commissie werd gevraagd hoe het deel van het dividend dat wordt ingehouden door de vennootschap die het dividend uitkeert, boekhoudkundig moet worden verwerkt. 

Zij is van oordeel dat, aangezien de schuld uit de dividenduitkering bruto[^3] moet worden geboekt en de belastingschuld, in voorkomend geval, slechts ontstaat wanneer niet meer kan worden voldaan aan de voorwaarde dat de deelneming gedurende ten minste één jaar ononderbroken moet worden behouden, het dividendsaldo ten belope van het bedrag van de roerende voorheffing behouden moet blijven in een rekening 47 ... *Schulden uit de bestemming van het resultaat* tot op het moment waarop:

- hetzij de belastingschuld ontstaat (de begunstigde vennootschap heeft haar deelneming van 25 % niet ten minste één jaar behouden); 
- hetzij is voldaan aan de voornoemde voorwaarde en het dividendsaldo aan de begunstigde vennootschap moet worden gestort. 

Voorbeeld : op 15 mei van jaar n wordt een dividend van 800 uitgekeerd door vennootschap A waarin vennootschap B sinds 15 februari van jaar n 30 % bezit (vóór 15 februari bezat B 15 % in A). Dit resulteert in de volgende boekingen : 

In de rekeningen van A

*Bij de opstelling van de jaarrekening[^4]:*

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 694 | Vergoeding van het kapitaal | 800 | |
| aan | 471 | Dividenden over het boekjaar | | 800 |

*Bij de dividenduitkering*

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 471 | Dividenden over het boekjaar | 600 | |
| aan | 55 | Kredietinstellingen | | 600 |

*Indien B, op 15 november van jaar n, 15 % van A verkoopt*

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 471 | Dividenden over het boekjaar | 200 | |
| aan | 453 | Ingehouden voorheffing | | 200 |

*Indien B, op 15 februari van jaar n+1, nog steeds meer dan 25 % van A bezit*

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 471 | Dividenden over het boekjaar | 200 | |
| aan | 55 | Kredietinstellingen | | 200 |

In de rekeningen van B 

*Bij de dividenduitkering*

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 55 | Kredietinstellingen | 600 | |
| | 41 | Overige vorderingen | 200 | |
| aan | 75 | Financiële opbrengsten | | 800 |

*Wanneer B op 15 november van jaar n 15 % van A verkoopt*

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 67 | Belastingen op het resultaat | 200 | |
| aan | 41 | Overige vorderingen | | 200 |

*Indien B op 15 februari van jaar n+1 nog steeds meer dan 25 % van A bezit*

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 55 | Kredietinstellingen | 200 | |
| aan | 41 | Overige vorderingen | | 200 |

[^1]: B.S., 30 juli 1997, p. 19487. Dit besluit vloeit voort uit het arrest van het Europees Hof van Justitie van 17 oktober 1996 in de zaak Denkavit International B.V. (nr. C-283/94), VITIC Amsterdam B.V. (nr. C-291/94) en Voormeer B.V. (nr. C-292/94), Jurisprudentie van het Hof van Justitie, 1996/10, P. 5063.

[^2]: Artikel 117, § 14 van het KB/WIB 92 zoals ingevoegd door het Koninklijk Besluit van 6 juli 1997.

[^3]: Zie terzake advies 133/3 in Bull. CBN nr. 16, april 1985, p. 14.

[^4]: Advies 133/3 van de CBN, Bull. CBN nr. 16.
