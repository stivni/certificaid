---
bron: https://www.cbn-cnc.be/nl/adviezen/transacties-onder-gemeenschappelijke-leiding-common-control-transactions-update
datum: 2017-09-13
nummer: CBN-advies 2017/15
provenance:
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/transacties-onder-gemeenschappelijke-leiding-common-control-transactions-update
      sha256: e34d71c0b915d2915bedf5f2e0faf1e45742e2108099e419f5bcf364e08f69b4
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
    confirmed_at: '2026-05-11T17:13:30Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "A6/G3: regel 59 (body) bevat ', bijgewerkt op 10 september 2025[^2]' als orphan-zin direct na de H1 — scraper-artefact. E1/E2: de drie balans-tabellen (regels 73-76, 82-83, 89-93) zijn malformed — meerdere data-kolommen aaneengeregen in één pipe-rij zonder correcte kolom-scheiding, tabel rendert niet als multi-kolom tabel. D4: regel 104 bevat '*pooling of interest[^5]*  methode' met dubbele spatie na sluitende asterisk."
    layer1:
      file_size_chars: 8767
      flags: []
      heading_count: 3
      max_section_chars: 4117
      run_at: '2026-05-11T15:05:53Z'
      run_id: 20260511-150547
      status: pass
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-11T17:13:30Z'
      rationale: "A6/G3: regel 59 (body) bevat ', bijgewerkt op 10 september 2025[^2]' als orphan-zin direct na de H1 — scraper-artefact. E1/E2: de drie balans-tabellen (regels 73-76, 82-83, 89-93) zijn malformed — meerdere data-kolommen aaneengeregen in één pipe-rij zonder correcte kolom-scheiding, tabel rendert niet als multi-kolom tabel. D4: regel 104 bevat '*pooling of interest[^5]*  methode' met dubbele spatie na sluitende asterisk."
      concrete_problemen:
        - regel: 59
          categorie: A6
          type: other
          voorbeeld: ', bijgewerkt op 10 september 2025[^2]'
        - regel: 73
          categorie: E2
          type: other
          voorbeeld: '| Positief consolidatieverschil | | 100 | | Eigen vermogen | | 80 |'
        - regel: 104
          categorie: D4
          type: other
          voorbeeld: '*pooling of interest[^5]*  methode te gebruiken bij een bedrijfscombinatie'
themas:
  - bedrijfscombinatie
  - common control transactie
  - consolidatie
  - gemeenschappelijke leiding
  - goodwill
  - overname
  - pooling of interest
  - consolidatieverschil
  - groottecriteria
---

# CBN-advies 2017/15 – Transacties onder gemeenschappelijke leiding (Common control transactions) (update)

, bijgewerkt op 10 september 2025[^2]

## Inleiding

Een “bedrijfscombinatie onder gemeenschappelijke leiding” is een bedrijfscombinatie waarin de uiteindelijke zeggenschap over alle bij de bedrijfscombinatie betrokken entiteiten of bedrijven door dezelfde partij of partijen wordt uitgeoefend, zowel voor als na de bedrijfscombinatie.[^3] 

Een bedrijfscombinatie, of *business combination*, is een transactie of andere gebeurtenis waarin een overnemende partij zeggenschap verkrijgt over een of meer bedrijven. In de Nederlandstalige terminologie spreken we over een overname. 

## Voorbeeld

De verkorte geconsolideerde balans van Holdco I per 31 december 20X0, in miljoenen EUR is als volgt:

| 31 december 20X0 | 
|---|
| Positief consolidatieverschil | | 100 | | Eigen vermogen | | 80 | 
| Materiële vaste activa | | 60 | | Vreemd vermogen | | 200 | 
| Vorderingen | | 120 | | | | | 
| | | 280 | | | | 280 | 

Per 1 januari 20X1 verwerft Holdco II de controle over Holdco I voor een bedrag van 600 miljoen EUR. De enkelvoudige balans van Holdco II kan per 1 januari 20X1 als volgt voorgesteld worden:

| 1 januari 20X1 | 
|---|
| Belang in Holdco I | | 600 | | Eigen vermogen | | 600 | 
| | | 600 | | | | 600 | 

De geconsolideerde balans van Holdco II kan als volgt voorgesteld worden per 1 januari 20X1:

| 1 januari 20X1 | 
|---|
| Positief consolidatieverschil II | | 520 | | Eigen vermogen | | 600 | 
| Positief consolidatieverschil I | | 100 | | Vreemd vermogen | | 200 | 
| Materiële vaste activa | | 60 | | | | | 
| Vorderingen | | 120 | | | | | 
| | | 800 | | | | 800 | 

De problematiek van een transactie onder gemeenschappelijke leiding situeert zich rond de erkenning van *het positief consolidatieverschil II* in de geconsolideerde balans van Holdco II. Mathematisch is deze immers ontstaan door het verschil tussen het verworven sub-geconsolideerd nettoactief van Holdco I, 80, en de overnameprijs van 600, hetgeen 520 geeft. 

Door het feit dat zowel voor als na de transactie dezelfde natuurlijk persoon nog steeds de controle heeft over Holdco I, en de respectievelijke Opco’s is er geen reden tot de uitdrukking van *het positief consolidatieverschil II* in de geconsolideerde balans van Holdco II.[^4] 

Richtlijn 2013/34/EU van 26 juni 2013 van het Europees Parlement en van de Raad betreffende de jaarlijkse financiële overzichten, geconsolideerde financiële overzichten en aanverwante verslagen van bepaalde ondernemingsvormen, tot wijziging van Richtlijn 2006/43/EG van het Europees Parlement en de Raad en tot intrekking van Richtlijnen 78/660/EEG en 83/349/EEG van de Raad stelt in artikel 25 het volgende: 

“1. De lidstaten kunnen toestaan of voorschrijven dat de boekwaarden van aandelen in het kapitaal van een in een consolidatie opgenomen onderneming slechts worden verrekend met het daarin belichaamde deel van het kapitaal, op voorwaarde dat de uiteindelijke zeggenschap over de ondernemingen in de bedrijfscombinatie door dezelfde partij wordt uitgeoefend, zowel voor als na de bedrijfscombinatie, en die zeggenschap niet tijdelijk is.
2. Eventuele uit de toepassing van lid 1 voortvloeiende verschillen worden, naar gelang van het geval, aan de geconsolideerde reserves toegevoegd dan wel daarop in mindering gebracht.
3. Het feit dat de in lid 1 beschreven methode is toegepast, de mutaties die daaruit voor de reserves voortvloeien en de naam en de zetel van de betrokken ondernemingen worden in de toelichting bij de geconsolideerde financiële overzichten vermeld”.
Richtlijn 2013/34/EU staat daardoor toe de zogenaamde *pooling of interest[^5]*  methode te gebruiken bij een bedrijfscombinatie onder gemeenschappelijke leiding, hetgeen wordt bevestigd in considerans 29: 

“Bij gebrek aan prijsvorming zoals in een transactie tussen onafhankelijke partijen, dienen de lidstaten evenwel het recht te krijgen om toe te staan dat de verslaglegging over intra-groepsoverdrachten van deelnemingen, ook transacties tussen ondernemingen onder gemeenschappelijke zeggenschap genoemd, geschiedt door gebruik te maken van de boekhoudkundige methode van pooling of interest (samenvoeging van belangen) volgens dewelke de boekwaarde van aandelen in het kapitaal van een in een consolidatie opgenomen onderneming slechts wordt verrekend tegen het daarmee overeenstemmende deel van het kapitaal”.
België heeft er naar aanleiding van de omzetting niet voor geopteerd gebruik te maken van deze lidstaatoptie. 

## Verband met de berekening van de groottecriteria bij transacties onder gemeenschappelijke leiding

Artikel 1:24 van het Wetboek van vennootschappen en verenigingen (hierna: WVV) definieert op basis van het jaargemiddelde van het aantal werknemers, de jaarlijkse netto-omzet en het balanstotaal kleine vennootschappen. Volgens artikel 1:24, § 1 WVV zijn kleine vennootschappen deze met rechtspersoonlijkheid die op balansdatum van het laatst afgesloten boekjaar niet meer dan één van de volgende criteria overschrijden:

- jaargemiddelde van het aantal werknemers: 50; 
- jaarlijkse netto-omzet, exclusief btw: 11.250.000 euro; 
- balanstotaal: 6.000.000 euro. 

De beoordeling van de criteria inzake omzet en balanstotaal op geconsolideerde basis geldt in principe uitsluitend voor moedervennootschappen in de zin van artikel 1:15, 1° WVV[^6] en niet voor de andere verbonden vennootschappen indien deze zelf geen moedervennootschappen zijn. 

Een beoordeling van de groottecriteria op geconsolideerde basis impliceert niet dat de moedervennootschap effectief een geconsolideerde jaarrekening moet opstellen. Met het oog op de vermindering van de administratieve lasten voor ondernemingen biedt artikel 1:24, § 6, tweede lid WVV de mogelijkheid om een vereenvoudigde berekeningsmethode toe te passen.[^7] 

Zowel voor de berekening op geconsolideerde basis als voor de berekening op geaggregeerde basis van de criteria opgenomen in art. 1:24 WVV, zal een transactie onder gemeenschappelijke leiding steeds tot gevolg hebben dat het geconsolideerd of geaggregeerd balanstotaal te hoog wordt voorgesteld. 

Zoals aangegeven onder randnummer 5 heeft België er niet voor geopteerd om de lidstaatoptie omtrent *pooling of interest* toe te passen. Echter kan het erkende positieve consolidatieverschil vanuit een bedrijfseconomisch standpunt niet gejustifieerd worden in de geconsolideerde jaarrekening. De Commissie is dan ook van oordeel dat op basis van artikel 3:131, § 1, tweede lid KB WVV dit positief consolidatieverschil onmiddellijk dient te worden afgeschreven daar het niet economisch verantwoord is om deze te handhaven in de geconsolideerde balans.[^8] 

Het lijkt de Commissie aangewezen om deze afschrijvingskost in de geconsolideerde jaarrekening op grond van artikel 1:131, § 1, derde lid KB WVV onder de *Niet-recurrente bedrijfskosten* of *Niet-recurrente financiële kosten* te presenteren alsook een toelichting rond de verwerkingswijze van* common control* transactie te verstrekken.

[^1]: Onderhavig advies is tot stand gekomen nadat een ontwerp van het advies op 13 juni 2017 ter consultatie werd gepubliceerd op de website van de CBN.

[^2]: Onderhavig geactualiseerd advies is tot stand gekomen nadat het ontwerpadvies op 8 mei 2025 ter publieke consultatie werd gepubliceerd op de website van de CBN.

[^3]: IFRS 3 Bedrijfscombinaties, paragraaf B1.

[^4]: Dit is dan ook het voornaamste argument waarom IFRS 3 Bedrijfscombinaties de erkenning van een positief consolidatieverschil niet toelaat in een zogenaamde common control transactie (IFRS 3.2, c).

[^5]: Onder IFRS wordt deze methode in de praktijk meestal gehanteerd, doch deze wordt niet formeel door de IASB als methode naar voor geschoven voor de verwerking van een combinatie van entiteiten of bedrijven waarover gezamenlijk de zeggenschap wordt uitgeoefend.

[^6]: Ofwel voor Holdco I en II in het aangehaalde voorbeeld.

[^7]: CBN-advies 2022/03 - Beoordeling van de groottecriteria overeenkomstig artikelen 1:24 en 1:25 van het Wetboek van vennootschappen en verenigingen, 19 januari 2022, spreekt in dit geval van een berekening op geaggregeerde basis.

[^8]: Het positief consolidatieverschil kan niet rechtstreeks worden afgeboekt van de consolidatiereserves aangezien deze mogelijkheid (als gevolg van het niet lichten van de lidstaatoptie omtrent pooling of interest) niet werd voorzien in de Belgische wetgeving. De niet-recurrente afschrijving van het positief consolidatieverschil ontstaan uit een transactie onder gemeenschappelijke leiding, opgenomen onder de niet-recurrente bedrijfskosten of niet-recurrente financiële kosten, moet (indien significant) in de toelichting worden vermeld (artikel 3:156, XII. KB WVV).
