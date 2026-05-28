---
title: "Resultaatverwerking"
concept_type: "procedure"
schema_version: "2.2"
status: "concept"
categorieen:
  - gebeurtenis
ankers:
  - 1.1.II.Q
tags:
  - concept
  - schema-2.2
  - type-procedure
  - cat-gebeurtenis
  - status-concept
gegenereerd_uit: "data/concepten/records/resultaatverwerking.json"
---

# Resultaatverwerking

_Procedure_

📅 Gebeurtenis · Anchors: `1.1.II.Q` · Wave: `extract-jaarrekening-rest-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: winstbestemming · resultaatbestemming · klasse 79

## Definitie

📖 **Resultaatverwerking** is de procedure waarbij het **te bestemmen resultaat** van het boekjaar (winst of verlies) wordt **toegewezen** aan verschillende bestemmingen: opbouw van wettelijke reserve, statutaire reserves, beschikbare reserves, overgedragen resultaat naar het volgende boekjaar, en uitkering aan aandeelhouders (dividend). Dit gebeurt formeel door de **algemene vergadering** op voorstel van het bestuursorgaan, ten laatste **zes maanden** na de afsluitdatum van het boekjaar. Het resulterende **bestemmingsschema** wordt boekhoudkundig vastgelegd via **MAR-klasse 79 — Resultaatverwerking** en bepaalt mee de presentatie van de **balans na toewijzing** (art. 3:3 KB).

<small>📚 KB 29-04-2019 WVV — art. 3:3 — _kb_ · WVV — art. 3:1 — _wettekst_</small>

## Substantie

📖 **Bestemmingsschema** (verplicht onderdeel van de toelichting bij de jaarrekening):

```
Te bestemmen resultaat (= winst/verlies van het boekjaar + overgedragen resultaat vorige periode)
├── Onttrekking aan eigen vermogen (bv. terugneming kapitaal-meerwaarden) (793)
├── Toevoeging aan eigen vermogen:
│   ├── 791 Toevoeging wettelijke reserve (5% winst tot 10% kapitaal)
│   ├── 792 Toevoeging onbeschikbare reserves (statutair of decisie AV)
│   └── 793 Toevoeging beschikbare reserves
├── Over te dragen resultaat naar volgend boekjaar (794)
├── Tussenkomst vennoten in verlies (795)
└── Vergoeding op kapitaal — dividend aan aandeelhouders (796)
```

**Verplichte volgorde**:
1. **Wettelijke reserve** — 5 % van de nettowinst (na verliezen vorige jaren) moet jaarlijks worden afgehouden zolang de wettelijke reserve minder dan **10 % van het kapitaal** bedraagt (WVV art. 7:211 voor NV, art. 5:153 voor BV);
2. **Statutaire reserves** — indien voorzien in de statuten;
3. Overige bestemmingen (dividend, beschikbare reserves, overgedragen winst) — vrij te beslissen door de AV mits naleving van uitkeringstests.

<small>📚 KB 21-10-2018 — MAR — Klasse 79 — _kb_ · WVV — art. 7:211 — _wettekst_</small>

## Rationale

🔗 De resultaatverwerking is het scharniermoment tussen **economisch resultaat** (winst van het boekjaar) en **juridische realisatie** (uitkering vs. interne aanhouding). De wettelijke reserve dient de **kapitaalbescherming**: ze creëert een groei-buffer die niet uitkeerbaar is — schuldeisers hebben hierdoor een grotere zekerheidsmarge. De statutaire reserves laten aandeelhouders toe contractueel afspraken te maken over winstinhouding (bv. voor groei-investeringen). Het dividend tenslotte realiseert het **vergoeding-voor-risicokapitaal**-principe. Onder het WVV is dit alles onderworpen aan de **dubbele uitkeringstest** voor BV en CV (nettoactieftest + liquiditeitstest) om kapitaalbescherming te garanderen.

<small>📚 WVV — art. 5:142 (BV), 7:212 (NV) — _wettekst_</small>

## Bouwstenen

### 👣 Boeking van te bestemmen winst  
_`stap`_

🔗 **Scenario**: Een BV met kapitaal 100.000 EUR sluit het boekjaar af met een winst van **50.000 EUR**. De wettelijke reserve bedraagt momenteel 8.000 EUR. De AV besluit:
- 5 % naar wettelijke reserve (2.500 EUR — totaal wordt 10.500 EUR < 10.000 EUR... eigenlijk volledig 2.000 EUR want max bereikt bij 10.000 EUR, dan stoppen)
- 10.000 EUR dividend
- saldo naar overgedragen winst

**Stap 1 — afsluit resultaat** (boekjaar einde):
De resultaten 60-66/70-76 saldo gaat naar **rekening 690 Te bestemmen winst** (debet voor verlies, credit voor winst).

**Stap 2 — bestemming via klasse 79**:
```
691 Te bestemmen winst (debet, beschikbaar) D 50.000
   791 Toevoeging wettelijke reserve         C 2.000
   796 Dividenden                            C 10.000
   794 Over te dragen winst                  C 38.000
```

**Stap 3 — uitbetaling dividend** (na AV-goedkeuring):
```
796 Dividenden (al gedebiteerd)              D 10.000
   471 Schuld dividend                        C 10.000
```
Bij effectieve betaling: rekening 471 D | 55 Bank C.

<small>📚 KB 21-10-2018 — MAR — Klasse 79 + Klasse 47 — _kb_</small>

### 📜 Wettelijke reserve — 5%/10%-regel  
_`regel`_

📖 Voor de NV (WVV art. 7:211) en BV (art. 5:153): **5 %** van de jaarlijkse nettowinst moet worden toegevoegd aan de wettelijke reserve, totdat deze reserve **10 %** van het kapitaal/inbreng bereikt. Daarna kan toevoeging stoppen. Bij vermindering van het kapitaal door verliezen kan de wettelijke reserve eveneens worden aangetast — en moet weer worden opgebouwd.

Functioneel: de wettelijke reserve is een **niet-uitkeerbare buffer** boven het kapitaal die alleen kan worden aangewend voor verlies-compensatie of kapitaalverhoging.

<small>📚 WVV — art. 7:211 (NV) + art. 5:153 (BV) — _wettekst_</small>

## Valkuilen

### ⚠️ Wettelijke reserve overslaan bij dividend-voorstel

**Verkeerde assumptie**: Een vennootschap met 10 % kapitaal in wettelijke reserve hoeft nooit meer iets toe te voegen, ook niet na een tussentijds verlies.

**Kernpunt**: Wanneer de wettelijke reserve **onder de 10 %**-drempel zakt (bv. door aanwending tegen verlies), moet ze opnieuw worden aangevuld via de 5%-regel op latere winsten. De drempel is **dynamisch**, niet een eenmalige verworvenheid.

<small>📚 WVV — art. 7:211 + 5:153 — _wettekst_</small>

### ⚠️ Dividend uitkeren zonder uitkeringstests (BV)

**Verkeerde assumptie**: De BV mag eenmaal de wettelijke reserve gevuld is vrij dividenden uitkeren.

**Kernpunt**: Voor BV en CV is sinds het WVV de **dubbele uitkeringstest** verplicht (art. 5:142-143): (1) **nettoactieftest** — eigen vermogen na uitkering ≥ 0; (2) **liquiditeitstest** — de vennootschap kan haar opeisbare schulden van de komende 12 maanden afbetalen. Zonder positief uitslag van beide tests is uitkering een **onwettige onttrekking** met aansprakelijkheid van het bestuursorgaan tot gevolg.

<small>📚 WVV — art. 5:142, 5:143 — _wettekst_</small>

## Verder lezen (scope-out)

- → Winstuitkering Σ (keuze-kader uitkeringsvormen) → [[winstuitkering]] _(moet-verwijzen)_
- → Eindejaarsverrichtingen (afsluit-cyclus) → [[eindejaarsverrichtingen]] _(moet-verwijzen)_
- ↪ Jaarrekening-presentatie → [[jaarrekening]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[boekhouding]]
### `triggert`
- [[winstuitkering]]
