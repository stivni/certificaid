---
title: "Banklening (investeringskrediet)"
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
gegenereerd_uit: "data/concepten/records/banklening-investeringskrediet.json"
---

# Banklening (investeringskrediet)

_Instrument_

📋 Regeling · Anchors: `3.0.IV.D` · Wave: `skeleton-vennootschapsrecht-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: investeringskrediet · bankkrediet op middellange/lange termijn · term loan — **Vertalingen**: fr: crédit d'investissement · en: investment loan

## Definitie

📖 Een banklening is een schriftelijke kredietovereenkomst waarbij een kredietinstelling een bepaald bedrag ter beschikking stelt van een onderneming, mits terugbetaling volgens een afgesproken schema en betaling van rente op het uitstaande saldo. Een investeringskrediet is de specifieke variant waarbij de financiering bestemd is voor een bepaalde investering (gebouw, machine, voertuig, immateriële activa) en de looptijd doorgaans gelijk loopt met de economische levensduur van het actief. De vennootschap boekt het volledige opgenomen bedrag op rekening 17 (schulden op meer dan een jaar). Bij elke boekjaarafsluiting wordt het deel dat binnen het volgende boekjaar opeisbaar wordt, overgeheveld naar rekening 42.

<small>📚 KB 29-04-2019 jaarrekening — MAR-rubriek 17 + 42 — _kb_ · CBN-advies 2016/11 — Boekhoudkundige verwerking - 'aan 174 Andere leningen op meer dan één jaar' — _cbn_ · CBN-advies 2012/16 — Wentelkredieten - rangschikkingscriterium volgens werkelijke vervaltermijn — _cbn_</small>

## Substantie

🔗 Voor de KMO is de banklening de standaardroute om grote investeringen te financieren wanneer de eigen middelen niet volstaan. De bank beoordeelt eerst de kredietwaardigheid (solvabiliteit, terugbetalingscapaciteit uit verwachte kasstromen, waarborgen) en bepaalt vervolgens drie kernparameters: bedrag, looptijd en rente. De rente wordt bepaald in functie van het krediet-risico (rating van de onderneming, kwaliteit van de waarborgen) en de marktrente. De terugbetaling kan in gelijke kapitaalaflossingen (dalend rente-component), in vaste annuïteiten (gelijk maandbedrag), of bullet (volledig op het einde). Tijdens de looptijd kunnen er financial covenants zijn die periodiek getoetst worden - bij overtreding kan de bank de lening opzeggen of bijkomende voorwaarden stellen.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 Het investeringskrediet is een matching-instrument: een investering in een actief met een lange economische levensduur (bv. een gebouw met 30 jaar levensduur) hoort gefinancierd met vreemd vermogen op vergelijkbare termijn - niet met kortlopende financiering die voortdurend herfinanciering vraagt (looptijdmismatch-risico). De bank op haar beurt eist tegen deze 'illiquide' positie zekerheden en covenants, omdat ze het uitstaande kapitaal niet kort-snel kan terugvorderen. Voor de schuldeiser zit het risico in twee dimensies: kredietrisico (gaat de onderneming failliet?) en herinvesteringsrisico voor de bank (rentecyclus). Voor de onderneming biedt het krediet een hefboomeffect: rendement op eigen vermogen kan stijgen mits het rendement op de gefinancierde activa hoger is dan de rentekost (na belasting).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: Algemeen contractenrecht + kredietregelgeving (Wet 21-12-2013 betreffende diverse bepalingen consumentenkrediet voor consumentenkredieten; voor B2B-investeringskredieten vooral contractvrijheid en Wet 14-07-2021 betreffende KMO-financiering)

**✅ Voor**
- 🔗 Financiering van duurzame investeringen waarvan de economische levensduur en de terugbetalingscapaciteit op de lange termijn gespreid kunnen worden: gebouwen, productiemiddelen, rollend materieel, omvangrijke immateriële activa, overnames.

**🚫 Niet voor**
- 📖 Niet voor seizoensgebonden werkkapitaal-tekort of tijdelijke kasspanning - daar past een kaskrediet, een wentelkrediet of straight loan (CBN 2012/16 - schulden binnen een jaar terugbetaalbaar horen onder rekening 43).

**📋 Voorwaarden**
- 🔗 Voorafgaand: positieve kredietbeoordeling van de bank (solvabiliteit, terugbetalingscapaciteit, business plan voor de investering). Schriftelijke kredietovereenkomst die bedrag, looptijd, aflossingsschema, rentevoet (vast of variabel + referte-index), eventuele waarborgen en convenanten vastlegt. Notariele akte vereist bij hypotheekverlening.

**👍 Voordeel**
- 🔗 Hefboomeffect (leverage): financiering met vreemd vermogen verhoogt het rendement op eigen vermogen wanneer het rendement op de gefinancierde activa hoger ligt dan de na-belasting-rentekost. Bewaart aandeelhoudersstructuur (geen verwatering). Rente is fiscaal aftrekbaar binnen de grenzen van art. 198/1 WIB92.

**⚠️ Risico**
- 🔗 Negatief hefboomeffect: wanneer het rendement op de gefinancierde activa onder de rentekost zakt, vergroot vreemd vermogen het verlies op het eigen vermogen. Bij rente op variabele basis komt daar renterisico bij - een stijgende referte-index kan de schuldenlast snel zwaarder maken.
- 🔗 Covenant-breach: financiële convenanten (minimum-solvabiliteit, EBITDA-coverage, beperking dividenden) worden periodiek getoetst. Een overtreding geeft de bank meestal het recht om bijkomende waarborgen te eisen, de rente te verhogen of het krediet onmiddellijk opeisbaar te stellen. Tijdige rapportering aan de bank en proactieve communicatie zijn essentieel.
- 🔗 Persoonlijke borg van de zaakvoerder of aandeelhouder: zeer courant bij KMO-kredieten. Bij niet-terugbetaling kan de bank op het persoonlijke vermogen van de borg verhalen. Bij echtgenoten/wettelijk samenwonenden kan dat ook het gezinsvermogen treffen - oprechte toestemming van de partner is vereist.

## Bouwstenen

### 📜 Boekhoudkundige rubricering 17 / 42 / 43  
_`regel`_

📖 Bij opname van de banklening: D 55 Bank | C 174 (of relevante subrekening van 17 'Andere leningen op meer dan een jaar') voor het volledige bedrag. Bij elke boekjaarafsluiting: overheveling van het binnen het volgende boekjaar opeisbare deel van rekening 17 naar rekening 42 ('Schulden op meer dan een jaar die binnen het jaar vervallen'). Bij volledige terugbetaling: schuld dooft uit. Belangrijk: het rangschikkingscriterium is de werkelijke vervaldatum, niet de benaming. Een 'lening op lange termijn' waarbij de bank het kapitaal binnen het jaar kan opvragen, hoort onder de korte-termijn-schulden.

<small>📚 CBN-advies 2012/16 — Boekhoudkundige verwerking wentelkredieten - rangschikking volgens werkelijke vervaltermijn — _cbn_ · CBN-advies 2016/11 — Boeking opname banklening op rekening 174 — _cbn_</small>

### ⚙️ Aflossingsschema-typen  
_`mechanisme`_

🔗 Drie standaardtypen: (1) Bullet - geen kapitaalaflossing tijdens looptijd, volledige hoofdsom op vervaldag terugbetaald; zwaarste eindbetaling, herfinancieringsrisico op vervaldag; (2) Lineair / vaste kapitaalaflossingen - elke periode hetzelfde kapitaalbedrag, rente op dalend uitstaand saldo; betalingen dalen over de tijd; (3) Annuïtair - vaste maand-/kwartaalbetalingen (kapitaal + rente) gedurende de hele looptijd; rentegedeelte daalt, kapitaalgedeelte stijgt over de tijd. Bij vaste rente is annuïteit voorspelbaar; bij variabele rente herrekenen bij elke rente-aanpassing. De accountant moet bij boeking telkens het rentegedeelte (rekening 65) afsplitsen van het kapitaalgedeelte (afboeking 17/42).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📜 Waarborgen - balansvermelding en niet-uitvoerings-verbintenissen  
_`regel`_

📖 Waarborgen versterken de positie van de bank: hypotheek op gebouwen, pand op handelszaak, pand op specifieke activa (machines, voorraden), of persoonlijke borg. Zakelijke zekerheden worden vermeld in de Staat over de betrekkingen + in de toelichting bij de jaarrekening, onder rekening 00-09 (orderrekeningen). Een hypothecair mandaat (onherroepelijke belofte om hypotheek te vestigen, zonder werkelijke inschrijving) wordt geboekt onder 'onherroepelijk beloofd'. Een effectieve hypotheek onder 'gesteld'. De jaarrekening-lezer moet zo zicht krijgen op de mate waarin activa al verpand of belast zijn.

<small>📚 CBN-advies 2018/17 — Schulden gewaarborgd door een zakelijke zekerheid - boekingstabel orderrekeningen — _cbn_</small>

### 📜 Renteboeking en prorata bij boekjaarafsluiting  
_`regel`_

🔗 Rente wordt op tijdsproportionele basis erkend (matching). Bij boekjaarafsluiting moet de vervallen maar nog niet betaalde rente opgenomen worden via een overlopende rekening (492 'Toe te rekenen kosten'). Bij vooruitbetaalde rente (zeldzaam) gebruikt men 490 'Over te dragen kosten'. De jaarlijkse rentelast komt in resultaat onder rekening 650 'Rente, commissies en kosten verbonden aan schulden'. Bij een banklening met variabele rente moet bij elke rente-aanpassing de toekomstige rentelast herrekend worden voor budgettering.

<small>📚 KB 29-04-2019 jaarrekening — MAR rekening 650 + 49 — _kb_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📜 Fiscale renteaftrek (art. 198/1 WIB92)  
_`regel`_

📖 De interest op een banklening is in beginsel een aftrekbare beroepskost. De algemene aftrekbeperking voor financieringskostensurplus (art. 198/1 WIB92, omzetting van ATAD-richtlijn) beperkt het netto-financieringskostensurplus (financieringskosten min financieringsopbrengsten) tot het hoogste van 3 miljoen EUR of 30% van het fiscaal EBITDA. Niet-aftrekbare interesten kunnen overgedragen worden naar latere boekjaren. Voor KMO's met beperkte financiering ligt het surplus typisch onder de 3 miljoen-drempel en is er geen praktische beperking.

<small>📚 WIB92 — art. 198/1 — _wettekst_ · CBN-advies 2020/06 — Financieringskostensurplus — _cbn_</small>

## Voorbeelden

### 💡 Annuïtaire investeringslening met vaste rente 🔗

_BV Optima neemt op 1 januari een investeringskrediet op van 500.000 EUR aan vaste rente 4%, met annuïtaire aflossing over 10 jaar (jaarlijkse vaste betalingen). De annuïteit = 500.000 * 4% / (1 - 1,04^-10) = ca. 61.645 EUR per jaar._

**Boeking:**


**Berekening:**
- Stap 1 - jaar 1 rente: 500.000 * 4% = 20.000 EUR. Kapitaalaflossing: 61.645 - 20.000 = 41.645 EUR.
- Stap 2 - boeking jaar 1: D 174 41.645 + D 650 (rentelasten) 20.000 | C 55 Bank 61.645.
- Stap 3 - eind boekjaar 1: nieuw uitstaand saldo = 500.000 - 41.645 = 458.355 EUR. Daarvan is het deel dat binnen jaar 2 opeisbaar wordt (kapitaalaflossing jaar 2) over te hevelen van 174 naar 42 ('Schulden op meer dan een jaar binnen het jaar vervallend').
- Stap 4 - kapitaalaflossing jaar 2: nieuwe rente = 458.355 * 4% = 18.334; kapitaal = 61.645 - 18.334 = 43.311 EUR. Overheveling: D 174 43.311 | C 42 43.311.
- Stap 5 - na 10 jaar is het volledige krediet terugbetaald; totale betaalde rente = 10 * 61.645 - 500.000 = ca. 116.450 EUR.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Geen overheveling 17 -> 42 bij afsluiting

**Verkeerde assumptie**: Een 10-jaars lening blijft de hele looptijd onder rekening 17 staan tot ze afgelost is.

**Kernpunt**: Bij elke boekjaarafsluiting moet het deel van de hoofdsom dat binnen het volgende boekjaar vervalt, overgeheveld worden van rekening 17 naar rekening 42. Zonder deze overheveling toont de jaarrekening een vertekend liquiditeitsbeeld - de current ratio en de kortlopende schulden zien er kunstmatig beter uit. Dit is een veel voorkomende fout bij niet-geprofessionaliseerde boekhoudingen.

<small>📚 CBN-advies 2012/16 — Rangschikking schulden volgens stijgende eisbaarheid — _cbn_</small>

### ⚠️ Variabele rente vergeten te herrekenen voor budget

**Verkeerde assumptie**: Bij een lening met variabele rente blijft de financiële last hetzelfde als bij opname.

**Kernpunt**: Variabele rentes worden periodiek herzien (vaak per kwartaal of jaar) op basis van een referte-index (Euribor, OLO). Een rentestijging van 2 procentpunten op een uitstaand saldo van 500.000 EUR = 10.000 EUR extra rentelast per jaar - dat kan een KMO uit balans brengen. Bij budgettering moet de gevoeligheid voor rentebewegingen expliciet getoetst worden.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Persoonlijke borg lichtzinnig laten ondertekenen

**Verkeerde assumptie**: De persoonlijke borg van de zaakvoerder is een formaliteit; bij een goedlopende vennootschap wordt die nooit aangesproken.

**Kernpunt**: Persoonlijke borg blijft normaal opeisbaar zolang het krediet niet volledig terugbetaald is - ook na overdracht van aandelen, ontslag als zaakvoerder, of echtscheiding. De zaakvoerder die zijn vennootschap verlaat moet expliciet onderhandelen over vrijgave van de borg, eventueel via vervanging door een nieuwe borg of door cash-zekerheid. Wettelijke samenwonende of gehuwde partner: oprechte toestemming verplicht, en de borg kan bij echtscheiding tot conflict leiden.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Speelruimtes

### 🎚️ Vaste vs variabele rente

## Accountant-perspectieven

### Debiteur-vennootschap

_De accountant die het bankkrediet bij de cliënt boekhoudkundig opvolgt, en die bij onderhandeling of advies meedenkt over de financieringsstructuur._

#### 📒 Boekhouder

##### 👣 Boekjaarafsluiting - overheveling en renteprorata  
_`stap`_

🔗 Bij elke afsluiting: (1) bereken het deel van de hoofdsom dat in het volgende boekjaar opeisbaar wordt op basis van het aflossingsschema; (2) boek D 17 | C 42 voor dat bedrag; (3) bij vervallen maar onbetaalde rente: D 650 | C 492 (toe te rekenen kosten); (4) bij vooruitbetaalde rente: D 490 (over te dragen kosten) | C 650; (5) controleer dat de jaarrekening de uitstaande hoofdsom correct splitst (17 langlopend vs 42 binnen het jaar) - dit is een kerncomponent van de liquiditeitsratio's.

<small>📚 CBN-advies 2012/16 — Rangschikking schulden volgens vervaltermijn — _cbn_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 🧭 Adviseur

##### 👣 Onderhandeling met de bank - dossier voorbereiden  
_`stap`_

🔗 Voor de cliënt het kredietdossier opbouwen: (1) recente jaarrekeningen + tussentijdse cijfers; (2) investeringsmemorandum met business case voor de investering; (3) prognose-kasstromen die de terugbetalingscapaciteit aantonen; (4) inventaris van beschikbare waarborgen (gebouwen, handelszaak, ...); (5) andere lopende financieringen + bestaande convenanten. Bij meerdere offertes: vergelijk niet enkel de rente, maar ook de afsluitingskosten, dossierkosten, beheerskosten, vervroegde-terugbetalingsvergoedingen, gevraagde waarborgen en convenanten. Een lagere rente met zware waarborgen kan duurder uitvallen dan een iets hogere rente met soepelere voorwaarden.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

##### 👣 Convenant-monitoring tijdens looptijd  
_`stap`_

🔗 Bij elke afsluiting expliciet de financial covenants berekenen: typisch minimum-solvabiliteit (eigen vermogen / balanstotaal), EBITDA-coverage-ratio (EBITDA / financiële lasten), debt-service-coverage. Bij dreigende overtreding: tijdig en proactief de bank contacteren. Banken zijn doorgaans bereid een waiver of aanpassing toe te staan bij open communicatie; daarentegen reageren ze hard op verborgen breuken die ze later zelf ontdekken.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Eigen vermogen - afbakening vreemd vs eigen vermogen → [[eigen-vermogen]] _(moet-verwijzen)_
- → Obligatielening - alternatief financieringsinstrument met effecten-statuut → [[obligatielening]] _(moet-verwijzen)_
- → Achtergestelde lening - variant met lagere rang → [[achtergestelde-lening]] _(moet-verwijzen)_
- ↪ Leasing - alternatieve route voor activa-financiering → [[leasing]] _(mag-verwijzen)_
- ↪ Financieringskostensurplus - art. 198/1 WIB92 → [[financieringskostensurplus]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[lening]]
### `vergelijkbaar_met`
- [[obligatielening]]
    - **Gelijkenissen**:
        - Beide zijn schuldinstrumenten op meer dan een jaar
        - Beide genereren aftrekbare rentelasten binnen art. 198/1 WIB92
        - Beide worden geboekt onder schulden op meer dan een jaar (rubriek VIII)
    - **Verschillen**:
        - Banklening: bilaterale overeenkomst met één kredietinstelling, sterk gestandaardiseerd via interne procedures van de bank
        - Obligatielening: effecten-instrument, uitgegeven aan veelheid van investeerders, vereist prospectusplicht (boven drempels) en effecten-procedure
        - Banklening kent meestal financial covenants; obligatielening werkt eerder met trust deed en covenants in de prospectus
        - Banklening is minder verhandelbaar; obligaties kunnen op markt circuleren
    - ⚠️ **Verwarringsrisico**: Beide eindigen in rubriek VIII van het passief, maar op verschillende subrekeningen: bankleningen op 173 of 174; obligaties op 170-171.
- [[achtergestelde-lening]]
    - **Gelijkenissen**:
        - Beide zijn leningen op middellange/lange termijn
        - Beide kennen rente die fiscaal aftrekbaar is
    - **Verschillen**:
        - Banklening is doorgaans niet achtergesteld (eventueel pari passu of bevoorrecht via zekerheden); de bank wil net vooraan in de rij staan
        - Bankleningen worden door kredietinstellingen verstrekt; achtergestelde leningen vaak door aandeelhouders
        - Banklening wordt niet als quasi-eigen-vermogen gezien; achtergestelde lening wel in bancaire beoordeling
    - ⚠️ **Verwarringsrisico**: Beide staan onder schulden op > 1 jaar (rubriek VIII), maar op verschillende sub-rubrieken. Achtergestelde leningen onder VIII.A.1 (rekening 17/4); bankleningen onder VIII.A.2 of B (rekening 173-174).
- [[leasing]]
    - **Gelijkenissen**:
        - Beide financieren de aankoop of het gebruik van een specifiek actief
        - Beide genereren een periodieke betalingsverbintenis
    - **Verschillen**:
        - Banklening: vennootschap wordt onmiddellijk eigenaar van het actief en boekt het op haar balans; krediet apart in passief
        - Leasing: vennootschap is huurder; eigendom blijft bij de leasinggever. Bij financiële leasing wordt het actief wel op de balans van de leasingnemer geboekt (CBN-advies leasing)
        - Banklening kent vaak ruimere waarborgkeuzes; leasing heeft het actief zelf als waarborg
    - ⚠️ **Verwarringsrisico**: De boekhoudkundige verwerking verschilt sterk (vooral bij operationele leasing). Vergelijk altijd de totale cost-of-financing - niet enkel rente of leasingbedrag.
