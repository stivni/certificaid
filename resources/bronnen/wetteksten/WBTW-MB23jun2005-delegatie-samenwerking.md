---
tags: ["VI.C", "2.4"]
itaa-lex-sectie: "VI.C"
wet: "M.B. van 23 juni 2005, met betrekking tot de delegatie van de bevoegde autoriteit inzake de administratieve samenwerking op het gebied van de belasting over de toegevoegde waarde"
bron_rol: "itaa_lex"
status: "beschikbaar"
bijgewerkt: "23.06.2005"
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
    pipeline_version: 4126295-dirty
    model:
    prompt_version:
  generated_at: '2026-05-13T11:20:55Z'
  stale: false
  stale_reason:
  trust:
    status: needs-rework
    confirmed_at: '2026-05-13T11:23:37Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "'Enig artikel' staat nog steeds als plain text (regel 48) en niet als ## Enig artikel heading. Bestand heeft geen enkele heading-anker voor de centrale bepaling. De huidige transformers pakken dit niet aan: noch strip_mb_compilatie_cover noch fix_pdftotext_glue_bugs voegt 'Enig artikel' als heading in. Voor RAG-chunking is dit een structureel probleem — er is geen sectie-anker voor de enige inhoudelijke bepaling van het MB."
    layer1:
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-13T11:23:37Z'
      rationale: "'Enig artikel' staat nog steeds als plain text (regel 48) en niet als ## Enig artikel heading. Bestand heeft geen enkele heading-anker voor de centrale bepaling. De huidige transformers pakken dit niet aan: noch strip_mb_compilatie_cover noch fix_pdftotext_glue_bugs voegt 'Enig artikel' als heading in. Voor RAG-chunking is dit een structureel probleem — er is geen sectie-anker voor de enige inhoudelijke bepaling van het MB."
      concrete_problemen:
        - "Regel 48: 'Enig artikel' als plain text i.p.v. '## Enig artikel' heading"
        - 'Bestand bevat 0 ## headings — geen retrieval-anker voor de centrale bepaling'
---

# M.B. van 23 juni 2005, met betrekking tot de delegatie van de bevoegde autoriteit inzake de administratieve samenwerking op het gebied van de belasting over de toegevoegde waarde

*Bijgewerkt tot en met 23.06.2005 — gecoördineerde versie.*

Ministerieel besluit, van 23 juni 2005, met betrekking tot de delegatie van de bevoegde autoriteit inzake de administratieve samenwerking op het gebied van de belasting over de toegevoegde waarde Officieuze coördinatie, nr. 2 – Laatstelijk gewijzigd met ingang van 13.05.2010 (MB 27.04.2010, B.S. 03.05.2010)

## Enig artikel
(De tekst van het enig artikel werd gewijzigd met ingang van 13.05.2010 (MB 27.04.2010, B.S. 03.05.2010))

Voor de toepassing van de bepalingen van de Verordening (EG) nr. 1798/2003 van de Raad van 7 oktober 2003 betreffende de administratieve samenwerking op het gebied van de belasting over de toegevoegde waarde, wordt de door artikel 2, eerste lid, van deze Verordening aan de Minister van Financiën toegestane bevoegde autoriteit gedelegeerd aan de Voorzitter van het Directiecomité, met mogelijkheid tot overdracht van die volmacht aan de door hem aangeduide diensten of ambtenaren.
