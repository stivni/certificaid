---
title: Uitvoeren van risico-inschatting en bepalen van het materieel belang in een
  audit
tags:
- competentie
- po-1-6
programmaonderdelen:
- '1.6'
status: voorgesteld
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/uitvoeren-risico-inschatting-en-materialiteit-audit.json
gegenereerd_op: '2026-05-18'
---
# Uitvoeren van risico-inschatting en bepalen van het materieel belang in een audit

**⚖️ 75% · 🤖 25%**

> Het auditrisicomodel en de plicht tot risico-inschatting zijn dwingend opgenomen in de ITAA KMO-controlenorm §75-§95 en de algemene controlenorm. De keuze van het materialiteitspercentage (typisch 0,5–5 %) en de calibratie van inherent + intern-beheersingsrisico per bewering is professionele oordeelsvorming.

## Aanbevolen werkwijze

### 1. Vaststellen van het materieel belang op jaarrekening-niveau

Kies een benchmark (winst vóór belastingen, omzet, totaal activa, eigen vermogen) en pas een percentage toe om het algemene materialiteitsbedrag te bepalen.

**Waarom?** Het materialiteitsbedrag stuurt zowel de scope (welke posten test ik?) als de evaluatie (welke afwijkingen zijn relevant?).

**📥 Input**:
- Voorlopige cijfers boekjaar → **Winst vóór belastingen, omzet, totaal activa, eigen vermogen** _(boekhoudkundig-bedrag)_
- Historische cijfers (drie boekjaren) → **Trend benchmark** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Werkpapier 'materialiteit' → **Benchmark + percentage + bedrag** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Selecteer een benchmark volgens [[materieel-belang-audit]] §benchmark — voor een winstgevende NV typisch 'winst vóór belastingen', voor verlieslatende: 'omzet' of 'totaal activa'.
2. Pas een redelijk percentage toe (illustratief 5 % van winst vóór belastingen, 0,5–1 % van omzet of totaal activa) en motiveer.
3. Bereken een 'performance materiality' (typisch 50–75 % van het algemene materialiteitsbedrag) om risico op aggregatie van ongedetecteerde fouten te dekken.
4. Bepaal ook een 'duidelijk te verwaarlozen drempel' (Clearly Trivial Threshold, typisch 5 % van materialiteit) waarboven afwijkingen worden gedocumenteerd.


> [!example]- Voorbeeld: Rotex Roeselare NV — voorlopige winst vóór belastingen € 4.500.000, omzet € 38.000.000, totaal activa € 27.000.000
> Rotex Roeselare NV — voorlopige winst vóór belastingen € 4.500.000, omzet € 38.000.000, totaal activa € 27.000.000.
>
> 1. **Keuze benchmark** 💬
>
>    Vennootschap is winstgevend en niet beursgenoteerd → benchmark = winst vóór belastingen.
>    
>
> 2. **Berekening algemene materialiteit** 🧮
>
>    algemene materialiteit = 5 % × € 4.500.000 = **€ 225.000**
>    
>
> 3. **Performance materiality + clearly trivial** 🧮
>
>    performance materiality = 60 % × € 225.000 = **€ 135.000**
>    clearly trivial threshold = 5 % × € 225.000 = **€ 11.250**
>    
>

**Grondslag**: [[materieel-belang-audit]] §benchmark, ITAA KMO-controlenorm §86-§91

> [!warning]- Materialiteit herbeoordelen indien voorlopige cijfers significant wijzigen tijdens het werk.
>
> _Vaak fout gedaan_: Materialiteit eenmalig vaststellen op planningsmoment en niet herbeoordelen wanneer eindcijfers materieel afwijken.
>
> _Grondslag_: [[materieel-belang-audit]] §herbeoordeling

### 2. Toepassen van het auditrisicomodel per bewering en rubriek

Schat inherent risico (IR) en intern-beheersingsrisico (IBR) per significante rubriek + bewering; calibreer ontdekkingsrisico (OR) om aanvaardbaar controlerisico (AR) te bereiken.

**Waarom?** Het model dwingt expliciete keuze waar je gegevensgerichte werkzaamheden of testen van interne beheersing inzet — de basis van een verdedigbaar werkprogramma.

**📥 Input**:
- Werkpapier kennis cliënt + omgeving (zie [[verwerven-kennis-van-clientonderneming-audit]]) → **Externe + interne risicofactoren** _(document)_
- Lijst beweringen per rubriek → **Bestaan, volledigheid, waardering, eigendom, presentatie** _(document)_

**📤 Output**:
- Risicomatrix per rubriek × bewering → **IR / IBR / OR-classificatie hoog/middel/laag** _(document)_

**🛠️ Hoe**:

1. Bouw een matrix met rubrieken (omzet, voorraden, vaste activa, voorzieningen, ...) in de rijen en beweringen ([[beweringen-audit]] §lijst) in de kolommen.
2. Schat IR per cel — bv. omzet × bestaan = hoog (typisch fraude-risico bij omzeterkenning).
3. Schat IBR per cel op basis van de IC-walkthrough — bv. voorraden × waardering = middel (geen sterke voorraadcontroles bij Rotex).
4. Bepaal het aanvaardbaar AR (typisch laag, ≤ 5 %) en bereken het residueel OR via het model uit [[auditrisicomodel]] §formule.
5. Markeer de cellen 'OR = laag' — daar plan je uitgebreid gegevensgericht werk; cellen 'OR = hoog' kunnen volstaan met cijferanalyse + selectieve testen.


> [!example]- Voorbeeld: Rotex Roeselare NV — risicomatrix voor twee posten
> Rotex Roeselare NV — risicomatrix voor twee posten.
>
> 1. **Voorbeeld-cellen uit risicomatrix** 🧮
>
>    | Rubriek × Bewering              | IR    | IBR   | Aanvaardbaar AR | Residueel OR |
>    |---------------------------------|-------|-------|-----------------|--------------|
>    | Omzet × bestaan (fraude-vermoeden) | hoog  | middel| laag (5 %)      | **laag**     |
>    | Vaste activa × waardering          | laag  | laag  | laag (5 %)      | middel       |
>    
>    → Omzet × bestaan: zwaar gegevensgericht testen + steekproef facturen + verzendbewijzen.
>    → Vaste activa × waardering: cijferanalyse + selectieve test op grote bewegingen.
>    
>

**Grondslag**: [[auditrisicomodel]] §formule, [[risico-inschatting-audit]] §matrix, ITAA KMO-controlenorm §75-§78

### 3. Identificeren en apart markeren van significante risico's

Markeer specifieke risico's als 'significant risk' (bv. omzet-erkenning, complexe schattingen, fraude-vermoeden) — die vragen aangepast werk.

**Waarom?** Significante risico's vereisen volgens [[significant-risico-audit]] §respons specifieke procedures, geen reliance op test van controls alleen.

**📥 Input**:
- Risicomatrix uit stap 2 → **Cellen met IR hoog + complexiteit** _(document)_
- Fraude-overwegingen volgens [[fraude-versus-fout]] → **Indicatoren management override + omzet-erkenning** _(document)_

**📤 Output**:
- Lijst 'significante risico's' → **Risico + bewering + plan respons** _(document)_

**🛠️ Hoe**:

1. Loop de risicomatrix door en markeer als 'significant' elke cel die voldoet aan de criteria uit [[significant-risico-audit]] §criteria — complexiteit, oordeelsvorming, niet-routinematig, fraude-risico.
2. Volgens [[fraude-versus-fout]] §verplicht-significant: omzet-erkenning is standaard een significant risico tenzij weerlegd; management-override blijft altijd significant.
3. Plan voor elk significant risico een specifieke respons: gegevensgericht detailwerk, externe bevestigingen, of inzet van een specialist (fiscalist, IT-auditor).


**Grondslag**: [[significant-risico-audit]] §criteria, ITAA KMO-controlenorm §80

> [!warning]- Omzet-erkenning standaard als significant risico opnemen, en alleen bij gemotiveerde redenering uitsluiten.
>
> _Vaak fout gedaan_: Omzet als laag risico classificeren omdat de boekhouder ervaren is — fraude-presumptie blijft.
>
> _Grondslag_: [[fraude-versus-fout]] §verplicht-significant

### 4. Documenteren van risico-inschatting en materialiteit

Leg de matrix, het materialiteitsbedrag, de significant risks en de gekozen respons-strategie vast in het controledossier.

**Waarom?** Volgens [[controledocumentatie]] §minimuminhoud is documentatie van risico-inschatting verplicht — voor latere review én voor tuchtonderzoek.

**📥 Input**:
- Werkpapieren stap 1–3 → **Materialiteit + risicomatrix + significant risks** _(document)_

**📤 Output**:
- Sectie 'risico-inschatting' in controledossier → **Eindversie + handtekening opdrachtverantwoordelijke** _(document)_

**🛠️ Hoe**:

1. Bundel de werkpapieren in een logische volgorde — externe omgeving → interne organisatie → risicomatrix → materialiteit → significant risks.
2. Laat het document beoordelen + ondertekenen door de opdrachtverantwoordelijke (Sofie Janssens) vóór de uitvoeringsfase start.
3. Plan een herziening op het einde van de tussenfase en vóór het sluiten van de eindfase (zie [[opstellen-auditstrategie-en-werkprogramma]] §bijsturing).


**Grondslag**: [[controledocumentatie]] §minimuminhoud, ITAA KMO-controlenorm §95


## Voorbeelden

> [!example]- Rotex Roeselare NV — voorlopige winst € 4.500.000 (vorig jaar € 2.000.000)
> **Conclusie**: Materialiteit herbeoordelen: 5 % × € 1.800.000 = € 90.000. Performance materiality van € 54.000. Voorraad-testresultaten van € 100.000-afwijking, eerder als 'binnen materialiteit' geklasseerd, kan nu materieel worden. Uitbreiden van testen vereist.
>
> **Grondslag**: [[materieel-belang-audit]] §herbeoordeling
>
> **Redenering**: Materialiteit volgt de uiteindelijke benchmark. Een eenmalige voorziening die winst halveert dwingt revisie van zowel materialiteit als planning. Niet-bijsturen = werkprogramma is overschatte zekerheid.

> [!example]- Meubelzaak Mertens BV — kassa-verkopen € 1.200.000 op jaaromzet € 2.800.000
> **Conclusie**: Wel significant risico → omzet-erkenning + fraude-vermoeden. Respons: gegevensgericht. Reconstrueer kasstromen + match met BTW-aangiftes + steekproef-tellingen onaangekondigd. Reliance op controls niet mogelijk.
>
> **Grondslag**: [[fraude-versus-fout]] §management-override; [[significant-risico-audit]] §criteria
>
> **Redenering**: Eenmansbestuur + geen scheiding van functies + cash-intensieve activiteit = klassiek scenario voor management-override van controls. Standaard significant risico zonder hertoetsing.


## Gebaseerd op concepten

[[risico-inschatting-audit]] · [[auditrisicomodel]] · [[materieel-belang-audit]] · [[significant-risico-audit]] · [[beweringen-audit]] · [[fraude-versus-fout]] · [[inherent-risico]] · [[intern-beheersingsrisico]] · [[ontdekkingsrisico]]
## Voortkomend uit

- **Taken**: 1.6.taak.1
- **Kenniselementen**: 1.6.II.B, 1.6.II, 1.6.III.A
