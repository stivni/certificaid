---
bron: https://www.cbn-cnc.be/nl/adviezen/gefactureerde-nog-niet-ontvangen-voorschotten-en-vooruitbetalingen-rekening-46
datum: 1981-04-01
nummer: CBN-advies R103
provenance:
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/gefactureerde-nog-niet-ontvangen-voorschotten-en-vooruitbetalingen-rekening-46
      sha256: 8984215a8cc3f55508224e316bb671bdff8327f7328acd0085a73f79beae77eb
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
    rationale: "E2: markdown-tabel (regels 62-65) heeft een lege eerste kolom zonder header-label — elke rij (inclusief de sub-rijen 460 en 461) begint met '| |' waarvoor geen overeenkomstige header bestaat. ETL heeft de originele rekeningstructuur niet correct naar pipe-markdown vertaald. De overige body-tekst is volledig en clean."
    layer1:
      file_size_chars: 1220
      flags: []
      heading_count: 0
      max_section_chars: 1220
      run_at: '2026-05-11T15:05:47Z'
      run_id: 20260511-150547
      status: pass
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-11T17:05:20Z'
      rationale: "E2: markdown-tabel (regels 62-65) heeft een lege eerste kolom zonder header-label — elke rij (inclusief de sub-rijen 460 en 461) begint met '| |' waarvoor geen overeenkomstige header bestaat. ETL heeft de originele rekeningstructuur niet correct naar pipe-markdown vertaald. De overige body-tekst is volledig en clean."
      concrete_problemen:
        - regel: 62
          categorie: E2
          type: pseudo-table
          voorbeeld: '| | Rekening | Omschrijving | Debet | Credit | — lege eerste kolom zonder header-label'
        - regel: 64
          categorie: E2
          type: pseudo-table
          voorbeeld: '| | 460 | Te ontvangen | | | — lege eerste kolom herhaald op datarij'
themas:
  - gefactureerde voorschotten en vooruitbetalingen
  - nog niet ontvangen voorschotten en vooruitbetalingen
  - rekeningenstelsel
  - te innen voorschotten en vooruitbetalingen
  - voorschot
  - Vooruitbetaling
---

# CBN-advies R103 - Gefactureerde, nog niet ontvangen voorschotten en vooruitbetalingen - Rekening 46

Naar aanleiding van een vraag daaromtrent heeft de Commissie geadviseerd dat op rekening 46 niet enkel de "ontvangen" - in de zin van effectief geïnde - voorschotten en vooruitbetalingen worden geboekt, doch eveneens de nog te innen voorschotten en vooruitbetalingen. Zodra derhalve een voorschot gefactureerd werd behoort het, hoewel nog niet "ontvangen", geboekt te worden op rekening 46.

De Commissie meent dan ook dat de huidige omschrijving van rekening 46, namelijk *Ontvangen voorschotten en vooruitbetalingen*, misleidend is. Zij zal de Regering voorstellen bij een volgende wijziging van het koninklijk besluit van 7 maart 1978 de omschrijving van rekening 46 te corrigeren door het woord "ontvangen" eruit te schrappen.

Verder beveelt de Commissie aan, ten einde het bedrag der gefactureerde nog niet vereffende voorschotten in de boekhouding tot uiting te doen komen, rekening 46 *Voorschotten en vooruitbetalingen* uit te splitsen in subrekeningen:

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 460 | Te ontvangen | | |
| | 461 | Ontvangen. | | |
