---
title: Voeren van een regelmatige dubbele boekhouding voor een onderneming
tags:
- concept
- competentie
- po-1-1
linked_anchors:
- 1.1.taak.1
- 1.1.I
- 1.1.I.A
- 1.1.I.B
programmaonderdelen:
- '1.1'
confidence: inferred
node_type: competentie
status: voorgesteld
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/voeren-regelmatige-dubbele-boekhouding.json
gegenereerd_op: '2026-05-18'
---
# Voeren van een regelmatige dubbele boekhouding voor een onderneming 🤖


## Stappen

### 1. Kwalificeer het boekhoudregime van de cliënt

Bepaal of de onderneming dubbele dan wel vereenvoudigde boekhouding moet voeren.

**Waarom?** Het regime bepaalt welke dagboeken en wetsartikelen van toepassing zijn — pas dan kan men correct organiseren.

**📥 Input**:
- Cliëntdossier → **Rechtsvorm, sector, omzet (vorig boekjaar)** _(document)_

**📤 Output**:
- Werknotitie → **Regime + grondslag** _(conclusie)_

**🛠️ Hoe**:

1. Lees rechtsvorm: NV, BV, CVBA → altijd dubbel; eenmanszaak/VOF → toets omzetdrempel.
2. Toets WER art. III.85: eenmanszaken en VOFs onder € 500.000 omzet excl. btw (€ 620.000 voor kolenwaren) mogen vereenvoudigd boekhouden — zie [[vereenvoudigde-boekhouding]] §drempels.
3. Bij Praktijk Persenaire (vrij beroep, eenmanszaak, omzet € 180.000): vereenvoudigd toegelaten. Bij Meubelzaak Mertens BV: altijd dubbel, ongeacht omvang.
4. Noteer het regime in de werknotitie en verwijs naar WER art. III.85.


**Grondslag**: [[regelmatige-boekhouding]] §toepassingsgebied, WER art. III.83-85

### 2. Stel het rekeningenplan op volgens MAR

Verfijn het minimum algemeen rekeningstelsel naar de aard en omvang van de cliënt.

**Waarom?** Een rekeningenplan op maat maakt de boekhouding bruikbaar voor analyse, btw en fiscaliteit, terwijl het MAR-skelet de wettelijke vergelijkbaarheid bewaart.

**📥 Input**:
- KB-MAR → **Volledige rekeningenlijst** _(document)_
- Activiteiten-overzicht cliënt → **Productgroepen, kostenplaatsen** _(document)_

**📤 Output**:
- Aangepast rekeningenplan → **MAR-rekeningen + sub-rekeningen** _(document)_

**🛠️ Hoe**:

1. Neem de zes klassen van het MAR over (1 t.e.m. 7) zoals voorzien in [[minimum-algemeen-rekeningenstelsel]] §structuur.
2. Verfijn enkel via sub-rekeningen — wijzig nooit de hoofdrekening-nummering.
3. Voor Meubelzaak Mertens BV: splits rekening 70 (Omzet) in 7000 Meubelen-stockverkoop en 7001 Meubelen-projectverkoop voor analytisch inzicht.
4. Voor Naaiatelier Ninove BV: splits 60 Aankopen in 600 Grondstoffen-textiel en 601 Hulpstoffen-garen.
5. Leg het aangepast rekeningenplan vast in de waarderingsregels (KB-WVV art. 3:6).


**Grondslag**: [[minimum-algemeen-rekeningenstelsel]] §aanpassing, KB-MAR

### 3. Voer dagelijkse verrichtingen in de hulpdagboeken

Boek elke verrichting in het juiste hulpdagboek met inachtneming van het dubbel-boekhoudprincipe.

**Waarom?** Dagelijkse registratie zorgt voor de chronologische bewijsfunctie en maakt periodieke btw-aangifte mogelijk.

**📥 Input**:
- Inkomende/uitgaande facturen, bankuittreksels, kasstukken → **Bewijsstukken met datum, partijen, bedragen, btw** _(document)_

**📤 Output**:
- Hulpdagboeken → **Geboekte journaalposten met debet/credit gelijkheid** _(boekingsregel)_

**🛠️ Hoe**:

1. Klasseer elke stuk: aankoop → aankoopdagboek, verkoop → verkoopdagboek, bank → financieel dagboek, kas → kasboek, overige → diversenboek. Zie [[dagboek]] §types.
2. Boek elke verrichting volgens [[dubbel-boekhouden]] — totaal debet = totaal credit per journaalpost.
3. Vermeld bewijsstuk-referentie (factuurnr, bankuittrekselnr) en boekingsdatum.
4. Verwerk btw correct: aftrekbare op rekening 411 voor aankopen, verschuldigde op 451 voor verkopen.
5. Voorbeeld bij Meubelzaak Mertens BV: zie voorbeeld-blok.


> [!example]- Voorbeeld: Meubelzaak Mertens BV ontvangt op 15/03/2026 een aankoopfactuur van leverancier Houthandel Hove: € 1.250 grondstoffen +…
> Meubelzaak Mertens BV ontvangt op 15/03/2026 een aankoopfactuur van leverancier Houthandel Hove: € 1.250 grondstoffen + 21% btw = € 1.512,50 totaal. Betaling op 30 dagen.
>
> 1. **Boeking in aankoopdagboek** 📝
>
>    | Datum | Rekening | Omschrijving | Debet | Credit |
>    |---|---|---|---|---|
>    | 15/03 | 600 Grondstoffen | Aankoopfactuur Houthandel Hove | € 1.250,00 | |
>    | 15/03 | 411 Aftrekbare btw 21% | btw aankoopfactuur | € 262,50 | |
>    | 15/03 | 4400 Leveranciers — Houthandel Hove | te betalen 14/04 | | € 1.512,50 |
>    
>
> 2. **Boeking betaling 14/04 in financieel dagboek** 📝
>
>    | Datum | Rekening | Omschrijving | Debet | Credit |
>    |---|---|---|---|---|
>    | 14/04 | 4400 Leveranciers — Houthandel Hove | aanzuivering | € 1.512,50 | |
>    | 14/04 | 5500 Bank — KBC | betaalopdracht | | € 1.512,50 |
>    
>

**Grondslag**: [[dagboek]] §hulpdagboeken, [[dubbel-boekhouden]] §regel, WER art. III.84

> [!warning]- Boek elke factuur op de factuurdatum, niet op de ontvangstdatum — anders verschuift de btw-periode.
>
> _Vaak fout gedaan_: De factuur boeken op het moment dat ze fysiek toekomt op kantoor.
>
> _Grondslag_: [[dagboek]] §boekingsdatum

### 4. Centraliseer naar het grootboek en stel proefbalans op

Breng alle hulpdagboek-saldi periodiek samen in het grootboek en toets de balans-gelijkheid.

**Waarom?** Centralisatie levert het bewijs van regelmatigheid (debet = credit) en is de basis voor btw-aangifte en jaarrekening.

**📥 Input**:
- Hulpdagboeken → **Maandelijkse totalen per rekening** _(berekening)_

**📤 Output**:
- Proef- en saldibalans → **Per rekening: openingsaldo, bewegingen, slotaldo** _(balans)_

**🛠️ Hoe**:

1. Centraliseer minstens maandelijks — verplicht voor btw-aangifte (zie [[regelmatige-boekhouding]] §centralisatie).
2. Toets controle door de balans: ∑ debet-saldi = ∑ credit-saldi.
3. Bij ongelijkheid: zoek de fout via reconciliatie (bank, klanten, leveranciers, btw).
4. Bewaar proefbalans als sluitend bewijsstuk per maand.


**Grondslag**: [[regelmatige-boekhouding]] §centralisatie, WER art. III.84

### 5. Maak jaarlijks inventaris en bewaar alle stukken 7 jaar

Voer eenmaal per jaar een volledige inventaris uit en archiveer alle boekhoudstukken volgens de wettelijke termijn.

**Waarom?** Inventaris is de wettelijke jaarlijkse toets dat de boekhouding aansluit op de werkelijkheid; bewaring is voorwaarde voor de bewijsfunctie.

**📥 Input**:
- Magazijn, balans, contracten, bewijsstukken → **Fysieke voorraden, openstaande vorderingen, schulden** _(document)_

**📤 Output**:
- Inventarisstaat + archief → **Volledige opname per balansrubriek** _(document)_

**🛠️ Hoe**:

1. Volg de procedure uit [[inventaris]] §opmaak — fysieke telling voorraden, bevestiging vorderingen, bankreconciliatie.
2. Waardeer volgens vastgelegde waarderingsregels (FIFO, GGP, lineaire afschrijving, ...).
3. Boek correctieboekingen voor verschillen (inventarisverschillen, waardeverminderingen).
4. Archiveer alle boekhoudstukken volgens [[bewaring-boekhoudstukken]] §termijnen — 7 jaar voor boekhoudkundige stukken, 10 jaar voor facturen en btw-documenten.
5. Documenteer in cliëntdossier: inventarislocatie, datum, aanwezigen.


**Grondslag**: [[inventaris]] §opmaak, [[bewaring-boekhoudstukken]] §wettelijke-termijn, WER art. III.86


## Voorbeelden




