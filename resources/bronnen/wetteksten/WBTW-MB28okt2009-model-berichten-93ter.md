---
tags: ["VI.C", "2.4"]
itaa-lex-sectie: "VI.C"
wet: "M.B. van 28 oktober 2009, tot bepaling van het model der berichten en kennisgevingen als bedoeld in de artikelen 93ter en 93quinquies van het Wetboek van de belasting over de toegevoegde waarde en in de artikelen 433 en 435 van het Wetboek van de inkomstenbelastingen 1992"
bron_rol: "itaa_lex"
status: "beschikbaar"
bijgewerkt: "28.10.2009"
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
    pipeline_version: d4b4775-dirty
    model:
    prompt_version:
  generated_at: '2026-05-13T11:04:32Z'
  stale: false
  stale_reason:
  trust:
    status: needs-rework
    confirmed_at: '2026-05-13T11:05:03Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "Hoofdtekst (Art. 1-5) is schoon, maar regels 78-82 bevatten nog steeds drie plain-text labels 'Bijlage 1' / 'Bijlage 2' / 'Bijlage 3' zonder ##-heading en zonder inhoud. De bijlagen (modelformulieren) zijn niet meegekomen uit de PDF maar de labels wel — dit oogt onafgemaakt en is bovendien inhoudelijk problematisch: het MB-doel is precies om deze modelberichten voor te schrijven, en zonder bijlagen mist de bron zijn kerncontent. De drie nieuwe transformers raken dit specifieke artefact niet — strip_empty_trailing_headings werkt op '## Art.' patronen, niet op plain-text 'Bijlage' labels."
    layer1:
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-13T11:05:03Z'
      rationale: "Hoofdtekst (Art. 1-5) is schoon, maar regels 78-82 bevatten nog steeds drie plain-text labels 'Bijlage 1' / 'Bijlage 2' / 'Bijlage 3' zonder ##-heading en zonder inhoud. De bijlagen (modelformulieren) zijn niet meegekomen uit de PDF maar de labels wel — dit oogt onafgemaakt en is bovendien inhoudelijk problematisch: het MB-doel is precies om deze modelberichten voor te schrijven, en zonder bijlagen mist de bron zijn kerncontent. De drie nieuwe transformers raken dit specifieke artefact niet — strip_empty_trailing_headings werkt op '## Art.' patronen, niet op plain-text 'Bijlage' labels."
      concrete_problemen:
        - "Regels 78, 80, 82: 'Bijlage 1', 'Bijlage 2', 'Bijlage 3' als plain-text labels zonder ##-prefix"
        - Bijlagen-inhoud (modelberichten 93ter/93quinquies en 433/435) ontbreekt volledig — kerncontent van het MB
        - "Lege trailing-labels zouden door strip_empty_trailing_headings opgeruimd moeten worden (uitbreiding nodig: ook 'Bijlage N' patroon)"
---

# M.B. van 28 oktober 2009, tot bepaling van het model der berichten en kennisgevingen als bedoeld in de artikelen 93ter en 93quinquies van het Wetboek van de belasting over de toegevoegde waarde en in de artikelen 433 en 435 van het Wetboek van de inkomstenbelastingen 1992

*Bijgewerkt tot en met 28.10.2009 — gecoördineerde versie.*

Ministerieel besluit, van 28 oktober 2009, tot bepaling van het model der berichten en kennisgevingen als bedoeld in de artikelen 93ter en 93quinquies van het Wetboek van de belasting over de toegevoegde waarde en in de artikelen 433 en 435 van het Wetboek van de inkomstenbelastingen 1992 Uitvoering van de artikelen 93ter en 93quinquies van het Btw-Wetboek.
Officieuze coördinatie

Dit ministerieel besluit werd opgeheven met ingang van 06.07.2020 bij: 22 JUNI 2020 - Koninklijk besluit tot uitvoering van de artikelen 93ter tot 93quinquies van het wetboek van de belasting over de toegevoegde waarde, de artikelen 412bis, 433 tot 435 van het wetboek van de inkomstenbelastingen 1992, de artikelen 35 tot 37, 43 tot 45 en 47 van het wetboek van de minnelijke en gedwongen invordering van fiscale en niet-fiscale schuldvorderingen en de artikelen 157 tot 159 en 161 van de programmawet (i) van 29 maart 2012, inzake het enotariaat (B.S. 26.06.2020, pg. 47298, Numac : 2019041722)

## Art. 1

De berichten bedoeld in de artikelen 93ter van het BTW-Wetboek en 433 WIB 92 worden opgemaakt overeenkomstig het model dat voorkomt in bijlage 1 bij dit besluit.

## Art. 2

De berichten bedoeld in de artikelen 93ter van het BTW-Wetboek en 433 WIB 92 en die een schip of een vaartuig tot voorwerp hebben worden opgemaakt overeenkomstig het model dat voorkomt in bijlage 2 bij dit besluit.

## Art. 3

De kennisgevingen bedoeld in de artikelen 93quinquies van het BTW-Wetboek en 435 WIB 92 worden opgemaakt overeenkomstig het model dat voorkomt in bijlage 3 bij dit besluit.

## Art. 4

Het ministerieel besluit van 26 februari 2007 tot bepaling van het model der berichten en kennisgevingen als bedoeld in de artikelen 93ter en 93quinquies van het Wetboek van de belasting over de toegevoegde waarde en in de artikelen 433 en 435 van het Wetboek van de inkomstenbelastingen 1992 wordt opgeheven.

## Art. 5

Dit besluit treedt in werking op 15 november 2009.

Bijlage 1

Bijlage 2

Bijlage 3
