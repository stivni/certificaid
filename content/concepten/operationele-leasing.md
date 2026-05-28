---
title: "Operationele leasing"
concept_type: "instrument"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 3.0.IV.D
tags:
  - concept
  - schema-2.2
  - type-instrument
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/operationele-leasing.json"
---

# Operationele leasing

_Instrument_

📋 Regeling · Anchors: `3.0.IV.D` · Wave: `skeleton-vennootschapsrecht-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: operating lease · off-balance lease · huur-leasing — **Vertalingen**: fr: location simple / leasing operationnel · en: operating lease

## Definitie

📖 Operationele leasing is een leasingvorm waarbij economisch gezien de risico's en voordelen van de eigendom van het actief NIET overgaan op de leasingnemer. De leasinggever blijft economisch en juridisch eigenaar, schrijft het actief op zijn eigen balans af en boekt de leasevergoedingen als opbrengsten. De leasingnemer behandelt het contract als een gewoon huurcontract: hij boekt de leasevergoeding als huurkost in rekening 610 ('Huur en huurlasten'), zonder actief of leasingschuld op de balans (off-balance). Het contract heeft enkel gevolgen voor de resultatenrekening. Belangrijke uitzondering: onder IFRS 16 (sinds 2019) moet de lessee een operationele lease toch on-balance brengen via een right-of-use-actief en leaseverplichting - het off-balance-voordeel geldt enkel nog onder BE-GAAP.

<small>📚 CBN-advies 2021/05 — Operationele leasing - actief blijft op balans van leasinggever, huurkost bij leasingnemer — _cbn_ · CBN-advies 2015/4 — Kwalificatie tegenover financiele leasing — _cbn_ · IFRS 16 (Verordening (EU) 2023/1803) — alinea 22 - lessee opname RoU + leaseverplichting — _wettekst_</small>

## Substantie

🔗 Voor de leasingnemer voelt operationele leasing aan als een huurcontract: hij gebruikt het actief, betaalt een vaste vergoeding, en heeft geen zorg over restwaarde of verkoop op het einde. Dat is precies de aantrekkingskracht voor activa met snelle technologische veroudering (IT-uitrusting, bedrijfswagens): de leasinggever draagt het risico op waardedaling en op marktwerking. Bij full-service lease (vooral bij wagenpark) zijn onderhoud, verzekering en wegenbelasting inbegrepen - de gebruiker hoeft enkel de leasingfactuur te betalen. Boekhoudkundig blijft alles eenvoudig: een lijn in de resultatenrekening, geen vast actief, geen leasingschuld - de solvabiliteitsratio blijft gunstig.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 De juridische en boekhoudkundige rationale: wanneer de leasinggever de risico's van eigendom blijft dragen (restwaarde-risico, technologisch risico, verzekeringsrisico, herinvesteringsrisico), is het oneerlijk de leasingnemer als economisch eigenaar te behandelen. Operationele leasing is een echt gebruiksrecht-contract - meer verwant met huur dan met financiering. Tot 2019 was deze structuur boekhoudkundig consistent in alle stelsels. IFRS 16 heeft dit voor de lessee-kant herzien: er werd geoordeeld dat te veel ondernemingen via operationele leasing materiele schulden buiten balans hielden, wat de vergelijkbaarheid verstoorde. Voor de lessor is het onderscheid wel behouden onder IFRS 16, en BE-GAAP volgt nog steeds de oude tweedeling voor zowel lessor als lessee.

<small>📚 IFRS 16 (Verordening (EU) 2023/1803) — Toelichting bij Lessor-classificatie - risico's en voordelen — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: BE-GAAP: KB WVV art. 3:89 + CBN-advies 2015/4 (off-balance bij lessee). IFRS 16 (Verordening (EU) 2023/1803): lessor-zijde behoudt onderscheid, lessee-zijde alle leases on-balance behalve vrijstellingen.

Voor enkelvoudige BE-GAAP-jaarrekeningen blijft de klassieke off-balance verwerking gelden. IFRS-rapporterende vennootschappen moeten sinds 2019 voor de geconsolideerde jaarrekening operationele leases on-balance brengen volgens IFRS 16.

**✅ Voor**
- 🔗 Gebruik van een actief met snelle technologische veroudering of waarvan de restwaarde onzeker is: bedrijfswagens, IT-uitrusting, kopieerapparaten, gespecialiseerde machines met korte cyclus. Ook voor activa waarbij service-elementen (onderhoud, verzekering, ondersteuning) makkelijker centraal bij de leasinggever geregeld kunnen worden.

**👍 Voordeel**
- 🔗 Off-balance onder BE-GAAP: gunstig voor solvabiliteitsratio en debt/equity-verhouding. Volledige leasingvergoeding aftrekbaar als beroepskost (eenvoudige fiscale verwerking, geen splitsing kapitaal/rente). Restwaarde-risico volledig bij de leasinggever - leasingnemer hoeft niet te zorgen voor doorverkoop. Bij full-service lease: service-elementen inbegrepen tegen een vaste prijs.

**⚠️ Risico**
- 📖 Onder IFRS 16 verdwijnt het off-balance-voordeel voor de lessee. Voor een groepscliënt die zowel een enkelvoudige BE-GAAP-jaarrekening als een geconsolideerde IFRS-jaarrekening opstelt: dubbele verwerking + reconciliatie. Het off-balance-voordeel blijft enkel volledig zichtbaar in de enkelvoudige Belgische jaarrekening.
- 🔗 Total cost-of-ownership over de levensduur kan hoger uitvallen dan bij koop of financiele leasing - de leasinggever rekent zijn risicodragend kapitaal en zijn service-marge door. Vooral bij langjarig gebruik van hetzelfde actief kan kopen of financiele leasing voordeliger zijn.
- 🔗 Toelichting bij de jaarrekening (BE-GAAP) vermeldt de niet-uit-de-balans-blijkende verbintenissen onder de operationele leasing. Wie deze toelichting niet correct opmaakt, riskeert een commissaris-opmerking en geeft een onvolledig beeld aan stakeholders.

## Bouwstenen

### 📜 Kwalificatie - tegenpool van financiele leasing  
_`regel`_

📖 Een leasing wordt als operationeel gekwalificeerd onder BE-GAAP wanneer de criteria voor financiele leasing niet vervuld zijn: typisch wanneer de wedersamenstelling van het kapitaal niet volledig gebeurt (leasevergoedingen + eventueel meegerekende koopoptie dekken niet het geinvesteerde kapitaal van de leasinggever), of wanneer de koopoptie boven 15% van het kapitaal ligt (en dus niet meetelt voor de wedersamenstelling). Onder IFRS 16 (lessor-zijde): de leasing is operationeel wanneer niet nagenoeg alle eigendoms-gerelateerde risico's en voordelen overgaan op de lessee.

<small>📚 CBN-advies 2015/4 — Kwalificatie - operationeel = niet voldoen aan financiele criteria — _cbn_ · IFRS 16 (Verordening (EU) 2023/1803) — alinea 62 - definitie operationele lease lessor-kant — _wettekst_</small>

### ⚙️ Off-balance verwerking bij leasingnemer (BE-GAAP)  
_`mechanisme`_

📖 Bij elke leaseperiode: D 610 'Huur en huurlasten' | C 55 Bank (volledige leasingvergoeding). Geen actief, geen leasingschuld op de balans. Bij vooruit- of achterafbetaalde periodes: regularisatie via rekening 490 ('Over te dragen kosten') of 492 ('Toe te rekenen kosten'). Service-elementen inbegrepen in de leasingvergoeding (bij full-service lease) worden niet apart geboekt; het volledige bedrag gaat in 610. In de toelichting bij de jaarrekening: melding van het bedrag en de looptijd van de niet-uit-de-balans-blijkende leasingverbintenissen.

<small>📚 CBN-advies 2021/05 — Boekhoudkundige verwerking operationele leasing — _cbn_</small>

### 📜 IFRS 16 lessee-on-balance - andere verwerking  
_`regel`_

📖 Onder IFRS 16 wordt elke operationele leasing bij de lessee on-balance gebracht (uitgezonderd short-term <=12m en low-value <=5.000 USD). Boeking: D Right-of-Use-actief | C Leaseverplichting voor de contante waarde van de toekomstige leasebetalingen, verdisconteerd tegen de marginale rentevoet van de lessee. Bij elke betaling: D Leaseverplichting (kapitaaldeel) + D Rentelasten (rentedeel) | C Bank. RoU-actief wordt afgeschreven over de leaseperiode. Voor cliëntenen die zowel BE-GAAP enkelvoudig als IFRS-geconsolideerd rapporteren: dubbele boekhouding met reconciliatie.

<small>📚 IFRS 16 (Verordening (EU) 2023/1803) — alinea 22-49 + B3-B8 vrijstellingen — _wettekst_</small>

### 💡 Full-service lease (typisch bedrijfswagens)  
_`begrip`_

🔗 Bij full-service lease (vooral courant voor bedrijfswagens) zijn naast het zuivere gebruik ook service-elementen inbegrepen: onderhoud, banden, verzekering, wegenbelasting, soms tankkaart. Eén factuur, één aftrekbare beroepskost. De fiscale aftrekbaarheid is voor wagens beperkt door de specifieke aftrekregels voor autokosten (CO2-gebonden + 17%/40%-regel voor VAA). De volledige leasingvergoeding wordt gesplitst tussen aftrekbaar en niet-aftrekbaar gedeelte; service-elementen volgen typisch dezelfde aftrek-procentages als de huur-kost zelf.

<small>📚 WIB92 — art. 66 en 198/1, 9° + 9°bis (autokosten) — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Voorbeelden

### 💡 Operationele leasing bedrijfswagen (full-service) 🔗

_BV Optima sluit een full-service leaseovereenkomst af voor een bedrijfswagen. Looptijd 4 jaar, maandelijkse leasingvergoeding 700 EUR (incl. onderhoud, verzekering, wegenbelasting). Aankoopprijs nieuwe wagen 35.000 EUR. Geen koopoptie - wagen gaat na 4 jaar terug naar de leasinggever._

**Berekening:**
- Stap 1 - kwalificatie: geen koopoptie + looptijd 4 jaar << economische levensduur wagen (8-10 jaar) -> operationele leasing onder BE-GAAP.
- Stap 2 - totale contractuele wedersamenstelling: 48 maanden x 700 = 33.600 EUR; geen koopoptie. Dat dekt 33.600/35.000 = 96% van het geinvesteerd kapitaal; deel van de risico's (restwaarde wagen, technologische veroudering) blijft bij leasinggever -> operationele leasing bevestigd.
- Stap 3 - maandelijkse boeking bij BV Optima: D 610 700 | C 55 700. Geen vast actief, geen leasingschuld op de balans.
- Stap 4 - fiscale aftrek (vennootschapsbelasting): autokostenpercentage afhankelijk van CO2-uitstoot (zie autokosten-record). Een wagen met 100 g/km CO2: ~ 75% aftrekbaar. De rest (25%) komt als verworpen uitgave (code 1206 in de aangifte VenB).
- Stap 5 - toelichting jaarrekening: vermeld de niet-uit-de-balans-blijkende verbintenis 4-jarige leasing, indicatief totaal 33.600 EUR.

→ **Resultaat**: Off-balance verwerking onder BE-GAAP. Voor een groep met IFRS-rapportering zou dezelfde wagen on-balance komen (RoU-actief ~ 30.000 EUR + leaseverplichting ~ 30.000 EUR).

<small>📚 CBN-advies 2021/05 — Operationele leasing - verwerking — _cbn_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Operationele leasing kiezen om off-balance te blijven, zonder rekening te houden met IFRS-rapporteringsplicht

**Verkeerde assumptie**: Door operationele leasing te kiezen blijft de schuld permanent off-balance.

**Kernpunt**: Voor BE-GAAP-only-cliënten (de meeste KMOs) klopt dit. Voor IFRS-rapporterende cliënten - typisch beursgenoteerde groepen of grote dochterondernemingen - brengt IFRS 16 sinds 2019 vrijwel alle leases on-balance. Voor zulke groepen verdwijnt het off-balance-voordeel. Vraag bij elke leaseovereenkomst van een groepscliënt: welk referentiestelsel geldt voor consolidatie?

<small>📚 IFRS 16 (Verordening (EU) 2023/1803) — alinea 22 - lessee on-balance — _wettekst_</small>

### ⚠️ Off-balance vergeten te vermelden in de toelichting

**Verkeerde assumptie**: Off-balance betekent helemaal geen vermelding in de jaarrekening.

**Kernpunt**: BE-GAAP vereist dat niet-uit-de-balans-blijkende verbintenissen (waaronder operationele leasing) in de toelichting bij de jaarrekening worden vermeld, met indicatie van het bedrag en de looptijd. Wie deze vermelding vergeet, geeft een onvolledig beeld en kan een commissaris-opmerking krijgen. Voor grote leaseverplichtingen kan dit ook materieel belangrijk zijn voor de jaarrekening-lezer.

<small>📚 KB 29-04-2019 jaarrekening — Toelichting - niet uit de balans blijkende verbintenissen — _kb_</small>

### ⚠️ Operationele leasing en huurcontract als hetzelfde behandelen

**Verkeerde assumptie**: Operationele leasing is gewoon een huurcontract - dezelfde behandeling, dezelfde aftrek.

**Kernpunt**: Boekhoudkundig zijn ze inderdaad sterk vergelijkbaar (beide op rekening 610). Maar de leasingstructuur is een driepartijenstructuur (leasinggever koopt op vraag van leasingnemer) - bij een huurcontract is de verhuurder al eigenaar voorgaand. Fiscaal en juridisch kunnen er nuances zijn: bedrijfswagens via leasing volgen de autokosten-aftrekregels onder art. 66/198/1 WIB92; gewone huur niet altijd op dezelfde manier. Bij een echte sale-and-lease-back zou de huurbetaling toegerekend kunnen worden aan een verborgen financiering - dan kan de operationele kwalificatie ter discussie staan.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Accountant-perspectieven

### Leasingnemer (clientvennootschap)

_De accountant die de operationele leasing bij de cliënt-vennootschap boekt en fiscaal verwerkt._

#### 📒 Boekhouder

##### 👣 Verwerking + toelichting bij jaarrekening  
_`stap`_

📖 (1) Boek elke leasevergoeding als D 610 | C 55. (2) Bij vooruit-/achterafbetaalde periodes: regulariseer via 490/492. (3) Bij boekjaarafsluiting: lijst de uitstaande verbintenissen (resterende leasebetalingen over de hele looptijd) en neem ze op in de toelichting bij de jaarrekening onder 'niet-uit-de-balans-blijkende verbintenissen'. (4) Voor IFRS-rapporterende cliënten: parallel berekenen van de IFRS 16-impact (RoU + leaseverplichting) - typisch via een aparte tool of Excel-spreadsheet die je elke afsluiting bijwerkt. (5) Bij autoleasing: pas de specifieke autokosten-aftrekregels toe.

<small>📚 CBN-advies 2021/05 — Verwerking operationele leasing — _cbn_ · KB 29-04-2019 jaarrekening — Toelichting niet-uit-de-balans-blijkende verbintenissen — _kb_</small>

#### 🧭 Adviseur

##### 📜 Afweging koop vs financiele vs operationele leasing  
_`regel`_

🔗 Bij elke grote actief-investering: drie scenario's vergelijken. Koop met banklening: eigenaarschap onmiddellijk, afschrijving + rente aftrekbaar, schuld op balans. Financiele leasing: eigenaarschap op het einde, on-balance verwerking, aftrek via afschrijving + rente. Operationele leasing: gebruiksrecht zonder eigendomsoverdracht, off-balance onder BE-GAAP, full leasingvergoeding aftrekbaar (eenvoudiger). Operationele leasing scoort bij snelle technologische veroudering en bij voorkeur voor full-service. Voor IFRS-cliënten: aandacht voor RoU-verwerking onder IFRS 16.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Leasing-parent - algemeen kader → [[leasing]] _(moet-verwijzen)_
- → Financiele leasing - tegenpool met on-balance-verwerking → [[financiele-leasing]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[leasing]]
### `vergelijkbaar_met`
- [[financiele-leasing]]
    - **Gelijkenissen**:
        - Beide vallen onder hetzelfde leasingkader (BE-GAAP + IFRS 16)
        - Beide hebben de driepartijenstructuur leasinggever-leasingnemer-actief
        - Beide leiden tot een periodieke betalingsverplichting van de leasingnemer
    - **Verschillen**:
        - Operationele leasing: off-balance bij lessee onder BE-GAAP; financiele leasing: on-balance
        - Operationele leasing: geen actief, geen leasingschuld, enkel huurkost; financiele leasing: actief op balans + leasingschuld + afschrijving + rente apart
        - Operationele leasing: lessor blijft economisch eigenaar (restwaarde-risico); financiele leasing: lessee draagt economische eigendomsrisico's
        - IFRS 16: voor de lessee verdwijnt het onderscheid - beide on-balance behalve vrijstellingen
    - ⚠️ **Verwarringsrisico**: Kwalificatie hangt af van details (koopoptieprijs, looptijd, gebruiksgraad). Eenzelfde economische situatie kan onder BE-GAAP operationeel zijn (off-balance) en onder IFRS 16 on-balance worden gebracht.
