---
title: "Aanvullende gemeentebelasting op de personenbelasting"
concept_type: "regime"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 2.7.II.B
tags:
  - concept
  - schema-2.2
  - type-regime
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/aanvullende-gemeentebelasting-pb.json"
---

# Aanvullende gemeentebelasting op de personenbelasting

_Regime_

📋 Regeling · Anchors: `2.7.II.B` · Wave: `skeleton-fiscaliteit-klein-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: gemeentelijke opcentiemen PB · AGB op PB

## Definitie

📖 De aanvullende gemeentebelasting op de personenbelasting is een belasting die gemeenten heffen als percentage opcentiemen op het federale PB-bedrag van hun inwoners. Elke gemeente bepaalt autonoom haar tarief tussen 0 % en 9 % (in de praktijk ligt het Belgisch gemiddelde rond 7 %). De aanslag wordt samen met de federale PB ingevorderd door de FOD Financiën en daarna doorgestort aan de gemeente (WIB92 art. 465-470/2).

<small>📚 WIB92 — art. 465 — _wettekst_ · WIB92 — art. 468 — _wettekst_</small>

## Substantie

🔗 Voor de belastingplichtige is dit een 'verdoken' opslag op zijn federale aanslag: een inwoner van een gemeente met 7 % aanvullende gemeentebelasting betaalt 7 % méér dan iemand met identieke inkomsten in een gemeente met 6 %. Op een gemiddelde PB-aanslag van 10.000 EUR is dat 100 EUR verschil per procentpunt. Praktisch effect: een 'tax-competitie' tussen gemeenten (vooral aan stadsranden) — sommige rijke gemeenten houden het tarief expliciet laag om hoge inkomens aan te trekken. De grondslag is de federale PB VÓÓR verrekening van voorheffingen — niet de werkelijk te betalen som.

<small>📚 WIB92 — art. 466 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 De ratio is institutioneel: gemeenten hebben grondwettelijke fiscale autonomie (art. 170 Grondwet) maar geen volledige fiscale ruimte; het 'piggy-back'-systeem op de federale PB is een efficiënte oplossing (gemeente moet geen eigen aangifte-apparaat opzetten, de FOD doet het werk). Voor de gemeente: een belangrijke inkomstenbron (na opcentiemen onroerende voorheffing). De keuze van het tarief is een politiek-budgettair instrument dat de lokale belastingdruk weerspiegelt.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: WIB92 art. 464-470/2 (federale machtigingskaders) + gemeentelijke reglementen (gemeenteraadsbeslissing)

Stabiel regime. Elke gemeente bepaalt het tarief jaarlijks bij beslissing van de gemeenteraad (vóór 31 januari of bij vaststelling van het begrotingsjaar).

**✅ Voor**
- 📖 Alle inwoners van een Belgische gemeente die personenbelasting verschuldigd zijn — de aanvullende gemeentebelasting wordt automatisch berekend op basis van de gemeente van fiscale woonplaats op 1 januari van het aanslagjaar.

**📋 Voorwaarden**
- 📖 (1) Belastingplichtige is rijksinwoner (art. 2 WIB92). (2) Gemeente heeft een belasting-reglement aangenomen door de gemeenteraad. (3) De PB is effectief verschuldigd — bij volledige vrijstelling van federale PB is er ook geen aanvullende gemeentebelasting.

**⛔ Uitsluitingen**
- 📖 Afzonderlijk belaste inkomsten (zoals roerende voorheffing op interesten/dividenden) zijn principieel uitgesloten van de aanvullende gemeentebelasting — die wordt enkel berekend op de gezamenlijk belaste inkomsten (Circulaire 2022/C/106). Dit is een belangrijk verschilpunt met de federale PB-aanslag.

## Bouwstenen

### 📏 Tarief 0-9 %  
_`drempel`_

🔗 Wettelijk maximum: niet wettelijk gefixeerd in vaste cap, maar in de praktijk schommelen gemeentelijke tarieven tussen 0 % (uitzonderlijk; bv. Knokke-Heist 0 %) en 9 % (uitschieters). Gemiddelde Belgische gemeente: ~7 %. Brussels Hoofdstedelijk Gewest: gemiddeld lager dan Vlaanderen (vaak 5-6 %). De gemeenteraad vastlegt jaarlijks het tarief.

<small>📚 WIB92 — art. 465 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 🧮 Berekeningsgrondslag  
_`formule`_

📖 AGB = federale PB op gezamenlijk belaste inkomsten × gemeentelijk tarief. De grondslag is de Staats-PB VÓÓR verrekening van voorheffingen en voorafbetalingen — niet de uiteindelijk te betalen som (WIB92 art. 466). Belangrijke voetnoot: de aanvullende gemeentebelasting volgt enkel de gezamenlijk belaste inkomsten — afzonderlijk belaste delen (RV op kapitalen, meerwaarden art. 90, ...) vallen erbuiten.

<small>📚 WIB92 — art. 466 — _wettekst_ · Circulaire 2022/C/106 — C. Aanvullende gemeentebelasting — _circulaire_</small>

### ⚙️ Gemeenschappelijke invordering door FOD Financiën  
_`mechanisme`_

📖 De FOD Financiën int de AGB samen met de federale PB op één aanslagbiljet en stort het bedrag door aan de gemeente. De gemeente hoeft geen eigen aangifte-, controle- of inningsapparaat — administratieve efficiëntie. WIB92 art. 470/2: 1 % inningskost wordt door FOD ingehouden voor de dienstverlening.

<small>📚 WIB92 — art. 470/2 — _wettekst_</small>

## Voorbeelden

### 💡 Berekening AGB voor gemeente met 7 % 🔗

_Belastingplichtige Aurelia, inwoner van een Vlaamse gemeente met 7 % AGB-tarief. Federale Staats-PB op gezamenlijk belaste inkomsten = 12.000 EUR. Roerende voorheffing op dividend (afzonderlijk belast) = 1.500 EUR._

**Berekening:**
- Stap 1 — grondslag AGB = federale PB op gezamenlijk belaste inkomsten = 12.000 EUR (de 1.500 EUR RV op dividend is afzonderlijk belast en valt erbuiten).
- Stap 2 — gemeentelijk tarief = 7 %.
- Stap 3 — AGB = 12.000 × 7 % = 840 EUR.
- Stap 4 — totale aanslag (federaal + gemeentelijk) = federale PB + 840 EUR (op één aanslagbiljet).

→ **Resultaat**: Als Aurelia in een gemeente met 6 % had gewoond: AGB = 720 EUR (120 EUR minder). De RV op dividend wordt enkel federaal afzonderlijk belast — geen 7 % AGB erop.

<small>📚 WIB92 — art. 466 — _wettekst_ · Circulaire 2022/C/106 — C. Aanvullende gemeentebelasting — _circulaire_</small>

## Valkuilen

### ⚠️ AGB toepassen op afzonderlijk belaste inkomsten

**Verkeerde assumptie**: De AGB van 7 % wordt op de TOTALE federale belasting toegepast, inclusief roerende voorheffing op dividenden en de afzonderlijk belaste delen.

**Kernpunt**: De AGB volgt enkel de gezamenlijk belaste inkomsten (Circulaire 2022/C/106). Roerende voorheffing op dividenden, interesten en meerwaarden art. 90 die afzonderlijk belast zijn, vallen erbuiten. Dit is een belangrijk verschilpunt — vooral relevant voor cliënten met aanzienlijk roerend inkomen.

<small>📚 Circulaire 2022/C/106 — C. Aanvullende gemeentebelasting — _circulaire_</small>

### ⚠️ Verwarring met 'gemeenten zonder PB-opcentiemen'

**Verkeerde assumptie**: Een gemeente met 0 % AGB heft helemaal geen lokale belasting.

**Kernpunt**: AGB op PB is slechts één van de gemeentelijke fiscale bronnen. Een gemeente met 0 % AGB compenseert dat typisch met andere belastingen: opcentiemen onroerende voorheffing, sui-generis gemeentebelastingen (huisvuil, drijfkracht, leegstand, ...). Totale belastingdruk vergelijken vereist ALLE gemeentelijke heffingen in rekening te brengen.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Accountant-perspectieven

### Particuliere cliënt (PB-aangifte)

_De accountant die de PB-aanslag becijfert._

#### 💰 Fiscaal adviseur

##### 👣 AGB meenemen in PB-simulatie  
_`stap`_

🔗 Bij elke PB-simulatie het AGB-tarief van de woonplaatsgemeente opzoeken (publiek beschikbaar via gemeentewebsite of FOD-databank) en toepassen op de federale PB om de werkelijk te verwachten totaalaanslag te tonen. Bij cliënten die overwegen te verhuizen: vergelijk de gecombineerde fiscale druk in verschillende gemeenten.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Personenbelasting cluster → [[personenbelasting]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[lokale-en-regionale-belastingen]]
### `beinvloed_door`
- [[personenbelasting]] — De grondslag van de AGB is de federale Staats-PB; wijzigingen in de PB-berekening werken automatisch door.
### `vergelijkbaar_met`
- [[gemeentelijke-opcentiemen-onroerende-voorheffing]]
    - **Gelijkenissen**:
        - Beide zijn opcentiemen-systemen op een hogere belasting
        - Beide gemeentelijk autonoom vastgelegd
    - **Verschillen**:
        - AGB-PB: op personenbelasting, gemiddeld 7 %, geheven door FOD Financiën
        - Opcentiemen OV: op onroerende voorheffing, vaak 700-2000+ opcentiemen, geheven door gewest (Vl) of de gemeente zelf
    - ⚠️ **Verwarringsrisico**: Beide worden in volkstaal vaak 'gemeentebelasting' genoemd — verschilpunt is de basisbelasting.
