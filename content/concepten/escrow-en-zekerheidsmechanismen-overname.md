---
title: Escrow en zekerheidsmechanismen bij overname
tags:
- concept
- cluster
- po-3-0
linked_anchors:
- 3.0.V
- 3.0.V.A
- 3.0.V.E
- 3.0.V.F
programmaonderdelen:
- '3.0'
confidence: inferred
node_type: cluster
status: seed
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/escrow-en-zekerheidsmechanismen-overname.json
gegenereerd_op: '2026-05-21'
---
# Escrow en zekerheidsmechanismen bij overname 🔗

Een geldige R&W-vrijwaring is theoretisch — pas wanneer de koper effectief geld kan recupereren wordt ze praktisch waardevol. Zekerheidsmechanismen zorgen dat een deel van de prijs of een gelijkwaardig bedrag beschikbaar blijft om eventuele claims te dekken. De accountant beoordeelt de boekhoudkundige verwerking en de fiscale impact van deze mechanismen.

> [!summary] Korte inhoud
> Zekerheidsmechanismen bij overname zijn contractuele constructies die garanderen dat de verkoper financieel kan instaan voor vrijwaringsclaims na closing, door een deel van de prijs te blokkeren op een derdenrekening, te koppelen aan een bankgarantie, uit te stellen in tijd, of o….

> [!info] Behoort tot: [[overnameovereenkomst]]

Zekerheidsmechanismen bij overname zijn contractuele constructies die garanderen dat de verkoper financieel kan instaan voor vrijwaringsclaims na closing, door een deel van de prijs te blokkeren op een derdenrekening, te koppelen aan een bankgarantie, uit te stellen in tijd, of om te zetten in een verkoperkrediet.



## Bouwstenen

### Escrow ⚖️

Een afzonderlijke geblokkeerde rekening waarop een deel van de prijs gedurende een afgesproken periode wordt geparkeerd. De bank houdt de gelden vrij volgens een escrow-overeenkomst die de vrijgave-procedure detailleert.

**Waarom?** Geeft koper een directe vorderingsgrond zonder de financiële situatie van verkoper te moeten beoordelen.


**In de praktijk**: Typisch 10–20 % van de prijs gedurende 12–24 maanden, met geleidelijke vrijgave op vaste vrijgavedatums.


_Grondslag: IBA-MA-Belgium-2022-EN §5.2.4 Escrow account_

### Bankgarantie ⚖️

De verkoper ontvangt de volledige prijs op closing maar zorgt via zijn bank voor een garantie aan de koper voor eventuele toekomstige vrijwaringsclaims.

**Waarom?** Verkoper heeft cash beschikbaar; koper blijft beschermd via een betalingsverplichting van de bank.


**In de praktijk**: Kan 'on first demand' zijn (eenzijdige opvraagbaarheid) of conditioneel (na voorlegging documenten). Bank vraagt vaak van verkoper een tegengarantie of geblokkeerde rekening.


_Grondslag: IBA-MA-Belgium-2022-EN §5.2.4 Escrow account_

### Deferred payment ⚖️

Een deel van de prijs wordt later betaald. De koper houdt het bedrag in tot een afgesproken datum en kan eventuele vrijwaringsclaims rechtstreeks verrekenen.

**Waarom?** Geeft koper een directe set-off-mogelijkheid en helpt bij financiering wanneer koper niet de volledige prijs cash kan betalen.


**In de praktijk**: Verkoper kan op zijn beurt een bankgarantie eisen voor het uitgesteld bedrag — anders draagt hij koperkredietrisico.


_Grondslag: IBA-MA-Belgium-2022-EN §5.2.4 Deferred payment_

### Vendor loan ⚖️

De verkoper schiet een deel van de prijs voor als achtergestelde lening aan de koper of de doelvennootschap.

**Waarom?** Werkt als financieringsmechanisme én als zekerheid: de uitstaande lening kan worden verrekend met vrijwaringsclaims.


**In de praktijk**: Typisch achtergesteld aan bankschulden van de koper; rente lager dan marktrente om het 'tweede tranche van de prijs'-karakter te onderstrepen.


_Grondslag: IBA-MA-Belgium-2022-EN §5.2.4 Deferred payment_

### Pand op vorderingen ⚖️

De verkoper ontvangt de volle prijs maar verleent koper een pand op de vorderingen die koper zou hebben tegen verkoper uit hoofde van vrijwaringen.

**Waarom?** Alternatief voor escrow met sterker zakelijk effect onder Belgisch recht.


**In de praktijk**: Minder courant maar relevant wanneer verkoper een kleinere vennootschap is met beperkte solvabiliteit.


_Grondslag: IBA-MA-Belgium-2022-EN §5.2.4 Escrow account_


## In de praktijk

- De accountant let op de boekhoudkundige verwerking: een escrow blijft activa van de verkoper tot vrijgave (vordering op de bank), terwijl een deferred payment een schuld bij de koper is.
- Fiscaal: meerwaarden op aandelen worden gerealiseerd op closing, ongeacht escrow- of earn-out-uitkomst — dit kan tot cash-flow-misalignment leiden voor de verkoper-vennootschap.

## Zie ook

- **Vereist kennis van**: [[indemnification-overname]]

> [!todo] Voorbeeld ontbreekt voor dit concept
> Een latere ENRICH-pass voegt een synthese-voorbeeld toe.

