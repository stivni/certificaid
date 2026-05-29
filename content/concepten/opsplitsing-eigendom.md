---
title: "Opsplitsing van eigendom (zakelijke rechten)"
concept_type: "kader"
schema_version: "2.2"
status: "concept"
categorieen:
  - kader
ankers:
  - 1.1.II.X
tags:
  - concept
  - schema-2.2
  - type-kader
  - cat-kader
  - status-concept
gegenereerd_uit: "data/concepten/records/opsplitsing-eigendom.json"
---

_Kader_ · ook: zakelijke rechten op onroerend goed · splitsing eigendom

## Definitie

Opsplitsing van eigendom = juridische techniek waarbij verschillende gebruiks- of genotsrechten op één goed worden verdeeld tussen meerdere personen. Drie hoofdvormen onder Belgisch recht: (1) erfpacht (Boek 3 BW, vroeger Wet 10/01/1824) = vol genot van een onroerend goed van een ander, tegen periodieke canon, looptijd 15-99 jaar; (2) opstalrecht (Wet 10/01/1824 hervormd door Boek 3 BW) = recht om te bouwen op grond van een ander, looptijd 0-99 jaar; (3) vruchtgebruik (art. 3.138 e.v. BW, vroeger art. 745 BW oud) = recht op genot + vruchten van een goed van een ander, levenslang of max. 30 jaar voor rechtspersonen, max. 99 jaar voor specifieke gevallen. Tegenover de gebruiks-genotsrechten staat de 'blote eigendom' van de oorspronkelijke eigenaar.

<small>📖 BW Boek 3 (zakelijke rechten — 2021) — Titel 5-8 — _wettekst_ · CBN-advies 2015/5 — Zakelijke rechten op onroerende goederen — _cbn_</small>

## Substantie

Waarom drie? Elk recht beantwoordt aan een specifieke economische behoefte: erfpacht voor langdurig gebruik tegen vergoeding (commercieel onroerend, vroeger landbouw); opstal voor 'bouwen op andermans grond' (windturbines, opslagloodsen, joint-venture-vastgoed); vruchtgebruik voor familiale planning (ouders geven blote eigendom aan kinderen + behouden vruchtgebruik tot overlijden — successieoptimalisatie). Boekhoudkundig (CBN 2015/5): in de regel boekt de houder van het zakelijk recht het actief op klasse 22 (gebouw) of 23 (installaties) met afschrijving over de looptijd van het recht. De blote eigenaar boekt geen actief tijdens looptijd — pas bij einde recht heropleving in klasse 22. Periodieke canon = kost (klasse 612 huur of 6602 erfpachtvergoeding).

<small>📖 CBN-advies 2015/5 — Boekhoudkundige verwerking — _cbn_</small>

## Rationale

Het systeem van zakelijke rechten verzoent twee belangen: (a) eigendomszekerheid voor langetermijn-eigenaar (familie, gemeente, religieuze instelling) en (b) gebruiks-flexibiliteit voor de exploitant. Fiscaal differentieert de wetgever: registratierechten op erfpacht/opstal slechts 5% (vroeger 2%, verhoogd in 2024 in Vlaanderen) tegenover 12% op gewone overdracht — gunsttarief stimuleert deze rechtsfiguren. Successierecht weegt op de waarde van het overgebrachte recht — vruchtgebruik dat eindigt bij overlijden van vader doet geen successie ontstaan bij kinderen die de blote eigendom hadden (waardevolle planningstool).

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Sub-concepten

### 📦 Vergelijkingsmatrix: erfpacht vs opstal vs vruchtgebruik

#### Definitie

Drie zakelijke rechten naast elkaar — termijn + tegenprestatie + objecten + boekhouding. Erfpacht: 15-99 jaar, jaarlijkse canon, onroerend goed, klasse 22 bij erfpachter. Opstal: 0-99 jaar, eenmalige of periodieke prijs, recht om te bouwen op onroerend goed van ander, klasse 23 bouw bij opstalhouder. Vruchtgebruik: levenslang of max 30 jaar rechtspersonen, eenmalige of periodieke prijs, vruchten + genot van een goed, klasse 21 (immaterieel) of 22 (materieel) bij vruchtgebruiker.

<small>📖 CBN-advies 2015/5 — Vergelijking 3 zakelijke rechten — _cbn_</small>

**📋 Erfpacht vs opstal vs vruchtgebruik**

| Aspect | Erfpacht | Opstal | Vruchtgebruik |

| --- | --- | --- | --- |

| Looptijd | 15-99 jaar | 0-99 jaar | Levenslang of max 30 j (rechtspersoon) |

| Object | Onroerend goed | Recht om te bouwen op grond ander | Roerend of onroerend goed |

| Tegenprestatie | Canon (jaarlijks) | Eenmalige of periodieke prijs | Eenmalige of periodieke vergoeding |

| Eind van het recht | Looptijd OF opzegging | Looptijd OF natrekking | Overlijden / vermenging |

| Boekhouding houder zakelijk recht | Actief klasse 22 — afschrijven over looptijd | Bouwwerk klasse 22-23 — afschrijven over looptijd | Recht klasse 22 — afschrijven over looptijd |

| Boekhouding blote eigenaar | Eigendom blijft op balans (vroeger); CBN 2015/5: niet meer | Eigendom grond blijft | Eigendom blijft (zonder afschrijving) |

| Registratierechten Vlaanderen 2024 | 5% | 5% | 5% |

### 📦 Boekhoudkundige cascade per zakelijk recht

#### Definitie

Bij vestiging: houder van zakelijk recht betaalt prijs + registratierechten + notaris → activeert totaalbedrag op klasse 22 (of 21 bij vruchtgebruik op roerend goed). Afschrijving lineair over looptijd. Eind recht: actief naar 0 (volledig afgeschreven) OF resterende boekwaarde uitboeken als minderwaarde. Periodieke canon: kost 6602 'erfpachtvergoeding' of 612 'huur'.

<small>📖 CBN-advies 2015/5 — Boekhoudkundige verwerking — _cbn_ · CBN-advies 158/1 — Periodieke vergoeding — _cbn_</small>

> [!example]- Vestiging erfpacht 50 jaar — eenmalige prijs 500.000 EUR + canon 10.000/jaar
> _Zelena Bio NV neemt erfpacht op terrein van familie Janssens._
>
> **📒 (1) Vestiging — activering 500.000**
>
> | Rekening | Debet | Credit |
> | --- | --- | --- |
> | 22 — Erfpachtrecht (terrein) | 500.000 |  |
> | 550 — Bank |  | 500.000 |
>
> **📒 (2) Jaarlijkse afschrijving 500.000 / 50 = 10.000**
>
> | Rekening | Debet | Credit |
> | --- | --- | --- |
> | 6302 — Afschrijving MVA | 10.000 |  |
> | 229 — Geboekte afschrijvingen (-) |  | 10.000 |
>
> **📒 (3) Jaarlijkse canon**
>
> | Rekening | Debet | Credit |
> | --- | --- | --- |
> | 6602 — Erfpachtvergoedingen (kost) | 10.000 |  |
> | 550 — Bank |  | 10.000 |
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

> [!warning]- Zakelijk recht ≠ leasing
> **Verkeerde assumptie**: Een 30-jarige erfpacht is een vorm van leasing.
>
> **Kernpunt**: Erfpacht/opstal/vruchtgebruik zijn ZAKELIJKE rechten (volgen het goed) — eigendomstitel geregistreerd in kadaster. Leasing is een PERSOONLIJK recht (volgt persoon). Boekhoudkundig: zakelijk recht ALTIJD geactiveerd; leasing is afhankelijk van klassificatie financieel vs operationeel.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!warning]- Levensduur recht vs gebruiksduur actief verwarren
> **Verkeerde assumptie**: Bij opstal 99 jaar voor gebouw afschrijving over 33 jaar (technische levensduur gebouw).
>
> **Kernpunt**: Bij ZAKELIJK recht: afschrijving over de juridische looptijd van het recht (de kortste van juridisch + technisch). Opstal 50 jaar voor gebouw met 33-jarige levensduur → afschrijven over 33 jaar. Maar opstal 20 jaar voor zelfde gebouw → afschrijven over 20 jaar (verlies recht doet boekwaarde verdwijnen).
>
> <small>📖 CBN-advies 2015/5 — Afschrijving zakelijke rechten — _cbn_</small>

## Accountant-perspectieven

### Onderneming als houder OF blote eigenaar van zakelijk recht

#### 🧭 Adviseur

##### 🧭 Welk zakelijk recht kiezen?

Klant wil langdurig gebruik onroerend goed zonder volle aankoop: vergelijk erfpacht (jaarlijkse canon, max 99 jaar, einde teruggave) ↔ opstal (vooral als zelf bouwen op andermans grond) ↔ vruchtgebruik (familiale planning, levenslang). Argumenten: cash flow (canon vs eenmalige prijs), looptijd-zekerheid, fiscale optimalisatie successie (vruchtgebruik > opstal > erfpacht voor planning), btw-implicaties (vruchtgebruik op nieuw gebouw = btw met aftrekrecht).

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Erfpacht-specifiek (15-99 jaar) → [[erfpacht]] _(moet-verwijzen)_
- → Opstal-specifiek (accessoir recht) → [[opstal]] _(moet-verwijzen)_
- → Vruchtgebruik (incl. blote-eigendom-perspectief) → [[vruchtgebruik]] _(moet-verwijzen)_

## Relaties

### `bevat`
- [[erfpacht]]
- [[opstal]]
- [[vruchtgebruik]]
### `valt_onder`
- [[vaste-activa]] — Drie sub-vormen worden ondergebracht in klasse 22-23 (MVA).
