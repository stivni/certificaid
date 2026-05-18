---
title: Opstellen van de auditstrategie en het werkprogramma
tags:
- competentie
- po-1-6
programmaonderdelen:
- '1.6'
status: voorgesteld
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/opstellen-auditstrategie-en-werkprogramma.json
gegenereerd_op: '2026-05-18'
---
# Opstellen van de auditstrategie en het werkprogramma

**⚖️ 70% · 🤖 30%**

> De auditplanning op twee lagen (strategie + werkprogramma) is wettelijk geregeld in de ITAA KMO-controlenorm §70-§73 en de algemene controlenorm. Concrete teamsamenstelling, timing en allocatie van uren over werkzaamheden is praktisch beheer en valt onder professionele oordeelsvorming.

## Aanbevolen werkwijze

### 1. Algemene auditstrategie formuleren

Documenteer scope, timing, te leveren rapportering, materieel belang, sleutelrisico's en middelen op één strategie-document.

**Waarom?** De strategie kadert het werkprogramma en zorgt dat de hele audit dezelfde focus en deadlines volgt.

**📥 Input**:
- Materialiteit + risicomatrix uit [[uitvoeren-risico-inschatting-en-materialiteit-audit]] → **Bedrag + significante posten** _(boekhoudkundig-bedrag)_
- Mandaat-document + opdrachtbrief → **Scope + deadlines** _(document)_

**📤 Output**:
- Strategie-memo (typisch 2–4 pagina's) → **Scope, timing, team, sleutelrisico's, materialiteit** _(document)_

**🛠️ Hoe**:

1. Vermeld scope: 'wettelijke controle jaarrekening 2025 + bestuursverslag + controleverslag art. 3:75 WVV'.
2. Vermeld timing: tussenfase (typisch okt-dec) + eindfase (typisch feb-mrt) + datum verslag (typisch 30 dagen na bestuursorgaan).
3. Bepaal teamsamenstelling — junior, senior, manager, opdrachtverantwoordelijke (Sofie Janssens), eventueel specialisten (IT-auditor, fiscalist).
4. Vermeld de gekozen materialiteit + performance materiality + clearly trivial threshold.
5. Lijst de drie tot vijf sleutelrisico's op en de gekozen reactie-strategie ('substantive only' / 'reliance op IC' / 'mixed').


**Grondslag**: [[auditstrategie]] §inhoud, ITAA KMO-controlenorm §72

### 2. Werkprogramma per rubriek uitwerken

Per significante rubriek en bewering: vertaal de risicomatrix naar concrete controlewerkzaamheden met aard (test of control / substantive), timing (interim / final) en omvang (steekproefgrootte).

**Waarom?** Het werkprogramma is de praktische uitvoeringsgids — junioren moeten erop kunnen werken zonder zelf de strategie te herbeoordelen.

**📥 Input**:
- Risicomatrix per rubriek × bewering → **IR / IBR / OR-classificatie** _(document)_
- Vorig-jaar werkprogramma indien lopend mandaat → **Goede practices + lacunes** _(document)_

**📤 Output**:
- Werkprogramma-spreadsheet per rubriek → **Werkzaamheid + uitvoerder + budget-uren** _(document)_

**🛠️ Hoe**:

1. Maak een werkblad per rubriek (omzet, voorraden, vaste activa, ...).
2. Per cel rubriek × bewering met OR = laag: plan minstens één gegevensgerichte werkzaamheid uit [[selecteren-en-uitvoeren-controle-instrumenten-audit]] §gereedschap.
3. Per cel met OR = middel/hoog: cijferanalyse of selectieve test volstaat — maar documenteer waarom OR aanvaardbaar is.
4. Geef per werkzaamheid een budget (uren) + verantwoordelijke + deadline.
5. Markeer in [[werkprogramma-audit]] §kruisverwijzing dat het werkprogramma terugverwijst naar de relevante risico-cel.


> [!example]- Voorbeeld: Werkprogramma-uittreksel voor rubriek Voorraden bij Rotex Roeselare NV
> Werkprogramma-uittreksel voor rubriek Voorraden bij Rotex Roeselare NV.
>
> 1. **Uittreksel werkprogramma voorraden** 💬
>
>    | Bewering    | Werkzaamheid                                      | Aard         | Timing  | Steekproef | Uitvoerder | Budget |
>    |-------------|---------------------------------------------------|--------------|---------|------------|-----------|--------|
>    | Bestaan     | Voorraadopname bijwonen op 31/12                  | substantive  | final   | n.v.t.     | Senior    | 8u     |
>    | Bestaan     | Steekproef 25 items tellen + naar grootboek matchen | substantive | final  | 25 items   | Junior    | 6u     |
>    | Waardering  | Berekening last-in/first-out + slow movers (>180d) | substantive  | final  | volledig   | Senior    | 6u     |
>    | Volledigheid| Cut-off test 5 dagen ervoor + 5 erna              | substantive  | final   | 10 items   | Junior    | 4u     |
>    
>

**Grondslag**: [[werkprogramma-audit]] §opbouw, ITAA KMO-controlenorm §71

### 3. Reviewen en goedkeuren vóór uitvoering

Laat de strategie + het werkprogramma reviewen door de opdrachtverantwoordelijke (en de Engagement Quality Reviewer indien aangewezen) vóór de uitvoering start.

**Waarom?** Vier-ogen-principe bij planning vermijdt blinde vlekken en is een hoeksteen van [[kwaliteitsbeheersing-opdrachtniveau]].

**📥 Input**:
- Strategie-memo + werkprogramma → **Concept-versies** _(document)_

**📤 Output**:
- Goedgekeurde strategie + werkprogramma → **Met handtekeningen en datum** _(document)_

**🛠️ Hoe**:

1. Plan een planningsmeeting met het volledige team + Sofie Janssens als opdrachtverantwoordelijke.
2. Bespreek de sleutelrisico's, de reactie-strategie en de werkverdeling.
3. Pas waar nodig aan na de meeting; laat de definitieve versie ondertekenen.
4. Bij OOB / beursgenoteerd: laat ook de Engagement Quality Reviewer expliciet aftekenen op strategie.


**Grondslag**: [[auditplanning]] §review, ITAA KMO-controlenorm §73

### 4. Doorlopend bijsturen tijdens uitvoering

Update strategie en werkprogramma telkens nieuwe informatie of risico's opduiken (bv. fraude-vermoeden, materiële wijziging in cijfers, gewijzigde regelgeving).

**Waarom?** Een audit is iteratief: de planning is een vertrekpunt, niet een vast contract met de werkelijkheid.

**📥 Input**:
- Bevindingen tussentijdse fase → **Wijzigingen IC / cijfers / context** _(document)_

**📤 Output**:
- Geactualiseerd werkprogramma + audit trail van wijzigingen → **Wijzigingen + reden + datum** _(document)_

**🛠️ Hoe**:

1. Bij elke materiële bevinding: heroverweeg of risicomatrix bijgewerkt moet worden.
2. Documenteer de wijziging in het werkprogramma volgens [[controledocumentatie]] §wijzigingsregister.
3. Indien materialiteit wijzigt: herbereken performance materiality en herzie steekproefgroottes in lopende testen.


**Grondslag**: [[auditplanning]] §bijsturing, ITAA KMO-controlenorm §73

> [!warning]- Wijzigingen aan strategie + werkprogramma altijd schriftelijk + gedateerd documenteren.
>
> _Vaak fout gedaan_: Mondeling bijsturen tijdens veldwerk zonder paper trail — review en latere verdediging onmogelijk.
>
> _Grondslag_: [[controledocumentatie]] §wijzigingsregister


## Voorbeelden

> [!example]- Wolters & Partners CVBA plant de controle van Rotex Roeselare NV
> **Conclusie**: Bijsturing: IT-auditor toevoegen aan team; werkprogramma uitbreiden met data-validatie tussen oude + nieuwe systeem; materialiteit reviewen indien dataverlies invloed heeft op cijfers. Strategie-document update met handtekening.
>
> **Grondslag**: [[auditplanning]] §bijsturing; [[auditstrategie]] §wijziging-context
>
> **Redenering**: IT-migratie tijdens boekjaar = nieuw inherent risico op volledigheid en cut-off. Werkprogramma dat geen data-validatie omvat = audit-bewijs onvoldoende.

> [!example]- Voor de controle van Meubelzaak Mertens BV (omzet € 2,8 M) plant Sofie Janssens 80 uren — 40 uur senior, 40 uur junior
> **Conclusie**: Uitbreiden van voorraadwerk met 6 extra uren (alternatieve tests: cut-off + analyse rotatie + steekproef facturen leveranciers). Werkprogramma-update + uren-budget bijgewerkt + reden gedocumenteerd.
>
> **Grondslag**: [[werkprogramma-audit]] §alternatieve-tests
>
> **Redenering**: Onvolledige voorraadopname = onvoldoende substantive evidence voor bewering 'bestaan'. Alternatieve werkzaamheden vereist, anders kan oordeel niet zonder voorbehoud.


## Gebaseerd op concepten

[[auditstrategie]] · [[auditplanning]] · [[werkprogramma-audit]] · [[risico-inschatting-audit]] · [[materieel-belang-audit]] · [[controledocumentatie]]
## Voortkomend uit

- **Taken**: 1.6.taak.1
- **Kenniselementen**: 1.6.III.A, 1.6.III.B, 1.6.III
