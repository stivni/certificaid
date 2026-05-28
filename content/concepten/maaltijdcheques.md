---
title: "Maaltijdcheques"
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
gegenereerd_uit: "data/concepten/records/maaltijdcheques.json"
---

# Maaltijdcheques

_Regime_

📋 Regeling · Anchors: `2.2.taak.3` · Wave: `cluster-extract-werknemers-vergoedingen-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: elektronische maaltijdcheques · lunch-cheques

## Definitie

📖 Maaltijdcheques zijn een elektronisch betaalmiddel dat een werkgever aan werknemers of bedrijfsleiders verstrekt voor de aankoop van een eetmaal of verbruiksklare voeding. Het betreft een gemengde financiering: de werkgever draagt het grootste deel bij (maximum 6,91 EUR per cheque), de werknemer een minimum bijdrage (1,09 EUR per cheque, doorgaans verrekend via netto-loon-inhouding), waarbij de totale nominale waarde van de cheque maximum 8 EUR bedraagt. Mits cumulatieve voorwaarden van WIB92 art. 38/1 §2 zijn vervuld, is de werkgevers-tussenkomst vrijgesteld van personenbelasting (art. 38 — 25°) en van Rijksdienst voor Sociale Zekerheid (RSZ).

<small>📚 WIB92 — art. 38/1 §2 — 5° — _wettekst_ · WIB92 — art. 38/1 §2 — 6° — _wettekst_ · WIB92 — art. 38 — 25° — _wettekst_</small>

## Substantie

📖 Economisch is de maaltijdcheque de populairste 'extra-legale' verloningsvorm in België. Bij maximale uitkering (220 werkdagen × 6,91 EUR werkgevers-tussenkomst) levert dit ca. 1.520 EUR netto per jaar aan de werknemer — vrij van PB en RSZ. Voor de werkgever is enkel 2 EUR per cheque aftrekbaar in vennootschapsbelasting (VenB) (art. 53 — 14° WIB92); de overige werkgevers-tussenkomst (max 4,91 EUR per cheque) komt in de verworpen uitgaven (code 1215). Dit beperkt het werkgeversvoordeel maar maakt de cheques nog steeds significant voordeliger dan equivalente bruto-loonsverhoging.

<small>📚 WIB92 — art. 38/1 §2 — _wettekst_ · aangifte-VenB-2025-verworpen-uitgaven — code 1215 — _aangifte_</small>

## Rationale

🔗 De ratio legis is dubbel: (1) historisch een maaltijdvergoeding voor werknemers die zelf hun lunch organiseren in plaats van een bedrijfsrestaurant; (2) economische stimulus voor de horeca-/voedingssector via gerichte koopkracht. De wetgever beperkt het regime via plafonds (max 8 EUR nominaal), administratieve discipline (CAO of individuele overeenkomst, op naam, geldigheidsduur 12 maanden) en specifieke besteedbaarheid (alleen eetmaal of verbruiksklare voeding), zodat de cheques niet als sluikse loonsverhoging worden gebruikt.

<small>📚 WIB92 — art. 38/1 §2 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: WIB92 art. 38 — 25° + art. 38/1 §2 + KB 28-11-1969 (RSZ-uitvoering)

Elektronische vorm verplicht sinds 1 oktober 2015 (papieren cheques uitgedoofd). Plafondbedragen (6,91 EUR werkgevers-tussenkomst, 1,09 EUR werknemers-bijdrage) zijn nominaal vastgelegd in art. 38/1 §2 — niet jaarlijks geïndexeerd.

**✅ Voor**
- 📖 Elke werkgever die zijn werknemers of bedrijfsleiders een fiscaal voordelige maaltijdvergoeding wil bieden via een collectief systeem (CAO sectoraal of ondernemingsniveau) of een individuele overeenkomst.

**📋 Voorwaarden**
- 📖 Cumulatief (art. 38/1 §2): (1) toekenning vervat in CAO sectoraal/ondernemingsvlak OF in een geschreven individuele overeenkomst (gelijke regeling werknemers en bedrijfsleiders); (2) aantal cheques = aantal werkelijke arbeidsdagen; (3) cheque op naam; (4) geldigheidsduur max 12 maanden + enkel besteedbaar voor eetmaal of verbruiksklare voeding; (5) werkgevers-tussenkomst ≤ 6,91 EUR; (6) werknemersbijdrage ≥ 1,09 EUR.

**👍 Voordeel**
- 🔗 Voor werknemer: tot ca. 1.520 EUR netto/jaar volledig PB-vrij en RSZ-vrij. Voor werkgever: lagere loonwig dan equivalente bruto-loonsverhoging (geen RSZ-werkgever, gedeeltelijke VenB-aftrek). Eenvoudig systeem, geen prestatie-koppeling nodig.

**⚠️ Risico**
- 📖 Bij overschrijding van één voorwaarde (bv. ontbrekende CAO, te hoge werkgevers-tussenkomst, gebruik buiten voeding) vervalt de PB-vrijstelling voor het VOLLEDIGE bedrag — niet enkel het excedent. De cheque wordt dan integraal belastbaar loon (BV + RSZ + 100 % aftrekbaar bij werkgever zoals gewoon loon). Daarnaast: dubbele uitkering (cheque + cash-restaurant-vergoeding voor dezelfde dag) kan herkwalificatie aantrekken.

## Bouwstenen

### 📏 Plafond werkgevers-tussenkomst: 6,91 EUR per cheque  
_`drempel`_

📖 De werkgevers-tussenkomst in de maaltijdcheque mag maximum 6,91 EUR per cheque bedragen. Boven dit bedrag vervalt de PB-vrijstelling voor het volledige cheque-bedrag — niet enkel het excedent. Dit is een nominaal bedrag in WIB92 art. 38/1 §2 — 5°, niet geïndexeerd.

<small>📚 WIB92 — art. 38/1 §2 — 5° — _wettekst_</small>

### 📏 Minimum werknemersbijdrage: 1,09 EUR per cheque  
_`drempel`_

📖 De werknemer of bedrijfsleider moet minstens 1,09 EUR per cheque zelf bijdragen. Deze bijdrage wordt doorgaans verrekend via inhouding op het netto-loon. Onder dit minimum vervalt de PB-vrijstelling. Samen met het maximum werkgevers-tussenkomst van 6,91 EUR levert dit een totale cheque-waarde van max 8 EUR.

<small>📚 WIB92 — art. 38/1 §2 — 6° — _wettekst_</small>

### 📏 Aftrekbaarheid werkgever: 2 EUR per cheque (art. 53 — 14°)  
_`drempel`_

📖 Voor de werkgever is per maaltijdcheque slechts 2 EUR fiscaal aftrekbaar in vennootschapsbelasting (WIB92 art. 53 — 14°). Het verschil tussen de werkgevers-tussenkomst en die 2 EUR komt in de verworpen uitgaven (code 1215 in de VenB-aangifte). Bij maximale werkgevers-tussenkomst van 6,91 EUR is dus 4,91 EUR per cheque een verworpen uitgave.

<small>📚 WIB92 — art. 53 — 14° — _wettekst_ · aangifte-VenB-2025-verworpen-uitgaven — code 1215 — _aangifte_</small>

### 📜 Aantal cheques = aantal werkelijke arbeidsdagen  
_`regel`_

📖 Het aantal toegekende cheques moet exact gelijk zijn aan het aantal werkelijke arbeidsdagen (art. 38/1 §2 — 2°). Bij ziekte, verlof of werkloosheid geen cheque. Voor deeltijdsen pro rata. Een 'forfaitaire' maandelijkse uitkering los van werkelijke arbeidsdagen voldoet niet aan de voorwaarde en doet de vrijstelling vervallen.

<small>📚 WIB92 — art. 38/1 §2 — 2° — _wettekst_</small>

### 📜 Geldigheidsduur 12 maanden + reactiveringsmogelijkheid  
_`regel`_

📖 Elke elektronische maaltijdcheque heeft een geldigheidsduur van maximaal 12 maanden vanaf terbeschikkingstelling (art. 38/1 §2 — 4°). Niet-bestede cheques verlopen na die termijn — geld terug naar de werkgever. De werknemer of bedrijfsleider kan binnen 3 maanden na vervaldatum een eenmalige reactivering vragen bij de uitgever; de gereactiveerde cheque heeft dan een geldigheidsduur van 3 maanden.

<small>📚 WIB92 — art. 38/1 §2 — 4° — _wettekst_ · WIB92 — art. 38/1 §2 — _wettekst_</small>

## Voorbeelden

### 💡 Maandelijkse boeking maaltijdcheques bij Zelena Bio NV 🔗

_Zelena Bio NV heeft 50 werknemers. In oktober telt elk gemiddeld 22 arbeidsdagen. Werkgevers-tussenkomst = 6,91 EUR/cheque, werknemersbijdrage = 1,09 EUR/cheque (ingehouden via netto-loon). Totaal cheques: 50 × 22 = 1.100 cheques._

**Berekening:**
- Stap 1 — Totale waarde cheques uitgegeven door uitgever: 1.100 × 8 EUR = 8.800 EUR.
- Stap 2 — Werkgevers-tussenkomst: 1.100 × 6,91 = 7.601 EUR.
- Stap 3 — Werknemersbijdrage (ingehouden via netto-loon): 1.100 × 1,09 = 1.199 EUR.
- Stap 4 — Fiscale aftrek werkgever: 1.100 × 2 EUR = 2.200 EUR aftrekbaar.
- Stap 5 — Verworpen uitgave (code 1215 VenB-aangifte): 7.601 − 2.200 = 5.401 EUR.

→ **Resultaat**: Werkgever boekt 7.601 EUR personeelskost (waarvan 2.200 EUR fiscaal aftrekbaar en 5.401 EUR verworpen uitgave) + ontvangt 1.199 EUR ingehouden netto-loon van werknemers.

**Boeking:**


<small>📚 WIB92 — art. 38/1 §2 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 💡 Werknemersperspectief — Jan, bediende met 220 werkdagen/jaar 🔗

_Jan werkt voltijds bij Zelena Bio NV (220 werkdagen/jaar). Werkgevers-tussenkomst 6,91 EUR/cheque, werknemersbijdrage 1,09 EUR. Cheques worden via debit-card opgeladen._

**Berekening:**
- Stap 1 — Bruto-tussenkomst werkgever: 220 × 6,91 = 1.520 EUR/jaar — volledig vrij van PB en RSZ.
- Stap 2 — Eigen bijdrage Jan: 220 × 1,09 = 240 EUR/jaar (via netto-loon-inhouding).
- Stap 3 — Netto-equivalent: indien Zelena Bio dezelfde 1.520 EUR als bruto-loon zou geven, zou Jan netto ca. 760 EUR ontvangen (na ca. 50 % marginaal tarief PB + 13,07 % RSZ).
- Stap 4 — Voordeel via maaltijdcheques: ca. 760 EUR netto extra in handen.

→ **Resultaat**: Door maaltijdcheques in plaats van extra bruto-loon krijgt Jan ca. dubbel zoveel netto. Beperking: cheques zijn alleen voor eetmaal/verbruiksklare voeding besteedbaar, niet voor andere uitgaven.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Maandelijkse 'forfait' in plaats van per werkdag toekennen

**Verkeerde assumptie**: Een werkgever geeft elke maand 22 cheques aan elke werknemer, ongeacht effectief gewerkte dagen ('voor de eenvoud').

**Kernpunt**: Art. 38/1 §2 — 2° vereist dat het aantal cheques gelijk is aan het aantal werkelijke arbeidsdagen. Bij ziekte, verlof, deeltijds, werkloosheid: minder cheques. Een vaste 22-cheques-per-maand-formule maakt de hele uitkering belastbaar loon (PB + RSZ).

<small>📚 WIB92 — art. 38/1 §2 — 2° — _wettekst_</small>

### ⚠️ Vergeten dat 'PB-vrij' niet betekent 'volledig aftrekbaar werkgever'

**Verkeerde assumptie**: Studenten denken dat maaltijdcheques voor zowel werknemer als werkgever 'gratis' zijn.

**Kernpunt**: Voor de werkgever is slechts 2 EUR per cheque aftrekbaar (art. 53 — 14° WIB92). De rest van de werkgevers-tussenkomst (max 4,91 EUR per cheque) is verworpen uitgave (code 1215 VenB-aangifte). Bij 25 % VenB-tarief kost elke verworpen euro de vennootschap 25 cent extra belasting.

<small>📚 WIB92 — art. 53 — 14° — _wettekst_ · aangifte-VenB-2025-verworpen-uitgaven — code 1215 — _aangifte_</small>

### ⚠️ Werknemersbijdrage 'achterhouden' — niet inhouden

**Verkeerde assumptie**: Werkgever betaalt de volledige 8 EUR per cheque 'cadeau' (werknemersbijdrage 1,09 EUR niet ingehouden).

**Kernpunt**: Art. 38/1 §2 — 6° vereist dat de werknemersbijdrage minstens 1,09 EUR bedraagt. Indien niet werkelijk ingehouden, vervalt de vrijstelling. De inhouding moet zichtbaar zijn op de loonbrief: bruto-loon − netto-uitkering − werknemersbijdrage maaltijdcheques.

<small>📚 WIB92 — art. 38/1 §2 — 6° — _wettekst_</small>

## Accountant-perspectieven

### Werkgever-vennootschap

#### 💰 Fiscaal adviseur

##### 👣 Verworpen-uitgave-berekening (code 1215)  
_`stap`_

📖 In de VenB-aangifte rubriek 13 (code 1215): (werkgevers-tussenkomst totaal − 2 EUR × aantal cheques) komt in de verworpen uitgaven. Bv. bij 1.100 cheques × 6,91 EUR werkgevers-tussenkomst en 2 EUR/cheque aftrekbaar: verworpen uitgave = 1.100 × (6,91 − 2) = 5.401 EUR. Deze verworpen uitgave verhoogt het belastbaar resultaat in de VenB.

<small>📚 aangifte-VenB-2025-verworpen-uitgaven — code 1215 — _aangifte_ · WIB92 — art. 53 — 14° — _wettekst_</small>

#### 📒 Boekhouder

##### 👣 Maandelijkse boeking maaltijdcheques  
_`stap`_

🔗 Bij factuur uitgever (Edenred, Pluxee, Monizze): debet 623 Andere personeelskosten voor werkgevers-tussenkomst + 455 Bezoldigingen schuldig voor werknemersbijdrage (later via netto-loon-inhouding gecompenseerd), credit 440 Leveranciers voor de totale factuur. Bij betaling: debet 440 / credit 550 Bank. De werknemersbijdrage wordt op de loonafrekening van de werknemer als netto-inhouding zichtbaar gemaakt.

<small>📚 KB 21.10.2018 — Minimum Algemeen Rekeningstelsel — Klasse 6 — 623 Andere personeelskosten — _kb_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Werknemer-loon (alternatief) → [[loon-en-payroll]] _(moet-verwijzen)_
- ↪ Andere cheques (vergelijking) → [[ecocheques]] _(mag-verwijzen)_
- ↪ Geschenken-aan-werknemers (vergelijking) → [[geschenken-aan-werknemers]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[werknemers-vergoedingen]]
### `vergelijkbaar_met`
- [[ecocheques]]
    - **Gelijkenissen**:
        - Beide cheques onder art. 38/1 WIB92 — voorwaarden CAO of individuele overeenkomst, op naam, geldigheidsduur
        - Beide PB-vrij + RSZ-vrij voor werknemer onder voorwaarden
    - **Verschillen**:
        - Maaltijdcheques: max 8 EUR nominaal · max 6,91 EUR werkgevers-tussenkomst + min 1,09 EUR werknemersbijdrage · alleen voor eetmaal/voeding · 12 maanden geldig · 2 EUR/cheque aftrekbaar werkgever
        - Ecocheques: max 10 EUR nominaal · max 250 EUR/jaar/werknemer · alleen voor ecologische producten/diensten (CAO 98-lijst NAR) · 24 maanden geldig · volledig verworpen uitgave werkgever
    - ⚠️ **Verwarringsrisico**: Studenten verwarren plafonds en aftrekbaarheid. Maaltijdcheques zijn deels aftrekbaar (2 EUR/cheque), ecocheques níét. Geldigheidsduren verschillen (12 vs 24 maanden).
