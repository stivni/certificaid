---
bron: https://www.cbn-cnc.be/nl/adviezen/in-aanmerking-te-nemen-termijn-contractuele-termijn-of-nog-te-lopen-termijn
datum: 1980-01-01
gerelateerde_adviezen:
  - datum: '1980-01-01'
    titel: Het begrip &quot;financiële instelling&quot;
    url: https://www.cbn-cnc.be/nl/adviezen/het-begrip-financiele-instelling
nummer: CBN-advies 120/2
provenance:
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/in-aanmerking-te-nemen-termijn-contractuele-termijn-of-nog-te-lopen-termijn
      sha256: 250bb526c3f37563d22490c4933153d5dccd5798ededcbf5ec312e8160465477
      version:
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: 3b788cd
    model:
    prompt_version:
  generated_at: '2026-05-11T13:15:10Z'
  stale: false
  stale_reason:
  trust:
    status: needs-rework
    confirmed_at: '2026-05-11T13:16:02Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "F1/G2: frontmatter regel 6 bevat ongedecodeëerd HTML-entity '&quot;' in gerelateerde_adviezen titel ('Het begrip &quot;financiële instelling&quot;'). Body zelf is schoon — italic '*Thesauriebeleggingen*' correct gesloten, geen andere artefacten. De HTML-entity maakt metadata onbetrouwbaar voor downstream verwerking."
    layer1:
      status: pass
      run_id: 20260511-131513
      run_at: '2026-05-11T13:15:14Z'
      heading_count: 0
      max_section_chars: 1126
      file_size_chars: 1126
      flags: []
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-11T13:16:02Z'
      rationale: "F1/G2: frontmatter regel 6 bevat ongedecodeëerd HTML-entity '&quot;' in gerelateerde_adviezen titel ('Het begrip &quot;financiële instelling&quot;'). Body zelf is schoon — italic '*Thesauriebeleggingen*' correct gesloten, geen andere artefacten. De HTML-entity maakt metadata onbetrouwbaar voor downstream verwerking."
      concrete_problemen:
        - regel: 6
          categorie: G2
          type: other
          voorbeeld: 'titel: Het begrip &quot;financiële instelling&quot;'
themas:
  - beschikbare waarden
  - contractuele termijn
  - nog te lopen termijn
  - termijn
  - thesauriebelegging
---

# CBN-advies 120/2 - In aanmerking te nemen termijn - Contractuele termijn of nog te lopen termijn

Wanneer de overblijvende duur van een tegoed op een financiële instelling, met een contractuele termijn van meer dan één maand, op de balansdatum geen maand meer bedraagt, mag - of moet - dit tegoed dan uit de rubriek *Thesauriebeleggingen* worden gehaald en onder de rubriek *Beschikbare waarden* worden ingeschreven ? 

De definitie van beide rubrieken in het koninklijk besluit van 8 oktober 1976 geeft geen duidelijk antwoord op de vraag of men voor dergelijke tegoeden op financiële instellingen rekening moet houden met de contractuele duur, dan wel met de overblijvende duur. De Commissie is van oordeel dat beide stellingen opgaan, en dat de onderneming zelf een beleidslijn moet uitstippelen, op grond van het algemene beginsel dat in artikel 3 van het besluit is vervat. Daarbij zal de onderneming rekening moeten houden met het feit dat dergelijke tegoeden bestemd zijn om op korte termijn te worden aangesproken voor de dekking van haar thesauriebehoeften, dan wel om voor een nieuwe termijn te worden herbelegd.
