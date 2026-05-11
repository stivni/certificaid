---
nummer: CBN-advies 132/6
datum: 1993-12-01
themas:
  - gefactureerde vooruitbetalingen
  - voorraden
  - Vooruitbetaling
  - waardering
  - waardering van voorraden
bron: https://www.cbn-cnc.be/nl/adviezen/vooruitbetalingen
provenance:
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/vooruitbetalingen
      sha256: f39529e8410b2cd371795a771f1e28a0d40fdd73287e098c06b0fef08e3a1f37
      version:
  tooling:
    pipeline: tools/etl/scrape_cbn_advies.py
    pipeline_version: uncommitted
    model:
    prompt_version:
  generated_at: '2026-05-08T18:34:52Z'
  stale: false
  stale_reason:
  trust:
    status: needs-rework
    confirmed_at: '2026-05-11T12:04:41Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "E2: de boekingstabellen zijn inconsistent opgebouwd. 'Aan'-rijen wisselen tussen twee patronen: soms '| aan | 440 Leveranciers |' (aan in cel 1) en soms '| | aan 55 Kredietinstellingen |' (aan samengevoegd in cel 2). Bovendien zijn de Debet- en Credit-kolommen structureel leeg — de tabellen tonen de rekeningnummers maar geen bedragen. Dit is acceptabel voor een advies dat de structuur illustreert, maar de inconsistentie in de 'aan'-plaatsing is een echte E2-issue."
    layer1:
      status: pass
      run_id: 20260511-083333
      run_at:
      heading_count: 0
      max_section_chars: 3514
      file_size_chars: 3514
      flags: []
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-11T12:04:41Z'
      rationale: "E2: de boekingstabellen zijn inconsistent opgebouwd. 'Aan'-rijen wisselen tussen twee patronen: soms '| aan | 440 Leveranciers |' (aan in cel 1) en soms '| | aan 55 Kredietinstellingen |' (aan samengevoegd in cel 2). Bovendien zijn de Debet- en Credit-kolommen structureel leeg — de tabellen tonen de rekeningnummers maar geen bedragen. Dit is acceptabel voor een advies dat de structuur illustreert, maar de inconsistentie in de 'aan'-plaatsing is een echte E2-issue."
      concrete_problemen:
        - regel: 67
          categorie: E2
          type: other
          voorbeeld: '| aan | 440 Leveranciers | | | | vs. | | aan 55 Kredietinstellingen | | | |'
        - regel: 74
          categorie: E2
          type: other
          voorbeeld: '| | aan 55 Kredietinstellingen | | | | (inconsistent met L67-patroon)'
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
