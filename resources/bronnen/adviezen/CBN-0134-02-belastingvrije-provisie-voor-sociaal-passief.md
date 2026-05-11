---
bron: https://www.cbn-cnc.be/nl/adviezen/belastingvrije-provisie-voor-sociaal-passief
datum: 1983-04-10
gerelateerde_adviezen:
  - datum: '1981-12-01'
    titel: Voorzieningen voor de schulden ten opzichte van het personeel bij sluiting van de onderneming
    url: https://www.cbn-cnc.be/nl/adviezen/voorzieningen-voor-de-schulden-ten-opzichte-van-het-personeel-bij-sluiting-van-de
nummer: CBN-advies 134/2
provenance:
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/belastingvrije-provisie-voor-sociaal-passief
      sha256: 938d859daac2fd8d5c51f728bb891bcb6c39abf197dd7efcb74f735ab792253e
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
    confirmed_at: '2026-05-11T15:15:33Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: HTML-entiteit '&#039;' in frontmatter themas-veld op L55 ('voorzieningen voor risico&#039;s en kosten') — scraper heeft de HTML-entiteit niet gedecodeerd naar het correcte apostrof-teken. Body is schoon. Eén artefact maar in machine-leesbare metadata en dus ETL-fixeerbaar. Bevestiging van eerder layer2-verdict.
    layer1:
      file_size_chars: 2126
      flags: []
      heading_count: 0
      max_section_chars: 2126
      run_at: '2026-05-11T15:05:49Z'
      run_id: 20260511-150547
      status: pass
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-11T15:15:33Z'
      rationale: HTML-entiteit '&#039;' in frontmatter themas-veld op L55 ('voorzieningen voor risico&#039;s en kosten') — scraper heeft de HTML-entiteit niet gedecodeerd naar het correcte apostrof-teken. Body is schoon. Eén artefact maar in machine-leesbare metadata en dus ETL-fixeerbaar. Bevestiging van eerder layer2-verdict.
      concrete_problemen:
        - regel: 55
          categorie: G2
          type: other
          voorbeeld: voorzieningen voor risico&#039;s en kosten (HTML-entiteit niet gedecodeerd)
themas:
  - afdanking van personeel
  - belastingen
  - belastingvrije provisie
  - fiscale steunmaatregel
  - provisie
  - provisie voor sociaal passief
  - voorziening
  - sociaal passief
  - reserves
  - voorzieningen voor risico&#039;s en kosten
  - vrijgestelde reserves
---

# CBN-advies 134/2 - Belastingvrije provisie voor sociaal passief

Door het koninklijk besluit nr. 7 van 15 februari 1982[^1] tot wijziging van het WIB met betrekking tot het sociaal passief wordt aan bepaalde ondernemingen de mogelijkheid verleend om bij de aanwerving van bijkomend personeel een belastingvrije «provisie» te vormen voor de kosten die de onderneming moet dragen in geval van afdanking van werknemers. Aan de Commissie werd gevraagd hoe deze «provisie» in de jaarrekening moet worden geboekt en of zij boekhoudkundig te beschouwen is als een reserve dan wel als een voorziening voor risico's en lasten in de zin van het besluit van 8 oktober 1976. 

Naar het oordeel van de Commissie moet ter zake een onderscheid worden gemaakt. 

Werd bijkomend personeel aangeworven zonder dat het ontslag van dit personeel binnen een afzienbare tijd wordt overwogen of een beslissing in die zin als waarschijnlijk voorkomt dan mag de «provisie» die krachtens het koninklijk besluit nr. 7 mag worden gevormd boekhoudkundig niet als een voorziening voor risico's en lasten worden beschouwd. Zoals de Commissie heeft aangeduid in haar advies 107/4[^2] vloeit uit de definitie van voorzieningen in het besluit van 8 oktober 1976 voort dat een loutere mogelijkheid niet de basis kan zijn voor de boeking van een voorziening. Zoals in het geval van algemene risico's kan daaraan slechts tegemoet gekomen worden door de vorming van reserves. De belastingvrije «provisie» zal derhalve worden geboekt onder de post III. C. *Vrijgestelde reserves*. De overboeking naar de vrijgestelde reserves geschiedt via de staat van de verwerking van de resultaten. 

Wanneer het evenwel vaststaat of waarschijnlijk is dat het personeelsbestand binnen afzienbare tijd zal worden teruggebracht via ontslagen tot de toestand vóór de aanwerving dan is de toestand verschillend. In dat geval moet de belastingvrije «provisie» voor de kosten verbonden met de afdanking worden beschouwd als een echte voorziening voor risico's en lasten die ook als zodanig moet worden geboekt.

[^1]: Belgisch Staatsblad, 20 februari 1982.

[^2]: Bull. CBN, nr. 9.
