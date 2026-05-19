---
title: Stelselwissel jaarrekening (BE GAAP ↔ IFRS)
tags:
- concept
- cluster
- po-1-5
linked_anchors:
- 1.5.III
- 1.5.IV.A
programmaonderdelen:
- '1.5'
confidence: inferred-from-aggregation
node_type: cluster
status: seed
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/stelselwissel-jaarrekening.json
gegenereerd_op: '2026-05-18'
---
# Stelselwissel jaarrekening (BE GAAP ↔ IFRS) 🤖

Bij beursintroductie of moederwissel (BE GAAP → IFRS) gebeurt de overgang via IFRS 1. Bij delisting of vrijwillige terugkeer (IFRS → BE GAAP) gebeurt de overgang via CBN-advies 2022/08. In beide gevallen zit de uitdaging in retroactieve herwerking versus prospectieve voortzetting: welke balansposten moeten herwerkt, welke disclosures verplicht.

> [!summary] Korte inhoud
> Een stelselwissel is de eenmalige overgang van het ene boekhoudkundige referentiestelsel naar het andere — typisch tussen Belgisch GAAP en IFRS, in beide richtingen.

> [!info] Behoort tot: [[jaarrekening]]

Een stelselwissel is de eenmalige overgang van het ene boekhoudkundige referentiestelsel naar het andere — typisch tussen Belgisch GAAP en IFRS, in beide richtingen. De wissel gebeurt op een overgangsdatum waarop een openingsbalans wordt opgesteld onder het nieuwe stelsel, met expliciete aansluitingsverklaring tussen het oude en het nieuwe stelsel.

_Bron: Synthese IFRS 1 + CBN 2022/08_


## Bouwstenen

### Twee richtingen, twee regimes ⚖️

Overgang BE GAAP → IFRS volgt IFRS 1 (First-time Adoption). Overgang IFRS → BE GAAP volgt CBN 2022/08. Beide regimes vereisen een openingsbalans onder het nieuwe stelsel; beide kennen vrijstellingen en uitzonderingen op volledige retroactieve herwerking.

**Waarom?** Hoewel de regimes verschillende juridische bronnen hebben, deelt de stelselwissel hetzelfde economische probleem: balanscijfers en resultaten vertonen een breuk; aansluitingen overbruggen die breuk voor de gebruiker.




_Grondslag: IFRS 1 alinea 6-9; CBN 2022/08 Standpunt_

### Continuïteit versus breuk ⚖️

Het algemene principe is **continuïteit van waarderingsregels** (geen retroactieve herwerking). De uitzonderingen — IFRS 1 §10 verplichte aanpassingen, CBN 2022/08 cumulatieve voorwaarden — gelden alleen wanneer het oude regime een waardering oplevert die in het nieuwe regime niet houdbaar is.

**Waarom?** Continuïteit beschermt de vergelijkbaarheid over tijd, breuken zijn enkel toegestaan waar getrouw beeld of regimevoorschriften dat eisen. Stagiair moet beide spanningen kennen.




_Grondslag: IFRS 1 alinea 7; CBN 2022/08 §Continuïteitsbeginsel_

### Aansluitingen voor de gebruiker ⚖️

Bij elke stelselwissel verlangt het nieuwe regime een aansluitingsverklaring: eigen vermogen op de overgangsdatum onder oud versus nieuw stelsel, en (voor IFRS 1) ook op het einde van de laatste vergelijkbare periode. Onder BE GAAP-richting is de verklaring eerder een toelichting in het jaarverslag dan een verplichte gestructureerde tabel.

**Waarom?** Zonder aansluiting kan de gebruiker de breuk niet plaatsen. Examen toetst regelmatig welke aansluitingen IFRS 1 expliciet eist (eigen vermogen + totaalresultaat).




_Grondslag: IFRS 1 alinea 24; CBN 2022/08 §Boekhoudkundige verwerking_


> [!info]- Niet verwarren met [[wijziging-boekhoudkundig-referentiestelsel]]
> Algemeen cluster dekt regime-overstijgende kern (continuïteit als gemene deler, twee richtingen, aansluitingen). CBN 2022/08-record dekt specifiek de richting IFRS → BE GAAP statutair.
>
> _Trigger_: Algemeen → 'wat zijn de gemeenschappelijke principes bij elke stelselwissel?'; CBN-record → 'wat zegt CBN 2022/08 over de uitzonderingen?'

> [!info]- Niet verwarren met [[ifrs-eerste-toepassing]]
> Algemeen cluster dekt regime-overstijgende kern. IFRS-1-record dekt specifiek de richting BE GAAP → IFRS.
>
> _Trigger_: Algemeen → 'welke aansluitingen vraagt elke wissel?'; IFRS-1-record → 'welke vrijstellingen kent IFRS 1?'


> [!todo] Voorbeeld ontbreekt voor dit concept
> Een latere ENRICH-pass voegt een synthese-voorbeeld toe.

## Bronnen

[^1]: `IFRS-1-eerste-toepassing-IFRS__sec_openingsbalans`
[^2]: `CBN-2022-08-wijziging-van-het-boekhoudkundig-referentiestelsel__sec_inleiding`
[^3]: `IFRS-1-eerste-toepassing-IFRS__sec_toelichting`
