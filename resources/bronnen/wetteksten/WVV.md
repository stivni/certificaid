---
bijgewerkt: 24.12.2025
bron: ejustice.just.fgov.be (gecoördineerde versie)
bron_rol: itaa_lex
chunk:
  level: 6
  sub_strategy: per_definitieblok
  type: Art.
itaa-lex-sectie: XV
provenance:
  inputs:
    - id: resources/raw/wetteksten/WVV.pdf
      sha256: 961fd384c0aa3d4d139917d7ede8fa8b9f4f126d5ed47025c5735c9b6156ad96
      version: 24.12.2025
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: 11f9196
    model:
    prompt_version:
  generated_at: '2026-05-11T16:34:49Z'
  stale: false
  stale_reason:
  trust:
    status: needs-rework
    confirmed_at: '2026-05-11T16:56:58Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: 'D2: het bestand bevat slechts 1 artikel (Art. 18:8, 58 regels totaal) terwijl layer1.heading_count 1866 aangeeft voor de verwachte volledige WVV. De volledige wet ontbreekt — vrijwel alle artikelen zijn niet geëxtraheerd. De ene aanwezige artikeltekst is correct opgemaakt, maar het bestand is inhoudelijk onbruikbaar voor RAG.'
    layer1:
      file_size_chars: 1571172
      flags: []
      heading_count: 1866
      max_section_chars: 13139
      run_at: '2026-05-11T13:40:49Z'
      run_id: 20260511-134044
      status: pass
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-11T16:56:58Z'
      rationale: 'D2: het bestand bevat slechts 1 artikel (Art. 18:8, 58 regels totaal) terwijl layer1.heading_count 1866 aangeeft voor de verwachte volledige WVV. De volledige wet ontbreekt — vrijwel alle artikelen zijn niet geëxtraheerd. De ene aanwezige artikeltekst is correct opgemaakt, maar het bestand is inhoudelijk onbruikbaar voor RAG.'
      concrete_problemen:
        - regel: 54
          categorie: D2
          type: missing-section
          voorbeeld: Bestand eindigt na Art. 18:8; layer1.heading_count=1866 maar slechts 1 artikel aanwezig.
status: beschikbaar
tags:
  - XV
  - '1.5'
  - '3.1'
  - '3.2'
wet: Wetboek van vennootschappen en verenigingen 23/03/2019
---

# Wetboek van vennootschappen en verenigingen 23/03/2019

*Bijgewerkt tot en met 24.12.2025 — gecoördineerde versie.*

## Art. 18:8

In afwijking van de artikelen 1:5, § 3, en 2:6 wordt het overeenkomstig dit wetboek opgerichte Europees economisch samenwerkingsverband geacht geen rechtspersoonlijkheid te bezitten voor de toepassing van de inkomstenbelastingen.  Het Europees economisch samenwerkingsverband wordt als dusdanig niet aan deze belastingen onderworpen. De uitgekeerde of niet uitgekeerde winst of baten evenals de opnemingen door de leden worden als winst of baten van de desbetreffende leden beschouwd en ten hunne name belast overeenkomstig het stelsel dat op hen van toepassing is.  Deze winst of baten worden geacht te zijn betaald of toegekend aan de leden op de datum van afsluiting van het boekjaar waarop zij betrekking hebben; het aandeel in de niet uitgekeerde winst of baten wordt voor elk lid vastgesteld overeenkomstig de bepalingen van de overeenkomst of, bij gebrek daaraan, volgens het hoofdelijk aandeel.    (NOTA : Inwerkingtreding van artikelen 3:1, § 3, 5° ; 3:4, L 1, 4° ; 3:8, § 1er, L 2, 2° ; 3:21, 4° ; 3:72, 3° ; 3:76, 3° ; 6:1, § 3 ; 8:2, 8:3 et 8:6 vastgesteld op 15-07-2019 door KB 2019-07-03/02, art. 1)  (NOTA : Inwerkingtreding van artikelen 31, L 1; 42, § 2 vastgesteld op 15-07-2019 door KB 2019-07-03/02, art. 1)
