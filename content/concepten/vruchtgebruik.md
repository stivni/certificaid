---
title: "Vruchtgebruik"
concept_type: "instrument"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 1.1.II.X
tags:
  - concept
  - schema-2.2
  - type-instrument
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/vruchtgebruik.json"
---

_Instrument_ · ook: usufructus

## Definitie

Vruchtgebruik (art. 3.138 e.v. BW — vroeger art. 745 e.v. BW oud) is het recht om van een zaak waarvan een ander de eigendom heeft het genot te hebben, zoals de eigenaar zelf, maar onder verplichting om de substantie te bewaren. Karakteristieken: (1) zakelijk recht; (2) op roerend OF onroerend goed; (3) levenslang voor natuurlijke personen (eindigt bij overlijden vruchtgebruiker — geen overdracht aan erfgenamen), max 30 jaar voor rechtspersonen (verlengbaar tot max 99 jaar onder voorwaarden); (4) onderscheid 'vruchtgebruiker' (heeft genot + vruchten) en 'blote eigenaar' (behoudt eigendomsrecht). Bij einde: volle eigendom keert terug naar blote eigenaar = 'vermenging' (art. 3.165 BW).

<small>📖 BW Boek 3 — art. 3.138 e.v. — _wettekst_ · CBN-advies 2015/5 — Vruchtgebruik — definitie en kenmerken — _cbn_</small>

## Substantie

Vruchtgebruik wordt vooral gebruikt voor: (a) familiale planning — ouders schenken blote eigendom huis aan kinderen + behouden vruchtgebruik tot overlijden (kinderen krijgen volle eigendom 'gratis' bij overlijden = successieoptimalisatie); (b) vennootschap-vruchtgebruik — vennootschap koopt vruchtgebruik op gebouw voor 15-20 jaar, zaakvoerder houdt blote eigendom; (c) erfgenaam-vruchtgebruik op woning langstlevende echtgenoot. Boekhoudkundig (CBN 2015/5): vruchtgebruiker activeert eenmalige instapprijs + bijhorende kosten op klasse 22 (onroerend) of 21 (roerend) — afschrijving over looptijd vruchtgebruik. Blote eigenaar tijdens vruchtgebruik: geen actief op balans (CBN 2015/5 nieuwe lijn) — eerst bij vermenging heropleving op klasse 22.

<small>📖 CBN-advies 2015/5 — Vruchtgebruiker betaalt uitsluitend periodieke vergoedingen — _cbn_</small>

## Rationale

Vruchtgebruik is het oudste zakelijk recht (Romeins recht) — bedoeld voor: (a) onderhouden van overlevende echtgenoot zonder hem/haar volle eigendom te geven; (b) gebruik scheiden van eigendom voor planning. De wetgever differentieert natuurlijke personen (levenslang — sterft met vruchtgebruiker) van rechtspersonen (max 30 j, voorkomt 'eeuwige' vruchtgebruiken voor fiscaal-optimaliserende holdings). Vennootschap-vruchtgebruik is fiscaal voordelig: vennootschap kan kosten activeren + afschrijven, terwijl de natuurlijke persoon-zaakvoerder na 15-20 jaar 'gratis' volle eigendom krijgt — vandaar veel fiscale controle (BIN 2018-23, circulaires).

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · sinds **2021-09-01** · basis: Boek 3 BW (Wet 04.02.2020)

Hervorming Boek 3 BW heeft vruchtgebruik gemoderniseerd. Hoofdregel ongewijzigd: levenslang natuurlijke personen, max 30 j rechtspersonen.

**✅ Voor**
- 🔗 Familiale successie-planning — schenking blote eigendom + behoud vruchtgebruik.
- 🔗 Vennootschap-vruchtgebruik op gebouw — fiscaal voordeel afschrijving + zaakvoerder blote eigenaar.

## Sub-concepten

### 📦 Vruchtgebruik natuurlijke persoon vs rechtspersoon

#### Definitie

NATUURLIJKE PERSOON: levenslang — eindigt bij overlijden (art. 3.159 BW). RECHTSPERSOON: max 30 jaar, verlengbaar (art. 3.158 BW). Belangrijk gevolg: bij overlijden vader-vruchtgebruiker krijgen de kinderen-blote-eigenaars gratis volle eigendom (geen successierecht op vruchtgebruik dat eindigt — art. 2.7.1.0.5 VCF).

<small>📖 BW Boek 3 — art. 3.158-3.159 — _wettekst_ · Vlaamse Codex Fiscaliteit — art. 2.7.1.0.5 — _wettekst_</small>

### 📦 Boeking vruchtgebruiker (gebruiker)

#### Definitie

Eenmalige prijs vruchtgebruik + notaris + registratierechten activeren op klasse 22 (vruchtgebruikrecht). Afschrijving lineair over looptijd vruchtgebruik. Periodieke vergoedingen (zeldzaam): kost 6602.

<small>📖 CBN-advies 2015/5 — Vruchtgebruiker — boekingen — _cbn_</small>

> [!example]- Vennootschap koopt 20-jarig vruchtgebruik op gebouw voor 400.000 EUR
> _Zelena Bio NV koopt vruchtgebruik van familie Janssens._
>
> **📒 (1) Vestiging — activering 400.000**
>
> | Rekening | Debet | Credit |
> | --- | --- | --- |
> | 22 — Vruchtgebruikrecht op gebouw | 400.000 |  |
> | 550 — Bank |  | 400.000 |
>
> **📒 (2) Jaarlijkse afschrijving 400.000 / 20 = 20.000**
>
> | Rekening | Debet | Credit |
> | --- | --- | --- |
> | 6302 — Afschrijving MVA | 20.000 |  |
> | 229 — Geboekte afschrijvingen (-) |  | 20.000 |
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

> [!warning]- Vennootschap-vruchtgebruik onbeperkt fiscaal aftrekbaar
> **Verkeerde assumptie**: Alle kosten verbonden aan vennootschap-vruchtgebruik op woning zijn aftrekbaar.
>
> **Kernpunt**: Fiscus controleert intensief: (a) marktconforme prijs vruchtgebruik (anders 'abnormaal voordeel' art. 26 WIB92); (b) effectief beroepsmatig gebruik; (c) onderhoudskosten gemengd privé/zakelijk niet volledig aftrekbaar. Veel rechtspraak hierover laatste jaren. Documenteer prijszetting + business use.
>
> <small>📖 WIB92 — art. 26 + 49 — _wettekst_</small>

> [!warning]- Vruchtgebruik = huur verwarren
> **Verkeerde assumptie**: Een 10-jarig vruchtgebruik is een vorm van huur.
>
> **Kernpunt**: Vruchtgebruik is een ZAKELIJK recht (ingeschreven in kadaster, opposable aan derden, kan worden verkocht aan derden behoudens contractuele beperking) — huur is een PERSOONLIJK recht. Vruchtgebruik wordt geactiveerd; huur is kost.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Accountant-perspectieven

### Vruchtgebruiker (gebruiker)

#### 💰 Fiscaal adviseur

##### 📜 Vennootschap-vruchtgebruik — prijszetting + business use

Prijszetting volgens leeftijds-tafels (Ruysseveldt-tabel of actuariële berekening) — niet boven marktwaarde. Documenteer effectief beroepsmatig gebruik (≥ X% beroepsmatige oppervlakte). Bij gemengd gebruik: pro rata aftrek. Bij belastingcontrole steeds: 'wat zou een derde betalen voor zelfde rechtspositie?'

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Opsplitsing-eigendom — overkoepelende vergelijking → [[opsplitsing-eigendom]] _(moet-verwijzen)_
- ↪ Vaste-activa-context (boekhouding) → [[vaste-activa]] _(mag-verwijzen)_
- ↪ Registratierechten (fiscaal) → [[registratie-en-successierechten]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[opsplitsing-eigendom]]
### `vergelijkbaar_met`
- [[erfpacht]]
    - **Gelijkenissen**:
        - Beide genotsrecht
    - **Verschillen**:
        - Vruchtgebruik: levenslang of max 30 j (rechtspersoon)
        - Erfpacht: 15-99 jaar zonder leeftijdslimiet
