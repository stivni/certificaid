---
bron: https://www.cbn-cnc.be/nl/adviezen/vervaardigingsprijs
datum: 1986-07-01
gerelateerde_adviezen:
  - datum: '2008-12-01'
    titel: Verwerking in de jaarrekening van de door de Vlaamse regering gecreëerde opleidingscheques
    url: https://www.cbn-cnc.be/nl/adviezen/verwerking-in-de-jaarrekening-van-de-door-de-vlaamse-regering-gecreeerde-opleidingscheques
  - datum: '1995-03-01'
    titel: Boekhoudkundige verwerking van afvalstoffen
    url: https://www.cbn-cnc.be/nl/adviezen/boekhoudkundige-verwerking-van-afvalstoffen
nummer: CBN-advies 126/5
themas:
  - financiële kosten
  - vervaardigingsprijs
bron_rol: interpretatief
chunk:
  level: 2
  type: '##'
  sub_strategy:
provenance:
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/vervaardigingsprijs
      sha256:
      version:
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: b4eac1f-dirty
    model:
    prompt_version:
  generated_at: '2026-05-12T23:37:36Z'
  stale: false
  stale_reason:
  trust:
    status: needs-rework
    confirmed_at: '2026-05-13T12:27:04Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "B3: dubbele page-title-heading op regels 49 en 51 (klassiek duplicate-title-patroon). D1: document eindigt abrupt mid-zin ('Toepassing daarvan zou de vervaardigingsprijs trouwens') zonder conclusie — het advies is duidelijk ingekort of afgekapt bij de scrape. Deze twee problemen samen maken de bron onbetrouwbaar voor RAG."
    layer1:
      status: pass
      run_id: 20260512-233938
      run_at: '2026-05-12T23:39:39Z'
      heading_count: 0
      max_section_chars: 1109
      file_size_chars: 1109
      flags: []
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-13T12:27:04Z'
      rationale: "B3: dubbele page-title-heading op regels 49 en 51 (klassiek duplicate-title-patroon). D1: document eindigt abrupt mid-zin ('Toepassing daarvan zou de vervaardigingsprijs trouwens') zonder conclusie — het advies is duidelijk ingekort of afgekapt bij de scrape. Deze twee problemen samen maken de bron onbetrouwbaar voor RAG."
      concrete_problemen:
        - regel: 49
          categorie: B3
          type: other
          voorbeeld: '# CBN advies 126-5 - Vervaardigingsprijs (regel 49 en 51 identiek)'
        - regel: 57
          categorie: D1
          type: abrupt-cutoff
          voorbeeld: Toepassing daarvan zou de vervaardigingsprijs trouwens
---
# CBN advies 126-5 - Vervaardigingsprijs
Aan de Commissie werd gevraagd of de financiële kosten die mogen worden opgenomen in de vervaardigingsprijs van voorraden en bestellingen in uitvoering, waarvan de produktie meer dan één jaar bestrijkt, alle daaraan verbonden financiële kosten omvatten of enkel de financiële kosten die betrekking hebben op de schulden op meer dan één jaar. 

Naar het oordeel van de Commissie doen de aard en termijn van de ontleende kapitalen in dat opzicht niets terzake. Doorslaggevende criteria zijn de band tussen de financiële kosten en het ontleende kapitaal enerzijds, en de te financieren activa, anderzijds, alsook de toerekening van de kosten aan de normale produktieperiode van deze voorraden of uitvoeringsperiode van deze bestellingen. 

Aangezien het hier om een mogelijkheid gaat, kunnen theoretisch gezien enkel de kosten worden opgenomen met betrekking tot schulden die contractueel meer dan één jaar bestrijken. De Commissie is evenwel van oordeel dat dergelijk criterium bedrijfseconomisch niet relevant is. Toepassing daarvan zou de vervaardigingsprijs trouwens
