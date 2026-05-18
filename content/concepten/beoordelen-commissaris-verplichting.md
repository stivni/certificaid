---
title: Beoordelen of een vennootschap een commissaris moet benoemen en welk regime
  van toepassing is
tags:
- concept
- competentie
- po-1-2
linked_anchors:
- 1.2.IV.E
- 1.2.IV
programmaonderdelen:
- '1.2'
confidence: inferred
node_type: competentie
status: voorgesteld
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/beoordelen-commissaris-verplichting.json
gegenereerd_op: '2026-05-18'
---
# Beoordelen of een vennootschap een commissaris moet benoemen en welk regime van toepassing is 🤖


## Stappen

### 1. Kwalificeer de vennootschap qua grootte en aard

Bepaal of de vennootschap klein/groot is en of ze een PIE is.

**Waarom?** Kleine vennootschappen zijn in beginsel vrijgesteld; PIE's hebben strengere regels.

**📥 Input**:
- Werknotitie groottecriteria + statuten → **Grootteklasse + PIE-status** _(conclusie)_

**📤 Output**:
- Werknotitie → **Klein/groot + wel/niet PIE** _(conclusie)_

**🛠️ Hoe**:

1. Open de resultaten van [[klasseren-vennootschap-naar-groottecategorie]].
2. Toets PIE-status volgens [[public-interest-entity]] §criteria: beursnotering op gereglementeerde markt, kredietinstelling, verzekeringsonderneming.
3. Noteer beide elementen in de werknotitie.


**Grondslag**: [[commissaris]] §toepassingsgebied, WVV art. 3:72

### 2. Pas de hoofdregel toe voor kleine vennootschappen

Kleine vennootschappen zijn in beginsel vrijgesteld van commissaris-benoeming, tenzij ze deel uitmaken van een grote groep.

**Waarom?** Vrijstelling beperkt de kost voor KMO's; verbondenheid heft de vrijstelling op.

**📥 Input**:
- Werknotitie stap 1 → **Klein/groot, PIE-status, eventueel groep** _(conclusie)_

**📤 Output**:
- Tussenstand → **Wel of niet commissaris** _(conclusie)_

**🛠️ Hoe**:

1. Klein én geen PIE én geen lid van een grote groep? → geen commissaris verplicht ([[commissaris]] §uitzondering-klein).
2. Toets groep-context: indien de groep als geheel groot is, vervalt de vrijstelling — zie [[groottecriteria-jaarrekening]] §verbondenheid.
3. Klein én lid grote groep → wel commissaris.
4. Documenteer beslissing en grondslag.


> [!example]- Voorbeeld: Meubelzaak Mertens BV (klein, geen deelnemingen) en Naaiatelier Ninove BV (klein op zich, dochter van Aurelia Holding NV…
> Meubelzaak Mertens BV (klein, geen deelnemingen) en Naaiatelier Ninove BV (klein op zich, dochter van Aurelia Holding NV — groep groot).
>
> 1. **Toets per cliënt** 💬
>
>    | Cliënt | Eigen grootte | Groep-context | Commissaris? |
>    |---|:---:|:---:|:---:|
>    | Meubelzaak Mertens BV | klein | geen groep | Nee |
>    | Naaiatelier Ninove BV | klein | groep groot | Ja |
>    
>

**Grondslag**: [[commissaris]] §uitzondering-klein, WVV art. 3:72

> [!warning]- Toets verbondenheid voor je 'geen commissaris' adviseert aan een kleine vennootschap.
>
> _Vaak fout gedaan_: Aannemen dat een kleine dochter altijd vrijgesteld is van commissaris-benoeming.
>
> _Grondslag_: [[commissaris]] §verbondenheid

### 3. Pas de regel toe voor grote vennootschappen en PIE's

Grote vennootschappen en PIE's moeten een commissaris benoemen.

**Waarom?** Externe wettelijke controle is verplicht voor entiteiten met ruimere stakeholderkring.

**📥 Input**:
- Werknotitie stap 1 → **Groot of PIE** _(conclusie)_

**📤 Output**:
- Beslissingsnota → **Commissaris verplicht + bijzondere PIE-vereisten** _(document)_

**🛠️ Hoe**:

1. Groot en geen PIE → één commissaris (of college) benoemen door de algemene vergadering (AV) op voordracht van het bestuursorgaan, na advies van de ondernemingsraad indien aanwezig.
2. PIE → strengere regels: rotatieplicht (maximum-mandaatduur), beperkte non-audit-diensten, toezicht door auditcomité. Zie [[public-interest-entity]] §strengere-eisen en EU-Verordening 537/2014.
3. Termijn van benoeming: drie jaar, hernieuwbaar ([[commissaris]] §mandaatduur).
4. Benoeming registreren bij de griffie van de ondernemingsrechtbank en bij het [[ibr]] (commissaris is IBR-lid).


**Grondslag**: [[commissaris]] §benoeming, WVV art. 3:72 § 1, [[public-interest-entity]] §strengere-eisen

### 4. Formuleer het advies aan de cliënt

Stel een korte nota op met de conclusie, de grondslag en de praktische stappen voor benoeming of vrijstelling.

**Waarom?** De cliënt heeft een duidelijk antwoord nodig, met geargumenteerde verwijzing naar wetsartikelen.

**📥 Input**:
- Beslissingsnota stap 2 of 3 → **Conclusie + grondslag** _(document)_

**📤 Output**:
- Cliëntbrief → **Advies + uit te voeren stappen** _(document)_

**🛠️ Hoe**:

1. Schrijf één conclusiezin: "Een commissaris is wel/niet verplicht voor [cliënt]."
2. Voeg de wettelijke grondslag toe (WVV art. 3:72 + groep-context indien relevant).
3. Bij verplichting: lijst van stappen — agenderen op AV, kandidaat voordragen, benoemingsduur (3 jaar), publicatie in Belgisch Staatsblad, communicatie ondernemingsraad.
4. Bij vrijstelling: vermeld dat dit kan herzien worden bij wijziging grootteklasse of groep-context.


**Grondslag**: [[commissaris]] §benoemingsprocedure (praktijk-discipline)


## Voorbeelden





