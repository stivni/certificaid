---
title: "Invorderingsprocedure"
concept_type: "procedure"
schema_version: "2.2"
status: "concept"
categorieen:
  - gebeurtenis
ankers:
  - 2.5.VII
tags:
  - concept
  - schema-2.2
  - type-procedure
  - cat-gebeurtenis
  - status-concept
gegenereerd_uit: "data/concepten/records/invorderingsprocedure.json"
---

# Invorderingsprocedure

_Procedure_

📅 Gebeurtenis · Anchors: `2.5.VII` · Wave: `skeleton-fiscaliteit-klein-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: fiscale invordering · gedwongen invordering — **Vertalingen**: fr: procédure de recouvrement

## Definitie

📖 De invorderingsprocedure is het geheel van wettelijke stappen waarmee de ontvanger van de fiscus de inning van een onbetaalde belastingschuld afdwingt. Sinds 2019 gegroepeerd in het Wetboek van de minnelijke en gedwongen invordering van fiscale en niet-fiscale schuldvorderingen (Wb.Inv.). De cascade: (1) minnelijke invordering (betalingsherinnering); (2) dwangbevel uitgevaardigd door de bevoegde ambtenaar; (3) bewarend en uitvoerend beslag; (4) gerechtelijke uitwinning (openbare verkoop, ...).

<small>📚 Wetboek minnelijke en gedwongen invordering — art. 15 + Titel 3 — _wettekst_</small>

## Substantie

🔗 De accountant moet het verschil kennen tussen vestigings-procedure (taxatie/bezwaar — de belastingschuld vastleggen) en invordering-procedure (de schuld innen). Een lopend bezwaar schorst NIET automatisch de invordering: het onbetwist gedeelte blijft onmiddellijk eisbaar; voor het betwiste deel kan de ontvanger bewarend beslag leggen (art. 410 WIB92). Praktijk: bij grote betwiste aanslagen adviseert men cliënten te betalen onder voorbehoud, zodat er geen beslag-actie tegen hen loopt tijdens de procedure.

<small>📚 WIB92 — art. 409-410 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 De ratio is dubbel: enerzijds zorgen dat de overheid haar inkomsten effectief int (zonder kasstroom geen functionerende staat), anderzijds waarborgen bieden aan de belastingplichtige (bezwaar moet zinvol blijven). De compromis-formule: 'onbetwist verschuldigd gedeelte' blijft eisbaar; voor het betwiste deel mag bewarend beslag, niet uitvoerend. De voorrechten van de schatkist (algemeen voorrecht op roerend, hypothecair voorrecht op onroerend) waarborgen dat de fiscus voorrang heeft bij samenloop van schuldeisers.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: Wetboek minnelijke en gedwongen invordering (in werking 1 januari 2020) + WIB92 art. 409-410

Het Wb.Inv. vervangt de oude regels uit het WIB92 en de wet van 1994. Centralisatie van invorderingsregels voor PB, VenB, BTW, douane, accijnzen + niet-fiscale schulden.

**▶️ Trigger start**
- 📖 Niet-betaling van de aanslag binnen de wettelijke termijn (2 maanden vanaf verzending aanslagbiljet) start de invorderingsprocedure.

## Sub-concepten

### 📦 Verzet tegen dwangbevel  
_`procedure` (subconcept)_

#### Definitie

📖 Verzet is de jurisdictionele tegenactie waarmee de belastingplichtige het uitgevaardigde dwangbevel betwist. Het is — in tegenstelling tot een louter administratief bezwaar — een rechterlijke procedure die ingeleid wordt via dagvaarding van de ontvanger bij de fiscale kamer van de rechtbank van eerste aanleg. Verzet stuit de verjaring van de fiscale schuld en is de enige weg om de invorderingstitel zelf aan te vechten. Per heffingsregime gelden eigen termijnen en bevoegdheidsregels: WIB92/Wb.Inv. voor inkomstenbelasting, WBTW art. 89 voor btw, W.Reg art. 221 voor registratierechten.

<small>📚 Wetboek minnelijke en gedwongen invordering — Titel 3 — _wettekst_ · W.Reg — art. 221 — _wettekst_ · WBTW — art. 89 — _wettekst_</small>

#### Substantie

🔗 Procedurele val voor de accountant: louter administratief bezwaar bij de gewestelijke directeur (federale PB) of bij de bevoegde administratie schorst de invordering NIET en stuit de verjaring evenmin. Verzet is jurisdictioneel: dagvaarding bij de rechtbank van eerste aanleg, fiscale kamer, met de ontvanger als verweerder. Het verzet schorst de invordering niet van rechtswege — de rechter kan op verzoek opschorten — maar bewarend beslag blijft mogelijk hangende de procedure. Voor btw geldt een strikte termijn van 1 maand vanaf betekening van het dwangbevel (art. 89 WBTW); voor registratierechten gelden gemeenrechtelijke termijnen (art. 221 W.Reg).

<small>📚 WBTW — art. 89 — _wettekst_ · W.Reg — art. 221 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-29)</small>

#### Rationale

🔗 De ratio is procedurele waarborg: het dwangbevel is een eenzijdige administratieve titel met uitvoeringskracht (art. 13 Wb.Inv.) — verzet biedt de belastingplichtige een rechterlijke toetsing van die titel. Omdat een louter administratief bezwaar geen impact heeft op de uitvoerbaarheid van het dwangbevel, is verzet het enige instrument dat zowel de verjaring stuit als de invorderingstitel ten gronde betwist. De compromis-formule: verzet stuit de verjaring (waarborg voor belastingplichtige), maar schorst de invordering niet van rechtswege (waarborg voor de schatkist).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-29)</small>

#### 📜 Termijnen verzet per heffingsregime  
_`regel`_

❓ WBTW art. 89: 1 maand vanaf betekening van het dwangbevel — strikt, niet verlengbaar. W.Reg art. 221: dagvaarding voor de rechtbank van eerste aanleg, fiscale kamer, binnen de gemeenrechtelijke termijn — best zo snel mogelijk om bewarend beslag te vermijden. WIB92/Wb.Inv.: verzet via dagvaarding tegen de ontvanger, conform Wb.Inv. + Gerechtelijk Wetboek. Vormvereiste: dagvaarding (geen aangetekende brief volstaat).

<small>📚 WBTW — art. 89 — _wettekst_ · W.Reg — art. 221 — _wettekst_ · Wetboek minnelijke en gedwongen invordering — Titel 3 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-29)</small>

#### ⚙️ Effect op invordering en verjaring  
_`mechanisme`_

🔗 Verzet stuit de verjaring van de fiscale schuld — een nieuwe termijn begint te lopen na het in kracht van gewijsde gaan van de eindbeslissing. Verzet schorst echter NIET automatisch de uitvoering van het dwangbevel: bewarend beslag blijft mogelijk (loon, bankrekening, hypothecaire inschrijving). De rechter kan op gemotiveerd verzoek opschorting bevelen, doorgaans op voorwaarde van een waarborg of betaling onder voorbehoud van het onbetwist gedeelte.

<small>📚 Wetboek minnelijke en gedwongen invordering — art. 23-24 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-29)</small>

#### ⚠️ Valkuil: bezwaar versus verzet  
_`risico`_

🔗 Een louter administratief bezwaar (federale PB: gewestelijke directeur; btw: bezwaarschrift bij administratie; registratie: bezwaar bij Vlabel/SPW/Brussel Fiscaliteit) is GEEN verzet en stuit de verjaring van het dwangbevel niet. Wie enkel bezwaar indient en verder geen verzet aantekent, riskeert dat de invorderingstitel definitief wordt ondanks de lopende administratieve betwisting. Vuistregel voor de accountant: bij ontvangst van een dwangbevel ALTIJD parallel verzet overwegen — niet enkel administratief bezwaar.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-29)</small>

## Bouwstenen

### 👣 Stap 1 — Minnelijke invordering  
_`stap`_

🔗 Betalingsherinnering(en) door de ontvanger. Vaak ook telefonisch contact. Mogelijkheid om een afbetalingsplan af te spreken (typisch tot 24 maanden voor PB; soms langer met bijkomende waarborgen). Geen kosten — informele fase.

<small>📚 Wetboek minnelijke en gedwongen invordering — Titel 2 — minnelijke invordering — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 👣 Stap 2 — Dwangbevel  
_`stap`_

📖 Indien minnelijke fase mislukt: de ontvanger vaardigt een dwangbevel uit (geviseerd en uitvoerbaar verklaard). Het dwangbevel wordt betekend door een gerechtsdeurwaardersexploot of bij aangetekende brief. Het is een uitvoerbare titel — dezelfde kracht als een vonnis voor de inning.

<small>📚 Wetboek minnelijke en gedwongen invordering — art. 13 + Titel 3 — _wettekst_</small>

### 👣 Stap 3 — Beslag  
_`stap`_

📖 Op grond van het dwangbevel kan de ontvanger beslag leggen: bewarend (om het vermogen 'vast te houden') of uitvoerend (om het te verkopen). Soorten: roerend beslag (kantoor- of huisinhoud), beslag onder derden (loon, bankrekening), beslag op onroerend goed met hypothecaire inschrijving. Beslag op loon respecteert de beslagvrije voet.

<small>📚 Wetboek minnelijke en gedwongen invordering — Titel 3 — gedwongen invordering — _wettekst_</small>

### 👣 Stap 4 — Uitwinning  
_`stap`_

📖 Slotfase: openbare verkoop van in beslag genomen goederen, inning van loonbeslag, opzeg van bankgaranties. De opbrengst wordt aangewend op de schuld in volgorde: kosten · nalatigheidsinteresten · boetes · belasting (art. 57 Brusselse Codex; analoog federaal).

<small>📚 Brusselse Codex Fiscale Procedure — art. 57 — _wettekst_</small>

### 📜 Voorrechten van de schatkist  
_`regel`_

📖 De fiscus heeft een algemeen voorrecht op alle roerende goederen van de belastingplichtige en een hypothecair voorrecht op onroerende goederen voor de inkomstenbelasting (art. 422-425 WIB92). Dit geeft de fiscus voorrang bij samenloop met andere schuldeisers (bv. bij faillissement) — beperkt door wettelijke rangorde (loon van werknemers, sociale zekerheid, fiscus, ...).

<small>📚 WIB92 — art. 422-425 — _wettekst_</small>

### ↪️ Hoofdelijkheid bestuurders (art. 442bis)  
_`uitzondering`_

📖 Bestuurders en feitelijke leidinggevenden van een vennootschap kunnen hoofdelijk aansprakelijk gesteld worden voor onbetaalde bedrijfsvoorheffing en BTW wanneer de niet-betaling toe te schrijven is aan een fout van de bestuurder (kennelijk grove fout). Dit doorbreekt het schermend karakter van de rechtspersoon. Voorzichtig: groot risico bij vennootschappen in moeilijkheden.

<small>📚 WIB92 — art. 442bis — _wettekst_</small>

### 📜 Schorsing van invordering bij bezwaar  
_`regel`_

📖 Bezwaar schorst de invordering NIET automatisch. Onbetwist verschuldigd gedeelte blijft onmiddellijk opeisbaar (art. 409 WIB92). Voor het betwiste deel: bewarend beslag is toegelaten, uitvoerend beslag in beginsel niet (art. 410 WIB92). De ontvanger kan een uitzondering bekomen via gerechtelijke procedure.

<small>📚 WIB92 — art. 409-410 — _wettekst_</small>

## Valkuilen

### ⚠️ Bezwaar = geen vrijbrief om niet te betalen

**Verkeerde assumptie**: Tijdens een lopend bezwaar mag de cliënt rustig wachten met betalen.

**Kernpunt**: Onbetwist deel blijft eisbaar. Betwist deel kan bewarend beslag opleveren — wat zelfs zonder verkoop al schadelijk is voor de bedrijfsvoering (geblokkeerde rekeningen, hypotheek-inschrijvingen op kavels). Advies: bij grote bedragen betalen onder voorbehoud.

<small>📚 WIB92 — art. 409-410 — _wettekst_</small>

### ⚠️ Hoofdelijkheid bestuurder = niet zomaar te ontwijken via rechtspersoon

**Verkeerde assumptie**: Als de vennootschap failliet gaat, is de bestuurder veilig voor de fiscale schulden.

**Kernpunt**: Art. 442bis (PB/BV) doorbreekt het rechtspersoonschild bij bedrijfsvoorheffing en BTW wanneer de niet-betaling te wijten is aan een fout. Bestuurder wordt persoonlijk en hoofdelijk aangesproken. Vooral relevant in zware financiële stress.

<small>📚 WIB92 — art. 442bis — _wettekst_</small>

### ⚠️ Verjaring kan worden gestuit

**Verkeerde assumptie**: Na 5 jaar zonder actie is de fiscale schuld verjaard, ook al heeft de fiscus reeds dwangbevel uitgevaardigd.

**Kernpunt**: Verjaring is 5 jaar (art. 23 Wb.Inv.) MAAR wordt gestuit door elke vervolgingshandeling (dwangbevel, beslag, kennisgeving). Na elke stuiting begint de termijn opnieuw. In de praktijk verjaart een actief opgevolgd dossier nooit.

<small>📚 Wetboek minnelijke en gedwongen invordering — art. 23-24 — _wettekst_</small>

## Verder lezen (scope-out)

- → Aanslag-cyclus als grondslag (inkohiering) → [[aanslag-cyclus]] _(moet-verwijzen)_
- ↪ Sancties bij niet-betaling → [[fiscale-sancties]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[fiscale-procedure]]
