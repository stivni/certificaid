---
bron: https://www.cbn-cnc.be/nl/adviezen/pensioenvoorzieningen
datum: 1987-11-24
nummer: CBN-advies 107/12
themas:
  - aanvullend rust- en overlevingspensioen
  - directieleden
  - pensioen
  - pensioenvoorzieningen
  - verplichting inzake rust- of overlevingspensioenen
  - voorziening
  - voorzieningen voor pensioenen
bron_rol: interpretatief
chunk:
  level: 2
  type: '##'
  sub_strategy:
provenance:
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/pensioenvoorzieningen
      sha256:
      version:
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: b4eac1f-dirty
    model:
    prompt_version:
  generated_at: '2026-05-12T23:37:27Z'
  stale: false
  stale_reason:
  trust:
    status: trusted
    confirmed_at: '2026-05-13T12:36:20Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "De enige eerder gerapporteerde issue (A5: en-dash '–' in H1-heading) is een source-karakter: analyse van het corpus toont dat 145 CBN-adviezen dezelfde '–' separator gebruiken in de H1-heading — dit is het dominante patroon van de CBN-website, geen ETL-inconsistentie. Body-tekst is volledig clean, inhoud compleet, voetnoot [^1] correct."
    layer1:
      status: pass
      run_id: 20260512-233938
      run_at: '2026-05-12T23:39:39Z'
      heading_count: 0
      max_section_chars: 2195
      file_size_chars: 2195
      flags: []
    layer2:
      status: trusted
      agent: subagent-sonnet-4-6
      run_at: '2026-05-13T12:36:20Z'
      rationale: "De enige eerder gerapporteerde issue (A5: en-dash '–' in H1-heading) is een source-karakter: analyse van het corpus toont dat 145 CBN-adviezen dezelfde '–' separator gebruiken in de H1-heading — dit is het dominante patroon van de CBN-website, geen ETL-inconsistentie. Body-tekst is volledig clean, inhoud compleet, voetnoot [^1] correct."
      concrete_problemen:
        - regel: 51
          categorie: (source)
          type: source-typo
          voorbeeld: '# CBN-advies 107/12 – Pensioenvoorzieningen — U+2013 EN-DASH is source-karakter (145 andere adviezen gebruiken hetzelfde patroon)'
---
# CBN-advies 107/12 – Pensioenvoorzieningen

De vroegere versie van artikel 45 van het koninklijk besluit van 8 oktober 1976 luidde als volgt : «Bij afwijking van artikel 19 moet voor de verplichtingen die voor de onderneming voortvloeien uit regelingen met betrekking tot een aanvullend rust- en overlevingspensioen ten behoeve van haar personeels- of directieleden slechts een voorziening worden gevormd vanaf de datum en volgens de modaliteiten door een later besluit te bepalen».

Het koninklijk besluit van 6 november 1987 heeft dit artikel vervangen door een nieuwe bepaling om de boekhoudwetgeving in overeenstemming te brengen met de bepalingen van de wet op de controle van de verzekeringsondernemingen, zoals toepasselijk verklaard op de «private voorzorgsinstellingen» bij koninklijk besluit van 14 mei 1985.

In tegenstelling tot de vroegere versie van artikel 45 slaat de nieuwe bepaling niet meer uitdrukkelijk op de directieleden van de ondernemingen en maakt alleen nog gewag van «personeelsleden».

Aan de Commissie werd gevraagd hoe het weglaten van de uitdrukkelijke verwijzing naar de directieleden diende te worden geïnterpreteerd en of hieruit moest worden afgeleid dat artikel 19 van het koninklijk besluit van 8 oktober 1976 integraal op hen van toepassing is, waar dit de vorming van voorzieningen voor pensioenkosten voorschrijft.

De Commissie is van oordeel dat het nieuwe artikel 45 van het koninklijk besluit van 8 oktober 1976 wel degelijk slaat op de verplichtingen inzake rust- of overlevingspensioenen die door een onderneming ten gunste van haar directieleden zijn aangegaan in het kader van een pensioenregeling. Het is inderdaad zo dat, enerzijds, de verplichting om in de toelichting bij de jaarrekening een beknopte beschrijving te geven van de aanvullende regeling voor rust- of overlevingspensioenen, uitdrukkelijk slaat op de directieleden van ondernemingen voor wie een dergelijke regeling geldt. Anderzijds blijkt nergens uit het Verslag aan de Koning dat het koninklijk besluit van 6 november 1987[^1] voorafgaat dat de Regering het toepassingsgebied van artikel 45 zou hebben willen wijzigen.

[^1]: Belgisch Staatsblad, 24 november 1987, p. 17311.
