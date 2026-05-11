---
nummer: CBN-advies 107/9
datum: 1988-12-01
themas:
  - brugpensioen
  - pensioen
  - pensioenvoorzieningen
  - verplichting voortvloeiend uit brugpensioen
  - voorziening
  - voorzieningen voor brugpensioen
  - voorzieningen voor pensioenen
bron: https://www.cbn-cnc.be/nl/adviezen/vaststelling-van-het-bedrag-van-een-voorziening-voor-pensioenen-of-brugpensioenen
provenance:
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/vaststelling-van-het-bedrag-van-een-voorziening-voor-pensioenen-of-brugpensioenen
      sha256: 026465f0ae0b5f1a6459175ff87cf60dcfb40d52954cccd1acadd0d1b91ffc21
      version:
  tooling:
    pipeline: tools/etl/scrape_cbn_advies.py
    pipeline_version: uncommitted
    model:
    prompt_version:
  generated_at: '2026-05-08T18:34:00Z'
  stale: false
  stale_reason:
  trust:
    status: needs-rework
    confirmed_at: '2026-05-11T11:57:45Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "D4-artefact op regel 66-67: de lange zin eindigend op '1987[^1]' gevolgd door newline + spatie + ' tot wijziging van het jaarrekeningbesluit...' — zelfde broken-footnote-marker-newline-spatie-patroon als in drie andere adviezen uit deze batch. ETL-fixbaar."
    layer1:
      status: pass
      run_id: 20260511-083333
      run_at:
      heading_count: 0
      max_section_chars: 2216
      file_size_chars: 2216
      flags: []
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-11T11:57:45Z'
      rationale: "D4-artefact op regel 66-67: de lange zin eindigend op '1987[^1]' gevolgd door newline + spatie + ' tot wijziging van het jaarrekeningbesluit...' — zelfde broken-footnote-marker-newline-spatie-patroon als in drie andere adviezen uit deze batch. ETL-fixbaar."
      concrete_problemen:
        - regel: 66
          categorie: D4
          type: other
          voorbeeld: "koninklijk besluit van 6 november 1987[^1]\n tot wijziging van het jaarrekeningbesluit..."
gerelateerde_adviezen:
  - titel: Voorzieningen
    url: https://www.cbn-cnc.be/nl/adviezen/voorzieningen
    datum: '2019-03-05'
  - titel: Voorzieningen voor geïndexeerde pensioenen en brugpensioenen
    url: https://www.cbn-cnc.be/nl/adviezen/voorzieningen-voor-geindexeerde-pensioenen-en-brugpensioenen
    datum: '1993-02-01'
  - titel: Verplichtingen voortvloeiend uit brugpensioen
    url: https://www.cbn-cnc.be/nl/adviezen/verplichtingen-voortvloeiend-uit-brugpensioen-0
    datum: '1986-07-19'
  - titel: Verplichtingen voortvloeiend uit brugpensioen
    url: https://www.cbn-cnc.be/nl/adviezen/verplichtingen-voortvloeiend-uit-brugpensioen
    datum: '1980-01-01'
---

# CBN-advies 107/9 - Vaststelling van het bedrag van een voorziening voor pensioenen of brugpensioenen

Een onderneming heeft de Commissie gevraagd hoe het bedrag moet worden vastgesteld van een voorziening tot dekking van pensioenverplichtingen of brugpensioenen en, inzonderheid, of artikel 27*bis*, § 2 van het koninklijk besluit van 8 oktober 1976 ter zake van toepassing is. Dit artikel over renteloze of abnormaal laag rentende schulden en vorderingen op meer dan één jaar, bepaalt dat zij voor hun nominale waarde in de balans moeten worden opgenomen en dat tegelijkertijd het disconto op deze schulden en vorderingen, berekend tegen de geldende marktrente, in de overlopende rekeningen respectievelijk van het actief of van het passief, moet worden geboekt.

De Commissie heeft er in de eerste plaats op gewezen dat artikel 27*bis*, § 2 enkel slaat op vorderingen en schulden en derhalve niet van toepassing is op pensioenverplichtingen die op het passief van de balans in de post *Voorzieningen voor risico's en kosten* moeten worden geboekt.

Het bedrag van de nodige voorziening moet in elk geval rekening houden met het sterfterisico, enerzijds, en met de factor rente, anderzijds. Wat deze laatste factor betreft, zullen de datum waarop de kost moet worden betaald en de spreiding ervan uiteraard een weerslag hebben, via actualisatie, bij de rechtstreekse waardering van de te vormen voorziening, indien deze datum meer dan een jaar verwijderd is. Voor de berekeningsmodaliteiten van deze voorziening wordt in het Verslag aan de Koning bij het koninklijk besluit van 6 november 1987[^1]
 tot wijziging van het jaarrekeningbesluit van 8 oktober 1976, verwezen naar het koninklijk besluit van 15 mei 1985 betreffende de activiteiten van de private voorzorgsinstellingen.

De omstandigheid dat de ondernemingsafdeling waarmee deze pensioenen en brugpensioenen verband houden, verdwijnt of wordt overgedragen, heeft geen invloed op het bedrag van de voorziening.

De waardering van voorzieningen m.b.t. geïndexeerde pensioenen wordt later onderzocht, in het licht van het algemene probleem van de waardering van geïndexeerde schulden en verplichtingen.

[^1]: BS, 24 november 1987, inzonderheid p. 17312.
