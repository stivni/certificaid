---
title: "Herwaardering van vast actief"
concept_type: "verrichting"
schema_version: "2.2"
status: "concept"
categorieen:
  - gebeurtenis
  - regeling
ankers:
  - 1.1.II.B
tags:
  - concept
  - schema-2.2
  - type-verrichting
  - cat-gebeurtenis
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/herwaardering-vast-actief.json"
---

_Verrichting_ · ook: herwaarderingsmeerwaarde

## Definitie

Herwaardering van een vast actief = de boekwaarde van een MVA of FVA verhogen naar de hogere actuele waarde, met als tegenboeking een 'herwaarderingsmeerwaarde' in het eigen vermogen (klasse 12). Wettelijke basis: art. 57 KB 29.04.2019 (uitvoering WVV). Toepassingsgebied: alleen materiële vaste activa (klasse 22-27) en financiële vaste activa (klasse 28 — deelnemingen en aandelen). Voorwaarden (art. 57 § 1): (a) duurzame waarde verhoogd boven aanschaffingswaarde; (b) waarde rechtvaardigt economisch nut activum; (c) waarde overschrijdt boekwaarde op materiële wijze; (d) consistent over vergelijkbare activa.

<small>📖 KB 29.04.2019 — art. 57 — _kb_ · CBN-advies 2011/14 — Herwaarderingsmeerwaarden — _cbn_</small>

## Substantie

Stagiair moet onthouden: (1) Herwaardering ≠ terugneming afschrijving. Afschrijving terugnemen = correctie eerdere foutieve afschrijving (uitzonderlijk, CBN 2011/14). Herwaardering = nieuwe waarde-vaststelling boven oorspronkelijke aanschaffingswaarde. (2) Geen impact op resultaat. Meerwaarde gaat naar klasse 12 (eigen vermogen) — niet naar 763 resultaat. (3) Verplicht jaarlijks toetsen of meerwaarde nog bestaat — bij waardedaling: corrigeren (CBN 2011/14). (4) Fiscaal niet belastbaar zolang in eigen vermogen blijft (uitgedrukte maar niet-gerealiseerde meerwaarde, art. 44 WIB92). Bij realisatie (verkoop activum): meerwaarde wordt belastbaar.

<small>📖 CBN-advies 2011/14 — Onderscheid + correctie — _cbn_ · WIB92 — art. 44 — _wettekst_</small>

## Rationale

Herwaardering doorbreekt het 'aanschaffingswaarde-principe' (waardering op kostprijs minus afschrijvingen) voor situaties waar de werkelijke economische waarde aanzienlijk en duurzaam hoger ligt — typisch oude gebouwen waarvan de marktwaarde door inflatie/aantrekkelijkheid stijgt. De wetgever beperkt dit STRICT: enkel MVA + FVA, niet voorraden of vorderingen; alleen duurzame waarde-verhoging (geen tijdelijke marktbubbel); meerwaarde in eigen vermogen (geen uitkeerbare winst). IFRS IAS 16 'revaluation model' is breder (alle waarderings-componenten, ook neerwaartse herziening via OCI). Voor de stagiair-analyse: een onderneming met grote rubriek 12 'herwaarderingsmeerwaarden' heeft een verleden van actieve herwaardering — niet noodzakelijk slecht maar wel signaal voor onderzoek.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Sub-concepten

### 📦 Voorwaarden art. 57 KB

#### Definitie

(1) Toepassingsgebied beperkt tot MVA (klasse 22-27) + FVA (deelnemingen + aandelen klasse 28). NIET op IMA, voorraden, vorderingen, geldbeleggingen klasse 5. (2) Duurzaam karakter: niet één toevallige waardestijging maar volgehouden hogere waarde. (3) Materieel verschil met boekwaarde. (4) Bewijs van waarde: meestal externe taxatie (vastgoed-expert, accountant). (5) Consistent toepassen op vergelijkbare activa-klassen.

<small>📖 KB 29.04.2019 — art. 57 § 1 — _kb_</small>

### 📦 Boekhoudkundige verwerking

#### Definitie

(1) Activum verhogen tot nieuwe waarde via rubriek ...8 'geboekte meerwaarden': bv. 2208 D voor gebouw. (2) Tegenpost in EV: 12 'herwaarderingsmeerwaarden' (sub 121 op MVA + 122 op FVA + 123 op deelnemingen) C. (3) Latere afschrijving rekent op nieuwe (hogere) boekwaarde — overschot van afschrijving wordt opbrengst uit terugneming herwaarderingsmeerwaarde 760. (4) Jaarlijkse toets: nog steeds gerechtvaardigd? Bij waardedaling: 12 D / 2208 C (correctie).

<small>📖 KB 29.04.2019 — art. 57 — _kb_ · CBN-advies 2011/14 — Correctie herwaarderingsmeerwaarden — _cbn_</small>

> [!example]- Herwaardering gebouw: boekwaarde 200.000 → marktwaarde 350.000
> _Zelena Bio NV bezit kantoorgebouw aanschaffingswaarde 250.000, geaccumuleerde afschrijvingen 50.000 = boekwaarde 200.000. Taxatie 2026: 350.000 EUR._
>
> **📒 Boeking herwaardering 150.000**
>
> | Rekening | Debet | Credit |
> | --- | --- | --- |
> | 2208 — Geboekte herwaarderingsmeerwaarden gebouwen | 150.000 |  |
> | 121 — Herwaarderingsmeerwaarden op MVA |  | 150.000 |
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

> [!warning]- Herwaarderingsmeerwaarde als winst boeken
> **Verkeerde assumptie**: Een herwaardering van 150.000 EUR = winst die kan worden uitgekeerd.
>
> **Kernpunt**: Art. 57 KB: meerwaarde gaat naar EIGEN VERMOGEN (klasse 12) — NIET resultaat. Niet uitkeerbaar als dividend zolang meerwaarde niet 'gerealiseerd' is (verkoop activum). Het verschil met realisatie-meerwaarde (763) is essentieel.
>
> <small>📖 KB 29.04.2019 — art. 57 — _kb_</small>

> [!warning]- Herwaardering op IMA, voorraden of vorderingen
> **Verkeerde assumptie**: Alle vaste activa kunnen worden geherwaardeerd.
>
> **Kernpunt**: Art. 57 KB beperkt herwaardering tot MVA + FVA (deelnemingen + aandelen). IMA (klasse 21), oprichtingskosten (20), voorraden, vorderingen mogen NIET worden geherwaardeerd. Uitzondering: tussentijdse opwaardering bij IMA-overgang naar IFRS — daar moet de stagiair de Be-GAAP-beperking kennen.
>
> <small>📖 KB 29.04.2019 — art. 57 § 1 — _kb_</small>

> [!warning]- Jaarlijkse toets vergeten
> **Verkeerde assumptie**: Een eenmaal geboekte herwaardering blijft op de balans.
>
> **Kernpunt**: CBN 2011/14: jaarlijks op inventarisdatum nagaan of meerwaarde nog bestaat. Bij waardedaling: meerwaarde corrigeren (12 D / activum C). Negeren is overtreding van het voorzichtigheidsbeginsel + auditor-aandachtspunt.
>
> <small>📖 CBN-advies 2011/14 — Correctie herwaarderingsmeerwaarden — _cbn_</small>

## Accountant-perspectieven

### Onderneming zelf

#### 📒 Boekhouder

##### 👣 Implementatie + jaarlijkse opvolging

Bij vestiging: externe taxatie + raad-van-bestuur-besluit + boeking. Toelichting bij jaarrekening: vermelding waarderingsgrondslag, vergelijkende meerwaarde-tabel. Jaarlijks: herziening met taxatie of marktindicator.

<small>📖 KB 29.04.2019 — art. 57 + toelichting — _kb_</small>

#### 🔍 Auditor

##### 👣 Toets herwaarderings-bewijs + duurzaamheid

Vraag taxatieverslag op + onafhankelijkheid taxateur. Toets methode (marktbenadering, inkomstenbenadering). Vergelijk met andere indicatoren (kadastrale waarde, vorige verkoop in omgeving). Bij FVA: dochter-JR + business plan + DCF. Vraag bewijs van duurzaam karakter (geen tijdelijke bubbel).

<small>📖 ISA 540 — Schattingen — _norm_ · ISA 620 — Werk van een deskundige — _norm_</small>

#### 💰 Fiscaal adviseur

##### 📜 Fiscale behandeling — art. 44 WIB92

WIB92 art. 44: 'uitgedrukte maar niet-verwezenlijkte meerwaarden' zijn vrijgesteld zolang ze (a) in onaantastbaarheids-rekening in EV blijven (klasse 12) en (b) niet uitgekeerd worden. Bij overdracht of uitkering: meerwaarde wordt belastbaar. Toelichting + onaantastbaarheids-vereiste in fiscaal aangifte VenB.

<small>📖 WIB92 — art. 44 — _wettekst_</small>

## Verder lezen (scope-out)

- → Vaste activa generiek → [[vaste-activa]] _(moet-verwijzen)_
- → Eigen vermogen (klasse 12 herwaarderings-meerwaarden) → [[eigen-vermogen]] _(moet-verwijzen)_
- ↪ IFRS — IAS 16 revaluation model → [[materiele-vaste-activa]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[vaste-activa]]
### `alternatief_referentiestelsel`
- [[materiele-vaste-activa]] — IAS 16 'revaluation model' — IFRS-variant van Be-GAAP herwaardering.
