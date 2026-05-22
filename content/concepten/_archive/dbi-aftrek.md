---
title: DBI-aftrek (Definitief Belaste Inkomsten — art. 202-205 WIB92)
tags:
- concept
- fiscale-regeling
- po-2-3
- po-2-8
linked_anchors:
- 2.3.II.B
- 2.3.II.F
- 2.3.taak.3
- 2.8.XV
programmaonderdelen:
- '2.3'
- '2.8'
confidence: grounded
node_type: fiscale-regeling
status: seed
schema_version: '2.0'
gegenereerd_uit: data/concepten/records/dbi-aftrek.json
gegenereerd_op: '2026-05-21'
---
# DBI-aftrek (Definitief Belaste Inkomsten — art. 202-205 WIB92) ⚖️

> [!summary] Korte inhoud
> **Definitief Belaste Inkomsten** (DBI) is de Belgische vennootschapsbelasting-techniek waarmee een vennootschap die dividenden ontvangt van een dochter-vennootschap die zelf al normaal werd belast, deze dividenden voor **100%** uit haar belastbare basis mag aftrekken — mits drie….

**Definitief Belaste Inkomsten** (DBI) is de Belgische vennootschapsbelasting-techniek waarmee een vennootschap die dividenden ontvangt van een dochter-vennootschap die zelf al normaal werd belast, deze dividenden voor **100%** uit haar belastbare basis mag aftrekken — mits drie cumulatieve voorwaarden vervuld zijn (deelnemingsdrempel + aanhoudtermijn + taxatievoorwaarde). Doel: **economische dubbele belasting** op dezelfde vennootschapswinst voorkomen wanneer ze door een keten van vennootschappen reist.

_Bron: WIB92 art. 202-205_



## Wat er economisch echt gebeurt 🔗

Een vennootschapswinst wordt **één keer** belast: bij de dochter. Wanneer die dochter haar netto-winst als dividend uitkeert aan haar moedervennootschap, zou diezelfde winst zonder DBI **een tweede keer** belast worden bij de moeder (dividend = belastbaar bestanddeel art. 24 WIB92). De DBI-aftrek herstelt dit door het ontvangen dividend in eerste orde uit de belastbare grondslag te lichten — *na* gewone aftrek beroepskosten, *vóór* overgedragen verliezen.

Economisch is DBI géén vrijstelling van het dividend zelf — het is een **technische aftrek** uit de belastbare winst, in een wettelijk vastgelegde volgorde (art. 207 WIB92). Als de winst van het belastbaar tijdperk onvoldoende is om de aftrek volledig op te slorpen, kan het overschot **overgedragen** worden naar volgende belastbare tijdperken (sinds wet 25 dec 2017). Dit lost het oude probleem op dat DBI in een verliesjaar verloren ging.


## Voorkennis & leespad

- **Lees eerst** (voorvereisten):
  [[vennootschapsbelasting-kader]]
  [[belastbare-grondslag-vennootschapsbelasting]]

- **Past binnen kader**: [[vennootschapsbelasting-kader]]

- **Naast deze fiche relevant**:
  [[vvprbis]]
  [[liquidatiereserve]]
  [[moedervennootschap]]
  [[dochteronderneming]]

- **Bij vervolgvragen**:
  [[meerwaarde-aandelen-venb]]
  [[verworpen-uitgaven]]


## Wanneer van toepassing

DBI is geen keuze maar een **automatisch werkend regime**: zodra een vennootschap-aandeelhouder een dividend ontvangt en de drie cumulatieve voorwaarden vervuld zijn, is de aftrek van toepassing. De accountant moet dus per dividend-ontvangst de voorwaarden **toetsen** — niet de regeling 'kiezen'.


### Voor wie

Elke **binnenlandse vennootschap** die onderworpen is aan de vennootschapsbelasting en die dividenden ontvangt van een andere vennootschap. Typisch:
- **Holdingvennootschappen** die deelnemingen aanhouden in operationele dochters.
- **Operationele vennootschappen** met een minderheidsparticipatie in een joint-venture of leverancier/klant.
- **Familiale moedervennootschappen** in een KMO-groepstructuur. 🧭


### Wanneer wel

- ⚖️ Dividend van een **binnenlandse dochter** die zelf vennootschapsbelasting betaalt — taxatievoorwaarde automatisch vervuld.
  _De Belgische dochter is by-definition onderworpen aan VenB tegen het gemene tarief — art. 203 §1 1° vereist enkel uitsluiting van niet-belaste of gunstig-belaste vennootschappen._

- ⚖️ Dividend van een **EU-dochter** waarvan de moeder ≥ 10 % bezit gedurende ≥ 1 jaar.
  _De moeder-dochterrichtlijn 2011/96/EU verplicht België als lidstaat van de moeder om de dubbele belasting weg te nemen (vrijstellings- of credit-methode) — België koos vrijstelling via art. 202-205 WIB92._

- 🔗 Dividend van een **niet-EU-dochter** uit een verdragsland zonder gunstig regime, met deelnemingsdrempel + aanhoudtermijn vervuld.
  _Buiten EU geldt geen richtlijn-verplichting, maar art. 202-203 WIB92 maken geen onderscheid naar herkomst zolang de taxatievoorwaarde vervuld is._


### Wanneer niet

- ⚖️ Dochter is gevestigd in een **belastingparadijs** of een land met **aanzienlijk gunstigere** gemeenrechtelijke belasting (nominaal tarief < 15 % of effectief gemiddeld tarief < 15 %).
  _Art. 203 §1 1° sluit dit expliciet uit; ratio: DBI mag geen kanaal worden voor witwas-via-laag-belast-buitenland._

- ⚖️ Dochter staat op de **EU-lijst van niet-coöperatieve rechtsgebieden** op einde belastbaar tijdperk.
  _Sinds 2018 expliciet toegevoegd aan art. 203 §1 1° — automatische uitsluiting._

- ⚖️ Dividend afkomstig van een **kunstmatige rechtshandeling** waarvan een hoofddoel was de DBI of de moeder-dochter-richtlijn-voordelen te bekomen.
  _Art. 203 §1 7° + algemene anti-misbruik-bepaling — sluit DBI uit bij structuren zonder economische substantie._

- ⚖️ Dividend uit een **inrichting in het buitenland** waarvan de winst krachtens een dubbelbelasting-verdrag is vrijgesteld.
  _Art. 205 §1 — DBI niet bovenop bestaande vrijstelling stapelen._


### Hoofdrisico

**Verlies van de aftrek door een gemiste voorwaarde** — typisch: de aandelen worden verkocht **vóór** het verstrijken van de éénjaars-aanhoudtermijn, of de moeder krijgt het dividend uitgekeerd terwijl ze haar 10%-deelneming net heeft afgebouwd. Gevolg: het hele dividend valt terug in de belastbare grondslag — een tarief-impact van **25 %** op het bruto-dividend. 🧭

### Hoofdvoordeel

**Volledige neutralisatie van de dubbele belasting** binnen een groepsstructuur — winst kan zonder fiscale erosie van dochter naar moeder doorvloeien, wat **kapitaal-allocatie** en **dividend-cascade** in een holdingstructuur economisch viable maakt. 🧭


## Hoe het werkt

De DBI-aftrek werkt in twee tijden: (1) bepaal het **aftrekbare bedrag** (art. 202 + 204), (2) trek het af van de winst volgens de wettelijke **volgorde** (art. 207). De toets aan de drie voorwaarden gebeurt **per dividend** (per uitkering) — niet per boekjaar.

### Aftrekpercentage: 100 % 🧭

Sinds wet van 25 december 2017 (aanslagjaar 2019) bedraagt het DBI-aftrekpercentage **100 %** van het bruto-dividend (vroeger 95 %). Vóór die hervorming bleef 5 % van het dividend belastbaar — die 'restbelasting' is nu volledig weggewerkt.

100 % aftrek = volledige neutralisatie binnen de moeder. Dit aligneert België met de meeste EU-lidstaten die ook 100 % toepassen onder de moeder-dochter-richtlijn.

### Voorwaarde 1 — Deelnemingsdrempel (art. 202 §2 1°) ⚖️

De moeder bezit op datum van toekenning/betaalbaarstelling van het dividend ofwel **≥ 10 %** van het kapitaal van de uitkerende vennootschap, ofwel een deelneming met een **aanschaffingswaarde ≥ 2 500 000 EUR**. De twee criteria zijn alternatief — één volstaat.

_Bron: WIB92 art. 202 §2 1° (drempel uit art. 264/1 §1)_

| Criterium | Drempel | Toepassingsmoment |
| --- | --- | --- |
| Kapitaalpercentage | ≥ 10 % | datum toekenning/betaalbaarstelling dividend |
| Aanschaffingswaarde | ≥ 2 500 000 EUR | datum toekenning/betaalbaarstelling dividend |

### Voorwaarde 2 — Aanhoudtermijn 1 jaar in volle eigendom ⚖️

De aandelen worden of werden gedurende een **ononderbroken periode van ten minste één jaar** in **volle eigendom** behouden — én ze hebben de **aard van financiële vaste activa**. De termijn mag vóór of na de uitkering vol lopen (wettelijk: 'worden of werden behouden'), maar de aftrek wordt pas definitief wanneer de éénjaars-termijn vervuld is.

_Bron: WIB92 art. 202 §2 2°_

**Volle eigendom** = niet enkel naakte eigendom of vruchtgebruik. Bij splitsing van eigendomsrechten (bv. successieplanning) kan de DBI verloren gaan voor de vruchtgebruiker. **Financiële vaste activa** = boekhoudkundige rubriek 28 — dwz aandelen aangehouden met intentie van duurzame band (KB WVV art. 3:89). Aandelen in geldbeleggingen (rubriek 51) kwalificeren niet.

### Voorwaarde 3 — Taxatievoorwaarde (art. 203) ⚖️

De uitkerende vennootschap mag **niet** onder een van de uitsluitings-categorieën van art. 203 §1 vallen. Zes hoofdcategorieën:
1. Vennootschappen niet onderworpen aan VenB of buitenlandse gelijkaardige belasting.
2. Vennootschappen in een land met aanzienlijk gunstiger gemeenrechtelijke belasting (nominaal tarief < 15 % of effectief gemiddeld tarief < 15 %).
3. Vennootschappen op de EU-lijst van niet-coöperatieve rechtsgebieden.
4. Bepaalde financierings-, thesaurie- of beleggingsvennootschappen met afwijkend regime.
5. Doorgift-vennootschappen die zelf voor het dividend geen aftrek-recht zouden hebben (anti-cascade-bepaling).
6. Kunstmatige rechtshandelingen opgezet om DBI/richtlijnvoordeel te bekomen (anti-misbruik).

_Bron: WIB92 art. 203 §1_

🧭 **Geen-cascade-regel**: ook wanneer alle individuele schakels op zich aan de voorwaarden voldoen, kan een dividend dat **doorheen** een uitsluitings-vennootschap is gestroomd (bv. via een tussenholding in een laag-belast land) zijn DBI-recht verliezen — art. 203 §3.

### Aftrekbaar bedrag = bruto-dividend (art. 204) ⚖️

Art. 204: het aftrekbare bedrag is het **geïnde of verkregen bedrag, eventueel vermeerderd met de roerende voorheffing (RV) of fictieve RV**. Praktisch: men 'gross-up't het netto-ontvangen dividend tot het bruto-bedrag waarvan inhouding plaatsvond — die bruto-grondslag is het bedrag dat de winst in en uit gaat.

_Bron: WIB92 art. 204_

| Stap | Bedrag |
| --- | --- |
| Netto-dividend ontvangen | 70 000 EUR |
| RV ingehouden door dochter (30 %) | 30 000 EUR |
| Bruto-dividend (= aftrekbaar onder DBI) | 100 000 EUR |
| Belastbare grondslag-impact | +100 000 (dividend in winst) − 100 000 (DBI-aftrek) = 0 |

### Volgorde van de aftrek (art. 207) ⚖️

DBI wordt afgetrokken in **eerste orde** uit de winst van het belastbaar tijdperk — vóór innovatie-aftrek, vóór NID, vóór overgedragen verliezen. Wettelijke volgorde (art. 207 lid 2):
1. Aftrek art. 202-205 (DBI) — uitsluitend lopende DBI, niet overgedragen.
2. Aftrek art. 543 (octrooi-inkomsten — uitdovend).
3. Aftrek art. 205/1-205/4 (innovatie-inkomsten).
4. Aftrek voor risicokapitaal (NID).
5. Overgedragen DBI.
6. Overgedragen verliezen.

_Bron: WIB92 art. 207_

1. Bepaal winst van belastbaar tijdperk na art. 199 (vrijgestelde inkomsten)
2. Pas correcties art. 205 §2 toe (verworpen kosten + giften terugnemen voor DBI-grondslag)
3. Trek DBI van lopend tijdperk af (in eerste orde)
4. Pas vervolgens innovatie, NID, overgedragen DBI, overgedragen verliezen toe
5. Restant winst → VenB-tarief

### Overdracht DBI-overschot (sinds wet 25 dec 2017) 🧭

Als de winst van het belastbaar tijdperk onvoldoende is om de DBI volledig op te slorpen, mag het **niet-gebruikte deel** worden overgedragen naar volgende belastbare tijdperken — zonder tijdslimiet. Vóór 2017 ging dit overschot definitief verloren in verliesjaren. Belangrijk om holding-structuren te beschermen tegen 'verloren' DBI in cyclische winstjaren.

De overdracht is geconditioneerd: enkel het deel dat niet onder de minimum-belastbare-basis ('art. 207 cap', 'Fairness Tax 2.0') valt, kan worden gebruikt.

### Uitbreiding naar meerwaarden op aandelen (art. 192) ⚖️

Art. 192 koppelt de vrijstelling van **meerwaarden op aandelen** aan de DBI-voorwaarden: een meerwaarde is volledig vrijgesteld in de mate dat de eventuele dividenden op die aandelen onder DBI zouden vallen (taxatievoorwaarde art. 203 + 10%/2,5 mio + 1 jaar volle eigendom). Eén en hetzelfde voorwaardenset bepaalt dus zowel de dividenden- als de meerwaarden-vrijstelling.

_Bron: WIB92 art. 192 §1_

| Voorwaarde | DBI-dividend (art. 202) | Meerwaarde aandelen (art. 192) |
| --- | --- | --- |
| Taxatievoorwaarde art. 203 | Ja | Ja |
| Deelnemingsdrempel 10 % of 2,5 mio EUR | Ja | Ja |
| Aanhoudtermijn 1 jaar in volle eigendom | Ja | Ja |
| Aftrek-/vrijstellingspercentage | 100 % | 100 % |


## Rol van de accountant

DBI raakt drie typische perspectieven: de **ontvangende moedervennootschap** (cliënt), de **uitkerende dochter** (vaak ook cliënt of zusterdossier) en de **auditor** die de jaarrekening van de moeder of dochter controleert. Voor de aandeelhouder-natuurlijke-persoon is DBI niet rechtstreeks relevant — wel via VVPRbis en RV.

### 🏢 ontvangende moedervennootschap (cliënt)

#### 🎯 Adviseur

##### Pre-investerings-screening van de dochter 🧭

Vóór de moeder beslist om een dochter te verwerven of haar deelneming uit te breiden naar 10 %, screen de **taxatievoorwaarde**: is de dochter aan een normaal regime onderworpen? Onderzoek het fiscale woonplaats-land, het nominale en effectieve VenB-tarief, en check de EU-lijst van niet-coöperatieve rechtsgebieden.

1. Vraag fiscale woonplaats-attest dochter op
2. Onderzoek nominaal tarief vs 15%-drempel art. 203 §1 1°
3. Check EU-lijst niet-coöperatieve rechtsgebieden actuele versie
4. Bij gunstig regime: documenteer afweging — DBI gaat verloren
5. Adviseer eventueel rechtsvorm-aanpassing of houdststructuur-wijziging

##### Houdtermijn bewaken bij voorgenomen verkoop 🧭

Wanneer de moeder een verkoop van haar deelneming overweegt **vóór** 1 jaar volle eigendom, waarschuw expliciet voor verlies van DBI op alle tussentijdse dividenden + verlies van art. 192-vrijstelling op de meerwaarde zelf. Reken het tarief-effect (typisch 25 %) door in de scenario-analyse.

#### 📋 Boekhouder

##### Boekhoudkundige verwerking ontvangen dividend onder DBI 🔗

Het dividend wordt boekhoudkundig **bruto** geboekt als opbrengst van financiële vaste activa (rekening 750). De RV-inhouding is een verrekenbare vordering op de fiscus (rekening 412 — terug te vorderen belastingen of 416 — diverse vorderingen). De DBI-aftrek zelf gebeurt **buiten de boekhouding** — in de fiscale aangifte (vak 'Aftrek DBI').

*Bij ontvangst dividend*

| Rekening | Naam | Debet | Credit |
|---:|---|---:|---:|
| 550 | Bank | 70000 | — |
| 412 | Te verrekenen RV | 30000 | — |
| 750 | Opbrengsten financiële vaste activa | — | 100000 |

⚠️ Voor moeder-dochterdividenden binnen de EU (≥ 10 % + 1 jaar) wordt geen RV ingehouden (art. 264/1 + EU-richtlijn art. 5) — netto = bruto, geen rekening 412.

##### Documentatie 'aard financieel vast actief' bewaken 🧭

Houd in het permanent fiscaal dossier per deelneming bij: aanschaffingsdatum, aanschaffingswaarde, kapitaalpercentage en intentie van duurzaam aanhouden (FVA-classificatie). Verschuiving van rubriek 28 naar rubriek 51 (geldbeleggingen) breekt de DBI-aanspraak — markeer als kritiek aandachtspunt bij heroverweging van strategische beslissingen.

#### 📑 Fiscaal

##### Aangifte VenB — opvulling DBI-vakken 🧭

In het aangifteformulier VenB wordt het bruto-dividend opgenomen in de **belastbare basis** (vak resultaat) én apart als **aftrekbaar onder DBI** (specifiek aftrekvak met onderscheid Belgische / EU / niet-EU-oorsprong). Bijlage 275-DBI documenteert per deelneming: identiteit dochter, kapitaalpercentage, aanschaffingsdatum, bruto-dividend, claim-onder-art. 202.

##### Beperking tot winstrestant (art. 205 §2) ⚖️

De DBI-aftrek wordt **beperkt** tot het bedrag van de winst dat overblijft na art. 199 verminderd met o.a. niet-aftrekbare giften, bepaalde art. 53-kosten (6° tot 11°, 14°, 21° tot 24°), niet-aftrekbare interesten (art. 54-55) en aanvullende premies. Praktisch: bepaalde **verworpen uitgaven** mogen niet weggemoffeld worden via DBI.

_Bron: WIB92 art. 205 §2_

### 🏭 uitkerende dochter (cliënt of zusterdossier)

#### 📑 Fiscaal

##### RV-vrijstelling bij uitkering aan EU-moeder (art. 264/1) ⚖️

Wanneer de dochter een dividend uitkeert aan een EU-moeder of een verdragslandsmoeder die ≥ 10 % deelneming aanhoudt gedurende ≥ 1 jaar, wordt **géén roerende voorheffing** ingehouden. Voorwaarden: rechtsvorm uit bijlage I-A richtlijn 2011/96/EU, fiscaal inwoner van EER of verdragsland met inlichtingenuitwisseling. Bij minder dan 10 % maar aanschaffingswaarde ≥ 2 500 000 EUR geldt een soortgelijke vrijstelling.

_Bron: WIB92 art. 264/1 §1; Richtlijn 2011/96/EU art. 5_

##### Attest moederstatus opvragen vóór RV-vrijstelling 🧭

De dochter moet vóór uitkering een attest van de moeder ontvangen waarin: (1) deelnemingspercentage of aanschaffingswaarde, (2) datum van verkrijging in volle eigendom, (3) fiscale woonplaats, (4) bevestiging dat de aandelen op uitkeringsdatum ≥ 1 jaar in eigendom zijn. Zonder attest = RV moet ingehouden worden, moeder kan ze later in haar VenB-aangifte terugvragen indien voorwaarden alsnog vervuld bleken.

### 🔍 auditor / commissaris

#### 🔍 Controleur

##### Controle DBI-claim in jaarrekening + fiscale aangifte 🧭

Controleer per gekrediteerde DBI: (1) bestaan van het dividend (bankuittreksel + AV-beslissing dochter), (2) classificatie dochter als FVA (rubriek 28), (3) deelnemingsdrempel-bewijs (aandeelhoudersregister + transactie-historiek), (4) aanhoudtermijn (verwervingsdatum), (5) taxatievoorwaarde (jaarrekening dochter of attest), (6) afwezigheid van uitsluitingsgrond art. 203. Bij grensoverschrijdende dividenden: bevestig dat dochter onder bijlage I richtlijn valt of dat verdragsland met inlichtingenuitwisseling van toepassing is.

##### Fiscaal risico bij twijfel art. 203 taxatievoorwaarde 🧭

Wanneer bij grensoverschrijdende structuren onduidelijkheid bestaat over de toepassing van art. 203 (bv. bij hybride entiteiten of complexe holdingstructuren), overweeg: (a) voorziening voor uitgesteld belasting-risico, (b) toelichting in jaarrekening, (c) eventueel ruling-aanvraag bij DVB. Een achteraf afgewezen DBI leidt tot bijbelasting tegen 25 % VenB + 6,75 % belastingvermeerdering bij gebrek aan voldoende voorafbetalingen.


## Veelvoorkomende verwarringen

### DBI vs Moeder-dochterrichtlijn ⚖️

De **EU-moeder-dochterrichtlijn 2011/96/EU** is een Europese richtlijn die elke EU-lidstaat verplicht om dubbele belasting weg te nemen — ze laat lidstaten kiezen tussen vrijstellings- en credit-methode. **DBI** is de Belgische uitvoering van die verplichting via aftrek-methode. De voorwaarden vallen grotendeels samen (10 % + 1 jaar), maar art. 202-203 WIB92 gaat verder: DBI geldt ook voor niet-EU-dividenden en kent eigen Belgische uitzonderingen (art. 203 §1 7° anti-misbruik).

### DBI vs VVPRbis 🔗

**DBI** werkt op niveau van de **ontvangende vennootschap** (verlaagt VenB-grondslag). **VVPRbis** werkt op niveau van de **ontvangende natuurlijke persoon** (verlaagt roerende voorheffing van 30 % naar 20 %/15 %). Beide regimes raken dezelfde dividend-stroom in een typische KMO-keten (Dochter → Holding-moeder → Aandeelhouder-NP), maar grijpen op verschillende schakels in. Voor een vennootschap-aandeelhouder is VVPRbis irrelevant — DBI doet het werk al volledig.

### Aftrek vs vrijstelling 🧭

DBI is technisch een **aftrek** (winstcorrectie na opname in belastbare basis), géén vrijstelling (waarbij het dividend nooit in de basis komt). Praktisch gevolg: DBI vereist altijd **voldoende winst** om op te slorpen; sinds 2017 lost de overdraagbaarheid dit op. Een vrijstelling zou geen winstrestant nodig hebben. Belangrijk voor interpretatie van art. 207-volgorde en interactie met andere aftrekken.

### DBI vs FBB (forfaitair gedeelte buitenlandse belasting) 🧭

**DBI** schakelt de dividend-belasting uit op winstniveau. **FBB** (art. 285-289 WIB92) is een verrekenbaar belastingkrediet voor *intresten en royalty's* uit het buitenland — een ander instrument, andere belastbare bestanddelen, andere techniek (verrekening na tariefberekening i.p.v. aftrek voor tariefberekening).


## Alternatieven (zelfde doel)

Andere technieken om dubbele belasting op grensoverschrijdende of binnenlandse winstdoorgift te vermijden of te verzachten:

- **Verrekening buitenlandse belasting onder dubbelbelasting-verdrag** — Credit-methode in plaats van vrijstelling — bilaterale verdragen kunnen DBI vervangen of aanvullen voor specifieke landen.
- **Liquidatiereserve** — Geen alternatief voor DBI maar voor de aandeelhouder-NP: 10 % anticipatieve heffing + 5 % RV bij uitkering ≥ 5 jaar — komt na DBI in de uitkeringsketen. → [[liquidatiereserve]]
- **VVPRbis** — Voor aandeelhouder-NP van een KMO; raakt de RV bij eind-uitkering, niet de DBI op tussenliggend dividend. → [[vvprbis]]

## Wat dit record dekt

### Behandelde competenties (chronologisch)

1. **Pre-investerings-screening dochter op taxatievoorwaarde** — zie [Pre-investerings-screening dochter op taxatievoorwaarde](#voorwaarden-screening-vooraf)2. **Deelnemingsdrempel toetsen (10 % of 2,5 mio EUR)** — zie [Deelnemingsdrempel toetsen (10 % of 2,5 mio EUR)](#voorwaarde-1-deelnemingsdrempel)3. **Aanhoudtermijn 1 jaar in volle eigendom bewaken** — zie [Aanhoudtermijn 1 jaar in volle eigendom bewaken](#voorwaarde-2-aanhoudtermijn)4. **Taxatievoorwaarde art. 203 toetsen** — zie [Taxatievoorwaarde art. 203 toetsen](#voorwaarde-3-taxatievoorwaarde)5. **Bruto-dividend grossing-up (art. 204)** — zie [Bruto-dividend grossing-up (art. 204)](#aftrekbaar-bedrag-bruto-grossing-up)6. **DBI invoegen in aftrekvolgorde art. 207** — zie [DBI invoegen in aftrekvolgorde art. 207](#aftrekvolgorde-art-207)7. **Boekhoudkundige verwerking dividend + DBI buiten boekhouding** — zie [Boekhoudkundige verwerking dividend + DBI buiten boekhouding](#boeking-ontvangen-dividend-met-dbi)8. **RV-vrijstelling bij moeder-dochter (EU)** — zie [RV-vrijstelling bij moeder-dochter (EU)](#rv-vrijstelling-moeder-dochter)9. **DBI-aangifte vakken + bijlage 275-DBI** — zie [DBI-aangifte vakken + bijlage 275-DBI](#aangifte-vak-dbi)10. **Auditcontrole DBI-claim in jaarrekening** — zie [Auditcontrole DBI-claim in jaarrekening](#audit-dbi-claim)
### Behandelde termen (alfabetisch)

- **Aanhoudtermijn 1 jaar** — zie [↑](#voorwaarde-2-aanhoudtermijn)- **Aftrekvolgorde art. 207** — zie [↑](#aftrekvolgorde-art-207)- **Belastingparadijs-uitsluiting** — zie [↑](#voorwaarde-3-taxatievoorwaarde)- **Deelnemingsdrempel** — zie [↑](#voorwaarde-1-deelnemingsdrempel)- **EU-lijst niet-coöperatieve rechtsgebieden** — zie [↑](#voorwaarde-3-taxatievoorwaarde)- **Financieel vast actief (FVA)** — zie [↑](#voorwaarde-2-aanhoudtermijn)- **Grossing-up (art. 204)** — zie [↑](#aftrekbaar-bedrag-bruto-grossing-up)- **Moeder-dochterrichtlijn 2011/96/EU** — zie [↑](#rv-vrijstelling-moeder-dochter)- **Overdracht DBI-overschot** — zie [↑](#overdracht-dbi-overschot)- **Taxatievoorwaarde art. 203** — zie [↑](#voorwaarde-3-taxatievoorwaarde)
### Behandelde formules

- {'naam': 'Bruto-dividend (DBI-grondslag)', 'expressie': 'netto-ontvangen + ingehouden RV (eventueel + fictieve RV)'}
- {'naam': 'Belastbare-grondslag-impact', 'expressie': '+bruto-dividend (in winst) − DBI-aftrek = 0 bij vervulde voorwaarden'}


## Zie ook

- **Vereist kennis van**: [[]]
- **Vereist kennis van**: [[]]

## Bronnen

[^1]: `WIB92__art_202__sub_1deg-3deg`
[^2]: `WIB92__art_203__sub_1deg-6deg`
[^3]: `WIB92__art_205`
[^4]: `WIB92__art_207`
[^5]: `EU-Richtlijn-moeder-dochter-2011-96__art_4`
[^6]: `EU-Richtlijn-moeder-dochter-2011-96__art_3`
[^7]: `WIB92__art_203__sub_7deg-1deg`
[^8]: `WIB92__art_264/1`
[^9]: `Wet-voorafgaande-beslissingen-2002__art_9`
[^10]: `WIB92__art_204`
[^11]: `WIB92__art_192`
[^12]: `EU-Richtlijn-moeder-dochter-2011-96__art_5`
