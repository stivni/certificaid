---
tags: ["1.1", "1.2"]
itaa-lex-sectie: ""
wet: "Minimum Algemeen Rekeningstelsel voor verenigingen en stichtingen (MAR VZW)"
bron_rol: "normatief"
status: "beschikbaar"
bijgewerkt: "2023"
bron: "onbekend"
chunk:
  level: 2
  type: "Art."
  sub_strategy:
provenance:
  inputs:
    - id: resources/raw/handcrafted/MAR-vzw.md
      sha256: ca3eae4fdcde3853eebe486ea37c842e1ee212b78055c17eab87ff6afdde75a0
      version: '2023'
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: 8add68e
    model:
    prompt_version:
  generated_at: '2026-05-12T19:15:24Z'
  stale: false
  stale_reason:
  trust:
    status: needs-rework
    confirmed_at: '2026-05-12T19:27:15Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "Handcrafted file, geen PDF-artefacten. Maar: rekeningnummers als plain text zonder ##-headings (bv. '66211 Besteding'), structuur is flat-text rekeningstelsel zonder markdown-hiërarchie. 0 headings voor 5338 chars. Voor een MAR (rekeningstelsel) kan dit acceptabel zijn, maar de pagina-aanduidingen ('9 | Minimum Algemeen Rekeningstelsel...') zijn PDF-footer-resten."
    layer1:
      status: pass
      run_id: 20260512-210357
      run_at: '2026-05-12T21:03:59Z'
      heading_count: 0
      max_section_chars: 5338
      file_size_chars: 5338
      flags: []
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-12T19:27:15Z'
      rationale: "Handcrafted file, geen PDF-artefacten. Maar: rekeningnummers als plain text zonder ##-headings (bv. '66211 Besteding'), structuur is flat-text rekeningstelsel zonder markdown-hiërarchie. 0 headings voor 5338 chars. Voor een MAR (rekeningstelsel) kan dit acceptabel zijn, maar de pagina-aanduidingen ('9 | Minimum Algemeen Rekeningstelsel...') zijn PDF-footer-resten."
      concrete_problemen:
        - regel:
          categorie: A1
          type: form-feed
          voorbeeld: 9 | Minimum Algemeen Rekeningstelsel (MAR) voor verenigingen en stichtingen (pagina-indicator)
        - regel:
          categorie: B4
          type: other
          voorbeeld: 66211 Besteding (-) als plain-text, niet als heading
---

# Minimum Algemeen Rekeningstelsel voor verenigingen en stichtingen (MAR VZW)

*Bijgewerkt tot en met 2023 — gecoördineerde versie.*

66211
Besteding (-)
Schenkingen worden niet langer opgedeeld in met of zonder terugnemingsrecht. Dit maakt een wezenlijk verschil bij de interpretatie van de rekeningen, dus ook hier zou onze suggestie zijn om de opdeling te behouden zoals die bestond (6431 voor schenkingen met terugnemingsrecht, 6432 voor schenkingen zonder terugnemingsrecht).

9 | Minimum Algemeen Rekeningstelsel (MAR) voor verenigingen en stichtingen

Minderwaarden op de realisatie van vaste activa
Minderwaarden op de realisatie van immateriële en materiële vaste activa Minderwaarden op de realisatie van financiële vaste activa 664-66Andere niet-recurrente bedrijfskosten 668 Andere niet-recurrente financiële kosten 669 Als herstructureringskosten geactiveerde niet-recurrente kosten Als herstructureringskosten geactiveerde niet-recurrente bedrijfskosten (-) Als herstructureringskosten geactiveerde niet-recurrente financiële kosten (-)
67. Belastingen 4
670 Belgische belastingen op het resultaat van het boekjaar
Verschuldigde of gestorte belastingen en voorheffingen
Geactiveerde overschotten van betaalde belastingen en voorheffingen (-) Geraamde belastingen 671 Belgische belastingen op het resultaat van vorige boekjaren Verschuldigde of gestorte belastingsupplementen Geraamde belastingsupplementen Gevormde fiscale voorzieningen 672 Buitenlandse belastingen op het resultaat van het boekjaar 673 Buitenlandse belastingen op het resultaat van vorige boekjaren
68. Overboeking naar de uitgestelde belastingen en naar de belastingvrije reserves 680 Overboeking naar de uitgestelde belastingen 689 Overboeking naar de belastingvrije reserves
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
In de klasse 67 worden geen rekeningen of categorieën voorzien waarop de rechtspersonenbelasting of de taks ter vergoeding van de successierechten kunnen geboekt worden. Geen van beide is namelijk een “belasting op het resultaat”. Onze suggestie hier is om deze zelf te voorzien: 674 voor de rechtspersonenbelasting en 675 voor de taks ter vergoeding van de successierechten.

10 | Minimum Algemeen Rekeningstelsel (MAR) voor verenigingen en stichtingen

In de voorraad onroerende goederen bestemd voor verkoop
In de bestellingen in uitvoering
Aanschaffingswaarde
Toegerekende winst

72. Geproduceerde vaste activa
73. Lidgeld, schenkingen, legaten en subsidies
730 Lidgelden
731 Schenkingen 5
732 Legaten6
733 Subsidies
74. Overige bedrijfsopbrengsten
741 Meerwaarden op de courante realisatie van materiële vaste activa
742 Meerwaarde op de realisatie van handelsvorderingen
743-74Diverse bedrijfsopbrengsten
75. Financiële opbrengsten
750 Opbrengsten uit financiële vaste activa
751 Opbrengsten uit vlottende activa
752 Meerwaarden op de realisatie van vlottende activa
754 Wisselresultaten
755 Resultaten uit de omrekening van vreemde valuta
756-7 Diverse financiële opbrengsten
76. Niet-recurrente bedrijfs- of financiële opbrengsten
760 Terugneming van afschrijvingen en waardeverminderingen op immateriële vaste activa op materiële vaste activa 761 Terugneming van waardeverminderingen op financiële vaste activa 762 Terugneming van voorzieningen voor niet-recurrente risico's en kosten Terugneming van voorzieningen voor niet-recurrente bedrijfsrisico's en kosten Terugneming van voorzieningen voor niet-recurrente financiële risico’s en kosten 763 Meerwaarden op de realisatie van vaste activa

Schenkingen worden niet langer opgedeeld in met of zonder terugnemingsrecht. Dit maakt een wezenlijk verschil bij de interpretatie van de rekeningen, dus ook hier zou onze suggestie zijn om de opdeling te behouden zoals die bestond (7311 voor schenkingen met terugnemingsrecht en 7312 voor schenkingen zonder terugnemingsrecht).
Legaten worden niet langer opgedeeld in met of zonder terugnemingsrecht. Dit maakt een wezenlijk verschil bij de interpretatie van de rekeningen, dus ook hier zou onze suggestie zijn om de opdeling te behouden zoals die bestond (7321 voor legaten met terugnemingsrecht en 7322 voor legaten zonder terugnemingsrecht).

11 | Minimum Algemeen Rekeningstelsel (MAR) voor verenigingen en stichtingen

Meerwaarde op de realisatie van immateriële en materiële vaste activa
Meerwaarde op de realisatie van financiële vaste activa
764-76Andere niet-recurrente bedrijfsopbrengsten
769 Andere niet-recurrente financiële opbrengsten
77. Regularisering van belastingen
78. Onttrekking aan de belastingvrije reserves en uitgestelde belastingen 780 Onttrekking aan de uitgestelde belastingen 789 Onttrekking aan de belastingvrije reserves
79. Resultaatverwerking
790 Overgedragen positief resultaat van het boekjaar
791 Andere reserves
792 Over te dragen negatief resultaat

Dit MAR werd opgesteld o.b.v. het koninklijk besluit van 21 oktober 2018.

12 | Minimum Algemeen Rekeningstelsel (MAR) voor verenigingen en stichtingen
