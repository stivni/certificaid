---
bron: https://www.cbn-cnc.be/nl/adviezen/pensioenvoorzieningen
datum: 1987-11-24
nummer: CBN-advies 107/12
provenance:
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/pensioenvoorzieningen
      sha256: 7cae9d96e7c8ebc8a0c451cf51977d4b9534ff2d00cc5a2ddf9057a1c1db7fe3
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
    rationale: "A5: H1-heading op regel 51 gebruikt U+2013 EN-DASH ('–') als scheidingsteken ('# CBN-advies 107/12 – Pensioenvoorzieningen') terwijl het gehele corpus ASCII-hyphen '-' gebruikt. Dit is een inconsistente separator die heading-matching en retrieval bemoeilijkt. Verdere inhoud volledig en clean."
    layer1:
      file_size_chars: 2196
      flags: []
      heading_count: 0
      max_section_chars: 2196
      run_at: '2026-05-11T15:05:48Z'
      run_id: 20260511-150547
      status: pass
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-11T15:15:32Z'
      rationale: "A5: H1-heading op regel 51 gebruikt U+2013 EN-DASH ('–') als scheidingsteken ('# CBN-advies 107/12 – Pensioenvoorzieningen') terwijl het gehele corpus ASCII-hyphen '-' gebruikt. Dit is een inconsistente separator die heading-matching en retrieval bemoeilijkt. Verdere inhoud volledig en clean."
      concrete_problemen:
        - regel: 51
          categorie: A5
          type: other
          voorbeeld: '# CBN-advies 107/12 – Pensioenvoorzieningen (U+2013 EN-DASH)'
themas:
  - aanvullend rust- en overlevingspensioen
  - directieleden
  - pensioen
  - pensioenvoorzieningen
  - verplichting inzake rust- of overlevingspensioenen
  - voorziening
  - voorzieningen voor pensioenen
---

# CBN-advies 107/12 – Pensioenvoorzieningen

De vroegere versie van artikel 45 van het koninklijk besluit van 8 oktober 1976 luidde als volgt : «Bij afwijking van artikel 19 moet voor de verplichtingen die voor de onderneming voortvloeien uit regelingen met betrekking tot een aanvullend rust- en overlevingspensioen ten behoeve van haar personeels- of directieleden slechts een voorziening worden gevormd vanaf de datum en volgens de modaliteiten door een later besluit te bepalen».

Het koninklijk besluit van 6 november 1987 heeft dit artikel vervangen door een nieuwe bepaling om de boekhoudwetgeving in overeenstemming te brengen met de bepalingen van de wet op de controle van de verzekeringsondernemingen, zoals toepasselijk verklaard op de «private voorzorgsinstellingen» bij koninklijk besluit van 14 mei 1985.

In tegenstelling tot de vroegere versie van artikel 45 slaat de nieuwe bepaling niet meer uitdrukkelijk op de directieleden van de ondernemingen en maakt alleen nog gewag van «personeelsleden».

Aan de Commissie werd gevraagd hoe het weglaten van de uitdrukkelijke verwijzing naar de directieleden diende te worden geïnterpreteerd en of hieruit moest worden afgeleid dat artikel 19 van het koninklijk besluit van 8 oktober 1976 integraal op hen van toepassing is, waar dit de vorming van voorzieningen voor pensioenkosten voorschrijft.

De Commissie is van oordeel dat het nieuwe artikel 45 van het koninklijk besluit van 8 oktober 1976 wel degelijk slaat op de verplichtingen inzake rust- of overlevingspensioenen die door een onderneming ten gunste van haar directieleden zijn aangegaan in het kader van een pensioenregeling. Het is inderdaad zo dat, enerzijds, de verplichting om in de toelichting bij de jaarrekening een beknopte beschrijving te geven van de aanvullende regeling voor rust- of overlevingspensioenen, uitdrukkelijk slaat op de directieleden van ondernemingen voor wie een dergelijke regeling geldt. Anderzijds blijkt nergens uit het Verslag aan de Koning dat het koninklijk besluit van 6 november 1987[^1] voorafgaat dat de Regering het toepassingsgebied van artikel 45 zou hebben willen wijzigen.

[^1]: Belgisch Staatsblad, 24 november 1987, p. 17311.
