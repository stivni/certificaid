---
title: "Themafiche — BTW vier kernvragen"
description: "Themafiche voor sub-cluster btw-kernvragen (PO 2.4): plaats van handeling, tarief, opeisbaarheid, schuldenaar — beslisboom per vraag"
tags:
  - themafiche
  - po-2.4
  - cluster-btw
---

<div class="no-print">

> ⚠️ **Voorlopig — themafiche-laag wordt uitgefaseerd.** Per **ADR-039** vervangt één PO-samenvatting per programmaonderdeel de cluster-themafiches. Deze fiche blijft beschikbaar tot het relevante PO een leerpad krijgt — dan migreert de inhoud naar `content/leerpaden/<po-slug>/samenvatting.md`. Voor cross-PO themafiches (vergelijkingen tussen verschillende PO's) volgt een aparte beslissing per fiche: incorporeren in alle relevante samenvattingen, óf upgraden naar concept-fiche.

</div>

<div class="no-print">

> **Themafiche — kapstok voor herhaling.** Vier kernvragen die elke BTW-casus beheersen: WAAR, WAT, WANNEER en WIE. Voor verhaal en routekaart: [[leerpaden/2.4|minicursus PO 2.4]].

</div>

---

## Take-away

- **Vier kernvragen in vaste volgorde**: WAAR (plaats van handeling) → WAT (tarief / vrijstelling) → WANNEER (opeisbaarheid) → WIE (schuldenaar). Verkeerde volgorde = systematisch verkeerde aangifte
- **Plaats van handeling beslist alles** — geen Belgische BTW als plaats ≠ België; verkeerde plaats-bepaling = facturatie in verkeerd land
- **Opeisbaarheid ≠ factuurdatum** — basisregel = chronologisch eerste van levering · betaling · factuur (B2B: factuur uiterlijk 15e van volgende maand)
- **Verleggingsregeling = geen vrijstelling** — schuldenaar verschuift naar afnemer maar BTW blijft verschuldigd (rooster 55-56 + 59)
- **Vastgoed-uitzondering trumpt B2B-hoofdregel** — onroerende diensten altijd plaats ligging gebouw, ongeacht status partijen

---

## De vier kernvragen — beslisboom

```mermaid
flowchart TD
    A["BTW-casus"] --> Q1["1. WAAR<br/>plaats van handeling?"]
    Q1 -->|België| Q2["2. WAT<br/>tarief of vrijstelling?"]
    Q1 -->|Buitenland| BL["Geen Belgische BTW<br/>(check buitenlandse regels / OSS)"]
    Q2 -->|Belastbaar| Q3["3. WANNEER<br/>opeisbaarheid?"]
    Q2 -->|Vrijgesteld art. 44| V["Geen BTW<br/>+ geen aftrek input"]
    Q2 -->|Vrijgesteld art. 39-42<br/>(export, ICL)| VE["Geen BTW<br/>+ wel aftrek input"]
    Q3 --> Q4["4. WIE<br/>schuldenaar?"]
    Q4 -->|Leverancier| LV["Standaard:<br/>leverancier factureert + voldoet"]
    Q4 -->|Afnemer (verlegging)| VL["Rooster 55-56 + 59<br/>bij afnemer"]
```

---

## Vraag 1 — WAAR: plaats van handeling

| Type | Regel | Bron |
|---|---|---|
| **Goederen — met vervoer** | Plaats waar vervoer aanvangt | W.BTW art. 14 |
| **Goederen — zonder vervoer** | Plaats waar goed zich bevindt bij overdracht | W.BTW art. 14 |
| **Goederen — IC-levering B2B** | Plaats vertrek (vrijstelling 39bis bij geldig VIES-nummer) | W.BTW art. 14, 39bis |
| **Goederen — B2C afstand EU** | < 10 000 EUR drempel: vertrek · ≥ drempel: bestemming + OSS | W.BTW art. 15 |
| **Diensten — B2B** | Plaats afnemer (verlegging) | W.BTW art. 21 §2 |
| **Diensten — B2C** | Plaats dienstverrichter | W.BTW art. 21 §3 |
| **Uitzondering — onroerend** | Plaats ligging gebouw (B2B én B2C) | W.BTW art. 21bis §2, 1° |
| **Uitzondering — restaurant, personenvervoer, evenement-toegang** | Plaats fysieke uitvoering | W.BTW art. 21bis |

⚠️ **Vastgoed-uitzondering trumpt B2B-hoofdregel**: Belgische makelaar voor Duits gebouw aan Belgische klant = Duitse BTW.

---

## Vraag 2 — WAT: tarief + vrijstelling

| Tarief | Toepassing | Voorbeelden |
|---|---|---|
| **21%** | Algemeen | Meeste goederen + diensten |
| **12%** | Bijzonder | Sociale huisvesting, bepaalde voeding, restaurant (excl. drank) |
| **6%** | Verlaagd | Voeding, water, geneesmiddelen, boeken, renovatie woningen > 10j |
| **0%** | Vrijstellingen met aftrek | Export, IC-levering (art. 39-42) |
| **Vrijgesteld art. 44** | Geen BTW + GEEN aftrek input | Medisch, onderwijs, financieel, vastgoedverhuur (basis) |

⚠️ Exacte tarieven + uitzondering-lijsten: **Cijferzakboekje bij examen** raadplegen.

---

## Vraag 3 — WANNEER: opeisbaarheid

| Handeling | Belastbaar feit | Opeisbaarheid (chronologisch eerste) |
|---|---|---|
| **Levering goederen** | Terbeschikkingstelling | Levering · betaling · factuur (B2B: uiterlijk 15e v/d maand na levering) |
| **Diensten** | Voltooiing | Idem |
| **Doorlopende diensten** | Verstrijken periode | Einde elke aanrekenings-periode |
| **B2C** | Levering / dienst | Datum levering of betaling (vooruitbetaling) |

**Vooruitbetaling** = BTW opeisbaar bij ontvangst, zelfs vóór levering.

---

## Vraag 4 — WIE: schuldenaar

| Situatie | Schuldenaar | Aangifte |
|---|---|---|
| **Standaard** | Leverancier / dienstverrichter | Rooster 03/54 |
| **B2B-diensten EU — verlegging art. 21 §2** | Afnemer | Rooster 55-56 + 59 (aftrek) |
| **IC-verwerving art. 25ter** | Belgische afnemer | Rooster 86 + 55 + 59 |
| **Invoer goederen — ET 14000-vergunning** | Importeur (verlegging i.p.v. cash bij douane) | Rooster 87 + 57 + 59 |
| **Verlegging vastgoed B2B (KB nr. 1 art. 20)** | Afnemer | Rooster 87 + 56 + 59 |

⚠️ **Verleggingsregeling = geen vrijstelling**: BTW blijft verschuldigd. Niet aangeven = BTW-tekort + boete, ook zonder cash-impact bij volledige aftrek.

---

## ⚠️ Valkuilen

| Valkuil | Wat klopt er niet | Wat klopt wél |
|---|---|---|
| WAAR overslaan en direct naar tarief | Eerst plaats bepalen — als plaats ≠ België: geen Belgische BTW | Vier kernvragen in volgorde WAAR-WAT-WANNEER-WIE |
| Verleggingsregeling = "geen BTW" | BTW blijft verschuldigd, alleen schuldenaar verschuift | Rooster 55-56 invullen + rooster 59 voor aftrek (netto = 0 bij volledige aftrek) |
| B2B-toets zonder VIES-controle | Buitenlands BTW-nummer voor waar aangenomen | VIES-verificatie verplicht; quick fixes 2020: materieel-substantiële voorwaarde voor IC-vrijstelling |
| Vastgoed-uitzondering vergeten | B2B-hoofdregel toegepast op onroerende dienst | Plaats = ligging gebouw, altijd, ongeacht B2B/B2C |
| Opeisbaarheid = factuurdatum | Factuur als trigger | Chronologisch eerste: levering · betaling · factuur (B2B: factuur uiterlijk 15e volgende maand) |
| Drempel 10 000 EUR per lidstaat | Oude drempels (35k/100k per lidstaat) | Sinds 2021: EU-brede drempel 10 000 EUR voor B2C-afstandsverkopen + TBE-diensten cumulatief |

---

<div class="no-print">

## Doorklik — losse concept-fiches

**Plaats van handeling**
- [[plaats-van-handeling-btw]] — hoofdregels + uitzonderingen
- [[btw-grensoverschrijdend]] — IC-levering / IC-verwerving / OSS
- [[btw-dienstverlening]] — diensten + verlegging

**Tarief + vrijstellingen**
- [[btw-tarieven]] — 6/12/21 + uitzonderingen
- [[btw-vrijstellingen]] — art. 44 (zonder aftrek) vs art. 39-42 (met aftrek)

**Opeisbaarheid + schuldenaar**
- [[opeisbaarheid-btw]] — belastbaar feit + opeisbaarheid-trigger
- [[maatstaf-van-heffing-btw]] — wat valt in de belastbare basis

**Verwante themafiches**
- [[themafiches/btw-aftrek|Themafiche — BTW-aftrek]]
- [[themafiches/btw-vastgoed|Themafiche — BTW & vastgoed]]
- [[themafiches/grensoverschrijdende-btw|Themafiche — Grensoverschrijdende BTW]]
- [[themafiches/vrijstellingsregeling-kleine-onderneming|Themafiche — Vrijstellingsregeling KO]]

</div>

---

*Themafiche afgeleid uit cluster btw (PO 2.4). Status: voorgesteld.*
