---
title: "Faillissement"
concept_type: "procedure"
schema_version: "2.2"
status: "concept"
categorieen:
  - gebeurtenis
  - regeling
ankers:
  - 3.0.X
  - 3.0.X.E
  - 3.0.X.F
tags:
  - concept
  - schema-2.2
  - type-procedure
  - cat-gebeurtenis
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/faillissement.json"
---

# Faillissement

_Procedure_

📅 Gebeurtenis · 📋 Regeling · Anchors: `3.0.X` · `3.0.X.E` · `3.0.X.F` · Wave: `skeleton-vennootschapsrecht-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: faillite · bankruptcy

## Definitie

📖 Het faillissement is de gerechtelijke procedure waarbij het volledige vermogen van een onderneming die duurzaam haar schulden niet meer kan betalen, onder het beheer van een curator wordt geplaatst. De curator realiseert de activa en verdeelt de opbrengst onder de schuldeisers volgens een wettelijke rangorde. Het is de eindprocedure binnen boek XX van het Wetboek van Economisch Recht (WER) — wat overblijft wanneer reorganisatie geen redelijk vooruitzicht meer biedt. Voor rechtspersonen leidt het faillissement tot ontbinding; voor natuurlijke personen kan het uitmonden in kwijtschelding van restschulden.

<small>📚 WER — art. XX.98 — _wettekst_ · WER — art. XX.99 § 1 — _wettekst_</small>

## Substantie

🔗 Economisch is faillissement het einde van de onderneming als going concern: de boedel (vermogen op datum vonnis) wordt 'bevroren', alle uitvoeringsmaatregelen van individuele schuldeisers worden opgeschort en vervangen door één collectieve afwikkeling. Voor de accountant valt zijn rol grotendeels weg vanaf het vonnis — de curator neemt het beheer over. Wat blijft: bijstand aan de gefailleerde-natuurlijke-persoon voor kwijtschelding restschulden, aangifte schuldvordering bij eigen openstaande facturen, en de stortvloed aan documenten die de curator opvraagt (boekhouding laatste 3 jaar, klantenlijsten, bankuittreksels).

<small>📚 WER — art. XX.110 (boedel-omvang) — _wettekst_ · WER — art. XX.156 (aangifte schuldvordering) — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 Het faillissement bestaat om twee redenen: (1) collectief schuldeisersbelang — zonder gemeenschappelijke procedure leidt 'eerst komt, eerst maalt' tot ongelijke behandeling en kapot-procederen van de schuldenaar; (2) marktintegriteit — een insolvabele onderneming uit de markt halen voorkomt dat ze nieuwe schuldeisers besmet. De 'tweede-kans'-gedachte (verschoonbaarheid voor natuurlijke personen sinds 2017) erkent dat sociale dood van de ondernemer een sub-optimaal maatschappelijk resultaat is.

<small>📚 WER — art. XX.173 (kwijtschelding restschulden) — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · sinds **2018-05-01** · basis: WER boek XX, titel VI (W 11-08-2017, hervormd W 7-06-2023)

**📋 Voorwaarden**
- 📖 Cumulatief: (1) **duurzame staking van betaling** — de schuldenaar betaalt structureel niet meer (geen incidentele kasspanning); (2) **geschokt krediet** — leveranciers en bankiers willen niet meer leveren of lenen zonder cash. Eén van beide volstaat niet. Beide voorwaarden worden door de rechter feitelijk getoetst.

**▶️ Trigger start**
- 📖 Drie initiatieven kunnen het faillissement uitlokken: (a) **bekentenis** door de schuldenaar zelf (art. XX.102 — verplicht binnen 1 maand na duurzame staking); (b) **dagvaarding** door een schuldeiser of door het openbaar ministerie; (c) **ambtshalve** door de rechtbank na onderzoek door de kamer voor ondernemingen in moeilijkheden.

**⚠️ Risico**
- 📖 Voor bestuurders: laattijdige aangifte (>1 maand na staking betaling) of voortzetten reddeloos verliesgevende activiteit kan leiden tot persoonlijke aansprakelijkheid voor het netto-passief van het faillissement (art. XX.225 — 'wrongful trading').

## Sub-concepten

### 📦 Twee cumulatieve toepassingsvoorwaarden  
_`kader` (subconcept)_

#### Definitie

📖 **Duurzame staking van betaling**: de schuldenaar is niet meer in staat om zijn opeisbare schulden structureel te voldoen. 'Duurzaam' onderscheidt dit van een tijdelijke kasspanning. Indicatoren: aanhoudende achterstanden RSZ/btw, protest van wisselbrieven, onbetaalde lonen, niet-gehonoreerde betalingsovereenkomsten. **Geschokt krediet**: het vertrouwen van de buitenwereld is verdwenen — banken willen niet meer lenen, leveranciers eisen contante betaling, kredietverzekeraars schrappen dekking. De rechtbank toetst beide feitelijk, niet op basis van een mathematische formule.

<small>📚 WER — art. XX.99 § 1 — _wettekst_</small>

#### Rationale

🔗 Het dubbele criterium voorkomt voortijdige faillietverklaring bij tijdelijke liquiditeitskrapte (vereiste 'duurzaam') én bij een onderneming die op papier solvabel lijkt maar de facto niet meer functioneert (vereiste 'geschokt krediet').

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 Procedure: aangifte → vonnis → publicatie  
_`procedure` (subconcept)_

#### Definitie

📖 **Stap 1 — Aangifte/dagvaarding**: schuldenaar dient aangifte in via Regsol, of een schuldeiser dagvaardt. Bijgevoegd: balans + resultatenrekening, lijst schuldeisers, personeelslijst. **Stap 2 — Faillietvonnis**: ondernemingsrechtbank spreekt faillissement uit, stelt curator(en) en rechter-commissaris aan, bepaalt termijn voor aangifte schuldvorderingen (meestal 30 dagen). **Stap 3 — Publicatie**: het vonnis wordt bekendgemaakt in het Belgisch Staatsblad en in Regsol. Het is uitvoerbaar bij voorraad (art. XX.108) — beroep schorst de uitvoering niet.

<small>📚 WER — art. XX.99 e.v. (vonnis) — _wettekst_ · WER — art. XX.108 — _wettekst_</small>

### 📦 Curator — beheer en vereffening boedel  
_`actor` (subconcept)_

#### Definitie

📖 De curator (vaak een advocaat, soms een gecertificeerd accountant of bedrijfsrevisor) wordt door de rechtbank aangesteld en neemt onmiddellijk na het vonnis het beheer van de gefailleerde over (art. XX.132). Drie kerntaken: (1) **inventariseren** van het vermogen (art. XX.134); (2) **realiseren** van de activa (verkoop voorraad, vorderingen innen, eventueel verderzetting activiteit met machtiging rechter-commissaris); (3) **verifiëren** van de aangegeven schuldvorderingen en **uitkeren** volgens rangorde. De curator legt periodiek rekening en verantwoording af aan de rechter-commissaris.

<small>📚 WER — art. XX.98 — _wettekst_ · WER — art. XX.132 — _wettekst_ · WER — art. XX.134 — _wettekst_ · WER — art. XX.140 (verderzetting met machtiging) — _wettekst_</small>

### 📦 Rangorde schuldeisers bij verdeling  
_`kader` (subconcept)_

#### Definitie

🔗 De opbrengst van de boedel wordt verdeeld volgens een wettelijke rangorde: (1) **boedelschulden** — kosten faillissement zelf (erelonen curator, lopende huur, lonen na faillietvonnis); (2) **bijzondere voorrechten** op specifieke goederen (pand, hypotheek, retentierecht); (3) **algemene voorrechten** (RSZ, btw, lonen vóór faillissement binnen wettelijke grenzen); (4) **gewone schuldeisers** (proportionele uitkering 'pari passu'); (5) **achtergestelde schuldeisers** (vaak aandeelhouders-leningen) — bijna altijd nul. Aandeelhouders staan na alle schuldeisers en krijgen meestal niets terug.

<small>📚 WER — art. XX.145 (uitkering door curator) — _wettekst_ · Hypotheekwet — art. 17-19 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 Termijnen en sluiting  
_`kader` (subconcept)_

#### Definitie

📖 **Aangifte schuldvorderingen**: schuldeisers dienen binnen de termijn van het vonnis (meestal 30 dagen, soms langer) hun vordering elektronisch in via Regsol (art. XX.155-156). Laattijdige aangifte blijft mogelijk tot de afsluiting, maar verliest het recht op reeds gedane uitkeringen. **Sluiting van het faillissement**: gebeurt door vonnis bij ofwel (a) **ontoereikend actief** (snelle sluiting zonder uitkering — vaak binnen 6-12 maanden), ofwel (b) **vereffening** na verdeling van de opbrengst. De sluiting beëindigt het mandaat van de curator en, voor een rechtspersoon, ontbindt en sluit ze ineens de vereffening.

<small>📚 WER — art. XX.155-156 — _wettekst_ · WER — art. XX.134 §2-5 — _wettekst_</small>

### 📦 Kwijtschelding restschulden (natuurlijke persoon)  
_`regime` (subconcept)_

#### Definitie

📖 Wanneer de gefailleerde een natuurlijke persoon is, kan hij bij de rechtbank de kwijtschelding van restschulden vragen (art. XX.173). De rechter wijst dit toe behoudens manifeste fraude of zware fout. Effect: schulden die na liquidatie van de boedel openblijven, worden onafdwingbaar. Dit geldt enkel voor de gefailleerde-natuurlijke-persoon zelf — niet voor borgen of mede-debiteuren, behalve voor de kosteloze persoonlijke zekerheidsteller (echtgenoot, ouder die borg stond).

<small>📚 WER — art. XX.173 § 1 — _wettekst_</small>

#### Rationale

🔗 Het 'tweede-kans'-principe: een ondernemer die te goeder trouw failliet ging mag herbeginnen zonder een levenslange schuldenlast. Voor rechtspersonen geldt dit niet — die houden bij sluiting gewoon op te bestaan.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 Faillissementsaansprakelijkheid van bestuurders  
_`regime` (subconcept)_

#### Definitie

📖 Twee aansprakelijkheidsgrondslagen bij faillissement van een rechtspersoon: (1) **art. XX.225 — wrongful trading**: bestuurders die wisten of moesten weten dat er geen redelijk vooruitzicht was om de continuïteit van de onderneming te behouden of een faillissement te vermijden, en die toch de verliesgevende activiteit voortzetten, kunnen aansprakelijk worden gesteld voor het netto-passief; (2) **art. XX.226 — kennelijk grove fout** die heeft bijgedragen tot het faillissement (bv. boekhouding niet gevoerd, fictieve facturen, gebruik vennootschap voor persoonlijke doeleinden). De curator (of een schuldeiser bij stilzittende curator) stelt de vordering in.

<small>📚 WER — art. XX.225 — _wettekst_ · WER — art. XX.226 — _wettekst_</small>

#### Substantie

🔗 Praktisch: de bestuurder die zijn jaarrekening laat publiceren met een waarschuwing 'continuïteit onzeker' en niet handelt, of die nog leveranciers laat leveren wetende dat hij niet kan betalen, riskeert zijn privé-vermogen. De accountant die bestuurders bijstaat moet hierop wijzen — laattijdige aangifte van faillissement is bijna altijd een verkeerde keuze voor de bestuurder.

<small>📚 WER — art. XX.226 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Bouwstenen

### 📏 Aangifteplicht binnen 1 maand  
_`drempel`_

📖 De schuldenaar die voldoet aan de voorwaarden van faillissement (duurzame staking + geschokt krediet) moet binnen één maand na het ontstaan ervan aangifte doen bij de ondernemingsrechtbank (art. XX.102). Niet-aangifte na deze termijn is op zichzelf al een mogelijk grond voor bestuurdersaansprakelijkheid.

<small>📚 WER — art. XX.102 — _wettekst_</small>

### 📜 Boedel = volledig vermogen op datum vonnis  
_`regel`_

📖 De boedel omvat alle goederen die toebehoren aan de gefailleerde op de datum van het faillietvonnis, inclusief vorderingen, onroerende goederen, immateriële activa en goederen verworven tijdens de procedure. Uitzondering: persoonlijke goederen 'voor eigen gebruik' en levensonderhoud voor de gefailleerde-natuurlijke-persoon en zijn gezin.

<small>📚 WER — art. XX.110 § 3 — _wettekst_ · WER — art. XX.2, 5° — _wettekst_</small>

### ↪️ Terugvordering niet-geleverde koopwaren  
_`uitzondering`_

📖 Verkochte koopwaren die nog niet aan de gefailleerde (of voor zijn rekening aan een derde) zijn geleverd of verzonden, kunnen door de verkoper worden teruggevorderd (art. XX.199). Dit is een uitzondering op het beginsel dat alle goederen tot de boedel behoren.

<small>📚 WER — art. XX.199 — _wettekst_</small>

### 📜 Faillissement op zich geen grond voor opzeg arbeidsovereenkomsten  
_`regel`_

📖 Het faillissement van een natuurlijke persoon of rechtspersoon kan op zich alleen geen grond zijn voor automatische beëindiging van arbeidsovereenkomsten (art. XX.191). De curator beslist over voortzetting of opzeg, met respect voor arbeidsrechtelijke beschermingsregels.

<small>📚 WER — art. XX.191 — _wettekst_</small>

## Voorbeelden

### 💡 Tijdslijn van een faillissement — Zelena Bio NV 🔗

_Zelena Bio NV staakt structureel haar betalingen sinds januari. De bank trekt het kaskrediet in op 15 februari. De zaakvoerder doet bekentenis op 1 maart._

**Weergave** `tijdslijn`:

```json
{
  "tekst": "Dag 0 (1 maart): Bekentenis via Regsol\nDag 3: Vonnis faillietverklaring — curator en rechter-commissaris aangesteld\nDag 3 + 1: Curator neemt boekhouding, sleutels, IT-toegang over\nDag 3 — Dag 30: Inventarisatie + aangifte schuldvorderingen door schuldeisers (termijn = 30 dagen)\nDag 30 — Maand 6: Realisatie activa (verkoop voorraad, inning vorderingen)\nMaand 6 — Maand 12: Verificatievonnis + verdeling opbrengst volgens rangorde\nMaand 12+: Sluitingsvonnis → ontbinding NV"
}
```

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Faillissement = einde van de accountant-rol

**Verkeerde assumptie**: Zodra het faillissement wordt uitgesproken, kan de accountant zijn dossier sluiten.

**Kernpunt**: De curator vraagt bijna altijd de volledige boekhouding van de laatste 3 jaar op + klantenlijsten + bankuittreksels. De accountant moet meewerken (beroepsplicht) en, als kosteloos zekerheidsteller of medebestuurder, eigen aansprakelijkheidsrisico's bewaken.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Beroep tegen faillietvonnis schorst niets

**Verkeerde assumptie**: Een hoger beroep tegen het faillietvonnis houdt de procedure tegen.

**Kernpunt**: Het vonnis is uitvoerbaar bij voorraad (art. XX.108): de curator neemt onmiddellijk het beheer over, zelfs als beroep is aangetekend. Pas bij vernietiging in beroep wordt de situatie achteraf rechtgezet — wat in de praktijk zelden gebeurt.

<small>📚 WER — art. XX.108 — _wettekst_</small>

### ⚠️ Verschoonbaarheid geldt voor de vennootschap

**Verkeerde assumptie**: Een failliete BV kan om kwijtschelding van restschulden vragen.

**Kernpunt**: Kwijtschelding (art. XX.173) geldt enkel voor natuurlijke personen. Een rechtspersoon houdt bij sluiting op te bestaan en de restschulden gaan mee verdwijnen — maar dat is geen kwijtschelding, dat is ontbinding. Wie persoonlijke borgen heeft gesteld (zaakvoerder, echtgenoot) blijft daarvoor instaan, tenzij die borg een 'kosteloze persoonlijke zekerheid' was.

<small>📚 WER — art. XX.173 § 1 — _wettekst_</small>

## Accountant-perspectieven

### Accountant bij faillissement van eigen cliënt

#### 📒 Boekhouder

##### 👣 Dossier overdragen aan curator  
_`stap`_

🔗 Binnen de eerste week na het vonnis: lever de volledige boekhouding van de laatste 7 jaar, de personeelslijst, de openstaande klanten- en leveranciersbalans en de bankuittreksels. De curator heeft toegang tot Regsol nodig — vraag de cliënt om elektronische toegangscodes mee te delen. Bewaar zelf kopieën — vooral van eigen advies-correspondentie.

<small>📚 WER — art. XX.152 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 🧭 Adviseur

##### 👣 Natuurlijke persoon: kwijtschelding restschulden vragen  
_`stap`_

📖 Als de gefailleerde een eenmanszaak of vrije beroeper is: dien binnen 3 maanden na faillietvonnis een verzoek tot kwijtschelding van restschulden in via Regsol (art. XX.173). De rechtbank wijst dit standaard toe behoudens fraude — zwijgen kost de cliënt zijn 'tweede kans'.

<small>📚 WER — art. XX.173 § 1 — _wettekst_</small>

##### 👣 Bestuurder-aansprakelijkheid bespreken vóór aangifte  
_`stap`_

🔗 Bij rechtspersoon-faillissement: bespreek met de bestuurder de risico's van art. XX.225 (wrongful trading) en XX.226 (kennelijk grove fout). Documenteer de redelijke vooruitzichten-analyse — als bestuurder kan aantonen dat hij op het moment van doorgaan redelijkerwijs op herstel mocht hopen, is wrongful trading uitgesloten. Een goed gedocumenteerd budget + cashflow-plan helpt.

<small>📚 WER — art. XX.225 + XX.226 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### Accountantskantoor als schuldeiser (openstaande erelonen)

#### 🧭 Adviseur

##### 👣 Eigen aangifte schuldvordering tijdig indienen  
_`stap`_

📖 Binnen de termijn van het faillietvonnis (meestal 30 dagen): dien via Regsol aangifte in van openstaande erelonen — naam, ondernemingsnummer, bedrag, eventuele voorrang. Boekhoudkundige erelonen genieten geen bijzonder voorrecht: ze zijn 'gewone schuld'. Verwacht dus zelden meer dan de 'pari passu'-uitkering (typisch 5-15% bij faillissement zonder voorrechten-overschot).

<small>📚 WER — art. XX.155-156 — _wettekst_</small>

## Verder lezen (scope-out)

- → Parent kader — WER boek XX → [[insolventierecht-wer-boek-xx]] _(moet-verwijzen)_
- → Gerechtelijke-reorganisatie als alternatieve route → [[gerechtelijke-reorganisatie]] _(moet-verwijzen)_
- → Bestuurdersaansprakelijkheid bij faillissement (WER XX:225) → [[bestuurdersaansprakelijkheid]] _(moet-verwijzen)_
- → Oprichtersaansprakelijkheid bij faillissement binnen 3 jaar → [[oprichtersaansprakelijkheid]] _(moet-verwijzen)_
- → Ontbinding-vereffening als gerechtelijke afhandeling → [[ontbinding-en-vereffening]] _(moet-verwijzen)_
- → Rehabilitatie + verschoonbaarheid → [[rehabilitatie-en-beroepsverbod]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[insolventierecht-wer-boek-xx]]
### `vergelijkbaar_met`
- [[gerechtelijke-reorganisatie]]
    - **Gelijkenissen**:
        - Beide vallen onder WER boek XX
        - Beide zijn gerechtelijke procedures onder ondernemingsrechtbank
    - **Verschillen**:
        - Reorganisatie zoekt continuïteit; faillissement vereffent de boedel
        - Reorganisatie schort uitvoeringsmaatregelen op; faillissement neemt het beheer over
    - ⚠️ **Verwarringsrisico**: Studenten zien faillissement vaak als 'mislukte reorganisatie'; in werkelijkheid zijn het twee autonome routes met eigen voorwaarden
### `triggert`
- [[bestuurdersaansprakelijkheid]]
- [[oprichtersaansprakelijkheid]]
- [[ontbinding-en-vereffening]]
### `vereist`
- [[rehabilitatie-en-beroepsverbod]]
