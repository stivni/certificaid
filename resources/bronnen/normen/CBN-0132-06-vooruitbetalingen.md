---
nummer: "CBN-advies 132/6"
datum: 1993-12-01
themas:
  - gefactureerde vooruitbetalingen
  - voorraden
  - Vooruitbetaling
  - waardering
  - waardering van voorraden
bron: https://www.cbn-cnc.be/nl/adviezen/vooruitbetalingen
bron_rol: interpretatief
chunk:
  level: 2
  type: '##'
  sub_strategy:
provenance:
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/vooruitbetalingen
      sha256:
      version:
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: 3b788cd
    model:
    prompt_version:
  generated_at: '2026-05-09T20:20:06Z'
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
      max_section_chars: 3513
      file_size_chars: 3513
      flags: []
      run_id: 20260509-212552
---
# CBN-advies 132/6 - Vooruitbetalingen

Naar hun aard zijn ontvangen en gedane vooruitbetalingen duidelijk te onderscheiden van schulden en vorderingen. Vooruitbetalingen doen geen toekomstige uitgaande of inkomende kasstromen ontstaan. Zodra het goed is ontvangen of geleverd of de dienst is verricht verdwijnen zij doordat zij worden verrekend met de vordering of de schuld die ontstaat ingevolge de levering of ontvangst van het goed of het verrichten van de dienst. 

In het algemeen rekeningenstelsel worden vooruitbetalingen dan ook in bijzondere rekeningen geboekt en in de balans afzonderlijk vermeld. Voor gedane vooruitbetalingen op materiële vaste activa en voorraden is dit aan actiefzijde, voor ontvangen vooruitbetalingen op bestellingen is dit aan passiefzijde. 

Gedane vooruitbetalingen zijn bestemd om te worden toegevoegd hetzij aan de aanschaffingswaarde van immateriële of materiële vaste activa, hetzij aan de kostprijs van voorraden en diensten. 

Vooruitbetalingen die met een actief verbonden zijn, worden dan ook in de balans vermeld in samenhang met het actief waarop zij betrekking hebben. Door de onderneming "gekochte" diensten worden daarentegen niet geactiveerd met als gevolg dat er ook geen overeenstemmende actiefpost bestaat. Daarom worden vooruitbetalingen op diensten toegerekend aan de handelsvorderingen. 

De Commissie werd gevraagd of ingeval van vooruitbetalingen op voorraadinkopen de wijzigingen dienen te verlopen via de rekeningen voor voorraadwijzigingen, zoals gebruikelijk voor de klasse "Voorraden en bestellingen in uitvoering", en of er een onderscheid moet worden gemaakt tussen al of niet gefactureerde vooruitbetalingen. 

Vooruitbetalingen kunnen niet fysiek in de inventaris worden opgenomen en worden bij levering aan de aanschaffingswaarde toegevoegd, zodat zij niet via de voorraadwijzigingen kunnen verlopen. Het algemeen rekeningenstelsel bevat dan ook geen rekening "Wijzigingen vooruitbetalingen op voorraden". 

Gefactureerde vooruitbetalingen worden als volgt geboekt: 

- bij ontvangst van de factuur met betrekking tot de vooruitbetaling :

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 36 Vooruitbetalingen op voorraadinkopen | | | |
| | 411 Terug te vorderen btw | | | |
| aan | 440 Leveranciers | | | |

- bij betaling van de factuur met betrekking tot de vooruitbetaling : 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 440 Leveranciers | | | |
| | aan 55 Kredietinstellingen | | | |

- bij ontvangst van de definitieve factuur : 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 60 Handelsgoederen, grond- en hulpstoffen | | | |
| | 411 Terug te vorderen btw | | | |
| aan | 36 Vooruitbetalingen op voorraadinkopen | | | |
| | 440 Leveranciers | | | |

Bij vooruitbetaling vóór facturatie geschiedt de boeking als volgt : 

- bij vooruitbetaling : 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 36 Vooruitbetalingen op voorraadinkopen | | | |
| aan | 55 Kredietinstellingen | | | |

- bij ontvangst van de factuur :

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 60 Handelsgoederen, grond- en hulpstoffen | | | |
| | 411 Terug te vorderen btw | | | |
| | aan 440 Leveranciers | | | |
| | 440 Leveranciers | | | |
| | aan 36 Vooruitbetalingen op voorraadinkopen | | | |
