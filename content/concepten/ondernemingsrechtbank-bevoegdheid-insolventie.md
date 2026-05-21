---
title: Bevoegdheid ondernemingsrechtbank bij insolventie
tags:
- concept
- regel
- po-3-0
linked_anchors:
- 3.0.X
- 3.0.X.A
programmaonderdelen:
- '3.0'
confidence: grounded
node_type: regel
status: seed
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/ondernemingsrechtbank-bevoegdheid-insolventie.json
gegenereerd_op: '2026-05-21'
---
# Bevoegdheid ondernemingsrechtbank bij insolventie ⚖️

De bevoegdheidsregel uit Boek XX is bewust afgestemd op de Europese Insolventieverordening (EU 2015/848): dezelfde COMI-test, dezelfde driemaanden-vermoeden voor zetelverplaatsing. Hierdoor wordt forum shopping (vlak vóór een aanvraag de zetel verleggen om een gunstigere rechtbank te kiezen) tegengegaan. Internationale concerns waarvan moeders en dochters elk een COMI in een ander land hebben, doorlopen meestal parallelle procedures met groepscoördinatie.

> [!summary] Korte inhoud
> De insolventierechtbank gelegen in het rechtsgebied waar de schuldenaar zijn **centrum van de voornaamste belangen (COMI)** heeft, is **uitsluitend** bevoegd om een insolventieprocedure te openen (art. XX.12 § 1).

> [!info] Behoort tot: [[insolventieprocedures-belgie]]

De insolventierechtbank gelegen in het rechtsgebied waar de schuldenaar zijn **centrum van de voornaamste belangen (COMI)** heeft, is **uitsluitend** bevoegd om een insolventieprocedure te openen (art. XX.12 § 1). Voor vennootschappen en rechtspersonen geldt het vermoeden dat de COMI de plaats van de zetel is, tenzij de zetel in de drie maanden vóór de aanvraag verplaatst is. Voor een natuurlijke persoon die een vrij beroep of zelfstandige activiteit uitoefent: de hoofdvestiging (of hoofdinschrijving bij ingeschreven vrije beroepen).

_Bron: WER art. XX.12 § 1_



## Voorwaarden / uitzonderingen

- {'tekst': 'Vennootschappen en rechtspersonen: COMI = plaats van de zetel, behoudens tegenbewijs. Vermoeden geldt enkel als de zetel in de drie maanden vóór de aanvraag niet naar een ander rechtsgebied is verplaatst.', 'grondslag': 'WER art. XX.12 § 1, tweede lid', 'confidence': 'grounded', '_provenance': {'inputs': [{'id': 'WER__art_XX_12', 'sha256': None, 'version': 'rag-v1'}]}} ⚖️
- {'tekst': 'Natuurlijke persoon vrij beroep / zelfstandige: COMI = hoofdvestiging, of bij ingeschreven beroepen de hoofdinschrijving. Driemaanden-vermoeden geldt analoog.', 'grondslag': 'WER art. XX.12 § 1, derde lid', 'confidence': 'grounded', '_provenance': {'inputs': [{'id': 'WER__art_XX_12', 'sha256': None, 'version': 'rag-v1'}]}} ⚖️
- {'tekst': '**Verbonden ondernemingen**: een rechtbank die bevoegd is voor de insolventieprocedure van onderneming A is ook bevoegd voor een procedure tegen een met A verbonden onderneming. Zij kan een gemeenschappelijke gerechtsmandataris aanstellen voor alle procedures (art. XX.13).', 'grondslag': 'WER art. XX.13', 'confidence': 'grounded', '_provenance': {'inputs': [{'id': 'WER__art_XX_12', 'sha256': None, 'version': 'rag-v1'}]}} ⚖️
- {'tekst': '**Onbeperkt aansprakelijke vennoten**: een rechtbank bevoegd voor een rechtspersoon waarvan vennoten onbeperkt aansprakelijk zijn (bv. VOF, CommV), of voor een onderneming als bedoeld in I.1, eerste lid, 1°, c), is ook bevoegd voor procedures tegen de vennoten. Het openen van een procedure tegen de vennootschap leidt **niet** automatisch tot een procedure tegen die vennoten (art. XX.14).', 'grondslag': 'WER art. XX.14', 'confidence': 'grounded', '_provenance': {'inputs': [{'id': 'WER__art_XX_13', 'sha256': None, 'version': 'rag-v1'}]}} ⚖️
- {'tekst': '**Beheersontneming-historiek**: heeft een rechtbank ooit een beslissing tot ontneming van het beheer gewezen (art. XX.32), dan blijft zij uitsluitend bevoegd voor het uitspreken van het faillissement gedurende de termijn bepaald in XX.32 § 5, vierde lid — ook al zou de gewone COMI-regel een andere rechtbank aanwijzen.', 'grondslag': 'WER art. XX.12 § 4', 'confidence': 'grounded', '_provenance': {'inputs': [{'id': 'WER__art_XX_12', 'sha256': None, 'version': 'rag-v1'}]}} ⚖️
## Valkuilen

> [!warning]- Controleer altijd of de zetel in de drie maanden vóór de aanvraag verplaatst is. Bij recente verplaatsing **werkt het vermoeden niet** en moet de werkelijke COMI bewezen worden (locatie operaties, hoofdactiviteit, contactpunt voor schuldeisers).
> ⚠️  🔗


> [!warning]- Voor concerns: dien procedures parallel aan bij dezelfde rechtbank wanneer de moeder al een procedure heeft. De rechtbank kan dan één gemeenschappelijke insolventiefunctionaris aanstellen (XX.13), wat coördinatie en kosten significant verbetert.
> ⚠️  🔗



## Zie ook

- **Vereist kennis van**: [[voorwaarden-faillietverklaring]]
- **Wordt voorondersteld in** (3): [[homologatie-collectief-akkoord]] · [[overdracht-onder-gerechtelijk-gezag]] · [[rehabilitatie-gefailleerde]]
## Voorbeelden

### COMI-test met recente zetelverplaatsing

_Personages: Solaris Sint-Truiden BV_

Solaris Sint-Truiden BV heeft sinds 2010 haar zetel in Sint-Truiden (rechtsgebied ondernemingsrechtbank Limburg). Op 1 maart 20X2 verplaatst het bestuur de zetel naar Antwerpen. Op 1 mei 20X2 vraagt een schuldeiser het faillissement aan.

1. Sinds 1 maart 20X2 zit Solaris formeel in Antwerpen — naar de zetelregel zou de ondernemingsrechtbank Antwerpen bevoegd zijn.
2. Tussen 1 maart 20X2 en 1 mei 20X2 zit minder dan drie maanden — het vermoeden uit art. XX.12 § 1 werkt niet.
3. De rechtbank moet de werkelijke COMI vaststellen. Indien blijkt dat de operationele activiteit (klanten, werknemers, leveranciers, boekhouding) in Sint-Truiden is gebleven, blijft de ondernemingsrechtbank Limburg bevoegd.
4. De aanvraag in Antwerpen wordt onbevoegd verklaard en doorverwezen.


## Bronnen

[^1]: `WER__art_XX_12`
[^2]: `WER__art_XX_13`
