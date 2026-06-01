---
title: "Themafiche — Eindejaarsverrichtingen & waardering"
description: "Themafiche voor sub-cluster eindejaarsverrichtingen + waarderingsregels (PO 1.1): inventaris, afschrijvingen, waardeverminderingen, voorzieningen, herwaarderingen"
tags:
  - themafiche
  - po-1.1
  - cluster-boekhouding
---

<div class="no-print">

> ⚠️ **Voorlopig — themafiche-laag wordt uitgefaseerd.** Per **ADR-039** vervangt één PO-samenvatting per programmaonderdeel de cluster-themafiches. Deze fiche blijft beschikbaar tot het relevante PO een leerpad krijgt — dan migreert de inhoud naar `content/studiemateriaal/<po-slug>/samenvatting.md`. Voor cross-PO themafiches (vergelijkingen tussen verschillende PO's) volgt een aparte beslissing per fiche: incorporeren in alle relevante samenvattingen, óf upgraden naar concept-fiche.

</div>

<div class="no-print">

> **Themafiche — kapstok voor herhaling.** Van inventaris tot afsluit: vijf waarderingsoperaties in vaste cadans. Voor verhaal en routekaart: [[studiemateriaal/1-1|overzicht PO 1.1]].

</div>

---

## Take-away

- **Inventaris ≠ voorraadtelling** — art. III.89 WER eist volledige waarderingsoefening op **alle** activa en passiva, niet alleen voorraad
- **Bestendigheid is dwingend** — eenmaal vastgelegde waarderingsregels gelden van jaar tot jaar; wijziging vereist motivering in toelichting
- **Afschrijving = systematisch · waardevermindering = bijkomstig** — twee verschillende mechaniek (lineair plan vs duurzame minderwaarde) met verschillende klasse-impact
- **Voorzichtigheid asymmetrisch** — niet-gerealiseerde verliezen wél, niet-gerealiseerde winsten niet (behalve in beperkte herwaarderings-context)
- **Overlopende rekeningen = matching-correctie** — kosten/opbrengsten in juiste periode plaatsen ongeacht facturatie-moment

---

## Vijf eindejaarsoperaties — vaste cadans

| Operatie | Wat? | MAR-klasse | Trigger |
|---|---|---|---|
| **Inventaris** | Tellen + waarderen alle activa/passiva | n.v.t. (procedure) | Art. III.89 WER · jaarlijks |
| **Afschrijvingen** | Systematische spreiding kostprijs vaste activa | 630-639 (kost) · 28X9 (cum.) | Plan op basis economische levensduur |
| **Waardeverminderingen** | Duurzame minderwaarde activum | 631-634 (kost) · per actief-klasse | Bewezen / waarschijnlijke minderwaarde |
| **Voorzieningen** | Voorzichtigheid voor risico/kost | 631 (kost) · 16 (passief) | Zekere oorzaak · onzekere termijn/bedrag |
| **Overlopende rekeningen** | Matching-correctie kosten/opbrengsten | 49 (passief) · 89 (actief) | Periode-toewijzing los van facturatie |

---

## Voorzieningen vs waardeverminderingen — verwarrende paren

| Aspect | **Voorziening** | **Waardevermindering** |
|---|---|---|
| Plek op balans | Passief (klasse 16) | Correctie op actief (-) |
| Oorsprong | Toekomstig risico of kost | Bestaande activum-mindering |
| Voorbeeld | Pensioenverplichting · waarborg | Dubieuze klant · voorraadverlies |
| Voorzichtigheid | Voorzichtigheidsbeginsel | Realiteits-correctie |
| CBN-kader | CBN 107/9 (voorzieningen) | CBN 174/1 (inventaris) |

---

## Waarderings-keuzes — kernregels

**Vaste activa**
- Aanschaffingswaarde inclusief bijkomende kosten (transport, installatie)
- **Geactiveerde rente**: art. 38 KB 29-04-2019 — interest tijdens constructie kan opgenomen; vereist vermelding in toelichting
- **Herwaardering**: art. 57 KB — duurzame meerwaarde + verzekerd → herwaarderings-meerwaarde in eigen vermogen (klasse 12); geen winst

**Voorraden**
- Aanschaffingswaarde of vervaardigingsprijs (laagste)
- Methodes: FIFO, gewogen gemiddelde — **LIFO niet meer toegelaten** (sinds 2003)
- Waardevermindering bij netto-realisatiewaarde < boekwaarde

**Vorderingen**
- Nominale waarde
- Waardevermindering individueel (specifieke dubieuze klant) of forfaitair (statistisch)
- Ouderdoms-staat verplicht onderdeel klanten-analyse

---

## ⚠️ Valkuilen

| Valkuil | Wat klopt er niet | Wat klopt wél |
|---|---|---|
| Inventaris = voorraadtelling | Art. III.89 WER + CBN 174/1 eist alle activa/passiva | Voorraad-telling + bank-afstemming + vorderings-review + voorzieningen-update + reservecontrole |
| Voorziening = waardevermindering | Twee verschillende mechanieken | Voorziening = passief (toekomstig); waardevermindering = actief-correctie (bestaand) |
| Afschrijvingsplan = fiscale tabel | Boekhoudkundige afschrijving volgt economische levensduur; fiscaal kan verschillen | Boekhoudkundig waar; fiscale aftrekbaarheid apart geregeld via WIB (cross VenB) |
| Herwaardering = winst | Klasse 12 herwaarderingsmeerwaarde komt **niet** door resultaat | Direct in EV; pas bij realisatie via klasse 76 in resultaat |
| Overlopende rekeningen = boekingsfout | Matching-principe vraagt periode-toewijzing los van factuur-moment | Klasse 49 (over te dragen kost/opbrengst) + 89 (verkregen/te ontvangen) = correctie, geen fout |
| LIFO bij voorraad | Niet meer toegelaten onder B-GAAP sinds KB 30-12-2002 | FIFO of gewogen gemiddelde — IFRS verbiedt LIFO ook (IAS 2) |

---

<div class="no-print">

## Doorklik — losse concept-fiches

**Procedure**
- [[eindejaarsverrichtingen]] — inventaris + afsluit-cyclus
- [[boekhoudbeginselen]] — 8 beginselen (waaronder bestendigheid + voorzichtigheid)

**Balansposten met specifieke waarderingsregels**
- [[vaste-activa]] — IMA + MVA + FVA · afschrijving + waardevermindering
- [[voorraden]] — FIFO/GMP · netto-realisatiewaarde
- [[handelsvorderingen]] — dubieuze · forfaitaire/individuele waardevermindering
- [[voorzieningen]] — pensioenen · garanties · grote herstellingen
- [[overlopende-rekeningen]] — matching-correctie klasse 49 + 89
- [[uitgestelde-belastingen]] — timing-verschillen (cross VenB)

**Specifieke regimes**
- [[geactiveerde-rente]] — art. 38 KB 29-04-2019
- [[herwaardering-vast-actief]] — art. 57 KB · klasse 12

**Verwante samenvattingen + themafiches**
- [[studiemateriaal/1-2/samenvatting|Samenvatting PO 1.2 — Boekhoudrecht en jaarrekeningenrecht]] *(jaarrekening-schema + publicatie + sancties)*
- [[themafiches/resultaten-en-resultaatverwerking|Themafiche — Resultaten & resultaatverwerking]]
- [[studiemateriaal/1-5/samenvatting|Samenvatting PO 1.5 — IFRS en EU-kader]] *(BE-GAAP↔IFRS-vergelijking per balanspost)*

</div>

---

*Themafiche afgeleid uit cluster boekhouding (PO 1.1). Status: voorgesteld.*
