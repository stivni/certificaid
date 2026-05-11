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
provenance:
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/vervaardigingsprijs
      sha256: 008e8c01ac1c4a8dc672d6eda2ea5765048ae1304d8ee04def94fced00021d24
      version:
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: 3b788cd
    model:
    prompt_version:
  generated_at: '2026-05-11T15:15:31Z'
  stale: false
  stale_reason:
  trust:
    status: needs-rework
    confirmed_at: '2026-05-11T15:15:32Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "D1: bestand eindigt abrupt mid-zin op regel 55 ('zou de vervaardigingsprijs trouwens') zonder afronding — duidelijke afkapfout in de extractie. Geen voetnoten, geen slotconclusie. Body is inhoudelijk onvolledig."
    layer1:
      file_size_chars: 1111
      flags: []
      heading_count: 0
      max_section_chars: 1111
      run_at: '2026-05-11T15:05:48Z'
      run_id: 20260511-150547
      status: pass
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-11T15:15:32Z'
      rationale: "D1: bestand eindigt abrupt mid-zin op regel 55 ('zou de vervaardigingsprijs trouwens') zonder afronding — duidelijke afkapfout in de extractie. Geen voetnoten, geen slotconclusie. Body is inhoudelijk onvolledig."
      concrete_problemen:
        - regel: 55
          categorie: D1
          type: abrupt-cutoff
          voorbeeld: De methode moet ... zou de vervaardigingsprijs trouwens
themas:
  - financiële kosten
  - vervaardigingsprijs
---

# CBN advies 126-5 - Vervaardigingsprijs

Aan de Commissie werd gevraagd of de financiële kosten die mogen worden opgenomen in de vervaardigingsprijs van voorraden en bestellingen in uitvoering, waarvan de produktie meer dan één jaar bestrijkt, alle daaraan verbonden financiële kosten omvatten of enkel de financiële kosten die betrekking hebben op de schulden op meer dan één jaar. 

Naar het oordeel van de Commissie doen de aard en termijn van de ontleende kapitalen in dat opzicht niets terzake. Doorslaggevende criteria zijn de band tussen de financiële kosten en het ontleende kapitaal enerzijds, en de te financieren activa, anderzijds, alsook de toerekening van de kosten aan de normale produktieperiode van deze voorraden of uitvoeringsperiode van deze bestellingen. 

Aangezien het hier om een mogelijkheid gaat, kunnen theoretisch gezien enkel de kosten worden opgenomen met betrekking tot schulden die contractueel meer dan één jaar bestrijken. De Commissie is evenwel van oordeel dat dergelijk criterium bedrijfseconomisch niet relevant is. Toepassing daarvan zou de vervaardigingsprijs trouwens
