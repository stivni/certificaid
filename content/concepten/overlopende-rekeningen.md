---
title: "Overlopende rekeningen"
concept_type: "balanspost"
schema_version: "2.2"
status: "concept"
categorieen:
  - entiteit
ankers:
  - 1.1.II.L
tags:
  - concept
  - schema-2.2
  - type-balanspost
  - cat-entiteit
  - status-concept
gegenereerd_uit: "data/concepten/records/overlopende-rekeningen.json"
---

# Overlopende rekeningen

_Balanspost_

🏢 Entiteit · Anchors: `1.1.II.L` · Wave: `extract-jaarrekening-rest-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: transitorische rekeningen · tijdsverschilcorrecties

## Definitie

📖 **Overlopende rekeningen** (MAR-klasse 49 actief + 89 passief) zijn balansposten die het **matching-principe** operationaliseren: ze schuiven kosten en opbrengsten naar het **juiste boekjaar** waarin ze economisch thuishoren, los van het moment van facturatie of betaling. Vier sub-rubrieken:
- **490 Over te dragen kosten** (actief): kosten **al betaald** maar economisch toebehorend aan volgend boekjaar
- **491 Verkregen opbrengsten** (actief): opbrengsten **al verdiend** maar nog niet gefactureerd
- **492 Toe te rekenen kosten** (passief): kosten **al opgelopen** maar nog niet gefactureerd door leverancier
- **493 Over te dragen opbrengsten** (passief): opbrengsten **al ontvangen** maar economisch toebehorend aan volgend boekjaar

<small>📚 KB 29-04-2019 WVV — bijlage MAR — Klasse 49 + 89 — _kb_</small>

## Substantie

📖 Het mechanisme: bij **jaarafsluit** worden bedragen overgeheveld tussen klasse 6/7 (resultaat) en klasse 49/89 (balans). Bij **heropening** van het volgende boekjaar worden de overlopende rekeningen omgekeerd doorgeboekt — de kost of opbrengst landt dan automatisch in het juiste boekjaar.

**Vier scenario's**:

| Scenario | Betaling | Werkelijke periode | Rekening | Effect resultaat huidig boekjaar |
|---|---|---|---|---|
| Huur-vooruit-betaling | Nu betaald | Volgend boekjaar | 490 Over te dragen kosten | Kost wordt teruggeschoven naar 49x → resultaat **stijgt** |
| Rente-verkregen-vooruit | Nog niet ontvangen | Huidig boekjaar | 491 Verkregen opbrengsten | Opbrengst extra erkend → resultaat **stijgt** |
| Eindejaars-bonus personeel | Nog niet betaald | Huidig boekjaar | 492 Toe te rekenen kosten | Kost extra erkend → resultaat **daalt** |
| Abonnement-jaarvooruit ontvangen | Nu ontvangen | Volgend boekjaar | 493 Over te dragen opbrengsten | Opbrengst teruggeschoven → resultaat **daalt** |

<small>📚 KB 29-04-2019 WVV — art. 3:24 + Klasse 49/89 — _kb_</small>

## Rationale

🔗 Zonder overlopende rekeningen zou het **moment van facturatie of betaling** bepalend zijn voor het resultaat — wat economisch misleidend is. Een huur die in december wordt betaald maar betrekking heeft op januari volgend jaar zou anders het lopende boekjaar onterecht belasten. Het matching-principe stelt dat opbrengsten en kosten **moeten worden erkend in de periode waarin ze zijn verdiend of opgelopen**, niet wanneer cash beweegt. Klasse 49/89 maakt deze verschuiving boekhoudkundig mogelijk zonder de oorspronkelijke factuur of betaling te herzien.

<small>📚 KB 29-04-2019 WVV — art. 3:24 — _kb_</small>

## Bouwstenen

### ⚙️ Boeking — over te dragen kost (490)  
_`mechanisme`_

🔗 **Scenario**: Een vennootschap betaalt in december 2025 een verzekeringspremie van 12.000 EUR voor de periode 1 januari 2026 tot 31 december 2026.

**Initiële boeking** (bij betaling, december 2025):
```
614 Verzekeringspremies        D 12.000
   55 Bank                      C 12.000
```

**Correctie eindejaar** (31-12-2025) — de hele premie hoort bij 2026:
```
490 Over te dragen kosten      D 12.000
   614 Verzekeringspremies      C 12.000
```
Resultaat: de 12.000 EUR kost staat nu op de balans (490) en niet in het resultaat van 2025.

**Heropening** (01-01-2026):
```
614 Verzekeringspremies        D 12.000
   490 Over te dragen kosten    C 12.000
```
De kost landt nu in het resultaat van 2026 — economisch correct.

<small>📚 KB 29-04-2019 WVV — Klasse 49 — _kb_</small>

### ⚙️ Boeking — toe te rekenen kost (492)  
_`mechanisme`_

🔗 **Scenario**: De vennootschap verbruikt in december 2025 elektriciteit voor 3.500 EUR, maar ontvangt de factuur pas in februari 2026.

**Correctie eindejaar** (31-12-2025) — de kost hoort economisch bij 2025:
```
6111 Elektriciteit             D 3.500
   492 Toe te rekenen kosten    C 3.500
```
Resultaat: kost van 3.500 EUR is in resultaat 2025 erkend; 492 is een **passief-rubriek** (verwachte schuld).

**Heropening** (01-01-2026):
```
492 Toe te rekenen kosten      D 3.500
   6111 Elektriciteit           C 3.500
```

**Ontvangst factuur** (februari 2026, bv. 3.700 EUR):
```
6111 Elektriciteit             D 3.700
   440 Leveranciers             C 3.700
```
In 2026 blijft netto in resultaat: 3.700 (werkelijke factuur) - 3.500 (heropening tegenboeking) = 200 EUR — de schattings-afwijking.

<small>📚 KB 29-04-2019 WVV — Klasse 89 — _kb_</small>

### ⚙️ Boeking — over te dragen opbrengst (493)  
_`mechanisme`_

🔗 **Scenario**: Een abonnementsbedrijf ontvangt in oktober 2025 een jaarabonnement van 600 EUR voor de periode oktober 2025 tot september 2026.

**Initiële boeking** (oktober 2025):
```
55 Bank                        D 600
   70 Omzet                     C 600
```

**Correctie eindejaar** (31-12-2025) — 3 van de 12 maanden zijn verdiend (3 × 50 = 150), 9 maanden niet (450):
```
70 Omzet                       D 450
   493 Over te dragen opbrengsten C 450
```
Resultaat: 150 EUR omzet erkend in 2025, 450 EUR teruggeschoven naar 2026 via balans-passief.

<small>📚 KB 29-04-2019 WVV — Klasse 89 — _kb_</small>

## Valkuilen

### ⚠️ Klasse 49 verwarren met klasse 89

**Verkeerde assumptie**: Alle overlopende rekeningen staan op de actief-zijde.

**Kernpunt**: **49 = actief**, **89 = passief**. De fictieve regel: "betaal/ontvang vooraf" levert een **actief** (490 of 491 — waarde nog te verbruiken/innen); "betaal/ontvang achteraf" levert een **passief** (492 of 493 — schuld of voorschot van klant).

<small>📚 KB 29-04-2019 WVV — Klasse 49 + Klasse 89 — _kb_</small>

### ⚠️ Vergeten te heropenen in volgend boekjaar

**Verkeerde assumptie**: Een eenmalige boeking op 31-12 is voldoende.

**Kernpunt**: Elke afsluit-boeking op klasse 49/89 moet bij **heropening** van het volgende boekjaar **omgekeerd** worden doorgeboekt, anders blijft het bedrag eeuwig op de balans staan en wordt het matchings-effect ongedaan gemaakt.

<small>📚 KB 29-04-2019 WVV — Klasse 49/89 — _kb_</small>

## Verder lezen (scope-out)

- → Boekhoudbeginselen (matching-principe) → [[boekhoudbeginselen]] _(moet-verwijzen)_
- → Eindejaarsverrichtingen (toepassings-context) → [[eindejaarsverrichtingen]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[boekhouding]]
### `vereist`
- [[boekhoudbeginselen]]
### `triggert`
- [[eindejaarsverrichtingen]]
