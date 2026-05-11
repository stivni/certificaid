---
bron: https://www.cbn-cnc.be/nl/adviezen/toevoegingen-en-onttrekkingen-boekhoudkundige-verwerking
datum: 1985-09-01
gerelateerde_adviezen:
  - datum: '2021-07-12'
    titel: Boekhoudrechtelijke verwerking van de wederopbouwreserve
    url: https://www.cbn-cnc.be/nl/adviezen/boekhoudrechtelijke-verwerking-van-de-wederopbouwreserve
  - datum: '2021-05-12'
    titel: Invloed van het buitengerechtelijk minnelijk akkoord en de gerechtelijke reorganisatie op de schulden en vorderingen (update)
    url: https://www.cbn-cnc.be/nl/adviezen/invloed-van-het-buitengerechtelijk-minnelijk-akkoord-en-de-gerechtelijke-reorganisatie-1
  - datum: '2018-05-30'
    titel: Tax shelter voor podiumkunsten
    url: https://www.cbn-cnc.be/nl/adviezen/tax-shelter-voor-podiumkunsten
  - datum: '2018-03-21'
    titel: Aftrek voor innovatie-inkomsten
    url: https://www.cbn-cnc.be/nl/adviezen/aftrek-voor-innovatie-inkomsten
nummer: CBN-advies 131/2
provenance:
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/toevoegingen-en-onttrekkingen-boekhoudkundige-verwerking
      sha256: e5d9c1109c84f82c4e79ce025649017333d189c32af26b16f1980baf13296ab2
      version:
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: 3b788cd
    model:
    prompt_version:
  generated_at: '2026-05-11T13:15:10Z'
  stale: false
  stale_reason:
  trust:
    status: needs-rework
    confirmed_at: '2026-05-11T13:16:02Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "B2: heading-hiërarchie springt van H1 direct naar H4 ('#### Over de stijving...' op L72, '#### Over onttrekkingen...' op L78) zonder tussenliggende H2/H3 — onnatuurlijk voor mens-geschreven markdown. Additioneel: L68 heeft 'een speciale rubriek* Overboeking...' zonder spatie voor de openende '*', wat italic-parsing kan breken (D4-adjacent). B2 is het primaire ETL-bug."
    layer1:
      status: pass
      run_id: 20260511-131513
      run_at: '2026-05-11T13:15:14Z'
      heading_count: 2
      max_section_chars: 2629
      file_size_chars: 4060
      flags: []
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-11T13:16:02Z'
      rationale: "B2: heading-hiërarchie springt van H1 direct naar H4 ('#### Over de stijving...' op L72, '#### Over onttrekkingen...' op L78) zonder tussenliggende H2/H3 — onnatuurlijk voor mens-geschreven markdown. Additioneel: L68 heeft 'een speciale rubriek* Overboeking...' zonder spatie voor de openende '*', wat italic-parsing kan breken (D4-adjacent). B2 is het primaire ETL-bug."
      concrete_problemen:
        - regel: 72
          categorie: B2
          type: other
          voorbeeld: '#### Over de stijving van de belastingvrije reserves (H1 → H4, geen H2/H3)'
        - regel: 78
          categorie: B2
          type: other
          voorbeeld: '#### Over onttrekkingen aan de belastingvrije reserves (idem)'
        - regel: 68
          categorie: D4
          type: other
          voorbeeld: een speciale rubriek* Overboeking naar de belastingvrije reserves* (geen spatie na 'rubriek')
themas:
  - belastingvrije reserves
  - onttrekking aan de belastingvrije reserves
  - toevoeging aan de belastingvrije reserves
---

# CBN-advies 131/2 - Toevoegingen en onttrekkingen - Boekhoudkundige verwerking

Krachtens het koninklijk besluit van 8 oktober 1976 moeten belastingvrije reserves, dat zijn de gerealiseerde meerwaarden en de winsten die belastingvrij zijn indien ze in het vermogen van de onderneming blijven, in een afzonderlijke rubriek op de passiefzijde van de balans worden geboekt. 

Het schema van de resultatenrekening bevat, onder de rubriek *Winst (verlies) van het boekjaar*, een speciale rubriek* Overboeking naar de belastingvrije reserves*. Daarin opgenomen bedragen worden afgetrokken van het bedrag van de winst (het verlies) van het boekjaar om de te bestemmen winst (het te verwerken verlies) vast te stellen. 

In dit verband rezen twee vragen : 

#### Over de stijving van de belastingvrije reserves 

Moeten de belastingvrije reserves worden gestijfd via deze rubriek van de resultatenrekening of mag dit ook via de resultaatverwerking, met de rubriek C.2. van het schema «Toevoeging aan de reserves», inzonderheid wanneer in fiscaal opzicht geen bezwaar bestaat tegen de stijving van deze reserves via de resultaatverwerking ? 

De Commissie is van oordeel dat met de invoering van deze rubriek door het besluit van 12 september 1983 en op grond van haar omschrijving, bedoeld wordt dat elke overboeking naar de belastingvrije reserves via deze rubriek moet gebeuren. 

#### Over onttrekkingen aan de belastingvrije reserves

Een onttrekking aan de belastingvrije reserves kan bedoeld zijn om deze reserves een andere bestemming te geven, bij voorbeeld dekking van een verlies of uitkering van een dividend aan de vennoten; zij kan ook ingegeven zijn door strikt fiscale overwegingen : belastingvrijdom verzaken door de belastingvrije reserves om te vormen tot een reserve waarvoor de normale fiscale regeling geldt. Onttrekking kan ook voortvloeien uit een gehele of gedeeltelijke toevoeging van de belastingvrije reserves aan het kapitaal. 

- zij is de duidelijkste uitdrukking van de aard van de betrokken verrichting; deze onttrekking toerekenen op een andere post van de resultatenrekening zou een verkeerd beeld geven van de oorsprong van het resultaat; 
- toerekening op de resultaatverwerking - a priori een rechtstreekse overboeking naar een beschikbare reserve - zou voor gevolg hebben dat de verplichting niet werd nageleefd om - binnen de wettelijke beperkingen - de wettelijke reserve te stijven met een gedeelte van de resultaten. In de mate waarin dergelijke onttrekking een weerslag heeft op het bedrag aan verschuldigde belastingen voor het boekjaar, past het overigens deze weerslag te relateren aan de verdwijning van de belastingvrijdom. 

Bij gebrek aan een speciale rubriek voor onttrekkingen aan de belastingvrije reserves rees de vraag hoe dergelijke onttrekkingen in de jaarrekening moeten worden uitgedrukt. De Commissie is van oordeel dat - bij gebruik van het resultatenrekeningschema in staffelvorm - de meest geschikte oplossing erin bestaat de rubriek *Overboeking naar de belastingvrije reserves* (rekening 68) te vervangen door de rubriek XII *Onttrekking aan de belastingvrije reserves* (rekening 78). Wordt het resultatenrekeningschema in scontrovorm gebruikt, dan moet aan de opbrengsten een rubriek XII *Onttrekking aan de belastingvrije reserves* (rekening 78) worden toegevoegd. 

Voor deze voorstelling pleiten volgende argumenten : Worden tijdens eenzelfde boekjaar bedragen toegevoegd of onttrokken aan de belastingvrije reserves dan moeten deze verrichtingen afzonderlijk in de boekhouding van de onderneming worden ingeschreven. In de jaarrekening mogen zij echter in eenzelfde rubriek worden gegroepeerd. 

In principe gelden bovenstaande argumenten ook als het de bedoeling is de belastingvrije reserves geheel of gedeeltelijk aan het kapitaal toe te voegen. Deze toevoeging mag echter zonder bezwaar gebeuren door rechtstreekse overboeking van de rekening *Belastingvrije reserves* naar de rekening *Kapitaal*, mochten anders de voorwaarden voor het behoud van de belastingvrijdom niet meer vervuld zijn.
