---
title: Aankoopcyclus — interne controle
tags:
- concept
- procedure
- po-1-7
linked_anchors:
- 1.7.IX.A
- 1.7.IX
programmaonderdelen:
- '1.7'
confidence: inferred
node_type: procedure
status: seed
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/aankoopcyclus-ic.json
gegenereerd_op: '2026-05-18'
---
# Aankoopcyclus — interne controle 🤖

> [!summary] Korte inhoud
> Geen wettelijke verplichting voor specifieke aankoopcyclus-controles.

> [!info] Behoort tot: [[interne-controle]]

Geen wettelijke verplichting voor specifieke aankoopcyclus-controles. Wel: btw-aftrek vereist correcte facturen (WBTW); boekhoudkundige verplichtingen vereisen documentatie (KB 21.10.2018).


## Stappen

### 1. Behoeftebepaling + bestelaanvraag

De inkoper of behoeftesteller identificeert wat nodig is en doet een bestelaanvraag.

**Waarom?** Zonder formele aanvraag riskeer je dubbele aankopen, onnodige aankopen, niet-geautoriseerde aankopen.

**🛠️ Hoe**:

1. Aanvraag via standaardformulier of ERP-module.
2. Specificeer leverancier, hoeveelheid, prijs, kostencentrum.
3. Verstuur naar autoriserende verantwoordelijke.

**Grondslag**: Audit-cyclusanalyse-doctrine

### 2. Autorisatie

Goedkeuring door bevoegde persoon volgens delegatie-procuratie (typisch op basis van bedrag).

**Waarom?** Onbevoegd aankopen = ongeautoriseerde uitgaven, mogelijk fraude (kickbacks bij bevriende leveranciers).

**🛠️ Hoe**:

1. Inkoper Tom Lefèvre tekent < € 5.000.
2. CFO David tekent < € 25.000.
3. Algemeen Directeur Pieter Vermeulen tekent ≥ € 25.000.
4. Boven drempel: dubbele handtekening + voorafgaande mededeling aan RvB.

> [!example]- Voorbeeld: Bij Yperse Werkplaats BV bestelt productie € 35.000 grondstoffen
> Bij Yperse Werkplaats BV bestelt productie € 35.000 grondstoffen.
>
> 1. **Procuratie-drempel-overschrijding** 💬
>
>    € 35.000 > € 25.000 → dubbele handtekening verplicht: CFO David + Algemeen Directeur Pieter Vermeulen + voorafgaande melding RvB.
>

**Grondslag**: Delegatie-procuratie-doctrine

### 3. Bestelling + ontvangst

Bestelling verzenden naar leverancier; bij ontvangst goederen tellen + controleren tegen bestelbon.

**Waarom?** Zonder ontvangstcontrole riskeer je 'paying for nothing' — facturen betalen voor goederen die nooit zijn geleverd.

**🛠️ Hoe**:

1. Bestelbon in ERP creëert verwacht-record.
2. Magazijnier Bart controleert leveringsbon tegen bestelbon (aantal, kwaliteit).
3. Tekent voor ontvangst; ERP-bestelbon wordt 'geleverd' gestempeld.
4. Bij afwijking: meld direct aan inkoper + boekhouding.

**Grondslag**: Cyclus-three-way-match-principe

### 4. Factuurcontrole + boeking

Boekhouder controleert factuur tegen bestelbon én leveringsbon ('three-way match') vóór boeking.

**Waarom?** Three-way match detecteert facturen voor niet-bestelde of niet-geleverde goederen, prijsafwijkingen, BTW-fouten.

**🛠️ Hoe**:

1. Boekhouder Cindy haalt bestelbon en leveringsbon op.
2. Vergelijkt: aantal, prijs, totaal, BTW.
3. Bij match: boek in ERP onder juiste kostencentrum.
4. Bij afwijking: terug naar inkoper voor opheldering.

**Grondslag**: Three-way-match-doctrine

### 5. Betaling

Betaling door iemand anders dan de boeker, opnieuw met handtekening volgens drempels.

**Waarom?** Wie boekt + betaalt kan fictieve facturen aanmaken en uitbetalen. Scheiding is essentieel.

**🛠️ Hoe**:

1. CFO David selecteert facturen voor betaling.
2. Klassieke uitvoering: digitale ondertekening in bankplatform vóór upload.
3. Bedragen boven € 25.000: dubbele digitale ondertekening.
4. Periodieke review bankuittreksels door zaakvoerder Pieter Vermeulen.

**Grondslag**: Functiescheiding-doctrine


## Valkuilen

> [!warning]- Spoedaankopen omzeilen vaak de hele procedure
> ⚠️ Spoedaankopen omzeilen vaak de hele procedure. Definieer expliciet uitzonderingsprotocol (welke bedragen, welke autorisatie achteraf, welke termijn voor inhaalcontrole). 🤖


> [!warning]- 'Persoonlijke aankopen via bedrijfsrekening' is fraude (verduistering)
> ⚠️ 'Persoonlijke aankopen via bedrijfsrekening' is fraude (verduistering). Klassieke detectie: ongebruikelijke leveranciers, ongewone factuuradressen, recurrente kleine bedragen. 🤖



## Zie ook

- **Vereist kennis van**: [[functiescheiding]]

