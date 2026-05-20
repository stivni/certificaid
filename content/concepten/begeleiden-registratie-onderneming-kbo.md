---
title: Begeleiden van de registratie van een nieuwe onderneming (KBO, btw, UBO)
tags:
- concept
- competentie
- po-3-0
linked_anchors:
- 3.0.taak.1
- 3.0.I
programmaonderdelen:
- '3.0'
confidence: inferred
node_type: competentie
status: seed
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/begeleiden-registratie-onderneming-kbo.json
gegenereerd_op: '2026-05-20'
---
# Begeleiden van de registratie van een nieuwe onderneming (KBO, btw, UBO) 🤖

Operationele competentie: na de notariële akte de praktische registratie-stappen begeleiden waardoor de vennootschap volwaardig operationeel wordt — inschrijving in de Kruispuntbank van Ondernemingen (KBO), btw-identificatie, UBO-register, sociaal verzekeringsfonds en de bedrijfsvergunningen. Doel: vermijden dat de vennootschap factureert of activiteit ontplooit zonder de wettelijke registraties.


## In de praktijk

- De notaris regelt KBO-inschrijving automatisch — accountant volgt op en doet de rest (btw, UBO, sociaal fonds).
- Plan UBO-registratie binnen 30 dagen na KBO-inschrijving — dit wordt vaak vergeten en levert sancties.
- Voor sector-vergunningen: maak een checklist per sector in cliëntdossier zodat geen vergunning vergeten wordt.

## Stappen

### 1. Verkrijgen ondernemingsnummer + inschrijving KBO

Na neerlegging van de oprichtingsakte bij de griffie van de ondernemingsrechtbank krijgt de vennootschap automatisch een ondernemingsnummer en wordt ze ingeschreven in de Kruispuntbank van Ondernemingen.

**Waarom?** Het ondernemingsnummer is de unieke identificator voor alle administratieve relaties (btw, sociale zekerheid, RSZ, registers, fiscale aangiften). Zonder dit nummer kan geen factuur, geen sociale aansluiting, geen btw-aangifte.

**📥 Input**:
- Authentieke oprichtingsakte → **Notarieel akte-document** _(wettelijk-document)_

**📤 Output**:
- KBO-inschrijving + ondernemingsnummer → **10-cijferig nummer** _(wettelijk-document)_

**🛠️ Hoe**:

1. De notaris legt de akte neer bij de griffie van de ondernemingsrechtbank van de zetel.
2. Griffie genereert het ondernemingsnummer en bezorgt dat aan de notaris.
3. Notaris geeft het nummer door aan de oprichters.
4. Controleer in de KBO-publieke databank dat de vennootschap correct is ingeschreven (naam, zetel, doel, bestuurders).
5. Bij niet-handelsbedrijvigheid (bv. landbouw): aanvullende inschrijving bij KBO via ondernemingsloket vaak nodig.

**Grondslag**: WER art. III.18-III.49

### 2. Activeren btw-identificatie

De vennootschap activeert haar btw-identificatie via een 604A-formulier bij de FOD Financiën — eenmaal het ondernemingsnummer toegekend.

**Waarom?** Een vennootschap kan pas geldig factureren met btw (en btw aftrekken) na de identificatie. Vóór activering is btw-aftrek op investeringskosten beperkt of onmogelijk.

**📥 Input**:
- Ondernemingsnummer → **Toegekend** _(wettelijk-document)_
- Beschrijving bedrijvigheid + verwachte omzet → **Voor btw-regime-keuze** _(vrije-tekst)_

**📤 Output**:
- Btw-identificatie (BE0xxx.xxx.xxx) → **Geactiveerd btw-nummer** _(wettelijk-document)_

**🛠️ Hoe**:

1. Vul 604A-formulier in (via MyMinfin of papier) met identificatie + bedrijvigheidsbeschrijving + NACE-code(s).
2. Bepaal btw-regime:
   - Vrijgesteld door kleine onderneming-regeling (omzetdrempel € 25.000) — niet meestal kiesbaar bij nieuwe vennootschap.
   - Forfaitair regime (bepaalde sectoren) — uitzondering.
   - Normaal regime — meest gangbaar.
3. Geef startdatum bedrijvigheid op.
4. Wacht op btw-nummer-bevestiging (typisch 1-2 weken).
5. Eerste factuur kan pas na ontvangst btw-nummer — kruis-link met [[boeken-oprichtings-en-kapitaalverhogingskosten]] voor de boeking van kosten vóór btw-activering.

**Grondslag**: Btw-wetboek art. 50

### 3. Aansluiting sociaal verzekeringsfonds + RSZ

Schrijf de vennootschap in bij een sociaal verzekeringsfonds (voor zelfstandige bedrijfsleider) en — indien personeel — registreer als werkgever bij de RSZ.

**Waarom?** De bestuurder/zaakvoerder is sociaal verzekerd als zelfstandige; zonder aansluiting riskeert hij sancties en geen ziekteverzekering. Personeel zonder DIMONA = zwartwerk.

**📥 Input**:
- Identiteit bestuurder + ingangsdatum → **Persoonlijke gegevens** _(wettelijk-document)_

**📤 Output**:
- Sociaal-verzekeringsfonds-aansluiting + eventueel RSZ-werkgeversnummer → **Bevestigingsdocumenten** _(wettelijk-document)_

**🛠️ Hoe**:

1. Kies een sociaal verzekeringsfonds (Acerta, Liantis, Xerius, ...) — vergelijking is mogelijk maar verschillen klein.
2. Bestuurder vult aansluitingsformulier in — voorlopige bijdrage gebaseerd op verwacht inkomen jaar 1.
3. Aansluiting moet binnen 90 dagen vanaf start bedrijvigheid; bij overschrijding administratieve boete.
4. Bij personeel: registreer als werkgever bij RSZ + sluit aan bij een sociaal secretariaat voor loonadministratie + start DIMONA per werknemer.
5. Verwijs cliënt naar pensioenfonds en hospitalisatie-verzekering voor onafhankelijk pakket.

**Grondslag**: KB nr. 38 art. 9 (zelfstandigen); RSZ-Wet art. 9

### 4. Registratie in het UBO-register

De vennootschap registreert haar uiteindelijke begunstigden (Ultimate Beneficial Owners) in het UBO-register, beheerd door de FOD Financiën — binnen 1 maand na inschrijving in de KBO.

**Waarom?** UBO-registratie is dwingend voor alle Belgische vennootschappen en koppelt persoonlijke identificatie van de begunstigde aan de juridische entiteit — anti-witwasmaatregel.

**📥 Input**:
- Identiteitsgegevens UBO('s) → **Natuurlijke personen met ≥ 25% controle of feitelijke leiding** _(wettelijk-document)_

**📤 Output**:
- UBO-registratie → **Online bevestiging** _(wettelijk-document)_

**🛠️ Hoe**:

1. Identificeer alle UBO's — natuurlijke persoon die direct of indirect ≥ 25% van aandelen/stemrechten bezit, of feitelijke leiding heeft.
2. Bij solo-BV: oprichter zelf is meestal UBO.
3. Bij grotere structuren: doorprik holdings tot aan natuurlijke persoon.
4. Registreer via MyMinfin → 'UBO' → voor elke vennootschap waarvoor je gemandateerd bent.
5. Lever motivatie en bewijsstukken: aandelenregister, aandeelhoudersovereenkomst, statuten.
6. Jaarlijkse herbevestiging verplicht (zelfs bij geen wijziging).
7. Bij wijziging UBO: update binnen 1 maand.

**Grondslag**: KB van 30/07/2018 m.b.t. de werkingsmodaliteiten van het UBO-register; Antiwitwaswet 18/09/2017

> [!warning]- UBO-registratie is geen formaliteit — niet-registreren of laat-registreren wordt streng beboet (€ 250 tot € 50.000).
>
> _Vaak fout gedaan_: UBO-registratie vergeten of uitstellen omdat 'het wel zal volgen'.

### 5. Aanvullende sector-specifieke vergunningen

Identificeer en vraag aan: bedrijfsvergunningen die de sector vereist (FAVV, FOD Volksgezondheid, vergunning klasse 2-3 milieu, ...) — zonder mag de activiteit niet starten.

**Waarom?** Activiteit zonder vereiste vergunning is illegaal — strafbaar én civielrechtelijk risico (contracten kunnen nietig zijn). De accountant signaleert deze sector-specifieke vereisten als adviseur.

**📥 Input**:
- Sectorinformatie cliënt → **NACE-code, type activiteit** _(vrije-tekst)_

**📤 Output**:
- Lijst aan te vragen vergunningen + status → **Per vergunning: verantwoordelijke + deadline** _(tabel)_

**🛠️ Hoe**:

1. Bevraag de NACE-code voor sector-typische vergunningen (bv. voeding → FAVV-erkenning; horeca → SABAM-billijke vergoeding, drankvergunning; bouw → registratie bij FOD Mobiliteit voor erkende aannemers).
2. Voor milieu-gevoelige activiteiten: milieuvergunning bij Vlaamse Omgevingsvergunning of equivalent in Brussel/Wallonië.
3. Voor gereglementeerde beroepen: erkenning bij beroepsorde (architecten, advocaten, ITAA, ...).
4. Stel een tijdspad: welke vergunning is randvoorwaarde voor opstart, welke kan parallel?
5. Adviseer cliënt: niet starten met operationele activiteit voordat de essentiële vergunningen rond zijn.

**Grondslag**: Sectorwetgeving (variabel)


## Voorbeelden



