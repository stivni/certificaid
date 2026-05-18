---
title: Kwalificeren of een onderneming boekhoudplichtig is en welk type boekhouding
  zij moet voeren
tags:
- competentie
- po-1-2
programmaonderdelen:
- '1.2'
status: voorgesteld
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/kwalificeren-boekhoudplichtige-onderneming.json
gegenereerd_op: '2026-05-18'
---
# Kwalificeren of een onderneming boekhoudplichtig is en welk type boekhouding zij moet voeren

**⚖️ 90% · 🤖 10%**

> De boekhoudplicht en de keuze tussen dubbele en vereenvoudigde boekhouding zijn strikt geregeld in WER Boek III en het uitvoerings-KB van 21 oktober 2018. Enkel het inschatten van de feitelijke omzet en de eventuele opportuniteit van vrijwillig dubbele boekhouding vragen praktijkoordeel.

## Aanbevolen werkwijze

### 1. Identificeer de juridische vorm en de aard van de activiteit

Bepaal of het om een rechtspersoon, een natuurlijke persoon-zelfstandige of een entiteit zonder rechtspersoonlijkheid gaat.

**Waarom?** Het toepassingsgebied van WER Boek III hangt af van de vorm — alleen 'ondernemingen' in de zin van WER art. I.1 vallen eronder.

**📥 Input**:
- Statuten of inschrijving in de Kruispuntbank van Ondernemingen (KBO) → **Juridische vorm + activiteitscode** _(document)_

**📤 Output**:
- Werknotitie → **Vorm-categorie (rechtspersoon-vennootschap / VZW / eenmanszaak / vrij beroep / maatschap)** _(conclusie)_

**🛠️ Hoe**:

1. Open het KBO-uittreksel van bv. Praktijk Persenaire of Meubelzaak Mertens BV.
2. Lees de juridische vorm — onderscheid:
   - vennootschap met rechtspersoonlijkheid (BV, NV, CV, ...);
   - VZW, IVZW, stichting;
   - natuurlijke persoon-zelfstandige of vrij beroep;
   - maatschap zonder rechtspersoonlijkheid.
3. Toets aan de ondernemingsdefinitie van [[boekhoudplichtige-onderneming]] §definitie. Conclusie: valt deze entiteit onder WER Boek III?


**Grondslag**: [[boekhoudplichtige-onderneming]] §definitie, WER art. I.1.1°

> [!warning]- Een maatschap zonder rechtspersoonlijkheid is wél een onderneming en is boekhoudplichtig.
>
> _Vaak fout gedaan_: Aannemen dat 'geen rechtspersoonlijkheid' gelijkstaat aan 'geen boekhoudplicht'.
>
> _Grondslag_: [[boekhoudplichtige-onderneming]] §maatschap

### 2. Beoordeel de drempels voor vereenvoudigde boekhouding

Toets de jaaromzet aan de WER-drempel die de keuze tussen dubbele en vereenvoudigde boekhouding bepaalt.

**Waarom?** Onder de wettelijke drempel mag een natuurlijke persoon of zeer kleine VOF een vereenvoudigde boekhouding voeren — geen dubbele boekhouding verplicht.

**📥 Input**:
- Resultaatcijfers vorig boekjaar of geprojecteerde omzet → **Omzet (excl. BTW)** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Werknotitie → **Verplichting tot dubbele OF vereenvoudigde boekhouding** _(conclusie)_

**🛠️ Hoe**:

1. Lees de actuele omzet-drempel uit [[vereenvoudigde-boekhouding]] §drempel (cijferzakboekje).
2. Vergelijk met de gerealiseerde omzet van het vorige boekjaar van Praktijk Persenaire.
3. Onder de drempel én natuurlijk persoon / kleine VOF? → vereenvoudigde boekhouding toegelaten.
4. Boven de drempel of rechtspersoon? → dubbele boekhouding verplicht ([[dubbel-boekhouden]] §verplichting).


> [!example]- Voorbeeld: Praktijk Persenaire (eenmanszaak vrij beroep, omzet vorig jaar € 280.000) en Meubelzaak Mertens BV (omzet € 4.500.000) —…
> Praktijk Persenaire (eenmanszaak vrij beroep, omzet vorig jaar € 280.000) en Meubelzaak Mertens BV (omzet € 4.500.000) — vergelijking.
>
> 1. **Toets drempel** 🧮
>
>    | Cliënt | Vorm | Omzet | Drempel WER | Regime |
>    |---|---|---:|---:|---|
>    | Praktijk Persenaire | eenmanszaak | € 280.000 | € 500.000 | Vereenvoudigde boekhouding toegelaten |
>    | Meubelzaak Mertens BV | rechtspersoon BV | € 4.500.000 | n.v.t. (rechtspersoon) | Dubbele boekhouding verplicht |
>    
>
> 2. **Conclusie** 💬
>
>    Rechtspersoon: drempel speelt niet — altijd dubbele boekhouding.
>    Eenmanszaak: drempel beslist.
>    
>

**Grondslag**: [[vereenvoudigde-boekhouding]] §drempel, [[dubbel-boekhouden]] §verplichting

> [!warning]- De drempel speelt enkel voor natuurlijke personen en kleine VOF — een BV moet altijd dubbele boekhouding voeren, ongeacht omzet.
>
> _Vaak fout gedaan_: Een BV met omzet onder € 500.000 toelaten tot vereenvoudigde boekhouding.
>
> _Grondslag_: [[vereenvoudigde-boekhouding]] §toepassingsgebied

### 3. Specificeer de inrichtings-eisen

Stel vast welke boeken en welk rekeningenstelsel de onderneming moet bijhouden.

**Waarom?** De wet schrijft niet alleen het type boekhouding voor, maar ook de instrumenten (centraal boek, dagboeken, MAR).

**📥 Input**:
- Conclusie stap 2 → **Regime (dubbel / vereenvoudigd)** _(conclusie)_

**📤 Output**:
- Inrichtingschecklist → **Lijst van vereiste boeken + rekeningenstelsel** _(document)_

**🛠️ Hoe**:

1. Bij dubbele boekhouding: stel het [[minimum-algemeen-rekeningenstelsel]] §opbouw op (zeven klassen 1-7, klasse 0 voor buiten balans), aangepast aan de bedrijfssector.
2. Bepaal de dagboeken: aankoopdagboek, verkoopdagboek, financieel dagboek, eventueel hulpdagboeken — zie [[regelmatige-boekhouding]] §inrichting.
3. Bij vereenvoudigde boekhouding: enkel drie afzonderlijke boeken (financieel, aankopen, verkopen) — geen MAR vereist.
4. Documenteer in het cliëntdossier welke boeken aangemaakt worden, met startdatum.


**Grondslag**: [[regelmatige-boekhouding]] §inrichting, [[minimum-algemeen-rekeningenstelsel]] §opbouw

### 4. Bevestig de bewaartermijn aan de cliënt

Communiceer dat alle boeken en verantwoordingsstukken zeven jaar bewaard moeten blijven.

**Waarom?** Niet-naleving van de bewaarplicht is strafbaar en hindert de onderbouwing bij fiscale of vennootschapsrechtelijke betwistingen.

**📥 Input**:
- Inrichtingschecklist stap 3 → **Lijst van boeken en stukken** _(document)_

**📤 Output**:
- Cliëntbrief → **Bewaarplicht-instructie + startdatum** _(document)_

**🛠️ Hoe**:

1. Vermeld in de cliëntbrief de termijn van zeven jaar uit [[bewaartermijn-boekhouding]] §termijn.
2. Geef aan vanaf welke datum de termijn loopt: 1 januari volgend op het afsluiten van het boekjaar.
3. Vermeld dat ook elektronische bewaring toegelaten is, mits leesbaar en onveranderlijk.


**Grondslag**: [[bewaartermijn-boekhouding]] §termijn, WER art. III.86


## Voorbeelden

> [!example]- Praktijk Persenaire is een eenmanszaak vrij beroep met omzet € 280.000 in 2024 (gefactureerde erelonen)
> **Conclusie**: Boekhoudplichtig onder WER Boek III. Omzet onder drempel + natuurlijke persoon → vereenvoudigde boekhouding toegelaten (drie boeken, geen MAR).
>
> **Grondslag**: [[boekhoudplichtige-onderneming]] §natuurlijke-personen; [[vereenvoudigde-boekhouding]] §drempel
>
> **Redenering**: WER-definitie omvat ook beoefenaars van een vrij beroep. Drempel-toets is gunstig. Cliënt moet wel jaarlijks een vereenvoudigde inventaris opmaken.

> [!example]- Meubelzaak Mertens BV is een BV met € 4.500.000 omzet en 12 werknemers
> **Conclusie**: Dubbele boekhouding verplicht — rechtspersoon. Inrichting met MAR, dagboeken (aankoop, verkoop, financieel) en eventueel hulpdagboeken voor de winkel.
>
> **Grondslag**: [[dubbel-boekhouden]] §verplichting; [[minimum-algemeen-rekeningenstelsel]] §opbouw
>
> **Redenering**: Voor rechtspersonen is dubbele boekhouding ongeacht omzet. Het MAR moet worden aangepast aan de detailhandel-sector (eigen subrubrieken voor voorraad winkelgoederen).


## Gebaseerd op concepten

[[boekhoudplichtige-onderneming]] · [[dubbel-boekhouden]] · [[vereenvoudigde-boekhouding]] · [[regelmatige-boekhouding]] · [[minimum-algemeen-rekeningenstelsel]] · [[bewaartermijn-boekhouding]] · [[wetboek-economisch-recht-boek-iii]]
## Voortkomend uit

- **Kenniselementen**: 1.2.III, 1.2.III.B, 1.2.III.C, 1.2.I.C
