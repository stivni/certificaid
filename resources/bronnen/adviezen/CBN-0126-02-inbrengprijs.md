---
nummer: CBN-advies 126/2
datum: 1980-06-01
themas:
  - inbreng
  - inbrengprijs
  - kosten van oprichting en kapitaalverhoging
  - oprichtingskosten
bron: https://www.cbn-cnc.be/nl/adviezen/inbrengprijs
provenance:
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/inbrengprijs
      sha256: b780564a7b1f0eed2709b1d3d3858fbf8e12a265541a5de2098929a68176c846
      version:
  tooling:
    pipeline: tools/etl/scrape_cbn_advies.py
    pipeline_version: uncommitted
    model:
    prompt_version:
  generated_at: '2026-05-08T18:34:35Z'
  stale: false
  stale_reason:
  trust:
    status: needs-rework
    confirmed_at: '2026-05-11T11:57:45Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "D4: regel 61 bevat malgevormde italic-opmaak '*Oprichtingskosten *als *Kosten van oprichting en kapitaalverhoging*' — spatie vóór tweede asterisk sluit de eerste italic niet in CommonMark, waardoor drie asterisks onbedoeld interageren. De bedoeling is duidelijk (twee aparte term-italics), maar de rendering is incorrect. Drie voetnoten correct. Rest volledig en correct."
    layer1:
      status: pass
      run_id: 20260511-083333
      run_at:
      heading_count: 0
      max_section_chars: 1653
      file_size_chars: 1653
      flags: []
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-11T11:57:45Z'
      rationale: "D4: regel 61 bevat malgevormde italic-opmaak '*Oprichtingskosten *als *Kosten van oprichting en kapitaalverhoging*' — spatie vóór tweede asterisk sluit de eerste italic niet in CommonMark, waardoor drie asterisks onbedoeld interageren. De bedoeling is duidelijk (twee aparte term-italics), maar de rendering is incorrect. Drie voetnoten correct. Rest volledig en correct."
      concrete_problemen:
        - regel: 61
          categorie: D4
          type: other
          voorbeeld: geboekt in de post *Oprichtingskosten *als *Kosten van oprichting en kapitaalverhoging*
gerelateerde_adviezen:
  - titel: Boekhoudkundige verwerking van de inbreng van een bedrijfstak of van een algemeenheid (update) [ONTWERP]
    url: https://www.cbn-cnc.be/nl/adviezen/boekhoudkundige-verwerking-van-de-inbreng-van-een-bedrijfstak-of-van-een-algemeenheid
    datum: '2023-08-29'
  - titel: Overgang van een kapitaalhoudende coöperatieve vennootschap naar een kapitaalloze vennootschap
    url: https://www.cbn-cnc.be/nl/adviezen/overgang-van-een-kapitaalhoudende-cooperatieve-vennootschap-naar-een-kapitaalloze
    datum: '2020-12-09'
  - titel: Inbreng in nijverheid bij besloten vennootschappen en coöperatieve vennootschappen [ONTWERP]
    url: https://www.cbn-cnc.be/nl/adviezen/inbreng-in-nijverheid-bij-besloten-vennootschappen-en-cooperatieve-vennootschappen-ontwerp
    datum: '2020-03-10'
  - titel: 'Neerlegging van de enkelvoudige jaarrekening bij de Nationale Bank van België: nieuwe modellen van de jaarrekening'
    url: https://www.cbn-cnc.be/nl/adviezen/neerlegging-van-de-enkelvoudige-jaarrekening-bij-de-nationale-bank-van-belgie-nieuwe
    datum: '2020-01-27'
---

# CBN-advies 126/2 - Inbrengprijs

Overeenkomstig artikel 23 van het besluit van 8 oktober 1976 behoren de belastingen en de kosten in verband met de inbreng niet tot de inbrengprijs. Hieraan ligt de gedachte ten grondslag dat de betrokken belastingen en kosten veelal moeilijk in verband kunnen worden gebracht met welbepaalde goederen zodat ze bezwaarlijk in de boekwaarde daarvan kunnen worden opgenomen. Gaat het om een inbreng in geld dan is het niet denkbaar dat de ingebrachte som geboekt wordt tegen een hogere waarde dan de nominale waarde. Bij inbreng als gevolg van een fusie, een opslorping, een splitsing of een inbreng van een onderdeel van een onderneming hebben de belastingen en kosten in verband met de inbreng betrekking op het netto ingebrachte vermogen en niet op het bruto-vermogen. Tenslotte kunnen er belastingen of kosten inzake inbreng verschuldigd zijn zonder dat er een echte inbreng van nieuwe activa heeft plaatsgehad, zoals bij kapitaalverhoging door incorporatie van reserves.

Dat is de reden waarom belastingen en kosten in verband met inbrengen volgens het besluit moeten worden geboekt in de post *Oprichtingskosten *als *Kosten van oprichting en kapitaalverhoging* (mec. nr. 6001). Zij worden op gepaste wijze afgeschreven bij jaarlijkse gedeelten van ten minste twintig ten honderd[^1]. Zij mogen ook onmiddellijk worden afgeschreven door aanrekening op de resultatenrekening van het boekjaar waarin ze werden gemaakt[^2]. Deze regeling is gelijklopend met de fiscale voorschriften terzake[^3].

[^1]: Artikel 28, § 1.

[^2]: Artikel 24.

[^3]: Cf. rondschrijven van 31 maart 1978, nr. RH 421/290.379 sub punt 32.
