---
title: Verplichte IFRS voor EU-beursgenoteerden — geconsolideerde jaarrekening
tags:
- concept
- regel
- po-1-5
linked_anchors:
- 1.5.II
- 1.5.III
programmaonderdelen:
- '1.5'
confidence: grounded
node_type: regel
status: seed
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/verplichte-ifrs-eu-beursgenoteerden.json
gegenereerd_op: '2026-05-18'
---
# Verplichte IFRS voor EU-beursgenoteerden — geconsolideerde jaarrekening ⚖️

> [!summary] Korte inhoud
> Voor elk boekjaar dat begint op of na **1 januari 2005** moet een onderneming die onder het recht van een EU-lidstaat valt haar **geconsolideerde** jaarrekening opstellen volgens de door de Europese Commissie goedgekeurde internationale standaarden (endorsed IAS/IFRS) wanneer haa….

Voor elk boekjaar dat begint op of na **1 januari 2005** moet een onderneming die onder het recht van een EU-lidstaat valt haar **geconsolideerde** jaarrekening opstellen volgens de door de Europese Commissie goedgekeurde internationale standaarden (endorsed IAS/IFRS) wanneer haar effecten op de balansdatum zijn toegelaten tot de handel op een **gereglementeerde markt** van een lidstaat (in de zin van Richtlijn 93/22/EEG, nu MiFID II). De verplichting raakt **uitsluitend de geconsolideerde** jaarrekening — de enkelvoudige (statutaire) jaarrekening van de moedervennootschap valt onder het nationale boekhoudrecht van de lidstaat. Lidstaten mogen het toepassingsgebied uitbreiden (art. 5): zij mogen ook beursgenoteerde ondernemingen toestaan of verplichten hun **enkelvoudige** jaarrekening onder IFRS op te stellen, en zij mogen IFRS openstellen voor niet-beursgenoteerde ondernemingen.

_Bron: Verordening (EG) 1606/2002 art. 4 + art. 5_


## Drempelwaarden

| Naam | Waarde | Eenheid | Gevolg |
|---|---|---|---|
| Trigger verplichte IFRS-toepassing | Beursnotering op gereglementeerde markt EU-lidstaat op balansdatum + EU-rechtsvorm | kwalitatief criterium | Verplichte IFRS-toepassing op geconsolideerde jaarrekening voor boekjaren beginnend op of na 1 januari 2005 |


## Voorwaarden / uitzonderingen

- {'voorwaarde': 'EU-rechtspersoon', 'uitleg': 'De onderneming valt onder het recht van een EU-lidstaat (rechtsvorm uit een lidstaat). Een Amerikaanse onderneming met secundaire notering op Euronext Brussel valt niét onder de verordening.', 'confidence': 'grounded', 'source': {'type': 'verordening', 'short': 'Verordening 1606/2002 art. 4'}, '_provenance': {'inputs': [{'id': 'EU-IFRS-verordening-1606-2002__art_4', 'sha256': None, 'version': 'rag-v1'}]}} ⚖️
- {'voorwaarde': 'Notering op gereglementeerde markt', 'uitleg': 'De effecten zijn op balansdatum toegelaten tot de handel op een **gereglementeerde markt** van een lidstaat. Een multilaterale handelsfaciliteit (MTF) zoals Euronext Growth telt niét — alleen de hoofdmarkten (Euronext Brussel, Paris, Amsterdam, Lisbon, Milan, Frankfurt, ...).', 'confidence': 'grounded', 'source': {'type': 'verordening', 'short': 'Verordening 1606/2002 art. 4 jo. Richtlijn 93/22/EEG art. 1 punt 13 (nu MiFID II)'}, '_provenance': {'inputs': [{'id': 'EU-IFRS-verordening-1606-2002__art_4', 'sha256': None, 'version': 'rag-v1'}]}} ⚖️
- {'voorwaarde': 'Geconsolideerd niveau', 'uitleg': 'De verplichting geldt voor de **geconsolideerde** jaarrekening (groep), niet voor de enkelvoudige jaarrekening van de moedervennootschap. Onderneming zonder dochters → geen consolidatieplicht → geen IFRS-verplichting op grond van deze verordening (al kan toezichtswetgeving voor banken/verzekeraars wel IFRS opleggen op enkelvoudig niveau).', 'confidence': 'grounded', 'source': {'type': 'verordening', 'short': 'Verordening 1606/2002 art. 4'}, '_provenance': {'inputs': [{'id': 'EU-IFRS-verordening-1606-2002__art_4', 'sha256': None, 'version': 'rag-v1'}]}} ⚖️
- {'uitzondering': 'Lidstatenoptie — uitbreiding naar enkelvoudig of niet-beursgenoteerd (art. 5)', 'uitleg': 'Lidstaten **mogen** de verplichting uitbreiden: (a) beursgenoteerden ook voor hun **enkelvoudige** jaarrekening laten of doen rapporteren onder IFRS; (b) **niet-beursgenoteerde** ondernemingen IFRS-rapportering laten of opleggen voor geconsolideerde en/of enkelvoudige jaarrekening. België heeft van deze optie zeer beperkt gebruik gemaakt — zie `ifrs-toepassingsgebied-belgie` voor de Belgische invulling.', 'confidence': 'grounded', 'source': {'type': 'verordening', 'short': 'Verordening 1606/2002 art. 5'}, '_provenance': {'inputs': [{'id': 'EU-IFRS-verordening-1606-2002__art_5', 'sha256': None, 'version': 'rag-v1'}]}} ⚖️
- {'uitzondering': 'Overgangsbepaling — uitsteldatum 1 januari 2007 (art. 9)', 'uitleg': 'Lidstaten konden bepalen dat de IFRS-verplichting pas vanaf boekjaren die begonnen op of na 1 januari 2007 gold voor: (a) ondernemingen waarvan **alleen schuldinstrumenten** waren toegelaten tot een gereglementeerde markt; (b) ondernemingen die in een derde land beursgenoteerd waren en daar al internationaal aanvaarde standaarden hanteerden.', 'confidence': 'grounded', 'source': {'type': 'verordening', 'short': 'Verordening 1606/2002 art. 9'}, '_provenance': {'inputs': [{'id': 'EU-IFRS-verordening-1606-2002__art_4', 'sha256': None, 'version': 'rag-v1'}]}} ⚖️
## Valkuilen

> [!warning]- De verordening verplicht alleen ondernemingen onder **EU-recht** met effecten op een **EU-gereglementeerde markt**
> ⚠️ De verordening verplicht alleen ondernemingen onder **EU-recht** met effecten op een **EU-gereglementeerde markt**. Een Amerikaanse onderneming met aandelen op Euronext volgt US-GAAP (of een gelijkwaardig kader); zij valt niét onder art. 4. ⚖️
>
> _Bron: Verordening 1606/2002 art. 4_


> [!warning]- **Alleen geconsolideerd**: de enkelvoudige jaarrekening van de moedervennootschap blijft onder nationaal boekhoudrecht (in België: KB WVV)
> ⚠️ **Alleen geconsolideerd**: de enkelvoudige jaarrekening van de moedervennootschap blijft onder nationaal boekhoudrecht (in België: KB WVV). Een examenvraag die suggereert dat een beursgenoteerde groep 'volledig op IFRS' rapporteert is een valstrik — de enkelvoudige cijfers volgen Belgisch GAAP. ⚖️
>
> _Bron: Verordening 1606/2002 art. 4_


> [!warning]- 'IFRS' in art. 4 betekent de door de Commissie **endorsed** set, niet de IASB-publicatie
> ⚠️ 'IFRS' in art. 4 betekent de door de Commissie **endorsed** set, niet de IASB-publicatie. Een examenvraag over 'verplichte IFRS' verwijst altijd naar endorsed IFRS — zie `endorsement-procedure-eu`. ⚖️
>
> _Bron: Verordening 1606/2002 art. 2 + art. 4_



## Zie ook

- **Vereist kennis van**: [[endorsement-procedure-eu]]
- **Getriggerd door**: [[ifrs-eerste-toepassing]]

## Voorbeelden

Zelena Bio NV is genoteerd op Euronext Brussel (gereglementeerde markt) en valt onder Belgisch recht. Vanaf boekjaar 2005 stelt zij haar **geconsolideerde** jaarrekening (omzet groep € 350.000.000) op onder endorsed IFRS. Haar **enkelvoudige** jaarrekening blijft onder KB WVV vallen — België heeft van art. 5-optie geen gebruik gemaakt voor enkelvoudige rekeningen.
Industria Antwerpen NV is alleen genoteerd op Euronext Growth (een MTF, geen gereglementeerde markt). Zij valt **niet** onder de art. 4-verplichting en rapporteert geconsolideerd onder Belgisch GAAP.

## Bronnen

[^1]: `EU-IFRS-verordening-1606-2002__art_2`
[^2]: `EU-IFRS-verordening-1606-2002__art_4`
[^3]: `EU-IFRS-verordening-1606-2002__art_5`
