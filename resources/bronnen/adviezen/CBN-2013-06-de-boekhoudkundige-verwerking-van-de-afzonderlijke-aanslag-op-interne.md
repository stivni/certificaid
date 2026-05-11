---
bron: https://www.cbn-cnc.be/nl/adviezen/de-boekhoudkundige-verwerking-van-de-afzonderlijke-aanslag-op-interne
datum: 2013-03-06
gerelateerde_adviezen:
  - datum: '2024-05-22'
    titel: Boekhoudkundige verwerking van de taks tot vergoeding der successierechten
    url: https://www.cbn-cnc.be/nl/adviezen/boekhoudkundige-verwerking-van-de-taks-tot-vergoeding-der-successierechten
  - datum: '2008-12-01'
    titel: Verwerking in de jaarrekening van de door de Vlaamse regering gecreëerde opleidingscheques
    url: https://www.cbn-cnc.be/nl/adviezen/verwerking-in-de-jaarrekening-van-de-door-de-vlaamse-regering-gecreeerde-opleidingscheques
nummer: CBN-advies 2013/6
provenance:
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/de-boekhoudkundige-verwerking-van-de-afzonderlijke-aanslag-op-interne
      sha256: b4049ba8b65296af7fe55261e3f7301d271578a23683196b0b39b803b32f232b
      version:
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: 3b788cd
    model:
    prompt_version:
  generated_at: '2026-05-11T13:15:12Z'
  stale: false
  stale_reason:
  trust:
    status: needs-rework
    confirmed_at: '2026-05-11T13:30:32Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "B4: het structuurlabel 'Boeking eerste jaar' op regel 70 staat als **bold** inline-tekst in plaats van als ##/###-heading. Het tweede structuurlabel op regel 77 is wel correct als ## heading. Inconsistente heading-behandeling in één document — mens zou beide als heading schrijven."
    layer1:
      status: pass
      run_id: 20260511-131513
      run_at: '2026-05-11T13:15:16Z'
      heading_count: 1
      max_section_chars: 3432
      file_size_chars: 3432
      flags: []
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-11T13:30:32Z'
      rationale: "B4: het structuurlabel 'Boeking eerste jaar' op regel 70 staat als **bold** inline-tekst in plaats van als ##/###-heading. Het tweede structuurlabel op regel 77 is wel correct als ## heading. Inconsistente heading-behandeling in één document — mens zou beide als heading schrijven."
      concrete_problemen:
        - regel: 70
          categorie: B4
          type: other
          voorbeeld: '**Boeking eerste jaar**'
themas:
  - bedrijfsbelastingen
  - interne pensioenvoorziening
  - pensioenvoorzieningen
---

# CBN-advies 2013/6 – De boekhoudkundige verwerking van de afzonderlijke aanslag op interne pensioenvoorzieningen

De Programmawet van 22 juni 2012[^1] onderwerpt interne pensioenvoorzieningen aan een éénmalige belastingheffing middels een afzonderlijke aanslag. De bedoelde voorzieningen zijn de voorzieningen die gevormd zijn ter uitvoering van aanvullende individuele pensioentoezeggingen bestaand op het einde van het laatste boekjaar met afsluitdatum vóór 1 januari 2012. De heffing bedraagt 1,75 procent van deze voorzieningen. De afzonderlijke aanslag wordt samen met de vennootschapsbelasting, de rechtspersonenbelasting of de belasting van niet-inwoners voor het aanslagjaar 2013 ingekohierd.

Onder bepaalde voorwaarden kan de belastingplichtige opteren om deze aanslag te spreiden over drie belastbare tijdperken. Het tarief van de aanslag wordt dan bepaald op 0,60 procent en is van toepassing op elk van de drie belastbare tijdperken. Zo zal de vennootschap die er voor opteert om de aanslag te spreiden uiteindelijk 1,80 procent van het totaal bedrag van de betreffende voorzieningen betalen. 

De afzonderlijke aanslag van 1,75 procent op de bestaande pensioentoezeggingen is een vaststaande schuld waarmee rekening moet worden gehouden overeenkomstig artikel 33 van het koninklijk besluit van 30 januari 2001 tot uitvoering van het Wetboek van vennootschappen, zelfs wanneer deze belasting nog niet werd ingekohierd. Deze schuld wordt uitgedrukt op de rekening 452 *Te betalen belastingen en taksen*. Deze belasting is een kost van de periode waarin deze belasting werd ingevoerd[^2] ongeacht wanneer deze belasting effectief zal worden betaald. 

Wanneer de onderneming ervoor opteert deze belasting niet in één keer te betalen maar te spreiden overeenkomstig de voorziene modaliteiten, zal de onderneming een bijkomende kost moeten boeken van 0,05 procent in het jaar waarin ze heeft uitgedrukt om de afzonderlijke aanslag te spreiden over drie aanslagjaren[^3]. 

In het Belgische boekhoudrecht wordt het schema van de resultatenrekening opgesteld in functie van de aard van de kosten. De afzonderlijke aanslag op de interne pensioenvoorzieningen is een niet-verrekenbare bedrijfsbelasting. De Commissie is van mening dat dergelijke kosten in de boekhouding moeten worden geregistreerd op de rekening 640 *Bedrijfsbelastingen*. 

**Boeking eerste jaar**

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 640 | Bedrijfsbelastingen | 1,75 | |
| aan | 452 | Te betalen belastingen en taksen | | 1,75 |

## Boeking in het jaar waarin wordt uitgedrukt om de afzonderlijke aanslag te spreiden over drie aanslagjaren

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 640 | Bedrijfsbelastingen | 0,05 | |
| aan | 452 | Te betalen belastingen en taksen | | 0,05 |

[^1]: Artikel 66 van de Programmawet van 22 juni 2012 (BS 28 juni 2012).

[^2]: Tien dagen na de publicatie van de Programmawet in het Belgisch Staatsblad.

[^3]: De Commissie merkt op dat deze kost van 0,05 procent zou kunnen worden aangemerkt als een kost die voortvloeit uit de gespreide betaling van de taks en bijgevolg eerder de aard heeft van een financiële kost. Echter, gelet op de specifieke kenmerken van deze taks is de Commissie van mening dat een boeking als diverse bedrijfskosten meer aangewezen is dan een boeking als financiële kosten.
