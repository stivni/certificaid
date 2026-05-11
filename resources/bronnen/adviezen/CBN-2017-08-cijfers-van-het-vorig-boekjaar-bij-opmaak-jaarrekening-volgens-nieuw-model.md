---
bron: https://www.cbn-cnc.be/nl/adviezen/cijfers-van-het-vorig-boekjaar-bij-opmaak-jaarrekening-volgens-nieuw-model
datum: 2017-03-15
gerelateerde_adviezen:
  - datum: '2022-03-15'
    titel: Beoordeling van de groottecriteria overeenkomstig artikelen 1:24 en 1:25 van het Wetboek van vennootschappen en verenigingen
    url: https://www.cbn-cnc.be/nl/adviezen/beoordeling-van-de-groottecriteria-overeenkomstig-artikelen-124-en-125-van-het-wetboek-van
  - datum: '2019-11-06'
    titel: Groottecriteria verenigingen en stichtingen - schema van de jaarrekening - begroting
    url: https://www.cbn-cnc.be/nl/adviezen/groottecriteria-verenigingen-en-stichtingen-schema-van-de-jaarrekening-begroting
nummer: CBN-advies 2017/08
provenance:
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/cijfers-van-het-vorig-boekjaar-bij-opmaak-jaarrekening-volgens-nieuw-model
      sha256: aa0dbd637f6bd1d94798fa80f37ddfbbfe3c609ad14a91465da7f47257dc3f56
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
    confirmed_at: '2026-05-11T15:23:43Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "B3: regel 73 bevat 'bij opmaak jaarrekening volgens nieuw model' als losstaande alinea direct na H1 — duplicaat van de ondertitel, extractie-artefact. A6: regels 79-80 en 86-87 bevatten spurious line-breaks na voetnootreferenties ('plaatsvindt.[^3]\\n Daarnaast' en '[^5]\\n Dit leidt ertoe') midden in zinnen. Klein advies, inhoud compleet."
    layer1:
      file_size_chars: 4127
      flags: []
      heading_count: 2
      max_section_chars: 2047
      run_at: '2026-05-11T15:05:52Z'
      run_id: 20260511-150547
      status: pass
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-11T15:23:43Z'
      rationale: "B3: regel 73 bevat 'bij opmaak jaarrekening volgens nieuw model' als losstaande alinea direct na H1 — duplicaat van de ondertitel, extractie-artefact. A6: regels 79-80 en 86-87 bevatten spurious line-breaks na voetnootreferenties ('plaatsvindt.[^3]\\n Daarnaast' en '[^5]\\n Dit leidt ertoe') midden in zinnen. Klein advies, inhoud compleet."
      concrete_problemen:
        - regel: 73
          categorie: B3
          type: other
          voorbeeld: bij opmaak jaarrekening volgens nieuw model
        - regel: 79
          categorie: A6
          type: other
          voorbeeld: "wijziging plaatsvindt.[^3]\n Daarnaast wordt er voor het volledige"
        - regel: 86
          categorie: A6
          type: other
          voorbeeld: "die aanvatten op of na 1 januari 2016.[^5]\n Dit leidt ertoe"
themas:
  - consistentiebeginsel
  - vergelijkende cijfers
---

# CBN-advies 2017/08 – Cijfers van het vorig boekjaar bij opmaak jaarrekening volgens nieuw model

bij opmaak jaarrekening volgens nieuw model

## Inleiding

Het koninklijk besluit van 18 december 2015 tot omzetting van Richtlijn 2013/34/EU van 26 juni 2013 van het Europees Parlement en van de Raad betreffende de jaarlijkse financiële overzichten, geconsolideerde financiële overzichten en aanverwante verslagen van bepaalde ondernemingsvormen, tot wijziging van Richtlijn 2006/43/EG van het Europees Parlement en de Raad en tot intrekking van Richtlijnen 78/660/EEG en 83/349/EEG van de Raad[^2], heeft een aantal wijzigingen aangebracht aan het volledige en verkorte schema van de balans- en resultatenrekening. Daarnaast werd tevens het microschema ontwikkeld.

Zo worden in het verkorte en volledige schema de uitzonderlijke resultaten geschrapt als afzonderlijke rubriek van de resultatenrekening en worden deze ondergebracht onder de bedrijfsresultaten dan wel de financiële resultaten. Ze worden voortaan aangeduid als niet-recurrente resultaten, evenwel zonder dat op inhoudelijk vlak, i.e. met betrekking tot de kwalificatie, een wijziging plaatsvindt.[^3]
 Daarnaast wordt er voor het volledige en verkorte schema van de balans een verdere uitsplitsing gevraagd binnen de voorzieningen. Voor wat betreft het verkorte schema en het microschema wordt er binnen de financiële opbrengsten tevens een aparte lijn toegevoegd die betrekking heeft op de recurrente financiële opbrengsten afkomstig van kapitaal- en interestsubsidies.

Als gevolg van de nieuwe rubriceringen en de introductie van het schema voor de microvennootschappen zullen de vergelijkende cijfers bij de jaarrekening die wordt neergelegd over het boekjaar dat aanvangt op of na 1 januari 2016 niet meer overeenstemmen met de rubricering in de jaarrekening die werd neergelegd over het boekjaar dat aanving vóór 1 januari 2016 en dus als vergelijkend boekjaar zal fungeren voor boekjaren die aanvatten op of na 1 januari 2016.

## Identieke voorstelling van de jaarrekening van het ene jaar tot het andere

Artikel 86 van het koninklijk besluit ter uitvoering van het Wetboek van vennootschappen (hierna: KB W.Venn.) stelt dat de voorstelling van de jaarrekening identiek moet zijn van het ene tot het andere jaar. De Commissie is van oordeel dat de toepassing van dit consistentiebeginsel[^4] als gevolg van de omzetting van Richtlijn 2013/34/EU van 26 juni 2013 niet werd aangetast. Immers zal de vennootschap de bedragen van het voorafgaande boekjaar tevens moeten presenteren conform de presentatievereisten toepasbaar vanaf 1 januari 2016.[^5]
 Dit leidt ertoe dat de vergelijkbaarheid van de cijfers tussen het huidige en het voorafgaande boekjaar behouden blijft en er derhalve bevestigend kan worden geantwoord op de vraag of de bedragen van het vorige boekjaar identiek zijn met die welke eerder openbaar werden gemaakt[^6] daar de aanpassing afkomstig is ten gevolge een uitsplitsing, een hergroepering of een verschuiving binnen het jaarrekeningschema. 

[^1]: Onderhavig advies is tot stand gekomen nadat een ontwerp van het advies op 3 februari 2017 ter consultatie werd gepubliceerd op de website van de CBN.

[^2]: Hierna: koninklijk besluit van 18 december 2015, BS 30 december 2015.

[^3]: Het gaat hier dus om wijziging in de presentatie die gepaard gaat met een wijziging van de benaming.

[^4]: Voor wat betreft een wijziging in de waarderingsregels als gevolg van een gewijzigde wetgeving, verwijst de Commissie naar haar CBN-advies 154/1 – Wijziging van de waarderingsregels als gevolg van gewijzigde wetgeving, Bulletin CBN, nr. 23, december 1988, 14-15.

[^5]: Als gevolg hiervan is de Commissie van oordeel dat artikel 83, tweede lid KB W.Venn. geen toepassing kent daar het jaarrekeningschema voor het vergelijkende jaar niet zal overeenstemmen met presentatievereisten die van toepassing waren op het ogenblik dat de jaarrekening van het vergelijkende jaar werd opgesteld.

[^6]: Ervan uitgaande dat er geen enkele andere wijziging heeft plaatsgevonden welke mogelijks wel een inbreuk zou vormen op het consistentiebeginsel.
