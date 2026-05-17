---
title: Selecteren en uitvoeren van controle-instrumenten (test of controls + gegevensgerichte
  werkzaamheden)
tags:
- competentie
- po-1-6
programmaonderdelen:
- '1.6'
status: voorgesteld
schema_version: '1.1'
gegenereerd_uit: data/concepten/competenties/selecteren-en-uitvoeren-controle-instrumenten-audit.yaml
gegenereerd_op: '2026-05-17'
---
# Selecteren en uitvoeren van controle-instrumenten (test of controls + gegevensgerichte werkzaamheden)

**⚖️ 75% · 🤖 25%**

> De ITAA KMO-controlenorm §96-§120 + de algemene controlenorm leggen een gesloten lijst van controle-instrumenten op (test of controls, gegevensgerichte werkzaamheden, cijferanalyse, externe bevestiging, steekproef, schriftelijke bevestiging). De keuze + dosering tussen instrumenten is risico-gestuurd professioneel oordeel.

## Aanbevolen werkwijze

### 1. Per bewering een instrument selecteren

Kies per cel rubriek × bewering uit de risicomatrix het meest geschikte controle-instrument (of combinatie).

**Waarom?** Het instrument moet passen bij het risico: niet alle beweringen worden even goed gedekt door alle instrumenten (bv. externe bevestiging dekt bestaan, niet volledigheid).

**📥 Input**:
- Werkprogramma per rubriek × bewering → **Gevraagd type werkzaamheid + omvang** _(document)_
- Risicomatrix met IR + IBR + OR → **Per cel risicoclassificatie** _(document)_

**📤 Output**:
- Instrument-keuze per werkzaamheid → **Naam instrument + motivering** _(document)_

**🛠️ Hoe**:

1. Kies bij 'bestaan' + extern bewijs: voorkeur voor [[externe-bevestiging-audit]] (bank, debiteuren, advocaat).
2. Kies bij 'volledigheid': cut-off + cijferanalyse + 'beneden-naar-boven'-test (bv. levering → factuur).
3. Kies bij 'waardering' + complexe schatting: substantive detail-test + werk van specialist + [[schriftelijke-bevestiging-management]] over uitgangspunten.
4. Bij sterke IC met OR = middel/hoog: combineer [[toetsing-interne-beheersing]] § test of controls met beperkte substantive werkzaamheden.


**Grondslag**: [[assurance-informatie]] §toepasselijkheid-per-bewering, ITAA KMO-controlenorm §103

### 2. Test of controls uitvoeren wanneer reliance gepland is

Test of de geïdentificeerde sleutelcontroles bij de cliënt effectief functioneren tijdens de gecontroleerde periode.

**Waarom?** Reliance op IC mag alleen indien tests bevestigen dat controles effectief zijn (ITAA KMO-controlenorm §107).

**📥 Input**:
- IC-walkthrough + flowchart uit [[verwerven-kennis-van-clientonderneming-audit]] → **Sleutelcontroles per cyclus** _(document)_

**📤 Output**:
- Testresultaat IC per controle → **Effectief / niet-effectief** _(conclusie)_

**🛠️ Hoe**:

1. Selecteer per cyclus 1–3 sleutelcontroles die je wilt steunen (bv. 'goedkeuring van betaling > € 5.000 door tweede ondertekenaar').
2. Test elke controle op een steekproef van bv. 25 transacties over de gecontroleerde periode volgens [[toetsing-interne-beheersing]] §steekproef.
3. Documenteer per geteste transactie of de controle effectief uitgevoerd is (handtekening, parafering, log).
4. Bij > 1 afwijking op 25: controle is niet betrouwbaar → val terug op uitgebreidere gegevensgerichte werkzaamheden in stap 3.


**Grondslag**: [[toetsing-interne-beheersing]] §uitvoering, ITAA KMO-controlenorm §107

> [!warning]- Pas reliance op IC alleen toe wanneer test of controls slaagt; documenteer fallback bij falen.
>
> _Vaak fout gedaan_: Test of controls plannen maar fallback niet voorbereid — bij falen geen tijd meer voor substantive werk.
>
> _Grondslag_: [[toetsing-interne-beheersing]] §fallback

### 3. Gegevensgerichte werkzaamheden uitvoeren

Voer detail-tests, cijferanalyse en externe bevestigingen uit om bewijs te verzamelen over de cijfers zelf.

**Waarom?** Gegevensgerichte werkzaamheden zijn altijd vereist bij significante risico's en bij OR = laag — onafhankelijk van IC-test-uitkomst.

**📥 Input**:
- Grootboek + subadministraties + saldobalans → **Per rubriek detailcijfers** _(boekhoudkundig-bedrag)_
- Steekproefkaders (facturen, contracten, bankafschriften) → **Populaties per test** _(document)_

**📤 Output**:
- Werkpapieren met testbevindingen per rubriek → **Bevinding + afwijking + extrapolatie** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Voor materiële posten: detail-test op een statistische of stelselmatige steekproef volgens [[steekproef-audit]] §omvang.
2. Voor stabiele posten met sterke correlatie: cijferanalyse volgens [[cijferanalyses-audit]] §verwachting-vs-werkelijk (bv. omzet × marge → bruto winst).
3. Voor extern bewijs: stuur bevestigingsbrieven volgens [[externe-bevestiging-audit]] §procedure (positief voor materiële saldi, negatief voor populaties).
4. Bij bewering 'volledigheid': start vanuit een externe bron (bv. bankafschriften, leveringsbonnen) en match terug naar de boekhouding.


> [!example]- Voorbeeld: Rotex Roeselare NV — handelsvorderingen € 4.200.000 verdeeld over 145 klanten
> Rotex Roeselare NV — handelsvorderingen € 4.200.000 verdeeld over 145 klanten. Sofie Janssens kiest een positieve confirmatie voor de top-10 klanten (€ 2.800.000) en een steekproef van 30 saldi uit de overige.
>
> 1. **Dekking-berekening** 🧮
>
>    top-10 klanten gedekt = € 2.800.000 (67 % van totaal)
>    steekproef 30 saldi uit € 1.400.000 resterend
>    verwachte dekking gecombineerd ≥ 75 % van populatie — voldoende
>    
>
> 2. **Bevestigingsbrief sjabloon** 💬
>
>    "Geachte heer/mevrouw, in het kader van onze controle van Rotex Roeselare NV
>    verzoeken wij u te bevestigen of het door Rotex aangegeven openstaand saldo
>    van € XXX op 31/12/2025 met uw boekhouding overeenstemt. Gelieve te
>    antwoorden aan Wolters & Partners CVBA per beveiligde e-mail of
>    ondertekende fax."
>    
>
> 3. **Verwerking antwoorden** 💬
>
>    Geen antwoord op 2 van 10: alternatieve test — match met bankafschriften
>    januari (betalingen na balansdatum bevestigen vordering).
>    Verschil bij 1 antwoord (€ 25.000 minder bij klant) → onderzoek geschil
>    of niet-erkende creditnota → mogelijke afwijking € 25.000.
>    
>

**Grondslag**: [[gegevensgerichte-werkzaamheden]] §typologie, ITAA KMO-controlenorm §96-§102

### 4. Schriftelijke bevestiging van management opvragen

Verkrijg op het einde van de werkzaamheden een schriftelijke bevestiging van het management over assertions die niet via andere bron volledig te dekken zijn (intenties, kennis fraude, volledigheid mededelingen).

**Waarom?** ISA / ITAA-normen vereisen een management representation letter; vaak verplicht element van het dossier.

**📥 Input**:
- Sjabloon-bevestigingsbrief → **Standaardparagrafen + cliënt-specifieke aanvullingen** _(document)_

**📤 Output**:
- Ondertekende bevestiging door bestuur → **Datum = datum verslag of vlak ervoor** _(document)_

**🛠️ Hoe**:

1. Stel de brief op met de standaardclausules uit [[schriftelijke-bevestiging-management]] §inhoud + cliënt-specifieke aanvullingen (rechtszaken, verbonden partijen, going concern).
2. Datum van de brief = datum verslag (of binnen een paar dagen ervoor).
3. Bij weigering management om te ondertekenen: dat is een beperking → mogelijk aangepast oordeel volgens [[opstellen-controleverslag-en-formuleren-oordeel]] §scope-beperking.


**Grondslag**: [[schriftelijke-bevestiging-management]] §verplicht-element, ITAA KMO-controlenorm §119


## Voorbeelden

> [!example]- Bij Rotex Roeselare NV staat het bankrekeningensaldo op € 1.800.000
> **Conclusie**: Bevestigingsbrief aan de bank is vereist — een uittreksel toont alleen saldo, geen verborgen rechten/plichten (pand, kredietlijnen, derivaten, niet-uitgevoerde transfers). Brief vraagt alle accounts + relaties van Rotex bij de bank.
>
> **Grondslag**: [[externe-bevestiging-audit]] §bank-volledigheid
>
> **Redenering**: Bewering 'volledigheid' op rekeningen + 'rechten en verplichtingen' op kredietlijnen kan alleen via bevestiging — niet via uittreksel.

> [!example]- Meubelzaak Mertens BV — voorraad € 180.000 op 31/12
> **Conclusie**: Alternatieve tests: (a) cut-off test 5 dagen voor/na 31/12 op inkomende + uitgaande leveringen; (b) cijferanalyse rotatie (voorraad/COGS); (c) onaangekondigde steekproef-telling in januari + terugrekenen naar 31/12 via bewegingen. Indien alternatieve tests onvoldoende: scope-beperking → aangepast oordeel.
>
> **Grondslag**: [[gegevensgerichte-werkzaamheden]] §alternatieve-procedures
>
> **Redenering**: Voorraadopname niet bijwonen = bewering 'bestaan' niet rechtstreeks gedekt. Alternatieve werkzaamheden zijn aanvaardbaar maar geen volwaardige vervanging — moeten samen voldoende bewijs leveren.


## Gebaseerd op concepten

[[gegevensgerichte-werkzaamheden]] · [[toetsing-interne-beheersing]] · [[cijferanalyses-audit]] · [[externe-bevestiging-audit]] · [[steekproef-audit]] · [[schriftelijke-bevestiging-management]] · [[beweringen-audit]] · [[assurance-informatie]]
## Voortkomend uit

- **Taken**: 1.6.taak.1
- **Kenniselementen**: 1.6.II.C, 1.6.II
