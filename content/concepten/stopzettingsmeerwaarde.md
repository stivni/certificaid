---
title: "Stopzettingsmeerwaarde"
concept_type: "regime"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
  - gebeurtenis
ankers:
  - 2.2.VI.B
  - 2.2.X
tags:
  - concept
  - schema-2.2
  - type-regime
  - cat-regeling
  - cat-gebeurtenis
  - status-concept
gegenereerd_uit: "data/concepten/records/stopzettingsmeerwaarde.json"
---

# Stopzettingsmeerwaarde

_Regime_

📋 Regeling · 📅 Gebeurtenis · Anchors: `2.2.VI.B` · `2.2.X` · Wave: `skeleton-pb-venb-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: cessatiemeerwaarde · plus-value de cessation — **Vertalingen**: fr: plus-value de cessation

## Definitie

📖 Een stopzettingsmeerwaarde is een meerwaarde verkregen of vastgesteld uit hoofde of naar aanleiding van de gehele of gedeeltelijke stopzetting van een beroepswerkzaamheid (eenmanszaak winst, vrij beroep baten) of van een bedrijfsafdeling/tak van werkzaamheid (art. 28, lid 1, 1° WIB92). Ze ontstaat op de activa die voor die beroepswerkzaamheid werden gebruikt (materiële vaste activa, immateriële vaste activa zoals goodwill en cliënteel, financiële vaste activa, voorraden) en wordt belast in de PB als 'winst of baten van een vorige beroepswerkzaamheid' (art. 23 § 1, 3°) — typisch tegen afzonderlijke gunsttarieven (10 %, 16,5 % of 33 %) in plaats van het progressief tarief.

<small>📚 WIB92 — art. 23 § 1-3°, 28 lid 1, 1° — _wettekst_</small>

## Substantie

🔗 Bij stopzetting van een eenmanszaak komt de zelfstandige aan een fiscaal 'afrekenmoment': de fiscus 'koopt' de verborgen meerwaarden af tegen een verlaagd afzonderlijk tarief. Hoeveel de zelfstandige uiteindelijk betaalt hangt af van drie variabelen: (1) wat hij stopzet (welk type activa); (2) hoe (vrijwillig of gedwongen door overlijden, ziekte, onteigening, pensioen); (3) op welke leeftijd (60-jaar-grens). De wetgever gebruikt deze cascade om enerzijds 'langlopende winsten' (cliënteel opgebouwd over jaren) niet te zwaar te belasten, anderzijds vrijwillige rocades (bv. omzetting eenmanszaak → vennootschap) te kanaliseren via art. 46 (fiscale neutraliteit). Praktisch is dit één van de meest gevoelige momenten voor optimalisatie: een goede planning van het stopzettingsmoment + activa-toewijzing kan tienduizenden euro fiscale besparing opleveren.

<small>📚 WIB92 — art. 28, 46, 47, 171 — _wettekst_</small>

## Rationale

🔗 De gunsttarieven (10/16,5/33 %) corrigeren een progressie-effect: zonder afzonderlijk tarief zouden alle latente meerwaarden in één belastbaar tijdperk vallen, waardoor het marginaal tarief 50 %+ wordt. De 10 %-grens (vanaf 60 jaar of gedwongen) erkent dat ouderen vaak hun pensioen-financiering uit de stopzetting halen. Art. 46-47-vrijstellingen ondersteunen herstructurering (vennootschap-vorming, voortzetting binnen familie) zonder fiscale hindernis.

<small>📚 WIB92 — art. 171 — _wettekst_</small>

## Gebruikscontext

**Status**: `in-voege` · basis: WIB92 art. 28, 39, 40, 46, 47, 169, 171

**✅ Voor**
- 📖 Bij elke definitieve stopzetting van zelfstandige eenmanszaak of vrij beroep (cessatie, pensioen, overlijden, omzetting in vennootschap).

**▶️ Trigger start**
- 🔗 Vrijwillige stopzetting (cessatie-akte + uitschrijving KBO + BTW-stopzetting), of gedwongen stopzetting (overlijden, blijvende arbeidsongeschiktheid > 66 %, onteigening), of omzetting in vennootschap.

## Bouwstenen

### 🧮 Bepaling van de meerwaarde (art. 43 WIB)  
_`formule`_

📖 Meerwaarde = werkelijke verkoopprijs (of overdrachtswaarde) − fiscale netto-boekwaarde van het actief. Fiscale netto-boekwaarde = aanschaffingswaarde − fiscaal aanvaarde afschrijvingen − eventuele waardeverminderingen. Aftrekbaar: werkelijke kosten van overdracht (notaris, makelaar) — vandaar 'meerwaarden na aftrek werkelijke overdrachtskosten' op aangifte vak XXI.

<small>📚 WIB92 — art. 43 — _wettekst_ · aangifte-PB-2025-stopzetting — vak XXI rubriek 1 — _aangifte_</small>

### 📜 Tariefcascade stopzettingsmeerwaarden (art. 171 WIB)  
_`regel`_

📖 Afzonderlijke tarieven (art. 171 WIB92), te beoordelen per activum:

<small>📚 WIB92 — art. 171, 1°-4° — _wettekst_ · aangifte-PB-2025-stopzetting — vak XXI rubriek 1 — _aangifte_</small>

### ↪️ Vrijstelling bij inbreng in vennootschap (art. 46 WIB)  
_`uitzondering`_

📖 Stopzettingsmeerwaarden worden volledig maar tijdelijk vrijgesteld bij inbreng van de eenmanszaak (of een bedrijfstak) in een vennootschap, mits cumulatief: (1) inbreng tegen aandelen; (2) maatschappelijke zetel binnen EER; (3) voortzetting van de activiteit; (4) vereiste boekhoudkundige continuïteit (zelfde boekwaarden in de vennootschap). De vrijgestelde meerwaarde wordt latent gehouden in de vennootschap en zal worden belast bij latere realisatie. Dit is dé manier om een eenmanszaak fiscaal-neutraal te transformeren in een BV/NV.

<small>📚 WIB92 — art. 46 § 1 — _wettekst_</small>

### ↪️ Gespreide belasting bij wederbelegging (art. 47 WIB)  
_`uitzondering`_

📖 Meerwaarden op materiële + immateriële vaste activa die meer dan 5 jaar gebruikt waren, kunnen onder bepaalde voorwaarden (art. 47 WIB) gespreid worden belast over de afschrijvingsperiode van een wederbelegging — d.w.z. herbelegging van de verkoopprijs in nieuwe vaste activa binnen 3 (of 5) jaar. Dit mechanisme is vooral relevant bij gehele stopzetting wanneer de zelfstandige onmiddellijk in een vennootschap herbelegt of in een ander beroepsproject investeert.

<small>📚 WIB92 — art. 47 — _wettekst_</small>

### ⚙️ Categorisering van activa bij stopzetting  
_`mechanisme`_

**Substantie**: 🔗 Niet alle activa volgen hetzelfde tarief. Per type:

<small>📚 WIB92 — art. 28, 171 — _wettekst_</small>

### ↪️ Vrijstelling voortzetting door erfgenaam (art. 40 + 169 WIB)  
_`uitzondering`_

📖 Bij overlijden van de zelfstandige worden stopzettingsmeerwaarden volledig vrijgesteld wanneer de beroepswerkzaamheid wordt voortgezet door de overlevende echtgenoot, één of meer erfgenamen of legatarissen in de rechte lijn of in de zijlijn tot de tweede graad (art. 40 WIB92). De activa moeten met behoud van boekwaarden worden overgenomen — fiscale neutraliteit (continuïteit). Doel: familiale ondernemingen niet onbedoeld liquideren wegens fiscaal afrekenmoment.

<small>📚 WIB92 — art. 40, 169 — _wettekst_</small>

## Voorbeelden

### 💡 Vrijwillige stopzetting bakker 52 jaar — tariefcascade volledig uitgewerkt 🔗

_Bakker stopt op 52 jaar. Verkoopt: cliënteel/goodwill (opgebouwd 25 jaar) voor € 60.000; oven (gebruikt 8 jaar, boekwaarde € 5.000) voor € 12.000; bestelwagen (gebruikt 3 jaar, boekwaarde € 8.000) voor € 14.000; voorraad grondstoffen (boekwaarde € 4.000) voor € 6.000._

**Berekening:**

<small>📚 WIB92 — art. 28, 43, 171 — _wettekst_ · aangifte-PB-2025-stopzetting — vak XXI rubriek 1 — _aangifte_</small>

### 💡 Inbreng eenmanszaak in BV — art. 46 fiscale neutraliteit 🔗

_Advocaat, 45 jaar, brengt zijn eenmanszaak (cliënteel € 200.000 marktwaarde, kantoor-inrichting boekwaarde € 10.000 marktwaarde € 15.000) in tegen aandelen van een nieuw opgerichte BV._

**Berekening:**

**Boeking:**


<small>📚 WIB92 — art. 28, 46 § 1 — _wettekst_</small>

### 💡 Overlijden ondernemer + voortzetting door echtgenoot 📖

_Bakker overlijdt op 58 jaar. Latente meerwaarde cliënteel + activa € 100.000. Echtgenote zet bakkerij voort._

**Berekening:**

<small>📚 WIB92 — art. 40, 171-2° — _wettekst_</small>

## Valkuilen

### ⚠️ Voorraden krijgen géén 16,5 %-tarief (ook bij oude ondernemer)

**Verkeerde assumptie**: Bij vrijwillige stopzetting wordt alle stille reserves tegen 16,5 % belast — ook voorraad.

**Kernpunt**: Voorraden zijn nooit 'vaste activa > 5 jaar' — ze worden continu doorverkocht. Meerwaarde op voorraden = winst gemaakt bij realisatie, en valt onder art. 171-1° (33 %) of progressief tarief, niet onder 16,5 %. Alleen materiële + immateriële vaste activa krijgen het verlaagd tarief.

<small>📚 WIB92 — art. 171-1°, 171-4° — _wettekst_</small>

### ⚠️ '5-jaar-regel' meet ingebruikname, niet aankoop

**Verkeerde assumptie**: Een actief telt voor 16,5 % zodra het meer dan 5 jaar in bezit is.

**Kernpunt**: Art. 171-4° spreekt over activa die 'meer dan 5 jaar voor de beroepswerkzaamheid zijn gebruikt'. Beslissend is de werkelijke ingebruikname als beroepsactief, niet de aankoopdatum. Voor cliënteel begint de telling typisch met het begin van de beroepswerkzaamheid.

<small>📚 WIB92 — art. 171-4° — _wettekst_</small>

### ⚠️ Art. 46-neutraliteit ≠ definitieve vrijstelling

**Verkeerde assumptie**: Wanneer de eenmanszaak in een vennootschap wordt ingebracht (art. 46), is de meerwaarde definitief vrijgesteld.

**Kernpunt**: Art. 46 is een uitstel, geen vrijstelling: de latente meerwaarde wordt 'meegegeven' aan de vennootschap (boekwaardecontinuïteit) en wordt bij latere realisatie in VenB belast. Voordeel: tijdwinst, mogelijk lager VenB-tarief, planning van realisatie. Risico: niet-naleving voorwaarden (geen aandelen, geen voortzetting) → onmiddellijke belasting alsnog.

<small>📚 WIB92 — art. 46 — _wettekst_</small>

## Speelruimtes

### 🎚️ Stopzettingsmoment kiezen

## Accountant-perspectieven

### Stagiair bij stopzetting eenmanszaak cliënt

_Strategisch + uitvoerend werkpakket: voorbereiden stopzetting, kiezen scenario, aangifte vak XXI invullen._

#### 🧭 Adviseur

##### 👣 Scenario-analyse vóór stopzetting  
_`stap`_

**Substantie**: 🔗 (1) Inventariseer activa: per actief boekwaarde, geschatte marktwaarde, ingebruikname-datum (> 5 j?). (2) Beoordeel mogelijke triggers: leeftijd 60+? Gedwongen stopzetting? Inbreng-perspectief? (3) Bereken belasting voor 3 scenario's: (a) vrijwillig nu, (b) wachten 60 j, (c) inbreng art. 46. (4) Maak cash-flow-projectie. (5) Adviseer cliënt schriftelijk met scenario's + risico's. (6) Documenteer overweging in cliëntdossier.

<small>📚 WIB92 — art. 28, 46, 171 — _wettekst_</small>

#### 💰 Fiscaal adviseur

##### 👣 Aangifte PB vak XXI invullen  
_`stap`_

**Substantie**: 📖 (1) Splits stopzettingsmeerwaarden in 3 tariefbuckets: code 1686 (10 %), 1690 (16,5 %), 1691 (33 %). (2) Trek werkelijke overdrachtskosten af (notaris, makelaar) — per actief. (3) Voeg opgave 276K bij (gespreide belasting art. 47) indien wederbelegging gekozen. (4) Voor inbreng art. 46: geen aangifte stopzettingsmeerwaarden — boekhoudkundige continuïteit in BV via fiscale staat 275C. (5) Bij overlijden + voortzetting: opgave continuïteits-verklaring.

<small>📚 aangifte-PB-2025-stopzetting — vak XXI — _aangifte_</small>

## Verder lezen (scope-out)

- → Winst-baten-zelfstandige als context → [[winst-baten-zelfstandige]] _(moet-verwijzen)_
- → Gespreide belasting meerwaarden (algemeen mechanisme) → [[gespreide-belasting-meerwaarden]] _(moet-verwijzen)_
- ↪ Gunstregime familiale onderneming (vrijstelling bij voortzetting) → [[gunstregime-familiale-onderneming]] _(mag-verwijzen)_
- → Belastingberekening (afzonderlijke tarieven) → [[belastingberekening-pb]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[winst-baten-zelfstandige]]
### `vergelijkbaar_met`
- [[gespreide-belasting-meerwaarden]]
    - **Gelijkenissen**:
        - beide gunstmechanismen op meerwaarden van vaste activa
        - beide vereisen > 5 j gebruik
    - **Verschillen**:
        - stopzettingsmeerwaarde = afzonderlijk tarief 10/16,5/33 % bij cessatie; gespreide belasting (art. 47) = wederbelegging spreidt over afschrijvingsperiode nieuwe activa
        - stopzettingsmeerwaarde komt enkel bij stopzetting; gespreide belasting werkt ook tijdens activiteit
    - ⚠️ **Verwarringsrisico**: Beide kunnen gecombineerd: bij stopzetting + wederbelegging in nieuwe vaste activa kan men kiezen tussen 16,5 %-tarief óf gespreide belasting via 47.
### `triggert`
- [[belastingberekening-pb]]
### `is_uitzondering_op`
- [[beroepsinkomen-pb]]
