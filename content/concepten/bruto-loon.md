---
title: "Bruto-loon"
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
gegenereerd_uit: "data/concepten/records/bruto-loon.json"
---

# Bruto-loon

_Regime_

📋 Regeling · Anchors: `2.2.taak.3` · Wave: `skeleton-cross-cutting-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: bruto bezoldiging · brutoloon

## Definitie

📖 Het bruto-loon is het volledige bedrag dat de werkgever contractueel verschuldigd is aan de werknemer voor zijn arbeidsprestaties, vóór inhouding van RSZ-werknemersbijdragen en bedrijfsvoorheffing. Het omvat het basisloon (uurloon × prestaties of vast maandloon), eventuele variabele componenten (commissies, premies, overuren) en voordelen in geld. Het bruto-loon is de berekeningsbasis voor zowel de sociale-zekerheidsbijdragen als voor de bedrijfsvoorheffing in de bruto-naar-netto-cascade.

<small>📚 Wet 3 juli 1978 betreffende de arbeidsovereenkomsten — art. 20 — _wettekst_ · WIB92 — art. 31 — _wettekst_</small>

## Substantie

🔗 Voor de werknemer is het bruto-loon de bovenkant van de loonstrook — het 'beloofde' loon volgens de arbeidsovereenkomst. Wat de werknemer effectief op zijn rekening krijgt (netto-loon) is significant lager: typisch 50-65 % van het bruto, afhankelijk van het loonniveau en de gezinssituatie. Voor de werkgever is het bruto-loon slechts een tussenstap: de totale loonkost ligt 25-30 % hoger door de werkgevers-RSZ. Het bruto-loon is dus de scharnier tussen werknemer-perspectief (loonstrook) en werkgever-perspectief (loonkost).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 Het bruto-loon bestaat als afzonderlijk concept omdat de loonkost in België gespreid wordt over drie betalers: de werknemer betaalt RSZ-werknemer en BV uit zijn bruto; de werkgever betaalt het bruto plus RSZ-werkgever; de overheid (RSZ + fiscus) int de bijdragen en voorheffingen. Het bruto-loon is het contractuele aanknopingspunt — wat in de arbeidsovereenkomst staat — en de wettelijke basis voor alle daaropvolgende berekeningen (BV, RSZ, vakantiegeld, opzegvergoeding, pensioen).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: Wet 3 juli 1978 (arbeidsovereenkomsten) + Loonbeschermingswet 12 april 1965 + WIB92 art. 31

**✅ Voor**
- 📖 Elke werknemer met een arbeidsovereenkomst (arbeider, bediende, handelsvertegenwoordiger). Het bruto-loon is steeds de berekeningsbasis voor RSZ en BV, ongeacht het statuut of de sector.

**🚫 Niet voor**
- 📖 Bedrijfsleidersbezoldigingen (zelfstandige bedrijfsleiders, art. 32 WIB92) — die volgen een ander regime zonder werknemers-RSZ. Voor bedrijfsleiders gelden enkel sociale-zekerheidsbijdragen voor zelfstandigen en BV op de bezoldiging.

**📋 Voorwaarden**
- 🔗 Het bruto-loon mag niet lager liggen dan (a) het sectorale baremaloon vastgesteld door CAO van het bevoegde paritair comité, (b) het gewaarborgd gemiddeld minimum maandinkomen (GGMMI) bij ontstentenis van een lagere sectorale CAO.

**▶️ Trigger start**
- 🔗 De verplichting tot uitbetaling ontstaat door de arbeidsprestatie — voor maandlonen typisch maandelijks ten laatste de 4e werkdag na de maand waarop het loon betrekking heeft (art. 9 Loonbeschermingswet).

## Bouwstenen

### 💡 Componenten van het bruto-loon  
_`begrip`_

🔗 Het bruto-loon omvat: (1) basisloon (uurloon of maandloon vastgelegd in de arbeidsovereenkomst, minimaal het sectorale barema); (2) variabele componenten — commissies, productiviteits-premies, overuren-toeslagen; (3) voordelen in geld — eindejaarspremie, dertiende maand, vakantiegeld (enkel + dubbel); (4) voordelen alle aard (bedrijfswagen, GSM) voor het deel dat als loon kwalificeert. Niet inbegrepen: terugbetaling van onkosten 'eigen aan de werkgever'.

<small>📚 WIB92 — art. 31 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📜 Sectoraal barema (CAO PC)  
_`regel`_

🔗 Elke werknemer valt onder een paritair comité (PC) — de sectorale CAO van dat PC bepaalt het minimum baremaloon per functieklasse en anciënniteits-trap. De werkgever mag een hoger loon toekennen, maar nooit lager dan het barema. Bij wijziging van functieklasse of bij overschrijding van een anciënniteits-trap moet het loon mechanisch worden aangepast.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚙️ Automatische indexering  
_`mechanisme`_

🔗 België kent een automatische loonindexering: wanneer de gezondheidsindex (afgevlakte gezondheidsindex) een spilindex overschrijdt, worden de lonen sectoraal verhoogd. De timing en formule verschilt per sector: sommige PC's hanteren maandelijkse indexering (bv. PC 200 — bedienden), andere jaarlijks (bv. PC 124 — bouw). De werkgever past de indexatie automatisch toe — de werknemer hoeft niets te doen.

<small>📚 Wet 3 juli 1978 betreffende de arbeidsovereenkomsten — art. 131 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚙️ Basis voor RSZ en BV  
_`mechanisme`_

🔗 Het bruto-loon dient als grondslag voor twee parallelle inhoudingen: (1) RSZ-werknemer (13,07 % van het bruto, met enkele uitzonderingen); (2) bedrijfsvoorheffing (BV) — progressief berekend volgens de schalen in het Cijferzakboekje, op basis van het belastbaar maandloon (bruto − RSZ-werknemer) en de gezinssituatie. De werkgever houdt beide bedragen in en stort ze door aan de RSZ respectievelijk de fiscus.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Voorbeelden

### 💡 Bediende — bruto-loon € 3.500/maand 🔗

_Sven, bediende bij Aurelia Holding NV, PC 200, alleenstaand zonder kinderen. Maandloon volgens arbeidsovereenkomst: 3.500 EUR bruto._

**Berekening:**
- Stap 1 — bruto-loon: 3.500,00 EUR
- Stap 2 — RSZ-werknemer (13,07 %): 3.500 × 13,07 % = 457,45 EUR
- Stap 3 — belastbaar loon: 3.500 − 457,45 = 3.042,55 EUR
- Stap 4 — bedrijfsvoorheffing (BV-schaal alleenstaande, indicatief): ≈ 725 EUR — exact bedrag in Cijferzakboekje opzoeken
- Stap 5 — netto-loon: 3.042,55 − ≈725 = ≈ 2.317 EUR
- Stap 6 — werkgevers-RSZ (≈ 25 %): 3.500 × 25 % = 875 EUR
- Stap 7 — totale loonkost werkgever: 3.500 + 875 = 4.375 EUR

→ **Resultaat**: Werknemer ontvangt ≈ 2.317 EUR netto; werkgever betaalt ≈ 4.375 EUR loonkost. Het bruto-loon van 3.500 EUR is het scharnierbedrag — exacte BV-bedragen via Cijferzakboekje.

**Boeking:**


<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Bruto-loon verwarren met loonkost werkgever

**Verkeerde assumptie**: Studenten denken dat 'het bruto-loon' het totale bedrag is dat de werkgever betaalt voor één werknemer.

**Kernpunt**: De loonkost werkgever ligt ≈ 25-30 % hoger dan het bruto-loon door de werkgevers-RSZ-bijdrage. Het bruto-loon is wat in de arbeidsovereenkomst staat én de berekeningsbasis voor RSZ + BV — niet de totale kost van de werkgever.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Sectoraal barema vergeten te checken

**Verkeerde assumptie**: Het loon dat in de arbeidsovereenkomst staat is automatisch geldig zolang beide partijen ermee instemmen.

**Kernpunt**: De CAO van het paritair comité (sectoraal barema) is bindend — een lager loon overeenkomen dan het barema is nietig en de werknemer kan het verschil terugvorderen. Eerst PC bepalen, dan barema-loon checken, dan pas effectief loon afspreken.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ RSZ-percentage uit het hoofd kennen vs Cijferzakboekje gebruiken

**Verkeerde assumptie**: 13,07 % en 25 % zijn exact in elke situatie.

**Kernpunt**: 13,07 % is de standaard werknemers-RSZ; werkgevers-RSZ varieert per sector en ondernemingsgrootte (basis ≈ 25 %, met sectorale toeslagen en eventuele structurele verminderingen — bv. doelgroepvermindering, lage-lonen-bonus). Bij het examen altijd het Cijferzakboekje raadplegen voor het exacte percentage.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Accountant-perspectieven

### Werkgever-cliënt (KMO met personeel)

_De accountant die de loonboekhouding van een KMO-cliënt voert of erop toeziet._

#### 📒 Boekhouder

##### 👣 Boeking bruto-loon in klasse 62  
_`stap`_

📖 Bij verwerking van de loonjournaal: het bruto-loon wordt geboekt op 620 (Bezoldigingen) of een sub-rekening per categorie (bv. 6201 directiepersoneel, 6202 administratief personeel). De werkgevers-RSZ komt op 621. Tegen-boekingen: 453 (ingehouden voorheffing BV), 454 (RSZ — totaal werknemer + werkgever), 455 (te betalen netto-loon). De maandelijkse loonjournaal wordt typisch door het sociaal secretariaat aangeleverd; de boekhouder controleert de splitsing en boekt.

<small>📚 CBN-advies 2016/15 — Vergoedingen aan bestuurders en werkende vennoten — Boekingen tijdens het boekjaar — _advies_</small>

#### 🧭 Adviseur

##### 🧭 Loonsverhoging vs alternatieve voordelen  
_`vuistregel`_

🔗 Bij vraag van werknemer of werkgever om het loon te verhogen: wijs op de hoge wig (≈ 50 % van elke euro bruto-loon gaat naar RSZ + BV). Alternatieven met lagere kost-naar-netto-verhouding: maaltijdcheques, ecocheques, groepsverzekering (2e-pijler pensioen), bedrijfsfiets, mobiliteitsbudget, warrants/aandelenopties. Elk alternatief heeft eigen voorwaarden en plafonds.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 🔍 Auditor

##### 👣 Volledigheids- en cut-off-controle payroll  
_`stap`_

🔗 Controleren of klasse 62 alle bezoldigingen omvat (volledigheid): aansluiting tussen sociaal-secretariaat-rapportering en grootboek, voldoende werknemers in loonlijst, geen ontbrekende maand. Cut-off: bezoldigingen december geboekt in december (provisie eindejaarspremie + provisie dubbel vakantiegeld voor het komende jaar). Substantief: steekproef arbeidsovereenkomsten + loonfiches 281.10 vs grootboek.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Loon-en-payroll K-techniek (cascade-context) → [[loon-en-payroll]] _(moet-verwijzen)_
- ↪ Werknemers-vergoedingen Σ (alternatieven) → [[werknemers-vergoedingen]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[loon-en-payroll]]
### `triggert`
- [[rsz-werknemer]] — Bruto-loon is grondslag voor RSZ-werknemer inhouding (13,07 %).
- [[rsz-werkgever]] — Bruto-loon is grondslag voor RSZ-werkgever bijdrage (≈ 25 %).
- [[bedrijfsvoorheffing]] — Belastbaar loon (bruto − RSZ-werknemer) is grondslag voor BV-berekening.
### `vergelijkbaar_met`
- [[bedrijfsleidersbezoldiging]]
    - **Gelijkenissen**:
        - Beide vormen beroepsinkomsten van een natuurlijke persoon
        - Beide worden onderworpen aan bedrijfsvoorheffing en personenbelasting
    - **Verschillen**:
        - Bruto-loon: werknemer met arbeidsovereenkomst — RSZ-werknemer 13,07 % + RSZ-werkgever 25 %
        - Bedrijfsleidersbezoldiging: zelfstandige bedrijfsleider — sociale bijdragen zelfstandigen (lager, afhankelijk van inkomen), geen werkgevers-RSZ
        - Boekhoudkundig: bruto-loon op 620; bedrijfsleidersbezoldiging op 618
    - ⚠️ **Verwarringsrisico**: Bij familiale vennootschappen is het soms onduidelijk of de bedrijfsleider ook 'als werknemer' werkt — fiscale en sociale herclassificatie mogelijk.
