---
tags: [VI.A, '2.4']
itaa-lex-sectie: VI.A
wet: Richtlijn 2006/112/EG van de Raad betreffende het gemeenschappelijke stelsel van belasting over de toegevoegde waarde
status: beschikbaar
bijgewerkt: 11.12.2006
bron: ejustice.just.fgov.be (gecoördineerde versie)
provenance:
  inputs:
    - id: resources/raw/wetteksten/BTW-richtlijn-2006-112.pdf
      sha256: d2e9f9e0e1ba01e3822dab19047137bf146cfbee10bc4f9d823c53587f91110d
      version: 11.12.2006
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: 732fcc0
    model:
    prompt_version:
  generated_at: '2026-05-07T13:37:32Z'
  stale: false
  stale_reason:
  trust:
    status: needs-rework
    confirmed_at: '2026-05-11T11:43:15Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "A1/A2: Lange inhoudstafel (regels 60-386) met dotted leaders is als ## / ### / #### / ##### headings in de body opgenomen, waardoor de TOC verdubbelt met de echte body-secties. A1: Pagina-footers 'NL', 'Publicatieblad van de Europese Unie' en 'L 347/x' staan als losse regels verspreid door de body (226 NL/L347-regels geteld). B2: Hiërarchiesprong: body-artikelen starten op ###### terwijl TITEL op ### staat. Inhoud is overigens volledig en leesbaar NL."
    layer1:
      status: warn
      run_id: 20260511-134044
      run_at: '2026-05-11T13:40:44Z'
      heading_count: 904
      max_section_chars: 27576
      file_size_chars: 388992
      flags:
        - name: max_section_size
          status: warn
          detail: 'langste sectie op ######-niveau: 27576 chars (>24000); chunker splitst auto op alinea-grenzen via split_long_chunk'
          samples: []
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-11T11:43:15Z'
      rationale: "A1/A2: Lange inhoudstafel (regels 60-386) met dotted leaders is als ## / ### / #### / ##### headings in de body opgenomen, waardoor de TOC verdubbelt met de echte body-secties. A1: Pagina-footers 'NL', 'Publicatieblad van de Europese Unie' en 'L 347/x' staan als losse regels verspreid door de body (226 NL/L347-regels geteld). B2: Hiërarchiesprong: body-artikelen starten op ###### terwijl TITEL op ### staat. Inhoud is overigens volledig en leesbaar NL."
      concrete_problemen:
        - regel: 61
          categorie: A2
          type: dotted-leader
          voorbeeld: '### TITEL I - VOORWERP EN TOEPASSINGSGEBIED . . . . . . . . . . . . . . .'
        - regel: 99
          categorie: A1
          type: form-feed
          voorbeeld: "L 347/6\n\nNL\n\nPublicatieblad van de Europese Unie"
        - regel: 387
          categorie: A3
          type: other
          voorbeeld: iii) — los tekstfragment tussen TOC en body (concordantietabel-residu)
        - regel: 392
          categorie: B2
          type: other
          voorbeeld: '### TITEL I (body) → ###### Art. 1: sprong van ### naar ###### zonder tussenniveaus'
chunk:
  level: 6
  type: Art.
  sub_strategy:
---

# Richtlijn 2006/112/EG van de Raad betreffende het gemeenschappelijke stelsel van belasting over de toegevoegde waarde

*Bijgewerkt tot en met 11.12.2006 — gecoördineerde versie.*

INHOUDSTAFEL
### TITEL I - VOORWERP EN TOEPASSINGSGEBIED . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

### TITEL II - GEOGRAFISCH TOEPASSINGSGEBIED . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

### TITEL III - BELASTINGPLICHTIGEN . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

### TITEL IV - BELASTBARE HANDELINGEN . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#### Hoofdstuk 1 - Levering van goederen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#### Hoofdstuk 2 - Intracommunautaire verwerving van goederen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#### Hoofdstuk 3 - Diensten . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#### Hoofdstuk 4 - Invoer van goederen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

### TITEL V - PLAATS VAN DE BELASTBARE HANDELINGEN . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#### Hoofdstuk 1 - Plaats van levering van goederen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .


##### Afdeling 1 - Levering van goederen zonder vervoer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

##### Afdeling 2 - Levering van goederen met vervoer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

##### Afdeling 3 - Levering van goederen aan boord van een schip, vliegtuig of trein . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

##### Afdeling 4 - Levering van goederen via distributiesystemen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
#### Hoofdstuk 2 - Plaats van een intracommunautaire verwerving van goederen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#### Hoofdstuk 3 - Plaats van een dienst . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .


##### Afdeling 1 - Algemene regel . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

##### Afdeling 2 - Bijzondere bepalingen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
##### Onderafdeling 1 - Diensten van tussenpersonen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

L 347/6

NL

Publicatieblad van de Europese Unie


##### Onderafdeling 2 - Diensten met betrekking tot onroerende goederen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

##### Onderafdeling 3 - Vervoerdiensten . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

##### Onderafdeling 4 - Culturele en soortgelijke diensten, diensten die samenhangen met vervoer of betrekking hebben op roerende lichamelijke zaken . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

##### Onderafdeling 5 - Diverse diensten . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

##### Onderafdeling 6 - Criterium inzake werkelijk gebruik en werkelijke exploitatie . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#### Hoofdstuk 4 - Plaats van invoer van goederen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

### TITEL VI - BELASTBAAR FEIT EN VERSCHULDIGDHEID VAN DE BELASTING . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#### Hoofdstuk 1 - Algemene bepalingen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#### Hoofdstuk 2 - Goederenleveringen en diensten . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#### Hoofdstuk 3 - Intracommunautaire verwerving van goederen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#### Hoofdstuk 4 - Invoer van goederen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

### TITEL VII - MAATSTAF VAN HEFFING . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#### Hoofdstuk 1 - Definitie . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#### Hoofdstuk 2 - Goederenleveringen en diensten . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#### Hoofdstuk 3 - Intracommunautaire verwerving van goederen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#### Hoofdstuk 4 - Invoer van goederen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#### Hoofdstuk 5 - Diverse bepalingen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

### TITEL VIII - TARIEVEN . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#### Hoofdstuk 1 - Toepassing van de tarieven . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#### Hoofdstuk 2 - Structuur en hoogte van de tarieven . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .


##### Afdeling 1 - Normaal tarief . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

##### Afdeling 2 - Verlaagde tarieven . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

##### Afdeling 3 - Bijzondere bepalingen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
#### Hoofdstuk 3 - Tijdelijke bepalingen voor bepaalde arbeidsintensieve diensten . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#### Hoofdstuk 4 - Bijzondere bepalingen van toepassing tot de invoering van de definitieve regeling . . . . . . . . . . . . . . . .

#### Hoofdstuk 5 - Tijdelijke bepalingen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

### TITEL IX - VRIJSTELLINGEN . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#### Hoofdstuk 1 - Algemene bepalingen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#### Hoofdstuk 2 - Vrijstellingen voor bepaalde activiteiten van algemeen belang . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#### Hoofdstuk 3 - Vrijstellingen ten gunste van andere activiteiten . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#### Hoofdstuk 4 - Vrijstellingen met betrekking tot intracommunautaire handelingen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .


##### Afdeling 1 - Vrijstellingen voor levering van goederen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

##### Afdeling 2 - Vrijstellingen voor intracommunautaire verwervingen van goederen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

##### Afdeling 3 - Vrijstellingen voor bepaalde vervoerdiensten . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
#### Hoofdstuk 5 - Vrijstellingen bij invoer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#### Hoofdstuk 6 - Vrijstellingen bij uitvoer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#### Hoofdstuk 7 - Vrijstellingen met betrekking tot internationaal vervoer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#### Hoofdstuk 8 - Vrijstellingen voor bepaalde met uitvoer gelijkgestelde handelingen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#### Hoofdstuk 9 - Vrijstellingen voor door tussenpersonen verrichte diensten . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#### Hoofdstuk 10 - Vrijstellingen voor handelingen met betrekking tot het internationale goederenverkeer . . . . . . . . . .


##### Afdeling 1 - Douane- en andere entrepots en soortgelijke regelingen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

##### Afdeling 2 - Handelingen die worden vrijgesteld met het oog op de uitvoer en in het kader van het handelsverkeer tussen de lidstaten . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .


NL

Publicatieblad van de Europese Unie

L 347/7

##### Afdeling 3 - Gemeenschappelijke bepalingen met betrekking tot de Afdelingen 1 en 2 . . . . . . . . . . . . . . . . . . . . . . . . . .
### TITEL X - AFTREK . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#### Hoofdstuk 1 - Ontstaan en omvang van het recht op aftrek . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#### Hoofdstuk 2 - Evenredige aftrek . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#### Hoofdstuk 3 - Beperkingen van het recht op aftrek . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#### Hoofdstuk 4 - Wijze van uitoefening van het recht op aftrek . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#### Hoofdstuk 5 - Herziening van de aftrek . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

### TITEL XI - VERPLICHTINGEN VAN DE BELASTINGPLICHTIGEN EN VAN BEPAALDE NIET-BELASTINGPLICHTIGE PERSONEN . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#### Hoofdstuk 1 - Verplichting tot betaling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .


##### Afdeling 1 - Tegenover de schatkist tot voldoening van de belasting gehouden personen . . . . . . . . . . . . . . . . . . . . . . . .

##### Afdeling 2 - Wijze van betaling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
#### Hoofdstuk 2 - Identificatie . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#### Hoofdstuk 3 - Facturering . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .


##### Afdeling 1 - Definitie . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

##### Afdeling 2 - Het begrip factuur . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

##### Afdeling 3 - Uitreiking van facturen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

##### Afdeling 4 - Inhoud van de facturen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

##### Afdeling 5 - Verzenden van facturen langs elektronische weg . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

##### Afdeling 6 - Vereenvoudigingsmaatregelen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
#### Hoofdstuk 4 - Boekhouding . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .


##### Afdeling 1 - Definitie . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

##### Afdeling 2 - Algemene verplichtingen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

##### Afdeling 3 - Specifieke verplichtingen ten aanzien van het bewaren van facturen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

##### Afdeling 4 - Recht van toegang tot elektronisch bewaarde facturen in een andere lidstaat . . . . . . . . . . . . . . . . . . . . . . .
#### Hoofdstuk 5 - Aangiften . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#### Hoofdstuk 6 - Lijsten . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#### Hoofdstuk 7 - Diverse bepalingen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#### Hoofdstuk 8 - Verplichtingen ter zake van bepaalde invoer- en uitvoerhandelingen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .


##### Afdeling 1 - Invoerhandelingen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

##### Afdeling 2 - Uitvoerhandelingen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
### TITEL XII - BIJZONDERE REGELINGEN . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#### Hoofdstuk 1 - Bijzondere regeling voor kleine ondernemingen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .


##### Afdeling 1 - Vereenvoudigde bepalingen inzake belastingheffing en belastinginning . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

##### Afdeling 2 - Vrijstellingen of degressieve verminderingen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

##### Afdeling 3 - Verslag en herziening . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
#### Hoofdstuk 2 - Gemeenschappelijke forfaitaire regeling voor landbouwproducenten . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#### Hoofdstuk 3 - Bijzondere regeling voor reisbureaus . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#### Hoofdstuk 4 - Bijzondere regelingen voor gebruikte goederen, kunstvoorwerpen, voorwerpen voor verzamelingen en antiquiteiten . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .


##### Afdeling 1 - Definities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

##### Afdeling 2 - Bijzondere regeling voor belastingplichtige wederverkopers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
##### Onderafdeling 1 - Winstmargeregeling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

##### Onderafdeling 2 - Overgangsregeling voor gebruikte vervoermiddelen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .


##### Afdeling 3 - Bijzondere regeling voor verkoop op openbare veilingen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

L 347/8

NL

Publicatieblad van de Europese Unie


##### Afdeling 4 - Maatregelen ter voorkoming van verstoring van de mededinging en fraude . . . . . . . . . . . . . . . . . . . . . . . .
#### Hoofdstuk 5 - Bijzondere regeling voor beleggingsgoud . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .


##### Afdeling 1 - Algemene bepalingen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

##### Afdeling 2 - Vrijstelling van de belasting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

##### Afdeling 3 - Recht om voor belastingheffing te kiezen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

##### Afdeling 4 - Handelingen op een gereglementeerde goudmarkt . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

##### Afdeling 5 - Bijzondere rechten en verplichtingen van handelaren in beleggingsgoud . . . . . . . . . . . . . . . . . . . . . . . . . . . .
#### Hoofdstuk 6 - Bijzondere regeling voor niet in de Gemeenschap gevestigde belastingplichtigen die langs elektronische weg diensten verrichten voor niet-belastingplichtigen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .


##### Afdeling 1 - Algemene bepalingen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

##### Afdeling 2 - Bijzondere regeling voor langs elektronische weg verrichte diensten . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
### TITEL XIII - AFWIJKINGEN . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#### Hoofdstuk 1 - Afwijkingen van toepassing tot de invoering van de definitieve regeling . . . . . . . . . . . . . . . . . . . . . . . . . .


##### Afdeling 1 - Afwijkingen voor de staten die op 1 januari 1978 lid waren van de Gemeenschap . . . . . . . . . . . . . . . . .

##### Afdeling 2 - Afwijkingen voor de staten die na 1 januari 1978 tot de Gemeenschap zijn toegetreden . . . . . . . . . . . .

##### Afdeling 3 - Gemeenschappelijke bepalingen met betrekking tot de Afdelingen 1 et 2 . . . . . . . . . . . . . . . . . . . . . . . . . .
#### Hoofdstuk 2 - Afwijkingen waarvoor machtiging is verleend . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .


##### Afdeling 1 - Vereenvoudigingsmaatregelen en maatregelen ter voorkoming van belastingfraude en -ontwijking . .

##### Afdeling 2 - Internationale overeenkomsten . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
### TITEL XIV - DIVERSE BEPALINGEN . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#### Hoofdstuk 1 - Uitvoeringsmaatregelen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#### Hoofdstuk 2 - BTW-Comité . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#### Hoofdstuk 3 - Omrekeningskoers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#### Hoofdstuk 4 - Andere belastingen, rechten en heffingen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

### TITEL XV - SLOTBEPALINGEN . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

#### Hoofdstuk 1 - Overgangsregeling voor de belastingheffing in het handelsverkeer tussen de lidstaten . . . . . . . . . . . . .

#### Hoofdstuk 2 - Overgangsmaatregelen in het kader van de toetreding tot de Europese Unie . . . . . . . . . . . . . . . . . . . . . .

#### Hoofdstuk 3 - Omzetting en inwerkingtreding . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

BIJLAGE I - LIJST VAN WERKZAAMHEDEN BEDOELD IN ARTIKEL 14, LID 1, DERDE ALINEA . . . . . . . . . . . . . . .

BIJLAGE II - INDICATIEVE LIJST VAN LANGS ELEKTRONISCHE WEG VERRICHTE DIENSTEN BEDOELD IN ARTIKEL 56, LID 1, PUNT K) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

BIJLAGE III - LIJST VAN DE GOEDERENLEVERINGEN EN DE DIENSTEN WAAROP DE IN ARTIKEL 98 BEDOELDE VERLAGDE TARIEVEN MOGEN WORDEN TOEGEPAST . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

BIJLAGE IV - LIJST VAN DE IN ARTIKEL 106 BEDOELDE DIENSTEN . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

BIJLAGE V - CATEGORIEËN GOEDEREN DIE VOLGENS ARTIKEL 160, LID 2, ONDER EEN ANDER STELSEL VAN ENTREPOTS DAN DOUANE-ENTREPOTS KUNNEN VALLEN . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

BIJLAGE VI - LIJST VAN GOEDERENLEVERINGEN EN DIENSTEN ALS BEDOELD IN PUNT D) VAN ARTIKEL 199, LID 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

BIJLAGE VII - LIJST VAN LANDBOUWPRODUCTIEWERKZAAMHEDEN BEDOELD IN ARTIKEL 295, LID 1, PUNT 4) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

BIJLAGE VIII - INDICATIEVE LIJST VAN AGRARISCHE DIENSTEN BEDOELD IN ARTIKEL 295, LID 1, PUNT 5)

BIJLAGE IX - KUNSTVOORWERPEN, VOORWERPEN VOOR VERZAMELINGEN EN ANTIQUITEITEN BEDOELD IN ARTIKEL 311, LID 1, PUNTEN 2), 3) EN 4) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

## Deel A - Kunstvoorwerpen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

## Deel B - Voorwerpen voor verzamelingen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

## Deel C - Antiquiteiten . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .


Publicatieblad van de Europese Unie

NL

BIJLAGE X - LIJST VAN HANDELINGEN WAARVOOR DE IN DE ARTIKELEN 370 EN 371 EN DE ARTIKELEN 375 TOT EN MET 390 BEDOELDE AFWIJKINGEN GELDEN . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

## Deel A - Handelingen die de lidstaten mogen blijven belasten . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

## Deel B - Handelingen die de lidstaten mogen blijven vrijstellen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

BIJLAGE XI . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

## Deel A - Ingetrokken richtlijnen met de achtereenvolgende wijzigingen ervan . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

## Deel B - Termijnen voor de omzetting in nationaal recht (bedoeld in artikel 411) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

BIJLAGE XII - CONCORDANTIETABEL . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

iii)

### TITEL I
VOORWERP EN TOEPASSINGSGEBIED

###### Art. 1
1. Bij deze richtlijn wordt het gemeenschappelijke stelsel van belasting over de toegevoegde waarde (BTW) vastgesteld.
2. Het gemeenschappelijke BTW-stelsel berust op het beginsel dat op goederen en diensten een algemene verbruiksbelasting wordt geheven die strikt evenredig is aan de prijs van de goederen en diensten, zulks ongeacht het aantal handelingen dat tijdens het productie- en distributieproces vóór de fase van heffing plaatsvond.
Bij elke handeling is de BTW, berekend over de prijs van het goed of van de dienst volgens het tarief dat voor dat goed of voor die dienst geldt, verschuldigd onder aftrek van het bedrag van de BTW waarmede de onderscheiden elementen van de prijs rechtstreeks zijn belast.

de diensten die binnen het grondgebied van een lidstaat door een als zodanig handelende belastingplichtige onder bezwarende titel worden verricht;

d)

de invoer van goederen.

2. a) Voor de toepassing van lid 1, onder b), punt ii), worden als
„vervoermiddelen” beschouwd, de volgende voor het personen- of goederenvervoer bestemde vervoermiddelen:
i)

landvoertuigen die zijn uitgerust met een motor van meer dan 48 cc cilinderinhoud of met een vermogen van meer dan 7,2 kilowatt;

ii)

schepen met een lengte van meer dan 7,5 meter, met uitzondering van schepen voor de vaart op volle zee waarmee personenvervoer tegen betaling plaatsvindt of die voor de uitoefening van enigerlei industriële, handels- of visserijactiviteit worden gebruikt, van reddingsboten en schepen voor hulpverlening op zee en van schepen voor de kustvisserij;

iii)

luchtvaartuigen met een totaal opstijggewicht van meer dan 1 550 kg, met uitzondering van luchtvaartuigen welke door luchtvaartmaatschappijen worden gebruikt die zich hoofdzakelijk toeleggen op het betaalde internationale vervoer.

###### Art. 2
1. De volgende handelingen zijn aan de BTW onderworpen:
a)

de leveringen van goederen, die binnen het grondgebied van een lidstaat door een als zodanig handelende belastingplichtige onder bezwarende titel worden verricht;

b)

de intracommunautaire verwervingen van goederen die binnen het grondgebied van een lidstaat onder bezwarende titel worden verricht:

ii)

door een als zodanig handelende belastingplichtige of door een niet-belastingplichtige rechtspersoon, wanneer de verkoper een als zodanig handelende belastingplichtige is die noch onder de in de artikelen 282 tot en met 292 bedoelde vrijstellingsregeling voor kleine ondernemingen, noch onder artikel 33 of artikel 36 valt; wanneer het nieuwe vervoermiddelen betreft, door een belastingplichtige of door een niet-belastingplichtige rechtspersoon van wie de andere verwervingen uit hoofde van artikel 3, lid 1, niet aan de BTW zijn onderworpen, of door enige andere niet-belastingplichtige;

wanneer het accijnsproducten betreft uit hoofde waarvan de accijnsrechten binnen het grondgebied van de lidstaat verschuldigd zijn krachtens Richtlijn 92/12/EEG, door een belastingplichtige of door een niet-belastingplichtige rechtspersoon van wie de andere verwervingen uit hoofde van artikel 3, lid 1, niet aan de BTW zijn onderworpen;

c)

Het gemeenschappelijke BTW-stelsel wordt toegepast tot en met de kleinhandelsfase.

i)

L 347/9

b) Deze vervoermiddelen worden in de volgende gevallen beschouwd als „nieuw”:
i)

voor gemotoriseerde landvoertuigen, wanneer de levering binnen zes maanden na de eerste ingebruikneming plaatsvindt of wanneer het voertuig niet meer dan 6 000 km heeft afgelegd;

ii)

voor schepen, wanneer de levering binnen drie maanden na de eerste ingebruikneming plaatsvindt of wanneer het schip niet meer dan 100 uur heeft gevaren;

L 347/10
iii)

Publicatieblad van de Europese Unie

NL

voor luchtvaartuigen, wanneer de levering binnen drie maanden na de eerste ingebruikneming plaatsvindt of wanneer het luchtvaartuig niet meer dan 40 uur heeft gevlogen.

c) De lidstaten stellen de voorwaarden vast waaronder de in de tweede alinea bedoelde gegevens kunnen worden aangetoond.

###### Art. 4
Naast de in artikel 3 bedoelde handelingen zijn ook de volgende handelingen niet aan BTW onderworpen:
a)

de intracommunautaire verwervingen van gebruikte goederen, kunstvoorwerpen, voorwerpen voor verzamelingen en antiquiteiten zoals omschreven in artikel 311, lid 1, punten 1) tot en met 4), wanneer de verkoper een als zodanig handelende belastingplichtige wederverkoper is en het verworven goed in de lidstaat van vertrek van de verzending of het vervoer aan de BTW is onderworpen overeenkomstig de in de artikelen 312 tot en met 325 vastgestelde winstmargeregeling;

b)

de intracommunautaire verwervingen van gebruikte vervoermiddelen, zoals omschreven in artikel 327, lid 3, wanneer de verkoper een als zodanig handelende belastingplichtige wederverkoper is en het verworven gebruikte vervoermiddel in de lidstaat van vertrek van de verzending of het vervoer aan de BTW is onderworpen overeenkomstig de overgangsregeling voor gebruikte vervoermiddelen;

c)

de intracommunautaire verwervingen van gebruikte goederen, kunstvoorwerpen, voorwerpen voor verzamelingen en antiquiteiten zoals omschreven in artikel 311, lid 1, punten 1) tot en met 4), wanneer de verkoper een als zodanig handelende organisator van openbare veilingen is en het verworven goed in de lidstaat van vertrek van de verzending of het vervoer aan de BTW is onderworpen overeenkomstig de bijzondere regeling voor openbare veilingen.

3. Als „accijnsproducten” worden beschouwd energieproducten, elektriciteit, alcohol en alcoholhoudende dranken en tabaksfabrikaten, zoals omschreven in de vigerende communautaire bepalingen, maar niet gas dat via het aardgasdistributiesysteem wordt geleverd.
###### Art. 3
1. In afwijking van artikel 2, lid 1, onder b), punt i), zijn de volgende handelingen niet aan BTW onderworpen:
a)

b)

de intracommunautaire verwervingen van goederen die worden verricht door een belastingplichtige of een nietbelastingplichtige rechtspersoon waarvan de levering krachtens de artikelen 148 en 151 binnen het grondgebied van de lidstaat van verwerving zou worden vrijgesteld;


de intracommunautaire verwervingen van andere goederen dan die bedoeld in punt a) en in artikel 4, en dan de verwervingen van vervoermiddelen en van accijnsproducten, die worden verricht door een belastingplichtige ten behoeve van zijn landbouw-, bosbouw- of visserijbedrijf dat onder de gemeenschappelijke forfaitaire regeling voor landbouwproducenten valt, door een belastingplichtige die uitsluitend goederenleveringen of diensten verricht waarvoor geen recht op aftrek bestaat, of door een nietbelastingplichtige rechtspersoon.

### TITEL II
GEOGRAFISCH TOEPASSINGSGEBIED

###### Art. 5
2. Het bepaalde in lid 1, onder b), is alleen van toepassing indien de volgende voorwaarden vervuld zijn:

Voor de toepassing van deze richtlijn wordt verstaan onder:

a)

1)

„Gemeenschap” en „grondgebied van de Gemeenschap”: het geheel van de grondgebieden van de lidstaten als omschreven in punt 2);

2)

„lidstaat” en „grondgebied van een lidstaat”: het grondgebied van iedere lidstaat van de Gemeenschap waarop het Verdrag houdende oprichting van de Europese Gemeenschap overeenkomstig zijn artikel 299 van toepassing is, met uitzondering van het (de) in artikel 6 van deze richtlijn genoemde gebied(en);

3)

„derdelandsgebieden”: de gebieden die in artikel 6 zijn genoemd;

4)

„derde land”: elke staat of elk grondgebied waarop het
Verdrag niet van toepassing is.

b)

het totale bedrag van de intracommunautaire verwervingen van goederen is in het lopende kalenderjaar niet hoger dan een door de lidstaten te bepalen maximumwaarde die niet lager mag zijn dan EUR 10 000 of de tegenwaarde daarvan in de nationale munteenheid; het totale bedrag van de intracommunautaire verwervingen van goederen heeft in het voorafgaande kalenderjaar de onder a) bepaalde maximumwaarde niet overschreden.

De maximumwaarde die als referentiepunt dient, is het totale bedrag van de intracommunautaire verwervingen van goederen als bedoeld in lid 1, onder b), de BTW die is verschuldigd of voldaan in de lidstaat van vertrek van de verzending of het vervoer van de goederen niet inbegrepen.
3. De lidstaten verlenen de belastingplichtigen en de nietbelastingplichtige rechtspersonen die voor de toepassing van lid 1, onder b), in aanmerking komen, het recht voor de in artikel 2, lid 1, onder b), punt i), omschreven algemene regeling te kiezen.
De lidstaten stellen de nadere regels vast voor de uitoefening van het in de eerste alinea bedoelde keuzerecht, dat in ieder geval voor een periode van twee kalenderjaren geldt.

###### Art. 6
1. Deze richtlijn is niet van toepassing op de volgende gebieden die deel uitmaken van het douanegebied van de Gemeenschap:
a)

de berg Athos;

b)

de Canarische Eilanden;


Publicatieblad van de Europese Unie

NL

c)

de Franse overzeese departementen;

d)

de Ålandseilanden;

e)

de Kanaaleilanden.

2. Deze richtlijn is niet van toepassing op de volgende gebieden die geen deel uitmaken van het douanegebied van de Gemeenschap:
a)

het eiland Helgoland;

b)

het gebied Büsingen;

c)

Ceuta;

d)

Melilla;

e)

Livigno;

f)

Campione d'Italia;

g)

de Italiaanse wateren van het meer van Lugano.

L 347/11

uitoefening van vrije of daarmede gelijkgestelde beroepen. Als economische activiteit wordt in het bijzonder beschouwd de exploitatie van een lichamelijke of onlichamelijke zaak om er duurzaam opbrengst uit te verkrijgen.
2. Naast de in lid 1 bedoelde personen wordt als belastingplichtige beschouwd eenieder die incidenteel een nieuw vervoermiddel levert dat door de verkoper, door de afnemer, of voor hun rekening, buiten het grondgebied van een lidstaat maar binnen het grondgebied van de Gemeenschap naar de afnemer wordt verzonden of vervoerd.
###### Art. 10
De in artikel 9, lid 1, bedoelde voorwaarde dat de economische activiteit zelfstandig moet worden verricht, sluit loontrekkenden en andere personen van de belastingheffing uit, voor zover zij met hun werkgever een arbeidsovereenkomst hebben aangegaan of enige andere juridische band hebben waaruit een verhouding van ondergeschiktheid ontstaat ten aanzien van de arbeids- en bezoldigingsvoorwaarden en de verantwoordelijkheid van de werkgever.

###### Art. 7
1. Het Vorstendom Monaco, het eiland Man en de zones die te
Akrotiri en Dhekelia onder de soevereiniteit van het Verenigd
Koninkrijk vallen, worden, gezien de overeenkomsten en verdragen die zij met respectievelijk Frankrijk, het Verenigd Koninkrijk en Cyprus hebben gesloten, voor de toepassing van deze richtlijn niet als derde landen beschouwd.
2. De lidstaten nemen de nodige maatregelen om te waarborgen dat handelingen met als herkomst of bestemming het Vorstendom Monaco als handelingen met herkomst of bestemming Frankrijk worden behandeld, dat handelingen met als herkomst of bestemming het eiland Man als handelingen met als herkomst of bestemming het Verenigd Koninkrijk worden behandeld en dat handelingen met als herkomst of bestemming de zones die te Akrotiri en Dhekelia onder de soevereiniteit van het Verenigd Koninkrijk vallen als handelingen met als herkomst of bestemming Cyprus worden behandeld.

###### Art. 11
Na raadpleging van het raadgevend Comité voor de Belasting op de toegevoegde waarde („BTW-comité”) kan elke lidstaat personen die binnen het grondgebied van deze lidstaat gevestigd zijn en die juridisch gezien zelfstandig zijn, doch financieel, economisch en organisatorisch nauw met elkaar verbonden zijn, tezamen als één belastingplichtige aanmerken.
Een lidstaat die de in de eerste alinea bedoelde mogelijkheid toepast, kan alle maatregelen vaststellen die nodig zijn om belastingfraude en -ontwijking met gebruikmaking van deze bepaling te voorkomen.
###### Art. 12
1. De lidstaten kunnen als belastingplichtige aanmerken eenieder die incidenteel een handeling verricht in verband met de in artikel 9, lid 1, tweede alinea, bedoelde werkzaamheden, met name een van de volgende handelingen:

###### Art. 8

a)

Indien de Commissie van mening is dat het bepaalde in de artikelen 6 en 7 niet meer gerechtvaardigd is, met name uit het oogpunt van de neutraliteit ten aanzien van de mededinging of van de eigen middelen, legt zij passende voorstellen aan de Raad voor.

de levering van een gebouw of een gedeelte van een gebouw en het bijbehorende terrein vóór de eerste ingebruikneming;

b)

de levering van een bouwterrein.

2. Voor de toepassing van lid 1, onder a), wordt als „gebouw” beschouwd ieder bouwwerk dat vast met de grond is verbonden.

### TITEL III
BELASTINGPLICHTIGEN

###### Art. 9
1. Als „belastingplichtige” wordt beschouwd eenieder die, op ongeacht welke plaats, zelfstandig een economische activiteit verricht, ongeacht het oogmerk of het resultaat van die activiteit.
Als „economische activiteit” worden beschouwd, alle werkzaamheden van een fabrikant, handelaar of dienstverrichter, met inbegrip van de winning van delfstoffen, de landbouw en de

De lidstaten kunnen de voorwaarden voor de toepassing van het in lid 1, onder a), bedoelde criterium op de verbouwing van gebouwen, alsmede het begrip „bijbehorend terrein” bepalen.
De lidstaten kunnen andere criteria dan dat van de eerste ingebruikneming toepassen, zoals het tijdvak dat verloopt tussen de datum van voltooiing van het gebouw en die van eerste levering, of het tijdvak tussen de datum van eerste ingebruikneming en die van de daaropvolgende levering, mits deze tijdvakken niet langer duren dan onderscheidenlijk vijf en twee jaar.

L 347/12

Publicatieblad van de Europese Unie

NL

3. Voor de toepassing van lid 1, onder b), wordt als „bouwterrein” beschouwd, de door de lidstaten als zodanig omschreven al dan niet bouwrijp gemaakte terreinen.

###### Art. 15

1. Elektriciteit, gas, warmte, koude en soortgelijke zaken worden met „lichamelijke zaken” gelijkgesteld.

###### Art. 13
2. De lidstaten kunnen als lichamelijke zaken beschouwen:
1. De staat, de regio's, de gewesten, de provincies, de gemeenten en de andere publiekrechtelijke lichamen worden niet als belastingplichtigen aangemerkt voor de werkzaamheden of handelingen die zij als overheid verrichten, ook niet indien zij voor die werkzaamheden of handelingen rechten, heffingen, bijdragen of retributies innen.

a)

bepaalde rechten op onroerende goederen;

b)

de zakelijke rechten die de rechthebbende de bevoegdheid verschaffen een onroerend goed te gebruiken;

Wanneer deze lichamen evenwel zodanige werkzaamheden of handelingen verrichten, moeten zij daarvoor als belastingplichtige worden aangemerkt, indien een behandeling als nietbelastingplichtige tot een verstoring van de mededinging van enige betekenis zou leiden.

c)

de deelbewijzen en aandelen waarvan het bezit rechtens of in feite recht geven op de eigendom of het genot van een onroerend goed of een deel daarvan.

De publiekrechtelijke lichamen worden in elk geval als belastingplichtige beschouwd voor de in bijlage I genoemde werkzaamheden, voorzover deze niet van onbeduidende omvang zijn.

Met een levering van goederen onder bezwarende titel wordt gelijkgesteld, het door een belastingplichtige aan zijn bedrijf onttrekken van een goed voor eigen privédoeleinden of voor privédoeleinden van zijn personeel, of dat hij om niet verstrekt of, meer in het algemeen, voor andere dan bedrijfsdoeleinden bestemt, ingeval met betrekking tot dat goed of de bestanddelen daarvan recht op volledige of gedeeltelijke aftrek van de BTW is ontstaan.

2. De lidstaten kunnen werkzaamheden van publiekrechtelijke lichamen die uit hoofde van de artikelen 132, 135, 136, 371, 374 tot en met 377, artikel 378, lid 2, artikel 379, lid 2, en de artikelen 380 tot en met 390 zijn vrijgesteld, als werkzaamheden van de overheid beschouwen.
### TITEL IV
BELASTBARE HANDELINGEN

###### Art. 16

Met een levering van goederen onder bezwarende titel worden niet gelijkgesteld, onttrekkingen van goederen om voor bedrijfsdoeleinden te dienen als geschenken van geringe waarde of als monster.
###### Art. 17

#### HOOFDSTUK 1

Levering van goederen
###### Art. 14
1. Als „levering van goederen” wordt beschouwd, de overdracht of overgang van de macht om als een eigenaar over een lichamelijke zaak te beschikken.
2. Naast de in lid 1 bedoelde handeling worden de volgende handelingen als een levering van goederen beschouwd:
a)

b)

c)

de eigendomsovergang van een goed tegen betaling van een vergoeding, ingevolge een vordering door of namens de overheid dan wel krachtens de wet; de afgifte van een goed ingevolge een overeenkomst volgens welke een goed gedurende een bepaalde periode in huur wordt gegeven of ingevolge een overeenkomst tot koop en verkoop op afbetaling, in beide gevallen onder het beding dat normaal het goed uiterlijk bij de betaling van de laatste termijn in eigendom wordt verkregen;

1. Met een levering van goederen onder bezwarende titel wordt gelijkgesteld, de overbrenging door een belastingplichtige van een goed van zijn bedrijf naar een andere lidstaat.
Als „overbrenging naar een andere lidstaat” wordt beschouwd iedere verzending of ieder vervoer van een roerende lichamelijke zaak voor bedrijfsdoeleinden, door of voor rekening van de belastingplichtige, buiten het grondgebied van de lidstaat waar het goed zich bevindt, maar binnen de Gemeenschap.
2. Als overbrenging naar een andere lidstaat wordt niet beschouwd, de verzending of het vervoer van een goed voor zover het daarbij om een van de volgende handelingen gaat:
a)

de levering van dat goed door de belastingplichtige binnen het grondgebied van de lidstaat van aankomst van de verzending of het vervoer, onder de in artikel 33 gestelde voorwaarden;

b)

de levering van dat goed, dat door of voor rekening van de leverancier moet worden geïnstalleerd of gemonteerd, door de belastingplichtige binnen het grondgebied van de lidstaat van aankomst van de verzending of het vervoer, onder de in artikel 36 gestelde voorwaarden;

c)

de levering van dat goed door de belastingplichtige aan boord van een schip, vliegtuig of trein tijdens een vervoer van passagiers, onder de in artikel 37 gestelde voorwaarden;

de overdracht van een goed ingevolge een overeenkomst tot koop of verkoop in commissie.

3. De lidstaten kunnen de oplevering van bepaalde werken in onroerende staat als een levering van goederen beschouwen.

d)

Publicatieblad van de Europese Unie

NL

de levering van gas via het aardgasdistributiesysteem of de levering van elektriciteit, onder de in de artikelen 38 en 39 gestelde voorwaarden;

L 347/13
###### Art. 19

De lidstaten kunnen, in geval van overgang van het geheel of een gedeelte van een algemeenheid van goederen onder bezwarende titel, om niet of in de vorm van een inbreng in een vennootschap, zich op het standpunt stellen dat geen levering van goederen heeft plaatsgevonden en dat degene op wie de goederen overgaan, in de plaats treedt van de overdrager.

e)

de levering van dat goed door de belastingplichtige binnen het grondgebied van de lidstaat, onder de in de artikelen 138, 146, 147, 148, 151 en 152 gestelde voorwaarden;

f)

de verrichting van een dienst voor de belastingplichtige in verband met werkzaamheden betreffende dat goed, die daadwerkelijk worden uitgevoerd binnen het grondgebied van de lidstaat van aankomst van de verzending of het vervoer van het goed, voor zover het goed na bewerking opnieuw wordt verzonden naar deze belastingplichtige in de lidstaat waarvandaan het oorspronkelijk was verzonden of vervoerd;

De lidstaten kunnen de nodige maatregelen nemen om verstoringen van de mededinging te voorkomen ingeval degene op wie de goederen overgaan, niet volledig belastingplichtig is.
Zij kunnen ook alle maatregelen vaststellen die nodig zijn om belastingfraude en -ontwijking met gebruikmaking van dit artikel te voorkomen.

het tijdelijke gebruik van dat goed binnen het grondgebied van de lidstaat van aankomst van de verzending of het vervoer, ten behoeve van diensten verricht door de binnen de lidstaat van vertrek van de verzending of het vervoer van het goed gevestigde belastingplichtige;

Intracommunautaire verwerving van goederen

g)

h)

het tijdelijke gebruik van dat goed voor een periode van ten hoogste 24 maanden binnen het grondgebied van een andere lidstaat waar de invoer van hetzelfde goed uit een derde land met het oog op tijdelijk gebruik in aanmerking zou komen voor de regeling voor tijdelijke invoer met volledige vrijstelling van invoerrechten.

3. Wanneer niet meer wordt voldaan aan een van de voorwaarden voor de toepassing van lid 2, wordt het goed als overgebracht naar een andere lidstaat beschouwd. In dat geval vindt de overbrenging plaats op het tijdstip waarop deze voorwaarde niet meer vervuld is.
###### Art. 18
De lidstaten kunnen de volgende handelingen met een levering van goederen onder bezwarende titel gelijkstellen:
a)

b)

c)

het door een belastingplichtige voor bedrijfsdoeleinden bestemmen van een goed dat in het kader van zijn bedrijf is vervaardigd, gebouwd, gewonnen, bewerkt, aangekocht of ingevoerd, indien het van een andere belastingplichtige betrekken van een dergelijk goed hem geen recht zou geven op volledige aftrek van de BTW; het door een belastingplichtige voor een niet-belaste sector van zijn bedrijfsuitoefening bestemmen van een goed, voor zover bij de verwerving van dat goed of bij de bestemming ervan overeenkomstig punt a) recht op volledige of gedeeltelijke aftrek van de BTW is ontstaan; met uitzondering van de in artikel 19 genoemde gevallen, het onder zich hebben van goederen door een belastingplichtige of zijn rechthebbenden wanneer hij zijn belastbare economische activiteit beëindigt, ingeval bij de verwerving van die goederen of bij de bestemming ervan overeenkomstig punt a) recht op volledige of gedeeltelijke aftrek van de BTW is ontstaan.

#### HOOFDSTUK 2

###### Art. 20
Als „intracommunautaire verwerving van goederen” wordt beschouwd het verkrijgen van de macht om als eigenaar te beschikken over een roerende lichamelijke zaak die door de verkoper of de afnemer, of voor hun rekening, met als bestemming de afnemer is verzonden of vervoerd naar een andere lidstaat dan de lidstaat van vertrek van de verzending of het vervoer van het goed.
Wanneer door een niet-belastingplichtige rechtspersoon verworven goederen uit een derdelandsgebied of een derde land worden verzonden of vervoerd en door deze niet-belastingplichtige rechtspersoon worden ingevoerd in een andere lidstaat dan die van aankomst van de verzending of het vervoer, worden de goederen geacht te zijn verzonden of vervoerd vanuit de lidstaat van invoer. Deze lidstaat verleent aan de importeur die uit hoofde van artikel 201 is aangewezen of erkend als de tot voldoening van de belasting gehouden persoon, teruggaaf van de uit hoofde van de invoer betaalde BTW, voorzover de importeur aantoont dat zijn verwerving in de lidstaat van aankomst van de verzending of het vervoer van de goederen aan de BTW onderworpen is geweest.
###### Art. 21
Met een intracommunautaire verwerving van goederen onder bezwarende titel wordt gelijkgesteld het door een belastingplichtige voor bedrijfsdoeleinden bestemmen van een goed dat door of voor rekening van de belastingplichtige wordt verzonden of vervoerd vanuit een andere lidstaat waar het is vervaardigd, gewonnen, bewerkt, aangekocht, verworven in de zin van artikel 2, lid 1, onder b), of door de belastingplichtige in het kader van zijn bedrijf in die andere lidstaat is ingevoerd.
###### Art. 22
Met een intracommunautaire verwerving van goederen onder bezwarende titel wordt gelijkgesteld de toewijzing door de strijdkrachten van een staat die partij bij het Noord-Atlantisch Verdrag is, ten behoeve van deze strijdkrachten of het hen begeleidende burgerpersoneel, van goederen die zij niet tegen de algemene belastingvoorwaarden van de interne markt van een lidstaat hebben verworven, wanneer de invoer van deze goederen niet in aanmerking zou kunnen komen voor de in artikel 143, punt h), bedoelde vrijstelling.

L 347/14

Publicatieblad van de Europese Unie

NL
###### Art. 23

De lidstaten nemen maatregelen om ervoor te zorgen dat als intracommunautaire verwerving van goederen worden beschouwd de handelingen die, indien zij op hun grondgebied door een als zodanig handelende belastingplichtige zouden zijn verricht, als levering van goederen zouden zijn aangemerkt.
#### HOOFDSTUK 3

Diensten
###### Art. 24
1. Als „dienst” wordt beschouwd elke handeling die geen levering van goederen is.
2. Als „telecommunicatiediensten” worden beschouwd de diensten waarmee de transmissie, uitzending of ontvangst van signalen, geschriften, beelden en geluiden of informatie van allerlei aard per draad, via radiofrequente straling, langs optische weg of met behulp van andere elektromagnetische middelen mogelĳk wordt gemaakt, met inbegrip van de daarmee samenhangende overdracht en verlening van rechten op het gebruik van infrastructuur voor de transmissie, uitzending of ontvangst, waaronder het bieden van toegang tot wereldwĳde informatienetten.
###### Art. 25
Een dienst kan onder meer een van de volgende handelingen zijn:
a)

de overdracht van een onlichamelijke zaak, ongeacht of deze al dan niet in een titel is belichaamd;

b)

de verplichting om een daad na te laten of om een daad of een situatie te dulden;

c)

het verrichten van een dienst op grond van een vordering door of namens de overheid, dan wel krachtens de wet.


dienst, voorzover hij, ingeval een dergelijke dienst door een andere belastingplichtige zou zijn verricht, geen recht op volledige aftrek van de BTW zou hebben.
###### Art. 28
Wanneer door tussenkomst van een belastingplichtige, handelend op eigen naam, maar voor rekening van een ander, een dienst wordt verricht, wordt de betrokken belastingplichtige geacht deze dienst zelf te hebben afgenomen en te hebben verricht.
###### Art. 29
Artikel 19 is op overeenkomstige wijze van toepassing op diensten.
#### HOOFDSTUK 4

Invoer van goederen
###### Art. 30
Als „invoer van goederen” wordt beschouwd het binnenbrengen in de Gemeenschap van een goed dat zich niet in het vrije verkeer bevindt in de zin van artikel 24 van het Verdrag.
Naast het in de eerste alinea bedoelde geval wordt als invoer van goederen beschouwd het binnenbrengen in de Gemeenschap van een goed dat zich in het vrije verkeer bevindt, uit een derdelandsgebied dat deel uitmaakt van het douanegebied van de Gemeenschap.
### TITEL V
PLAATS VAN DE BELASTBARE HANDELINGEN
#### HOOFDSTUK 1

Plaats van levering van goederen

###### Art. 26


1. Met diensten verricht onder bezwarende titel worden de volgende handelingen gelijkgesteld:

Lever ing van goederen zonder ver voer

a)

b)

##### Afdeling 1
###### Art. 31

het gebruiken van een tot het bedrijf behorend goed voor privédoeleinden van de belastingplichtige of van zijn personeel, of, meer in het algemeen, voor andere dan bedrijfsdoeleinden, wanneer voor dit goed recht op volledige of gedeeltelijke aftrek van de BTW is ontstaan;

Ingeval het goed niet wordt verzonden of vervoerd, wordt als plaats van levering aangemerkt de plaats waar het goed zich op het tijdstip van de levering bevindt.

het om niet verrichten van diensten door de belastingplichtige voor eigen privédoeleinden of voor privédoeleinden van zijn personeel, of, meer in het algemeen, voor andere dan bedrijfsdoeleinden.

Lever ing van goederen met ver voer


##### Afdeling 2
###### Art. 32

###### Art. 27

Ingeval het goed door de leverancier, door de afnemer of door een derde wordt verzonden of vervoerd, wordt als plaats van levering aangemerkt de plaats waar het goed zich op het tijdstip van vertrek van de verzending of het vervoer naar de afnemer bevindt.

Ter voorkoming van verstoring van de mededinging kunnen de lidstaten, na raadpleging van het BTW-Comité, met een dienst verricht onder bezwarende titel gelijkstellen het door een belastingplichtige voor bedrijfsdoeleinden verrichten van een

Ingeval de plaats van vertrek van de verzending of het vervoer echter in een derdelandsgebied of een derde land ligt, worden de plaats van de levering, verricht door de importeur die uit hoofde van artikel 201 is aangewezen of erkend als de tot voldoening

2. De lidstaten kunnen van lid 1 afwijken, mits deze afwijking niet tot verstoring van de mededinging leidt.


Publicatieblad van de Europese Unie

NL

van de belasting gehouden persoon, alsmede de plaats van daaropvolgende leveringen geacht in de lidstaat van invoer van de goederen te liggen.
###### Art. 33
1. In afwijking van artikel 32 wordt als de plaats van levering van goederen die door of voor rekening van de leverancier worden verzonden of vervoerd vanuit een andere lidstaat dan die van aankomst van de verzending of het vervoer, aangemerkt de plaats waar de goederen zich bevinden op het tijdstip van aankomst van de verzending of het vervoer naar de afnemer, wanneer de volgende voorwaarden vervuld zijn:
a)

b)

de levering van goederen wordt verricht voor een belastingplichtige of voor een niet–belastingplichtige rechtspersoon van wie de intracommunautaire verwervingen van goederen uit hoofde van artikel 3, lid 1, niet aan de BTW zijn onderworpen, of voor enige andere niet-belastingplichtige; de geleverde goederen zijn geen nieuwe vervoermiddelen, noch goederen, geleverd na montage of installatie, door of voor rekening van de leverancier, met of zonder beproeven van de geïnstalleerde of gemonteerde goederen.

2. Wanneer de geleverde goederen uit een derdelandsgebied of een derde land worden verzonden of vervoerd en door de leverancier worden ingevoerd in een andere lidstaat dan de lidstaat van aankomst van de verzending of het vervoer naar de afnemer, worden zij geacht te zijn verzonden of vervoerd vanuit de lidstaat van invoer.
###### Art. 34
1. Artikel 33 is niet van toepassing op de leveringen van goederen die alle worden verzonden of vervoerd naar eenzelfde lidstaat van aankomst van de verzending of het vervoer indien de volgende voorwaarden vervuld zijn:
a)

de geleverde goederen zijn geen accijnsproducten;

b)

het totale bedrag, de BTW niet inbegrepen, van de onder de voorwaarden van artikel 33 in die lidstaat verrichte leveringen in eenzelfde kalenderjaar is niet hoger dan EUR 100 000 of de tegenwaarde daarvan in de nationale munteenheid;

c)

het totale bedrag, de BTW niet inbegrepen, van de onder de voorwaarden van artikel 33 in de lidstaat verrichte leveringen van andere goederen dan accijnsproducten in het voorafgaande kalenderjaar is niet hoger dan EUR 100 000 of de tegenwaarde daarvan in de nationale munteenheid.

2. De lidstaat binnen het grondgebied waarvan de goederen zich bevinden op het tijdstip van aankomst van de verzending of het vervoer naar de afnemer, mag het in lid 1 genoemde maximumbedrag beperken tot EUR 35 000 of de tegenwaarde daarvan in de nationale munteenheid, wanneer deze lidstaat vreest dat het maximum van EUR 100 000 tot ernstige verstoring van de mededinging zou leiden.
De lidstaten die van de in de eerste alinea bedoelde mogelijkheid gebruik maken, nemen de nodige maatregelen om de bevoegde

L 347/15

overheidsinstanties van de lidstaat van vertrek van de verzending of het vervoer van de goederen daarvan in kennis te stellen.
3. De Commissie dient zo spoedig mogelijk bij de Raad een verslag in over de werking van het in lid 2 genoemde bijzondere maximum van EUR 35 000 en doet dit in voorkomend geval vergezeld gaan van passende voorstellen.
4. De lidstaat binnen het grondgebied waarvan de goederen zich op het tijdstip van vertrek van de verzending of het vervoer bevinden, verleent de belastingplichtigen die leveringen van goederen verrichten welke in aanmerking kunnen komen voor het bepaalde in lid 1, het recht ervoor te kiezen dat de plaats van deze leveringen wordt bepaald overeenkomstig artikel 33.
De betrokken lidstaten stellen de nadere regels vast voor de uitoefening van het in de eerste alinea bedoelde keuzerecht, dat in ieder geval voor een periode van twee kalenderjaren geldt.
###### Art. 35
De artikelen 33 en 34 zijn niet van toepassing op de leveringen van gebruikte goederen, kunstvoorwerpen, voorwerpen voor verzamelingen en antiquiteiten, zoals omschreven in artikel 311, lid 1, punten 1) tot en met 4), noch op leveringen van gebruikte vervoermiddelen als omschreven in artikel 327, lid 3, die aan de BTW zijn onderworpen overeenkomstig de toepasselijke bijzondere regelingen.
###### Art. 36
Ingeval het door de leverancier, door de afnemer of door een derde verzonden of vervoerde goed door of voor rekening van de leverancier wordt geïnstalleerd of gemonteerd, met of zonder beproeven van het geïnstalleerde of gemonteerde goed, wordt als plaats van de levering aangemerkt de plaats waar de installatie of de montage geschiedt.
Wanneer de installatie of de montage plaatsvindt in een andere lidstaat dan die van de leverancier, treft de lidstaat op het grondgebied waarvan de installatie of de montage plaatsvindt, de nodige maatregelen om dubbele belastingheffing in deze lidstaat te voorkomen.
Lever ing van goederen aan boord van een schip, vliegtuig of trein
##### Afdeling 3
###### Art. 37
1. Ingeval de levering van goederen plaatsvindt aan boord van een schip, vliegtuig of trein en tijdens het in de Gemeenschap verrichte gedeelte van een passagiersvervoer, wordt als plaats van deze levering aangemerkt de plaats van vertrek van het passagiersvervoer.
2. Voor de toepassing van lid 1 wordt onder „in de Gemeenschap verricht gedeelte van een passagiersvervoer” verstaan, het gedeelte van een vervoer dat, zonder tussenstop buiten de Gemeenschap, plaatsvindt tussen de plaats van vertrek en de plaats van aankomst van het passagiersvervoer.

L 347/16

Publicatieblad van de Europese Unie

NL

Als „plaats van vertrek van een passagiersvervoer” wordt beschouwd het eerste punt in de Gemeenschap waar passagiers aan boord kunnen komen, eventueel na een tussenstop buiten de Gemeenschap.

#### HOOFDSTUK 2

Plaats van een intracommunautaire verwerving van goederen
###### Art. 40

Als „plaats van aankomst van een passagiersvervoer” wordt beschouwd het laatste punt in de Gemeenschap waar passagiers die binnen de Gemeenschap aan boord zijn gekomen, van boord kunnen gaan, eventueel vóór een tussenstop buiten de Gemeenschap.

Als plaats van een intracommunautaire verwerving van goederen wordt aangemerkt de plaats waar de goederen zich bevinden op het tijdstip van aankomst van de verzending of van het vervoer naar de afnemer.

Ingeval het een heen- en terugreis betreft, wordt de terugreis als een afzonderlijk vervoer beschouwd.

###### Art. 41

3. De Commissie legt de Raad zo spoedig mogelijk een verslag voor, dat in voorkomend geval vergezeld gaat van passende voorstellen, over de plaats van belastingheffing op leveringen van voor verbruik aan boord bestemde goederen en op diensten, met inbegrip van restauratie, die worden verleend aan passagiers aan boord van een schip, vliegtuig of trein.

Onverminderd artikel 41 wordt als plaats van een intracommunautaire verwerving van goederen als bedoeld in artikel 2, lid 1, onder b), punt i), aangemerkt het grondgebied van de lidstaat die het BTW-identificatienummer heeft toegekend waaronder de afnemer deze verwerving heeft verricht, voor zover de afnemer niet aantoont dat de BTW op deze verwerving is geheven overeenkomstig artikel 40.

Totdat de in de eerste alinea bedoelde voorstellen zijn aangenomen, kunnen de lidstaten leveringen van voor verbruik aan boord bestemde goederen waarvan de plaats van belastingheffing overeenkomstig lid 1 wordt vastgesteld, vrijstellen of blijven vrijstellen, met recht op aftrek van voorbelasting.

Indien op de verwerving uit hoofde van artikel 40 BTW wordt geheven in de lidstaat van aankomst van de verzending of van het vervoer van de goederen, nadat de BTW erop is geheven op grond van de eerste alinea, wordt de maatstaf van heffing dienovereenkomstig verlaagd in de lidstaat die het BTWidentificatienummer heeft toegekend waaronder de afnemer deze verwerving heeft verricht.

Levering van goederen via distributiesystemen

##### Afdeling 4
###### Art. 42

###### Art. 38
1. Ingeval de levering van gas via het aardgasdistributiesysteem of van elektriciteit wordt verricht aan een belastingplichtige wederverkoper wordt als plaats van deze levering aangemerkt, de plaats waar de belastingplichtige wederverkoper de zetel van zijn bedrijfsuitoefening of een vaste inrichting heeft gevestigd waarvoor de goederen worden geleverd, dan wel, bij gebreke van een dergelijke zetel of vaste inrichting, zijn woonplaats of zijn gebruikelijke verblijfplaats.
2. Voor de toepassing van lid 1 wordt onder „belastingplichtige wederverkoper” verstaan, een belastingplichtige wiens hoofdactiviteit op het gebied van de aankoop van gas of elektriciteit bestaat in het wederverkopen van die producten en wiens eigen verbruik van die producten verwaarloosbaar is.

Artikel 41, eerste alinea, is niet van toepassing en de intracommunautaire verwerving van goederen wordt geacht overeenkomstig artikel 40 aan de BTW te zijn onderworpen wanneer de volgende voorwaarden vervuld zijn:
a)

de afnemer toont aan deze verwerving te hebben verricht met het oog op een daaropvolgende levering binnen het grondgebied van de overeenkomstig artikel 40 bepaalde lidstaat, waarvoor degene voor wie deze levering bestemd is, overeenkomstig artikel 197 is aangewezen als de tot voldoening van de belasting gehouden persoon;

b)

de afnemer heeft voldaan aan de in artikel 265 bedoelde verplichtingen inzake de indiening van de aldaar bedoelde lijst.

###### Art. 39

#### HOOFDSTUK 3

In het geval van een levering van gas via het aardgasdistributiesysteem of van elektriciteit die niet wordt bestreken door artikel 38, wordt als plaats van deze levering aangemerkt, de plaats waar de afnemer het werkelijke gebruik en verbruik van de goederen heeft.

Plaats van een dienst
Algemene regel

Ingeval alle goederen of een deel ervan niet daadwerkelijk door deze afnemer worden verbruikt, worden deze niet verbruikte goederen geacht te zijn gebruikt en verbruikt op de plaats waar hij de zetel van zijn bedrijfsuitoefening of een vaste inrichting heeft gevestigd waarvoor de goederen worden geleverd. Bij gebreke van een dergelijke zetel of vaste inrichting wordt de afnemer geacht de goederen te hebben gebruikt en verbruikt in zijn woonplaats of gebruikelijke verblijfplaats.

##### Afdeling 1
###### Art. 43
Als plaats van een dienst wordt aangemerkt, de plaats waar de dienstverrichter de zetel van zijn bedrijfsuitoefening of een vaste inrichting heeft gevestigd van waaruit hij de dienst verricht, of bij gebreke van een dergelijke zetel of vaste inrichting, zijn woonplaats of zijn gebruikelijke verblijfplaats.


Publicatieblad van de Europese Unie

NL

L 347/17

plaats van aankomst op het grondgebied van twee verschillende lidstaten gelegen zijn.

Bijzondere bepalingen
##### Afdeling 2
##### Onderafdeling 1
Diensten van tussenpersonen

###### Art. 44
Als plaats van een door een in naam en voor rekening van een ander handelende tussenpersoon verrichte dienst, anders dan de in artikel 50, artikel 54 en artikel 56, lid 1, bedoelde diensten, wordt aangemerkt de plaats waar de onderliggende handeling overeenkomstig deze richtlijn wordt verricht.
Wanneer echter de afnemer van de door de tussenpersoon verrichte dienst voor BTW-doeleinden is geïdentificeerd in een andere lidstaat dan die binnen het grondgebied waarvan die handeling wordt verricht, wordt de plaats van de door de tussenpersoon verrichte dienst geacht te zijn gelegen op het grondgebied van de lidstaat die aan de afnemer het BTWidentificatienummer heeft toegekend waaronder hem de dienst is verleend.
##### Onderafdeling 2
Diensten met betrekking tot onroerende goederen

###### Art. 45
De plaats van diensten die betrekking hebben op een onroerend goed, met inbegrip van diensten van makelaars in onroerende goederen en van experts, alsmede van diensten die erop gericht zijn de uitvoering van bouwwerken voor te bereiden of te coördineren, zoals bijvoorbeeld de diensten verricht door architecten en bureaus die op de uitvoering van het werk toezicht houden, is de plaats waar het goed is gelegen.
##### Onderafdeling 3
Ve r v o e r d i e n s t e n

Als „plaats van vertrek” wordt beschouwd de plaats waar het goederenvervoer daadwerkelijk begint, zonder rekening te houden met de trajecten die worden afgelegd om zich naar de plaats te begeven waar de goederen zich bevinden.
Als „plaats van aankomst” wordt beschouwd de plaats waar het goederenvervoer daadwerkelijk eindigt.
###### Art. 49
Met intracommunautair goederenvervoer wordt gelijkgesteld goederenvervoer waarvan de plaats van vertrek en die van aankomst binnen het grondgebied van eenzelfde lidstaat zijn gelegen, wanneer dit vervoer rechtstreeks samenhangt met goederenvervoer waarvan de plaats van vertrek en die van aankomst binnen het grondgebied van twee verschillende lidstaten zijn gelegen.
###### Art. 50
De plaats van diensten verricht door een in naam en voor rekening van een ander handelende tussenpersoon, indien hij bemiddelt bij het verrichten van intracommunautaire goederenvervoerdiensten, is de plaats van vertrek van het vervoer.
Wanneer echter de afnemer van de door de tussenpersoon verrichte dienst voor BTW-doeleinden is geïdentificeerd in een andere lidstaat dan de lidstaat van vertrek van het vervoer, wordt de plaats van de door de tussenpersoon verrichte dienst geacht te zijn gelegen binnen het grondgebied van de lidstaat die aan de afnemer het BTW-identificatienummer heeft toegekend waaronder de dienst voor hem is verricht.
###### Art. 51
De lidstaten behoeven het gedeelte van het intracommunautaire goederenvervoer dat overeenkomt met de trajecten die zijn afgelegd over wateren die niet tot het grondgebied van de Gemeenschap behoren, niet aan de BTW te onderwerpen.

###### Art. 46
De plaats van andere vervoerdiensten dan het intracommunautaire vervoer van goederen is de plaats waar het vervoer plaatsvindt, zulks naar verhouding van de afgelegde afstanden.

##### Onderafdeling 4
Culturele en soortgelijke diensten, diensten die samenhangen met ver voer of betrekking hebben op roerende lichamelijke zaken

###### Art. 47
De plaats van intracommunautaire goederenvervoerdiensten is de plaats van vertrek van het vervoer.
Wanneer echter intracommunautaire goederenvervoerdiensten worden verricht voor afnemers die voor BTW-doeleinden zijn geïdentificeerd in een andere lidstaat dan de lidstaat van vertrek van het vervoer, wordt de plaats van de diensten geacht te zijn gelegen binnen het grondgebied van de lidstaat die aan de afnemer het BTW-identificatienummer heeft toegekend waaronder hem de dienst is verleend.

###### Art. 52
De plaats van de volgende diensten is de plaats waar die diensten daadwerkelijk worden verricht:
a)

culturele, artistieke, sportieve, wetenschappelijke, onderwijs-, amusements- of soortgelijke activiteiten, met inbegrip van die van de organisatoren van dergelijke activiteiten, alsmede in voorkomend geval, van daarmee samenhangende diensten;

b)

activiteiten die met vervoer samenhangen, zoals laden, lossen, intern vervoer en soortgelijke activiteiten;

c)

expertises of werkzaamheden met betrekking tot roerende lichamelijke zaken.

###### Art. 48
Als „intracommunautair goederenvervoer” wordt beschouwd ieder vervoer van goederen waarvan de plaats van vertrek en de

L 347/18

Publicatieblad van de Europese Unie

NL


###### Art. 53

c)

In afwijking van artikel 52, punt b), wordt de plaats van diensten in verband met activiteiten die samenhangen met intracommunautair goederenvervoer, verricht voor afnemers die voor BTWdoeleinden zijn geïdentificeerd in een andere lidstaat dan die op het grondgebied waarvan de activiteiten daadwerkelijk worden verricht, geacht te zijn gelegen binnen het grondgebied van de lidstaat die aan de afnemer het BTW-identificatienummer heeft toegekend waaronder de dienst voor hem is verricht.

diensten verricht door raadgevende personen, ingenieurs, adviesbureaus, advocaten, accountants en andere soortgelijke diensten, alsmede informatieverwerking en informatieverschaffing;

d)

de verbintenis een beroepsactiviteit of een in dit lid vermeld recht geheel of gedeeltelijk niet uit te oefenen;

e)

bank-, financiële en verzekeringsverrichtingen met inbegrip van herverzekeringsverrichtingen en met uitzondering van de verhuur van safeloketten;

f)

het beschikbaar stellen van personeel;

g)

de verhuur van roerende lichamelijke zaken, met uitzondering van alle vervoermiddelen;

Wanneer echter de afnemer van de door de tussenpersoon verrichte dienst voor BTW-doeleinden is geïdentificeerd in een andere lidstaat dan die binnen het grondgebied waarvan de met het vervoer samenhangende activiteiten daadwerkelijk worden verricht, wordt de plaats van de door de tussenpersoon verrichte dienst geacht te zijn gelegen binnen het grondgebied van de lidstaat die aan de afnemer het BTW-identificatienummer heeft toegekend waaronder de dienst voor hem is verricht.

h)

het bieden van toegang tot aardgas- en elektriciteitsdistributiesystemen alsmede het verrichten van transport - en transmissiediensten via deze systemen en het verrichten van andere daarmee rechtstreeks verbonden diensten;

i)

telecommunicatiediensten;

###### Art. 55

j)

radio- en televisieomroepdiensten;

k)

langs elektronische weg verrichte diensten, en met name de in bijlage II bedoelde diensten;

l)

de diensten verricht door een in naam en voor rekening van een ander handelende tussenpersoon wanneer hij bemiddelt bij het verrichten van de in dit lid bedoelde diensten.

###### Art. 54
De plaats van diensten verricht door een in naam en voor rekening van een ander handelende tussenpersoon, wanneer hij bemiddelt bij het verrichten van een dienst in verband met activiteiten die samenhangen met intracommunautair goederenvervoer, is de plaats waar de met het vervoer samenhangende activiteiten daadwerkelijk worden verricht.

In afwijking van artikel 52, onder c), wordt bij expertises of werkzaamheden met betrekking tot roerende lichamelijke zaken die worden verricht voor afnemers die voor BTW-doeleinden zijn geïdentificeerd in een andere lidstaat dan die op het grondgebied waarvan de dienst daadwerkelijk wordt verricht, de plaats van de diensten geacht te zijn gelegen op het grondgebied van de lidstaat die aan de afnemer het BTW-identificatienummer heeft toegekend waaronder de dienst voor hem is verricht.
De in de eerste alinea bedoelde afwijking is slechts van toepassing indien de goederen worden verzonden of vervoerd buiten de lidstaat waar de dienst daadwerkelijk is verricht.

2. Het feit dat een dienstverrichter en zijn afnemer via elektronische post communiceren, betekent op zich niet dat de verrichte dienst een elektronische dienst is in de zin van lid 1, punt k).

##### Onderafdeling 5
Diverse diensten

3. Lid 1, punten j) en k), en lid 2 zijn van toepassing tot en met
31 december 2006.

###### Art. 56
###### Art. 57
1. De plaats van de volgende diensten die worden verricht voor afnemers die buiten de Gemeenschap zijn gevestigd of voor belastingplichtigen die weliswaar in de Gemeenschap doch buiten het land van de dienstverrichter zijn gevestigd, is de plaats waar de afnemer de zetel van zijn bedrijfsuitoefening of een vaste inrichting heeft gevestigd waarvoor de dienst is verricht, of bij gebreke van een dergelijke zetel of vaste inrichting, zijn woonplaats of zijn gebruikelijke verblijfplaats:
a)

de overdracht en het verlenen van auteursrechten, octrooien, licentierechten, fabrieks- en handelsmerken, en andere soortgelijke rechten;

1. Ingeval de in artikel 56, lid 1, punt k), bedoelde diensten worden verricht voor een niet-belastingplichtige die in een lidstaat is gevestigd of er zijn woonplaats of zijn gebruikelijke verblijfplaats heeft, door een belastingplichtige die de zetel van zijn bedrijfsuitoefening buiten de Gemeenschap heeft gevestigd of daar over een vaste inrichting beschikt van waaruit de dienst wordt verricht of die, bij gebreke van een dergelijke zetel of vaste inrichting, zijn woonplaats of gebruikelijke verblijfplaats buiten de Gemeenschap heeft, is de plaats van deze dienst de plaats waar de niet-belastingplichtige gevestigd is of zijn woonplaats of gebruikelijke verblijfplaats heeft.

b)

diensten op het gebied van de reclame;

2. Lid 1 is van toepassing tot en met 31 december 2006.


Publicatieblad van de Europese Unie

NL
##### Onderafdeling 6

Cr iterium inzake werkelijk gebr uik en werkelijke exploitatie

###### Art. 58
Teneinde dubbele heffing of niet-heffing van de belasting alsmede verstoring van de mededinging te voorkomen, kunnen de lidstaten voor de in artikel 56, lid 1, bedoelde diensten alsmede voor de verhuur van vervoermiddelen:
a)

b)

de plaats van deze diensten of van sommige ervan, die op hun grondgebied is gelegen, aanmerken als buiten de Gemeenschap te zijn gelegen, wanneer het werkelijke gebruik en de werkelijke exploitatie buiten de Gemeenschap geschieden;

regelingen of situaties, onder een regeling voor tijdelijke invoer met volledige vrijstelling van invoerrechten of onder een regeling voor extern douanevervoer wordt geplaatst, de invoer van dat goed plaats in de lidstaat op het grondgebied waarvan het goed aan die regelingen of situaties wordt onttrokken.
Wanneer een goed dat zich in het vrije verkeer bevindt, vanaf het binnenbrengen ervan in de Gemeenschap onder een van de in de artikelen 276 en 277 bedoelde regelingen of situaties wordt geplaatst, vindt de invoer van dat goed plaats in de lidstaat binnen het grondgebied waarvan het goed aan die regelingen of situaties wordt onttrokken.
### TITEL VI
BELASTBAAR FEIT EN VERSCHULDIGDHEID VAN DE
BELASTING

de plaats van deze diensten of van sommige ervan, die buiten de Gemeenschap is gelegen, aanmerken als op hun grondgebied te zijn gelegen, wanneer het werkelijke gebruik en de werkelijke exploitatie op hun grondgebied geschieden.

Deze bepaling geldt echter niet voor de in artikel 56, lid 1, punt k), bedoelde diensten, wanneer deze voor niet-belastingplichtigen worden verricht.

#### HOOFDSTUK 1

Algemene bepalingen
###### Art. 62
Voor de toepassing van deze richtlijn:
1)

wordt onder „belastbaar feit” verstaan het feit waardoor de wettelijke voorwaarden, vereist voor het verschuldigd worden van de belasting, worden vervuld;

2)

wordt de belasting geacht „verschuldigd te zijn” wanneer de schatkist krachtens de wet de belasting met ingang van een bepaald tijdstip van de belastingplichtige kan vorderen, ook al kan de betaling daarvan worden uitgesteld.

###### Art. 59
1. De lidstaten passen artikel 58, onder b), toe op telecommunicatiediensten die worden verricht voor niet-belastingplichtigen die in een lidstaat gevestigd zijn of er hun woonplaats of gebruikelijke verblijfplaats hebben, door een belastingplichtige die de zetel van zijn bedrijfsuitoefening buiten de Gemeenschap heeft gevestigd of daar over een vaste inrichting beschikt van waaruit de diensten worden verricht, of die, bij gebreke van een dergelijke zetel of vaste inrichting, zijn woonplaats of gebruikelijke verblijfplaats buiten de Gemeenschap heeft.
2. Tot en met 31 december 2006 passen de lidstaten artikel 58, punt b), toe op de in artikel 56, lid 1, punt j), bedoelde radio- en televisieomroepdiensten welke worden verricht voor niet-belastingplichtigen die in een lidstaat gevestigd zijn of er hun woonplaats of gebruikelijke verblijfplaats hebben, door een belastingplichtige die de zetel van zijn bedrijfsuitoefening buiten de Gemeenschap heeft gevestigd of daar over een vaste inrichting beschikt van waaruit de diensten worden verricht, of die, bij gebreke van een dergelijke zetel of vaste inrichting, zijn woonplaats of gebruikelijke verblijfplaats buiten de Gemeenschap heeft.
#### HOOFDSTUK 4

Plaats van invoer van goederen
###### Art. 60
De invoer van goederen vindt plaats in de lidstaat binnen het grondgebied waarvan het goed zich ten tijde van het binnenkomen in de Gemeenschap bevindt.

L 347/19

#### HOOFDSTUK 2

Goederenleveringen en diensten
###### Art. 63
Het belastbare feit vindt plaats en de belasting wordt verschuldigd op het tijdstip waarop de goederenleveringen of de diensten worden verricht.
###### Art. 64
1. Wanneer zij aanleiding geven tot opeenvolgende afrekeningen of betalingen worden goederenleveringen, met uitzondering van de leveringen van goederen die gedurende een bepaalde periode in huur worden gegeven of op afbetaling worden verkocht als bedoeld in artikel 14, lid 2, punt b), en diensten geacht te zijn verricht bij het verstrijken van de periode waarop deze afrekeningen of betalingen betrekking hebben.
2. De lidstaten kunnen bepalen dat in bepaalde gevallen goederenleveringen en diensten die gedurende een zekere periode doorlopend worden verricht, worden geacht ten minste eenmaal per jaar te zijn voltooid.
###### Art. 65

###### Art. 61
In afwijking van artikel 60 vindt, wanneer een goed dat zich niet in het vrije verkeer bevindt, vanaf het binnenbrengen ervan in de Gemeenschap onder een van de in artikel 156 bedoelde

Indien vooruitbetalingen worden gedaan alvorens de goederen zijn geleverd of de diensten zijn verricht, wordt de belasting verschuldigd op het tijdstip van ontvangst van de vooruitbetalingen, ten belope van het ontvangen bedrag.

L 347/20

Publicatieblad van de Europese Unie

NL


###### Art. 66

###### Art. 71

In afwijking van de artikelen 63, 64 en 65 kunnen de lidstaten bepalen dat de belasting voor bepaalde handelingen of bepaalde categorieën belastingplichtigen op één van de volgende tijdstippen verschuldigd wordt:

1. Wanneer goederen vanaf het binnenbrengen ervan in de
Gemeenschap onder een van de in de artikelen 156, 276 en 277 bedoelde regelingen of situaties, onder een regeling voor tijdelijk invoer met volledig vrijstelling van invoerrechten of onder een regeling voor extern douanevervoer worden geplaatst, vindt het belastbare feit pas plaats en wordt de belasting pas verschuldigd op het tijdstip waarop de goederen aan die regelingen of situaties worden onttrokken.

a)

uiterlijk bij de uitreiking van de factuur;

b)

uiterlijk bij ontvangst van de prijs;

c)

wanneer de factuur niet of niet tijdig wordt uitgereikt, binnen een bepaalde termijn te rekenen vanaf de datum van het belastbare feit.
###### Art. 67

1. Wanneer, onder de in artikel 138 vastgestelde voorwaarden, naar een andere lidstaat dan de lidstaat van vertrek van de verzending of het vervoer verzonden of vervoerde goederen, met vrijstelling van BTW worden geleverd of goederen met vrijstelling van BTW door een belastingplichtige voor bedrijfsdoeleinden naar een andere lidstaat worden overgebracht, wordt de belasting verschuldigd op de 15e van de maand volgende op die waarin het belastbare feit zich heeft voorgedaan.

Wanneer de ingevoerde goederen echter onderworpen zijn aan invoerrechten, aan landbouwheffingen of aan heffingen van gelijke werking die zijn ingesteld in het kader van een gemeenschappelijk beleid, vindt het belastbare feit plaats en wordt de belasting verschuldigd op het tijdstip waarop het belastbare feit en het verschuldigd worden ter zake van deze rechten zich voordoen.
2. In de gevallen waarin de ingevoerde goederen niet aan een van de in lid 1, tweede alinea, bedoelde rechten zijn onderworpen, passen de lidstaten met betrekking tot het belastbare feit en het verschuldigd worden van de belasting de geldende bepalingen inzake invoerrechten toe.
### TITEL VII
MAATSTAF VAN HEFFING

2. In afwijking van lid 1 wordt de belasting verschuldigd bij de uitreiking van de in artikel 220 bedoelde factuur wanneer deze factuur is uitgereikt vóór de 15e van de maand volgende op die waarin het belastbare feit zich heeft voorgedaan.

#### HOOFDSTUK 1

Definitie

#### HOOFDSTUK 3

###### Art. 72

Intracommunautaire verwerving van goederen

Voor de toepassing van deze richtlijn wordt als „normale waarde” beschouwd het volledige bedrag dat een afnemer, om de desbetreffende goederen of diensten op dat tijdstip te verkrijgen, in dezelfde handelsfase als waarin de goederenlevering of de dienst wordt verricht, op het tijdstip van die verrichting en bij vrije mededinging zou moeten betalen aan een zelfstandige leverancier of dienstverrichter op het grondgebied van de lidstaat waar de verrichting belastbaar is.

###### Art. 68
Het belastbare feit vindt plaats op het tijdstip waarop de intracommunautaire verwerving van goederen wordt verricht.
De intracommunautaire verwerving van goederen wordt geacht te zijn verricht op het tijdstip waarop de levering van soortgelijke goederen binnen het grondgebied van de lidstaat wordt geacht te zijn verricht.
###### Art. 69

Indien geen vergelijkbare verrichting voorhanden is, wordt onder
„normale waarde” het volgende verstaan:
1)

met betrekking tot goederen, een waarde die niet lager is dan de aankoopprijs van de goederen of van soortgelijke goederen of, indien er geen aankoopprijs is, dan de kostprijs, berekend op het tijdstip waarop de levering wordt verricht;

2)

met betrekking tot diensten, een waarde die niet lager is dan de door de belastingplichtige voor het verrichten van de dienst gemaakte uitgaven.

1. Voor de intracommunautaire verwervingen van goederen wordt de belasting verschuldigd op de 15e van de maand volgende op die waarin het belastbare feit zich heeft voorgedaan.
2. In afwijking van lid 1 wordt de belasting verschuldigd bij de uitreiking van de in artikel 220 bedoelde factuur wanneer deze factuur is uitgereikt vóór de 15e van de maand volgende op die waarin het belastbare feit zich heeft voorgedaan.

#### HOOFDSTUK 2

#### HOOFDSTUK 4

Goederenleveringen en diensten

Invoer van goederen

###### Art. 73

###### Art. 70

Voor andere goederenleveringen en diensten dan die bedoeld in de artikelen 74 tot en met 77 omvat de maatstaf van heffing alles wat de leverancier of dienstverrichter voor deze handelingen als tegenprestatie verkrijgt of moet verkrijgen van de zijde van de

Het belastbare feit vindt plaats en de belasting wordt verschuldigd op het tijdstip waarop de invoer van de goederen geschiedt.


Publicatieblad van de Europese Unie

NL

afnemer of van een derde, met inbegrip van subsidies die rechtstreeks met de prijs van deze handelingen verband houden.

c)

###### Art. 74
Voor het door een belastingplichtige onttrekken van goederen aan zijn bedrijf of bestemmen van goederen voor zijn bedrijf en het onder zich hebben van goederen door een belastingplichtige of zijn rechthebbenden wanneer hij zijn belastbare economische activiteit beëindigt, als bedoeld in de artikelen 16 en 18, is de maatstaf van heffing de aankoopprijs van de goederen of van soortgelijke goederen of, bij gebreke van een aankoopprijs, de kostprijs, berekend op het tijdstip waarop deze handelingen worden verricht.
###### Art. 75
Voor de in artikel 26 bedoelde diensten, waarbij een tot het bedrijf behorend goed voor privédoeleinden wordt gebruikt of diensten om niet worden verricht, is de maatstaf van heffing het bedrag van de door de belastingplichtige voor het verrichten van de diensten gemaakte kosten.

###### Art. 80
1. Om belastingfraude en belastingontwijking te voorkomen, kunnen de lidstaten in de volgende gevallen bepalen dat voor goederenleveringen of diensten waarbij familiale of andere nauwe persoonlijke, bestuurlijke, eigendoms-, lidmaatschaps-, financiële of juridische banden zoals omschreven door de lidstaat bestaan, de maatstaf van heffing de normale waarde is:
a)

wanneer de tegenprestatie lager is dan de normale waarde en de afnemer geen volledig recht op aftrek uit hoofde van de artikelen 167 tot en met 171 en 173 tot en met 177 heeft;

b)

wanneer de tegenprestatie lager is dan de normale waarde, degene die de handeling verricht geen volledig recht op aftrek uit hoofde van de artikelen 167 tot en met 171 en 173 tot en met 177 heeft en de handeling uit hoofde van de artikelen 132, 135, 136, 371, 375, 367 en 377, artikel 378, lid 2, of artikel 379, lid 2, en de artikelen 380 tot en met 390, is vrijgesteld;

c)

wanneer de tegenprestatie hoger is dan de normale waarde en degene die de handeling verricht geen volledig recht op aftrek uit hoofde van de artikelen 167 tot en met 171 en 173 tot en met 177 heeft.

###### Art. 77
Voor de door een belastingplichtige voor bedrijfsdoeleinden verrichte diensten, bedoeld in artikel 27, is de maatstaf van heffing de normale waarde van de verrichte diensten.

door een belastingplichtige van de afnemer als terugbetaling van in naam en voor rekening van laatstgenoemden gemaakte kosten ontvangen bedragen die in de boekhouding van de belastingplichtige als doorlopende posten voorkomen.

De belastingplichtige moet het werkelijke bedrag van de in de eerste alinea punt c), bedoelde kosten verantwoorden en mag de eventueel daarop drukkende BTW niet in aftrek brengen.

###### Art. 76
Voor goederenleveringen bestaande in de overbrenging naar een andere lidstaat is de maatstaf van heffing de aankoopprijs van de goederen of van soortgelijke goederen of, bij gebreke van een aankoopprijs, de kostprijs, berekend op het tijdstip waarop deze handelingen worden verricht.

L 347/21

###### Art. 78
In de maatstaf van heffing moeten de volgende elementen worden opgenomen:
a)

b)

belastingen, rechten en heffingen, met uitzondering van de
BTW zelf; bijkomende kosten, zoals kosten van commissie, verpakking, vervoer en verzekering, die de leverancier de afnemer in rekening brengt.

Voor de toepassing van punt b) van de eerste alinea mogen de lidstaten uitgaven die bij afzonderlijke overeenkomst zijn geregeld, als bijkomende kosten beschouwen.
###### Art. 79
In de maatstaf van heffing worden de volgende elementen niet opgenomen:
a)

prijsverminderingen wegens korting voor vooruitbetaling;

b)

prijskortingen en -rabatten die aan de afnemer worden toegekend en die zijn verkregen op het tijdstip waarop de handeling wordt verricht;

Voor de toepassing van de eerste alinea kan een dienstverband tussen werkgever en werknemer, het gezin van de werknemer of andere personen die nauwe banden met hem hebben, als nauwe betrekkingen gelden.
2. Wanneer zij gebruik maken van de in lid 1 bedoelde mogelijkheid, kunnen de lidstaten de categorieën van leveranciers, dienstverrichters of afnemers waarop de maatregelen van toepassing zijn, omschrijven.
3. De lidstaten stellen het BTW-Comité in kennis van de nationale maatregelen die zij uit hoofde van lid 1 hebben genomen indien het geen maatregelen betreft die voor 13 augustus 2006 door de Raad overeenkomstig artikel 27, leden 1 tot en met 4, van Richtlijn 77/388/EEG zijn toegestaan en uit hoofde van genoemd lid 1 worden verlengd.
###### Art. 81
De lidstaten die op 1 januari 1993 geen gebruik hebben gemaakt van de mogelijkheid uit hoofde van artikel 98 een verlaagd tarief toe te passen, kunnen, wanneer zij gebruikmaken van de in artikel 89 bedoelde mogelijkheid, bepalen dat de maatstaf van heffing voor de in artikel 103, lid 2, bedoelde leveringen van kunstvoorwerpen gelijk is aan een gedeelte van het overeenkomstig de artikelen 73, 74, 76, 78 en 79 vastgestelde bedrag.

L 347/22

Publicatieblad van de Europese Unie

NL

Het in de eerste alinea bedoelde gedeelte wordt op zodanige wijze vastgesteld dat de aldus verschuldigde BTW ten minste gelijk is aan 5 % van het overeenkomstig de artikelen 73, 74, 76, 78 en 79 vastgestelde bedrag.
###### Art. 82
De lidstaten kunnen bepalen dat in de maatstaf van heffing voor goederenleveringen en diensten de waarde moet worden opgenomen van vrijgesteld beleggingsgoud in de zin van artikel 346, dat door de afnemer ter beschikking is gesteld om voor verwerking te worden gebruikt en dat als gevolg van die verwerking zijn status van vrijgesteld beleggingsgoud verliest wanneer die goederenlevering of die dienst wordt verricht. De te hanteren waarde is de normale waarde van het beleggingsgoud op het tijdstip waarop die goederenlevering of die dienst wordt verricht.
#### HOOFDSTUK 3

Intracommunautaire verwerving van goederen
###### Art. 83
Voor de intracommunautaire verwerving van goederen bestaat de maatstaf van heffing uit dezelfde elementen als die welke in aanmerking worden genomen om overeenkomstig hoofdstuk 1 de maatstaf van heffing voor de levering van dezelfde goederen binnen het grondgebied van de lidstaat in kwestie te bepalen. Met name is voor de in de artikelen 21 en 22 bedoelde handelingen die met een intracommunautaire verwerving van goederen worden gelijkgesteld, de maatstaf van heffing de aankoopprijs van de goederen of van soortgelijke goederen of, bij gebreke van een aankoopprijs, de kostprijs, berekend op het tijdstip waarop deze handelingen worden verricht.

###### Art. 86

1. In de maatstaf van heffing moeten de volgende elementen worden opgenomen, voorzover zij niet reeds daarin zijn begrepen:
a)

de buiten de lidstaat van invoer verschuldigde rechten, heffingen en andere belastingen, alsmede die welke ter zake van de invoer verschuldigd zijn, met uitzondering van de te heffen BTW;

b)

de bijkomende kosten, zoals de kosten van commissie, verpakking, vervoer en verzekering, tot de eerste plaats van bestemming binnen het grondgebied van de lidstaat van invoer, alsmede de kosten die voortvloeien uit het vervoer naar een andere plaats van bestemming in de Gemeenschap, indien deze plaats bekend is op het tijdstip waarop het belastbare feit plaatsvindt.

2. Voor de toepassing van lid 1, eerste alinea, punt b), wordt onder „eerste plaats van bestemming” verstaan de plaats die genoemd is in de vrachtbrief of een ander document waaronder de goederen in de lidstaat van invoer binnenkomen. Bij gebreke van deze vermelding wordt de eerste plaats van bestemming geacht de plaats te zijn waar de eerste overlading van de goederen in de lidstaat van invoer geschiedt.
###### Art. 87
In de maatstaf van heffing worden de volgende elementen niet opgenomen:
a)

prijsverminderingen wegens korting voor vooruitbetaling;

b)

aan de afnemer toegekende prijskortingen en -rabatten die zijn verkregen op het tijdstip waarop de invoer wordt verricht.

###### Art. 84
###### Art. 88
1. De lidstaten nemen de nodige maatregelen om ervoor te zorgen dat de accijns die verschuldigd of voldaan is door degene die de intracommunautaire verwerving van een accijnsproduct verricht, overeenkomstig artikel 78, eerste alinea, punt a), in de maatstaf van heffing wordt opgenomen.
2. Wanneer de afnemer na het tijdstip waarop de intracommunautaire verwerving van goederen plaatsvindt, teruggaaf verkrijgt van de in de lidstaat van vertrek van de verzending of het vervoer van de goederen voldane accijns, wordt de maatstaf van heffing dienovereenkomstig verlaagd in de lidstaat binnen het grondgebied waarvan de verwerving heeft plaatsgevonden.
#### HOOFDSTUK 4

Invoer van goederen

Voor tijdelijk uit de Gemeenschap uitgevoerde goederen die, na buiten de Gemeenschap een herstelling, bewerking, verwerking of aanpassing te hebben ondergaan, wederom worden ingevoerd, treffen de lidstaten maatregelen teneinde te verzekeren dat de voor de verkregen goederen geldende behandeling met betrekking tot de BTW dezelfde is als die welke op de betrokken goederen zou zijn toegepast indien vorengenoemde handelingen op hun grondgebied zouden zijn verricht.
###### Art. 89
De lidstaten die op 1 januari 1993 geen gebruik hebben gemaakt van de mogelijkheid uit hoofde van artikel 98 een verlaagd tarief toe te passen, kunnen bepalen dat bij de invoer van kunstvoorwerpen, voorwerpen voor verzamelingen en antiquiteiten zoals omschreven in artikel 311, lid 1, punten 2), 3) en 4), de maatstaf van heffing gelijk is aan een gedeelte van het overeenkomstig de artikelen 85, 86 en 87 vastgestelde bedrag.

###### Art. 85
Voor de invoer van goederen is de maatstaf van heffing de waarde die in de geldende communautaire bepalingen als de douanewaarde wordt omschreven.

Het in de eerste alinea bedoelde gedeelte wordt op zodanige wijze vastgesteld, dat de aldus bij invoer verschuldigde BTW ten minste gelijk is aan 5 % van het overeenkomstig de artikelen 85, 86 en 87 vastgestelde bedrag.


Publicatieblad van de Europese Unie

NL
#### HOOFDSTUK 5

Diverse bepalingen
###### Art. 90
1. In geval van annulering, verbreking, ontbinding of gehele of gedeeltelijk niet-betaling, of in geval van prijsvermindering nadat de handeling is verricht, wordt de maatstaf van heffing dienovereenkomstig verlaagd onder de voorwaarden die door de lidstaten worden vastgesteld.

L 347/23

In de volgende gevallen is het toe te passen tarief echter het tarief dat van kracht is op het tijdstip waarop de belasting verschuldigd wordt:
a)

de gevallen, bedoeld in de artikelen 65 en 66;

b)

de intracommunautaire verwerving van goederen;

c)

de gevallen van invoer van goederen bedoeld in artikel 71, lid 1, tweede alinea, en lid 2.

2. In geval van gehele of gedeeltelijke niet-betaling kunnen de lidstaten van lid 1 afwijken.

###### Art. 94

###### Art. 91

1. Het op de intracommunautaire verwerving van goederen toe te passen tarief is het tarief dat binnen het grondgebied van de lidstaat op de levering van eenzelfde goed wordt toegepast.

1. Indien de elementen voor de bepaling van de maatstaf van heffing bij invoer zijn uitgedrukt in een andere munteenheid dan die van de lidstaat waar de maatstaf van heffing wordt bepaald, wordt de wisselkoers vastgesteld overeenkomstig de geldende communautaire bepalingen voor de berekening van de douanewaarde.
2. Indien de elementen voor de bepaling van de maatstaf van heffing voor een andere handeling dan een invoer van goederen zijn uitgedrukt in een andere munteenheid dan die van de lidstaat waar de maatstaf van heffing wordt bepaald, is de toepasselijke wisselkoers de laatste verkoopkoers die op het tijdstip waarop de belasting verschuldigd wordt, op de meest representatieve wisselmarkt of wisselmarkten van de betrokken lidstaat wordt geregistreerd, of een koers die wordt vastgesteld onder verwijzing naar die markt of markten, op een door die lidstaat vastgestelde wijze.
Voor sommige van de in de eerste alinea bedoelde handelingen of voor sommige categorieën belastingplichtigen kunnen de lidstaten evenwel kiezen voor de volgens de geldende communautaire bepalingen voor de berekening van de douanewaarde vastgestelde wisselkoers.

2. Onverminderd de in artikel 103, lid 1, bepaalde mogelijkheid een verlaagd tarief toe te passen op de invoer van kunstvoorwerpen, voorwerpen voor verzamelingen en antiquiteiten, is het bij invoer van goederen toe te passen tarief het tarief dat binnen het grondgebied van de lidstaat op de levering van eenzelfde goed wordt toegepast.
###### Art. 95
Bij tariefwijzigingen kunnen de lidstaten in de in de artikelen 65 en 66 bedoelde gevallen tot herziening overgaan, teneinde rekening te houden met het tarief geldend op het waarop de goederenleveringen of de diensten worden verricht.
De lidstaten kunnen bovendien elke passende overgangsmaatregel treffen.
#### HOOFDSTUK 2

Structuur en hoogte van de tarieven

##### Afdeling 1
###### Art. 92
Wat het statiegeld voor retouremballage betreft, kunnen de lidstaten het volgende bepalen:

Normaal tarief
###### Art. 96

a)

hetzij het statiegeld van de maatstaf van heffing uitsluiten door de nodige maatregelen te nemen opdat de maatstaf wordt herzien wanneer de emballage niet wordt teruggeven;

De lidstaten passen een normaal BTW-tarief toe, dat door elke lidstaat wordt vastgesteld op een percentage van de maatstaf van heffing, dat voor goederenleveringen en voor diensten gelijk is.

b)

hetzij het statiegeld in de maatstaf van heffing opnemen door de nodige maatregelen te nemen opdat de maatstaf wordt herzien wanneer de emballage wel wordt teruggeven.

###### Art. 97

### TITEL VIII
TARIEVEN
#### HOOFDSTUK 1

1. Vanaf 1 januari 2006 tot en met 31 december 2010 mag het normale tarief niet lager zĳn dan 15 %.
2. De Raad besluit overeenkomstig artikel 93 van het Verdrag over de hoogte van het na 31 december 2010 geldende normale tarief.

Toepassing van de tarieven
Ve r l a a g d e t a r i e v e n
##### Afdeling 2
###### Art. 93
###### Art. 98
Het op belastbare handelingen toe te passen tarief is het tarief dat van kracht is op het tijdstip waarop het belastbare feit zich voordoet.

1. De lidstaten kunnen een of twee verlaagde tarieven toepassen.

L 347/24

Publicatieblad van de Europese Unie

NL

2. De verlaagde tarieven zijn uitsluitend van toepassing op de goederenleveringen en de diensten die tot de in bĳlage III genoemde categorieën behoren.
De verlaagde tarieven zijn niet van toepassing op de in artikel 56, lid 1, punt k), bedoelde diensten.
3. Bij de toepassing van de in lid 1 bedoelde verlaagde tarieven op de categorieën waarin aan goederen wordt gerefereerd, mogen de lidstaten voor de vaststelling van de juiste omschrijving van de betrokken categorie gebruikmaken van de gecombineerde nomenclatuur.

###### Art. 103
1. De lidstaten kunnen bepalen dat het verlaagde tarief dat, of een van de verlaagde tarieven die, zij overeenkomstig de artikelen 98 en 99 toepassen, eveneens van toepassing is op de invoer van kunstvoorwerpen, voorwerpen voor verzamelingen en antiquiteiten, zoals omschreven in artikel 311, lid 1, punten 2), 3) en 4).
2. Wanneer zij van de in lid 1 bedoelde mogelijkheid gebruikmaken, kunnen de lidstaten het verlaagde tarief eveneens toepassen op de volgende handelingen:
a)

leveringen van kunstvoorwerpen die door de maker of diens rechthebbenden worden verricht;

b)

leveringen van kunstvoorwerpen die incidenteel worden verricht door een andere belastingplichtige dan een belastingplichtige wederverkoper wanneer de kunstvoorwerpen door deze belastingplichtige zelf zijn ingevoerd of hem zijn geleverd door de maker of diens rechthebbenden, of te zijnen gunste het recht op volledige aftrek van de BTW hebben doen ontstaan.

###### Art. 99
1. De verlaagde tarieven worden vastgesteld op een percentage van de maatstaf van heffing dat niet lager mag zĳn dan 5 %.
2. Een verlaagd tarief wordt zodanig vastgesteld, dat het bij toepassing van dit tarief verkregen BTW-bedrag het normaliter mogelijk maakt de overeenkomstig de artikelen 167 tot en met 171 en de artikelen 173 tot en met 177 aftrekbare belasting volledig af te trekken.
###### Art. 100
Aan de hand van een verslag van de Commissie onderwerpt de
Raad, voor de eerste maal in 1994 en vervolgens om de twee jaar, de werkingssfeer van de verlaagde tarieven aan een onderzoek.
De Raad kan overeenkomstig artikel 93 van het Verdrag besluiten wijzigingen aan te brengen in de in bijlage III opgenomen lijst van goederen en diensten.

###### Art. 104
Oostenrijk mag in de gemeenten Jungholz en Mittelberg (Kleines
Walsertal) een tweede normaal tarief toepassen dat lager ligt dan het overeenkomstige tarief dat in de rest van Oostenrijk wordt toegepast, maar dat niet minder dan 15 % mag bedragen.
###### Art. 105
Portugal mag op de handelingen in de autonome gebieden van de Azoren en Madeira en op de rechtstreekse invoer in deze gebieden lagere tarieven toepassen dan die welke op het vasteland gelden.

###### Art. 101
De Commissie legt uiterlijk op 30 juni 2007 aan het Europees
Parlement en aan de Raad een algemeen evaluatieverslag voor over het effect van de verlaagde tarieven op lokale diensten, inclusief restauratie, waarin met name aandacht wordt geschonken aan het scheppen van werkgelegenheid, de economische groei en de goede werking van de interne markt, en dat gebaseerd is op een studie van een onafhankelijke economischereflectiegroep.
Bijzondere bepalingen
##### Afdeling 3
###### Art. 102
De lidstaten kunnen voor de levering van aardgas, elektriciteit en stadsverwarming een verlaagd tarief toepassen, mits er geen gevaar voor verstoring van de mededinging bestaat.
Een lidstaat die voornemens is een verlaagd tarief uit hoofde van de eerste alinea toe te passen, stelt de Commissie daarvan vooraf in kennis. De Commissie besluit of er gevaar voor verstoring van de mededinging bestaat. Indien de Commissie binnen drie maanden na ontvangst van de kennisgeving geen besluit heeft genomen, wordt er geacht geen gevaar voor verstoring van de mededinging te bestaan.


#### HOOFDSTUK 3

Tijdelijke bepalingen voor bepaalde arbeidsintensieve diensten
###### Art. 106
De lidstaten kunnen door de Raad op voorstel van de Commissie met eenparigheid van stemmen worden gemachtigd om uiterlijk tot en met 31 december 2010 de in artikel 98 bedoelde verlaagde tarieven toe te passen op de in bĳlage IV genoemde diensten.
De verlaagde tarieven mogen worden toegepast op diensten behorende tot ten hoogste twee van de in bijlage IV genoemde categorieën.
In uitzonderlĳke gevallen mag het een lidstaat worden toegestaan het verlaagde tarief toe te passen op diensten behorende tot drie van de bovenbedoelde categorieën.
###### Art. 107
De in artikel 106 bedoelde diensten moeten de volgende voorwaarden vervullen:
a)

arbeidsintensief zĳn;

b)

grotendeels rechtstreeks voor eindverbruikers worden verricht;

c)

Publicatieblad van de Europese Unie

NL

hoofdzakelĳk lokaal zĳn en niet tot verstoring van de mededinging leiden.

Voorts moet er een nauw verband bestaan tussen de prĳsverlaging als gevolg van de tariefverlaging en de te verwachten toename van de vraag en de werkgelegenheid. De toepassing van een verlaagd tarief mag de goede werking van de interne markt niet in gevaar brengen.
###### Art. 108
Iedere lidstaat die voor het eerst na 31 december 2005 uit hoofde van dit artikel een verlaagd tarief wenst toe te passen op een of meer van de in artikel 106 bedoelde diensten, stelt de Commissie uiterlijk op 31 maart 2006 daarvan in kennis. De lidstaat deelt de Commissie vóór die datum alle toepasselijke inlichtingen betreffende de beoogde nieuwe maatregelen mede, met name:
a)

het toepassingsgebied van de maatregel en de nauwkeurige beschrĳving van de betrokken diensten;

b)

de gegevens waaruit blĳkt dat de in artikel 107 genoemde voorwaarden vervuld zijn;

c)

de gegevens waaruit de budgettaire kosten van de voorgenomen maatregel blĳken.
#### HOOFDSTUK 4

Bijzondere bepalingen van toepassing tot de invoering van de definitieve regeling
###### Art. 109
Dit hoofdstuk is van toepassing tot de invoering van de in artikel 402 bedoelde definitieve regeling.
###### Art. 110
De lidstaten die op 1 januari 1991 vrijstellingen met recht op aftrek van voorbelasting verleenden of verlaagde tarieven toepasten die onder het in artikel 96 vastgestelde minimum liggen, mogen deze blijven toepassen.

L 347/25
###### Art. 112

Indien artikel 106 in Ierland tot verstoring van de mededinging leidt bij de levering van energie voor verwarming en verlichting, kan de Commissie op uitdrukkelijk verzoek van Ierland aan die lidstaat toestaan voor die leveringen een verlaagd tarief toe te passen overeenkomstig de artikelen 95 en 96.
Ierland doet in het in de eerste alinea bedoelde geval zijn verzoek aan de Commissie vergezeld gaan van alle nodige informatie.
Indien de Commissie binnen drie maanden na ontvangst van het verzoek geen besluit heeft genomen, wordt Ierland geacht toestemming te hebben gekregen de voorgestelde verlaagde tarieven toe te passen.
###### Art. 113
De lidstaten die op 1 januari 1991 in overeenstemming met het
Gemeenschapsrecht met betrekking tot andere dan de in bijlage III genoemde goederen en diensten vrijstellingen met recht op aftrek van voorbelasting verleenden of verlaagde tarieven toepasten die onder het in artikel 99 vastgestelde minimum liggen, mogen voor de levering van die goederen of voor die diensten overeenkomstig artikel 98 een verlaagd tarief of een van de twee verlaagde tarieven toepassen.
###### Art. 114
1. De lidstaten die op 1 januari 1993 verplicht waren hun op
1 januari 1991 geldende normale tarief met meer dan 2 % te verhogen, mogen voor goederenleveringen en diensten van de in bijlage III genoemde categorieën, een verlaagd tarief toepassen dat onder het in artikel 99 bepaalde minimum ligt.
Voorts mogen de in de eerste alinea bedoelde lidstaten een dergelijk tarief hanteren voor restauratie, kinderkleding en -schoeisel en huisvesting.
2. De lidstaten mogen op grond van lid 1 geen vrijstellingen met recht op aftrek van voorbelasting invoeren.
###### Art. 115

De in de eerste alinea bedoelde vrijstellingen en verlaagde tarieven moeten in overeenstemming zijn met het Gemeenschapsrecht en moeten om duidelijk omschreven redenen van maatschappelijk belang en ten behoeve van de eindverbruikers vastgesteld zijn.

De lidstaten die op 1 januari 1991 een verlaagd tarief toepasten voor restauratie, kinderkleding en -schoeisel en huisvesting, mogen op die goederenleveringen en diensten een verlaagd tarief blijven toepassen.

###### Art. 111

###### Art. 116

Onder de in artikel 110, tweede alinea, gestelde voorwaarden mogen vrijstellingen met recht op aftrek van voorbelasting in de volgende gevallen toegepast blijven worden:

Portugal mag een van de twee in artikel 98 bedoelde verlaagde tarieven toepassen voor restauratie, op voorwaarde dat dit tarief niet lager ligt dan 12 %.

a)

b)

door Finland op abonnementen van dagbladen en tijdschriften en op het vervaardigen van drukwerk voor de leden van verenigingen voor algemeen welzijn; door Zweden voor de levering van nieuwsbladen, ook via radio en cassette voor visueel gehandicapten, van farmaceutische producten aan ziekenhuizen of op voorschrift, en voor de productie van periodieken van organisaties zonder winstoogmerk en andere daarmee samenhangende diensten.

###### Art. 117
1. Voor de toepassing van artikel 115 mag Oostenrijk een verlaagd tarief blijven toepassen voor restauratie.
2. Oostenrĳk mag een van de twee in artikel 98 bedoelde verlaagde tarieven toepassen op de verhuring van onroerend goed voor residentieel gebruik, op voorwaarde dat dit tarief niet lager ligt dan 10 %.

L 347/26

Publicatieblad van de Europese Unie

NL
###### Art. 118

De lidstaten die op 1 januari 1991 een verlaagd tarief toepasten voor andere leveringen van goederen en voor andere diensten dan de in bijlage III genoemde, mogen voor die leveringen of voor die diensten het verlaagde tarief of een van de twee verlaagde tarieven overeenkomstig artikel 98 toepassen, op voorwaarde dat dit tarief niet lager ligt dan 12 %.


warmwaterproductie, met uitzondering van grondstoffen voor het opwekken van warmte-energie;
b)

de levering van bouwwerkzaamheden voor huisvesting die niet in het kader van sociaal beleid worden verricht, met uitsluiting van bouwmaterialen.
###### Art. 124

De eerste alinea is niet van toepassing op leveringen van gebruikte goederen, kunstvoorwerpen, voorwerpen voor verzamelingen en antiquiteiten zoals omschreven in artikel 311, lid 1, punten 1) tot en met 4), die overeenkomstig de in de artikelen 312 tot en met 325 vastgestelde winstmargeregeling of de regeling voor verkoop op openbare veilingen aan de BTW zijn onderworpen.

Estland mag tot en met 30 juni 2007 een verlaagd tarief van ten minste 5 % blijven toepassen op de levering van warmte-energie aan natuurlijke personen, woningverenigingen, kerken, congregaties en door de staat, plattelandsgemeenten of steden gefinancierde instellingen of rechtspersonen, alsmede op de verkoop aan natuurlijke personen van turf, brandstofbriketten, kolen en brandhout.

###### Art. 119
Voor de toepassing van artikel 118 mag Oostenrijk een verlaagd tarief toepassen op door de producerende boer op de boerderij geproduceerde wijn, op voorwaarde dat dit tarief niet lager ligt dan 12 %.
###### Art. 120
Griekenland mag tarieven die tot 30 % lager liggen dan de overeenkomstige tarieven op het Griekse vasteland, toepassen in de departementen Lesbos, Chios, Samos, de Dodekanesos en de Cycladen, en op de eilanden Thassos, de noordelijke Sporaden, Samothraki en Skiros.
###### Art. 121
De lidstaten die op 1 januari 1993 de oplevering van een werk in roerende staat als een levering van goederen aanmerkten, kunnen op de oplevering van een werk in roerende staat het tarief toepassen dat van toepassing is op het na de uitvoering van het aangenomen werk verkregen goed.
Voor de toepassing van de eerste alinea wordt onder „oplevering van een werk in roerende staat” verstaan de afgifte door de opdrachtnemer aan de opdrachtgever van een roerend goed dat hij heeft vervaardigd of samengesteld met behulp van stoffen en voorwerpen die daartoe door de opdrachtgever aan de opdrachtnemer zijn verstrekt, ongeacht of de opdrachtnemer al dan niet een deel van de gebruikte materialen heeft verschaft.
###### Art. 122
De lidstaten mogen een verlaagd tarief toepassen op leveringen van levende planten en andere producten van de bloementeelt, met inbegrip van bollen, wortelen en dergelijke, snijbloemen en snijgroen, alsmede op leveringen van brandhout.

###### Art. 125
1. Cyprus mag tot en met 31 december 2007 een vrijstelling met recht op aftrek van voorbelasting blijven toepassen op geneesmiddelen en levensmiddelen voor menselijke consumptie, met uitzondering van roomijs, ijslollies, bevroren yoghurt, waterijs en soortgelijke producten, en voor hartige snacks (aardappelchips/-sticks, „puffs” (gepofte aardappelbrokjes) en soortgelijke producten die zonder verdere bereiding worden verpakt voor menselijke consumptie).
2. Cyprus mag een verlaagd tarief van ten minste 5 % blijven toepassen op restaurantdiensten, tot en met 31 december 2007 of tot de invoering van de in artikel 402 bedoelde definitieve regeling, naargelang welke datum eerder valt.
###### Art. 126
Hongarije mag een verlaagd tarief van ten minste 12 % blijven toepassen op de volgende handelingen:
a)

tot en met 31 december 2007 op de levering van kolen, steenkool en cokes, brandhout en houtskool, alsmede op de levering van stadsverwarmingsdiensten;

b)

tot en met 31 december 2007 of tot de invoering van de in artikel 402 bedoelde definitieve regeling, naargelang welke datum eerder valt, op restauratie en in horecabedrijven verkochte levensmiddelen.
###### Art. 127

Malta mag tot 1 januari 2010 een vrijstelling met aftrek van voorbelasting blijven toepassen op de levering van levensmiddelen voor menselijke consumptie en van geneesmiddelen.

#### HOOFDSTUK 5

Tijdelijke bepalingen
###### Art. 123
Tsjechië mag tot en met 31 december 2007 een verlaagd tarief van ten minste 5 % blijven toepassen op de volgende handelingen:
a)

de levering van warmte-energie aan huishoudens en nietbelastingplichtige kleine ondernemers voor verwarming en

###### Art. 128
1. Polen mag tot en met 31 december 2007 een vrijstelling met recht op aftrek van voorbelasting toepassen op de levering van bepaalde categorieën boeken en gespecialiseerde tijdschriften.
2. Polen mag tot en met 31 december 2007 of tot de invoering van de in artikel 402 bedoelde definitieve regeling, naar gelang welke datum eerder valt, een verlaagd tarief van ten minste 7 % blijven toepassen op restauratie.


Publicatieblad van de Europese Unie

NL

3. Polen mag tot en met 30 april 2008 een verlaagd tarief van ten minste 3 % blijven toepassen op de levering van levensmiddelen bedoeld in bijlage III, punt 1.
4. Polen mag tot en met 30 april 2008 een verlaagd tarief van ten minste 3 % blijven toepassen op de in bijlage III, punt 11, bedoelde goederenleveringen en diensten die normaal bestemd zijn voor gebruik in de landbouw, met uitzondering evenwel van kapitaalgoederen, zoals machines of gebouwen.
5. Polen mag tot en met 31 december 2007 een verlaagd tarief van ten minste 7 % toepassen op diensten die niet in het kader van sociaal beleid worden verricht voor de bouw, de verbouwing of de aanpassing van woningen, met uitzondering van bouwmaterialen, en op de levering van woongebouwen of delen van woongebouwen vóór de eerste ingebruikneming, zoals bedoeld in artikel 12, lid 1, punt a).

#### HOOFDSTUK 2

Vrijstellingen voor bepaalde activiteiten van algemeen belang
###### Art. 132
1. De lidstaten verlenen vrijstelling voor de volgende handelingen:
a)

de door openbare postdiensten verrichte diensten en daarmee gepaard gaande goederenleveringen, met uitzondering van personenvervoer en telecommunicatiediensten;

b)

ziekenhuisverpleging en medische verzorging, alsmede de handelingen die daarmede nauw samenhangen, door publiekrechtelijke lichamen of, onder sociale voorwaarden die vergelijkbaar zijn met die welke gelden voor genoemde lichamen, door ziekenhuizen, centra voor medische verzorging en diagnose en andere naar behoren erkende inrichtingen van dezelfde aard;

c)

medische verzorging in het kader van de uitoefening van medische en paramedische beroepen als omschreven door de betrokken lidstaat;

d)

de levering van menselijke organen, menselijk bloed en moedermelk;

e)

de door tandtechnici in het kader van de uitoefening van hun beroep verrichte diensten, alsmede de levering van tandprothesen door tandartsen en tandtechnici;

f)

diensten verricht door zelfstandige groeperingen van personen die een activiteit uitoefenen welke is vrijgesteld of waarvoor zij niet belastingplichtig zijn, teneinde aan hun leden de diensten te verlenen die direct nodig zijn voor de uitoefening van voornoemde activiteit, wanneer die groeperingen van hun leden enkel terugbetaling vorderen van hun aandeel in de gezamenlijke uitgaven, mits deze vrijstelling niet tot verstoring van de mededinging kan leiden;

g)

diensten en goederenleveringen welke nauw samenhangen met maatschappelijk werk en met de sociale zekerheid, waaronder begrepen die welke worden verricht door bejaardentehuizen, door publiekrechtelijke lichamen of door andere organisaties die door de betrokken lidstaat als instellingen van sociale aard worden erkend;

h)

diensten en goederenleveringen welke nauw samenhangen met de bescherming van kinderen en jongeren en welke worden verricht door publiekrechtelijke lichamen of door andere organisaties die door de betrokken lidstaat als instellingen van sociale aard worden erkend;

i)

onderwijs aan kinderen of jongeren, school- of universitair onderwijs, beroepsopleiding of -herscholing, met inbegrip van de diensten en goederenleveringen welke hiermede nauw samenhangen, door publiekrechtelijke lichamen die daartoe zijn ingesteld of door andere organisaties die door de betrokken lidstaat als lichamen met soortgelijke doeleinden worden erkend;

j)

lessen die particulier door docenten worden gegeven en betrekking hebben op het school- of universitair onderwijs;

###### Art. 129
1. Slovenië mag tot en met 31 december 2007 of tot de invoering van de in artikel 402 bedoelde definitieve regeling, naargelang welke datum eerder valt, een verlaagd tarief van ten minste 8,5 % blijven toepassen op restauratie.
2. Slovenië mag tot en met 31 december 2007 een verlaagd tarief van ten minste 5 % blijven toepassen op woningbouwwerkzaamheden en renovatie- en onderhoudswerkzaamheden aan woningen, voorzover die werkzaamheden niet in het kader van sociaal beleid worden verricht, met uitzondering van bouwmaterialen.
###### Art. 130
Slowakije mag een verlaagd tarief van ten minste 5 % blijven toepassen op de volgende handelingen:
a)

b)

tot en met 31 december 2007 op woningbouwwerkzaamheden die niet in het kader van sociaal beleid worden verricht, met uitzondering van bouwmaterialen; tot en met 31 december 2008 op de levering van warmteenergie aan huishoudens en niet-belastingplichtige kleine ondernemers voor verwarming en warmwaterproductie, met uitzondering van grondstoffen voor het opwekken van warmte-energie.
### TITEL IX

L 347/27

VRIJSTELLINGEN
#### HOOFDSTUK 1

Algemene bepalingen
###### Art. 131
De in de hoofdstukken 2 tot en met 9 geregelde vrijstellingen zijn van toepassing onverminderd andere communautaire bepalingen en onder de voorwaarden die de lidstaten stellen om een juiste en eenvoudige toepassing van deze vrijstellingen te verzekeren en elke vorm van fraude, ontwijking en misbruik te voorkomen.

L 347/28

Publicatieblad van de Europese Unie

NL

k)

beschikbaarstelling van personeel door religieuze of levensbeschouwelijke instellingen voor de in de punten b), g), h) en i), bedoelde werkzaamheden en met het oog op de verlening van geestelijke bijstand;

l)

diensten en nauw daarmee samenhangende goederenleveringen ten behoeve van hun leden in het collectief belang, tegen een statutair vastgestelde contributie door instellingen zonder winstoogmerk met doeleinden van politieke, syndicale, religieuze, vaderlandslievende, levensbeschouwelijke, filantropische of staatsburgerlijke aard, mits deze vrijstelling niet tot verstoring van de mededinging kan leiden;

m)

sommige diensten welke nauw samenhangen met de beoefening van sport of met lichamelijke opvoeding en welke door instellingen zonder winstoogmerk worden verricht voor personen die aan sport of lichamelijke opvoeding doen;


c)

de instellingen moeten prijzen toepassen die zijn goedgekeurd door de overheid, of prijzen die niet hoger liggen dan de goedgekeurde prijzen, of, voor handelingen waarvoor geen goedkeuring van prijzen plaatsvindt, prijzen die lager zijn dan die welke voor soortgelijke aan de BTW onderworpen handelingen in rekening worden gebracht door commerciële ondernemingen;

d)

de vrijstellingen mogen niet tot verstoring van de mededinging leiden ten nadele van belastingplichtige commerciële ondernemingen.

De lidstaten die krachtens bijlage E van Richtlijn 77/388/EEG van de Raad op 1 januari 1989 de in artikel 132, lid 1, punten m) en n), bedoelde handelingen aan BTW onderwierpen, mogen de in de eerste alinea, punt d), vermelde voorwaarden ook toepassen wanneer vrijstelling wordt verleend voor de genoemde diensten of goederenleveringen, verricht door publiekrechtelijke lichamen.
###### Art. 134

n)

bepaalde culturele diensten alsmede nauw daarmee samenhangende goederenleveringen, verricht door publiekrechtelijke culturele instellingen of door andere culturele instellingen die door de betrokken lidstaat worden erkend;

o)

diensten en goederenleveringen door lichamen waarvan de handelingen overeenkomstig de punten b), g), h), i), l), m) en n), zijn vrijgesteld, in samenhang met activiteiten die zijn bestemd ter verkrijging van financiële steun en die uitsluitend ten bate van henzelf zijn georganiseerd, mits deze vrijstelling niet tot verstoring van de mededinging kan leiden;

p)

q)

Goederenleveringen en diensten zijn in de volgende gevallen van de in artikel 132, lid 1, punten b), g), h), i), l), m) en n), bedoelde vrijstellingen uitgesloten:
a)

wanneer zij niet onontbeerlijk zijn voor het verrichten van de vrijgestelde handelingen;

b)

wanneer zij in hoofdzaak ertoe strekken aan de instelling extra opbrengsten te verschaffen door de uitvoering van handelingen welke worden verricht in rechtstreekse mededinging met aan de BTW onderworpen handelingen van commerciële ondernemingen.

vervoer van zieken of gewonden met speciaal daartoe ingerichte voertuigen door naar behoren gemachtigde lichamen; niet-commerciële activiteiten van openbare radio- en televisieorganisaties.

2. Voor de toepassing van lid 1, punt o), kunnen de lidstaten alle nodige beperkingen invoeren, met name ten aanzien van het aantal evenementen of het bedrag van de opbrengsten waarvoor recht op vrijstelling bestaat.

#### HOOFDSTUK 3

Vrijstellingen ten gunste van andere activiteiten
###### Art. 135
1. De lidstaten verlenen vrijstelling voor de volgende handelingen:
a)

handelingen ter zake van verzekering en herverzekering met inbegrip van daarmee samenhangende diensten, verricht door assurantiemakelaars en verzekeringstussenpersonen;

b)

de verlening van kredieten en de bemiddeling inzake kredieten, alsmede het beheer van kredieten door degene die deze heeft verleend;

c)

de bemiddeling bij en het aangaan van borgtochten en andere zekerheids- en garantieverbintenissen, alsmede het beheer van kredietgaranties door degene die het krediet heeft verleend;

d)

handelingen, bemiddeling daaronder begrepen, betreffende deposito's, rekening-courantverkeer, betalingen, overmakingen, schuldvorderingen, cheques en andere handelspapieren met uitzondering van de inning van schuldvorderingen;

e)

handelingen, bemiddeling daaronder begrepen, betreffende deviezen, bankbiljetten en munten die wettig betaalmiddel zijn, met uitzondering van munten en biljetten die

###### Art. 133
De lidstaten kunnen de verlening van elk der in artikel 132, lid 1, punten b), g), h), i), l), m) en n), bedoelde vrijstellingen aan andere dan publiekrechtelijke instellingen van geval tot geval afhankelijk stellen van een of meer van de volgende voorwaarden:
a)

b)

de instellingen mogen niet systematisch het maken van winst beogen; eventuele winsten mogen niet worden uitgekeerd, maar moeten worden aangewend voor de instandhouding of verbetering van de diensten die worden verricht; het beheer en het bestuur van de instellingen moeten in hoofdzaak op vrijwillige basis en zonder vergoeding geschieden door personen die noch zelf, noch via tussenpersonen, enig rechtstreeks of zijdelings belang hebben bij de resultaten van de werkzaamheden van de instellingen;


Publicatieblad van de Europese Unie

NL

verzamelobject zijn, namelijk gouden, zilveren of uit een ander metaal geslagen munten, alsmede biljetten, die normaal niet als wettig betaalmiddel worden gebruikt of die een numismatische waarde hebben;
f)

handelingen, bemiddeling daaronder begrepen, uitgezonderd bewaring en beheer, inzake aandelen, deelnemingen in vennootschappen of verenigingen, obligaties en andere waardepapieren, met uitzondering van documenten die goederen vertegenwoordigen en van de in artikel 16, lid 2, bedoelde rechten of effecten;

g)

het beheer van gemeenschappelijke beleggingsfondsen, zoals omschreven door de lidstaten;

h)

leveringen, tegen de nominale waarde, van postzegels die frankeerwaarde hebben binnen hun respectieve grondgebied, fiscale zegels en andere soortgelijke zegels;

i)

weddenschappen, loterijen en andere kans- en geldspelen, met inachtneming van de door elke lidstaat gestelde voorwaarden en beperkingen;

j)

de levering van een gebouw of een gedeelte ervan en van het bijbehorende terrein, met uitzondering van de in artikel 13, lid 1, punt a), bedoelde levering;

k)

de levering van onbebouwde onroerende goederen, met uitzondering van de in artikel 12, lid 1, punt b), bedoelde levering van een bouwterrein;

l)

L 347/29
###### Art. 137

1. De lidstaten kunnen aan de belastingplichtigen het recht verlenen voor belastingheffing ter zake van de volgende handelingen te kiezen:
a)

de financiële handelingen bedoeld in artikel 135, lid 1, punten b) tot en met g);

b)

de levering van een gebouw of een gedeelte ervan en van het bijbehorende terrein, met uitzondering van de in artikel 12, lid 1, punt a), bedoelde levering;

c)

de levering van onbebouwde onroerende goederen, met uitzondering van de in artikel 12, lid 1, punt b), bedoelde levering van een bouwterrein;

d)

de verhuur en verpachting van onroerende goederen.

2. De lidstaten stellen de bepalingen voor de uitoefening van het in lid 1 bedoelde keuzerecht vast.
De lidstaten kunnen de omvang van dit keuzerecht beperken.
#### HOOFDSTUK 4

Vrijstellingen met betrekking tot intracommunautaire handelingen

de verhuur en verpachting van onroerende goederen.


2. De volgende handelingen zijn van de in lid 1, punt l), geregelde vrijstelling uitgesloten:

Vr i j s t e l l i n g e n vo o r l e ve r i n g v a n g o e d e r e n
##### Afdeling 1
###### Art. 138

a)

het verstrekken van accommodatie, als omschreven in de wetgeving der lidstaten, in het hotelbedrijf of in sectoren met een soortgelijke functie, met inbegrip van de verhuuraccommodatie in vakantiekampen of op kampeerterreinen;

b)

verhuur van parkeerruimte voor voertuigen;

c)

verhuur van blijvend geïnstalleerde werktuigen en machines;

d)

verhuur van safeloketten.

De lidstaten kunnen nog andere handelingen van de toepassing van de in lid 1, punt l), geregelde vrijstelling uitsluiten.

1. De lidstaten verlenen vrijstelling voor de levering van goederen, door of voor rekening van de verkoper of de afnemer verzonden of vervoerd naar een plaats buiten hun respectieve grondgebied, maar binnen de Gemeenschap, welke wordt verricht voor een andere belastingplichtige of voor een nietbelastingplichtige rechtspersoon die als zodanig handelt in een andere lidstaat dan de lidstaat van vertrek van de verzending of het vervoer van de goederen.
2. Behalve voor de in lid 1 bedoelde goederenleveringen verlenen de lidstaten vrijstelling voor de volgende handelingen:
a)

de levering van nieuwe vervoermiddelen, door of voor rekening van de verkoper of de afnemer met als bestemming de afnemer verzonden of vervoerd naar een plaats buiten hun respectieve grondgebied maar binnen de Gemeenschap, welke wordt verricht voor belastingplichtigen of voor niet-belastingplichtige rechtspersonen wier intracommunautaire verwervingen van goederen uit hoofde van artikel 3, lid 1, niet aan de BTW zijn onderworpen, of voor elke andere niet-belastingplichtige;

b)

de levering van accijnsproducten, door of voor rekening van de verkoper of de afnemer met als bestemming de afnemer verzonden of vervoerd naar een plaats buiten hun respectieve grondgebied maar binnen de Gemeenschap, welke wordt verricht voor belastingplichtigen of voor niet-Artikel 136 De lidstaten verlenen vrijstelling voor de volgende handelingen:
a)

b)

leveringen van goederen die uitsluitend zijn gebruikt voor een activiteit die krachtens de artikelen 132, 135, 371, 375, 376 en 377, artikel 378, lid 2, artikel 379, lid 2, en de artikelen 380 tot en met 390 is vrijgesteld, wanneer voor deze goederen geen recht op aftrek is genoten; leveringen van goederen bij de aanschaffing of bestemming waarvan overeenkomstig artikel 176 het recht op aftrek van de BTW is uitgesloten.

L 347/30

Publicatieblad van de Europese Unie

NL

belastingplichtige rechtspersonen wier intracommunautaire verwervingen van andere goederen dan accijnsproducten, uit hoofde van artikel 3, lid 1, niet aan de BTW zijn onderworpen wanneer de verzending of het vervoer van deze producten plaatsvindt overeenkomstig artikel 7, leden 4 en 5, of artikel 16 van Richtlijn 92/12/EEG;

c)


b)

de intracommunautaire verwerving van goederen waarvan de invoer in ieder geval op grond van artikel 143, punten a),
b) en c), en e) tot en met l), is vrijgesteld;

c)

de intracommunautaire verwerving van goederen waarvoor de afnemer van de goederen op grond van de artikelen 170 en 171 in ieder geval recht heeft op volledige teruggaaf van de BTW die krachtens artikel 2, lid 1, onder b), verschuldigd zou zijn.

de goederenlevering bestaande in de overbrenging naar een andere lidstaat, die voor de in lid 1 en de punten a) en b) bedoelde vrijstellingen in aanmerking zou komen indien zij voor een andere belastingplichtige was verricht.

###### Art. 141
###### Art. 139
1. De in artikel 138, lid 1, bedoelde vrijstelling is niet van toepassing op de goederenlevering welke wordt verricht door belastingplichtigen die voor de in de artikelen 282 tot en met 292 geregelde vrijstelling voor kleine ondernemingen in aanmerking komen.

De vrijstelling is evenmin van toepassing op de goederenlevering welke wordt verricht voor belastingplichtigen of voor nietbelastingplichtige rechtspersonen wier intracommunautaire verwervingen uit hoofde van artikel 3, lid 1, niet aan de BTW zijn onderworpen.

2. De in artikel 138, lid 2, onder b), geregelde vrijstelling is niet van toepassing op de levering van accijnsproducten welke wordt verricht door belastingplichtigen die voor de in de artikelen 282 tot en met 292 geregelde vrijstelling voor kleine ondernemingen in aanmerking komen.

3. De in artikel 138, lid 1, en lid 2, onder b) en c), geregelde vrijstelling is niet van toepassing op de goederenlevering welke overeenkomstig de in de artikelen 312 tot en met 325 neergelegde winstmargeregeling of de regeling inzake de verkoop op openbare veilingen aan de BTW is onderworpen.

De in artikel 138, lid 1, en lid 2, onder c), geregelde vrijstelling is niet van toepassing op de levering van gebruikte vervoermiddelen als omschreven in artikel 327, lid 3, die overeenkomstig de overgangsregeling voor gebruikte vervoermiddelen aan de BTW zijn onderworpen.

Elke lidstaat treft bijzondere maatregelen om de intracommunautaire verwerving van goederen die overeenkomstig artikel 40 binnen zijn grondgebied wordt verricht, niet aan de BTW te onderwerpen indien de volgende voorwaarden vervuld zijn:

a)

de verwerving van goederen wordt verricht door een niet in die lidstaat gevestigde, maar in een andere lidstaat voor BTW-doeleinden geïdentificeerde belastingplichtige;

b)

de verwerving van goederen wordt verricht met het oog op een daaropvolgende levering van deze goederen in diezelfde lidstaat door de in punt a) bedoelde belastingplichtige;

c)

de aldus door de in punt a) bedoelde belastingplichtige verworven goederen worden rechtstreeks vanuit een andere lidstaat dan die waarin hij voor BTW-doeleinden geïdentificeerd is, verzonden of vervoerd naar degene voor wie hij de daaropvolgende levering verricht;

d)

degene voor wie de daaropvolgende levering bestemd is, is een andere belastingplichtige of een niet-belastingplichtige rechtspersoon, die in diezelfde lidstaat voor BTW-doeleinden is geïdentificeerd;

e)

de in punt d) bedoelde persoon voor wie de volgende levering is bestemd, is overeenkomstig artikel 197 aangewezen als degene die is gehouden tot voldoening van de belasting, verschuldigd uit hoofde van de levering welke is verricht door de belastingplichtige die niet gevestigd is in de lidstaat waar de belasting is verschuldigd.

Vr i j s t e l l i n g e n vo o r i n t r a c o m m u n a u t a i r e ver wer vingen van goederen
##### Afdeling 2
###### Art. 140
De lidstaten verlenen vrijstelling voor de volgende handelingen:

a)

de intracommunautaire verwerving van goederen waarvan de levering door belastingplichtigen in ieder geval op hun respectieve grondgebied is vrijgesteld;

Vr i j s t e l l i n g e n vo o r b e p a a l d e ver voerdiensten
##### Afdeling 3
###### Art. 142
De lidstaten verlenen vrijstelling voor het intracommunautaire vervoer van goederen naar of vanaf de eilanden die de autonome gebieden van de Azoren en van Madeira vormen, alsmede voor het vervoer van goederen tussen deze eilanden.


Publicatieblad van de Europese Unie

NL
#### HOOFDSTUK 5

h)

de invoer van goederen verricht in de lidstaten die partij zijn bij het Noord-Atlantische Verdrag, door de strijdkrachten van de andere staten die partij bij dat verdrag zijn, ten behoeve van deze strijdkrachten of het hen begeleidende burgerpersoneel of voor de bevoorrading van hun messes of kantines, voor zover deze strijdkrachten deelnemen aan de gemeenschappelijke defensie-inspanning;

i)

de invoer van goederen door de strijdkrachten van het
Verenigd Koninkrijk die op Cyprus zijn gestationeerd overeenkomstig het Verdrag betreffende de oprichting van de Republiek Cyprus van 16 augustus 1960, ten behoeve van de strijdkrachten of het hen begeleidende burgerpersoneel of voor de bevoorrading van hun messes of kantines;

j)

de invoer in havens, door zeevisserijbedrijven, van visserijproducten, niet be- of verwerkt of nadat deze met het oog op de afzet een bederfwerende behandeling hebben ondergaan, en die nog niet zijn geleverd;

k)

de invoer van goud door de centrale banken;

l)

de invoer van gas via het aardgasdistributiesysteem, of de invoer van elektriciteit.

Vrijstellingen bij invoer
###### Art. 143
De lidstaten verlenen vrijstelling voor de volgende handelingen:
a)

de definitieve invoer van goederen waarvan de levering door belastingplichtigen in ieder geval op hun respectieve grondgebied is vrijgesteld;

b)

de definitieve invoer van goederen die valt onder de
Richtlijnen 69/169/EEG (1), 83/181/EEG (2) en 2006/79/
EG (3) van de Raad;

c)

de definitieve invoer van goederen in het vrije verkeer afkomstig uit een derdelandsgebied dat deel uitmaakt van het douanegebied van de Gemeenschap, die voor de in punt b) bedoelde vrijstelling in aanmerking zouden komen indien zij waren ingevoerd in de zin van artikel 31, eerste alinea;

d)

de invoer van vanuit een derdelandsgebied of een derde land verzonden of vervoerde goederen in een andere lidstaat dan de lidstaat van aankomst van de verzending of het vervoer, indien de levering van deze goederen, verricht door de importeur die uit hoofde van artikel 201 is aangewezen of erkend als de tot voldoening van de belasting gehouden persoon, overeenkomstig artikel 138 is vrijgesteld;

e)

de wederinvoer van goederen in de toestand waarin zij zijn uitgevoerd, door degene die deze heeft uitgevoerd, indien de goederen voor vrijstelling van invoerrechten in aanmerking komen;

f)

de invoer van goederen in het kader van de diplomatieke en consulaire betrekkingen, indien de goederen voor vrijstelling van invoerrechten in aanmerking komen;

g)

de invoer van goederen verricht door internationale instellingen die als zodanig door de overheid van de lidstaat waar zij zijn gevestigd, zijn erkend, alsmede door de leden van deze instellingen, zulks binnen de beperkingen en onder de voorwaarden die zijn vastgesteld bij de internationale verdragen tot oprichting van deze instellingen of bij de vestigingsovereenkomsten;

(1) Richtlijn 69/169/EEG van de Raad van 28 mei 1969 inzake de harmonisatie van de wettelijke en bestuursrechtelijke bepalingen met betrekking tot de vrijstellingen van omzetbelastingen en accijnzen die bij invoer worden geheven in het internationale reizigersverkeer (PB L 133 van 4.6.1969, blz. 6). Richtlijn laatstelijk gewijzigd bij Richtlijn 2005/93/EG (PB L 346 van 29.12.2005, blz. 16).
(2) Richtlijn 83/181/EEG van de Raad van 28 maart 1983 houdende bepaling van de werkingssfeer van artikel 14, lid 1, sub d), van Richtlijn 77/388/EEG met betrekking tot de vrijstelling van de belasting over de toegevoegde waarde voor de definitieve invoer van bepaalde goederen (PB L 105 van 23.4.1983, blz. 38). Richtlijn laatstelijk gewijzigd bij de Toetredingsakte van 1994.
(3) Richtlijn 2006/79/EG van de Raad van 5 oktober 2006 inzake de belastingvrijstellingen die van toepassing zijn bij invoer van uit derde landen afkomstige kleine zendingen goederen zonder commercieel karakter (PB L 286 van 17.10.2006, blz. 15).

L 347/31

###### Art. 144
De lidstaten verlenen vrijstelling voor de diensten die betrekking hebben op de invoer van goederen en waarvan de waarde overeenkomstig artikel 86, lid 1, onder b), in de maatstaf van heffing is opgenomen.
###### Art. 145
1. De Commissie dient, indien nodig, zo spoedig mogelijk voorstellen in bij de Raad om de werkingssfeer en de uitvoering van de in de artikelen 143 en 144 geregelde vrijstellingen nader te bepalen.
2. Totdat de in lid 1 bedoelde uitvoeringsbepalingen in werking treden, kunnen de lidstaten hun geldende nationale voorschriften blijven toepassen.
De lidstaten kunnen hun nationale voorschriften aanpassen, teneinde verstoring van de mededinging te beperken en met name gevallen van niet-heffing of dubbele heffing van belasting in de Gemeenschap te vermijden.
De lidstaten kunnen de administratieve procedures gebruiken die zij het meest geschikt achten om tot vrijstelling te komen.
3. De lidstaten stellen, voorzover dat nog niet is gebeurd, de
Commissie in kennis van de geldende nationale voorschriften en van de voorschriften die zij krachtens lid 2 nemen. De Commissie stelt de andere lidstaten daarvan in kennis.

L 347/32

Publicatieblad van de Europese Unie

NL
#### HOOFDSTUK 6

Vrijstellingen bij uitvoer
###### Art. 146
1. De lidstaten verlenen vrijstelling voor de volgende handelingen:
a)

de levering van goederen die door of voor rekening van de verkoper worden verzonden of vervoerd naar een plaats buiten de Gemeenschap;

b)

de levering van goederen die door of voor rekening van een niet op hun respectieve grondgebied gevestigde afnemer worden verzonden of vervoerd naar een plaats buiten de Gemeenschap, met uitzondering van door de afnemer zelf vervoerde goederen bestemd voor de uitrusting of de bevoorrading van pleziervaartuigen en sportvliegtuigen of van andere vervoermiddelen voor privé-gebruik;

c)

d)

e)

de levering van goederen aan erkende organisaties die deze goederen uit de Gemeenschap uitvoeren in het kader van hun menslievende, liefdadige of opvoedkundige werk buiten de Gemeenschap; diensten bestaande uit werkzaamheden met betrekking tot roerende zaken die zijn verworven of ingevoerd teneinde deze werkzaamheden in de Gemeenschap te ondergaan, en die door of voor rekening van de dienstverrichter of de niet binnen hun respectieve grondgebied gevestigde afnemer worden vervoerd of verzonden naar een plaats buiten de Gemeenschap; diensten, met inbegrip van vervoer en met die diensten samenhangende handelingen en met uitzondering van de overeenkomstig de artikelen 132 en 135 vrijgestelde diensten, wanneer die diensten rechtstreeks verband houden met de uitvoer of invoer van goederen die onder artikel 61 en artikel 157, lid 1, onder a), vallen.

De lidstaten mogen evenwel een levering waarvan het totale bedrag lager is dan het in de eerste alinea, punt c), genoemde bedrag, van belasting vrijstellen.
2. Voor de toepassing van lid 1 wordt onder „reiziger die niet in de Gemeenschap is gevestigd” verstaan een reiziger wiens woonplaats of gebruikelijke verblijfplaats niet in de Gemeenschap is gelegen. In dat geval wordt onder „woonplaats of gebruikelijke verblijfplaats” verstaan de plaats die als zodanig is vermeld op het paspoort, de identiteitskaart of enig ander document dat door de lidstaat op het grondgebied waarvan de levering wordt verricht, als identiteitsbewijs wordt erkend.
Het bewijs van de uitvoer wordt geleverd door middel van de factuur, of van een in de plaats daarvan komend bewijsstuk, voorzien van het visum van het douanekantoor van uitgang uit de Gemeenschap.
Elke lidstaat verstrekt aan de Commissie een specimen van de stempels die hij voor het afgeven van het in de tweede alinea bedoelde visum gebruikt. De Commissie stelt de belastingautoriteiten van de andere lidstaten van deze informatie in kennis.
#### HOOFDSTUK 7

Vrijstellingen met betrekking tot internationaal vervoer
###### Art. 148
De lidstaten verlenen vrijstelling voor de volgende handelingen:
a)

de levering van goederen, bestemd voor de bevoorrading van schepen voor de vaart op volle zee waarmee passagiersvervoer tegen betaling plaatsvindt of die worden gebruikt voor de uitoefening van een industriële, handelsof visserijactiviteit alsmede van reddingsboten en schepen voor hulpverlening op zee of schepen voor de kustvisserij, behalve, wat de laatstgenoemde schepen betreft, de scheepsvoorraden;

b)

de levering van goederen, bestemd voor de bevoorrading van oorlogsschepen vallende onder GN-code 8906 10 00, die hun grondgebied verlaten met als bestemming een haven of een ankerplaats buiten de lidstaat;

c)

de levering, de verbouwing, de reparatie, het onderhoud, de bevrachting en de verhuur van de in punt a) bedoelde schepen, alsmede de levering, de verhuur, de reparatie en het onderhoud van de voorwerpen — met inbegrip van uitrusting voor de visserij — die met deze schepen vast verbonden zijn of die voor hun exploitatie dienen;

d)

andere dan de in punt c) bedoelde diensten die voor de rechtstreekse behoeften van de in punt a) bedoelde schepen en hun lading worden verricht;

e)

de levering van goederen, bestemd voor de bevoorrading van de luchtvaartuigen welke worden gebruikt door luchtvaartmaatschappijen die zich hoofdzakelijk op het betaalde internationale vervoer toeleggen;

f)

de levering, de verbouwing, de reparatie, het onderhoud, de bevrachting en de verhuur van de in punt e) bedoelde luchtvaartuigen, alsmede de levering, de verhuur, de reparatie en het onderhoud van de voorwerpen die met

2. De in lid 1, punt c), geregelde vrijstelling kan worden toegekend in de vorm van teruggaaf van de BTW.
###### Art. 147
1. Indien de in artikel 146, lid 1, punt b), bedoelde levering betrekking heeft op goederen die deel uitmaken van de persoonlijke bagage van reizigers, geldt de vrijstelling slechts wanneer de volgende voorwaarden vervuld zijn:
a)

de reiziger is niet in de Gemeenschap gevestigd;

b)

de goederen worden naar een plaats buiten de Gemeenschap vervoerd vóór het einde van de derde maand volgende op die waarin de levering geschiedde;

c)

het totale bedrag van de levering, BTW inbegrepen, is hoger dan EUR 175 of de tegenwaarde daarvan in nationale munteenheid die eenmaal per jaar op basis van de op de eerste werkdag van de maand oktober geldende wisselkoers wordt vastgesteld en met ingang van 1 januari van het daaropvolgende jaar van toepassing is.



Publicatieblad van de Europese Unie

NL

deze luchtvaartuigen vast verbonden zijn of die voor hun exploitatie dienen;
g)

andere dan de in punt f) bedoelde diensten, die voor de rechtstreekse behoeften van de in punt e) bedoelde luchtvaartuigen en hun lading worden verricht.

L 347/33

ten behoeve van de strijdkrachten of het hen begeleidende burgerpersoneel of voor de bevoorrading van hun messes of kantines.

###### Art. 149

De in de eerste alinea geregelde vrijstellingen zijn van toepassing met inachtneming van de door de lidstaat van ontvangst vastgestelde beperkingen, totdat een uniforme belastingregeling is vastgesteld.

Portugal mag het vervoer over zee en door de lucht tussen de eilanden die de autonome gebieden van de Azoren en Madeira vormen onderling en tussen deze eilanden en het vasteland gelijkstellen met internationaal vervoer.

2. Voor goederen die niet worden verzonden of vervoerd naar een plaats buiten de lidstaat waar de levering van deze goederen wordt verricht, evenals voor diensten, kan de vrijstelling worden verleend in de vorm van teruggaaf van de BTW.

###### Art. 150

###### Art. 152

1. De Commissie dient, indien nodig, zo spoedig mogelijk voorstellen in bij de Raad om de werkingssfeer en de uitvoering van de in artikel 148 geregelde vrijstellingen nader te bepalen.

De lidstaten verlenen vrijstelling voor de levering van goud aan de centrale banken.

2. Totdat de in lid 1 bedoelde bepalingen in werking treden, kunnen de lidstaten de draagwijdte van de in artikel 148, punten a) en b), geregelde vrijstellingen beperken.

#### HOOFDSTUK 9

Vrijstellingen voor door tussenpersonen verrichte diensten
###### Art. 153

#### HOOFDSTUK 8

Vrijstellingen voor bepaalde met uitvoer gelijkgestelde handelingen
###### Art. 151
1. De lidstaten verlenen vrijstelling voor de volgende handelingen:
a)

b)

c)

d)

e)

goederenleveringen en diensten verricht in het kader van de diplomatieke en consulaire betrekkingen; goederenleveringen en diensten bestemd voor internationale instellingen die als dusdanig door de overheid van de lidstaat waar zij zijn gevestigd, zijn erkend, alsmede voor de leden van deze instellingen, zulks binnen de beperkingen en onder de voorwaarden die zijn vastgesteld bij de internationale verdragen tot oprichting van deze instellingen of bij de vestigingsovereenkomsten; goederenleveringen en diensten verricht in de lidstaten die partij zijn bij het Noord-Atlantische Verdrag, en bestemd voor de strijdkrachten van de andere staten die partij bij dat verdrag zijn, ten behoeve van deze strijdkrachten of het hen begeleidende burgerpersoneel of voor de bevoorrading van hun messes of kantines, voor zover deze strijdkrachten deelnemen aan de gemeenschappelijke defensie-inspanning; goederenleveringen en diensten verricht voor een andere lidstaat, bestemd voor de strijdkrachten van andere staten die partij zijn bij het Noord-Atlantische Verdrag dan de lidstaat van bestemming zelf, ten behoeve van deze strijdkrachten of het hen begeleidende burgerpersoneel of voor de bevoorrading van hun messes of kantines, voor zover deze strijdkrachten deelnemen aan de gemeenschappelijke defensie-inspanning; goederenleveringen en diensten verricht voor de strijdkrachten van het Verenigd Koninkrijk die op Cyprus zijn gestationeerd overeenkomstig het Verdrag betreffende de oprichting van de Republiek Cyprus van 16 augustus 1960,

De lidstaten verlenen vrijstelling voor de diensten van tussenpersonen die handelen in naam en voor rekening van derden, wanneer hun diensten betrekking hebben op de in de hoofdstukken 6, 7 en 8 bedoelde handelingen of op buiten de Gemeenschap verrichte handelingen.
De in de eerste alinea bedoelde vrijstelling is niet van toepassing op reisbureaus wanneer zij in naam en voor rekening van de reiziger diensten verrichten die in andere lidstaten plaatsvinden.
#### HOOFDSTUK 10

Vrijstellingen voor handelingen met betrekking tot het internationale goederenverkeer
Douane- en andere entrepots en soortgelijke regelingen
##### Afdeling 1
###### Art. 154
Voor de toepassing van deze afdeling worden onder andere entrepots dan douane-entrepots verstaan, wat accijnsproducten betreft, de als belastingentrepots in de zin van artikel 4, onder b), van Richtlijn 92/12/EEG aangemerkte plaatsen, en wat andere goederen dan accijnsproducten betreft, de als zodanig door de lidstaten aangemerkte plaatsen.
###### Art. 155
Onverminderd de andere communautaire belastingbepalingen kunnen de lidstaten, na raadpleging van het BTW-Comité, bijzondere maatregelen nemen teneinde vrijstelling te verlenen voor de in deze afdeling bedoelde handelingen of sommige daarvan, mits zij geen betrekking hebben op eindgebruik of eindverbruik en het BTW-bedrag dat verschuldigd is wanneer de goederen aan de in deze afdeling bedoelde regelingen of situaties worden onttrokken, overeenkomt met het BTW-bedrag dat verschuldigd zou zijn geweest indien elk van deze handelingen op hun grondgebied was belast.

L 347/34

Publicatieblad van de Europese Unie

NL

vliegtuig of schip tijdens een vlucht of zeereis waarvan de plaats van aankomst buiten de Gemeenschap is gelegen;

###### Art. 156
1. De lidstaten kunnen vrijstelling verlenen voor de volgende handelingen:
a)

de levering van goederen die bestemd zijn om bij de douane te worden aangebracht en, in voorkomend geval, in tijdelijke opslag te worden geplaatst;

b)

de levering van goederen die bestemd zijn om in een vrije zone of een vrij entrepot te worden geplaatst;

c)

de levering van goederen die bestemd zijn om onder een stelsel van douane-entrepots of onder een stelsel van actieve veredeling te worden geplaatst;

d)

e)

de levering van goederen die bestemd zijn om in de territoriale zee te worden toegelaten om integrerend deel uit te maken van boor- of werkeilanden, met het oog op de bouw, de reparatie, het onderhoud, de verbouwing of de uitrusting van die boor- of werkeilanden, of om die boor- of werkeilanden met het vasteland te verbinden; de levering van goederen die bestemd zijn om in de territoriale zee te worden toegelaten voor de bevoorrading van boor- of werkeilanden.

2. De in lid 1 bedoelde plaatsen zijn de plaatsen die als zodanig in de geldende communautaire douanevoorschriften zijn omschreven.
###### Art. 157
1. De lidstaten kunnen vrijstelling verlenen voor de volgende handelingen:
a)

de invoer van goederen die onder een ander stelsel van entrepots dan dat van douane-entrepots worden geplaatst;

b)

de levering van goederen die op hun grondgebied onder een ander stelsel van entrepots dan dat van douaneentrepots worden geplaatst.

2. De lidstaten mogen voor andere goederen dan accijnsproducten niet in een ander stelsel van entrepots dan dat van douane-entrepots voorzien, indien deze goederen bestemd zijn om in het kleinhandelsstadium te worden geleverd.


c)

indien de goederen bestemd zijn voor belastingplichtigen, met het oog op leveringen die worden verricht met vrijstelling van BTW overeenkomstig artikel 151.

2. Indien de lidstaten gebruik maken van de in lid 1, punt a), bedoelde mogelijkheid tot vrijstelling, treffen zij de nodige maatregelen om een juiste en eenvoudige toepassing van deze vrijstelling te verzekeren en elke vorm van fraude, ontwijking en misbruik te voorkomen.
3. Voor de toepassing van lid 1, punt a), wordt onder
„verkooppunt voor belastingvrije verkoop” verstaan elke in een luchthaven of haven gelegen inrichting die aan de door de bevoegde overheidsinstanties gestelde voorwaarden voldoet.
###### Art. 159
De lidstaten kunnen vrijstelling verlenen voor de diensten die samenhangen met de in artikel 156, artikel 1527 lid 1, onder b), en artikel 158 bedoelde goederenleveringen.
###### Art. 160
1. De lidstaten kunnen vrijstelling verlenen voor de volgende handelingen:
a)

goederenleveringen en diensten verricht op de in artikel 156, lid 1, genoemde plaatsen met handhaving op hun grondgebied van een van de in dat lid genoemde situaties;

b)

goederenleveringen en diensten verricht op de in artikel 157, lid 1, onder b), en artikel 158 genoemde plaatsen met handhaving op hun grondgebied van een van de in artikel 157, lid 1, onder b), of in artikel 158, lid 1, genoemde situaties.

2. De lidstaten die voor handelingen die in een douaneentrepot worden verricht, gebruikmaken van de in lid 1, punt a), bepaalde mogelijkheid, nemen de nodige maatregelen om te voorzien in andere stelsels van entrepots dan dat van douaneentrepots die de toepassing van lid 1, punt b), mogelijk maken op dezelfde handelingen met betrekking tot in bijlage V opgenomen goederen, welke in die andere entrepots dan douane-entrepots worden verricht.

###### Art. 158
1. In afwijking van artikel 157, lid 2, kunnen de lidstaten in de volgende gevallen een ander stelsel van entrepots dan dat van douane-entrepots invoeren:
a)

b)

indien de goederen bestemd zijn voor verkooppunten voor belastingvrije verkoop, met het oog op de levering van goederen welke worden meegenomen in de persoonlijke bagage van reizigers die zich door middel van een vlucht of zeereis naar een derdelandsgebied of een derde land begeven, wanneer die levering overeenkomstig artikel 146, lid 1, punt b), is vrijgesteld; indien de goederen bestemd zijn voor belastingplichtigen, met het oog op levering aan reizigers aan boord van een

###### Art. 161
De lidstaten kunnen vrijstelling verlenen voor de volgende goederenleveringen en de daarop betrekking hebbende diensten:
a)

de levering van goederen bedoeld in artikel 30, eerste alinea, die nog onderworpen zijn aan een regeling voor tijdelijke invoer met volledige vrijstelling van invoerrechten of aan een regeling voor extern douanevervoer;

b)

de levering van goederen bedoeld in artikel 30, tweede alinea, die nog onderworpen zijn aan de in artikel 276 bedoelde regeling voor intern communautair douanevervoer.


Publicatieblad van de Europese Unie

NL

L 347/35

###### Art. 162

### TITEL X

De lidstaten die van de in deze afdeling bedoelde mogelijkheid gebruikmaken, nemen de nodige maatregelen om te waarborgen dat de intracommunautaire verwerving van goederen die bestemd zijn om onder of in een van de in artikel 156, artikel 157, lid 1, onder b), en artikel 158 bedoelde regelingen of situaties te worden geplaatst, onder dezelfde bepalingen vallen als de goederenlevering die op hun grondgebied onder dezelfde voorwaarden wordt verricht.

AFTREK

###### Art. 163
Indien de goederen worden onttrokken aan de in deze afdeling bedoelde regelingen of situaties, waardoor aanleiding wordt gegeven tot invoer in de zin van artikel 61, neemt de lidstaat van invoer de nodige maatregelen om dubbele belastingheffing te voorkomen.
Handelingen die worden vrijgesteld met het oog op de uitvoer en in het kader van het handelsverkeer tussen de lidst aten
##### Afdeling 2
###### Art. 164
1. Na raadpleging van het BTW-Comité kunnen de lidstaten voor de volgende door een belastingplichtige verrichte of voor een belastingplichtige bestemde handelingen, vrijstelling verlenen binnen de grenzen van het bedrag waarvoor deze belastingplichtige in de afgelopen twaalf maanden heeft uitgevoerd:
a)

b)

de intracommunautaire verwerving van goederen door de belastingplichtige alsmede de invoer en de levering van goederen bestemd voor de belastingplichtige die deze goederen betrekt met het oog op hun uitvoer uit de Gemeenschap, al dan niet na verwerking; de diensten in verband met de uitvoeractiviteit van de betreffende belastingplichtige.

2. De lidstaten die gebruikmaken van de in lid 1 bedoelde mogelijkheid tot vrijstelling, verlenen, na raadpleging van het BTW-Comité, deze vrijstelling ook voor handelingen die betrekking hebben op de door de belastingplichtige onder de in artikel 138 gestelde voorwaarden verrichte leveringen, ten belope van het bedrag van de leveringen die hij onder dezelfde voorwaarden in de voorafgaande twaalf maanden heeft verricht.

#### HOOFDSTUK 1

Ontstaan en omvang van het recht op aftrek
###### Art. 167
Het recht op aftrek ontstaat op het tijdstip waarop de aftrekbare belasting verschuldigd wordt.
###### Art. 168
Voor zover de goederen en diensten worden gebruikt voor de belaste handelingen van een belastingplichtige, is deze gerechtigd in de lidstaat waar hij deze handelingen verricht, van het door hem verschuldigde belastingbedrag de volgende bedragen af te trekken:
a)

de BTW die in die lidstaat verschuldigd of voldaan is voor de goederenleveringen of de diensten die een andere belastingplichtige voor hem heeft verricht;

b)

de BTW die verschuldigd is voor overeenkomstig artikel 18, punt a), en artikel 27 met goederenleveringen of met diensten gelijkgestelde handelingen;

c)

de BTW die verschuldigd is voor de intracommunautaire verwervingen van goederen overeenkomstig artikel 2, lid 1, onder b), punt i);

d)

de BTW die verschuldigd is voor overeenkomstig de artikelen 21 en 22 met intracommunautaire verwerving gelijkgestelde handelingen;

e)

de BTW die verschuldigd of voldaan is voor de in die lidstaat ingevoerde goederen.
###### Art. 169

Naast de in artikel 168 bedoelde aftrek heeft de belastingplichtige recht op aftrek van de in dat artikel bedoelde BTW, voorzover de goederen en de diensten worden gebruikt voor de volgende handelingen:
a)

door de belastingplichtige buiten de lidstaat waar de belasting verschuldigd of voldaan is verrichte handelingen in verband met de in artikel 9, lid 1, tweede alinea, bedoelde werkzaamheden, waarvoor recht op aftrek zou ontstaan indien zij in die lidstaat zouden zijn verricht;

b)

door de belastingplichtige verrichte handelingen waarvoor overeenkomstig de artikelen 138, 142 en 144, de artikelen 146 tot en met 149, de artikelen 151, 152, 153 en 156, artikel 157, lid 1, onder b), de artikelen 158 tot en met 161 en artikel 164 vrijstelling is verleend;

c)

door de belastingplichtige verrichte handelingen waarvoor krachtens artikel 135, lid 1, punten a) tot en met f), vrijstelling is verleend, indien de afnemer buiten de Gemeenschap gevestigd is of indien de handelingen rechtstreeks samenhangen met goederen die bestemd zijn om uit de Gemeenschap te worden uitgevoerd.

###### Art. 165
De lidstaten kunnen een gemeenschappelijke grens vaststellen voor het bedrag van de vrijstellingen die zij op grond van artikel 164 verlenen.
Gemeenschappelijke bepaling met betrekking tot de afdelingen 1 en 2
##### Afdeling 3
###### Art. 166
De Commissie dient, indien nodig, zo spoedig mogelijk bij de
Raad voorstellen in betreffende de gemeenschappelijke bepalingen voor de toepassing van de BTW op de in de afdelingen 1 en 2 bedoelde handelingen.

L 347/36

Publicatieblad van de Europese Unie

NL


###### Art. 170

###### Art. 172

Een belastingplichtige die in de zin van artikel 1 van Richtlijn 79/
1072/EEG (1), artikel 1 van Richtlijn 86/560/EEG (2) en artikel 171 van deze richtlijn, niet gevestigd is in de lidstaat waar hij goederen en diensten aankoopt of aan BTW onderworpen goederen invoert, heeft recht op teruggaaf van de BTW indien de goederen en diensten worden gebruikt voor de volgende handelingen:

1. Eenieder die als belastingplichtige wordt beschouwd op grond van het feit dat hij incidenteel de levering van een nieuw vervoermiddel verricht onder de in artikel 138, lid 1 en lid 2, onder a), gestelde voorwaarden is gerechtigd, in de lidstaat waar de levering wordt verricht, de BTW die in de aankoopprijs begrepen is of die wegens de invoer of de intracommunautaire verwerving van het vervoermiddel voldaan, af te trekken binnen de grenzen of ten belope van het bedrag van de belasting dat hij verschuldigd zou zijn indien voor de levering geen vrijstelling gold.

a)

de in artikel 169 bedoelde handelingen;

b)

de handelingen waarvoor de belasting overeenkomstig de artikelen 194 tot en met 197 en artikel 199 alleen door de afnemer verschuldigd is.
###### Art. 171

1. De teruggaaf van de BTW aan belastingplichtigen die niet in de lidstaat waar zij goederen en diensten aankopen of aan BTW onderworpen goederen invoeren, maar in een andere lidstaat gevestigd zijn, geschiedt volgens de bij Richtlijn 79/1072/EEG van de Raad vastgestelde uitvoeringsbepalingen.
De in artikel 1 van Richtlijn 79/1072/EEG bedoelde belastingplichtigen die in de lidstaat waar zij goederen en diensten aankopen of aan BTW onderworpen goederen invoeren, slechts goederenleveringen of diensten hebben verricht waarvoor degene voor wie deze handelingen bestemd zijn, overeenkomstig de artikelen 194 tot en met 197 en artikel 199 is aangewezen als de tot voldoening van de belasting gehouden persoon, worden voor de toepassing van die richtlijn eveneens beschouwd als niet in die lidstaat gevestigde belastingplichtigen.
2. De teruggaaf van de BTW aan belastingplichtigen die niet op het grondgebied van de Gemeenschap gevestigd zijn, geschiedt volgens de bij Richtlijn 86/560/EEG van de Raad vastgestelde uitvoeringsbepalingen.
De in artikel 1 van Richtlijn 86/560/EEG bedoelde belastingplichtigen die in de lidstaat waar zij goederen en diensten aankopen of aan BTW onderworpen goederen invoeren, slechts goederenleveringen of diensten hebben verricht waarvoor degene voor wie deze handelingen zijn bestemd, overeenkomstig de artikelen 194 tot en met 197 en artikel 199, is aangewezen als de tot voldoening van de belasting gehouden persoon, worden voor de toepassing van die richtlijn eveneens beschouwd als niet in de Gemeenschap gevestigde belastingplichtigen.
3. De Richtlijnen 79/1072/EEG en 86/560/EEG zijn niet van toepassing op goederenleveringen waarvoor krachtens artikel 138 vrijstelling is verleend of kan worden verleend indien de aldus geleverde goederen door of voor rekening van de afnemer worden verzonden of vervoerd.
(1) Achtste Ricthlijn 79/1072/EEG van de Raad van 6 december 1979 betreffende de harmonisatie van de wetgevingen der lidstaten inzake omzetbelasting — Regeling voor de teruggaaf van de belasting over de toegevoegde waarde aan niet in het binnenland gevestigde belastingplichtigen (PB L 331 van 27.12.1979, blz. 11). Richtlijn laatstelijk gewijzigd bij de Toetredingsakte van 2003.
(2) Dertiende Richtlijn 86/560/EEG van de Raad van 17 november 1986 betreffende de harmonisatie van de wetgevingen der lidstaten inzake omzetbelasting — Regeling voor de teruggaaf van de belasting over de toegevoegde waarde aan niet op het grondgebied van de Gemeenschap gevestigde belastingplichtigen (PB L 326 van 21.11.1986, blz. 40).

Het recht op aftrek ontstaat pas en kan pas worden uitgeoefend op het tijdstip van de levering van het nieuwe vervoermiddel.
2. De lidstaten stellen nadere regels voor de toepassing van lid 1 vast.
#### HOOFDSTUK 2

Evenredige aftrek
###### Art. 173
1. Voor goederen en diensten die door een belastingplichtige zowel worden gebruikt voor de in de artikelen 168, 169 en 170 bedoelde handelingen, waarvoor recht op aftrek bestaat, als voor handelingen waarvoor geen recht op aftrek bestaat, wordt aftrek slechts toegestaan voor het gedeelte van de BTW dat evenredig is aan het bedrag van de eerstbedoelde handelingen (evenredige aftrek).
Het aftrekbare gedeelte wordt overeenkomstig de artikelen 174 en 175 bepaald voor het totaal van de door de belastingplichtige verrichte handelingen.
2. De lidstaten kunnen de volgende maatregelen nemen:
a)

de belastingplichtige toestaan een aftrekbaar gedeelte te bepalen voor iedere sector van zijn bedrijfsuitoefening, indien voor ieder van deze sectoren een aparte boekhouding wordt gevoerd;

b)

de belastingplichtige verplichten voor iedere sector van zijn bedrijfsuitoefening een aftrekbaar gedeelte te bepalen en voor ieder van deze sectoren een aparte boekhouding te voeren;

c)

de belastingplichtige toestaan of ertoe verplichten de aftrek toe te passen volgens het gebruik van de goederen en diensten of van een deel daarvan;

d)

de belastingplichtige toestaan of ertoe verplichten de aftrek toe te passen volgens de in lid 1, eerste alinea, vastgestelde regel voor alle goederen en diensten die zijn gebruikt voor alle daarin bedoelde handelingen;

e)

bepalen dat, indien de BTW die niet door de belastingplichtige kan worden afgetrokken, onbeduidend is, hiermee geen rekening wordt gehouden.


Publicatieblad van de Europese Unie

NL

L 347/37

###### Art. 174

#### HOOFDSTUK 3

1. Het aftrekbare gedeelte is de uitkomst van een breuk, waarvan:

Beperkingen van het recht op aftrek
###### Art. 170

a)

de teller bestaat uit het totale bedrag van de per jaar berekende omzet, de BTW niet inbegrepen, met betrekking tot handelingen waarvoor overeenkomstig de artikelen 168 en 169 recht op aftrek bestaat, en

b)

de noemer bestaat uit het totale bedrag van de per jaar berekende omzet, de BTW niet inbegrepen, met betrekking tot de handelingen die in de teller zijn opgenomen en de handelingen waarvoor geen recht op aftrek bestaat.

De lidstaten kunnen in de noemer het bedrag van andere subsidies opnemen dan die welke rechtstreeks verband houden met de in artikel 73 bedoelde prijs van de handelingen.

De Raad bepaalt op voorstel van de Commissie met eenparigheid van stemmen voor welke uitgaven geen recht op aftrek van de BTW bestaat. In ieder geval zijn uitgaven zonder strikt professioneel karakter, zoals weelde-uitgaven en uitgaven voor ontspanning of representatie, van het recht op aftrek uitgesloten.
Totdat de in de eerste alinea bedoelde bepalingen in werking treden, kunnen de lidstaten elke uitsluiting handhaven waarin hun wetgeving op 1 januari 1979 dan wel, voor de lidstaten die na die datum tot de Gemeenschap zijn toegetreden, op de datum van hun toetreding voorzag.
###### Art. 177

2. In afwijking van lid 1 worden voor de berekening van het aftrekbare gedeelte de volgende bedragen buiten beschouwing gelaten:

Na raadpleging van het BTW-Comité kan elke lidstaat om conjuncturele redenen investeringsgoederen of andere goederen geheel of gedeeltelijk van de aftrekregeling uitsluiten.

a)

de omzet met betrekking tot de levering van investeringsgoederen die door de belastingplichtige in het kader van zijn onderneming worden gebruikt;

b)

de omzet met betrekking tot bijkomstige handelingen ter zake van onroerende goederen en bijkomstige financiële handelingen;

Teneinde gelijke mededingingsvoorwaarden te behouden, kunnen de lidstaten in plaats van de aftrek te weigeren, de door de belastingplichtige zelf vervaardigde of door hem in de Gemeenschap aangekochte dan wel door hem ingevoerde gelijksoortige goederen zodanig belasten dat deze belasting het bedrag van de BTW op de verwerving van soortgelijke goederen niet overschrijdt.

c)

de omzet met betrekking tot de in artikel 135, lid 1, punten b) tot en met g), bedoelde handelingen die bijkomstig zijn.

#### HOOFDSTUK 4

Wijze van uitoefening van het recht op aftrek
###### Art. 178

3. Indien de lidstaten gebruikmaken van de in artikel 191 geboden mogelijkheid geen herziening voor investeringsgoederen te eisen, mogen zij de opbrengst van de verkoop van investeringsgoederen opnemen in de berekening van het aftrekbare gedeelte.

Om zijn recht op aftrek te kunnen uitoefenen, moet de belastingplichtige aan de volgende voorwaarden voldoen:
a)

voor de in artikel 168, punt a), bedoelde aftrek met betrekking tot goederenleveringen en diensten: in het bezit zijn van een overeenkomstig de artikelen 220 tot en met 236 en de artikelen 238, 239 en 240 opgestelde factuur;

1. Het aftrekbare gedeelte wordt op jaarbasis vastgesteld, uitgedrukt in een percentage en op de hogere eenheid afgerond.

b)

2. De voorlopige aftrek voor een bepaald jaar is gelijk aan de aftrek die op grond van de handelingen van het voorgaande jaar is berekend. Indien een dergelijke basis ontbreekt of niet relevant is, wordt de aftrek door de belastingplichtige onder toezicht van de belastingdiensten aan de hand van zijn eigen prognoses voorlopig geraamd.

voor de in artikel 168, punt b), bedoelde aftrek met betrekking tot met goederenleveringen en diensten gelijkgestelde handelingen: de door elke lidstaat voorgeschreven formaliteiten vervullen;

c)

voor de in artikel 168, punt c), bedoelde aftrek met betrekking tot intracommunautaire verwerving van goederen: op de in artikel 250 bedoelde BTW-aangifte alle gegevens hebben vermeld die nodig zijn om het bedrag van de wegens zijn verwerving van goederen verschuldigde BTW vast te stellen, en in het bezit zijn van een overeenkomstig de artikelen 220 tot en met 236 opgestelde factuur;

d)

voor de in artikel 168, punt d), bedoelde aftrek met betrekking tot met intracommunautaire verwervingen van goederen gelijkgestelde handelingen: de door elke lidstaat voorgeschreven formaliteiten vervullen;

###### Art. 175

De lidstaten kunnen evenwel hun op 1 januari 1979 geldende regeling dan wel, voor de lidstaten die na die datum tot de Gemeenschap zijn toegetreden, hun op de datum van hun toetreding geldende regeling handhaven.
3. De aftrek die op grond van de voorlopige aftrek heeft plaatsgevonden, wordt herzien nadat voor elk jaar in het daaropvolgende jaar de definitieve aftrek is vastgesteld.

L 347/38
e)

f)

Publicatieblad van de Europese Unie

NL

voor de in artikel 168, punt e), bedoelde aftrek met betrekking tot invoer van goederen: in het bezit zijn van een document waaruit de invoer blijkt en waarin hij wordt aangeduid als degene voor wie de invoer bestemd is of als de importeur, en waarin het bedrag van de verschuldigde BTW wordt vermeld of op grond waarvan dat bedrag kan worden berekend; wanneer hij als afnemer tot voldoening van de belasting is gehouden, in geval van toepassing van de artikelen 194 tot en met 197 en artikel 199: de door de respectieve lidstaten voorgeschreven formaliteiten vervullen.
###### Art. 179

###### Art. 185

1. De herziening vindt met name plaats indien zich na de
BTW-aangifte wijzigingen hebben voorgedaan in de elementen die voor het bepalen van het bedrag van de aftrek in aanmerking zijn genomen, bijvoorbeeld in geval van geannuleerde aankopen of verkregen rabatten.
2. In afwijking van lid 1 vindt geen herziening plaats voor handelingen die geheel of gedeeltelijk onbetaald zijn gebleven, in geval van naar behoren bewezen en aangetoonde vernietiging, verlies of diefstal, alsmede in geval van de in artikel 16 bedoelde onttrekking voor het verstrekken van geschenken van geringe waarde en van monsters.

De belastingplichtige past de aftrek toe door op het totale bedrag van de over een belastingtijdvak verschuldigde belasting het totale bedrag van de BTW in mindering te brengen waarvoor in hetzelfde tijdvak het recht op aftrek is ontstaan en krachtens artikel 178 wordt uitgeoefend.

In geval van geheel of gedeeltelijk onbetaald gebleven handelingen en in geval van diefstal, kunnen de lidstaten evenwel herziening eisen.

De lidstaten kunnen evenwel bepalen dat belastingplichtigen die de in artikel 12 omschreven handelingen incidenteel verrichten, het recht op aftrek uitsluitend op het tijdstip van levering mogen uitoefenen.

De lidstaten stellen nadere regels voor de toepassing van de artikelen 184 en 185 vast.

###### Art. 180
De lidstaten kunnen een belastingplichtige een aftrek toestaan die niet overeenkomstig de artikelen 178 en 179 is toegepast.
###### Art. 181
De lidstaten kunnen een belastingplichtige die niet in het bezit is van een overeenkomstig de artikelen 220 tot en met 236 opgestelde factuur, toestaan de in artikel 168, punt c), bedoelde aftrek toe te passen met betrekking tot diens intracommunautaire verwervingen van goederen.
###### Art. 182
De lidstaten stellen de voorwaarden en de nadere regels voor de toepassing van de artikelen 180 en 181 vast.
###### Art. 183
Indien voor een bepaald belastingtijdvak het bedrag van de aftrek groter is dan dat van de verschuldigde BTW, kunnen de lidstaten hetzij het overschot doen overbrengen naar het volgende tijdvak, hetzij het overschot teruggeven overeenkomstig de door hen vastgestelde regeling.
De lidstaten kunnen evenwel bepalen dat het bedrag van het overschot niet naar een volgend tijdvak wordt overgebracht, of niet wordt teruggegeven, indien dit bedrag onbeduidend is.
#### HOOFDSTUK 5

Herziening van de aftrek

###### Art. 186

###### Art. 187
1. Voor investeringsgoederen wordt de herziening gespreid over een periode van vijf jaar, het jaar van verkrijging of vervaardiging der goederen daaronder begrepen.
De lidstaten kunnen evenwel de herziening baseren op een periode van vijf volle jaren te rekenen vanaf de ingebruikneming van de goederen.
Voor onroerende investeringsgoederen kan de herzieningsperiode tot maximaal twintig jaar worden verlengd.
2. Voor elk jaar heeft de herziening slechts betrekking op eenvijfde deel, of, indien de herzieningsperiode is verlengd, op het overeenkomstige gedeelte van de BTW op de investeringsgoederen.
De in de eerste alinea bedoelde herziening geschiedt op basis van de wijzigingen in het recht op aftrek die zich in de loop van de volgende jaren ten opzichte van het jaar van verkrijging, vervaardiging of, in voorkomend geval, eerste gebruik van de goederen hebben voorgedaan.
###### Art. 188
1. Investeringsgoederen die gedurende de herzieningsperiode worden geleverd, worden tot het verstrijken van de herzieningsperiode beschouwd als investeringsgoederen die voor een economische activiteit van de belastingplichtige worden gebruikt.
De economische activiteit wordt geacht volledig belast te zijn indien de levering van het investeringsgoed belast is.
De economische activiteit wordt geacht volledig vrijgesteld te zijn indien de levering van het investeringsgoed vrijgesteld is.

###### Art. 184
De oorspronkelijk toegepaste aftrek wordt herzien indien deze hoger of lager is dan die welke de belastingplichtige gerechtigd was toe te passen.

2. De in lid 1 bepaalde herziening wordt in één keer verricht voor de gehele nog resterende herzieningsperiode. Indien de levering van investeringsgoederen vrijgesteld is, kunnen de lidstaten er evenwel van afzien herziening te eisen, voorzover


Publicatieblad van de Europese Unie

NL

de afnemer een belastingplichtige is die de betrokken investeringsgoederen uitsluitend gebruikt voor handelingen waarvoor de BTW in aftrek mag worden gebracht.
###### Art. 189
Voor de toepassing van de artikelen 187 en 188 kunnen de lidstaten de volgende maatregelen nemen:
a)

het begrip investeringsgoederen definiëren;

b)

het bedrag aan BTW dat bij de herziening in aanmerking moet worden genomen, nader bepalen;

c)

alle passende maatregelen nemen om te verzekeren dat de herziening niet tot ongerechtvaardigde voordelen leidt;

d)

administratieve vereenvoudigingen toestaan.

###### Art. 194
1. In het geval dat de belastbare goederenlevering of de belastbare dienst wordt verricht door een belastingplichtige die niet gevestigd is in de lidstaat waar de BTW verschuldigd is, kunnen de lidstaten bepalen dat de tot voldoening van de belasting gehouden persoon degene is voor wie de goederenlevering of de dienst wordt verricht.
2. De lidstaten stellen de voorwaarden voor de toepassing van lid 1 vast.
###### Art. 195
De BTW is verschuldigd door de voor BTW-doeleinden in de lidstaat waar de belasting verschuldigd is geïdentificeerde afnemer aan wie de goederen worden geleverd onder de in de artikelen 38 of 39 bepaalde voorwaarden, wanneer deze leveringen worden verricht door een niet in die lidstaat gevestigde belastingplichtige.

###### Art. 190
Voor de toepassing van dit hoofdstuk kunnen de lidstaten diensten die kenmerken hebben die vergelijkbaar zijn met de kenmerken die doorgaans aan investeringsgoederen worden toegeschreven, als investeringsgoederen beschouwen.
###### Art. 191
Indien het praktische effect van de toepassing van de artikelen 187 en 188 in een lidstaat onbeduidend is, kan die lidstaat, na raadpleging van het BTW-Comité, afzien van de toepassing van deze artikelen, rekening houdend met de totale BTW-druk in de betrokken lidstaat en de noodzaak van administratieve vereenvoudiging en mits zulks niet tot verstoring van de mededinging leidt.

###### Art. 196
De BTW is verschuldigd door de belastingplichtige afnemer van een in artikel 56 bedoelde dienst, of door de voor BTWdoeleinden in de lidstaat waar de belasting verschuldigd is geïdentificeerde afnemer van een onder de artikelen 44, 47, 50, 53, 54 en 55 vallende dienst wanneer de dienst door een niet in die lidstaat gevestigde belastingplichtige wordt verricht.
###### Art. 197
1. De BTW is verschuldigd door degene voor wie de goederenlevering bestemd is wanneer aan de volgende voorwaarden vervuld zijn:
a)

de belastbare handeling is een goederenlevering die onder de voorwaarden van artikel 141 wordt verricht;

b)

degene voor wie de levering bestemd is, is een andere belastingplichtige of een niet-belastingplichtige rechtspersoon, die voor BTW-doeleinden is geïdentificeerd in de lidstaat waar de levering wordt verricht;

c)

de factuur welke is uitgereikt door de belastingplichtige die niet gevestigd is in de lidstaat van degene voor wie de levering bestemd is, is opgesteld overeenkomstig de artikelen 220 tot en met 236.

###### Art. 192
Bij overgang van een normale belastingregeling naar een bijzondere regeling, of andersom, kunnen de lidstaten de nodige maatregelen nemen om te verzekeren dat de betrokken belastingplichtigen noch ongerechtvaardigde voordelen genieten, noch ongerechtvaardigde nadelen ondervinden.
### TITEL XI
VERPLICHTINGEN VAN DE BELASTINGPLICHTIGEN EN VAN
BEPAALDE NIET–BELASTINGPLICHTIGE PERSONEN

L 347/39

Verplichting tot betaling

2. In het geval dat overeenkomstig artikel 204 een fiscaal vertegenwoordiger wordt aangewezen als de tot voldoening van de belasting gehouden persoon, kunnen de lidstaten een afwijking van lid 1 van dit artikel toestaan.


##### Afdeling 1
###### Art. 198

Te g e n o v e r d e s c h a t k i s t t o t v o l d o e n i n g v a n de belasting gehouden personen

1. Wanneer uit hoofde van artikel 344 belasting wordt geheven over specifieke handelingen met betrekking tot beleggingsgoud tussen een lid van een gereglementeerde goudmarkt en een andere belastingplichtige die geen lid is van die markt, wijzen de lidstaten de afnemer aan als de tot voldoening van de belasting gehouden persoon.

#### HOOFDSTUK 1

###### Art. 193
De BTW is verschuldigd door de belastingplichtige die een belastbare goederenlevering of een belastbare dienst verricht, behalve in de gevallen waarin de belasting uit hoofde van de artikelen 194 tot en met 199 en artikel 202 door een andere persoon verschuldigd is.

Indien de afnemer die geen lid is van een gereglementeerde goudmarkt een belastingplichtige is en zich uitsluitend voor de in artikel 344 bedoelde handelingen voor BTW-doeleinden dient te

L 347/40

Publicatieblad van de Europese Unie

NL

goederen of diensten overeenkomstig artikel 2 worden beschouwd, voor alle in lid 1 bedoelde voor hem verrichte diensten als belastingplichtige wordt aangemerkt;

identificeren in de lidstaat waar de belasting verschuldigd is, vervult de verkoper de fiscale verplichtingen namens de afnemer, overeenkomstig de voorschriften van die lidstaat.
2. In het geval dat een belastingplichtige die een keuzerecht overeenkomstig de artikelen 348, 349 of 350 uitoefent, een levering van goud of van halffabrikaten met een zuiverheid van ten minste 325/1 000, of een levering van beleggingsgoud als omschreven in artikel 344, lid 1, verricht, kunnen de lidstaten de afnemer aanwijzen als de tot voldoening van de belasting gehouden persoon.
3. De lidstaten stellen de procedures en voorwaarden voor de toepassing van lid 1 en lid 2 vast.
###### Art. 199
1. De lidstaten kunnen bepalen dat de tot voldoening van de belasting gehouden persoon degene is voor wie de volgende goederenleveringen of diensten worden verricht:
a)

bouwwerkzaamheden, met inbegrip van herstel-, schoonmaak-, onderhouds-, aanpassings- en sloopwerkzaamheden ter zake van onroerend goed, alsmede de oplevering van een werk in onroerende staat die krachtens artikel 14, lid 3, als een levering van goederen wordt beschouwd;

b)

de uitlening van personeel dat de onder punt a) genoemde werkzaamheden verricht;

c)

de levering van onroerend goed als bedoeld in artikel 135, lid 1, punten j) en k), wanneer de leverancier overeenkomstig artikel 137 heeft gekozen voor belastingheffing ter zake van die levering;

d)

de levering van oude materialen, oude materialen ongeschikt voor hergebruik in dezelfde staat, industrieel en nietindustrieel afval, afval voor hergebruik, gedeeltelijk verwerkt afval, schroot, en bepaalde goederen en diensten, overeenkomstig de lijst in bijlage VI;

e)

de levering van in zekerheid gegeven goederen door een belastingplichtige aan een andere persoon tot executie van die zekerheid;

f)

de levering van goederen na overdracht van eigendomsvoorbehoud aan een rechtverkrijgende die zijn recht uitoefent;

g)

de levering van onroerend goed dat in een openbare verkoop op grond van een executoriale titel door de executieschuldenaar aan een andere persoon wordt verkocht.

2. Wanneer zij gebruik maken van de mogelijkheid die lid 1 biedt, kunnen de lidstaten de goederenleveringen en diensten die eronder vallen, omschrijven, alsook de categorieën van leveranciers en dienstverrichters of afnemers waarop deze maatregelen van toepassing kunnen zijn.
3. Voor de toepassing van lid 1 kunnen de lidstaten de volgende maatregelen nemen:
a)

bepalen dat een belastingplichtige die ook activiteiten of handelingen verricht die niet als belastbare leveringen van


b)

bepalen dat een niet-belastingplichtige publiekrechtelijke instelling met betrekking tot de overeenkomstig lid 1, punten e), f) en g) afgenomen goederenleveringen of diensten als belastingplichtige wordt aangemerkt.

4. De lidstaten stellen het BTW-Comité in kennis van de nationale maatregelen die zij uit hoofde van lid 1 hebben genomen indien het geen maatregelen betreft die voor 13 augustus 2006 door de Raad overeenkomstig artikel 27, leden 1 tot en met 4, van Richtlijn 77/388/EEG zijn toegestaan en uit hoofde van die bepaling worden verlengd.
###### Art. 200
De BTW is verschuldigd door eenieder die een belastbare intracommunautaire verwerving van goederen verricht.
###### Art. 201
Bij invoer is de BTW verschuldigd door degene(n) die de lidstaat van invoer als de tot voldoening van de belasting gehouden personen heeft aangewezen of erkend.
###### Art. 202
De BTW is verschuldigd door degene door wiens toedoen de goederen worden onttrokken aan de in de artikelen 156, 157, 158, 160 en 161 genoemde regelingen of situaties.
###### Art. 203
De BTW is verschuldigd door eenieder die deze belasting op een factuur vermeldt.
###### Art. 204
1. Wanneer bij de toepassing van de artikelen 193 tot en met
197 en de artikelen 199 en 200 de tot voldoening van de belasting gehouden persoon een belastingplichtige is die niet is gevestigd in de lidstaat waar de BTW verschuldigd is, kunnen de lidstaten hem de mogelijkheid geven een fiscaal vertegenwoordiger aan te wijzen als tot voldoening van de belasting gehouden persoon.
In het geval dat de belastbare handeling wordt verricht door een belastingplichtige die niet in de lidstaat is gevestigd waar de BTW verschuldigd is, en er met het land van het hoofdkantoor of de vestiging van deze belastingplichtige geen rechtsinstrument inzake wederzijdse bijstand bestaat waarvan de strekking gelijk is aan die van Richtlijn 76/308/EEG (1) en
(1) Richtlijn 76/308/EEG van de Raad van 15 maart 1976 betreffende de wederzijdse bijstand inzake de invordering van schuldvorderingen die voortvloeien uit verrichtingen die deel uitmaken van het financieringsstelsel van het Europees Oriëntatie- en Garantiefonds voor de Landbouw, alsmede van landbouwheffingen en douanerechten (PB L 73 van 19.3.1976, blz. 18). Richtlijn laatstelijk gewijzigd bij de Toetredingsakte van 2003.


Publicatieblad van de Europese Unie

NL

Verordening (EG) nr. 1798/2003 (1), kunnen de lidstaten bepalen dat een door deze belastingplichtige aangewezen fiscaal vertegenwoordiger tot voldoening van de belasting wordt gehouden.
De lidstaten kunnen de in de tweede alinea bedoelde mogelijkheid echter niet toepassen op niet in de Gemeenschap gevestigde belastingplichtigen in de zin van artikel 358, punt 1), die voor de bijzondere regeling voor langs elektronische weg verrichte diensten hebben gekozen.
2. De in lid 1, eerste alinea, bedoelde mogelijkheid is onderworpen aan de door de respectieve lidstaten vastgestelde voorwaarden en uitvoeringsbepalingen.
###### Art. 205
In de in de artikelen 193 tot en met 200 en 202, 203 en 204 bedoelde situaties kunnen de lidstaten bepalen dat een andere persoon dan degene die tot voldoening van de belasting is gehouden, hoofdelijk verplicht is de BTW te voldoen.
Wijze van betaling
##### Afdeling 2
###### Art. 206
Iedere belastingplichtige die tot voldoening van de belasting is gehouden, moet het nettobedrag van de BTW bij de indiening van de in artikel 250 bedoelde aangifte voldoen. De lidstaten kunnen echter een ander tijdstip voor de betaling van dit bedrag vaststellen of bepalen dat voorlopige vooruitbetalingen moeten worden gedaan.

L 347/41
###### Art. 209

De lidstaten treffen de nodige maatregelen opdat niet-belastingplichtige rechtspersonen die gehouden zijn tot voldoening van de belasting welke verschuldigd is wegens de in artikel 2, lid 1, onder b), punt i), bedoelde intracommunautaire verwerving van goederen, de in deze afdeling vastgestelde betalingsverplichtingen nakomen.
###### Art. 210
De lidstaten stellen nadere regels vast met betrekking tot de betaling ter zake van de in artikel 2, lid 1, onder b), punt ii), bedoelde intracommunautaire verwerving van nieuwe vervoermiddelen en de in artikel 2, lid 1, onder b), punt iii), bedoelde intracommunautaire verwerving van accijnsproducten.
###### Art. 211
De lidstaten stellen nadere regels vast met betrekking tot de betaling ter zake van de invoer van goederen.
De lidstaten kunnen in het bijzonder bepalen dat met betrekking tot de invoer van goederen die wordt verricht door belastingplichtigen of tot betaling van de belasting gehouden personen, of door bepaalde categorieën daarvan, de wegens de invoer verschuldigde BTW niet hoeft te worden betaald op het tijdstip van de invoer, mits deze belasting als zodanig wordt vermeld in de overeenkomstig artikel 250 opgestelde BTW-aangifte.
###### Art. 212
De lidstaten kunnen de belastingplichtigen vrijstellen van de betaling van de verschuldigde BTW wanneer het bedrag daarvan onbeduidend is.

###### Art. 207
#### HOOFDSTUK 2

De lidstaten treffen de nodige maatregelen opdat de personen die overeenkomstig de artikelen 194 tot en met 197 en de artikelen 199 en 204 worden geacht in plaats van een niet op hun respectieve grondgebied gevestigde belastingplichtige tot voldoening van de belasting te zijn gehouden, de in deze afdeling vastgestelde betalingsverplichtingen nakomen.
De lidstaten treffen voorts de nodige maatregelen opdat de personen die overeenkomstig artikel 205 worden geacht hoofdelijk verplicht te zijn de BTW te voldoen, deze betalingsverplichtingen nakomen.
###### Art. 208
De lidstaten die overeenkomstig artikel 198, lid 1, de afnemer van beleggingsgoud als de tot voldoening van de belasting gehouden persoon aanwijzen of gebruik maken van de in artikel 198, lid 2, geboden mogelijkheid om de afnemer van goud, halffabrikaten of beleggingsgoud als omschreven in artikel 344, lid 1, als de tot voldoening van de belasting gehouden persoon aan te wijzen, treffen de nodige maatregelen opdat die afnemer de in deze afdeling vastgestelde betalingsverplichtingen nakomt.
(1) Verordening (EG) nr. 1798/2003 van de Raad van 7 oktober 2003 betreffende de administratieve samenwerking op het gebied van de belasting over de toegevoegde waarde (PB L 264 van 15.10.2003, blz. 1). Verordening gewijzigd bij Verordening (EG) nr. 885/2004 (PB L 168 van 1.5.2004, blz. 1).

Identificatie
###### Art. 213
1. Iedere belastingplichtige moet opgave doen van het begin, de wijziging en de beëindiging van zijn activiteit als belastingplichtige.
De lidstaten staan onder door hen vast te stellen voorwaarden toe dat de aangifte langs elektronische weg geschiedt en kunnen dit ook verplicht stellen.
2. Onverminderd lid 1, eerste alinea, moet iedere belastingplichtige of niet-belastingplichtige rechtspersoon die intracommunautaire verwervingen van goederen verricht welke niet op grond van artikel 3, lid 1, aan de BTW zijn onderworpen, melden dat hij dergelijke verwervingen verricht, indien de in dat artikel gestelde voorwaarden om deze verwervingen niet aan de BTW te onderwerpen niet meer vervuld zijn.
###### Art. 214
1. De lidstaten treffen de nodige maatregelen voor de identificatie onder een individueel nummer van de volgende personen:
a)

iedere belastingplichtige, uitgezonderd de in artikel 9, lid 2, bedoelde, die op hun respectieve grondgebied

L 347/42

Publicatieblad van de Europese Unie

NL

goederenleveringen of diensten verricht welke recht op aftrek doen ontstaan, andere dan de goederenleveringen of de diensten waarvoor overeenkomstig de artikelen 194 tot en met 197 en artikel 199 uitsluitend de afnemer of degene voor wie de goederen of de diensten bestemd zijn, de BTW verschuldigd is;
b)

c)

iedere belastingplichtige of niet-belastingplichtige rechtspersoon die intracommunautaire verwervingen van goederen verricht welke op grond van artikel 2, lid 1, onder b), aan de BTW zijn onderworpen of die het in artikel 3, lid 3, bedoelde keuzerecht uitoefent zijn intracommunautaire verwervingen aan de BTW te onderwerpen; iedere belastingplichtige die op hun respectieve grondgebied intracommunautaire verwervingen van goederen verricht met betrekking tot handelingen in verband met de in artikel 9, lid 1, tweede alinea, bedoelde werkzaamheden welke hij buiten dat grondgebied verricht.

2. Het staat de lidstaten vrij bepaalde belastingplichtigen die incidenteel de in artikel 12 bedoelde handelingen verrichten, niet voor BTW-doeleinden te identificeren.
###### Art. 215
Het individuele identificatienummer begint met een landencode overeenkomstig de ISO-code 3166 alpha 2, die aangeeft welke lidstaat het nummer heeft toegekend.
Griekenland is evenwel gerechtigd het prefix EL te hanteren.

formaat dat aan de in dit hoofdstuk vastgestelde voorwaarden voldoet.
###### Art. 219
Ieder document of bericht dat wijzigingen aanbrengt in en specifiek en ondubbelzinnig verwijst naar de oorspronkelijke factuur, geldt als factuur.
Uitreiking van facturen
##### Afdeling 3
###### Art. 220
Iedere belastingplichtige zorgt ervoor dat door hemzelf, door de afnemer of, in zijn naam en voor zijn rekening, door een derde, in de volgende gevallen een factuur wordt uitgereikt: 1)

de goederenleveringen of de diensten die hij heeft verricht voor een andere belastingplichtige of een niet-belastingplichtige rechtspersoon;

2)

de in artikel 33 bedoelde levering van goederen;

3)

de levering van goederen, verricht onder de in artikel 138 gestelde voorwaarden;

4)

de vooruitbetalingen die aan hem worden gedaan voordat een van de in de punten 1), 2) en 3) bedoelde leveringen van goederen is verricht;

5)

de vooruitbetalingen die door een andere belastingplichtige of door een niet-belastingplichtige rechtspersoon aan hem worden gedaan voordat de dienst is verricht.

###### Art. 216
De lidstaten treffen de nodige maatregelen opdat hun identificatiesysteem de in artikel 214 bedoelde belastingplichtigen kan onderscheiden en aldus de juiste toepassing van de in artikel 402 bedoelde overgangsregeling voor de belastingheffing op intracommunautaire handelingen verzekert.


###### Art. 221
#### HOOFDSTUK 3

Facturering
Definitie
##### Afdeling 1
###### Art. 217
Voor de toepassing van dit hoofdstuk wordt onder „langs elektronische weg verzenden” verstaan het verzenden of ter beschikking stellen van gegevens aan de geadresseerde door middel van elektronische apparatuur voor gegevensverwerking (inclusief digitale compressie) en gegevensopslag, met gebruikmaking van draden, radio, optische of andere elektromagnetische middelen.
Het begrip factuur

1. De lidstaten kunnen de belastingplichtige de verplichting opleggen een factuur uit te reiken voor andere dan de in artikel 220 bedoelde goederenleveringen of diensten die hij op hun grondgebied heeft verricht.
De lidstaten kunnen voor de in de eerste alinea bedoelde facturen minder verplichtingen opleggen dan die welke in de artikelen 226, 230, 233, 244 en 246 zijn opgenomen.
2. De lidstaten kunnen de belastingplichtige van de in artikel 220 vastgestelde factureringsplicht ontheffen voor de op hun grondgebied verrichte goederenleveringen of diensten die, al dan niet met recht op aftrek van voorbelasting, overeenkomstig de artikelen 110 en 111, artikel 125, lid 1, artikel 127, artikel 128, lid 1, de artikelen 132, 135, 136, 371, 375, 376 en 377, artikel 378, lid 2, artikel 379, lid 2, en de artikelen 380 tot en met 390 vrijgesteld zijn.
##### Afdeling 2
###### Art. 222

###### Art. 218
Voor de toepassing van deze richtlijn aanvaarden de lidstaten als factuur ieder document of bericht op papier of in elektronisch

De lidstaten kunnen de belastingplichtigen die op hun grondgebied goederenleveringen of diensten verrichten een termijn opleggen voor het uitreiken van de factuur.


Publicatieblad van de Europese Unie

NL

L 347/43

###### Art. 223

4)

Onder de voorwaarden, gesteld door de lidstaten op het grondgebied waarvan de goederenleveringen of de diensten worden verricht, kan voor verscheidene afzonderlijke goederenleveringen of diensten een periodieke factuur worden opgemaakt.

het in artikel 214 bedoelde BTW-identificatienummer van de afnemer waaronder hij een goederenlevering of een dienst heeft afgenomen waarvoor hij tot voldoening van de belasting is gehouden of waaronder hij een in artikel 138 bedoelde goederenlevering heeft afgenomen;

5)

de volledige naam en het volledige adres van de belastingplichtige en zijn afnemer;

6)

de hoeveelheid en de aard van de geleverde goederen of de omvang en de aard van de verrichte diensten;

7)

de datum waarop de goederenlevering of de dienst heeft plaatsgevonden of voltooid is of de datum waarop de in artikel 220, punten 4) en 5), bedoelde vooruitbetaling is gedaan, voor zover die datum vastgesteld is en verschilt van de uitreikingsdatum van de factuur;

8)

de maatstaf van heffing voor elk tarief of elke vrijstelling, de eenheidsprijs, BTW niet inbegrepen, evenals de eventuele vooruitbetalingskortingen, prijskortingen en -rabatten indien die niet in de eenheidsprijs zijn begrepen;

9)

het toegepaste BTW-tarief;

###### Art. 224
1. Facturen mogen door de afnemer worden opgemaakt voor goederenleveringen of diensten die door een belastingplichtige voor hem worden verricht, mits beide partijen dat vooraf onderling zijn overeengekomen en op voorwaarde dat iedere factuur het voorwerp uitmaakt van een procedure van aanvaarding door de belastingplichtige die de goederenleveringen of de diensten verricht.
2. De voorwaarden en uitvoeringsbepalingen van die voorafgaande overeenkomst en van de aanvaardingsprocedures tussen de belastingplichtige en de afnemer worden vastgesteld door de lidstaat op het grondgebied waarvan de goederenleveringen of de diensten worden verricht.
3. De lidstaten kunnen belastingplichtigen die op hun grondgebied goederenleveringen of diensten verrichten, verdere voorwaarden opleggen betreffende de uitreiking van facturen door de afnemer. Zij kunnen met name verlangen dat die facturen worden uitgereikt in naam en voor rekening van de belastingplichtige.
De in de eerste alinea bedoelde voorwaarden moeten in ieder geval altijd dezelfde zijn, ongeacht de plaats waar de afnemer is gevestigd.
###### Art. 225
De lidstaten kunnen de belastingplichtigen die op hun grondgebied goederenleveringen of diensten verrichten, specifieke voorwaarden opleggen in het geval dat de derde, of de afnemer, die de facturen uitreikt, gevestigd is in een land waarmee geen rechtsinstrument inzake wederzijdse bijstand bestaat waarvan de strekking gelijk is aan die van Richtlijn 76/308/EEG en Verordening (EG) nr. 1798/2003.
Inhoud van de facturen
##### Afdeling 4
###### Art. 226
Onverminderd de bijzondere bepalingen van deze richtlijn zijn voor BTW-doeleinden op de overeenkomstig de artikelen 220 en 221 uitgereikte facturen alleen de volgende vermeldingen verplicht: 1)

de datum van uitreiking van de factuur;

2)

een opeenvolgend nummer, met één of meer reeksen, waardoor de factuur eenduidig wordt geïdentificeerd;

3)

het in artikel 214 bedoelde BTW-identificatienummer waaronder de belastingplichtige de goederenleveringen of de diensten heeft verricht;

10) het te betalen BTW-bedrag, tenzij er een bijzondere regeling van toepassing is waarvoor deze richtlijn die vermelding uitsluit;
11) in geval van een vrijstelling of wanneer de afnemer tot voldoening van de belasting is gehouden, een verwijzing naar de toepasselijke bepaling in deze richtlijn of naar de overeenkomstige nationale bepaling of enige andere vermelding dat de goederenlevering of de diensten zijn vrijgesteld of onder de toepassing van de verleggingsregeling vallen;
12) in geval van levering van een nieuw vervoermiddel onder de in artikel 138, lid 1 en lid 2, onder a), gestelde voorwaarden, de in artikel 2, lid 2, tweede alinea, bedoelde gegevens;
13) wanneer de bijzondere regeling voor reisbureaus wordt gehanteerd, een verwijzing naar artikel 306 of de overeenkomstige nationale bepalingen of enige andere vermelding dat deze regeling is toegepast;
14) wanneer een van de bijzondere regelingen voor gebruikte goederen, kunstvoorwerpen, voorwerpen voor verzamelingen of antiquiteiten wordt gehanteerd, een verwijzing naar artikel 313, artikel 326 of artikel 333, of de overeenkomstige nationale bepalingen of enige andere vermelding dat een van deze regelingen is toegepast;
15) wanneer degene die tot voldoening van de belasting gehouden is, een fiscaal vertegenwoordiger is in de zin van artikel 204, het in artikel 214 bedoelde BTWidentificatienummer van deze fiscaal vertegenwoordiger, samen met zijn volledige naam en adres.
###### Art. 227
De lidstaten kunnen belastingplichtigen die op hun grondgebied gevestigd zijn en er goederenleveringen of diensten verrichten, de verplichting opleggen in andere dan de in artikel 226, punt 4),

L 347/44

Publicatieblad van de Europese Unie

NL

bedoelde gevallen het in artikel 214 bedoelde BTW-identificatienummer van hun afnemer te vermelden.


authenticiteit van de oorsprong en de integriteit van de gegevens waarborgen.

###### Art. 228
De lidstaten op het grondgebied waarvan goederenleveringen of diensten worden verricht, kunnen ontheffing verlenen van bepaalde verplichte vermeldingen in de met een factuur gelijkgestelde documenten of berichten bedoeld in artikel 219.

De facturen kunnen evenwel langs elektronische weg worden verzonden of ter beschikking worden gesteld volgens andere methoden, mits deze door de betrokken lidstaten worden aanvaard.

###### Art. 229
De lidstaten leggen niet de verplichting op de facturen te ondertekenen.
###### Art. 230
Op een factuur kunnen bedragen in willekeurig welke munteenheid voorkomen, mits het te betalen BTW-bedrag is uitgedrukt in de nationale munteenheid van de lidstaat waar de plaats van de goederenlevering of de plaats van de diensten is gelegen en mits daarbij gebruik wordt gemaakt van het in artikel 91 bedoelde wisselkoersmechanisme.

2. Voor de toepassing van lid 1, eerste alinea, punt a), kunnen de lidstaten bovendien eisen dat de geavanceerde elektronische handtekening berust op een gekwalificeerd certificaat en is aangemaakt met een veilig middel voor het aanmaken van handtekeningen in de zin van artikel 2, punten 6) en 10), van Richtlijn 1999/93/EG.

3. Voor de toepassing van lid 1, eerste alinea, punt b), kunnen de lidstaten bovendien onder door hen gestelde voorwaarden de toezending eisen van een aanvullend kort overzicht op papier.

###### Art. 231
Ter controle kunnen de lidstaten een vertaling eisen in hun nationale taal van de facturen betreffende op hun grondgebied verrichte goederenleveringen of diensten, alsmede van de facturen die worden ontvangen door op hun grondgebied gevestigde belastingplichtigen.
Ve r z e n d e n v a n f a c t u r e n l a n g s e l e k t r o n i s c h e weg

##### Afdeling 5
###### Art. 234
De lidstaten mogen de belastingplichtigen die op hun grondgebied goederenleveringen of diensten verrichten, geen andere verplichtingen of formaliteiten opleggen betreffende het gebruik van een systeem voor elektronische verzending of terbeschikkingstelling van facturen.

###### Art. 235

###### Art. 232
De overeenkomstig afdeling 2 uitgereikte facturen mogen zowel op papier worden verzonden als, behoudens aanvaarding door de afnemer, elektronisch worden verzonden of ter beschikking gesteld.
###### Art. 233
1. Elektronisch verzonden of ter beschikking gestelde facturen worden door de lidstaten aanvaard, mits de authenticiteit van de herkomst en de integriteit van de inhoud ervan worden gewaarborgd aan de hand van een van de volgende methoden:
a)

een geavanceerde elektronische handtekening in de zin van artikel 2, punt 2), van Richtlijn 1999/93/EG van het Europees Parlement en de Raad van 13 december 1999 betreffende een gemeenschappelijk kader voor elektronische handtekeningen (1);

b)

een elektronische uitwisseling van gegevens (EDI), zoals gedefinieerd in artikel 2 van Aanbeveling 1994/820/EG van de Commissie van 19 oktober 1994 betreffende de juridische aspecten van de elektronische uitwisseling van gegevens (2), wanneer het akkoord betreffende deze uitwisseling in het gebruik van procedures voorziet die de

(1) PB L 13 van 19.1.2000, blz. 12.
(2) PB L 338 van 28.12.1994, blz. 98.

De lidstaten kunnen specifieke voorwaarden opleggen voor het langs elektronische weg uitreiken van facturen betreffende goederenleveringen en diensten die op hun grondgebied zijn verricht vanuit een land waarmee geen rechtsinstrument inzake wederzijdse bijstand bestaat waarvan de strekking gelijk is aan die van Richtlijn 76/308/EEG en Verordening (EG) nr. 1798/2003.

###### Art. 236
Bij een reeks facturen die langs elektronische weg aan dezelfde afnemer worden verzonden of ter beschikking worden gesteld, hoeven de voor de verschillende facturen gelijke vermeldingen slechts één keer te worden opgenomen, voorzover voor elke factuur alle informatie toegankelijk is.

###### Art. 237
De Commissie dient uiterlijk op 31 december 2008 een verslag in, dat in voorkomend geval vergezeld gaat van een voorstel tot wijziging van de voorwaarden inzake elektronische facturering teneinde rekening te houden met toekomstige technologische ontwikkelingen op dit gebied.


Publicatieblad van de Europese Unie

NL

Ve r e e n v o u d i g i n g s m a a t r e g e l e n
##### Afdeling 6
###### Art. 238
1. Na raadpleging van het BTW-Comité kunnen de lidstaten onder de door hen te stellen voorwaarden bepalen dat op de facturen betreffende op hun grondgebied verrichte goederenleveringen of diensten in de volgende gevallen sommige van de in de artikelen 226 en 230 voorgeschreven vermeldingen niet behoeven te worden opgenomen, onverminderd de mogelijkheden waarvan de lidstaten krachtens de artikelen 227, 228 en 231 verkiezen gebruik te maken:
a)

wanneer het bedrag van de factuur onbeduidend is;

b)

wanneer de handels- of administratieve praktijken van de betrokken bedrijfssector of de technische voorwaarden waaronder die facturen uitgereikt worden, de naleving van alle in de artikelen 226 en 230 bedoelde verplichtingen bemoeilijken.

2. De facturen moeten in ieder geval de volgende vermeldingen bevatten:
a)

de datum van uitreiking van de factuur;

b)

de identificatie van de belastingplichtige;

c)

de identificatie van de aard van de geleverde goederen of de verrichte diensten;

d)

het te betalen BTW-bedrag of de gegevens aan de hand waarvan dat bedrag kan worden berekend.

3. De vereenvoudiging waarin lid 1 voorziet, mag niet worden toegepast op de handelingen bedoeld in de artikelen 20, 21, 22, 33, 36, 138 en 141.
###### Art. 239
Ingeval de lidstaten gebruikmaken van de in artikel 272, lid 1, eerste alinea, punt b), geboden mogelijkheid geen BTWidentificatienummer toe te kennen aan belastingplichtigen die geen van de handelingen bedoeld in de artikelen 20, 21, 22, 33, 36, 138 en 141 verrichten, wordt bij niet-toekenning van dat identificatienummer aan de verrichter en de afnemer van de goederenleveringen of de diensten op de factuur een ander nummer vermeld, het zogenaamde fiscaal registratienummer, zoals gedefinieerd door de betrokken lidstaten.
###### Art. 240
Wanneer het BTW-identificatienummer aan de belastingplichtige is toegekend, kunnen de lidstaten die van de in artikel 272, lid 1, eerste alinea, punt b), bedoelde mogelijkheid gebruik maken, bovendien bepalen dat op de factuur het volgende wordt vermeld:

2)

L 347/45

voor andere goederenleveringen of diensten alleen het fiscaal registratienummer van de verrichter van de goederenleveringen of de diensten, dan wel alleen het BTW-identificatienummer.
#### HOOFDSTUK 4

Boekhouding
Definitie
##### Afdeling 1
###### Art. 241
Voor de toepassing van dit hoofdstuk wordt onder „bewaren van een factuur langs elektronische weg” verstaan, het bewaren van gegevens door middel van elektronische apparatuur voor gegevensverwerking (inclusief digitale compressie) en gegevensopslag, met gebruikmaking van draden, radio, optische of andere elektromagnetische middelen.
Algemene verplichtingen
##### Afdeling 2
###### Art. 242
Iedere belastingplichtige moet een boekhouding voeren die voldoende gegevens bevat om de toepassing van de BTW en de controle daarop door de belastingadministratie mogelijk te maken.
###### Art. 243
1. Iedere belastingplichtige moet een register bijhouden van de goederen die door hemzelf of voor zijn rekening zijn verzonden of vervoerd buiten het grondgebied van de lidstaat van vertrek, maar binnen de Gemeenschap, ten behoeve van de in artikel 17, lid 2, punten f), g) en h), bedoelde handelingen bestaande uit werkzaamheden betreffende die goederen of uit het tijdelijke gebruik ervan.
2. Iedere belastingplichtige moet een boekhouding voeren die voldoende gegevens bevat om de goederen te kunnen identificeren die vanuit een andere lidstaat naar hem verzonden zijn door of voor rekening van een in die andere lidstaat voor BTWdoeleinden geïdentificeerde belastingplichtige en die het voorwerp zijn van de in artikel 52, punt c), bedoelde diensten bestaande uit expertises of werkzaamheden betreffende die goederen.
Specif ieke verplichtingen ten aanzien van het bewaren van facturen
##### Afdeling 3
###### Art. 244

1)

voor de in de artikelen 44, 47, 50, 53, 54 en 55 bedoelde diensten en voor de in de artikelen 138 en 141 bedoelde goederenleveringen, het BTW-identificatienummer en het fiscaal registratienummer van de verrichter van de diensten of de goederenleveringen;

Iedere belastingplichtige moet erop toezien dat kopieën van de door hemzelf of door zijn afnemer of, in zijn naam en voor zijn rekening, door een derde uitgereikte facturen en alle door hemzelf ontvangen facturen worden bewaard.

L 347/46

Publicatieblad van de Europese Unie

NL


###### Art. 245


1. Voor de toepassing van deze richtlijn mag de belastingplichtige de plaats van bewaring bepalen, mits hij alle overeenkomstig artikel 244 bewaarde facturen of gegevens op ieder verzoek zonder onnodig uitstel ter beschikking van de bevoegde autoriteiten stelt.

Recht van toegang tot elektronisch bewaarde facturen in een andere lidstaat

2. De lidstaten kunnen de op hun grondgebied gevestigde belastingplichtigen verplichten tot kennisgeving van de plaats van bewaring wanneer deze buiten hun grondgebied gelegen is.
De lidstaten kunnen de op hun grondgebied gevestigde belastingplichtigen er bovendien toe verplichten de door henzelf, door hun afnemers of, in hun naam en voor hun rekening, door derden uitgereikte facturen, alsmede de door hen ontvangen facturen, binnen dat grondgebied te bewaren, wanneer deze bewaring niet geschiedt langs een elektronische weg die een volledige on–linetoegang tot de betrokken gegevens waarborgt.

##### Afdeling 4
###### Art. 249
Wanneer een belastingplichtige de door hem verzonden of ontvangen facturen elektronisch bewaart waarbij een on– linetoegang tot de gegevens wordt gewaarborgd, en de plaats van bewaring in een andere lidstaat gelegen is dan de lidstaat waar hij is gevestigd, hebben de bevoegde autoriteiten van de lidstaat waar deze belastingplichtige gevestigd is met het oog op de toepassing van deze richtlijn het recht van elektronische toegang tot alsmede downloading en gebruik van deze facturen binnen de grenzen bepaald bij de regelgeving van de lidstaat van vestiging van de belastingplichtige, en voorzover deze lidstaat de facturen nodig heeft voor controledoeleinden.
#### HOOFDSTUK 5

Aangiften
###### Art. 246
De authenticiteit van de oorsprong en de integriteit van de inhoud van de bewaarde facturen, alsmede de leesbaarheid ervan, moeten gedurende de volledige periode van bewaring worden gewaarborgd.
De gegevens op de in artikel 233, lid 1, tweede alinea, bedoelde facturen mogen niet worden gewijzigd en moeten gedurende deze periode leesbaar blijven.
###### Art. 247
1. Iedere lidstaat bepaalt hoe lang de belastingplichtigen ervoor moeten zorgen dat de facturen betreffende de op zijn grondgebied verrichte goederenleveringen of diensten en de facturen die op zijn grondgebied gevestigde belastingplichtigen hebben ontvangen, moeten worden bewaard.
2. Om te waarborgen dat de in artikel 246 bedoelde voorwaarden worden vervuld, kan de in lid 1 bedoelde lidstaat bepalen dat de facturen moeten worden bewaard in de oorspronkelijke vorm — op papier of elektronisch — waarin zij zijn toegezonden of ter beschikking gesteld. De lidstaat kan tevens bepalen dat, wanneer de facturen langs elektronische weg worden bewaard, de gegevens die de authenticiteit van de herkomst en de integriteit van de inhoud overeenkomstig artikel 246, eerste alinea, waarborgen, eveneens worden bewaard.
3. De in lid 1 bedoelde lidstaat kan bijzondere voorwaarden stellen met het oog op het verbieden of beperken van de bewaring van de facturen in een land waarmee geen rechtsinstrument inzake wederzijdse bijstand bestaat waarvan de strekking gelijk is aan die van Richtlijn 76/308/EEG en Verordening (EG) nr. 1798/2003 of inzake het in artikel 249 bedoelde recht van elektronische toegang, downloading en gebruik.

###### Art. 250
1. Iedere belastingplichtige moet een BTW-aangifte indienen waarop alle gegevens staan die nodig zijn om het bedrag van de verschuldigde belasting en van de aftrek vast te stellen, daarbij inbegrepen, voorzover zulks voor de vaststelling van de grondslag nodig is, het totale bedrag van de handelingen waarop deze belasting en deze aftrek betrekking hebben, alsmede het bedrag van de vrijgestelde handelingen.
2. De lidstaten staan onder door hen te stellen voorwaarden toe dat de in lid 1 bedoelde BTW-aangifte langs elektronische weg wordt ingediend en mogen dit ook verplicht stellen.
###### Art. 251
Behalve de in artikel 242 bedoelde gegevens moeten in de BTW– aangifte betreffende een bepaald belastingtijdvak de volgende gegevens vermeld zijn:
a)

het totale bedrag, de BTW niet inbegrepen, van de in artikel 138 bedoelde goederenleveringen uit hoofde waarvan de belasting in de loop van dit belastingtijdvak verschuldigd is geworden;

b)

het totale bedrag, de BTW niet inbegrepen, van de in artikel 33 en artikel 36, eerste alinea, bedoelde goederenleveringen die binnen het grondgebied van een andere lidstaat zijn verricht en uit hoofde waarvan de belasting in de loop van dit belastingtijdvak verschuldigd is geworden, indien de plaats van vertrek van de verzending of het vervoer van de goederen is gelegen in de lidstaat waar de aangifte moet worden ingediend;

c)

het totale bedrag, de BTW niet inbegrepen, van de intracommunautaire verwervingen van goederen en van de krachtens de artikelen 21 en 22 bedoelde daarmee gelijkgestelde handelingen, verricht in de lidstaat waar de aangifte moet worden ingediend, en uit hoofde waarvan de belasting in de loop van dit belastingtijdvak verschuldigd is geworden;

d)

het totale bedrag, de BTW niet inbegrepen, van de in artikel 33 en artikel 36, eerste alinea, bedoelde

###### Art. 248
De lidstaten kunnen onder door hen gestelde voorwaarden voorzien in een bewaringsplicht voor door niet–belastingplichtigen ontvangen facturen.


Publicatieblad van de Europese Unie

NL

goederenleveringen die zijn verricht in de lidstaat waar de aangifte moet worden ingediend, en uit hoofde waarvan de belasting in de loop van dit belastingtijdvak verschuldigd is geworden, wanneer de plaats van vertrek van de verzending of het vervoer van de goederen op het grondgebied van een andere lidstaat is gelegen;
e)

het totale bedrag, de BTW niet inbegrepen, van de goederenleveringen, verricht in de lidstaat waar de aangifte moet worden ingediend, waarvoor de belastingplichtige overeenkomstig artikel 197 als de tot voldoening van de belasting gehouden persoon is aangewezen en uit hoofde waarvan de belasting in de loop van dit belastingtijdvak verschuldigd is geworden.
###### Art. 252

1. De BTW-aangifte moet worden ingediend binnen een door de lidstaten vast te stellen termijn. Deze termijn mag niet langer zijn dan twee maanden na het verstrijken van ieder belastingtijdvak.
2. Het belastingtijdvak wordt door de lidstaten vastgesteld op een, twee of drie maanden.
De lidstaten kunnen evenwel andere belastingtijdvakken bepalen, die echter niet langer dan een jaar mogen zijn.
###### Art. 253
Zweden mag voor kleine en middelgrote ondernemingen een vereenvoudigde procedure toepassen, waarbij de indiening van de BTW-aangifte kan geschieden drie maanden na het verstrijken van het directe-belastingjaar voor belastingplichtigen die uitsluitend binnenlandse belastbare handelingen verrichten.
###### Art. 254
Voor leveringen van nieuwe vervoermiddelen onder de in artikel 138, lid 2, onder a), gestelde voorwaarden door een voor BTW–doeleinden geïdentificeerde belastingplichtige aan een niet voor BTW-doeleinden geïdentificeerde afnemer, of door een in artikel 9, lid 2, bedoelde belastingplichtige, treffen de lidstaten de nodige maatregelen opdat de verkoper alle gegevens verschaft die noodzakelijk zijn voor de toepassing van de BTW en voor de controle daarop door de belastingdienst.

L 347/47

zijn gehouden, de in dit hoofdstuk vastgestelde verplichtingen inzake aangifte nakomen.
###### Art. 257
De lidstaten treffen de nodige maatregelen opdat niet-belastingplichtige rechtspersonen die zijn gehouden tot voldoening van de belasting welke verschuldigd is uit hoofde van de in artikel 2, lid 1, onder b), punt i), bedoelde intracommunautaire verwervingen van goederen, voldoen aan de in dit hoofdstuk vastgestelde verplichtingen inzake aangifte.
###### Art. 258
De lidstaten stellen nadere regels vast met betrekking tot de aangifte ter zake van de in artikel 2, lid 1, onder b), punt ii), bedoelde intracommunautaire verwervingen van nieuwe vervoermiddelen en de in artikel 2, lid 1, onder b), punt iii), bedoelde intracommunautaire verwervingen van accijnsproducten.
###### Art. 259
De lidstaten kunnen verlangen dat personen die de in artikel 2, lid 1, onder b), punt ii), bedoelde intracommunautaire verwervingen van nieuwe vervoermiddelen verrichten, bij het indienen van de BTW-aangifte alle gegevens verstrekken die noodzakelijk zijn voor de toepassing van de BTW en voor de controle daarop door de belastingdienst.
###### Art. 260
De lidstaten stellen nadere regels vast betreffende de aangifte ter zake van de invoer van goederen.
###### Art. 261
1. De lidstaten kunnen verlangen dat de belastingplichtige een aangifte indient betreffende alle in het voorgaande jaar verrichte handelingen met daarin alle in de artikelen 250 en 251 bedoelde gegevens. In die aangifte moeten tevens alle gegevens staan die nodig zijn voor eventuele herzieningen.
2. De lidstaten staan onder door hen te stellen voorwaarden toe dat de in lid 1 bedoelde aangifte langs elektronische weg worden ingediend en mogen dit ook verplicht stellen.
#### HOOFDSTUK 6

###### Art. 255

Lijsten

De lidstaten die overeenkomstig artikel 198, lid 1, de afnemer van beleggingsgoud als de tot voldoening van de belasting gehouden persoon aanwijzen of gebruik maken van de in artikel 198, lid 2, geboden mogelijkheid om de afnemer van goud, halffabrikaten of beleggingsgoud als omschreven in artikel 344, lid 1, als de tot voldoening van de belasting gehouden persoon aan te wijzen, treffen de nodige maatregelen opdat die afnemer de in deze afdeling vastgestelde verplichtingen inzake aangifte nakomt.

###### Art. 262
Iedere voor BTW-doeleinden geïdentificeerde belastingplichtige moet een lijst indienen van de voor BTW-doeleinden geïdentificeerde afnemers aan wie hij goederen heeft geleverd onder de in artikel 138, lid 1, en lid 2, onder c), gestelde voorwaarden, alsmede van de voor BTW-doeleinden geïdentificeerde personen voor wie de goederen waarop de in artikel 42 bedoelde intracommunautaire verwervingen betrekking hebben, bestemd zijn.

###### Art. 256
De lidstaten treffen de nodige maatregelen opdat de personen die overeenkomstig de artikelen 194 tot en met 197 en artikel 204 worden geacht in plaats van een niet op hun grondgebied gevestigde belastingplichtige tot voldoening van de belasting te

###### Art. 263
1. De lijst wordt voor elk kalenderkwartaal opgesteld, binnen een termijn en volgens regels die door de lidstaten worden vastgesteld.

L 347/48

Publicatieblad van de Europese Unie

NL

is, in de lidstaat van aankomst van de verzending of het vervoer van de goederen is geïdentificeerd;

De lidstaten kunnen evenwel bepalen dat de lijsten maandelijks worden ingediend.
2. De lidstaten staan onder door hen te stellen voorwaarden toe dat de in lid 1 bedoelde lijsten langs elektronische weg worden ingediend en mogen dit ook verplicht stellen.

c)

###### Art. 264
1. Op de lijst worden de volgende gegevens vermeld:
a)

b)

c)

het nummer waaronder de belastingplichtige voor BTWdoeleinden is geïdentificeerd in de lidstaat waar de lijst moet worden ingediend, en waaronder hij goederenleveringen heeft verricht onder de in artikel 138, lid 1, gestelde voorwaarden; het nummer waaronder elke afnemer voor BTW-doeleinden is geïdentificeerd in een andere lidstaat dan die waar de lijst moet worden ingediend, en waaronder de goederen aan hem geleverd zijn; het nummer waaronder de belastingplichtige voor BTWdoeleinden is geïdentificeerd in de lidstaat waar de lijst moet worden ingediend, en waaronder hij de in artikel 138, lid 2, onder c), bedoelde overbrenging naar een andere lidstaat heeft verricht, alsmede het nummer waaronder hij in de lidstaat van aankomst van de verzending of het vervoer is geïdentificeerd;

d)

voor elke afnemer het totale bedrag van de door de belastingplichtige verrichte goederenleveringen;

e)

voor de in artikel 138, lid 2, onder c) bedoelde leveringen bestaande uit de overbrenging van goederen naar een andere lidstaat, het totale bedrag van deze leveringen, vastgesteld overeenkomstig artikel 76;

f)

het bedrag van de krachtens artikel 90 verrichte herzieningen.


voor elk van degenen voor wie de daaropvolgende levering bestemd is, het totale bedrag, de BTW niet inbegrepen, van de door de belastingplichtige in de lidstaat van aankomst van de verzending of het vervoer van de goederen verrichte leveringen.

2. Het in lid 1, punt c), bedoelde bedrag wordt opgegeven voor het kalenderkwartaal waarin de belasting verschuldigd is geworden.
###### Art. 266
In afwijking van de artikelen 264 en 265 kunnen de lidstaten bepalen dat de lijsten meer gegevens bevatten.
###### Art. 267
De lidstaten treffen de nodige maatregelen opdat de personen die overeenkomstig de artikelen 194 en 204, worden geacht in plaats van een niet op hun grondgebied gevestigde belastingplichtige tot voldoening van de belasting te zijn gehouden, de in dit hoofdstuk vastgestelde verplichting inzake de indiening van lijsten nakomen.
###### Art. 268
De lidstaten kunnen verlangen dat belastingplichtigen die op hun grondgebied intracommunautaire verwervingen van goederen of de krachtens de artikelen 21 en 22 daarmee gelijkgestelde handelingen verrichten, gespecificeerde aangiften over deze verwervingen indienen, met dien verstande dat dergelijke aangiften niet voor tijdvakken van minder dan een maand mogen worden verlangd.
###### Art. 269

2. Het in lid 1, punt d), bedoelde bedrag wordt opgegeven voor het kalenderkwartaal waarin de belasting verschuldigd is geworden.
Het in lid 1, punt f), bedoelde bedrag wordt opgegeven voor het kalenderkwartaal waarin van de herziening kennis is gegeven aan de afnemer.
###### Art. 265
1. In de in artikel 43 bedoelde gevallen van intracommunautaire verwerving van goederen dient de belastingplichtige die voor BTW-doeleinden is geïdentificeerd in de lidstaat welke het BTW-nummer heeft toegekend waaronder de belastingplichtige deze verwervingen heeft verricht, duidelijk de volgende gegevens op de lijst te vermelden:
a)

het nummer waaronder hij voor BTW-doeleinden in die lidstaat is geïdentificeerd en waaronder hij de verwerving en de daaropvolgende goederenlevering heeft verricht;

b)

het nummer waaronder degene voor wie de daaropvolgende levering, verricht door de belastingplichtige, bestemd

De Raad kan op voorstel van de Commissie met eenparigheid van stemmen elke lidstaat machtigen de in de artikelen 270 en 271 bepaalde bijzondere maatregelen in te voeren om de in dit hoofdstuk vastgestelde verplichtingen inzake de indiening van lijsten te vereenvoudigen. Deze maatregelen mogen de betrouwbaarheid van de controle op de intracommunautaire handelingen niet verminderen.
###### Art. 270
Uit hoofde van de in artikel 269 bedoelde machtiging kunnen de lidstaten de belastingplichtigen toestaan een lijst over een periode van een jaar in te dienen waarin voor elke afnemer aan wie de belastingplichtige onder de in artikel 138, lid 1 en lid 2, onder c), gestelde voorwaarden goederen heeft geleverd het nummer wordt vermeld waaronder deze in een andere lidstaat voor BTWdoeleinden is geïdentificeerd, wanneer de belastingplichtige aan de volgende drie voorwaarden voldoet:
a)

het jaarlijkse totale bedrag, de BTW niet inbegrepen, van de door hem verrichte goederenleveringen en diensten overschrijdt met niet meer dan EUR 35 000 of de tegenwaarde daarvan in de nationale munteenheid het bedrag van de jaarlijkse omzet die als maatstaf dient voor de toepassing van de in de artikelen 282 tot en met 292 vervatte vrijstellingsregeling voor kleine ondernemingen;

b)

c)

Publicatieblad van de Europese Unie

NL

het jaarlijkse totale bedrag, de BTW niet inbegrepen, van de goederenleveringen die hij verricht onder de in artikel 138 gestelde voorwaarden bedraagt niet meer dan EUR 15 000 of de tegenwaarde daarvan in de nationale munteenheid; de goederenleveringen die hij verricht onder de in artikel 138 gestelde voorwaarden zijn geen leveringen van nieuwe vervoermiddelen.
###### Art. 271

Uit hoofde van de in artikel 269 bedoelde machtiging kunnen de lidstaten die de duur van het belastingtijdvak waarover een belastingplichtige de in artikel 250 bedoelde BTW-aangifte moet indienen, op meer dan drie maanden vaststellen, deze belastingplichtige toestaan de lijst over datzelfde tijdvak in te dienen, wanneer de belastingplichtige de volgende drie voorwaarden vervult:

L 347/49

artikelen 220 tot en met 236 en de artikelen 238, 239 en 240 vastgestelde verplichtingen inzake facturering.
2. Wanneer de lidstaten van de in lid 1, eerste alinea, punt e), bedoelde mogelijkheid gebruikmaken, nemen zij de nodige maatregelen voor een juiste toepassing van de overgangsregeling voor de belastingheffing op intracommunautaire handelingen.
3. De lidstaten kunnen andere dan de in lid 1 bedoelde belastingplichtigen ontheffing verlenen van bepaalde van de in artikel 242 bedoelde boekhoudkundige verplichtingen.
###### Art. 273

a)

het jaarlijkse totale bedrag, de BTW niet inbegrepen, van de door hem verrichte goederenleveringen en diensten bedraagt niet meer dan EUR 200 000 of de tegenwaarde daarvan in de nationale munteenheid;

De lidstaten kunnen, onder voorbehoud van gelijke behandeling van door belastingplichtigen verrichte binnenlandse handelingen en handelingen tussen de lidstaten, andere verplichtingen voorschrijven die zij noodzakelijk achten ter waarborging van de juiste inning van de BTW en ter voorkoming van fraude, mits deze verplichtingen in het handelsverkeer tussen de lidstaten geen aanleiding geven tot formaliteiten in verband met een grensoverschrijding.

b)

het jaarlijkse totale bedrag, de BTW niet inbegrepen, van de goederenleveringen die hij verricht onder de in artikel 138 gestelde voorwaarden bedraagt niet meer dan EUR 15 000 of de tegenwaarde daarvan in de nationale munteenheid;

De in de eerste alinea geboden mogelijkheid mag niet worden benut voor het opleggen van extra verplichtingen naast de in hoofdstuk 3 vastgestelde verplichtingen inzake facturering.

c)

de goederenleveringen die hij verricht onder de in artikel 138 gestelde voorwaarden zijn geen leveringen van nieuwe vervoermiddelen.

#### HOOFDSTUK 8

Verplichtingen ter zake van bepaalde invoer- en uitvoerhandelingen

#### HOOFDSTUK 7

Diverse bepalingen


##### Afdeling 1
###### Art. 272

Invoerhandelingen

1. De lidstaten kunnen de volgende belastingplichtigen van bepaalde verplichtingen of van alle verplichtingen bedoeld in de hoofdstukken 2 tot en met 6 ontheffen:

###### Art. 274

a)

de belastingplichtigen wier intracommunautaire verwervingen overeenkomstig artikel 3, lid 1, niet aan de BTW zijn onderworpen;

b)

de belastingplichtigen die geen van de in de artikelen 20,
21, 22, 33, 36, 138 en 141 bedoelde handelingen verrichten;

c)

de belastingplichtigen die slechts goederenleveringen of diensten verrichten die uit hoofde van de artikelen 132, 135 en 136, de artikelen 146 tot en met 149 en de artikelen 151, 152 en 153 zijn vrijgesteld;

d)

de belastingplichtigen die in aanmerking komen voor de in de artikelen 282 tot en met 292 vervatte vrijstellingsregeling voor kleine ondernemingen;

e)

de belastingplichtigen die voor de forfaitaire regeling voor landbouwproducenten in aanmerking komen.

De lidstaten mogen de in de eerste alinea, punt b), bedoelde belastingplichtigen geen ontheffing verlenen van de in de

De artikelen 275, 276 en 277 zijn van toepassing op invoerhandelingen die betrekking hebben op goederen in het vrije verkeer welke de Gemeenschap worden binnengebracht vanuit een derdelandsgebied dat deel uitmaakt van het douanegebied van de Gemeenschap.
###### Art. 275
De formaliteiten betreffende de invoer van de in artikel 274 bedoelde goederen zijn dezelfde als die welke zijn bepaald in de geldende communautaire douanebepalingen betreffende de invoer van goederen in het douanegebied van de Gemeenschap.
###### Art. 276
Wanneer de plaats van aankomst van de verzending of van het vervoer van de in artikel 274 bedoelde goederen buiten de lidstaat van binnenkomst van die goederen in de Gemeenschap is gelegen, bevinden zij zich in de Gemeenschap in het verkeer onder de regeling voor intern communautair douanevervoer van de geldende communautaire douanebepalingen, indien op het moment van het binnenbrengen van de goederen in de Gemeenschap aangifte is gedaan dat zij onder die regeling zijn geplaatst.

L 347/50

Publicatieblad van de Europese Unie

NL


###### Art. 277


Wanneer de in artikel 274 bedoelde goederen zich op het moment van het binnenbrengen ervan in de Gemeenschap bevinden in een van de situaties waardoor zij, indien zij ingevoerd waren in de zin van artikel 30, eerste alinea, in aanmerking konden komen voor een van de in artikel 156 bedoelde regelingen of situaties of voor een regeling van tijdelijke invoer met volledige vrijstelling van invoerrechten, nemen de lidstaten de maatregelen om ervoor te zorgen dat deze goederen onder dezelfde voorwaarden in de Gemeenschap kunnen verblijven als die welke voor de toepassing van die regelingen of situaties gelden.

Vr i j s t e l l i n g e n o f d e g r e s s i e ve ver minderingen

##### Afdeling 2
Uitvoerhandelingen

##### Afdeling 2
###### Art. 282
De in deze afdeling vastgestelde vrijstellingen en verminderingen zijn van toepassing op door kleine ondernemingen verrichte goederenleveringen en diensten.
###### Art. 283
1. De volgende handelingen zijn van de in deze afdeling vastgestelde regeling uitgesloten:
a)

de in artikel 12 bedoelde incidenteel verrichte handelingen;

b)

de leveringen van nieuwe vervoermiddelen verricht onder de in artikel 138, lid 1, en lid 2, onder a), gestelde voorwaarden;

c)

de goederenleveringen en de diensten die worden verricht door een belastingplichtige die niet is gevestigd in de lidstaat waar de BTW verschuldigd is.

###### Art. 278
De artikelen 279 en 280 zijn van toepassing op de uitvoerhandelingen met betrekking tot goederen in het vrije verkeer die vanuit een lidstaat worden verzonden of vervoerd naar een derdelandsgebied dat deel uitmaakt van het douanegebied van de Gemeenschap.
###### Art. 279
De formaliteiten betreffende de uitvoer van de in artikel 278 bedoelde goederen uit het douanegebied van de Gemeenschap zijn dezelfde als die welke zijn voorgeschreven in de geldende communautaire douanebepalingen betreffende de uitvoer van goederen uit het douanegebied van de Gemeenschap.

2. De lidstaten kunnen andere dan de in lid 1 bedoelde handelingen van de in deze afdeling vastgestelde regeling uitsluiten.

###### Art. 280

1. De lidstaten die gebruik hebben gemaakt van de in artikel 14 van Richtlijn 67/228/EEG van de Raad van 11 april 1967 betreffende de harmonisatie van de wetgevingen der lidstaten inzake omzetbelasting — Structuur en wijze van toepassing van het gemeenschappelijk stelsel van belasting over de toegevoegde waarde (1) gegeven mogelijkheid vrijstellingen of degressieve verminderingen van de belasting in te voeren, mogen deze alsmede de desbetreffende uitvoeringsbepalingen handhaven, indien zij met het BTW-stelsel in overeenstemming zijn.

Voor goederen die tijdelijk uit de Gemeenschap worden uitgevoerd met het oog op wederinvoer, nemen de lidstaten de nodige maatregelen om ervoor te zorgen dat die goederen bij hun wederinvoer in de Gemeenschap in aanmerking komen voor dezelfde bepalingen als wanneer zij tijdelijk uit het douanegebied van de Gemeenschap waren uitgevoerd.

###### Art. 284

### TITEL XII
BIJZONDERE REGELINGEN
#### HOOFDSTUK 1

2. De lidstaten die op 17 mei 1977 een vrijstelling van belasting toekenden aan belastingplichtigen met een jaaromzet die minder bedroeg dan de tegenwaarde van 5 000 Europese rekeneenheden in de nationale munteenheid tegen de omrekeningskoers geldend op die datum, mogen die vrijstelling verhogen tot EUR 5 000.

Bijzondere regeling voor kleine ondernemingen
Ve r e e n v o u d i g d e b e p a l i n g e n i n z a k e belastingheff ing en belastinginning

De lidstaten die degressieve verminderingen van de belasting toepasten, mogen noch de bovengrens van die verminderingen verhogen, noch de voorwaarden voor de toekenning daarvan gunstiger maken.

##### Afdeling 1
###### Art. 281

###### Art. 285

Lidstaten die moeilijkheden zouden kunnen ondervinden bij het toepassen van de normale BTW-regeling op kleine ondernemingen, wegens de activiteit of de structuur van die ondernemingen, kunnen binnen de grenzen en onder de voorwaarden die zij stellen, na raadpleging van het BTW-Comité vereenvoudigde regels inzake belastingheffing en belastinginning, zoals forfaitaire regelingen, toepassen, mits dit niet leidt tot een vermindering van de belasting.

De lidstaten die geen gebruik hebben gemaakt van de in artikel 14 van Richtlijn 67/228/EEG gegeven mogelijkheid, mogen vrijstelling van belasting toekennen aan belastingplichtigen met een jaaromzet welke ten hoogste gelijk is aan EUR 5 000 of de tegenwaarde van dit bedrag in de nationale munteenheid.
(1) PB L 71 van 14.4.1967, blz. 1303/67. Richtlijn ingetrokken bij
Richtlijn 77/388/EEG.


Publicatieblad van de Europese Unie

NL

De in de eerste alinea bedoelde lidstaten kunnen een degressieve belastingvermindering toekennen aan belastingplichtigen wier jaaromzet het plafond overschrijdt dat deze lidstaten voor de toepassing van de vrijstelling hebben vastgesteld.

L 347/51
###### Art. 288

De omzet die als maatstaf dient voor de toepassing van de in deze afdeling vastgestelde regeling, wordt gevormd door de volgende bedragen, de BTW niet inbegrepen:

###### Art. 286
De lidstaten die op 17 mei 1977 een vrijstelling van belasting toekenden aan belastingplichtigen met een jaaromzet gelijk aan of hoger dan de tegenwaarde van 5 000 Europese rekeneenheden in de nationale munteenheid tegen de op die datum geldende omrekeningskoers, mogen deze vrijstelling verhogen teneinde de reële waarde ervan te handhaven.

1)

het bedrag van de goederenleveringen en de diensten, voor zover deze belast zijn;

2)

het bedrag van de handelingen die krachtens de artikelen 110 en 111, artikel 125, lid 1, artikel 127 en artikel 128, lid 1, zijn vrijgesteld met recht op aftrek van voorbelasting;

3)

het bedrag van de krachtens de artikelen 146 tot en met
149 en de artikelen 151, 152 en 153 vrijgestelde handelingen;

4)

het bedrag van handelingen met betrekking tot onroerende goederen, financiële handelingen als bedoeld in artikel 135, lid 1, punten b) tot en met g), en verzekeringsdiensten, tenzij die handelingen met ander handelingen samenhangende handelingen zijn.

###### Art. 287
De lidstaten die na 1 januari 1978 zijn toegetreden, kunnen een vrijstelling van belasting toekennen aan belastingplichtigen met een jaarlijkse omzet die ten hoogste gelijk is aan de tegenwaarde in de nationale munteenheid van de volgende bedragen tegen de op de dag van hun toetreding geldende omrekeningskoers: 1)

Griekenland: 10 000 Europese rekeneenheden;

2)

Spanje: 10 000 ecu;

3)

Portugal: 10 000 ecu;

4)

Oostenrijk: 35 000 ecu;

5)

Finland: 10 000 ecu;

6)

Zweden: 10 000 ecu;

7)

Tsjechië: EUR 35 000;

De belastingplichtigen voor wie vrijstelling van belasting geldt, hebben geen recht op aftrek van BTW overeenkomstig de artikelen 167 tot en met 171 en de artikelen 173 tot en met 177 en mogen de BTW evenmin op hun facturen vermelden.

8)

Estland: EUR 16 000;

###### Art. 290

9)

Cyprus: EUR 15 600;

11) Litouwen: EUR 29 000;

De belastingplichtigen die in aanmerking kunnen komen voor vrijstelling van belasting, kunnen kiezen hetzij voor toepassing van de normale BTW-regeling, hetzij voor toepassing van de in artikel 281 bedoelde vereenvoudigde regelingen. In dit geval gelden voor hen de degressieve belastingverminderingen waarin de nationale wetgeving voorziet.

12) Hongarije: EUR 35 000;

###### Art. 291

10) Letland: EUR 17 200;

13) Malta: EUR 37 000 wanneer de economische activiteit voornamelijk bestaat uit goederenleveringen, EUR 24 300 wanneer de economische activiteit voornamelijk bestaat uit diensten met een lage toegevoegde waarde (hoge inputs), en EUR 14 600 in andere gevallen, namelijk diensten met een hoge toegevoegde waarde (lage inputs);

De overdracht van lichamelijke of onlichamelijke investeringsgoederen van de onderneming wordt evenwel niet in aanmerking genomen voor de vaststelling van de omzet.
###### Art. 289

De belastingplichtigen voor wie degressieve belastingvermindering geldt, worden, behoudens de toepassing van artikel 281, beschouwd als belastingplichtigen vallende onder de normale BTW-regeling.
###### Art. 292

14) Polen: EUR 10 000;
15) Slovenië: EUR 25 000;
16) Slowakije: EUR 35 000.

De in deze afdeling vastgestelde regeling is van toepassing tot een datum die door de Raad overeenkomstig artikel 93 van het Verdrag wordt vastgesteld en die niet later mag vallen dan het tijdstip van inwerkingtreding van de in artikel 402 bedoelde definitieve regeling.

L 347/52

Publicatieblad van de Europese Unie

NL

de forfaitaire regeling vallende landbouw-, bosbouw- en visserijbedrijven gezamenlijk van elke lidstaat, voor zover deze belasting door een landbouwproducent die onder de normale BTW-regeling valt, overeenkomstig de artikelen 167, 168 en 169 en de artikelen 173 tot en met 177 zou kunnen worden afgetrokken;

Ve r s l a g e n h e r z i e n i n g
##### Afdeling 3
###### Art. 293
De Commissie brengt aan de Raad, op grond van de van de lidstaten verkregen gegevens, vanaf de aanneming van deze richtlijn om de vier jaar verslag uit over de toepassing van dit hoofdstuk, indien nodig en rekening houdend met de noodzaak van uiteindelijke convergentie van de nationale regelingen, vergezeld van voorstellen betreffende de volgende punten: 1)

7)

forfaitaire compensatiepercentages: de percentages die de lidstaten overeenkomstig in de artikelen 297, 298 en 299 vaststellen en die zij toepassen in de in artikel 300 bedoelde gevallen teneinde de forfaitair belaste landbouwers in aanmerking te doen komen voor een forfaitaire compensatie voor de BTW-voordruk;

8)

forfaitaire compensatie: het bedrag dat voortvloeit uit de toepassing van het forfaitaire compensatiepercentage op de omzet van de forfaitair belaste landbouwer in de in artikel 300 bedoelde gevallen.

de in de bijzondere regeling voor kleine ondernemingen aan te brengen verbeteringen;

2)

de aanpassing van de nationale regelingen inzake vrijstellingen en degressieve belastingverminderingen;

3)

de aanpassing van de in afdeling 2 bedoelde maximumbedragen.
###### Art. 294

De Raad bepaalt overeenkomstig artikel 93 van het Verdrag of in het kader van de definitieve regeling een bijzondere regeling voor kleine ondernemingen nodig is, en neemt, in voorkomend geval, tevens een beslissing over de gemeenschappelijke grenzen en toepassingsvoorwaarden van de genoemde bijzondere regeling.
#### HOOFDSTUK 2

Gemeenschappelijke forfaitaire regeling voor landbouwproducenten
###### Art. 295
1. Voor de toepassing van dit hoofdstuk wordt verstaan onder:
1)

landbouwproducent: de belastingplichtige die zijn werkzaamheid uitoefent in het kader van een landbouw-, bosbouw- of visserijbedrijf;

2)

landbouw-, bosbouw- of visserijbedrijf: de bedrijven die door elke lidstaat als zodanig worden beschouwd in het kader van de in bijlage VI vermelde productiewerkzaamheden;

3)

forfaitair belaste landbouwer: de landbouwproducent op wie de in dit hoofdstuk vastgestelde forfaitaire regeling van toepassing is;


2. De verwerking door een landbouwproducent van de in hoofdzaak uit zijn landbouwproductie afkomstige producten, verricht met behulp van de middelen die normaal in de landbouw-, bosbouw- of visserijbedrijven worden gebezigd, wordt gelijkgesteld met de in bijlage VII genoemde landbouwproductiewerkzaamheden.
###### Art. 296
1. De lidstaten kunnen ten aanzien van landbouwproducenten voor wie de toepassing van de normale BTW-regeling of, in voorkomend geval, van de bijzondere regeling van hoofdstuk 1, op moeilijkheden zou stuiten, overeenkomstig het bepaalde in dit hoofdstuk een forfaitaire regeling toepassen ter compensatie van de BTW die is betaald over de aankopen van goederen en diensten van de forfaitair belaste landbouwers.
2. Iedere lidstaat kan bepaalde categorieën landbouwproducenten, alsmede landbouwproducenten voor wie de toepassing van de normale BTW-regeling of, in voorkomend geval, van de in artikel 281 bedoelde vereenvoudigde regels geen administratieve moeilijkheden oplevert, van de forfaitaire regeling uitsluiten.
3. Iedere forfaitair belaste landbouwer heeft het recht te kiezen voor toepassing van de normale BTW-regeling of, in voorkomend geval, van de in artikel 281 bedoelde vereenvoudigde regels, met inachtneming van de door elke lidstaat gestelde nadere regels en voorwaarden.
###### Art. 297

4)

landbouwproducten: de goederen die door de landbouw-, bosbouw- of visserijbedrijven van elke lidstaat worden voortgebracht door middel van de in bijlage VI vermelde werkzaamheden;

De lidstaten stellen, voorzover nodig, forfaitaire compensatiepercentages vast. Zij kunnen gedifferentieerde forfaitaire compensatiepercentages vaststellen voor de bosbouw, de verschillende deelsectoren van de landbouw en de visserij.

5)

agrarische diensten: de diensten, met name de in bijlage VIII genoemde, die worden verricht door een landbouwproducent met gebruikmaking van zijn arbeidskrachten of de normale uitrusting van zijn landbouw-, bosbouw- of visserijbedrijf en die normaliter tot de verwezenlijking van de landbouwproductie bijdragen;

De lidstaten brengen de uit hoofde van de eerste alinea vastgestelde forfaitaire compensatiepercentages, voordat zij worden toegepast, ter kennis van de Commissie.

6)

BTW-voordruk: de totale druk aan BTW die rust op de goederen en diensten welke zijn aangekocht door alle onder

###### Art. 298
De forfaitaire compensatiepercentages worden bepaald aan de hand van de macro-economische gegevens over de laatste drie jaar betreffende uitsluitend de forfaitair belaste landbouwers.


Publicatieblad van de Europese Unie

NL

De percentages mogen naar boven of naar beneden op een half punt worden afgerond. De lidstaten kunnen deze percentages ook tot nihil terugbrengen.
###### Art. 299

2. De lidstaten kennen aan de afnemer terugbetaling toe van het bedrag aan forfaitaire compensatie dat hij uit hoofde van een van de volgende handelingen heeft betaald:
a)

de landbouwproductenleveringen die onder de in artikel 138 gestelde voorwaarden worden verricht voor een belastingplichtige afnemer, of een niet-belastingplichtige rechtspersoon, die als zodanig handelt in een andere lidstaat binnen het grondgebied waarvan zijn intracommunautaire verwervingen van goederen overeenkomstig artikel 2, lid 1, onder b), aan de BTW zijn onderworpen;

b)

de landbouwproductenleveringen die onder de in de artikelen 146, 147, 148 en 156, artikel 157, lid 1, onder b), en de artikelen 158, 160 en 161 gestelde voorwaarden worden verricht voor een belastingplichtige afnemer die buiten de Gemeenschap is gevestigd, voor zover deze landbouwproducten door de afnemer worden gebruikt ten behoeve van zijn in artikel 169, punten a) en b), bedoelde handelingen of zijn diensten die worden geacht te worden verricht binnen het grondgebied van de lidstaat waar de afnemer is gevestigd, en waarvoor de belasting overeenkomstig artikel 196 alleen door de afnemer verschuldigd is;

c)

de agrarische diensten die worden verricht voor een binnen de Gemeenschap maar in een andere lidstaat gevestigde belastingplichtige afnemer of voor een buiten de Gemeenschap gevestigde belastingplichtige afnemer, voor zover deze diensten door de afnemer worden gebruikt ten behoeve van zijn in artikel 169, punten a) en b), bedoelde handelingen of van zijn diensten die worden geacht te worden verricht binnen het grondgebied van de lidstaat waar de afnemer is gevestigd, en waarvoor de belasting overeenkomstig artikel 196 alleen door de afnemer verschuldigd is.

De forfaitaire compensatiepercentages mogen niet tot gevolg hebben dat aan de forfaitair belaste landbouwers gezamenlijk bedragen worden terugbetaald die hoger zijn dan de BTWvoordruk.
###### Art. 300
De forfaitaire compensatiepercentages worden toegepast op de prijs, de BTW niet inbegrepen, van de volgende goederen en diensten: 1)

de landbouwproducten die de forfaitair belaste landbouwers hebben geleverd aan andere belastingplichtigen dan die welke in de lidstaat waar deze leveringen zijn verricht onder deze forfaitaire regeling vallen;

2)

de landbouwproducten die de forfaitair belaste landbouwers onder de in artikel 138 gestelde voorwaarden hebben geleverd aan niet–belastingplichtige rechtspersonen wier intracommunautaire verwervingen overeenkomstig artikel 2, lid 1, onder b), aan de BTW zijn onderworpen in de lidstaat van aankomst van de verzending of het vervoer van de aldus geleverde landbouwproducten;

3)

de agrarische diensten die worden verricht door forfaitair belaste landbouwers voor andere belastingplichtigen dan die welke in de lidstaat waar deze diensten zijn verricht onder deze forfaitaire regeling vallen.
###### Art. 301

1. Voor de in artikel 300 bedoelde landbouwproductenleveringen en agrarische diensten bepalen de lidstaten dat de forfaitaire compensaties hetzij door de afnemer hetzij door de overheid worden betaald.
2. Voor andere dan de in artikel 300 bedoelde landbouwproductenleveringen en agrarische diensten worden de forfaitaire compensaties geacht betaald te worden door de afnemer.
###### Art. 302
Wanneer een forfaitair belaste landbouwer een forfaitaire compensatie geniet, heeft hij voor de onder deze forfaitaire regeling vallende werkzaamheden geen recht op aftrek.
###### Art. 303
1. De belastingplichtige afnemer die overeenkomstig artikel 301, lid 1, een forfaitaire compensatie betaalt, heeft het recht, onder de in de artikelen 167, 168 en 169 en de artikelen 173 tot en met 177 gestelde voorwaarden en volgens de door de lidstaten vastgestelde nadere regels, het bedrag van deze compensatie af te trekken van de BTW die hij verschuldigd is in de lidstaat waar hij zijn belaste handelingen verricht.

L 347/53

3. De lidstaten stellen de nadere regels voor de in lid 2 bedoelde terugbetalingen vast. Zij kunnen met name de Richtlijnen 79/1072/EEG en 86/560/EEG toepassen.
###### Art. 304
De lidstaten nemen alle nodige maatregelen om de uitbetaling van de forfaitaire compensaties aan de forfaitair belaste landbouwers doeltreffend te kunnen controleren.
###### Art. 305
Wanneer de lidstaten deze forfaitaire regeling toepassen, treffen zij alle nodige maatregelen om ervoor te zorgen dat leveringen van landbouwproducten tussen lidstaten, verricht onder de in artikel 33 bedoelde voorwaarden, ongeacht of zij worden verricht door een forfaitair belaste landbouwer of door een andere belastingplichtige, op identieke wijze worden belast.
#### HOOFDSTUK 3

Bijzondere regeling voor reisbureaus
###### Art. 306
1. De lidstaten passen overeenkomstig het bepaalde in dit hoofdstuk een bijzondere regeling voor de BTW op de handelingen van reisbureaus toe, voor zover de reisbureaus op eigen naam tegenover de reiziger handelen en zij voor de totstandbrenging van de reizen gebruikmaken van goederenleveringen en diensten van andere belastingplichtigen.

L 347/54

Publicatieblad van de Europese Unie

NL

Deze bijzondere regeling is niet van toepassing op reisbureaus die alleen handelen als tussenpersoon en waarop artikel 79, eerste alinea, punt c), van toepassing is om de maatstaf van heffing te berekenen.

#### HOOFDSTUK 4

Bijzondere regelingen voor gebruikte goederen, kunstvoorwerpen, voorwerpen voor verzamelingen en antiquiteiten

2. Voor de toepassing van dit hoofdstuk worden reisorganisatoren (tour-operators) als reisbureaus beschouwd.

Definities
##### Afdeling 1
###### Art. 311

###### Art. 307
De onder de voorwaarden van artikel 306 verrichte handelingen van het reisbureau met het oog op de totstandkoming van de reis, worden beschouwd als één enkele dienst die het reisbureau voor de reiziger verricht.

1. Voor de toepassing van dit hoofdstuk, en onverminderd andere communautaire bepalingen, wordt verstaan onder: 1)

„gebruikte goederen”: roerende lichamelijke zaken die in de staat waarin zij verkeren of na herstelling opnieuw kunnen worden gebruikt, andere dan kunstvoorwerpen, voorwerpen voor verzamelingen en antiquiteiten, en andere dan edele metalen of edelstenen als omschreven door de lidstaten;

2)

„kunstvoorwerpen”: de in bijlage IX, deel A, genoemde goederen;

3)

„voorwerpen voor verzamelingen”: de in bijlage IX, deel B, genoemde goederen;

4)

„antiquiteiten”: de in bijlage IX, deel C, genoemde goederen;

5)

„belastingplichtige wederverkoper”: elke belastingplichtige die in het kader van zijn economische activiteit gebruikte goederen, kunstvoorwerpen, voorwerpen voor verzamelingen of antiquiteiten koopt, voor bedrijfsdoeleinden bestemt dan wel invoert met het oog op wederverkoop, ongeacht of deze belastingplichtige handelt voor eigen rekening dan wel, ingevolge een overeenkomst tot aan- of verkoop in commissie, voor rekening van een derde;

6)

„organisator van een openbare veiling”: elke belastingplichtige die in het kader van zijn economische activiteit op een openbare veiling een goed aanbiedt voor overdracht aan de meestbiedende;

7)

„opdrachtgever van een organisator van een openbare veiling”: elke persoon die een goed overdraagt aan een organisator van een openbare veiling ingevolge een overeenkomst tot verkoop in commissie.

Deze ene dienst wordt belast in de lidstaat waar het reisbureau de zetel van zijn bedrijfsuitoefening of een vaste inrichting heeft gevestigd van waaruit het de dienst heeft verricht.

###### Art. 308
Voor de door het reisbureau verrichte ene dienst wordt als maatstaf van heffing en prijs, de BTW niet inbegrepen, in de zin van artikel 226, punt 8), beschouwd de winstmarge van het reisbureau, dat wil zeggen het verschil tussen het totale bedrag, de BTW niet inbegrepen, dat de reiziger moet betalen en de werkelijk door het reisbureau gedragen kosten voor goederenleveringen en diensten van andere belastingplichtigen, mits deze handelingen de reiziger rechtstreeks ten goede komen.

###### Art. 309
Indien de handelingen waarvoor het reisbureau een beroep doet op andere belastingplichtigen, door laatstgenoemden buiten de Gemeenschap worden verricht, wordt de dienst van het reisbureau gelijkgesteld met een krachtens artikel 153 vrijgestelde handeling van een tussenpersoon.

Indien de in de eerste alinea bedoelde handelingen zowel binnen als buiten de Gemeenschap worden verricht, mag alleen het gedeelte van de dienst van het reisbureau betreffende de buiten de Gemeenschap verrichte handelingen als vrijgesteld worden beschouwd.

2. De lidstaten behoeven de in bijlage IX, deel A, punten 5, 6 en
7, genoemde voorwerpen niet als kunstvoorwerpen te beschouwen.

###### Art. 310
De BTW die aan het reisbureau in rekening wordt gebracht door andere belastingplichtigen voor de in artikel 307 bedoelde handelingen welke de reiziger rechtstreeks ten goede komen, mogen in de lidstaten afgetrokken noch teruggegeven worden.

3. De in lid 1, punt 7), bedoelde overeenkomst tot verkoop in commissie moet bepalen dat de organisator het goed in eigen naam, maar voor rekening van zijn opdrachtgever, in openbare veiling brengt en het goed in eigen naam, maar voor rekening van zijn opdrachtgever, overdraagt aan de meestbiedende aan wie het goed tijdens de openbare verkoping wordt gegund.


Publicatieblad van de Europese Unie

NL

wederverkoper overeenkomstig deze bijzondere regeling aan de BTW onderworpen is geweest.

Bijzondere regeling voor belastingplichtige weder verkopers
##### Afdeling 2
##### Onderafdeling 1
Winstmargeregeling

###### Art. 312
Voor de toepassing van deze onderafdeling wordt verstaan onder:
1)

2)

„verkoopprijs”: alles wat de tegenprestatie uitmaakt die een belastingplichtige wederverkoper verkrijgt of moet verkrijgen van de afnemer of een derde, met inbegrip van subsidies die rechtstreeks verband houden met de handeling, belastingen, rechten, heffingen en bijkomende kosten zoals kosten van commissie, verpakking, vervoer en verzekering die de belastingplichtige wederverkoper de afnemer in rekening brengt, echter met uitsluiting van de in artikel 79 bedoelde bedragen;
„aankoopprijs”: alles wat de in punt 1) gedefinieerde tegenprestatie uitmaakt die de leverancier van de belastingplichtige wederverkoper verkrijgt of moet verkrijgen.

L 347/55

###### Art. 315
De maatstaf van heffing voor de in artikel 314 bedoelde goederenleveringen is de winstmarge van de belastingplichtige wederverkoper, verminderd met het bedrag van de BTW die voor de winstmarge zelf geldt.
De winstmarge van de belastingplichtige wederverkoper is gelijk aan het verschil tussen de door de belastingplichtige wederverkoper voor het goed gevraagde verkoopprijs en de aankoopprijs.
###### Art. 316
1. De lidstaten verlenen de belastingplichtige wederverkopers het recht te kiezen voor toepassing van de winstmargeregeling op de leveringen van de volgende goederen:
a)

kunstvoorwerpen, voorwerpen voor verzamelingen en antiquiteiten die zij zelf hebben ingevoerd;

b)

kunstvoorwerpen die aan hen geleverd zijn door de maker of diens rechthebbenden;

c)

kunstvoorwerpen die aan hen geleverd zijn door een andere belastingplichtige dan een belastingplichtige wederverkoper, wanneer die levering aan het verlaagde tarief uit hoofde van artikel 103 onderworpen is.

###### Art. 313
1. De lidstaten passen op door belastingplichtige wederverkopers verrichte leveringen van gebruikte goederen, kunstvoorwerpen, voorwerpen voor verzamelingen en antiquiteiten een bijzondere regeling toe voor de belastingheffing over de winstmarge van de belastingplichtige wederverkoper, overeenkomstig het bepaalde in deze onderafdeling.
2. Tot de invoering van de in artikel 402 bedoelde definitieve regeling is de in lid 1 van dit artikel bedoelde regeling niet van toepassing op leveringen van nieuwe vervoermiddelen die worden verricht onder de in artikel 138, lid 1 en lid 2, onder a), gestelde voorwaarden.
###### Art. 314
De winstmargeregeling is van toepassing op door een belastingplichtige wederverkoper verrichte leveringen van gebruikte goederen, kunstvoorwerpen, voorwerpen voor verzamelingen en antiquiteiten, wanneer deze goederen hem binnen de Gemeenschap door een der onderstaande personen worden geleverd:
a)

een niet-belastingplichtige;

b)

een andere belastingplichtige, voor zover de levering van het goed door deze andere belastingplichtige overeenkomstig artikel 133 is vrijgesteld;

c)

een andere belastingplichtige, voor zover de levering van het goed door deze andere belastingplichtige in aanmerking komt voor de in de artikelen 282 tot en met 292 bedoelde vrijstellingsregeling voor kleine ondernemingen en het gaat om een investeringsgoed;

d)

een andere belastingplichtige wederverkoper, voor zover de levering van het goed door deze andere belastingplichtige

2. De lidstaten stellen nadere regels vast inzake de uitoefening van het in lid 1 gegeven keuzerecht, dat in ieder geval gedurende een periode van ten minste twee kalenderjaren van kracht is.
###### Art. 317
Wanneer een belastingplichtige wederverkoper het in artikel 316 bedoelde keuzerecht uitoefent, wordt de maatstaf van heffing overeenkomstig artikel 315 vastgesteld.
Voor de leveringen van kunstvoorwerpen, voorwerpen voor verzamelingen of antiquiteiten die door de belastingplichtige wederverkoper zelf zijn ingevoerd, is de voor de berekening van de winstmarge in aanmerking te nemen verkoopprijs gelijk aan de overeenkomstig de artikelen 85 tot en met 89 vastgestelde maatstaf van heffing bij invoer, vermeerderd met de bij invoer verschuldigde of betaalde BTW.
###### Art. 318
1. Teneinde de inning van de belasting te vereenvoudigen, kunnen de lidstaten na raadpleging van het BTW-Comité, voor bepaalde handelingen of voor bepaalde categorieën belastingplichtige wederverkopers bepalen dat de maatstaf van heffing voor leveringen van goederen die onderworpen zijn aan de winstmargeregeling, wordt vastgesteld voor ieder belastingtijdvak uit hoofde waarvan de belastingplichtige wederverkoper de in artikel 250 bedoelde BTW-aangifte moet indienen.
In het in de eerste alinea bedoelde geval is de maatstaf van heffing voor goederenleveringen waarop hetzelfde BTW-tarief van toepassing is, de totale winstmarge van de belastingplichtige

L 347/56

Publicatieblad van de Europese Unie

NL

###### Art. 322

wederverkoper, verminderd met het bedrag van de BTW op diezelfde winstmarge.

2. De totale winstmarge is gelijk aan het verschil tussen de volgende twee bedragen:

a)

b)

het totale bedrag van de goederenleveringen die onderworpen zijn aan de winstmargeregeling en die gedurende het belastingtijdvak door de belastingplichtige wederverkoper verricht zijn, dit wil zeggen de som van de verkoopprijzen;

het totale bedrag van de in artikel 314 bedoelde goederenaankopen die gedurende het belastingtijdvak door de belastingplichtige wederverkoper zijn verricht, dit wil zeggen de som van de aankoopprijzen.


Voor zover de goederen worden gebruikt ten behoeve van zijn aan de winstmargeregeling onderworpen leveringen mag de belastingplichtige wederverkoper van de door hem verschuldigde belasting de volgende bedragen niet aftrekken:
a)

de BTW die verschuldigd of voldaan is voor kunstvoorwerpen, voorwerpen voor verzamelingen of antiquiteiten die hij zelf heeft ingevoerd;

b)

de BTW die verschuldigd of voldaan is voor aan hem geleverde of te leveren kunstvoorwerpen door de maker of diens rechthebbenden;

c)

de BTW die verschuldigd of voldaan is voor aan hem geleverde of te leveren kunstvoorwerpen door een andere belastingplichtige dan een belastingplichtige wederverkoper.
###### Art. 323

3. De lidstaten treffen de nodige maatregelen om te voorkomen dat de in lid 1 bedoelde belastingplichtigen ongerechtvaardigde voordelen genieten of ongerechtvaardigde schade lijden.

###### Art. 319
Voor elke levering die onder de winstmargeregeling valt, kan de belastingplichtige wederverkoper de normale BTW–regeling toepassen.

###### Art. 320
1. De belastingplichtige wederverkoper die de normale BTWregeling toepast op de levering van kunstvoorwerpen, voorwerpen voor verzamelingen en antiquiteiten welke hij zelf heeft ingevoerd, heeft het recht de bij invoer van dit goed verschuldigde of voldane BTW af te trekken van het door hem verschuldigde belastingbedrag.

De belastingplichtige mag de BTW die verschuldigd of voldaan is voor aan hem geleverde of te leveren goederen door een belastingplichtige wederverkoper, niet aftrekken van de door hem verschuldigde belasting, voorzover de levering van deze goederen door de belastingsplichtige wederverkoper aan de winstmargeregeling is onderworpen.
###### Art. 324
De belastingplichtige wederverkoper die zowel de normale BTWregeling als de winstmargeregeling toepast, moet de transacties voor elk van deze regelingen afzonderlijk in zijn boekhouding bijhouden, overeenkomstig de door de lidstaten vastgestelde bepalingen.
###### Art. 325
De belastingplichtige wederverkoper mag op de door hem uitgereikte factuur de BTW over de goederenleveringen waarop hij de winstmargeregeling toepast, niet afzonderlijk vermelden.
##### Onderafdeling 2

De belastingplichtige wederverkoper die de normale BTWregeling toepast op de levering van kunstvoorwerpen welke hem door de maker of diens rechthebbenden of door een andere belastingplichtige dan een belastingplichtige wederverkoper zijn geleverd, heeft het recht, de met betrekking tot de hem geleverde kunstvoorwerpen verschuldigde of voldane BTW af te trekken van het door hem verschuldigde belastingbedrag.

2. Het recht op aftrek ontstaat op het tijdstip waarop de belasting verschuldigd wordt voor de levering waarvoor de belastingplichtige wederverkoper voor de normale BTW-regeling kiest.

###### Art. 321

Overgangsregeling voor gebr uikte ver voer middelen

###### Art. 326
De lidstaten die op 31 december 1992 een andere bijzondere belastingregeling toepasten op de levering van gebruikte vervoermiddelen door belastingplichtige wederverkopers dan de winstmargeregeling, kunnen die regeling tot de invoering van de in artikel 402 bedoelde definitieve regeling blijven toepassen, voorzover zij voldoet, of zodanig is aangepast dat zij voldoet, aan de in deze onderafdeling gestelde voorwaarden.
Denemarken mag een bijzondere regeling als bedoeld in de eerste alinea invoeren.
###### Art. 327

De leveringen van gebruikte goederen, kunstvoorwerpen, voorwerpen voor verzamelingen en antiquiteiten die onderworpen zijn aan de winstmargeregeling, zijn vrijgesteld indien zij plaatsvinden onder de in de artikelen 146, 147, 148 en 151 gestelde voorwaarden.

1. Deze overgangsregeling is van toepassing op door belastingplichtige wederverkopers verrichte leveringen van gebruikte vervoermiddelen die aan de winstmargeregeling zijn onderworpen.


Publicatieblad van de Europese Unie

NL

2. Deze overgangsregeling is niet van toepassing op de leveringen van nieuwe vervoermiddelen die worden verricht onder de in artikel 138, lid 1 en lid 2, onder a), gestelde voorwaarden.

###### Art. 332
De belastingplichtige wederverkoper mag op de door hem uitgereikte factuur de BTW over de leveringen waarop hij deze overgangsregeling toepast, niet afzonderlijk vermelden.

3. Voor de toepassing van lid 1 worden als „gebruikte vervoermiddelen” beschouwd de in artikel 2, lid 2, onder a), bedoelde landvoertuigen, schepen en luchtvaartuigen die gebruikte goederen zijn welke niet aan de voorwaarden voldoen om als nieuwe vervoermiddelen te worden beschouwd.

Bijzondere regeling voor verkoop op openbare veilingen

##### Afdeling 3
###### Art. 328
De voor elke in artikel 327 bedoelde levering verschuldigde BTW is gelijk aan het bedrag van de belasting die verschuldigd zou zijn indien de levering onder de normale BTW-regeling zou zijn gevallen, verminderd met het BTW-bedrag dat geacht wordt nog begrepen te zijn in de aankoopprijs van het vervoermiddel door de belastingplichtige wederverkoper.
###### Art. 329
De BTW die geacht wordt nog in de aankoopprijs van het vervoermiddel door de belastingplichtige wederverkoper te zijn begrepen, wordt als volgt berekend:
a)

de in aanmerking te nemen aankoopprijs is de aankoopprijs in de zin van artikel 312, punt 2);

b)

deze door de belastingplichtige wederverkoper betaalde aankoopprijs wordt geacht de BTW te omvatten die verschuldigd zou zijn geweest indien de leverancier van de belastingplichtige wederverkoper de normale BTW– regeling op zijn levering had toegepast;

c)

het in aanmerking te nemen tarief is het tarief dat uit hoofde van artikel 93 van toepassing is in de lidstaat binnen het grondgebied waarvan de overeenkomstig de artikelen 31 en 32 bepaalde plaats van levering aan de belastingplichtige wederverkoper wordt geacht te zijn gelegen.

###### Art. 333
1. De lidstaten mogen, overeenkomstig het bepaalde in deze afdeling, een bijzondere regeling toepassen voor de belastingheffing over de door een organisator van openbare veilingen gemaakte winstmarge op leveringen van gebruikte goederen, kunstvoorwerpen, voorwerpen voor verzamelingen en antiquiteiten, welke deze organisator die handelt in eigen naam en voor rekening van de in artikel 334 bedoelde personen, verricht krachtens een overeenkomst tot verkoop in commissie ter openbare veiling van deze goederen.
2. De in lid 1 bedoelde regeling is niet van toepassing op leveringen van nieuwe vervoermiddelen die worden verricht onder de in artikel 138, lid 1 en lid 2, onder a), gestelde voorwaarden.
###### Art. 334
Deze bijzondere regeling is van toepassing op leveringen door een organisator van openbare veilingen die handelt in eigen naam en voor rekening van een van de volgende personen:
a)

een niet-belastingplichtige;

b)

een andere belastingplichtige, voor zover de levering van het goed door deze belastingplichtige krachtens een overeenkomst tot verkoop in commissie verricht, overeenkomstig artikel 136 is vrijgesteld;

c)

een andere belastingplichtige, voor zover de levering van het goed door deze belastingplichtige, krachtens een overeenkomst tot verkoop in commissie verricht, in aanmerking komt voor de in de artikelen 282 tot en met 292 bedoelde vrijstellingsregeling voor kleine ondernemingen en een investeringsgoed betreft;

d)

een belastingplichtige wederverkoper, voor zover de levering van het goed door deze belastingplichtige wederverkoper, krachtens een overeenkomst tot verkoop in commissie verricht, is onderworpen aan de BTW overeenkomstig de winstmargeregeling.

###### Art. 330
De voor elke in artikel 327, lid 1, bedoelde levering van vervoermiddelen verschuldigde BTW, vastgesteld overeenkomstig artikel 328, mag niet minder bedragen dan het BTW-bedrag dat verschuldigd zou zijn indien deze levering aan de winstmargeregeling onderworpen zou zijn geweest.
De lidstaten kunnen bepalen dat, indien de levering aan de winstmargeregeling onderworpen zou zijn geweest, deze winstmarge niet lager mag zijn dan 10 % van de verkoopprijs in de zin van artikel 312, punt 1).
###### Art. 331
De belastingplichtige mag van de door hem verschuldigde belasting niet de BTW aftrekken, die verschuldigd of voldaan is voor gebruikte vervoermiddelen welke aan hem geleverd zijn door een belastingplichtige wederverkoper, voorzover de levering van die goederen door de belastingplichtige wederverkoper overeenkomstig deze overgangsregeling aan de belasting is onderworpen.

L 347/57

###### Art. 335
De levering van een goed aan een belastingplichtige organisator van openbare veilingen wordt geacht te hebben plaatsgevonden op het tijdstip waarop de verkoop van dat goed ter openbare veiling heeft plaatsgevonden.

L 347/58

Publicatieblad van de Europese Unie

NL
###### Art. 336

De maatstaf van heffing voor elke in deze afdeling bedoelde goederenlevering is het overeenkomstig artikel 339 door de organisator van de openbare veiling aan de afnemer in rekening gebrachte totale bedrag, verminderd met de volgende bedragen:
a)

b)

het door de organisator van de openbare veiling aan zijn opdrachtgever betaalde of te betalen nettobedrag, vastgesteld overeenkomstig artikel 337; het bedrag van de door de organisator van de openbare veiling krachtens zijn levering verschuldigde BTW.
###### Art. 337

Het door de organisator van de openbare veiling aan zijn opdrachtgever betaalde of te betalen nettobedrag is gelijk aan het verschil tussen de prijs waarvoor het goed geveild is, en het bedrag van de door de organisator van zijn opdrachtgever ontvangen of te ontvangen commissie krachtens de overeenkomst tot verkoop in commissie.

dat wil zeggen de veilingprijs van het goed, verminderd met het bedrag van de van de opdrachtgever ontvangen of te ontvangen commissie.
2. Het overeenkomstig lid 1 opgestelde verslag doet dienst als de factuur die de opdrachtgever, wanneer hij een belastingplichtige is, overeenkomstig artikel 220 aan de organisator van de openbare veiling moet uitreiken.
###### Art. 341
De lidstaten die de in deze afdeling vastgestelde regeling toepassen, passen deze ook toe op de leveringen van gebruikte vervoermiddelen als omschreven in artikel 327, lid 3, door een organisator van openbare veilingen die handelt in eigen naam ingevolge een overeenkomst tot verkoop in commissie op een openbare veiling van deze goederen voor rekening van een belastingplichtige wederverkoper, voorzover dezelfde leveringen door deze belastingplichtige wederverkoper overeenkomstig de overgangsregeling voor gebruikte vervoermiddelen aan de BTW zouden zijn onderworpen.

##### Afdeling 4
###### Art. 338
De organisatoren van openbare veilingen die onder de in de artikelen 333 en 334 vastgestelde voorwaarden goederen leveren, zijn gehouden de volgende bedragen in hun boekhouding op tussenrekeningen te boeken:
a)

de van de afnemer van het goed ontvangen of te ontvangen bedragen;

b)

de aan de verkoper van het goed betaalde of te betalen bedragen.

De in de eerste alinea bedoelde bedragen moeten naar behoren gerechtvaardigd worden.
###### Art. 339
De organisator van de openbare veiling moet aan de afnemer een factuur uitreiken waarop de volgende gegevens afzonderlijk zijn vermeld:
a)

de veilingprijs;

b)

de belastingen, rechten en heffingen;

c)

de bijkomende kosten, zoals kosten van commissie, verpakking, vervoer en verzekering, die de organisator de afnemer van het goed in rekening brengt.


Maatregelen ter voorkoming van verstor ing van de mededinging en fraude
###### Art. 342
De lidstaten kunnen maatregelen treffen betreffende het recht op aftrek van de BTW om te voorkomen dat de belastingplichtige wederverkopers op wie een van de in afdeling 2 vastgestelde regelingen van toepassing is, ongerechtvaardigde voordelen genieten, dan wel ongerechtvaardigde schade lijden.
###### Art. 343
De Raad kan op voorstel van de Commissie met eenparigheid van stemmen elke lidstaat machtigen bijzondere maatregelen ter bestrijding van fraude te treffen, waarin wordt bepaald dat de uit hoofde van de winstmargeregeling verschuldigde BTW niet lager mag zijn dan het belastingbedrag dat verschuldigd zou zijn indien de winstmarge gelijk was aan een bepaald percentage van de verkoopprijs.
Bij de vaststelling van het percentage van de verkoopprijs wordt rekening gehouden met de normale winstmarges van de economische subjecten in de betrokken sector.
#### HOOFDSTUK 5

Bijzondere regeling voor beleggingsgoud

Op de door de organisator van de openbare veiling uitgereikte factuur mag de BTW niet afzonderlijk zijn vermeld.

Algemene bepalingen

##### Afdeling 1
###### Art. 340

###### Art. 344

1. De organisator van de openbare veiling aan wie het goed is overgedragen krachtens een overeenkomst tot verkoop in commissie op een openbare veiling, verstrekt aan zijn opdrachtgever een verslag.

1. Onverminderd andere bepalingen van het Gemeenschapsrecht wordt voor de toepassing van deze richtlijn als „beleggingsgoud” beschouwd: 1)

In het door de organisator van de openbare veiling verstrekte verslag wordt afzonderlijk het bedrag van de handeling vermeld,

goud, in de vorm van staven of plaatjes van een door de goudmarkten aanvaard gewicht, met een zuiverheid van ten minste 995/1 000, al dan niet belichaamd in effecten;

2)

Publicatieblad van de Europese Unie

NL

gouden munten die een zuiverheid van ten minste 900/
1 000 hebben, na 1800 zijn geslagen, in het land van oorsprong als wettig betaalmiddel fungeren of hebben gefungeerd en normaal worden verkocht voor een prijs die de openmarktwaarde van het in de munten vervatte goud niet met meer dan 80 % overschrijdt.

2. De lidstaten kunnen kleine staven of plaatjes met een gewicht van ten hoogste 1 gram uitsluiten van deze bijzondere regeling.
3. Voor de toepassing van deze richtlijn worden de in lid 1, punt 2), bedoelde munten niet geacht wegens hun numismatisch belang te worden verkocht.

L 347/59

van goud in de vorm van de in artikel 344, lid 1, punt 1), bedoelde staven of plaatjes aan een andere belastingplichtige welke anders uit hoofde van artikel 346 zouden zijn vrijgesteld.
2. De lidstaten kunnen het toepassingsgebied van het in lid 1 bedoelde keuzerecht beperken.
###### Art. 350
Indien de leverancier het recht overeenkomstig de artikelen 348 en 349 voor belastingheffing te kiezen, heeft uitgeoefend, verlenen de lidstaten de agent het recht, voor belastingheffing over de in artikel 347 bedoelde diensten te kiezen.
###### Art. 351

###### Art. 345
Vanaf 1999 deelt elke lidstaat de Commissie, vóór 1 juli van elk jaar, mee welke munten die aan de in artikel 344, lid 1, punt 2), genoemde criteria voldoen, in die lidstaat worden verhandeld.
Vóór 1 december van elk jaar publiceert de Commissie in de reeks C van het Publicatieblad van de Europese Unie de volledige lijst van deze munten. De in de gepubliceerde lijst opgenomen munten worden geacht aan deze criteria te voldoen gedurende het gehele jaar waarvoor de lijst wordt gepubliceerd.
Vr i j s t e l l i n g v a n d e b e l a s t i n g
##### Afdeling 2
###### Art. 346
De lidstaten verlenen vrijstelling van de BTW voor de levering, de intracommunautaire verwerving en de invoer van beleggingsgoud, waaronder beleggingsgoud dat belichaamd is in certificaten voor toegewezen of niet toegewezen goud of dat verhandeld wordt op goudrekeningen, en waaronder, in het bijzonder, goudleningen en swaps, die een eigendoms- of vorderingsrecht op beleggingsgoud belichamen, evenals voor handelingen betreffende beleggingsgoud bestaande in future- en termijncontracten die leiden tot de overdracht van een eigendoms- of vorderingsrecht met betrekking tot beleggingsgoud.
###### Art. 347
De lidstaten verlenen vrijstelling voor de diensten van agenten die optreden in naam en voor rekening van een ander wanneer zij betrokken zijn bij de levering van beleggingsgoud voor hun principaal.

De lidstaten stellen de nadere bepalingen voor de uitoefening van de in deze afdeling geregelde keuzerechten vast en stellen de Commissie ervan in kennis.
Handelingen op een gereglementeerde goudmarkt
##### Afdeling 4
###### Art. 352
Iedere lidstaat kan, na raadpleging van het BTW-Comité, specifieke handelingen met betrekking tot beleggingsgoud welke in die lidstaat plaatsvinden tussen belastingplichtigen die lid zijn van een door de betrokken lidstaat gereglementeerde goudmarkt, of tussen een lid van een door de betrokken lidstaat gereglementeerde goudmarkt en een andere belastingplichtige die geen lid is van die markt, aan de BTW onderwerpen. De lidstaat mag leveringen die worden verricht onder de in artikel 138 gestelde voorwaarden en de uitvoer van beleggingsgoud echter niet aan de BTW onderwerpen.
###### Art. 353
De lidstaten die uit hoofde van artikel 352 belasting heffen over de handelingen tussen belastingplichtigen die lid zijn van een gereglementeerde goudmarkt, staan eenvoudigheidshalve toe dat de te innen belasting wordt opgeschort en verlenen de belastingplichtigen ontheffing van de boekhoudingsvereisten inzake de BTW.

##### Afdeling 5

Bijzondere rechten en ver plichtingen van handelaren in beleggingsgoud

Recht om voor belastingheff ing te kiezen

##### Afdeling 3
###### Art. 354

###### Art. 348

Wanneer zijn daaropvolgende levering van beleggingsgoud krachtens dit hoofdstuk vrijgesteld is, heeft de belastingplichtige recht op aftrek van de volgende bedragen:

De lidstaten verlenen belastingplichtigen die beleggingsgoud produceren of goud omzetten in beleggingsgoud, het recht te kiezen voor belastingheffing over de leveringen van beleggingsgoud aan een andere belastingplichtige welke anders uit hoofde van artikel 346 zouden zijn vrijgesteld.

a)

de BTW die verschuldigd of voldaan is met betrekking tot beleggingsgoud dat hem is geleverd door een persoon die het in de artikelen 348 en 349 bedoelde keuzerecht heeft uitgeoefend of dat hem overeenkomstig afdeling 4 is geleverd;

b)

de BTW die verschuldigd of voldaan is met betrekking tot de levering aan hem dan wel de intracommunautaire verwerving of de invoer door hem van ander goud dan

###### Art. 349
1. De lidstaten kunnen belastingplichtigen die in het kader van hun bedrijf normaal goud leveren voor industriële doeleinden, het recht verlenen te kiezen voor belastingheffing over leveringen

L 347/60

Publicatieblad van de Europese Unie

NL

beleggingsgoud dat vervolgens door hem of in zijn naam wordt omgezet in beleggingsgoud;
c)

de BTW die verschuldigd of voldaan is met betrekking tot voor hem verrichte diensten bestaande in een wijziging van de vorm, het gewicht of de zuiverheid van goud met inbegrip van beleggingsgoud.
###### Art. 355

Belastingplichtigen die beleggingsgoud produceren of goud in beleggingsgoud omzetten, hebben recht op aftrek van de belasting die door hen verschuldigd of voldaan is met betrekking tot de levering, de intracommunautaire verwerving of de invoer van goederen of met betrekking tot diensten die met de productie of de omzetting van dat goud verband houden, alsof de daaropvolgende levering van het krachtens artikel 346 vrijgestelde goud belast was.
###### Art. 356

gevestigd noch daar over een vaste inrichting beschikt, en ook niet anderszins uit hoofde van artikel 214 geïdentificeerd moet zijn;
2)

„elektronische diensten” en „langs elektronische weg verrichte diensten”: de diensten bedoeld in artikel 56, lid 1, punt k);

3)

„lidstaat van identificatie”: de lidstaat die de niet in de
Gemeenschap gevestigde belastingplichtige verkiest te contacteren om opgave te doen van het begin van zijn activiteit als belastingplichtige op het grondgebied van de Gemeenschap overeenkomstig dit hoofdstuk;

4)

„lidstaat van verbruik”: de lidstaat waar de elektronische diensten worden geacht plaats te vinden overeenkomstig artikel 57;

5)

„BTW–aangifte”: de aangifte die alle gegevens omvat die nodig zijn om het bedrag van de in elke lidstaat verschuldigde BTW vast te stellen.

1. De lidstaten zorgen ervoor dat handelaren in beleggingsgoud ten minste een boekhouding voeren van alle belangrijke handelingen betreffende beleggingsgoud en de documenten bewaren aan de hand waarvan de identiteit van de afnemer bij dergelijke handelingen kan worden vastgesteld.
De handelaren bewaren de in de eerste alinea bedoelde informatie gedurende ten minste vijf jaar.
2. De lidstaten kunnen evenwaardige verplichtingen uit hoofde van maatregelen vastgesteld krachtens andere communautaire wetgeving, zoals Richtlijn 2005/60/EG van het Europees Parlement en de Raad van 26 oktober 2005 tot voorkoming van het gebruik van het financiële stelsel voor het witwassen van geld en de financiering van terrorisme (1), aanvaarden om aan de vereisten van lid 1 te voldoen.
3. De lidstaten kunnen strengere verplichtingen vaststellen, inzonderheid inzake speciale registratie- of boekhoudingsvereisten.
#### HOOFDSTUK 6

Bijzondere regeling voor niet in de Gemeenschap gevestigde belastingplichtigen die langs elektronische weg diensten verrichten voor niet-belastingplichtigen


Bijzondere regeling voor langs elektronische weg ver richte diensten
##### Afdeling 2
###### Art. 359
De lidstaten staan toe dat een niet in de Gemeenschap gevestigde belastingplichtige die elektronische diensten verricht voor een niet–belastingplichtige die in een lidstaat gevestigd is of er zijn woonplaats of zijn gebruikelijke verblijfplaats heeft, gebruikmaakt van deze bijzondere regeling. Deze regeling is van toepassing op alle aldus in de Gemeenschap verrichte diensten.
###### Art. 360
De niet in de Gemeenschap gevestigde belastingplichtige moet aan de lidstaat van identificatie opgave doen van het begin of de beëindiging van zijn activiteit als belastingplichtige, alsook van wijziging ervan in die mate dat hij niet langer aan de voorwaarden voldoet om van deze bijzondere regeling gebruik te mogen maken. Deze opgave gebeurt langs elektronische weg.
###### Art. 361

Algemene bepalingen
##### Afdeling 1
###### Art. 357
Dit hoofdstuk is van toepassing tot en met 31 december 2006.

1. De mededeling die de niet in de Gemeenschap gevestigde belastingplichtige aan de lidstaat van identificatie doet wanneer zijn belastbare activiteiten beginnen, bevat de volgende bijzonderheden voor de identificatie:
a)

de naam;

b)

het postadres;

c)

de elektronische adressen, met inbegrip van websites;

d)

in voorkomend geval, het nationale belastingnummer;

e)

een verklaring dat de belastingplichtige niet voor BTWdoeleinden in de Gemeenschap geïdentificeerd is.

###### Art. 358
Onverminderd andere communautaire bepalingen wordt voor de toepassing van dit hoofdstuk verstaan onder: 1)

„niet in de Gemeenschap gevestigde belastingplichtige”: een belastingplichtige die de zetel van zijn bedrijfsuitoefening niet op het grondgebied van de Gemeenschap heeft

(1) PB L 309 van 25.11.2005, blz. 15.


Publicatieblad van de Europese Unie

NL

2. De niet in de Gemeenschap gevestigde belastingplichtige doet de lidstaat van identificatie mededeling van eventuele wijzigingen in de verstrekte informatie.

L 347/61
###### Art. 367

De niet in de Gemeenschap gevestigde belastingplichtige voldoet de BTW op het moment dat de BTW-aangifte wordt ingediend.

###### Art. 362
De lidstaat van identificatie kent de niet in de Gemeenschap gevestigde belastingplichtige een individueel identificatienummer toe en deelt hem dit nummer langs elektronische weg mee.
Uitgaande van de voor deze identificatie gebruikte gegevens mogen de lidstaten van verbruik hun eigen identificatiesystemen gebruiken.
###### Art. 363
De lidstaat van identificatie verwijdert de niet in de Gemeenschap gevestigde belastingplichtige in de volgende gevallen uit het identificatieregister:
a)

de belastingplichtige deelt die lidstaat mee dat hij niet langer elektronische diensten verricht;

b)

er kan anderszins worden aangenomen dat zijn belastbare activiteiten beëindigd zijn;

c)

hij vervult niet langer de voorwaarden om van de bijzondere regeling gebruik te mogen maken;

d)

hij voldoet bij voortduring niet aan de voorschriften van de bijzondere regeling.
###### Art. 364

De niet in de Gemeenschap gevestigde belastingplichtige dient langs elektronische weg bij de lidstaat van identificatie een BTWaangifte in voor elk kalenderkwartaal, ongeacht of er elektronische diensten zijn verricht. De aangifte wordt uiterlijk 20 dagen na het verstrijken van het belastingtijdvak waarop de aangifte betrekking heeft, ingediend.

De belasting moet worden overgemaakt naar een door de lidstaat van identificatie opgegeven bankrekening in euro. De lidstaten die de euro niet hebben aangenomen, kunnen eisen dat de betaling wordt overgemaakt naar een bankrekening in hun eigen munteenheid.
###### Art. 368
De niet in de Gemeenschap gevestigde belastingplichtige die van deze bijzondere regeling gebruikmaakt, past in de aangifte geen aftrek van BTW uit hoofde van artikel 168 van deze richtlijn toe.
Niettegenstaande artikel 1, lid 1, van Richtlijn 86/560/EEG, wordt deze belastingplichtige teruggaaf verleend overeenkomstig die richtlijn. Artikel 2, leden 2 en 3, en artikel 4, lid 2, van Richtlijn 86/560/EEG zijn niet van toepassing op de teruggaaf die verband houdt met de onder deze bijzondere regeling vallende elektronische diensten.
###### Art. 369
1. De niet in de Gemeenschap gevestigde belastingplichtige voert van alle handelingen waarop deze bijzondere regeling van toepassing is, een boekhouding die voldoende gegevens moet bevatten om de belastingadministratie van de lidstaat van verbruik in staat te stellen de juistheid van de BTW-aangifte te bepalen.
2. Desgevraagd moet de in lid 1 bedoelde boekhouding langs elektronische weg aan de lidstaat van identificatie en aan de lidstaat van verbruik beschikbaar worden gesteld.
De boekhouding wordt bewaard gedurende tien jaar na afloop van het jaar waarin de handeling is verricht.
### TITEL XIII

###### Art. 365
AFWIJKINGEN

De BTW-aangifte bevat het identificatienummer en, voor elke lidstaat van verbruik waar de BTW verschuldigd is, het totale bedrag, de BTW niet inbegrepen, van de gedurende het belastingtijdvak verrichte elektronische diensten en het totale bedrag van de belasting daarover. De geldende BTW-tarieven en de totale verschuldigde belasting moeten eveneens op de aangifte worden vermeld.
###### Art. 366
1. De BTW-aangifte luidt in euro.

#### HOOFDSTUK 1

Afwijkingen van toepassing tot de invoering van de definitieve regeling
Afwijkingen voor de st aten die op 1 januari
1978 l i d w a r e n v a n d e G e m e e n s c h a p
##### Afdeling 1
###### Art. 370

De lidstaten die de euro niet hebben aangenomen, kunnen eisen dat de BTW-aangifte in hun nationale munteenheid luidt. Indien de diensten in een andere munteenheid luiden, hanteert de niet in de Gemeenschap gevestigde belastingplichtige bij het invullen van de BTW-aangifte de wisselkoers die gold op de laatste dag van het belastingtijdvak.
2. De omwisseling geschiedt volgens de wisselkoersen die de
Europese Centrale Bank voor die dag bekend heeft gemaakt of, wanneer die dag geen bekendmaking heeft plaatsgevonden, op de eerstvolgende dag van bekendmaking.

De lidstaten die op 1 januari 1978 de in de lijst van bijlage IX, deel A, genoemde handelingen belastten, mogen deze blijven belasten.
###### Art. 371
De lidstaten die op 1 januari 1978 vrijstelling verleenden voor de in de lijst van bijlage X, deel B, genoemde handelingen, mogen deze, onder de in iedere betrokken lidstaat op die datum bestaande voorwaarden, blijven vrijstellen.

L 347/62

Publicatieblad van de Europese Unie

NL

###### Art. 379

###### Art. 372
De lidstaten die op 1 januari 1978 bepalingen toepasten waarbij wordt afgeweken van het beginsel van onmiddellijke aftrek bedoeld in artikel 179, eerste alinea, mogen deze bepalingen blijven toepassen.


1. Finland mag de in bijlage X, deel A, punt 2, vermelde handelingen blijven belasten, zolang dezelfde handelingen worden belast in een van de lidstaten die op 31 december 1994 lid van de Gemeenschap waren.

###### Art. 373
De lidstaten die op 1 januari 1978 bepalingen toepasten waarbij wordt afgeweken van artikel 28 en artikel 79, eerste alinea, punt c), mogen deze bepalingen blijven toepassen.
###### Art. 374
In afwijking van de artikelen 169 en 309 mogen de lidstaten die op 1 januari 1978 vrijstelling zonder recht op aftrek van voorbelasting verleenden voor de diensten van reisbureaus bedoeld in artikel 309, deze vrijstelling handhaven. Deze afwijking is ook van toepassing op reisbureaus die in naam en voor rekening van de reiziger handelen.
Afwijkingen voor de staten die na 1 januari
1978 t o t d e G e m e e n s c h a p z i j n t oe g e t r e d e n
##### Afdeling 2
###### Art. 375

2. Finland mag onder de voorwaarden die in deze lidstaat op de datum van zijn toetreding bestonden, de in bijlage X, deel B, punt 2, vermelde diensten verricht door auteurs, kunstenaars en vertolkers van kunstwerken, alsmede de in bijlage X, deel B, punten 5, 9 en 10, vermelde handelingen blijven vrijstellen, zolang dezelfde vrijstellingen worden toegepast in een van de lidstaten die op 31 december 1994 lid van de Gemeenschap waren.
###### Art. 380
Zweden mag onder de voorwaarden die in deze lidstaat op de datum van zijn toetreding bestonden, de in bijlage X, deel B, punt 2, vermelde diensten verricht door auteurs, kunstenaars en vertolkers van kunstwerken, alsmede de in bijlage X, deel B, punten 1, 9 en 10, vermelde handelingen blijven vrijstellen, zolang dezelfde vrijstellingen worden toegepast in een van de lidstaten die op 31 december 1994 lid van de Gemeenschap waren.

Griekenland mag de in bijlage X, deel B, punten 2, 8, 9, 11 en 12, vermelde handelingen blijven vrijstellen onder de voorwaarden die in deze lidstaat op 1 januari 1987 bestonden.
###### Art. 376
Spanje mag de in bijlage X, deel B, punt 2, vermelde diensten van auteurs, alsmede de in bijlage X, deel B, punten 11 en 12, vermelde handelingen blijven vrijstellen onder de voorwaarden die in deze lidstaat op 1 januari 1993 bestonden.

###### Art. 381
Tsjechië mag, onder de voorwaarden die in deze lidstaat op de datum van zijn toetreding bestonden, vrijstelling blijven verlenen voor internationaal personenvervoer omschreven in bijlage X, deel B, punt 10, zolang dezelfde vrijstelling wordt toegepast in één van de lidstaten die op 30 april 2004 lid van de Gemeenschap waren.

###### Art. 377
Portugal mag de in bijlage X, deel B, punten 2, 4, 7, 9, 10 en 13, vermelde handelingen blijven vrijstellen onder de voorwaarden die in deze lidstaat op 1 januari 1989 bestonden.
###### Art. 378
1. Oostenrijk mag de in bijlage X, deel A, punt 2, vermelde handelingen blijven belasten.

###### Art. 382
Estland mag, onder de voorwaarden die in deze lidstaat op de datum van zijn toetreding bestonden, vrijstelling blijven verlenen voor internationaal personenvervoer omschreven in bijlage X, deel B, punt 10, zolang dezelfde vrijstelling wordt toegepast in één van de lidstaten die op 30 april 2004 lid van de Gemeenschap waren.
###### Art. 383

2. Zolang dezelfde vrijstellingen worden toegepast in een van de lidstaten die op 31 december 1994 lid van de Gemeenschap waren, mag Oostenrijk onder de voorwaarden die in deze lidstaat op de datum van zijn toetreding bestonden, vrijstelling blijven verlenen voor de volgende handelingen:
a)

de in bijlage X, deel B, punten 5 en 9, vermelde handelingen;

b)

met recht op aftrek van voorbelasting, alle onderdelen van het personenvervoer per vliegtuig, over zee of via de waterwegen van Oostenrijk naar een lidstaat of een derde land en omgekeerd, met uitzondering van het personenvervoer op het Bodenmeer.

Cyprus mag, zolang dezelfde vrijstelling wordt toegepast in één van de lidstaten die op 30 april 2004 lid van de Gemeenschap waren, vrijstelling blijven verlenen voor de volgende handelingen:
a)

leveringen van bouwterreinen omschreven in bijlage X, deel B, punt 9, tot en met 31 december 2007;

b)

internationaal personenvervoer omschreven in bijlage X, deel B, punt 10, zolang dezelfde vrijstelling wordt toegepast in één van de lidstaten die op 30 april 2004 lid van de Gemeenschap waren.


Publicatieblad van de Europese Unie

NL
###### Art. 384

Zolang dezelfde vrijstellingen worden verleend in een van de lidstaten die op 30 april 2004 lid van de Gemeenschap waren, mag Letland, onder de voorwaarden die in deze lidstaat op de datum van zijn toetreding bestonden, vrijstelling blijven verlenen:
a)

voor diensten die worden verricht door auteurs, kunstenaars en vertolkers van kunstwerken omschreven in bijlage X, deel B, punt 2;

b)

voor internationaal personenvervoer omschreven in bijlage X, deel B, punt 10.

L 347/63

voor internationaal personenvervoer omschreven in bijlage X, deel B, punt 10, zolang dezelfde vrijstelling wordt toegepast in één van de lidstaten die op 30 april 2004 lid van de Gemeenschap waren.
###### Art. 390
Slowakije mag, onder de voorwaarden die in deze lidstaat op de datum van zijn toetreding bestonden, vrijstelling blijven verlenen voor internationaal personenvervoer omschreven in bijlage X, deel B, punt 10, zolang dezelfde vrijstelling wordt toegepast in één van de lidstaten die op 30 april 2004 lid van de Gemeenschap waren.

###### Art. 385


Litouwen mag, onder de voorwaarden die in deze lidstaat op de datum van zijn toetreding bestonden, vrijstelling blijven verlenen voor internationaal personenvervoer omschreven in bijlage X, deel B, punt 10, zolang dezelfde vrijstelling wordt toegepast in één van de lidstaten die op 30 april 2004 lid van de Gemeenschap waren.

Gemeenschappelijke bepalingen met betrekking tot de afdelingen 1 en 2

##### Afdeling 3
###### Art. 386
Hongarije mag, onder de voorwaarden die in deze lidstaat op de datum van zijn toetreding bestonden, vrijstelling blijven verlenen voor internationaal personenvervoer omschreven in bijlage X, deel B, punt 10, zolang dezelfde vrijstelling wordt toegepast in één van de lidstaten die op 30 april 2004 lid van de Gemeenschap waren.
###### Art. 387
Zolang dezelfde vrijstellingen worden toegepast in een van de lidstaten die op 30 april 2004 lid van de Gemeenschap waren, mag Malta onder de voorwaarden die in deze lidstaat op de datum van zijn toetreding bestonden de volgende handelingen blijven vrijstellen:
a)

zonder recht op aftrek van voorbelasting, waterdistributie door publiekrechtelijke diensten omschreven in bijlage X, deel B, punt 8;

b)

zonder recht op aftrek van voorbelasting, leveringen van gebouwen en bouwterreinen omschreven in bijlage X, deel B, punt 9;

c)

met recht op aftrek van de voorbelasting, binnenlands personenvervoer, internationaal personenvervoer en personenvervoer tussen de eilanden over zee, omschreven in bijlage X, deel B, punt 10.

###### Art. 391
De lidstaten die vrijstelling verlenen voor de in de artikelen 371,
375, 376 en 377, artikel 378, lid 2, artikel 379, lid 2, en de artikelen 380 tot en met 383 bedoelde handelingen, mogen de belastingplichtigen het recht verlenen voor belastingheffing ter zake van deze handelingen te kiezen.
###### Art. 392
De lidstaten mogen bepalen dat voor de leveringen van gebouwen en bouwterreinen welke met het oog op wederverkoop zijn gekocht door een belastingplichtige die voor die aankoop geen recht op aftrek heeft gehad, de maatstaf van heffing het verschil tussen de verkoopprijs en de aankoopprijs is.
###### Art. 393
1. Teneinde de overgang naar de in artikel 402 bedoelde definitieve regeling te vergemakkelijken, beziet de Raad, aan de hand van een verslag van de Commissie, de toestand met betrekking tot de in de afdelingen 1 en 2 vastgestelde afwijkingen opnieuw en beslist overeenkomstig artikel 93 van het Verdrag over de eventuele intrekking van deze afwijkingen of sommige daarvan.
2. In de definitieve regeling zal het personenvervoer in de lidstaat van vertrek worden belast voor het binnen de Gemeenschap afgelegde traject, volgens door de Raad overeenkomstig artikel 93 van het Verdrag vast te stellen nadere bepalingen.
#### HOOFDSTUK 2

Afwijkingen waarvoor machtiging is verleend

###### Art. 388


Polen mag, onder de voorwaarden die in deze lidstaat op de datum van zijn toetreding bestonden, vrijstelling blijven verlenen voor internationaal personenvervoer omschreven in bijlage X, deel B, punt 10, zolang dezelfde vrijstelling wordt toegepast in één van de lidstaten die op 30 april 2004 lid van de Gemeenschap waren.

Ve r e e n v o u d i g i n g s m a a t r e g e l e n e n maatregelen ter voorkoming van belastingfraude en -ontwijking

##### Afdeling 1
###### Art. 389
Slovenië mag, onder de voorwaarden die in deze lidstaat op de datum van zijn toetreding bestonden, vrijstelling blijven verlenen

###### Art. 394
De lidstaten die op 1 januari 1977 bijzondere maatregelen toepasten ter vereenvoudiging van de belastingheffing of ter voorkoming van bepaalde vormen van belastingfraude of -ontwijking, mogen deze handhaven op voorwaarde dat zij de Commissie vóór 1 januari 1978 van deze maatregelen in kennis

L 347/64

Publicatieblad van de Europese Unie

NL

hebben gesteld en onder voorbehoud dat de vereenvoudigingsmaatregelen voldoen aan de in artikel 395, lid 1, tweede alinea, omschreven voorwaarde.
###### Art. 395


3. Binnen drie maanden na toezending van de in lid 2, tweede alinea, bedoelde gegevens legt de Commissie de Raad hetzij een passend voorstel voor, hetzij, wanneer zij bezwaren heeft tegen het verzoek om een afwijking, een mededeling waarin zij deze bezwaren toelicht.

1. De Raad kan op voorstel van de Commissie met eenparigheid van stemmen elke lidstaat machtigen bijzondere, van de bepalingen van deze richtlijn afwijkende maatregelen te treffen, teneinde de belastinginning te vereenvoudigen of bepaalde vormen van belastingfraude of -ontwijking te voorkomen.

4. De in de leden 2 en 3 vastgestelde procedure moet in ieder geval worden voltooid binnen acht maanden na ontvangst van het verzoek door de Commissie.

De maatregelen tot vereenvoudiging van de belastinginning mogen geen noemenswaardige invloed hebben op de totale belastingopbrengst van de lidstaat in het stadium van het eindverbruik.

DIVERSE BEPALINGEN

2. De lidstaat die de in lid 1 bedoelde maatregelen wil treffen, dient een verzoek in bij de Commissie en verschaft haar alle nodige gegevens. Wanneer de Commissie meent niet over alle nodige gegevens te beschikken, neemt zij binnen twee maanden na ontvangst van het verzoek contact op met de betrokken lidstaat en deelt zij hem mede welke aanvullende gegevens vereist zijn.
Zodra de Commissie over alle gegevens beschikt die zij nodig acht voor de beoordeling van het verzoek, stelt zij de verzoekende lidstaat binnen een maand daarvan in kennis en zendt zij het verzoek in de oorspronkelijke taal aan de andere lidstaten toe.
3. Binnen drie maanden na toezending van de in lid 2, tweede alinea, bedoelde gegevens legt de Commissie de Raad hetzij een passend voorstel voor, hetzij, wanneer zij bezwaren heeft tegen het verzoek om een afwijking, een mededeling waarin zij deze bezwaren toelicht.
4. De in de leden 2 en 3 vastgestelde procedure moet in ieder geval worden voltooid binnen acht maanden na ontvangst van het verzoek door de Commissie.

##### Afdeling 2
### TITEL XIV

#### HOOFDSTUK 1

Uitvoeringsmaatregelen
###### Art. 397
De Raad stelt op voorstel van de Commissie met eenparigheid van stemmen de nodige maatregelen ter uitvoering van deze richtlijn vast.
#### HOOFDSTUK 2

BTW-Comité
###### Art. 398
1. Er wordt een raadgevend comité voor de belasting over de toegevoegde waarde ingesteld, „BTW-Comité” genoemd.
2. Het BTW-Comité is samengesteld uit vertegenwoordigers van de lidstaten en van de Commissie.
Het comité staat onder voorzitterschap van een vertegenwoordiger van de Commissie.
De Commissie is belast met het secretariaat van het comité.
3. Het BTW-Comité stelt zijn reglement van orde vast.

Inter nationale overeenkoms ten
###### Art. 396
1. De Raad kan op voorstel van de Commissie met eenparigheid van stemmen elke lidstaat machtigen met een derde land of een internationale organisatie een overeenkomst te sluiten waarin bepalingen kunnen voorkomen die van deze richtlijn afwijken.
2. De lidstaat die een overeenkomst als bedoeld in lid 1 wil sluiten, dient een verzoek in bij de Commissie en verschaft haar alle nodige gegevens. Wanneer de Commissie meent niet over alle nodige gegevens te beschikken, neemt zij binnen twee maanden na ontvangst van het verzoek contact op met de betrokken lidstaat en deelt zij hem mede welke aanvullende gegevens vereist zijn.
Zodra de Commissie over alle gegevens beschikt die zij nodig acht voor de beoordeling van het verzoek, stelt zij de verzoekende lidstaat binnen een maand daarvan in kennis en zendt zij het verzoek in de oorspronkelijke taal aan de andere lidstaten toe.

4. Naast de punten die volgens deze richtlijn aan raadpleging onderworpen zijn, onderzoekt het BTW-Comité de aangelegenheden die door zijn voorzitter op diens initiatief of op verzoek van een vertegenwoordiger van een lidstaat aan de orde worden gesteld en die betrekking hebben op de toepassing van de communautaire bepalingen inzake de BTW.
#### HOOFDSTUK 3

Omrekeningskoers
###### Art. 399
Onverminderd andere bijzondere bepalingen wordt de tegenwaarde van de in deze richtlijn in euro's uitgedrukte bedragen in de nationale munteenheid bepaald aan de hand van de op 1 januari 1999 geldende omrekeningskoers van de euro. De lidslaker die na deze daken lot de Europese Unie rijn toegetreden en die de euro niet als enige munt hebben aangenomen gebruiken echter de ten tijde van hun toetreding geldende omrekeningskoers.


Publicatieblad van de Europese Unie

NL

L 347/65

###### Art. 400

#### HOOFDSTUK 2

Bij de omrekening van de in artikel 399 bedoelde bedragen in de nationale munteenheid mogen de lidstaten de uit die omrekening voortvloeiende bedragen met maximaal 10 % naar boven of beneden afronden.

Overgangsmaatregelen in het kader van de toetreding tot de
Europese Unie

#### HOOFDSTUK 4

Andere belastingen, rechten en heffingen

###### Art. 405
Voor de toepassing van dit hoofdstuk wordt verstaan onder:
1)

„Gemeenschap”: het grondgebied van de Gemeenschap als omschreven in artikel 5, punt 1), vóór de toetreding van de nieuwe lidstaten;

2)

„nieuwe lidstaten”: het grondgebied van de lidstaten die op
1 januari 1995 tot de Europese Unie zijn toegetreden, als omschreven voor elk van deze lidstaten in artikel 5, punt 2);

3)

„uitgebreide Gemeenschap”: het grondgebied van de
Gemeenschap als omschreven in artikel 5, punt 1), na de toetreding van de nieuwe lidstaten.

###### Art. 401
Onverminderd andere communautaire bepalingen vormen de bepalingen van deze richtlijn geen beletsel voor de handhaving of invoering door een lidstaat van belastingen op verzekeringsovereenkomsten en op spelen en weddenschappen, alsmede van accijnzen, registratierechten en, meer in het algemeen, van alle belastingen, rechten en heffingen die niet het karakter van een omzetbelasting bezitten, mits de heffing van deze belastingen, rechten en heffingen in het verkeer tussen de lidstaten geen aanleiding geeft tot formaliteiten in verband met grensoverschrijding.
### TITEL XV
SLOTBEPALINGEN
#### HOOFDSTUK 1

Overgangsregeling voor de belastingheffing in het handelsverkeer tussen de lidstaten

###### Art. 406
De bepalingen die van toepassing waren op het tijdstip dat een goed onder een regeling voor tijdelijke invoer met volledige vrijstelling van invoerrechten, onder een van de in artikel 156 bedoelde regelingen of situaties, of onder vergelijkbare regelingen of situaties in één van de nieuwe lidstaten werd geplaatst, blijven van toepassing totdat het goed na de datum van toetreding aan de regeling of de situatie wordt onttrokken, indien de volgende voorwaarden vervuld zijn:
a)

het goed is vóór de datum van toetreding in de Gemeenschap of in een van de nieuwe lidstaten binnengebracht;

b)

het goed is bij het binnenbrengen ervan in de Gemeenschap of in een van de nieuwe lidstaten onder de regeling of situatie geplaatst;

c)

het goed is niet vóór de datum van toetreding aan deze regeling of situatie onttrokken.

###### Art. 402
1. De in deze richtlijn vastgestelde regeling voor de belastingheffing in het handelsverkeer tussen de lidstaten is een overgangsregeling en zal worden vervangen door een definitieve regeling, in beginsel gebaseerd op belastingheffing in de lidstaat van oorsprong van de goederenleveringen en de diensten.
2. Na het in artikel 404 bedoelde verslag te hebben bestudeerd en te hebben vastgesteld dat de voorwaarden voor de overgang naar de definitieve regeling vervuld zijn, stelt de Raad, overeenkomstig de procedure van artikel 93 van het Verdrag, de bepalingen vast die noodzakelijk zijn voor de inwerkingtreding en de werking van de definitieve regeling.
###### Art. 403
De Raad stelt overeenkomstig artikel 93 van het Verdrag passende richtlijnen vast met het oog op de aanvulling van het gemeenschappelijke BTW-stelsel en met name de geleidelijke beperking of intrekking van de afwijkingen van dit stelsel.

###### Art. 407
De bepalingen die van toepassing waren op het tijdstip dat een goed onder een regeling voor douanevervoer werd geplaatst, blijven van toepassing totdat het goed na de datum van toetreding aan de regeling wordt onttrokken, indien de volgende voorwaarden vervuld zijn:
a)

het goed is vóór de datum van toetreding onder een regeling voor douanevervoer geplaatst;

b)

het goed is niet vóór de datum van toetreding aan de regeling onttrokken.

###### Art. 404
Vanaf de vaststelling van deze richtlijn dient de Commissie om de vier jaar, op basis van de van de lidstaten verkregen gegevens, bij het Europees Parlement en de Raad een verslag in over de werking van het gemeenschappelijke BTW-stelsel in de lidstaten en met name over de werking van de overgangsregeling voor de belastingheffing in het handelsverkeer tussen de lidstaten, in voorkomend geval vergezeld van voorstellen voor de definitieve regeling.

###### Art. 408
1. Met de invoer van een goed waarvan wordt aangetoond dat het zich in het vrije verkeer in een van de nieuwe lidstaten of in de Gemeenschap bevond, wordt gelijkgesteld:
a)

elke onttrekking, met inbegrip van een onregelmatige onttrekking, van een goed aan een regeling voor tijdelijke invoer waaronder het goed vóór de datum van toetreding

L 347/66

Publicatieblad van de Europese Unie

NL

onder de algemene belastingvoorwaarden van de binnenlandse markt van een van de nieuwe lidstaten of een van de lidstaten van de Gemeenschap werd verworven of ingevoerd, of waarvoor, uit hoofde van de uitvoer ervan, geen vrijstelling of teruggaaf van de BTW werd verleend.

onder de in artikel 406 vermelde voorwaarden werd geplaatst;
b)

c)

d)

elke onttrekking, met inbegrip van een onregelmatige onttrekking, van een goed aan een in artikel 156 bedoelde regeling of situatie of een daarmee vergelijkbare regeling waaronder het goed vóór de datum van toetreding onder de in artikel 406 vermelde voorwaarden werd geplaatst; het einde van een van de in artikel 407 bedoelde regelingen waarmee vóór de datum van toetreding op het grondgebied van een van de nieuwe lidstaten een aanvang werd gemaakt ten behoeve van een vóór die datum onder bezwarende titel verrichte levering binnen het grondgebied van een lidstaat door een als zodanig handelende belastingplichtige; elke onregelmatigheid of overtreding die werd begaan tijdens een regeling voor douanevervoer waarmee een aanvang werd gemaakt onder de in punt c) bedoelde voorwaarden.

2. Naast het in lid 1 bedoelde geval wordt eveneens met de invoer van een goed gelijkgesteld, het gebruik, na de datum van toetreding, binnen het grondgebied van een lidstaat door een belastingplichtige of een niet-belastingplichtige, van goederen die vóór de datum van toetreding binnen het grondgebied van de Gemeenschap of een van de nieuwe lidstaten aan hem zijn geleverd, wanneer de volgende voorwaarden vervuld zijn:
a)

b)

de levering van deze goederen is of kon worden vrijgesteld uit hoofde van artikel 146, lid 1, punten a) en b), of uit hoofde van een vergelijkbare bepaling in een van de nieuwe lidstaten; de goederen zijn vóór de datum van toetreding niet ingevoerd in een van de nieuwe lidstaten of in de Gemeenschap.


2. De in lid 1, onder c), bedoelde voorwaarde wordt geacht te zijn vervuld in de volgende gevallen:
a)

de periode hussen de eerste ingebruikneming van het vervoermiddel en de dahern van toetrebing tot de Europese Unie is langer dan acht iaar;

b)

het bedrag van de belasting die uit hoofde van de invoer verschuldigd zou zijn, is te verwaarlozen.
#### HOOFDSTUK 3

Omzetting en inwerkingtreding
###### Art. 411
1. Richtlijn 67/227/EEG en Richtlijn 77/388/EEG worden ingetrokken, onverminderd de verplichtingen van de lidstaten met betrekking tot de in bijlage XI, deel B, aangegeven termijnen voor de omzetting en de uitvoering van deze richtlijnen.
2. Verwijzingen naar de ingetrokken richtlijnen gelden als verwijzingen naar deze richtlijn en worden gelezen volgens de concordantietabel in bijlage XII.
###### Art. 412
1. De lidstaten doen de nodige wettelijke en bestuursrechtelijke bepalingen in werking treden om uiterlijk op 1 januari 2008 aan artikel 2, lid 3, artikel 44, artikel 59, lid 1, artikel 399, en bijlage III, punt 18, van deze richtlijn te voldoen. Zij delen de Commissie de tekst van die bepalingen mede, alsmede een tabel ter weergave van het verband tussen die bepalingen en deze richtlijn.

###### Art. 409
In de gevallen bedoeld in artikel 408, lid 1, wordt de invoer in de zin van artikel 61 geacht te hebben plaatsgevonden in de lidstaat binnen het grondgebied waarvan het goed wordt onttrokken aan de regeling waaronder het vóór de datum van toetreding werd geplaatst.
###### Art. 410
1. In afwijking van artikel 71 vindt de invoer van een goed in de zin van artikel 408 plaats zonder dat een belastbaar feit plaatsvindt wanneer één van de volgende voorwaarden vervuld is:
a)

b)

c)

het ingevoerde goed wordt verzonden of vervoerd naar een plaats buiten de uitgebreide Gemeenschap; het in de zin van artikel 408, lid 1, punt a), ingevoerde goed is geen vervoermiddel en wordt herverzonden of vervoerd naar de lidstaat waaruit het werd uitgevoerd en naar degene die het heeft uitgevoerd; het in de zin van artikel 408, lid 1, punt a), ingevoerde goed is een vervoermiddel dat vóór de datum van toetreding

Wanneer de lidstaten die bepalingen aannemen, wordt in de bepalingen zelf of bij de officiële bekendmaking daarvan naar deze richtlijn verwezen. De regels voor de verwijzing worden vastgesteld door de lidstaten.
2. De lidstaten delen de Commissie de tekst van de belangrijkste bepalingen van intern recht mee die zij op het onder deze richtlijn vallende gebied vaststellen.
###### Art. 413
Deze richtlijn treedt in werking op 1 januari 2007.
###### Art. 414
Deze richtlijn is gericht tot de lidstaten.
Gedaan te Brussel, 28 november 2006.
Voor de Raad
De voorzitter
E. HEINÄLUOMA


Publicatieblad van de Europese Unie

NL

## BIJLAGE I
LIJST VAN WERKZAAMHEDEN BEDOELD IN ARTIKEL 14, LID 1, DERDE ALINEA

1)

Telecommunicatiediensten;

2)

levering van water, gas, elektriciteit en stoom;

3)

goederenvervoer;

4)

haven- en luchthavendiensten;

5)

personenvervoer;

6)

levering van nieuwe goederen geproduceerd voor de verkoop;

7)

handelingen van de landbouwinterventiebureaus met betrekking tot landbouwproducten, die worden verricht op grond van verordeningen houdende een gemeenschappelijke marktordening voor deze producten;

8)

exploitatie van commerciële beurzen en tentoonstellingen;

9)

opslag van goederen;

10)

werkzaamheden van commerciële reclamebureaus;

11)

werkzaamheden van reisbureaus;

12)

exploitatie van bedrijfskantines, bedrijfswinkels, coöperaties en soortgelijke inrichtingen;

13)

werkzaamheden van radio- en televisiediensten voor zover deze niet uit hoofde van artikel 132, lid 1, onder q), zijn vrijgesteld.

L 347/67

L 347/68

NL

Publicatieblad van de Europese Unie
## BIJLAGE II — INDICATIEVE LIJST VAN LANGS ELEKTRONISCHE WEG VERRICHTE DIENSTEN BEDOELD IN ARTIKEL 56, LID 1, PUNT K)

1)

Het leveren en onderbrengen van websites, het onderhoud op afstand van programma's en uitrustingen;

2)

de levering van software en de bijwerking ervan;

3)

de levering van beelden, geschreven stukken en informatie en de terbeschikkingstelling van databanken;

4)

de levering van muziek of films, van spelen, met inbegrip van kans- of gokspelen, en van uitzendingen of manifestaties op het gebied van politiek, cultuur, kunst, sport, wetenschappen of ontspanning;

5)

de levering van onderwijs op afstand.



NL

Publicatieblad van de Europese Unie
## BIJLAGE III

LIJST VAN DE GOEDERENLEVERINGEN EN DE DIENSTEN WAAROP DE IN ARTIKEL 98 BEDOELDE VERLAAGDE TARIEVEN MOGEN WORDEN TOEGEPAST

1)

Levensmiddelen (met inbegrip van dranken, maar met uitsluiting van alcoholhoudende dranken) voor menselijke en dierlijke consumptie, levende dieren, zaaigoed, planten en ingrediënten die gewoonlijk bestemd zijn voor gebruik bij de bereiding van levensmiddelen, alsmede producten die gewoonlijk bestemd zijn ter aanvulling of vervanging van levensmiddelen;

2)

waterdistributie;

3)

farmaceutische producten van een soort die gewoonlijk gebruikt wordt voor de gezondheidszorg, het voorkomen van ziekten of voor medische en veterinaire behandelingen, met inbegrip van voorbehoedsmiddelen en producten bestemd voor de hygiënische bescherming van de vrouw;

4)

medische uitrusting, hieronder begrepen in huur, hulpmiddelen en andere apparaten die gewoonlijk bestemd zijn voor verlichting of behandeling van handicaps, voor uitsluitend persoonlijk gebruik door gehandicapten, met inbegrip van de herstelling daarvan, en levering van kinderzitjes voor motorvoertuigen;

5)

vervoer van personen en de bagage die zij bij zich hebben;

6)

levering van boeken ook bij uitlening door bibliotheken (met inbegrip van brochures, folders en soortgelijk drukwerk, albums platen-, teken- en kleurboeken voor kinderen, gedrukte of geschreven muziekpartituren, landkaarten en hydrografische en soortgelijke kaarten), kranten en tijdschriften, voor zover niet uitsluitend of hoofdzakelijk reclamemateriaal;

7)

het verlenen van toegang tot shows, schouwburgen, circussen, kermissen, amusementsparken, concerten, musea, dierentuinen, bioscopen, tentoonstellingen en soortgelijke culturele evenementen en voorzieningen;

8)

de ontvangst van radio- en televisie-uitzendingen;

9)

diensten door en auteursrechten voor schrijvers, componisten en uitvoerende kunstenaars;

10)

levering, bouw, renovatie en verbouwing van in het kader van het sociaal beleid verstrekte huisvesting;

11)

levering van goederen en diensten die normaal bestemd zijn voor gebruik in de landbouw, met uitzondering evenwel van kapitaalgoederen, zoals machines of gebouwen;

12)

door hotels en dergelijke inrichtingen verstrekte accommodatie, met inbegrip van het verstrekken van vakantieaccommodatie en de verhuur van percelen op kampeerterreinen en in caravanparken;

13)

het verlenen van toegang tot sportevenementen;

14)

het recht gebruik te maken van sportaccommodaties;

15)

levering van goederen en diensten door organisaties die door de lidstaten als liefdadige instellingen zijn erkend en die betrokken zijn bij activiteiten op het gebied van bijstand en sociale zekerheid, voor zover deze handelingen niet krachtens de artikelen 132, 135 en 136 vrijgesteld zijn;

16)

diensten verricht door lijkbezorgers en crematoria, alsmede de daarmee verband houdende levering van goederen;

17)

de verstrekking van medische en tandheelkundige verzorging, alsmede thermale behandeling, voor zover deze niet krachtens artikel 132, lid 1, punten b) tot en met e), vrijgesteld zijn;

18)

diensten in verband met de reiniging van de openbare weg, het ophalen van huisvuil en de afvalverwerking, andere dan de diensten die door de in artikel 13 bedoelde lichamen worden verstrekt.

L 347/69

L 347/70

Publicatieblad van de Europese Unie

NL

## BIJLAGE IV
LIJST VAN DE IN ARTIKEL 106 BEDOELDE DIENSTEN

1)

Kleine hersteldiensten:
a)

fietsen;

b)

schoeisel en lederwaren;

c)

kleding en huishoudlinnen (ook herstellen en vermaken);

2)

renovatie en herstel van particuliere woningen, met uitzondering van materialen die een beduidend deel vertegenwoordigen van de waarde van de verstrekte diensten;

3)

glazenwassen en schoonmaken van particuliere woningen;

4)

thuiszorg zoals hulp in de huishouding en zorg voor kinderen, ouderen, zieken of gehandicapten;

5)

kappersdiensten.



NL

Publicatieblad van de Europese Unie
## BIJLAGE V

CATEGORIEËN GOEDEREN DIE VOLGENS ARTIKEL 160, LID 2, ONDER EEN ANDER STELSEL VAN ENTREPOTS DAN DOUANE-ENTREPOTS KUNNEN VALLEN

GN–code

Omschrijving

1)

Aardappelen

2)

0711 20

Olijven

3)

Kokosnoten, paranoten en cashewnoten

4)

Andere noten

5)

0901 11 00

Koffie, ongebrand

0901 12 00
6)

Thee

7)

1001 t/m 1005

Granen

1007 t/m 1008
8)

Padie

9)

1201 t/m 1207

Zaden, oliehoudende vruchten en zaaigoed (sojabonen daaronder begrepen)

10)

1507 t/m 1515

Plantaardige vetten en oliën, alsmede fracties daarvan, ook indien geraffineerd, doch niet chemisch gewijzigd

11)

1701 11

Ruwe suiker

1701 12
12)

Cacaobonen, ook indien gebroken, al dan niet gebrand

13)

Minerale oliën (met inbegrip van propaan en butaan en ruwe olie uit aardolie)

2711 12
2711 13
14)

hoofdstukken 28 en 29

Chemische producten (in bulk)

15)

Rubber, in primaire vormen of in platen, vellen of strippen

16)

Wol

17)

Zilver

18)

7110 11 00

Platina (palladium, rhodium)

7110 21 00
7110 31 00
19)

Koper

20)

Nikkel

21)

Aluminium

L 347/71

L 347/72

Publicatieblad van de Europese Unie

NL
GN–code

Omschrijving

22)

Lood

23)

Zink

24)

Tin

25)

ex 8112 92

Indium

ex 8112 99

## BIJLAGE VI
LIJST VAN GOEDERENLEVERINGEN EN DIENSTEN ALS BEDOELD IN PUNT D) VAN ARTIKEL 199, LID 1

1)

De levering van resten en afval van ferro- en non-ferroproducten en oude materialen, halffabrikaten daaronder begrepen, die het resultaat zijn van het verwerken, vervaardigen of smelten van ferro- en non-ferrometalen of legeringen daarvan;

2)

de levering van ferro- en non-ferrohalffabrikaten en bepaalde daarmee samenhangende verwerkingsdiensten;

3)

de levering van residuen en andere materialen voor hergebruik bestaande uit ferro- en non-ferrometalen, legeringen daarvan, slakken, assen, bladders en industriële residuen die metalen of legeringen daarvan bevatten, alsmede de diensten bestaande in het scheiden, snijden, fragmenteren en samenpersen van deze producten;

4)

de levering van en bepaalde verwerkingsdiensten met betrekking tot afval van ferro- en non-ferroproducten alsmede snippers, schroot, resten en afval, en oud materiaal en materiaal voor hergebruik bestaande uit glasscherven en glas, papier en karton, lompen, beenderen, leder, kunstleder, perkament, huiden en vellen, pezen en zenen, bindgaren, touw en kabel, rubber en kunststof;

5)

de levering van de in deze bijlage genoemde materialen na bewerking in de vorm van reinigen, polijsten, scheiden, snijden, fragmenteren, samenpersen of gieten tot ingots;

6)

de levering van resten en afval dat ontstaat bij de bewerking van grondstoffen.



Publicatieblad van de Europese Unie

NL

## BIJLAGE VII
LIJST VAN LANDBOUWPRODUCTIEWERKZAAMHEDEN BEDOELD IN ARTIKEL 295, LID 1, PUNT 4)

1)

2)

Landbouw:
a)

algemene landbouw met inbegrip van wijnbouw;

b)

vruchtboomteelt (olijvencultuur daaronder begrepen) en tuinbouw (groenten, bloemen en sierplanten), ook in kassen;

c)

kwekerijen van paddestoelen, specerijen en kruiden; teelt van zaad- en pootgoed;

d)

boomkwekerijen;

fokken en houden van dieren samenhangend met de exploitatie van de bodem:
a)

fokken en houden van dieren;

b)

pluimveebedrijf;

c)

konijnenteelt;

d)

imkerij;

e)

zijderupsenteelt;

f)

slakkenteelt;

3)

bosbouw;

4)

visserij:
a)

zoetwatervisserij;

b)

visteelt;

c)

teelt van mosselen, oesters en andere week- en schaaldieren;

d)

kikvorsenteelt.

L 347/73

L 347/74

NL

Publicatieblad van de Europese Unie
## BIJLAGE VIII — INDICATIEVE LIJST VAN AGRARISCHE DIENSTEN BEDOELD IN ARTIKEL 295, LID 1, PUNT 5)

1)

Bewerking van de grond, maaien, dorsen, persen, verzamelen en oogsten, inclusief het inzaaien en poten;

2)

verpakken en marktklaar maken, zoals drogen, schonen, kneuzen, desinfecteren en ensileren van landbouwproducten;

3)

opslag van landbouwproducten;

4)

inscharen, fokken, houden of mesten van dieren;

5)

verhuur, voor landbouwdoeleinden, van middelen die normaal in de landbouw-, bosbouw- of visserijbedrijven worden gebruikt;

6)

technische bijstand;

7)

vernietiging van schadelijke planten en dieren, behandelen van planten en grond door bespuiting;

8)

exploitatie van irrigatie- en draineerinstallaties;

9)

snoeien van bomen, kappen van hout en andere diensten in de bosbouw.



NL

Publicatieblad van de Europese Unie
## BIJLAGE IX — KUNSTVOORWERPEN, VOORWERPEN VOOR VERZAMELINGEN EN ANTIQUITEITEN BEDOELD IN ARTIKEL 311, LID 1, PUNTEN 2), 3) EN 4)

## DEEL A
Kunstvoorwerpen
1)

Schilderijen, collages en dergelijke decoratieve platen, schilderingen en tekeningen geheel van de hand van de kunstenaar, met uitzondering van bouwtekeningen en andere tekeningen voor industriële, commerciële, topografische en dergelijke doeleinden en van met de hand versierde voorwerpen alsmede van beschilderd doek voor theatercoulissen, voor achtergronden van studio's of voor dergelijk gebruik (GN-code 9701);

2)

originele gravures, originele etsen en originele litho's, dat wil zeggen een of meer door de kunstenaar geheel met de hand vervaardigde platen die in een beperkte oplage rechtstreeks in het zwart of in kleuren zijn afgedrukt, ongeacht het materiaal waarop dit afdrukken is geschied en ongeacht de gevolgde techniek, met uitzondering van de mechanische en van de fotomechanische reproductietechniek (GN-code 9702 00 00);

3)

originele standbeelden en origineel beeldhouwwerk, ongeacht het materiaal waarvan zij vervaardigd zijn, mits het werk geheel van de hand van de kunstenaar is; afgietsels van beeldhouwwerken in een oplage van maximaal acht exemplaren, die door de kunstenaar of diens rechthebbenden wordt gecontroleerd (GN-code 9703 00 00); bij wijze van uitzondering mag, in door de lidstaten bepaalde gevallen, met betrekking tot vóór 1 januari 1989 gemaakte afgietsels van beeldhouwwerken, het maximum van acht exemplaren worden overschreden;

4)

tapisserieën (GN-code 5805 00 00) en wandtextiel (GN-code 6304 00 00), met de hand vervaardigd volgens originele ontwerpen van kunstenaars, mits er niet meer dan acht exemplaren van elk zijn;

5)

unieke voorwerpen van keramiek, geheel van de hand van de kunstenaar en door hem gesigneerd;

6)

emailwerk op koper, geheel met de hand vervaardigd tot maximaal acht genummerde en door de kunstenaar of het atelier gesigneerde exemplaren, met uitsluiting van sieraden, juwelen en edelsmeedwerk;

7)

foto's die genomen zijn door de kunstenaar, door hem of onder zijn toezicht zijn afgedrukt, gesigneerd en genummerd, met een oplage van maximaal 30 exemplaren voor alle formaten en dragers samen.

## DEEL B
Voorwerpen voor verzamelingen
1)

Postzegels, fiscale zegels, gefrankeerde enveloppen en postkaarten, eerstedagsenveloppen en dergelijke, gestempeld of, indien ongestempeld, voor zover zij niet geldig zijn of niet geldig zullen worden (GN-code 9704 00 00);

2)

verzamelingen en voorwerpen voor verzamelingen, met een zoölogisch, botanisch, mineralogisch, anatomisch, historisch, archeologisch, paleontologisch, etnografisch of numismatisch belang (GN-code 9705 00 00).

## DEEL C
Antiquiteiten
Andere voorwerpen dan kunstvoorwerpen en voorwerpen voor verzamelingen, ouder dan 100 jaar (GN-code 9706 00 00).

L 347/75

L 347/76

NL

Publicatieblad van de Europese Unie
## BIJLAGE X

LIJST VAN HANDELINGEN WAARVOOR DE IN DE ARTIKELEN 370 EN 371 EN DE ARTIKELEN 375 TOT EN MET 390 BEDOELDE AFWIJKINGEN GELDEN

## DEEL A
Handelingen die de lidstaten mogen blijven belasten
1)

De door tandtechnici in het kader van de uitoefening van hun beroep verrichte diensten, alsmede het verschaffen van tandprothesen door tandartsen en tandtechnici;

2)

niet–commerciële activiteiten van openbare radio- en televisieorganisaties;

3)

leveringen van een gebouw, een gedeelte van een gebouw en het bijbehorende terrein, andere dan die bedoeld in artikel 12, lid 1, punt a), wanneer zij worden verricht door belastingplichtigen die recht hebben op aftrek van voorbelasting voor het betrokken gebouw;

4)

diensten van reisbureaus bedoeld in artikel 306 alsmede van reisbureaus die in naam en voor rekening van de reiziger handelen, voor reizen buiten de Gemeenschap.

## DEEL B
Handelingen die de lidstaten mogen blijven vrijstellen
1)

Het verlenen van toegang tot sportmanifestaties;

2)

diensten van auteurs, kunstenaars, vertolkers van kunstwerken, advocaten en andere beoefenaren van vrije beroepen, andere dan de medische en paramedische beroepen, met uitzondering van volgende diensten:
a)

de overdracht van octrooien, fabrieks- en handelsmerken en van soortgelijke rechten, alsmede het verlenen van licenties inzake deze rechten;

b)

andere werkzaamheden dan de oplevering van een werk in roerende staat, betrekking hebbende op roerende lichamelijke zaken en verricht voor belastingplichtigen;

c)

diensten die erop gericht zijn de uitvoering van bouwwerken voor te bereiden of te coördineren, zoals bijvoorbeeld de diensten verricht door architecten en bureaus die op de uitvoering van het werk toezicht houden;

d)

diensten op het gebied van de commerciële reclame;

e)

het vervoer en de opslag van goederen, alsmede daarmee samenhangende diensten;

f)

de verhuur van roerende lichamelijke zaken aan belastingplichtigen;

g)

het terbeschikkingstellen van personeel aan belastingplichtigen;

h)

op technisch, economisch of wetenschappelijk gebied: de diensten verricht door raadgevende personen, ingenieurs en planningbureaus, alsmede soortgelijke diensten;

i)

de nakoming van een verbintenis, bestaande uit het geheel of gedeeltelijk niet-uitoefenen van een beroepsactiviteit of van een in de punten a) tot en met h) en j) bedoeld recht;

j)

de diensten van expediteurs, makelaars, handelsagenten en andere zelfstandige tussenpersonen, voor zover zij betrekking hebben op de levering of de invoer van goederen of de in de punten a) tot en met i) bedoelde diensten;

3)

telecommunicatiediensten en daarmee rechtstreeks verband houdende leveringen van goederen door de openbare postdiensten;

4)

diensten verricht door lijkbezorgers en crematoria, alsmede levering door hen van goederen die met deze diensten in rechtstreeks verband staan;



NL

Publicatieblad van de Europese Unie

5)

handelingen verricht door blinden en/of blindenwerkplaatsen, mits door vrijstelling hiervan geen belangrijke verstoring van de mededinging ontstaat;

6)

goederenleveringen en diensten verricht voor instellingen die zijn belast met het aanleggen, het inrichten en het onderhouden van begraaf- en grafplaatsen en gedenktekens voor oorlogsslachtoffers;

7)

handelingen van ziekenhuizen die niet onder artikel 132, lid 1, punt b), vallen;

8)

waterdistributie door publiekrechtelijke diensten;

9)

leveringen van gebouwen of gedeelten van gebouwen en het bijbehorende terrein vóór de eerste ingebruikneming alsook leveringen van bouwterreinen als bedoeld in artikel 12;

10)

personenvervoer en vervoer van goederen, zoals bagage en personenauto's die door reizigers worden meegevoerd, of diensten die samenhangen met het vervoer van personen, voor zover het vervoer van deze personen vrijgesteld is;

11)

levering, verbouwing, reparatie, onderhoud, bevrachting en verhuur van luchtvaartuigen die worden gebruikt door staatsinstellingen (inclusief voorwerpen die met deze luchtvaartuigen vast verbonden zijn of voor hun exploitatie dienen);

12)

levering, verbouwing, reparatie, onderhoud, bevrachting en verhuur van oorlogsschepen;

13)

diensten van reisbureaus als bedoeld in artikel 306 alsmede van reisbureaus die in naam en voor rekening van de reiziger handelen, voor reizen binnen de Gemeenschap.

L 347/77

L 347/78

Publicatieblad van de Europese Unie

NL

## BIJLAGE XI

## DEEL A
Ingetrokken richtlijnen met de achtereenvolgende wijzigingen ervan
1)

Richtlijn 67/227/EEG (PB 71 van 14.4.1967, blz. 1301)
Richtlijn 77/388/EEG

2)

Richtlijn 77/388/EEG (PB L 145 van 13.6.1977, blz. 1)
Richtlijn 78/583/EEG (PB L 194 van 19.7.1978, blz. 16)
Richtlijn 80/368/EEG (PB L 90 van 3.4.1980, blz. 41)
Richtlijn 84/386/EEG (PB L 208 van 3.8.1984, blz. 58)
Richtlijn 89/465/EEG (PB L 226 van 3.8.1989, blz. 21)
Richtlijn 91/680/EEG (PB L 376 van 31.12.1991, blz. 1) — (met uitzondering van artikel 2) Richtlijn 92/77/EEG (PB L 316 van 31.10.1992, blz. 1) Richtlijn 92/111/EEG (PB L 384 van 30.12.1992, blz. 47) Richtlijn 94/4/EG (PB L 60 van 3.3.1994, blz. 14) — (enkel artikel 2) Richtlijn 94/5/EG (PB L 60 van 3.3.1994, blz. 16) Richtlijn 94/76/EG (PB L 365 van 31.12.1994, blz. 53) Richtlijn 95/7/EG (PB L 102 van 5.5.1995, blz. 18) Richtlijn 96/42/EG (PB L 170 van 9.7.1996, blz. 34) Richtlijn 96/95/EG (PB L 338 van 28.12.1996, blz. 89) Richtlijn 98/80/EG (PB L 281 van 17.10.1998, blz. 31) Richtlijn 1999/49/EG (PB L 139 van 2.6.1999, blz. 27) Richtlijn 1999/59/EG (PB L 162 van 26.6.1999, blz. 63) Richtlijn 1999/85/EG (PB L 277 van 28.10.1999, blz. 34) Richtlijn 2000/17/EG (PB L 84 van 5.4.2000, blz. 24) Richtlijn 2000/65/EG (PB L 269 van 21.10.2000, blz. 44) Richtlijn 2001/4/EG (PB L 22 van 24.1.2001, blz. 17) Richtlijn 2001/115/EG (PB L 15 van 17.1.2001, blz. 24) Richtlijn 2002/38/EG (PB L 128 van 15.5.2002, blz. 41) Richtlijn 2002/93/EG (PB L 331 van 7.12.2002, blz. 27) Richtlijn 2003/92/EG (PB L 260 van 11.10.2003, blz. 8)



NL

Publicatieblad van de Europese Unie

Richtlijn 2004/7/EG (PB L 27 van 30.1.2004, blz. 44)
Richtlijn 2004/15/EG (PB L 52 van 21.2.2004, blz. 61)
Richtlijn 2004/66/EG (PB L 168 van 1.5.2004, blz. 35) — (enkel punt V van de bijlage) Richtlijn 2005/92/EG (PB L 345 van 28.12.2005, blz. 19) Richtlijn 2006/18/EG (PB L 51 van 22.2.2006, blz. 12) Richtlijn 2006/58/EG (PB L 174 van 28.6.2006, blz. 5) Richtlijn 2006/69/EG (PB L 221 van 12.8.2006, blz. 9) — (enkel artikel 1)

## DEEL B
Termijnen voor de omzetting in nationaal recht
(bedoeld in artikel 411)

Richtlijn

Richtlijn 67/227/EEG
Richtlijn 77/388/EEG
Richtlijn 78/583/EEG
Richtlijn 80/368/EEG
Richtlijn 84/386/EEG
Richtlijn 89/465/EEG

Richtlijn 91/680/EEG
Richtlijn 92/77/EEG
Richtlijn 92/111/EEG

Richtlijn 94/4/EG
Richtlijn 94/5/EG
Richtlijn 94/76/EG
Richtlijn 95/7/EG
Richtlijn 96/42/EG
Richtlijn 96/95/EG
Richtlijn 98/80/EG
Richtlijn 1999/49/EG
Richtlijn 1999/59/EG
Richtlijn 1999/85/EG
Richtlijn 2000/17/EG
Richtlijn 2000/65/EG
Richtlijn 2001/4/EG
Richtlijn 2001/115/EG
Richtlijn 2002/38/EG
Richtlijn 2002/93/EG
Richtlijn 2003/92/EG
Richtlijn 2004/7/EG
Richtlijn 2004/15/EG
Richtlijn 2004/66/EG
Richtlijn 2005/92/EG

Omzettingstermijn

1 januari 1970
1 januari 1978
1 januari 1979
1 januari 1979
1 juli 1985
1 januari 1990
1 januari 1991
1 januari 1992
1 januari 1993
1 januari 1994 voor Portugal
1 januari 1993
31 december 1992
1 januari 1993
1 januari 1994
1 oktober 1993 voor Duitsland
1 april 1994
1 januari 1995
1 januari 1995
1 januari 1996
1 januari 1997 voor Duitsland en Luxemburg
1 januari 1995
1 januari 1997
1 januari 2000
1 januari 1999
1 januari 2000
—
—
31 december 2001
1 januari 2001
1 januari 2004
1 juli 2003
—
1 januari 2005
30 januari 2004
—
1 mei 2004
1 januari 2006

L 347/79

L 347/80

NL

Publicatieblad van de Europese Unie

Richtlijn

Richtlijn 2006/18/EG
Richtlijn 2006/58/EG
Richtlijn 2006/69/EG

Omzettingstermijn

—
1 juli 2006
1 januari 2008



## BIJLAGE XII — CONCORDANTIETABEL

Richtlijn 67/227/EEG

Richtlijn 77/388/EEG

Wijzigingsrichtlijnen

Andere besluiten

Deze richtlijn

Artikel 1, lid 1

Artikel 1, tweede en derde alinea

—

Artikel 2, eerste, tweede en derde alinea

Artikel 1, lid 2, eerste, tweede en derde alinea

Artikelen 3, 4 en 6

—

Artikel 2, onder 1)

Artikel 2, lid 1, onder a) en c)

Artikel 2, onder 2)

Artikel 2, lid 1, onder d)

Artikel 3, lid 1, eerste streepje

Artikel 5, onder 2)

Artikel 3, lid 1, tweede streepje

Artikel 5, onder 1)

Artikel 3, lid 1, derde streepje

Artikel 5, onder 3) en 4)

Artikel 3, lid 2

—

Artikel 3, lid 3, eerste alinea, eerste streepje

Artikel 6, lid 2, onder a) en b)

Artikel 3, lid 3, eerste alinea, tweede streepje

Artikel 6, lid 2, onder c) en d)

Artikel 3, lid 3, eerste alinea, derde streepje

Artikel 6, lid 2, onder e), f) en g)

Artikel 3, lid 3, tweede alinea, eerste streepje

Artikel 6, lid 1, onder b)

Artikel 3, lid 3, tweede alinea, tweede streepje

Artikel 6, lid 1, onder c)

Artikel 3, lid 3, tweede alinea, derde streepje

Artikel 6, lid 1, onder a)

Artikel 3, lid 4, eerste alinea, eerste en tweede streepje

Artikel 7, lid 1

Artikel 3, lid 4, tweede alinea, eerste, tweede en derde streepje

Artikel 7, lid 2

L 347/81

—

Publicatieblad van de Europese Unie

###### Art. 1

NL

Artikel 1, eerste alinea

Richtlijn 77/388/EEG

Wijzigingsrichtlijnen

Andere besluiten

Deze richtlijn

Artikel 9, lid 1, eerste en tweede alinea

Artikel 4, lid 3, onder a), eerste alinea, eerste volzin

Artikel 12, lid 1, onder a)

Artikel 4, lid 3, onder a), eerste alinea, tweede volzin

Artikel 12, lid 2, tweede alinea

Artikel 4, lid 3, onder a), tweede alinea

Artikel 12, lid 2, derde alinea

Artikel 4, lid 3, onder a), derde alinea

Artikel 12, lid 2, eerste alinea

Artikel 4, lid 3, onder b), eerste alinea

Artikel 12, lid 1, onder b)

Artikel 4, lid 3, onder b), tweede alinea

Artikel 12, lid 3

Artikel 4, lid 4, eerste alinea

###### Art. 10

Artikel 4, lid 4, tweede en derde alinea

Artikel 11, eerste en tweede alinea

Artikel 4, lid 5, eerste, tweede en derde alinea

Artikel 13, lid 1, eerste, tweede en derde alinea

Artikel 4, lid 5, vierde alinea

Artikel 13, lid 2

Artikel 5, lid 1

Artikel 14, lid 1

Artikel 5, lid 2

Artikel 15, lid 1

Artikel 5, lid 3, onder a), b) en c)

Artikel 15, lid 2, onder a), b) en c)

Artikel 5, lid 4, onder a), b) en c)

Artikel 14, lid 2, onder a), b) en c)

Artikel 5, lid 5

Artikel 14, lid 3

Artikel 5, lid 6, eerste en tweede volzin

Artikel 16, eerste en tweede alinea

Artikel 5, lid 7, onder a), b) en c)

Artikel 18, onder a), b) en c)

Artikel 5, lid 8, eerste volzin

Artikel 19, eerste alinea

Artikel 5, lid 8, tweede en derde volzin

Artikel 19, tweede alinea

Artikel 6, lid 1, eerste alinea

Artikel 24, lid 1

Artikel 6, lid 1, tweede alinea, eerste, tweede en derde streepje

Artikel 25, onder a), b) en c)

Artikel 6, lid 2, eerste alinea, onder a) en
b)

Artikel 26, lid 1, onder a) en b)


Artikel 4, leden 1 en 2

Publicatieblad van de Europese Unie

###### Art. 8

NL

Artikel 3, lid 5

L 347/82

Richtlijn 67/227/EEG

Richtlijn 77/388/EEG

Wijzigingsrichtlijnen

Andere besluiten

Deze richtlijn

###### Art. 27

Artikel 6, lid 4

###### Art. 28

Artikel 6, lid 5

###### Art. 29

Artikel 7, lid 1, onder a) en b)

Artikel 30, eerste en tweede alinea

Artikel 7, lid 2

###### Art. 60

Artikel 7, lid 3, eerste en tweede alinea

Artikel 61, eerste en tweede alinea

Artikel 8, lid 1, onder a), eerste volzin

Artikel 32, eerste alinea

Artikel 8, lid 1, onder a), tweede en derde volzin

Artikel 36, eerste en tweede alinea

Artikel 8, lid 1, onder b)

###### Art. 31

Artikel 8, lid 1, onder c), eerste alinea

Artikel 37, lid 1

Artikel 8, lid 1, onder c), tweede alinea, eerste streepje

Artikel 37, lid 2, eerste alinea

Artikel 8, lid 1, onder c), tweede alinea, tweede en derde streepje

Artikel 37, lid 2, tweede en derde alinea

Artikel 8, lid 1, onder c), derde alinea

Artikel 37, lid 2, vierde alinea

Artikel 8, lid 1, onder c), vierde alinea

Artikel 37, lid 3, eerste alinea

Artikel 8, lid 1, onder c), vijfde alinea

—

Artikel 8, lid 1, onder c), zesde alinea

Artikel 37, lid 3, tweede alinea

Artikel 8, lid 1, onder d), eerste en tweede alinea

Artikel 38, leden 1 en 2

Artikel 8, lid 1, onder e), eerste volzin

Artikel 39, eerste alinea

Artikel 8, lid 1, onder e), tweede en derde volzin

Artikel 39, tweede alinea

Artikel 8, lid 2

Artikel 32, tweede alinea

Artikel 9, lid 1

###### Art. 43

Artikel 9, lid 2, inleidende zin

—

Artikel 9, lid 2, onder a)

###### Art. 45

L 347/83

Artikel 6, lid 3

Publicatieblad van de Europese Unie

Artikel 26, lid 2

NL

Artikel 6, lid 2, tweede alinea


Richtlijn 67/227/EEG

Richtlijn 77/388/EEG

Wijzigingsrichtlijnen

Andere besluiten

Deze richtlijn

Artikel 52, onder a) en b)

Artikel 9, lid 2, onder c), derde en vierde streepje

Artikel 52, onder c)

Artikel 9, lid 2, onder e), eerste tot en met zesde streepje

Artikel 56, lid 1, onder a) tot en met f)

Artikel 9, lid 2, onder e), zevende streepje

Artikel 56, lid 1, onder l)

Artikel 9, lid 2, onder e), achtste streepje

Artikel 56, lid 1, onder g)

Artikel 9, lid 2, onder e), negende streepje

Artikel 56, lid 1, onder h)

Artikel 9, lid 2, onder e), tiende streepje, eerste volzin

Artikel 56, lid 1, onder i)

Artikel 9, lid 2, onder e), tiende streepje, tweede volzin

Artikel 24, lid 2

Artikel 9, lid 2, onder e), tiende streepje, derde volzin

Artikel 56, lid 1, onder i)

Artikel 9, lid 2, onder e), elfde en twaalfde streepje

Artikel 56, lid 1, onder j) en k)

Artikel 9, lid 2, onder f)

Artikel 57, lid 1

Artikel 9, lid 3

Artikel 58, eerste en tweede alinea

Artikel 9, lid 3, onder a) en b)

Artikel 58, eerste alinea, onder a) en b)

Artikel 9, lid 4

Artikel 59, leden 1 en 2

Artikel 10, lid 1, onder a) en b)

Artikel 62, onder 1) en 2)

Artikel 10, lid 2, eerste alinea, eerste volzin

###### Art. 63

Artikel 10, lid 2, eerste alinea, tweede en derde volzin

Artikel 64, leden 1 en 2

Artikel 10, lid 2, tweede alinea

###### Art. 65

Artikel 10, lid 2, derde alinea, eerste, tweede en derde streepje

Artikel 66, onder a), b) en c)


Artikel 9, lid 2, onder c), eerste en tweede streepje

Publicatieblad van de Europese Unie

###### Art. 46

NL

Artikel 9, lid 2, onder b)

L 347/84

Richtlijn 67/227/EEG

Richtlijn 77/388/EEG

Wijzigingsrichtlijnen

Andere besluiten

Deze richtlijn

Artikel 71, lid 1, eerste alinea

Artikel 10, lid 3, tweede alinea

Artikel 71, lid 1, tweede alinea

Artikel 10, lid 3, derde alinea

Artikel 71, lid 2

Artikel 11, A, lid 1, onder a)

###### Art. 73

Artikel 11, A, lid 1, onder b)

###### Art. 74

Artikel 11, A, lid 1, onder c)

###### Art. 75

Artikel 11, A, lid 1, onder d)

###### Art. 77

Artikel 11, A, lid 2, onder a)

Artikel 78, eerste alinea, onder a)

Artikel 11, A, lid 2, onder b), eerste volzin

Artikel 78, eerste alinea, onder b)

Artikel 11, A, lid 2, onder b), tweede volzin

Artikel 78, tweede alinea

Artikel 11, A, lid 3, onder a) en b)

Artikel 79, eerste alinea, onder a) en b)
Artikel 87, onder a) en b)

Artikel 11, A, lid 3, onder c), eerste volzin

Artikel 79, eerste alinea, onder c)

Artikel 11, A, lid 3, onder c), tweede volzin

Artikel 79, tweede alinea

Artikel 11, A, lid 4, eerste en tweede alinea

Artikel 81, eerste en tweede alinea

Artikel 11, A, lid 5

###### Art. 82

Artikel 11, A, lid 6, eerste alinea, eerste en tweede volzin

Artikel 80, lid 1, eerste alinea

Artikel 11, A, lid 6, eerste alinea, derde volzin

Artikel 80, lid 1, tweede alinea

Artikel 11, A, lid 6, tweede alinea

Artikel 80, lid 1, eerste alinea

Artikel 11, A, lid 6, derde alinea

Artikel 80, lid 2

Artikel 11, A, lid 6, vierde alinea

Artikel 80, lid 3

L 347/85

Artikel 10, lid 3, eerste alinea, tweede volzin

Publicatieblad van de Europese Unie

###### Art. 70

NL

Artikel 10, lid 3, eerste alinea, eerste volzin


Richtlijn 67/227/EEG

Richtlijn 77/388/EEG

Wijzigingsrichtlijnen

Andere besluiten

Deze richtlijn

###### Art. 85

Artikel 11, B, lid 3, onder a)

Artikel 86, lid 1, onder a)

Artikel 11, B, lid 3, onder b), eerste alinea

Artikel 86, lid 1, onder b)

Artikel 11, B, lid 3, onder b), tweede alinea

Artikel 86, lid 2

Artikel 11, B, lid 3, onder b), derde alinea

Artikel 86, lid 1, onder b)

Artikel 11, B, lid 4

###### Art. 87

Artikel 11, B, lid 5

###### Art. 88

Artikel 11, B, lid 6, eerste en tweede alinea

Artikel 89, eerste en tweede alinea

Artikel 11, C, lid 1, eerste en tweede alinea

Artikel 90, leden 1 en 2

Artikel 11, C, lid 2, eerste alinea

Artikel 91, lid 1

Artikel 11, C, lid 2, tweede alinea, eerste en tweede volzin

Artikel 91, lid 2, eerste en tweede alinea

Artikel 11, C, lid 3, eerste en tweede streepje

Artikel 92, onder a) en b)

Artikel 12, lid 1

Artikel 93, eerste alinea

Artikel 12, lid 1, onder a)

Artikel 93, tweede alinea, onder a)

Artikel 12, lid 1, onder b)

Artikel 93, tweede alinea, onder c)

Artikel 12, lid 2, eerste en tweede streepje

Artikel 95, eerste en tweede alinea

Artikel 12, lid 3, onder a), eerste alinea, eerste volzin

###### Art. 96

Artikel 12, lid 3, onder a), eerste alinea, tweede volzin

Artikel 97, lid 1

Artikel 12, lid 3, onder a), tweede alinea

Artikel 97, lid 2

Artikel 12, lid 3, onder a), derde alinea, eerste volzin

Artikel 98, lid 1


Artikel 11, B, lid 1

Publicatieblad van de Europese Unie

Artikel 72, eerste en tweede alinea

NL

Artikel 11, A, lid 7, eerste en tweede alinea

L 347/86

Richtlijn 67/227/EEG

Richtlijn 77/388/EEG

Wijzigingsrichtlijnen

Andere besluiten

Deze richtlijn

Artikel 98, lid 2, tweede alinea

Artikel 12, lid 3, onder b), eerste volzin

Artikel 102 eerste alinea

Artikel 12, lid 3, onder b), tweede, derde en vierde volzin

Artikel 102, tweede alinea

Artikel 12, lid 3, onder c), eerste alinea

Artikel 103, lid 1

Artikel 12, lid 3, onder c), tweede alinea, eerste en tweede streepje

Artikel 103 lid 2, onder a) en b)

Artikel 12, lid 4, eerste alinea

Artikel 99, lid 2

Artikel 12, lid 4, tweede alinea, eerste en tweede volzin

Artikel 100, eerste en tweede alinea

Artikel 12, lid 4, derde alinea

###### Art. 101

Artikel 12, lid 5

Artikel 94, lid 2

Artikel 12, lid 6

###### Art. 105

Artikel 13, A, lid 1, inleidende zin

###### Art. 131

Artikel 13, A, lid 1, onder a) tot en met
n)

Artikel 132, lid 1, onder a) tot en met n)

Artikel 13, A, lid 1, onder o), eerste volzin

Artikel 132, lid 1, onder o)

Artikel 13, A, lid 1, onder o), tweede volzin

Artikel 132, lid 2

Artikel 13, A, lid 1, onder p) en q)

Artikel 132, lid 1, onder p) en q)

Artikel 13, A, lid 2, onder a), eerste tot en met vierde streepje

Artikel 133, eerste alinea, onder a) tot en met d)

Artikel 13, A, lid 2, onder b), eerste en tweede streepje

Artikel 134, onder a) en b)

Artikel 13, B, inleidende zin

###### Art. 131

Artikel 13, B, onder a)

Artikel 135, lid 1, onder a)

Artikel 13, B, onder b), eerste alinea

Artikel 135, lid 1, onder l)

L 347/87

Artikel 12, lid 3, onder a), vierde alinea

Publicatieblad van de Europese Unie

Artikel 98, lid 2, eerste alinea
Artikel 99, lid 1

NL

Artikel 12, lid 3, onder a), derde alinea, tweede volzin


Richtlijn 67/227/EEG

Richtlijn 77/388/EEG

Wijzigingsrichtlijnen

Andere besluiten

Deze richtlijn

Artikel 135, lid 2, tweede alinea

Artikel 13, B, onder c)

Artikel 136, onder a) en b)

Artikel 13, B, onder d)

—

Artikel 13, B, onder d), 1) tot en met 5)

Artikel 135, lid 1, onder b) tot en met f)

Artikel 13, B, onder d), 1) tot en met 5), eerste en tweede streepje

Artikel 135, lid 1, onder f)

Artikel 13, B, onder d), 6)

Artikel 135, lid 1, onder g)

Artikel 13, B, onder e) tot en met h)

Artikel 135, lid 1, onder h) tot en met k)

Artikel 13, C, eerste alinea, onder a)

Artikel 137, lid 1, onder d)

Artikel 13, C, eerste alinea, onder b)

Artikel 137, lid 1, onder a), b) en c)

Artikel 13, C, tweede alinea

Artikel 137, lid 2, eerste en tweede alinea

Artikel 14, lid 1, inleidende zin

###### Art. 131

Artikel 14, lid 1, onder a)

Artikel 140, onder a)

Artikel 14, lid 1, onder d), eerste en tweede alinea

Artikel 143, onder b) en c)

Artikel 14, lid 1, onder e)

Artikel 143, onder e)

Artikel 14, lid 1, onder g), eerste tot en met vierde streepje

Artikel 143, onder f) tot en met i)

Artikel 14, lid 1, onder h)

Artikel 143, onder j)

Artikel 14, lid 1, onder i)

###### Art. 144

Artikel 14, lid 1, onder j)

Artikel 143, onder k)

Artikel 14, lid 1, onder k)

Artikel 143, onder l)

Artikel 14, lid 2, eerste alinea

Artikel 145, lid 1

Artikel 14, lid 2, tweede alinea, eerste, tweede en derde streepje

Artikel 145, lid 2, eerste, tweede en derde alinea

Artikel 14, lid 2, derde alinea

Artikel 145, lid 3

Artikel 15, inleidende zin

###### Art. 131


Artikel 13, B, onder b), tweede alinea

Publicatieblad van de Europese Unie

Artikel 135, lid 2, eerste alinea, onder a) tot en met d)

NL

Artikel 13, B, onder b), eerste alinea, onder 1) tot en met 4)

L 347/88

Richtlijn 67/227/EEG

Richtlijn 77/388/EEG

Wijzigingsrichtlijnen

Andere besluiten

Deze richtlijn

Artikel 146, lid 1, onder b)

Artikel 15, onder 2), tweede alinea, eerste en tweede streepje

Artikel 147, lid 1, eerste alinea, onder a) en
b)

Artikel 15, onder 2), tweede alinea, derde streepje, eerste deel van volzin

Artikel 147, lid 1, eerste alinea, onder c)

Artikel 15, onder 2), tweede alinea, derde streepje, tweede deel van volzin

Artikel 147, lid 1, tweede alinea

Artikel 15, onder 2), derde alinea, eerste en tweede streepje

Artikel 147, lid 2, eerste en tweede alinea

Artikel 15, ondert 2), vierde alinea

Artikel 147, lid 2, derde alinea

Artikel 15, onder 3)

Artikel 146, lid 1, onder d)

Artikel 15, onder 4), eerste alinea, onder a) en b)

Artikel 148, onder a)

Artikel 15, onder 4), eerste alinea, onder c)

Artikel 148, onder b)

Artikel 15, onder 4), tweede alinea, eerste en tweede streepje

Artikel 150, leden 1 en 2

Artikel 15, onder 5)

Artikel 148, onder c)

Artikel 15, onder 6)

Artikel 148, onder f)

Artikel 15, onder 7)

Artikel 148, onder e)

Artikel 15, onder 8)

Artikel 148, onder d)

Artikel 15, onder 9)

Artikel 148, onder g)

Artikel 15, onder 10), eerste alinea, eerste tot en met vierde streepje

Artikel 151, lid 1, eerste alinea, onder a) tot en met d)

Artikel 15, onder 10), tweede alinea

Artikel 151, lid 1, tweede alinea

Artikel 15, onder 10), derde alinea

Artikel 151, lid 2

Artikel 15, onder 11)

###### Art. 152

Artikel 15, onder 12), eerste volzin

Artikel 146, lid 1, onder c)

Artikel 15, onder 12), tweede volzin

Artikel 146, lid 2

L 347/89

Artikel 15, onder 2), eerste alinea

Publicatieblad van de Europese Unie

Artikel 146, lid 1, onder a)

NL

Artikel 15, onder 1)


Richtlijn 67/227/EEG

Richtlijn 77/388/EEG

Wijzigingsrichtlijnen

Andere besluiten

Deze richtlijn

Artikel 153, eerste en tweede alinea

Artikel 15, onder 15)

###### Art. 149

Artikel 16, lid 1

—

Artikel 16, lid 2

Artikel 164, lid 1

Artikel 16, lid 3

###### Art. 166

Artikel 17, lid 1

###### Art. 167

Artikel 17, leden 2, 3 en 4

—

Artikel 17, lid 5, eerste en tweede alinea

Artikel 173, lid 1, eerste en tweede alinea

Artikel 17, lid 5, derde alinea, onder a) tot en met e)

Artikel 173, lid 2, onder a) tot en met e)

Artikel 17, lid 6

###### Art. 176

Artikel 17, lid 7, eerste en tweede volzin

Artikel 177, eerste en tweede alinea

Artikel 18, lid 1

—

Artikel 18, lid 2, eerste en tweede alinea

Artikel 179, eerste en tweede alinea

Artikel 18, lid 3

###### Art. 180

Artikel 18, lid 4, eerste en tweede alinea

Artikel 183, eerste en tweede alinea

Artikel 19, lid 1, eerste alinea, eerste streepje

Artikel 174, lid 1, eerste alinea, onder a)

Artikel 19, lid 1, eerste alinea, tweede streepje, eerste volzin

Artikel 174, lid 1, eerste alinea, onder b)

Artikel 19, lid 1, eerste alinea, tweede streepje, tweede volzin

Artikel 174, lid 1, tweede alinea

Artikel 19, lid 1, tweede alinea

Artikel 175, lid 1

Artikel 19, lid 2, eerste volzin

Artikel 174, lid 2, onder a)

Artikel 19, lid 2, tweede volzin

Artikel 174, lid 2, onder a) en b)

Artikel 19, lid 2, derde volzin

Artikel 174, lid 3


Artikel 15, onder 14), eerste en tweede alinea

Publicatieblad van de Europese Unie

Artikel 146, lid 1, onder e)

NL

Artikel 15, onder 13)

L 347/90

Richtlijn 67/227/EEG

Richtlijn 77/388/EEG

Wijzigingsrichtlijnen

Andere besluiten

Deze richtlijn

Artikel 175, lid 2, tweede alinea

Artikel 19, lid 3, tweede alinea

Artikel 175, lid 3

Artikel 20, lid 1, inleidende zin

###### Art. 186

Artikel 20, lid 1, onder a)

###### Art. 184

Artikel 20, lid 1, onder b), eerste deel van eerste volzin

Artikel 185, lid 1

Artikel 20, lid 1, onder b), tweede deel van eerste volzin

Artikel 185, lid 2, eerste alinea

Artikel 20, lid 1, onder b), tweede volzin

Artikel 185, lid 2, tweede alinea

Artikel 20, lid 2, eerste alinea, eerste volzin

Artikel 187, lid 1, eerste alinea

Artikel 20, lid 2, eerste alinea, tweede en derde volzin

Artikel 187, lid 2, eerste en tweede alinea

Artikel 20, lid 2, tweede en derde alinea

Artikel 187, lid 1, tweede en derde alinea

Artikel 20, lid 3, eerste alinea, eerste volzin

Artikel 188, lid 1, eerste alinea

Artikel 20, lid 3, eerste alinea, tweede volzin

Artikel 188, lid 1, tweede en derde alinea

Artikel 20, lid 3, eerste alinea, derde volzin

Artikel 188, lid 2

Artikel 20, lid 3, tweede alinea

Artikel 188, lid 2

Artikel 20, lid 4, eerste alinea, eerste tot en met vierde streepje

Artikel 189, onder a) tot en met d)

Artikel 20, lid 4, tweede alinea

###### Art. 190

Artikel 20, lid 5

###### Art. 191

Artikel 20, lid 6

###### Art. 192

###### Art. 21

—

###### Art. 22

—

Artikel 22 bis

###### Art. 249

L 347/91

Artikel 19, lid 3, eerste alinea, derde volzin

Publicatieblad van de Europese Unie

Artikel 175, lid 2, eerste alinea

NL

Artikel 19, lid 3, eerste alinea, eerste en tweede volzin


Richtlijn 67/227/EEG

Richtlijn 77/388/EEG

Wijzigingsrichtlijnen

Andere besluiten

Deze richtlijn

Artikel 211, tweede alinea

Artikel 24, lid 1

###### Art. 281

Artikel 24, lid 2, inleidende zin

###### Art. 292

Artikel 24, lid 2, onder a), eerste alinea

Artikel 284, lid 1

Artikel 24, lid 2, onder a), tweede en derde alinea

Artikel 284, lid 2, eerste en tweede alinea

Artikel 24, lid 2, onder b), eerste en tweede volzin

Artikel 285, eerste en tweede alinea

Artikel 24, lid 2, onder c)

###### Art. 286

Artikel 24, lid 3, eerste alinea

###### Art. 282

Artikel 24, lid 3, tweede alinea, eerste volzin

Artikel 283, lid 2

Artikel 24, lid 3, tweede alinea, tweede volzin

Artikel 283, lid 1, onder a)

Artikel 24, lid 4, eerste alinea

Artikel 288, eerste alinea, onder 1) tot en met 4)

Artikel 24, lid 4, tweede alinea

Artikel 288, tweede alinea

Artikel 24, lid 5

###### Art. 289

Artikel 24, lid 6

###### Art. 290

Artikel 24, lid 7

###### Art. 291

Artikel 24, lid 8, onder a), b) en c)

Artikel 293, onder 1), 2) en 3)

Artikel 24, lid 9

###### Art. 294

Artikel 24 bis, eerste alinea, eerste tot en met twaalfde streepje

Artikel 287, onder 7) tot en met 16)

Artikel 25, lid 1

Artikel 296, lid 1

Artikel 25, lid 2, eerste tot en met achtste streepje

Artikel 295, lid 1, onder 1) tot en met 8)

Artikel 25, lid 3, eerste alinea, eerste volzin

Artikel 297, eerste alinea, eerste volzin, en tweede alinea


Artikel 23, tweede alinea

Publicatieblad van de Europese Unie

Artikel 211, eerste alinea
###### Art. 260

NL

Artikel 23, eerste alinea

L 347/92

Richtlijn 67/227/EEG

Richtlijn 77/388/EEG

Wijzigingsrichtlijnen

Andere besluiten

Deze richtlijn

###### Art. 299

Artikel 25, lid 3, eerste alinea, vierde en vijfde volzin

Artikel 298, tweede alinea

Artikel 25, lid 3, tweede alinea

Artikel 297, eerste alinea, tweede volzin

Artikel 25, lid 4, eerste alinea

Artikel 272, lid 1, eerste alinea, onder e)

Artikel 25, leden 5 en 6

—

Artikel 25, lid 7

###### Art. 304

Artikel 25, lid 8

Artikel 301, lid 2

Artikel 25, lid 9

Artikel 296, lid 2

Artikel 25, lid 10

Artikel 296, lid 3

Artikel 25, leden 11 en 12

—

Artikel 26, lid 1, eerste en tweede volzin

Artikel 306, lid 1, eerste en tweede alinea

Artikel 26, lid 1, derde volzin

Artikel 306, lid 2

Artikel 26, lid 2, eerste en tweede volzin

Artikel 307, eerste en tweede alinea

Artikel 26, lid 2, derde volzin

###### Art. 308

Artikel 26, lid 3, eerste en tweede volzin

Artikel 309, eerste en tweede alinea

Artikel 26, lid 4

###### Art. 310

Artikel 26 bis, A, onder a), eerste alinea

Artikel 311, lid 1, onder 2)

Artikel 26 bis, A, onder a), tweede alinea

Artikel 311, lid 2

Artikel 26 bis, A, onder b) en c)

Artikel 311, lid 1, onder 3) en 4)

Artikel 26 bis, A, onder d)

Artikel 311, lid 1, onder 1)

Artikel 26 bis, A, onder e) en f)

Artikel 311, lid 1, onder 5) en 6)

Artikel 26 bis, A, onder g), inleidende zin

Artikel 311, lid 1, onder 7)

L 347/93

Artikel 25, lid 3, eerste alinea, derde volzin

Publicatieblad van de Europese Unie

Artikel 298, eerste alinea

NL

Artikel 25, lid 3, eerste alinea, tweede volzin


Richtlijn 67/227/EEG

Richtlijn 77/388/EEG

Wijzigingsrichtlijnen

Andere besluiten

Deze richtlijn

Artikel 313, lid 1

Artikel 26 bis, B, lid 2

###### Art. 314

Artikel 26 bis, B, lid 2, eerste en tweede streepje

Artikel 314, onder a) tot en met d)

Artikel 26 bis, B, lid 3, eerste alinea, eerste en tweede volzin

Artikel 315, eerste en tweede alinea

Artikel 26 bis, B, lid 3, tweede alinea

###### Art. 312

Artikel 26 bis, B, lid 3, tweede alinea, eerste en tweede streepje

Artikel 312, onder 1) en 2)

Artikel 26 bis, B, lid 4, eerste alinea

Artikel 316, lid 1

Artikel 26 bis, B, lid 4, eerste alinea, onder a), b) en c)

Artikel 316, lid 1, onder a), b) en c)

Artikel 26 bis, B, lid 4, tweede alinea

Artikel 316, lid 2

Artikel 26 bis, B, lid 4, derde alinea, eerste en tweede volzin

Artikel 317, eerste en tweede alinea

Artikel 26 bis, B, lid 5

###### Art. 321

Artikel 26 bis, B, lid 6

###### Art. 323

Artikel 26 bis, B, lid 7

###### Art. 322

Artikel 26 bis, B, lid 7, onder a), b) en c)

Artikel 322, onder a), b) en c)

Artikel 26 bis, B, lid 8

###### Art. 324

Artikel 26 bis, B, lid 9

###### Art. 325

Artikel 26 bis, B, lid 10, eerste en tweede alinea

Artikel 318, lid 1, eerste en tweede alinea

Artikel 26 bis, B, lid 10, derde alinea, eerste en tweede streepje

Artikel 318, lid 2, onder a) en b)

Artikel 26 bis, B, lid 10, vierde alinea

Artikel 318, lid 3

Artikel 26 bis, B, lid 11, eerste alinea

###### Art. 319

Artikel 26 bis, B, lid 11, tweede alinea, onder a)

Artikel 320, lid 1, eerste alinea


Artikel 26 bis, B, lid 1

Publicatieblad van de Europese Unie

Artikel 311, lid 3

NL

Artikel 26 bis, A, onder g), eerste en tweede streepje

L 347/94

Richtlijn 67/227/EEG

Richtlijn 77/388/EEG

Wijzigingsrichtlijnen

Andere besluiten

Deze richtlijn

Artikel 320, lid 2

Artikel 26 bis, C, lid 1, inleidende zin

Artikel 333, lid 1
###### Art. 334

Artikel 26 bis, C, lid 1, eerste tot en met vierde streepje

Artikel 334, onder a) tot en met d)

Artikel 26 bis, C, lid 2, eerste en tweede streepje

Artikel 336, onder a) en b)

Artikel 26 bis, C, lid 3

###### Art. 337

Artikel 26 bis, C, lid 4, eerste alinea, eerste, tweede en derde streepje

Artikel 339, eerste alinea, onder a), b) en c)

Artikel 26 bis, C, lid 4, tweede alinea

Artikel 339, tweede alinea

Artikel 26 bis, C, lid 5, eerste en tweede alinea

Artikel 340, lid 1, eerste en tweede alinea

Artikel 26 bis, C, lid 5, derde alinea

Artikel 340, lid 2

Artikel 26 bis, C, lid 6, eerste alinea, eerste en tweede streepje

Artikel 338, eerste alinea, onder a) en b)

Artikel 26 bis, C, lid 6, tweede alinea

Artikel 338, tweede alinea

Artikel 26 bis, C, lid 7

###### Art. 335

Artikel 26 bis, D, inleidende zin

—

Artikel 26 bis, D, onder a)

Artikel 313, lid 2
Artikel 333, lid 2

Artikel 26 bis, D, onder b)

Artikel 4, onder a) en c)

Artikel 26 bis, D, onder c)

###### Art. 35
Artikel 139, lid 3, eerste alinea

Artikel 26 ter, A, eerste alinea, onder i), eerste volzin

Artikel 344, lid 1, onder 1)

Artikel 26 ter, A, eerste alinea, onder i), tweede volzin

Artikel 344, lid 2

Artikel 26 ter, A, eerste alinea, onder ii), eerste tot en met vierde streepje

Artikel 344, lid 1, onder 2)

L 347/95

Artikel 26 bis, B, lid 11, derde alinea

Publicatieblad van de Europese Unie

Artikel 320, lid 1, tweede alinea

NL

Artikel 26 bis, B, lid 11, tweede alinea, onder b) en c)


Richtlijn 67/227/EEG

Richtlijn 77/388/EEG

Wijzigingsrichtlijnen

Andere besluiten

Deze richtlijn

###### Art. 345

Artikel 26 ter, B, eerste alinea

###### Art. 346

Artikel 26 ter, B, tweede alinea

###### Art. 347

Artikel 26 ter, C, eerste alinea

###### Art. 348

Artikel 26 ter, C, tweede alinea, eerste en tweede volzin

Artikel 349, leden 1 en 2

Artikel 26 ter, C, derde alinea

###### Art. 350

Artikel 26 ter, C, vierde alinea

###### Art. 351

Artikel 26 ter, D, lid 1, onder a), b) en c)

Artikel 354, onder a), b) en c)

Artikel 26 ter, D, lid 2

###### Art. 355

Artikel 26 ter, E, eerste en tweede alinea

Artikel 356, lid 1, eerste en tweede alinea

Artikel 26 ter, E, derde en vierde alinea

Artikel 356, leden 2 en 3

Artikel 26 ter, F, eerste volzin

Artikel 198, leden 2 en 3

Artikel 26 ter, F, tweede volzin

Artikelen 208 en 255

Artikel 26 ter, G, lid 1, eerste alinea

###### Art. 352

Artikel 26 ter, G, lid 1, tweede alinea

—

Artikel 26 ter, G, lid 2, onder a)

###### Art. 353

Artikel 26 ter, G, lid 2, onder b), eerste en tweede volzin

Artikel 198, leden 1 en 3

Artikel 26 quater, A, onder a) tot en met
e)

Artikel 358, onder 1) tot en met 5)

Artikel 26 quater, B, lid 1

###### Art. 359

Artikel 26 quater, B, lid 2, eerste alinea

###### Art. 360

Artikel 26 quater, B, lid 2, tweede alinea, eerste deel van eerste volzin

Artikel 361, lid 1

Artikel 26 quater, B, lid 2, tweede alinea, tweede deel van eerste volzin

Artikel 361, lid 1, onder a) tot en met e)


Artikel 26 ter, A, derde alinea

Publicatieblad van de Europese Unie

Artikel 344, lid 3

NL

Artikel 26 ter, A, tweede alinea

L 347/96

Richtlijn 67/227/EEG

Richtlijn 77/388/EEG

Wijzigingsrichtlijnen

Andere besluiten

Deze richtlijn

###### Art. 362

Artikel 26 quater, B, lid 4, onder a) tot en met d)

Artikel 363, onder a) tot en met d)

Artikel 26 quater, B, lid 5, eerste alinea

###### Art. 364

Artikel 26 quater, B, lid 5, tweede alinea

###### Art. 365

Artikel 26 quater, B, lid 6, eerste volzin

Artikel 366, lid 1, eerste alinea

Artikel 26 quater, B, lid 6, tweede en derde volzin

Artikel 366, lid 1, tweede alinea

Artikel 26 quater, B, lid 6, vierde volzin

Artikel 366, lid 2

Artikel 26 quater, B, lid 7, eerste volzin

Artikel 367, eerste alinea

Artikel 26 quater, B, lid 7, tweede en derde volzin

Artikel 367, tweede alinea

Artikel 26 quater, B, lid 8

###### Art. 368

Artikel 26 quater, B, lid 9, eerste volzin

Artikel 369, lid 1

Artikel 26 quater, B, lid 9, tweede en derde volzin

Artikel 369, lid 2, eerste en tweede alinea

Artikel 26 quater, B, lid 10

Artikel 204, lid 1, derde alinea

Artikel 27, lid 1, eerste en tweede volzin

Artikel 395, lid 1, eerste en tweede alinea

Artikel 27, lid 2, eerste en tweede volzin

Artikel 395, lid 2, eerste alinea

Artikel 27, lid 2, derde volzin

Artikel 395, lid 2, tweede alinea

Artikel 27, leden 3 en 4

Artikel 395, leden 3 en 4

Artikel 27, lid 5

###### Art. 394

Artikel 28, leden 1 en 1 bis

—

Artikel 28, lid 2, inleidende zin

###### Art. 109

Artikel 28, lid 2, onder a), eerste alinea

Artikel 110, eerste en tweede alinea

Artikel 28, lid 2, onder a), tweede alinea

—

L 347/97

Artikel 26 quater, B, lid 3, eerste en tweede alinea

Publicatieblad van de Europese Unie

Artikel 361, lid 2

NL

Artikel 26 quater, B, lid 2, tweede alinea, tweede volzin


Richtlijn 67/227/EEG

Richtlijn 77/388/EEG

Wijzigingsrichtlijnen

Andere besluiten

Deze richtlijn

Artikel 112, tweede alinea

Artikel 28, lid 2, onder b)

###### Art. 113

Artikel 28, lid 2, onder c), eerste en tweede volzin

Artikel 114, lid 1, eerste en tweede alinea

Artikel 28, lid 2, onder c), derde volzin

Artikel 114, lid 2

Artikel 28, lid 2, onder d)

###### Art. 115

Artikel 28, lid 2, onder e), eerste en tweede alinea

Artikel 118, eerste en tweede alinea

Artikel 28, lid 2, onder f)

###### Art. 120

Artikel 28, lid 2, onder g)

—

Artikel 28, lid 2, onder h), eerste en tweede alinea

Artikel 121, eerste en tweede alinea

Artikel 28, lid 2, onder i)

###### Art. 122

Artikel 28, lid 2, onder j)

Artikel 117, lid 2

Artikel 28, lid 2, onder k)

###### Art. 116

Artikel 28, lid 3, onder a)

###### Art. 370

Artikel 28, lid 3, onder b)

###### Art. 371

Artikel 28, lid 3, onder c)

###### Art. 391

Artikel 28, lid 3, onder d)

###### Art. 372

Artikel 28, lid 3, onder e)

###### Art. 373

Artikel 28, lid 3, onder f)

###### Art. 392

Artikel 28, lid 3, onder g)

###### Art. 374

Artikel 28, lid 3 bis

###### Art. 376

Artikel 28, leden 4 en 5

Artikel 393, leden 1 en 2

Artikel 28, lid 6, eerste alinea, eerste volzin

Artikel 106, eerste en tweede alinea


Artikel 28, lid 2, onder a), derde alinea, tweede en derde volzin

Publicatieblad van de Europese Unie

Artikel 112, eerste alinea

NL

Artikel 28, lid 2, onder a), derde alinea, eerste volzin

L 347/98

Richtlijn 67/227/EEG

Richtlijn 77/388/EEG

Wijzigingsrichtlijnen

Andere besluiten

Deze richtlijn

Artikel 107, eerste alinea, onder a), b) en c)

Artikel 28, lid 6, tweede alinea, onder d)

Artikel 107, tweede alinea

Artikel 28, lid 6, derde alinea

Artikel 107, tweede alinea

Artikel 28, lid 6, vierde alinea, onder a),
b) en c)

Artikel 108, onder a), b) en c)

Artikel 28, lid 6, vijfde en zesde alinea

—

Artikel 28 bis, lid 1, inleidende zin

Artikel 2, lid 1

Artikel 28 bis, lid 1, onder a), eerste alinea

Artikel 2, lid 1, onder b), i)

Artikel 28 bis, lid 1, onder a), tweede alinea

Artikel 3, lid 1

Artikel 28 bis, lid 1, onder a), derde alinea

Artikel 3, lid 3

Artikel 28 bis, lid 1, onder b)

Artikel 2, lid 1, onder b), ii)

Artikel 28 bis, lid 1, onder c)

Artikel 3, lid 1, onder b), iii)

Artikel 28 bis, lid 1 bis, onder a)

Artikel 3, lid 1, onder a)

Artikel 28 bis, lid 1 bis, onder b), eerste alinea, eerste streepje

Artikel 3, lid 1, onder b)

Artikel 28 bis, lid 1 bis, onder b), eerste alinea, tweede en derde streepje

Artikel 3, lid 2, eerste alinea, onder a) en b)

Artikel 28 bis, lid 1 bis, onder b), tweede alinea

Artikel 3, lid 2, tweede alinea

Artikel 28 bis, lid 2, inleidende zin

—

Artikel 28 bis, lid 2, onder a)

Artikel 2, lid 2, eerste alinea, onder a), b) en c)

Artikel 28 bis, lid 2, onder b), eerste alinea

Artikel 2, lid 2, tweede alinea

Artikel 28 bis, lid 2, onder b), eerste alinea, eerste en tweede streepje

Artikel 2, lid 2, tweede alinea, onder a), b) en c)

L 347/99

Artikel 28, lid 6, tweede alinea, onder a),
b) en c)

Publicatieblad van de Europese Unie

Artikel 106, derde alinea

NL

Artikel 28, lid 6, eerste alinea, tweede volzin


Richtlijn 67/227/EEG

Richtlijn 77/388/EEG

Wijzigingsrichtlijnen

Andere besluiten

Deze richtlijn

Artikel 20, eerste en tweede alinea

Artikel 28 bis, lid 4, eerste alinea

Artikel 9, lid 2

Artikel 28 bis, lid 4, tweede alinea, eerste streepje

Artikel 172, lid 1, tweede alinea

Artikel 28 bis, lid 4, tweede alinea, tweede streepje

Artikel 172, lid 1, eerste alinea

Artikel 28 bis, lid 4, derde alinea

Artikel 172, lid 2

Artikel 28 bis, lid 5, onder b), eerste alinea

Artikel 17, lid 1, eerste alinea

Artikel 28 bis, lid 5, onder b), tweede alinea

Artikel 17, lid 1, tweede alinea, en lid 2, inleidende zin

Artikel 28 bis, lid 5, onder b), tweede alinea, eerste streepje

Artikel 17, lid 2, onder a) en b)

Artikel 28 bis, lid 5, onder b), tweede alinea, tweede streepje

Artikel 17, lid 2, onder c)

Artikel 28 bis, lid 5, onder b), tweede alinea, derde streepje

Artikel 17, lid 2, onder e)

Artikel 28 bis, lid 5, onder b), tweede alinea, vijfde, zesde en zevende streepje

Artikel 17, lid 2, onder f), g) en h)

Artikel 28 bis, lid 5, onder b), tweede alinea, achtste streepje

Artikel 17, lid 2, onder d)

Artikel 28 bis, lid 5, onder b), derde alinea

Artikel 17, lid 3

Artikel 28 bis, lid 6, eerste alinea

###### Art. 21

Artikel 28 bis, lid 6, tweede alinea

###### Art. 22

Artikel 28 bis, lid 7

###### Art. 23

Artikel 28 ter, A, lid 1

###### Art. 40

Artikel 28 ter, A, lid 2, eerste en tweede alinea

Artikel 41, eerste en tweede alinea

Artikel 28 ter, A, lid 2, derde alinea, eerste en tweede streepje

Artikel 42, onder a) en b)


Artikel 28 bis, lid 3, eerste en tweede alinea

Publicatieblad van de Europese Unie

Artikel 2, lid 2, derde alinea

NL

Artikel 28 bis, lid 2, onder b), tweede alinea

L 347/100

Richtlijn 67/227/EEG

Richtlijn 77/388/EEG

Wijzigingsrichtlijnen

Andere besluiten

Deze richtlijn

Artikel 33, lid 2

Artikel 28 ter, B, lid 2, eerste alinea

Artikel 34, lid 1, onder a)

Artikel 28 ter, B, lid 2, eerste alinea, eerste en tweede streepje

Artikel 34, lid 1, onder b) en c)

Artikel 28 ter, B, lid 2, tweede alinea, eerste en tweede volzin

Artikel 34, lid 2, eerste en tweede alinea

Artikel 28 ter, B, lid 2, derde alinea, eerste volzin

Artikel 34, lid 3

Artikel 28 ter, B, lid 2, derde alinea, tweede en derde volzin

—

Artikel 28 ter, B, lid 3, eerste en tweede alinea

Artikel 34, lid 4, eerste en tweede alinea

Artikel 28 ter, C, lid 1, eerste streepje, eerste alinea

Artikel 48, eerste alinea

Artikel 28 ter, C, lid 1, eerste streepje, tweede alinea

###### Art. 49

Artikel 28 ter, C, lid 1, tweede en derde streepje

Artikel 48, tweede en derde alinea

Artikel 28 ter, C, leden 2 en 3

Artikel 47, eerste en tweede alinea

Artikel 28 ter, C, lid 4

###### Art. 51

Artikel 28 ter, D

###### Art. 53

Artikel 28 ter, E, lid 1, eerste en tweede alinea

Artikel 50, eerste en tweede alinea

Artikel 28 ter, E, lid 2, eerste en tweede alinea

Artikel 54, eerste en tweede alinea

Artikel 28 ter, E, lid 3, eerste en tweede alinea

Artikel 44, eerste en tweede alinea

Artikel 28 ter, F, eerste en tweede alinea

Artikel 55, eerste en tweede alinea

Artikel 28 quater, A, inleidende zin

###### Art. 131

Artikel 28 quater, A, onder a), eerste alinea

Artikel 138, lid 1

L 347/101

Artikel 28 ter, B, lid 1, tweede alinea

Publicatieblad van de Europese Unie

Artikel 33, lid 1, onder a) en b)

NL

Artikel 28 ter, B, lid 1, eerste alinea, eerste en tweede streepje


Richtlijn 67/227/EEG

Richtlijn 77/388/EEG

Wijzigingsrichtlijnen

Andere besluiten

Deze richtlijn

Artikel 28 quater, A, onder b)

Artikel 138, lid 2, onder a)

Artikel 28 quater, A, onder c), eerste alinea

Artikel 138, lid 2, onder b)

Artikel 28 quater, A, onder c), tweede alinea

Artikel 139, lid 2

Artikel 28 quater, A, onder d)

Artikel 138, lid 2, onder c)

Artikel 28 quater, B, inleidende zin

###### Art. 131

Artikel 28 quater, B, onder a), b) en c)

Artikel 140, onder a), b) en c)

Artikel 28 quater, C

###### Art. 142

Artikel 28 quater, D, eerste alinea

Artikel 143, onder d)

Artikel 28 quater, D, tweede alinea

###### Art. 131

Artikel 28 quater, E, punt 1, eerste streepje, dat artikel 16, lid 1, vervangt lid 1, eerste alinea

###### Art. 155

—

lid 1, eerste alinea, A

Artikel 157, lid 1, onder a)

—

lid 1, eerste alinea, B, eerste alinea, onder a), b) en c)

Artikel 156, lid 1, onder a), b) en c)

—

lid 1, eerste alinea, B, eerste alinea, onder d), eerste en tweede streepje

Artikel 156, lid 1, onder d) en e)

—

lid 1, eerste alinea, B, eerste alinea, onder e), eerste alinea

Artikel 157, lid 1, onder b)

—

lid 1, eerste alinea, B, eerste alinea, onder e), tweede alinea, eerste streepje

###### Art. 154

—

lid 1, eerste alinea, B, eerste alinea, onder e), tweede alinea, tweede streepje, eerste volzin

###### Art. 154

—

lid 1, eerste alinea, B, eerste alinea, onder e), tweede alinea, tweede streepje, tweede volzin

Artikel 157, lid 2


—

Publicatieblad van de Europese Unie

Artikel 139, lid 1, eerste en tweede alinea

NL

Artikel 28 quater, A, onder a), tweede alinea

L 347/102

Richtlijn 67/227/EEG

Richtlijn 77/388/EEG

Wijzigingsrichtlijnen

Andere besluiten

Deze richtlijn

lid 1, eerste alinea, B, eerste alinea, onder e), derde alinea, eerste streepje

—

—

lid 1, eerste alinea, B, eerste alinea, onder e), derde alinea, tweede, derde en vierde streepje

Artikel 158, lid 1, onder a), b) en c)

—

lid 1, eerste alinea, B, tweede alinea

Artikel 156, lid 2

—

lid 1, eerste alinea, C

###### Art. 159

—

lid 1, eerste alinea, D, eerste alinea, onder a) en b)

Artikel 160, lid 1, onder a) en b)

—

lid 1, eerste alinea, D, tweede alinea

Artikel 160, lid 2

—

lid 1, eerste alinea, E, eerste en tweede streepje

Artikel 161, onder a) en b)

—

lid 1, tweede alinea

###### Art. 202

—

lid 1, derde alinea

###### Art. 163

NL

—

lid 1 bis

###### Art. 162

Artikel 28 quater, E, onder 2), eerste streepje, dat artikel 16, lid 2, wijzigt —

lid 2, eerste alinea

Publicatieblad van de Europese Unie

Artikel 28 quater, E, onder 1), tweede streepje, dat lid 1 bis in artikel 16, invoegt —


Richtlijn 67/227/EEG

Artikel 164, lid 1

Artikel 28 quater, E, onder 2), tweede streepje, dat de tweede en derde alinea in artikel 16, lid 2, invoegt —

lid 2, tweede alinea

Artikel 164, lid 2

—

lid 2, derde alinea

###### Art. 165
Artikel 141, onder a) tot en met e)

Artikel 28 quinquies, lid 1, eerste en tweede volzin

Artikel 68, eerste en tweede alinea

Artikel 28 quinquies, leden 2 en 3

Artikel 69, leden 1 en 2

L 347/103

Artikel 28 quater, E, onder 3), eerste tot en met vijfde streepje

Richtlijn 77/388/EEG

Wijzigingsrichtlijnen

Andere besluiten

Deze richtlijn

Artikel 67, leden 1 en 2

Artikel 28 sexies, lid 1, eerste alinea

###### Art. 83

Artikel 28 sexies, lid 1, tweede alinea, eerste en tweede volzin

Artikel 84, leden 1 en 2

Artikel 28 sexies, lid 2

###### Art. 76

Artikel 28 sexies, lid 3

Artikel 93, tweede alinea, onder b)

Artikel 28 sexies, lid 4

Artikel 94, lid 1

NL

Artikel 28 quinquies, lid 4, eerste en tweede alinea

L 347/104

Richtlijn 67/227/EEG

Artikel 28 septies, onder 1), dat artikel 17, leden 2, 3 en 4, vervangt lid 2, onder a)

Artikel 168, onder a)

—

lid 2, onder b)

Artikel 168, onder e)

—

lid 2, onder c)

Artikel 168, onder b) en d)

—

lid 2, onder d)

Artikel 168, onder c)

—

lid 3, onder a), b) en c)

Artikel 169, onder a), b) en c)
Artikel 170, onder a) en b)s

—

lid 4, eerste alinea, eerste streepje

Artikel 171, lid 1, eerste alinea

—

lid 4, eerste alinea, tweede streepje

Artikel 171, lid 2, eerste alinea

—

lid 4, tweede alinea, onder a)

Artikel 171, lid 1, tweede alinea

—

lid 4, tweede alinea, onder b)

Artikel 171, lid 2, tweede alinea

—

lid 4, tweede alinea, onder c)

Artikel 171, lid 3

Publicatieblad van de Europese Unie

—

Artikel 28 septies, onder 2), dat artikel 18, lid 1, vervangt lid 1, onder a)

Artikel 178, onder a)

—

lid 1, onder b)

Artikel 178, onder e)

—

lid 1, onder c)

Artikel 178, onder b) en d)

—

lid 1, onder d)

Artikel 178, onder f)

—

lid 1, onder e)

Artikel 178, onder c)


—

Richtlijn 77/388/EEG

Wijzigingsrichtlijnen

Andere besluiten

Deze richtlijn

Artikel 28 septies, onder 3), dat lid 3 bis in artikel 18 invoegt lid 3 bis, eerste deel van volzin

###### Art. 181

—

lid 3 bis, tweede deel van volzin

###### Art. 182

NL

—


Richtlijn 67/227/EEG

Artikel 28 octies, dat artikel 21 vervangt lid 1, onder a), eerste alinea

###### Art. 193

—

lid 1, onder a), tweede alinea

Artikel 194, leden 1 en 2

—

lid 1, onder b)

###### Art. 196

—

lid 1, onder c), eerste alinea, eerste, tweede en derde streepje

Artikel 197, lid 1, onder a), b) en c)

—

lid 1, onder c), tweede alinea

Artikel 197, lid 2

—

lid 1, onder d)

###### Art. 203

—

lid 1, onder e)

###### Art. 200

—

lid 1, onder f)

###### Art. 195

—

lid 2

—

—

lid 2, onder a), eerste volzin

Artikel 204, lid 1, eerste alinea

—

lid 2, onder a), tweede volzin

Artikel 204, lid 2

—

lid 2, onder b)

Artikel 204, lid 1, tweede alinea

—

lid 2, onder c), eerste alinea

Artikel 199, lid 1, onder a) tot en met g)

—

lid 2, onder c), tweede, derde en vierde alinea

Artikel 199, leden 2, 3 en 4

—

lid 3

###### Art. 205

—

lid 4

###### Art. 201

Publicatieblad van de Europese Unie

—

Artikel 28 nonies, dat artikel 21 vervangt lid 1, onder a), eerste en tweede volzin

Artikel 213, lid 1, eerste en tweede alinea

—

lid 1, onder b)

Artikel 213, lid 2

L 347/105

—

Richtlijn 77/388/EEG

Wijzigingsrichtlijnen

Andere besluiten

Deze richtlijn

—

lid 1, onder c), eerste streepje, tweede volzin

Artikel 214, lid 2

—

lid 1, onder c), tweede en derde streepje

Artikel 214, lid 1, onder b) en c)

—

lid 1, onder d), eerste en tweede volzin

Artikel 215, eerste en tweede alinea

—

lid 1, onder e)

###### Art. 216

—

lid 2, onder a)

###### Art. 242

—

lid 2, onder b), eerste en tweede alinea

Artikel 243, leden 1 en 2

—

lid 3, onder a), eerste alinea, eerste volzin

Artikel 220, onder 1)

—

lid 3, onder a), eerste alinea, tweede volzin

Artikel 220, onder 2) en 3)

—

lid 3, onder a), tweede alinea

Artikel 220, onder 4) en 5)

—

lid 3, onder a), derde alinea, eerste en tweede volzin

Artikel 221, lid 1, eerste en tweede alinea

—

lid 3, onder a), vierde alinea

Artikel 221, lid 2

—

lid 3, onder a), vijfde alinea, eerste volzin

###### Art. 219

—

lid 3, onder a), vijfde alinea, tweede volzin

###### Art. 228

—

lid 3, onder a), zesde alinea

###### Art. 222

—

lid 3, onder a), zevende alinea

###### Art. 223

—

lid 3, onder a), achtste alinea, eerste en tweede volzin

Artikel 224, leden 1 en 2

—

lid 3, onder a), negende alinea, eerste en tweede volzin

Artikel 224, lid 3, eerste alinea

—

lid 3, onder a), negende alinea, derde volzin

Artikel 224, lid 3, tweede alinea

—

lid 3, onder a), tiende alinea

###### Art. 225


Artikel 214, lid 1, onder a)

Publicatieblad van de Europese Unie

lid 1, onder c), eerste streepje, eerste volzin

NL

—

L 347/106

Richtlijn 67/227/EEG

Richtlijn 77/388/EEG

Wijzigingsrichtlijnen

Andere besluiten

Deze richtlijn

—

lid 3, onder b), eerste alinea, dertiende streepje

Artikel 226, onder 13) en 14)

—

lid 3, onder b), eerste alinea, veertiende streepje

Artikel 226, onder 15)

—

lid 3, onder b), tweede alinea

###### Art. 227

—

lid 3, onder b), derde alinea

###### Art. 229

—

lid 3, onder b), vierde alinea

###### Art. 230

—

lid 3, onder b), vijfde alinea

###### Art. 231

—

lid 3, onder c), eerste alinea

###### Art. 232

—

lid 3, onder c), tweede alinea, inleidende zin

Artikel 233, lid 1, eerste alinea

—

lid 3, onder c), tweede alinea, eerste streepje, eerste volzin

Artikel 233, lid 1, eerste alinea, onder a)

—

lid 3, onder c), tweede alinea, eerste streepje, tweede volzin

Artikel 233, lid 2

—

lid 3, onder c), tweede alinea, tweede streepje, eerste volzin

Artikel 233, lid 1, eerste alinea, onder b)

—

lid 3, onder c), tweede alinea, tweede streepje, tweede volzin

Artikel 233, lid 3

—

lid 3, onder c), derde alinea, eerste volzin

Artikel 233, lid 1, tweede alinea

—

lid 3, onder c), derde alinea, tweede volzin

###### Art. 237

—

lid 3, onder c), vierde alinea, eerste en tweede volzin

###### Art. 234

—

lid 3, onder c), vijfde alinea

###### Art. 235

—

lid 3, onder c), zesde alinea

###### Art. 236

—

lid 3, onder d), eerste alinea

###### Art. 244

—

lid 3, onder d), tweede alinea, eerste volzin

Artikel 245, lid 1

L 347/107

Artikel 226, onder 1) tot en met 12)

Publicatieblad van de Europese Unie

lid 3, onder b), eerste alinea, eerste tot en met twaalfde streepje

NL

—


Richtlijn 67/227/EEG

Richtlijn 77/388/EEG

Wijzigingsrichtlijnen

Andere besluiten

Deze richtlijn

—

lid 3, onder d), derde alinea, eerste en tweede volzin

Artikel 246, eerste en tweede alinea

—

lid 3, onder d), vierde, vijfde en zesde alinea

Artikel 247, leden 1, 2 en 3

—

lid 3, onder d), zevende alinea

###### Art. 248

—

lid 3, onder e), eerste alinea

Artikelen 217 en 241

—

lid 3, onder e), tweede alinea

###### Art. 218

—

lid 4, onder a), eerste en tweede volzin

Artikel 252, lid 1

—

lid 4, onder a), derde en vierde volzin

Artikel 252, lid 2, eerste en tweede alinea

—

lid 4, onder a), vijfde volzin

Artikel 250, lid 2

—

lid 4, onder b)

Artikel 250, lid 1

—

lid 4, onder c), eerste streepje, eerste en tweede alinea

Artikel 251, onder a) en b)

—

lid 4, onder c), tweede streepje, eerste alinea

Artikel 251, onder c)

—

lid 4, onder c), tweede streepje, tweede alinea

Artikel 251, onder d) en e)

—

lid 5

###### Art. 206

—

lid 6, onder a), eerste en tweede volzin

Artikel 261, lid 1

—

lid 6, onder a), derde volzin

Artikel 261, lid 2

—

lid 6, onder b), eerste alinea

###### Art. 262

—

lid 6, onder b), tweede alinea, eerste volzin

Artikel 263, lid 1, eerste alinea

—

lid 6, onder b), tweede alinea, tweede volzin

Artikel 263, lid 2

—

lid 6, onder b), derde alinea, eerste en tweede streepje

Artikel 264, lid 1, onder a) en b)


Artikel 245, lid 2, eerste en tweede alinea

Publicatieblad van de Europese Unie

lid 3, onder d), tweede alinea, tweede en derde volzin

NL

—

L 347/108

Richtlijn 67/227/EEG

Richtlijn 77/388/EEG

Wijzigingsrichtlijnen

Andere besluiten

Deze richtlijn

—

lid 6, onder b), derde alinea, derde streepje, tweede volzin

Artikel 264, lid 2, eerste alinea

—

lid 6, onder b), vierde alinea, eerste streepje

Artikel 264, lid 1, onder c) en e)

—

lid 6, onder b), vierde alinea, tweede streepje, eerste volzin

Artikel 264, lid 1, onder f)

—

lid 6, onder b), vierde alinea, tweede streepje, tweede volzin

Artikel 264, lid 2, tweede alinea

—

lid 6, onder b), vijfde alinea, eerste en tweede streepje

Artikel 265, lid 1, onder a) en b)

—

lid 6, onder b), vijfde alinea, derde streepje, eerste volzin

Artikel 265, lid 1, onder c)

—

lid 6, onder b), vijfde alinea, derde streepje, tweede volzin

Artikel 265, lid 2

—

lid 6, onder c), eerste streepje

Artikel 263, lid 1, tweede alinea

—

lid 6, onder c), tweede streepje

###### Art. 266

—

lid 6, onder d)

###### Art. 254

—

lid 6, onder e), eerste alinea

###### Art. 268

—

lid 6, onder e), tweede alinea

###### Art. 259

—

lid 7, eerste deel van volzin

Artikel 207, eerste alinea
###### Art. 256
###### Art. 267

—

lid 7, tweede deel van volzin

Artikel 207, tweede alinea

—

lid 8, eerste en tweede alinea

Artikel 273, eerste en tweede alinea

—

lid 9, onder a), eerste alinea, eerste streepje

Artikel 272, lid 1, eerste alinea, onder c)

—

lid 9, onder a), eerste alinea, tweede streepje

Artikel 272, lid 1, eerste alinea, onder a) en d)

—

lid 9, onder a), eerste alinea, derde streepje

Artikel 272, lid 1, eerste alinea, onder b)

—

lid 9, onder a), tweede alinea

Artikel 272, lid 1, tweede alinea

L 347/109

Artikel 264, lid 1, onder d)

Publicatieblad van de Europese Unie

lid 6, onder b), derde alinea, derde streepje, eerste volzin

NL

—


Richtlijn 67/227/EEG

Richtlijn 77/388/EEG

Wijzigingsrichtlijnen

Andere besluiten

Deze richtlijn

Artikel 272, lid 3

—

lid 9, onder c)

###### Art. 212

—

lid 9, onder d), eerste alinea, eerste en tweede streepje

Artikel 238, lid 1, onder a) en b)

—

lid 9, onder d), tweede alinea, eerste tot en met vierde streepje

Artikel 238, lid 2, onder a) tot en met d)

—

lid 9, onder d), derde alinea

Artikel 238, lid 3

—

lid 9, onder e), eerste alinea

###### Art. 239

—

lid 9, onder e), tweede alinea, eerste en tweede streepje

Artikel 240, onder 1) en 2)

—

lid 10

Artikelen 209 en 257

—

lid 11

Artikelen 210 en 258

—

lid 12, inleidende zin

###### Art. 269

—

lid 12, onder a), eerste, tweede en derde streepje

Artikel 270, onder a), b) en c)

—

lid 12, onder b), eerste, tweede en derde streepje

Artikel 271, onder a), b) en c)

Artikel 28 decies, dat de derde alinea in artikel 23, lid 3, invoegt
—

lid 3, derde alinea

Artikel 283, lid 1, onder b) en c)

Publicatieblad van de Europese Unie

lid 9, onder b)

NL

—

L 347/110

Richtlijn 67/227/EEG

Artikel 28 undecies, onder 1), dat de tweede alinea in artikel 25, lid 4, invoegt —

lid 4, tweede alinea

Artikel 272, lid 2

Artikel 28 undecies, onder 2), dat artikel 25, leden 5 en 6, vervangt lid 5, eerste alinea, onder a), b) en
c)

Artikel 300, onder 1), 2) en 3)

—

lid 5, tweede alinea

###### Art. 302

—

lid 6, onder a), eerste alinea, eerste volzin

Artikel 301, lid 1

—

lid 6, onder a), eerste alinea, tweede volzin

Artikel 303, lid 1


—

Richtlijn 77/388/EEG

Wijzigingsrichtlijnen

Andere besluiten

Deze richtlijn

lid 6, onder a), tweede alinea, eerste, tweede en derde streepje

Artikel 303, lid 2, onder a), b) en c)

—

lid 6, onder a), derde alinea

Artikel 303, lid 3

—

lid 6, onder b)

Artikel 301, lid 1

Artikel 28 undecies, onder 3), dat de tweede alinea in artikel 25, lid 9, invoegt —

lid 9, tweede alinea

NL

—


Richtlijn 67/227/EEG

###### Art. 305

Artikel 28 duodecies, onder 1), tweede alinea, onder a)

Artikel 158, lid 3

Artikel 28 duodecies, onder 1), tweede alinea, onder b) en c)

—

Artikel 28 duodecies, onder 2), 3) en 4)

—

Artikel 28 duodecies, onder 5)

Artikel 158, lid 2

Artikel 28 terdecies, eerste alinea

—

Artikel 28 terdecies, tweede en derde alinea

Artikel 402, leden 1 en 2

Artikel 28 terdecies, vierde alinea

—

Artikel 28 quaterdecies

Artikel 399, eerste alinea

Artikel 28 quindecies

—

Artikel 28 sexdecies, lid 1, inleidende zin

Artikel 326, eerste alinea

Artikel 28 sexdecies, lid 1, onder a), eerste volzin

Artikel 327, leden 1 en 3

Artikel 28 sexdecies, lid 1, onder a), tweede volzin

Artikel 327, lid 2

Artikel 28 sexdecies, lid 1, onder b)

###### Art. 328

Artikel 28 sexdecies, lid 1, onder c), eerste, tweede en derde streepje

Artikel 329, onder a), b) en c)

Artikel 28 sexdecies, lid 1, onder d), eerste en tweede alinea

Artikel 330, eerste en tweede alinea

L 347/111

—

Publicatieblad van de Europese Unie

Artikel 28 duodecies, onder 1), eerste alinea

Richtlijn 77/388/EEG

Wijzigingsrichtlijnen

Andere besluiten

Deze richtlijn

###### Art. 331

Artikel 28 sexdecies, lid 1, onder g)

Artikel 4, onder b)

Artikel 28 sexdecies, lid 1, onder h)

###### Art. 35
Artikel 139, lid 3, tweede alinea

Artikel 28 sexdecies, lid 2

Artikel 326, tweede alinea

Artikel 28 sexdecies, lid 3

###### Art. 341

Artikel 28 sexdecies, lid 4

—

Artikel 28 septdecies, lid 1, eerste, tweede en derde streepje

Artikel 405, onder 1), 2) en 3)

Artikel 28 septdecies, lid 2

###### Art. 406

Artikel 28 septdecies, eerste alinea, eerste en tweede streepje

Artikel 407, onder a) en b)

Artikel 28 septdecies, lid 3, tweede alinea

—

Artikel 28 septdecies, lid 4, onder a) tot en met d)

Artikel 408, lid 1, onder a) tot en met d)

Artikel 28 septdecies, lid 5, eerste en tweede streepje

Artikel 408, lid 2, onder a) en b)

Artikel 28 septdecies, lid 6

###### Art. 409

Artikel 28 septdecies, lid 7, eerste alinea, onder a), b) en c)

Artikel 410, lid 1, onder a), b) en c)

Artikel 28 septdecies, lid 7, tweede alinea, eerste streepje

—

Artikel 28 septdecies, lid 7, tweede alinea, tweede en derde streepje

Artikel 410, lid 2, onder a) en b)

Artikel 29, leden 1 tot en met 4

Artikel 398, leden 1 tot en met 4

Artikel 29 bis

###### Art. 397

Artikel 30, lid 1

Artikel 396, lid 1

Artikel 30, lid 2, eerste en tweede volzin

Artikel 396, lid 2, eerste alinea

Artikel 30, lid 2, derde volzin

Artikel 396, lid 2, tweede alinea


Artikel 28 sexdecies, lid 1, onder f)

Publicatieblad van de Europese Unie

###### Art. 332

NL

Artikel 28 sexdecies, lid 1, onder e)

L 347/112

Richtlijn 67/227/EEG

Richtlijn 77/388/EEG

Wijzigingsrichtlijnen

Andere besluiten

Deze richtlijn

—

Artikel 31, lid 2

###### Art. 400

Artikel 33, lid 1

###### Art. 401

Artikel 33, lid 2

Artikel 2, lid 3

Artikel 33 bis, lid 1, inleidende zin

###### Art. 274

Artikel 33 bis, lid 1, onder a)

###### Art. 275

Artikel 33 bis, lid 1, onder b)

###### Art. 276

Artikel 33 bis, lid 1, onder c)

###### Art. 277

Artikel 33 bis, lid 2, inleidende zin

###### Art. 278

Artikel 33 bis, lid 2, onder a)

###### Art. 279

Artikel 33 bis, lid 2, onder b)

###### Art. 280

###### Art. 34

###### Art. 404

###### Art. 35

###### Art. 403

Artikelen 36 en 37

—

###### Art. 38

###### Art. 414

Bijlage A, onder I, onder 1) en 2)

Bijlage VII, onder 1), a) en b)

Bijlage A, onder I, onder 3)

Bijlage VII, onder 1, b) en c)

Bijlage A, onder II, onder 1) tot en met
6)

Bijlage VII, onder 2), a) tot en met f)

Bijlage A, onder III en IV

Bijlage VII, onder 3) en 4)

Bijlage A, onder IV, onder 1) tot en met
4)

Bijlage VII, onder 4), a) tot en met d)

Bijlage A, onder V

Artikel 295, lid 2

Bijlage B, inleidende zin

Artikel 295, lid 1, onder 5)

Bijlage B, eerste tot en met negende streepje

Bijlage VIII, onder 1) tot en met 9)

Bijlage C

—

L 347/113

Artikel 31, lid 1

Publicatieblad van de Europese Unie

Artikel 396, leden 3 en 4

NL

Artikel 30, leden 3 en 4


Richtlijn 67/227/EEG

Richtlijn 77/388/EEG

Wijzigingsrichtlijnen

Andere besluiten

Deze richtlijn

Bijlage X, Deel A, onder 1)

Bijlage E, onder 7)

Bijlage X, Deel A, onder 2)

Bijlage E, onder 11)

Bijlage X, Deel A, onder 3)

Bijlage E, onder 15)

Bijlage X, Deel A, onder 4)

Bijlage F, onder 1)

Bijlage X, Deel B, onder 1)

Bijlage F, onder 2)

Bijlage X, deel B, onder 2), a) tot en met j)

Bijlage F, onder 5) tot en met 8)

Bijlage X, Deel B, onder 3) tot en met 6)

Bijlage F, onder 10)

Bijlage X, Deel B, onder 7)

Bijlage F, onder 12)

Bijlage X, Deel B, onder 8)

Bijlage F, onder 16)

Bijlage X, Deel B, onder 9)

Bijlage F, onder 17), eerste en tweede alinea

Bijlage X, Deel B, onder 10)

Bijlage F, onder 23)

Bijlage X, Deel B, onder 11)

Bijlage F, onder 25)

Bijlage X, Deel B, onder 12)

Bijlage F, onder 27)

Bijlage X, Deel B, onder 13)

Bijlage G, leden 1 en 2

###### Art. 391

Bijlage H, eerste alinea

Artikel 98, lid 3

Bijlage H, tweede alinea, inleidende zin

—

Bijlage H, tweede alinea, onder 1) tot en met 6)

Bijlage III, onder 1) tot en met 6)

Bijlage H, tweede alinea, onder 7), eerste en tweede alinea

Bijlage III, onder 7) en 8)

Bijlage H, tweede alinea, onder 8) tot en met 17)

Bijlage III, onder 9) tot en met 18)

Bijlage I, inleidende zin

—

Bijlage I, onder a), eerste tot en met zevende streepje

Bijlage IX, deel A, onder 1) tot en met 7)


Bijlage E, onder 2)

Publicatieblad van de Europese Unie

Bijlage I, onder 1) tot en met 13)

NL

Bijlage D, onder 1) tot en met 13)

L 347/114

Richtlijn 67/227/EEG

Richtlijn 77/388/EEG

Wijzigingsrichtlijnen

Andere besluiten

Deze richtlijn

Bijlage I, onder c)

Bijlage IX, deel C

Bijlage J, inleidende zin

Bijlage V, inleidende zin

Bijlage J

Bijlage V, onder 1) tot en met 25)

Bijlage K, onder 1), eerste, tweede en derde streepje

Bijlage IV, onder 1), a), b) en c)

Bijlage K, onder 2) tot en met 5)

Bijlage IV, onder 2) tot en met 5)

Bijlage L, eerste alinea, onder 1) tot en met 5)

Bijlage II, onder 1) tot en met 5)

Bijlage L, tweede alinea

Artikel 56, lid 2

Bijlage M, onder a) tot en met f)

Bijlage VI, onder 1) tot en met 6)
Artikel 1, onder 1), tweede alinea, van
Richtlijn 89/465/EEG

Artikel 133, tweede alinea

Artikel 2 van Richtlijn 94/5/EG

###### Art. 342

Artikel 3, eerste en tweede volzin, van
Richtlijn 94/5/EG

Artikel 343, eerste en tweede alinea

Artikel 4 van Richtlijn 2002/38/EG

Artikel 56, lid 3
Artikel 57, lid 2
###### Art. 357

Artikel 5 van Richtlijn 2002/38/EG

—
Artikel 287, onder 1)

Bijlage VIII, deel II, onder 2), b), van de
Toetredingsakte van Griekenland

###### Art. 375

Bijlage XXXII, deel IV, onder 3), a), eerste en tweede streepje, van de Toetredingsakte van Spanje en Portugal

Artikel 287, onder 2) en 3)

Bijlage XXXII, deel IV, onder 3), b), eerste alinea, van de Toetredingsakte van Spanje en Portugal

###### Art. 377

Bijlage XV, deel IX, onder 2), b), eerste alinea, van de Toetredingsakte van Oostenrijk, Finland en Zweden

###### Art. 104

L 347/115

Bijlage VIII, deel II, onder 2), a), van de
Toetredingsakte van Griekenland

Publicatieblad van de Europese Unie

Bijlage IX, deel B, onder 1) en 2)

NL

Bijlage I, onder b), eerste en tweede streepje


Richtlijn 67/227/EEG

Richtlijn 77/388/EEG

Wijzigingsrichtlijnen

Andere besluiten

Deze richtlijn

Artikel 287, onder 4)

Bijlage XV, deel IX, onder 2), f), eerste alinea, van de Toetredingsakte van Oostenrijk, Finland en Zweden

Artikel 117, lid 1

Bijlage XV, deel IX, onder 2), g), eerste alinea, van de Toetredingsakte van Oostenrijk, Finland en Zweden

###### Art. 119

Bijlage XV, deel IX, onder 2), h), eerste alinea, eerste en tweede streepje, van de Toetredingsakte van Oostenrijk, Finland en Zweden

Artikel 378, lid 1

Bijlage XV, deel IX, onder 2), i), eerste alinea, eerste streepje, van de Toetredingsakte van Oostenrijk, Finland en Zweden

—

Bijlage XV, deel IX, onder 2), i), eerste alinea, tweede en derde streepje, van de Toetredingsakte van Oostenrijk, Finland en Zweden

Artikel 378, lid 2, onder a) en b)

Bijlage XV, deel IX, onder 2), j), van de
Toetredingsakte van Oostenrijk, Finland en Zweden

Artikel 287, onder 5)

Bijlage XV, deel IX, onder 2), l), eerste alinea, van de Toetredingsakte van Oostenrijk, Finland en Zweden

Artikel 111, onder a)

Bijlage XV, deel IX, onder 2), m), eerste alinea, van de Toetredingsakte van Oostenrijk, Finland en Zweden

Artikel 379, lid 1

Bijlage XV, deel IX, onder 2), n), eerste alinea, eerste en tweede streepje, van de Toetredingsakte van Oostenrijk, Finland en Zweden

Artikel 379, lid 2

Bijlage XV, deel IX, onder 2), x), eerste streepje, van de Toetredingsakte van Oostenrijk, Finland en Zweden

###### Art. 253

Bijlage XV, deel IX, onder 2), x), tweede streepje, van de Toetredingsakte van Oostenrijk, Finland en Zweden

Artikel 287, onder 6)

NL

Bijlage XV, deel IX, onder 2), c), eerste alinea, van de Toetredingsakte van Oostenrijk, Finland en Zweden

L 347/116

Richtlijn 67/227/EEG

Publicatieblad van de Europese Unie

Richtlijn 77/388/EEG

Wijzigingsrichtlijnen

Andere besluiten

Deze richtlijn

Artikel 111, onder b)

Bijlage XV, deel IX, onder 2), aa), eerste alinea, eerste en tweede streepje, van de Toetredingsakte van Oostenrijk, Finland en Zweden

###### Art. 380

Protocol nr. 2 van de Toetredingsakte van Oostenrijk, Finland en Zweden

Artikel 6, lid 1, onder d)

Bijlage V, lid 5, onder 1), a), van de
Toetredingsakte van Tsjechië, Estland,
Cyprus, Letland, Litouwen, Hongarije,
Malta, Polen, Slovenië en Slowakije

###### Art. 123

Bijlage V, lid 5, onder 1), b), van de
Toetredingsakte van 2003

###### Art. 381

Bijlage VI, lid 7, onder 1), a), van de
Toetredingsakte van 2003

###### Art. 124

Bijlage VI, lid 7, onder 1), b), van de
Toetredingsakte van 2003

###### Art. 382

Bijlage VII, lid 7, onder 1), eerste en tweede alinea, van de Toetredingsakte van 2003

Artikel 125, leden 1 en 2

Bijlage VIII, lid 7, onder 1), derde alinea, van de Toetredingsakte van 2003

—

Bijlage VII, lid 7, onder 1), vierde alinea, van de Toetredingsakte van 2003

Artikel 383, onder a)

Bijlage VII, lid 7, onder 1), vijfde alinea, van de Toetredingsakte van 2003

—

Bijlage VII, lid 7, onder 1), zesde alinea, van de Toetredingsakte van 2003

Artikel 383, onder b)

Bijlage VIII, lid 7, onder 1), a), van de
Toetredingsakte van 2003

—

Bijlage VIII, lid 7, onder 1), b), tweede alinea, van de Toetredingsakte van 2003

Artikel 384, onder a)

Bijlage VIII, lid 7, onder 1), derde alinea, van de Toetredingsakte van 2003

Artikel 384, onder b)

Bijlage IX, lid 8, onder 1), van de
Toetredingsakte van 2003

###### Art. 385

NL

Bijlage XV, deel IX, onder 2), z), eerste alinea, van de Toetredingsakte van Oostenrijk, Finland en Zweden


Richtlijn 67/227/EEG

Publicatieblad van de Europese Unie
L 347/117

Richtlijn 77/388/EEG

Wijzigingsrichtlijnen

Andere besluiten

Deze richtlijn

Bijlage X, lid 7, onder 1) c), van de
Toetredingsakte van 2003

###### Art. 386

Bijlage XI, lid 7, onder 1), van de
Toetredingsakte van 2003

###### Art. 127

Bijlage XI, lid 7, onder 2), a), van de
Toetredingsakte van 2003

Artikel 387, onder c)

Bijlage XI, lid 7, onder 2), b), van de
Toetredingsakte van 2003

Artikel 387, onder a)

Bijlage XI, lid 7, onder 2), c), van de
Toetredingsakte van 2003

Artikel 387, onder b)

Bijlage XII, lid 9, onder 1), a), van de
Toetredingsakte van 2003

Artikel 128, leden 1 en 2

Bijlage XII, lid 9, onder 1), b), van de
Toetredingsakte van 2003

Artikel 128, leden 3, 4 en 5

Bijlage XII, lid 9, onder 2), van de
Toetredingsakte van 2003

###### Art. 388

Bijlage XIII, lid 9, onder 1), a), van de
Toetredingsakte van 2003

Artikel 129, leden 1 en 2

Bijlage XIII, lid 9, onder 1), b), van de
Toetredingsakte van 2003

###### Art. 389

Bijlage XIV, lid 7, eerste alinea, van de
Toetredingsakte van 2003

Artikel 130, onder a) en b)

Bijlage XIV, lid 7, tweede alinea, van de
Toetredingsakte van 2003

—

Bijlage XIV, lid 7, derde alinea, van de
Toetredingsakte van 2003

###### Art. 390

Publicatieblad van de Europese Unie

Artikel 126, onder a) en b)

NL

Bijlage X, lid 7, onder 1), a), onder i) en ii), van de Toetredingsakte van 2003

L 347/118

Richtlijn 67/227/EEG


