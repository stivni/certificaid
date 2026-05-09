---
tags: ["VI.C", "2.4"]
itaa-lex-sectie: "VI.C"
wet: "M.B. nr. 12 van 28 augustus 1973, met betrekking tot de automatische weegtoestellen te gebruiken in slachthuizen voor de toepassing van de belasting over de toegevoegde waarde"
bron_rol: "itaa_lex"
status: "beschikbaar"
bijgewerkt: "28.08.1973"
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
    pipeline_version: 7a134f4
    model:
    prompt_version:
  generated_at: '2026-05-09T16:15:20Z'
  stale: false
  stale_reason:
  trust:
    status: trusted
    qa_version: trust-rework-2
    confirmed_at: '2026-05-09T21:27:46Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "L1=pass; L1.5=improvement (Auto-synthesized: heading-injection (inject_wbtw_headings.py) — staging is structureel beter dan resources-versie.); L2=trusted (ETL-fix toegepast: inject_wbtw_headings.py heeft TOC-strip + Artikel-N → ## Art. heading-injectie + AFDELING-normalisatie uitgevoerd. Eerdere needs-rework op 'missing-section' opgeheven.)"
    agent_verdict_at: '2026-05-09T21:27:46Z'
    sample_pick: false
    sample_reviewed_at:
    sample_reviewed_by:
    layer1:
      verdict: pass
      heading_count: 2
      max_section_chars: 1597
      file_size_chars: 2218
      flags: []
      run_id: 20260509-212552
    layer1_5_diff:
      verdict: improvement
      rationale: 'Auto-synthesized: heading-injection (inject_wbtw_headings.py) — staging is structureel beter dan resources-versie.'
      kritieke_observaties: []
      auto: true
      run_id: trust-rework-2
    layer2_content:
      verdict: needs-rework
      rationale: 'Idem familie-patroon: inhoud OK, geen ##-headings ondanks chunk.level=2.'
      problemen:
        - regel: 0
          type: missing-section
          voorbeeld: Artikel 1 en 2 als plaintext-centering ipv heading
      sterkte:
        - Volledige tekst inclusief slotartikel aanwezig
      auto: false
      run_id: qa-batch-W4
---

# M.B. nr. 12 van 28 augustus 1973, met betrekking tot de automatische weegtoestellen te gebruiken in slachthuizen voor de toepassing van de belasting over de toegevoegde waarde

*Bijgewerkt tot en met 28.08.1973 — gecoördineerde versie.*

Ministerieel besluit nr. 12, van 28 augustus 1973, met betrekking tot de
automatische weegtoestellen te gebruiken in slachthuizen voor de toepassing
van de belasting over de toegevoegde waarde
Uitvoering van artikel 54 van het Wetboek en van artikel 1 van het koninklijk besluit nr. 27.
Officieuze coördinatie

## Art. 1

Het automatisch weegtoestel bedoeld in artikel 1, § 4, van het koninklijk besluit nr. 27 van 26 juni 1973, is een
weegwerktuig dat aan de volgende voorwaarden moet voldoen:
1°     behoren tot een model dat is goedgekeurd en de ijk ondergaan hebben volgens de voorschriften
       betreffende de weegwerktuigen, in toepassing van de vigerende wetgeving over de meetwerktuigen;
2°     een maximaal weegvermogen hebben van minstens 300 kg wanneer het uitsluitend bestemd is voor
       het wegen van varkens, en van minstens 500 kg in de andere gevallen;
3°     voorzien zijn van een aanwijs- en afdrukinrichting waarvan het schaaldeel 500 g bedraagt wanneer het
       uitsluitend bestemd is voor het wegen van varkens, en 1 kg in de andere gevallen;
4°     geschikt zijn voor het wegen van hangende lasten.
Bovendien, moet de afdrukinrichting, gelijktijdig op een individuele weegstrook voor iedere weging en op een
controlestrook waarop de opeenvolgende wegingen worden opgenomen, de volgende inlichtingen afdrukken:
-      de naam en het adres van het slachthuis;
-      het nummer van het weegwerktuig wanneer er verscheidene in gebruik zijn;
-      een jaarlijks volgnummer;
-      de datum van de weging;
-      de naam en het adres van de eigenaar;
-      de diersoort en het nummer van het merkteken tot individualisering;
-      het nettogewicht van het geslachte dier;
-      ieder ander gegeven door of vanwege de Minister van Financiën te bepalen.
Iedere controlestrook mag slechts de inlichtingen omvatten aangaande de wegingen die gedurende maximaal
veertien dagen werden verricht.

## Art. 2

Dit besluit treedt in werking op 1 oktober 1973.
