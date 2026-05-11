---
bijgewerkt: 29.04.2024
bron: ejustice.just.fgov.be (gecoördineerde versie)
bron_rol: itaa_lex
chunk:
  level: 6
  sub_strategy: null
  type: Art.
itaa-lex-sectie: VI.C
provenance:
  generated_at: '2026-05-11T16:34:24Z'
  inputs:
  - id: resources/raw/wetteksten/btw-kbs/WBTW-MB-compilatie.pdf
    sha256: e2e322b0d748d0314e5f16d11a0aac6c964d684451d00738c9352b4f32f9171c
    version: 29.04.2024
  stale: false
  stale_reason: null
  tooling:
    model: null
    pipeline: tools/etl/convert.py
    pipeline_version: ec1f304
    prompt_version: null
  trust:
    confirmed_at: '2026-05-09T21:27:46Z'
    confirmed_by: subagent-sonnet-4-6
    layer1:
      file_size_chars: 52317
      flags: []
      heading_count: 135
      max_section_chars: 2386
      run_at: '2026-05-11T13:40:48Z'
      run_id: 20260511-134044
      status: pass
    layer2:
      agent: null
      concrete_problemen: []
      rationale: 'Goed gestructureerd: 135 headings tot ###### Art.-niveau, max sectie
        2386 chars. Compilatiebestand met TITEL/HOOFDSTUK/AFDELING-hierarchie + per-artikel-headings.'
      run_at: null
      status: trusted
    rationale: L1=pass
    status: trusted
status: beschikbaar
tags:
- VI.C
- '2.4'
wet: Ministeriële besluiten inzake belasting over de toegevoegde waarde (compilatie
  Fisconet, bijgewerkt t.e.m. 29.04.2024)
---

# Ministeriële besluiten inzake belasting over de toegevoegde waarde (compilatie Fisconet, bijgewerkt t.e.m. 29.04.2024)

*Bijgewerkt tot en met 29.04.2024 — gecoördineerde versie.*

#### Afdeling 3. - Identificatie van het kassasysteem

###### Art. 46

Elk kassasysteem moet voorzien zijn van een modelaanduiding en een productienummer. Dit productienummer moet een uniek nummer zijn waarmee zowel het kassasysteem als de producent ervan éénduidig wordt geïdentificeerd. Het productienummer wordt als volgt opgebouwd: CXXXNNNPPPPPP waarbij: - CXXX = identificatienummer producent van een kassasysteem (op aanvraag verstrekt door de administratie);
- NNN = volgnummer, door de administratie toegekend aan het model;
- PPPPPPP = alfanumeriek uniek productienummer (gebaseerd op serienummer of licentiesleutel).
Dit unieke productienummer moet op elk opgesteld kassasysteem duidelijk zichtbaar zijn of op eenvoudige manier raadpleegbaar zijn (procedure voor te leggen door de producent).

###### Art. 47
De kassasoftware moet voorzien zijn van een versienummer. Dit versienummer moet een unieke aanduiding zijn van een softwareversie en bij elke wijziging van de software worden aangepast.
Het versienummer van de kassasoftware en de naam van de producent van het programma moeten gemakkelijk kunnen worden afgelezen. De softwareversie dient gemakkelijk opvraagbaar te zijn of minstens duidelijk vermeld te worden op het aanmeldingsscherm. Deze versiegegevens worden bij elke communicatie met de FDM meegestuurd.

    - MB 29.04.2024 / 16 -
FOD Financiën (AA BEO) www.fisconetplus.be Btw MB 29.04.2024 – Bijw. nr. 1 / 03.06.2024

#### Afdeling 4. - Communicatie met de Fiscal Data Module

###### Art. 48
Het kassasysteem moet de ingebrachte gegevens zoals bepaald in artikel 1, 5° van dit ministerieel besluit kunnen verzenden naar FDM.
De bedragen die voor de diverse events worden doorgestuurd worden steeds in EURO uitgedrukt; bedragen in vreemde valuta kunnen slechts informatief vermeld worden en moeten voorzien zijn van hun ISO-code ter identificatie.

###### Art. 49
Deze communicatie omvat verplicht de in artikel 53 opgesomde berichten en volgens het in artikel 54 voorziene communicatieprotocol. Eventuele andere berichten tussen de twee apparaten moeten gedocumenteerd zijn bij de certificatieaanvraag en bijdragen tot een goede werking van het systeem. Niet gedocumenteerde uitbreidingen zijn strikt verboden.

###### Art. 50
Het kassasysteem moet in staat zijn om de - door de FDM - berekende maatstaven van heffing en de bijhorende btw-bedragen te ontvangen, op te slaan en af te drukken op het btw-kasticket. Deze informatie wordt enkel op dit soort kasticket vermeld.

###### Art. 51
Het kassasysteem moet in staat zijn om volgende controlegegevens te ontvangen van de FDM en op te slaan: - de footer zoals geconfigureerd door de FOD Financiën en doorgestuurd via de FDM;
- het unieke identificatienummer van de transactie;
- de digitale handtekeningen.
Deze controlegegevens worden afgedrukt op het btw-kasticket.

##### Onderafdeling 1. - Fysieke verbinding met de Fiscal Data Module

###### Art. 52
Het kassasysteem en de FDM worden met elkaar verbonden met een kabel (LAN) of draadloos (WiFi). De configuratie van de verbinding gebeurt in de backoffice van zowel kassa als FDM.
Het kassasysteem en de FDM communiceren met elkaar via berichten over HTTPS. De FDM stelt hiervoor zijn GraphQL service aan de POS beschikbaar.
Voor de beveiliging wordt mTLS gebruikt, gebaseerd op het intermediate certificaat van de FDM producent.
De FDM is via het internet verbonden met de FODFIN cloud API en ontvangt via deze weg ook regelmatig instructies van FODFIN cloud API. In bepaalde gevallen kan dergelijke instructie leiden tot het tonen van een boodschap op het kassasysteem en/of een manuele interventie via het kassasysteem.

    - MB 29.04.2024 / 17 -
FOD Financiën (AA BEO) www.fisconetplus.be Btw MB 29.04.2024 – Bijw. nr. 1 / 03.06.2024

##### Onderafdeling 2. - Berichten van het kassasysteem naar de Fiscal Data Module

###### Art. 53
De berichten worden door het kassasysteem naar de GraphQL service van de FDM gestuurd.
De verstuurde gegevens omvatten onder andere:
- transactiegegevens (events P en N);
- financiële gegevens (event F);
- sociale gegevens (event S);
- kopieën (event C);
- training events (event T);
- facturen (event I);
- rapporten (event R).

###### Art. 54
Alle events worden naar de FDM gestuurd, om digitaal ondertekend te worden. Hiervoor worden er diverse mutaties beschikbaar gesteld door de GraphQL service van de FDM.

##### Onderafdeling 3. - Antwoord van de Fiscal Data Module

###### Art. 55
Als antwoord op de berichten ontvangt het kassasysteem controlegegevens de berekende maatstaven van heffing, de berekende btw-bedragen, de handtekeningen en diverse mededelingen. Dit antwoord volgt steeds de structuur, gedefinieerd door de GraphQL service van de FDM, die beschreven staat in de detailbeschrijvingen.

###### Art. 56
De digitale handtekening, bedoeld in artikel 54, wordt geplaatst op de datavelden, waarvan de inhoud en structuur in de detailbeschrijvingen wordt beschreven.

#### Afdeling 5. - Detailbeschrijvingen

###### Art. 57
De geactualiseerde volledige technische detailbeschrijvingen (veldbeschrijvingen, data formaten, GraphQL mutaties, inhoud, use cases) van de communicatie tussen het kassasysteem en de FDM, met inbegrip van de errorhandling worden door de FOD Financiën ter beschikking op haar website:

### HOOFDSTUK 2. - Technische eisen ten aanzien van de fiscal data module

###### Art. 58
Dit hoofdstuk bevat, verduidelijkt en specificeert de voorschriften waaraan de FDM van het GKS moet voldoen, zoals voorzien in artikel 2, punt 7, van het koninklijk besluit van 30 december 2009.

    - MB 29.04.2024 / 18 -
FOD Financiën (AA BEO) www.fisconetplus.be Btw MB 29.04.2024 – Bijw. nr. 1 / 03.06.2024

De FDM moet aangesloten zijn op het kassasysteem en maakt hierdoor integraal deel uit van het geregistreerd kassasysteem.

###### Art. 59
Gezien zijn aard en functie dient de FDM zich steeds in de onderneming te bevinden en gekoppeld te zijn aan het kassasysteem. Dit kan op het adres van de uitbating (aan te bevelen), maar kan ook op het administratief adres, of het fiscaal domicilie van de onderneming of enige andere plaats binnen de EU.
Een FDM mag niet voor meerdere uitbatingen gebruikt worden (dus minimaal één FDM per uitbating).

#### Afdeling 1. - Algemene voorschriften

###### Art. 60
Elke geïnstalleerde FDM moet voldoen aan de eisen gesteld in dit ministerieel besluit.

###### Art. 61
De FDM mag enkel de in dit ministerieel besluit beschreven functionaliteiten bevatten.
Eventuele extra functionaliteiten kunnen enkel toegelaten worden indien zij bijdragen aan een goede werking van het geheel. Deze functionaliteiten moeten uitvoerig beschreven worden in de documentatie die wordt overgemaakt bij de certificatieaanvraag.

###### Art. 62
De werking van de FDM mag niet verstoord worden door het aansluiten van andere hardware op het kassasysteem.

###### Art. 63
De FDM moet berichten van het kassasysteem kunnen ontvangen, valideren en beantwoorden en tegelijkertijd de transactie-gegevens online kunnen doorsturen naar de servers van FOD Financiën.

##### Onderafdeling 1. - Tellers

###### Art. 64

De FDM bevat minimaal volgende tellers, die bij ondertekening van de inhoud van de betreffende events worden geüpdatet: - aantal events Normal;
- aantal events Pro Forma;
- aantal events Invoice;
- aantal events Financial;
- aantal events Social;
- aantal events Copy;
- aantal events Training;
- aantal events Report;
- doorlopende teller over alle events heen.

    - MB 29.04.2024 / 19 -
FOD Financiën (AA BEO) www.fisconetplus.be Btw MB 29.04.2024 – Bijw. nr. 1 / 03.06.2024

##### Onderafdeling 2. - Berekening maatstaven van heffing en btw-bedragen

###### Art. 65
De FDM ontvangt van de FOD Financiën bij zijn initialisatie en bij elke wijziging de btw-tarieven die van toepassing zijn op de eerder genoemde btw-labels A, B, C, D en X. Deze laten de FDM toe om voor de events Normal de maatstaven van heffing en btw-bedragen te berekenen.
Deze berekening inzake het btw-bedrag per btw-tarief gebeurt in overeenstemming met de artikelen 26, 28 en 33 van het koninklijk besluit nr. 8 van 12 maart 1970 tot vaststelling van de wijze van afronding van de verschuldigde, de aftrekbare of de voor teruggaaf vatbare belasting over de toegevoegde waarde.

###### Art. 66
De berekening van de maatstaf van heffing en de verschuldigde btw gebeurt als volgt.
1. De FDM maakt per btw-label de som van alle bedragen over alle productlijnen heen.
2. De FDM berekent de btw uit die prijs voor het bepalen van de maatstaf van heffing met volgende formule: P x (t/(100 + t)) waarbij: P = prijs inclusief btw t = het op dat moment geldende btw-tarief, uitgedrukt als een nummer met 2 decimalen.
Op het ogenblik van publicatie van dit ministerieel besluit gelden volgende btw-tarieven: - voor btw-label A: 21;
- voor btw-label B: 12;
- voor btw-label C: 6;
- voor btw-label D: 0;
- voor btw-label X: 0.
3. btw-bedrag wordt afgerond op de hogere of lagere cent, naargelang de derde decimaal 5 bereikt of niet.
4. Het eventueel afgeronde bedrag wordt afgetrokken van het bedrag inclusief btw en het verschil vormt de maatstaf van heffing.

##### Onderafdeling 3. - Buffering

###### Art. 67
De FDM moet de ontvangen berichten voldoende lang kunnen bufferen in zijn intern geheugen, zodat gegarandeerd kan worden dat deze berichten effectief naar de servers van FOD Financiën werden gestuurd.

###### Art. 68
In geval van onbereikbaarheid van de servers van de FOD Financiën blijft de FDM de berichten ontvangen van het kassasysteem, antwoorden versturen en deze berichten opslaan binnen de buffercapaciteit van de FDM.
Van zodra de servers opnieuw beschikbaar zijn, stuurt de FDM zo snel mogelijk de nog niet verstuurde berichten door. De buffercapaciteit is echter beperkt en eenmaal de limiet is bereikt, weigert de FDM nog berichten te ondertekenen. Elk antwoord van de FDM op een boodschap van de kassa bevat een melding omtrent de reeds opgebruikte buffercapaciteit.

    - MB 29.04.2024 / 20 -
FOD Financiën (AA BEO) www.fisconetplus.be Btw MB 29.04.2024 – Bijw. nr. 1 / 03.06.2024

##### Onderafdeling 4. - Aanpasbaarheid instellingen

###### Art. 69
De FDM moet in beperkte mate een aanpassing van zijn instellingen door (of voor) de FOD Financiën toelaten, meer bepaald voor: - de klok (verbinding met een externe time server);
- de maximale offlinetijd (van de servers van de FOD Financiën);
- de hoogte van de btw-tarieven (bij wijziging);
- de doorzendfrequentie van de transactie berichten;
- het clientcertificaat voor de beveiligde verbinding;
- de parameters;
- de aan te roepen url's en webservices.

##### Onderafdeling 5. - Identificatie en product-veiligheid

###### Art. 70
Elke FDM zal een uniek productienummer dragen, dat als volgt wordt samengesteld: AAABBNNNNNN, waarbij: - AAA = identificatienummer producent (na aanvraag verstrekt door de FOD Financiën);
- BB = modelnummer producent (na aanvraag verstrekt door de FOD Financiën);
- NNNNNN = serienummer (oplopend, bepaald door de producent).

###### Art. 71
Elke FDM voldoet aan de toepasselijke EU-richtlijnen inzake productveiligheid. Bij het aanvraagformulier tot certificatie dient het bekomen CE keurmerk voorgelegd te worden.

###### Art. 72
Elke FDM is zichtbaar voorzien van volgende informatie:
- modelaanduiding;
- productienummer zoals voorzien in artikel 70;
- productiedatum;
- CE keurmerk.

    - MB 29.04.2024 / 21 -
FOD Financiën (AA BEO) www.fisconetplus.be Btw MB 29.04.2024 – Bijw. nr. 1 / 03.06.2024

#### Afdeling 2. - Hardware eisen

##### Onderafdeling 1. - Processor (module)

###### Art. 73
De FDM wordt opgebouwd rond een ARM/CORTEX processor of gelijkwaardig. Deze heeft of ondersteunt minimaal: - het aantal GPIO's nodig om de gevraagde functionaliteit te ondersteunen;
- een werktemperatuur tussen 0 ° C en 70° C (commerciële standaard);
- een RTC.

###### Art. 74
De stroomvoorziening van de FDM gebeurt via de usb-c poort (+5V) en/of PoE (PD).

###### Art. 75
Communicatie met het kassasysteem verloopt minimaal via ethernet LAN en WIFI.

###### Art. 76
De FDM wordt voorzien van voldoende intern geheugen voor een vlotte werking (opslag besturingssysteem, opslag firmware, opslag tellers, ...), rekening houdend met alle vereisten opgenomen in dit besluit.

##### Onderafdeling 2. - Beveiliging

###### Art. 77
De FDM wordt uitgerust met secure element (ATECC608B of gelijkwaardig), met onder andere de volgende kenmerken: - niet-vluchtig geheugen, opslag van minimaal 2 tellers (telkens van minimaal 256 bit), certificaten, en gemengd read/write, read only of secret data;
- toegang tot de diverse secties van het geheugen is beschermd;
- conform de GDPR regelgeving.

##### Onderafdeling 3. - Connectiviteit

###### Art. 78
De FDM is voorzien van een gecertificeerde WiFi module, een LAN-poort en kan optioneel voorzien worden van minimaal een LTE 4/5G module.

###### Art. 79
De FDM mag bijkomend uitgerust zijn met een GPS-ontvanger, die per communicatie zijn geolokalisatie doorstuurt.

    - MB 29.04.2024 / 22 -
FOD Financiën (AA BEO) www.fisconetplus.be Btw MB 29.04.2024 – Bijw. nr. 1 / 03.06.2024

###### Art. 80
Een FDM mag bijkomende hardwarecomponenten bevatten (zoals bijvoorbeeld een LiPo batterij), op voorwaarde dat zij de gevraagde functionaliteiten beter ondersteunen en/of geen negatieve of beperkende invloed hierop hebben.

##### Onderafdeling 4. - Fysische opslagcapaciteit

###### Art. 81
De FDM heeft een minimale opslagcapaciteit van 2 GB beschikbaar voor het opslaan van transactiegegevens.

##### Onderafdeling 5. - Software

###### Art. 82
De firmware voldoet minimaal aan de eisen gesteld in dit ministerieel besluit en de eerder vermelde detailbeschrijvingen. De firmware mag meer functionaliteiten bevatten, die evenwel geen invloed mogen hebben op de gestelde technische eisen en die duidelijk moeten beschreven worden in de bijgeleverde documentatie bij de certificatieaanvraag.
Met respect voor de regels beschreven dit ministerieel besluit (in casu voorleggen aan en toelating krijgen van de bevoegde dienst FOD Financiën) kan de firmware een noodzakelijke patch of upgrade krijgen. Dit kan enkel door de producent of zijn gedelegeerde en op een beveiligde manier. Dit wordt uitvoerig beschreven in de documentatie gevoegd bij de aanvraag van certificatie en vormt een onderdeel van het certificatieproces.

#### Afdeling 3. - User interface - werking

##### Onderafdeling 1. - Verplicht op het toestel

###### Art. 83
Volgende minimale gezondheidsindicatoren moeten minimaal worden beschikbaar gesteld voor de gebruiker: - batterijstatus (indien het toestel zonder netstroomadapter kan werken);
- communicatiestatus met de aangesloten kassasysteem (`succesvolle' communicatie, `niet-succesvolle' communicatie);
- bufferstatus: minimaal `near full buffer' en `buffer full';
- internet network status: `succesvolle communicatie' met FODFIN, `fout communicatie' met FODFIN.
Deze indicatoren mogen naar keuze van de producent zichtbaar zijn op een display of via led. De ter beschikking gestelde gebruikershandleiding vermeldt duidelijk alle mogelijke statussen van deze indicatoren.

##### Onderafdeling 2. - Te voorzien op het toestel

###### Art. 84
De toegang tot de backoffice van de FDM wordt op een adequate manier beveiligd om de goede werking van het toestel te beschermen. De producent documenteert dit uitvoerig bij zijn certificatieaanvraag.

    - MB 29.04.2024 / 23 -
FOD Financiën (AA BEO) www.fisconetplus.be Btw MB 29.04.2024 – Bijw. nr. 1 / 03.06.2024

###### Art. 85
De user interface van de FDM mag:
- hetzij voorzien zijn op het toestel zelf;
- hetzij toegankelijk zijn via een geconnecteerd toestel;
- hetzij toegankelijk zijn via het aangesloten kassasysteem;
- hetzij een combinatie van de hierboven vermelde mogelijkheden.

##### Onderafdeling 3. - User interface - configuratie

###### Art. 86
Hieronder worden zowel de configuratie van de netwerkverbinding met het kassasysteem als deze met de servers van de FOD Financiën bedoeld.

##### Onderafdeling 4. - Cyberbeveiliging

###### Art. 87
De fabrikanten van de FDM dienen de voorwaarden van de Richtlijn (EU) 2022/2555 van het Europees Parlement en de Raad van 14 december 2022 betreffende maatregelen voor een hoog gezamenlijk niveau van cyberbeveiliging in de Unie, tot wijziging van Verordening (EU) nr. 910/2014 en Richtlijn (EU) 2018/1972 en tot intrekking van Richtlijn (EU) 2016/1148 (NIS 2-richtlijn) na te leven.

#### Afdeling 4. - Communicatie tussen de Fiscal Data Module en de cloudservice van de FOD Financiën

##### Onderafdeling 1. - First boot ever

###### Art. 88
Conform de bepalingen met betrekking tot de registratie van de onderdelen van het geregistreerd kassasysteem opgenomen in dit besluit, worden zowel het kassasysteem als de FDM door de betrokken stakeholders in de diverse fases (productie, levering) geregistreerd in de GKS e-service van de FOD FINANCIEN.
Hierbij wordt op ondernemings- en vestigingsniveau bepaald welke FDM aan welk kassasysteem is gekoppeld.
Bij de indienstneming van het GKS worden kassasysteem en FDM aan elkaar gekoppeld. Bij een correcte opstart (unieke verantwoordelijkheid van de onderneming en haar leverancier(s)) zal de FDM contact maken met de cloudservice van de FOD Financiën via een beveiligde internetverbinding.
De FODFIN cloudservice:
1. verifieert het serienummer van de FDM en kassasysteem, kent het unieke en gepersonaliseerde authenticatiecertificaat toe en stuurt het via de beveiligde verbinding naar de FDM die het opslaat op de beveiligde omgeving;
2. stuurt gelijktijdig een overzicht van de geldende btw-tarieven door;
3. stuurt gelijktijdig de gepersonaliseerde frequentiesettings door;
4. stuurt de `footergegevens' die vermeld worden op het btw-kasticket, bij dit eerste contact door.

    - MB 29.04.2024 / 24 -
FOD Financiën (AA BEO) www.fisconetplus.be Btw MB 29.04.2024 – Bijw. nr. 1 / 03.06.2024

##### Onderafdeling 2. - Verbinding en beveiliging

###### Art. 89
De verbinding via het internet wordt geconfigureerd via de backoffice van de FDM. Deze backoffice is producent-eigen, waarbij de gebruikersinterface verschillend kan zijn. De backoffice biedt minstens volgende configuratiemogelijkheden aan: - de URL's van de FODFIN cloudservice;
- de URL van de time server.

###### Art. 90
Elke communicatie wordt beveiligd door het gebruik van:
- het authentificatiecertificaat;
- het mTLS protocol dat de zendingen encrypteert.

##### Onderafdeling 3. - Online doorsturen van de transactiegegevens

###### Art. 91
Afhankelijk van de geconfigureerde zendfrequentie stuurt de FDM pakketten met transactiegegevens van de FDM (JSON-berichten) door naar de FODFIN cloudservice. Dergelijke pakketten bevatten minimaal de inhoud van één volledig event of een NOP.
De FODFIN cloudservice bevestigt (of ontkent) de goede ontvangst van de pakketten. De FDM houdt deze pakketten nog 10 dagen bij, waarna deze mogen verwijderd worden uit de buffer.
Deze pakketten worden door de FODFIN cloudservice minimaal 3 jaar bijgehouden.
Deze bewaring doet geen afbreuk aan de wettelijke fiscale bewaar- en voorleggings-verplichtingen van de originele gegevens op het kassasysteem (artikelen 315bis en 315ter van het WIB92 en artikelen 60 en 63 van het Wbtw).
Andere dan in dit ministerieel besluit opgenomen gegevens kunnen en mogen niet via deze verbinding doorgestuurd worden.

##### Onderafdeling 4. - API Application programming interface

###### Art. 92
De FDM communiceert via het hieronder beschreven protocol met de (cloud)servers van de FODFIN. Geen enkele andere dan deze communicatie is toegelaten.

#### Afdeling 5. - Detailbeschrijvingen

###### Art. 93
De geactualiseerde volledige technische detailbeschrijvingen (hardware, firmware, veldbeschrijvingen, data formaten, API, JSON, protocol) van de communicatie tussen de FDM en de servers van de FOD Financiën ter beschikking op haar website: www.geregistreerdkassasysteem.be.

    - MB 29.04.2024 / 25 -
FOD Financiën (AA BEO) www.fisconetplus.be Btw MB 29.04.2024 – Bijw. nr. 1 / 03.06.2024

## TITEL III. - VERPLICHTINGEN IN HOOFDE VAN DE DIVERSE BETROKKEN PARTIJEN

### HOOFDSTUK 1. - Verplichtingen in hoofde van de producent of invoerder van onderdelen van het geregistreerd kassasysteem

#### Afdeling 1. - Certificatieprocedure

##### Onderafdeling 1. - Bevoegde dienst

###### Art. 94
De bevoegde dienst van de FOD Financiën is de enige certificerende overheid in dit proces en beslist éénzijdig omtrent elk dispuut rond certificatie-issues en voert hierover geen correspondentie met derde partijen.
De bevoegde dienst van de FOD Financiën kan ten allen tijde een reeds gecertificeerd toestel/programma onderwerpen aan nieuwe tests.

##### Onderafdeling 2. - Algemene principes

###### Art. 95
Alle vaststellingen (of vermoedens) van niet-conformiteit van hetzij een kassasysteem, hetzij een FDM dienen onverwijld gemeld te worden aan deze certificerende overheid, die na een eventuele analyse de gepaste maatregelen zal nemen om de vastgestelde inbreuk te corrigeren.
Deze corrigerende maatregelen kunnen zijn:
- het intrekken van het certificaat, ingeval het een inbreuk betreft die de correcte fiscale werking van het GKS compromitteert;
- het eisen van een correctie voor toekomstige producties, in combinatie met een eenmalige tolerantie van de vastgestelde non-conformiteit, indien de correcte werking van het GKS niet in het gedrang is en de producent ter goeder trouw handelde;
- het eisen van een correctie van de software in reeds in gebruik zijnde toestellen;
- de regularisatie van de vaststelling en aanvullende verduidelijking van regelgeving, ingeval de nietconformiteit het resultaat is van onduidelijkheid binnen de regelgeving.

###### Art. 96
De certificerende overheid spreekt zich enkel uit over onderwerpen die betrekking hebben op dit ministerieel besluit en de interpretatie ervan (m.a.w. de productconformiteit met de technische bepalingen van de ministerieel besluit).

###### Art. 97
De certificerende overheid behoudt zich het recht voor om de correcte implementatie van gecertificeerde toestellen te verifiëren, in het kader van het behoud van het certificaat.

    - MB 29.04.2024 / 26 -
FOD Financiën (AA BEO) www.fisconetplus.be Btw MB 29.04.2024 – Bijw. nr. 1 / 03.06.2024

###### Art. 98
Wijzigingen in de technische bepalingen van de werking van de FDM t.o.v. de circulaire Circulaire AAFisc Nr.
33/2016 (nr. E.T.124.747) van 8 november 2016, zijn enkel van toepassing op toestellen die na datum van inwerkingtreding van dit besluit ter certificatie worden aangeboden.

##### Onderafdeling 3. - De aanvraag tot certificatie

###### Art. 99
Voor elke versie of model van een FDM of een kassasysteem dat in België op de markt zal worden gebracht met de bedoeling opgesteld te worden als onderdeel van een geregistreerd kassasysteem, dient conform artikel 3 van voormelde wet met betrekking tot de certificatie van een geregistreerd kassasysteem van 30 juli 2013 een certificatieaanvraag bij de bevoegde dienst van de FOD Financiën te worden ingediend, hetzij door de producent, hetzij door de invoerder.

###### Art. 100
Elke producent of invoerder dient bij elke certificatieaanvraag een volledig dossier over te maken aan de bevoegde dienst binnen de FOD Financiën, waaruit blijkt dat het product, volgens de producent of invoerder, voldoet aan de technische eisen gesteld in dit ministerieel besluit.
De procedure duurt maximaal 3 maanden, tenzij bijkomende inlichtingen gevraagd worden.

###### Art. 101
De aanvrager dient bij een certificatieaanvraag een volledig aanvraagdossier over te maken aan de bevoegde dienst bij de FOD Financiën, met daarin minimaal volgende documenten en informatie: - lijst met overzicht van de ingediende documenten en informatie;
- volledige identificatie van de producent, o.a. bestaande uit:
* maatschappelijke benaming, juridische vorm;
* adres;
* voor de certificatie gemandateerde contactpersoon, telefoonnummer, e-mailadres;
* btw-identificatienummer; in voorkomend geval, de volledige identiteit van de invoerder, o.a. bestaande uit:
* maatschappelijke benaming, juridische vorm;
* adres;
* contactpersoon, telefoonnummer, e-mailadres, website;
* btw-identificatienummer;
- ingevulde opgave met gegevens omtrent de aanvrager (activiteit, productgamma, productiefaciliteiten, ...) en overzicht van de verdelers;
- lijst met verdelers, aan wie een deel van het productieproces wordt gedelegeerd;
- alle beschikbare handleidingen (gebruikershandleiding, Configuratiehandleiding, programmeringshandleiding, service handleiding, ...) die, hetzij bestemd zijn voor de eindgebruiker, hetzij voor de verdeler;
- de volledige beschrijving van de door de FDM of kassasysteem gebruikte en aangemaakte data;

    - MB 29.04.2024 / 27 -
FOD Financiën (AA BEO) www.fisconetplus.be Btw MB 29.04.2024 – Bijw. nr. 1 / 03.06.2024

- de wijze waarop de hierboven vermelde data op een GDPR conforme manier worden bewaard op het kassasysteem (door de gebruiker/uitbater);
- technische beschrijving van het productieproces;
- uitvoerige technische beschrijving van hoe alle technische voorschriften geïncorporeerd werden;
- beschrijving van de resultaten van de testen die hij zelf heeft uitgevoerd (of in een geaccrediteerd labo heeft laten uitvoeren) op het product;
- voor de FDM: de constructie en zijn conformiteit met de in dit ministerieel besluit opgelegde CE-normen;
- voor de FDM: de functionaliteiten, met inbegrip van de technische bepalingen vermeld in de detailbeschrijvingen;
- voor de FDM: het functioneren binnen de geschetste werkomgeving, met inbegrip van het naleven van de geëiste performantiecriteria in dit ministerieel besluit.

###### Art. 102
De producent van het kassasysteem voorziet bij de aanvraag tot certificatie een gedetailleerde beschrijving van de database en meer in het bijzonder van alle tabellen die event-gegevens bevatten of een volledige beschrijving van elke andere manier van bewaring van de in het ministerieel besluit vermelde gegevens.
De producent verklaart bij zijn aanvraag uitdrukkelijk dat:
- de belastingplichtige-uitbater hoogstens over leesrechten voor de database beschikt, - de FOD Financiën, zo nodig en op eenvoudig verzoek, toegang heeft tot de relevante gegevens voor kopiename van deze gegevens op de bij de gebruikers geïnstalleerde systemen.
De producent verstrekt bijkomend volgende informatie aan de bevoegde dienst bij de FOD Financiën: - de software (en -versie) van het DBMS;
- de toegangsweg tot de database (en voor cloudbased systemen hoe een volledig extract ervan kan worden bekomen);
- de gebruikte programmeertaal;
- een login en paswoord voor de FOD Financiën.
De producenten van kassasystemen worden er uitdrukkelijk op gewezen dat zij verantwoordelijk zijn voor de manier van beveiligen van de database gegevens met betrekking tot de voormelde events. De producent vermeldt bij zijn aanvraag tot certificatie de beveiligingsmechanismen die werden gebruikt (ongeacht of die in de software zelf zijn ingebouwd of via derden worden voorzien).

###### Art. 103
Op de website van de FOD Financiën (www.geregistreerdkassasysteem.be) zal een aanvraagformulier elektronisch ter beschikking worden gesteld dat bij elke aanvraag ingevuld moet meegestuurd worden.
De FOD Financiën stelt bijkomend een certificatiehandleiding ter beschikking.

###### Art. 104
Elke aanvraag die niet alle vereiste documenten en rapporten bevat, wordt door de bevoegde dienst bij de FOD Financiën ter aanvulling teruggestuurd naar de indiener. De certificatieprocedure wordt pas formeel opgestart na ontvangst van alle gevraagde stukken.

    - MB 29.04.2024 / 28 -
FOD Financiën (AA BEO) www.fisconetplus.be Btw MB 29.04.2024 – Bijw. nr. 1 / 03.06.2024

###### Art. 105
Er dient minstens één normaal werkend toestel ter beschikking gesteld te worden van de bevoegde dienst bij de FOD Financiën. Voor de FDM zijn dit minstens drie normaal werkende toestellen.
Deze voorbeeldexemplaren blijven in uitvoering van artikel 2, § 1, laatste lid van het koninklijk besluit van 1 oktober 2013 met betrekking tot de toepassingsmodaliteiten ten aanzien van de certificatie van een geregistreerd kassasysteem bewaard bij de bevoegde dienst van de FOD Financiën, als referentiepunt voor het certificaat. Voor elk individueel model zal in onderling overleg beslist worden over wat specifiek bij de FOD Financiën zal bewaard worden en onder welke vorm (hardware, virtualisatie, image, enz.).
FDM-producenten bezorgen de bevoegde dienst van de FOD Financiën dezelfde FDM-simulator als deze die aangeboden wordt aan geïnteresseerde ontwikkelaars van kassasoftware.

###### Art. 106
De bevoegde dienst bij de FOD Financiën kan na de start van de certificatieprocedure nog bijkomende informatie opvragen, indien de hierboven beschreven documenten en informatie onvolledig blijken te zijn en/of ter verduidelijking van de bekomen informatie. De aanvrager beschikt hiervoor over een termijn van één maand. Bij gebrek aan antwoord binnen deze termijn wordt de certificatieaanvraag beschouwd als ingetrokken. De aanvrager kan steeds een verlenging van de hierboven vermelde termijn vragen, mits een gemotiveerd schrijven dat voor de oorspronkelijke vervaldag bij de bevoegde dienst bij de FOD Financiën dient toe komen.

##### Onderafdeling 4. - Verloop van de certificatieprocedure

###### Art. 107
De certificatie van een kassasysteem omvat steeds twee luiken:
- nazicht dossier: nakijken of de uitgevoerde testen voldoende de conformiteit van het kassasysteem garanderen;
- testen van het kassasysteem: het uitvoeren van functionele testen, met inbegrip van simulaties, het verifiëren van de communicatie met de FDM.
De certificatie zal zich in hoofdzaak toespitsen op de functionaliteiten van het kassasysteem en omvat minimaal de analyse van volgende punten, die ook vermeld worden in de certificatiehandleiding die de FOD Financiën ter beschikking zal stellen van de producenten: - de (correcte) werking van de verplichte functionaliteiten;
- de onmogelijkheid om verboden functionaliteiten te gebruiken;
- nagaan of alle event- en transactietypes mogelijk zijn en correct gelabeld zijn;
- nagaan of het kassasysteem correct kan communiceren met om het even welke gecertificeerde FDM;
- nagaan of het kassasysteem de events correct omzet naar de JSON en correct reageert op de antwoorden van de FDM;
- nagaan of het kassasysteem effectief stopt met functioneren als de buffer van de FDM is volgelopen;
- het uittesten van de conformiteit met de technische bepalingen van de ministerieel besluit en de detailbeschrijvingen.

    - MB 29.04.2024 / 29 -
FOD Financiën (AA BEO) www.fisconetplus.be Btw MB 29.04.2024 – Bijw. nr. 1 / 03.06.2024

###### Art. 108
De certificatie van een FDM omvat steeds twee luiken:
- nazicht dossier: nakijken of de uitgevoerde testen voldoende de conformiteit van het kassasysteem garanderen;
- technische testen van de FDM: de conformiteit met de minimale technische eisen, nakijken van de verplichte en verboden functionaliteiten, nakijken van de performantie, evalueren betrouwbaarheid (technisch concept en geheugenopslag), het uitvoeren van functionele en regressietesten, met inbegrip van simulaties, het geautomatiseerd opvullen van de geheugencapaciteit met transactiegegevens en het onderzoeken van de opgeslagen gegevens (correctheid van de berekeningen, nagaan of de gegevens niet aangetast kunnen worden), het verifiëren van de communicatie tussen het kassasysteem en de FDM (in het bijzonder de behandeling van de mutaties in de GraphQL service) en tussen de FDM en de servers van de FOD Financiën (protocol, JSON, enz.).
De naleving van de normen vervat in het CE-keurmerk wordt door de producent gegarandeerd. De producent verstrekt daarvoor de nodige verklaringen.
In geval van ernstige twijfel behoudt de FOD Financiën zich het recht voor om het toestel te laten testen door een geaccrediteerde certificatie-instelling, op kosten van de aanvrager.
De certificatie door de bevoegde dienst bij de FOD Financiën houdt GEEN garantie in van de naleving van de Europese normen vervat in het globale CE-keurmerk. De naleving hiervan wordt immers door de producent zelf gewaarborgd.

##### Onderafdeling 5. - Toekenning van certificaat

###### Art. 109
Indien uit het onderzoek blijkt dat het aangeboden kassasysteem of de aangeboden FDM niet voldoet aan de technische voorwaarden, wordt de producent of invoerder hiervan in kennis gesteld door de bevoegde dienst bij de FOD Financiën. De producent of invoerder kan dan ofwel zijn aanvraag volledig intrekken of het product aanpassen aan de opmerkingen en opnieuw ter certificatie voorleggen.
Indien de aangeboden kassasysteem of de FDM ook na aanpassing niet voldoet aan de voorwaarden, wordt het certificaat geweigerd. De producent kan hetzelfde, aangepaste, product pas na 3 maanden opnieuw ter certificatie aanbieden, wat hem toelaat om het product verder te ontwikkelen en te testen.

###### Art. 110
1° Indien uit het onderzoek blijkt dat het aangeboden kassasysteem of de aangeboden FDM voldoet aan de technische voorwaarden, wordt de producent of invoerder hiervan in kennis gesteld.
Voor een kassasysteem: de producent of invoerder ontvangt van de bevoegde dienst bij de FOD Financiën een certificaat, met vermelding van het identificatienummer van de producent (CXXX) en het certificaatnummer voor deze producent (NNN). De combinatie van het identificatienummer en het certificaatnummer vormt de basis voor de productienummers.
Voor een FDM: de producent of invoerder ontvangt van de bevoegde dienst bij de FOD Financiën een certificaat, met vermelding van het identificatienummer van de producent of invoerder (AAA) en het certificaatnummer van de producent of invoerder (BB), die o.a. als basis zullen dienen voor de unieke productienummers.
2° De kennisgeving en het certificaat zullen verzonden worden naar het adres van de aanvrager, zoals opgegeven in het aanvraagdossier. Op het certificaat wordt altijd de softwareversie vermeld.

    - MB 29.04.2024 / 30 -
FOD Financiën (AA BEO) www.fisconetplus.be Btw MB 29.04.2024 – Bijw. nr. 1 / 03.06.2024

3° Een exemplaar van het testverslag en van de ontvangen documentatie wordt bewaard bij de FOD Financiën, samen met de voorbeeldtoestellen waarop de testen werden uitgevoerd.
4° De FOD Financiën zal de product- en certificaatgegevens in de registratiedatabank opladen.
5° De toekenning van het certificaat zal eveneens gepubliceerd worden op de website, die de administratie voorziet in het kader van het "geregistreerd kassasysteem" en die toegankelijk is via de globale portaalsite van de FOD Financiën.

###### Art. 111
De certificatiewerkzaamheden uitsluitend beperken zich tot hetgeen bepaald werd in het koninklijk besluit van 1 oktober 2013 (Belgisch Staatsblad 8 oktober 2013) ter uitvoering van de wet met betrekking tot de certificatie van een geregistreerd kassasysteem van 30 juli 2013, zoals gewijzigd met artikelen 101 tot en met 103 van de wet houdende diverse fiscale bepalingen van 28 december 2023 en in huidig ministerieel besluit.
Het uitgereikte certificaat door de bevoegde dienst van de FOD Financiën heeft uitdrukkelijk geen betrekking op functionaliteiten van het betreffende onderdeel van het geregistreerd kassasysteem, die niet gedocumenteerd werden in het dossier ingediend door de aanvrager.

##### Onderafdeling 6. - Verplichtingen na de certificatie

###### Art. 112
Productgarantie
Van zodra een producent een certificaat voor zijn model van kassasysteem of FDM heeft ontvangen, garandeert hij dat elk exemplaar dat geproduceerd wordt om als onderdeel van een geregistreerd kassasysteem te functioneren en om verkocht te worden op de Belgische markt, identiek is aan het exemplaar dat werd aangeboden ter certificatie.
Voor een kassasysteem zal deze garantie onder andere verstrekt worden door het verstrekken van de hashwaarde, berekend op hetzij de volledige source code van de kassasoftware, hetzij de relevante programmabestanden. Voor het berekenen van deze hash-waarde dient minimaal een SHA-1 gehanteerd te worden.

###### Art. 113
Wijzigingen
1° Indien de producent of invoerder wijzigingen wenst aan te brengen aan een reeds gecertificeerd kassasysteem of gecertificeerde FDM, dient hij een nieuwe certificatieprocedure te starten. De bevoegde dienst bij de FOD Financiën beslist, op basis van de aangegeven wijzigingen, in hoeverre de testprocedure geheel of gedeeltelijk wordt overgedaan. Het vervolg is identiek aan de procedure hierboven beschreven.
De producent of invoerder geeft de wijzigingen aan het product minstens een maand voor het op de markt brengen in België van de nieuwe versie door aan de bevoegde dienst bij de FOD Financiën.
Elke wijziging betreffende de identiteit van de producent of invoerder dient onmiddellijk meegedeeld te worden aan de bevoegde dienst bij de FOD Financiën.
2° Behoudens het wegwerken van kritische bugs dienen updates die betrekking hebben op functionaliteiten zoals bedoeld in dit besluit beperkt/gegroepeerd te worden tot 12 updates per kalenderjaar.
Om de bevoegde dienst bij de FOD Financiën toe te laten de hierboven vermelde wijzigingen te beoordelen, verstrekt de producent volgende zaken:

    - MB 29.04.2024 / 31 -
FOD Financiën (AA BEO) www.fisconetplus.be Btw MB 29.04.2024 – Bijw. nr. 1 / 03.06.2024

- de nieuwe versie van de software (bij voorkeur installatie door de producent);
- een releasenota die in detail de wijzigingen/aanpassingen beschrijft;
- de informatie omtrent de productgarantie.
3° Behoudens de wijzigingen ter correctie van kritische bugs, die onmiddellijk mogen gebeuren, neemt de bevoegde dienst bij de FOD Financiën binnen de 15 dagen een beslissing omtrent de update, voor zover er geen bijkomende inlichtingen moeten verstrekt worden. In dat geval beschikt de bevoegde dienst over een nieuwe termijn van 15 dagen, die aanvangt bij ontvangst van de gevraagde inlichtingen, om een beslissing te nemen. De update mag pas gecommercialiseerd worden na verloop van deze periode en mits toestemming van de bevoegde dienst.
4° Indien er een nieuw certificaat dient aangevraagd te worden, is het vervolg identiek aan de procedure hierboven beschreven. De praktische modaliteiten worden beschreven in de certificatiehandleiding.
5° Elke wijziging betreffende de identiteit van de producent of invoerder dient onmiddellijk meegedeeld te worden aan de bevoegde dienst bij de FOD Financiën.

##### Onderafdeling 7. - Recuperatie modelexemplaar

###### Art. 114
Wanneer een certificatieprocedure wordt stopgezet (wegens niet toekennen certificaat of vrijwillige terugtrekking), kan de producent zijn aangeleverde modelexempla(a)r(en) bij de bevoegde dienst van de FOD Financiën terug ophalen. Hij beschikt hiervoor over 6 maanden na de stopzetting van de procedure. Na deze periode wordt de FOD Financiën definitief eigenaar van dit materiaal en kan zij hier vrij over beschikken.

#### Afdeling 2. - Registratieprocedure

###### Art. 115
Artikel 2bis van het koninklijk besluit van 30 december 2009, artikel 4 van de wet met betrekking tot de certificatie van een geregistreerd kassasysteem van 30 juli 2013 en artikel 5 van het koninklijk besluit met betrekking tot de toepassingsmodaliteiten ten aanzien van de certificatie van een geregistreerd kassasysteem van 1 oktober 2013 voorzien in de registratie door alle betrokkenen van alle onderdelen van het geregistreerd kassasysteem, namelijk: - het kassasysteem;
- de FDM.

###### Art. 116
Na toekenning van zijn eerste certificaat wordt de producent of invoerder door de bevoegde dienst bij de FOD Financiën in de registratiemodule geregistreerd, waarna deze via de CSAM-procedure toegang krijgt tot deze webapplicatie.
Indien een producent of invoerder zowel kassasystemen als FDM produceert, dan moet deze zich afzonderlijk te registreren voor elk van beide producten.
Wijzigingen van de personen die verantwoordelijk zijn voor de registraties (in het geval het gaat om producenten of invoerders of verdelers) dienen voorafgaandelijk aan de bevoegde dienst van de FOD Financiën kenbaar gemaakt te worden, teneinde tijdig de toegangsrechten te kunnen regelen.

    - MB 29.04.2024 / 32 -
FOD Financiën (AA BEO) www.fisconetplus.be Btw MB 29.04.2024 – Bijw. nr. 1 / 03.06.2024

###### Art. 117
1° Bij de toekenning van het eerste certificaat aan een producent of invoerder ontvangt deze een identificatiecode (AAA voor een FDM, CXXX voor een kassasysteem). Op basis daarvan wordt de prefix van het gecertificeerde model aangemaakt, die als basis dient voor aanmaak van de individuele productienummers van de toestellen. Conform de bepalingen van artikelen 46 en 70 van dit besluit worden die als volgt samengesteld: - voor een kassasysteem: CXXXNNN, gevolgd door 7 karakters;
- voor een FDM: AAABB, gevolgd door 6 karakters.
2° Het certificaat en de in punt 1° vermelde prefix worden door de bevoegde dienst bij de FOD Financiën geregistreerd in de webapplicatie.

###### Art. 118
Van zodra een lot van kassasystemen of FDM is geproduceerd/klaar is voor uitlevering, met bestemming de Belgische markt en om er geleverd te worden als onderdeel van een geregistreerd kassasysteem, zoals bedoeld in dit ministerieel besluit, dient de producent of invoerder de reeks van productienummers via de webapplicatie te registreren.

###### Art. 119
Van zodra de producent of invoerder de een kassasysteem of een FDM levert aan een verdeler, dient hij onverwijld de FOD Financiën hiervan in kennis te stellen, via de webapplicatie. Hierbij zullen minimaal volgende gegevens worden gevraagd: - identificatie van de verdeler (btw-identificatienummer);
- leveringsdatum;
- productienummers geleverde toestellen.
De levering van een FDM of een kassasysteem dient geregistreerd te worden op de vroegste datum van de volgende twee momenten: - het moment waarop de verdeler er juridisch eigenaar van wordt;
- het moment waarop de verdeler het onderdeel fysisch in zijn bezit heeft.

### HOOFDSTUK 2. - Verplichtingen in hoofde van de verdeler van onderdelen van het geregistreerd kassasysteem

###### Art. 120
Iedere onderneming die een kassasysteem of FDM, bedoeld om te worden gebruikt als in een geregistreerd kassasysteem, wenst te verkopen (leveren en factureren) aan een belastingplichtige exploitant uitbater of verdeler, dient zich voorafgaandelijk bij de FOD Financiën als dusdanig kenbaar te maken.
Deze registratie gebeurt via de voorziene webapplicatie. De te verstrekken informatie bevat minimaal: - volledige identiteit van de verdeler (btw-identificatienummer, maatschappelijke benaming, juridische vorm, adres, contactpersoon, telefoon, email, website);
- adresgegevens van verdeel- en verkooppunten;
- korte omschrijving van referenties en producten.

    - MB 29.04.2024 / 33 -
FOD Financiën (AA BEO) www.fisconetplus.be Btw MB 29.04.2024 – Bijw. nr. 1 / 03.06.2024

De bevoegde dienst bij de FOD Financiën valideert, na een administratief onderzoek, deze aanvraag tot registratie.
De producent of invoerder die rechtstreeks aan eindgebruikers levert, dient zich bijkomend aan zijn hoedanigheid van producent of invoerder ook als verdeler te registreren.
Wijzigingen van de personen die verantwoordelijk zijn voor de registraties (in het geval het gaat om producenten of invoerders of verdelers) dienen voorafgaandelijk aan de bevoegde dienst van de FOD Financiën kenbaar gemaakt te worden, teneinde tijdig de toegangsrechten te kunnen regelen.

###### Art. 121
Van zodra de verdeler één of meerdere onderdelen van geregistreerde kassasystemen levert aan de eindgebruiker, de belastingplichtige-uitbater, dient hij onverwijld de FOD Financiën hiervan in kennis te stellen, via de webapplicatie. Op deze pagina dienen minimaal volgende gegevens worden ingevuld: - identificatie belastingplichtige uitbater (btw-identificatienummer, naam, adres);
- identificatie van de uitbating van opstelling (uithangbord, adres, lokaal opstelling);
- leveringsdatum;
- productienummer(s) geleverde toestel(len).
In voorkomend geval dat de verdeler één of meerdere onderdelen van geregistreerde kassasystemen levert aan een andere verdeler, dient hij dit eveneens onverwijld te melden aan de FOD Financiën, via de daarvoor voorziene pagina binnen de webapplicatie, waarbij minimaal volgende informatie dient te worden verstrekt: - identificatie andere verdeler (btw-identificatienummer, maatschappelijke benaming, juridische vorm, adres);
- leveringsdatum;
- productienummers van de doorverkochte toestellen.

### HOOFDSTUK 3. - Verplichtingen in hoofde van de gebruiker van het geregistreerd kassasysteem

###### Art. 122
Elke onderneming die krachtens artikel 21bis van het koninklijk besluit nr. 1 met betrekking tot de regeling voor de voldoening van de belasting over de toegevoegde waarde gehouden is een geregistreerd kassasysteem te gebruiken voor de registratie van zijn uitgaande handelingen, waarvoor zij niet verplicht zijn een factuur uit te reiken, moet zich als gebruiker van een geregistreerd kassasysteem registreren. Dit gebeurt altijd via de daarvoor voorziene webapplicatie van de FOD Financiën.

###### Art. 123
Om het geregistreerd kassasysteem operationeel te maken, dient de belastingplichtige-uitbater via de webapplicatie de leveringen van de onderdelen van zijn GKS (kassasysteem en FDM) te valideren. Daarna linkt hij in de toepassing de kassa(`s) aan de correcte FDM(`s). Eens dit voltooid is, kan het GKS operationeel worden gemaakt en zal de FDM proberen verbinding te maken met de servers van de FOD Financiën.

###### Art. 124
Indien de FDM zich niet in de uitbating bevindt en via een netwerk met de kassa is verbonden (intern netwerk, internet, ...) zal bij het uitvallen van dit netwerk de kassa niet langer kunnen communiceren met de FDM. Dit

    - MB 29.04.2024 / 34 -
FOD Financiën (AA BEO) www.fisconetplus.be Btw MB 29.04.2024 – Bijw. nr. 1 / 03.06.2024

heeft tot gevolg dat het onmogelijk wordt om nog transacties te registreren op het GKS.
Ingeval van een ernstige storing van het GKS dient de belastingplichtige-uitbater de bevoegde dienst van de FOD Financiën hiervan in kennis te stellen via e-mail (bij de start en bij het einde van de storing).

###### Art. 125
Buitengebruikstelling
1° Een kassasysteem en/of een FDM kan om diverse redenen buitengebruik gesteld worden door een belastingplichtige-uitbater: definitief defect, doorverkoop of overlating aan andere belastingplichtigeuitbater, doorverkoop aan- of overname door een verdeler.
De belastingplichtige-uitbater dient dan, onverwijld, via de webapplicatie de nodige vermeldingen te doen. Er wordt uitdrukkelijk gewezen op de fiscale bewaarverplichting met betrekking tot de op het kassasysteem opgeslagen gegevens.
2° In uitzondering op punt 1° mag een FDM onder geen enkel beding overgedragen worden door de belastingplichtige-uitbater aan een andere belastingplichtige-uitbater. De FDM bevat data die onderdeel blijven van de boekhouding.

###### Art. 126
De belastingplichtige-gebruiker van een geregistreerd kassasysteem is verantwoordelijk voor de bewaring van de gegevens die door het kassasysteem zijn aangemaakt, conform de btw-wetgeving (en bij uitbreiding de boekhoud-wetgeving). Zo is de belastingplichtige-gebruiker met name verantwoordelijk voor de bewaring van de gegevens op het kassasysteem en op de FDM. Gemaakte back-up's van kassadata blijven deel uitmaken van het kassasysteem en zijn bijgevolg aan dezelfde bewaringstermijnen onderhevig.

## TITEL IV. - SANCTIES - BEROEPSMOGELIJKHEDEN

### HOOFDSTUK 1. - Sancties met betrekking tot de certificatie van onderdelen van het geregistreerd kassasysteem

###### Art. 127
1° Wanneer de bevoegde dienst van FOD Financiën vaststelt dat de producent of invoerder de verplichtingen opgenomen in de artikelen 97 tot 122 niet respecteert, voor één of meer van deze verplichtingen in gebreke blijft, zal hij hiervan schriftelijk op de hoogte gesteld worden teneinde zich opnieuw in regel te stellen. Het certificaat wordt twee maanden opgeschort.
2° Wanneer de producent of invoerder daarna nog in gebreke blijft, kan de FOD Financiën het certificaat intrekken.

###### Art. 128
1° Indien wordt vastgesteld dat toestellen, die niet conform het certificaat zijn en/of die niet voldoen aan de in dit ministerieel besluit gestelde voorwaarden, als onderdeel van een geregistreerd kassasysteem werden opgesteld, wordt de producent of invoerder hiervan schriftelijk in kennis gesteld door de bevoegde dienst.
2° Deze kennisgeving schorst het certificaat twee maanden vanaf datum van ontvangst (artikel 5 van de wet met betrekking tot de certificatie van een geregistreerd kassasysteem van 30 juli 2013 en artikel 6 § 2 van

    - MB 29.04.2024 / 35 -
FOD Financiën (AA BEO) www.fisconetplus.be Btw MB 29.04.2024 – Bijw. nr. 1 / 03.06.2024

het koninklijk besluit met betrekking tot de toepassingsmodaliteiten ten aanzien van de certificatie van een geregistreerd kassasysteem).
3° Het certificaat kan na onderzoek door de FOD Financiën definitief ingetrokken worden.
4° Het intrekken het certificaat heeft als automatisch gevolg dat alle geregistreerde kassasystemen, die gebruik maken van het niet langer gecertificeerd kassasysteem of de niet langer gecertificeerde FDM, niet meer voldoen aan de eisen gesteld in het koninklijk besluit van 30 december 2009 tot het bepalen van de definitie en de voorwaarden waaraan het geregistreerd moet voldoen.
5° De FOD Financiën stelt de gebruikers van een dergelijk geregistreerd kassasysteem in kennis van het intrekken van het certificaat. Deze gebruikers dienen, conform artikel 7 van het koninklijk besluit met betrekking tot de toepassingsmodaliteiten ten aanzien van de certificatie van een geregistreerd kassasysteem van 01 oktober 2013, binnen de drie maanden opnieuw over een volledig gecertificeerd systeem te beschikken.
Indien de gebruiker van mening is dat zijn toestel(len) wel degelijk voldoet(n) aan de eisen van het certificaat, dient hij dit binnen de maand te melden aan de bevoegde dienst bij de FOD Financiën, die binnen de maand na ontvangst van deze melding ter plaatse de conformiteit zal gaan beoordelen.

### HOOFDSTUK 2. - Beroepsmogelijkheid met betrekking tot het intrekken/weigeren van het certificaat

###### Art. 129
Wanneer de producent van oordeel is dat de definitieve administratieve beslissing van weigering of intrekken van het certificaat onterecht is gebeurd (en zijn product volledig conform de technische voorschriften is), kan hij conform de bepalingen van artikel 569, 32° Ger.W. bij dagvaarding tegen deze weigering een beroep indienen bij de rechtbank van eerste aanleg te Brussel.

### HOOFDSTUK 3. - Sancties met betrekking tot de registratie van onderdelen van het geregistreerd kassasysteem

###### Art. 130
Indien bij een eindgebruiker een onderdeel van het geregistreerd kassasysteem niet werd geregistreerd volgens bovenstaande procedure, heeft dit tot gevolg dat het aldaar opgestelde kassasysteem met controlemodule NIET voldoet aan de voorwaarden gesteld in het koninklijk besluit van 30 december 2009 tot het bepalen van de definitie en de voorwaarden waaraan het geregistreerd kassasysteem moet voldoen. Deze overtreding kan in hoofde van de belastingplichtige-uitbater bestraft worden met een administratieve boete conform Afdeling 2, rubriek II.A van het koninklijk besluit nr. 44 tot vaststelling van het bedrag van de nietproportionele fiscale geldboeten op het stuk van de belasting over de toegevoegde waarde.

###### Art. 131
Het niet registreren van onderdelen van het geregistreerd kassasysteem door producenten of invoerders en verdelers kan aanleiding geven tot opleggen van een administratieve boete conform Afdeling 6 van het koninklijk besluit nr. 44 tot vaststelling van het bedrag van de niet-proportionele fiscale geldboeten op het stuk van de belasting over de toegevoegde waarde.

    - MB 29.04.2024 / 36 -
FOD Financiën (AA BEO) www.fisconetplus.be Btw MB 29.04.2024 – Bijw. nr. 1 / 03.06.2024

## TITEL V. - SLOTBEPALINGEN

###### Art. 132

Dit besluit vervangt Circulaire AAFisc Nr. 33/2016 (E.T. 124.747) van 8 november 2016 (Belgisch Staatsblad 16 januari 2017).

    - MB 29.04.2024 / 37 -
