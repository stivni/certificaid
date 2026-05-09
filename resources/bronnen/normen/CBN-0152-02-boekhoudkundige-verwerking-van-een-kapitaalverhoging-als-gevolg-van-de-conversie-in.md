---
nummer: "CBN-advies 152/2"
datum: 1988-12-01
themas:
  - conversie in aandelen van obligaties uitgedrukt in vreemde valuta
  - deviezen
  - kapitaalverhoging
  - omrekeningskoers
  - wisselverrichting
bron: https://www.cbn-cnc.be/nl/adviezen/boekhoudkundige-verwerking-van-een-kapitaalverhoging-als-gevolg-van-de-conversie-in
bron_rol: interpretatief
chunk:
  level: 2
  type: '##'
  sub_strategy:
provenance:
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/boekhoudkundige-verwerking-van-een-kapitaalverhoging-als-gevolg-van-de-conversie-in
      sha256:
      version:
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: 3b788cd
    model:
    prompt_version:
  generated_at: '2026-05-09T20:20:16Z'
  stale: false
  stale_reason:
  trust:
    status: trusted
    qa_version: trust-rework-2
    confirmed_at: '2026-05-09T21:27:46Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: L1=pass
    agent_verdict_at: '2026-05-09T21:27:46Z'
    sample_pick: false
    sample_reviewed_at:
    sample_reviewed_by:
    layer1:
      verdict: pass
      heading_count: 0
      max_section_chars: 2577
      file_size_chars: 2577
      flags: []
      run_id: 20260509-212552
---
# CBN-advies 152/2 - Boekhoudkundige verwerking van een kapitaalverhoging als gevolg van de conversie in aandelen van obligaties uitgedrukt in Ecu of in andere vreemde valuta

Naar aanleiding van haar advies over de boekhoudkundige verwerking van vreemde valuta[^1] werden aan de Commissie vragen gesteld over de boeking van een kapitaalverhoging voortvloeiend uit de conversie in aandelen van obligaties uitgedrukt in Ecu of in een andere vreemde valuta. 

Naar het oordeel van de Commissie moet de conversie van obligaties in aandelen geanalyseerd worden als een betalingsmodaliteit van de schuld die de vennootschap tegenover de obligatiehouders heeft aangegaan. Een dergelijke conversie is assimileerbaar met een deviezenverrichting die dient geboekt met naleving van de regels beschreven in Deel III van genoemd advies 152.

Daaruit volgt dat de verrichting die erin bestaat obligaties uitgedrukt in deviezen te converteren in aandelen die het kapitaal van de vennootschap vertegenwoordigen, boekhoudkundig wordt verwerkt door als omrekeningskoers toe te passen de contantwisselkoers van de dag van de verrichting[^2]. Daarbij weze er tevens aan herinnerd dat wat de Ecu betreft, deze naar keuze van de onderneming hetzij als een afzonderlijke munt mag worden behandeld, hetzij mag worden omgerekend tot de munten waaruit hij is samengesteld[^3]. 

Daar de aldus bepaalde omrekeningskoers naar alle waarschijnlijkheid zal verschillen van de oorspronkelijke omrekeningskoers toegepast bij het boeken van de obligatieschuld, zal uit deze omrekening een positief of negatief resultaat voortvloeien dat als dusdanig moet worden geboekt. 

Voorbeeld : 

- Conversie op 1 april 1988 van een obligatie van vennootschap X met nominale waarde van 50 Ecu in aan aandeel van vennootschap X. 
- Omrekeningskoers: 1 Ecu = 43,60 BEF (omrekeningskoers bij veronderstelling bepaald met toepassing van de beginselen uitgedrukt in Deel III,B van advies 152). 
- Oorspronkelijke omrekeningskoers: 1 Ecu = 46 BEF. 
- Boekhoudkundig pari van het aandeel X: 1.000 BEF. 
- Boekingen (in BEF) : 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 1700 | Achtergestelde converteerbare lening, uitgegeven in Ecu | 2.300 | |
| aan | 100 | Geplaatst kapitaal | | 1.000 |
| | 11 | Uitgiftepremie | 1.180 | |
| | 754 | Wisselresultaten Ecu | 120 | |

[^1]: Bull. CBN nr. 20, december 1987.

[^2]: Zie over de concrete bepaling van de omrekeningskoers, de commentaren sub Deel III, B van genoemd advies 152.

[^3]: Cf. voetnoot op p. 34 van advies 152.
