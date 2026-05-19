---
title: Inventaris
tags:
- concept
- cluster
- po-1-1
- po-1-2
linked_anchors:
- 1.1.I
- 1.1.I.A
- 1.1.taak.1
- 1.1.II.S
- 1.2.III.E
- 1.2.III
- 1.2.taak.1
programmaonderdelen:
- '1.1'
- '1.2'
confidence: grounded
node_type: cluster
status: seed
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/inventaris.json
gegenereerd_op: '2026-05-18'
---
# Inventaris ⚖️

De inventaris is het **gestructureerd overzicht** van alle bezittingen, vorderingen, schulden en verplichtingen op balansdatum. Voor de stagiair-GA cruciaal omdat de inventaris de **brug** vormt tussen het hele boekjaar (dagboeken, hulpdagboeken) en de jaarrekening: zonder correcte inventaris geen correcte jaarrekening. Examenvalkuil: inventaris ↔ proef- en saldibalans verwarren.

> [!summary] Korte inhoud
> Het **gestructureerd overzicht** van alle bezittingen, vorderingen, schulden, verplichtingen en eigen middelen van een onderneming op één gekozen datum (typisch balansdatum), opgesteld door fysieke telling, contractverificatie en waardering.

> [!info] Behoort tot: [[regelmatige-boekhouding]]

Het **gestructureerd overzicht** van alle bezittingen, vorderingen, schulden, verplichtingen en eigen middelen van een onderneming op één gekozen datum (typisch balansdatum), opgesteld door fysieke telling, contractverificatie en waardering. De inventaris is de feitelijke check op de boekhouding: voorraad ter plaatse tellen, klantenlijst nakijken, schuldenlijst opmaken. Verschillen tussen boekhouding en inventaris worden gecorrigeerd vóór de jaarrekening wordt opgesteld (WER art. III.89).

_Bron: WER art. III.89_


## In de praktijk

<h3 id="cut-off-rond-balansdatum">Cut-off rond balansdatum</h3>

> [!tip]- Cut-off rond balansdatum
> Goederen ontvangen vóór 31/12 horen in de voorraad, ook al komt de factuur in januari. Goederen verzonden vóór 31/12 horen niet meer in de voorraad, ook al wordt de verkoopfactuur pas in januari opgemaakt. Cut-off is de kritische bewaking rond balansdatum. 🤖

> [!tip]- Herkennen op het examen
> Examenvraag: 'levering op 30/12 met factuur op 5/1' — boeking in 20X1 of 20X2?

<h3 id="rechten-en-verplichtingen-buiten-balans">Rechten en verplichtingen buiten balans</h3>

> [!tip]- Rechten en verplichtingen buiten balans
> De inventaris omvat ook rechten en verplichtingen die NIET in de balans staan: huurverplichtingen, persoonlijke borgstellingen, lopende garanties, opties, hangende geschillen. Deze gaan naar klasse 0 en in de toelichting. ⚖️

> [!tip]- Herkennen op het examen
> Examen: vergeten een verplichting buiten balans op te nemen = onvolledige inventaris.


## Stappen

### 1. Bepaal de inventarisdatum

Kies één vaste datum per boekjaar — meestal afsluitingsdatum (31/12 of een ander afsluitingsmoment).

**Waarom?** Eén vaste datum is nodig voor de coherentie van de jaarrekening; alle posten moeten op dezelfde datum gewaardeerd worden.

**🛠️ Hoe**:

1. Kies de afsluitingsdatum van het boekjaar (statuten).
2. Plan tellingen, controleberekeningen en bevragingen rond deze datum (cut-off-discipline: leveringen na 31/12 nog wel goederen onderweg?).

**Grondslag**: WER art. III.89

### 2. Tel de fysieke voorraden en bezittingen

Voer een fysieke telling uit van voorraden (grondstoffen, halffabrikaten, afgewerkte producten, handelsgoederen) en controleer aanwezigheid van vaste activa (machines, voertuigen, ICT).

**Waarom?** De boekhoudkundige voorraad volgt aankopen en verkopen; fysieke telling vangt verlies, diefstal, breuk en administratieve fouten op.

**📥 Input**:
- Voorraadboeking + telblad → **Aantal en eenheidsprijs per item** _(lijst)_

**📤 Output**:
- Inventarislijst voorraad → **Totaalwaarde voorraad** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Maak telbladen per magazijnplaats.
2. Tel item per item door 2 personen onafhankelijk; vergelijk.
3. Waardeer aan aanschaffingswaarde, vervangingswaarde of marktwaarde (de laagste — voorzichtigheidsbeginsel).
4. Vergelijk met boekhoudkundige voorraad → verschil = inventarisverschil.


> [!example]- Voorbeeld: Meubelzaak Mertens BV: boekhoudkundige voorraad op 31/12 = € 184.500; fysieke telling levert € 175.800 op
> Meubelzaak Mertens BV: boekhoudkundige voorraad op 31/12 = € 184.500; fysieke telling levert € 175.800 op.
>
> 1. **Verschil boekhouding / fysieke telling** 🧮
>
>    Boekhouding:  € 184.500
>    Fysiek:       € 175.800
>    **Verschil:**  € 8.700 negatief (verlies/diefstal/breuk)
>
> 2. **Correctieboeking diversendagboek** 📝
>
>    Debet 609 Voorraadcorrecties (kosten) € 8.700 / Credit 34 Voorraad € 8.700
>    (Som debet = som credit ✓)
>

**Grondslag**: WER art. III.89; CBN 174/1

### 3. Verifieer vorderingen en schulden

Maak een lijst van openstaande klantenvorderingen (op basis van de hulpklantenrekening), leveranciersschulden, bank, andere financiële schulden. Vraag eventueel saldobevestigingen.

**Waarom?** Open vorderingen kunnen geheel of gedeeltelijk oninbaar zijn; schulden kunnen ontbreken (verplichtingen die nog niet zijn gefactureerd). Zonder verificatie ontstaat een verkeerd vermogensbeeld.

**📥 Input**:
- Hulpklantenrekening + leveranciersrekening → **Openstaand bedrag** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Inventarislijst vorderingen en schulden → **Geverifieerd saldo** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Print de openstaande klantenlijst en leveranciersposten per balansdatum.
2. Voor grote saldi: stuur saldobevestigingen.
3. Beoordeel inbaarheid: voor twijfelachtige vorderingen → waardevermindering boeken (zie [[bedrijfsvorderingen-waardevermindering]]).
4. Check schulden die nog niet gefactureerd zijn: ontvangen goederen zonder factuur, gewerkte uren personeel december, etc. → overlopende rekeningen.


**Grondslag**: WER art. III.89

### 4. Pas waarderingsregels toe

Waardeer elke inventaris-post volgens de geldende waarderingsregels van de onderneming (aanschaffingswaarde, afschrijvingen, voorzichtigheidsbeginsel, going concern).

**Waarom?** Een ruwe inventarislijst zegt 'wat er is'; pas de waardering geeft 'wat het waard is op deze datum'.

**🛠️ Hoe**:

1. Vaste activa: aanschaffingswaarde minus geboekte afschrijvingen (zie afschrijvingsplan).
2. Voorraden: lagere van aanschaffingswaarde en marktwaarde.
3. Vorderingen: nominale waarde minus waardeverminderingen voor oninbaarheid.
4. Schulden: terugbetalingswaarde.
5. Vreemde valuta: omrekenen tegen slotkoers (uitzonderingen).


**Grondslag**: KB 21 oktober 2018; CBN 174/1

### 5. Schrijf de inventaris over in het inventarisboek

De volledige inventaris en de jaarrekening worden overgeschreven in een inventarisboek dat samen met de andere boekhoudstukken wordt bewaard (minstens 7 jaar).

**Waarom?** Het inventarisboek is het tastbaar spoor van de jaarrekening — controleerbaar door fiscus, commissaris of curator.

**🛠️ Hoe**:

1. Stel inventarislijst op (gestructureerd per balansrubriek).
2. Schrijf samen met jaarrekening over in inventarisboek.
3. Onderteken (bestuursorgaan).
4. Bewaar 7 jaar.


**Grondslag**: WER art. III.86 (bewaring); CBN 174/1


## Valkuilen

> [!warning]- De inventaris is niet 'gewoon de boekhoudkundige saldi'
> ⚠️ De inventaris is niet 'gewoon de boekhoudkundige saldi'. Het is een onafhankelijke vaststelling per fysieke telling, contractcheck en waardering. Wie enkel het balanscijfer overschrijft, voldoet niet aan de inventarisplicht. ⚖️
>
> _Bron: CBN 174/1_



## Zie ook

- **Getriggerd door**: [[eindejaarsverrichtingen]]
- **Vereist kennis van**: [[waarderingsregels-jaarrekening]]

## Bronnen

[^1]: `CBN-0174-01-beginselen-van-een-regelmatige-boekhouding__sec_regels-die-voor-elke-bedrijfsboekhouding-gelden`
[^2]: `CBN-0174-01-beginselen-van-een-regelmatige-boekhouding__sec_volledigheid-van-de-boekhouding-en-van-de-inventaris`
[^3]: `CBN-0003-02-niet-in-de-balans-opgenomen-rechten-en-verplichtingen__sec_top_part1`
