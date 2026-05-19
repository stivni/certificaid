---
title: Digital Operational Resilience Act (DORA)
tags:
- concept
- regel
- po-1-7
linked_anchors:
- 1.7.X
- 1.7.X.A
- 1.7.XII.A
programmaonderdelen:
- '1.7'
confidence: inferred
node_type: regel
status: seed
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/dora-verordening.json
gegenereerd_op: '2026-05-18'
---
# Digital Operational Resilience Act (DORA) 🤖

DORA is een rechtstreeks werkende EU-verordening die digitale operationele weerbaarheid oplegt aan de financiële sector. Sinds 17 januari 2025 moeten financiële entiteiten ICT-risico's beheersen volgens een uniform Europees kader, in plaats van de eerdere lappendeken van nationale prudentiële vereisten. Voor de gecertificeerd accountant relevant omdat ICT-risicobeheer raakt aan de interne controle (PO 1.7) en omdat externe ICT-leveranciers van financiële cliënten plots onder Europees toezicht vallen.

> [!summary] Korte inhoud
> Financiële entiteiten in de EU moeten een geïntegreerd kader voor digitale operationele weerbaarheid implementeren rond vijf pijlers: (1) ICT-risicobeheer, (2) ICT-incidenten classificeren en rapporteren, (3) digitale weerbaarheid testen (waaronder threat-led penetration testing)….

Financiële entiteiten in de EU moeten een geïntegreerd kader voor digitale operationele weerbaarheid implementeren rond vijf pijlers: (1) ICT-risicobeheer, (2) ICT-incidenten classificeren en rapporteren, (3) digitale weerbaarheid testen (waaronder threat-led penetration testing), (4) ICT-derdenrisico beheersen, en (5) informatiedeling over cyberbedreigingen. Verordening (EU) 2022/2554, toepasselijk sinds 17 januari 2025.

_Bron: Verordening (EU) 2022/2554 (DORA)_


## In de praktijk

- Een Belgische bank moet een ICT-risico-strategie hebben goedgekeurd door het bestuursorgaan, incident-rapportering naar de NBB binnen strakke deadlines, periodieke threat-led penetration testing (TLPT) elke 3 jaar, en een schriftelijke ICT-derdenovereenkomst met elke kritieke leverancier.
- Voor een gewone niet-financiële KMO geldt DORA NIET — die valt eventueel onder NIS-2 (essentiële of belangrijke entiteit). Het is dus belangrijk om eerst sector + grootte te bepalen voor je bepaalt welk regime geldt.

## Drempelwaarden

| Naam | Waarde | Eenheid | Gevolg |
|---|---|---|---|
| Toepassingsdatum | 17 januari 2025 | datum |  |


## Voorwaarden / uitzonderingen

- Toepassingsgebied: kredietinstellingen, betalingsinstellingen, beleggingsondernemingen, beheerders van alternatieve beleggingsinstellingen, verzekerings- en herverzekeringsondernemingen, aanbieders van crypto-activadiensten, centrale tegenpartijen, handelsplatforms — én kritieke ICT-derde-dienstverleners die deze entiteiten bedienen. 🤖
- Bevoegde toezichthouders in België: NBB voor prudentieel gereguleerde entiteiten (banken, verzekeraars), FSMA voor markt- en gedragstoezicht, en ESAs (EBA, EIOPA, ESMA) voor de kritieke ICT-derden via het Joint Oversight Framework. 🤖
- Micro-ondernemingen onder DORA (< 10 werknemers én < € 2 miljoen balans of omzet) krijgen een vereenvoudigd ICT-risicobeheerregime met minder uitgebreide testverplichtingen. 🤖
> [!info]- Niet verwarren met [[nis-2-richtlijn]]
> DORA = sector-specifiek voor financiële diensten + hun kritieke ICT-derden; rechtstreeks werkende EU-verordening; lex specialis voor de financiële sector. NIS-2 = cross-sectoraal (energie, vervoer, gezondheid, digitale infrastructuur, ...); richtlijn die nationaal omgezet moet worden; lex generalis. Voor een bank: DORA primeert. Voor een chemiebedrijf: NIS-2.
>
> _Trigger_: Examenvraag 'welk cybersecurity-regime geldt voor een Belgische verzekeraar?' → DORA (lex specialis). 'voor een ziekenhuis?' → NIS-2.


## Valkuilen

> [!warning]- DORA is een verordening, NIS-2 een richtlijn
> ⚠️ DORA is een verordening, NIS-2 een richtlijn. Verordening = rechtstreeks toepasselijk zonder omzetting; richtlijn = nationale omzettingswet nodig. Verkeerd kwalificeren leidt tot fouten over directe werking. 🤖


> [!warning]- Denken dat DORA enkel de bank zelf raakt — kritieke ICT-leveranciers (cloud, software-as-a-service, datacenter) vallen óók onder Europees ov…
> ⚠️ Denken dat DORA enkel de bank zelf raakt — kritieke ICT-leveranciers (cloud, software-as-a-service, datacenter) vallen óók onder Europees oversight, ook als zij zelf geen financiële entiteit zijn. 🤖



> [!todo] Voorbeeld ontbreekt voor dit concept
> Een latere ENRICH-pass voegt een synthese-voorbeeld toe.

