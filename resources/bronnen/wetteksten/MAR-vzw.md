---
bijgewerkt: '2023'
bron: sbb.be / CBN-CNC
chunk:
  level: 2
  sub_strategy:
  type: Art.
itaa-lex-sectie: ''
provenance:
  inputs:
    - id: sbb.be / CBN-CNC
      sha256:
      version:
  tooling:
    pipeline: manual-import
    pipeline_version: skel-2026-05-11
    model:
    prompt_version:
  generated_at: '2026-05-11T11:42:59Z'
  stale: false
  stale_reason:
  trust:
    status: needs-rework
    confirmed_at: '2026-05-11T11:43:15Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "A7/C3: Het bestand is een rekeningplan-lijst waarbij de kolom-layout van het PDF totaal verloren is gegaan. Rekeningnummers (3- en 4-cijferig) staan als losse regels, gevolgd door de rekeningnaam op een volgende regel, soms met sub-nummers (bv. '2800' op één regel, 'Aanschaffingswaarde' op de volgende). Dit is geen markdown-conventie maar een directe PDF-column-extractie. A1: Paginanummer-resten staan als body-regels door het bestand ('1 | Minimum Algemeen Rekeningstelsel...', '2 | ...', enz. op 12 plaatsen). B4: Secties 1 t/m 7 (Klassen) staan als plain-text paragrafen ('1.', '2.', enz.) zonder ## of ### heading. Laag-1 was 'not_run'."
    layer1:
      file_size_chars:
      flags: []
      heading_count:
      max_section_chars:
      run_at:
      run_id:
      status: not_run
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-11T11:43:15Z'
      rationale: "A7/C3: Het bestand is een rekeningplan-lijst waarbij de kolom-layout van het PDF totaal verloren is gegaan. Rekeningnummers (3- en 4-cijferig) staan als losse regels, gevolgd door de rekeningnaam op een volgende regel, soms met sub-nummers (bv. '2800' op één regel, 'Aanschaffingswaarde' op de volgende). Dit is geen markdown-conventie maar een directe PDF-column-extractie. A1: Paginanummer-resten staan als body-regels door het bestand ('1 | Minimum Algemeen Rekeningstelsel...', '2 | ...', enz. op 12 plaatsen). B4: Secties 1 t/m 7 (Klassen) staan als plain-text paragrafen ('1.', '2.', enz.) zonder ## of ### heading. Laag-1 was 'not_run'."
      concrete_problemen:
        - regel: 80
          categorie: A1
          type: form-feed
          voorbeeld: "1\n\n1 | Minimum Algemeen Rekeningstelsel (MAR) voor verenigingen en stichtingen"
        - regel: 38
          categorie: B4
          type: other
          voorbeeld: "1.\n\nEigen vermogen, voorzieningen voor risico's en kosten... — plain text klasse-sectie zonder heading"
        - regel: 73
          categorie: A7
          type: scrambled-words
          voorbeeld: "1730\nSchulden op rekening\n\n...174\n175\n\n176\n178\n179 — rekeningnummers en namen door elkaar"
        - regel: 64
          categorie: C3
          type: pseudo-table
          voorbeeld: 164-16Voorzieningen voor overige risico's — afgekapte rekeningcode (164-16x, punt ontbreekt)
status: beschikbaar
tags:
  - '1.1'
  - '1.2'
wet: Minimum Algemeen Rekeningstelsel voor verenigingen en stichtingen (MAR VZW)
---

# MAR — Minimum Algemeen Rekeningstelsel voor verenigingen en stichtingen

*Standaard rekeningencodes voor vzw's, ivzw's en stichtingen. Het MAR voor ondernemingen (bv, nv, ...) is opgenomen in KB 21 oktober 2018 (resources/bronnen/wetteksten/KB-21-10-2018.md).*

Minimum Algemeen Rekeningstelsel (MAR) voor
verenigingen en stichtingen
1.

Eigen vermogen, voorzieningen voor risico's en kosten en schulden op
meer dan één jaar

10. Fondsen van de vereniging of stichting 1
11.
12. Herwaarderingsmeerwaarden
120 Herwaarderingsmeerwaarden op immateriële vaste activa
121 Herwaarderingsmeerwaarden materiele vaste activa
122 Herwaarderingsmeerwaarden op financiële vaste activa
124 Terugneming van waardeverminderingen op geldbelegging
13. Bestemde fondsen en andere reserves
130 Fondsen bestemd voor investeringen
131 Fondsen bestemd voor sociaal passief
132 Belastingvrije reserves
139 Andere bestemde fondsen en reserves
14. Overgedragen resultaat (+)(-)
15. Kapitaalsubsidies
16. Voorzieningen en uitgestelde belastingen
160 Voorziening voor pensioenen en soortgelijke verplichtingen
161 Voorzieningen voor belastingen
162 Voorzieningen voor grote herstellingen en grote onderhoudswerken
163 Voorzieningen voor milieuverplichtingen
164-16Voorzieningen voor overige risico's en kosten
Voorzieningen voor terug te betalen subsidies, legaten en schenkingen met
167 terugnemingsrecht
168 Uitgestelde belastingen
17. Schulden op meer dan één jaar
170 Achtergestelde leningen
171 Niet achtergestelde obligatieleningen
172 Leasingschulden en soortgelijke schulden
173 Kredietinstellingen
1730
Schulden op rekening
Bij de fondsen van de vereniging (klasse 10) voorziet men niet langer in rekeningnummers om de opdeling
tussen het beginvermogen en permanente financiering. Het blijft wel verplicht om de opdeling te maken. Onze
suggestie hier is om de opdeling zoals die vroeger bestond te behouden: “100 – Beginvermogen” en “101 –
Permanente financiering”.

1

1 | Minimum Algemeen Rekeningstelsel (MAR) voor verenigingen en stichtingen


174
175

176
178
179

2.

1731
Promessen
1732
Acceptkredieten
Overige leningen
Handelsschulden
1750
Handelsschulden leveranciers
1751
Handelsschulden te betalen wissels
Ontvangen vooruitbetaling op bestelling
Borgtochten ontvangen in contanten
Overige schulden
1790
Overige schulden rentedragend
1791
Overige schulden niet-rentedragend

Oprichtingskosten, vaste activa en vorderingen op meer dan één jaar 2

20. Oprichtingskosten
200 Kosten van oprichting
201 Kosten bij uitgifte van leningen
202 Overige oprichtingskosten
204 Herstructureringskosten
21. Immateriële vaste activa
210 Kosten van onderzoek en ontwikkeling
211 Concessies, octrooien, licenties, knowhow, merken en soortgelijke rechten
212 Goodwill
213 Vooruitbetalingen
22. Terreinen en gebouwen
220 Terreinen
221 Gebouwen
222 Bebouwde terreinen
223 Overige zakelijke rechten op onroerende goederen
23. Installaties, machines en uitrusting
24. Meubilair en rollend materieel
25. Vaste activa in leasing of op grond van soortgelijke rechten
250 Terreinen en gebouwen
251 Installaties, machines en uitrusting
252 Meubilair en rollend materieel
26. Overige materiële vaste activa
Bij de vaste activa voorziet men niet langer in een opdeling op basis van het eigendomsrecht, vroeger was dit
voor alle materiële vaste activa voorzien. In de jaarrekening vraagt men deze opdeling op vandaag wel nog,
waardoor de onderverdeling in het rekeningplan zeker nog steeds valt aan te bevelen. Bovendien maakt dit een
wezenlijk verschil bij de interpretatie van een balans, waar de opdeling nodig is om een waar en getrouw beeld
te geven van de werkelijkheid.

2

2 | Minimum Algemeen Rekeningstelsel (MAR) voor verenigingen en stichtingen


27. Materiële vaste activa in aanbouw en vooruitbetalingen
28. Financiële vaste activa
280 Deelnemingen in verbonden vennootschappen
2800
Aanschaffingswaarde
2801
Nog te storten bedragen (-)
2808
Geboekte meerwaarden
2809
Geboekte waardeverminderingen (-)
281 Vorderingen op verbonden entiteiten
2810
Vorderingen op rekening
2811
Te innen wissels
2812
Vastrentende effecten
2817
Dubieuze debiteuren
2819
Geboekte waardeverminderingen (-)
282 Deelnemingen in vennootschappen waarmee een deelnemingsverhouding bestaat
2820
Aanschaffingswaarde
2821
Nog te storten bedragen (-)
2828
Geboekte meerwaarden
2829
Geboekte waardeverminderingen (-)
283 Vorderingen op vennootschappen waarmee een deelnemingsverhouding bestaat
2830
Vorderingen op rekening
2831
Te innen wissels
2832
Vastrentende effecten
2837
Dubieuze debiteuren
2839
Geboekte waardeverminderingen (-)
284 Andere aandelen
2840
Aanschaffingswaarde
2841
Nog te storten bedragen (-)
2848
Geboekte meerwaarden
2849
Geboekte waardeverminderingen (-)
285 Overige vorderingen
2850
Vorderingen op rekening
2851
Te innen wissels
2852
Vastrentende effecten
2857
Dubieuze debiteuren
2859
Geboekte waardeverminderingen (-)
288 Borgtochten betaald in contanten
29. Vorderingen op meer dan één jaar
290 Handelsvorderingen
2900
Handelsdebiteuren
2901
Te innen wissels
2906
Vooruitbetalingen
2907
Dubieuze debiteuren
2909
Geboekte waardeverminderingen (-)

3 | Minimum Algemeen Rekeningstelsel (MAR) voor verenigingen en stichtingen


291

Overige vorderingen
2910
2911
2915
2916
2919

3.

Vorderingen op rekening
Te innen wissels
Niet-rentedragende vorderingen of gekoppeld aan een abnorma
lage rente
Dubieuze debiteuren
Geboekte waardeverminderingen (-)

Voorraden en bestellingen in uitvoering

30. Grondstoffen
300 Aanschaffingswaarde
309 Geboekte waardeverminderingen (-)
31. Hulpstoffen
310 Aanschaffingswaarde
319 Geboekte waardeverminderingen (-)
32. Goederen in bewerking
320 Aanschaffingswaarde
329 Geboekte waardeverminderingen (-)
33. Gereed product
330 Aanschaffingswaarde
339 Geboekte waardeverminderingen (-)
34. Handelsgoederen
340 Aanschaffingswaarde
349 Geboekte waardeverminderingen (-)
35. Onroerende goederen bestemd voor verkoop
350 Aanschaffingswaarde
359 Geboekte waardeverminderingen (-)
36. Vooruitbetalingen op voorraadinkopen
360 Vooruitbetalingen
369 Geboekte waardeverminderingen (-)
37. Bestellingen in uitvoering
370 Aanschaffingswaarde
371 Toegerekende winst
379 Geboekte waardeverminderingen (-)

4.

Vorderingen en schulden op ten hoogste één jaar

40. Handelsvorderingen
400 Klanten

4 | Minimum Algemeen Rekeningstelsel (MAR) voor verenigingen en stichtingen


401
404
406
407
409

Te innen wissels
Te innen opbrengsten
Vooruitbetalingen
Dubieuze debiteuren
Geboekte waardeverminderingen (-)

41. overige vorderingen
410
411 Terug te vorderen btw
412 Terug te vorderen belastingen en voorheffingen
4120-4124
4125-4127
Andere Belgische belastingen
4128
Buitenlandse belastingen
413 Te ontvangen subsidies
414 Te innen opbrengsten
415 Niet-rentedragende vorderingen of gekoppeld aan een abnormaal lage rente
416 Diverse vorderingen
417 Dubieuze debiteuren
418 Borgtochten betaald in contanten
419 Geboekte waardeverminderingen (-)
42. Schulden op meer dan één jaar die binnen het jaar vervallen
420 Achtergestelde leningen
421 Niet achtergestelde obligatieleningen
422 Leasingschulden en soortgelijke schulden
423 Kredietinstellingen
4230
Schulden op rekening
4231
Promessen
4232
Acceptkredieten
424 Overige leningen
425 Handelsschulden
4250
Handelsschulden leveranciers
4251
Handelsschulden te betalen wissels
426 Ontvangen vooruitbetaling op bestelling
428 Borgtochten ontvangen in contanten
429 Overige schulden
4290
Overige schulden rentedragend
4291
Overige schulden niet-rentedragend
43. Financiële schulden
430 Kredietinstellingen - leningen op rekening met vaste termijn
431 Kredietinstellingen - promessen
432 Kredietinstellingen - acceptkredieten
433 Kredietinstellingen - schulden op rekening courant
439 Overige leningen
44. Handelsschulden

5 | Minimum Algemeen Rekeningstelsel (MAR) voor verenigingen en stichtingen


440
441
444

Leveranciers
Te betalen wissels
Te ontvangen facturen

45. Schulden met betrekking tot belastingen, bezoldigingen en sociale lasten
450 Geraamd bedrag der belastingschulden
4500-4504
4505-4507
Andere Belgische belastingen
4508
Buitenlandse belastingen
451 Te betalen btw
452 Te betalen belastingen en taksen
4520-4524
4525-4527
Andere Belgische belastingen
4528
Buitenlandse belastingen
453 Ingehouden voorheffingen
454 Rijksdienst voor Sociale Zekerheid
455 Bezoldigingen
456 Vakantiegeld
459 Andere sociale schulden
46. Vooruitbetalingen op bestellingen
48. Diverse schulden
480 Vervallen obligaties en coupons
483 Terug te betalen subsidies
488 Borgtochten ontvangen in contanten
489 Andere diverse schulden
4890
Rentedragend
4891
Niet-rentedragend of gekoppeld aan een abnormaal lage rente
49. Overlopende rekeningen
490 Over te dragen kosten (actief)
491 Verkregen opbrengsten (actief)
492 Toe te rekenen kosten (passief)
493 Over te dragen opbrengsten (passief)
499 Wachtrekeningen

5.

Geldbeleggingen en liquide middelen

50. Geldbeleggingen andere dan aandelen, vastrentende effecten en termijndeposito's
500 Aanschaffingswaarde
509 Geboekte waardeverminderingen
51. Aandelen
510 Aanschaffingswaarde
511 Nog te storten bedragen (-)
519 Geboekte waardeverminderingen (-)

6 | Minimum Algemeen Rekeningstelsel (MAR) voor verenigingen en stichtingen


52. Vastrentende effecten
520 Aanschaffingswaarde
529 Geboekte waardeverminderingen (-)
53. Termijndeposito's
530 Op meer dan één jaar
531 Op meer dan een maand en op ten hoogste één jaar
532 Op ten hoogste één maand
539 Geboekte waardeverminderingen
54. Te incasseren vervallen waarden
55. Kredietinstellingen
550-55Rekeningen geopend bij diverse instellingen onder te verdelen in:
…0 Rekening-courant
...1 Uitgeschreven cheques
…9 Geboekte waardeverminderingen (-)
57. Kassen
570-5 Kassen-contanten
578 Kassen-zegels
58. Interne overboekingen

6.

Kosten

60. Handelsgoederen, grond- en hulpstoffen
600 Aankopen van grondstoffen
601 Aankopen van hulpstoffen
602 Aankopen van diensten, werk en studies
603 Algemene onderaannemingen
604 Aankopen van handelsgoederen
605 Aankopen van onroerende goederen bestemd voor verkoop
608 Ontvangen kortingen, ristorno's en rabatten (-)
609 Voorraadwijzigingen
6090
Voorraadwijziging grondstoffen
6091
Voorraadwijziging hulpstoffen
6094
Voorraadwijziging handelsgoederen
Voorraadwijziging gekochte onroerende goederen bestemd voo
6095
verkoop
61. Diensten en diverse goederen
617 Uitzendpersoneel en personen die ter beschikking worden gesteld van de vereniging
Bezoldiging, premies voor buitenwettelijke verzekeringen, ouderdoms- en
overlevingspensioenen van bestuurders die niet worden toegekend krachtens een
618 arbeidscontract
62. Bezoldigingen, sociale lasten en pensioenen

7 | Minimum Algemeen Rekeningstelsel (MAR) voor verenigingen en stichtingen


620

621
622
623
624

Bezoldigingen en rechtstreekse sociale voordelen
6200
Bestuurders of zaakvoerders
6201
Directiepersoneel
6202
Bedienden
6203
Arbeiders
6204
Andere personeelsleden
Werkgeversbijdragen voor sociale verzekeringen
Werkgeverspremies voor buitenwettelijke verzekeringen
Andere personeelskosten
Ouderdoms- en overlevingspensioenen
6240
Bestuurders of zaakvoerders
6241
Personeel

63. Afschrijvingen, waardeverminderingen en voorzieningen voor risico's en kosten
630 Afschrijvingen en waardeverminderingen op vaste activa toevoeging
6300
Afschrijvingen op oprichtingskosten
6301
Afschrijvingen op immateriële vaste activa
6302
Afschrijvingen op materiële vaste activa
6308
Waardeverminderingen op immateriële vaste activa
6309
Waardeverminderingen op materiële vaste activa
631 Waardeverminderingen op voorraden
6310
Toevoeging
6311
Terugneming (-)
632 Waardeverminderingen op bestellingen in uitvoering
6320
Toevoeging
6321
Terugneming (-)
633 Waardeverminderingen op handelsvorderingen op meer dan één jaar
6330
Toevoeging
6331
Terugneming (-)
634 Waardeverminderingen op handelsvorderingen op ten hoogste één jaar
6340
Toevoeging
6341
Terugneming (-)
635 Voorzieningen voor pensioenen en soortgelijke verplichtingen
6350
Toevoeging
6351
Besteding en terugneming (-)
636 Voorzieningen voor grote herstellingswerken en grote onderhoudswerken
6360
Toevoeging
6361
Besteding en terugneming (-)
637 Voorzieningen voor milieuverplichtingen
6370
Toevoeging
6371
Besteding en terugneming (-)
Voorzieningen voor terug te betalen subsidies en legaten en voor schenkingen met
638 terugnemingsrecht
6380
Toevoeging
6381
Besteding en terugneming (-)
639 Voorzieningen voor andere risico's en kosten

8 | Minimum Algemeen Rekeningstelsel (MAR) voor verenigingen en stichtingen


6390
6391

Toevoeging
Besteding en terugneming (-)

64. Andere bedrijfskosten
640 Bedrijfsbelastingen
641 Minderwaarden op de courante realisatie van vaste activa
642 Minderwaarden op de realisatie van handelsvorderingen
643 Schenkingen 3
644-64Diverse bedrijfskosten
649 Als herstructureringskosten geactiveerde bedrijfskosten (-)
65. Financiële kosten
650 Kosten van schulden
6500
Rente, commissies en kosten verbonden aan schulden
6501
Afschrijving van kosten bij uitgifte van leningen en van disagio
6502
Geactiveerde intercalaire interesten (-)
651 Waardeverminderingen op vlottende activa
6510
Toevoeging
6511
Terugneming (-)
652 Minderwaarden op verwezenlijking van vlottende activa
653 Discontokosten op vorderingen
654 Wisselresultaten
655 Resultaten uit de omrekening van vreemde valuta
656 Voorzieningen van financiële aard
6560
Toevoeging
6561
Besteding en terugneming (-)
657-65Diverse financiële kosten
659 Als herstructureringskosten geactiveerde financiële kosten (-)
66. Niet-recurrente bedrijfs- of financiële kosten
660 Niet-recurrente afschrijvingen en waardeverminderingen (toevoeging)
6600
op oprichtingskosten
6601
op immateriële vaste activa
6602
op materiële vaste activa
661 Waardeverminderingen op financiële vaste activa (toevoeging)
662 Voorzieningen voor niet-recurrente risico's en kosten
6620
Voorzieningen voor niet-recurrente bedrijfsrisico's en kosten
66200
Toevoeging
66201
Bestedingen (-)
6621
Voorzieningen voor niet-recurrente financiële risico's en kosten
66210
Toevoeging
66211
Besteding (-)
Schenkingen worden niet langer opgedeeld in met of zonder terugnemingsrecht. Dit maakt een wezenlijk
verschil bij de interpretatie van de rekeningen, dus ook hier zou onze suggestie zijn om de opdeling te
behouden zoals die bestond (6431 voor schenkingen met terugnemingsrecht, 6432 voor schenkingen zonder
terugnemingsrecht).

3

9 | Minimum Algemeen Rekeningstelsel (MAR) voor verenigingen en stichtingen


663

Minderwaarden op de realisatie van vaste activa
Minderwaarden op de realisatie van immateriële en materiële
6630
vaste activa
6631
Minderwaarden op de realisatie van financiële vaste activa
664-66Andere niet-recurrente bedrijfskosten
668 Andere niet-recurrente financiële kosten
669 Als herstructureringskosten geactiveerde niet-recurrente kosten
Als herstructureringskosten geactiveerde niet-recurrente
6690
bedrijfskosten (-)
Als herstructureringskosten geactiveerde niet-recurrente
6691
financiële kosten (-)
67. Belastingen 4
670 Belgische belastingen op het resultaat van het boekjaar
6700
Verschuldigde of gestorte belastingen en voorheffingen
Geactiveerde overschotten van betaalde belastingen en
6701
voorheffingen (-)
6702
Geraamde belastingen
671 Belgische belastingen op het resultaat van vorige boekjaren
6710
Verschuldigde of gestorte belastingsupplementen
6711
Geraamde belastingsupplementen
6712
Gevormde fiscale voorzieningen
672 Buitenlandse belastingen op het resultaat van het boekjaar
673 Buitenlandse belastingen op het resultaat van vorige boekjaren
68. Overboeking naar de uitgestelde belastingen en naar de belastingvrije reserves
680 Overboeking naar de uitgestelde belastingen
689 Overboeking naar de belastingvrije reserves
69. Resultaatverwerking
690 Overgedragen negatief resultaat van het vorig boekjaar
691 Overboeking naar de bestemde fondsen en andere reserves
692 Over te dragen positief resultaat

7.

Opbrengsten

70. Omzet
700-70Verkopen en dienstprestaties
708 Toegekende kortingen, ristorno's en rabatten (-)
71. Wijzigingen n de voorraad en bestellingen in uitvoering
712 In de voorraad goederen in bewerking
713 In de voorraad gereed product
In de klasse 67 worden geen rekeningen of categorieën voorzien waarop de rechtspersonenbelasting of de
taks ter vergoeding van de successierechten kunnen geboekt worden. Geen van beide is namelijk een
“belasting op het resultaat”. Onze suggestie hier is om deze zelf te voorzien: 674 voor de
rechtspersonenbelasting en 675 voor de taks ter vergoeding van de successierechten.

4

10 | Minimum Algemeen Rekeningstelsel (MAR) voor verenigingen en stichtingen


715
717

In de voorraad onroerende goederen bestemd voor verkoop
In de bestellingen in uitvoering
7170
Aanschaffingswaarde
7171
Toegerekende winst

72. Geproduceerde vaste activa
73. Lidgeld, schenkingen, legaten en subsidies
730 Lidgelden
731 Schenkingen 5
732 Legaten6
733 Subsidies
74. Overige bedrijfsopbrengsten
740
741 Meerwaarden op de courante realisatie van materiële vaste activa
742 Meerwaarde op de realisatie van handelsvorderingen
743-74Diverse bedrijfsopbrengsten
75. Financiële opbrengsten
750 Opbrengsten uit financiële vaste activa
751 Opbrengsten uit vlottende activa
752 Meerwaarden op de realisatie van vlottende activa
753
754 Wisselresultaten
755 Resultaten uit de omrekening van vreemde valuta
756-7 Diverse financiële opbrengsten
76. Niet-recurrente bedrijfs- of financiële opbrengsten
760 Terugneming van afschrijvingen en waardeverminderingen
7600
op immateriële vaste activa
7601
op materiële vaste activa
761 Terugneming van waardeverminderingen op financiële vaste activa
762 Terugneming van voorzieningen voor niet-recurrente risico's en kosten
Terugneming van voorzieningen voor niet-recurrente
7620
bedrijfsrisico's en kosten
Terugneming van voorzieningen voor niet-recurrente financiële
7621
risico’s en kosten
763 Meerwaarden op de realisatie van vaste activa

Schenkingen worden niet langer opgedeeld in met of zonder terugnemingsrecht. Dit maakt een wezenlijk
verschil bij de interpretatie van de rekeningen, dus ook hier zou onze suggestie zijn om de opdeling te
behouden zoals die bestond (7311 voor schenkingen met terugnemingsrecht en 7312 voor schenkingen zonder
terugnemingsrecht).
6
Legaten worden niet langer opgedeeld in met of zonder terugnemingsrecht. Dit maakt een wezenlijk verschil
bij de interpretatie van de rekeningen, dus ook hier zou onze suggestie zijn om de opdeling te behouden zoals
die bestond (7321 voor legaten met terugnemingsrecht en 7322 voor legaten zonder terugnemingsrecht).
5

11 | Minimum Algemeen Rekeningstelsel (MAR) voor verenigingen en stichtingen


Meerwaarde op de realisatie van immateriële en materiële vaste
7630
activa
7631
Meerwaarde op de realisatie van financiële vaste activa
764-76Andere niet-recurrente bedrijfsopbrengsten
769 Andere niet-recurrente financiële opbrengsten
77. Regularisering van belastingen
78. Onttrekking aan de belastingvrije reserves en uitgestelde belastingen
780 Onttrekking aan de uitgestelde belastingen
789 Onttrekking aan de belastingvrije reserves
79. Resultaatverwerking
790 Overgedragen positief resultaat van het boekjaar
791 Andere reserves
792 Over te dragen negatief resultaat

Dit MAR werd opgesteld o.b.v. het koninklijk besluit van 21 oktober 2018.

12 | Minimum Algemeen Rekeningstelsel (MAR) voor verenigingen en stichtingen
