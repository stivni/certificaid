---
nummer: "CBN-advies 151/1"
datum: 1986-07-01
themas:
  - kapitaal
  - kapitaalvermindering
  - schulden
  - terugbetaling aan vennoten
  - vrijstelling
  - vrijstelling van volstorting
bron: https://www.cbn-cnc.be/nl/adviezen/kapitaalvermindering-door-terugbetaling-aan-de-vennoten-of-vrijstelling-van-volstorting
gerelateerde_adviezen:
  - titel: Terugbetaling van kapitaal in vreemde valuta aan de aandeelhouders
    url: https://www.cbn-cnc.be/nl/adviezen/terugbetaling-van-kapitaal-in-vreemde-valuta-aan-de-aandeelhouders
    datum: '2024-03-13'
  - titel: Overgang van een kapitaalhoudende coöperatieve vennootschap naar een kapitaalloze vennootschap
    url: https://www.cbn-cnc.be/nl/adviezen/overgang-van-een-kapitaalhoudende-cooperatieve-vennootschap-naar-een-kapitaalloze
    datum: '2020-12-09'
  - titel: 'Neerlegging van de enkelvoudige jaarrekening bij de Nationale Bank van België: nieuwe modellen van de jaarrekening'
    url: https://www.cbn-cnc.be/nl/adviezen/neerlegging-van-de-enkelvoudige-jaarrekening-bij-de-nationale-bank-van-belgie-nieuwe
    datum: '2020-01-27'
  - titel: Van een kapitaalhoudende BVBA naar een kapitaalloze BV
    url: https://www.cbn-cnc.be/nl/adviezen/van-een-kapitaalhoudende-bvba-naar-een-kapitaalloze-bv
    datum: '2019-11-13'
bron_rol: interpretatief
chunk:
  level: 2
  type: '##'
  sub_strategy:
provenance:
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/kapitaalvermindering-door-terugbetaling-aan-de-vennoten-of-vrijstelling-van-volstorting
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
      heading_count: 2
      max_section_chars: 3769
      file_size_chars: 3769
      flags: []
      run_id: 20260509-212552
---
# CBN-advies 151/1 - Kapitaalvermindering door terugbetaling aan de vennoten of vrijstelling van volstorting

De wet van 5 december 1984 heeft de vroegere bepalingen van de vennootschapswet inzake kapitaalvermindering, grondig gewijzigd. Het nieuwe artikel 72bis stelt in § 1 dat, indien de vermindering van het kapitaal geschiedt door een terugbetaling aan de aandeelhouders of door vrijstelling van de storting van het saldo van de inbreng, de schuldeisers het recht hebben om een zekerheid te eisen voor hun vorderingen. Elke uitkering of betaling aan de aandeelhouders of vrijstelling van storting van het saldo van de inbreng is verboden, zolang de schuldeisers, die binnen de voorgeschreven termijn hun rechten hebben doen gelden, geen voldoening hebben gekregen, tenzij hun aanspraak om zekerheid te verkrijgen bij een rechterlijke beslissing is verworpen. 

Aan de Commissie werd gevraagd hoe dergelijke beslissingen tot kapitaalvermindering in de jaarrekening moeten worden uitgedrukt, rekening houdend met de wettelijk voorgeschreven regeling vervat in de vennootschapswet. Zij formuleerde volgend advies. 

Onbetwistbaar geldt onder vennoten de kapitaalvermindering vanaf de dag waarop daartoe door de algemene vergadering wordt besloten. Artikel 72bis koppelt aan de beslissing tot kapitaalvermindering geen opschortende noch ontbindende voorwaarde. Het heeft enkel tot doel de geldmiddelen - die zonder het voorschrift van artikel 72bis, aan de vennoten zouden zijn uitgekeerd als terugbetaling van hun inbreng -of de vordering van de vennootschap op haar vennoten - in geval van vrijstelling van volstorting - voorlopig in het vermogen van de vennootschap te behouden. 

Bijgevolg wordt de beslissing van de algemene vergadering tot terugbetaling in speciën aan de vennoten, als volgt geboekt : 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 100 | Geplaatst kapitaal | | |
| aan | 48 | Diverse | | |

Omvat de kapitaalvermindering een vrijstelling van volstorting, dan volstaat een parallelle vermindering van het kapitaal (rekening 100) en van het niet opgevraagd kapitaal (rekening 101) niet. Dergelijke boekingswijze zou indruisen tegen het voorschrift van artikel 72bis, § 1, vierde lid, van de vennootschapswet, krachtens hetwelk"... geen vrijstelling van de storting van het saldo van de inbreng mogelijk is zolang ...". 

De vennootschap moet derhalve haar vordering op haar aandeelhouders in haar actief behouden. De aard van de vordering verandert evenwel. Het gaat niet langer om een vordering tot volstorting van het kapitaal, maar om een vordering die krachtens de wet verplicht voorlopig in het actief van de vennootschap moet behouden blijven. 

In dit geval worden bijgevolg onderstaande boekingen verricht : 

### Kapitaalvermindering

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 100 | Geplaatst kapitaal | | |
| aan | 48 | Diverse schulden | | |

### Voorlopig behoud van de vordering op de aandeelhouders: 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 410 | Diverse vorderingen | | |
| aan | | 101 | | Niet-opgevraagd kapitaal |

Voornoemde boekingen blijven behouden tot, overeenkomstig artikel 72bis, de schuldeisers die hun rechten hebben laten gelden binnen de termijn van twee maanden, voldoening hebben gekregen tenzij hun aanspraak bij een rechterlijke beslissing is verworpen. 

Bij het verstrijken van deze termijn wordt de schuld van de vennootschap ten opzichte van haar aandeelhouders een gewone schuld die terugbetaalbaar is hetzij door onttrekking aan de geldmiddelen van de onderneming, hetzij door compensatie met de bestaande vordering te hunnen laste.
