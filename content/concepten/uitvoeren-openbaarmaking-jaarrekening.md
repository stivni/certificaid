---
title: Uitvoeren van de openbaarmaking van de jaarrekening bij de Nationale Bank
tags:
- concept
- competentie
- po-1-2
linked_anchors:
- 1.2.IV.F
- 1.2.IV
programmaonderdelen:
- '1.2'
confidence: inferred
node_type: competentie
status: voorgesteld
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/uitvoeren-openbaarmaking-jaarrekening.json
gegenereerd_op: '2026-05-18'
---
# Uitvoeren van de openbaarmaking van de jaarrekening bij de Nationale Bank 🤖


## Stappen

### 1. Stel het neerleggingsdossier samen

Verzamel alle documenten die op de neerlegging betrekking hebben.

**Waarom?** De wet vereist een coherent dossier; ontbrekende stukken leiden tot weigering van de neerlegging.

**📥 Input**:
- Goedgekeurde jaarrekening + bijhorende documenten → **Balans, RR, toelichting, eventueel sociale balans, jaarverslag, commissarisverslag** _(document)_

**📤 Output**:
- Neerleggingsdossier → **Bundel klaar voor NBB-Filing** _(document)_

**🛠️ Hoe**:

1. Open de door de AV goedgekeurde jaarrekening (datum AV vastleggen — startpunt termijn).
2. Stel de checklist op volgens [[openbaarmaking-jaarrekening]] §verplichte-bijlagen: balans, RR, toelichting, sociale balans (volledig/verkort), jaarverslag (groot), commissarisverslag (indien commissaris).
3. Voeg het bestuursorgaan-besluit toe waarin de jaarrekening is opgemaakt en de AV-notulen waarin ze is goedgekeurd.
4. Check dat alle documenten in het juiste schema-formaat zitten (volledig/verkort/micro — zie [[jaarrekening-schema]] §componenten).


**Grondslag**: [[openbaarmaking-jaarrekening]] §verplichte-bijlagen, WVV art. 3:10

### 2. Respecteer de wettelijke termijn

Bereken de uiterste datum van neerlegging (30 dagen na goedkeuring AV, max 7 maanden na balansdatum).

**Waarom?** Laattijdige neerlegging leidt tot retributie en mogelijke bestuurdersaansprakelijkheid.

**📥 Input**:
- Boekjaar-einde + AV-datum → **Twee data** _(datum)_

**📤 Output**:
- Termijn-werkblad → **Uiterste neerleggingsdatum** _(datum)_

**🛠️ Hoe**:

1. Lees de balansdatum (bv. 31/12/2024 voor Meubelzaak Mertens BV).
2. Bepaal de AV-datum binnen 6 maanden na balansdatum — [[openbaarmaking-jaarrekening]] §AV-termijn.
3. Bereken uiterste neerleggingsdatum: AV-datum + 30 dagen, met absoluut plafond op 7 maanden na balansdatum.
4. Zet deadline in cliëntagenda; vermeld termijn schriftelijk in cliëntbrief.


> [!example]- Voorbeeld: Meubelzaak Mertens BV, boekjaar afgesloten 31/12/2024, AV gehouden op 25/05/2025
> Meubelzaak Mertens BV, boekjaar afgesloten 31/12/2024, AV gehouden op 25/05/2025.
>
> 1. **Termijn berekenen** 🧮
>
>    | Element | Datum |
>    |---|---|
>    | Balansdatum | 31/12/2024 |
>    | Uiterste datum AV (6 maanden) | 30/06/2025 |
>    | Werkelijke AV | 25/05/2025 |
>    | AV + 30 dagen | 24/06/2025 |
>    | Plafond 7 maanden na balansdatum | 31/07/2025 |
>    | Uiterste neerleggingsdatum | 24/06/2025 |
>    
>

**Grondslag**: [[openbaarmaking-jaarrekening]] §termijn, WVV art. 3:10

> [!warning]- Tel altijd 30 dagen vanaf de AV-datum, niet vanaf het einde van het boekjaar.
>
> _Vaak fout gedaan_: De termijn berekenen op zes maanden na balansdatum, terwijl de AV-datum bepalend is.
>
> _Grondslag_: [[openbaarmaking-jaarrekening]] §termijn

### 3. Leg het dossier elektronisch neer bij de Balanscentrale van de NBB

Voer de neerlegging uit via NBB-Filing en bewaar het ontvangstbewijs.

**Waarom?** Elektronische neerlegging is verplicht; papierneerlegging wordt geweigerd.

**📥 Input**:
- Neerleggingsdossier + termijn-werkblad → **Documenten + deadline** _(document)_

**📤 Output**:
- Neerleggingsbewijs NBB → **Bevestiging + retributiebewijs** _(document)_

**🛠️ Hoe**:

1. Log in op NBB-Filing met de elektronische identiteit van de bestuurder of de mandataris (accountant ITAA-lid).
2. Selecteer het juiste schema (volledig/verkort/micro) — [[nationale-bank-belgie]] §balanscentrale.
3. Upload de XBRL- of PDF-bestanden volgens het NBB-formaat. Voer de aanvullende statistische gegevens in.
4. Betaal de retributie (afhankelijk van schema en eventuele laattijdigheid).
5. Bewaar het ontvangstbewijs in het cliëntdossier.


**Grondslag**: [[nationale-bank-belgie]] §balanscentrale, [[openbaarmaking-jaarrekening]] §filing-procedure

### 4. Volg neerleggingsvermeldingen op bij de griffie

Controleer of de jaarrekening-neerlegging correct gemeld is in het ondernemingsdossier van de griffie.

**Waarom?** De griffie houdt een paralleldossier waarin de neerlegging-datums opgenomen worden — controle op tijdigheid.

**📥 Input**:
- Neerleggingsbewijs stap 3 → **Bevestiging + datum** _(document)_

**📤 Output**:
- Bevestiging in ondernemingsdossier → **Vermelding zichtbaar in KBO / griffie** _(document)_

**🛠️ Hoe**:

1. Open in de KBO of via de portaalsite van [[griffies-ondernemingsrechtbank]] §ondernemingsdossier het dossier van de cliënt.
2. Controleer dat de neerlegging-vermelding is opgenomen (meestal binnen 5-10 werkdagen na neerlegging).
3. Bij ontbreken na 4 weken: contact NBB-Filing helpdesk.
4. Documenteer in cliëntdossier en sluit het neerleggingsdossier af.


**Grondslag**: [[griffies-ondernemingsrechtbank]] §ondernemingsdossier


