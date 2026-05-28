---
title: "Forfaitaire onkostenvergoeding"
concept_type: "regime"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 2.2.taak.3
tags:
  - concept
  - schema-2.2
  - type-regime
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/forfaitaire-onkostenvergoeding.json"
---

# Forfaitaire onkostenvergoeding

_Regime_

📋 Regeling · Anchors: `2.2.taak.3` · Wave: `cluster-extract-werknemers-vergoedingen-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: kostenforfait · onkostenvergoeding · kosten eigen aan de werkgever · KEW

## Definitie

📖 Een forfaitaire onkostenvergoeding is een vast bedrag dat een werkgever periodiek (meestal maandelijks) aan een werknemer of bedrijfsleider toekent als terugbetaling van kosten die deze maakt vóór rekening van de werkgever — typisch verplaatsingen, parking, kleine bureaukosten, representatie, verblijfskosten op zending. Indien correct opgezet, is de vergoeding niet belastbaar in hoofde van de werknemer (geen loon — artikel 31 in fine WIB92) en volledig aftrekbaar bij de werkgever (artikel 49 WIB92). Het regime wordt door de fiscus aanvaard mits cumulatief: (1) een redelijke forfaitaire raming gebaseerd op normen of een dossier per kosten-categorie, en (2) de vergoeding dient werkelijk ter dekking van kosten die de werkgever anders zelf had moeten dragen.

<small>📚 WIB92 — art. 31, in fine — _wettekst_ · WIB92 — art. 32/1 — _wettekst_ · WIB92 — art. 49 — _wettekst_</small>

## Substantie

🔗 Economisch: de forfaitaire onkostenvergoeding levert dezelfde netto-euro aan de werknemer als ca. 1,75 EUR bruto-loon zou doen (geen RSZ, geen bedrijfsvoorheffing) en kost de werkgever maar ca. 0,75 EUR na vennootschapsbelasting (volledig aftrekbaar zonder RSZ-bijdrage). Dat is structureel goedkoper dan elke andere verloningsvorm — vandaar de aantrekkingskracht én de bijzondere aandacht van de fiscus. De praktijk: bedrijven werken met een onkosten-policy (per functie-categorie een vast maandbedrag, opgesplitst in deelposten: kantoor-thuis, autoparking, kleine onkosten, lunch onderweg). Wie een ruling aanvraagt bij de Dienst Voorafgaande Beslissingen krijgt rechtszekerheid voor ca. 5 jaar.

<small>📚 WIB92 — art. 31, in fine — _wettekst_ · WIB92 — art. 49 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 Het regime vermijdt dat de werknemer kosten die de werkgever uiteindelijk draagt, persoonlijk moet voorschieten en achteraf detail-bonnetjes moet indienen. Het forfait is administratief efficiënt voor kleine, recurrente, moeilijk te documenteren kosten (postzegels, koffie op vergadering, parking-tickets). De anti-misbruik-eis (redelijke raming + werkelijke bestemming) bewaakt dat het regime niet wordt gebruikt om loon te 'omzetten' in vrijgestelde vergoedingen — wat de RSZ- en PB-grondslag zou uithollen. Het bewijs ligt bij de werkgever (art. 49 WIB92).

<small>📚 WIB92 — art. 49 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: WIB92 art. 31 + 32/1 + 49; administratieve commentaar (Com. IB) nrs. 31/35 e.v.

**✅ Voor**
- 🔗 Werknemers of bedrijfsleiders die in hun functie kosten maken vóór rekening van de werkgever (verplaatsingen, parking, kleine bureaukosten, representatie, zendingen). Vooral handig wanneer de kosten klein, frequent en moeilijk individueel te documenteren zijn.

**🚫 Niet voor**
- 📖 Pure 'loonomzetting' waarbij de werkgever cash-loon vervangt door een onkostenforfait zonder reëel kostenverhaal. Ook niet voor kosten die de werknemer maakt voor eigen rekening (woon-werkverkeer is hierop een uitzondering: art. 38 — 9° WIB92 voorziet een specifieke vrijstelling tot maximum 250 EUR per jaar voor woon-werk met privévervoer voor werknemers die het forfait beroepskosten kiezen).

**📋 Voorwaarden**
- 📖 Cumulatief: (1) forfait is redelijk geraamd op basis van een dossier (onkosten-policy, statistieken, ruling); (2) bedragen blijven in lijn met administratieve normen (geactualiseerde Comm. IB-bedragen of FOD-richtbedragen voor specifieke categorieën); (3) de werkgever houdt een dossier bij dat aantoont welke kosten het forfait dekt; (4) vermelding op de fiche 281.10 (werknemer) of 281.20 (bedrijfsleider) is doorgaans vereist.

**👍 Voordeel**
- 🔗 Hoogste netto-rendement per euro werkgeverskost — vrij van PB (werknemer), vrij van Rijksdienst voor Sociale Zekerheid (RSZ) werknemer en werkgever, 100 % aftrekbaar in vennootschapsbelasting (VenB). Administratief licht voor recurrente kleine kosten.

**⚠️ Risico**
- 📖 Herkwalificatie tot belastbaar loon bij gebrekkig dossier of onredelijk hoog forfait — met retroactieve bedrijfsvoorheffing, RSZ-rechtzetting en boetes. Bij geheime commissielonen (art. 219 WIB92) zelfs 100 %-bijzondere aanslag bovenop de gewone VenB. De werkgever draagt het volledige bewijslast-risico (art. 49 WIB92).

## Bouwstenen

### 📜 Dubbele bewijslast: redelijkheid + werkelijke bestemming  
_`regel`_

📖 Voor elke forfaitaire onkostenvergoeding moet de werkgever twee zaken kunnen bewijzen: (1) dat het forfait op redelijke gronden geraamd is — d.w.z. gebaseerd op statistieken, onderzoek of administratieve normen, niet uit de losse pols; (2) dat de vergoeding werkelijk dient ter dekking van kosten die normaal de werkgever zou hebben gedragen. Een onkosten-policy + ruling DVB is de zekerste opzet. Zonder dossier herkwalificeert de fiscus de vergoeding tot loon.

<small>📚 WIB92 — art. 49 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 💡 Typische kostencategorieën onder het forfait  
_`begrip`_

🔗 De fiscus aanvaardt typisch volgende categorieën als 'eigen kosten van de werkgever': (a) thuiskantoor-vergoeding voor structureel telewerk (orde van grootte ca. 154 EUR/maand sinds Covid-circulaire, geïndexeerd); (b) kleine onkosten (postzegels, koffie, snacks bij klant); (c) parking en kleine vervoerskosten; (d) representatie- en verblijfskosten op zending (verblijfsvergoeding binnenland ca. 20,75 EUR/dag, buitenland volgens landenlijst FOD BuiZa); (e) carwash en kleine autokosten. Elke categorie heeft eigen administratieve referentie-bedragen — exacte cijfers raadplegen via Cijferzakboekje of recente circulaire.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ↪️ Specifiek regime: vergoeding buitenlandse dienstreis (art. 38 — 2°)  
_`uitzondering`_

📖 Voor sommige specifieke vergoedingen voorziet WIB92 art. 38 expliciete plafonds. Bv. art. 38 — 2°: voor forfaitaire onkostenvergoedingen van zekere mandatarissen mag het bedrag niet hoger zijn dan 70 EUR per dag (eventueel verhoogd met max 20 EUR werkelijke verplaatsingskosten); bij overschrijding van die plafonds vervalt de vrijstelling voor het volledige bedrag. Deze art. 38-plafonds zijn aparte uitzonderingsregimes naast het algemene regime van 'kosten eigen aan de werkgever' onder art. 31/49.

<small>📚 WIB92 — art. 38 — 2° — _wettekst_</small>

### 🧭 Ruling-aanvraag Dienst Voorafgaande Beslissingen  
_`vuistregel`_

🔗 Voor structurele forfaits (bv. een full-package thuiskantoor + autoparking + representatie voor managers) is een ruling-aanvraag bij de Dienst Voorafgaande Beslissingen (DVB) sterk aan te raden. De ruling bevriest het regime voor doorgaans 5 jaar mits feitelijke situatie ongewijzigd blijft, en geeft rechtszekerheid bij latere controle. Argumentatie in de aanvraag: functie-omschrijving, kostencategorieën met statistische onderbouwing, vergelijking met andere geruliede dossiers in de sector.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Voorbeelden

### 💡 Thuiskantoor-vergoeding bij Zelena Bio NV 🔗

_Zelena Bio NV biedt al haar bedienden 3 dagen per week structureel telewerk aan. De accountant adviseert om een thuiskantoor-vergoeding te installeren conform de circulaire 2021/C/20 (Covid-stelsel, sindsdien permanent gemaakt)._

**Berekening:**
- Stap 1 — Vaststellen functie + structureel telewerk-volume (≥ 5 dagen/maand): ja, alle bedienden.
- Stap 2 — Bedrag bepalen volgens circulaire (orde van grootte 154,74 EUR/maand vanaf 2024 — actueel bedrag in Cijferzakboekje).
- Stap 3 — Vastleggen in policy 'Telewerk-vergoeding Zelena Bio NV' + addendum aan arbeidsovereenkomst.
- Stap 4 — Vermelding op fiche 281.10 (rubriek 'Kosten eigen aan de werkgever — forfait').
- Stap 5 — Maandelijkse boeking: debet 623 Andere personeelskosten 154,74 EUR, credit 455 Bezoldigingen schuldig.

→ **Resultaat**: Werknemer ontvangt 154,74 EUR netto bovenop loon (geen PB, geen RSZ); Zelena Bio betaalt 154,74 EUR + 0 RSZ-werkgever; volledige bedrag is aftrekbaar in VenB. Netto-kost na VenB-aftrek voor Zelena bedraagt ca. 115 EUR (bij 25 % VenB-tarief).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 💡 Mislukte loonomzetting — Aurelia Holding NV 🔗

_Aurelia Holding NV wil het bruto-maandloon van een commerciële directeur verlagen met 800 EUR en compenseren via 800 EUR/maand 'forfaitaire onkostenvergoeding'. Geen dossier, geen ruling. De fiscus controleert na 3 jaar._

**Berekening:**
- Stap 1 — Fiscus eist dossier (onkosten-policy, statistieken, bonnen-staal): Aurelia kan niets voorleggen.
- Stap 2 — Herkwalificatie 800 EUR/maand × 36 maanden = 28.800 EUR + 5.376 EUR woonwerk-component → belastbaar loon retroactief.
- Stap 3 — Werkgeversrechtzetting: bedrijfsvoorheffing achterstallig + RSZ-werkgever (ca. 25 %) + RSZ-werknemer (13,07 %) op de geherkwalificeerde bedragen.
- Stap 4 — Werknemersrechtzetting: belastbaar inkomen verhoogd → bijkomende PB tegen marginaal tarief (ca. 50 %).
- Stap 5 — Totale meerkost: ca. 60 % van 28.800 EUR ≈ 17.000 EUR + boetes + nalatigheidsinteresten.

→ **Resultaat**: De 'optimalisatie' kost Aurelia + werknemer samen ca. 17.000 EUR aan rechtzettingen, plus reputatieschade en mogelijk geheime-commissielonen-aanslag (100 %) als de fiscus het kwaadwillig acht.

<small>📚 WIB92 — art. 49 — _wettekst_ · WIB92 — art. 219 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ 'Het is forfaitair, dus geen bewijs nodig' — fout

**Verkeerde assumptie**: Het 'forfait' staat in de naam, dus de werkgever hoeft de kosten niet te bewijzen — een rond getal volstaat.

**Kernpunt**: Forfaitair betekent: niet per individuele kost gedocumenteerd, maar wél op basis van een redelijk dossier (statistieken, policy, ruling). De werkgever draagt de bewijslast voor BEIDE poten: (a) redelijkheid van het bedrag én (b) werkelijke bestemming voor kosten van de werkgever (art. 49 WIB92).

<small>📚 WIB92 — art. 49 — _wettekst_</small>

### ⚠️ Forfait gebruiken om netto-loon op te krikken

**Verkeerde assumptie**: Een werkgever wil de werknemer een hoger netto bieden zonder bruto-loon te verhogen, dus 'splitst' het loon in cash + onkosten.

**Kernpunt**: Pure loonomzetting (geen extra kosten gemaakt, alleen bruto verschoven naar 'forfait') wordt door de fiscus geherkwalificeerd — met retroactieve PB + RSZ + boete. Het forfait mag enkel kosten dekken die de werknemer effectief maakt vóór rekening van de werkgever en moet evenredig zijn met de functie.

<small>📚 WIB92 — art. 31 — _wettekst_ · WIB92 — art. 32/1 — _wettekst_</small>

### ⚠️ Vergeten dat forfait + werkelijke kostenvergoeding niet cumulatief is voor dezelfde kost

**Verkeerde assumptie**: Een werknemer krijgt 200 EUR/maand forfaitaire parking-vergoeding én dient ook elke parking-bon individueel in voor terugbetaling.

**Kernpunt**: Dubbele compensatie van dezelfde kost = verboden — ofwel het forfait dekt die kostencategorie en de individuele bonnen vervallen, ofwel de werkgever vergoedt op basis van bonnen. Vermenging maakt het forfait kwetsbaar voor herkwalificatie (de fiscus zal het forfait zien als loon omdat de werkelijke kost al apart vergoed is).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Accountant-perspectieven

### Werkgever (vennootschap)

#### 🧭 Adviseur

##### 👣 Onkosten-policy + ruling-aanvraag  
_`stap`_

🔗 Voor elke functie-categorie (manager, commercieel, technisch, thuiswerker): (1) inventariseer de kosten die de werknemer effectief maakt vóór rekening van de werkgever; (2) onderbouw de forfait-bedragen per categorie met statistieken (vergelijking met sectorale benchmarks, FOD-richtbedragen, oudere ruling-precedenten); (3) leg de policy vast in een bedrijfsdocument + addenda aan arbeidsovereenkomsten; (4) voor grote of complexe pakketten: ruling-aanvraag bij Dienst Voorafgaande Beslissingen voor 5-jaars rechtszekerheid.

<small>📚 WIB92 — art. 49 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 💰 Fiscaal adviseur

##### 👣 Vermelding op fiche 281.10/281.20  
_`stap`_

📖 De forfaitaire onkostenvergoeding moet op de fiche 281.10 (werknemer) of 281.20 (bedrijfsleider) worden vermeld in de specifieke rubriek 'Kosten eigen aan de werkgever — forfait'. Vermelding is verplicht voor aftrekbaarheid bij de werkgever (art. 57 WIB92) en om de bijzondere aanslag geheime commissielonen (art. 219 WIB92, 100 %) te vermijden. De code zelf op de fiche signaleert aan de fiscus dat het GEEN belastbaar loon is voor de werknemer.

<small>📚 WIB92 — art. 57 — _wettekst_ · WIB92 — art. 219 — _wettekst_</small>

#### 📒 Boekhouder

##### 👣 Boekingstechniek  
_`stap`_

🔗 Maandelijks: debet 623 Andere personeelskosten (of 615 Diensten en diverse goederen — Onkosten personeel, afhankelijk van rekeningstelsel) voor het forfait-bedrag, credit 455 Bezoldigingen schuldig (of rechtstreeks 550 Bank bij directe overschrijving). Geen RSZ-boeking nodig (vrij). Geen bedrijfsvoorheffings-boeking nodig (vrij). Bij jaareinde: controle dat alle forfaits ook op de fiche 281.10 zijn opgenomen.

<small>📚 KB 21.10.2018 — Minimum Algemeen Rekeningstelsel — Klasse 6 — 623 Andere personeelskosten — _kb_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Werknemer-loon (afbakening) → [[loon-en-payroll]] _(moet-verwijzen)_
- ↪ Bedrijfsleider-bezoldigingsmix → [[bedrijfsleidersbezoldiging]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[werknemers-vergoedingen]]
### `vergelijkbaar_met`
- [[loon-en-payroll]]
    - **Gelijkenissen**:
        - Beide zijn werkgever → werknemer geldstromen
        - Beide worden op de fiche 281.10 vermeld
    - **Verschillen**:
        - Loon = belastbaar bij werknemer (PB + RSZ), 100 % aftrekbaar bij werkgever
        - Forfaitaire onkostenvergoeding = niet belastbaar bij werknemer (geen PB, geen RSZ), 100 % aftrekbaar bij werkgever
        - Loon = compensatie voor prestaties; forfait = terugbetaling van kosten die werkgever zou dragen
    - ⚠️ **Verwarringsrisico**: Studenten verwarren forfaitaire onkostenvergoeding met cash-loon omdat beide periodiek worden uitbetaald aan dezelfde werknemer. De juridische natuur verschilt fundamenteel: prestatievergoeding vs kostenterugbetaling.
