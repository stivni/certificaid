---
bron: https://www.cbn-cnc.be/nl/adviezen/boekhoudkundige-verwerking-van-de-voorzieningen-voor-risicos-en-kosten
datum: 1988-06-01
nummer: CBN-advies 107/8
provenance:
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/boekhoudkundige-verwerking-van-de-voorzieningen-voor-risicos-en-kosten
      sha256: d753bc74c5fd679b41db4da5185b9d315db89113f7fc81e0cf1c003ccd4d619d
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
    confirmed_at: '2026-05-11T17:05:20Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "G2: frontmatter themas-veld op regel 45 bevat ongeparseerde HTML-entity '&#039;' ('voorzieningen voor risico&#039;s en kosten') — ETL-bug, HTML niet gedecode. Body-tekst is volledig clean en goed leesbaar."
    layer1:
      file_size_chars: 2994
      flags: []
      heading_count: 0
      max_section_chars: 2994
      run_at: '2026-05-11T15:05:48Z'
      run_id: 20260511-150547
      status: pass
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-11T17:05:20Z'
      rationale: "G2: frontmatter themas-veld op regel 45 bevat ongeparseerde HTML-entity '&#039;' ('voorzieningen voor risico&#039;s en kosten') — ETL-bug, HTML niet gedecode. Body-tekst is volledig clean en goed leesbaar."
      concrete_problemen:
        - regel: 45
          categorie: G2
          type: other
          voorbeeld: voorzieningen voor risico&#039;s en kosten — HTML-entity &#039; niet gedecode in YAML
themas:
  - fiscale voorziening
  - voorziening
  - voorzieningen met een financieel karakter
  - voorzieningen voor risico&#039;s en kosten
---

# CBN-advies 107/8 - Boekhoudkundige verwerking van de voorzieningen voor risico's en kosten

Als gevolg van concrete vragen daaromtrent heeft de Commissie een algemeen onderzoek verricht met betrekking tot de boekhoudkundige verwerking van de voorzieningen voor risico's en kosten.

Zij is van oordeel dat in de regel de wijziging - van een boekjaar naar een ander - van de passiefpost *Voorzieningen voor risico's en kosten* moet overeenstemmen met de algebraïsche som van de verschillende rubrieken uit de resultatenrekening met betrekking tot voorzieningen voor risico's en kosten (toevoegingen, bestedingen, terugnemingen). Deze regel, die als dusdanig niet expliciet geformuleerd is in de reglementering, vloeit voort uit de interne logica van het algemeen rekeningenstelsel.

Op deze regel werden een drietal uitzonderingen vastgesteld.

Een eerste uitzondering slaat op de voorzieningen met een financieel karakter. Inderdaad, daar waar inzake bedrijfsresultaten de nodige rekeningen inzake voorzieningen zijn opgenomen, ontbreken die rekeningen (toevoeging, besteding, terugneming) wat de financiële resultaten betreft.

De Commissie is van oordeel dat deze uitzondering een vrij beperkte draagwijdte heeft, daar de voorzieningen met een financieel karakter uitzonderlijk zijn. Met de definitieve goedkeuring van het advies inzake verrichtingen, tegoeden en verplichtingen in deviezen[^1] zijn de hypotheses waarin voorzieningen met een financieel karakter kunnen of moeten worden gevormd nog beperkter dan voorheen[^2].

In het algemeen rekeningenstelsel komt een bijzondere rekening voor met betrekking tot de tenlasteneming van fiscale voorzieningen (rekening 6712 *Gevormde fiscale voorzieningen*) en een bijzondere rekening voor de terugnemingen van fiscale voorzieningen (rekening 7712). In de jaarrekening worden de gevormde fiscale voorzieningen evenwel samengevoegd met de andere bestanddelen van belastingen op het resultaat (post X, A) en de terugnemingen van fiscale voorzieningen met de regulariseringen van belastingen op het resultaat. Ook deze uitzondering heeft een beperkte draagwijdte daar de fiscale voorzieningen afzonderlijk op het passief verschijnen en daar sinds de wijziging in september 1983 van het jaarrekeningbesluit, de vorming van dergelijke voorzieningen bovendien slechts in een vrij beperkt aantal gevallen voorkomt[^3].

Een derde uitzondering slaat op de boekhoudkundige verwerking van lijfrente[^4].

In de drie hierboven beschreven hypotheses lijkt het de Commissie aangewezen dat passende informatie wordt verstrekt in de toelichting teneinde de vergelijking tussen enerzijds de mutaties in de balansposten en anderzijds de algebraïsche som van de betrokken posten uit de resultatenrekening, mogelijk te maken.

[^1]: Bulletin nr. 20, december 1987.

[^2]: Cf. Deel IX. «Risico's verbonden aan wisselposities» uit genoemd advies.

[^3]: Cf. de definitie van passiefpost VII, B.

[^4]: Cf. advies 149/1 opgenomen in Bulletin nr. 16, april 1985.
