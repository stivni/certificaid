---
title: Waardeverminderingen
tags:
- concept
- cluster
- po-1-1
- po-1-2
linked_anchors:
- 1.1.II.B
- 1.1.II.C
- 1.1.II.E
- 1.1.II.F
- 1.1.II.G
- 1.2.V.B
- 1.2.V
- 1.2.taak.1
programmaonderdelen:
- '1.1'
- '1.2'
confidence: grounded
node_type: cluster
status: seed
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/waardeverminderingen.json
gegenereerd_op: '2026-05-18'
---
# Waardeverminderingen ⚖️

Correcties boeken op de aanschaffingswaarde van actiefbestanddelen om rekening te houden met **al-dan-niet-definitieve ontwaardingen** op balansdatum — voor activa met **onbeperkte gebruiksduur** of voor **vlottende activa** (voorraden, vorderingen, geldbeleggingen).

> [!summary] Korte inhoud
> Onder **waardeverminderingen** verstaat men de correcties op de aanschaffingswaarde van actiefbestanddelen — andere dan die met beperkte gebruiksduur (waarvoor afschrijvingen gelden) — om rekening te houden met al dan niet als definitief aan te merken ontwaardingen bij het afslui….

Onder **waardeverminderingen** verstaat men de correcties op de aanschaffingswaarde van actiefbestanddelen — andere dan die met beperkte gebruiksduur (waarvoor afschrijvingen gelden) — om rekening te houden met al dan niet als definitief aan te merken ontwaardingen bij het afsluiten van het boekjaar. Toepassing: terreinen (onbeperkt), financiële vaste activa, voorraden, handelsvorderingen, geldbeleggingen. De gecumuleerde waardeverminderingen worden in mindering gebracht van de actiefposten waarop ze betrekking hebben (KB WVV art. 3:23, lid 2).

_Bron: KB WVV art. 3:23_


## Bouwstenen

### Wanneer waardevermindering vs afschrijving ⚖️

Afschrijving = activa met BEPERKTE gebruiksduur (gebouw, machine, software). Waardevermindering = activa met ONBEPERKTE gebruiksduur (terrein, financiële vaste activa) of VLOTTENDE activa (voorraden, handelsvorderingen, geldbeleggingen).

**Waarom?** Beperkte gebruiksduur impliceert een gestructureerd plan; onbeperkte gebruiksduur of vlottende activa hebben geen 'natuurlijke' afnamecurve, dus eventuele correcties zijn ad-hoc reactie op vastgestelde ontwaarding.



Naaiatelier Ninove BV bezit een terrein (aanschaffingswaarde € 320.000) en een gebouw erop (€ 480.000). Het gebouw wordt jaarlijks afgeschreven; het terrein NIET. Als het terrein verontreinigd geraakt en € 90.000 zakt in waarde → waardevermindering op terrein.

_Grondslag: KB WVV art. 3:23 lid 1 vs lid 2_

### Geboekt op rekening eindigend op 9 ⚖️

Gecumuleerde waardeverminderingen verschijnen op rekeningen waarvan de subrekening eindigt op 9 (bv. 409 'Geboekte waardeverminderingen op handelsvorderingen', 349 'Geboekte waardeverminderingen op voorraad', 519 'Geboekte waardeverminderingen op geldbeleggingen').

**Waarom?** Het MAR-systeem groepeert correctierekeningen consistent: 0 = aanschaffingswaarde, 8 = meerwaarden, 9 = afschrijvingen/waardeverminderingen. Zo is de bruto-aanschaffingswaarde altijd zichtbaar.



Op de balans van Meubelzaak Mertens BV: rekening 400 Handelsdebiteuren € 145.000; rekening 409 Geboekte waardeverminderingen op handelsvorderingen € −12.600. Netto klantenvordering = € 132.400.

_Grondslag: MAR + KB WVV art. 3:23_

### Terugname als ontwaarding wegvalt 🤖

Wanneer de oorzaak van de ontwaarding wegvalt (klant betaalt alsnog, voorraadprijs herstelt, financiële markt veert op), wordt de eerder geboekte waardevermindering teruggenomen ten gunste van het resultaat.

**Waarom?** De waardevermindering reflecteert een toestand op balansdatum; als die toestand wijzigt, moet ook de boekhouding worden bijgewerkt.



Klant X van Meubelzaak Mertens betaalt onverwacht € 15.000 van de € 18.000 vordering. Terugname waardevermindering: van € 12.600 wordt € 9.600 teruggenomen (€ 15.000 effectief ontvangen × 70 % was geprovisioneerd → 70 % × € 15.000 = € 10.500 niet meer nodig; pragmatisch terugname op niveau van de werkelijke ontvangst). Boeking: Debet 409 / Credit 7340 Terugname waardeverminderingen.

_Grondslag: KB WVV art. 3:23 + algemene voorzichtigheid_


## In de praktijk

<h3 id="voorzichtigheid-voorzien-zodra-waarschijnlijk">Voorzichtigheid: voorzien zodra waarschijnlijk</h3>

> [!tip]- Voorzichtigheid: voorzien zodra waarschijnlijk
> Waardevermindering wordt al geboekt zodra de ontwaarding waarschijnlijk is — niet pas wanneer ze 'zeker' is. Een vordering op een klant met betalingsmoeilijkheden wordt niet gewacht tot de curator een dividend bekendmaakt; de ontwaarding moet redelijk geraamd worden bij afsluiting. ⚖️

> [!tip]- Herkennen op het examen
> Examen: 'klant heeft 6 maanden niet betaald, advocaat aangemaand' — waardevermindering verplicht in lopend boekjaar.


> [!info]- Niet verwarren met [[afschrijvingen]]
> Afschrijvingen: planmatig, voor activa met beperkte gebruiksduur (gebouw, machine, software, oprichtingskosten). Waardeverminderingen: ad-hoc, voor activa met onbeperkte gebruiksduur (terrein) of vlottende activa (voorraden, vorderingen, geldbeleggingen).
>
> _Trigger_: Examen: 'voorraad goederen waarvan marktprijs daalt' → waardevermindering (vlottend actief). 'machine waarvan technische ontwaarding sneller dan voorzien' → niet-recurrente afschrijving (beperkte gebruiksduur).

> [!info]- Niet verwarren met [[voorzieningen]]
> Waardevermindering = correctie op een specifiek actief; staat aan actiefzijde als negatieve correctie. Voorziening = passief-post voor toekomstig risico/last; staat aan passiefzijde.
>
> _Trigger_: Examen: 'wij verwachten een vonnis tegen ons van € 80.000' → voorziening. 'klant zal vermoedelijk niet betalen' → waardevermindering.


## Valkuilen

> [!warning]- Waardevermindering is GEEN voorziening
> ⚠️ Waardevermindering is GEEN voorziening. Waardevermindering = correctie op een specifiek actief (vordering, voorraad, terrein). Voorziening = passief-post voor een toekomstig risico of last (rechtsgeding, herstelling). Examen: 'reservering voor een toekomstig gerechtelijk verlies' → voorziening, niet waardevermindering. 🤖
>
> _Bron: KB WVV art. 3:11 (voorzieningen) vs. 3:23 (waardeverminderingen)_



## Zie ook

- **Wordt voorondersteld in** (2): [[bedrijfsvorderingen]] · [[voorraden]]
## Voorbeelden

Meubelzaak Mertens BV heeft een handelsvordering van € 18.000 op klant X. Op balansdatum 31/12 wordt klant X dubbel aangemaand zonder reactie; advocaat schat 70 % verlies. Waardevermindering = 70 % × € 18.000 = € 12.600. Boeking: Debet 6340 Waardeverminderingen op handelsvorderingen € 12.600 / Credit 409 Geboekte waardeverminderingen op handelsvorderingen € 12.600.

## Bronnen

[^1]: `KB-WVV-2019__art_3_18`
[^2]: `CBN-2019-04-gevolgen-op-gebied-van-financiele-rapportering-als-gevolg-van-de-bre__sec_afwaardering-van-vlottende-en-vaste-activa`
[^3]: `MAR-ondernemingen__art_2`
