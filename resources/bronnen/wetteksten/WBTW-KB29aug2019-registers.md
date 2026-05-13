---
tags: ["VI.B", "2.4"]
itaa-lex-sectie: "VI.B"
wet: "K.B. van 29 augustus 2019, tot uitvoering van artikel 85, § 2, derde lid van het Wetboek van de belasting over de toegevoegde waarde met betrekking tot de opmaak van innings- en invorderingsregisters"
bron_rol: "itaa_lex"
status: "beschikbaar"
bijgewerkt: "29.08.2019"
bron: "Afgesplitst uit Fisconet-compilatie (pdftotext_compilatie_btw)"
chunk:
  level: 2
  type: "Art."
  sub_strategy:
provenance:
  inputs:
    - id: resources/raw/wetteksten/btw-kbs/WBTW-KB-compilatie.pdf
      sha256: 5f1bad7278d1f8e1f5c00efb5d792f61342d3f7a14a7950caca2937924bfa91c
      version: 06.03.2020
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
    rationale: "Hoofdtekst (3 artikelen) is schoon, maar het 'Recent opgeheven of vervangen koninklijke besluiten' overzicht onderaan (regels 63-71) bevat nog steeds kolom-bleed artefacten: 'Bijw. 04/01.01.2020', 'Bijw. 03/12.07.2019', '(Opgeheven)', '(vervangen)' staan midden in beschrijvingen ingebed alsof het lopende tekst is. Dit was duidelijk een meerkoloms-tabel in de PDF die verkeerd is geconcateneerd. De drie nieuwe transformers raken dit specifieke artefact niet (geen running-header, geen 'Bijwerkingen'-appendix, geen lege Art.-heading)."
    layer1:
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-13T11:17:05Z'
      rationale: "Hoofdtekst (3 artikelen) is schoon, maar het 'Recent opgeheven of vervangen koninklijke besluiten' overzicht onderaan (regels 63-71) bevat nog steeds kolom-bleed artefacten: 'Bijw. 04/01.01.2020', 'Bijw. 03/12.07.2019', '(Opgeheven)', '(vervangen)' staan midden in beschrijvingen ingebed alsof het lopende tekst is. Dit was duidelijk een meerkoloms-tabel in de PDF die verkeerd is geconcateneerd. De drie nieuwe transformers raken dit specifieke artefact niet (geen running-header, geen 'Bijwerkingen'-appendix, geen lege Art.-heading)."
      concrete_problemen:
        - "Regel 65: 'Koninklijk besluit nr. 39, van 17 oktober 1980, tot regeling van de Bijw. 04/01.01.2020 toepassingsmodaliteiten van artikel 93duodecies van het Wetboek van de (Opgeheven) belasting over de toegevoegde waarde.' — kolom-bleed midden in zin"
        - "Regel 67: idem voor KB 47 met 'Bijw. 03/12.07.2019' en '(Opgeheven)' mid-zin"
        - "Regel 69: idem voor KB 50 met 'Bijw. 03/01.01.2020' en '(vervangen)' mid-zin"
        - "Regel 71: idem voor KB 52 met 'Bijw. 02/01.01.2020' en '(vervangen)-' mid-zin"
        - "Regel 63: 'Recent opgeheven of vervangen koninklijke besluiten.' als plain text zonder ##-heading"
        - "Regel 48: 'Officieuze cöordinatie' bevat OCR-typo (mogelijk source)"
---

# K.B. van 29 augustus 2019, tot uitvoering van artikel 85, § 2, derde lid van het Wetboek van de belasting over de toegevoegde waarde met betrekking tot de opmaak van innings- en invorderingsregisters

*Bijgewerkt tot en met 29.08.2019 — gecoördineerde versie.*

Koninklijk besluit van 29 augustus 2019 tot uitvoering van artikel 85, § 2, derde lid van het Wetboek van de belasting over de toegevoegde waarde met betrekking tot de opmaak van innings- en invorderingsregisters (Uitvoering van artikel 85, § 2, derde lid, van het Wetboek van de Btw) Officieuze cöordinatie – KB ingevoerd, met ingang van 13.09.2019 (KB 29.08.2019, B.S. 13.09.2019, pg. 86194)

## Art. 1

De belastingschuld wordt op naam van de belastingschuldige opgenomen in een innings- en invorderingsregister bedoeld in artikel 85 van het Wetboek.
Indien de belastingschuldige overleden is, wordt de belastingschuld opgenomen in een innings- en invorderingsregister op zijn naam, voorafgegaan door het woord "Nalatenschap".

## Art. 2

Dit besluit treedt in werking de dag waarop het in het Belgisch Staatsblad wordt bekendgemaakt.

## Art. 3

De minister bevoegd voor Financiën is belast met de uitvoering van dit besluit.

Recent opgeheven of vervangen koninklijke besluiten.

* Koninklijk besluit nr. 39, van 17 oktober 1980, tot regeling van de Bijw. 04/01.01.2020 toepassingsmodaliteiten van artikel 93duodecies van het Wetboek van de (Opgeheven) belasting over de toegevoegde waarde. (Opgeheven bij W 13.04.2019)

* Koninklijk besluit nr. 47, van 25 februari 1996, tot regeling van de controle Bijw. 03/12.07.2019 van de voldoening van de BTW verschuldigd ter zake van de levering, (Opgeheven) intracommunautaire verwerving en invoer van vervoermiddelen, in de zin van artikel 8bis, § 2, 1°, van het Wetboek. (Opgeheven bij KB 28.06.2019)

* Koninklijk besluit nr. 50, van 9 december 2009, met betrekking tot de BTW- Bijw. 03/01.01.2020 opgave van de intracommunautaire handelingen. (vervangen)

* Koninklijk besluit nr. 52, van 29 december 1992, met betrekking tot de Bijw. 02/01.01.2020 vrijstellingen betreffende de intracommunautaire leveringen van goederen en (vervangen)- de ermee gelijkgestelde handelingen, alsook betreffende de intracommunautaire verwervingen van goederen, op het stuk van de belasting over de toegevoegde waarde. (Vervangen bij KB 11.12.2019)
