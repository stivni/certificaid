---
title: "Aandeelhoudersovereenkomsten"
concept_type: "instrument"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 3.0.IV.C
tags:
  - concept
  - schema-2.2
  - type-instrument
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/aandeelhoudersovereenkomsten.json"
---

# Aandeelhoudersovereenkomsten

_Instrument_

📋 Regeling · Anchors: `3.0.IV.C` · Wave: `skeleton-vennootschapsrecht-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Afk.**: SHA — **Synoniemen**: shareholders agreement · SHA · syndicaatsovereenkomst · aandeelhoudersovereenkomst — **Vertalingen**: fr: pacte d'actionnaires

## Definitie

📖 Een aandeelhoudersovereenkomst (SHA — Shareholders Agreement) is een privaatrechtelijk contract tussen twee of meer aandeelhouders van eenzelfde vennootschap waarin zij afspraken maken over de uitoefening van hun aandeelhoudersrechten — typisch over (a) controle en stemcoördinatie, (b) overdracht en exit van aandelen, (c) board-vertegenwoordiging, (d) winstuitkering en dividend-beleid, (e) vetorechten en bijzondere meerderheden. De SHA is een aanvulling op de statuten en het WVV — geen vervanging. Bindingskracht beperkt tot ondertekenaars (relativiteit van het contract, art. 1165 oud BW / 5.103 nieuw BW); de vennootschap is in principe geen partij tenzij ze meetekent. Aanvaard door WVV art. 5:34 (BV) en 7:79-7:80 (NV) — stemovereenkomsten zijn uitdrukkelijk geldig binnen bepaalde grenzen.

<small>📚 WVV — art. 5:34 — _wettekst_ · WVV — art. 7:79 — _wettekst_ · WVV — art. 7:80 — _wettekst_</small>

## Substantie

🔗 De SHA is het 'tweede leven' van vennootschapsrecht buiten de statuten. Voordeel: privacy (geen publicatie in KBO, ondertegenstelbaar voor derden) en flexibiliteit (kan gedetailleerder zijn dan statuten kunnen). Nadeel: relativiteit — geen tegenstelbaarheid aan derde verkrijger zonder kennisgeving; geen rechtstreekse 'reële' uitvoering (art. 1142 oud BW / 5.85 nieuw BW: niet-nakoming verbintenis = schadevergoeding, geen automatische dwang). Bij belangrijke clausules (voorkooprecht, lock-up) verkiest men daarom dubbele verankering: statutair (tegenwerpelijk aan iedereen, ook nieuwe aandeelhouders) + contractueel (bijkomende sancties bv. boetebeding, gedwongen verkoop). Common law-clausules zoals drag-along, tag-along, leaver-clausules zijn vrijelijk in Belgisch recht inzetbaar mits respect voor openbare orde en goede zeden.

<small>📚 BW — art. 1142 (oud) / 5.85 (nieuw) — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 Waarom een SHA naast de statuten? (1) Privacy — statuten worden gepubliceerd via KBO; SHA blijft onder partijen. (2) Detailniveau — SHA kan complexere voorwaarden bevatten (tag-along percentages, leaver-prijsformules) die de statuten conceptueel niet vatten. (3) Tijdelijke afspraken — SHA's hebben vaak een looptijd (5-10 jaar); statuten zijn permanent tot wijziging. (4) Bilateraal versus erga omnes — SHA bindt alleen ondertekenaars; statuten binden ook nieuwe aandeelhouders. (5) Sancties — SHA kan boetes en gedwongen verkoop bevatten die statutair moeilijker te schrijven zijn.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: WVV art. 5:34 (BV) · 7:79-7:80 (NV) + gemeenrechtelijk contractenrecht (boek 5 + 6 BW)

Geldig in beginsel sinds altijd; gecodificeerd onder WVV met expliciete erkenning stemovereenkomsten.

**✅ Voor**
- 🔗 Typisch ingezet bij: (a) joint ventures (verdeling 50/50 of 60/40, deadlock-mechanismen); (b) familievennootschappen (afspraken tussen generaties); (c) start-ups met investeerders (preferent dividend, anti-dilution, exit-rechten); (d) management buy-out / leveraged buy-out (rol management vs financier); (e) opvolging-overdracht (gefaseerde overname met earn-out).

**📋 Voorwaarden**
- 📖 Geldigheidsvoorwaarden contract (art. 5.27 nieuw BW): (1) toestemming partijen; (2) bekwaamheid; (3) bepaald voorwerp; (4) geoorloofde oorzaak. Specifiek voor SHA-stemovereenkomsten (art. 5:34 BV / 7:80 NV WVV): (a) beperkt in de tijd (anders nietigheid wegens onbepaalde looptijd); (b) verenigbaar met vennootschapsbelang; (c) niet in strijd met WVV-bepalingen (bv. NIET 'altijd voor goedkeuring jaarrekening stemmen' — schending wettelijke beoordelingsplicht).

**⛔ Uitsluitingen**
- 📖 Nietige SHA-clausules: (a) stemverbintenissen voor onbepaalde tijd of voor onbeperkte materies (art. 7:80 §2); (b) clausule die wettelijke minderheidsrechten uitschakelt (art. 2:60 minderheidsvordering bv. niet contractueel weg te bedingen); (c) clausules in strijd met goede zeden of openbare orde; (d) verbintenissen die de bestuursonafhankelijkheid van bestuurders ondermijnen (bv. bestuurder die zich engageert 'tegen het vennootschapsbelang' te stemmen — nietig).

**⚠️ Risico**
- 🔗 Sancties bij schending SHA: meestal contractuele schadevergoeding (art. 1142 oud BW); slechts uitzonderlijk gedwongen uitvoering (verkoop aandelen aan koper indien gerechtelijke vordering binnen redelijke termijn). Verkrijger te goeder trouw die niet wist van SHA-beperking is in principe beschermd — daarom de gelaagde aanbeveling: dubbele verankering statutair + contractueel + neerlegging SHA-uittreksel in aandeelhoudersregister voor 'kennis-fictie'.

## Bouwstenen

### 📜 Stand-stillclausule (lock-up)  
_`regel`_

🔗 Verbintenis van een aandeelhouder om gedurende een bepaalde periode (typisch 3-7 jaar) zijn aandelen NIET over te dragen, te verpanden of te bezwaren. Doel: rust in aandeelhouderschap, vermijden 'free riders' die mee profiteren van waardestijging en dan vroegtijdig uitstappen, voldoende horizon voor strategische beslissingen.

**Uitwerking**:
- Looptijd: noodzakelijk bepaald (art. 1129 oud BW); typisch 3-7 jaar; oneindige duur = nietigheid.
- Uitzonderingen vaak voorzien: schenking aan eerste-graads-familie, overdracht binnen consortium, overlijden, gedwongen uitvoering door schuldeisers.
- Sancties: forfaitaire boete (X% van transactieprijs) + verplichting tot herstel (verkoper moet aandelen terugkopen).
- Combinatie met voorkooprecht: lock-up gevolgd door voorkooprecht is klassieke twee-staps-bescherming.

**Praktische tip**: noteer in aandeelhoudersregister 'aandelen onderworpen aan lock-up SHA dd. xx-xx-xxxx tot xx-xx-xxxx' — verschaft kennis aan nieuwe verkrijgers en versterkt afdwingbaarheid.

<small>📚 WVV — art. 5:62 — _wettekst_ · BW — art. 5.27 (nieuw) — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📜 Voorkooprecht (SHA) — Right of First Refusal (ROFR)  
_`regel`_

🔗 Contractueel recht van bestaande aandeelhouders om voorrang te krijgen wanneer een mede-aandeelhouder zijn aandelen wil verkopen. Mechaniek typisch:

1. Verkopende aandeelhouder ontvangt bod van derde partij X met prijs P.
2. Verkoper notificeert mede-aandeelhouders: 'derde X biedt P voor mijn aandelen — wenst u voorkoop?'
3. Mede-aandeelhouders hebben een termijn (typisch 15-30 dagen) om mee te delen of ze de aandelen aan dezelfde voorwaarden willen overnemen.
4. Bij uitoefening voorkoop: aandelen gaan naar mede-aandeelhouders pro rata of volgens afgesproken verdeelsleutel.
5. Bij geen-uitoefening: verkoper mag verkopen aan X aan dezelfde of betere voorwaarden binnen bepaalde termijn.

**Verschil met wettelijk voorkeurrecht (art. 5:128/7:188)**: voorkeurrecht bij uitgifte NIEUWE aandelen (kapitaalverhoging); voorkooprecht SHA bij verkoop BESTAANDE aandelen aan derde. Verschillende mechaniek, ander toepassingsgebied.

**Aanvullende varianten**:
- *Right of First Offer (ROFO)*: verkoper moet eerst zijn aandelen aanbieden aan mede-aandeelhouders aan een prijs die HIJ bepaalt; pas indien afgewezen mag hij aan derden verkopen aan minimaal dezelfde prijs.
- *Tag-along*: meerderheidsaandeelhouder die verkoopt, moet ook minderheid laten mee verkopen aan dezelfde prijs.
- *Drag-along*: meerderheidsaandeelhouder die verkoopt kan minderheid VERPLICHTEN mee te verkopen aan dezelfde prijs.

<small>📚 WVV — art. 5:62 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📜 Exit-clausule (uitstapmechanismen)  
_`regel`_

🔗 Contractuele bepalingen die regelen onder welke omstandigheden een aandeelhouder zijn aandelen kan of moet verkopen aan de andere(n). Typische varianten:

**Put-optie (verkooprecht)**: aandeelhouder X heeft recht zijn aandelen te verkopen aan Y aan een vooraf bepaalde prijs of formule, bij triggers zoals: overlijden, arbeidsongeschiktheid, exit, change of control, dispute.

**Call-optie (kooprecht)**: omgekeerd, Y heeft recht aandelen X te kopen.

**Leaver-clausules** (typisch in start-ups voor managers-aandeelhouders):
- *Good leaver*: bij overlijden, ziekte, ontslag zonder fout → aandelen aan 'fair market value'.
- *Bad leaver*: bij ontslag wegens fout, niet-naleving non-compete → aandelen aan boekwaarde (laag) of zelfs 0,01 EUR (extreem geval).

**Russian Roulette / Texas Shoot-out** (bij deadlock 50/50): aandeelhouder A maakt aandeelhouder B een prijsbod voor de helft van de aandelen; B kiest: ofwel verkoopt aan A aan die prijs, ofwel koopt van A aan dezelfde prijs. Beslecht deadlock door af te dwingen dat de bieder een eerlijke prijs voorstelt.

**Earn-out**: prijs gedeeltelijk gekoppeld aan toekomstige prestaties (typisch overdracht onderneming met behoud verkoper als manager).

**Statutaire uittreding BV**: art. 5:154 WVV — kan ook geïmplementeerd worden in SHA voor extra detail.

<small>📚 WVV — art. 5:154 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📜 Board-vertegenwoordiging  
_`regel`_

🔗 Afspraken over hoeveel zetels in het bestuursorgaan elke aandeelhouder of -groep krijgt. Typisch:

- Investeerder met 30% krijgt 1 zetel op 5 (in plaats van 0 die hij anders bij gewone meerderheidsbeslissing zou hebben).
- Familie-aandeelhouders A en B krijgen 2 zetels elk; investeerder C krijgt 1 zetel + observerrol.
- Onafhankelijk bestuurder benoemd door beide partijen samen — vaak voor deadlock-vermijding.

**Beperking**: het bestuur is volgens WVV onafhankelijk — een bestuurder mag zich niet contractueel verplichten om altijd 'volgens instructies van X' te stemmen (schending fiduciaire plicht jegens vennootschap). Wel geldig: aandeelhouders verbinden zich op AV te stemmen voor benoeming X als bestuurder. Eens benoemd moet X autonoom oordelen.

**Sancties bij schending**: ontslag van overeenkomstig benoemde bestuurder door tegenpartij is door AV mogelijk (gewone meerderheid art. 7:73 §4) — SHA kan voorzien in compensatie (schadevergoeding) voor dat ontslag.

<small>📚 WVV — art. 2:51 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📜 Controle-verwerving (stemcoördinatie / syndicaatsovereenkomst)  
_`regel`_

📖 Stemovereenkomst tussen meerdere aandeelhouders om hun stemmen gezamenlijk uit te oefenen, vaak om in concert controle te verwerven of te bewaren. Expliciet erkend door art. 5:34 BV / 7:79-7:80 NV WVV.

**Geldigheidsvoorwaarden** (art. 7:80 §2 WVV):
1. **Beperkt in de tijd** — vaste looptijd, niet 'onbeperkt'. Typisch 5-10 jaar.
2. **Niet in strijd met vennootschapsbelang** — een afspraak om systematisch tégen het belang van de vennootschap te stemmen is nietig.
3. **Verenigbaar met WVV-bepalingen** — bv. niet contractueel afzien van minderheidsvordering (art. 2:60).

**Praktische toepassing**:
- Twee kleine aandeelhouders A (15%) en B (10%) verbinden zich gezamenlijk te stemmen — combineren 25% en kunnen daardoor statutenwijziging (75%-drempel) blokkeren.
- Familievennootschap waar 3 broers/zussen elk 20% hebben + niet-familie investeerder 40%: 3 familie-leden tekenen syndicaatsovereenkomst om in concert te stemmen → 60% controle als blok.

**Cassatie + rechtspraak**: niet-naleving = schadevergoeding (art. 1142 oud BW); reële uitvoering (= het feit dwingen dat de afvallige aandeelhouder alsnog volgens afspraak stemt) is in beginsel niet mogelijk maar uitzonderlijk wel via kort geding-bevel voor toekomstige stemmingen.

<small>📚 WVV — art. 5:34 — _wettekst_ · WVV — art. 7:80 — _wettekst_ · BW — art. 1142 — _wettekst_</small>

### 🧭 Dubbele verankering — statuten + SHA  
_`vuistregel`_

🔗 Beste praktijk voor kritieke clausules (lock-up, voorkooprecht, drag-along, tag-along): verankeren in zowel de statuten als in een SHA tussen aandeelhouders.

**Voordeel statutair**:
- Erga omnes binding — geldt voor elke aandeelhouder, ook nieuwe verkrijgers.
- Inschrijving in KBO = openbaarheid.
- Bij overdracht in strijd met statutaire clausule: nietigheid mogelijk.

**Voordeel SHA**:
- Detailniveau (formules, drempels, sancties).
- Privacy — niet in KBO.
- Specifieke boetes en uitvoering-clausules.

**Combinatie**: statuten verankeren het PRINCIPE ('overdracht onderworpen aan voorkooprecht van bestaande aandeelhouders'); SHA werkt de UITVOERING uit (procedure, termijnen, prijsformule, sancties).

Bij elke nieuwe aandeelhouder: meteen laten meetekenen op SHA (de 'adherence-clausule' — bestaande aandeelhouders maken acceptatie SHA voorwaarde voor verkoopgoedkeuring).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Voorbeelden

### 💡 Start-up SHA — founders + VC-investeerder 🔗

_Start-up BV Techo: founders A en B elk 40% (= 800 aandelen elk); VC-investeerder C 20% (= 400 aandelen) na series A van 500.000 EUR. SHA wordt opgesteld om de relatie te kaderen._

**Belangrijkste SHA-clausules**:

1. **Lock-up**: founders A en B verbinden zich 4 jaar lang hun aandelen niet over te dragen. Uitzonderingen: schenking aan partner/kinderen, overlijden, ontslag (zie leaver).

2. **Vesting-clausule** (specifiek startup): founders 'verdienen' hun aandelen over 4 jaar — 25% na 1 jaar 'cliff', dan maandelijks pro rata. Bij vroegtijdig vertrek (bad leaver) worden niet-gevestigde aandelen aan 0,01 EUR ingekocht door vennootschap.

3. **Voorkooprecht / ROFR**: bij verkoop aan derde, eerst aanbieden aan andere ondertekenaars pro rata.

4. **Tag-along**: indien A of B verkoopt aan derde X meer dan 25% van zijn aandelen, mag VC-investeerder C mee verkopen aan dezelfde prijs pro rata.

5. **Drag-along**: bij verkoop van ≥ 75% van de vennootschap aan een externe overnemer, kunnen de meerderheidsaandeelhouders de minderheid VERPLICHTEN mee te verkopen aan dezelfde prijs (vermijdt minderheid-blokkering bij exit).

6. **Board-vertegenwoordiging**: raad van bestuur 5 leden — A en B elk 2 zetels, VC-investeerder 1 zetel + observerrol bij audit-vragen.

7. **Anti-dilution**: VC-investeerder krijgt bij latere kapitaalverhoging tegen LAGERE prijs dan zijn instap (= 'down round'), compenserende uitgifte gratis aandelen ('full ratchet' of 'weighted average').

8. **Preferred dividend**: VC krijgt eerst zijn 5% rendement op de inbreng (500.000 × 5% = 25.000 EUR/jaar) vooraleer A en B dividenden krijgen.

9. **Looptijd SHA**: 7 jaar of tot exit (IPO of verkoop > 80%).

10. **Sancties**: bij schending — boete 25% van transactiewaarde + verplichting tot herstel.

**Dubbele verankering**: clausules 3, 4, 5 ook in statuten opgenomen voor tegenwerpelijkheid; gedetailleerde uitvoering blijft in SHA.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 💡 Familievennootschap — stand-stillclausule bij overdracht 🔗

_BV Familieholding: ouder V draagt 60% van zijn 600 aandelen over aan zijn 3 kinderen K1, K2, K3 (200 aandelen elk). V wil vermijden dat één kind binnen 5 jaar zijn aandelen aan een buitenstaander verkoopt._

**Stand-stillclausule SHA**:

```
Art. 4 — Stand-still
4.1 K1, K2 en K3 verbinden zich gedurende een periode van 5 jaar vanaf de datum van overdracht (1 juli 2026 tot 30 juni 2031) hun aandelen NIET over te dragen aan personen buiten de familie [V, K1, K2, K3 en hun eerste-graads-afstammelingen].
4.2 Uitzonderingen toegelaten zonder voorafgaande toestemming: schenking aan partner/kinderen, overlijden, gedwongen overdracht door schuldeisers met voorafgaande aankondiging.
4.3 Bij schending: forfaitaire boete 50% van transactiewaarde + verplichting tot terugkoop door overige familieleden aan dezelfde prijs.
```

**Dubbele verankering statuten**: art. 8 statuten BV Familieholding: 'Overdracht van aandelen aan personen buiten de familie [V, K1, K2, K3, hun afstammelingen] vereist goedkeuring van de andere familie-aandeelhouders. Statutair overdrachtsverbod gedurende 5 jaar vanaf overdrachtsdatum.'

**Effect**: indien K1 toch wil verkopen aan investeerder X binnen die 5 jaar:
- Statutair: overdracht is nietig wegens niet-naleving statutaire goedkeuringsregel.
- Contractueel SHA: K1 betaalt 50% boete + moet aandelen terugbieden aan K2+K3.

**Boekhoudkundige impact**: stand-still heeft geen directe boekhoudkundige impact (geen vermogensoverdracht); wel relevant voor waardebepaling bij latere overdracht (lock-up verlaagt liquiditeit en dus waarde — discount typisch 15-25%).

<small>📚 WVV — art. 5:62 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 💡 Voorkooprecht (ROFR) — concrete uitwerking 🔗

_BV Trio: aandeelhouders A (40%), B (35%), C (25%). SHA bevat voorkooprecht (ROFR): bij verkoop aan derde moeten aandelen eerst worden aangeboden aan andere ondertekenaars pro rata van hun bestaand belang. C wil zijn 250 aandelen verkopen aan derde X voor 1.000 EUR/aandeel = 250.000 EUR._

**Berekening:**
- Stap 1 — C notificeert A en B per aangetekende brief: 'derde X biedt 250.000 EUR voor mijn 250 aandelen — wenst u voorkoop?'
- Stap 2 — termijn voor antwoord: 30 dagen (zoals in SHA bepaald).
- Stap 3 — pro rata-verdeling: A heeft 40%, B heeft 35%. Verhouding A:B = 40:35 = 8:7. Indien beide voorkoop willen → A koopt 8/15 × 250 = 133,3 aandelen, B 7/15 × 250 = 116,7. Door afronding-clausule (typisch SHA): A krijgt 134, B krijgt 116.
- Stap 4a — beide voorkopen: 134 × 1.000 + 116 × 1.000 = 250.000 EUR. C heeft zijn geld; A bezit nu 940 aandelen (40% + 134), B heeft 466 aandelen (35% + 116).
- Stap 4b — alleen A voorkoopt: A koopt 250 aandelen volledig voor 250.000 EUR. A bezit nu 1.050 aandelen (= 60% indien geen herverdeling).
- Stap 4c — niemand voorkoopt: C mag verkopen aan X aan dezelfde of betere voorwaarden binnen termijn (typisch 6 maanden). Aandeel-overdracht in aandeelhoudersregister; X wordt nieuwe aandeelhouder en moet typisch SHA-adherence-clausule tekenen.
- Stap 5 — boekhoudkundig: in BV Trio geen impact (interne overdracht). In A's boekhouding (indien A vennootschap is): rekening 280 'Deelnemingen in verbonden ondernemingen' debet × bedrag voorkoop, 550 'Bank' credit.

→ **Resultaat**: Voorkooprecht beschermt de bestaande aandeelhouders tegen ongewenste nieuwkomers EN tegen overdracht aan partijen waarmee strategisch belangenconflict bestaat. Belangrijk: prijs ligt vast (geboden prijs van X) — geen onderhandeling, voorkomt prijs-spelletjes.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ SHA = statuten

**Verkeerde assumptie**: Een aandeelhoudersovereenkomst werkt automatisch erga omnes en bindt nieuwe verkrijgers van aandelen.

**Kernpunt**: SHA = contract = relativiteit (art. 1165 oud BW / 5.103 nieuw BW). Bindt ALLEEN ondertekenaars. Een nieuwe verkrijger te goeder trouw die niet wist van SHA is niet gebonden. Daarom: (a) bij elke aandeel-overdracht laten nieuwe verkrijger meetekenen op SHA (adherence-clausule); (b) kritieke clausules statutair verankeren voor erga omnes-binding.

<small>📚 BW — art. 5.103 (nieuw) — _wettekst_</small>

### ⚠️ Voorkooprecht SHA = voorkeurrecht WVV

**Verkeerde assumptie**: Het contractuele voorkooprecht in een SHA is hetzelfde concept als het wettelijk voorkeurrecht bij kapitaalverhoging.

**Kernpunt**: Verschillende concepten:
- **Wettelijk voorkeurrecht** (art. 5:128 / 7:188 WVV): bij UITGIFTE van nieuwe aandelen (kapitaalverhoging in geld). Beschermt tegen verwatering. Niet contractueel weg te bedingen — wettelijk dwingend.
- **Contractueel voorkooprecht / ROFR** (in SHA): bij VERKOOP van bestaande aandelen aan derde. Beschermt tegen ongewenste nieuwe aandeelhouders.

Beide kunnen tegelijk gelden voor dezelfde aandeelhouder maar grijpen op andere momenten in.

<small>📚 WVV — art. 5:128 — _wettekst_ · WVV — art. 7:188 — _wettekst_</small>

### ⚠️ Stemovereenkomst altijd geldig

**Verkeerde assumptie**: Aandeelhouders mogen om het even welke afspraken maken over hun stemgedrag.

**Kernpunt**: Art. 7:80 §2 WVV: stemovereenkomsten zijn nietig indien (a) onbeperkt in tijd, (b) in strijd met vennootschapsbelang, of (c) bestuurders worden contractueel verplicht hun stem in bepaalde zin uit te brengen ('bestuurders mogen niet meegebonden zijn aan stemafspraken van aandeelhouders, dit ondermijnt hun fiduciaire plicht).

Geldige stemovereenkomsten = beperkt in tijd + voor specifieke materies + niet in strijd met vennootschapsbelang.

<small>📚 WVV — art. 7:80 §2 — _wettekst_</small>

## Accountant-perspectieven

### Cliënt-aandeelhouder bij SHA-opstelling

_De accountant adviseert bij opzet en uitvoering van een SHA — vaak in samenwerking met advocaat-vennootschapsrecht._

#### 🧭 Adviseur

##### 👣 SHA-checklist voor cliënt  
_`stap`_

🔗 Bij opzet van een SHA voor cliënt-aandeelhouder doorlopen:

1. **Doel** — control, exit, dividend-beleid, board-vertegenwoordiging? Per doel: passende clausule.
2. **Looptijd** — bepaald (5-10 jaar typisch) + verlengmechanisme.
3. **Triggers** — wanneer grijpt elke clausule in (verkoop, ontslag, overlijden, change of control)?
4. **Prijsformules** — voor exit-clausules: fair market value, vermogenswaarde, EBITDA-multiple, ...?
5. **Sancties** — boeteclausules, terugkoop-verplichting, dwangsom.
6. **Statutair verankeren** welke clausules (kritieke).
7. **Adherence-clausule** voor nieuwe aandeelhouders.
8. **Geschillenbeslechting** — arbitrage, bevoegde rechtbank.
9. **Fiscaal advies** — sommige SHA-clausules (preferred dividend, anti-dilution) kunnen fiscale impact hebben (controle-vraag bij DBI-vrijstelling, art. 90 9° meerwaarde-belasting).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

##### 🧭 Impact SHA-clausules op aandelen-waardering  
_`vuistregel`_

🔗 SHA-clausules beïnvloeden de waarde van aandelen — relevant voor bedrijfswaardering, fiscale aangifte (schenking, successie), 'fair market value'-bepaling:

- Lock-up + voorkoopclausules → discount voor illiquiditeit (typisch 15-25%).
- Drag-along → kan minderheidsdiscount verkleinen (mogelijkheid mee in exit).
- Tag-along → beschermt minderheidsdiscount.
- Preferred dividend → verlaagt waarde van gewone aandelen, verhoogt waarde preferente.
- Anti-dilution → beschermt waarde investeerder ten koste van overige.

Bij waardebepaling expliciet rapporteren welke SHA-clausules in aanmerking zijn genomen en hoe ze de waarde beïnvloeden.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Aandeel als onderliggend object → [[aandeel]] _(moet-verwijzen)_
- → Algemene vergadering — formeel orgaan → [[algemene-vergadering]] _(moet-verwijzen)_
- → Overdracht onderneming — share-deal-context → [[overdracht-onderneming]] _(moet-verwijzen)_
- → Vennootschapsgeschillen — afdwingbaarheid + sancties bij schending → [[vennootschapsgeschillen]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[aandeel]]
### `beinvloed_door`
- [[algemene-vergadering]] — Stemcoördinatie via SHA werkt door op stemgedrag in AV.
### `uitgevoerd_door`
- [[gecertificeerd-accountant]] — GA adviseert bij opzet (samen met advocaat) en waardering-impact op aandelen.
