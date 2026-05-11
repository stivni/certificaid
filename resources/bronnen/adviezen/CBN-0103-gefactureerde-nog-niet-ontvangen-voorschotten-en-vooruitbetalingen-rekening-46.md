---
bron: https://www.cbn-cnc.be/nl/adviezen/gefactureerde-nog-niet-ontvangen-voorschotten-en-vooruitbetalingen-rekening-46
datum: 1981-04-01
nummer: CBN-advies R103
provenance:
  generated_at: '2026-05-11T13:05:05Z'
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/gefactureerde-nog-niet-ontvangen-voorschotten-en-vooruitbetalingen-rekening-46
      sha256: 8984215a8cc3f55508224e316bb671bdff8327f7328acd0085a73f79beae77eb
      version:
  stale: false
  stale_reason:
  tooling:
    model:
    pipeline: tools/etl/convert.py
    pipeline_version: 3b788cd
    prompt_version:
  trust:
    confirmed_at: '2026-05-11T11:57:44Z'
    confirmed_by: subagent-sonnet-4-6
    layer1:
      status: pass
      run_id: 20260511-130524
      run_at: '2026-05-11T13:05:24Z'
      heading_count: 0
      max_section_chars: 1220
      file_size_chars: 1220
      flags: []
    layer2:
      agent: subagent-sonnet-4-6
      concrete_problemen:
        - categorie: E2
          regel: 54
          type: other
          voorbeeld: '| | Rekening | Omschrijving | Debet | Credit | — lege eerste kolom in header én alle rijen'
      rationale: 'E2: de markdown-tabel heeft een lege eerste kolom (extra leidende `| |` op elke rij) die geen overeenkomende header-label heeft — een ongebruikelijke structuur die een mens zo niet zou typen. Verder is de inhoud inhoudelijk volledig en schoon: geen artefacten, geen duplicate headings, geen unicode-issues.'
      run_at: '2026-05-11T11:57:44Z'
      status: needs-rework
    rationale: 'E2: de markdown-tabel heeft een lege eerste kolom (extra leidende `| |` op elke rij) die geen overeenkomende header-label heeft — een ongebruikelijke structuur die een mens zo niet zou typen. Verder is de inhoud inhoudelijk volledig en schoon: geen artefacten, geen duplicate headings, geen unicode-issues.'
    status: needs-rework
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
