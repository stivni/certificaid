---
title: Proportionele integratie (registratiesysteem)
tags:
- concept
- cluster
- po-1-8
linked_anchors:
- 1.8.IV.C
- 1.8.IV
programmaonderdelen:
- '1.8'
confidence: inferred
node_type: cluster
status: seed
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/registratiesysteem-proportionele-integratie.json
gegenereerd_op: '2026-05-18'
---
# Proportionele integratie (registratiesysteem) 🤖

Bij proportionele integratie worden kosten en opbrengsten 'rubriek per rubriek, proportioneel met het aandeel' opgenomen. CBN 3/3 formuleert dit voor tijdelijke verenigingen; in analytische boekhouding wordt het analoog toegepast wanneer een gemeenschappelijke kost over meerdere centra of dragers pro-rata moet worden verdeeld.

> [!info] Behoort tot: [[rekeningenstelsel-analytisch]]


## Bouwstenen

### Pro-rata-verdeling per rubriek ⚖️

Elke kost-/opbrengstpost wordt individueel pro-rata verdeeld volgens een vooraf afgesproken percentage of sleutel. Vergt aparte 'verdeelboekingen'.

**Waarom?** Maakt aandeel per centrum/partner zichtbaar; vereiste bij meervoudige eigenaars of bij sterk gedeelde resources.



Yperse Werkplaats BV verdeelt de gezamenlijke energiekost weverij € 145.000/jaar proportioneel over de drie productlijnen volgens machine-uren: 40 % Tapijten, 35 % Stoffenrol, 25 % Garen. Verdeelboeking: Tapijten € 58.000, Stoffenrol € 50.750, Garen € 36.250.

_Grondslag: CBN 3/3_


## Berekening

### Inrichting proportionele integratie (pro-rata-verdeling per rubriek)

**Pro-rata-aandeel per ontvangend kostencentrum** 
```
aandeel_centrum = verzamel_saldo × (sleutel_eenheden_centrum / sleutel_eenheden_totaal)
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `verzamel_saldo` | Totaal te verdelen kost in verzamelrekening | EUR |
| `sleutel_eenheden_centrum` | Sleutelmeting voor het ontvangende centrum | uren / m² / FTE / % |
| `sleutel_eenheden_totaal` | Som sleutelmetingen alle ontvangende centra | uren / m² / FTE / % |

**Voorbeeld-invulling**: Yperse Werkplaats BV energiekost weverij € 145.000; machine-uren Tapijten = 2.000, Stoffenrol = 1.750, Garen = 1.250 (totaal 5.000 uren)

```
Tapijten = € 145.000 × (2.000 / 5.000) = € 58.000; Stoffenrol = € 145.000 × (1.750 / 5.000) = € 50.750; Garen = € 145.000 × (1.250 / 5.000) = € 36.250
```

_Resultaat in EUR_
*Stappenschema waarmee gezamenlijke kosten en opbrengsten per rubriek pro-rata over meerdere kostencentra of kostendragers verdeeld worden volgens vooraf vastgelegde sleutels — toepasbaar bij gedeelde infrastructuur, joint-venture-relaties of gemeenschappelijke overhead.*

### 1. Identificeer gedeelde kost-rubrieken en doelcentra

Lijst de kost- en opbrengstposten die gedeeld zijn over meerdere kostencentra/dragers (energiekost gemeenschappelijke productiehal, ICT-kosten, algemene directie, gezamenlijke marketingcampagne, joint-venture-omzet).

**🛠️ Hoe**:

Per rubriek: noteer ontvangende kostencentra en de objectieve sleutel (machine-uren, m² vloeroppervlakte, FTE, contractueel afgesproken percentage, verkoopvolume).

**Grondslag**: [[verdeelsleutel]]

### 2. Bepaal en documenteer de verdeelsleutel per rubriek

Voor elke gedeelde rubriek leg vast: type sleutel (volume, oppervlakte, omzet, contractueel percentage), de meet-eenheid en de periodiciteit van herijking (jaarlijks, kwartaal).

**🛠️ Hoe**:

Documenteer in een verdeel-charter per kostensoort. Bij joint-ventures of consortia: de sleutel komt uit het samenwerkingscontract. Bij interne shared services: meting via machine-uur-registratie of vloerplattegrond.

**Grondslag**: CBN 3/3 — proportionele integratie

### 3. Boek gedeelde kost initieel op verzamelrekening klasse 9

Bij ontvangst van een gedeelde kost-factuur: boek in klasse 6 (algemene boekhouding) zoals gewoonlijk, én in klasse 9 op een verzamelrekening 'gedeelde kost <rubriek>'. Geen onmiddellijke toewijzing aan eindkostencentra.

**🛠️ Hoe**:

Bv. energiekost weverij € 145.000/jaar → 612 Energie / 440 Leveranciers in klasse 6, én 9500 Verzamel Energie weverij / 9060 Reflectie Energie in klasse 9.

**Grondslag**: [[reflectie-rekening]]

### 4. Bereken pro-rata-bedragen + maak verdeelboeking

Periodiek (maand/kwartaal): pas de verdeelsleutel toe op het verzamel-saldo. Maak een verdeel-boeking die het verzamel-saldo nul-stelt en de pro-rata-bedragen op de eindkostencentra plaatst.

**🛠️ Hoe**:

Verdeel-boeking: 9XXX Eindkostencentrum A debet (= aandeel A) + 9YYY Eindkostencentrum B debet (= aandeel B) + ... / 9500 Verzamel <rubriek> credit (= totaal). Saldo verzamelrekening moet nul zijn na verdeling.

**Grondslag**: [[verdeelsleutel]] · [[verdeelboeking]]

### 5. Periodieke verificatie en herijking sleutels

Aan periodeafsluiting: controleer dat verzamelrekeningen nul-saldo hebben (alles verdeeld) en dat de sleutels nog actueel zijn (machine-uren verschoven? oppervlakte herorganiseerd?).

**🛠️ Hoe**:

Verschillen op verzamelrekeningen wijzen op vergeten of foute verdeelboekingen. Herijk sleutels jaarlijks of bij structuurwijziging; documenteer wijziging in verdeel-charter.

**Grondslag**: CBN 3/3 + [[registratiesysteem-waarderingsneutraal]]


> [!info]- Niet verwarren met [[registratiesysteem-eenvoudige-integratie]]
> Proportioneel: pro-rata-verdeling per rubriek. Eenvoudig: direct aan één centrum toegewezen.
>
> _Trigger_: Bij gedeelde infrastructuur of joint-venture-vergelijkbare context.


## Bronnen

[^1]: `CBN-0003-03-advies-inzake-de-boekhoudkundige-verwerking-van-verrichtingen-van-tijdelijk__sec_de-proportionele-integratie-van-kosten-en-opbrengsten`
