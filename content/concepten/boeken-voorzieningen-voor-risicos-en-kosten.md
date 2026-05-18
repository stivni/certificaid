---
title: Boeken van een voorziening voor risico's en kosten
tags:
- concept
- competentie
- po-1-1
linked_anchors:
- 1.1.taak.1
- 1.1.II.I
programmaonderdelen:
- '1.1'
confidence: inferred
node_type: competentie
status: voorgesteld
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/boeken-voorzieningen-voor-risicos-en-kosten.json
gegenereerd_op: '2026-05-18'
---
# Boeken van een voorziening voor risico's en kosten 🤖


## Stappen

### 1. Identificeer de potentiële last of risico

Stel vast of er op balansdatum een gebeurtenis is die in de toekomst tot uitgave zal leiden.

**Waarom?** Een voorziening is alleen gerechtvaardigd als er werkelijk een toekomstige verplichting bestaat ter gevolge van een gebeurtenis vóór balansdatum.

**📥 Input**:
- Bestuurlijke briefing + juridische dossiers + contracten → **Lopende geschillen, garanties, herstructureringsplannen, pensioenbeloftes** _(document)_

**📤 Output**:
- Lijst risico-events → **Per event: oorsprong, waarschijnlijkheid, geschat bedrag** _(conclusie)_

**🛠️ Hoe**:

1. Overloop met bestuurder de lopende geschillen, garanties, beloftes — zie [[voorzieningen]] §types.
2. Typische categorieën: pensioenverplichtingen (rubriek 160), belastingverplichtingen (161), grote herstellingen/onderhoud (162), andere risico's en kosten (163-164).
3. Bij Naaiatelier Ninove BV — schade-claim € 22.000 wegens defecte levering, advocaat oordeelt "veroordeling waarschijnlijk in 2027".
4. Bij Rotex Roeselare NV — herstructureringsplan aangekondigd in december 2026, ontslagvergoedingen geschat € 480.000.
5. Documenteer in werkdocument.


**Grondslag**: [[voorzieningen]] §scope, KB-WVV art. 3:11

### 2. Toets de drie voorwaarden voor verplichte voorziening

Verifieer of de gebeurtenis voldoet aan de cumulatieve voorwaarden van het voorzichtigheidsbeginsel.

**Waarom?** Niet elk risico vraagt voorziening — alleen waarschijnlijke verplichtingen waarvan oorsprong vóór balansdatum ligt en bedrag betrouwbaar te schatten is.

**📥 Input**:
- Risico-event uit stap 1 → **Oorsprong, waarschijnlijkheid, bedrag** _(conclusie)_

**📤 Output**:
- Beslissing voorziening Ja/Nee → **Conclusie + grondslag** _(conclusie)_

**🛠️ Hoe**:

1. Toets voorwaarde 1 — Oorsprong vóór balansdatum (bv. dagvaarding ontvangen, fout in product geleverd): Ja/Nee.
2. Toets voorwaarde 2 — Waarschijnlijke uitstroom (> 50% kans): Ja/Nee.
3. Toets voorwaarde 3 — Betrouwbare schatting van bedrag mogelijk: Ja/Nee.
4. Drie maal Ja → verplichte voorziening volgens [[voorzichtigheidsbeginsel]] §verplichting.
5. Als 1 of 2 niet voldaan: alleen toelichting buiten balans (zie [[rechten-verplichtingen-buiten-balans]]).
6. Als 3 niet voldaan: best estimate van bandbreedte; bij ontbreken toets aan IFRS-praktijk (range-midpoint).


**Grondslag**: [[voorzieningen]] §drie-voorwaarden, [[voorzichtigheidsbeginsel]] §verplichting

> [!warning]- Boek geen voorziening voor toekomstige bedrijfsverliezen — die zijn pas erkenbaar wanneer ze zich voordoen, niet vooraf.
>
> _Vaak fout gedaan_: Voorziening boeken voor verwachte slechte tijden zonder concrete gebeurtenis vóór balansdatum.
>
> _Grondslag_: [[voorzieningen]] §verboden-gebruik

### 3. Bepaal het bedrag (beste schatting)

Schat het bedrag dat het bestuur het meest waarschijnlijk moet uitgeven bij realisatie van de verplichting.

**Waarom?** Voorziening moet realistisch zijn — overdrijven verlaagt onterecht winst en is fiscaal niet aftrekbaar; onderschatten geeft geen getrouw beeld.

**📥 Input**:
- Documenten met cijfermateriaal → **Schade-eisen, contracten, externe expertise** _(document)_

**📤 Output**:
- Schattings-onderbouwing → **Bedrag + methode + bronnen** _(berekening)_

**🛠️ Hoe**:

1. Bij éénduidig bedrag: gebruik dat bedrag (bv. eis schadeclaim met advocaat-inschatting).
2. Bij bandbreedte: gebruik beste schatting; bij gelijke waarschijnlijkheid → midden van bandbreedte.
3. Voor langlopende voorzieningen (pensioenen, grote herstellingen): contant maken aan een passende rente — zie CBN 2018/25.
4. Bij Naaiatelier Ninove BV — schade € 22.000 is concrete claim; geen contantmaking nodig (kort verwachte uitstroom).
5. Bij Rotex Roeselare NV — herstructurering € 480.000; bestaat uit ontslagvergoedingen volgens CAO-berekening + outplacement.


**Grondslag**: [[voorzieningen]] §bedragbepaling, CBN 2018/25

### 4. Boek de voorziening op balansdatum

Boek de dotatie als kost op rekening 6370 en de tegenpost op de passende voorzienings-rubriek (16X).

**Waarom?** De voorziening verschijnt op passief-zijde van balans en vermindert het resultaat — beide effecten zijn de boekhoudkundige uitdrukking van het voorzichtigheidsbeginsel.

**📥 Input**:
- Schattingsbedrag stap 3 → **Voorzieningsbedrag** _(berekening)_

**📤 Output**:
- Boeking voorziening → **Dotatie + voorzieningsrubriek** _(boekingsregel)_

**🛠️ Hoe**:

1. Boek: Debet 6370 Voorzieningen voor risico's en kosten — toevoeging; Credit 16X Voorzieningen (160 pensioenen, 161 belastingen, 162 grote herstellingen, 163 andere risico's en kosten).
2. Voor Naaiatelier Ninove BV — claim € 22.000: D 6370 € 22.000; C 163 Andere voorzieningen voor risico's en kosten € 22.000.
3. Vermeld aard en bedrag in toelichting bij jaarrekening (KB-WVV art. 3:74).


> [!example]- Voorbeeld: Naaiatelier Ninove BV — schade-claim € 22.000 ontvangen 27/12/2026, advocaat-inschatting 'veroordeling waarschijnlijk in…
> Naaiatelier Ninove BV — schade-claim € 22.000 ontvangen 27/12/2026, advocaat-inschatting 'veroordeling waarschijnlijk in 2027'.
>
> 1. **Boeking voorziening** 📝
>
>    | Datum | Rekening | Omschrijving | Debet | Credit |
>    |---|---|---|---|---|
>    | 31/12/2026 | 6370 Voorzieningen voor risico's en kosten — toev. | schade-claim | € 22.000,00 | |
>    | 31/12/2026 | 163 Andere voorzieningen voor risico's en kosten | claim Ninove | | € 22.000,00 |
>    
>
> 2. **Toelichting bij jaarrekening** 💬
>
>    In de toelichting onder "Voorzieningen": "Op 27/12/2026 ontvingen wij een schade-eis van € 22.000 wegens defecte levering. Advocaat-advies oordeelt veroordeling waarschijnlijk in 2027."
>    
>

**Grondslag**: [[voorzieningen]] §boeking, KB-WVV art. 3:11

### 5. Beheer de voorziening in volgende boekjaren

Pas de voorziening jaarlijks aan naar nieuwe inschatting en hef ze op bij realisatie of bij wegvallen van het risico.

**Waarom?** Voorzieningen zijn dynamisch — overdotatie wordt teruggenomen (opbrengst), onderdotatie aangevuld (extra kost), realisatie boekt de daadwerkelijke uitgave.

**📥 Input**:
- Voortgangsrapport per voorziening → **Status risico, nieuwe inschatting** _(document)_

**📤 Output**:
- Aanpassingsboeking → **Toename, terugname of besteding** _(boekingsregel)_

**🛠️ Hoe**:

1. Bij toename inschatting: Debet 6370; Credit 16X (extra dotatie).
2. Bij afname inschatting: Debet 16X; Credit 7370 Voorzieningen — terugneming.
3. Bij realisatie: Debet 16X; Credit 4400 Schuld of 5500 Bank (uitbetaling); eventueel verschil via 6370 of 7370.
4. Bij volledig wegvallen risico (vonnis in voordeel onderneming): volledige terugneming via 7370.
5. Bij Naaiatelier Ninove BV — uitspraak in 2027: veroordeling € 19.500 → besteding D 163 € 22.000; C 5500 Bank € 19.500; C 7370 Terugneming € 2.500 (overschatting).


**Grondslag**: [[voorzieningen]] §dynamisch-beheer, CBN 2018/25 §opvolging


