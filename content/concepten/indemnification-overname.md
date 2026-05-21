---
title: Vrijwaringsmechanisme in overnameovereenkomst
tags:
- concept
- cluster
- po-3-0
linked_anchors:
- 3.0.V
- 3.0.V.A
- 3.0.V.B
- 3.0.V.E
- 3.0.V.F
programmaonderdelen:
- '3.0'
confidence: inferred
node_type: cluster
status: seed
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/indemnification-overname.json
gegenereerd_op: '2026-05-21'
---
# Vrijwaringsmechanisme in overnameovereenkomst 🔗

De vrijwaring vertaalt een R&W-schending in een betaalverplichting. Onder Belgisch recht moet ze contractueel uitgewerkt worden — er is geen standaardregime. De kalibratie via de minimis, basket, cap en termijn weerspiegelt de risicoverdeling tussen koper en verkoper.

> [!summary] Korte inhoud
> Een vrijwaringsclausule (indemnification) verplicht de verkoper om de koper (en/of de doelvennootschap) schadeloos te stellen voor verlies dat voortvloeit uit een schending van een verklaring of waarborg, of uit een specifiek vermeld risico, binnen contractueel afgebakende beperk….

> [!info] Behoort tot: [[overnameovereenkomst]]

Een vrijwaringsclausule (indemnification) verplicht de verkoper om de koper (en/of de doelvennootschap) schadeloos te stellen voor verlies dat voortvloeit uit een schending van een verklaring of waarborg, of uit een specifiek vermeld risico, binnen contractueel afgebakende beperkingen.



## Bouwstenen

### De minimis-drempel ⚖️

Een drempelbedrag per individuele claim — claims onder de drempel zijn niet ontvankelijk. Beoogt verkoper te beschermen tegen kleine, administratieve claims.

**Waarom?** Vermijdt dat verkoper met triviale claims wordt overstelpt en moedigt koper aan om claims te aggregreren.


**In de praktijk**: Typisch 0,1–0,5 % van de prijs per individuele claim.


_Grondslag: IBA-MA-Belgium-2022-EN §5.2.6 De minimis_

### Basket (mandje) ⚖️

Een aggregatie-drempel: pas zodra de cumulatieve claims een bepaald bedrag bereiken, kan de koper iets vorderen. Twee varianten: 'tipping basket' (alles boven de drempel inclusief het mandje zelf) of 'deductible basket' (alleen het bedrag boven de drempel).

**Waarom?** Zelfde rationale als de minimis maar op aggregatieniveau: verkoper aanvaardt een vrijwaring pas als de totale impact wezenlijk is.


**In de praktijk**: Typisch 0,5–1 % van de prijs als drempel; tipping basket is gangbaar bij seller's market, deductible bij buyer's market.


_Grondslag: IBA-MA-Belgium-2022-EN §5.2.6 De minimis_

### Cap (plafond) ⚖️

Het maximumbedrag waarvoor de verkoper aansprakelijk is. Cap geldt typisch voor het geheel van algemene R&W-claims, vaak met een hoger cap of geen cap voor specifieke categorieën (titel, fiscaliteit, fraude).

**Waarom?** Beperkt verkoper's downside en is essentieel voor een 'clean exit'.


**In de praktijk**: Typisch 10–30 % van de prijs voor algemene R&W; voor fundamental R&W (titel, kapitaal) tot 100 %; voor fraude geen cap.


_Grondslag: IBA-MA-Belgium-2022-EN §5.2.6 Cap_

### Termijn (survival period) ⚖️

Hoe lang na closing kan een claim worden ingediend. Verschilt per categorie.

**Waarom?** Een tijdslimiet brengt rechtszekerheid en koppelt aan de externe verjarings- en fiscale onderzoekstermijnen.


**In de praktijk**: Algemene R&W: 18–36 maanden; fiscaliteit en sociale zekerheid: tot het einde van de wettelijke onderzoekstermijn (typisch 3–7 jaar); milieu: tot 10 jaar; titel aandelen: 30 jaar (verjaringstermijn); fraude: geen limiet of zeer lang.


_Grondslag: IBA-MA-Belgium-2022-EN §5.2.6 Duration_

### Specifieke vrijwaringen ⚖️

Voor gekende of geïdentificeerde risico's (vaak uit de DD) wordt een aparte vrijwaring opgenomen, los van de algemene R&W. Heeft typisch eigen cap, eigen duur en geen de minimis.

**Waarom?** Voorkomt dat een gekend risico de algemene cap opvreet ten nadele van onbekende issues; verschuift het risico expliciet naar de verkoper.


**In de praktijk**: Een lopend belastinggeschil van € 200.000 over de jaren 2022–2024 krijgt een specifieke vrijwaring met cap € 250.000 en duur tot afsluiting van het bezwaar — onafhankelijk van de algemene R&W-cap.


_Grondslag: IBA-MA-Belgium-2022-EN §4.2_

### Seller-protections ⚖️

Aanvullende clausules die de verkoper beschermen: neutralisatie van fiscale voordelen die de koper haalt uit de schade, conduct of defense van derde-partij-claims, niet-aansprakelijkheid voor wetswijzigingen.

**Waarom?** Vermijden dat de koper dubbel wordt vergoed of dat verkoper opdraait voor zaken buiten zijn invloed.


**In de praktijk**: Een DGS-claim die de doelvennootschap later kan recupereren via belastingaftrek: de schade onder vrijwaring wordt verminderd met het belastingvoordeel.


_Grondslag: IBA-MA-Belgium-2022-EN §5.2.6 Seller protections_


## In de praktijk

- De accountant kan helpen om de cap-niveaus economisch te onderbouwen — wat is de redelijke worst-case-blootstelling per categorie?
- De vrijwaring wordt vaak gecombineerd met een escrow, deferred payment of bankgarantie om de feitelijke afdwingbaarheid te waarborgen wanneer de verkoper een natuurlijk persoon of kleine vennootschap is.

## Valkuilen

> [!warning]- Maak duidelijk of de basket 'tipping' of 'deductible' is — verschil van vele tienduizenden euro's.
> ⚠️  🔗


> [!warning]- Sluit fraude uitdrukkelijk uit van alle beperkingen — anders zou een rechter de cap kunnen toepassen ook bij kwade trouw.
> ⚠️  🔗



## Zie ook

- **Getriggerd door**: [[representations-and-warranties]]
- **Wordt voorondersteld in** (5): [[begeleiden-due-diligence-overname]] · [[due-diligence-overname]] · [[escrow-en-zekerheidsmechanismen-overname]] · [[overnameovereenkomst]] · [[representations-and-warranties]]
## Voorbeelden

### Vrijwaringsstructuur SPA Brugse Brouwerij BV

_Personages: Brugse Brouwerij BV, Aurelia Holding NV, Pieter Vermeulen_

Aurelia Holding NV koopt Brugse Brouwerij BV voor € 4.500.000 van Pieter Vermeulen. Volgende vrijwaringsstructuur wordt onderhandeld.

Algemene R&W: cap 25 % = € 1.125.000; basket (tipping) € 45.000 (1 %); de minimis € 9.000 (0,2 %); duur 24 maanden.
Fundamental R&W (titel, kapitaal, vennootschapsbestaan): cap 100 % = € 4.500.000; geen basket; duur 7 jaar.
Fiscale R&W: cap 50 % = € 2.250.000; geen basket; duur tot einde wettelijke termijn fiscale aanslag (7 jaar bij bedrog, anders 3 jaar).
Specifieke vrijwaring lopend arbeidsgeschil: cap € 75.000 (= ingeschat maximum); geen basket; duur tot eindvonnis.
Fraude: geen cap, geen drempel, geen termijn (binnen verjaring 30 jaar).


