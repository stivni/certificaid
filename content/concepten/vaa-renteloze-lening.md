---
title: "VAA — renteloze of goedkope lening"
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
gegenereerd_uit: "data/concepten/records/vaa-renteloze-lening.json"
---

# VAA — renteloze of goedkope lening

_Regime_

📋 Regeling · Anchors: `2.2.taak.3` · Wave: `skeleton-cross-cutting-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: VAA lening · rekening-courant-VAA · RC-zaakvoerder-VAA — **Vertalingen**: fr: ATN prêt sans intérêt

## Definitie

🔗 Wanneer een werkgever of vennootschap aan een werknemer of bedrijfsleider een renteloze of goedkope lening verstrekt — d.w.z. een lening tegen een rente die lager is dan de marktrente — vormt het verschil een belastbaar voordeel van alle aard (VAA). Het VAA wordt forfaitair berekend als: openstaand kapitaal × (referentierentevoet − werkelijk betaalde rente). De referentierentevoeten worden jaarlijks bij KB vastgesteld (KB/WIB92 art. 18 §3) en verschillen naargelang het soort lening: hypothecaire vs niet-hypothecaire lening, vaste vs variabele rente. Het meest courante toepassingsgeval is de negatieve rekening-courant van een zaakvoerder bij zijn vennootschap.

<small>📚 KB/WIB92 — art. 18 §3 — _kb_ · WIB92 — art. 36 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Substantie

🔗 Praktisch komt dit vooral voor bij bedrijfsleiders die meer uit hun vennootschap halen dan ze als bezoldiging of dividend uitkeren — de schuld 'in rekening-courant' is dan economisch een lening van de vennootschap aan de bedrijfsleider. Zonder bezoldigings-VAA-correctie zou dit een lege fiscale gunst zijn (geld nemen zonder fiscaal effect). Het KB-systeem belast forfaitair een marktrente — meestal hoger dan wat de zaakvoerder werkelijk zou betalen. Het werkelijk overgemaakte bedrag (of het saldo per einde maand × dagen / 365) maal de referentievoet vormt de berekenings­basis. Voor 2026 ligt de niet-hypothecaire vaste-rente-referentievoet rond 6–7 %, hypothecair fors lager (gewoonlijk in de buurt van de marktrente — ongeveer 2–4 % afhankelijk van duurtijd).

<small>📚 KB/WIB92 — art. 18 §3 — _kb_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🤖 De referentievoet vangt de gedachte op dat 'gratis kapitaal lenen' een economisch voordeel is — niet zelfanders dan een bezoldiging in natura. Door een vaste forfaitaire voet te gebruiken vermijdt de wetgever discussies over wat de 'werkelijke' marktrente voor een specifieke lening zou zijn. De ratio is anti-misbruik: zonder het VAA-regime zou een bedrijfsleider zijn winst in feite onbeperkt kunnen omtoveren tot rente-loze schulden, wat ineens een verkapte uitkering wordt.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · sinds **2026-01-01** · basis: KB/WIB92 art. 18 §3 + jaarlijks KB met percentages

De referentievoeten worden jaarlijks bij KB vastgesteld op basis van OLO + opslag. Stabiel principe sinds decennia; exacte percentages variëren met de markt.

**✅ Voor**
- 📖 Lening van vennootschap of werkgever aan een natuurlijke persoon (werknemer of bedrijfsleider) tegen géén of lagere rente dan de jaarlijkse referentievoet (KB/WIB92 art. 18 §3). Inclusief debet-rekening-courant van bedrijfsleider (vennootschap heeft tegoed op zaakvoerder).

**🚫 Niet voor**
- 🔗 Lening tegen marktrente of HOGER dan referentievoet — geen voordeel, geen VAA. Een bedrijfsleider die zijn rekening-courant aan ≥ referentievoet rente vergoedt, ontsnapt aan VAA-belasting (maar interestopbrengsten zijn belastbaar als roerend inkomen in PB).
- 🔗 Lening tussen onafhankelijke partijen (bank, externe schuldeiser) of een lening waarbij het rentegevoel marktconforme rente betaalt aan een derde. Het VAA-regime geldt enkel binnen de werknemer/werkgever- of bedrijfsleider/vennootschap-relatie.

## Bouwstenen

### 📜 Categorieën referentierentevoeten  
_`regel`_

📖 KB/WIB92 art. 18 §3 onderscheidt vier categorieën met elk een eigen referentievoet: (1) Hypothecaire lening met vaste rente; (2) Hypothecaire lening met variabele rente; (3) Niet-hypothecaire lening met vaste looptijd; (4) Niet-hypothecaire lening zonder vaste looptijd (= klassiek rekening-courant zaakvoerder). De niet-hypothecaire voet zonder vaste looptijd is doorgaans de hoogste (cijfer 2026: orde van grootte 6–7 %) — net om RC-zaakvoerder fiscaal te ontmoedigen.

<small>📚 KB/WIB92 — art. 18 §3 — _kb_</small>

### 🧮 Formule VAA renteloze lening  
_`formule`_

🔗 VAA = gemiddeld openstaand kapitaal over het jaar × (referentievoet − werkelijke aangerekende rente). Het gemiddelde wordt berekend op het rekening-courant-saldo per einde maand (Σ saldi / 12). Bij wisselend kapitaal: lineaire interpolatie of dagberekening. Resultaat: het verschil 'gemist aan rente' wordt als bezoldiging toegevoegd op de fiche 281 van de begunstigde.

<small>📚 KB/WIB92 — art. 18 §3 — _kb_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚙️ Klassieke toepassing — rekening-courant zaakvoerder  
_`mechanisme`_

🔗 Bij een rekening-courant met debet-saldo (zaakvoerder schuldt aan de vennootschap) wordt de niet-hypothecaire voet zonder vaste looptijd toegepast (categorie 4). Boekhoudkundig: rekening 416 'Vorderingen op aandeelhouders' (D, vordering vennootschap op zaakvoerder). Wordt geen rente aangerekend? Volledig VAA op die referentievoet. Wordt deel-rente aangerekend (bv. 2 % terwijl referentievoet 6,5 %)? VAA op het verschil van 4,5 %.

<small>📚 KB/WIB92 — art. 18 §3 — _kb_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚙️ Boekhoudkundige verwerking rente RC  
_`mechanisme`_

🔗 Indien de vennootschap wél rente aanrekent op de RC (best practice om VAA te vermijden of te minimaliseren): vordering rente op 416 (D) tegenover opbrengst 751 'Opbrengsten uit vlottende activa' (C). De zaakvoerder ontvangt fiche 281.50 voor interesten als roerend inkomen — onderworpen aan 30 % roerende voorheffing in zijn PB (categorie roerende inkomsten). VAA op het verschil tussen referentievoet en aangerekende rente komt op fiche 281.20 (bedrijfsleider) bij bezoldigingen — onderworpen aan PB-progressie + 13,07 % RSZ niet (bedrijfsleider zonder dienstverband).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Voorbeelden

### 💡 Negatieve rekening-courant zaakvoerder Pieter — 50.000 EUR 🔗

_Pieter heeft als zaakvoerder van Aurelia Holding NV een gemiddeld openstaand rekening-courant-debet-saldo van 50.000 EUR over het hele jaar 2026. De vennootschap rekent géén rente aan. Stel: referentievoet niet-hypothecair zonder vaste looptijd 2026 = 6,5 % (illustratief — exact uit Cijferzakboekje)._

**Berekening:**
- Stap 1 — Gemiddeld saldo = 50.000 EUR over 12 maanden
- Stap 2 — Referentievoet 2026: 6,5 % (illustratief, opzoeken in Cijferzakboekje)
- Stap 3 — VAA = 50.000 × (6,5 % − 0 %) = 3.250 EUR
- Stap 4 — Op fiche 281.20 van Pieter: bezoldigingen + 3.250 EUR VAA
- Stap 5 — Belasting bij marginaal 50 % + gemeente: ~1.700 EUR netto PB-impact
- Stap 6 — Vergelijk: zou Pieter 6,5 % vrijwillig betalen → 3.250 EUR rente aan vennootschap (= aanvullende winst → 25 % VenB → ~813 EUR vennootschapsbelasting) + Pieter geen VAA. Soms gunstiger om wel rente aan te rekenen.

→ **Resultaat**: Door géén rente aan te rekenen bespaart de vennootschap 0 EUR; Pieter draagt ~1.700 EUR PB-meerprijs. Optimalisatie-overweging: matig rente aanrekenen tot ~75 % van referentievoet, of regulariseren via dividend.

**Boeking:**


<small>📚 KB/WIB92 — art. 18 §3 — _kb_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Werkelijke marktrente gebruiken in plaats van KB-referentievoet

**Verkeerde assumptie**: Studenten denken dat het VAA = openstaand kapitaal × (huidige marktrente − werkelijke rente).

**Kernpunt**: Het VAA gebruikt steeds de FORFAITAIRE referentievoet uit het jaarlijks KB (KB/WIB92 art. 18 §3), niet een 'echte' marktrente die de zaakvoerder elders zou kunnen krijgen. Cijferzakboekje raadplegen voor het exacte percentage per categorie en per AJ.

<small>📚 KB/WIB92 — art. 18 §3 — _kb_</small>

### ⚠️ VAA op brutosaldo i.p.v. gemiddeld saldo

**Verkeerde assumptie**: VAA = eindsaldo RC × referentievoet.

**Kernpunt**: Niet op het eindsaldo maar op het GEMIDDELD openstaand kapitaal over het jaar — typisch berekend als gemiddelde van de maand-einde-saldi. Een zaakvoerder die zijn RC vlak voor jaareinde 'aflost' om dan kort daarna weer op te nemen, ontsnapt niet aan VAA: het hele jaar telt mee.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Rente aanrekenen = altijd voordeliger dan VAA betalen

**Verkeerde assumptie**: Het is altijd beter om rente aan te rekenen op de RC dan VAA te dragen — zo loopt het probleem weg.

**Kernpunt**: De afweging is niet eenduidig. Rente aanrekenen genereert een belastbare opbrengst bij de vennootschap (25 % VenB) + 30 % roerende voorheffing bij de zaakvoerder. Dat is een totaal van 47,5 % belasting op die rente. VAA daarentegen wordt belast aan de marginale PB-voet van de zaakvoerder + gemeente, doorgaans 53–55 %. Het verschil kan klein zijn; bij hoge marginale PB-voeten is rente aanrekenen iets gunstiger.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Accountant-perspectieven

### Vennootschap met rekening-courant zaakvoerder

_De accountant die de jaarafsluiting van een KMO-vennootschap met een actieve RC-zaakvoerder doet._

#### 📒 Boekhouder

##### 👣 Maandelijkse opvolging RC-saldi  
_`stap`_

🔗 Houd elk maand het eindsaldo van rekening 416 'Vorderingen op aandeelhouders' bij. Op jaarafsluiting: bereken het gemiddeld saldo (Σ maand-einde-saldi / 12). Vermenigvuldig met de referentievoet (jaarlijks KB) min de werkelijk aangerekende rente → VAA-bedrag. Toevoegen aan fiche 281.20 voor de bedrijfsleider.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 🧭 Adviseur

##### 🧭 Afbouw-strategie negatieve RC  
_`vuistregel`_

🔗 Bij chronisch negatieve RC: drie afbouwstrategieën — (1) bezoldiging optrekken (cash bezoldiging → vermindering schuld op 416); (2) dividend uitkeren (compensatie tegen schuld); (3) rente aanrekenen aan minstens de referentievoet (vermijdt VAA maar genereert rente-opbrengst vennootschap + RV bij zaakvoerder). Combineren is vaak optimaal: lichte rente + jaarlijkse bezoldigingsverhoging.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Bedrijfsleider-bezoldigingsmix (overkoepelende advies-context) → [[bedrijfsleidersbezoldiging]] _(moet-verwijzen)_
- ↪ Werknemer-loon → [[loon-en-payroll]] _(mag-verwijzen)_
- ↪ Rekening-courant-zaakvoerder boekhoudkundig _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[werknemers-vergoedingen]]
### `vereist`
- [[bedrijfsleidersbezoldiging]] — Klassieke toepassing in de bezoldigingsmix van bedrijfsleiders — niet enkel cash + dividenden maar ook de RC-positie speelt mee.
### `vergelijkbaar_met`
- [[vaa-pc-en-communicatie]]
    - **Gelijkenissen**:
        - Beide forfaitaire VAA's onder KB/WIB92 art. 18 §3
        - Beide leiden tot fiche-vermelding op 281.10 of 281.20
    - **Verschillen**:
        - ICT-VAA: vast bedrag per element ongeacht waarde
        - Lening-VAA: berekening per saldo × renteverschil — bedragen kunnen sterk variëren
