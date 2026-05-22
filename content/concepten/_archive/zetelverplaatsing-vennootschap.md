---
title: Zetelverplaatsing van een vennootschap — operatie
tags:
- concept
- operatie
- po-1-4
- po-2-1
- po-2-8
- po-3-0
linked_anchors:
- 2.8.XII
- 2.8.XVI
- 2.8.taak.2
- 3.0.I
- 2.1.X
- 1.4.I
programmaonderdelen:
- '1.4'
- '2.1'
- '2.8'
- '3.0'
confidence: grounded
node_type: operatie
status: seed
schema_version: '2.0'
gegenereerd_uit: data/concepten/records/zetelverplaatsing-vennootschap.json
gegenereerd_op: '2026-05-21'
---
# Zetelverplaatsing van een vennootschap — operatie ⚖️

> [!summary] Korte inhoud
> **Zetelverplaatsing van een vennootschap** is de operatie waarbij een vennootschap haar **statutaire zetel** over een staatsgrens verplaatst, waardoor zij zich automatisch **omzet in een rechtsvorm van de jurisdictie waarheen** zij vertrekt — **met behoud van rechtspersoonlijkhei….

**Zetelverplaatsing van een vennootschap** is de operatie waarbij een vennootschap haar **statutaire zetel** over een staatsgrens verplaatst, waardoor zij zich automatisch **omzet in een rechtsvorm van de jurisdictie waarheen** zij vertrekt — **met behoud van rechtspersoonlijkheid**, dus zonder ontbinding (WVV art. 14:16). Twee richtingen: **outbound** (BE-vennootschap vertrekt naar buitenland) en **inbound** (buitenlandse vennootschap vestigt zich in BE), elk met eigen vennootschapsrechtelijke procedure, boekhoudkundige continuïteitsregels en fiscale gevolgen.

_Bron: WVV art. 14:16 + WIB92 art. 210 §1, 4° + art. 214bis_



## Wat er economisch echt gebeurt 🔗

Substance over form: er is **continuïteit van de juridische persoon** (zelfde aandeelhouders, zelfde activa, zelfde passiva, zelfde contracten) maar het **toepasselijke vennootschapsrecht verandert** — een Belgische BV wordt na verplaatsing naar Nederland een Nederlandse BV, een Luxemburgse SARL wordt een Belgische BV. De vennootschap *stopt niet en herstart niet* — zij wisselt van rechtssysteem zoals een mens van nationaliteit wisselt. Economisch is dit dus fundamenteel anders dan een **liquidatie + heroprichting** (waarbij contracten opnieuw onderhandeld moeten worden, activa worden overgedragen via verkoop, en de aandeelhouders fiscaal afrekenen op de liquidatiebonus).

Fiscaal echter behandelt de **bronstaat** de operatie typisch alsof er wél een eindpunt is: BE belast de vertrekkende vennootschap op haar **latente meerwaarden** alsof zij vereffend werd (WIB92 art. 210 §1, 4° — exit-tax). De ratio: zonder die afrekening verliest BE definitief het recht om die meerwaarden ooit te belasten omdat de vennootschap zich daarna in een andere jurisdictie bevindt. De interne EU-markt voegt daar een **temperende** laag aan toe (art. 214bis WIB92 voor intra-EU + ATAD-spreiding) en het Hof van Justitie heeft de outbound-vrijheid versterkt (Cartesio/Vale/Polbud) — maar geen enkele EU-regel verplicht een staat zijn belastinggrondslag onverdedigd los te laten.


## Voorkennis & leespad

- **Lees eerst** (voorvereisten):
  [[rechtspersoonlijkheid]]
  [[statutaire-zetel-vs-werkelijke-zetel]]
  [[vennootschapsbelasting-kader]]

- **Past binnen kader**: [[grensoverschrijdende-verrichtingen]]

- **Naast deze fiche relevant**:
  [[grensoverschrijdende-fusie]]
  [[grensoverschrijdende-splitsing]]
  [[omzetting-vennootschap]]
  [[oeso-modelverdrag]]
  [[vaste-inrichting]]

- **Bij vervolgvragen**:
  [[exit-belasting]]
  [[atad-richtlijn]]
  [[fusie-richtlijn-2009-133]]
  [[eu-mobiliteitsrichtlijn-2019-2121]]



## Hoe het werkt

De operatie heeft drie poten die parallel lopen: (1) een **vennootschapsrechtelijke procedure** met strikte voorwaarden in beide jurisdicties; (2) een **fiscaal regime** dat in BE als hoofdregel exit-tax oplegt (art. 210 §1, 4° WIB92) maar gemilderd wordt door art. 214bis (intra-EU) en ATAD-spreiding; (3) een **boekhoudkundig continuïteits-regime** (CBN-advies 2018/03 + 2011/2) dat bepaalt hoe de boekhouding wordt overgezet. Voor inbound naar BE is de spiegel: BE-vennootschapsrecht en BE-boekhoudrecht worden van toepassing vanaf de verplaatsing (art. 112 WIPR).

### Wettelijke voorwaarden — drie regimes ⚖️

Drie scenarios met elk hun eigen voorwaardenbundel. De keuze tussen 'binnen-België adreswijziging', 'intra-EU verplaatsing' en 'verplaatsing van/naar derde staat' bepaalt de zwaarte van de procedure en de fiscale behandeling.

_Bron: WVV Boek 14 Hoofdstuk 3 (art. 14:16 e.v.) + EU-richtlijn 2019/2121 + WIPR art. 112_

| Aspect | Binnen-België | Intra-EU (BE ↔ EU) | BE ↔ derde staat (niet-EU/EER) |
| --- | --- | --- | --- |
| Juridische continuïteit | Vanzelfsprekend | Ja — WVV art. 14:16 + EU-richtlijn 2019/2121 | Afhankelijk van doelland — niet gegarandeerd |
| Bevoegd orgaan BE | Bestuursorgaan, tenzij statuten anders bepalen of taalregime wijzigt (WVV art. 1:27, MvT) | Algemene vergadering — buitengewone meerderheid | Algemene vergadering — buitengewone meerderheid + notariële akte |
| Werknemersmedezeggenschap | Geen impact | EU-richtlijn 2019/2121 — bescherming bestaand niveau | Variabel — geen EU-bescherming |
| Schuldeisersverzet | Geen specifieke termijn | Termijn voor verzet schuldeisers (EU-richtlijn) | Variabel |
| Boekhoudkundige continuïteit | Continu | Toegestaan (CBN 2018/03 — voor inbound) | Beperkt — niet automatisch voor derde staten zonder gelijkwaardig boekhoudrecht (CBN 2018/03 voetnoot 2) |
| BE-exit-tax (outbound) | n.v.t. | Vrijstelling voor activa die in BE-inrichting blijven (art. 214bis) + spreiding mobiele activa (ATAD) | Onmiddellijke afrekening op latente meerwaarden (art. 210 §1, 4° WIB92) |

**Belangrijk onderscheid**: een **adreswijziging binnen België** (zelfs naar een ander gewest) is **geen** zetelverplaatsing in de zin van Boek 14 — dat is een gewone statutenwijziging of zelfs een bestuursbeslissing zonder statutenwijziging (WVV art. 1:27, MvT). Alleen wanneer de zetel een **staatsgrens** overschrijdt treedt het mobiliteitsregime van Boek 14 in werking, met de gevolgen voor het toepasselijke recht (art. 112 WIPR).

### Procedurele stappen — tijdslijn outbound vanuit BE ⚖️

Sequentiële stappen voor een outbound zetelverplaatsing van een Belgische vennootschap naar een ander EU-land, conform WVV Boek 14 Hoofdstuk 3 en EU-richtlijn 2019/2121. Inbound spiegelt deze procedure aan de BE-zijde (registratie + boekhoudkundige overgang).

_Bron: WVV art. 14:16 e.v. + EU-richtlijn 2019/2121_



⚠️ De exacte termijnen en meerderheden zijn na de implementatie van EU-richtlijn 2019/2121 (deadline 31 januari 2023) in WVV Boek 14 verfijnd; concrete art.-nummers (14:17/1 e.v.) en termijnen te verifiëren in actuele WVV-tekst. De wet van 25 mei 2023 (BS 16 juni 2023) bracht aanpassingen aan art. 14:16.

### Fiscaal regime BE-outbound — exit-tax (art. 210 §1, 4°) + intra-EU temperingen ⚖️

Wanneer een binnenlandse vennootschap haar voornaamste inrichting of zetel van bestuur of beheer naar het buitenland verplaatst, wordt dit fiscaal **gelijkgesteld met vereffening** (WIB92 art. 210 §1, 4°): er moet afgerekend worden op alle latente meerwaarden, ongerealiseerde resultaten en vrijgestelde reserves alsof de vennootschap geliquideerd werd. Dit is de **exit-tax**.

De ATAD-richtlijn (omgezet in BE-recht) en art. 214bis WIB92 milderen dit binnen EU:

_Bron: WIB92 art. 210 §1, 4° + art. 214bis_

| Activa-categorie | Outbound naar EU-lidstaat | Outbound naar derde staat |
| --- | --- | --- |
| Activa die blijvend toegewezen worden aan een BE-vaste inrichting | Géén afrekening (art. 214bis 1e streepje) — BE behoudt heffingsrecht via BNI/ven (art. 229 + 233 WIB92) | Géén afrekening op BE-VI-bestanddelen, voor het overige onmiddellijke afrekening |
| Vrijgestelde reserves teruggevonden in eigen vermogen BE-vaste inrichting | Géén afrekening (art. 214bis 2e streepje) | Onmiddellijke belasting |
| Mobiele activa (deelnemingen, IP, goodwill) verplaatst naar EU-doelland zonder BE-link | Belastbaar — maar **spreiding over 5 jaar** mogelijk (ATAD-richtlijn) | Onmiddellijke belasting aan VenB-tarief |
| Activa naar EER-staat (Noorwegen/IJsland/Liechtenstein) | Behandeld als EU — spreiding mogelijk | n.v.t. |

⚖️ Wettelijke basis art. 214bis WIB92: *"Niettegenstaande artikel 210, § 1, 4°, ingeval van overbrenging van de voornaamste inrichting of de zetel van bestuur of beheer door een binnenlandse vennootschap naar een andere lidstaat van de Europese Unie, vindt geen belastingheffing ingevolge artikel 208, tweede lid, of artikel 209 plaats: voor wat betreft de bestanddelen die blijvend worden aangewend binnen een in artikel 229, § 1, bedoelde Belgische inrichting waarover de vennootschap in België, al dan niet ten gevolge van deze verrichting, beschikt (...)"*. De **substance-test** is dus: blijft er na verplaatsing een BE-vaste inrichting die de activa effectief gebruikt? Zo ja → vrijstelling; zo nee → afrekening, met spreiding indien EU.

### Fiscaal regime BE-inbound — start onderwerping VenB 🔗

Een buitenlandse vennootschap die haar voornaamste inrichting naar België verplaatst, wordt vanaf dat moment binnenlandse vennootschap (art. 2 §1, 5° WIB92) en onderworpen aan BE-VenB. De fiscale **startbalans** in BE volgt typisch de boekwaarde uit het herkomstland (boekhoudkundige continuïteit — CBN-advies 2018/03), behalve waar BE-waarderingsregels afwijken. ⚠️ Step-up-discussie: in welke mate kan de inbound-vennootschap latente meerwaarden in haar BE-startbalans opnemen tegen werkelijke waarde? Te verifiëren in actuele CBN-doctrine.

Voor aandeelhouders-natuurlijke-personen die inwoner van BE worden door samenloop met de zetelverplaatsing: de **inwerking van het OESO-modelverdrag** (tie-breaker art. 4) bepaalt of zij PB-belastingplichtig worden in BE. Voor BE-vennootschap-aandeelhouders: deelnemingen in de inbound-vennootschap blijven gewaardeerd zoals voorheen; het feit dat de target nu BE-VenB wordt verandert niets aan hun boekwaarde.

### Boekhoudkundige continuïteit (CBN-advies 2018/03 + 2011/2) ⚖️

De CBN heeft het beginsel van **boekhoudkundige continuïteit** voor inbound zetelverplaatsingen bevestigd in advies 2011/2 (algemeen) en 2018/03 (verschillen in waarderingsregels). De boekhouding wordt overgebracht naar België mits de nodige aanpassingen aan BE-boekhoudrecht. Drie tijds-categorieën van verrichtingen:

_Bron: CBN-advies 2011/2 + CBN-advies 2018/03_

| Type verrichting | Toepasselijk boekhoudrecht |
| --- | --- |
| Vóór zetelverplaatsing — afgesloten effect | Boekhoudregels van de Staat van herkomst |
| Vóór zetelverplaatsing — effect over meerdere boekjaren | BE-boekhoudrecht (zelfs al gerealiseerd vóór verplaatsing) — bijvoorbeeld afschrijvingen, voorzieningen |
| Na zetelverplaatsing | BE-boekhoudrecht |

⚠️ Beperkingen: continuïteit geldt voor verplaatsingen vanuit een **EER-lidstaat** of een **derde Staat met gelijkaardig boekhoudrecht** (Richtlijn 2013/34/EU als referentie). Vanuit een derde Staat zonder gelijkwaardig boekhoudrecht is continuïteit **niet** toegelaten (CBN-advies 2018/03 voetnoot 2) — dan moet een volledig nieuwe BE-openingsbalans opgesteld worden, vergelijkbaar met een oprichting.

### EU-Hof van Justitie-trilogie — Cartesio · Vale · Polbud ⚖️

Drie sleutelarresten van het HvJ-EU vormen het kader voor de outbound-vrijheid van vennootschappen binnen de EU. Hun gezamenlijke leer is dat een lidstaat een vertrekkende vennootschap niet mag verplichten te ontbinden enkel omdat zij naar een andere lidstaat wenst te verhuizen, terwijl die andere lidstaat haar als rechtspersoon van het eigen rechtssysteem moet kunnen aanvaarden mits voldaan aan de daar geldende oprichtingsvoorwaarden.

| Arrest | Jaar | Kernregel |
| --- | --- | --- |
| Cartesio (C-210/06) | 2008 | Lidstaat van herkomst mag verplaatsing van werkelijke zetel verbieden, maar moet outbound *zetelverplaatsing-met-vormomzetting* toelaten (de basis voor de EU-mobiliteitsrichtlijn) |
| Vale (C-378/10) | 2012 | Lidstaat van ontvangst moet binnenkomende vennootschap als rechtspersoon erkennen mits compliance met eigen oprichtingsvoorwaarden — anti-discriminatie t.o.v. zuiver-interne omzettingen |
| Polbud (C-106/16) | 2017 | Verplaatsing van louter de **statutaire zetel** zonder verplaatsing van de werkelijke economische activiteit is gerechtvaardigd onder vrijheid van vestiging — lidstaten kunnen dit niet verbieden enkel omwille van vermoeden van misbruik |

🧭 Voor de praktijk: deze rechtspraak is de juridische rugdekking voor outbound-keuzes naar fiscaal of governance-gunstiger EU-jurisdicties. De fiscus kan een outbound niet blokkeren maar wel de fiscale gevolgen (exit-tax) opleggen — mits die proportioneel zijn (Polbud + National Grid Indus C-371/10 voor exit-tax). De EU-mobiliteitsrichtlijn 2019/2121 is de **codificatie** van deze rechtspraak.


## Rol van de accountant

Drie typische perspectieven: (1) de **verplaatsende vennootschap** zelf — strategie, procedure, fiscale afrekening, boekhouding; (2) een **inbound buitenlandse vennootschap** die in BE landt — opening BE-boekhouding, eerste BE-aangifte; (3) **auditor/commissaris** indien de vennootschap onder controleverplichting valt — controleverklaring continuïteit en bijzondere verklaringen. De accountant is hier vaak in een coördinatie-rol met buitenlandse counterparts (notaris, advocaat, lokale accountant in doelland).

### 🏢 verplaatsende vennootschap (outbound of inbound)

#### 🎯 Adviseur

##### Strategische afweging — zetelverplaatsing vs alternatieven 🧭

Vóór de juridische opzet doorloopt de adviseur met de klant systematisch de keuzemenu. Zetelverplaatsing is een **zware en onomkeerbare** ingreep; vaak is een lichter alternatief geschikter voor het zakelijk doel.

| Doel | Best alternatief | Wanneer toch zetelverplaatsing |
| --- | --- | --- |
| Buitenlandse verkoopactiviteit zonder eigen entiteit | Vaste inrichting onder DBV | Wanneer volledige operationele shift gewenst is |
| Lokale dochter in doelland | Nieuwe dochter-vennootschap oprichten | Wanneer de moeder zelf moet verhuizen (governance, woonplaats UBO) |
| Fusie met buitenlandse zustermaatschappij | Grensoverschrijdende fusie (WVV Boek 12) | Wanneer de vennootschap als entiteit moet blijven bestaan (geen verdwijning) |
| Liquidatie + heroprichting elders | Liquidatie (duur, fiscale afrekening op iedereen) | Wanneer contracten en vergunningen behouden moeten worden |

##### Substance-test vooraf — anti-misbruik-screening 🧭

De adviseur screent of de verplaatsing een **echte economische verhuizing** is of een louter papieren zetelshift met fiscaal motief. Hoewel Polbud (C-106/16) confirmeert dat louter statutaire zetelverplaatsing op zich geen misbruik is, gebruikt de fiscus de **bestuurszetel-doctrine** (waar wordt de vennootschap werkelijk geleid?) en de **algemene anti-misbruikbepaling** (art. 344 WIB92) om papieren verhuizingen aan te vechten. ATAD CFC-regels kunnen de buitenlandse winst opnieuw bij de uiteindelijke BE-aandeelhouder belasten.

1. Verifieer dat bestuurders fysiek aanwezig zijn in doelland (raden van bestuur ter plaatse)
2. Verifieer dat operationele beslissingen in doelland genomen worden (bank, contracten, personeel)
3. Documenteer de niet-fiscale rationale (governance, opvolging, EU-toegang, talent)
4. Toets PPT (Principal Purpose Test, OESO art. 29 §9) — geen fiscale dominantie als hoofddoel
5. Maak ruling-aanvraag bij DVB indien onzeker

#### 📋 Begeleider

##### Procedure-checklist begeleider (outbound BE → EU) 🔗

De accountant als begeleider coördineert de stappen-volgorde, bewaakt termijnen en verzamelt de documenten voor notaris en buitenlandse counterpart. Centrale rol bij operaties — hier zit de meeste accountant-arbeid.

1. Opmaken financiële situatie + tussentijdse jaarrekening per voorgestelde verplaatsings­datum
2. Berekenen exit-tax-grondslag (latente meerwaarden per actief + vrijgestelde reserves)
3. Opmaken art. 214bis-analyse: welke activa blijven in BE-VI? Welke niet?
4. Coördinatie met notaris voor authentieke akte + voorstel-document
5. Begeleiden bestuursorgaan bij opmaken bestuursverslag
6. Termijn-bewaking schuldeisersverzet + werknemersinformatie
7. Opmaken bestek voor algemene vergadering
8. Aangifte slot-VenB-periode na verplaatsing (met art. 210 §1, 4° afrekening of art. 214bis vrijstelling)
9. Indien BE-VI blijft: opening BNI/ven-fiscale boekhouding + KBO-VI-aanmelding
10. Coördinatie schrapping KBO + neerlegging laatste BE-jaarrekening

##### Procedure-checklist begeleider (inbound EU → BE) 🔗

Spiegel-procedure voor een vennootschap die naar BE verhuist. De accountant zorgt voor de soepele landing in het Belgische rechts- en boekhoudkader.

1. Aanvraag KBO-inschrijving + BTW-nummer op nieuwe BE-zetel
2. Opmaken BE-openingsbalans op basis van laatste balans herkomstland
3. Boekhoudkundige continuïteits-toets (CBN-advies 2018/03): EER-lidstaat of derde Staat met gelijkwaardig boekhoudrecht?
4. Aanpassingen aan BE-waarderingsregels documenteren (verschillen herwerken in eerste BE-jaarrekening)
5. Eerste BE-VenB-aangifte: kies aanvangsdatum boekjaar (CBN: feitelijke verplaatsing heeft geen invloed op statutaire boekjaarduur)
6. Statutenherwerking aan BE-rechtsvorm (BV/NV) + neerlegging notariële akte
7. Informeren stakeholders (bank, klanten, leveranciers) van nieuwe BE-juridische identiteit

#### 🎯 💰 Fiscaal adviseur

##### Exit-tax-berekening + ATAD-spreidingskeuze 🔗

Bij outbound naar EU zonder volledige BE-VI: de accountant berekent de exit-tax-grondslag (verschil tussen werkelijke waarde en boekwaarde per actief) en adviseert over de **spreidings-keuze** onder ATAD: onmiddellijke betaling of spreiding over 5 jaar tegen intrest. Spreiding is bijna altijd voordelig (cashflow-argument); risico = zekerheidstelling vragen door fiscus + intrest-kost.

| Component | Voorbeeld bedrag |
| --- | --- |
| Werkelijke waarde deelneming X (verplaatst naar EU-doelland) | € 10.000.000 |
| Boekwaarde deelneming X | € 3.000.000 |
| Latente meerwaarde (belastbaar) | € 7.000.000 |
| VenB-tarief (2026) | 25 % |
| Exit-tax verschuldigd | € 1.750.000 |
| Optie 1: onmiddellijke betaling | € 1.750.000 in jaar verplaatsing |
| Optie 2: ATAD-spreiding 5 jaar | € 350.000 per jaar + intrest |

⚠️ ATAD-spreiding-modaliteiten (intresttarief, zekerheidstelling, vervroeging bij wederverkoop) zijn omgezet in BE-recht maar exacte art.-nummers en uitvoeringsbesluit te verifiëren. Voor deelnemingen die voldoen aan DBI-meerwaarde-vrijstelling (art. 192 WIB92) kan de exit-tax-grondslag bij outbound onder voorwaarden worden gemilderd — analyseer per actief.

##### DBV-toepassing — tie-breaker bij dubbele inwonerschap 🔗

Wanneer de zetelverplaatsing samenvalt met dubbele inwonerschap (BE en doelland claimen beide woonplaats), grijpt de **tie-breaker** van art. 4 §3 OESO-modelverdrag in: place of effective management bepaalt het verdragsdomicilie. Dit kan voor een overgangsperiode complex zijn — adviseur documenteert het moment van **effectieve leiding-shift** zorgvuldig.

Verwijzing → [[oeso-modelverdrag]] · [[tie-breaker-woonplaats]] (te schrijven)

#### 📋 Boekhouder

##### Afsluiting BE-boekjaar bij outbound + transferbalans 🔗

Op het moment van de outbound-zetelverplaatsing wordt een **tussentijdse balans** opgemaakt die fungeert als (a) de afrekenings­basis voor de exit-tax en (b) de openingsbalans van de vennootschap in haar nieuwe jurisdictie. De accountant zorgt voor consistente waarderingsregels-overgang en documenteert eventuele step-ups op activa die in BE blijven via vaste inrichting.

##### BE-openingsbalans bij inbound — continuïteit of step-up? 🔗

Voor inbound geldt boekhoudkundige continuïteit (CBN-advies 2018/03) — boekwaardes uit herkomstland worden overgenomen, met aanpassingen aan BE-waarderingsregels. ⚠️ Step-up naar werkelijke waarde is fiscaal niet algemeen toegelaten; voor activa die in BE belastbaar worden moet onderzocht worden of art. 184ter (inbreng-step-up-regels) analogisch toepasbaar is.

### 🔍 auditor / commissaris

#### 🔍 Commissaris

##### Bijzondere verklaring bij zetelverplaatsing ⚠️

Indien de vennootschap onder commissarisverplichting valt, levert de commissaris een **bijzondere verklaring** over (a) de boekhoudkundige situatie per voorgenomen verplaatsings­datum (financieel verslag voor de AV), (b) de going-concern-aanname (continuïteit van de activiteit na verplaatsing), en (c) de waardering van activa en passiva in de transferbalans. Analoge regel met commissarisverslag bij omzetting (CBN-advies 2022/16) — exacte WVV-art. te verifiëren onder Boek 14 H.3.

⚠️ Specifieke commissaris-verslagverplichtingen bij grensoverschrijdende omzetting onder WVV Boek 14 + EU-richtlijn 2019/2121 — exacte verwijzing te verifiëren. Verwacht analoog aan binnenlandse omzetting (verslag commissaris + bestuursorgaan).


## Veelvoorkomende verwarringen

###  





## Wat dit record dekt

### Behandelde competenties (chronologisch)

1. **Klant adviseren over keuze zetelverplaatsing vs alternatieven** — zie [Klant adviseren over keuze zetelverplaatsing vs alternatieven](#strategische-keuze-vs-alternatieven)2. **Substance-test vooraf doen — anti-misbruik-screening** — zie [Substance-test vooraf doen — anti-misbruik-screening](#substance-test-vooraf)3. **Procedurele stappen begeleiden — voorstel → AV → akte → registratie** — zie [Procedurele stappen begeleiden — voorstel → AV → akte → registratie](#procedure-checklist)4. **Exit-tax-grondslag berekenen + ATAD-spreidingskeuze adviseren** — zie [Exit-tax-grondslag berekenen + ATAD-spreidingskeuze adviseren](#exit-tax-berekening)5. **Art. 214bis-analyse: welke activa blijven in BE-VI?** — zie [Art. 214bis-analyse: welke activa blijven in BE-VI?](#fiscaal-regime-outbound)6. **Boekhoudkundige continuïteit toepassen bij inbound (CBN 2018/03)** — zie [Boekhoudkundige continuïteit toepassen bij inbound (CBN 2018/03)](#boekhoudkundige-continuiteit)7. **DBV-tie-breaker analyseren bij dubbele inwonerschap** — zie [DBV-tie-breaker analyseren bij dubbele inwonerschap](#dbv-toepassing-na-verplaatsing)8. **Slot-VenB-aangifte + opening BNI/ven of nieuwe BE-aangifte** — zie [Slot-VenB-aangifte + opening BNI/ven of nieuwe BE-aangifte](#procedure-checklist)9. **Commissarisverslag (indien van toepassing) — bijzondere verklaring** — zie [Commissarisverslag (indien van toepassing) — bijzondere verklaring](#continuiteit-verklaring)
### Behandelde termen (alfabetisch)

- **ATAD-spreiding** — zie [↑](#exit-tax-berekening)- **boekhoudkundige continuïteit** — zie [↑](#boekhoudkundige-continuiteit)- **Cartesio-arrest** — zie [↑](#hvj-rechtspraak)- **EU-mobiliteitsrichtlijn 2019/2121** — zie [↑](#wettelijke-voorwaarden)- **exit-tax** — zie [↑](#fiscaal-regime-outbound)- **inbound zetelverplaatsing** — zie [↑](#fiscaal-regime-inbound)- **outbound zetelverplaatsing** — zie [↑](#fiscaal-regime-outbound)- **place of effective management** — zie [↑](#dbv-toepassing-na-verplaatsing)- **Polbud-arrest** — zie [↑](#hvj-rechtspraak)- **statutaire zetel vs werkelijke zetel** — zie [↑](#wettelijke-voorwaarden)- **substance-test** — zie [↑](#substance-test-vooraf)- **Vale-arrest** — zie [↑](#hvj-rechtspraak)- **werknemersmedezeggenschap** — zie [↑](#wettelijke-voorwaarden)
### Behandelde formules

- {'naam': 'Exit-tax-grondslag per actief', 'expressie': 'werkelijke waarde − fiscale boekwaarde = belastbare latente meerwaarde'}
- {'naam': 'ATAD-spreiding', 'expressie': 'exit-tax / 5 = jaarlijkse betaling + intrest (tarief en modaliteiten in BE-omzetting)'}


