---
title: "Fiscale voordelen vennootschap"
concept_type: "kader"
schema_version: "2.2"
status: "concept"
categorieen:
  - kader
ankers:
  - 2.3.II
  - 2.3.III
  - 2.3.taak.3
tags:
  - concept
  - schema-2.2
  - type-kader
  - cat-kader
  - status-concept
gegenereerd_uit: "data/concepten/records/fiscale-voordelen-vennootschap.json"
---

# Fiscale voordelen vennootschap

_Kader_

🏛️ Kader · Anchors: `2.3.II` · `2.3.III` · `2.3.taak.3` · Wave: `fiscale-voordelen-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: aftrekken vennootschapsbelasting · fiscale regimes vennootschap

## Definitie

📖 De vennootschapsbelasting kent een reeks aftrekken en regimes die het belastbaar inkomen of het tarief verlagen. Ze worden in een wettelijk vastgelegde volgorde toegepast (art. 207 WIB92) op de Belgische resterende winst en de niet bij verdrag vrijgestelde resterende winst. Dit Σ-record is het overzicht: definitief belaste inkomsten (DBI), innovatie-aftrek, investeringsaftrek, groepsbijdrage, overgedragen verliezen, gespreide belasting van meerwaarden, liquidatiereserve, KMO-tarief en verlaagde roerende voorheffing (VVPR-bis). De individuele regimes hebben elk een eigen record.

<small>📚 WIB92 — art. 207 — _wettekst_ · aangifte-VenB-2025-uiteenzetting-winst — Tabel aftrekken in volgorde — blz. 8 — _aangifte_</small>

## Substantie

🔗 Praktisch gezien is dit het 'menu' van fiscale optimalisatie voor een vennootschap. Bij elk boekjaar moet de accountant nagaan welke aftrekken combineerbaar zijn, welke voorwaarden vervuld zijn (bv. KMO-statuut, bezoldigingstoets, R&D-activiteit, herinvesteringsverplichting) en in welke volgorde ze gebruikt moeten worden. De volgorde is niet onschuldig: aftrekken met onbeperkte overdracht (DBI, innovatie) komen vóór aftrekken zonder of met beperkte overdracht (groepsbijdrage), zodat de minst-flexibele eerst opgaat. Boven de drempel van 1.000.000 EUR (korf-regime art. 207 §5 WIB92) is slechts 70 % van de overgedragen aftrekken bruikbaar op de winst boven 1 mio.

<small>📚 WIB92 — art. 207 — _wettekst_ · aangifte-VenB-2025-uiteenzetting-winst — code 1440 — grondslag korf — _aangifte_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 Ratio legis: het Belgisch VenB-stelsel kent een nominaal tarief van 25 % (20 % voor de eerste schijf KMO), maar daalt door aftrekken vaak naar een effectief lager tarief. De wetgever beheerst dit op twee manieren: (1) elke aftrek heeft eigen voorwaarden (bv. taxatie- en deelnemingsvoorwaarden voor DBI, KMO-statuut voor VVPR-bis); (2) sinds AJ 2019 garandeert het korf-regime dat winsten boven 1.000.000 EUR steeds een minimumbasis houden waarop het tarief loopt — dit beschermt de begrotingsopbrengst tegen volledige uitholling door overgedragen aftrekken. Pijler-2 (15 % wereldwijde minimumbelasting) voegt sinds 2024 een tweede vloer toe voor grote multinationals.

<small>📚 WIB92 — art. 215 — _wettekst_ · WIB92 — art. 207 §5 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: WIB92 art. 207 (volgorde) + art. 215 (tarief) + art. 205/1-205/4 (innovatie) + art. 184quater (liquidatiereserve)

Stelsel sinds VenB-hervorming 2017 (wet 25-12-2017) ingrijpend gewijzigd: tarief van 33,99 % naar 25 % (20 % KMO eerste schijf), korf-regime ingevoerd, notionele interestaftrek hervormd (alleen incrementeel) en uiteindelijk afgeschaft AJ 2024. Pijler-2-minimum-belasting voor MNE-groepen vanaf AJ 2025.

**✅ Voor**
- 🔗 Elke Belgische vennootschap of vaste inrichting onderworpen aan de VenB — bij de jaarlijkse aangifte moet de aftrek-volgorde correct toegepast worden. Vooral relevant bij vennootschappen met aanzienlijke overgedragen aftrekken, investeringen, R&D-activiteit of dividend-stromen uit deelnemingen.

**👍 Voordeel**
- 🔗 Verlaging van de effectieve belastingdruk via legitiem gebruik van aftrekken. Sommige aftrekken (DBI, innovatie) zijn onbeperkt overdraagbaar — niet-gebruikte aftrek dit jaar blijft beschikbaar volgende jaren. Andere (investeringsaftrek) hebben beperkte overdracht maar geven onmiddellijk fiscaal effect.

**⚠️ Risico**
- 🔗 Verkeerde volgorde of dubbel gebruik leidt tot aanslagcorrecties en eventuele administratieve boetes. Voorwaarden voor aftrek (bv. bezoldigingstoets KMO-tarief, herinvesteringsverplichting gespreide meerwaarde) worden niet altijd door de aangifte-software gevalideerd — controle is mensen-werk.

## Bouwstenen

### 📜 Aftrek-volgorde art. 207 WIB92  
_`regel`_

📖 Art. 207 WIB92 legt de exacte volgorde vast waarin aftrekken op de resterende winst worden toegepast (Belgische en niet bij verdrag vrijgestelde resterende winst). In de aangifte (codes 1432-1450) komen ze als volgt: (1) niet-belastbare bestanddelen 1432, (2) DBI van het belastbare tijdperk 1433, (3) innovatie-aftrek van het belastbare tijdperk 1439, (4) correctie innovatie-aftrek omgezet in belastingkrediet 1446, (5) investeringsaftrek enkel kolom Belgisch resultaat 1437, (6) aftrek groepsbijdrage 1445, (7) berekening korf 1440, (8a-e) overgedragen aftrekken: overgedragen DBI 1441, overgedragen innovatie 1442, vorige verliezen 1436, overgedragen NIA 1443. Elke aftrek is beperkt tot wat overblijft na de voorafgaande.

<small>📚 WIB92 — art. 207 — _wettekst_ · WIB92 — art. 206/5 — _wettekst_ · aangifte-VenB-2025-uiteenzetting-winst — Tabel aftrekken in volgorde — blz. 8 — _aangifte_</small>

### 🚧 Korf-regime — minimum belastbare basis  
_`beperking`_

📖 Sinds AJ 2019 (wet 25-12-2017) beperkt het korf-regime de aftrek van bepaalde overgedragen aftrekken (overgedragen DBI, overgedragen innovatie-aftrek, vorige verliezen, overgedragen NIA-onbeperkt-deel) tot 1.000.000 EUR + 70 % van de winst boven 1.000.000 EUR. Concreet: van de winst boven 1 mio kan slechts 70 % weggewerkt worden door deze overgedragen aftrekken — 30 % wordt steeds belast als minimum-grondslag. De korf geldt niet voor aftrekken van het belastbare tijdperk zelf (huidig DBI, huidig innovatie, investeringsaftrek).

<small>📚 WIB92 — art. 207 §5 — _wettekst_ · aangifte-VenB-2025-uiteenzetting-winst — code 1440 — grondslag korf — _aangifte_</small>

### 🚧 Aftrekverbod art. 206/3 WIB92  
_`beperking`_

📖 Op bepaalde bestanddelen van de winst is GEEN ENKELE aftrek toegestaan, ook geen verliescompensatie. Dit zijn de 'sanctie-bestanddelen' uit art. 206/3 §1 WIB92: abnormale of goedgunstige voordelen (art. 79), verkregen voordelen van alle aard (art. 53,24°), grondslag afzonderlijke aanslag op geheime commissielonen (art. 219), niet-naleving onaantastbaarheidsvoorwaarde investeringsreserve (art. 194quater), grondslag exit-tax (art. 519ter). Deze bestanddelen blijven altijd belastbaar, zelfs als de vennootschap globaal verlies maakt.

<small>📚 WIB92 — art. 206/3 §1 — _wettekst_ · aangifte-VenB-2025-uiteenzetting-winst — Rubriek B blz. 7 — code 1420 — _aangifte_</small>

### ⚙️ Overzicht beschikbare aftrekken + regimes  
_`mechanisme`_

🔗 Het VenB-stelsel kent grosso modo twee soorten voordelen. (A) Aftrekken op de belastbare basis (verlagen de grondslag waarop het tarief loopt): definitief belaste inkomsten (DBI — art. 202-205, voor dividend-inkomen), innovatie-aftrek (art. 205/1-205/4, 85 % vrijstelling netto-octrooi-inkomen), investeringsaftrek (art. 68-77, % van investering), gespreide belasting meerwaarden (art. 47, herinvesteringsregime), groepsbijdrage (art. 205/5, overdracht winst/verlies binnen groep). (B) Tarief-modulerende of uitkeer-modulerende regimes: verlaagd KMO-tarief 20 % (art. 215, eerste schijf 100.000 EUR), liquidatiereserve (art. 184quater, 10 % nu + 0 %/5 % roerende voorheffing later i.p.v. 30 %), VVPR-bis (art. 269 §2, verlaagde roerende voorheffing 15 % bij dividenduitkering KMO), meerwaarde-aandelen 0 % (art. 192 mits DBI-voorwaarden vervuld).

<small>📚 WIB92 — art. 202-205 — _wettekst_ · WIB92 — art. 205/1-205/4 — _wettekst_ · WIB92 — art. 184quater — _wettekst_ · WIB92 — art. 215 — _wettekst_ · WIB92 — art. 269 §2 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 🚧 Pijler-2-minimum-belasting (vanaf AJ 2025)  
_`beperking`_

📖 Voor multinationale groepen (MNE) of grote binnenlandse groepen met geconsolideerde omzet ≥ 750 mio EUR geldt sinds AJ 2025 een wereldwijde minimumbelasting van 15 % (OESO-Pijler-2). Indien het effectieve VenB-tarief in België na alle aftrekken daalt onder 15 %, wordt een aanvullende heffing (top-up tax) ingehouden. In de aangifte VenB 2025 staan codes 1815-1820 voor Pijler-2-identificatie en overdracht van overschotten voorafbetalingen. Voor KMO's en niet-groep-vennootschappen heeft Pijler-2 geen impact.

<small>📚 aangifte-VenB-2025-tarief-voorafbetalingen — codes 1815-1820 Pijler-2 — _aangifte_</small>

## Valkuilen

### ⚠️ Aftrek-volgorde negeren in planning

**Verkeerde assumptie**: Studenten denken dat de vennootschap zelf de aftrek-volgorde kan kiezen om optimaal te zijn.

**Kernpunt**: De volgorde is wettelijk vastgelegd in art. 207 WIB92 — geen vrije keuze. Wel keuze bij sommige regimes: bv. afzien van investeringsaftrek (om hogere onmiddellijke winst te tonen) of innovatie-aftrek omzetten in belastingkrediet (art. 289decies). Maar binnen de aftrek-toepassing zelf: geen keuzevrijheid.

<small>📚 WIB92 — art. 207 — _wettekst_</small>

### ⚠️ Korf-regime verwarren met aftrekverbod

**Verkeerde assumptie**: De korf en het aftrekverbod (art. 206/3) zijn hetzelfde — beide beperken aftrek.

**Kernpunt**: Aftrekverbod 206/3: bepaalde bestanddelen (abnormale voordelen, geheime commissielonen, ...) zijn NOOIT vatbaar voor aftrek — ze blijven altijd belastbaar. Korf 207 §5: aftrekken zijn TOEGESTAAN maar BEPERKT tot 1 mio + 70 % van de meerwinst; alleen voor overgedragen aftrekken. Verschillende doelen: 206/3 is sanctie-bestanddeel; korf is begrotingsbescherming.

<small>📚 WIB92 — art. 206/3 — _wettekst_ · WIB92 — art. 207 §5 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Notionele interestaftrek nog actief denken

**Verkeerde assumptie**: Notionele interestaftrek is een van de courante aftrekken die je in elke planning moet meenemen.

**Kernpunt**: Notionele interestaftrek is sinds AJ 2024 volledig afgeschaft (wet 22-12-2023). Alleen overgedragen saldi uit vóór-2024-tijdperken kunnen nog worden uitgeput — voor lopende boekjaren geen nieuwe creatie meer. Geen rol meer in toekomstige planning.

<small>📚 WIB92 — art. 536 (overgangsregeling NIA) — _wettekst_</small>

## Accountant-perspectieven

### Vennootschap (eigen aangifte/planning)

_De accountant die de VenB-aangifte voorbereidt of fiscale planning doet._

#### 💰 Fiscaal adviseur

##### 👣 Checklist aftrekken per aanslagjaar  
_`stap`_

🔗 Per aanslagjaar systematisch nakijken: (1) KMO-statuut (art. 1:24 WVV) → KMO-tarief mogelijk? Bezoldigingstoets vervuld? (2) Dividend-inkomen → DBI-voorwaarden vervuld (taxatie + 10 %/2,5 mio + 1 jaar bezit)? (3) R&D-activiteit → innovatie-aftrek opgave 275 INNO? (4) Investeringen → investeringsaftrek (basis 8 % of verhoogd voor energie/R&D)? (5) Meerwaarden gerealiseerd → keuze gespreide belasting art. 47? (6) Liquidatiereserve aanleggen voor uitkering toekomst? (7) Aftrek-volgorde correct: codes 1432-1450 in juiste sequentie.

<small>📚 WIB92 — art. 207 — _wettekst_ · aangifte-VenB-2025-uiteenzetting-winst — blz. 8 — _aangifte_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

##### 👣 Korf-impact bij hoge winst  
_`stap`_

🔗 Bij winst > 1.000.000 EUR: bereken de korf-grondslag (code 1440). Niet-overdraagbare aftrekken (DBI-tijdperk, innovatie-tijdperk, investeringsaftrek) eerst toepassen — die zitten vóór de korf. Daarna kijken hoeveel ruimte voor overgedragen aftrekken (max 1 mio + 70 % van meerwinst). Belangrijk: investeringsaftrek mag enkel op het Belgisch resultaat (code 1437) — niet op het buitenlandse deel.

<small>📚 WIB92 — art. 207 §5 — _wettekst_ · aangifte-VenB-2025-uiteenzetting-winst — code 1437 + 1440 — _aangifte_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 🧭 Adviseur

##### 🧭 Stapeling-keuzes uitleggen aan cliënt  
_`vuistregel`_

🔗 Toon cliënt het effectieve tarief na alle aftrekken — niet alleen het nominale 25 %. Bv. een kmo met 200.000 EUR winst, eerste schijf KMO-tarief, plus investeringsaftrek 8 % op 50.000 EUR investeringen, plus innovatie-aftrek op licentie-inkomen: effectief tarief kan dalen tot 15-18 %. Maar altijd voorwaarden checken (bezoldigingstoets, herinvesterings-verplichting, taxatie-voorwaarde DBI). Geen voorwaarde = aanslagcorrectie achteraf.

<small>📚 WIB92 — art. 215 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → KMO-tarief detail → [[verlaagd-tarief-kleine-vennootschap]] _(moet-verwijzen)_
- → DBI-aftrek detail → [[dbi-aftrek]] _(moet-verwijzen)_
- → Notionele interestaftrek (afgeschaft AJ 2024) → [[notionele-interestaftrek]] _(moet-verwijzen)_
- → Innovatie-aftrek detail → [[innovatie-aftrek]] _(moet-verwijzen)_
- → Investeringsaftrek detail → [[investeringsaftrek]] _(moet-verwijzen)_
- → Anti-misbruik bij aftrekken → [[algemene-anti-misbruik-bepaling]] _(moet-verwijzen)_
- ↪ Aangifte VenB (uitvoerings-context) → [[aangifte-vennootschapsbelasting]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[vennootschapsbelasting]]
### `bevat`
- [[dbi-aftrek]]
- [[innovatie-aftrek]]
- [[investeringsaftrek]]
- [[gespreide-belasting-meerwaarden]]
- [[liquidatiereserve]]
- [[verlaagd-tarief-kleine-vennootschap]]
- [[vvprbis]]
- [[meerwaarde-aandelen-venb]]
- [[notionele-interestaftrek]]
- [[thin-cap-regime]]
### `triggert`
- [[aangifte-vennootschapsbelasting]] — Aftrekken worden via codes 1432-1450 in de aangifte uitgevoerd.
### `beinvloed_door`
- [[algemene-anti-misbruik-bepaling]] — Art. 344 §1 WIB92 kan onbedoeld gebruik van aftrekken corrigeren.
