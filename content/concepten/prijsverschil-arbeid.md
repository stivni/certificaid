---
title: Tariefverschil en efficiëntieverschil bij arbeid
tags:
- concept
- begrip
- po-1-8
linked_anchors:
- 1.8.II.C
- 1.8.VI.D
programmaonderdelen:
- '1.8'
confidence: inferred
node_type: begrip
status: seed
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/prijsverschil-arbeid.json
gegenereerd_op: '2026-05-21'
---
# Tariefverschil en efficiëntieverschil bij arbeid 🔗

Tariefverschil en efficiëntieverschil zijn de twee componenten van het arbeidskosten-verschil in een standaardkostencalculatie. Het totale verschil tussen werkelijke en standaard arbeidskost wordt gesplitst in (1) een tariefcomponent — werkelijk uurtarief versus standaard, gevolg van HR-/loonbeleid — en (2) een efficiëntiecomponent — gebruikte uren versus norm-uren, gevolg van productie-efficiëntie. Deze splitsing is de basis van verschillenboekhouding bij arbeid en wijst aan wélke factor sturing nodig heeft.

> [!summary] Korte inhoud
> Bij arbeidskosten wordt het totaal verschil tussen werkelijke en standaard arbeidskost gesplitst in: tariefverschil = werkelijke uren × (werkelijk uurtarief − standaard uurtarief) en efficiëntieverschil = (werkelijke uren − standaarduren) × standaard uurtarief.

> [!info] Behoort tot: [[verschillenboekhouding]]

Bij arbeidskosten wordt het totaal verschil tussen werkelijke en standaard arbeidskost gesplitst in: tariefverschil = werkelijke uren × (werkelijk uurtarief − standaard uurtarief) en efficiëntieverschil = (werkelijke uren − standaarduren) × standaard uurtarief. Tariefverschil wijst op HR-/loon-oorzaak; efficiëntieverschil op productie-snelheid.

_Bron: Management accounting — bron-gap_



## Berekening

### Splitsing arbeidskosten-verschil in tarief en efficiëntie

**Tariefverschil arbeid (labour rate variance)** 
```
tariefverschil = werkelijke_uren × (werkelijk_uurtarief − standaard_uurtarief)
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `werkelijke_uren` | Effectief gepresteerde arbeidsuren | uren |
| `werkelijk_uurtarief` | Werkelijk betaalde all-in uurkost | EUR/uur |
| `standaard_uurtarief` | Begroot all-in uurtarief (norm) | EUR/uur |

**Voorbeeld-invulling**: werkelijke_uren = 530, werkelijk_uurtarief = € 26,50, standaard_uurtarief = € 25,00

```
530 × (€ 26,50 − € 25,00) = 530 × € 1,50 = € 795 ongunstig
```

_Resultaat in EUR_
**Efficiëntieverschil arbeid (labour efficiency variance)** 
```
efficientieverschil = (werkelijke_uren − standaarduren) × standaard_uurtarief
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `werkelijke_uren` | Effectief gepresteerde arbeidsuren | uren |
| `standaarduren` | Toegestane norm-uren voor de werkelijke output | uren |
| `standaard_uurtarief` | Begroot all-in uurtarief | EUR/uur |

**Voorbeeld-invulling**: werkelijke_uren = 530, standaarduren = 100 × 5 = 500 (100 tapijten × 5 uur norm), standaard_uurtarief = € 25,00

```
(530 − 500) × € 25 = 30 × € 25 = € 750 ongunstig
```

_Resultaat in EUR_
**Totaal arbeidskosten-verschil** (volgt op: tariefverschil, efficientieverschil)
```
totaal = tariefverschil + efficientieverschil
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `tariefverschil` | Resultaat tarief-formule | EUR |
| `efficientieverschil` | Resultaat efficiëntie-formule | EUR |

**Voorbeeld-invulling**: tariefverschil = € 795 ongunstig, efficientieverschil = € 750 ongunstig

```
€ 795 + € 750 = € 1.545 ongunstig
```

_Resultaat in EUR_

## Zie ook

- **Vereist kennis van**: [[arbeidskosten]]

## Voorbeelden

Yperse Werkplaats BV — partij 100 tapijten: standaard 5 uur/tapijt × € 25/uur. Werkelijk: 530 uur × € 26,50/uur. Tariefverschil = 530 × (26,50 − 25,00) = € 795 ongunstig. Efficiëntieverschil = (530 − 500) × € 25 = € 750 ongunstig. Totaal: € 1.545 ongunstig.

