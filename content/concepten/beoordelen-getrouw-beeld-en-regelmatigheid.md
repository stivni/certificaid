---
title: Beoordelen van regelmatigheid, waarachtigheid en getrouw beeld van de jaarrekening
tags:
- concept
- competentie
- po-1-6
linked_anchors:
- 1.6.taak.1
- 1.6.IV.A
- 1.6.IV
programmaonderdelen:
- '1.6'
confidence: inferred
node_type: competentie
status: voorgesteld
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/beoordelen-getrouw-beeld-en-regelmatigheid.json
gegenereerd_op: '2026-05-18'
---
# Beoordelen van regelmatigheid, waarachtigheid en getrouw beeld van de jaarrekening 🤖

> [!update] Bijgewerkt sinds `b2f4a4ad` — laatste wijziging 2026-05-18


Deze competentie bundelt wat de stagiair moet kunnen bij het beoordelen van de jaarrekening op haar drie wettelijke eigenschappen: regelmatigheid (in overeenstemming met het boekhoud- en jaarrekeningenrecht), waarachtigheid (geen materiële afwijkingen), en getrouw beeld (juiste weergave van vermogen, financiële toestand en resultaat). Deze drie samen vormen het toetsingsobject van het uiteindelijke controleoordeel.


## Stappen

### 1. Toetsen of de jaarrekening regelmatig is opgesteld

Vergelijk de jaarrekening met het toepasselijke financieel rapporteringsstelsel (KB WVV, IFRS, sectoraal stelsel).

**Waarom?** Regelmatigheid is een binaire toets — alles wat afwijkt is een 'afwijking op het stelsel' die in het verslag moet vermeld worden.

**📥 Input**:
- Volledige jaarrekening (balans + resultatenrekening + toelichting + sociale balans) → **Alle onderdelen** _(document)_
- Toepasselijk stelsel — KB WVV 2019 (volledig of verkort schema) → **Vormvereisten + waarderingsregels** _(document)_

**📤 Output**:
- Werkpapier 'regelmatigheidstoets' → **Per onderdeel: conform / afwijking** _(conclusie)_

**🛠️ Hoe**:

1. Toets vorm volgens [[regelmatigheid-jaarrekening-audit]] §schema — verkort of volledig schema, sociale balans, toelichtingen.
2. Toets waarderingsregels: voorraad (FIFO/GGP), vaste activa (afschrijvingsmethode), vorderingen (waardeverminderingen), voorzieningen.
3. Toets bestendigheid: zijn waarderingsregels consistent met vorig jaar? Wijzigingen toegelicht?
4. Documenteer per onderdeel de slotsom 'conform' of 'afwijking' met verwijzing naar specifieke KB WVV-artikel.


**Grondslag**: [[regelmatigheid-jaarrekening-audit]] §toetsing, ITAA KMO-controlenorm §123

### 2. Beoordelen of de jaarrekening waarachtig is

Toets of de bedragen daadwerkelijk overeenstemmen met de onderliggende boekhouding en met de werkelijkheid op de balansdatum.

**Waarom?** Waarachtigheid is de tweede pijler: een formeel regelmatige jaarrekening kan toch onjuist zijn (bv. fictieve omzet, niet-bestaande voorraad).

**📥 Input**:
- Resultaten controle-instrumenten uit [[selecteren-en-uitvoeren-controle-instrumenten-audit]] → **Testbevindingen per rubriek** _(document)_

**📤 Output**:
- Waarachtigheidsoordeel per rubriek → **Geen materiële afwijking / afwijking € XXX** _(conclusie)_

**🛠️ Hoe**:

1. Aggregeer per rubriek de testbevindingen (factuele afwijkingen, geprojecteerde steekproefafwijkingen, gemiste toelichtingen).
2. Vergelijk de aggregatie met de performance materiality uit [[uitvoeren-risico-inschatting-en-materialiteit-audit]].
3. Bij overschrijding materialiteit: oordeel materieel onjuist. Bij overschrijding én pervasief effect: oordeel onthouding of afkeurend (zie [[opstellen-controleverslag-en-formuleren-oordeel]]).
4. Hou een 'Summary of Audit Differences' bij — gewone afwijkingen (boekhoudkundige correctie voorgesteld) + ongereinigde afwijkingen (waarop het oordeel rust).


**Grondslag**: [[regelmatigheid-jaarrekening-audit]] §waarachtigheid, ITAA KMO-controlenorm §125

### 3. Toetsen of de jaarrekening een getrouw beeld geeft

Beoordeel of de jaarrekening, ondanks formele conformiteit, een eerlijke voorstelling geeft van vermogen, financiële positie en resultaat.

**Waarom?** Getrouw beeld is breder dan regelmatigheid: een transactie kan boekhoudkundig juist verwerkt zijn maar de jaarrekening misleidend door context (bv. gebrekkige toelichting bij hoog risico).

**📥 Input**:
- Aggregaat regelmatigheid + waarachtigheid stap 1+2 → **Geïdentificeerde issues** _(document)_
- Toelichting bij jaarrekening → **Volledigheid + leesbaarheid** _(document)_

**📤 Output**:
- Werkpapier 'getrouw-beeld-conclusie' → **Per balansrubriek + toelichting** _(conclusie)_

**🛠️ Hoe**:

1. Stap terug: 'als ik de lezer was, krijg ik dan een correct beeld?' — volgens [[getrouw-beeld-controle]] §test.
2. Toets of materiële posten in toelichting voldoende zijn uitgelegd — verbonden partijen, garanties, off-balance.
3. Toets dat schattingen redelijk zijn binnen een aanvaardbare bandbreedte, zelfs als regelmatig.
4. Bij twijfel of formele regelmatigheid een misleidend beeld dekt: 'true and fair view override' overwegen volgens [[getrouw-beeld-controle]] §override.


**Grondslag**: [[getrouw-beeld-controle]] §toetsing, art. 3:75 §1, 2° WVV

> [!warning]- Een jaarrekening kan regelmatig zijn (conform stelsel) maar tegelijk geen getrouw beeld geven — toets de twee onafhankelijk.
>
> _Vaak fout gedaan_: Regelmatigheid als equivalent van getrouw beeld behandelen; alleen vormcheck doen.
>
> _Grondslag_: [[getrouw-beeld-controle]] §scheiding-met-regelmatigheid

### 4. Continuïteit als overkoepelende toets

Toets of de continuïteitsveronderstelling van de jaarrekening passend is en of materiële onzekerheid moet worden vermeld.

**Waarom?** Continuïteitsproblemen raken zowel waardering (going-concern versus liquidatie) als toelichting — kerncomponent van het oordeel.

**📥 Input**:
- Indicatoren continuïteit uit [[verwerven-kennis-van-clientonderneming-audit]] stap 3 → **Risicocategorie** _(conclusie)_
- Cashflow-prognose 12 maanden + financieringsplanning → **Liquiditeit + ratio-verplichtingen** _(document)_

**📤 Output**:
- Conclusie continuïteit → **Aanvaardbaar / aanvaardbaar mits toelichting / niet aanvaardbaar** _(conclusie)_

**🛠️ Hoe**:

1. Vraag een 12-maanden cashflow-prognose en financieringsoverzicht van het management.
2. Toets de redelijkheid van de assumpties volgens [[continuiteitsveronderstelling-audit]] §toetsing.
3. Bij materiële onzekerheid: vereis een toelichting in de jaarrekening + plan een 'paragraaf ter benadrukking' of een aangepast oordeel.
4. Bij vaststelling dat de going-concern-basis niet aanvaardbaar is: jaarrekening moet op liquidatiebasis worden opgesteld — anders afkeurend oordeel.


**Grondslag**: [[continuiteitsveronderstelling-audit]] §toetsing, ITAA KMO-controlenorm §122


## Zie ook

- **Vereist kennis van**: [[getrouw-beeld-controle]]
- **Vereist kennis van**: [[regelmatigheid-jaarrekening-audit]]
- **Vereist kennis van**: [[continuiteitsveronderstelling-audit]]
- **Vereist kennis van**: [[materieel-belang-audit]]
- **Vereist kennis van**: [[assurance-informatie]]

## Voorbeelden




## Bronnen

[^1]: `KB-WVV-2019__art_3`
[^2]: `ITAA-norm-kmo-controlenorm__sec_3-3-1-basis-voor-het-oordeel`
