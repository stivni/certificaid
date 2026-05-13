---
tags: ["VI.C", "2.4"]
itaa-lex-sectie: "VI.C"
wet: "M.B. nr. 1 van 2 september 1980, met betrekking tot de aftrekregeling voor de toepassing van de belasting over de toegevoegde waarde"
bron_rol: "itaa_lex"
status: "beschikbaar"
bijgewerkt: "02.09.1980"
bron: "Afgesplitst uit Fisconet-compilatie (pdftotext_compilatie_btw)"
chunk:
  level: 2
  type: "Art."
  sub_strategy:
provenance:
  inputs:
    - id: resources/raw/wetteksten/btw-kbs/WBTW-MB-compilatie.pdf
      sha256: e2e322b0d748d0314e5f16d11a0aac6c964d684451d00738c9352b4f32f9171c
      version: 29.04.2024
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: 04e910e-dirty
    model:
    prompt_version:
  generated_at: '2026-05-13T11:16:46Z'
  stale: false
  stale_reason:
  trust:
    status: needs-rework
    confirmed_at: '2026-05-13T11:17:05Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "Massieve ETL-bleed onveranderd: regels 56-140 (85 regels) bevatten de complete compilatie-cover ('BELASTING OVER DE TOEGEVOEGDE WAARDE', 'Federale Overheidsdienst FINANCIEN', contact-email) plus de volledige TOC van alle 25+ MB's met PDF-glyph-bullets ' * ', onderstreepte placeholders '_____' en 'Bijw. XX/datum' kolom-bleed midden in beschrijvingen. De eigenlijke MB-1 wettekst begint pas op regel 141 en is slechts 16 regels lang. De drie nieuwe transformers raken dit volume aan pre-tekst-pollutie niet (niet 'Lijst van de bijwerkingen', niet running-header met pg.-formaat, niet lege heading)."
    layer1:
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-13T11:17:05Z'
      rationale: "Massieve ETL-bleed onveranderd: regels 56-140 (85 regels) bevatten de complete compilatie-cover ('BELASTING OVER DE TOEGEVOEGDE WAARDE', 'Federale Overheidsdienst FINANCIEN', contact-email) plus de volledige TOC van alle 25+ MB's met PDF-glyph-bullets ' * ', onderstreepte placeholders '_____' en 'Bijw. XX/datum' kolom-bleed midden in beschrijvingen. De eigenlijke MB-1 wettekst begint pas op regel 141 en is slechts 16 regels lang. De drie nieuwe transformers raken dit volume aan pre-tekst-pollutie niet (niet 'Lijst van de bijwerkingen', niet running-header met pg.-formaat, niet lege heading)."
      concrete_problemen:
        - "Regels 56-78: compilatie-cover ('BELASTING OVER DE TOEGEVOEGDE WAARDE', 'Federale Overheidsdienst FINANCIEN', 'contact : comments.kms@minfin.fed.be') als plain text vóór de wettekst"
        - "Regels 79-139: complete 'Lijst van de ministeriële besluiten' (25 MB's) met PDF-bullet-glyphs ' * '"
        - "Regels 85-121: onderstreepte placeholders '_____' midden in TOC-regels"
        - "Regels 81, 83, 91, 101-105, 123, 126-132, 134, 137, 139: bijwerkingsmarkers 'Bijw. XX/datum' kolom-bleed midden in beschrijvingen"
        - Regel 141 bevat de eigenlijke MB-titel als plain text ipv heading, gevolgd door 'Officieuze coördinatie - Laatstelijk gewijzigd...' op één lange regel
        - 'Body/content-ratio: 85 regels pollutie versus 16 regels eigenlijke wettekst'
---

# M.B. nr. 1 van 2 september 1980, met betrekking tot de aftrekregeling voor de toepassing van de belasting over de toegevoegde waarde

*Bijgewerkt tot en met 02.09.1980 — gecoördineerde versie.*

2°, 53ter, 1°, 53quinquies en 53sexies van het Wetboek van de belasting over de toegevoegde waarde moeten worden ingediend

 * Ministerieel besluit, van 23 juni 2005, met betrekking tot de delegatie Bijw. 01/01.01.2012 van de bevoegde autoriteit inzake de administratieve samenwerking op het gebied van de belasting over de toegevoegde waarde

 * Ministerieel besluit, van 29 augustus 2006, tot aanduiding van de Bijw.02/13.07.2012 ambtenaar bedoeld in artikel 62bis van het Wetboek van de belasting over de toegevoegde waarde en in artikel 318 van het Wetboek van de inkomstenbelastingen 1992

 * Ministerieel besluit, van 26 februari 2007, met betrekking tot de aanduiding van Recent opgeheven de dienst bevoegd voor het ontvangen van de berichten en het afleveren van de 06.07.2020 ontvangstmeldingen in het kader van het systeem van elektronische notificaties tussen de Federale Overheidsdienst Financiën en bepaalde ministeriële officiers, openbare ambtenaren en andere personen (Opgeheven bij MB 22.06.2020)

 * Ministerieel besluit, van 28 oktober 2009, tot bepaling van het model der Recent opgeheven berichten en kennisgevingen als bedoeld in de artikelen 93ter en 93quinquies 06.07.2020 van het Wetboek van de belasting over de toegevoegde waarde en in de artikelen 433 en 435 van het Wetboek van de inkomstenbelastingen 1992

 * Ministerieel besluit, van 16 juli 2019, tot aanduiding van de ambtenaren Bijw. 01/02.08.2019 die in de functie van adviseur-generaal zitting hebben in de beroepscommissie zoals bedoeld in artikel 66, § 2 van het wetboek van de minnelijke en gedwongen invordering van fiscale en niet-fiscale schuldvorderingen en dat aan die beroepscommissie de machtiging geeft om op te treden als beroepscommissie zoals bedoeld in artikel 84octies, § 2, van het wetboek van de belasting over de toegevoegde waarde en als beroepscommissie zoals bedoeld in artikel 413quinquies, § 2, van het wetboek van de inkomstenbelastingen 1992

 * Ministerieel besluit, van 17 maart 2023, met betrekking tot de Bijw. 01/01.04.2023 vaststelling van de modaliteiten voor het bijhouden van een elektronisch dagboek van ontvangsten en van een centralisatiedagboek enerzijds en de bewaring en de integriteit van de inhoud van de elektronische kastickets anderzijds, alsmede de modaliteiten voor de bewaring van de financiële rapporten

 * Ministerieel besluit, van 29 april 2024, betreffende de technische Bijw. 01/03.06.2024 aspecten ten aanzien van de certificatie van een geregistreerd kassasysteem

Ministerieel besluit nr. 1, van 2 september 1980, met betrekking tot de aftrekregeling voor de toepassing van de belasting over de toegevoegde waarde Uitvoering van de artikelen 12, § 1, en 48 § 2, van het Wetboek en van artikel 6 van het koninklijk besluit nr. 3, met betrekking tot de aftrekregeling voor de toepassing van de belasting over de toegevoegde waarde Officieuze coördinatie - Laatstelijk gewijzigd met ingang van 01.01.2014 (M.B. 04.12.2013, B.S. 09.12.2013)

## Art. 1
(De tekst van MB nr. 1, 1°, werd gewijzigd met ingang van 01.01.2014 (Art. 1, M.B. 04.12.2013, B.S. 09.12.2013, Ed. 2))

Voor de toepassing van de artikelen 12, § 1, en 48, § 2, van het Wetboek, worden niet als bedrijfsmiddelen aangemerkt:
1° klein materieel, klein gereedschap en kantoorbehoeften, wanneer de prijs of, bij ontstentenis van een prijs, de normale waarde, per in de handel gebruikelijke eenheid, lager is dan 1.000 euro ;
2° verpakkingsmiddelen, zelfs indien ze opnieuw kunnen worden gebruikt.

## Art. 2

Dit besluit vervangt het ministerieel besluit nr. 1 van 10 november 1970 met betrekking tot de aftrekregeling voor de toepassing van de belasting over de toegevoegde waarde.

## Art. 3

Dit besluit werkt terug tot 1 juli 1980.
