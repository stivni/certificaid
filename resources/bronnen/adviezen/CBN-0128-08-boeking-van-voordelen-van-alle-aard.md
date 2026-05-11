---
nummer: CBN-advies 128/8
datum: 1993-02-01
themas:
  - bezoldiging
  - voordelen van alle aard
bron: https://www.cbn-cnc.be/nl/adviezen/boeking-van-voordelen-van-alle-aard
provenance:
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/boeking-van-voordelen-van-alle-aard
      sha256: 3377a5382b98d5739afd52a9d08f17c433ac02189e1042ca5c2664f306f5c9f9
      version:
  tooling:
    pipeline: tools/etl/scrape_cbn_advies.py
    pipeline_version: uncommitted
    model:
    prompt_version:
  generated_at: '2026-05-08T18:34:47Z'
  stale: false
  stale_reason:
  trust:
    status: needs-rework
    confirmed_at: '2026-05-11T12:04:41Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: 'D4 op L63, L65 en L67: het woord *Bezoldigingen * heeft een spatie vóór de sluitende asterisk — *Bezoldigingen * in plaats van *Bezoldigingen*. Dit is een consistent scraping-patroon dat drie keer optreedt en in elke markdown-renderer resulteert in niet-gesloten italic of letterlijk zichtbare asterisk.'
    layer1:
      status: pass
      run_id: 20260511-083333
      run_at:
      heading_count: 0
      max_section_chars: 1875
      file_size_chars: 1875
      flags: []
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-11T12:04:41Z'
      rationale: 'D4 op L63, L65 en L67: het woord *Bezoldigingen * heeft een spatie vóór de sluitende asterisk — *Bezoldigingen * in plaats van *Bezoldigingen*. Dit is een consistent scraping-patroon dat drie keer optreedt en in elke markdown-renderer resulteert in niet-gesloten italic of letterlijk zichtbare asterisk.'
      concrete_problemen:
        - regel: 63
          categorie: D4
          type: other
          voorbeeld: '...kwalificatie *Bezoldigingen *vallen...'
        - regel: 65
          categorie: D4
          type: other
          voorbeeld: '...in de rekening *Bezoldigingen *in de boekhouding...'
        - regel: 67
          categorie: D4
          type: other
          voorbeeld: '...in de rekening *Bezoldigingen *worden geboekt...'
gerelateerde_adviezen:
  - titel: Vergoedingen vrijwilligerswerk en verenigingswerk
    url: https://www.cbn-cnc.be/nl/adviezen/vergoedingen-vrijwilligerswerk-en-verenigingswerk
    datum: '2019-06-14'
  - titel: Provisie aanvullende dagen verlof – Arbeidsduurvermindering
    url: https://www.cbn-cnc.be/nl/adviezen/provisie-aanvullende-dagen-verlof-arbeidsduurvermindering
    datum: '2018-05-30'
  - titel: Boekhoudkundige verwerking van loontussenkomst door de overheid in hoofde van de werkgever (update)
    url: https://www.cbn-cnc.be/nl/adviezen/boekhoudkundige-verwerking-van-loontussenkomst-door-de-overheid-in-hoofde-van-de-werkgever
    datum: '2010-09-08'
  - titel: Loonmatiging (bezoldigingen van bestuurders)
    url: https://www.cbn-cnc.be/nl/adviezen/loonmatiging-bezoldigingen-van-bestuurders
    datum: '1995-03-01'
---

# CBN-advies 128/8 - Boeking van voordelen van alle aard

Aan de Commissie voor Boekhoudkundige Normen werd gevraagd hoe door de onderneming gedragen kosten die later fiscaal zouden worden beschouwd als «voordelen van alle aard» ten gunste van de personeelsleden, dienen te worden geboekt. 

Vooraf zij erop gewezen dat het Belgische boekhoudrecht het beginsel huldigt dat kosten naar hun aard moeten worden geboekt. 

Hoe door een onderneming gemaakte kosten in fiscaalrechtelijk opzicht worden gekwalificeerd heeft in beginsel geen belang voor hun boekhoudkundige verwerking. Dit geldt a fortiori ook wanneer de fiscale kwalificatie waarmee men rekening zou willen houden, uiteindelijk niet op de onderneming maar op een derde slaat. 

«Voordelen van alle aard» is een fiscaal begrip. Dit omvat niet alleen de kosten die in het boekhoudrecht niet onder de kwalificatie *Bezoldigingen *vallen, maar ook kosten die in fiscaal opzicht voordelen voor derden vertegenwoordigen die boekhoudkundig niet als kost in de jaarrekening van de onderneming worden uitgedrukt. Dat is bij voorbeeld het geval met een renteloos voorschot dat een onderneming aan een personeelslid zou toestaan. 

Kosten louter op grond van hun fiscale kwalificatie boeken strookt derhalve niet met de boekhoudreglementering. Naar het oordeel van de Commissie voor Boekhoudkundige Normen zullen de bedragen die op de persoonlijke fiscale fiches als bezoldigingen worden vermeld, derhalve niet volledig overeenstemmen met de bedragen die in de rekening *Bezoldigingen *in de boekhouding van de onderneming worden vermeld. 

Privé-uitgaven die normaliter door de werknemer zelf moeten worden gedragen, maar door de onderneming definitief in zijn plaats zijn betaald, moeten evenwel steeds in de rekening *Bezoldigingen *worden geboekt, omdat een dergelijke betaling als een bezoldiging moet worden beschouwd.
